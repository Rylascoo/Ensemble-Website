#!/usr/bin/env python3
from __future__ import annotations
import argparse
import base64
import hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TEMPLATE=ROOT/'prototypes/app-syn-01/harness-template.html'
C0=ROOT/'assets/brand/kymaean-threshold-k-working-candidate.svg'
O3=ROOT/'assets/brand/kymaean-o3-wordmark-temporary-incumbent.svg'
EXPECTED_C0='72cdd4c35928e1fb0bc279b680b9b7a698707dc1564ee800a84840fe61356305'
EXPECTED_O3='204e6f7b3239f44267a04afa2c12f0254a56142e9298ee6e7fab9f9061a674f5'
EXPECTED_STAGE='7f3b3a815d71d1aa47350e69824f14f92a5dd399cf0c68bf16074827ead6b3c0'
EXPECTED_STAGE_BYTES=1431659

def raw_sha(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def lf_bytes(path:Path)->bytes:return path.read_text(encoding='utf-8').replace('\r\n','\n').replace('\r','\n').encode('utf-8')
def lf_sha(path:Path)->str:return hashlib.sha256(lf_bytes(path)).hexdigest()

def main()->int:
 p=argparse.ArgumentParser()
 p.add_argument('--stage',required=True)
 p.add_argument('--output',default=str(ROOT/'.tmp/app-syn-01/harness.html'))
 a=p.parse_args();stage=Path(a.stage);out=Path(a.output)
 if lf_sha(C0)!=EXPECTED_C0: raise SystemExit('C0 hash mismatch')
 if lf_sha(O3)!=EXPECTED_O3: raise SystemExit('O3 hash mismatch')
 if raw_sha(stage)!=EXPECTED_STAGE or stage.stat().st_size!=EXPECTED_STAGE_BYTES: raise SystemExit('Stage byte/hash mismatch')
 template=TEMPLATE.read_text(encoding='utf-8').replace('\r\n','\n').replace('\r','\n')
 c0=C0.read_text(encoding='utf-8').replace('\r\n','\n').replace('\r','\n')
 o3=O3.read_text(encoding='utf-8').replace('\r\n','\n').replace('\r','\n')
 data='data:image/png;base64,'+base64.b64encode(stage.read_bytes()).decode('ascii')
 rendered=template.replace('__C0_SVG__',c0).replace('__O3_SVG__',o3).replace('__STAGE_DATA_URI__',data)
 if '__C0_SVG__' in rendered or '__O3_SVG__' in rendered or '__STAGE_DATA_URI__' in rendered: raise SystemExit('unresolved template token')
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(rendered,encoding='utf-8',newline='\n')
 print('APP_SYN_01_MATERIALIZE=PASS')
 print('OUTPUT='+str(out))
 print('OUTPUT_SHA256='+hashlib.sha256(out.read_bytes()).hexdigest())
 print('STAGE_SHA256='+EXPECTED_STAGE)
 return 0

if __name__=='__main__':
 raise SystemExit(main())
