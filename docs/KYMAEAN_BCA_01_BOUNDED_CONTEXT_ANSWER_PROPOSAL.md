<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN BCA-01 — BOUNDED CONTEXT ANSWER PROPOSAL

Status: DIRECTOR PROPOSAL FOR REVIEW / NON-RENDER CONTEXT-CONTENT CONTRACT / NO FINAL CONTEXT TAXONOMY OR IMPLEMENTATION SELECTED

Date: 2026-09-03

Phase: Kymaean App + Website Design Synthesis — after CDT-V1 structural transition validation

## 0. Purpose

Define the smallest truthful contextual answer Kymaean should reveal when the creator follows one meaningful current anchor and asks one bounded question.

BCA-01 exists because CDT-V1 validated the transition structure but exposed content failure: the context panel became too schema-complete and promoted rendered Scene cues into unsupported Character-observation claims.

This proposal does not select final panel geometry, Character Context taxonomy, transcript architecture, causal-history UI, final labels, final WinUI controls, inference pipeline, or production implementation.

Authority basis:

- `CURRENT_STATE.md`;
- `docs/KYMAEAN_CDT_01_CONTEXT_DISCLOSURE_TRANSITION_PROPOSAL.md`;
- `docs/KYMAEAN_CDT_V1_BOUNDED_CONTEXT_INVOCATION_RESULT.md`;
- `docs/KYMAEAN_SIPD_01_STAGE_INFORMATION_PRESENCE_PROGRESSIVE_DISCLOSURE_PROPOSAL.md`;
- `docs/KYMAEAN_CHARACTER_BOUNDED_WATCH_PERFORM_CONTRACT_01.md`;
- `docs/KYMAEAN_APP_ARCHITECTURE_TO_VISUAL_REQUIREMENTS_PATCH_0014_ADDENDUM_01.md`;
- current application authority at `Rylascoo/Ensemble-Project` main `7475a9397cff9063673908c666a729f0f3cd4525`, H1 Patch 0014.

Durable laws:

> **More detail does not mean more privilege.**

> **Question-bounded, not schema-complete.**

> **Current Stage presents what is true now; causal trace explains why.**

> **Visible in the Stage representation != observed by the Character.**

---

## 1. Design question

Given:

- one current anchor;
- one current creator question;
- one active Presentation Perspective;
- one current Production state;

what is the minimum answer that helps the creator understand or act without exposing unrelated context, inventing observation/private mind, or turning a contextual surface into a Character dossier?

The answer must avoid both failure modes:

```text
TOO LITTLE
-> the creator cannot resolve the current question safely

TOO MUCH
-> the interface dumps every field/category it can access
```

---

## 2. Core answer law

A bounded context answer should contain only information that passes all four gates:

1. **Question relevance** — directly helps answer the invoked question.
2. **Disclosure authority** — legitimately available under the active Presentation Perspective.
3. **Current authority** — supported by current authoritative state or by an explicitly entered historical route.
4. **Minimum sufficiency** — no additional field/category is shown merely because it exists.

Required principle:

> **The answer is composed for the question, not rendered from the storage schema.**

This is a presentation/composition law, not permission for model-authored invention.

---

## 3. BCA answer shape

The default answer has at most four semantic parts. These are responsibilities, not required visual containers.

### A0 — Anchor + question

Identify what the creator is inspecting and what question is being answered.

Examples of semantic form:

```text
Anchor: Current Opportunity C
Question: Why is C currently relevant?
```

or:

```text
Anchor: current condition X
Question: What is available to B about this condition now?
```

The exact user-facing wording remains open.

### A1 — Direct answer

One compact statement of the current authoritative answer.

Requirements:

- current-tense when the route is current context;
- no inferred psychology;
- no unsupported observation;
- no hidden provenance metadata;
- no thematic narration.

### A2 — Supporting basis

Only the smallest authoritative facts/evidence needed to understand or trust A1.

Not every answer requires this section.

Support may include legitimately available current facts, conditions, or explicit accessible evidence.

Do not enumerate all possible evidence categories.

### A3 — One justified next path

At most one or a very small number of semantically relevant follow-up actions, such as:

- inspect the relevant current fact;
- ask `Why?` and deliberately enter causal trace;
- return to Stage.

Do not expose a standing mini-navigation system such as `Current Context / Related Details / Causal Trace / Transcript / Relationships / Diagnostics` for every anchor.

---

## 4. Question classes

BCA recognizes a small set of interaction question classes for design purposes only. These are not storage enums or mandatory UI tabs.

### Q1 — Current relevance

Example:

`Why is this Character/opportunity/condition relevant now?`

Answer from current authoritative state only.

Do not automatically enter history.

### Q2 — Available current context

Example:

`What is available to B about this current situation?`

Answer only from material legitimately available under B's disclosure authority.

Absence remains absence. Do not name inaccessible private categories to explain what is missing.

