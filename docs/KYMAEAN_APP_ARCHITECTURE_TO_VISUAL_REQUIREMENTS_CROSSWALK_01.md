<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN APP ARCHITECTURE -> VISUAL REQUIREMENTS CROSSWALK 01

Status: DIRECTOR PROPOSAL FOR REVIEW / ARCHITECTURE-ALIGNMENT CHECKPOINT / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Phase: Kymaean App + Website Design Synthesis — visual work grounded against current `Rylascoo/Ensemble-Project` authority

Current application authority read for this crosswalk:

- `Rylascoo/Ensemble-Project/CURRENT_STATE.md`
- app `main` resolved at `e06668a2307433bf99b0501dc38a701db392c633`
- latest completed patch: **H1 Patch 0013 — E0 Effective Opportunity Authority**
- frozen/approved architecture used where visually material:
  - `docs/blueprint/H1_PATCH_0004_DETERMINISTIC_ACCESS_CONTROL.md`
  - `docs/blueprint/H1_PATCH_0005_DETERMINISTIC_CONTEXT_COMPOSER.md`
  - `docs/blueprint/H1_PATCH_0006_PERFORMER_CANDIDATE_CONTRACT.md`
  - `docs/blueprint/H1_PATCH_0007_DIRECTOR_OPPORTUNITY_CONTRACT.md`
  - `docs/blueprint/H1_PATCH_0011_TAKE_SEMANTICS.md`
  - `docs/blueprint/H1_PATCH_0012_ATOMIC_CAUSAL_COMMIT.md`
  - `docs/blueprint/H1_PATCH_0013_EFFECTIVE_OPPORTUNITY_AUTHORITY.md`
  - `docs/blueprint/CREATOR_ONTOLOGY_EXTENSIBILITY_GUARD.md`

This document does not redesign those contracts. It translates their durable semantic requirements into design constraints and falsification questions for future Kymaean app/website visual work.

---

## 1. Crosswalk thesis

The current architecture does **not** require one final Stage layout, portrait medium, typography system, navigation control, or visual style.

It does require the future visual system to make several distinctions truthful and usable:

```text
persistent Character identity
        != Performer identity
        != portrait identity

who is present
        != who is currently salient
        != who is obliged to act

what a Character may know
        != what the Production knows

candidate Performance
        != Accepted Take
        != effective causal history

historical cause
        -> changed current projection
        -> next effective opportunity
```

The visual-design task is therefore not simply "design a Stage screen."

It is:

> **Make one persistent creative reality legible while identity, disclosure, agency, causal authority, consequence, and attention change without collapsing into conventional chat, graph, dashboard, or game-turn metaphors.**

---

## 2. Authority classification

### HARD / VALIDATED OR APPROVED SEMANTIC AUTHORITY

Visual work must preserve:

- Character-bounded information authority;
- Access Control before relevance/context selection;
- Character != Performer;
- Performance may include speech, action, silence, refusal, redirection, or other Character-legible expression;
- Director manages attention/opportunity, not required outcomes;
- opportunity is not obligation;
- equal dialogue is not the goal;
- Candidate / Integrity / Take / causal-effect lifecycle distinctions;
- Accepted Take != effective history;
- exact Accepted Performance + retained Approved consequences become effective atomically or neither does;
- rejected/alternate/failed/uncommitted material does not become effective Production history;
- current Production projection remains authoritative current state;
- successful causal commit consumes the source Current Opportunity;
- Patch 0013 establishes the next effective opportunity before another Performer boundary;
- technical/provider failure must not become fiction;
- deterministic authority state does not depend on decorative background compute.

### STRONG DIRECTION / OPEN DESIGN GUARD

Visual work should preserve:

- creator-facing dramatic vocabulary remains extensible;
- E0 Knowledge/Belief/Suspicion/Memory/Goal/Pressure/etc. categories do not freeze a closed final UI ontology;
- creator-facing labels may be projections over more general authoritative data.

### OPEN / NOT YET DEFINED BY APP ARCHITECTURE

The current app repo does not freeze:

- final Character portrait/avatar/reference-image system;
- whether users upload Character images;
- AI-assisted Character imagery;
- photoreal, illustrated, abstract, typographic, or no-portrait representation;
- final Stage composition;
- final Studio/Production UI;
- final Archive/history UI;
- final transcript prominence;
- final Take/rehearsal/branch interaction;
- final Character Context disclosure UI;
- final Presentation Perspective switching control;
- final WinUI control composition;
- final motion/material/color/type/icon systems;
- final Scene loop orchestration;
- Windows AI/NPU execution or Store behavior.

Therefore render experiments must not accidentally freeze these open surfaces.

---

## 3. Persistent Character identity -> visual requirement

