#!/usr/bin/env python3
"""Validate only the Q-ADMIN-05 frozen authority graph; never execute transfer."""

import argparse
from collections import Counter, defaultdict
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ORACLE = ROOT / 'docs/evidence/Q_ADMIN_05_RECURSIVE_AUTHORITY_CLOSURE_2026_09_20.json'
SELECTED = [203, 226, 227, 228, 233, *range(235, 254), 255, *range(262, 271)]
SEALED = {'NORMATIVE', 'SUPPORTING_METHOD_SEALED', 'EVIDENCE_SEALED'}
DISPOSITIONS = {'HISTORICAL_ONLY', 'EVIDENCE_ONLY', 'NON_AUTHORITATIVE_REFERENCE',
                'WEBSITE_ONLY_AUTHORITY', 'CROSS_SURFACE_RYLADMIN_AUTHORITY',
                'DRIVE_MASTER_REFERENCE_ONLY', 'EXCLUDED_FROM_TRANSFER_WITH_REASON'}
REFERENCE = re.compile(
    r'(?<![A-Za-z0-9_-])(?:docs|prototypes|tools|assets|site|intelligence|updates)/'
    r'[A-Za-z0-9_./-]+\.(?:md|json|html|mjs|py|png|txt|svg)'
    r'|(?<![A-Za-z0-9_/])(?:[A-Z][A-Z0-9_]+\.(?:json|md)'
    r'|(?:AGENTS|CURRENT_STATE)\.md|PKT-[A-Z0-9-]+)')
