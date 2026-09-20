<!-- D-R1-STATUS: ACTIVE LAW -->

# Q-ADMIN-05 App Design Source Freeze

Status: **FROZEN FOR TRANSFER - DEPENDENCY COMPLETE / AUTHORITY TRANSFER NOT EXECUTED**

Package: `ADMIN-Q05-SOURCE-FREEZE-01`

## Frozen authority boundary

| Alias | Repository / role | Exact commit |
|---|---|---|
| `W` | `Rylascoo/Ensemble-Website` correction baseline / then-live `main` source | `cf28c80161bdf7157e8063ed27e56fc70dd438fc` |
| `A` | Website active APPUI authority | `33b8e13c4e71c8ceee1fdc3a646f291c9422a047` |
| `F` | Website FIRSTUSE evidence branch | `e2e4119dcffc9082378a822c048523c9675c1bf6` |
| `H` | Website Home re-entry evidence branch | `4c73d02c6a1c85d860024a9e2d55b3ef490906b3` |
| `R` | Ryladmin Q-ADMIN-05 authority | `452c1730aaa68da1d03bc18ee080ca9eb41df337` |
| `P` | Project receiving authority / merged PR 234 | `734f27878b0976ff5f63945070d059000d50c719` |

This packet freezes source identity only. It does not copy material to Project, relinquish Website authority, modify Drive, choose Home A/B, adopt FIRSTUSE, change production Website behavior, or resume application design.

## Dependency-completeness correction

The first integrated revision was **source-classification complete** and verified all **98/98 recorded source identities**, but it was not dependency-complete. Project correctly stopped before materialization because the Stage presentation successor method had no identity record and C03 did not deterministically resolve its APPUI-era versus live-main `DESIGN_CONTINUITY.md` dependency.

This correction also closes one same-class omission found by the required all-bundle revalidation: C03 explicitly names the engineering-informed translation law, so that current Website object is now recorded rather than left as unsealed context.

Corrected counts and scope:

- receiving-manifest bundles: **22**;
- recorded source identities: **100** exact alias/path/blob/byte/SHA-256 records;
- dependency identities: **100** exact records in the closed source/dependency object set;
- unresolved dependency identities: **0**;
- transfer forms: **unchanged** at 5 whole-document, 2 selected-section, 8 normalized-contract, 4 pointer, 2 evidence-only and 1 do-not-transfer.

For these counts, a source identity is one appendix alias/path record. A dependency identity is a source identity proved reachable from at least one bundle's source or direct-dependency closure; repeated use is counted once. The appendix is therefore both the source-object set and the closed dependency-object set. Project and Drive authority named only as destination constraints, ownership locators, or pointer values do not authorize transferred source bytes and are not counted as Website dependency objects.

## Website-data exclusion

The receiving set contains no Website-only data. `site/**`, kymaean.com implementation, Website hero/doorway assets and evidence, Website motion/CSS, Website responsive behavior, Website copy/presentation, Website accessibility evidence, hosting/deployment records, Website `intelligence/` and `updates/`, and PR 147 artifacts are excluded. A mixed source is eligible only for the named application or genuinely cross-surface clauses below. Website-specific clauses, examples, IDs, binaries, results and implementation details remain Website authority and are not transfer dependencies.

## Bundle classification and provenance

Every row is one Project receiving-manifest bundle. File identities are in the appendix. `NORMALIZE` preserves the named active meaning with source locators; `POINTER` carries no source contract bytes; `EVIDENCE` preserves a pending/unresolved evidence locator without adoption.

