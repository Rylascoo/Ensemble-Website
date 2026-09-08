#!/usr/bin/env python3
"""Generate the document index from D-R1 first-line headers only."""

import argparse
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = "docs/INDEX.md"
STATUSES = ("ACTIVE LAW", "SUPERSEDED", "HISTORICAL EVIDENCE", "UNCLASSIFIED")
HEADER = re.compile(rb"<!-- D-R1-STATUS: (.+) -->")
MARKER = re.compile(rb"<!--\s*D-R1-STATUS\b")


def markdown_paths(root):
    """Include the entire Markdown tree, including new files, excluding Git metadata."""
    paths = []
    for directory, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d != ".git")
        for name in files:
            if name.endswith(".md"):
                paths.append((Path(directory) / name).relative_to(root).as_posix())
    return sorted(paths)


def read_status(root, path):
    data = (root / path).read_bytes()
    count = len(MARKER.findall(data))
    if count != 1:
        raise ValueError(f"{path}: expected one D-R1 header, found {count}")
    lines = data.splitlines()
    match = HEADER.fullmatch(lines[0]) if lines else None
    if not match:
        raise ValueError(f"{path}: canonical D-R1 header must be the first line")
    status = match.group(1).decode("utf-8")
    if status not in STATUSES:
        raise ValueError(f"{path}: invalid D-R1 status {status!r}")
    return status


def document_paths(root):
    """Preserve repo-wide Markdown collection; also collect text under docs/."""
    return sorted(markdown_paths(root) + [
        path.relative_to(root).as_posix()
        for path in (root / "docs").rglob("*.txt") if path.is_file()
    ])


def collect_statuses(root):
    return {path: read_status(root, path) for path in document_paths(root)}


def render_index(statuses):
    """Account for INDEX on the first run without changing subsequent output."""
    statuses = dict(statuses)
    if INDEX in statuses and statuses[INDEX] != "ACTIVE LAW":
        raise ValueError(f"{INDEX}: generated index must be ACTIVE LAW")
    statuses[INDEX] = "ACTIVE LAW"
    lines = [
        "<!-- D-R1-STATUS: ACTIVE LAW -->", "", "# Document index", "",
        "Generated file; do not hand-maintain.", "",
        "Generation command: `python3 tools/generate_docs_index.py`", "",
        f"Total Markdown documents: {len(statuses)}", "",
        "Groups reflect only the first-line D-R1 machine header, never legacy body `Status:` text.",
        "UNCLASSIFIED records remain visible reconciliation debt; no authority is inferred here.", "",
    ]
    for status in STATUSES:
        paths = sorted(path for path, value in statuses.items() if value == status)
        lines.extend([f"## {status} ({len(paths)})", ""])
        lines.extend(f"- `{path}`" for path in paths)
        lines.append("")
    return "\n".join(lines).encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check byte-for-byte idempotence without writing")
    args = parser.parse_args()
    try:
        expected = render_index(collect_statuses(ROOT))
        target = ROOT / INDEX
        if args.check:
            if not target.is_file() or target.read_bytes() != expected:
                raise ValueError(f"{INDEX}: missing or stale; run python3 tools/generate_docs_index.py")
            print(f"PASS: {INDEX} is byte-for-byte up to date")
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or target.read_bytes() != expected:
                target.write_bytes(expected)
            print(f"Generated {INDEX}")
        return 0
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
