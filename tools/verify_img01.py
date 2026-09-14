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
PREFLIGHT = ROOT / "docs/evidence/IMG_01_REFERENCE_BOARD_MECHANICAL_PREFLIGHT_01.json"
EXPOSURE = ROOT / "docs/evidence/IMG_01_DIRECTOR_PRIOR_EXPOSURE_AND_EVALUATION_QUARANTINE_01.json"
PACKETS = ROOT / "docs/evidence/IMG_01_EXEMPLAR_RENDERER_PACKETS_01.json"
CARRIER = ROOT / "prototypes/img-01/reference-board.html"
PROBE = ROOT / "tools/img01_reference_board_probe.mjs"
CURRENT = ROOT / "CURRENT_STATE.md"
LEDGER = ROOT / "docs/evidence/DESIGN_LEDGER.md"
AUDIT_SHA = "13291d7d1f09114bf59063229fdc018ed277cd077d4dc5174650c8f9a0346d49"
METHOD_SHA = "2d7cbdc5471b0c97f156d9bf1928eba0f12ba821ac954dce4d1c3877a1c8be13"
STAGE0_SHA = "c3ddc1fa9c5ade158edbf8f82f1b6c8afa086eda4e62441f9fc25e11146f7283"
FAMILIES_SHA = "13513408875a6f4f6ba8be8e5aaead83bf616d38cb821f36291e82d2f79e8207"
PREFLIGHT_SHA = "3dc93454fe9caa2962e87c193dfac68e9db197bdf6925fa79f48dd2ee702d575"
EXPOSURE_SHA = "be4b7063c8c76174e90898d7c32073af7341a338218c94b0906364f2a543743a"
PACKETS_SHA = "7b861b38acec500013c62ed2284d3c7eb0e0db42b3254483590a98a302cd5b33"
CARRIER_SHA = "879816826a7e1b7d9afe8bfd514f875f2cc148e698f6421046d995079456a4a0"
PROBE_SHA = "f500b7d1d157f60b90e73b719db73a89c5c638ea52c01d75bb3b6de1681d3ed3"

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
    if sha256(PREFLIGHT) != PREFLIGHT_SHA:
        fail("IMG-01 mechanical-preflight hash mismatch")
    if sha256(EXPOSURE) != EXPOSURE_SHA:
        fail("IMG-01 prior-exposure hash mismatch")
    if sha256(PACKETS) != PACKETS_SHA:
        fail("IMG-01 renderer-packet hash mismatch")
    if sha256(CARRIER) != CARRIER_SHA or sha256(PROBE) != PROBE_SHA:
        fail("IMG-01 reference carrier/probe hash mismatch")

    audit = load(AUDIT)
    method = load(METHOD)
    stage0 = load(STAGE0)
    families = load(FAMILIES)
    preflight = load(PREFLIGHT)
    exposure = load(EXPOSURE)
    packets = load(PACKETS)
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

    if preflight.get("status") != "PASS_COMPLETE_PRE_AESTHETIC_MECHANICAL_MATRIX":
        fail("mechanical preflight status")
    if preflight.get("carrier", {}).get("sha256") != CARRIER_SHA or preflight.get("carrier", {}).get("probe_sha256") != PROBE_SHA:
        fail("preflight carrier/probe pins")
    modes = preflight.get("matrix", [])
    expected_modes = ["NORMAL_WIDE", "NORMAL_COMPACT", "FORCED_COLORS_WIDE", "FORCED_COLORS_COMPACT", "TEXT_200_COMPACT"]
    if [x.get("mode") for x in modes] != expected_modes or not all(x.get("pass") is True for x in modes):
        fail("mechanical matrix")
    if not all(x.get("families") == 3 and x.get("roles") == 12 and x.get("sources_loaded") == "5/5" for x in modes):
        fail("mechanical matrix counts")
    if not all(x.get("no_image_descendant_images") == 0 and x.get("page_overflow") is False and x.get("internal_overflow") == 0 for x in modes):
        fail("mechanical matrix fallback/overflow")
    if preflight.get("result", {}).get("surviving_families") != ["IMG-F1", "IMG-F2", "IMG-F3"]:
        fail("preflight survivors")
    if preflight.get("result", {}).get("subjective_scoring_started") is not False or preflight.get("result", {}).get("new_generated_visual_exemplars_consumed") is not False:
        fail("premature preflight scoring/generation")
    if preflight.get("drive_review_folder", {}).get("id") != "1FdfoCY4pjsTRs3AuCUczDrHbq3rj-p40":
        fail("Drive review folder")
    expected_drive_ids = ["1_DatC27ZFudlJDh3eNNY8h8XhRhp-ZSd", "1YUHiHkfHFPbtMO9fJLraZwSm0H878uuJ", "1UXG2nJrfNnTWSahUwvNzfe8JtbqWmIPT", "120Hmh6WYzOOaN2vFRy8F04GdcBXe5MrE", "1HeU08xD-P0JLVVVoaqXrNJwr_nG_PgfB"]
    if [x.get("drive_file_id") for x in preflight.get("drive_review_masters", [])] != expected_drive_ids:
        fail("Drive review master ids")

    if exposure.get("status") != "RECORDED_AFTER_MECHANICAL_PREFLIGHT_BEFORE_SUBJECTIVE_SCORING":
        fail("prior exposure status")
    sources = exposure.get("drive_sources", [])
    if [x.get("document_id") for x in sources] != ["1KJeorPBsNnRivFVFJQqKB3CsB6nHtlLiApfAHxh0-VU", "1VXug3hCV-LDyfgqN5QXh6aNOB-G5W3CtR_TFdClGcns"]:
        fail("prior source document ids")
    if exposure.get("event", {}).get("independence_effect") is None or exposure.get("event", {}).get("generated_exemplar_prompts_affected") is not False:
        fail("prior exposure boundary")
    q = exposure.get("quarantine_law", {})
    if "frozen IMG-01" not in q.get("prompt_construction", "") or "Do not add" not in q.get("candidate_criteria", ""):
        fail("prior quarantine law")
    if exposure.get("recursive_audit", {}).get("blind_independence_claim_withdrawn") is not True:
        fail("blind independence correction")

    if packets.get("status") != "FROZEN_EXTERNAL_ISOLATED_EXECUTION_READY_NO_RENDER_RESULT":
        fail("renderer packet status")
    if packets.get("execution_protocol", {}).get("images_per_context") != 1:
        fail("renderer packet image count")
    if packets.get("execution_protocol", {}).get("drive_destination_folder_id") != "1FdfoCY4pjsTRs3AuCUczDrHbq3rj-p40":
        fail("renderer packet Drive destination")
    packet_rows = packets.get("packets", [])
    if [x.get("id") for x in packet_rows] != ["IMG-F1", "IMG-F2", "IMG-F3"]:
        fail("renderer packet order")
    prohibited = ["Kymaean", "Ensemble", "Director", "APP-SYN", "IMG-F1", "IMG-F2", "IMG-F3", "pre-candidate"]
    shared = [
        "exactly three distinct, specific adults",
        "A and B carry the strongest current relational focus",
        "C remains visibly present, specific and relevant",
        "Before this depicted moment, one completed human action changed the shared present",
        "without explaining private motive, belief, knowledge, emotion or hidden state",
        "Do not prescribe or depend on a brand palette",
        "No UI, text, labels, logos, design-board framing",
    ]
    for row in packet_rows:
        prompt = row.get("renderer_visible_prompt", "")
        if not all(token in prompt for token in shared):
            fail(f"renderer packet shared parity {row.get('id')}")
        if any(token in prompt for token in prohibited):
            fail(f"renderer packet contamination {row.get('id')}")
        if not prompt.endswith("Return only the uninterrupted artwork."):
            fail(f"renderer packet output contract {row.get('id')}")
    pa = packets.get("prompt_audit", {})
    if pa.get("shared_facts_identical") is not True or pa.get("director_prior_visible_to_renderer") is not False:
        fail("renderer packet parity/prior audit")
    if pa.get("subjective_family_scoring_started") is not False or pa.get("new_visual_generation_consumed") is not False:
        fail("renderer packet pre-execution boundary")
    for token in ("IMG-01", AUDIT.relative_to(ROOT).as_posix(), AUDIT_SHA, METHOD_SHA, STAGE0_SHA, FAMILIES_SHA,
                  PREFLIGHT.relative_to(ROOT).as_posix(), PREFLIGHT_SHA, EXPOSURE.relative_to(ROOT).as_posix(), EXPOSURE_SHA,
                  PACKETS.relative_to(ROOT).as_posix(), PACKETS_SHA,
                  "MECHANICAL PREFLIGHT PASS", "ALL 3 FAMILIES SURVIVE", "DIRECTOR PRIOR EXPOSED PRE-SCORING",
                  "RENDERER PACKETS FROZEN", "EXTERNAL ISOLATED FIRST-RENDER EXECUTION NEXT", "NO SUBJECTIVE RANKING", "ZERO RENDERS"):
        if token not in current:
            fail(f"CURRENT_STATE missing {token}")
    if "L-154 - IMG-01 mechanical preflight passes; Director prior exposure is quarantined before scoring" not in ledger:
        fail("ledger L-154 missing")
    if "L-155 - IMG-01 sterile renderer packets are frozen for three isolated first outputs" not in ledger:
        fail("ledger L-155 missing")
    bad = [ord(c) for c in ledger if ord(c) < 32 and c not in "\n\r\t"]
    if bad:
        fail(f"ledger control characters: {bad}")

    print("IMG_01_RENDERER_PACKETS=PASS")
    print(f"AUDIT_SHA256={AUDIT_SHA}")
    print(f"METHOD_SHA256={METHOD_SHA}")
    print(f"STAGE0_SHA256={STAGE0_SHA}")
    print(f"FAMILIES_SHA256={FAMILIES_SHA}")
    print(f"PREFLIGHT_SHA256={PREFLIGHT_SHA}")
    print(f"EXPOSURE_SHA256={EXPOSURE_SHA}")
    print(f"PACKETS_SHA256={PACKETS_SHA}")
    print("FAMILIES=3 PAIRWISE_DIVERGENCE=6/7/6 MODES=5 DRIVE_MASTERS=5 PACKETS=3 RENDERS=0")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"IMG_01_FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
