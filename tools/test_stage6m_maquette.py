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

    def test_schema_constants_match_implementation(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        props = schema["properties"]
        self.assertEqual(props["format"]["const"], FORMAT)
        self.assertEqual(props["projection"]["const"], FROZEN_PROJECTION)
        self.assertEqual(props["instrumentation"]["const"], FROZEN_INSTRUMENTATION)
        self.assertEqual(props["sanitization"]["const"], FROZEN_SANITIZATION)


if __name__ == "__main__":
    unittest.main(verbosity=2)
