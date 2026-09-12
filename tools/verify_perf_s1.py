#!/usr/bin/env python3
import argparse, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/'prototypes/perf-s1/harness.html'
METHOD=ROOT/'docs/evidence/PERF_S1_STAGE_PERFORMANCE_ATTRIBUTION_COUPLING_METHOD_AND_MATRIX_01.json'
PROBE=ROOT/'tools/perf_s1_browser_probe.mjs'
FAMILIES=('CINC','CNEG','F1','F2','F3','F4')
CANDIDATES=('F1','F2','F3','F4')

def sha256(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def die(msg):
    print('FAIL:',msg,file=sys.stderr)
    raise SystemExit(1)
def is_gray_hex(v):
    v=v.lstrip('#')
    if len(v)==3: v=''.join(c*2 for c in v)
    return len(v)==6 and v[0:2].lower()==v[2:4].lower()==v[4:6].lower()

def static_checks(method,allow_pending=False):
    src=HARNESS.read_text(encoding='utf-8'); actual=sha256(HARNESS)
    expected=method['source_freeze']['harness_sha256']
    if expected=='PENDING_AFTER_MATERIALIZATION':
        if not allow_pending: die('harness hash still pending')
    elif actual!=expected: die('harness sha256 mismatch')
    if not PROBE.exists(): die('browser probe missing')
    if method.get('program_id')!='PERF-S1': die('program id mismatch')
    if method.get('baseline_main')!='86a11d3eb58bea81dddf4dc74233e58dcf7fc2e7': die('baseline mismatch')
    if tuple(method['controls'])!=FAMILIES[:2]: die('control ids/order mismatch')
    if tuple(method['families'])!=CANDIDATES: die('candidate ids/order mismatch')
    for fid in FAMILIES:
        if fid not in src: die(f'{fid} missing from harness source')
    exact=method['incumbent_content_control']
    for token in [exact['source_character'],exact['dominant_copy'],exact['secondary_history_label']]:
        if token not in src: die('exact incumbent content missing from harness')
    for row in exact['secondary_history_rows']:
        for token in (row['time'],row['source'],row['text']):
            if token not in src: die(f'exact history token missing: {token}')
    if '@media(forced-colors:active)' not in src: die('forced-colors fallback missing')
    if re.search(r'\b(animation|transition)\s*:',src,re.I): die('animation/transition authored')
    if re.search(r'https?://|<img\b|\bfetch\s*\(',src,re.I): die('external/network/image dependency found')
    if re.search(r'Math\.random|\bDate\s*\(',src): die('nondeterministic runtime source found')
    bad=[h for h in re.findall(r'#[0-9a-fA-F]{3,6}\b',src) if not is_gray_hex(h)]
    if bad: die(f'non-gray hex colors: {bad}')
    if 'clip-path:polygon' not in src: die('neutral Character scaffold missing')
    if 'SOURCE / PERFORMING' not in src: die('explicit source instrumentation missing')
    if 'SECONDARY RECENT HISTORY' not in src: die('neutral history structure missing')
    if set(method['matrix']['character_layouts'])!={'2','3','4','5'}: die('matrix character counts mismatch')
    if method['families']['F1']['geometry']['panel_width']!=620 or '.family-F1 .perf-panel{width:62%' not in src:
        die('F1 width mismatch')
    if method['families']['F2']['geometry']['source_header_clamp']!=[90,910] or 'clamp(s,9,91)' not in src:
        die('F2 clamp mismatch')
    if method['families']['F3']['geometry']['witness_width_px']!=1 or 'width:1px' not in src:
        die('F3 witness mismatch')
    if method['families']['F4']['geometry']['aperture_width']!=44 or 'width:44px' not in src:
        die('F4 aperture mismatch')
    if 'padding:14px 0 0' not in src: die('Character coordinate normalization missing')
    return {
        'harness_sha256':actual,
        'families':6,
        'candidate_families':4,
        'stress_specimens_expected':24,
        'exact_content_specimens_expected':6,
        'total_specimens_expected':30,
        'character_loci_expected':114,
        'source_status':'PASS'
    }

def check_diag(path,forced,width):
    d=json.loads(Path(path).read_text(encoding='utf-8'))
    if d.get('schema')!='kymaean.perf-s1.browser-diagnostic.v1': die(f'{path}: schema mismatch')
    expected={'families':6,'boards':30,'stressBoards':24,'exactBoards':6,'characterLoci':114,'sourceFlags':30,'sourceHeaders':30,'panels':30,'historyRows':120,'exactCopyBoards':6}
    for k,v in expected.items():
        if d.get(k)!=v: die(f'{path}: {k} {d.get(k)} != {v}')
    if bool(d.get('forcedColors'))!=forced: die(f'{path}: forced-colors mismatch')
    vp=d.get('viewport',{})
    if vp.get('innerWidth')!=width: die(f'{path}: viewport width mismatch {vp}')
    if vp.get('scrollWidth',width)>width: die(f'{path}: horizontal overflow {vp}')
    for key in ('missingSourceFlags','sourceHeaderMismatch','geometryFailures','sourceAlignmentFailures','labelVisibilityFailures','boardOverflowFailures'):
        if d.get(key)!=[]: die(f'{path}: {key}={d.get(key)}')
    if d.get('witnessCount')!=5: die(f'{path}: F3 witness count mismatch')
    if d.get('apertureCount')!=5: die(f'{path}: F4 aperture count mismatch')
    return {'mode':'FORCED_COLORS_FALLBACK' if forced else 'NORMAL_NEUTRAL','viewport_width':width,'scroll_width':vp.get('scrollWidth'),'status':'PASS'}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--allow-pending-hash',action='store_true')
    ap.add_argument('--normal-wide'); ap.add_argument('--forced-wide'); ap.add_argument('--normal-320'); ap.add_argument('--forced-320')
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty'); ap.add_argument('--output')
    a=ap.parse_args(); method=json.loads(METHOD.read_text(encoding='utf-8'))
    result={'schema':'kymaean.perf-s1.structural-preflight.v1','program_id':'PERF-S1','status':'STATIC_ONLY','static':static_checks(method,a.allow_pending_hash)}
    supplied=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    if any(supplied):
        if not all(supplied): die('all four browser diagnostics are required')
        checks=[check_diag(a.normal_wide,False,1200),check_diag(a.forced_wide,True,1200),check_diag(a.normal_320,False,320),check_diag(a.forced_320,True,320)]
        result.update({'status':'CLEAN_BROWSER_PREFLIGHT_NO_SUBJECTIVE_RESULT','browser_version':a.browser_version,'os_pretty':a.os_pretty,'browser_checks':checks,'failures':[]})
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
