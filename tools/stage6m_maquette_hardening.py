"""Fail-closed physical/statics hardening for the Stage 6M base generator."""
from __future__ import annotations
from typing import Any
import stage6m_maquette_core as core

EPS = core.EPS
FORMAT = core.FORMAT
FROZEN_PROJECTION = core.FROZEN_PROJECTION
FROZEN_INSTRUMENTATION = core.FROZEN_INSTRUMENTATION
FROZEN_SANITIZATION = core.FROZEN_SANITIZATION
ValidationError = core.ValidationError
fail = core.fail
_base_validate_manifest = core.validate_manifest


def point_on_polygon_boundary(point: list[float], polygon: list[list[float]]) -> bool:
    x, y = point
    for i in range(len(polygon)):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % len(polygon)]
        cross = (x - x0) * (y1 - y0) - (y - y0) * (x1 - x0)
        if (abs(cross) <= 1e-8 and min(x0, x1) - EPS <= x <= max(x0, x1) + EPS
                and min(y0, y1) - EPS <= y <= max(y0, y1) + EPS):
            return True
    return False


def boundary_contact_points(p1: list[list[float]], p2: list[list[float]]) -> list[list[float]]:
    found: list[list[float]] = []
    for p in p1:
        if point_on_polygon_boundary(p, p2):
            found.append([float(p[0]), float(p[1])])
    for p in p2:
        if point_on_polygon_boundary(p, p1):
            found.append([float(p[0]), float(p[1])])
    unique: list[list[float]] = []
    for p in found:
        if not any(abs(p[0] - q[0]) <= 1e-8 and abs(p[1] - q[1]) <= 1e-8 for q in unique):
            unique.append(p)
    return unique


def solids_share_boundary(a: dict[str, Any], b: dict[str, Any]) -> bool:
    z_overlap = min(float(a["z1"]), float(b["z1"])) - max(float(a["z0"]), float(b["z0"]))
    return z_overlap > EPS and len(boundary_contact_points(a["polygon"], b["polygon"])) >= 2


def solids_connected(solids: list[dict[str, Any]]) -> bool:
    if not solids:
        return False
    seen = {0}
    frontier = [0]
    while frontier:
        i = frontier.pop()
        for j in range(len(solids)):
            if j not in seen and solids_share_boundary(solids[i], solids[j]):
                seen.add(j)
                frontier.append(j)
    return len(seen) == len(solids)


def _positive_volume_overlap(a: dict[str, Any], b: dict[str, Any]) -> bool:
    z_overlap = min(float(a["z1"]), float(b["z1"])) - max(float(a["z0"]), float(b["z0"]))
    return z_overlap > EPS and core.positive_overlap_area(a["polygon"], b["polygon"]) > 1e-10


