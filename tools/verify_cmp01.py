#!/usr/bin/env python3
import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/'prototypes/cmp-01/harness.html'
METHOD=ROOT/'docs/evidence/CMP_01_BOUNDED_PACKET_COMPOSITION_METHOD_AND_MATRIX_01.json'
DEFAULTS=ROOT/'docs/evidence/CMP_01_EXECUTION_DEFAULTS_01.json'
MANIFEST=ROOT/'docs/evidence/CMP_01_FROZEN_SOURCE_MANIFEST_03.json'
PROBE=ROOT/'tools/cmp01_browser_probe.mjs'
BVERIFY=ROOT/'tools/verify_cmp01_browser.py'
WORKFLOW=ROOT/'.github/workflows/tmp-cmp01-browser-preflight.yml'
C0=ROOT/'assets/brand/kymaean-threshold-k-working-candidate.svg'
PACKETS=['PKT_SYM_01_PRIMARY_SYMBOL_SUCCESSOR_01.json','PKT_MAT_01_MATERIAL_SHAPE_GRAMMAR_01.json','PKT_STA_01_NONCOLOR_STATE_GRAMMAR_01.json','PKT_MOT_F1A_WITHIN_CONTEXT_SUCCESSION_01.json','PKT_MOT_CS2_CONTEXT_SHIFT_01.json']
VARIANTS=['FULL','NO_MAT','NO_SYM','NO_STA','NO_MOT']
ALLOWED_HEX={'#f7f7f4','#ecece7','#1b1b19','#8a8a82','#62625d'}
C0_PATHS=['M 65 15 L 54 21 L 52 23 L 47 25 L 45 27 L 40 29 L 38 31 L 33 33 L 31 35 L 26 37 L 24 39 L 21 40 L 19 42 L 10 47 L 10 116 L 23 109 L 28 105 L 31 104 L 49 92 L 55 86 L 61 77 L 61 75 L 63 72 L 64 65 L 65 64 Z','M 10 126 L 10 192 L 16 196 L 19 197 L 21 199 L 24 200 L 26 202 L 29 203 L 31 205 L 41 210 L 43 212 L 48 214 L 55 219 L 65 224 L 65 179 L 64 178 L 63 171 L 60 164 L 55 158 L 55 157 L 50 152 L 22 133 L 19 132 Z','M 160 22 L 88 64 L 77 74 L 71 84 L 68 94 L 67 140 L 71 158 L 84 175 L 161 221 L 161 201 L 156 188 L 148 180 L 100 152 L 89 140 L 84 127 L 85 111 L 94 95 L 102 88 L 148 62 L 156 54 L 161 42 Z']
def fail(msg): raise AssertionError(msg)
def sha(p): return hashlib.sha256(Path(p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()
def main():
 text=HARNESS.read_text(encoding='utf-8'); method=json.loads(METHOD.read_text(encoding='utf-8')); defaults=json.loads(DEFAULTS.read_text(encoding='utf-8')); m=json.loads(MANIFEST.read_text(encoding='utf-8'))
 if method['status']!='FROZEN_PRE_MATERIALIZATION': fail('method status')
 if defaults['status']!='FROZEN_PRE_SPECIMEN': fail('defaults status')
 if m['status']!='FROZEN_BROWSER_MEASUREMENT_REPAIR_AFTER_INVALID_RUN_NO_DESIGN_RESULT': fail('manifest status')
 files=m['files']; expected={'harness':HARNESS,'static_verifier':Path(__file__),'browser_probe':PROBE,'browser_verifier':BVERIFY,'workflow':WORKFLOW,'method':METHOD,'defaults':DEFAULTS,'c0':C0}
 for k,p in expected.items():
  got=sha(p); want=files[k]['sha256_lf']
  if got!=want: fail(f'hash mismatch {k}: {got} != {want}')
 packet_dir=ROOT/'docs/evidence/packets'
 for fn in PACKETS:
  rec=files['packet_sources'][fn]; got=sha(packet_dir/fn)
  if got!=rec['sha256_lf']: fail(f'packet hash mismatch {fn}')
 if [x['id'] for x in method['composition_variants']]!=VARIANTS: fail('method variants')
 if text.count('data-variant-section=')!=5 or text.count('class="surface ')!=10: fail('variant/surface count')
 for v in VARIANTS:
  if text.count(f'data-variant-section="{v}"')!=1: fail('variant section '+v)
  for c in ('APP','WEB'):
   if text.count(f'id="{v}-{c}"')!=1: fail(f'surface id {v}-{c}')
 if text.count('class="c0"')!=10 or text.count('<path d=')!=30: fail('C0 instance/path count')
 for d in C0_PATHS:
  if text.count(f'd="{d}"')!=10: fail('C0 path drift')
 if sha(C0)!='72cdd4c35928e1fb0bc279b680b9b7a698707dc1564ee800a84840fe61356305': fail('canonical C0 drift')
 low=text.lower()
 for token in ('<img','<canvas','<video','<picture','<object','<embed','<iframe','linear-gradient','radial-gradient','conic-gradient','backdrop-filter','box-shadow:','filter:'):
  if token in low: fail('prohibited source '+token)
 if 'http://' in low or 'https://' in low or 'url(' in low: fail('external resource')
 for forbidden in ('mineral theater','clr-01','kymaean-o3','hero artwork'):
  if forbidden in low: fail('forbidden coupling '+forbidden)
 hexes=set(re.findall(r'#[0-9a-fA-F]{6}',text))
 if hexes!=ALLOWED_HEX: fail(f'palette drift {hexes}')
 compact=re.sub(r'\s+','',text)
 required=['.top-channel{left:9%;top:0;width:30%;height:18px}', '.right-channel{right:0;top:57%;width:24px;height:23%}', '.web.top-channel{height:28px}', '.web.right-channel{width:36px}', '.surface.app{max-width:420px;min-height:340px;padding:18px;--dy:28px;--mark:32px;--slot:44px', '.surface.web{max-width:680px;min-height:390px;padding:24px;--dy:56px;--mark:48px;--slot:60px', '.sample:focus-visible{outline:2pxsolidvar(--ink);outline-offset:2px}', 'padding-inline-start:15px', 'inset-block:7px;inset-inline-start:5px;width:3px', 'inset-inline:9px;bottom:5px;height:3px;width:auto', "constF1A={duration:460,interval:70,easing:'cubic-bezier(0.2,0,0,1)'}", "constCS2={duration:280,easing:'cubic-bezier(0.2,0,0,1)'}", "matchMedia('(prefers-reduced-motion:reduce)')", '@media(forced-colors:active)', '@media(prefers-reduced-motion:reduce)', 'window.__CMP01_API__']
 for token in required:
  if token not in compact: fail('missing frozen token '+token)
 if 'setInterval(' in text or 'setTimeout(' in text: fail('autoplay/timer source')
 if text.count('data-action=')!=30: fail('diagnostic trigger count')
 for v,cls in [('NO_MAT','no-mat'),('NO_SYM','no-sym'),('NO_STA','no-sta'),('NO_MOT','no-mot')]:
  for c in ('app','web'):
   if f'class="surface {c} {cls}"' not in text: fail(f'{v}/{c} class')
 # Normal text uses ink on page/field only; both exceed WCAG normal-text floor.
 def lum(h):
  vals=[int(h[i:i+2],16)/255 for i in (1,3,5)]
  vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals]
  return .2126*vals[0]+.7152*vals[1]+.0722*vals[2]
 def contrast(a,b):
  x,y=lum(a),lum(b); return (max(x,y)+.05)/(min(x,y)+.05)
 min_text=min(contrast('#1b1b19','#f7f7f4'),contrast('#1b1b19','#ecece7'))
 if min_text<4.5: fail('text contrast')
 print('CMP01_STATIC=PASS')
 print('HARNESS_SHA256='+sha(HARNESS))
 print('METHOD_SHA256='+sha(METHOD))
 print('DEFAULTS_SHA256='+sha(DEFAULTS))
 print('C0_SHA256='+sha(C0))
 print(f'MIN_TEXT_CONTRAST={min_text:.4f}')
if __name__=='__main__':
 try: main()
 except Exception as e:
  print('CMP01_STATIC_FAIL:',e,file=sys.stderr); sys.exit(1)
