#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "docs/evidence/PHASE_C_SHARED_IDENTITY_COMPLETION_AUDIT_01.json"
METHOD = ROOT / "docs/evidence/IMG_01_SHARED_IMAGE_CHARACTER_ART_DIRECTION_METHOD_01.json"
STAGE0 = ROOT / "docs/evidence/IMG_01_STAGE0_EVIDENCE_ATLAS_AND_SOURCE_MANIFEST_01.json"
FAMILIES = ROOT / "docs/evidence/IMG_01_FROZEN_ART_DIRECTION_FAMILIES_01.json"
CURRENT = ROOT / "CURRENT_STATE.md"
LEDGER = ROOT / "docs/evidence/DESIGN_LEDGER.md"
AUDIT_SHA = "13291d7d1f09114bf59063229fdc018ed277cd077d4dc5174650c8f9a0346d49"
METHOD_SHA = "2d7cbdc5471b0c97f156d9bf1928eba0f12ba821ac954dce4d1c3877a1c8be13"
STAGE0_SHA = "c3ddc1fa9c5ade158edbf8f82f1b6c8afa086eda4e62441f9fc25e11146f7283"
FAMILIES_SHA = "13513408875a6f4f6ba8be8e5aaead83bf616d38cb821f36291e82d2f79e8207"

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
    if sha256(STAGE0) != STAGE0_SHA:
        fail("IMG-01 Stage-0 hash mismatch")
    if sha256(FAMILIES) != FAMILIES_SHA:
        fail("IMG-01 family-freeze hash mismatch")

    audit = load(AUDIT)
    method = load(METHOD)
    stage0 = load(STAGE0)
    families = load(FAMILIES)
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

    if stage0.get("status") != "FROZEN_STAGE0_NO_NEW_VISUAL_GENERATION":
        fail("Stage-0 status")
    if len(stage0.get("repository_sources", [])) != 16 or len(stage0.get("drive_visual_sources", [])) != 9:
        fail("Stage-0 source counts")
    if len(stage0.get("positive_laws", [])) != 15 or len(stage0.get("negative_quarantine_laws", [])) != 12:
        fail("Stage-0 law counts")
    conclusion = stage0.get("stage0_conclusion", {})
    if conclusion.get("new_visual_generation_consumed") is not False:
        fail("Stage-0 generation boundary")
    if conclusion.get("historical_source_surfaces_selected_as_incumbents") is not False:
        fail("historical inheritance boundary")

    if families.get("status") != "FROZEN_BEFORE_REFERENCE_BOARD_OR_SUBJECTIVE_COMPARISON":
        fail("family-freeze status")
    family_ids = [x.get("id") for x in families.get("families", [])]
    if family_ids != ["IMG-F1", "IMG-F2", "IMG-F3"]:
        fail("family identities/order")
    if [x.get("count") for x in families.get("pairwise_divergence_audit", [])] != [6, 7, 6]:
        fail("pairwise divergence counts")
    if families.get("subjective_scoring_started") is not False or families.get("new_visual_generation_consumed") is not False:
        fail("premature scoring/generation")
    if families.get("clr_selection_created") is not False or families.get("stage_change_created") is not False:
        fail("CLR/Stage authority leak")
    for token in ("IMG-01", AUDIT.relative_to(ROOT).as_posix(), AUDIT_SHA, METHOD.relative_to(ROOT).as_posix(), METHOD_SHA,
                  STAGE0.relative_to(ROOT).as_posix(), STAGE0_SHA, FAMILIES.relative_to(ROOT).as_posix(), FAMILIES_SHA,
                  "STAGE-0 + FAMILY FREEZE COMPLETE", "REFERENCE BOARD NEXT", "NO NEW VISUAL GENERATION"):
        if token not in current:
            fail(f"CURRENT_STATE missing {token}")
    if "L-152 - Phase C completion audit corrects overbroad parking and activates IMG-01" not in ledger:
        fail("ledger L-152 missing")
    bad = [ord(c) for c in ledger if ord(c) < 32 and c not in "\n\r\t"]
    if bad:
        fail(f"ledger control characters: {bad}")

    print("IMG_01_STAGE0_FAMILY_FREEZE=PASS")
    print(f"AUDIT_SHA256={AUDIT_SHA}")
    print(f"METHOD_SHA256={METHOD_SHA}")
    print(f"STAGE0_SHA256={STAGE0_SHA}")
    print(f"FAMILIES_SHA256={FAMILIES_SHA}")
    print("FAMILIES=3 PAIRWISE_DIVERGENCE=6/7/6")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"IMG_01_FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
