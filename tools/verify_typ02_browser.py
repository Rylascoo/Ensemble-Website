from pathlib import Path
import argparse,json,re,hashlib,sys
R=Path(__file__).resolve().parents[1]
def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def repo(p): return json.loads((R/p).read_text(encoding='utf-8'))
def num(s): return float(re.match(r'[-+]?\d*\.?\d+',str(s)).group())
def lfsha(p): return hashlib.sha256((R/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()
def parse(v):
    a=v.split('/'); return float(a[0].replace('rem','')),int(a[1]),float(a[2])
ap=argparse.ArgumentParser();ap.add_argument('--diagnostics-dir',required=True);ap.add_argument('--browser-version',required=True);ap.add_argument('--os-pretty',required=True);ap.add_argument('--output',required=True);args=ap.parse_args()
D=repo('docs/evidence/TYP_02_EXECUTION_DEFAULTS_01.json');A=repo('docs/evidence/TYP_02_EXECUTION_DEFAULTS_ADDENDUM_01.json')
root=Path(args.diagnostics_dir); errors=[]; summaries={}
fams=['CNEG','F1','F2','F3','F4']; contexts=['APP','WEB']
for m in A['browser_modes']:
    mid=m['id']; p=root/(mid+'.json')
    if not p.exists(): errors.append(f'{mid}: diagnostic missing'); continue
    x=load(p); width=m['width']; fontp=m['root_font_percent']; spacing=m['text_spacing']; forced=m['forced_colors']
    if x.get('requested')!={'width':width,'forced':forced,'fontPercent':fontp,'spacing':spacing}: errors.append(f'{mid}: requested mode mismatch {x.get("requested")}')
    if x.get('viewport',{}).get('width')!=width: errors.append(f'{mid}: viewport width mismatch')
    if bool(x.get('forced'))!=forced: errors.append(f'{mid}: forced-colors mismatch')
    if bool(x.get('spacing'))!=spacing: errors.append(f'{mid}: spacing flag mismatch')
    expected_root=16*(fontp/100)
    if abs(num(x.get('rootFont','0'))-expected_root)>.25: errors.append(f'{mid}: root font mismatch {x.get("rootFont")}')
    if x.get('document',{}).get('scrollWidth',999)>x.get('document',{}).get('clientWidth',0)+1: errors.append(f'{mid}: document horizontal overflow')
    if x.get('overflowElements'): errors.append(f'{mid}: overflow elements present {x["overflowElements"][:3]}')
    surfaces=x.get('surfaces',[])
    ids={s.get('id') for s in surfaces}
    expected_ids={f'{f}-{c}' for f in fams for c in contexts}
    if ids!=expected_ids: errors.append(f'{mid}: surface id set mismatch')
    for s in surfaces:
        f=s['family']; c=s['context']; fv=D['family_vectors'][f]; roles=s['roles']; scale=expected_root
        for role in ['eyebrow','heading','body','support']:
            rem,wt,lh=parse(fv[role]); expected_rem=rem
            if role=='heading' and width<=520: expected_rem=float(D['responsive_rules']['narrow_heading_rem'][f])
            fs=expected_rem*scale
            if abs(num(roles[role]['fontSize'])-fs)>.35: errors.append(f'{mid}:{s["id"]}:{role} font-size mismatch')
            if int(roles[role]['fontWeight'])!=wt: errors.append(f'{mid}:{s["id"]}:{role} weight mismatch')
            if roles[role]['scrollWidth']>roles[role]['clientWidth']+1: errors.append(f'{mid}:{s["id"]}:{role} horizontal text overflow')
            if spacing:
                if num(roles[role]['lineHeight'])<num(roles[role]['fontSize'])*1.49: errors.append(f'{mid}:{s["id"]}:{role} spacing line-height floor')
                if num(roles[role]['letterSpacing'])<num(roles[role]['fontSize'])*.115: errors.append(f'{mid}:{s["id"]}:{role} letter-spacing stress floor')
                if num(roles[role]['wordSpacing'])<num(roles[role]['fontSize'])*.155: errors.append(f'{mid}:{s["id"]}:{role} word-spacing stress floor')
            else:
                if abs(num(roles[role]['lineHeight'])-fs*lh)>.6: errors.append(f'{mid}:{s["id"]}:{role} line-height mismatch')
        st=s['states']; tops=[round(q['top'],1) for q in st]
        if width<=520:
            if not (tops[0]<tops[1]<tops[2]): errors.append(f'{mid}:{s["id"]}: state zone not one-column')
        else:
            if max(tops)-min(tops)>1: errors.append(f'{mid}:{s["id"]}: state zone not three-column')
        w=s['selectedWitness']
        if c=='APP' and abs(num(w['width'])-3)>.6: errors.append(f'{mid}:{s["id"]}: APP witness width mismatch')
        if c=='WEB' and abs(num(w['height'])-3)>.6: errors.append(f'{mid}:{s["id"]}: WEB witness height mismatch')
        if len(s.get('c0Paths',[]))!=3: errors.append(f'{mid}:{s["id"]}: C0 path count mismatch')
    focused={q.get('surface') for q in x.get('keyboardFocus',[]) if q and q.get('selected') and q.get('focusVisible') and num(q.get('outlineWidth','0'))>=1.9}
    if focused!=expected_ids: errors.append(f'{mid}: selected keyboard focus coverage mismatch {sorted(focused)}')
    summaries[mid]={'width':width,'forced_colors':forced,'root_font_percent':fontp,'text_spacing':spacing,'surface_count':len(surfaces),'overflow_count':len(x.get('overflowElements',[])),'selected_focus_surface_count':len(focused)}
if errors:
    print('TYP02_BROWSER=FAIL'); print('\n'.join(errors[:120])); sys.exit(1)
out={'schema':'kymaean.typ02.browser-preflight.v1','status':'PASS_COMPLETE_8_MODE_MATRIX','date':'2026-09-11','source_manifest':'docs/evidence/TYP_02_FROZEN_SOURCE_MANIFEST_01.json','harness_sha256':lfsha('prototypes/typ-02/harness.html'),'browser_verifier_sha256':hashlib.sha256(Path(__file__).read_bytes().replace(b'\r\n',b'\n')).hexdigest(),'browser_version':args.browser_version,'os_pretty':args.os_pretty,'modes':summaries,'mechanical_findings':['Five-family APP/WEB matrix preserved across all eight frozen modes.','No horizontal document/text overflow under baseline, 200% resize, text-spacing stress, or forced-colors.','Selected-state witness and real keyboard focus coexist across all ten surfaces.','Candidate role vectors and shared responsive heading map match frozen execution defaults.'],'scope':'Mechanical/source/layout/accessibility validation only. Subjective TYP-02 review is separate.'}
Path(args.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print('TYP02_BROWSER=PASS_COMPLETE_8_MODE_MATRIX')
print('HARNESS_SHA256='+out['harness_sha256'])
