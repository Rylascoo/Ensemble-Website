#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/evidence/stage6m/NONCANDIDATE_FIXTURE_01.json"
CORE = ROOT / "tools/stage6m_maquette_core.py"
HARDENING = ROOT / "tools/stage6m_maquette_hardening.py"
SOURCE_PARTS = sorted((ROOT / "tools").glob("stage6m_maquette_core_source.part*"))
EXPECTED_SOURCE_PART_NAMES = [f"stage6m_maquette_core_source.part{i}" for i in range(1, 6)]


class Stage6MCoreBypassTest(unittest.TestCase):
    def test_internal_core_cannot_bypass_hardening(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CORE), "validate", str(FIXTURE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(proc.returncode, 2)
        self.assertIn("mandatory hardening", proc.stderr)

    def test_hardening_cannot_bypass_physical_union_renderer(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(HARDENING), "validate", str(FIXTURE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(proc.returncode, 2)
        self.assertIn("physical-union renderer", proc.stderr)

    def test_preserved_source_data_is_not_directly_executable(self) -> None:
        self.assertEqual([p.name for p in SOURCE_PARTS], EXPECTED_SOURCE_PART_NAMES)
        for source in SOURCE_PARTS:
            proc = subprocess.run(
                [sys.executable, str(source), "validate", str(FIXTURE)],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(proc.returncode, 0, source.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
