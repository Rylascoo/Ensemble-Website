#!/usr/bin/env python3
import argparse, hashlib, json, math, sys
from pathlib import Path

FAMILIES=["CNEG","F1","F2","F3","F4"]
COUNTS={"CNEG":3,"F1":2,"F2":2,"F3":3,"F4":2}
PACKET={
  "eyebrow":"NEUTRAL FIELD",
  "heading":"Primary content",
  "body":"Supporting text remains unchanged across every material grammar.",
  "units":["Content A","Content B","Content C"]
}
SIZES=[16,20,24,32]

def fail(msg): raise AssertionError(msg)
def close(a,b,tol=.75): return abs(float(a)-float(b))<=tol
def inside(inner,outer,tol=.75):
    return inner["x"]>=outer["x"]-tol and inner["y"]>=outer["y"]-tol and inner["right"]<=outer["right"]+tol and inner["bottom"]<=outer["bottom"]+tol
def sha(path): return hashlib.sha256(Path(path).read_bytes().replace(b"\r\n",b"\n")).hexdigest()

def check(path,label):
    d=json.loads(Path(path).read_text(encoding="utf-8"))
    width=320 if label.endswith("320") else 1200
    forced=label.startswith("forced")
    vp=d.get("viewport",{})
    if round(vp.get("width",-1))!=width: fail(f"{label}: viewport {vp}")
    if vp.get("scrollWidth",10**9)>width+1: fail(f"{label}: horizontal document overflow {vp}")
    if bool(d.get("forcedColors"))!=forced: fail(f"{label}: forced-colors mismatch")
    if d.get("prohibitedElements")!=0 or d.get("externalStyleLinks")!=0: fail(f"{label}: prohibited resource elements")
    if d.get("overflowElements"): fail(f"{label}: overflow elements {d['overflowElements'][:3]}")
    if d.get("familyOrder")!=FAMILIES: fail(f"{label}: family order {d.get('familyOrder')}")
    fams=d.get("families",{})
    if list(fams)!=FAMILIES: fail(f"{label}: family keys")
    for fid in FAMILIES:
        f=fams[fid]
        surfaces=f.get("surfaces",[])
        if [x.get("context") for x in surfaces]!=["APP","WEB"]: fail(f"{label}/{fid}: contexts")
        for s in surfaces:
            sr=s["surfaceRect"]; cr=s["contentRect"]; context=s["context"]
            if s.get("overflow")!="hidden": fail(f"{label}/{fid}/{context}: surface overflow")
            if s.get("text")!=PACKET: fail(f"{label}/{fid}/{context}: content drift")
            if s.get("geometryCount")!=1: fail(f"{label}/{fid}/{context}: geometry root count")
            if len(s.get("geometryRects",[]))!=COUNTS[fid]: fail(f"{label}/{fid}/{context}: geometry child count")
            if not inside(cr,sr): fail(f"{label}/{fid}/{context}: required content clipped")
            floor=210 if context=="APP" else 250
            if sr["height"]+0.75<floor: fail(f"{label}/{fid}/{context}: min-height")
            if sr["right"]>width+.75 or sr["x"]<-.75: fail(f"{label}/{fid}/{context}: viewport bounds")
            if width==320 and sr["width"]>296.75: fail(f"{label}/{fid}/{context}: 320 content-box width")
            if width==1200:
                cap=420 if context=="APP" else 680
                if sr["width"]>cap+.75: fail(f"{label}/{fid}/{context}: max-width")
        if width==320:
            a,w=surfaces
            if not close(a["surfaceRect"]["x"],w["surfaceRect"]["x"],1): fail(f"{label}/{fid}: one-column alignment")
            if w["cellRect"]["y"]<=a["cellRect"]["bottom"]: fail(f"{label}/{fid}: contexts not stacked")
        else:
            a,w=surfaces
            if w["cellRect"]["x"]<=a["cellRect"]["right"]: fail(f"{label}/{fid}: wide contexts not two-column")
        probes=f.get("probes",[])
        if [p.get("size") for p in probes]!=SIZES: fail(f"{label}/{fid}: probe sizes")
        for p,n in zip(probes,SIZES):
            wr=p["wrapperRect"]; can=p["canonicalRect"]
            if not close(wr["width"],n,.25) or not close(wr["height"],n,.25): fail(f"{label}/{fid}/{n}: wrapper size")
            if not close(can["width"],n,.35) or not close(can["height"],n,.35): fail(f"{label}/{fid}/{n}: scaled clone size")
            if len(p.get("geometryRects",[]))!=COUNTS[fid]: fail(f"{label}/{fid}/{n}: compact geometry count")
    return d

def main():
    ap=argparse.ArgumentParser()
    for name in ("normal-wide","forced-wide","normal-320","forced-320"): ap.add_argument("--"+name,required=True)
    ap.add_argument("--browser-version");ap.add_argument("--os-pretty");ap.add_argument("--output")
    a=ap.parse_args()
    labels=["normal-wide","forced-wide","normal-320","forced-320"]
    paths=[a.normal_wide,a.forced_wide,a.normal_320,a.forced_320]
    data={label:check(path,label) for label,path in zip(labels,paths)}
    base=data["normal-wide"]["families"]
    for label in labels[1:]:
        cur=data[label]["families"]
        for fid in FAMILIES:
            if [len(x["geometryRects"]) for x in cur[fid]["surfaces"]]!=[len(x["geometryRects"]) for x in base[fid]["surfaces"]]:
                fail(f"{label}/{fid}: topology child-count drift")
    print("MAT01_BROWSER=PASS")
    if a.output:
        out={
          "schema":"kymaean.mat01.browser-preflight.v1",
          "status":"PASS_COMPLETE_MATRIX",
          "browser_version":a.browser_version,
          "os_pretty":a.os_pretty,
          "families":FAMILIES,
          "contexts":["APP","WEB"],
          "viewports":[1200,320],
          "modes":{k:{"viewport":v["viewport"],"forcedColors":v["forcedColors"]} for k,v in data.items()},
          "browser_verifier_sha256":sha(Path(__file__))
        }
        Path(a.output).write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8",newline="\n")
if __name__=="__main__":
    try: main()
    except Exception as e:
        print("MAT01_BROWSER_FAIL:",e,file=sys.stderr);sys.exit(1)
