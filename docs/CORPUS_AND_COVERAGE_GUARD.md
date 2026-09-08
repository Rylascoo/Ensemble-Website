<!-- D-R1-STATUS: ACTIVE LAW -->

# Corpus and coverage guard

Run `python3 tools/validate_document_status.py` in a complete Git checkout.
A, INDEX, B and C run independently; any failure exits 1.

A extends collection to text under docs/ and retains repo-wide Markdown.
Every document needs the existing canonical first-line header. Failures are
listed individually. Index rendering is unchanged, including its existing
label and ordering. INDEX always compares bytes, even while A fails. Invalid
headers are excluded from the comparison because they have no authoritative
group; INDEX still fails closed when any document cannot be indexed. It reports
both an index mismatch and incomplete coverage when both apply.

Fixing the existing .txt markers REQUIRES regenerating docs/INDEX.md in the same
change: collect_statuses feeds text files into render_index (329+ entries,
rather than the committed 282). The generator refuses invalid headers. Packet
02-A therefore regenerates only the Markdown projection to add this one newly
conforming document: 283 entries. It neither classifies nor indexes invalid
text files. Full corpus/index validation remains failing until that existing
debt is corrected in an authorized change.

B groups SVG/JSON files by their immediate evidence directory, including the
evidence root. It searches every tools file and YAML workflow for literal
repository-relative directory references with path boundaries. Parent
references do not cover children; child references also mention their parent.
This detects lexical tooling references, not effective validation or prose
governance. Renderer artifacts remain governed by audit prose.

C uses `git rev-list --count <last-state-modification>..HEAD`, fails above 3,
and prints intervening subjects. Missing state/history, shallow clones and
Git errors fail closed. The existing CI job fetches full history; checkout
uses the engineering repository's v7.0.1 commit SHA.
Path filters were removed so every push/PR runs currency; no job was added.

## Verification

Branch: `tooling/corpus-coverage-guard-02`, based on freshly fetched origin/main
at `7ed2da9617e119a3208789d3e5f0e694bd6c2f41`.
Detached fixture worktrees have only the two updated scripts and workflow
overlaid. Both fixture commits are ancestors of the branch base. Files were
materialized with committed bytes to avoid Windows checkout CRLF conversion.
The bundled Python executable ran the validator; python3 is unavailable here.
The new document is excluded from the immutable fixture runs.

Both fixtures have 279 docs/ Markdown files, 282 repo-wide, and 50 text files.
48 text files have no marker; two first contain markers at lines 28 and 31,
with further example markers later. All 50 fail the first-line contract.

Only this new document received a first-line marker. No existing document
received a marker. The Markdown index change adds only this document and
updates the total/ACTIVE LAW counts. State and evidence content is unchanged.
The authored branch has 50 text marker failures, not 51 document failures.

## Raw verification output (Packet 02-A)

### a4db6d7

```text
FAIL: docs/evidence/D_R1_ASTRA_MECHANICAL_CENSUS_ARTIFACT_MANIFEST_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_ASTRA_MECHANICAL_CENSUS_TASK_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_ASTRA_PHASE_2_MECHANICAL_IMPLEMENTATION_TASK_01.txt: canonical D-R1 header must be the first line
FAIL: docs/evidence/D_R1_ASTRA_PHASE_2_MECHANICAL_IMPLEMENTATION_TASK_02.txt: canonical D-R1 header must be the first line
FAIL: docs/evidence/D_R1_PHASE_0_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_0_CLOSURE_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_2_ADOPTION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_3_BRANCH_DISPOSITION_VERIFICATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_3_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_4_PUBLICATION_SOURCE_BOUNDARY_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_5_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_5_CLOSURE_AUDIT_CONTRACT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_POST_PHASE_4_NEXT_PHASE_AUTHORITY_GAP_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_ROUND_06_EVALUATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_07_RECURSIVE_PRE_RENDER_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_07_STERILE_ARTWORK_TRANSLATION_PACKAGE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_CONSTRUCTION_STAGES_01_05.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_ROUND_07_EVALUATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_07_RECURSIVE_PRE_RENDER_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_07_STERILE_ARTWORK_TRANSLATION_PACKAGE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_6M_NEUTRAL_PHYSICAL_MAQUETTE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_STAGE_6M_PREFLIGHT_TOOLING_DEFECT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_08_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_CORRECTED_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_WORKING_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CANDIDATE_MECHANISM_GEOMETRY_INVESTIGATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CANDIDATE_MECHANISM_GEOMETRY_INVESTIGATION_01_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CHANGE_TO_POSTURE_MECHANISM_GEOMETRY_INVESTIGATION_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_NEUTRAL_PHYSICAL_MAQUETTE_TRANSFER_ADDENDUM_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_NEUTRAL_PHYSICAL_MAQUETTE_TRANSFER_ADDENDUM_01_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_POST_ROUND_06_TRANSFER_FIDELITY_REVIEW_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_POST_ROUND_07_TRANSFER_FIDELITY_CAUSAL_TOPOLOGY_REVIEW_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_PHYSICAL_UNION_RENDERER_CORRECTION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_CLOSURE_AND_D9_REENTRY_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_FORMAT_IMPLEMENTATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_HARDENING_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_TRANSFER_SURFACE_SUFFICIENCY_INVESTIGATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/STAGE_CONE_INTERACTION_01_ORACLE.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_ROUND04_RENDERER_HANDOFF.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_ROUND05_RENDERER_HANDOFF.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_TRANSFER_FIDELITY_RENDERER_PACKET_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C06-ASPB-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C07-CBSR-01_STAGE07_SANITIZED_MAQUETTE_REFERENCE_SHA256.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C07-CBSR-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
A: 50 .txt marker failures; 50 total document failures
INDEX: FAIL: 50 documents have invalid headers; full corpus index cannot be verified (valid-document byte comparison: PASS)
COVERED: docs/evidence/ (2 files)
UNCOVERED: docs/evidence/renderer/ (7 files)
UNCOVERED: docs/evidence/renderer/rejected/ (1 files)
UNCOVERED: docs/evidence/scaffolds/ (8 files)
UNCOVERED: docs/evidence/scaffolds/rejected/ (1 files)
COVERED: docs/evidence/stage6m/ (6 files)
B: FAIL: 4 uncovered directories / 17 files
C: FAIL: CURRENT_STATE.md currency distance 6 (maximum 3)
Approve Candidate 08 Stage 6 scaffold
Add Candidate 08 Stage 6 neutral scaffold
Add Candidate 08 Stage 6 scaffold manifest
Approve D9-S2 stages 1-5 as Candidate 08
Correct D9-S2 stages 1-5 before audit
Construct D9-S2 Method 02 stages 1-5
EXIT CODE: 1
```