### Q3 — Current authority/effect

Example:

`Is this current, effective, provisional, or historical?`

Answer with the smallest local authority/effect distinction necessary to prevent confusion.

### Q4 — Causal why

Example:

`Why is this true now?`

This is not an ordinary current-context answer. It is the entry point to causal trace/history.

BCA should hand off deliberately to the historical route rather than smuggling history into the current answer.

### Q5 — Capability availability

Example:

`Why can’t I do this action right now?`

Answer technical capability truth without fictionalizing it.

Capability state is not Character state and not Production history.

---

## 5. Evidence discipline

### 5.1 Current authoritative facts

These are the preferred basis where available.

Examples may include, only when actually authoritative and disclosure-permitted:

- a current condition is active;
- a revised agreement is operative;
- an opportunity is currently assigned/salient;
- a constraint currently applies or no longer applies;
- a current Scene fact is established.

### 5.2 Observation

Do not claim a Character observed something unless current product authority explicitly provides that observation.

Current Patch 0014 specifically prohibits deriving observation merely from:

- co-presence;
- Candidate visible text;
- addressed Characters;
- nomination;
- Director selection;
- relationships;
- SceneState;
- causal adjacency.

Therefore:

```text
rendered/visible Scene cue
!=
Character observation fact
```

A future observation system may later authorize such content. BCA must not anticipate it.

### 5.3 Heard / recent Performance

Current Patch 0014 canonical Context v2 does not populate recent Performance:

```text
recentPerformances = []
RecentPerformanceText = empty
```

Therefore recent dialogue/transcript cannot be required to answer a current bounded-context question at this checkpoint.

Future canonical Performance context may later extend BCA, but it must arrive through separate product authority.

### 5.4 CharacterClaim / recall

CharacterClaim disclosure/recall remains deferred.

Do not answer `B remembers...` or `B recalls...` merely because a CharacterClaim exists.

### 5.5 Private subjective state

Other-owned Constitution, Disposition, Circumstance, Observation, Knowledge, Belief, Suspicion, Memory, Goal and Relationship material remains denied under current Patch 0014 access rules unless the material belongs to the active subject as authorized.

Do not convert expression, gaze, posture or social geometry into trust, fear, confidence, skepticism, intention, understanding, affection, hostility, agreement, or desire.

---

## 6. Bounded absence law

If information is not legitimately available, default to omission rather than placeholder disclosure.

Avoid:

```text
Unknown to B:
- C's private reasoning
- C's hidden goal
- C's true belief
```

because merely naming those categories can reveal schema/privilege information.

Allowed only when the existence of a specific unavailable item is itself legitimately known and materially relevant.

Required principle:

> **A bounded answer becomes quieter through subtraction.**

---

## 7. Direct-answer composition rules

The direct answer must be:

- narrow;
- factual;
- current-locus aware;
- perspective-bounded;
- authority-sensitive;
- non-psychological unless authoritative subjective state is actually available;
- free of marketing/thematic narration;
- free of model/provider/provenance identifiers unless the creator explicitly enters technical detail.

Avoid language such as:

- `C seems ready`;
- `B understands`;
- `A is listening`;
- `C appears confident`;
- `the group is aligned`;
- `the conversation is moving forward`;
- `new possibilities are emerging`.

Such language may be visually suggestive but is not authoritative context unless separate product state explicitly supports it.

---

## 8. Example design test — Current Opportunity C

Controlled question:

> **Why is C currently relevant?**

The answer must not rely on:

- facial expression;
- gaze;
- body orientation;
- implied turn-taking;
- transcript not currently present in Context v2;
- hidden Character intent;
- historical causal chain unless the user asks `Why?` at the history level.

A valid answer would need to derive from current deterministic Production/Opportunity authority and only the smallest disclosure-permitted current facts that explain the present relevance.

Important limitation:

BCA-01 does **not** invent the exact answer content here because current app authority must supply the actual authoritative fields available for this specific Production state.

The visual test should therefore use a controlled mocked authoritative current fact set explicitly labeled as design-test data, not silently imply that Patch 0014 already exposes an unimplemented field.

---

## 9. Current answer versus causal trace

BCA reinforces the CDT boundary:

```text
Current answer
= what is legitimately true/available now for this question

Causal trace
= why that current truth became true
```

If the creator asks a historical `why`, BCA should transition to causal trace rather than append a mini-history beneath every current answer.

A current answer may contain a concise `Why?` affordance when the origin fact has causal history worth inspecting.

---

## 10. One answer, one center of gravity

A contextual answer should have one semantic center.

Do not simultaneously answer:

- who is this Character;
- what they know;
- what they heard;
- what they believe;
- why history changed;
- what the provider did;
- what commands are available.

unless the creator explicitly asked a compound question and product authority permits each part.

Default law:

> **One current question -> one bounded answer -> one clear return path.**

---

## 11. Accessibility contract

