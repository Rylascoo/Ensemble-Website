#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'docs/evidence/VFD_01_PRIMARY_INPUT_MANIFEST_01.json'
METHOD=ROOT/'docs/evidence/VFD_01_SECOND_FAMILY_WHOLE_SURFACE_REPRESENTATION_METHOD_01.json'
FORBIDDEN=(
    'Kymaean','Ensemble','Threshold K','Ratio Ladder','Subtractive Channel',
    'Ring + Edge','F1A','CS2','CLR-01','Quiet Stage','Mineral Theater',
    'CMP-01','CMP-02','SYM-01','SYM-02','TYP-02','STA-01','MOT-01'
)
def fail(msg:str)->None:
    print('VFD01_STATIC=FAIL',msg)
    raise SystemExit(1)
def load(path:Path):
    return json.loads(path.read_text(encoding='utf-8'))
def main()->None:
    m=load(MANIFEST); method=load(METHOD)
    if m.get('program_id')!='VFD-01' or m.get('image_generation_consumed')!=0: fail('manifest state')
    if m.get('primary_packets_frozen')!=4 or m.get('transfer_packets_frozen')!=4: fail('packet counts')
    if method.get('premise_matrix',{}).get('premise_count')!=4: fail('method premise count')
    if method.get('probe_budget',{}).get('maximum_total_images')!=6: fail('method image ceiling')
    files=m.get('files',{})
    for rel,meta in files.items():
        path=ROOT/rel
        if not path.is_file(): fail(f'missing {rel}')
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=meta.get('sha256'): fail(f'hash {rel}')
        if len(data)!=meta.get('bytes'): fail(f'bytes {rel}')
    prim=list((ROOT/'docs/evidence/renderer').glob('VFD_01_P*_PRIMARY_STERILE_PACKET_01.txt'))
    trans=list((ROOT/'docs/evidence/renderer').glob('VFD_01_P*_TRANSFER_STERILE_PACKET_01.txt'))
    if len(prim)!=4 or len(trans)!=4: fail('renderer packet cardinality')
    for path in prim+trans:
        text=path.read_text(encoding='utf-8')
        for token in FORBIDDEN:
            if token.lower() in text.lower(): fail(f'forbidden renderer token {token} in {path.name}')
    audit=load(ROOT/'docs/evidence/VFD_01_PREMISE_PAIRWISE_AUDIT_01.json')
    if len(audit.get('pairs',[]))!=6 or not all(x.get('passes_floor') and x.get('count',0)>=4 for x in audit['pairs']): fail('pairwise floor')
    distance=load(ROOT/'docs/evidence/VFD_01_PRE_RENDER_CONTAMINATION_DISTANCE_AUDIT_01.json')
    if not all(str(v.get('result','')).startswith('ELIGIBLE') for v in distance.get('premises',{}).values()): fail('distance eligibility')
    print(f"VFD01_STATIC=PASS files={len(files)} primary=4 transfer=4 image_budget=0/6")
if __name__=='__main__': main()