### 7ed2da9

```text
FAIL: docs/evidence/D_R1_ASTRA_MECHANICAL_CENSUS_ARTIFACT_MANIFEST_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_ASTRA_MECHANICAL_CENSUS_TASK_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_ASTRA_PHASE_2_MECHANICAL_IMPLEMENTATION_TASK_01.txt: canonical D-R1 header must be the first line
FAIL: docs/evidence/D_R1_ASTRA_PHASE_2_MECHANICAL_IMPLEMENTATION_TASK_02.txt: canonical D-R1 header must be the first line
FAIL: docs/evidence/D_R1_PHASE_0_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_0_CLOSURE_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_2_ADOPTION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_3_BRANCH_DISPOSITION_VERIFICATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_3_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_4_PUBLICATION_SOURCE_BOUNDARY_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_5_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_5_CLOSURE_AUDIT_CONTRACT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_POST_PHASE_4_NEXT_PHASE_AUTHORITY_GAP_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_ROUND_06_EVALUATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_07_RECURSIVE_PRE_RENDER_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_07_STERILE_ARTWORK_TRANSLATION_PACKAGE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_CONSTRUCTION_STAGES_01_05.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_ROUND_07_EVALUATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_07_RECURSIVE_PRE_RENDER_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_07_STERILE_ARTWORK_TRANSLATION_PACKAGE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_6M_NEUTRAL_PHYSICAL_MAQUETTE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_STAGE_6M_PREFLIGHT_TOOLING_DEFECT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_08_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_CORRECTED_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_WORKING_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CANDIDATE_MECHANISM_GEOMETRY_INVESTIGATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CANDIDATE_MECHANISM_GEOMETRY_INVESTIGATION_01_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CHANGE_TO_POSTURE_MECHANISM_GEOMETRY_INVESTIGATION_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_NEUTRAL_PHYSICAL_MAQUETTE_TRANSFER_ADDENDUM_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_NEUTRAL_PHYSICAL_MAQUETTE_TRANSFER_ADDENDUM_01_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_POST_ROUND_06_TRANSFER_FIDELITY_REVIEW_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_POST_ROUND_07_TRANSFER_FIDELITY_CAUSAL_TOPOLOGY_REVIEW_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_PHYSICAL_UNION_RENDERER_CORRECTION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_CLOSURE_AND_D9_REENTRY_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_FORMAT_IMPLEMENTATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_HARDENING_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_TRANSFER_SURFACE_SUFFICIENCY_INVESTIGATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/STAGE_CONE_INTERACTION_01_ORACLE.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_ROUND04_RENDERER_HANDOFF.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_ROUND05_RENDERER_HANDOFF.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_TRANSFER_FIDELITY_RENDERER_PACKET_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C06-ASPB-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C07-CBSR-01_STAGE07_SANITIZED_MAQUETTE_REFERENCE_SHA256.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C07-CBSR-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
A: 50 .txt marker failures; 50 total document failures
INDEX: FAIL: 50 documents have invalid headers; full corpus index cannot be verified (valid-document byte comparison: PASS)
COVERED: docs/evidence/ (2 files)
UNCOVERED: docs/evidence/renderer/ (7 files)
UNCOVERED: docs/evidence/renderer/rejected/ (1 files)
UNCOVERED: docs/evidence/scaffolds/ (8 files)
UNCOVERED: docs/evidence/scaffolds/rejected/ (1 files)
COVERED: docs/evidence/stage6m/ (6 files)
B: FAIL: 4 uncovered directories / 17 files
C: PASS: CURRENT_STATE.md currency distance 0 (maximum 3)
EXIT CODE: 1
```

