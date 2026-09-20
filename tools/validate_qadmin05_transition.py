#!/usr/bin/env python3
"""Validate the durable Q-ADMIN-05 Website authority-transition boundary."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE_REF = "846c60ee448abf7d5c57bdd64de55cb9294880e2"
TRANSITION = ROOT / "docs/Q_ADMIN_05_APP_DESIGN_AUTHORITY_TRANSITION_2026_09_20.md"
SOURCE_ARTIFACTS = {
    "docs/Q_ADMIN_05_APP_DESIGN_SOURCE_FREEZE_2026_09_20.md": (
        70960,
        "2a0920e7beeee498acff731c431d72db3244375455a5f08ddade6a9b2fb0c0a3",
    ),
    "docs/evidence/Q_ADMIN_05_RECURSIVE_AUTHORITY_CLOSURE_2026_09_20.json": (
        1208034,
        "1bc102a4b051eaf721d1359d65a03401d6b286f3e9e490b3c7a9f58ea6da506e",
    ),
}
ROUTING_FILES = (
    "AGENTS.md",
    "CURRENT_STATE.md",
    "README.md",
    "docs/DESIGN_CONTINUITY.md",
    "docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md",
    "docs/INDEX.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def git_show(spec: str) -> bytes:
    return subprocess.check_output(["git", "show", spec], cwd=ROOT)


def digest(data: bytes) -> tuple[int, str]:
    return len(data), hashlib.sha256(data).hexdigest()


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    for path, expected in SOURCE_ARTIFACTS.items():
        # Read the indexed Git bytes so checkout line-ending conversion cannot
        # manufacture cross-platform drift in an otherwise unchanged blob.
        current = git_show(f":{path}")
        require(digest(current) == expected, f"frozen source artifact drift: {path}")
        require(git_show(f"{SOURCE_REF}:{path}") == current, f"source ref mismatch: {path}")

    transition = TRANSITION.read_text(encoding="utf-8")
    for token in (
        "APP DESIGN SOURCE RELINQUISHED / HISTORICAL PROVENANCE RETAINED",
        "ADMIN-Q05-WEBSITE-RELINQUISHMENT-01-20260920",
        "Rylascoo/Ensemble-Project",
        "docs/design/app/",
        "UNRESOLVED_APP_DESIGN_DECISION",
        "EVIDENCE_PENDING_ADOPTION",
        "Q-ADMIN-05 is not globally closed",
        "Website PR #147",
        "Google Drive",
        "Ryladmin",
    ):
        require(token in transition, f"transition pointer missing: {token}")

    routing = {path: read(path) for path in ROUTING_FILES}
    for path, text in routing.items():
        require(
            "Q_ADMIN_05_APP_DESIGN_AUTHORITY_TRANSITION_2026_09_20.md" in text,
            f"routing surface lacks transition pointer: {path}",
        )
    require(
        "Rylascoo/Ensemble-Project/docs/design/app/" in routing["AGENTS.md"],
        "AGENTS.md does not route application design to Project",
    )
    require(
        "Website remains active app-design authority" not in "\n".join(routing.values()),
        "stale active Website app-design ownership remains in current routing",
    )
    require(
        "native-app visual-system and interaction design" not in routing["AGENTS.md"]
        and "native-app visual-system and interaction design" not in routing["docs/DESIGN_CONTINUITY.md"],
        "stale native-app ownership remains in Website role law",
    )

    state = routing["CURRENT_STATE.md"]
    require(len((ROOT / "CURRENT_STATE.md").read_bytes()) <= 3072, "CURRENT_STATE.md exceeds 3 KiB")
    require("UNRESOLVED_APP_DESIGN_DECISION" in state, "Home A/B state missing")
    require("EVIDENCE_PENDING_ADOPTION" in state, "FIRSTUSE state missing")
    require("final Ryladmin Q-ADMIN-05 cross-repository authority-graph verification" in state,
            "exact next Q-ADMIN-05 task drift")

    ledger = read("docs/evidence/DESIGN_LEDGER.md")
    require("## L-243 - Q-ADMIN-05 Website app-design source relinquishment integrated" in ledger,
            "Design Ledger transition entry missing")
    require(not (ROOT / "docs/design/app").exists(), "Project app-design authority was mirrored into Website")

    print(json.dumps({
        "result": "PASS",
        "source_artifacts_intact": len(SOURCE_ARTIFACTS),
        "routing_surfaces": len(ROUTING_FILES),
        "home_ab": "UNRESOLVED_APP_DESIGN_DECISION",
        "firstuse": "EVIDENCE_PENDING_ADOPTION",
        "website_state": "APP DESIGN SOURCE RELINQUISHED / HISTORICAL PROVENANCE RETAINED",
    }, indent=2))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Q-ADMIN-05 transition FAIL: {error}", file=sys.stderr)
        sys.exit(1)
