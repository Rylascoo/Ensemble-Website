#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import pathlib
import unittest

from stage6m_maquette import (
    FORMAT,
    FROZEN_INSTRUMENTATION,
    FROZEN_PROJECTION,
    FROZEN_SANITIZATION,
    ValidationError,
    deterministic_bytes,
    validate_manifest,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/evidence/stage6m/NONCANDIDATE_FIXTURE_01.json"
SCHEMA = ROOT / "docs/evidence/stage6m/STAGE6M_MANIFEST_SCHEMA_01.json"


class Stage6MToolingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_fixture_passes_automated_validation_but_is_not_transfer_eligible(self) -> None:
        svg, report_text = deterministic_bytes(self.fixture)
        report = json.loads(report_text)
        self.assertTrue(report["automated_validation_pass"])
        self.assertFalse(report["transfer_eligible"])
        self.assertNotIn("<text", svg)
        self.assertNotIn("<metadata", svg)
        self.assertNotIn(" id=", svg)
        self.assertNotIn("<rect", svg)

    def test_same_volume_internal_boundaries_do_not_transfer_as_seams(self) -> None:
        svg, _ = deterministic_bytes(self.fixture)
        # These were the exact bookkeeping side walls at the two internal
        # surface-solid joins in the original renderer. They must disappear
        # while true exposed depth faces remain present.
        self.assertNotIn("650.7,545.65 650.7,587.65 657,584.5 657,542.5", svg)
        self.assertNotIn("850.7,545.65 850.7,587.65 857,584.5 857,542.5", svg)
        self.assertIn("650.7,545.65 750.7,503.65 757,500.5 657,542.5", svg)

    def test_contact_must_be_actual_adjacency(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        mutated["contacts"][0]["point_b"][0] += 0.01
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_proxy_mass_solids_must_be_interior_disjoint(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        for solid in mutated["proxy_volumes"][1]["solids"]:
            if solid["id"] == "Q-contact-pad":
                solid["polygon"] = [[0.49, 0.40], [0.56, 0.40], [0.56, 0.45], [0.49, 0.45]]
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_instrumentation_is_not_candidate_tunable(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        mutated["instrumentation"]["base_gray"] += 1
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_projection_is_not_candidate_tunable(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        mutated["projection"]["depth_dx"] += 0.001
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_transfer_eligibility_is_fail_closed(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        mutated["review"]["transfer_eligible"] = True
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_support_solid_must_contact_shared_surface(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        for solid in mutated["proxy_volumes"][0]["solids"]:
            if solid["id"] == "P-foot":
                solid["polygon"] = [[0.34, 0.72], [0.46, 0.72], [0.46, 0.76], [0.34, 0.76]]
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_proxy_may_not_penetrate_shared_surface(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        for solid in mutated["proxy_volumes"][0]["solids"]:
            if solid["id"] == "P-foot":
                solid["polygon"] = [[0.34, 0.76], [0.46, 0.76], [0.46, 0.80], [0.34, 0.80]]
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_distinct_proxies_may_touch_but_not_interpenetrate(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        for solid in mutated["proxy_volumes"][1]["solids"]:
            if solid["id"] == "Q-contact-pad":
                solid["polygon"] = [[0.48, 0.40], [0.54, 0.40], [0.54, 0.45], [0.48, 0.45]]
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_static_solver_uses_source_artboard_aspect_ratio(self) -> None:
        _, report_text = deterministic_bytes(self.fixture)
        report = json.loads(report_text)
        supported = next(c for c in report["static_cases"] if c["id"] == "Q-supported-by-P")
        self.assertAlmostEqual(supported["fx_fraction_of_proxy_weight"], 0.08137019, places=8)

    def test_surface_solids_must_be_convex_and_connected(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        mutated["surface_volumes"][0]["solids"][1]["polygon"] = [
            [0.65, 0.78], [0.75, 0.72], [0.72, 0.80], [0.85, 0.78], [0.85, 0.84], [0.65, 0.84]
        ]
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

        mutated = copy.deepcopy(self.fixture)
        for pnt in mutated["surface_volumes"][0]["solids"][2]["polygon"]:
            pnt[0] = round(pnt[0] + 0.03, 4)
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_proxy_solids_must_be_boundary_connected(self) -> None:
        mutated = copy.deepcopy(self.fixture)
        head = next(s for s in mutated["proxy_volumes"][0]["solids"] if s["id"] == "P-head")
        head["polygon"] = [[0.30,0.20],[0.36,0.20],[0.36,0.29],[0.30,0.29]]
        with self.assertRaises(ValidationError):
            validate_manifest(mutated)

    def test_schema_constants_match_implementation(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        props = schema["properties"]
        self.assertEqual(props["format"]["const"], FORMAT)
        self.assertEqual(props["projection"]["const"], FROZEN_PROJECTION)
        self.assertEqual(props["instrumentation"]["const"], FROZEN_INSTRUMENTATION)
        self.assertEqual(props["sanitization"]["const"], FROZEN_SANITIZATION)
        self.assertEqual(props["surface_volumes"]["maxItems"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
