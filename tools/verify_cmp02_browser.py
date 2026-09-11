from pathlib import Path
import argparse, json, re, hashlib, sys
R=Path(__file__).resolve().parents[1]

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def repo(p): return json.loads((R/p).read_text(encoding='utf-8'))
def num(s):
    m=re.match(r'[-+]?\d*\.?\d+',str(s))
    return float(m.group()) if m else 0.0
def lfsha(p): return hashlib.sha256((R/p).read_bytes().replace(b'\r\n',b'\n')).hexdigest()

def close(a,b,t=1.0): return abs(float(a)-float(b))<=t

ap=argparse.ArgumentParser()
ap.add_argument('--diagnostics-dir',required=True)
ap.add_argument('--browser-version',required=True)
ap.add_argument('--os-pretty',required=True)
ap.add_argument('--output',required=True)
args=ap.parse_args()
D=repo('docs/evidence/CMP_02_EXECUTION_DEFAULTS_01.json')
root=Path(args.diagnostics_dir); errors=[]; summaries={}
ROLES=['APP_COMPACT','WEB_HEADER','ACQUISITION_PRELUDE']; VARS=['FULL','NEUTRAL_TYP','O3_SOLO','NO_O3']
ORDER=[f'{r}/{v}' for r in ROLES for v in VARS]
ROLE_C0={'APP_COMPACT':28,'WEB_HEADER':32,'ACQUISITION_PRELUDE':64}
ROLE_O3={'APP_COMPACT':130,'WEB_HEADER':160,'ACQUISITION_PRELUDE':340}

def expected_heading(role,var,width,fontp):
    neutral=var=='NEUTRAL_TYP'
    rem=(1.15 if neutral else 1.35) if width<=520 else (1.25 if neutral else 1.50)
    return 16*(fontp/100)*rem

