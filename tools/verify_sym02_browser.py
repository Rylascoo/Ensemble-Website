#!/usr/bin/env python3
import argparse, json, math, sys
from pathlib import Path
FAMILIES=['C0-ORIGINAL','C0-R1','C0-R2','C0-R3','N1','N2','N3']
SIZES=[16,20,24,32,48,64,96,128]
PATH_COUNTS={'C0-ORIGINAL':3,'C0-R1':3,'C0-R2':3,'C0-R3':3,'N1':1,'N2':4,'N3':3}
def fail(msg): raise AssertionError(msg)
def finite(v): return v is not None and math.isfinite(float(v))
def distance(a,b): return math.hypot(float(a['centroidX'])-float(b['centroidX']),float(a['centroidY'])-float(b['centroidY']))
def browser_check(path,label):
    d=json.loads(Path(path).read_text(encoding='utf-8'))
    expected_width=320 if label.endswith('320') else 1200
    expected_forced=label.startswith('forced')
    vp=d.get('viewport',{})
    if round(vp.get('width',-1))!=expected_width: fail(f'{label}: viewport width {vp}')
    if vp.get('scrollWidth',10**9)>expected_width+1: fail(f'{label}: horizontal overflow {vp}')
    if bool(d.get('forcedColors'))!=expected_forced: fail(f'{label}: forcedColors mismatch')
    if d.get('overflowElements'): fail(f'{label}: overflow elements {d["overflowElements"][:3]}')
    fams=d.get('families',{})
    if list(fams.keys())!=FAMILIES: fail(f'{label}: family order/set {list(fams)}')
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
        eps=.01
        if bx<x-eps or by<y-eps or bx+bw>x+w+eps or by+bh>y+h+eps: fail(f'{label}/{fid}: geometry outside viewBox')
        margins=[(bx-x)/w,(by-y)/h,(x+w-(bx+bw))/w,(y+h-(by+bh))/h]
        if min(margins)<.025: fail(f'{label}/{fid}: safe-envelope margin {margins}')
        pb=src.get('pathBBoxes') or []
        if len(pb)!=PATH_COUNTS[fid]: fail(f'{label}/{fid}: path bbox count')
    metrics=d.get('rasterMetrics') or {}
    if list(metrics.keys())!=FAMILIES: fail(f'{label}: raster metric family set/order')
    for fid in FAMILIES:
        m=metrics[fid]
        if not all(finite(m.get(k)) for k in ('filledArea','centroidX','centroidY')): fail(f'{label}/{fid}: invalid raster metrics')
        if len(m.get('paths') or [])!=PATH_COUNTS[fid]: fail(f'{label}/{fid}: raster path metrics')
    return d

def weighted(parts):
    area=sum(float(p['filledArea']) for p in parts)
    return {'filledArea':area,'centroidX':sum(float(p['centroidX'])*float(p['filledArea']) for p in parts)/area,'centroidY':sum(float(p['centroidY'])*float(p['filledArea']) for p in parts)/area}
def refinement_checks(d):
    m=d['rasterMetrics']; c0=m['C0-ORIGINAL']; r1=m['C0-R1']; r3=m['C0-R3']
    r1_area_delta=abs(float(r1['filledArea'])-float(c0['filledArea']))/float(c0['filledArea'])
    r1_centroid=distance(r1,c0)
    if r1_area_delta>.02: fail(f'C0-R1: filled-area delta {r1_area_delta:.4f} > .02')
    if r1_centroid>1.5: fail(f'C0-R1: centroid shift {r1_centroid:.3f} > 1.5')
    c0_right=d['families']['C0-ORIGINAL']['source']['pathBBoxes'][2]
    r2_right=d['families']['C0-R2']['source']['pathBBoxes'][2]
    for key in ('x','y','width','height'):
        if abs(float(c0_right[key])-float(r2_right[key]))>.01: fail(f'C0-R2: right bbox {key} changed')
    c0_left=weighted(c0['paths'][:2]); r3_left=weighted(r3['paths'][:2])
    r3_area_delta=abs(r3_left['filledArea']-c0_left['filledArea'])/c0_left['filledArea']
    r3_centroid=distance(r3_left,c0_left)
    if r3_area_delta>.08: fail(f'C0-R3: left-area delta {r3_area_delta:.4f} > .08')
    if r3_centroid>4: fail(f'C0-R3: left centroid shift {r3_centroid:.3f} > 4')
    return {'C0-R1':{'filled_area_delta_ratio':r1_area_delta,'centroid_shift':r1_centroid},'C0-R2':{'right_bbox_exact':True},'C0-R3':{'left_filled_area_delta_ratio':r3_area_delta,'left_centroid_shift':r3_centroid}}

def main():
    ap=argparse.ArgumentParser()
    for key in ('normal-wide','forced-wide','normal-320','forced-320'): ap.add_argument('--'+key,required=True)
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty'); ap.add_argument('--output')
    a=ap.parse_args(); data={}
    for label,attr in [('normal-wide','normal_wide'),('forced-wide','forced_wide'),('normal-320','normal_320'),('forced-320','forced_320')]: data[label]=browser_check(getattr(a,attr),label)
    refinements=refinement_checks(data['normal-wide'])
    print('SYM02_BROWSER=PASS')
    if a.output:
        out={'schema':'kymaean.sym02.browser-preflight.v1','status':'PASS','browser_version':a.browser_version,'os_pretty':a.os_pretty,'modes':{k:{'viewport':v['viewport'],'forcedColors':v['forcedColors']} for k,v in data.items()},'refinement_metrics':refinements,'scope':'Mechanical/source/viewport/forced-colors/refinement-tolerance validation only. No subjective survivor judgment.'}
        Path(a.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    return 0
if __name__=='__main__':
    try: sys.exit(main())
    except Exception as e:
        print('SYM02_BROWSER_FAIL:',e,file=sys.stderr); sys.exit(1)
