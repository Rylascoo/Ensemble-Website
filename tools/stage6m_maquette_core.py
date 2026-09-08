#!/usr/bin/env python3
"""Internal Stage 6M base-core loader.

The preserved base implementation is stored as data, not as the canonical
entrypoint. This loader exposes only primitives required by the audited
hardening layer. Generation/validation is fail-closed until hardening replaces
base validation/report functions.
"""
from __future__ import annotations
import base64
import hashlib
import pathlib
import sys
import types
import zlib
from typing import Any

_SOURCE_DIR = pathlib.Path(__file__).parent
_SOURCE_PARTS = [_SOURCE_DIR / f"stage6m_maquette_core_source.part{i}" for i in range(1, 6)]
if not all(p.is_file() for p in _SOURCE_PARTS):
    raise RuntimeError("missing Stage 6M preserved core source part")
if set(_SOURCE_DIR.glob("stage6m_maquette_core_source.part*")) != set(_SOURCE_PARTS):
    raise RuntimeError("unexpected Stage 6M preserved core source part")
_SOURCE = _SOURCE_PARTS[0]
_EXPECTED_SOURCE_GIT_BLOB = "fb3f367a4064129c1421c2008c7f4622e85bcc14"
_SOURCE_MODULE_NAME = "_stage6m_maquette_core_source"
_SOURCE_MODULE = types.ModuleType(_SOURCE_MODULE_NAME)
_SOURCE_MODULE.__file__ = str(_SOURCE)
sys.modules[_SOURCE_MODULE_NAME] = _SOURCE_MODULE
_NS: dict[str, Any] = _SOURCE_MODULE.__dict__
parts = [p.read_text(encoding="ascii").strip() for p in _SOURCE_PARTS]
if any(not part.startswith("!") for part in parts):
    raise RuntimeError("invalid Stage 6M core source part")
encoded = "".join(part[1:] for part in parts)
source_bytes = zlib.decompress(base64.b64decode(encoded))
git_blob = hashlib.sha1(f"blob {len(source_bytes)}\0".encode("ascii") + source_bytes).hexdigest()
if git_blob != _EXPECTED_SOURCE_GIT_BLOB:
    raise RuntimeError("Stage 6M preserved core source hash mismatch")
exec(compile(source_bytes.decode("utf-8"), "<stage6m_preserved_core>", "exec"), _NS)

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
