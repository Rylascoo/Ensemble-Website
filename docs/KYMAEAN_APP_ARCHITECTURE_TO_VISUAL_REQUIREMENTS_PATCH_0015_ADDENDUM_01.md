# KYMAEAN APP ARCHITECTURE -> VISUAL REQUIREMENTS — PATCH 0015 ADDENDUM 01

Status: ARCHITECTURE-ALIGNMENT ADDENDUM / CURRENT PRODUCT-TRUTH RECONCILIATION / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Date: 2026-09-04

Purpose: extend the base app-to-visual crosswalk and Patch 0014 addendum with visually material consequences of completed H1 Patch 0015 — E0 Accepted Performance History + Context Continuity.

## 0. Current app authority

`Rylascoo/Ensemble-Project` current `main` at reconciliation:

`a92199a0a66810d201b4c7834b813b45f4999184`

Latest completed patch:

`H1 Patch 0015 — E0 Accepted Performance History + Context Continuity`

Architecture:

`FROZEN — Proposal 0.15`

Machine authority recorded by the app repository:

- full Core tests `571/571` PASS at `b890b7eca66c391fae3ec30af0442dcc0e9f6aec`;
- native Harness/Core + fixtures exercised at `5cb055e6dddea721aee98fee7f633191543e6490`;
- Patch 0015 promoted to `main`;
- no current evidence establishes WinUI runtime behavior, Windows AI Foundry/NPU execution/performance, MSIX/WACK success, or Store certification.

## 1. Patch 0014 history limitation is superseded for the Patch 0015 v3 path

Patch 0014 correctly established that canonical Context v2 had `recentPerformances = []` and empty recent-Performance rendering.

Patch 0015 adds a new exact history-aware path rather than rewriting that historical truth:

- historical Context v1 remains exact;
- Production-bound Context v2 remains exact;
- synchronized nonempty accepted Performance history uses Context v3;
- v3 renders an accepted recent-Performance layer.

Therefore the visual rule changes from:

> recent Performance is only a design hypothesis

to:

> **Recent accepted Character-legible Performance is now supported by current product authority on the exact synchronized Patch 0015 v3 path; it remains absent from v1/v2 and must not be generalized beyond that authority.**

## 2. Recent Performance is fictional occurrence, not epistemic promotion

Patch 0015 records accepted Character-legible Performance history, but explicitly does not promote that history into:

- objective truth;
- Observation;
- Knowledge;
- Belief;
- Suspicion;
- Memory;
- CharacterClaim.

Visual consequence:

A Character-facing context surface may represent an authoritatively eligible recent accepted Performance as historical occurrence, but must not style or phrase it as proof that a Character observed, knows, remembers, believes, agrees with, or was affected by that Performance unless separate authority establishes that claim.

Required distinction:

```text
accepted recent Performance occurred
!=
this Character observed it
!=
this Character knows/remembers/believes it
```

## 3. Character-legible history is deliberately narrow

The history projection contains only:

- `SourceCharacterId`;
- exact Character-legible `VisibleText`;
- canonical append order.

It deliberately excludes per-entry engineering/provenance machinery such as CommitId, TakeId, state hashes, ContextPacket IDs, candidate hashes, provider data, State Authority material, and causal-commit internals.

Visual consequence:

> **The UI should render the fictional occurrence, not the machinery that proved it.**

This reinforces the established law:

> **Trust machinery should govern behavior more strongly than it occupies the interface.**

## 4. Exact source Character must remain human-readable

Patch 0015 recent history is sourced by Character identity. Product-facing presentation should resolve the source to the same stable human-readable Character identity system established by CIR rather than expose research aliases or internal IDs as the primary identity surface.

Example semantic form:

```text
Dr. Voss
No.
```

not:

```text
Character C
PERF-...
No.
```

Exact copy and typography remain open.

## 5. Historical occurrence and durable consequence remain separate

Patch 0015 records accepted Character-legible Performance even when the accepted Take produces zero durable mutation or all durable consequences are rejected.

