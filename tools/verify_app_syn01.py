from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METHOD_PATH = ROOT / "docs/evidence/APP_SYN_01_WHOLE_APP_PACKET_SYNTHESIS_METHOD_01.json"
REGISTRY_PATH = ROOT / "docs/evidence/DESIGN_PACKET_REGISTRY_01.json"
STAGE_PATH = ROOT / "docs/evidence/packets/PKT_STAGE_CORE_02.json"
STATE_PATH = ROOT / "CURRENT_STATE.md"

method = json.loads(METHOD_PATH.read_text(encoding="utf-8"))
registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
stage = json.loads(STAGE_PATH.read_text(encoding="utf-8"))
state = STATE_PATH.read_text(encoding="utf-8")

assert method["schema"] == "kymaean.app-syn-01.whole-app-synthesis-method.v1"
assert method["status"] == "PREREGISTERED_ACTIVE_METHOD_NO_VISUAL_RESULT"
assert method["recursive_audit"]["material_defects_remaining"] is False
assert method["recursive_audit"]["no_new_visual_synthesis_evidence_consumed"] is True

anchor = method["frozen_anchor"]
master = stage["visual_master"]
assert anchor["packet_id"] == "PKT-STAGE-CORE-02"
assert anchor["drive_file_id"] == master["drive_file_id"]
assert anchor["sha256"] == master["sha256"]
assert anchor["uploaded_size_bytes"] == master["uploaded_size_bytes"]
assert anchor["dimensions"] == master["dimensions"]

policy = registry["synthesis_policy"]
assert policy["active_whole_app_synthesis_program"] == "APP-SYN-01"
assert policy["active_whole_app_synthesis_status"] == "SOURCE_FREEZE_COMPLETE_NO_VISUAL_RESULT"
assert policy["active_whole_app_synthesis_method"] == "docs/evidence/APP_SYN_01_WHOLE_APP_PACKET_SYNTHESIS_METHOD_01.json"
assert policy["active_whole_app_synthesis_manifest"] == "docs/evidence/APP_SYN_01_EXECUTION_DEFAULTS_AND_SOURCE_MANIFEST_01.json"
assert policy["active_whole_app_synthesis_manifest_sha256"] == "af5e8c2a05bb368344c4538a616dfbfcd4594ec10377dca28d7f2c236f37dceb"
assert policy["whole_app_synthesis_packets_created"] == []

packet_ids = {item["packet_id"] for item in registry["packets"]}
for packet_id in method["primary_input_packets"]:
    assert packet_id in packet_ids, packet_id

assert "APP-SYN-01" in state
assert "ACTIVE / METHOD + EXECUTION SOURCE FREEZE COMPLETE / NO NEW VISUAL SYNTHESIS EVIDENCE YET" in state
assert "APP_SYN_01_EXECUTION_DEFAULTS_AND_SOURCE_MANIFEST_01.json" in state
assert len(state.encode("utf-8")) <= 3072

non_authority = "\n".join(method["explicit_non_authority"])
for required in ("No automatic CLR-01 winner", "No Phase-C exit", "No WinUI/runtime", "ODR-05/07/14/15/19/30"):
    assert required in non_authority, required

closed = "\n".join(method["closed_gate_constraints"])
for required in ("CIR-S1", "CONE-S1", "STATE-S1", "PERF-S1", "SEL-S1"):
    assert required in closed, required

print("APP_SYN_01_METHOD=PASS")
print(f"CURRENT_STATE_BYTES={len(state.encode('utf-8'))}")
print(f"INPUT_PACKETS={len(method['primary_input_packets'])}")
