#!/usr/bin/env python3
import argparse, hashlib, html, json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/'prototypes/sta-01/harness.html'
METHOD=ROOT/'docs/evidence/STA_01_NONCOLOR_FOCUS_SELECTION_METHOD_AND_MATRIX_01.json'
ADDENDUM=ROOT/'docs/evidence/STA_01_EXECUTION_DEFAULTS_ADDENDUM_01.json'

def sha256(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def die(msg):
    print('FAIL:', msg, file=sys.stderr)
    raise SystemExit(1)

def extract_diag(path):
    s=Path(path).read_text(encoding='utf-8', errors='replace').strip()
    if s.startswith('{'):
        return json.loads(s)
    m=re.search(r'<pre\s+id="sta-diagnostic"[^>]*>(.*?)</pre>', s, flags=re.S|re.I)
    if not m: die(f'no sta-diagnostic in {path}')
    return json.loads(html.unescape(m.group(1)))

def witness_present(s):
    b=s['before']; a=s['after']
    vals=[b.get('width'),b.get('height'),b.get('borderTop'),b.get('borderRight'),b.get('borderBottom'),b.get('borderLeft'),
          a.get('width'),a.get('height'),a.get('borderTop'),a.get('borderRight'),a.get('borderBottom'),a.get('borderLeft')]
    return any(isinstance(v,(int,float)) and v >= 2 for v in vals if v is not None)

def static_checks(method, addendum):
    src=HARNESS.read_text(encoding='utf-8')
    if sha256(HARNESS) != method['source_freeze']['harness_sha256']: die('harness sha256 mismatch')
    if addendum.get('parent_harness_sha256') != method['source_freeze']['harness_sha256']: die('addendum harness pin mismatch')
    if addendum.get('invalid_attempt',{}).get('workflow_run') != 34532967279: die('unexpected modality-correction lineage')
    bad_patterns={
        'img element':r'<img\b','svg element':r'<svg\b','gradient':r'gradient\s*\(',
        'filter':r'\bfilter\s*:','animation declaration':r'\banimation\s*:(?!none)','transition declaration':r'\btransition\s*:(?!none)'
    }
    for label,pat in bad_patterns.items():
        if re.search(pat,src,re.I): die(f'prohibited {label}')
    if '@media(forced-colors:active)' not in src: die('forced-colors law missing')
    if '@media(prefers-reduced-motion:reduce)' not in src: die('reduced-motion law missing')
    if '.sample:focus-visible' not in src: die(':focus-visible law missing')
    if src.count('<section class="family ') != 4: die('family count source mismatch')
    if src.count('class="context ') != 8: die('context count source mismatch')
    if src.count('class="sample ') != 40: die('sample count source mismatch')
    if len(re.findall(r'<button[^>]+aria-pressed="true"',src,re.I)) != 16: die('aria-pressed source count mismatch')
    if len(re.findall(r'<button[^>]+disabled',src,re.I)) != 8: die('disabled source count mismatch')
    return {
        'harness_sha256':sha256(HARNESS),
        'source_matrix':'4 families / 8 contexts / 40 specimens / 16 selected / 8 disabled',
        'keyboard_focus_measurement':'STA_01_EXECUTION_DEFAULTS_ADDENDUM_01.json'
    }

def check_keyboard_focus(d, fam, ctx):
    try: p=d['keyboardFocus'][fam][ctx]
    except Exception: die(f'{fam}/{ctx} keyboard-focus observation missing')
    if p.get('disabled'): die(f'{fam}/{ctx} keyboard traversal landed on disabled specimen')
    if not p.get('focusVisible'): die(f'{fam}/{ctx} keyboard focus did not match :focus-visible')
    if (p.get('outlineWidth') or 0) < 2 or p.get('outlineStyle')=='none': die(f'{fam}/{ctx} keyboard focus outline missing')
    expected='dotted' if fam=='f4' else 'solid'
    if p.get('outlineStyle') != expected: die(f'{fam}/{ctx} keyboard focus style {p.get("outlineStyle")} != {expected}')

def check_diag(d, expected_forced, expected_width):
    if d['schema']!='kymaean.sta01.browser-diagnostic.v1': die('diagnostic schema mismatch')
    c=d['counts']
    if c != {'families':4,'contexts':8,'specimens':40,'ariaPressed':16,'disabled':8}: die(f'count mismatch {c}')
    if bool(d['media']['forcedColors']) != expected_forced: die('forced-colors media mismatch')
    if d['viewport']['innerWidth'] != expected_width: die(f'viewport width mismatch {d["viewport"]["innerWidth"]} != {expected_width}')
    if d['viewport']['scrollWidth'] > d['viewport']['innerWidth']: die(f'horizontal overflow {d["viewport"]}')
    for fam in ('f1','f2','f3','f4'):
        for ctx in ('APP','WEB'):
            check_keyboard_focus(d,fam,ctx)
            states=d['specimens'][fam][ctx]
            required={'default','focus','selected','focus_plus_selected','disabled'}
            if set(states)!=required: die(f'{fam}/{ctx} states mismatch')
            fs=states['focus_plus_selected']; sel=states['selected']; dis=states['disabled']
            if fs['ariaPressed']!='true' or sel['ariaPressed']!='true': die(f'{fam}/{ctx} selected aria mismatch')
            if not dis['disabled'] or dis['ariaPressed'] is not None: die(f'{fam}/{ctx} disabled semantics mismatch')
            if (fs['outline']['width'] or 0) < 2 or fs['outline']['style']=='none': die(f'{fam}/{ctx} combined focus outline missing')
            if fam=='f1':
                if min(sel['border'].values()) < 2 or min(fs['border'].values()) < 2: die(f'{fam}/{ctx} selection boundary lost')
            elif fam=='f2':
                if not witness_present(sel) or not witness_present(fs): die(f'{fam}/{ctx} edge witness lost')
            elif fam=='f3':
                if not witness_present(sel) or not witness_present(fs): die(f'{fam}/{ctx} bracket witness lost')
            elif fam=='f4':
                if int(sel['fontWeight']) < 700 or int(fs['fontWeight']) < 700: die(f'{fam}/{ctx} weight carrier lost')
                if expected_forced and fs['boxShadow']!='none': die(f'{fam}/{ctx} forced-colors shadow not suppressed')
    return {
        'mode':'FORCED_COLORS' if expected_forced else 'NORMAL',
        'viewport_width':expected_width,
        'scroll_width':d['viewport']['scrollWidth'],
        'keyboard_focus_contexts':'8/8 PASS',
        'status':'PASS'
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--normal-wide'); ap.add_argument('--forced-wide'); ap.add_argument('--normal-320'); ap.add_argument('--forced-320'); ap.add_argument('--output')
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty')
    a=ap.parse_args()
    method=json.loads(METHOD.read_text(encoding='utf-8'))
    addendum=json.loads(ADDENDUM.read_text(encoding='utf-8'))
    result={'schema':'kymaean.sta01.structural-accessibility-preflight.v1','status':'STATIC_ONLY','program_id':'STA-01','static':static_checks(method,addendum)}
    supplied=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    if any(supplied):
        if not all(supplied): die('all four browser diagnostics are required')
        checks=[
            check_diag(extract_diag(a.normal_wide),False,1200),
            check_diag(extract_diag(a.forced_wide),True,1200),
            check_diag(extract_diag(a.normal_320),False,320),
            check_diag(extract_diag(a.forced_320),True,320)
        ]
        result.update({'status':'CLEAN_HOSTED_PREFLIGHT_NO_SUBJECTIVE_RESULT','browser_version':a.browser_version,'os_pretty':a.os_pretty,'browser_checks':checks,'failures':[]})
    if a.output:
        Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