def validate_manifest(m: dict[str, Any]) -> None:
    _base_validate_manifest(m)
    surfaces = m["surface_volumes"]
    if len(surfaces) != 1:
        fail("surface_volumes must contain exactly one shared surface volume")
    surface = surfaces[0]
    surface_solids = surface["solids"]
    for s in surface_solids:
        if not core.is_convex(s["polygon"]):
            fail(f"surface {surface['id']} solid {s['id']} polygon must be convex")
    for i in range(len(surface_solids)):
        for j in range(i + 1, len(surface_solids)):
            if _positive_volume_overlap(surface_solids[i], surface_solids[j]):
                fail(f"surface solids {surface_solids[i]['id']} and {surface_solids[j]['id']} overlap in volume")
    if not solids_connected(surface_solids):
        fail(f"surface volume {surface['id']} solids must form one boundary-connected physical volume")
    proxies = m["proxy_volumes"]
    for proxy in proxies:
        if not solids_connected(proxy["solids"]):
            fail(f"proxy {proxy['id']} solids must form one boundary-connected physical volume")
    for i in range(len(proxies)):
        for j in range(i + 1, len(proxies)):
            for a in proxies[i]["solids"]:
                for b in proxies[j]["solids"]:
                    if _positive_volume_overlap(a, b):
                        fail(f"proxies {proxies[i]['id']} and {proxies[j]['id']} interpenetrate at solids {a['id']} / {b['id']}")
    for proxy in proxies:
        for solid in proxy["solids"]:
            for surface_solid in surface_solids:
                if _positive_volume_overlap(solid, surface_solid):
                    fail(f"proxy {proxy['id']} solid {solid['id']} penetrates shared surface solid {surface_solid['id']}")
            if solid.get("support_contact", False):
                points: list[list[float]] = []
                for surface_solid in surface_solids:
                    z_overlap = min(float(solid["z1"]), float(surface_solid["z1"])) - max(float(solid["z0"]), float(surface_solid["z0"]))
                    if z_overlap > EPS:
                        points.extend(boundary_contact_points(solid["polygon"], surface_solid["polygon"]))
                unique: list[list[float]] = []
                for p in points:
                    if not any(abs(p[0] - q[0]) <= 1e-8 and abs(p[1] - q[1]) <= 1e-8 for q in unique):
                        unique.append(p)
                if len(unique) < 2:
                    fail(f"support solid {solid['id']} must share at least two boundary vertices with the shared surface")


def proxy_metrics(proxy: dict[str, Any], surface_solids: list[dict[str, Any]]) -> dict[str, Any]:
    masses = [core.solid_mass(s) for s in proxy["solids"]]
    total = sum(m.volume for m in masses)
    if total <= EPS:
        fail(f"proxy {proxy['id']} has zero volume")
    cx = sum(m.volume * m.cx for m in masses) / total
    cy = sum(m.volume * m.cy for m in masses) / total
    cz = sum(m.volume * m.cz for m in masses) / total
    contact_points: list[list[float]] = []
    z_ranges: list[tuple[float, float]] = []
    for support in (s for s in proxy["solids"] if s.get("support_contact", False)):
        for surface in surface_solids:
            z0 = max(float(support["z0"]), float(surface["z0"]))
            z1 = min(float(support["z1"]), float(surface["z1"]))
            if z1 - z0 <= EPS:
                continue
            points = boundary_contact_points(support["polygon"], surface["polygon"])
            if len(points) >= 2:
                contact_points.extend(points)
                z_ranges.append((z0, z1))
    unique: list[list[float]] = []
    for p in contact_points:
        if not any(abs(p[0] - q[0]) <= 1e-8 and abs(p[1] - q[1]) <= 1e-8 for q in unique):
            unique.append(p)
    if len(unique) < 2 or not z_ranges:
        fail(f"proxy {proxy['id']} has no valid shared-surface support boundary")
    xs = [p[0] for p in unique]
    ys = [p[1] for p in unique]
    return {"volume": total, "com": [cx, cy, cz], "support_x": [min(xs), max(xs)],
            "support_y_range": [min(ys), max(ys)],
            "support_z": [min(z[0] for z in z_ranges), max(z[1] for z in z_ranges)],
            "support_contact_points": unique}