### Architecture source

Patch 0006 preserves:

> **Character != Performer.**

A Performer portrays a Character from bounded context but owns neither truth nor persistence.

### Visual requirement

A persistent Character must remain identifiable when:

- Performer/model changes;
- Presentation Perspective changes;
- creator posture changes;
- current/historical orientation changes;
- portrait treatment changes;
- the Character becomes salient or peripheral;
- the Production state changes around them.

### Design law

> **Character != Portrait.**

A portrait, uploaded reference image, generated illustration, name, silhouette, voice, typography treatment, or other representation may participate in identity, but no single representation is the Character's authority.

### Current implication

User-supplied Character imagery is a plausible future authoring path but is **not currently frozen by application architecture**.

### Failure to avoid

- provider/model badge becoming primary identity;
- one mandatory headshot system;
- identity changing when visual medium changes;
- generic avatar token replacing Character specificity.

---

## 4. Character-bounded access -> disclosure visual requirement

### Architecture source

Patch 0004 derives a Character-safe projection before later Context composition.

A Character may receive shared Scene/roster information and permitted Character-owned subjective state while Production-only truth and other Characters' private state are excluded.

### Visual requirement

Character-bounded surfaces must behave primarily through **subtraction**:

```text
not permitted
    -> absent from Character-facing experience
```

rather than:

```text
not permitted
    -> visible but blurred / locked / ghosted / summarized
```

unless a future product contract explicitly establishes awareness of the hidden item's existence.

### Failure to avoid

- omniscient Character dashboards;
- other Characters' private psychology exposed as summaries;
- locked cards that reveal hidden categories or existence;
- provenance/source IDs leaking through Character UI;
- creator-only truth remaining visible merely because the human creator owns the Production.

---

## 5. Context Composer -> information hierarchy requirement

### Architecture source

Patch 0005 keeps permitted context categories semantically distinct and separates identity/current situation/knowledge/belief/memory/presence/relationships/goals/pressure/recent Performance/current opportunity.

### Visual requirement

The UI must be able to present different kinds of evidence without flattening them into one undifferentiated text feed.

Useful creator-facing projection may distinguish concepts such as:

```text
observed
heard / received
known / established and available
believed / suspected where legitimately modeled
remembered
current pressure / circumstance
relationship context
recent Performance
current opportunity
```

but final labels and grouping remain open.

### Ontology guard

The visual surface must not turn those categories into a mandatory permanent schema for all creative meaning.

### Failure to avoid

- Character dossier as universal database form;
- one card per engine category;
- every creator-defined dramatic idea requiring a new top-level UI type;
- renderer-generated psychology presented as authority.

---

## 6. Performance grammar -> Stage visual requirement

### Architecture source

Patch 0006 says Performance may be speech, action, silence, refusal, redirection, or another Character-legible response.

Its E0 `VisibleText` representation explicitly does **not** freeze the final product as text-only or message-centric; future representation may be richer, structured, spatial, or multimodal.

### Visual requirement

The live Stage-like experience must not require a chat transcript to be the primary visual object.

The visual system should support:

- people first;
- current relational configuration;
- nonverbal action;
- silence/refusal without appearing broken;
- current action without forcing it into a message bubble;
- transcript/language as supporting evidence where useful.

### Failure to avoid

- chat-thread-first Stage;
- every Performance becoming a speech bubble;
- silence looking like missing output;
- text length determining Character importance.

---

## 7. Director Opportunity -> salience visual requirement

### Architecture source

Patch 0007 defines the Director's central question as:

> **Whose agency becomes salient next, and why?**

Director manages attention/opportunity only. Equal dialogue is not the goal. Opportunity is not obligation. A selected Character may act, speak, evade, redirect, refuse, or remain silent.

Blueprint-level product scope permits one Character or a very small salient subset; E0's single `SelectedCharacterId` is a narrower execution constraint, not final product law.

### Visual requirement

The interface must distinguish:

```text
PRESENT IN SCENE
        !=
CURRENTLY SALIENT / HAS OPPORTUNITY
        !=
MUST RESPOND
```

Salience may affect composition, focus, available context, or command emphasis but cannot read as a turn queue or forced actor selection.

### Failure to avoid

- "your turn" game semantics by default;
- round-robin equal-turn visualization;
- one permanent highlighted-character layout that cannot support a small salient subset;
- glow/selection ring implying narrative obligation;
- opportunity indicator presented as truth/relationship score.

---

## 8. Candidate / Take / effect lifecycle -> authority-state visual requirement

### Architecture source

Patch 0011 preserves distinct lifecycle states:

```text
provider attempt
    -> CandidatePerformance
    -> Integrity evaluation
    -> Interpretation + State Authority
    -> Accepted / Rejected / Alternate Take
    -> successful later causal commit
    -> effective historical Performance + Approved consequences
```