| ID | Source and exact section | Active role and dependencies | Transfer form | Destination / post-transfer source state |
|---|---|---|---|---|
| A01 | `W:docs/KYMAEAN_EXPERIENCE_ONTOLOGY_SYNTHESIS_01.md`, §§1-10, 12-18; exclude §11 Website responsibility | App experience ontology; Project Product law controls | `NORMALIZED_ACTIVE_CONTRACT` | `docs/design/app/contracts/EXPERIENCE_ONTOLOGY.md`; `TRANSITION_POINTER_TO_PROJECT` |
| A02 | `A:docs/KYMAEAN_APPUI_PHASE_1_STAGE_INTERFACE_ENVELOPE_AND_LAYOUT_MAP_01.md`, whole document | L0-L3 shell/workspace/Stage/depth layout; depends A01 | `NORMALIZED_ACTIVE_CONTRACT` | `docs/design/app/contracts/STAGE_INTERFACE_ENVELOPE_AND_LAYOUT.md`; `HISTORICAL_SOURCE_RETAINED` |
| A03 | `A:docs/KYMAEAN_APPUI_COMPONENT_SYSTEM_FOUNDATION_01.md`, whole document | App control/input/list/disclosure grammar; depends A02 | `NORMALIZED_ACTIVE_CONTRACT` | `docs/design/app/contracts/COMPONENT_SYSTEM_FOUNDATION.md`; `HISTORICAL_SOURCE_RETAINED` |
| A04 | `A:docs/KYMAEAN_APPUI_PHASE_3_STATIC_APP_VISUAL_SYSTEM_01.md` plus named JSON reference | Active F2/D3, MAT F1, TYP F1/Source Sans 3, STA F2 and FICON references; token/package limits preserved | `NORMALIZED_ACTIVE_CONTRACT` | Project static contract plus verbatim evidence; `HISTORICAL_SOURCE_RETAINED` |
| A05 | `A:docs/KYMAEAN_APPUI_NATIVE_IMPLEMENTATION_HANDOFF_01.md` plus three named reference/packet/reconciliation JSON files | Design-to-Engineering consumption/return and APPUI-QDESIGN20-R2; depends A02-A04 and Project contracts | `NORMALIZED_ACTIVE_CONTRACT` | Project native contract/evidence; `HISTORICAL_SOURCE_RETAINED` |
| A06 | Seven `A:docs/evidence/APPUI_ALPHA_*` files listed in the appendix | Conditional Alpha/Stage static law; depends A01-A04 | `WHOLE_DOCUMENT` | Project `contracts/alpha-stage/`; `HISTORICAL_SOURCE_RETAINED` |
| A07 | COMP-03 method/result/carrier/probe closure | Studio/shaping expression; no storage or editing-command adoption | `WHOLE_DOCUMENT` | Project component evidence/reference closure; `HISTORICAL_SOURCE_RETAINED` |
| A08 | COMP-04 and COMP-06 method/result/carrier/probe closures | Archive contextual/deep and causal/history inspection; no permanent Archive tab | `WHOLE_DOCUMENT` | Project component evidence/reference closure; `HISTORICAL_SOURCE_RETAINED` |
| A09 | COMP-07 and COMP-10 closures plus A02 | Creator/Audience/Character-bounded disclosure; agency/timing remains open | `NORMALIZED_ACTIVE_CONTRACT` | Project perspectives contract plus evidence; `HISTORICAL_SOURCE_RETAINED` |
| A10 | COMP-08, COMP-09 and COMP-11 closures | App/failure state presentation; fixtures/hooks create no Product operation | `NORMALIZED_ACTIVE_CONTRACT` | Project app/failure contract plus evidence; `HISTORICAL_SOURCE_RETAINED` |
| A11 | A02 §§9,11; A03 §9; A04 §§7-8,10; A06 state-witness/responsive clauses | Keyboard/focus return, non-color state, reflow/text, forced colors and reduced motion; native proof pending | `SELECTED_SECTIONS` | `docs/design/app/contracts/ACCESSIBILITY.md`; `TRANSITION_POINTER_TO_PROJECT` |
| A12 | Two Stage packet JSON files, the whole Stage successor method, Stage successor result, and six Stage carrier/materializer/probe dependencies | Stage carrier/presentation and derivative provenance; the method is the supporting frozen pre-exposure law for the selected S1 result; Drive retains master ownership | `WHOLE_DOCUMENT` | Project Stage evidence; `HISTORICAL_SOURCE_RETAINED` |
| A13 | `A:docs/evidence/DESIGN_LEDGER.md`, exactly 34 entries listed below | Active adoption/provisionality/hold register | `SELECTED_SECTIONS` | Project app ledger; original full ledger remains `HISTORICAL_SOURCE_RETAINED` |
| A14 | COMP-01..11 exact method/result/carrier/probe closure plus the seven Stage dependencies, including the successor method | Reproducible implementation-reference closure; rejected/intermediate carriers excluded | `WHOLE_DOCUMENT` | Project evidence/prototype/tool reference subtrees; `HISTORICAL_SOURCE_RETAINED` |
| C01 | Two motion packets and ten named contract/adjudication dependencies | Provisional shared motion principle only; app adaptation Project, Website adaptation Website, cross-surface governance Ryladmin | `PROVENANCE_POINTER` | Project pointer; `CROSS_SURFACE_POINTER_TO_RYLADMIN` |
| C02 | `W:docs/DESIGN_CONTINUITY.md` §3 shared/app clauses, §11 master/provenance rule, and only the app-exclusion clauses of §§18-23; §24 and all Website-specific clauses excluded | Cross-surface identity/use exclusions; Drive masters unchanged; no app mascot placement | `PROVENANCE_POINTER` | Project pointer; `CROSS_SURFACE_POINTER_TO_RYLADMIN` and `DRIVE_MASTER_POINTER` |
| C03 | App/cross-surface clauses only from `W:AGENTS.md`, `W:docs/DESIGN_CONTINUITY.md`, `W:docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md`, and `W:docs/KYMAEAN_ENGINEERING_INFORMED_VISUAL_TRANSLATION_PROTOCOL_01.md`; all Website implementation clauses excluded | Ryladmin-governed routing and validation boundary; `CURRENT_MAIN_DEPENDENCY_REQUIRED`; owning repositories retain surface implementation law | `NORMALIZED_ACTIVE_CONTRACT` | Coordinated owning amendments only; `WEBSITE_ONLY_REMAINDER` |
| C04 | Framework, registry and APP-SYN packet at A | Project-primary app packet identity/current closure; original research remains Website history | `PROVENANCE_POINTER` | Project normalized index/pointers; `HISTORICAL_SOURCE_RETAINED` |
| D01 | Six exact H Home review/study carriers | Two co-equal alternatives; decision is `UNRESOLVED_APP_DESIGN_DECISION` | `EVIDENCE_REFERENCE_ONLY` | Later Project unresolved pointer only; `HISTORICAL_SOURCE_RETAINED` |
| D02 | Exact F FIRSTUSE carrier and closeout JSON | `EVIDENCE_PENDING_ADOPTION`; no creation/import schema promotion | `EVIDENCE_REFERENCE_ONLY` | Later Project pending-evidence pointer only; `HISTORICAL_SOURCE_RETAINED` |
| D03 | Drive IDs below, with repository authority locators | Duplicate/conflicting non-authoritative app-design holdings; repository contracts prevail until exact conflict review | `PROVENANCE_POINTER` | Project Drive-reconciliation pointer; `DRIVE_MASTER_POINTER` |
| D04 | C01/C02 clauses plus Ryladmin charter | Stewardship resolved by Director: app-specific motion Project; Website-specific motion Website; small genuinely cross-surface motion/general brand-use principles Ryladmin | `DO_NOT_TRANSFER` | No duplicate contract; coordinated pointers/amendments only |

Counts: **5 whole-document; 2 selected-section; 8 normalized-contract; 4 pointer; 2 evidence-only; 1 do-not-transfer = 22 bundles.**

## Corrected dependency determinations

### A12 Stage presentation successor method

The required successor-method source is the whole document `A:docs/evidence/APPUI_01_STAGE_PRESENTATION_SUCCESSOR_METHOD_01.json` at Website commit `33b8e13c4e71c8ceee1fdc3a646f291c9422a047`, blob `aa9b9fc575d5c9d1dd0412c76039b0f51c863be1`, 5,401 bytes, SHA-256 `ce6d074c3b8df82e7f59d820ab77a3823d1ab76af026977ac8cd4eedb9b7c712`.

Classification: **supporting method**. It is the frozen pre-exposure law directly named by `APPUI_01_STAGE_PRESENTATION_SUCCESSOR_RESULT_01.json` and `PKT_APPUI_STAGE_PRESENTATION_01.json`. It governs the exact-pixel R1/S1 construction, invariants, falsifiers, seven-case matrix and selection law used to produce the frozen S1 shell-facing presentation. It does not replace current Stage semantic authority (`PKT-STAGE-CORE-02`), does not redesign Stage, and is neither current standalone Stage authority nor a historical predecessor.

### C03 continuity dependency

The APPUI branch snapshot that made the dependency ambiguous was `A:docs/DESIGN_CONTINUITY.md` at commit `33b8e13c4e71c8ceee1fdc3a646f291c9422a047`, blob `301229b64d462ef83edf544652dccd14d7747fae`, 23,557 bytes, SHA-256 `1136cb0a74cb8b87f5f47c353f1118bdea4d7da08f136f8473261c3b2f521201`. It is preserved as historical comparison evidence only and is not a transfer dependency.