for m in D['browser_modes']:
    mid=m['id']; p=root/(mid+'.json')
    if not p.exists(): errors.append(f'{mid}: diagnostic missing'); continue
    x=load(p); width=m['width']; fontp=m['root_font_percent']; spacing=m['text_spacing']; forced=m['forced_colors']
    req={'width':width,'forced':forced,'fontPercent':fontp,'spacing':spacing}
    if x.get('requested')!=req: errors.append(f'{mid}: requested mismatch {x.get("requested")}')
    if x.get('viewport',{}).get('innerWidth')!=width: errors.append(f'{mid}: viewport width mismatch {x.get("viewport")}')
    if x.get('viewport',{}).get('scrollWidth',999)>width+1: errors.append(f'{mid}: document overflow {x.get("viewport")}')
    if bool(x.get('forced'))!=forced: errors.append(f'{mid}: forced-colors mismatch {x.get("forced")}')
    if bool(x.get('spacing'))!=spacing: errors.append(f'{mid}: spacing mismatch {x.get("spacing")}')
    expected_root=16*(fontp/100)
    if abs(num(x.get('rootFont','0'))-expected_root)>.3: errors.append(f'{mid}: root font mismatch {x.get("rootFont")}')
    if x.get('surfaceCount')!=12: errors.append(f'{mid}: surface count {x.get("surfaceCount")}')
    if x.get('order')!=ORDER: errors.append(f'{mid}: surface order mismatch')
    if x.get('overflowElements'): errors.append(f'{mid}: overflow elements {x["overflowElements"][:5]}')
    ss=x.get('surfaces',[])
    if len(ss)!=12: errors.append(f'{mid}: surface payload count {len(ss)}')
    by={(s.get('role'),s.get('variant')):s for s in ss}
    for role in ROLES:
      for var in VARS:
        s=by.get((role,var))
        if not s: errors.append(f'{mid}:{role}/{var}: missing surface'); continue
        sid=s['id']; r=s['rect']
        if s['scrollWidth']>s['clientWidth']+1: errors.append(f'{mid}:{sid}: surface overflow')
        if s.get('brandNames')!=['Kymaean']: errors.append(f'{mid}:{sid}: accessible brand name mismatch {s.get("brandNames")}')
        want_c0_hidden=var=='O3_SOLO'; want_o3_hidden=var=='NO_O3'
        if (s['c0']['visibility']=='hidden')!=want_c0_hidden: errors.append(f'{mid}:{sid}: C0 visibility mismatch')
        if (s['o3']['visibility']=='hidden')!=want_o3_hidden: errors.append(f'{mid}:{sid}: O3 visibility mismatch')
        if s['c0'].get('pathCount')!=3: errors.append(f'{mid}:{sid}: C0 path count {s["c0"].get("pathCount")}')
        if s['o3'].get('pathCount')!=19: errors.append(f'{mid}:{sid}: O3 path count {s["o3"].get("pathCount")}')
        if not close(s['c0']['rect']['height'],ROLE_C0[role],1.0): errors.append(f'{mid}:{sid}: C0 height {s["c0"]["rect"]["height"]}')
        if role!='ACQUISITION_PRELUDE' and not close(s['o3']['rect']['width'],ROLE_O3[role],1.5): errors.append(f'{mid}:{sid}: O3 width {s["o3"]["rect"]["width"]}')
        if role=='ACQUISITION_PRELUDE' and not (0 < s['o3']['rect']['width'] <= ROLE_O3[role]+1): errors.append(f'{mid}:{sid}: acquisition O3 width {s["o3"]["rect"]["width"]}')
        for g in (s['c0']['rect'],s['o3']['rect']):
            if g['left']<r['left']-1 or g['right']>r['right']+1: errors.append(f'{mid}:{sid}: identity geometry outside surface')
        for t in s.get('text',[]):
            if t['scrollWidth']>t['clientWidth']+1: errors.append(f'{mid}:{sid}: text overflow {t["text"]}')
            if spacing:
                if num(t['lineHeight']) < num(t['fontSize'])*1.49: errors.append(f'{mid}:{sid}:{t["text"]}: spacing line-height floor')
                if num(t['letterSpacing']) < num(t['fontSize'])*.115: errors.append(f'{mid}:{sid}:{t["text"]}: letter-spacing floor')
                if num(t.get('wordSpacing','0')) < num(t['fontSize'])*.155: errors.append(f'{mid}:{sid}:{t["text"]}: word-spacing floor')
        heading=next((t for t in s.get('text',[]) if 'heading' in str(t.get('cls','')).split()),None)
        if not heading: errors.append(f'{mid}:{sid}: missing heading metric')
        else:
            expected=expected_heading(role,var,width,fontp)
            if not close(num(heading['fontSize']),expected,.8): errors.append(f'{mid}:{sid}: heading {heading["fontSize"]} expected {expected}')
        buttons=s.get('buttons',[])
        scopes=[t['text'] for t in s.get('text',[]) if 'scope-label' in str(t.get('cls','')).split()]
        expected_scope={'APP_COMPACT':['PRIMARY SCOPE'],'WEB_HEADER':['OVERVIEW   DETAILS'],'ACQUISITION_PRELUDE':[]}[role]
        if scopes!=expected_scope: errors.append(f'{mid}:{sid}: scope text mismatch {scopes}')
        if len(buttons)!=3 or [b['text'] for b in buttons]!=['Field A','Field B','Field C']: errors.append(f'{mid}:{sid}: buttons mismatch')
        sel=[b for b in buttons if b['selected']]
        if len(sel)!=1 or sel[0]['text']!='Field B' or sel[0]['pressed']!='true': errors.append(f'{mid}:{sid}: selected state mismatch')
        wit=s['selectedWitness']
        if role=='APP_COMPACT':
            if not close(num(wit['width']),3,.6): errors.append(f'{mid}:{sid}: APP witness width {wit}')
        else:
            if not close(num(wit['height']),3,.6): errors.append(f'{mid}:{sid}: WEB witness height {wit}')
        state_rects=[b['rect'] for b in buttons if b.get('rect')]
        if len(state_rects)!=3: errors.append(f'{mid}:{sid}: state rect count {len(state_rects)}')
        else:
            tops=[round(q['top'],1) for q in state_rects]
            if width<=520:
                if not (tops[0]<tops[1]<tops[2]): errors.append(f'{mid}:{sid}: state not one-column')
            elif max(tops)-min(tops)>1.0: errors.append(f'{mid}:{sid}: state not three-column')
    k=[z for z in x.get('keyboardFocus',[]) if z and z.get('surface')]
    if len(k)!=36: errors.append(f'{mid}: keyboard focus count {len(k)}')
    for s in ss:
        hits=[z for z in k if z.get('surface')==s['id']]
        if len(hits)!=3: errors.append(f'{mid}:{s["id"]}: keyboard hits {len(hits)}')
        selected=[z for z in hits if z.get('selected')]
        if len(selected)!=1: errors.append(f'{mid}:{s["id"]}: selected focus hits {len(selected)}')
        else:
            z=selected[0]
            if not z.get('focusVisible') or z.get('outlineStyle')=='none': errors.append(f'{mid}:{s["id"]}: focus-visible missing')
            if z.get('outlineWidth')!='2px': errors.append(f'{mid}:{s["id"]}: outline width {z.get("outlineWidth")}')
    summaries[mid]={'width':width,'forced_colors':forced,'root_font_percent':fontp,'text_spacing':spacing,'surface_count':len(ss),'overflow_count':len(x.get('overflowElements',[])),'keyboard_focus_count':len(k)}

if errors:
    print('CMP02_BROWSER=FAIL'); print('\n'.join(errors[:160])); sys.exit(1)
out={
 'schema':'kymaean.cmp02.browser-preflight.v1',
 'status':'PASS_COMPLETE_8_MODE_MATRIX',
 'date':'2026-09-11',
 'source_manifest':'docs/evidence/CMP_02_FROZEN_SOURCE_MANIFEST_01.json',
 'harness_sha256':lfsha('prototypes/cmp-02/harness.html'),
 'browser_verifier_sha256':hashlib.sha256(Path(__file__).read_bytes().replace(b'\r\n',b'\n')).hexdigest(),
 'browser_version':args.browser_version,
 'os_pretty':args.os_pretty,
 'modes':summaries,
 'mechanical_findings':[
   'Twelve-surface APP_COMPACT / WEB_HEADER / ACQUISITION_PRELUDE matrix preserved across all eight frozen modes.',
   'No horizontal document or required-content overflow under baseline, 200% resize, text-spacing stress, or forced-colors.',
   'Exactly one accessible Kymaean identity name remains per surface while C0/O3 visual diagnostics preserve their frozen slots.',
   'STA F2 selected witness and real keyboard focus coexist across all twelve surfaces.',
   'FULL and diagnostic typography/identity geometry remain within frozen role dimensions and responsive rules.'
 ],
 'scope':'Mechanical/source/layout/accessibility validation only. Subjective CMP-02 review is separate.'
}
Path(args.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print('CMP02_BROWSER=PASS_COMPLETE_8_MODE_MATRIX')
print('HARNESS_SHA256='+out['harness_sha256'])
