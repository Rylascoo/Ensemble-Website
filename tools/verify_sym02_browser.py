#!/usr/bin/env python3
import argparse, hashlib, json, math, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FAMILIES=['C0-ORIGINAL','C0-R1','C0-R2','C0-R3','N1','N2','N3']
ELIGIBLE=FAMILIES[1:]
SIZES=[16,20,24,32,48,64,96,128]
PATH_COUNTS={'C0-ORIGINAL':3,'C0-R1':3,'C0-R2':3,'C0-R3':3,'N1':1,'N2':4,'N3':3}
def fail(msg): raise AssertionError(msg)
def finite(v): return v is not None and math.isfinite(float(v))
def dist(a,b): return math.hypot(float(a['centroidX'])-float(b['centroidX']),float(a['centroidY'])-float(b['centroidY']))
def bbox_close(a,b,tol=.02): return all(abs(float(a[k])-float(b[k]))<=tol for k in ('x','y','width','height'))
def add(issues,fid,msg):
    if msg not in issues[fid]: issues[fid].append(msg)
def weighted(parts):
    area=sum(float(p['filledArea']) for p in parts)
    if area<=0: fail('nonpositive path area')
    return {'filledArea':area,'centroidX':sum(float(p['filledArea'])*float(p['centroidX']) for p in parts)/area,'centroidY':sum(float(p['filledArea'])*float(p['centroidY']) for p in parts)/area}
def sha(path): return hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n')).hexdigest()
def browser_check(path,label):
    d=json.loads(Path(path).read_text(encoding='utf-8')); issues={k:[] for k in ELIGIBLE}
    width=320 if label.endswith('320') else 1200; forced=label.startswith('forced')
    vp=d.get('viewport',{})
    if round(vp.get('width',-1))!=width: fail(f'{label}: viewport width {vp}')
    if vp.get('scrollWidth',10**9)>width+1: fail(f'{label}: horizontal overflow {vp}')
    if bool(d.get('forcedColors'))!=forced: fail(f'{label}: forcedColors mismatch')
    if d.get('overflowElements'): fail(f'{label}: carrier overflow {d["overflowElements"][:3]}')
    fams=d.get('families',{})
    if list(fams.keys())!=FAMILIES: fail(f'{label}: family order/set {list(fams)}')
    metrics=d.get('rasterMetrics',{})
    if list(metrics.keys())!=FAMILIES: fail(f'{label}: raster metric order/set {list(metrics)}')
    for fid in FAMILIES:
        q=fams[fid]
        if q.get('error'): fail(f'{label}/{fid}: source load {q["error"]}')
        if q.get('probeCount')!=16 or q.get('markCount')!=20: fail(f'{label}/{fid}: mark counts')
        probes=q.get('probes',[]); exp=SIZES+SIZES
        if len(probes)!=len(exp): fail(f'{label}/{fid}: probe list')
        for i,(pr,s) in enumerate(zip(probes,exp)):
            if abs(pr.get('w',-999)-s)>.25 or abs(pr.get('h',-999)-s)>.25: fail(f'{label}/{fid}: size {i}')
            if pr.get('mask') in (None,'none'): fail(f'{label}/{fid}: missing mask {i}')
            if pr.get('bg') in (None,'rgba(0, 0, 0, 0)','transparent'): fail(f'{label}/{fid}: invisible paint {i}')
        src=q.get('source') or {}; vb=src.get('viewBox') or {}; bb=src.get('bbox') or {}
        vals=[vb.get(k) for k in ('x','y','width','height')]+[bb.get(k) for k in ('x','y','width','height')]
        if any(not finite(v) for v in vals): fail(f'{label}/{fid}: invalid bbox/viewBox')
        x,y,w,h=(float(vb[k]) for k in ('x','y','width','height')); bx,by,bw,bh=(float(bb[k]) for k in ('x','y','width','height'))
        outside=bx<x-.01 or by<y-.01 or bx+bw>x+w+.01 or by+bh>y+h+.01
        margins=[(bx-x)/w,(by-y)/h,(x+w-(bx+bw))/w,(y+h-(by+bh))/h]
        if fid=='C0-ORIGINAL':
            if outside: fail(f'{label}/{fid}: control geometry outside viewBox')
            if min(margins)<.025: fail(f'{label}/{fid}: control safe-envelope margin {margins}')
        else:
            if outside: add(issues,fid,'geometry extends outside viewBox')
            if min(margins)<.025: add(issues,fid,f'safe-envelope margin below 2.5%: {min(margins):.4f}')
        pbb=src.get('pathBBoxes') or []
        if len(pbb)!=PATH_COUNTS[fid]: fail(f'{label}/{fid}: path bbox count')
        m=metrics[fid]
        if not all(finite(m.get(k)) for k in ('filledArea','centroidX','centroidY')): fail(f'{label}/{fid}: invalid raster metrics')
        if len(m.get('paths',[]))!=PATH_COUNTS[fid]: fail(f'{label}/{fid}: raster path metric count')
    return d,issues
