from pathlib import Path
import hashlib,json,re,sys
R=Path(__file__).resolve().parents[1]
def raw(p): return (R/p).read_bytes()
def lfbytes(p): return raw(p).replace(b'\r\n',b'\n')
def sha(p): return hashlib.sha256(lfbytes(p)).hexdigest()
def load(p): return json.loads((R/p).read_text(encoding='utf-8'))
M=load('docs/evidence/TYP_02_FROZEN_SOURCE_MANIFEST_04.json')
H=(R/'prototypes/typ-02/harness.html').read_text(encoding='utf-8')
D=load('docs/evidence/TYP_02_EXECUTION_DEFAULTS_01.json')
A=load('docs/evidence/TYP_02_EXECUTION_DEFAULTS_ADDENDUM_01.json')
errors=[]
for p,want in M['lf_sha256'].items():
    if sha(p)!=want: errors.append(f'hash mismatch {p}: {sha(p)} != {want}')
if sha('assets/brand/kymaean-threshold-k-working-candidate.svg')!=D['c0_canonical_lf_sha256']:
    errors.append('C0 canonical source hash mismatch')
svg=(R/'assets/brand/kymaean-threshold-k-working-candidate.svg').read_text(encoding='utf-8')
paths=re.findall(r'<path d="([^"]+)"/>',svg)
for p in paths:
    if H.count(f'<path d="{p}"/>')!=10: errors.append('C0 path repetition mismatch')
for f in ['CNEG','F1','F2','F3','F4']:
    if H.count(f'data-family="{f}"')!=1: errors.append(f'family row mismatch {f}')
    for c in ['APP','WEB']:
        if H.count(f'id="{f}-{c}"')!=1: errors.append(f'surface mismatch {f}-{c}')
for k,v in D['content_packet'].items():
    if k=='state_labels':
        for x in v:
            if H.count('>'+x+'</button>')!=10: errors.append(f'state content mismatch {x}')
    elif H.count(v)!=10:
        errors.append(f'content mismatch {k}')
for token in ['@font-face','http://','https://','animation:','transition:','setTimeout','setInterval','requestAnimationFrame']:
    if token in H: errors.append(f'forbidden source token {token}')
if '__TYP02_API__' not in H: errors.append('diagnostic API missing')
for token in ['overflow-wrap:break-word','word-break:normal','hyphens:none']:
    if token not in H: errors.append(f'frozen responsive rule missing {token}')
if H.count('class="mat-top"')!=10 or H.count('class="mat-right"')!=10: errors.append('MAT geometry count mismatch')
if H.count('aria-pressed="true"')!=10: errors.append('selected state count mismatch')
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def ratio(a,b):
    x,y=sorted([lum(a),lum(b)],reverse=True);return (x+.05)/(y+.05)
contrast=ratio(D['neutral_palette']['ink'],D['neutral_palette']['field'])
if contrast<4.5: errors.append(f'contrast {contrast:.4f} below 4.5')
if len(A['browser_modes'])!=8 or len({x['id'] for x in A['browser_modes']})!=8: errors.append('browser mode count/id mismatch')
if set(A['review_modes'])!={'normal-baseline-wide','normal-baseline-320'}: errors.append('review mode set mismatch')
if errors:
    print('TYP02_STATIC=FAIL');print('\n'.join(errors));sys.exit(1)
print('TYP02_STATIC=PASS')
print('HARNESS_SHA256='+sha('prototypes/typ-02/harness.html'))
print('C0_SHA256='+sha('assets/brand/kymaean-threshold-k-working-candidate.svg'))
print(f'MIN_TEXT_CONTRAST={contrast:.4f}')
