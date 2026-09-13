#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "docs/evidence/PHASE_C_SHARED_IDENTITY_COMPLETION_AUDIT_01.json"
METHOD = ROOT / "docs/evidence/IMG_01_SHARED_IMAGE_CHARACTER_ART_DIRECTION_METHOD_01.json"
CURRENT = ROOT / "CURRENT_STATE.md"
LEDGER = ROOT / "docs/evidence/DESIGN_LEDGER.md"
AUDIT_SHA = "13291d7d1f09114bf59063229fdc018ed277cd077d4dc5174650c8f9a0346d49"
METHOD_SHA = "2d7cbdc5471b0c97f156d9bf1928eba0f12ba821ac954dce4d1c3877a1c8be13"

def fail(message):
    raise AssertionError(message)

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))
def main():
    if sha256(AUDIT) != AUDIT_SHA:
        fail("Phase C completion audit hash mismatch")
    if sha256(METHOD) != METHOD_SHA:
        fail("IMG-01 method hash mismatch")

    audit = load(AUDIT)
    method = load(METHOD)
    current = CURRENT.read_text(encoding="utf-8")
    ledger = LEDGER.read_text(encoding="utf-8")

    if audit.get("status") != "COMPLETE_NEXT_PROGRAM_SELECTED_IMG_01":
        fail("audit status")
    selected = audit.get("selected_program", {})
    if selected.get("id") != "IMG-01":
        fail("selected program")

    matrix = {x.get("requirement"): x for x in audit.get("phase_c_requirement_matrix", [])}
    required = {
        "symbol", "app icon", "wordmark", "typography roles",
        "color jobs and accessible palettes", "material/shape principles",
        "Character/human imagery principles", "icon family",
        "motion principles and reduced-motion equivalents", "public voice",
        "image/art direction", "small-scale/monochrome/high-contrast durability",
        "cross-surface translation"
    }
    if set(matrix) != required:
        fail("Phase C requirement matrix set")
    for req in ("Character/human imagery principles", "image/art direction"):
        if matrix[req].get("classification") != "UNRESOLVED_DESIGN_READY":
            fail(f"{req} classification")
        if matrix[req].get("design_readiness") != "READY_FOR_SUCCESSOR_CONVERGENCE":
            fail(f"{req} readiness")

    program = method.get("program", {})
    if method.get("status") != "FROZEN_PRE_MATERIALIZATION_NO_VISUAL_RESULT":
        fail("method status")
    if program.get("id") != "IMG-01" or program.get("type") != "SUCCESSOR_CONVERGENCE_SYNTHESIS_NOT_FRESH_RESET":
        fail("program identity/type")
    divergence = method.get("required_family_divergence", {})
    if divergence.get("family_count") != 3 or divergence.get("must_materially_differ_on_at_least") != 4:
        fail("family divergence contract")

    dimensions = {x.get("id") for x in method.get("evaluation_dimensions", [])}
    must_have = {
        "HUMAN_SPECIFICITY", "REPRESENTATION_DEPTH_CONTINUITY",
        "RELATIONAL_CAUSAL_MEANING", "STAGE_PRIMACY_NONCOPY",
        "CROSS_SURFACE_TRANSLATION", "IMAGE_FALLBACK_SEMANTIC_SURVIVAL",
        "MONOCHROME_HIGH_CONTRAST_DURABILITY", "CLR_INDEPENDENCE",
        "NON_GENERIC_AI_ART_DIRECTION", "USAGE_RESTRAINT",
        "PROVENANCE_REPRODUCIBILITY"
    }
    if not must_have.issubset(dimensions):
        fail("evaluation dimensions")
    if "CLR F2-versus-F1 adjudication or palette tokenization" not in method.get("excluded_variables", []):
        fail("CLR exclusion")
    if not method.get("hard_failures"):
        fail("hard-failure contract")

    for token in ("IMG-01", AUDIT.relative_to(ROOT).as_posix(), AUDIT_SHA, METHOD.relative_to(ROOT).as_posix(), METHOD_SHA,
                  "PRE-MATERIALIZATION", "NO VISUAL RESULT"):
        if token not in current:
            fail(f"CURRENT_STATE missing {token}")
    if "L-152 - Phase C completion audit corrects overbroad parking and activates IMG-01" not in ledger:
        fail("ledger L-152 missing")
    bad = [ord(c) for c in ledger if ord(c) < 32 and c not in "\n\r\t"]
    if bad:
        fail(f"ledger control characters: {bad}")

    print("IMG_01_ACTIVATION=PASS")
    print(f"AUDIT_SHA256={AUDIT_SHA}")
    print(f"METHOD_SHA256={METHOD_SHA}")
    print("FAMILIES=3")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"IMG_01_FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