def classify(data,issues):
    m=data['rasterMetrics']; c0=m['C0-ORIGINAL']
    r1=m['C0-R1']; area_delta=abs(float(r1['filledArea'])/float(c0['filledArea'])-1)
    if area_delta>.02: add(issues,'C0-R1',f'total filled-area delta {area_delta:.4%} exceeds 2%')
    if dist(r1,c0)>1.5: add(issues,'C0-R1',f'filled centroid shift {dist(r1,c0):.3f} exceeds 1.5')
    if not bbox_close(r1['bbox'],c0['bbox']): add(issues,'C0-R1','outer extrema differ from C0')
    r2=m['C0-R2']; c0r=c0['paths'][2]; r2r=r2['paths'][2]
    if not bbox_close(r2r['bbox'],c0r['bbox']): add(issues,'C0-R2','right-field bounding box differs from exact C0')
    r3=m['C0-R3']; c0left=weighted(c0['paths'][:2]); r3left=weighted(r3['paths'][:2])
    left_delta=abs(float(r3left['filledArea'])/float(c0left['filledArea'])-1)
    if left_delta>.08: add(issues,'C0-R3',f'aggregate left-field area delta {left_delta:.4%} exceeds 8%')
    if dist(r3left,c0left)>4: add(issues,'C0-R3',f'aggregate left-field centroid shift {dist(r3left,c0left):.3f} exceeds 4')
    return {'C0-R1_area_delta':area_delta,'C0-R1_centroid_shift':dist(r1,c0),'C0-R3_left_area_delta':left_delta,'C0-R3_left_centroid_shift':dist(r3left,c0left)}
def merge_issues(target,source):
    for fid,msgs in source.items():
        for msg in msgs: add(target,fid,msg)
def main():
    ap=argparse.ArgumentParser()
    for name in ('normal-wide','forced-wide','normal-320','forced-320'): ap.add_argument('--'+name,required=True)
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty'); ap.add_argument('--output')
    a=ap.parse_args(); paths=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    labels=['normal-wide','forced-wide','normal-320','forced-320']; data={}; issues={k:[] for k in ELIGIBLE}
    for label,path in zip(labels,paths):
        d,local_issues=browser_check(path,label); data[label]=d; merge_issues(issues,local_issues)
    baseline=data['normal-wide']['rasterMetrics']
    for label in labels[1:]:
        cur=data[label]['rasterMetrics']
        for fid in FAMILIES:
            for key in ('filledArea','centroidX','centroidY'):
                if abs(float(cur[fid][key])-float(baseline[fid][key]))>.02: fail(f'{label}/{fid}: raster metric drift {key}')
    quantitative=classify(data['normal-wide'],issues)
    results={fid:{'status':'PASS_MECHANICAL' if not issues[fid] else 'FAIL_MECHANICAL','issues':issues[fid]} for fid in ELIGIBLE}
    survivors=[fid for fid in ELIGIBLE if not issues[fid]]
    print('SYM02_BROWSER=PASS')
    for fid in ELIGIBLE: print(f'{fid}={results[fid]["status"]}' + ('' if not issues[fid] else ': '+'; '.join(issues[fid])))
    if a.output:
        out={'schema':'kymaean.sym02.browser-preflight.v1','status':'PASS_COMPLETE_MATRIX','browser_version':a.browser_version,'os_pretty':a.os_pretty,'candidate_results':results,'eligible_for_subjective_review':survivors,'quantitative_checks':quantitative,'modes':{k:{'viewport':v['viewport'],'forcedColors':v['forcedColors']} for k,v in data.items()},'browser_verifier_sha256':sha(Path(__file__))}
        Path(a.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':
    try: main()
    except Exception as e:
        print('SYM02_BROWSER_FAIL:',e,file=sys.stderr); sys.exit(1)
