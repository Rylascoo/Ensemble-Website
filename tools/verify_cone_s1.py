#!/usr/bin/env python3
import argparse, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/'prototypes/cone-s1/harness.html'
METHOD=ROOT/'docs/evidence/CONE_S1_STAGE_OPTICAL_HIERARCHY_METHOD_AND_MATRIX_01.json'
PROBE=ROOT/'tools/cone_s1_browser_probe.mjs'
FAMILIES=('CREF','CNEG','F1','F2','F3','F4')

def sha256(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def die(msg):
    print('FAIL:',msg,file=sys.stderr)
    raise SystemExit(1)
def extract_defs(src):
    m=re.search(r'<script type="application/json" id="cone-s1-definitions">\s*(\{.*?\})\s*</script>',src,re.S)
    if not m: die('embedded definitions missing')
    return json.loads(m.group(1))
def is_gray_hex(v):
    v=v.lstrip('#')
    if len(v)==3: v=''.join(c*2 for c in v)
    return len(v)==6 and v[0:2].lower()==v[2:4].lower()==v[4:6].lower()

def static_checks(method):
    src=HARNESS.read_text(encoding='utf-8'); actual=sha256(HARNESS)
    if actual!=method['source_freeze']['harness_sha256']: die('harness sha256 mismatch')
    if not PROBE.exists(): die('browser probe missing')
    d=extract_defs(src)
    if tuple(d['families'])!=FAMILIES: die('family ids/order mismatch')
    if d['counts']!=method['matrix']['character_counts']: die('character counts mismatch')
    if d['centers']!={str(k):v for k,v in method['matrix']['wide_centers_pct'].items()}: die('center matrix mismatch')
    if d['stageHeight']!=method['matrix']['stage_height_px'] or d['opticalTop']!=method['matrix']['optical_zone_top_px'] or d['floorBottom']!=method['matrix']['shared_floor_bottom_px']: die('stage coordinate mismatch')
    for fid in FAMILIES:
        a=d['families'][fid]; b=method['families'][fid]
        pairs=(('width','envelope_width_pct_stage'),('height','height_pct_optical_zone'),('top','top_aperture_pct_envelope'),('base','base_aperture_pct_envelope'),('blur','blur_px'))
        for ek,mk in pairs:
            if a[ek]!=b[mk]: die(f'{fid} {ek} mismatch')
        if a['falloff']!=b['falloff']: die(f'{fid} falloff mismatch')
    if d['names']!=method['neutral_shared_constants']['names']: die('name list mismatch')
    if d['poolWidth']!=method['neutral_shared_constants']['floor_pool_width_pct_stage']: die('pool width mismatch')
    if d['poolHeight']!=method['neutral_shared_constants']['floor_pool_height_px']: die('pool height mismatch')
    if d['poolBlur']!=method['neutral_shared_constants']['floor_pool_blur_px']: die('pool blur mismatch')
    if d['poolAlpha']!=method['neutral_shared_constants']['floor_pool_peak_alpha']: die('pool alpha mismatch')
    if re.search(r'\b(animation|transition)\s*:',src,re.I): die('animation/transition authored')
    for word in ('opportunity','speaking','listening','selected','performing','take a seat'):
        if word in src.lower(): die(f'forbidden state-specific term in harness: {word}')
    if '@media(forced-colors:active)' not in src: die('forced-colors fallback missing')
    hexes=re.findall(r'#[0-9a-fA-F]{3,6}\b',src)
    bad=[h for h in hexes if not is_gray_hex(h)]
    if bad: die(f'non-gray hex color(s): {bad}')
    rgba=re.findall(r'rgba\(([^)]*)\)',src,re.I)
    for body in rgba:
        nums=[x.strip() for x in body.split(',')]
        if nums[:3]!=['255','255','255']: die(f'non-neutral rgba: {body}')
    return {'harness_sha256':actual,'families':6,'candidate_families':4,'character_counts':[2,3,4,5],'source_status':'PASS'}
def check_diag(path,forced,width):
    d=json.loads(Path(path).read_text(encoding='utf-8'))
    if d.get('schema')!='kymaean.cone-s1.browser-diagnostic.v1': die(f'{path}: schema mismatch')
    expected={'families':6,'specimens':24,'cones':84,'names':84,'restLabels':84}
    for k,v in expected.items():
        if d.get(k)!=v: die(f'{path}: {k} {d.get(k)} != {v}')
    if bool(d.get('forcedColors'))!=forced: die(f'{path}: forced-colors mismatch')
    vp=d.get('viewport',{})
    if vp.get('innerWidth')!=width: die(f'{path}: viewport width mismatch {vp}')
    if vp.get('scrollWidth',width)>width: die(f'{path}: horizontal overflow {vp}')
    if d.get('geometryInvariantFailures')!=[]: die(f'{path}: family geometry mutation')
    family_failures={fid:[] for fid in FAMILIES}
    if not forced:
        for item in d.get('clipFailures',[]): family_failures[item['fid']].append('CLIP')
        for item in d.get('nameOverlapFailures',[]): family_failures[item['fid']].append('NAME_COLLISION')
        ov=d.get('overlapByFamily',{})
        if set(ov)!=set(FAMILIES): die(f'{path}: overlap family set mismatch')
        if not (ov['F3']>ov['F2'] and ov['F3']>ov['F1'] and ov['F3']>ov['F4']): die(f'{path}: F3 stress overlap separation missing {ov}')
    return {'mode':'FORCED_COLORS_FALLBACK' if forced else 'NORMAL_NEUTRAL','viewport_width':width,'scroll_width':vp.get('scrollWidth'),'family_failures':family_failures,'status':'PASS'}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--normal-wide'); ap.add_argument('--forced-wide'); ap.add_argument('--normal-320'); ap.add_argument('--forced-320')
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty'); ap.add_argument('--output')
    a=ap.parse_args(); method=json.loads(METHOD.read_text(encoding='utf-8'))
    result={'schema':'kymaean.cone-s1.structural-preflight.v1','program_id':'CONE-S1','status':'STATIC_ONLY','static':static_checks(method)}
    supplied=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    if any(supplied):
        if not all(supplied): die('all four browser diagnostics are required')
        checks=[check_diag(a.normal_wide,False,1200),check_diag(a.forced_wide,True,1200),check_diag(a.normal_320,False,320),check_diag(a.forced_320,True,320)]
        mech={fid:[] for fid in FAMILIES}
        for c in checks:
            for fid,items in c['family_failures'].items(): mech[fid].extend(items)
        mech={fid:{'status':'FAIL' if items else 'PASS','failures':sorted(set(items))} for fid,items in mech.items()}
        candidate_failures=[fid for fid in ('F1','F2','F3','F4') if mech[fid]['status']=='FAIL']
        status='CLEAN_BROWSER_PREFLIGHT_WITH_FAMILY_FAILURES' if candidate_failures else 'CLEAN_BROWSER_PREFLIGHT_NO_SUBJECTIVE_RESULT'
        result.update({'status':status,'browser_version':a.browser_version,'os_pretty':a.os_pretty,'browser_checks':checks,'mechanical_family_status':mech,'candidate_mechanical_failures':candidate_failures,'failures':[]})
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
