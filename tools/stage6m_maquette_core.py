#!/usr/bin/env python3
"""Internal Stage 6M base-core loader.

The preserved base implementation is stored as data, not as the canonical
entrypoint. This loader exposes only primitives required by the audited
hardening layer. Generation/validation is fail-closed until hardening replaces
base validation/report functions.
"""
from __future__ import annotations
import pathlib
import sys
import types
from typing import Any

_SOURCE = pathlib.Path(__file__).with_name("stage6m_maquette_core_source.txt")
_SOURCE_MODULE_NAME = "_stage6m_maquette_core_source"
_SOURCE_MODULE = types.ModuleType(_SOURCE_MODULE_NAME)
_SOURCE_MODULE.__file__ = str(_SOURCE)
sys.modules[_SOURCE_MODULE_NAME] = _SOURCE_MODULE
_NS: dict[str, Any] = _SOURCE_MODULE.__dict__
exec(compile(_SOURCE.read_text(encoding="utf-8"), str(_SOURCE), "exec"), _NS)

for _name in (
    "EPS", "FORMAT", "FROZEN_PROJECTION", "FROZEN_INSTRUMENTATION",
    "FROZEN_SANITIZATION", "ValidationError", "fail", "load_json", "dump_json",
    "polygon_area_centroid", "is_convex", "positive_overlap_area", "point_in_polygon",
    "point_in_proxy", "solid_mass", "margin_inside", "rounded", "render_svg",
    "validate_sanitized_svg",
):
    globals()[_name] = _NS[_name]

_BASE_VALIDATE = _NS["validate_manifest"]
_BASE_BUILD_REPORT = _NS["build_report"]
validate_manifest = _BASE_VALIDATE
build_report = _BASE_BUILD_REPORT


def _hardening_active() -> bool:
    return validate_manifest is not _BASE_VALIDATE and build_report is not _BASE_BUILD_REPORT


def deterministic_bytes(m: dict[str, Any]) -> tuple[str, str]:
    if not _hardening_active():
        fail("internal Stage 6M core cannot generate/validate without mandatory hardening")
    validate_manifest(m)
    report = build_report(m)
    svg = render_svg(m)
    validate_sanitized_svg(svg)
    return svg, dump_json(report)


def main() -> int:
    if not _hardening_active():
        print("Stage 6M validation FAIL: internal core cannot run without mandatory hardening", file=sys.stderr)
        return 2
    _NS["deterministic_bytes"] = deterministic_bytes
    return _NS["main"]()


if __name__ == "__main__":
    raise SystemExit(main())
