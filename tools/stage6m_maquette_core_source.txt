#!/usr/bin/env python3
"""Deterministic Stage 6M neutral physical-maquette generator/validator.

Standard-library only. This tool is mechanism-neutral: it validates a 2.5D
manifest, computes uniform-density proxy centers of mass and support intervals,
solves optional horizontal-contact static cases, and emits a sanitized SVG plus
Director-side JSON report.
"""

from __future__ import annotations
import argparse
import json
import math
import pathlib
import sys
from dataclasses import dataclass
from typing import Any

EPS = 1e-9
FORMAT = "kymaean.hero.method02.stage6m/1"
FROZEN_PROJECTION = {
    "mode": "fixed_orthographic_oblique",
    "depth_dx": 0.035,
    "depth_dy": 0.025,
}
FROZEN_INSTRUMENTATION = {
    "base_gray": 184,
    "top_delta": 12,
    "side_delta": -12,
    "outline_gray": 150,
    "outline_width": 0.6,
}
FROZEN_SANITIZATION = {
    "transparent_background": True,
    "allow_text": False,
    "allow_ids": False,
    "allow_metadata": False,
    "allow_guides": False,
}

class ValidationError(ValueError):
    pass

def fail(msg: str) -> None:
    raise ValidationError(msg)

def load_json(path: pathlib.Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def dump_json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"

def polygon_area_centroid(points: list[list[float]]) -> tuple[float, float, float]:
    if len(points) < 3:
        fail("polygon requires at least three points")
    a2 = 0.0
    cx_num = 0.0
    cy_num = 0.0
    for i, p in enumerate(points):
        q = points[(i + 1) % len(points)]
        x0, y0 = p
        x1, y1 = q
        cross = x0 * y1 - x1 * y0
        a2 += cross
        cx_num += (x0 + x1) * cross
        cy_num += (y0 + y1) * cross
    area = a2 / 2.0
    if abs(area) <= EPS:
        fail("polygon area must be non-zero")
    cx = cx_num / (3.0 * a2)
    cy = cy_num / (3.0 * a2)
    return abs(area), cx, cy

def check_unit(v: float, label: str) -> None:
    if not isinstance(v, (int, float)) or not math.isfinite(v):
        fail(f"{label} must be a finite number")
    if v < -EPS or v > 1.0 + EPS:
        fail(f"{label} must be within [0,1]")

def check_four_decimals(v: float, label: str) -> None:
    if abs(float(v) - round(float(v), 4)) > 1e-10:
        fail(f"{label} must use at most four decimal places")

def validate_polygon(points: Any, label: str) -> list[list[float]]:
    if not isinstance(points, list) or len(points) < 3:
        fail(f"{label} must contain at least three points")
    out = []
    for i, p in enumerate(points):
        if not isinstance(p, list) or len(p) != 2:
            fail(f"{label}[{i}] must be [x,y]")
        x, y = p
        check_unit(x, f"{label}[{i}].x")
        check_unit(y, f"{label}[{i}].y")
        check_four_decimals(x, f"{label}[{i}].x")
        check_four_decimals(y, f"{label}[{i}].y")
        out.append([float(x), float(y)])
    polygon_area_centroid(out)
    return out

def signed_area(points: list[list[float]]) -> float:
    total = 0.0
    for i, p in enumerate(points):
        q = points[(i + 1) % len(points)]
        total += p[0] * q[1] - q[0] * p[1]
    return total / 2.0

def is_convex(points: list[list[float]]) -> bool:
    sign = 0
    n = len(points)
    for i in range(n):
        a, b, c = points[i], points[(i + 1) % n], points[(i + 2) % n]
        cross = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
        if abs(cross) <= EPS:
            continue
        current = 1 if cross > 0 else -1
        if sign == 0:
            sign = current
        elif current != sign:
            return False
    return sign != 0

def _line_intersection(s: list[float], e: list[float], a: list[float], b: list[float]) -> list[float]:
    dx1, dy1 = e[0] - s[0], e[1] - s[1]
    dx2, dy2 = b[0] - a[0], b[1] - a[1]
    denom = dx1 * dy2 - dy1 * dx2
    if abs(denom) <= EPS:
        return [e[0], e[1]]
    t = ((a[0] - s[0]) * dy2 - (a[1] - s[1]) * dx2) / denom
    return [s[0] + t * dx1, s[1] + t * dy1]

def convex_intersection(subject: list[list[float]], clip: list[list[float]]) -> list[list[float]]:
    if signed_area(clip) < 0:
        clip = list(reversed(clip))
    output = [list(p) for p in subject]
    for i, a in enumerate(clip):
        b = clip[(i + 1) % len(clip)]
        inp = output
        output = []
        if not inp:
            break
        def inside(p: list[float]) -> bool:
            return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= -EPS
        s = inp[-1]
        for e in inp:
            if inside(e):
                if not inside(s):
                    output.append(_line_intersection(s, e, a, b))
                output.append(e)
            elif inside(s):
                output.append(_line_intersection(s, e, a, b))
            s = e
    return output

def positive_overlap_area(p1: list[list[float]], p2: list[list[float]]) -> float:
    inter = convex_intersection(p1, p2)
    if len(inter) < 3:
        return 0.0
    return abs(signed_area(inter))

def point_in_polygon(point: list[float], polygon: list[list[float]]) -> bool:
    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % n]
        cross = (x - x0) * (y1 - y0) - (y - y0) * (x1 - x0)
        if abs(cross) <= 1e-8 and min(x0, x1) - EPS <= x <= max(x0, x1) + EPS and min(y0, y1) - EPS <= y <= max(y0, y1) + EPS:
            return True
        if ((y0 > y) != (y1 > y)):
            xin = (x1 - x0) * (y - y0) / (y1 - y0) + x0
            if x < xin:
                inside = not inside
    return inside