The required C03 dependency is `W:docs/DESIGN_CONTINUITY.md` at `cf28c80161bdf7157e8063ed27e56fc70dd438fc`, blob `a99b00a2afd09686ff625076ae615ffd82fe0d73`, 37,177 bytes, SHA-256 `a9ea2787d1d14ccbfa823271bf42f583aa7f5b1c956ee4c412c3ab4c83f88b74`. This is byte-identical to the version already sealed at the predecessor W alias `b016ad864d829b8dadcaf12ad5e1212fa0bcd12f` and to live Website main at correction start.

Classification: **`CURRENT_MAIN_DEPENDENCY_REQUIRED`**. The versions differ because the APPUI branch forked before commit `82e91265ccee9955604d1386e6cdb4c37cfd2b57` integrated later durable Design continuity. The earlier clauses remain semantically present in current main, while current main adds durable cross-surface mascot/app-exclusion law needed to prevent C03 from being normalized as broader app-placement authority. Substituting the historical APPUI snapshot would omit current governing exclusions; no historical-only C03 semantic requires the older bytes.

C03 uses the following exact current-main ranges: `AGENTS.md` Design Sol role, fresh-chat reconciliation, cross-project execution-queue, dispatch, residency, backend-boundary and authority/evidence clauses; `DESIGN_CONTINUITY.md` §§1-4, the app/cross-surface clauses of §§6-17, and only the app-exclusion/cross-surface clauses of §§18-23; the visual-workflow authority's accountable-role, cross-lane, external-work, validation-boundary and earned-approval clauses; and the engineering-informed translation protocol's §§Purpose through Guardrail. `DESIGN_CONTINUITY.md` §24 and all Website implementation/production clauses remain excluded.

## Full 22-bundle dependency closure

Every path named below resolves through its alias to an exact appendix blob/byte/SHA-256 record. “Direct dependencies” names semantic bundle edges or exact supporting object groups; it does not expand destination-side Project law into Website source bytes.

| ID | Exact source/section and identity set | Transfer form | Direct dependencies / closure result |
|---|---|---|---|
| A01 | W experience ontology, §§1-10 and 12-18 | `NORMALIZED_ACTIVE_CONTRACT` | Project Product law is a destination constraint; one exact W object; closed |
| A02 | A Phase-1 Stage envelope, whole document | `NORMALIZED_ACTIVE_CONTRACT` | A01; one exact A object; closed |
| A03 | A component-system foundation, whole document | `NORMALIZED_ACTIVE_CONTRACT` | A02; one exact A object; closed |
| A04 | A Phase-3 static system, whole document, plus its named JSON reference | `NORMALIZED_ACTIVE_CONTRACT` | two exact A objects; closed |
| A05 | A native handoff, whole document, plus reference map, handoff packet and reconciliation JSON | `NORMALIZED_ACTIVE_CONTRACT` | A02-A04 and destination Project contracts; four exact A objects; closed |
| A06 | Seven exact A06-closure JSON objects | `WHOLE_DOCUMENT` | A01-A04; seven exact A objects; closed |
| A07 | COMP-03 method/result/carrier/probe quartet | `WHOLE_DOCUMENT` | four exact A objects; closed |
| A08 | COMP-04 and COMP-06 method/result/carrier/probe quartets | `WHOLE_DOCUMENT` | eight exact A objects; closed |
| A09 | COMP-07 and COMP-10 quartets plus A02 | `NORMALIZED_ACTIVE_CONTRACT` | A01/A02 and destination Product truth/access law; nine exact A records; closed |
| A10 | COMP-08, COMP-09 and COMP-11 quartets | `NORMALIZED_ACTIVE_CONTRACT` | destination Application/Persistence truth; twelve exact A objects; closed |
| A11 | A02 §§9,11; A03 §9; A04 §§7-8,10; A06 state-witness and responsive clauses | `SELECTED_SECTIONS` | A02-A04/A06; five exact A records; closed |
| A12 | Two Stage packets; whole successor method; whole successor result; two Stage carriers, two materializers and two probes | `WHOLE_DOCUMENT` | A06 plus exact Drive master locator/hash carried inside the Stage objects; ten exact A records; closed |
| A13 | A Design Ledger, exactly the 34 listed entries | `SELECTED_SECTIONS` | named decisions/dependencies resolve through A01-A12/A14; one exact A ledger object; closed |
| A14 | COMP-01..11 component/prototype closure plus the seven-object Stage reference closure including the successor method | `WHOLE_DOCUMENT` | A05-A12; every exact method/result/carrier/materializer/probe record is in the appendix; closed |
| C01 | Two motion packets plus the ten named MOT contract/adjudication dependencies | `PROVENANCE_POINTER` | twelve exact A objects; closed |
| C02 | W continuity §3, §11 and named app-exclusion clauses of §§18-23 | `PROVENANCE_POINTER` | exact W continuity object and literal Drive locators; closed |
| C03 | Four exact current-main W objects and the ranges stated above | `NORMALIZED_ACTIVE_CONTRACT` | current-main continuity required; Ryladmin governs coordination; closed |
| C04 | A framework, registry and APP-SYN packet | `PROVENANCE_POINTER` | three exact A objects; closed |
| D01 | Six exact H Home carriers | `EVIDENCE_REFERENCE_ONLY` | no selection; six exact H objects; closed |
| D02 | Exact F FIRSTUSE carrier and closeout | `EVIDENCE_REFERENCE_ONLY` | no adoption; two exact F objects; closed |
| D03 | Literal Drive IDs in this packet; no Drive bytes transfer | `PROVENANCE_POINTER` | repository authority remains controlling; no unrecorded external byte dependency; closed |
| D04 | C01/C02 clauses plus exact R authority locator | `DO_NOT_TRANSFER` | no destination contract bytes; stewardship decision preserved; closed |

## Selected Design Ledger manifest

All entries originate at `A`, source blob `be4c9ffcecb8366694836b691b3916f4033b1f9f`, source SHA-256 `1d281e3134332c39d04307853db366ef950106e0e6a1aa7311fdc27098b46682`. Destination is the Project app ledger. Normalize each active decision while retaining the original ID/ref and quote its `State` line verbatim. Entries L-247, L-249 and L-251 are provenance links only because their successor decisions carry current authority.

