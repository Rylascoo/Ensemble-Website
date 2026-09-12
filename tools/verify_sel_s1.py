#!/usr/bin/env python3
import argparse, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/'prototypes/sel-s1/harness.html'
METHOD=ROOT/'docs/evidence/SEL_S1_STAGE_FOCUS_SELECTION_HINGE_METHOD_AND_MATRIX_01.json'
EXPECTED_METHOD='270c71e5d668f88134bb46dbd80dbccc7de7fd43bbfb09b73f9da77c6324901f'
EXPECTED_HARNESS='68990067baa686284959324ba0df76136b205a20f79a02ef373a99579ed4722c'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def die(msg): print('FAIL:',msg,file=sys.stderr); raise SystemExit(1)
def static_checks():
    method=json.loads(METHOD.read_text(encoding='utf-8')); src=HARNESS.read_text(encoding='utf-8')
    if sha(METHOD)!=EXPECTED_METHOD: die('method hash mismatch')
    if sha(HARNESS)!=EXPECTED_HARNESS: die('harness hash mismatch')
    if method['matrix']['logical_boards']!=30: die('method board count mismatch')
    for label,pat in {'img':r'<img\b','svg':r'<svg\b','gradient':r'gradient\s*\(','filter':r'\bfilter\s*:','animation':r'\banimation\s*:(?!none)','transition':r'\btransition\s*:(?!none)'}.items():
        if re.search(pat,src,re.I): die('prohibited '+label)
    for token in ('CNEG','CINC','F1','F2','F3','F4','L2_SELECTED_RIGHT','L3_FOCUS_LEFT','L4_FOCUS_SELECTED_THIRD','L5_SELECTED_OPPORTUNITY_SECOND','L5_SELECTED_SPEAKING_FOURTH'):
        if token not in src: die('missing source token '+token)
    if '@media(forced-colors:active)' not in src or '@media(prefers-reduced-motion:reduce)' not in src: die('accessibility media law missing')
    if ':focus-visible' not in src: die('focus-visible source law missing')
    return {'method_sha256':EXPECTED_METHOD,'harness_sha256':EXPECTED_HARNESS,'matrix':'6 families / 5 layouts / 30 boards / 114 Character loci'}
def load_diag(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))
def check_keyboard(d):
    obs=d.get('keyboardFocus') or []
    if len(obs)!=12: die(f'keyboard focus count {len(obs)} != 12')
    seen=[]
    for i,o in enumerate(obs):
        if not o: die(f'keyboard focus observation {i} missing')
        if o['layout'] not in ('L3_FOCUS_LEFT','L4_FOCUS_SELECTED_THIRD'): die('Tab landed on unexpected layout')
        if not o.get('focusVisible'): die(f'{o["family"]}/{o["layout"]} not :focus-visible')
        if o['family']=='CINC':
            if o.get('nameBorderWidth',0)<1 or o.get('nameBorderStyle')=='none': die(f'{o["family"]}/{o["layout"]} historical focus control missing')
        elif o.get('pseudoContent')=='none' or o.get('borderWidth',0)<2 or o.get('borderStyle')=='none': die(f'{o["family"]}/{o["layout"]} focus ellipse missing')
        seen.append((o['family'],o['layout']))
    expected={(f,l) for f in ('CNEG','CINC','F1','F2','F3','F4') for l in ('L3_FOCUS_LEFT','L4_FOCUS_SELECTED_THIRD')}
    if set(seen)!=expected: die('keyboard target coverage mismatch')
def check_diag(d,forced,width):
    if d.get('schema')!='kymaean.sel-s1.browser-diagnostic.v1': die('diagnostic schema mismatch')
    if bool(d.get('forcedColors'))!=forced: die('forced-colors media mismatch')
    v=d['viewport']
    if v['innerWidth']!=width: die(f'viewport width {v["innerWidth"]} != {width}')
    if v['scrollWidth']>v['innerWidth']: die(f'horizontal page overflow {v}')
    expected={'families':6,'boards':30,'characters':114,'selected':24,'focusFixtures':12,'keyboardTargets':12}
    if d.get('counts')!=expected: die(f'count mismatch {d.get("counts")}')
    for key in ('boardOverflowFailures','baseGeometryFailures','textMismatchFailures','candidateWitnessFailures','focusFixtureFailures'):
        if d.get(key): die(f'{key}: {d[key]}')
    check_keyboard(d)
    return {'mode':'FORCED_COLORS' if forced else 'NORMAL','viewport_width':width,'scroll_width':v['scrollWidth'],'keyboard_targets':'12/12 PASS','status':'PASS'}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--normal-wide'); ap.add_argument('--forced-wide'); ap.add_argument('--normal-320'); ap.add_argument('--forced-320')
    ap.add_argument('--output'); ap.add_argument('--browser-version'); ap.add_argument('--os-pretty')
    a=ap.parse_args()
    result={'schema':'kymaean.sel-s1.structural-accessibility-preflight.v1','status':'STATIC_ONLY','program_id':'SEL-S1','static':static_checks()}
    supplied=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    if any(supplied):
        if not all(supplied): die('all four browser diagnostics are required')
        checks=[check_diag(load_diag(a.normal_wide),False,1200),check_diag(load_diag(a.forced_wide),True,1200),check_diag(load_diag(a.normal_320),False,320),check_diag(load_diag(a.forced_320),True,320)]
        result.update({'status':'CLEAN_BROWSER_PREFLIGHT_NO_SUBJECTIVE_RESULT','browser_version':a.browser_version,'os_pretty':a.os_pretty,'browser_checks':checks,'failures':[]})
    if a.output: Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