def evaluate_cases(m: dict[str, Any], metrics: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    contacts = {c["id"]: c for c in m["contacts"]}
    width = float(m["source_artboard"]["width"])
    height = float(m["source_artboard"]["height"])
    out: list[dict[str, Any]] = []
    for case in m["static_cases"]:
        pm = metrics[case["proxy"]]
        if case["kind"] == "unsupported":
            margin = core.margin_inside(pm["com"][0], pm["support_x"])
            actual = "stable" if margin >= 0.0 else "unstable"
            if case["expected"] == "stable":
                passed = actual == "stable" and margin >= case["minimum_margin"] - EPS
            else:
                passed = actual == "unstable" and -margin >= case["minimum_margin"] - EPS
            out.append({"id": case["id"], "kind": case["kind"], "proxy": case["proxy"],
                        "computed_margin": margin, "computed_margin_source_px": margin * width,
                        "actual": actual, "expected": case["expected"],
                        "minimum_margin": case["minimum_margin"], "pass": passed})
            continue
        contact = contacts[case["contact_id"]]
        if contact["a"] == case["proxy"]:
            p_self, p_other = contact["point_a"], contact["point_b"]
        elif contact["b"] == case["proxy"]:
            p_self, p_other = contact["point_b"], contact["point_a"]
        else:
            fail(f"contact {contact['id']} does not include proxy {case['proxy']}")
        target = float(case["target_cop_x"])
        lo, hi = pm["support_x"]
        if not lo - EPS <= target <= hi + EPS:
            fail(f"case {case['id']} target COP outside support interval")
        lever = pm["support_y_range"][0] - float(p_self[1])
        if lever <= EPS:
            fail(f"case {case['id']} contact must be above all support contact geometry")
        weight = pm["volume"]
        horizontal_arm_px = (pm["com"][0] - target) * width
        vertical_arm_px = lever * height
        fx = -horizontal_arm_px * weight / vertical_arm_px
        other_id = case["counterparty"]
        om = metrics[other_id]
        other_lever = om["support_y_range"][1] - float(p_other[1])
        if other_lever <= EPS:
            fail(f"case {case['id']} counterparty contact must be above all support contact geometry")
        fx_other = -fx
        other_shift_x = (other_lever * height * fx_other / om["volume"]) / width
        resultant_other_x = om["com"][0] + other_shift_x
        other_margin = core.margin_inside(resultant_other_x, om["support_x"])
        self_margin = core.margin_inside(target, pm["support_x"])
        actual = "stable" if self_margin >= 0.0 and other_margin >= 0.0 else "unstable"
        if case["expected"] == "stable":
            passed = actual == "stable" and self_margin >= case["minimum_margin"] - EPS and other_margin >= case["minimum_margin"] - EPS
        else:
            passed = actual == "unstable" and -min(self_margin, other_margin) >= case["minimum_margin"] - EPS
        out.append({"id": case["id"], "kind": case["kind"], "proxy": case["proxy"],
                    "counterparty": other_id, "required_fx_on_proxy": fx,
                    "fx_fraction_of_proxy_weight": fx / weight, "target_cop_x": target,
                    "proxy_margin": self_margin, "proxy_margin_source_px": self_margin * width,
                    "counterparty_resultant_x": resultant_other_x, "counterparty_margin": other_margin,
                    "counterparty_margin_source_px": other_margin * width, "actual": actual,
                    "expected": case["expected"], "minimum_margin": case["minimum_margin"], "pass": passed})
    return out


def build_report(m: dict[str, Any]) -> dict[str, Any]:
    surface_solids = [s for v in m["surface_volumes"] for s in v["solids"]]
    metrics = {p["id"]: proxy_metrics(p, surface_solids) for p in m["proxy_volumes"]}
    cases = evaluate_cases(m, metrics)
    automated_pass = all(c["pass"] for c in cases)
    review = m["review"]
    transfer_eligible = automated_pass and review["maquette_leakage"] == "PASS" and review["surface_read"] == "PASS" and review["transfer_eligible"] is True
    return core.rounded({"format": FORMAT, "source_artboard": m["source_artboard"],
                         "automated_validation_pass": automated_pass, "proxy_metrics": metrics,
                         "static_cases": cases,
                         "human_review": {"maquette_leakage": review["maquette_leakage"],
                                          "surface_read": review["surface_read"]},
                         "transfer_eligible": transfer_eligible, "sanitization": m["sanitization"]})


def apply_hardening() -> None:
    core.validate_manifest = validate_manifest
    core.build_report = build_report


apply_hardening()
deterministic_bytes = core.deterministic_bytes


def main() -> int:
    return core.main()


if __name__ == "__main__":
    raise SystemExit(main())