An Accepted Take is commit-eligible, not yet effective history.

### Visual requirement

When these distinctions become creator-visible, the UI must be capable of representing them without collapsing them into one generic `done`, `accepted`, or `saved` state.

Exact creator-facing terms remain open.

### Failure to avoid

- `Take Effective` as a universal state label;
- accepted = already historical/effective;
- alternate/rejected material visually indistinguishable from current truth;
- candidate creator input appearing to mutate Production immediately;
- color-only authority state.

---

## 9. Atomic causal commit -> changed-present visual requirement

### Architecture source

Patch 0012 establishes:

> exact Accepted Performance + every retained Approved consequence become effective together or neither does.

`ProductionState` is the immutable authoritative current projection produced by successful deterministic authority.

### Visual requirement

The creator should be able to experience causal consequence as a change in the **current Production**, not only as a history receipt.

The strongest target remains:

> **I am back in the same world, but it is different because of what happened.**

Potential visible evidence may include, when actually supported by state:

- changed relationships or available relationship evidence;
- changed knowledge/disclosure;
- changed circumstance/pressure;
- changed action affordances;
- changed salience/opportunity;
- changed unresolved conditions;
- changed information organization.

### Important nuance

A meaningful accepted historical Performance may produce no durable projected mutation. Therefore:

> **meaningful Performance != mandatory meter movement.**

### Failure to avoid

- every consequence causing a visual spectacle;
- mandatory relationship/progress meters;
- history screen becoming the endpoint of the causal loop;
- before/event/after storyboard becoming permanent product structure.

---

## 10. Patch 0013 effective opportunity -> post-consequence attention requirement

### Architecture source

Patch 0012 consumes the source Current Opportunity on successful commit.

Patch 0013 then recomputes and atomically establishes the next effective Current Opportunity before another Performer boundary.

Routing authority changes Current Opportunity only; it does not itself mutate World/Character/Knowledge/Relationship/Pressure truth.

### Visual requirement

The changed present may include a new salience/opportunity configuration after consequence.

The design should be able to communicate:

```text
something became effective
        -> current Production changed
        -> prior opportunity is consumed
        -> next opportunity becomes effective
        -> the living Scene continues
```

without implying that the Director authored what Characters must do next.

### Failure to avoid

- next actor appearing before causal-effect boundary completes;
- routing presented as Character intent/truth;
- opportunity-history mechanics exposed as default UI;
- automatic visual narrative that says the newly salient Character must speak.

---

## 11. Technical failure -> non-fiction visual requirement

### Architecture source

Performance/provider failure, refusal, timeout, cancellation, retry, malformed output, and other technical conditions do not become fiction merely because they occurred during generation.

### Visual requirement

Capability and technical-state communication must remain visually separate from dramatic state.

A provider timeout must not look like:

- Character silence;
- refusal;
- indecision;
- dramatic tension;
- consequence.

Likewise, Character silence/refusal must remain valid creative agency and not look like a system failure.

### Failure to avoid

- spinner/timeout becoming fictional behavior;
- generated placeholder dialogue masking failure;
- capability degradation mutating Production truth;
- background inference required just to maintain ambience.

---

## 12. Architecture-derived visual state axes

The design workstream should preserve these as orthogonal dimensions when relevant:

```text
PERSISTENT IDENTITY
Character identity / roster presence

DISCLOSURE PERSPECTIVE
creator-production | audience | character-bounded

CREATOR POSTURE
watch | direct | perform | write

TEMPORAL LOCUS
current | historical

PERFORMANCE / TAKE LIFECYCLE
candidate | evaluated | accepted/rejected/alternate | effective history
[exact creator-facing simplification remains open]

CAUSAL EFFECT
non-effective | effective

CURRENT OPPORTUNITY / SALIENCE
none during valid postcommit gap | one E0 Character | future small subset where later product permits

DRAMATIC CONTINUATION
resolved | unresolved / still active where authoritative state supports it

TECHNICAL CAPABILITY
available | degraded/partial | unavailable
```

No one visual treatment should be forced to encode all axes simultaneously.

---

## 13. Corrections to current render practice

Architecture review materially changes the next render brief.

### Remove by default

Unless the controlled scenario establishes them legitimately, future renderer prompts should not include generic:

- `Tension: High/Medium/Low`;
- `Progress`;
- `Risk`;
- `Relationship Dynamics` summaries;
- global psychological assessments;
- invented Character goals/motives;
- `Take Effective` terminology;
- automatic next-action recommendations framed as Character intent.

### Preserve

Future relational-field experiments should preserve:

