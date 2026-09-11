from pathlib import Path
import hashlib,json,re,sys
R=Path(__file__).resolve().parents[1]
def lfbytes(p): return (R/p).read_bytes().replace(b'\r\n',b'\n')
def sha(p): return hashlib.sha256(lfbytes(p)).hexdigest()
def load(p): return json.loads((R/p).read_text(encoding='utf-8'))
H=(R/'prototypes/cmp-02/harness.html').read_text(encoding='utf-8')
errors=[]
METHOD=load('docs/evidence/CMP_02_IDENTITY_STACK_WORDMARK_TYPOGRAPHY_HIERARCHY_METHOD_AND_MATRIX_01.json')
DEFAULTS=load('docs/evidence/CMP_02_EXECUTION_DEFAULTS_01.json')
if METHOD.get('status')!='FROZEN_PRE_SPECIMEN' or METHOD.get('program_id')!='CMP-02': errors.append('method authority mismatch')
if DEFAULTS.get('status')!='FROZEN_PRE_SPECIMEN' or DEFAULTS.get('program_id')!='CMP-02': errors.append('defaults authority mismatch')
if METHOD.get('matrix',{}).get('logical_surfaces')!=12 or METHOD.get('matrix',{}).get('browser_stress_modes')!=8: errors.append('method matrix mismatch')
if len(DEFAULTS.get('browser_modes',[]))!=8: errors.append('defaults browser mode count mismatch')
C0='assets/brand/kymaean-threshold-k-working-candidate.svg';O3='assets/brand/kymaean-o3-wordmark-temporary-incumbent.svg'
C0SHA='72cdd4c35928e1fb0bc279b680b9b7a698707dc1564ee800a84840fe61356305';O3SHA='204e6f7b3239f44267a04afa2c12f0254a56142e9298ee6e7fab9f9061a674f5'
if sha(C0)!=C0SHA: errors.append('C0 canonical hash mismatch')
if sha(O3)!=O3SHA: errors.append('O3 canonical hash mismatch')
if DEFAULTS.get('source_rules',{}).get('exact_c0_lf_sha256')!=C0SHA: errors.append('defaults C0 authority mismatch')
if DEFAULTS.get('source_rules',{}).get('exact_o3_lf_sha256')!=O3SHA: errors.append('defaults O3 authority mismatch')
c0=(R/C0).read_text(encoding='utf-8');o3=(R/O3).read_text(encoding='utf-8')
for d in re.findall(r'<path d="([^"]+)"/>',c0):
    if H.count(f'<path d="{d}"/>')!=1: errors.append('C0 template path mismatch')
for cls,d in re.findall(r'<path class="([^"]+)" d="([^"]+)"/>',o3):
    if H.count(f'<path class="{cls}" d="{d}"/>')!=1: errors.append('O3 template path mismatch')
for rule in ['.v{fill:none;stroke:currentColor;stroke-width:5.9;stroke-linecap:round;stroke-linejoin:round}', '.d{fill:none;stroke:currentColor;stroke-width:5.35;stroke-linecap:round;stroke-linejoin:round}', '.h{fill:none;stroke:currentColor;stroke-width:4.55;stroke-linecap:round;stroke-linejoin:round}', '.fine{fill:none;stroke:currentColor;stroke-width:2.35;stroke-linecap:round;stroke-linejoin:round;opacity:.7}']:
    if H.count(rule)!=1: errors.append('O3 template stroke rule mismatch '+rule[:8])
for token in ["['APP_COMPACT','App compact','app','PRIMARY SCOPE']","['WEB_HEADER','Website header','web','OVERVIEW   DETAILS']","['ACQUISITION_PRELUDE','Acquisition / prelude','acq','']","const VARS=['FULL','NEUTRAL_TYP','O3_SOLO','NO_O3']"]:
    if token not in H: errors.append('role/variant generator token missing '+token)
for text in ['Kymaean','CONTEXT','Primary information remains clear.','Supporting text explains the situation without changing the hierarchy.','Secondary detail remains available.','Field A','Field B','Field C']:
    if text not in H: errors.append('content token missing '+text)
for token in ['@font-face','http://','https://','animation:','transition:','setTimeout','setInterval','requestAnimationFrame','linear-gradient','radial-gradient','backdrop-filter','<canvas','WebGL']:
    if token in H: errors.append('forbidden source token '+token)
for token in ['__CMP02_API__','overflow-wrap:break-word','word-break:normal','hyphens:none','html.spacing-stress','html.spacing-stress .type-zone>*+*','@media(forced-colors:active)','min-height:44px','outline:2px solid currentColor','outline-offset:2px','pathCount:q(\'.c0\').querySelectorAll(\'path\').length','pathCount:q(\'.o3\').querySelectorAll(\'path\').length']:
    if token not in H: errors.append('required source token missing '+token)
if 'OVERVIEW · DETAILS' in H: errors.append('unfrozen WEB scope separator present')
M=load('docs/evidence/CMP_02_FROZEN_SOURCE_MANIFEST_02.json')
for fp,want in M['lf_sha256'].items():
    got=sha(fp)
    if got!=want: errors.append(f'manifest hash mismatch {fp}: {got} != {want}')
if M.get('harness_sha256')!=sha('prototypes/cmp-02/harness.html'): errors.append('manifest harness SHA mismatch')
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)];c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c];return .2126*c[0]+.7152*c[1]+.0722*c[2]
def ratio(a,b):
    x,y=sorted([lum(a),lum(b)],reverse=True);return (x+.05)/(y+.05)
contrast=ratio('#1b1b19','#ecece7')
if contrast<4.5: errors.append(f'contrast {contrast:.4f} below 4.5')
if errors:
    print('CMP02_STATIC=FAIL');print('\n'.join(errors));sys.exit(1)
print('CMP02_STATIC=PASS');print('HARNESS_SHA256='+sha('prototypes/cmp-02/harness.html'));print('C0_SHA256='+sha(C0));print('O3_SHA256='+sha(O3));print(f'MIN_TEXT_CONTRAST={contrast:.4f}')
