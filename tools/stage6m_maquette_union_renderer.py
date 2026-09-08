"""Mechanism-neutral physical-union renderer for Stage 6M sanitized output.

Convex pieces remain separate for validation/statics, but same-volume internal
bookkeeping boundaries must not become physical seams in transferable pixels.
"""
from __future__ import annotations
from typing import Any
import stage6m_maquette_core as core

EPS = core.EPS


def _fmt(value: float) -> str:
    value = round(float(value), 6)
    if abs(value) < 5e-10:
        value = 0.0
    return f"{value:.6f}".rstrip("0").rstrip(".") or "0"


def _gray(value: int) -> str:
    value = int(value)
    return f"#{value:02x}{value:02x}{value:02x}"


def _sub(a: list[float] | tuple[float, float], b: list[float] | tuple[float, float]) -> tuple[float, float]:
    return float(a[0]) - float(b[0]), float(a[1]) - float(b[1])


def _dot(a: tuple[float, float], b: tuple[float, float]) -> float:
    return a[0] * b[0] + a[1] * b[1]


def _cross(a: tuple[float, float], b: tuple[float, float]) -> float:
    return a[0] * b[1] - a[1] * b[0]


def _point(a: list[float], b: list[float], t: float) -> tuple[float, float]:
    return float(a[0]) + (float(b[0]) - float(a[0])) * t, float(a[1]) + (float(b[1]) - float(a[1])) * t


def _collinear_overlap_interval(a0: list[float], a1: list[float], b0: list[float], b1: list[float]) -> tuple[float, float] | None:
    axis = _sub(a1, a0)
    length2 = _dot(axis, axis)
    if length2 <= EPS:
        return None
    if abs(_cross(axis, _sub(b0, a0))) > 1e-9 or abs(_cross(axis, _sub(b1, a0))) > 1e-9:
        return None
    t0 = _dot(_sub(b0, a0), axis) / length2
    t1 = _dot(_sub(b1, a0), axis) / length2
    lo = max(0.0, min(t0, t1))
    hi = min(1.0, max(t0, t1))
    if hi - lo <= 1e-9:
        return None
    return lo, hi


def _merged(intervals: list[tuple[float, float]]) -> list[list[float]]:
    out: list[list[float]] = []
    for lo, hi in sorted(intervals):
        if not out or lo > out[-1][1] + 1e-10:
            out.append([lo, hi])
        else:
            out[-1][1] = max(out[-1][1], hi)
    return out


def _subtract_z(z0: float, z1: float, covers: list[tuple[float, float]]) -> list[tuple[float, float]]:
    clipped = [(max(z0, lo), min(z1, hi)) for lo, hi in covers if min(z1, hi) - max(z0, lo) > 1e-10]
    merged = _merged(clipped)
    exposed: list[tuple[float, float]] = []
    cursor = z0
    for lo, hi in merged:
        if lo > cursor + 1e-10:
            exposed.append((cursor, lo))
        cursor = max(cursor, hi)
    if cursor < z1 - 1e-10:
        exposed.append((cursor, z1))
    return exposed


def _exposed_side_patches(solid: dict[str, Any], others: list[dict[str, Any]]) -> list[tuple[tuple[float, float], tuple[float, float], float, float]]:
    polygon = solid["polygon"]
    z0 = float(solid["z0"])
    z1 = float(solid["z1"])
    patches: list[tuple[tuple[float, float], tuple[float, float], float, float]] = []
    for i, a0 in enumerate(polygon):
        a1 = polygon[(i + 1) % len(polygon)]
        overlaps: list[tuple[float, float, float, float]] = []
        for other in others:
            op = other["polygon"]
            for j, b0 in enumerate(op):
                b1 = op[(j + 1) % len(op)]
                interval = _collinear_overlap_interval(a0, a1, b0, b1)
                if interval is not None:
                    overlaps.append((interval[0], interval[1], float(other["z0"]), float(other["z1"])))
        breaks = {0.0, 1.0}
        for lo, hi, _, _ in overlaps:
            breaks.add(round(lo, 12))
            breaks.add(round(hi, 12))
        ordered = sorted(breaks)
        for ta, tb in zip(ordered, ordered[1:]):
            if tb - ta <= 1e-10:
                continue
            midpoint = (ta + tb) / 2.0
            covers = [(oz0, oz1) for lo, hi, oz0, oz1 in overlaps if lo - 1e-10 <= midpoint <= hi + 1e-10]
            p0 = _point(a0, a1, ta)
            p1 = _point(a0, a1, tb)
            for za, zb in _subtract_z(z0, z1, covers):
                patches.append((p0, p1, za, zb))
    return patches


def _project(point: tuple[float, float] | list[float], z: float, manifest: dict[str, Any]) -> tuple[float, float]:
    width = float(manifest["source_artboard"]["width"])
    height = float(manifest["source_artboard"]["height"])
    projection = manifest["projection"]
    return (
        float(point[0]) * width + z * float(projection["depth_dx"]) * width,
        float(point[1]) * height - z * float(projection["depth_dy"]) * height,
    )


def _polygon(points: list[tuple[float, float]], fill: str, stroke: str | None = None, width: float | None = None) -> str:
    encoded = " ".join(f"{_fmt(x)},{_fmt(y)}" for x, y in points)
    if stroke is None:
        return f'  <polygon points="{encoded}" fill="{fill}" stroke="none"/>'
    return f'  <polygon points="{encoded}" fill="{fill}" stroke="{stroke}" stroke-width="{_fmt(float(width))}"/>'


def render_svg(manifest: dict[str, Any]) -> str:
    width = int(manifest["source_artboard"]["width"])
    height = int(manifest["source_artboard"]["height"])
    instrumentation = manifest["instrumentation"]
    base = _gray(instrumentation["base_gray"])
    top = _gray(instrumentation["base_gray"] + instrumentation["top_delta"])
    side = _gray(instrumentation["base_gray"] + instrumentation["side_delta"])
    outline = _gray(instrumentation["outline_gray"])
    outline_width = float(instrumentation["outline_width"])
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']

    volumes = list(manifest["surface_volumes"]) + list(manifest["proxy_volumes"])
    for volume in volumes:
        solids = volume["solids"]

        # Same-volume front/back bookkeeping boundaries receive no stroke.
        # Adjacent coplanar fills therefore read as one physical surface.
        for solid in solids:
            lines.append(_polygon([_project(p, float(solid["z0"]), manifest) for p in solid["polygon"]], base))
        for solid in solids:
            lines.append(_polygon([_project(p, float(solid["z1"]), manifest) for p in solid["polygon"]], top))

        # Only genuinely exposed side-wall area is emitted. Shared collinear
        # boundary intervals subtract neighboring same-volume z occupancy.
        for i, solid in enumerate(solids):
            others = solids[:i] + solids[i + 1:]
            for p0, p1, za, zb in _exposed_side_patches(solid, others):
                quad = [
                    _project(p0, za, manifest),
                    _project(p1, za, manifest),
                    _project(p1, zb, manifest),
                    _project(p0, zb, manifest),
                ]
                lines.append(_polygon(quad, side, outline, outline_width))

    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def apply_union_renderer() -> None:
    core.render_svg = render_svg
