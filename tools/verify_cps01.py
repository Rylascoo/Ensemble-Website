#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONCORDANCE = ROOT / 'docs/evidence/IMG_01_DIRECTOR_PRIOR_CONCORDANCE_01.json'
METHOD = ROOT / 'docs/evidence/CPS_01_CANONICAL_CHARACTER_PRESENCE_SYSTEM_METHOD_01.json'
PREFLIGHT = ROOT / 'docs/evidence/CPS_01_MECHANICAL_ACCESSIBILITY_PREFLIGHT_01.json'
EVALUATION = ROOT / 'docs/evidence/CPS_01_DESIGN_SOL_ARCHITECTURE_EVALUATION_01.json'
PACKET = ROOT / 'docs/evidence/packets/PKT_CPS_01_CANONICAL_CHARACTER_PRESENCE_SYSTEM_01.json'
REGISTRY = ROOT / 'docs/evidence/DESIGN_PACKET_REGISTRY_01.json'
CARRIER = ROOT / 'prototypes/cps-01/carrier.html'
PROBE = ROOT / 'tools/cps01_browser_probe.mjs'
HANDOFF = ROOT / 'docs/HANDOFF_CPS_01_CANONICAL_CHARACTER_PRESENCE_SYSTEM_2026_09_13.md'
CURRENT = ROOT / 'CURRENT_STATE.md'
LEDGER = ROOT / 'docs/evidence/DESIGN_LEDGER.md'