def point_in_proxy(point: list[float], proxy: dict[str, Any]) -> bool:
    x, y, z = point
    for s in proxy["solids"]:
        if float(s["z0"]) - EPS <= z <= float(s["z1"]) + EPS and point_in_polygon([x, y], s["polygon"]):
            return True
    return False

def validate_manifest(m: dict[str, Any]) -> None:
    required = [
        "format", "source_artboard", "projection", "instrumentation",
        "surface_volumes", "proxy_volumes", "contacts", "static_cases",
        "sanitization", "review"
    ]
    for key in required:
        if key not in m:
            fail(f"missing required key: {key}")
    if m["format"] != FORMAT:
        fail(f"format must be {FORMAT}")
    art = m["source_artboard"]
    if not isinstance(art, dict) or not isinstance(art.get("width"), int) or not isinstance(art.get("height"), int):
        fail("source_artboard width/height must be integers")
    if art["width"] <= 0 or art["height"] <= 0:
        fail("source_artboard dimensions must be positive")

    proj = m["projection"]
    if proj != FROZEN_PROJECTION:
        fail(f"projection must equal frozen method constants {FROZEN_PROJECTION}")

    inst = m["instrumentation"]
    if inst != FROZEN_INSTRUMENTATION:
        fail(f"instrumentation must equal frozen method constants {FROZEN_INSTRUMENTATION}")

    ids: set[str] = set()
    solid_ids: set[str] = set()
    proxy_ids: set[str] = set()

    def validate_solid(s: dict[str, Any], prefix: str) -> None:
        if set(s) - {"id", "polygon", "z0", "z1", "support_contact"}:
            fail(f"{prefix} contains unsupported keys")
        sid = s.get("id")
        if not isinstance(sid, str) or not sid:
            fail(f"{prefix}.id required")
        if sid in solid_ids:
            fail(f"duplicate solid id {sid}")
        solid_ids.add(sid)
        validate_polygon(s.get("polygon"), f"{prefix}.polygon")
        z0, z1 = s.get("z0"), s.get("z1")
        check_unit(z0, f"{prefix}.z0")
        check_unit(z1, f"{prefix}.z1")
        check_four_decimals(z0, f"{prefix}.z0")
        check_four_decimals(z1, f"{prefix}.z1")
        if not z1 > z0:
            fail(f"{prefix}.z1 must exceed z0")
        if "support_contact" in s and not isinstance(s["support_contact"], bool):
            fail(f"{prefix}.support_contact must be boolean")

    if not isinstance(m["surface_volumes"], list) or not m["surface_volumes"]:
        fail("surface_volumes must be a non-empty list")
    for i, vol in enumerate(m["surface_volumes"]):
        if set(vol) != {"id", "solids"}:
            fail(f"surface_volumes[{i}] must contain id, solids")
        vid = vol["id"]
        if not isinstance(vid, str) or not vid or vid in ids:
            fail(f"invalid/duplicate volume id {vid!r}")
        ids.add(vid)
        if not isinstance(vol["solids"], list) or not vol["solids"]:
            fail(f"surface volume {vid} requires solids")
        for j, s in enumerate(vol["solids"]):
            validate_solid(s, f"surface_volumes[{i}].solids[{j}]")

    if not isinstance(m["proxy_volumes"], list) or not m["proxy_volumes"]:
        fail("proxy_volumes must be a non-empty list")
    for i, vol in enumerate(m["proxy_volumes"]):
        if set(vol) != {"id", "density", "solids"}:
            fail(f"proxy_volumes[{i}] must contain id, density, solids")
        vid = vol["id"]
        if not isinstance(vid, str) or not vid or vid in ids:
            fail(f"invalid/duplicate volume id {vid!r}")
        ids.add(vid); proxy_ids.add(vid)
        if vol["density"] != "uniform":
            fail(f"proxy {vid} density must be uniform")
        if not isinstance(vol["solids"], list) or not vol["solids"]:
            fail(f"proxy {vid} requires solids")
        support_count = 0
        for j, s in enumerate(vol["solids"]):
            validate_solid(s, f"proxy_volumes[{i}].solids[{j}]")
            if not is_convex(s["polygon"]):
                fail(f"proxy {vid} solid {s['id']} polygon must be convex")
            support_count += int(bool(s.get("support_contact", False)))
        if support_count == 0:
            fail(f"proxy {vid} requires at least one support_contact solid")
        solids = vol["solids"]
        for a_idx in range(len(solids)):
            for b_idx in range(a_idx + 1, len(solids)):
                sa, sb = solids[a_idx], solids[b_idx]
                z_overlap = min(float(sa["z1"]), float(sb["z1"])) - max(float(sa["z0"]), float(sb["z0"]))
                if z_overlap > EPS and positive_overlap_area(sa["polygon"], sb["polygon"]) > 1e-10:
                    fail(f"proxy {vid} solids {sa['id']} and {sb['id']} overlap in volume; mass solids must be interior-disjoint")

    proxy_by_id = {p["id"]: p for p in m["proxy_volumes"]}

    contact_ids: set[str] = set()
    if not isinstance(m["contacts"], list):
        fail("contacts must be a list")
    for i, c in enumerate(m["contacts"]):
        if set(c) != {"id", "a", "b", "point_a", "point_b", "axis"}:
            fail(f"contacts[{i}] schema mismatch")
        cid = c["id"]
        if not isinstance(cid, str) or not cid or cid in contact_ids:
            fail(f"invalid/duplicate contact id {cid!r}")
        contact_ids.add(cid)
        if c["a"] not in proxy_ids or c["b"] not in proxy_ids or c["a"] == c["b"]:
            fail(f"contact {cid} participants must be distinct proxy ids")
        for pkey in ("point_a", "point_b"):
            p = c[pkey]
            if not isinstance(p, list) or len(p) != 3:
                fail(f"contact {cid}.{pkey} must be [x,y,z]")
            for axis, val in zip("xyz", p):
                check_unit(val, f"contact {cid}.{pkey}.{axis}")
                check_four_decimals(val, f"contact {cid}.{pkey}.{axis}")
        if c["axis"] != "horizontal_x":
            fail(f"contact {cid} axis must be horizontal_x")
        if any(abs(float(a) - float(b)) > 1e-8 for a, b in zip(c["point_a"], c["point_b"])):
            fail(f"contact {cid} points must coincide; contact must be embodied as actual adjacency")
        if not point_in_proxy(c["point_a"], proxy_by_id[c["a"]]):
            fail(f"contact {cid} point is not contained by proxy {c['a']}")
        if not point_in_proxy(c["point_b"], proxy_by_id[c["b"]]):
            fail(f"contact {cid} point is not contained by proxy {c['b']}")

    if not isinstance(m["static_cases"], list):
        fail("static_cases must be a list")
    case_ids: set[str] = set()
    for i, case in enumerate(m["static_cases"]):
        expected = {"id", "kind", "proxy", "expected", "minimum_margin", "contact_id", "target_cop_x", "counterparty"}
        if set(case) != expected:
            fail(f"static_cases[{i}] schema mismatch")
        cid = case["id"]
        if not isinstance(cid, str) or not cid or cid in case_ids:
            fail(f"invalid/duplicate static case id {cid!r}")
        case_ids.add(cid)
        if case["kind"] not in {"unsupported", "supported_pair"}:
            fail(f"static case {cid} has unknown kind")
        if case["proxy"] not in proxy_ids:
            fail(f"static case {cid} proxy unknown")
        if case["expected"] not in {"stable", "unstable"}:
            fail(f"static case {cid} expected invalid")
        if not isinstance(case["minimum_margin"], (int, float)) or case["minimum_margin"] < 0:
            fail(f"static case {cid} minimum_margin invalid")
        check_four_decimals(case["minimum_margin"], f"static case {cid}.minimum_margin")
        if case["kind"] == "unsupported":
            if any(case[k] is not None for k in ("contact_id", "target_cop_x", "counterparty")):
                fail(f"unsupported case {cid} must use null contact fields")
        else:
            if case["contact_id"] not in contact_ids:
                fail(f"supported_pair case {cid} contact_id unknown")
            check_unit(case["target_cop_x"], f"static case {cid}.target_cop_x")
            check_four_decimals(case["target_cop_x"], f"static case {cid}.target_cop_x")
            if case["counterparty"] not in proxy_ids or case["counterparty"] == case["proxy"]:
                fail(f"supported_pair case {cid} counterparty invalid")

    san = m["sanitization"]
    if san != FROZEN_SANITIZATION:
        fail(f"sanitization must equal frozen fail-closed values {FROZEN_SANITIZATION}")

    review = m["review"]
    if set(review) != {"maquette_leakage", "surface_read", "transfer_eligible"}:
        fail("review schema mismatch")
    if review["maquette_leakage"] not in {"UNASSESSED", "PASS", "FAIL"}:
        fail("review.maquette_leakage invalid")
    if review["surface_read"] not in {"UNASSESSED", "PASS", "FAIL"}:
        fail("review.surface_read invalid")
    if not isinstance(review["transfer_eligible"], bool):
        fail("review.transfer_eligible must be boolean")
    if review["transfer_eligible"] and (
        review["maquette_leakage"] != "PASS" or review["surface_read"] != "PASS"
    ):
        fail("transfer_eligible=true requires both human review gates PASS")

