#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONCORDANCE = ROOT / "docs/evidence/IMG_01_DIRECTOR_PRIOR_CONCORDANCE_01.json"
METHOD = ROOT / "docs/evidence/CPS_01_CANONICAL_CHARACTER_PRESENCE_SYSTEM_METHOD_01.json"
HANDOFF = ROOT / "docs/HANDOFF_CPS_01_CANONICAL_CHARACTER_PRESENCE_SYSTEM_2026_09_13.md"
CURRENT = ROOT / "CURRENT_STATE.md"
LEDGER = ROOT / "docs/evidence/DESIGN_LEDGER.md"
CONCORDANCE_SHA = "1ddf51fa28ddea497b8dd1da353f26733c0cf1a7a857e02020e1322a9c06ce27"
METHOD_SHA = "3069f468a0fb98964758154f82e126d7a4296a529b78885c90818235527d6dc4"
HANDOFF_SHA = "6a99ac0c4cf2eb673031949591de4a876a13cb249945cb7e6062adebdfa87cf2"

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def fail(message):
    raise AssertionError(message)

def main():
    if sha256(CONCORDANCE) != CONCORDANCE_SHA:
        fail("concordance hash mismatch")
    if sha256(METHOD) != METHOD_SHA:
        fail("CPS-01 method hash mismatch")
    if sha256(HANDOFF) != HANDOFF_SHA:
        fail("CPS-01 handoff hash mismatch")
    concordance = load(CONCORDANCE)
    method = load(METHOD)
    current = CURRENT.read_text(encoding="utf-8")
    ledger = LEDGER.read_text(encoding="utf-8")
    handoff = HANDOFF.read_text(encoding="utf-8")

    if concordance.get("status") != "MATERIAL_CONFLICT_SUCCESSOR_GATE_SELECTED_CPS_01":
        fail("concordance status")
    unchanged = concordance.get("unchanged_method_result", {})
    if unchanged != {
        "IMG-F1": "FAMILY_SURVIVES_WITH_USAGE_RESTRAINT",
        "IMG-F2": "TARGETED_REFINEMENT_REQUIRED",
        "IMG-F3": "FAMILY_REJECTED_GENERIC_OR_SEMANTICALLY_WEAK",
    }:
        fail("IMG-01 result preservation")
    effect = concordance.get("authority_effect", {})
    if any(effect.get(k) is not False for k in [
        "img01_scores_changed", "img01_prompt_retune_authorized", "f2_retroactively_rescued",
        "f3_reopened", "f1_promoted_to_final_identity", "clr_or_stage_changed", "phase_c_exit_authorized"
    ]):
        fail("concordance authority effect")
    conclusion = concordance.get("system_conclusion", {})
    if conclusion.get("successor_gate") != "CPS-01 - Canonical Character Presence System":
        fail("successor gate")
    if conclusion.get("successor_type") != "DETERMINISTIC_NON_RENDER_SYSTEM_ARCHITECTURE_BEFORE_ANY_NEW_GENERATED_ART":
        fail("successor type")
    if method.get("status") != "FROZEN_PRE_CONSTRUCTION_DETERMINISTIC_NON_RENDER":
        fail("CPS-01 method status")
    program = method.get("program", {})
    if program.get("id") != "CPS-01" or program.get("type") != "SUCCESSOR_SYSTEM_ARCHITECTURE_AFTER_IMG_01":
        fail("CPS-01 program identity/type")
    layers = [x.get("layer") for x in method.get("layer_model", [])]
    if layers != [
        "CANONICAL_IDENTITY_PRESENCE",
        "AUTHORIZED_CURRENT_STATE",
        "AUTHORITATIVE_HISTORY_RESIDUE",
        "RELATIONAL_CONTEXT",
        "OPTIONAL_EXPRESSIVE_DEPICTION",
    ]:
        fail("CPS-01 layer model")
    candidates = [x.get("id") for x in method.get("architecture_candidates", [])]
    if candidates != ["CPS-A", "CPS-B", "CPS-C"]:
        fail("CPS-01 architecture candidates")
    roles = method.get("deterministic_test_roles", [])
    role_names = [x.split(":", 1)[0] for x in roles]
    expected_roles = [
        "MICRO", "COMPACT", "FOCUSED", "CROPPED_FRAGMENT", "RELATIONAL_PAIR",
        "ENSEMBLE_THREE", "MONOCHROME_HIGH_CONTRAST", "NO_IMAGE",
        "STATIC_REDUCED_MOTION", "APP_WEB_TRANSLATION"
    ]
    if role_names != expected_roles:
        fail("CPS-01 deterministic roles")
    if "new renderer/image generation during CPS-01" not in method.get("excluded_variables", []):
        fail("CPS-01 renderer exclusion")
    dimensions = {x.get("id") for x in method.get("evaluation_dimensions", [])}
    required_dimensions = {
        "PORTRAIT_INDEPENDENT_RECOVERY", "SCALE_CROP_CONTINUITY", "ACCESSIBILITY_REDUNDANCY",
        "LAYER_SEPARATION", "OPTIONAL_DEPICTION_DECOUPLING", "ORDINARY_PERSON_VIABILITY",
        "RELATIONAL_COMPOSITION", "PERSPECTIVE_PROVENANCE_RESTRAINT", "APP_WEB_TRANSLATION",
        "STAGE_AND_CLR_INDEPENDENCE", "NON_AVATAR_NON_GAME_NON_EDITORIAL", "IMPLEMENTATION_NEUTRALITY"
    }
    if dimensions != required_dimensions:
        fail("CPS-01 evaluation dimensions")
    if not method.get("hard_failures") or not method.get("promotion_floor"):
        fail("CPS-01 promotion contract")
    if method.get("recursive_audit", {}).get("deterministic_non_render_first") is not True:
        fail("CPS-01 non-render audit")

    for token in [
        "CPS-01 - Canonical Character Presence System",
        CONCORDANCE.relative_to(ROOT).as_posix(), CONCORDANCE_SHA,
        METHOD.relative_to(ROOT).as_posix(), METHOD_SHA,
        HANDOFF.relative_to(ROOT).as_posix(),
        "DETERMINISTIC NON-RENDER CONSTRUCTION NEXT",
        "No new image generation is authorized inside CPS-01",
    ]:
        if token not in current:
            fail(f"CURRENT_STATE missing {token}")
    if "L-157 - IMG-01 prior concordance selects CPS-01 as the canonical Character-presence successor" not in ledger:
        fail("ledger L-157 missing")
    for token in ["CPS-A", "CPS-B", "CPS-C", "Exact next action", "No new image generation is authorized inside CPS-01"]:
        if token not in handoff:
            fail(f"handoff missing {token}")
    bad = []
    for path in (CONCORDANCE, METHOD, HANDOFF, CURRENT, LEDGER):
        text = path.read_text(encoding="utf-8")
        bad.extend((path.name, ord(c)) for c in text if ord(c) < 32 and c not in "\n\r\t")
    if bad:
        fail(f"control characters: {bad}")

    print("CPS_01_METHOD_FREEZE=PASS")
    print(f"CONCORDANCE_SHA256={CONCORDANCE_SHA}")
    print(f"METHOD_SHA256={METHOD_SHA}")
    print(f"HANDOFF_SHA256={HANDOFF_SHA}")
    print("ARCHITECTURES=3 LAYERS=5 ROLES=10 RENDER_GENERATION=0")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"CPS_01_FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
