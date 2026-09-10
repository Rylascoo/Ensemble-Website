#!/usr/bin/env python3
import argparse, hashlib, html.parser, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
M=ROOT/'prototypes/clr-01/manifest.json'; H=ROOT/'prototypes/clr-01/harness.html'; A=ROOT/'docs/evidence/CLR_01_EXECUTION_DEFAULTS_ADDENDUM_01.json'
def rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))
def lin(c): return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
def lum(h):
 r,g,b=rgb(h); return .2126*lin(r)+.7152*lin(g)+.0722*lin(b)
def ratio(a,b):
 x,y=lum(a),lum(b); return (max(x,y)+.05)/(min(x,y)+.05)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
class Grab(html.parser.HTMLParser):
 def __init__(self): super().__init__(); self.on=False; self.parts=[]
 def handle_starttag(self,t,a):
  if t=='pre' and dict(a).get('id')=='diagnostic-report': self.on=True
 def handle_endtag(self,t):
  if t=='pre' and self.on:self.on=False
 def handle_data(self,d):
  if self.on:self.parts.append(d)
def load_diag(p):
 g=Grab(); g.feed(Path(p).read_text(errors='replace')); raw=''.join(g.parts).strip()
 if not raw: raise RuntimeError(f'missing diagnostic report in {p}')
 return json.loads(raw)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--normal'); ap.add_argument('--forced'); ap.add_argument('--output'); ap.add_argument('--browser-version',default=''); ap.add_argument('--os-pretty',default=''); args=ap.parse_args()
 m=json.loads(M.read_text()); json.loads(A.read_text()); failures=[]; contrast=[]
 expected=[f'{f}-{c}-{v}' for f in m['families_in_order'] for c in m['contexts_in_order'] for v in m['viewports_in_order']]
 if len(expected)!=24 or len(set(expected))!=24: failures.append('matrix cardinality')
 src=H.read_text()
 for bad in ['linear-gradient','radial-gradient','filter:blur','background-image:url','@font-face','@keyframes','.animate(','transition: all','box-shadow:0']:
  if bad in src: failures.append('forbidden source carrier '+bad)
 for f in m['families_in_order']:
  for c in m['contexts_in_order']:
   v=m['families'][f][c]
   checks={'primary_field':ratio(v['primary'],v['field']),'secondary_field':ratio(v['secondary'],v['field']),'primary_soft':ratio(v['primary'],v['soft_surface']),'secondary_soft':ratio(v['secondary'],v['soft_surface']),'accent_field':ratio(v['accent'],v['field']),'boundary_field':ratio(v['boundary'],v['field'])}
   ok=checks['primary_field']>=4.5 and checks['secondary_field']>=4.5 and checks['primary_soft']>=4.5 and checks['secondary_soft']>=4.5 and checks['accent_field']>=4.5 and checks['boundary_field']>=3
   contrast.append({'family':f,'context':c,'ratios':{k:round(x,6) for k,x in checks.items()},'pass':ok})
   if not ok: failures.append(f'contrast floor {f}-{c}')
 if args.normal and args.forced:
  n=load_diag(args.normal); fc=load_diag(args.forced)
  if n.get('forcedColors') is not False: failures.append('normal forcedColors not false')
  if fc.get('forcedColors') is not True: failures.append('forced-colors emulation inactive')
  nb={x['id']:x for x in n['specimens']}; fb={x['id']:x for x in fc['specimens']}
  if sorted(nb)!=sorted(expected):failures.append('normal matrix mismatch')
  if sorted(fb)!=sorted(expected):failures.append('forced matrix mismatch')
  for sid in expected:
   for mode,b in [('normal',nb),('forced',fb)]:
    if sid not in b: continue
    z=b[sid]; target_w=1280 if z['context']=='WEB' and z['viewport']=='WIDE' else 1024 if z['context']=='APP' and z['viewport']=='WIDE' else 320
    panel_w=720 if z['context']=='WEB' and z['viewport']=='WIDE' else 680 if z['context']=='APP' and z['viewport']=='WIDE' else 288
    if abs(z['frame']['width']-target_w)>.01 or z['frame']['scrollWidth']>target_w: failures.append(f'{mode} frame/reflow {sid}')
    if abs(z['panel']['width']-panel_w)>.01 or abs(z['panel']['top']-72)>.01 or z['panel']['scrollWidth']>z['panel']['width']+.01: failures.append(f'{mode} panel geometry {sid}')
    if not z['action']['focused'] or z['action']['style']['outlineStyle']!='double' or float(z['action']['style']['outlineWidth'].replace('px',''))<3: failures.append(f'{mode} focus geometry {sid}')
    if z['action']['text']!='Open another view':failures.append(f'{mode} action text {sid}')
    for st in [z['panel']['style'],z['heading'],z['body'],z['action']['style']]+z['labels']+z['texts']+[r['style'] for r in z['rows']]:
     if st['backgroundImage']!='none' or st['filter']!='none' or st['boxShadow']!='none' or st['animationName']!='none' or st['transitionDuration']!='0s': failures.append(f'{mode} forbidden computed carrier {sid}')
    if mode=='forced':
     if z['strip']['display']!='none': failures.append(f'forced accent strip not suppressed {sid}')
     if not all(r['style']['borderBottomStyle']!='none' and float(r['style']['borderBottomWidth'].replace('px',''))>=1 for r in z['rows']):failures.append(f'forced row structure {sid}')
     for text in ['A field holds several related parts.','Each part remains distinct while sharing one context.','Primary note','A relationship remains visible.','Secondary note','Another detail remains present.','Reference','The surrounding field stays quiet.','Open another view']:
      if text not in z['textContent']: failures.append(f'forced missing text {sid}: {text}')
 ev={'schema':'kymaean.clr01.structural-accessibility-preflight.v1','status':'CLEAN_PREFLIGHT_NO_DIRECTOR_PREFERENCE' if not failures else 'FAILED_PREFLIGHT_NO_DIRECTOR_PREFERENCE','date':'2026-09-10','program_id':'CLR-01','method_main':m['method_main'],'source_sha256':{'harness.html':sha(H),'manifest.json':sha(M),'execution_defaults':sha(A),'verifier':sha(Path(__file__))},'environment':{'browser_version':args.browser_version,'os_pretty':args.os_pretty},'checks':{'matrix_count':len(expected),'contrast':contrast,'browser_normal':bool(args.normal),'browser_forced_colors':bool(args.forced)},'historical_palette_quarantine':m['historical_palette_quarantine'],'failures':failures}
 if args.output: Path(args.output).write_text(json.dumps(ev,indent=2)+'\n')
 print(json.dumps(ev,indent=2)); return 1 if failures else 0
if __name__=='__main__': raise SystemExit(main())
