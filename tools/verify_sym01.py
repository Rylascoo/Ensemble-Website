#!/usr/bin/env python3
import argparse, hashlib, json, math, re, sys
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'docs/evidence/SYM_01_FROZEN_CANDIDATE_MANIFEST_01.json'
C0_SHA='72cdd4c35928e1fb0bc279b680b9b7a698707dc1564ee800a84840fe61356305'
FAMILIES=['C0','CNEG','F1','F2','F3','F4']
SIZES=[16,20,24,32,48,64,96,128]
def fail(msg): raise AssertionError(msg)
def sha(p): return hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n')).hexdigest()
def local(tag): return tag.rsplit('}',1)[-1]
def static_checks():
    m=json.loads(MANIFEST.read_text(encoding='utf-8'))
    if m.get('status')!='FROZEN_CANDIDATE_BYTES': fail('manifest status')
    if m.get('candidate_eligibility')!=['F1','F2','F3','F4']: fail('candidate eligibility')
    for fid in FAMILIES:
        ent=m['assets'][fid]; p=ROOT/ent['path']
        if not p.is_file(): fail(f'{fid}: missing {p}')
        if sha(p)!=ent['sha256']: fail(f'{fid}: hash mismatch')
        if fid=='C0' and ent['sha256']!=C0_SHA: fail('C0 bytes changed')
        raw=p.read_text(encoding='utf-8')
        root=ET.fromstring(raw)
        if local(root.tag)!='svg': fail(f'{fid}: root not svg')
        vb=root.attrib.get('viewBox','').replace(',',' ').split()
        if len(vb)!=4: fail(f'{fid}: invalid viewBox')
        nums=[float(x) for x in vb]
        if nums[2]<=0 or nums[3]<=0: fail(f'{fid}: nonpositive viewBox')
        tags=[local(e.tag) for e in root.iter()]
        for bad in ('text','image','script','foreignObject','use'):
            if bad in tags: fail(f'{fid}: disallowed <{bad}>')
        for e in root.iter():
            for k,v in e.attrib.items():
                lk=local(k).lower()
                if lk in ('href','src'): fail(f'{fid}: external/reference attribute {lk}')
                if lk in ('fill','stroke') and v not in ('none','currentColor'): fail(f'{fid}: visible paint {lk}={v}')
                if 'url(' in v.lower(): fail(f'{fid}: referenced paint/resource')
        exp=m['expected_topology'][fid]
        if 'path_count' in exp and tags.count('path')!=exp['path_count']: fail(f'{fid}: path count')
        if 'circle_count' in exp and tags.count('circle')!=exp['circle_count']: fail(f'{fid}: circle count')
        if exp.get('fill_rule') and not any(e.attrib.get('fill-rule')==exp['fill_rule'] for e in root.iter()): fail(f'{fid}: fill-rule')
    for key in ('harness','method'):
        ent=m[key]; p=ROOT/ent['path']
        if sha(p)!=ent['sha256']: fail(f'{key}: hash mismatch')
    h=(ROOT/m['harness']['path']).read_text(encoding='utf-8')
    for token in ('forced-colors:active','mask-image','sym-diagnostic'):
        if token not in h: fail(f'harness missing {token}')
    for fid in FAMILIES:
        if f'data-family="{fid}"' not in h: fail(f'harness missing {fid}')
    return m
def browser_check(path,label):
    d=json.loads(Path(path).read_text(encoding='utf-8'))
    expected_width=320 if label.endswith('320') else 1200
    expected_forced=label.startswith('forced')
    vp=d.get('viewport',{})
    if round(vp.get('width',-1))!=expected_width: fail(f'{label}: viewport width {vp}')
    if vp.get('scrollWidth',10**9)>expected_width+1: fail(f'{label}: horizontal overflow {vp}')
    if bool(d.get('forcedColors'))!=expected_forced: fail(f'{label}: forcedColors mismatch')
    fams=d.get('families',{})
    if list(fams.keys())!=FAMILIES: fail(f'{label}: family order/set {list(fams)}')
    for fid in FAMILIES:
        q=fams[fid]
        if q.get('error'): fail(f'{label}/{fid}: source load {q["error"]}')
        if q.get('probeCount')!=16 or q.get('markCount')!=20: fail(f'{label}/{fid}: mark counts')
        probes=q.get('probes',[])
        exp=SIZES+SIZES
        if len(probes)!=len(exp): fail(f'{label}/{fid}: probe list')
        for i,(pr,s) in enumerate(zip(probes,exp)):
            if abs(pr.get('w',-999)-s)>.25 or abs(pr.get('h',-999)-s)>.25: fail(f'{label}/{fid}: size {i}')
            if pr.get('mask') in (None,'none'): fail(f'{label}/{fid}: missing mask {i}')
            if pr.get('bg') in (None,'rgba(0, 0, 0, 0)','transparent'): fail(f'{label}/{fid}: invisible paint {i}')
        src=q.get('source') or {}; vb=src.get('viewBox') or {}; bb=src.get('bbox') or {}
        vals=[vb.get(k) for k in ('x','y','width','height')]+[bb.get(k) for k in ('x','y','width','height')]
        if any(v is None or not math.isfinite(float(v)) for v in vals): fail(f'{label}/{fid}: invalid bbox/viewBox')
        x,y,w,h=(float(vb[k]) for k in ('x','y','width','height')); bx,by,bw,bh=(float(bb[k]) for k in ('x','y','width','height'))
        eps=0.01
        if bx < x-eps or by < y-eps or bx+bw > x+w+eps or by+bh > y+h+eps: fail(f'{label}/{fid}: geometry outside viewBox')
        margins=[(bx-x)/w,(by-y)/h,(x+w-(bx+bw))/w,(y+h-(by+bh))/h]
        if min(margins)<0.025: fail(f'{label}/{fid}: safe-envelope margin {margins}')
    return d
def main():
    ap=argparse.ArgumentParser();
    ap.add_argument('--normal-wide'); ap.add_argument('--forced-wide'); ap.add_argument('--normal-320'); ap.add_argument('--forced-320')
    ap.add_argument('--browser-version'); ap.add_argument('--os-pretty'); ap.add_argument('--output')
    a=ap.parse_args(); m=static_checks(); print('SYM01_STATIC=PASS')
    supplied=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    if any(supplied) and not all(supplied): fail('all four browser diagnostics required')
    if all(supplied):
        data={}
        for label,path in [('normal-wide',a.normal_wide),('forced-wide',a.forced_wide),('normal-320',a.normal_320),('forced-320',a.forced_320)]: data[label]=browser_check(path,label)
        print('SYM01_BROWSER=PASS')
        if a.output:
            out={'schema':'kymaean.sym01.browser-preflight.v1','status':'PASS','manifest_sha256':sha(MANIFEST),'browser_version':a.browser_version,'os_pretty':a.os_pretty,'modes':{k:{'viewport':v['viewport'],'forcedColors':v['forcedColors']} for k,v in data.items()}}
            Path(a.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    return 0
if __name__=='__main__':
    try: sys.exit(main())
    except Exception as e:
        print('SYM01_FAIL:',e,file=sys.stderr); sys.exit(1)