- specific persistent people;
- relationship as composition rather than drawn graph;
- explicit but quiet current opportunity/salience when relevant;
- bounded information by absence;
- creator posture separate from disclosure perspective;
- candidate input separate from effective history;
- changed present after causal effect;
- next opportunity as salience, not obligation;
- transcript as supporting evidence rather than dominant surface.

---

## 14. Next changed-present experiment — corrected target

Do **not** repeat the prior explanatory triptych as a product hypothesis.

The next visual falsification target should be a **single current-state surface** after one already-effective causal change.

Controlled requirements:

- same Production P0;
- same Scene S0;
- same persistent Characters A / B / C;
- one explicitly defined prior effective event/consequence package known only to the Director-side experiment brief;
- current relational field reflects the changed authoritative projection;
- current opportunity reflects the post-Patch-0013 effective salience state;
- no before panel;
- no event panel;
- no timeline;
- no causal graph;
- no generic tension/progress/risk meters;
- no explanatory `what changed` summary in the primary surface;
- no private-mind inference;
- no invented creator-facing ontology;
- only information allowed under the selected Presentation Perspective;
- still-frame must remain intelligible without motion/color alone.

Primary test:

> **Can the creator infer that something consequential happened because the same people now occupy a materially different current reality?**

Secondary test:

> **Can the new current opportunity be legible as salience without reading as obligation?**

---

## 15. Accessibility + ARM64/NPU implications

Architecture-derived visual meaning must remain accessible through programmatic state and textual equivalents.

Do not require:

- spatial composition alone to convey disclosure/authority;
- portrait recognition alone to identify Characters;
- color alone to distinguish lifecycle/effect/posture;
- continuous motion to convey current opportunity;
- graph physics or persistent custom rendering to maintain relationship meaning;
- idle AI/NPU inference to calculate decorative emotional state.

The design should be computationally quiescent when Production state is unchanged.

---

## 16. What this crosswalk does not authorize

This document does not authorize or freeze:

- final UI;
- final Stage layout;
- final Character image workflow;
- user-uploaded Character image feature;
- generated Character portrait feature;
- exact Character Context taxonomy;
- final opportunity indicator;
- final Take interaction;
- branch/rehearsal/canon/retcon UX;
- exact Windows controls/materials;
- XAML/C#;
- provider/model integration;
- Windows AI Foundry/NPU behavior;
- website production implementation;
- branch convergence or final visual identity.

---

## 17. Recursive audit

Audit sequence:

`current app authority -> Character/Performer identity -> Access disclosure -> Context semantics -> Performance grammar -> Director opportunity -> Take lifecycle -> causal effect -> effective next opportunity -> creator ontology guard -> technical failure boundary -> existing visual laws -> accessibility -> ARM64 quiescence -> renderer validity -> scope`

Material corrections made during construction:

1. updated design engineering authority from completed Patch 0012 to completed Patch 0013;
2. separated E0 single-Character opportunity from broader product small-subset attention possibility;
3. removed any implication that current textual CandidatePerformance freezes a transcript-first final product;
4. made `Character != Portrait` a visual inference, not an app-engineering contract;
5. classified user-supplied Character images as open, not current product authority;
6. strengthened hidden-information behavior from dimming to absence unless existence itself is legitimately disclosed;
7. removed generic `Tension / Progress / Risk` instrumentation from default render requirements;
8. preserved creator-facing ontology extensibility instead of mapping every E0 category to a permanent panel;
9. separated current opportunity/salience from obligation and from Character intent;
10. preserved Accepted Take != causal effectiveness;
11. preserved meaningful accepted historical texture without requiring durable mutation or meter movement;
12. incorporated Patch 0013's postcommit next-opportunity boundary into changed-present visual requirements;
13. separated technical failure from fictional silence/refusal;
14. prevented before/event/after comparison from becoming required final UI;
15. converted the next changed-present test from explanatory storyboard to a single current-state falsification surface;
16. retained accessibility and quiescent ARM64/NPU constraints without claiming unverified WinUI/NPU implementation.

After each material correction, the audit restarted from current app authority.

Final complete pass:

> **PASS — no remaining material architecture mismatch, visual-authority collapse, disclosure leak, stale Patch 0012 dependency, scope violation, or worthwhile improvement within this crosswalk scope.**

---

## 18. Director gate

Director decision requested:

> **Adopt this crosswalk as the architecture-to-visual requirements bridge for subsequent Kymaean visual experiments.**

If approved, the next smallest justified action is:

> **Prepare and render one isolated VSG-B changed-present current-state experiment using the corrected architecture-derived brief in Section 14, preserving the original output before critique or refinement.**

Do not automatically reopen VSG-A/VSG-C, select a final visual branch, design a final Character-image workflow, or begin production implementation.