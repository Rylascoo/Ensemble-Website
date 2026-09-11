#!/usr/bin/env python3
import hashlib, json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
HARNESS=ROOT/"prototypes/mat-01/harness.html"
METHOD=ROOT/"docs/evidence/MAT_01_CROSS_SURFACE_MATERIAL_SHAPE_SUCCESSOR_DIVERGENCE_METHOD_AND_MATRIX_01.json"
ADD1=ROOT/"docs/evidence/MAT_01_EXECUTION_DEFAULTS_ADDENDUM_01.json"
ADD2=ROOT/"docs/evidence/MAT_01_EXECUTION_DEFAULTS_ADDENDUM_02.json"
DEFECT=ROOT/"docs/evidence/MAT_01_BROWSER_PREFLIGHT_FIXTURE_DEFECT_01.json"
REPAIR=ROOT/"docs/evidence/MAT_01_BROWSER_REPAIR_VALIDATION_01.json"
MANIFEST=ROOT/"docs/evidence/MAT_01_FROZEN_CANDIDATE_MANIFEST_02.json"
PROBE=ROOT/"tools/mat01_browser_probe.mjs"
BROWSER_VERIFY=ROOT/"tools/verify_mat01_browser.py"
FAMILIES=["CNEG","F1","F2","F3","F4"]
ALLOWED_HEX={"#f7f7f4","#1b1b19","#62625d","#ecece7","#ddddd6","#c9c9c1","#8a8a82"}

def fail(msg): raise AssertionError(msg)
def sha(path): return hashlib.sha256(path.read_bytes().replace(b"\r\n",b"\n")).hexdigest()
def srgb_lum(h):
    vals=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    vals=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in vals]
    return .2126*vals[0]+.7152*vals[1]+.0722*vals[2]
def contrast(a,b):
    x,y=srgb_lum(a),srgb_lum(b)
    return (max(x,y)+.05)/(min(x,y)+.05)

