#!/usr/bin/env python3
"""Verify SYM-02 source isolation, topology, and C0 refinement boundaries."""
from pathlib import Path
import hashlib
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "docs/evidence/SYM_02_REFINEMENT_AND_NEW_CONCEPT_PROGRAM_01.json"
MANIFEST = ROOT / "docs/evidence/SYM_02_FROZEN_CANDIDATE_MANIFEST_01.json"
C0 = ROOT / "assets/brand/kymaean-threshold-k-working-candidate.svg"
HARNESS = ROOT / "prototypes/sym-02/harness.html"
ASSETS = {
    "C0-R1": ROOT / "prototypes/sym-02/assets/c0-r1-bezier-fidelity.svg",
    "C0-R2": ROOT / "prototypes/sym-02/assets/c0-r2-curve-tension.svg",
    "C0-R3": ROOT / "prototypes/sym-02/assets/c0-r3-proportion.svg",
    "N1": ROOT / "prototypes/sym-02/assets/n1-counterform-junction.svg",
    "N2": ROOT / "prototypes/sym-02/assets/n2-tension-quartet.svg",
    "N3": ROOT / "prototypes/sym-02/assets/n3-emergent-spine.svg",
}
EXPECTED_PATHS = {"C0-R1": 3, "C0-R2": 3, "C0-R3": 3, "N1": 1, "N2": 4, "N3": 3}
EXPECTED_VIEWBOX = {"C0-R1": "0 0 170 233", "C0-R2": "0 0 170 233", "C0-R3": "0 0 170 233", "N1": "0 0 100 100", "N2": "0 0 100 100", "N3": "0 0 100 100"}
SVGNS = "{http://www.w3.org/2000/svg}"

def canonical_bytes(path: Path) -> bytes:
    return path.read_bytes().replace(b"\r\n", b"\n")


def parse_svg(path: Path):
    root = ET.fromstring(canonical_bytes(path))
    paths = root.findall(f".//{SVGNS}path")
    return root, paths


def fail(errors, message):
    errors.append(message)


def main() -> int:
    errors = []
    program = json.loads(PROGRAM.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("status") != "FROZEN_CANDIDATE_BYTES":
        fail(errors, "manifest status is not FROZEN_CANDIDATE_BYTES")
    c0_sha = hashlib.sha256(canonical_bytes(C0)).hexdigest()
    frozen_paths = {"C0-ORIGINAL": C0, **ASSETS}
    for ident, path in frozen_paths.items():
        expected = manifest.get("assets", {}).get(ident, {}).get("sha256")
        actual = hashlib.sha256(canonical_bytes(path)).hexdigest()
        if actual != expected:
            fail(errors, f"{ident}: frozen manifest hash mismatch {actual}")
    for key, path in (("program_contract", PROGRAM), ("harness", HARNESS), ("browser_probe", ROOT / "tools/sym02_browser_probe.mjs")):
        expected = manifest.get(key, {}).get("sha256")
        actual = hashlib.sha256(canonical_bytes(path)).hexdigest()
        if actual != expected:
            fail(errors, f"{key}: frozen manifest hash mismatch {actual}")
    if c0_sha != program["control"]["canonical_lf_sha256"]:
        fail(errors, f"C0 SHA mismatch: {c0_sha}")
    c0_root, c0_paths = parse_svg(C0)
    if len(c0_paths) != 3:
        fail(errors, "C0 path count changed")
    for ident, path in ASSETS.items():
        root, paths = parse_svg(path)
        if root.get("viewBox") != EXPECTED_VIEWBOX[ident]:
            fail(errors, f"{ident}: unexpected viewBox")
        if len(paths) != EXPECTED_PATHS[ident]:
            fail(errors, f"{ident}: unexpected path count {len(paths)}")
        if root.findall(f".//{SVGNS}text"):
            fail(errors, f"{ident}: text element forbidden")
        for elem in root.iter():
            for key, value in elem.attrib.items():
                if key.endswith("href"):
                    fail(errors, f"{ident}: external href forbidden")
                if key == "fill" and value not in ("currentColor", "none"):
                    fail(errors, f"{ident}: non-currentColor fill {value!r}")
                if key == "style" and ("#" in value or "rgb" in value.lower()):
                    fail(errors, f"{ident}: hard-coded style color")
    r1_paths = parse_svg(ASSETS["C0-R1"])[1]
    r2_paths = parse_svg(ASSETS["C0-R2"])[1]
    r3_paths = parse_svg(ASSETS["C0-R3"])[1]
    c0d = [p.get("d") for p in c0_paths]
    if r1_paths[2].get("d") != c0d[2]:
        fail(errors, "C0-R1: right field must remain exact C0")
    if [p.get("d") for p in r2_paths[:2]] != c0d[:2]:
        fail(errors, "C0-R2: both left fields must remain exact C0")
    if r3_paths[2].get("d") != c0d[2]:
        fail(errors, "C0-R3: right field must remain exact C0")
    if parse_svg(ASSETS["N1"])[1][0].get("fill-rule") != "evenodd":
        fail(errors, "N1: expected evenodd counterform construction")
    h = HARNESS.read_text(encoding="utf-8")
    for ident in ["C0-ORIGINAL", *ASSETS.keys()]:
        if ident not in h:
            fail(errors, f"harness missing {ident}")
    if "C0-R4" in h or "N4" in h:
        fail(errors, "reserved/post-batch candidate leaked into harness")
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: SYM-02 source/topology/C0-boundary verification clean")
    print("C0_SHA256:", c0_sha)
    for ident, path in ASSETS.items():
        print(f"{ident}_SHA256:", hashlib.sha256(canonical_bytes(path)).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