| Entries | Semantic decision carried forward | Destination treatment |
|---|---|---|
| L-203 | F2 Monochrome + Intruder selected; no production token authority | normalize + quote state |
| L-226-L-228 | D3 selected; static system/reference consolidated; production tokens remain open | normalize + quote state |
| L-233 | F1 Native Quiet Carrier sole conventional-icon survivor | normalize + quote state |
| L-235-L-246 | COMP-01..11 active shell/workspace integration and no lawful COMP-12 | normalize + quote state |
| L-247 | exact Stage/shell conflict that triggered successor | provenance-link |
| L-248 | S1 exact-pixel Stage presentation successor | normalize + quote state |
| L-249 | typeface convergence gate opening | provenance-link |
| L-250 | Source Sans 3 selected as design-reference typeface | normalize + quote state |
| L-251 | conventional platform-icon finalization gate opening | provenance-link |
| L-252-L-253 | system-backed icon mapping and static-coverage authority hold | normalize + quote state |
| L-255 | native handoff opened under Q-PROD-01 with explicit limits | normalize + quote state |
| L-262-L-263 | native architecture acceptance/corrections and APPUI-QDESIGN20-R2 presentation return | normalize + quote state |
| L-264-L-270 | Alpha foundation, Stage grammar, disclosure, state, anchor, responsive law and conformance matrix | normalize + quote state |

Selected entry count: **34** (`L-203`, `L-226`-`L-228`, `L-233`, `L-235`-`L-253`, `L-255`, `L-262`-`L-270`).

## Ambiguities and Drive classification

- Home A/B: **`UNRESOLVED_APP_DESIGN_DECISION`**. Both exact H alternatives remain equal evidence; neither is selected or transferred as authority.
- FIRSTUSE: **`EVIDENCE_PENDING_ADOPTION`**. Only the exact F carrier and interaction/accessibility closeout accompany the status; no schema or authority is promoted.
- Drive Alpha `1ZaxYARCLFFi33psHy3GkBEhyyqhUX2tr`: duplicate app-design reference corresponding to A06/A13; repository authority controls.
- Drive Component System `14IIvJEZApq9GWr0cqJd4cmiu8eraUJfI` and Foundation `1CWMy8-bMudWYBsS8RgtyBBiPsweKNzTu`: duplicate references with a naming/precedence conflict corresponding to A03 and COMP-01..11; non-authoritative until exact asset-level reconciliation.
- Drive Lane A `1QwNzNugjH6cmlxTipfXsdY7BF87ama4z` and `18s1Qft5RVs1ThSYeJ5crDHPbSb_t264Z`: conflicting non-authoritative holdings corresponding to Stage carrier/interaction authority and A12; do not select by folder name.
- Shared logo, wordmark, mascot, artwork and source-render masters remain canonical in Drive `Ensemble Project / 03 Visual Identity & Artwork / Kymaean`; repositories consume pinned derivatives/references. No Website-specific Drive datum is included here.

## Relinquishment and retained authority

After Project successfully receives, validates and accepts the frozen set, Website app-current entry points become exact transition pointers or historical sources as listed above. No replacement occurs in this package. Website retains complete authority for `site/`, kymaean.com, hero/doorway, Website-specific motion and responsive behavior, Website copy/presentation, Website accessibility, Website evidence/production validation and the historical PR 147 lifecycle. Historical branches, renders, experiments and superseded candidates remain where they occurred.

## Transfer gates and next task

The source side is **FROZEN FOR TRANSFER - DEPENDENCY COMPLETE** at the aliases above. Authority transfer remains **NOT EXECUTED** and Website remains current app-design authority until destination acceptance plus source-pointer closure. Exact next task: resume `ADMIN-Q05-TRANSFER-01` — in a separately authorized Project worktree, materialize only these 22 classified bundles from the frozen identities, preserve the stated normalization/pointer limits, validate Project receipt, then return for Website relinquishment/pointer closure. No Website-only data may enter that task.

## Exact source identity appendix

Columns are alias, repository-relative path, Git blob SHA-1, byte size and SHA-256 of exact blob bytes. Each alias/path record appears once even when multiple bundles depend on it. The appendix contains no Website-only implementation or evidence path.

