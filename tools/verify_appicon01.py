#!/usr/bin/env python3
import hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AUD=ROOT/'docs/evidence/PHASE_C_POST_DUR_01_REENTRY_AUDIT_08.json'
METHOD=ROOT/'docs/evidence/APPICON_01_PRIMARY_APP_ICON_DESIGN_MASTER_METHOD_01.json'
C0=ROOT/'assets/brand/kymaean-threshold-k-working-candidate.svg'
REG=ROOT/'docs/evidence/DESIGN_PACKET_REGISTRY_01.json'
CURRENT=ROOT/'CURRENT_STATE.md'
LEDGER=ROOT/'docs/evidence/DESIGN_LEDGER.md'
HAND=ROOT/'docs/HANDOFF_APPICON_01_PRIMARY_APP_ICON_DESIGN_MASTER_2026_09_14.md'
OLD_HAND=ROOT/'docs/HANDOFF_DUR_01_INTEGRATED_IDENTITY_DURABILITY_2026_09_14.md'
AUD_SHA='305e4c7fff0ddd58cd0c43fb0da5a9c62f6535e231a5818d28e0246e0ab29447'
METHOD_SHA='37bd7fff587779167a2062868430829f2fc660da7753214ea15a1f43b0c7712a'
C0_LF='72cdd4c35928e1fb0bc279b680b9b7a698707dc1564ee800a84840fe61356305'
C0_PATH='95304d003e63ab2272501da3451c1bca3deb84d206468d7e35264575d2bfe30d'
def lfbytes(p): return p.read_bytes().replace(b'\r\n',b'\n')
def sha_lf(p): return hashlib.sha256(lfbytes(p)).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def fail(msg): raise AssertionError(msg)
def main():
    if sha_lf(AUD)!=AUD_SHA: fail('audit hash mismatch')
    if sha_lf(METHOD)!=METHOD_SHA: fail('method hash mismatch')
    if sha_lf(C0)!=C0_LF: fail('C0 canonical LF hash mismatch')
    svg=C0.read_text(encoding='utf-8')
    paths=re.findall(r'<path d="([^"]+)"',svg)
    norm='|'.join(' '.join(x.split()) for x in paths).encode('utf-8')
    if len(paths)!=3 or hashlib.sha256(norm).hexdigest()!=C0_PATH: fail('C0 path-semantic mismatch')
    aud,method,reg=load(AUD),load(METHOD),load(REG)
    if aud.get('status')!='COMPLETE_APPICON_01_ACTIVATED': fail('audit status')
    if aud.get('selected_program',{}).get('id')!='APPICON-01': fail('selected program')
    if method.get('status')!='FROZEN_PRE_CONSTRUCTION_DETERMINISTIC_NON_RENDER': fail('method status')
    if method.get('activation_audit_sha256')!=AUD_SHA: fail('audit linkage')
    cands=method.get('candidates',[])
    if [(x.get('id'),x.get('inset_percent')) for x in cands] != [('E06',6),('E12',12),('E18',18)]: fail('candidate freeze')
    src=method.get('source',{})
    if src.get('canonical_lf_git_blob_sha256')!=C0_LF or src.get('path_semantic_sha256')!=C0_PATH: fail('source provenance')
    sp=reg.get('synthesis_policy',{})
    if sp.get('active_appicon_program')!='APPICON-01': fail('registry appicon program')
    if sp.get('active_appicon_status')!='METHOD_FROZEN_PRE_CONSTRUCTION': fail('registry appicon status')
    if sp.get('active_appicon_method_sha256')!=METHOD_SHA or sp.get('active_appicon_activation_audit_sha256')!=AUD_SHA: fail('registry hashes')
    cur=CURRENT.read_text(encoding='utf-8'); led=LEDGER.read_text(encoding='utf-8'); hand=HAND.read_text(encoding='utf-8'); old=OLD_HAND.read_text(encoding='utf-8')
    for token in ['APPICON-01 - Primary App Icon Design-Master Convergence','ACTIVE / METHOD FROZEN / PRE-CONSTRUCTION',AUD_SHA,METHOD_SHA,'E06/E12/E18']:
        if token not in cur: fail(f'CURRENT_STATE missing {token}')
    if len(CURRENT.read_bytes())>3072: fail('CURRENT_STATE exceeds 3 KiB')
    for token in ['## L-164 - Post-DUR reentry activates APPICON-01 design-master convergence',AUD_SHA,METHOD_SHA,C0_LF,C0_PATH]:
        if token not in led: fail(f'ledger missing {token}')
    for token in ['APPICON-01 METHOD FROZEN / PRE-CONSTRUCTION',AUD_SHA,METHOD_SHA,C0_LF,C0_PATH]:
        if token not in hand: fail(f'handoff missing {token}')
    if not old.startswith('<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->'): fail('old DUR handoff not historical')
    for token in ['C0 path geometry is immutable','Do not create C0-R4','Do not select CLR F2/F1','No Store/package/MSIX/shipping asset']:
        if not any(token in x for x in aud.get('hard_boundaries',[])): fail(f'audit boundary missing {token}')
    for p in [AUD,METHOD,REG,CURRENT,LEDGER,HAND,OLD_HAND,C0]:
        txt=p.read_text(encoding='utf-8')
        bad=[ord(c) for c in txt if ord(c)<32 and c not in '\n\r\t']
        if bad: fail(f'control characters in {p.name}: {bad[:8]}')
    print('APPICON_01_ACTIVATION=PASS')
    print('C0=IMMUTABLE E06_E12_E18=FROZEN METHOD=PRE_CONSTRUCTION')
    print('CLR=DEFERRED STAGE=UNCHANGED PHASE_D=NOT_AUTHORIZED SHIPPING=NOT_AUTHORIZED')
    return 0
if __name__=='__main__':
    try: sys.exit(main())
    except Exception as e:
        print(f'APPICON_01_FAIL: {e}',file=sys.stderr)
        sys.exit(1)
