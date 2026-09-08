#!/usr/bin/env python3
from __future__ import annotations
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "docs/evidence/stage6m/NONCANDIDATE_FIXTURE_01.json"
CORE = ROOT / "tools/stage6m_maquette_core.py"


class Stage6MCoreBypassTest(unittest.TestCase):
    def test_internal_core_cannot_bypass_hardening(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CORE), "validate", str(FIXTURE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(proc.returncode, 2)
        self.assertIn("mandatory hardening", proc.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
