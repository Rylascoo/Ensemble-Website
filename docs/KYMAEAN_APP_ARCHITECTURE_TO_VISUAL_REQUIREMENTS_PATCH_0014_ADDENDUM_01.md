<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN APP ARCHITECTURE -> VISUAL REQUIREMENTS — PATCH 0014 ADDENDUM 01

Status: DIRECTOR PROPOSAL FOR REVIEW / ARCHITECTURE-ALIGNMENT ADDENDUM / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Purpose: extend `docs/KYMAEAN_APP_ARCHITECTURE_TO_VISUAL_REQUIREMENTS_CROSSWALK_01.md` with the visually material consequences of completed H1 Patch 0014 — E0 Production Context Continuity.

Current app authority:

- `Rylascoo/Ensemble-Project` main `7475a9397cff9063673908c666a729f0f3cd4525`;
- Patch 0014 Proposal `0.10` frozen and implemented for exercised scope;
- exact full Core-test authority `4ac0250005c8d88c3b815c5d53cfca0a982e454c` with `538/538` PASS;
- exact native Harness/fixture authority `84b3e23db55910f746670cd2e06a67b8a5dea2b3`;
- no evidence of Windows AI/NPU execution, WinUI implementation, MSIX/WACK success, or Store certification.

## 1. Production-bound context is now explicit authority

Patch 0014 closes:

```text
current ProductionState
-> Character Access
-> Character Context
```

through deterministic Production-bound composition.

Visual consequence:

> A Character-facing surface must be understood as a projection of an exact current Production state, not as a free-form AI summary of the Scene.

The UI may organize or phrase legitimate information, but it must not manufacture new Character knowledge merely to make the screen feel complete.

## 2. Observation is not implied by social geometry

Patch 0014 explicitly does **not** infer observation from:

- co-presence;
- Candidate visible text;
- addressed Characters;
- nomination;
- Director selection;
- relationships;
- SceneState;
- causal adjacency.

Visual law:

```text
present together != observed everything
looking toward != knows
salient != informed
related != aware
```

This is especially important for the relational Stage: composition may communicate relation and salience, but cannot silently become epistemic authority.

## 3. Character-owned subjective material remains bounded

Production-backed Access preserves:

- shared/public SceneState and Pressure where permitted;
- Character-owned Constitution, Disposition, Circumstance, Observation, Knowledge, Belief, Suspicion, Memory, Goal, and Relationship material only for the owning subject;
- denial of other-owned Character material;
- denial of Production HistoricalTruth, UnresolvedProposition, and WorldState;
- deferred CharacterClaim disclosure.

Visual consequence:

Character-bounded surfaces remain primarily subtractive. Other Characters' subjective state should not appear as omniscient summaries, disabled cards, inferred motive labels, or relationship-psychology prose.

## 4. CharacterClaim and recall remain deliberately unresolved

Patch 0014 denies active `CharacterClaim` for every Character under `CharacterClaimDisclosureDeferred` and explicitly does not infer current recall merely because a CharacterClaim exists.

Visual consequence:

Do not invent a creator-facing `remembers / knows / believes this claim` treatment from current Patch 0014 state.

Any future CharacterClaim disclosure or recall visualization requires later product authority.

## 5. Recent Performance remains outside current Context v2

Patch 0014 keeps canonical `recentPerformances = []` and `RecentPerformanceText` empty.

Visual consequence:

The transcript/recent-Performance panels used in current design renders remain **design hypotheses**, not Patch 0014-derived Character Context authority.

Do not cite Patch 0014 as proof that recent Performance belongs in the bounded Character context surface.

## 6. Source state identity is not Character-facing content

Patch 0014 binds Production Context to exact `SourceStateHash`, but `SourceStateHash` never enters Character-facing rendered text.

Visual consequence:

Do not expose state hashes, ContextPacket IDs, composition contracts, provenance hashes, or similar deterministic proof machinery merely because they exist in Core authority.

These are engineering/provenance mechanisms, not fictional knowledge.

## 7. Visual requirements added to the base crosswalk

Any current Character/Stage experiment must additionally preserve:

1. relational composition without epistemic inference;
2. co-presence without automatic observation;
3. Current Opportunity without implied knowledge or intent;
4. Character identity without implying subjective state from visual appearance;
5. bounded context sourced from authoritative permitted information only;
6. no CharacterClaim/recall UI treated as current authority;
7. recent Performance UI treated as open design, not Patch 0014 contract;
8. engineering source-proof metadata kept outside Character-facing fiction.

## 8. Representation implication

Patch 0014 therefore strengthens `Character != Portrait`:

> A Character representation may show **who this is** and **where/how they participate in the current relational field**, but the representation itself may not be used as evidence of what the Character knows, observed, believes, remembers, wants, or intends.

This requirement applies regardless of whether the future representation is photographic, illustrated, abstract, user-referenced, generated, or text-only.

## 9. Scope boundary

This addendum does not authorize:

- CharacterClaim disclosure;
- Observation generation/eligibility;
- recent-Performance Context population;
- World Resolver or spatial-hearing semantics;
- final Character Context UI;
- final portrait/image workflow;
- provider/model execution;
- WinUI implementation;
- Windows AI Foundry/NPU integration;
- packaging/WACK/Store work.

## 10. Audit result

Audit order:

`Patch 0014 current authority -> Access laws -> Context laws -> privacy/disclosure -> relational-design interaction -> Character representation -> recent Performance -> provenance metadata -> scope`

Corrections made:

1. updated app authority from Patch 0013 to Patch 0014;
2. made no-observation-from-co-presence explicit;
3. separated social/relational visual structure from epistemic authority;
4. prevented current CharacterClaim/recall behavior from being invented;
5. marked recent Performance UI as open design despite render use;
6. kept deterministic source proof out of fictional UI;
7. preserved all Patch 0014 deferred non-scope.

Final pass:

> **PASS — no remaining material Patch 0014 visual-authority omission or scope overreach.**