A bounded answer must remain coherent without relying on panel position, portraits, color or motion.

Required:

- anchor relationship is programmatically identified;
- question/answer heading is semantically clear;
- active perspective is available where disclosure differs materially;
- reading order places direct answer before supporting basis;
- omitted privileged information does not leave confusing empty placeholders;
- any `Why?`/history action is distinguished from current-context detail;
- focus returns predictably to the invoking anchor;
- high contrast/text scaling/narrow layout preserve answer meaning.

---

## 12. ARM64 / quiescence contract

The BCA contract should favor deterministic local composition from already-authoritative state.

Do not require:

- speculative background summaries;
- idle generative inference;
- provider polling;
- face/emotion analysis;
- continuous relationship scoring;
- precomputed answers for every possible anchor/question;
- persistent GPU/NPU activity merely to keep context surfaces ready.

Future inference-backed explanation, if separately authorized, must be capability-gated and degrade truthfully without altering Production authority.

---

## 13. Controlled validation proposal

If BCA-01 is approved, the smallest justified visual test is:

`BCA-V1 — One Question / One Answer`

Use the established SIPD/CDT semantic baseline:

- P0 / S0 / A / B / C;
- Character-Bounded Watch;
- Current Opportunity = C;
- response not required;
- same current Production state;
- context invoked from Current Opportunity C or Character C;
- exactly one explicit current question;
- exactly one compact bounded answer;
- only the minimum supporting current facts required;
- one return affordance;
- optional single `Why?` affordance that clearly enters causal trace;
- no full evidence taxonomy;
- no `What I Can Observe` unless explicit observation authority is supplied by the design-test data;
- no recent transcript requirement;
- no inaccessible-category placeholders;
- no Character dossier sections;
- no private-mind inference;
- no Perform controls;
- no diagnostics;
- no thematic narration.

The visual surface remains unselected; this is an information-composition test.

Falsification questions:

1. Can the user identify the anchor and exact question?
2. Does the first statement directly answer that question?
3. Is every supporting fact necessary?
4. Is every supporting fact authorized under the active perspective?
5. Does any statement infer observation/private mind from visual portrayal?
6. Does the answer avoid a schema dump?
7. Does current context remain distinct from causal trace?
8. Does Watch remain Watch?
9. Does Current Opportunity remain independent/non-obligatory?
10. Could the same answer be read coherently in a narrow sequential layout and by assistive technology?

Stop after one unrefined output and critique. No automatic correction chain.

---

## 14. Surface quarantine

BCA selects no final surface.

No inheritance rights for:

- CDT/SIPD photoreal office/cast;
- exact inspector width/position;
- white rounded cards;
- portrait chips;
- tab bars;
- evidence-section iconography;
- green/orange/blue states;
- exact typography;
- generic productivity/SaaS shell styling.

`Surface != law.`

---

## 15. Recursive audit

Audit order:

`Director authorization -> CDT-V1 result -> Patch 0014 Access/Context authority -> question relevance -> disclosure authority -> current authority -> minimum sufficiency -> observation boundary -> recent-Performance boundary -> CharacterClaim/recall boundary -> private subjective-state boundary -> current/history separation -> Watch/Perform -> opportunity independence -> accessibility -> ARM64 quiescence -> surface quarantine -> validation sufficiency -> scope`

Material corrections made during construction:

1. made question relevance an explicit first gate so context cannot default to schema enumeration;
2. separated direct answer from supporting basis;
3. prohibited observation claims derived from rendered visibility;
4. prohibited recent transcript as a required current answer source under Patch 0014;
5. kept CharacterClaim/recall deferred;
6. made bounded absence subtractive rather than placeholder-based;
7. separated current answer from causal trace/history;
8. limited follow-up navigation so every answer does not become a mini information portal;
9. avoided inventing the exact `Why is C relevant?` answer because current product authority must supply the actual authoritative facts;
10. made deterministic local composition the default and speculative inference non-required.

After each material correction, audit restarted from Director authorization and current product authority.

Final complete pass:

> **PASS — no remaining material privilege leak, unsupported-observation assumption, transcript-assumption leak, schema-completeness drift, current/history conflation, posture/opportunity coupling, accessibility defect, quiescence concern, surface-inheritance leak, or worthwhile correction inside BCA-01 proposal scope.**

---

## 16. Director gate

Director decision requested:

> **Adopt BCA-01: one current anchor and one creator question produce one minimal truthful answer composed only from question-relevant, perspective-authorized, currently authoritative information; unsupported observation/private mind, schema dumps, transcript assumptions, inaccessible-category placeholders, and hidden historical explanation are excluded.**

If approved, the next smallest justified action is exactly one controlled:

`BCA-V1 — One Question / One Answer`

Then critique and stop.

No final Character Context taxonomy, transcript system, observation system, causal-history UI, WinUI implementation, AI inference pipeline, or website implementation is authorized by this proposal.