Visual consequence:

> **Something can have happened without having changed durable Production state.**

The UI must not imply:

```text
recorded accepted Performance
=
durable consequence
```

This strengthens the need to distinguish:

- performance occurrence;
- accepted Take semantics;
- durable consequence/effect;
- causal history/state change.

Archive/history surfaces should preserve that distinction rather than flatten every accepted Performance into a state-changing event.

## 6. Append order is history, not a free-form transcript model

Patch 0015 preserves exact current-Scene append order, including identical repeated items and Character recurrence.

This provides authoritative recent Performance history but does not by itself freeze a final transcript UI, chat log, conversational bubbles, chronological pane, summarization layer, or infinite history browser.

Visual consequence:

> **Authority for recent Performance content does not select transcript geometry.**

A future Stage/context/history surface may use this ordered occurrence layer only in ways consistent with information-presence, bounded-context, and Stage-reduction laws.

## 7. Context eligibility remains bounded

Patch 0015 adds only the bounded common recent-Performance eligibility rule defined for current E0 `ensemble.e0.copresent-trio.v1` behavior.

It does not generalize co-presence into complete perception and does not create CharacterObservation.

Therefore the Patch 0014 no-observation-from-social-geometry law remains fully binding.

## 8. No provider-session memory is required

Recent Performance continuity is deterministic product state/history continuity, not provider-session memory.

Visual/website communication consequence:

Kymaean may eventually explain continuity as belonging to the Production rather than as a chat model merely remembering conversation context. Public claims must still track what is actually implemented at launch.

This is a strong conceptual distinction for future website education:

```text
Production continuity
!=
provider conversation memory
```

## 9. Stage/context design consequences

Current design research should now preserve all of the following:

1. recent accepted Performance may be authoritatively available on v3;
2. v1/v2 historical behavior remains exact and does not gain invented history;
3. recent Performance is occurrence, not Knowledge/Observation/Memory/objective truth;
4. source Character identity resolves through the stable human-readable Character identity system;
5. history order may be rendered without forcing chat/transcript visual grammar;
6. accepted occurrence must remain distinguishable from durable consequence;
7. engineering source-proof metadata remains outside default fictional UI;
8. co-presence still does not imply Observation;
9. CharacterClaim disclosure remains outside current authority;
10. the visual system must tolerate both empty and nonempty recent-history conditions without structural collapse.

## 10. Website communication consequence

The public exploratory website may eventually demonstrate that an accepted Performance becomes part of Production continuity and can affect what future contexts contain.

However the website must not overstate this as:

- universal memory;
- perfect perception;
- automatic knowledge acquisition;
- cloud/provider memory;
- complete cross-Scene recollection;
- currently validated Windows AI/NPU behavior.

A truthful educational framing is:

> **Kymaean treats accepted performance as part of the Production's evolving continuity, rather than relying on a model's conversation memory alone.**

Final launch copy must be revalidated against the then-current implementation.

## 11. Scope boundary

This addendum does not authorize or select:

- CharacterObservation generation;
- complete location/hearing/attention/concealment semantics;
- CharacterClaim disclosure;
- Knowledge/Belief/Suspicion/Memory promotion;
- cross-Scene/cross-Production history policy;
- relevance/windowing/summarization/index layers;
- final transcript/history geometry;
- final Stage or Archive UI;
- provider/model execution;
- WinUI implementation;
- Windows AI/NPU behavior;
- packaging/WACK/Store claims.

## 12. Recursive audit

Audit order:

`Patch 0015 CURRENT_STATE -> v1/v2 preservation -> v3 history authority -> occurrence vs epistemic state -> occurrence vs consequence -> source Character identity -> ordered history -> context eligibility -> provenance -> website truth -> scope -> ARM64/quiescence`

Final result:

> **PASS — Patch 0015's visually material authority is reconciled without weakening Patch 0014 epistemic restraint, selecting transcript geometry, or overclaiming implementation/runtime capability.**
