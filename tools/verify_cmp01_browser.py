#!/usr/bin/env python3
import argparse,hashlib,json,math,sys
from pathlib import Path
VARIANTS=['FULL','NO_MAT','NO_SYM','NO_STA','NO_MOT']
CONTEXTS=['APP','WEB']
IDS=[f'{v}-{c}' for v in VARIANTS for c in CONTEXTS]
def fail(msg): raise AssertionError(msg)
def sha(p): return hashlib.sha256(Path(p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()
def close(a,b,tol=.8): return abs(float(a)-float(b))<=tol
def px(v):
 try:return float(str(v).replace('px',''))
 except:return -1
def by_id(d): return {s['id']:s for s in d['surfaces']}
def check_file(path,label,width,forced,reduced):
 d=json.loads(Path(path).read_text(encoding='utf-8'))
 vp=d.get('viewport',{})
 if round(vp.get('width',-1))!=width: fail(f'{label}: viewport')
 if vp.get('scrollWidth',10**9)>width+1: fail(f'{label}: document overflow {vp}')
 if bool(d.get('forcedColors'))!=forced: fail(f'{label}: forced-colors mismatch')
 if bool(d.get('reducedMotion'))!=reduced: fail(f'{label}: reduced-motion mismatch')
 if d.get('variantOrder')!=VARIANTS: fail(f'{label}: variant order')
 if d.get('prohibitedElements')!=0 or d.get('externalStyleLinks')!=0: fail(f'{label}: prohibited resources')
 if d.get('overflowElements'): fail(f'{label}: overflow elements {d["overflowElements"][:3]}')
 surfaces=d.get('surfaces',[])
 if [s.get('id') for s in surfaces]!=IDS: fail(f'{label}: surface order')
 m=by_id(d)
 for sid,s in m.items():
  ctx=s['context']; r=s['rect']; floor=340 if ctx=='APP' else 390; cap=420 if ctx=='APP' else 680
  if r['height']+1<floor: fail(f'{label}/{sid}: min-height')
  if r['x']<-.75 or r['right']>width+.75: fail(f'{label}/{sid}: viewport bounds')
  if width==1200 and r['width']>cap+.75: fail(f'{label}/{sid}: max-width')
  if width==320 and r['width']>300.75: fail(f'{label}/{sid}: 320 width')
  if s['selected']['aria']!='true': fail(f'{label}/{sid}: selected aria')
  v=s['variant']; channels=s['channels']; c0=s['c0']['visibility']; wit=s['selected']['witness']['display']
  if v=='NO_MAT':
   if any(x['display']!='none' for x in channels): fail(f'{label}/{sid}: MAT ablation')
  elif any(x['display']=='none' for x in channels): fail(f'{label}/{sid}: MAT unexpectedly absent')
  if (v=='NO_SYM')!=(c0=='hidden'): fail(f'{label}/{sid}: symbol ablation')
  if v=='NO_STA':
   if wit!='none': fail(f'{label}/{sid}: STA witness remains')
  elif wit=='none': fail(f'{label}/{sid}: STA witness missing')
 for v in VARIANTS:
  a,w=m[f'{v}-APP'],m[f'{v}-WEB']
  if width==1200:
   if w['rect']['x']<=a['rect']['right']: fail(f'{label}/{v}: wide contexts not side by side')
  else:
   if w['rect']['y']<=a['rect']['bottom']: fail(f'{label}/{v}: 320 contexts not stacked')
 k=d.get('keyboardFocus',[])
 for sid in ('FULL-APP','FULL-WEB'):
  hits=[x for x in k if x and x.get('surface')==sid and x.get('text')=='Field B']
  if not hits: fail(f'{label}: keyboard did not reach {sid} selected')
  x=hits[0]
  if not x.get('focusVisible') or px(x.get('outlineWidth'))<1.9 or x.get('outlineStyle')=='none': fail(f'{label}/{sid}: focus-visible ring')
  if x.get('witnessDisplay')=='none': fail(f'{label}/{sid}: selected witness lost under focus')
 return d
def check_motion(d,label,reduced):
 motion=d.get('motion',{})
 for sid,dy in [('FULL-APP',28),('FULL-WEB',56)]:
  x=motion.get(sid); 
  if not x: fail(f'{label}/{sid}: motion diagnostic missing')
  if reduced:
   if x['midF1A']!={'peerAnimations':0,'fieldAnimations':0}: fail(f'{label}/{sid}: reduced F1A animation')
   if x['midCS2']!={'peerAnimations':0,'fieldAnimations':0}: fail(f'{label}/{sid}: reduced CS2 animation')
  else:
   if x['midF1A']!={'peerAnimations':3,'fieldAnimations':0}: fail(f'{label}/{sid}: F1A partition {x["midF1A"]}')
   if x['midCS2']!={'peerAnimations':0,'fieldAnimations':2}: fail(f'{label}/{sid}: CS2 partition {x["midCS2"]}')
  if any(not close(p['translateY'],dy,1) for p in x['afterF1A']['peers']): fail(f'{label}/{sid}: F1A final displacement')
  if [round(f['opacity'],2) for f in x['afterF1A']['fields']]!=[1,0]: fail(f'{label}/{sid}: F1A changed context')
  if x['afterCS2']['activeContext']!='B' or [round(f['opacity'],2) for f in x['afterCS2']['fields']]!=[0,1]: fail(f'{label}/{sid}: CS2 final context')
  if any(not close(p['translateY'],dy,1) for p in x['afterCS2']['peers']): fail(f'{label}/{sid}: CS2 disturbed peer final state')
 for sid,dy in [('NO_MOT-APP',28),('NO_MOT-WEB',56)]:
  x=motion.get(sid)
  if not x: fail(f'{label}/{sid}: no-mot diagnostic missing')
  if x['midF1A']!={'peerAnimations':0,'fieldAnimations':0} or x['midCS2']!={'peerAnimations':0,'fieldAnimations':0}: fail(f'{label}/{sid}: NO_MOT animated')
  if any(not close(p['translateY'],dy,1) for p in x['afterCS2']['peers']): fail(f'{label}/{sid}: NO_MOT peer final')
  if x['afterCS2']['activeContext']!='B' or [round(f['opacity'],2) for f in x['afterCS2']['fields']]!=[0,1]: fail(f'{label}/{sid}: NO_MOT context final')
def main():
 ap=argparse.ArgumentParser()
 labels=[]
 for forced in ('normal','forced'):
  for motion in ('full','reduced'):
   for width in ('wide','320'):
    name=f'{forced}-{motion}-{width}'
    ap.add_argument('--'+name,required=True)
    labels.append(name)
 ap.add_argument('--browser-version',required=True)
 ap.add_argument('--os-pretty',required=True)
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 data={}
 for label in labels:
  forced=label.startswith('forced-')
  reduced='-reduced-' in label
  width=320 if label.endswith('-320') else 1200
  path=getattr(a,label.replace('-','_'))
  d=check_file(path,label,width,forced,reduced)
  check_motion(d,label,reduced)
  data[label]=d
 print('CMP01_BROWSER=PASS')
 out={'schema':'kymaean.cmp01.browser-preflight.v1','status':'PASS_COMPLETE_8_MODE_MATRIX','browser_version':a.browser_version,'os_pretty':a.os_pretty,'variants':VARIANTS,'contexts':CONTEXTS,'scored_variant':'FULL','modes':{}}
 for label,d in data.items():
  out['modes'][label]={'viewport':d['viewport'],'forcedColors':d['forcedColors'],'reducedMotion':d['reducedMotion']}
 out['browser_verifier_sha256']=sha(Path(__file__))
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':
 try: main()
 except Exception as e:
  print('CMP01_BROWSER_FAIL:',e,file=sys.stderr);sys.exit(1)
