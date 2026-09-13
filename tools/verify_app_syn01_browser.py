#!/usr/bin/env python3
from __future__ import annotations
import json
import math
import sys
from pathlib import Path

EXPECTED_IDS={'REF_NEUTRAL_COMPOSITION','REF_IDENTITY_STACK','REF_INTERACTION_STRIP','F2_FULL','F2_NO_MAT','F2_NO_O3','F2_NO_MOT','F1_FULL','F1_NO_MAT','F1_NO_O3','F1_NO_MOT'}
O3_HIDDEN={'REF_NEUTRAL_COMPOSITION','REF_INTERACTION_STRIP','F2_NO_O3','F1_NO_O3'}
EXPECTED_MODES={(1200,False,False,100,False),(320,False,False,100,False),(1200,False,False,200,False),(320,False,False,200,False),(1200,False,False,100,True),(320,False,False,100,True),(1200,True,False,100,False),(320,True,False,100,False),(1200,False,True,100,False),(320,False,True,100,False)}

def px(value:str)->float:
 if value.endswith('px'):return float(value[:-2])
 return 0.0

def main()->int:
 root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.tmp/app-syn-01/diagnostics')
 files=sorted(root.glob('*.json'));assert len(files)==10,(len(files),files)
 seen=set()
 for path in files:
  d=json.loads(path.read_text(encoding='utf-8'));r=d['requested'];mode=(r['width'],r['forced'],r['reduced'],r['fontPercent'],r['spacing']);seen.add(mode)
  assert d['stage']['complete'] and d['stage']['naturalWidth']==1672 and d['stage']['naturalHeight']==941 and d['stage']['srcIsDataPng']
  assert math.isclose(d['stage']['width']/d['stage']['height'],1672/941,rel_tol=.002)
  assert d['surfaceCount']==11 and not d['remoteRefs'],path
  raw_overflow=d.get('overflowElements') or []
  sr_only=[x for x in raw_overflow if x.get('tag')=='SPAN' and 'brand-name' in (x.get('cls') or '').split() and float(x.get('width',0))<=1.1 and float(x.get('clientWidth',0))<=1]
  material_overflow=[x for x in raw_overflow if x not in sr_only]
  assert len(sr_only)==11,(path,'sr-only overflow count',len(sr_only))
  assert not material_overflow,(path,material_overflow)
  surfaces={s['id']:s for s in d['surfaces']};assert set(surfaces)==EXPECTED_IDS
  for sid,s in surfaces.items():
   assert s['brandNames']==1 and s['c0Paths']==3
   assert s['o3Visible']==(sid not in O3_HIDDEN),(sid,s['o3Visible'])
   assert px(s['selectedWitness']['width'])>=3 or px(s['selectedWitness']['height'])>=3
   assert s['peerCount']==3 and s['contextCount']==2
   assert s['width']<=420.6 and s['scrollWidth']<=s['clientWidth']+1
  focused={x['surface'] for x in d['keyboardFocus'] if x and x.get('surface') and x.get('focusVisible') and px(x.get('outlineWidth') or '0px')>=2}
  assert focused==EXPECTED_IDS,(path,EXPECTED_IDS-focused)
  m=d['motionComputed'];assert m and m['surface']=='REF_NEUTRAL_COMPOSITION'
  if r['reduced']:
   assert m['peerTransitionDuration'] in ('0s','0ms') and m['contextBTransitionDuration'] in ('0s','0ms')
  else:
   assert m['peerTransitionDuration']=='0.46s' and m['peerTransitionDelay']=='0.07s'
   assert m['contextATransitionDuration']=='0.28s' and m['contextBTransitionDuration']=='0.28s'
 assert seen==EXPECTED_MODES,(EXPECTED_MODES-seen,seen-EXPECTED_MODES)
 print('APP_SYN_01_BROWSER=PASS')
 print('MODES=10')
 print('SURFACES_PER_MODE=11')
 return 0

if __name__=='__main__':
 raise SystemExit(main())