| Alias | Path | Blob | Bytes | SHA-256 |
|---|---|---|---:|---|
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_CAUSAL_HISTORY_INSPECTION_INTEGRATION_METHOD_01.json | 6c5de7d7561b486db47e003c9082075670c45db6 | 4599 | a8dbb3fb7728d3955af82bafbe0603ec06f03a4009c638a392bb80b1405fde2d |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_CAUSAL_HISTORY_INSPECTION_INTEGRATION_RESULT_01.json | a9af62b7e6a19b20699df91cf399efee9d569638 | 5685 | 3b9a0769bd01bf77c104ef3117011f6b0b6918d614d46cea86b1a5c1cdd9e15a |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_CHARACTER_BOUNDED_WORKSPACE_INTEGRATION_METHOD_01.json | 50937d9ad8542bcd6529303dc2f84feda35bedb2 | 4675 | a043f1ddf8fa8b22d688a9bbec52ac48e595b96c1a29491765ae2f4c2d125431 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_CHARACTER_BOUNDED_WORKSPACE_INTEGRATION_RESULT_01.json | 7eda4ac6b85db824adf72e8444f24929e2293280 | 5833 | 952a1c3eea63a34a786daad8c8c8bd4d07f2abd76b1194d5960b9dafa3693ed4 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_CONTEXTUAL_DEEP_INSPECTION_INTEGRATION_METHOD_01.json | c8c4544518717f9f4ab7d0c30b843aa2beba12e5 | 4674 | f685aae54f35b9154242eb4dfb0d12b403e6dc4e7bd3ba0e3354b32a08d2eef2 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_CONTEXTUAL_DEEP_INSPECTION_INTEGRATION_RESULT_01.json | cdb4ef212e12329b806bb7c844a81c5b0e003338 | 5883 | 4b33c385ae3f101a598c4bbfbc4a843988ef6344f1aa7f64a07388b1d36ad782 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_EMPTY_UNAVAILABLE_TRANSITIONAL_INTEGRATION_METHOD_01.json | 098dc54b1d0d6f9d3cf7ec5f07ab0f090aa72e1f | 3932 | fa489d77119879889990327bd1fa48f55151bd7a4994bd135af536c9c4873d08 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_EMPTY_UNAVAILABLE_TRANSITIONAL_INTEGRATION_RESULT_01.json | 0eace6700d7f450e67efd1431fe5e5b8c81a6d2f | 6315 | 873b0ae8a7b1160b8d2c580444d651d41ac5c77a7528aa28f6e6a854f57255e0 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_FOUNDATION_METHOD_01.json | f1a7fef60e5dc2ec4db77fad5d94c9f1bda751d4 | 2582 | 15673b3b2ea0d67136560192ba8c47d7de99913172b8f1fa40a6240a0bffe690 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_FOUNDATION_PREFLIGHT_01.json | dc796b48fdf26256282955d5158d4a2c283ea01c | 3850 | 2c967521883b547bd1b7359d6fe7bbeb788716a22c07faf4408a56657750ca34 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_FOUNDATION_RESULT_01.json | 95b073fa4dd3f006e262259abc511872653ce922 | 4112 | 9ba2d80721f280efbb706d1f94a360fd96862c9ab8ec44c0309c9fe2b3361672 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_PERSISTENCE_RECOVERY_INTEGRATION_METHOD_01.json | 779d99f7ba254da4f6779c3fcf80f1b11810c862 | 4977 | 55a65ac1dd9408ec868249c499000a3eabd02502d68675d2a25cc15ea8b2bdc5 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_PERSISTENCE_RECOVERY_INTEGRATION_RESULT_01.json | ad933182290dd244a9f1cd8fe110700294cbe9fc | 6208 | 5a11d8c8a451ec4c50d4239dba2c08de87669c5dff93ea80a8a604c5fe325e9d |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_PRODUCTION_LIFECYCLE_UTILITIES_INTEGRATION_METHOD_01.json | 5b48e929298fa1830116488e456a86c702d69b8e | 5062 | f9a4de4c56ce07cc53eef5afb00847838262796266b4bcad387441343610097b |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_PRODUCTION_LIFECYCLE_UTILITIES_INTEGRATION_RESULT_01.json | 95f449a9d38d4ac445786c583d20f5416b7b7be9 | 6192 | 79a0c9c7a436104ede021195059db5de3bfde93c1191668ce0e3ee32c74db050 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_SHAPING_WORKSPACE_INTEGRATION_METHOD_01.json | 1785d7818c2ac889411c02cfea28a2361eff49e9 | 4214 | f960b353cb0cf8498fa37aeaf302ffd173393e7b91a54bb12314b1380250b5e5 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_SHAPING_WORKSPACE_INTEGRATION_RESULT_01.json | 46768eb0b3fc7e5b4da2e9007010e278df0a435e | 5530 | fed5c5b55ab5f1b4b0fadcf07bc577089ed52c73f9311b626ef73b7116a1fc14 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_SHELL_INTEGRATION_METHOD_01.json | e904364820f1016de2be9cb5072f5762f329abf5 | 4449 | 79441b03dcf68a3b44d6f893c39ddfc045c607259289584a8af8f351cba67284 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_SHELL_INTEGRATION_RESULT_01.json | ba96e677765a07d916f3f25b92d04cdd2fb1d8df | 4149 | 26cac1983c2821eea9b49ec04ba5b70d3935f1203221b8d2e4a3ab2306d0091c |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_TRUTH_KNOWLEDGE_DISCLOSURE_INTEGRATION_METHOD_01.json | 02d93af4a1d0c7991c77c572a8f2146d4da8514e | 4976 | b5d45f26722e5ede1200d29d03bac8671551a6c48e97e27374267310536081e4 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_TRUTH_KNOWLEDGE_DISCLOSURE_INTEGRATION_RESULT_01.json | 57f558757f16c9cfe94e6338eedf5d5f37e6095f | 6137 | 65eee467b9983e55c9ffae63af6b05a1d016fb900021db82cc92e17aff1e7424 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_WHOLE_PRODUCTION_CHARACTER_MANAGEMENT_INTEGRATION_METHOD_01.json | ac967ec2e521e0f59d205c7f9dbe9b2717de5658 | 4662 | c03e7da2ea7357b6033f870fe8b5044dd39ab0f04813f7ab753f464ac3349500 |
| A | docs/evidence/APPUI_01_COMPONENT_SYSTEM_WHOLE_PRODUCTION_CHARACTER_MANAGEMENT_INTEGRATION_RESULT_01.json | af73c0c5fd520b768941b8a0eb1df11cf47f7806 | 5638 | 142c273c6e4ac4e4ea4f6868e1647f8fb85db96c7459353796e3fb1ab052e63f |
| A | docs/evidence/APPUI_01_NATIVE_IMPLEMENTATION_REFERENCE_MAP_01.json | 399ac818818d9fbbab2176f62381e6c67ddb9aae | 6870 | 3793ad4dd03f5a80fcf7b428a07fe8b111b3fffa216ed6c9e5c4a834af8967fe |
| A | docs/evidence/APPUI_01_PHASE_3_STATIC_APP_VISUAL_SYSTEM_REFERENCE_01.json | 559bf916061cce2b8007788c3f1dfaaf7d2c1126 | 4101 | 5c31c67b9a9057f07bb78f827d2ed38a8004cf3b801d1950d38005b9aa12029b |
| A | docs/evidence/APPUI_01_Q_DESIGN_20_POST_COMPOSITION_RECONCILIATION_01.json | b916de21add987b76393333fd74505050fdcf11a | 5493 | 57f12eadf3d62983b7a3d6fc803a2ac5959142202fb5de34ec53510ed6e6f10d |
| A | docs/evidence/APPUI_01_STAGE_PRESENTATION_SUCCESSOR_METHOD_01.json | aa9b9fc575d5c9d1dd0412c76039b0f51c863be1 | 5401 | ce6d074c3b8df82e7f59d820ab77a3823d1ab76af026977ac8cd4eedb9b7c712 |
| A | docs/evidence/APPUI_01_STAGE_PRESENTATION_SUCCESSOR_RESULT_01.json | 771d12b2079ea9754136841883a04a291f97773a | 5699 | 3eb970302606e5a2a46d78f5d7c28d6ecc96fd01020c3c63f0e1bf8407e70940 |
| A | docs/evidence/APPUI_ALPHA_CHARACTER_ANCHOR_COMPONENT_ANATOMY_01.json | 89618e49557fde46dab598858b33297e1b9e3225 | 5514 | 89091554c1c5af901dd5a15fba46b65aa05f34e0debf53d579ded683b3ee1864 |
| A | docs/evidence/APPUI_ALPHA_FOUNDATIONAL_UI_STAGE_CONSTITUTION_01.json | 80eeffb2a614609fb5092bafe1ba87d6fbe859b3 | 3772 | e6044877bca16bc36a60af815fb1e13e2261ce5be1c2bc623e688666e2a0e028 |
| A | docs/evidence/APPUI_ALPHA_STAGE_ENSEMBLE_RESPONSIVE_COMPOSITION_LAW_01.json | d9025278ac4fc218a9c4811652fd3dfbdf32bb12 | 6952 | 2a512884ffa95ebdbd6a4afe2badebbe966084015fb8163e59c6c98c578b0873 |
| A | docs/evidence/APPUI_ALPHA_STAGE_INFORMATION_DISCLOSURE_ARCHITECTURE_01.json | 3c3a98cf2c616f725dcdbf6b6874d3ae510bffdc | 5883 | 061b5646acacf7ce8cf7cf0e14e3ca023195b108071828fe7db7dcbc109d84a3 |
| A | docs/evidence/APPUI_ALPHA_STAGE_INTERACTION_SPATIAL_GRAMMAR_01.json | 60bd23f93f1dec907cdc7da446ee74d3dfdccaeb | 5233 | 9e5f8435628555bdb3189e9064c2772971ab2411bd42f9addf68902a94d42cc0 |
| A | docs/evidence/APPUI_ALPHA_STAGE_STATE_WITNESS_REDUNDANCY_GRAMMAR_01.json | 7abc319c94d557391477ab260f5aba51efeeb3f3 | 5798 | 13ea3f55b738dab2741a5144596e4eb41a9d659b02ea208efd2efd79911d04b6 |
| A | docs/evidence/APPUI_ALPHA_STATIC_CONFORMANCE_MATRIX_01.json | 681a5e287ad19be7767751787993a69cb9eae15d | 7131 | e257c8f5df2b8286a0c94a59222f7c53f7a32b804ef5da9e689baa4ef9b8236e |
| A | docs/evidence/DESIGN_LEDGER.md | be4c9ffcecb8366694836b691b3916f4033b1f9f | 525695 | 1d281e3134332c39d04307853db366ef950106e0e6a1aa7311fdc27098b46682 |
| A | docs/evidence/DESIGN_PACKET_AND_SYNTHESIS_FRAMEWORK_01.json | 703da33424bfc243c6234cdfc7bbfbf56553a2ed | 10144 | b30dd7b6af16d664e370ef4f5a456cdd527a869689497183010ed632bcdcfc3f |
| A | docs/evidence/DESIGN_PACKET_REGISTRY_01.json | 2c2639a8ae48bf24ac685dd900e8554485bcf0e7 | 37409 | 103e3f666109636a47083f8569631f0c26d25d95eedeb8ca52898894bfab147b |
| A | docs/evidence/MOT_01_CONTEXT_SHIFT_CS2_ADJUDICATION_01.json | 747ddfe557f1dd371f832fd68b30269d1d2d723b | 3377 | cd28c903190a77cd1f19c05987ea2eb3df5590f775b9be5fb95b21573d0d4167 |
| A | docs/evidence/MOT_01_CONTEXT_SHIFT_DIFFERENTIATION_CONTRACT_01.json | e6873e599da4a7f34f7679ae7d0f09152652cbec | 5963 | 6038c4bc29fc90cb7a66a1262608f9d88643f7528932a4506a2d0e68e7f07e32 |
| A | docs/evidence/MOT_01_CS2_DEPLOYMENT_ENVELOPE_CONTRACT_01.json | 5fba62675651515263243217b6202cfe8f208f08 | 10478 | 8d53f13e25538aa63f52049b5990f4ef5cc169eb7f3b92b9f6daf99446e3005a |
| A | docs/evidence/MOT_01_CS2_DEPLOYMENT_ENVELOPE_DESIGN_SOL_VIEW_01.json | 73cea8b86d6988e006eeccabb276eac38c0f4b15 | 3275 | 15b1cd7cbe5e8b792d95d0c3cf8beabe14320282b6b4372115337ef2b1c6e305 |
| A | docs/evidence/MOT_01_CS2_DEPLOYMENT_ENVELOPE_DIRECTOR_DELEGATED_ADJUDICATION_01.json | 5f0c9789f24576a78a3daca37b522f5d64d914d4 | 3566 | 8e948909f34e38ac9771eee8148171545edda3aef93ce6a38e73f76e4d648d68 |
| A | docs/evidence/MOT_01_CS2_DEPLOYMENT_ENVELOPE_EXEMPLAR_PREFLIGHT_01.json | e5d41e17d6cd4b038962fd8eb753b21616e07efb | 3471 | be0edacd8cc178b2a941363bb091d849d7113954628788125de1b31d9ed80c7d |
| A | docs/evidence/MOT_01_F1_CADENCE_ADJUDICATION_01.json | 466142566c73f3c95b06d61086e0708ad0613734 | 4275 | c5c4149d37c7812330567fad676f6e36e4617fe4a52369109281f4f0741f14bc |
| A | docs/evidence/MOT_01_F1A_DEPLOYMENT_ENVELOPE_ADJUDICATION_01.json | cb3fce6557829ef34c88ce50daf8d0dc1281ee44 | 3445 | 53c39fda0119412bcde5cb9a10125a0af8540721a3d2e7334a948e5853463ac5 |
| A | docs/evidence/MOT_01_F1A_DEPLOYMENT_ENVELOPE_CONTRACT_01.json | 4ac041e9c270ef11cd0cfc14648abc8a7a972996 | 10599 | a73f1de1ecf96c808835e0212652847cd1dcd6d3fb87dbddb4d5d3d18e643fb3 |
| A | docs/evidence/MOT_01_F1A_DEPLOYMENT_ENVELOPE_EXEMPLAR_PREFLIGHT_01.json | 5125207fa526d178f109c74b6bf2ffd5ec1fee0f | 6097 | b61438e9fcc7a961d8666d552f4cf9cdcd35bd62390fcda6c121e7fbfe70b402 |
| A | docs/evidence/packets/PKT_APP_SYN_01_WHOLE_APP_SYNTHESIS_01.json | d764713b927d0ce8ae9b6586cd030726c690c41f | 11531 | 7ffef03bdec0dda58f5857508e8f1376d03980cb5b486eaa58f23c0a3ea956e1 |
| A | docs/evidence/packets/PKT_APPUI_NATIVE_HANDOFF_01.json | 81f78173a7066e843d6de6b64516eaa501827269 | 3886 | c3cf942fea6b835261e68cd9e3774316d0aa7b69198ab5b280bf9e8472d5896d |
| A | docs/evidence/packets/PKT_APPUI_STAGE_PRESENTATION_01.json | 7bd978e2e0cb4a5d66b5a2226e121206f70172ae | 5383 | e318d14007a5c2cbeb527113963eee8cd83285d0f5582595d4c01db58c6f773a |
| A | docs/evidence/packets/PKT_MOT_CS2_CONTEXT_SHIFT_01.json | cf395c21cf1639e05ca3e6618bcc2645ef89c5f1 | 4918 | 4a29b39e2c5b0c46d738105d0b0fd5b1849ee766b5ee3863e5c3c4adcdf00bbb |
| A | docs/evidence/packets/PKT_MOT_F1A_WITHIN_CONTEXT_SUCCESSION_01.json | 1db41d54f72c6d42c120eb86b49e733314107051 | 4324 | 29faa99a469115eed19dd124d1c6f6b1961bfca14c968c3c833755738f81dfe1 |
| A | docs/evidence/packets/PKT_STAGE_CORE_02.json | adf234bf42b4e24622288c12b1d95f90d30b04be | 3394 | 2318109789f24021258f50135d7535818b3ee0295292654897dabef6b595d625 |
| A | docs/KYMAEAN_APPUI_COMPONENT_SYSTEM_FOUNDATION_01.md | 8f649dcff5a7b39418460d543adfcf5beb443109 | 7089 | 69adf45d09365d20ca68218fdd8e3f9d7add81bbca6e5f411cc24ae44042014e |
| A | docs/KYMAEAN_APPUI_NATIVE_IMPLEMENTATION_HANDOFF_01.md | cfff9742acc8868569a3726fad6b787ea597fe75 | 7430 | 4bfcd871567a01f61caba646aedfa83e1fb7adf4d702523d77578ed1eed34d89 |
| A | docs/KYMAEAN_APPUI_PHASE_1_STAGE_INTERFACE_ENVELOPE_AND_LAYOUT_MAP_01.md | 3baf8cc94baf9df0f1838dd1e81cbd4ec0cd33fd | 19975 | 6df606fe19510ad49b7b95c5e021899964035839091c78ff8a733989396dfaae |
| A | docs/KYMAEAN_APPUI_PHASE_3_STATIC_APP_VISUAL_SYSTEM_01.md | fac4033eabfe744e010f6fe418fcec286da6064b | 11194 | b0c5ad0e6ed2b5ab5c02a68728fad4483d41c1787465dcbb8039cc177034b31e |
| A | docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md | af5a79fe071059599587e094e4b54fd42365c15f | 18205 | e9b4d7c352588f42b01762991adf495d13656ede310e0b2f95a66ff53e03b9f2 |
| A | prototypes/appui-01/component-system-causal-history-inspection-integration-01.html | 98e20085f2614f990fedb59c61bb6df4a921f312 | 25320 | 702ae52c5de128328e1d1acc86c1d7600440d1c1771043c929cda01014c862de |
| A | prototypes/appui-01/component-system-character-bounded-workspace-integration-01.html | 9045e4cb8533ac2a35d97d9c98c85e96abc55d18 | 27446 | f109095957b45e0c8c3252672a24b4cd9e6b1005da210021c7affefb3116a18c |
| A | prototypes/appui-01/component-system-contextual-deep-inspection-integration-01.html | 3748727de2cecdff9e9786183e3a39224601bafe | 23303 | 3b6596fc04bd8d5e142ce339cc42c7710459d84115d775218f37c7395bbf7792 |
| A | prototypes/appui-01/component-system-empty-unavailable-transitional-integration-01.html | d1c5df82dc6448bd758aac545ba72c8ca71ca89b | 30069 | 238424002c5d1e527a9d8c3b40f0df70c9e92f243ff6978495a7fa75581405ba |
| A | prototypes/appui-01/component-system-foundation-01.html | cff6b84042208f8c8e7b7633cc5b392ab0cb5a1a | 19029 | ee2d3aebc79ee4af94a8295c43cf8b1b3bf3b82818fcd776b3c6e661d904cf50 |
| A | prototypes/appui-01/component-system-persistence-recovery-integration-01.html | e71b37540defeee4a33dd46b264ac70c9fcccb61 | 26961 | 085e37b7abe955348d842055d253f216973264fa56380f15e6b8d02ad9dfe54d |
| A | prototypes/appui-01/component-system-production-lifecycle-utilities-integration-01.html | 608b2a362994da05c22572bb70cef082a850718b | 27378 | e8e203062e9be8a3f8265fa52430a129489536237931ce1577b6d64ea8e6f50b |
| A | prototypes/appui-01/component-system-shaping-workspace-integration-01.html | 98f408e905f629875744cc6e6967a5e0c311b4cf | 19041 | d65329d90ea968c7336d2b80610a9893192cf3727a70ad6584644d574e53bdaf |
| A | prototypes/appui-01/component-system-shell-integration-01.html | 73a084d4f4ac95f5250a24163a2dafb11ea3b511 | 22247 | 57ef7392d61d56cd19c7369a2e27ca758d8cee25007e3f914dfe10ea2d7c4b3b |
| A | prototypes/appui-01/component-system-truth-knowledge-disclosure-integration-01.html | c19b0cf0343367187e18bdfcb5b720a016fe5efc | 29390 | b9481b1457d7cb8452fd640996b1580173da9e40c75082f86854d1217500a60e |
| A | prototypes/appui-01/component-system-whole-production-character-management-integration-01.html | 8b1b3fc01d55e0d0fa08ce91df72608566851be0 | 27046 | df249cb9f9b7a65582cbf6aee2ec40b033a5ab3ba67c113be1ff0a4219a288d3 |
| A | prototypes/appui-01/real-assembly-exact-stage-shell-adjacency-01.template.html | 7f713ed2b3fe96d2b0a25d3694e97bb7937de037 | 13044 | 142468172dd7206c53a81e206f006322ba0650c4a87180be732cc4e88b355ad2 |
| A | prototypes/appui-01/stage-presentation-successor-01.template.html | fe546a85d62117e74f24f693a3830dce68da3dd1 | 13176 | 9c2a6f5a70a0f01af3bc0337a9df68126df33697518619f2e42121017ee6076d |
| A | tools/appui_component_system_causal_history_inspection_matrix_probe.mjs | a41cd83aa6409e5ed13feaa4c85cc2e7da7f3cc9 | 9627 | 659581a4ddfeb9b29d0a04ae26558ba44011f8c492b990a0d2ef5ca0d2123f3c |
| A | tools/appui_component_system_character_bounded_workspace_matrix_probe.mjs | 87ebd902b41c871746f7967810fe17597490479f | 10186 | ee10ac2c2b0ec194ee5b3a4174bc307e7aaa22189d295585cb2a1f86f817c793 |
| A | tools/appui_component_system_contextual_deep_inspection_matrix_probe.mjs | 68b4260b03ad520854da062792ce47031a5c6c57 | 8117 | 8f3488bc1be3d2ddcc4a3fec8bbe1b723ca3698bdf5f29b55178e36408937c3d |
| A | tools/appui_component_system_empty_unavailable_transitional_matrix_probe.mjs | 04bc55cf2c3ada564021675e2da83445864d66ed | 11026 | fd5c1a03201d2b79187a38dc45c330bc38258810ca52ee78071caaf1352aa457 |
| A | tools/appui_component_system_foundation_matrix_probe.mjs | 378a27dd956136835e223e6b162e3c5fde12b184 | 6377 | fbddff6e3a4b38fc1b2121633418ff65f136430ad5b4afd01ccf0c0bf7013703 |
| A | tools/appui_component_system_persistence_recovery_matrix_probe.mjs | fb2a7b2a4e6e4f38c8a5865dedb84ff706e8fc53 | 10103 | b0ba234ccafd046febe063ad827cea1554a329c35f9395bf21446aeda158c9fc |
| A | tools/appui_component_system_production_lifecycle_utilities_matrix_probe.mjs | ead8b0fc491f9c1e81a10115e0263eff2be6f1dd | 10687 | 97a18899e13dfac30be65d3329aeb180f0bab9dd3ee82fc3f8b77e6f05a56636 |
| A | tools/appui_component_system_shaping_workspace_matrix_probe.mjs | 57d957708dd2af40bc4c583858b2b23688dc0369 | 6850 | b271c64550b0c6f9f08b2c32b587cddc82329f81f13f0b368e50dad618f2adb9 |
| A | tools/appui_component_system_shell_integration_matrix_probe.mjs | e67d6bd76295d3a8fead3f4e87d7ac4390ce9c15 | 7102 | 978b029f012aa7d549943f11641deb5be01a7b6bc7c87639aa739a2442417fb6 |
| A | tools/appui_component_system_truth_knowledge_disclosure_matrix_probe.mjs | 76918ae0ef0e56d00445bfedd167730fc1a35e09 | 10165 | c9ac876b12d76d58137b8587a389f70909b1f85e9c64058e053cd5144a95628c |
| A | tools/appui_component_system_whole_production_character_management_matrix_probe.mjs | f364feeb260ee058516f87b0d837b81964b92c8a | 9010 | 73a10eb817ade5065767aa84a3e1fe0b3d8e301a77c65aeef2f499165edb10e8 |
| A | tools/appui_real_assembly_stage_shell_matrix_probe.mjs | 375ed9bf20fed16e9ba27401e49de25d3448432f | 6319 | f7da5926e177b752cc906ade03043126bdd72b68094861844e3ff46763218c96 |
| A | tools/appui_stage_presentation_successor_matrix_probe.mjs | 132090fab66212793fbd77ee16d8a49871f1a730 | 6506 | 5af6ec854f21bc2a360de822acfe56af96a601fe75a198537298fbdfe67e91cf |
| A | tools/materialize_appui_real_assembly_stage_shell.py | 5e0d077e59c53a1d75f1f8cdf01d1bc9b0ee2b17 | 1630 | 66201cacc78871fadf3918b77b4854526bf5797accd3399d9c8658a991abfec2 |
| A | tools/materialize_appui_stage_presentation_successor.py | c4c242c81aa9083f553efa9a81a548004343f77a | 3494 | 96acb4b42869b4394de8da1b1fa7e857df4dc3453759e8824506a5beeb7ce9b1 |
| F | docs/evidence/APPUI_FIRSTUSE_01_INTERACTION_ACCESSIBILITY_CLOSEOUT_02_2026_09_17.json | d0c54939e2350557b075787e2b3402289e485935 | 3349 | 64a316c853256b190f27cf43fa94f814e3b914ce0d56b95cb822cdf150923ca1 |
| F | prototypes/appui-01/first-use-entry-experience-02.html | fa52681ccc8e8b28bd9e126b3b9cace9119ba854 | 15327 | ad5784dc283b1fa01fb35305f23325fd03b1cd4636a7d47b76d934767d5ae56f |
| H | docs/evidence/APPUI_01_HOME_REENTRY_TWO_OPTION_REVIEW_SET_01.json | d6a57a098c55686338163d71464d17730d079104 | 2031 | 2187998f969771c0ecff153271bbdeb32bc46fd86499b54f11f40809e6360046 |
| H | docs/evidence/APPUI_01_HOME_SCENE_HORIZON_STUDY_01.json | fa575d4330fc05a62689e13f53eb361228c84f6c | 3018 | eb4c2522dd4f44192dd30090d6751d8c47425948a8d6f3d1fd9d2e4a5f695ac1 |
| H | docs/evidence/APPUI_01_HOME_THRESHOLD_REENTRY_STUDY_01.json | 0d9a424d3dc6dcab2532f195c72ea9816d5a24bc | 8423 | e2aca64cc289b08a65bef6b6852615838acdb3badc57225d8b816bce83d28b79 |
| H | prototypes/appui-01/home-scene-horizon-study-01.html | 293a9ebf790bcf6ee549f3665a0791e9226de6a9 | 14304 | 8ec602d61d7c87644c89d2da02d6ab2f3626487a67beefa4c5e065a504312718 |
| H | prototypes/appui-01/home-threshold-reentry-study-01.html | 46c23ea21958329049f607ef454cf0a9cf945208 | 15111 | 2b19eb20781be9a1d5b4c3bfc2f7a1ed06efe9d5829fc5fdf5a3564e3bbe3073 |
| H | prototypes/appui-01/home-two-option-review-board-01.html | 747019563e79b3f60ab769ff9a1ffd38d3e74922 | 6050 | 5ead98cfadda13193c4ac81dbcd1f225ebd2e60d49ba77fa58c9d17671828987 |
| W | AGENTS.md | 1067031d29e500a086adc56af1a0a069e4283136 | 20728 | 86685ce05ca44f90c58d5d8ddd8c53e70c3a1d970c278cdec95a24025acd62a9 |
| W | docs/DESIGN_CONTINUITY.md | a99b00a2afd09686ff625076ae615ffd82fe0d73 | 37177 | a9ea2787d1d14ccbfa823271bf42f583aa7f5b1c956ee4c412c3ab4c83f88b74 |
| W | docs/KYMAEAN_ENGINEERING_INFORMED_VISUAL_TRANSLATION_PROTOCOL_01.md | a00fdfb1de355ac2c4d0fe3fd73a8990da10e8ee | 7045 | 1fc0dca8bb41ee12f4966c76d9ecedb50be6f4d784e8f4fa3305cfb5713efd96 |
| W | docs/KYMAEAN_EXPERIENCE_ONTOLOGY_SYNTHESIS_01.md | be875e273109d235d4a6a8219521fe7f291da5a9 | 20054 | b5b4244fe645cb20bbc4d15daf5251add3c0c575ad885bfdc66386f3e00fd68b |
| W | docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md | af5a79fe071059599587e094e4b54fd42365c15f | 18205 | e9b4d7c352588f42b01762991adf495d13656ede310e0b2f95a66ff53e03b9f2 |
