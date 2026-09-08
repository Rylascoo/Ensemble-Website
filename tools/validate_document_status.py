#!/usr/bin/env python3
"""Validate document structure, not design correctness or creative authority."""

import re
import subprocess
import sys

sys.dont_write_bytecode = True
from generate_docs_index import HEADER, INDEX, MARKER, ROOT, document_paths, read_status, render_index


def validate_documents():
    failures = []
    for path in document_paths(ROOT):
        try:
            if path.endswith('.txt'):
                lines = (ROOT / path).read_bytes().splitlines()
                if any(MARKER.search(line) for line in lines) and not HEADER.fullmatch(lines[0]):
                    raise ValueError(f"{path}: canonical D-R1 header must be the first line")
            read_status(ROOT, path)
        except (OSError, ValueError) as error:
            failures.append(path)
            print(f"FAIL: {error}")
    print(f"A: {sum(path.endswith('.txt') for path in failures)} .txt marker failures; {len(failures)} total document failures")
    return not failures


def validate_index():
    statuses = {}
    invalid = 0
    for path in document_paths(ROOT):
        try:
            statuses[path] = read_status(ROOT, path)
        except (OSError, ValueError):
            invalid += 1
    # Always compare bytes, even when A reports invalid headers. Invalid
    # documents have no authoritative group; never silently classify them.
    matches = (ROOT / INDEX).read_bytes() == render_index(statuses)
    if not matches:
        print(f"INDEX: FAIL: {INDEX}: differs from the canonical corpus index; regenerate it")
    if invalid:
        print(f"INDEX: FAIL: {invalid} documents have invalid headers; full corpus index cannot be verified "
              f"(valid-document byte comparison: {'PASS' if matches else 'FAIL'})")
    if matches and not invalid:
        print(f"INDEX: PASS: {len(statuses)} documents; byte-exact index valid")
    return matches and not invalid


def validate_artifact_coverage():
    evidence = ROOT / 'docs' / 'evidence'
    sources = ROOT / 'tools'
    workflows = ROOT / '.github' / 'workflows'
    for directory in (evidence, sources, workflows):
        if not directory.is_dir():
            raise ValueError(f"missing directory: {directory}")
    reference_files = [path for path in sources.rglob('*') if path.is_file()]
    reference_files += [path for path in workflows.rglob('*')
                        if path.is_file() and path.suffix in ('.yml', '.yaml')]
    references = b'\n'.join(path.read_bytes() for path in reference_files)
    groups = {}
    for path in evidence.rglob('*'):
        if path.is_file() and path.suffix in ('.svg', '.json'):
            directory = path.parent.relative_to(ROOT).as_posix()
            groups[directory] = groups.get(directory, 0) + 1
    uncovered = {}
    for directory, count in sorted(groups.items()):
        pattern = rb'(?<![\w/.-])' + re.escape(directory.encode()) + rb'(?![\w.-])'
        covered = re.search(pattern, references) is not None
        print(f"{'COVERED' if covered else 'UNCOVERED'}: {directory}/ ({count} files)")
        if not covered:
            uncovered[directory] = count
    print(f"B: {'FAIL' if uncovered else 'PASS'}: {len(uncovered)} uncovered directories / {sum(uncovered.values())} files")
    return not uncovered


def validate_currency():
    def git(*args):
        return subprocess.run(['git', *args], cwd=ROOT, check=True,
                              capture_output=True, text=True, encoding='utf-8').stdout.strip()

    if git('rev-parse', '--is-shallow-repository') != 'false':
        raise ValueError('currency requires complete Git history (fetch-depth: 0)')
    if not (ROOT / 'CURRENT_STATE.md').is_file():
        raise ValueError('CURRENT_STATE.md: missing')
    last = git('log', '-1', '--format=%H', 'HEAD', '--', 'CURRENT_STATE.md')
    if not last:
        raise ValueError('CURRENT_STATE.md: no modification commit found')
    distance = int(git('rev-list', '--count', f'{last}..HEAD'))
    passed = distance <= 3
    print(f"C: {'PASS' if passed else 'FAIL'}: CURRENT_STATE.md currency distance {distance} (maximum 3)")
    subjects = git('log', '--format=%s', f'{last}..HEAD')
    if subjects:
        print(subjects)
    return passed


def main():
    results = []
    for label, check in (('A', validate_documents), ('INDEX', validate_index), ('B', validate_artifact_coverage), ('C', validate_currency)):
        try:
            results.append(check())
        except (OSError, ValueError, subprocess.CalledProcessError) as error:
            print(f"{label}: FAIL: {error}", file=sys.stderr)
            results.append(False)
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
