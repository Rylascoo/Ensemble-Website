#!/usr/bin/env python3
import hashlib
import json
import pathlib
import sys
import xml.etree.ElementTree as ET
from fractions import Fraction

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from stage6m_maquette import deterministic_bytes

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/evidence/stage6m/C08-EWTF-01_STAGE6M_MANIFEST.json"
REPORT_PATH = ROOT / "docs/evidence/stage6m/C08-EWTF-01_STAGE6M_REPORT.json"
SCAFFOLD_MANIFEST_PATH = ROOT / "docs/evidence/scaffolds/C08-EWTF-01_STAGE06_NEUTRAL_GEOMETRY_SCAFFOLD_MANIFEST.json"
SCAFFOLD_SVG_PATH = ROOT / "docs/evidence/scaffolds/C08-EWTF-01_STAGE06_NEUTRAL_GEOMETRY_SCAFFOLD.svg"

EXPECTED_SVG_SHA256 = "54d34361fb597a1ba67ef493ec7d8b189a4680a1e1e54c753de7fba30c9f15db"
EXPECTED_REPORT_SHA256 = "064f4e94072089c0b9266c0943d99578398345e68f873948fabeaeefdd9099bc"
EXPECTED_STAGE6_CLEARANCE_PX = Fraction(514, 5)  # 102.8 px exactly
EXPECTED_STAGE6_CLEARANCE_BASIS = "exact_integer_stage6_svg_polyline_at_registered_left_support_root"


def _exact_stage6_clearance_px():
    root = ET.parse(SCAFFOLD_SVG_PATH).getroot()
    upper = root.find(".//*[@id='field-free-edge-upper']")
    support_root = root.find(".//*[@id='B-left-root-changed']")
    assert upper is not None
    assert support_root is not None

    points = []
    for token in upper.attrib["points"].split():
        x, y = token.split(",")
        points.append((Fraction(x), Fraction(y)))

    root_x = Fraction(support_root.attrib["cx"])
    root_y = Fraction(support_root.attrib["cy"])
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 == x1 or not min(x0, x1) <= root_x <= max(x0, x1):
            continue
        edge_y = y0 + (root_x - x0) * (y1 - y0) / (x1 - x0)
        return edge_y - root_y
    raise AssertionError(f"no Stage 6 source segment brackets x={root_x}")


def main():
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    svg, report_text = deterministic_bytes(manifest)
    svg_sha = hashlib.sha256(svg.encode("utf-8")).hexdigest()
    report_sha = hashlib.sha256(report_text.encode("utf-8")).hexdigest()
    assert svg_sha == EXPECTED_SVG_SHA256, svg_sha
    assert report_sha == EXPECTED_REPORT_SHA256, report_sha
    assert REPORT_PATH.read_text(encoding="utf-8") == report_text

    report = json.loads(report_text)
    assert report["automated_validation_pass"] is True
    assert report["transfer_eligible"] is True
    assert report["human_review"]["maquette_leakage"] == "PASS"
    assert report["human_review"]["surface_read"] == "PASS"

    cases = {case["id"]: case for case in report["static_cases"]}
    assert cases["A-unsupported"]["computed_margin_source_px"] >= 75.0
    assert -cases["B-unsupported"]["computed_margin_source_px"] >= 25.0
    assert cases["B-supported-by-A"]["proxy_margin_source_px"] >= 5.0
    assert cases["B-supported-by-A"]["counterparty_margin_source_px"] >= 40.0

    width = float(manifest["source_artboard"]["width"])
    height = float(manifest["source_artboard"]["height"])
    a = report["proxy_metrics"]["A"]
    fx_fraction = abs(cases["B-supported-by-A"]["fx_fraction_of_proxy_weight"])
    contact_y = float(manifest["contacts"][0]["point_a"][1])
    lever_px = (float(a["support_y_range"][1]) - contact_y) * height
    sensitivity_shift_px = lever_px * fx_fraction * 2.0
    sensitivity_x = float(a["com"][0]) - sensitivity_shift_px / width
    sensitivity_margin_px = min(
        sensitivity_x - float(a["support_x"][0]),
        float(a["support_x"][1]) - sensitivity_x,
    ) * width
    assert sensitivity_margin_px >= 40.0, sensitivity_margin_px

    proxies = {proxy["id"]: proxy for proxy in manifest["proxy_volumes"]}
    a_head = next(s for s in proxies["A"]["solids"] if s["id"] == "A-head")
    b_head = next(s for s in proxies["B"]["solids"] if s["id"] == "B-head")
    a_right = max(float(p[0]) for p in a_head["polygon"])
    b_left = min(float(p[0]) for p in b_head["polygon"])
    head_gap_px = (b_left - a_right) * width
    assert head_gap_px >= 50.0, head_gap_px

    scaffold = json.loads(SCAFFOLD_MANIFEST_PATH.read_text(encoding="utf-8"))
    audit = scaffold["audit_only_constraints"]
    assert Fraction(str(audit["B_support_to_free_edge_clearance_px"])) == EXPECTED_STAGE6_CLEARANCE_PX
    assert audit["B_support_to_free_edge_clearance_basis"] == EXPECTED_STAGE6_CLEARANCE_BASIS
    minimum_clearance_px = Fraction(str(audit["minimum_projected_support_to_free_edge_clearance_px"]))
    assert minimum_clearance_px == 100

    exact_stage6_clearance_px = _exact_stage6_clearance_px()
    assert exact_stage6_clearance_px == EXPECTED_STAGE6_CLEARANCE_PX, exact_stage6_clearance_px
    assert exact_stage6_clearance_px >= minimum_clearance_px

    b_foot = next(s for s in proxies["B"]["solids"] if s["id"] == "B-left-foot")
    foot_xs = [float(p[0]) for p in b_foot["polygon"]]
    foot_ys = [float(p[1]) for p in b_foot["polygon"]]
    physical_root_x = (min(foot_xs) + max(foot_xs)) / 2.0
    physical_root_y = max(foot_ys)
    candidates = []
    for solid in manifest["surface_volumes"][0]["solids"]:
        if not solid["id"].startswith("top-"):
            continue
        polygon = solid["polygon"]
        for p0, p1 in zip(polygon, polygon[1:] + polygon[:1]):
            x0, y0 = map(float, p0)
            x1, y1 = map(float, p1)
            if x0 == x1 or min(y0, y1) <= physical_root_y + 0.05:
                continue
            if min(x0, x1) <= physical_root_x <= max(x0, x1):
                candidates.append(y0 + (physical_root_x - x0) * (y1 - y0) / (x1 - x0))
    assert candidates
    physical_clearance_px = (min(candidates) - physical_root_y) * height
    assert physical_clearance_px >= float(minimum_clearance_px), physical_clearance_px

    print("C08 SVG SHA256", svg_sha)
    print("C08 report SHA256", report_sha)
    print("C08 2:1 sensitivity margin source px", sensitivity_margin_px)
    print("C08 projected head gap source px", head_gap_px)
    print("C08 exact Stage 6 support-root edge clearance source px", float(exact_stage6_clearance_px))
    print("C08 Stage 6M support-root edge clearance source px", physical_clearance_px)


if __name__ == "__main__":
    main()
