#!/usr/bin/env python3
import argparse, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/'prototypes/state-s1/harness.html'
METHOD=ROOT/'docs/evidence/STATE_S1_STATIC_STATE_SALIENCE_METHOD_AND_MATRIX_01.json'
PROBE=ROOT/'tools/state_s1_browser_probe.mjs'
FAMILIES=('CREF','CNEG','F1','F2','F3','F4')
STATES=('REST','LISTENING','CURRENT_OPPORTUNITY','SPEAKING')

def sha256(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def die(msg):
    print('FAIL:',msg,file=sys.stderr)
    raise SystemExit(1)
def extract_defs(src):
    m=re.search(r'<script type="application/json" id="state-s1-definitions">\s*(\{.*?\})\s*</script>',src,re.S)
    if not m: die('embedded definitions missing')
    return json.loads(m.group(1))
def is_gray_hex(v):
    v=v.lstrip('#')
    if len(v)==3: v=''.join(c*2 for c in v)
    return len(v)==6 and v[0:2].lower()==v[2:4].lower()==v[4:6].lower()

def static_checks(method,allow_pending=False):
    src=HARNESS.read_text(encoding='utf-8'); actual=sha256(HARNESS); expected=method['source_freeze']['harness_sha256']
    if expected=='PENDING_PRE_EXPOSURE_FREEZE':
        if not allow_pending: die('harness hash still pending')
    elif actual!=expected: die('harness sha256 mismatch')
    if not PROBE.exists(): die('browser probe missing')
    d=extract_defs(src)
    if tuple(d['families'])!=FAMILIES: die('family ids/order mismatch')
    g=method['incumbent_geometry_control']
    if d['viewBox']!=g['viewbox']: die('viewBox mismatch')
    if d['geometry']!=g['character_geometry']: die('incumbent geometry mismatch')
    if d['patterns']!={str(k):v for k,v in method['matrix']['state_patterns'].items()}: die('state pattern mismatch')
    c=method['neutral_shared_constants']
    if d['falloff']!=c['beam_falloff'] or d['blur']!=c['beam_blur_px']: die('fixed beam optics mismatch')
    if d['textureAlpha']!=c['texture_alpha'] or d['poolAlpha']!=c['floor_pool_alpha']: die('fixed texture/pool mismatch')
    for fid in FAMILIES:
        f=d['families'][fid]; mf=method['families'][fid]
        for state in STATES:
            pair=f[state]; target=[mf[state]['envelope_alpha'],mf[state]['core_alpha']]
            if pair!=target: die(f'{fid} {state} signature mismatch')
            if pair[0]<=.35: die(f'{fid} {state} violates presence floor')
        unique=len({tuple(f[s]) for s in STATES})
        if fid=='CNEG' and unique!=1: die('CNEG must remain flat')
        if fid!='CNEG' and unique!=4: die(f'{fid} state signatures not unique')
    if re.search(r'\b(animation|transition)\s*:',src,re.I): die('animation/transition authored')
    if '@media(forced-colors:active)' not in src: die('forced-colors fallback missing')
    bad=[h for h in re.findall(r'#[0-9a-fA-F]{3,6}\b',src) if not is_gray_hex(h)]
    if bad: die(f'non-gray hex colors: {bad}')
    if set(d['patterns'])!={'2','3','4','5'}: die('character-count pattern set mismatch')
    allowed=set(STATES)
    for rows in d['patterns'].values():
        for _,state in rows:
            if state not in allowed: die(f'forbidden state in matrix: {state}')
    return {'harness_sha256':actual,'families':6,'candidate_families':4,'states':list(STATES),'specimens':24,'cones':84,'source_status':'PASS'}

def check_diag(path,forced,width):
    d=json.loads(Path(path).read_text(encoding='utf-8'))
    if d.get('schema')!='kymaean.state-s1.browser-diagnostic.v1': die(f'{path}: schema mismatch')
    expected={'families':6,'specimens':24,'cones':84,'names':84,'stateLabels':84}
    for k,v in expected.items():
        if d.get(k)!=v: die(f'{path}: {k} {d.get(k)} != {v}')
    if bool(d.get('forcedColors'))!=forced: die(f'{path}: forced-colors mismatch')
    vp=d.get('viewport',{})
    if vp.get('innerWidth')!=width: die(f'{path}: viewport width mismatch {vp}')
    if vp.get('scrollWidth',width)>width: die(f'{path}: horizontal overflow {vp}')
    for key in ('geometryInvariantFailures','signatureFailures','presenceFailures','labelVisibilityFailures'):
        if d.get(key)!=[]: die(f'{path}: {key}={d.get(key)}')
    visible=d.get('decorativeBeamsVisible')
    if forced and visible!=0: die(f'{path}: decorative beams visible in forced colors: {visible}')
    if not forced and visible!=84: die(f'{path}: normal beams missing: {visible}')
    return {'mode':'FORCED_COLORS_FALLBACK' if forced else 'NORMAL_NEUTRAL','viewport_width':width,'scroll_width':vp.get('scrollWidth'),'status':'PASS'}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--allow-pending-hash',action='store_true')
    ap.add_argument('--normal-wide'); ap.add_argument('--forced-wide'); ap.add_argument('--normal-320'); ap.add_argument('--forced-320')
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty'); ap.add_argument('--output')
    a=ap.parse_args(); method=json.loads(METHOD.read_text(encoding='utf-8'))
    result={'schema':'kymaean.state-s1.structural-preflight.v1','program_id':'STATE-S1','status':'STATIC_ONLY','static':static_checks(method,a.allow_pending_hash)}
    supplied=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    if any(supplied):
        if not all(supplied): die('all four browser diagnostics are required')
        checks=[check_diag(a.normal_wide,False,1200),check_diag(a.forced_wide,True,1200),check_diag(a.normal_320,False,320),check_diag(a.forced_320,True,320)]
        result.update({'status':'CLEAN_BROWSER_PREFLIGHT_NO_SUBJECTIVE_RESULT','browser_version':a.browser_version,'os_pretty':a.os_pretty,'browser_checks':checks,'failures':[]})
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