NAMED = {
    'Selected MAT F1': r'\bMAT(?:-01)?(?: \*\*)? F1\b',
    'Selected STA F2': r'\bSTA(?:-01)?(?: \*\*)? F2\b',
    'Selected TYP F1': r'\bTYP(?:-02)?(?: \*\*)? F1\b',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def scoped_lines(key, text):
    """Keep original line numbers even for the bounded ledger/iconography audit."""
    lines = text.splitlines()
    if key.endswith('DESIGN_LEDGER.md'):
        active = False
        result = []
        for line in lines:
            match = re.match(r'## L-(\d+)\b', line)
            if match:
                active = int(match[1]) in SELECTED
            result.append(line if active else '')
        return result
    if key.endswith('KYMAEAN_VISUAL_SYSTEM_GRAMMAR_PROPOSAL_01.md'):
        active = False
        result = []
        for line in lines:
            if line.startswith('## 14.'):
                active = True
            elif line.startswith('## 15.'):
                active = False
            result.append(line if active else '')
        return result
    if key == 'W:docs/DESIGN_CONTINUITY.md':
        end = next(i for i, line in enumerate(lines) if line.startswith('## 24.'))
        return lines[:end]
    return lines


def references(key, text):
    lines = scoped_lines(key, text)
    found = defaultdict(set)
    for number, line in enumerate(lines, 1):
        for match in REFERENCE.finditer(line):
            found[match[0]].add(number)
        for match in re.finditer(r'(?<![A-Za-z0-9_-])1[A-Za-z0-9_-]{24,}(?![A-Za-z0-9_-])', line):
            if not re.fullmatch('[0-9a-f]+', match[0]):
                found['DRIVE:' + match[0]].add(number)
        for match in re.finditer(r'\bL-\d{2,3}\b', line):
            found[match[0]].add(number)
        for title, pattern in NAMED.items():
            if re.search(pattern, line):
                found[title].add(number)
    try:
        doc = json.loads(text)
    except ValueError:
        doc = {}
    for field in ('source_authority', 'source_lineage'):
        values = doc.get(field, []) if isinstance(doc, dict) else []
        if isinstance(values, str):
            values = [values]
        for value in values:
            if isinstance(value, str) and not REFERENCE.search(value):
                escaped = [json.dumps(value, ensure_ascii=ascii_)[1:-1] for ascii_ in (True, False)]
                locations = [i for i, line in enumerate(lines, 1) if any(v in line for v in escaped)]
                require(locations, f'Cannot locate named authority: {key}: {value}')
                found[value].update(locations)
    return {token: sorted(numbers) for token, numbers in sorted(found.items())}


def graph_checks(data, contents):
    nodes, edges, bundles = data['nodes'], data['edges'], data['bundles']
    by_source = defaultdict(dict)
    for edge in edges:
        source, token = edge['source'], edge['reference']
        require(source in nodes, f'Unknown edge source: {source}')
        require(token not in by_source[source], f'Duplicate edge: {source}: {token}')
        require(edge['classification'] in SEALED | DISPOSITIONS, f'Unresolved classification: {token}')
        require(edge['reason'].strip(), f'Missing disposition reason: {token}')
        if edge['classification'] in SEALED:
            require(edge['target'] in nodes, f'Missing sealed dependency: {token}')
        by_source[source][token] = edge
    for key, text in contents.items():
        discovered = references(key, text)
        require(set(discovered) == set(by_source[key]),
                f'Unclassified/stale references in {key}: {set(discovered) ^ set(by_source[key])}')
        for token, locations in discovered.items():
            require(locations == by_source[key][token]['lines'], f'Source locator drift: {key}: {token}')
    require(set(bundles) == {*(f'A{i:02}' for i in range(1, 15)), *(f'C{i:02}' for i in range(1, 5)), *(f'D{i:02}' for i in range(1, 5))}, '22-bundle census drift')
    require(Counter(b['form'] for b in bundles.values()) == Counter(data['expected_forms']), 'Transfer-form drift')
    require(Counter(data['expected_forms']) == Counter({'WHOLE_DOCUMENT': 5, 'SELECTED_SECTIONS': 2,
            'NORMALIZED_ACTIVE_CONTRACT': 8, 'PROVENANCE_POINTER': 4,
            'EVIDENCE_REFERENCE_ONLY': 2, 'DO_NOT_TRANSFER': 1}), 'Frozen form-count contract changed')
    seeds = set(data['source_identities'])
    roots = {key for b in bundles.values() for key in b['roots']}
    require(roots <= seeds, 'Bundle root not an original source identity')
    require(len(seeds) == 100 and seeds <= nodes.keys(), 'Original 100-source identity census drift')
    reached, frontier, passes = set(roots), set(roots), []
    while frontier:
        new = {e['target'] for key in frontier for e in by_source[key].values()
               if e['classification'] in SEALED} - reached
        passes.append({'objects_inspected': len(frontier), 'new_sealed_objects': len(new)})
        reached.update(new)
        frontier = new
    require(reached == set(nodes), f'Orphan/unreachable sealed identities: {set(nodes) - reached}')
    # A complete confirmation pass over every reachable source, not just a leaf frontier.
    require(all(set(references(k, contents[k])) == set(by_source[k]) for k in reached), 'Fixed point failed')
    alpha = sorted(k for k in seeds if '/APPUI_ALPHA_' in k)
    require(len(alpha) == 7 and alpha == data['coverage']['alpha'], 'Alpha 7/7 census drift')
    require(set(data['coverage']['components']) == {f'COMP-{i:02}' for i in range(1, 12)}, 'Component 11/11 census drift')
    for family, keys in data['coverage']['components'].items():
        require(len(keys) >= 4 and set(keys) <= reached, f'Incomplete method/result/carrier/probe: {family}')
    ledger = contents['A:docs/evidence/DESIGN_LEDGER.md']
    for number, entry in data['coverage']['ledger'].items():
        start, end = entry['range']
        section = ledger.splitlines()[start - 1:end]
        require(int(number[2:]) in SELECTED and re.match(rf'## {number}\b', section[0]) and
                entry['state'] in section, f'Ledger state/range drift: {number}')
    require(len(data['coverage']['ledger']) == 34, 'Ledger 34/34 census drift')
    seen, visited, frontier, discoveries = set(seeds), set(), set(seeds), []
    while frontier:
        touched = {e['target'] or e['reference'] for k in frontier for e in by_source[k].values()}
        discoveries.append(len(touched - seen))
        seen.update(touched)
        visited.update(frontier)
        frontier = {e['target'] for k in frontier for e in by_source[k].values()
                    if e['classification'] in SEALED} - visited
    discoveries.append(0)  # Full-source confirmation after the frontier empties.
    require(discoveries == data['traversal']['new_reference_targets_by_pass'], 'Reference discovery-count drift')
    require(data['traversal']['confirmation_pass_objects_inspected'] == len(nodes), 'Incomplete confirmation pass')
    return passes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    data = json.loads(ORACLE.read_text(encoding='utf-8'))
    baseline = git('show', '53dd20c8397209dfad6e5db6912c124dc82ae2b4:docs/Q_ADMIN_05_APP_DESIGN_SOURCE_FREEZE_2026_09_20.md').decode('utf-8')
    original = re.findall(r'^\| ([AWFH]) \| ([^|]+) \| ([0-9a-f]{40}) \| (\d+) \| ([0-9a-f]{64}) \|', baseline, re.M)
    require(set(data['source_identities']) == {a + ':' + p.strip() for a, p, *_ in original}, 'Original source set changed')
    contents = {}
    for key, node in data['nodes'].items():
        require(node['repository'] == 'Rylascoo/Ensemble-Website', f'Foreign source bytes: {key}')
        require(node['ref'] == data['refs'][node['alias']], f'Alias drift: {key}')
        raw = git('show', f"{node['ref']}:{node['path']}")
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        require((blob, len(raw), hashlib.sha256(raw).hexdigest()) ==
                (node['blob'], node['bytes'], node['sha256']), f'Identity mismatch: {key}')
        require(node['semantic_role'] and node['authority_scope'] and node['dependent_bundles'], f'Unscoped identity: {key}')
        contents[key] = raw.decode('utf-8-sig')
    passes = graph_checks(data, contents)
    require(data['counts']['sealed_source_identities_total'] == len(contents) and
            data['counts']['added_dependency_identities'] == len(contents) - len(original), 'Identity count drift')
    require(passes == data['traversal']['sealed_object_passes'], 'Traversal-count drift')
    require(data['traversal']['unresolved_authority_references'] == 0 and
            data['traversal']['full_confirmation_pass_new_references'] == 0, 'Closure not asserted cleanly')
    for key in data['c03_current_main_objects']:
        node = data['nodes'][key]
        require(hashlib.sha256(git('show', f"{data['base']}:{node['path']}")).hexdigest() == node['sha256'],
                f'C03 correction-baseline reconciliation mismatch: {key}')
    if args.self_test:
        mutations = []
        omitted_edge = copy.deepcopy(data)
        omitted_edge['edges'].pop(0)
        mutations.append(('omitted edge', omitted_edge, contents))
        omitted_identity = copy.deepcopy(data)
        del omitted_identity['nodes']['A:docs/KYMAEAN_LANE_A_STAGE_CONE_INTERACTION_01.md']
        mutations.append(('omitted normative identity', omitted_identity, contents))
        injected = dict(contents)
        injected['A:docs/KYMAEAN_APPUI_COMPONENT_SYSTEM_FOUNDATION_01.md'] += '\nRequired authority: docs/UNRECORDED_AUTHORITY.md\n'
        mutations.append(('new undisposed authority', data, injected))
        for name, changed, texts in mutations:
            try:
                graph_checks(changed, texts)
            except ValueError:
                print(f'Negative control PASS: {name}')
            else:
                raise ValueError(f'Negative control incorrectly passed: {name}')
    print(json.dumps({'result': 'PASS', 'identities': len(contents), 'edges': len(data['edges']),
                      'bundles': 22, 'alpha': '7/7', 'components': '11/11', 'ledger': '34/34',
                      'passes': passes, 'unresolved_authority_references': 0,
                      'full_confirmation_pass_new_references': 0}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f'Q-ADMIN-05 recursive closure FAIL: {error}', file=sys.stderr)
        sys.exit(1)
