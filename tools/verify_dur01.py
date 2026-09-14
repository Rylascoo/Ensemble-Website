#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'docs/evidence/PHASE_C_POST_CPS_01_REENTRY_AUDIT_07.json'
METHOD=ROOT/'docs/evidence/DUR_01_INTEGRATED_IDENTITY_DURABILITY_METHOD_01.json'
DECISION=ROOT/'docs/evidence/CPS_01_DIRECTOR_ARCHITECTURE_DECISION_01.json'
REGISTRY=ROOT/'docs/evidence/DESIGN_PACKET_REGISTRY_01.json'
CURRENT=ROOT/'CURRENT_STATE.md'
LEDGER=ROOT/'docs/evidence/DESIGN_LEDGER.md'
HANDOFF=ROOT/'docs/HANDOFF_DUR_01_INTEGRATED_IDENTITY_DURABILITY_2026_09_14.md'
EXPECTED={AUDIT:'7623092491bdc705351cc74d856ab15b61be04a71ae0d72ef3f5e27c956080f3',METHOD:'7b82ddc895843f27e7ca8b0740b5108fa0b44f2a29507e129cf6aa14e9d8c308',DECISION:'02f14c5360b07ca6b5d04f80e16fb9877976eee0c4a0ec10f1d9a924f82413a8'}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def fail(s): raise AssertionError(s)
def main():
 for p,h in EXPECTED.items():
  if sha(p)!=h: fail(f'hash mismatch {p.relative_to(ROOT)}: {sha(p)}')
 audit,method,decision,reg=map(load,[AUDIT,METHOD,DECISION,REGISTRY])
 if audit.get('status')!='COMPLETE_DUR_01_ACTIVATED': fail('audit status')
 if audit.get('selected_program',{}).get('id')!='DUR-01': fail('DUR activation')
 if method.get('status')!='FROZEN_PRE_CONSTRUCTION_DETERMINISTIC_NON_RENDER': fail('method status')
 if method.get('activation_audit_sha256')!=EXPECTED[AUDIT]: fail('audit linkage')
 if decision.get('selected_architecture',{}).get('id')!='CPS-B': fail('CPS-B decision')
 sp=reg.get('synthesis_policy',{})
 if sp.get('active_character_presence_status')!='DIRECTOR_SELECTED_CPS_B': fail('stale CPS synthesis status')
 if sp.get('active_durability_program')!='DUR-01' or sp.get('active_durability_status')!='METHOD_FROZEN_PRE_CONSTRUCTION': fail('registry DUR state')
 if sp.get('active_durability_method_sha256')!=EXPECTED[METHOD]: fail('registry method hash')
 cur=CURRENT.read_text(encoding='utf-8'); led=LEDGER.read_text(encoding='utf-8'); hand=HANDOFF.read_text(encoding='utf-8')
 for token in ['DUR-01 — Integrated Identity Durability','ACTIVE / METHOD FROZEN / PRE-CONSTRUCTION',EXPECTED[AUDIT],EXPECTED[METHOD],'CPS-B Distributed Recognition Mesh']:
  if token not in cur: fail(f'CURRENT_STATE missing {token}')
 if len(CURRENT.read_bytes())>3072: fail('CURRENT_STATE exceeds 3 KiB cap')
 for token in ['## L-161 - Post-CPS reentry activates DUR-01 integrated identity durability',EXPECTED[AUDIT],EXPECTED[METHOD]]:
  if token not in led: fail(f'ledger missing {token}')
 for token in ['DUR-01 METHOD FROZEN / PRE-CONSTRUCTION',EXPECTED[AUDIT],EXPECTED[METHOD],'CPS-B Distributed Recognition Mesh']:
  if token not in hand: fail(f'handoff missing {token}')
 for token in ['new Character artwork or renderer generation','CLR F2/F1','Stage','Phase D']:
  if not any(token in x for x in audit.get('hard_boundaries',[])): fail(f'audit boundary {token}')
 bad=[]
 for p in [AUDIT,METHOD,DECISION,REGISTRY,CURRENT,LEDGER,HANDOFF]:
  txt=p.read_text(encoding='utf-8'); bad += [(p.name,ord(c)) for c in txt if ord(c)<32 and c not in '\n\r\t']
 if bad: fail(f'control characters {bad[:8]}')
 print('DUR_01_ACTIVATION=PASS')
 print('CPS_B=CANONICAL DUR_01=METHOD_FROZEN_PRE_CONSTRUCTION')
 print('CLR=DEFERRED STAGE=UNCHANGED PHASE_D=NOT_AUTHORIZED')
 return 0
if __name__=='__main__':
 try: sys.exit(main())
 except Exception as e: print(f'DUR_01_FAIL: {e}',file=sys.stderr); sys.exit(1)