@dataclass
class SolidMass:
    volume: float
    cx: float
    cy: float
    cz: float

def solid_mass(s: dict[str, Any]) -> SolidMass:
    area, cx, cy = polygon_area_centroid(s["polygon"])
    depth = float(s["z1"]) - float(s["z0"])
    return SolidMass(area * depth, cx, cy, (float(s["z0"]) + float(s["z1"])) / 2.0)

def proxy_metrics(proxy: dict[str, Any]) -> dict[str, Any]:
    masses = [solid_mass(s) for s in proxy["solids"]]
    total = sum(m.volume for m in masses)
    if total <= EPS:
        fail(f"proxy {proxy['id']} has zero volume")
    cx = sum(m.volume * m.cx for m in masses) / total
    cy = sum(m.volume * m.cy for m in masses) / total
    cz = sum(m.volume * m.cz for m in masses) / total
    supports = [s for s in proxy["solids"] if s.get("support_contact", False)]
    sx = [p[0] for s in supports for p in s["polygon"]]
    sz0 = min(float(s["z0"]) for s in supports)
    sz1 = max(float(s["z1"]) for s in supports)
    sy = max(p[1] for s in supports for p in s["polygon"])
    return {
        "volume": total,
        "com": [cx, cy, cz],
        "support_x": [min(sx), max(sx)],
        "support_z": [sz0, sz1],
        "support_y": sy,
    }