EXPECTED = {
    CONCORDANCE: '1ddf51fa28ddea497b8dd1da353f26733c0cf1a7a857e02020e1322a9c06ce27',
    METHOD: '3069f468a0fb98964758154f82e126d7a4296a529b78885c90818235527d6dc4',
    PREFLIGHT: '6cb91ac47baf957e15fe8fef6d8daa9cab5cadc9c97d22acf3fb4ee98b486275',
    EVALUATION: 'b85fd86efc65bd74d1def8c2e9445f343257801c04cd3510de02eea222e19137',
    PACKET: 'e3c12d607e370dd4304421082d29719a9a39a72f2c0906facb27d18279b4069f',
    CARRIER: '28fb10f481345288b8dc1cb278caf60a804027b82a1a4fd7058ccdd9f04ea65e',
    PROBE: 'a351cd302afa27365206af1338c00e463efffaa1dba16c8bb1d48d036b6ec8b2',
    HANDOFF: '465fa49ab1372a7b6415de5d91e218cc143c119f397903b49f25a43c36a1b623',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def fail(message):
    raise AssertionError(message)

def assert_hashes():
    for path, expected in EXPECTED.items():
        actual = sha(path)
        if actual != expected:
            fail(f'hash mismatch {path.relative_to(ROOT)}: {actual}')

def main():
    assert_hashes()
    method = load(METHOD)
    preflight = load(PREFLIGHT)
    evaluation = load(EVALUATION)
    packet = load(PACKET)
    registry = load(REGISTRY)
    current = CURRENT.read_text(encoding='utf-8')
    ledger = LEDGER.read_text(encoding='utf-8')
    handoff = HANDOFF.read_text(encoding='utf-8')

    if method.get('status') != 'FROZEN_PRE_CONSTRUCTION_DETERMINISTIC_NON_RENDER':
        fail('method status changed')
    if [x.get('id') for x in method.get('architecture_candidates', [])] != ['CPS-A', 'CPS-B', 'CPS-C']:
        fail('architecture candidates changed')
    roles = [x.split(':', 1)[0] for x in method.get('deterministic_test_roles', [])]
    expected_roles = [
        'MICRO','COMPACT','FOCUSED','CROPPED_FRAGMENT','RELATIONAL_PAIR',
        'ENSEMBLE_THREE','MONOCHROME_HIGH_CONTRAST','NO_IMAGE',
        'STATIC_REDUCED_MOTION','APP_WEB_TRANSLATION'
    ]
    if roles != expected_roles:
        fail('frozen roles changed')

    if preflight.get('status') != 'PASS_COMPLETE_MATRIX_POST_REPAIR':
        fail('preflight status')
    if preflight.get('authority', {}).get('carrier_sha256') != EXPECTED[CARRIER]:
        fail('preflight carrier hash')
    if preflight.get('authority', {}).get('browser_probe_sha256') != EXPECTED[PROBE]:
        fail('preflight probe hash')
    matrix = preflight.get('matrix', {})
    expected_modes = ['normal-1440','normal-320','text200-1440','text200-320','forced-1440','forced-320','reduced-1440']
    if list(matrix.keys()) != expected_modes:
        fail('preflight mode matrix')
    for mode, row in matrix.items():
        if row.get('overflow_count') != 0:
            fail(f'{mode} overflow')
        if row.get('image_count') != 0 or row.get('external_resource_count') != 0:
            fail(f'{mode} resource isolation')
        if row.get('motion_dependency_count') != 0:
            fail(f'{mode} motion dependency')
        if row.get('minimum_visible_crop_signature_segments', 0) < 2:
            fail(f'{mode} crop survival')
        if row.get('app_web_identity_match') is not True:
            fail(f'{mode} app-web identity')
    if preflight.get('candidate_mechanical_eligibility') != {
        'CPS-A':'ELIGIBLE_FOR_FROZEN_METHOD_SCORING',
        'CPS-B':'ELIGIBLE_FOR_FROZEN_METHOD_SCORING',
        'CPS-C':'ELIGIBLE_FOR_FROZEN_METHOD_SCORING',
    }:
        fail('mechanical eligibility')

    if evaluation.get('status') != 'DESIGN_SOL_VIEW_FROZEN_DIRECTOR_ADJUDICATION_PENDING':
        fail('evaluation status')
    results = {x['candidate']: x['result_class'] for x in evaluation.get('candidate_results', [])}
    if results != {'CPS-A':'TARGETED_REFINEMENT_REQUIRED','CPS-B':'ARCHITECTURE_SURVIVES','CPS-C':'ARCHITECTURE_SURVIVES_WITH_USAGE_RESTRAINT'}:
        fail('candidate result classes')
    conclusion = evaluation.get('comparative_conclusion', {})
    if conclusion.get('survivors') != ['CPS-B','CPS-C']:
        fail('survivor set')
    if conclusion.get('targeted_refinement_required') != ['CPS-A']:
        fail('targeted refinement set')
    if conclusion.get('design_sol_recommendation') != 'CPS-B':
        fail('Design Sol recommendation')
    if conclusion.get('canonical_architecture_selected') is not False or conclusion.get('director_adjudication_required') is not True:
        fail('Director adjudication boundary')
    if conclusion.get('director_choice_set') != ['CPS-B','CPS-C']:
        fail('Director choice set')

    if packet.get('packet_id') != 'PKT-CPS-01-01' or packet.get('status') != 'DIRECTOR_ADJUDICATION_PENDING':
        fail('packet identity/status')
    if packet.get('local_result', {}).get('survivors_or_closure') != ['CPS-B','CPS-C']:
        fail('packet survivor set')
    if packet.get('judgment', {}).get('resolution_mode') != 'DIRECTOR_ADJUDICATION_PENDING':
        fail('packet resolution mode')
    packet_rows = [x for x in registry.get('packets', []) if x.get('packet_id') == 'PKT-CPS-01-01']
    if len(packet_rows) != 1 or packet_rows[0].get('status') != 'DIRECTOR_ADJUDICATION_PENDING':
        fail('registry CPS packet')

    required_current = [
        'CPS-01 - Canonical Character Presence System',
        'MECHANICAL PREFLIGHT PASS / DESIGN SOL VIEW FROZEN / DIRECTOR B-C ADJUDICATION PENDING',
        EXPECTED[CARRIER], EXPECTED[PREFLIGHT], EXPECTED[EVALUATION], EXPECTED[PACKET],
        'choose **CPS-B** or **CPS-C**',
    ]
    for token in required_current:
        if token not in current:
            fail(f'CURRENT_STATE missing {token}')
    if len(CURRENT.read_bytes()) > 4096:
        fail('CURRENT_STATE exceeds 4096-byte continuity budget')

    if '## L-158 - CPS-01 deterministic carrier leaves B/C survivor choice pending Director adjudication' not in ledger:
        fail('ledger L-158 missing')
    for token in [EXPECTED[CARRIER], EXPECTED[PREFLIGHT], EXPECTED[EVALUATION], EXPECTED[PACKET]]:
        if token not in ledger:
            fail(f'ledger missing checkpoint hash {token}')

    for token in [
        'DIRECTOR B-C ADJUDICATION PENDING',
        'CPS-B — Distributed Recognition Mesh',
        'CPS-C — Context-Persistent Presence Scaffold',
        EXPECTED[PREFLIGHT], EXPECTED[EVALUATION], EXPECTED[PACKET], EXPECTED[CARRIER],
    ]:
        if token not in handoff:
            fail(f'handoff missing {token}')

    bad = []
    for path in [CONCORDANCE,METHOD,PREFLIGHT,EVALUATION,PACKET,REGISTRY,HANDOFF,CURRENT,LEDGER,CARRIER,PROBE]:
        text = path.read_text(encoding='utf-8')
        bad.extend((path.relative_to(ROOT).as_posix(), ord(c)) for c in text if ord(c) < 32 and c not in '\n\r\t')
    if bad:
        fail(f'control characters: {bad[:8]}')

    print('CPS_01_CHECKPOINT=PASS')
    print('SURVIVORS=CPS-B,CPS-C TARGETED_REFINEMENT=CPS-A')
    print('DESIGN_SOL_RECOMMENDATION=CPS-B DIRECTOR_ADJUDICATION=PENDING')
    print('MATRIX=7_MODES OVERFLOW=0 IMAGES=0 EXTERNAL=0 MOTION_DEPENDENCIES=0')
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(f'CPS_01_FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