def main():
    text=HARNESS.read_text(encoding="utf-8")
    method=json.loads(METHOD.read_text(encoding="utf-8"))
    a1=json.loads(ADD1.read_text(encoding="utf-8"))
    a2=json.loads(ADD2.read_text(encoding="utf-8"))
    defect=json.loads(DEFECT.read_text(encoding="utf-8"))
    repair=json.loads(REPAIR.read_text(encoding="utf-8"))
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    if method["status"]!="FROZEN_PRE_MATERIALIZATION": fail("method status")
    if a1["status"]!="FROZEN_PRE_SPECIMEN": fail("addendum 01 status")
    if a2["status"]!="FROZEN_PRE_SPECIMEN_COMPLETENESS_CORRECTION": fail("addendum 02 status")
    if defect["classification"]["candidate_failure"] is not False: fail("defect classification")
    if repair["status"]!="PASS_RUNTIME_MECHANICAL_REPAIR_VALIDATION": fail("repair validation status")
    if method["matrix"]["families"]!=FAMILIES: fail("family order")
    if method["matrix"]["contexts"]!=["APP","WEB"]: fail("context order")
    if a2["compact_structural_probe_fixture"]["sizes_px"]!=[16,20,24,32]: fail("compact sizes")
    if manifest.get("status")!="FROZEN_REPAIRED_EXECUTION_PACKET_BEFORE_SUBJECTIVE_REVIEW": fail("manifest status")
    if manifest.get("candidate_order")!=FAMILIES: fail("manifest candidate order")
    if manifest.get("repair_provenance",{}).get("authorized_selector_change")!={"from":".surface{max-width:100%!important}","to":".cell>.surface{max-width:100%!important}"}: fail("repair provenance selector")

    files=manifest.get("files",{})
    expected={
      "harness":(HARNESS,files.get("harness",{}).get("sha256")),
      "static_verifier":(Path(__file__),files.get("static_verifier",{}).get("sha256")),
      "browser_probe":(PROBE,files.get("browser_probe",{}).get("sha256")),
      "browser_verifier":(BROWSER_VERIFY,files.get("browser_verifier",{}).get("sha256")),
      "addendum_02":(ADD2,files.get("addendum_02",{}).get("sha256")),
      "fixture_defect":(DEFECT,files.get("fixture_defect",{}).get("sha256")),
      "repair_validation":(REPAIR,files.get("repair_validation",{}).get("sha256"))
    }
    for key,(path,want) in expected.items():
        got=sha(path)
        if got!=want: fail(f"manifest hash mismatch {key}: {got} != {want}")

    low=text.lower()
    for token in ["<img","<svg","<canvas","<video","<picture","<object","<embed","<iframe"]:
        if token in low: fail("prohibited element "+token)
    for token in ["linear-gradient","radial-gradient","conic-gradient","backdrop-filter","filter:","animation:","animation-name","transition:"]:
        if token in low: fail("prohibited CSS "+token)
    bad=[m.group(0) for m in re.finditer(r"box-shadow\s*:\s*(?!none\b)[^;}]+",low)]
    if bad: fail("non-none box shadow")
    if "url(" in low or "http://" in low or "https://" in low: fail("external/resource URL")
    for forbidden in ("threshold k","clr-01","kymaean-o3","hero artwork"):
        if forbidden in low: fail("forbidden source coupling "+forbidden)

    hexes=set(re.findall(r"#[0-9a-fA-F]{6}",text))
    if hexes!=ALLOWED_HEX: fail(f"hex palette drift {hexes}")
    min_contrast=min(contrast("#1b1b19",bg) for bg in ("#f7f7f4","#ecece7","#ddddd6","#c9c9c1"))
    if min_contrast<4.5: fail(f"contrast {min_contrast}")

    for fid in FAMILIES:
        if text.count(f'data-family="{fid}"')!=1: fail(fid+" family section count")
    if text.count('data-context="APP"')!=5 or text.count('data-context="WEB"')!=5: fail("context cell counts")
    for n in (16,20,24,32):
        if text.count(f'data-size="{n}"')!=5: fail(f"probe count {n}")
    for packet in ("NEUTRAL FIELD","Primary content","Supporting text remains unchanged across every material grammar.","Content A","Content B","Content C"):
        if text.count(packet)!=10: fail(f"content packet drift/count: {packet}={text.count(packet)}")

    compact=re.sub(r"\s+","",text)
    required=[
      "left:9%;top:0;width:30%;height:18px",
      ".web .f1-geometry .top-channel{height:28px}",
      "right:0;top:57%;width:24px;height:23%",
      ".web .f1-geometry .right-channel{width:36px}",
      "left:23%;top:26%;width:54%;height:48%",
      "border-radius:12px",
      ".web .f2-geometry .pressed-zone{border-radius:18px}",
      "right:0;bottom:0;width:23%;height:2px",
      "grid-template-columns:49fr 29fr 18fr;grid-template-rows:100%;gap:6px",
      ".web .f3-geometry{gap:10px}",
      ".mass-1{top:18%;height:62%",
      ".mass-2{top:6%;height:78%",
      ".mass-3{top:24%;height:54%",
      "clip-path:polygon(56% 0,100% 0,100% 100%,48% 100%)",
      "clip-path:polygon(calc(56% - 1px) 0,calc(56% + 1px) 0,calc(48% + 1px) 100%,calc(48% - 1px) 100%)",
      "@media (max-width:520px)",
      "grid-template-columns:1fr",
      ".cell>.surface{max-width:100%!important}",
      "@media (forced-colors:active)"
    ]
    for token in required:
        if re.sub(r"\s+","",token) not in compact: fail("missing frozen/repaired token "+token)
    if re.search(r"(?m)^\s*\.surface\{max-width:100%!important\}\s*$",text): fail("unscoped defective 320 selector remains")
    if len(re.findall(r"(?m)^\s*\.cell>\.surface\{max-width:100%!important\}\s*$",text))!=1: fail("scoped repair selector count")
    if "--probe:" not in text or "--scale:" not in text: fail("compact scaling variables absent")

    print("MAT01_REPAIRED_STATIC=PASS")
    print("HARNESS_SHA256="+sha(HARNESS))
    print("METHOD_SHA256="+sha(METHOD))
    print("ADDENDUM01_SHA256="+sha(ADD1))
    print("ADDENDUM02_SHA256="+sha(ADD2))
    print("DEFECT_SHA256="+sha(DEFECT))
    print("REPAIR_VALIDATION_SHA256="+sha(REPAIR))
    print(f"MIN_TEXT_CONTRAST={min_contrast:.4f}")

if __name__=="__main__":
    try: main()
    except Exception as e:
        print("MAT01_REPAIRED_STATIC_FAIL:",e,file=sys.stderr); sys.exit(1)