def margin_inside(x: float, interval: list[float]) -> float:
    lo, hi = interval
    if x < lo:
        return x - lo
    if x > hi:
        return hi - x
    return min(x - lo, hi - x)

def evaluate_cases(m: dict[str, Any], metrics: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    contacts = {c["id"]: c for c in m["contacts"]}
    out = []
    for case in m["static_cases"]:
        pm = metrics[case["proxy"]]
        if case["kind"] == "unsupported":
            margin = margin_inside(pm["com"][0], pm["support_x"])
            actual = "stable" if margin >= case["minimum_margin"] - EPS else "unstable"
            passed = actual == case["expected"]
            out.append({
                "id": case["id"],
                "kind": case["kind"],
                "proxy": case["proxy"],
                "computed_margin": margin,
                "actual": actual,
                "expected": case["expected"],
                "pass": passed,
            })
            continue

        c = contacts[case["contact_id"]]
        if c["a"] == case["proxy"]:
            p_self, p_other = c["point_a"], c["point_b"]
        elif c["b"] == case["proxy"]:
            p_self, p_other = c["point_b"], c["point_a"]
        else:
            fail(f"contact {c['id']} does not include proxy {case['proxy']}")

        target = float(case["target_cop_x"])
        lo, hi = pm["support_x"]
        if not lo - EPS <= target <= hi + EPS:
            fail(f"case {case['id']} target COP outside support interval")
        lever = pm["support_y"] - float(p_self[1])
        if lever <= EPS:
            fail(f"case {case['id']} contact must be above support")
        weight = pm["volume"]
        fx = -(pm["com"][0] - target) * weight / lever

        other_id = case["counterparty"]
        om = metrics[other_id]
        other_lever = om["support_y"] - float(p_other[1])
        if other_lever <= EPS:
            fail(f"case {case['id']} counterparty contact must be above support")
        fx_other = -fx
        resultant_other_x = om["com"][0] + other_lever * fx_other / om["volume"]
        other_margin = margin_inside(resultant_other_x, om["support_x"])

        self_margin = margin_inside(target, pm["support_x"])
        pair_stable = (
            self_margin >= case["minimum_margin"] - EPS
            and other_margin >= case["minimum_margin"] - EPS
        )
        actual = "stable" if pair_stable else "unstable"
        out.append({
            "id": case["id"],
            "kind": case["kind"],
            "proxy": case["proxy"],
            "counterparty": other_id,
            "required_fx_on_proxy": fx,
            "fx_fraction_of_proxy_weight": fx / weight,
            "target_cop_x": target,
            "proxy_margin": self_margin,
            "counterparty_resultant_x": resultant_other_x,
            "counterparty_margin": other_margin,
            "actual": actual,
            "expected": case["expected"],
            "pass": actual == case["expected"],
        })
    return out

def gray(v: int) -> str:
    v = max(0, min(255, int(v)))
    return f"#{v:02x}{v:02x}{v:02x}"

def fmt(v: float) -> str:
    s = f"{v:.4f}".rstrip("0").rstrip(".")
    return s if s else "0"

def project(p: list[float], z: float, art: dict[str, int], proj: dict[str, float]) -> tuple[float, float]:
    x, y = p
    sx = (x + z * proj["depth_dx"]) * art["width"]
    sy = (y - z * proj["depth_dy"]) * art["height"]
    return sx, sy

def polygon_str(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{fmt(x)},{fmt(y)}" for x, y in points)

def solid_svg_faces(s: dict[str, Any], art: dict[str, int], proj: dict[str, float],
                    inst: dict[str, Any]) -> list[str]:
    pts = s["polygon"]
    z0, z1 = float(s["z0"]), float(s["z1"])
    front = [project(p, z0, art, proj) for p in pts]
    back = [project(p, z1, art, proj) for p in pts]
    base = inst["base_gray"]
    top_fill = gray(base + inst["top_delta"])
    side_fill = gray(base + inst["side_delta"])
    front_fill = gray(base)
    stroke = gray(inst["outline_gray"])
    sw = fmt(float(inst["outline_width"]))

    faces: list[str] = []
    faces.append(
        f'<polygon points="{polygon_str(back)}" fill="{top_fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )
    n = len(pts)
    for i in range(n):
        j = (i + 1) % n
        quad = [front[i], front[j], back[j], back[i]]
        faces.append(
            f'<polygon points="{polygon_str(quad)}" fill="{side_fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )
    faces.append(
        f'<polygon points="{polygon_str(front)}" fill="{front_fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )
    return faces

def render_svg(m: dict[str, Any]) -> str:
    art = m["source_artboard"]
    proj = m["projection"]
    inst = m["instrumentation"]
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{art["width"]}" height="{art["height"]}" viewBox="0 0 {art["width"]} {art["height"]}">'
    ]
    for group in (m["surface_volumes"], m["proxy_volumes"]):
        for vol in group:
            for s in vol["solids"]:
                lines.extend("  " + face for face in solid_svg_faces(s, art, proj, inst))
    lines.append("</svg>")
    return "\n".join(lines) + "\n"

def rounded(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 8)
    if isinstance(value, list):
        return [rounded(v) for v in value]
    if isinstance(value, dict):
        return {k: rounded(v) for k, v in value.items()}
    return value

def build_report(m: dict[str, Any]) -> dict[str, Any]:
    metrics = {p["id"]: proxy_metrics(p) for p in m["proxy_volumes"]}
    cases = evaluate_cases(m, metrics)
    automated_pass = all(c["pass"] for c in cases)
    review = m["review"]
    transfer_eligible = (
        automated_pass
        and review["maquette_leakage"] == "PASS"
        and review["surface_read"] == "PASS"
        and review["transfer_eligible"] is True
    )
    return rounded({
        "format": FORMAT,
        "automated_validation_pass": automated_pass,
        "proxy_metrics": metrics,
        "static_cases": cases,
        "human_review": {
            "maquette_leakage": review["maquette_leakage"],
            "surface_read": review["surface_read"],
        },
        "transfer_eligible": transfer_eligible,
        "sanitization": m["sanitization"],
    })

def validate_sanitized_svg(svg: str) -> None:
    forbidden = ("<text", "<metadata", "<title", "<desc", " id=", "<!--", "<style", "<rect")
    for token in forbidden:
        if token in svg:
            fail(f"sanitized SVG contains forbidden token {token!r}")
    allowed_tags = ("<svg ", "<polygon ", "</svg>")
    for line in svg.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if not any(stripped.startswith(tag) for tag in allowed_tags):
            fail(f"sanitized SVG contains non-whitelisted element: {stripped[:40]}")

def deterministic_bytes(m: dict[str, Any]) -> tuple[str, str]:
    validate_manifest(m)
    report = build_report(m)
    svg = render_svg(m)
    validate_sanitized_svg(svg)
    return svg, dump_json(report)

def cmd_generate(args: argparse.Namespace) -> int:
    m = load_json(pathlib.Path(args.manifest))
    svg, report = deterministic_bytes(m)
    pathlib.Path(args.svg).write_text(svg, encoding="utf-8", newline="\n")
    pathlib.Path(args.report).write_text(report, encoding="utf-8", newline="\n")
    return 0

def cmd_validate(args: argparse.Namespace) -> int:
    m = load_json(pathlib.Path(args.manifest))
    svg, report = deterministic_bytes(m)
    rep = json.loads(report)
    if not rep["automated_validation_pass"]:
        fail("one or more static cases failed")
    if args.expected_svg:
        actual = pathlib.Path(args.expected_svg).read_text(encoding="utf-8")
        if actual != svg:
            fail("committed SVG differs from deterministic generator output")
    if args.expected_report:
        actual = pathlib.Path(args.expected_report).read_text(encoding="utf-8")
        if actual != report:
            fail("committed report differs from deterministic generator output")
    print("Stage 6M validation PASS")
    print(f"transfer_eligible={rep['transfer_eligible']}")
    return 0

def self_test() -> None:
    area, cx, cy = polygon_area_centroid([[0,0],[1,0],[1,1],[0,1]])
    assert abs(area - 1.0) < EPS and abs(cx - 0.5) < EPS and abs(cy - 0.5) < EPS

def main() -> int:
    self_test()
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("manifest")
    g.add_argument("--svg", required=True)
    g.add_argument("--report", required=True)
    g.set_defaults(func=cmd_generate)
    v = sub.add_parser("validate")
    v.add_argument("manifest")
    v.add_argument("--expected-svg")
    v.add_argument("--expected-report")
    v.set_defaults(func=cmd_validate)
    args = p.parse_args()
    try:
        return args.func(args)
    except ValidationError as e:
        print(f"Stage 6M validation FAIL: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