### branch

```text
FAIL: docs/evidence/D_R1_ASTRA_MECHANICAL_CENSUS_ARTIFACT_MANIFEST_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_ASTRA_MECHANICAL_CENSUS_TASK_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_ASTRA_PHASE_2_MECHANICAL_IMPLEMENTATION_TASK_01.txt: canonical D-R1 header must be the first line
FAIL: docs/evidence/D_R1_ASTRA_PHASE_2_MECHANICAL_IMPLEMENTATION_TASK_02.txt: canonical D-R1 header must be the first line
FAIL: docs/evidence/D_R1_PHASE_0_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_0_CLOSURE_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_2_ADOPTION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_3_BRANCH_DISPOSITION_VERIFICATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_3_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_4_PUBLICATION_SOURCE_BOUNDARY_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_5_CLOSURE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_PHASE_5_CLOSURE_AUDIT_CONTRACT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/D_R1_POST_PHASE_4_NEXT_PHASE_AUTHORITY_GAP_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_ROUND_06_EVALUATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_07_RECURSIVE_PRE_RENDER_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_06_METHOD_02_STAGE_07_STERILE_ARTWORK_TRANSLATION_PACKAGE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_CONSTRUCTION_STAGES_01_05.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_ROUND_07_EVALUATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_07_RECURSIVE_PRE_RENDER_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_07_STERILE_ARTWORK_TRANSLATION_PACKAGE_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_METHOD_02_STAGE_6M_NEUTRAL_PHYSICAL_MAQUETTE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_07_STAGE_6M_PREFLIGHT_TOOLING_DEFECT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_CANDIDATE_08_METHOD_02_STAGE_06_NEUTRAL_GEOMETRY_SCAFFOLD_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_CORRECTED_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_RECURSIVE_AUDIT_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_S2_CONSTRUCTION_STAGES_01_05_WORKING_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CANDIDATE_MECHANISM_GEOMETRY_INVESTIGATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CANDIDATE_MECHANISM_GEOMETRY_INVESTIGATION_01_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_D9_SUCCESSOR_CHANGE_TO_POSTURE_MECHANISM_GEOMETRY_INVESTIGATION_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_NEUTRAL_PHYSICAL_MAQUETTE_TRANSFER_ADDENDUM_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_NEUTRAL_PHYSICAL_MAQUETTE_TRANSFER_ADDENDUM_01_RECURSIVE_AUDIT.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_POST_ROUND_06_TRANSFER_FIDELITY_REVIEW_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_POST_ROUND_07_TRANSFER_FIDELITY_CAUSAL_TOPOLOGY_REVIEW_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_PHYSICAL_UNION_RENDERER_CORRECTION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_CLOSURE_AND_D9_REENTRY_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_FORMAT_IMPLEMENTATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_STAGE_6M_TOOLING_HARDENING_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/HERO_METHOD_02_TRANSFER_SURFACE_SUFFICIENCY_INVESTIGATION_01.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/STAGE_CONE_INTERACTION_01_ORACLE.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_ROUND04_RENDERER_HANDOFF.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_ROUND05_RENDERER_HANDOFF.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C04-ACLT-01_TRANSFER_FIDELITY_RENDERER_PACKET_02.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C06-ASPB-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C07-CBSR-01_STAGE07_SANITIZED_MAQUETTE_REFERENCE_SHA256.txt: expected one D-R1 header, found 0
FAIL: docs/evidence/renderer/C07-CBSR-01_STAGE07_STERILE_RENDERER_PACKET.txt: expected one D-R1 header, found 0
A: 50 .txt marker failures; 50 total document failures
INDEX: FAIL: 50 documents have invalid headers; full corpus index cannot be verified (valid-document byte comparison: PASS)
COVERED: docs/evidence/ (2 files)
UNCOVERED: docs/evidence/renderer/ (7 files)
UNCOVERED: docs/evidence/renderer/rejected/ (1 files)
UNCOVERED: docs/evidence/scaffolds/ (8 files)
UNCOVERED: docs/evidence/scaffolds/rejected/ (1 files)
COVERED: docs/evidence/stage6m/ (6 files)
B: FAIL: 4 uncovered directories / 17 files
C: PASS: CURRENT_STATE.md currency distance 0 (maximum 3)
EXIT CODE: 1
```
