#!/usr/bin/env python3
import argparse, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/'prototypes/cir-s1/harness.html'
METHOD=ROOT/'docs/evidence/CIR_S1_STAGE_REDUNDANT_IDENTITY_CUE_METHOD_AND_MATRIX_01.json'
PROBE=ROOT/'tools/cir_s1_browser_probe.mjs'
FAMILIES=('cneg','cinc','f1','f2','f3','f4')
CHARS=('marlowe','voss','wren','iona','keir')

def sha256(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def die(msg):
    print('FAIL:',msg,file=sys.stderr)
    raise SystemExit(1)

def definitions(src):
    m=re.search(r'<script type="application/json" id="cir-s1-definitions">\s*(\{.*?\})\s*</script>',src,re.S)
    if not m: die('embedded definitions missing')
    return json.loads(m.group(1))

def static_checks(method):
    src=HARNESS.read_text(encoding='utf-8')
    actual=sha256(HARNESS)
    if actual!=method['source_freeze']['harness_sha256']: die('harness sha256 mismatch')
    if not PROBE.exists(): die('browser probe missing')
    d=definitions(src)
    chars=tuple(c['id'] for c in d['characters'])
    if chars!=CHARS: die(f'character ids mismatch {chars}')
    if tuple(d['families'])!=FAMILIES: die(f'family ids/order mismatch {tuple(d["families"])}')
    if [c['name'] for c in d['characters']] != method['controlled_characters']: die('controlled names mismatch')
    for fid in FAMILIES:
        glyphs=d['families'][fid]['glyphs']
        if tuple(glyphs)!=CHARS: die(f'{fid} glyph character order mismatch')
        vals=list(glyphs.values())
        unique=len(set(vals))
        expected=1 if fid=='cneg' else 5
        if unique!=expected: die(f'{fid} unique glyph count {unique} != {expected}')
        for cid,g in glyphs.items():
            low=g.lower()
            if '<text' in low or 'aria-' in low or 'style=' in low: die(f'{fid}/{cid} forbidden semantic/style content')
            if re.search(r'#[0-9a-f]{3,8}|rgb\(|hsl\(',low): die(f'{fid}/{cid} authored color found')
    for cid,g in d['families']['f1']['glyphs'].items():
        if g.count('<path')!=1 or 'Z' not in g: die(f'f1/{cid} contour grammar mismatch')
    for fid in ('f2','f3'):
        for cid,g in d['families'][fid]['glyphs'].items():
            if g.count('<path')!=2: die(f'{fid}/{cid} two-part grammar mismatch')
    for cid,g in d['families']['f4']['glyphs'].items():
        if g.count('<path')!=1 or "fill-rule='evenodd'" not in g: die(f'f4/{cid} aperture grammar mismatch')
    if '@media(forced-colors:active)' not in src: die('forced-colors compatibility rule missing')
    if 'currentColor' not in src: die('currentColor cue paint law missing')
    if 'window.__CIR_S1_DIAGNOSTIC__' not in src: die('browser diagnostic missing')
    if method['matrix']['sizes_css_px'] != [12,16,20,24,32]: die('size matrix mismatch')
    if method['matrix']['state_conditions'] != ['REST','LISTENING','SELECTED','CURRENT_OPPORTUNITY','SPEAKING']: die('state matrix mismatch')
    return {'harness_sha256':actual,'families':6,'candidate_families':4,'characters':5,'source_status':'PASS'}

def check_diag(path,forced,width):
    d=json.loads(Path(path).read_text(encoding='utf-8'))
    if d.get('schema')!='kymaean.cir-s1.browser-diagnostic.v1': die(f'{path}: schema mismatch')
    if d.get('families')!=6: die(f'{path}: family count mismatch')
    if d.get('cues') is None or len(d['cues'])!=450: die(f'{path}: cue count mismatch')
    if d.get('stateCards')!=150: die(f'{path}: state-card count mismatch')
    if d.get('reduced')!=30: die(f'{path}: reduced-name count mismatch')
    expected_unique={'cneg':1,'cinc':5,'f1':5,'f2':5,'f3':5,'f4':5}
    for fid,n in expected_unique.items():
        got=d.get('familyDistinctness',{}).get(fid,{})
        if got.get('unique')!=n or got.get('total')!=5: die(f'{path}: {fid} distinctness mismatch {got}')
    if d.get('geometryInvariantFailures')!=[]: die(f'{path}: cue geometry mutated {d.get("geometryInvariantFailures")}')
    if bool(d.get('forcedColors'))!=forced: die(f'{path}: forced-colors mismatch')
    vp=d.get('viewport',{})
    if vp.get('innerWidth')!=width: die(f'{path}: viewport width {vp.get("innerWidth")} != {width}')
    if vp.get('scrollWidth',width)>width: die(f'{path}: horizontal document overflow {vp}')
    narrow=d.get('narrow',[])
    if len(narrow)!=6: die(f'{path}: narrow-frame count mismatch')
    for item in narrow:
        if item.get('scrollWidth',0)>item.get('clientWidth',0)+1: die(f'{path}: narrow overflow {item}')
    zero=[x for x in d['cues'] if x.get('width',0)<=0 or x.get('height',0)<=0]
    if zero: die(f'{path}: zero-size cue(s)')
    return {'mode':'FORCED_COLORS' if forced else 'NORMAL','viewport_width':width,'scroll_width':vp.get('scrollWidth'),'cue_count':len(d['cues']),'status':'PASS'}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--normal-wide'); ap.add_argument('--forced-wide')
    ap.add_argument('--normal-320'); ap.add_argument('--forced-320')
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty'); ap.add_argument('--output')
    a=ap.parse_args()
    method=json.loads(METHOD.read_text(encoding='utf-8'))
    result={'schema':'kymaean.cir-s1.structural-accessibility-preflight.v1','program_id':'CIR-S1','status':'STATIC_ONLY','static':static_checks(method)}
    supplied=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    if any(supplied):
        if not all(supplied): die('all four browser diagnostics are required')
        checks=[check_diag(a.normal_wide,False,1200),check_diag(a.forced_wide,True,1200),check_diag(a.normal_320,False,320),check_diag(a.forced_320,True,320)]
        result.update({'status':'CLEAN_BROWSER_PREFLIGHT_NO_SUBJECTIVE_RESULT','browser_version':a.browser_version,'os_pretty':a.os_pretty,'browser_checks':checks,'failures':[]})
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
