<!-- D-R1-STATUS: ACTIVE LAW -->

# Ensemble Website / Kymaean — Repository Agent Authority

Status: ACTIVE REPOSITORY WORKFLOW LAW
Updated: 2026-09-08

## Purpose

This file is the durable bootstrap for any agent or fresh chat working in `Rylascoo/Ensemble-Website`. It governs repository workflow and continuity; it does not replace design law, product law, or the active checkpoint.

## First reads

Read in this order before substantive work:

1. `CURRENT_STATE.md` — the only volatile phase/current-boundary authority in this repository.
2. `docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md` — design-gate and recursive-audit authority.
3. `docs/PROJECT_REASONING_TASK_SCOPE_OPTIMIZATION_PROTOCOL.md` — Sol High task-scope and external-specialist allocation law.
4. `docs/evidence/DESIGN_LEDGER.md` — durable closure, prior-result, and re-derivation guardrail.
5. The active handoff and evidence named by `CURRENT_STATE.md`.
6. `docs/DESIGN_CONTINUITY.md` only for durable design law and lineage; historical phase/status statements inside it do not override `CURRENT_STATE.md`.
7. `Rylascoo/Ensemble-Project/CURRENT_STATE.md` only when exact current product/engineering truth materially matters.
8. Google Drive `Ensemble Project` for visual-master assets and provenance when the task requires them.

Do not reconstruct current authority from branch names, old handoffs, historical approval records, or chat history.

## Primary reasoning surface

GPT-5.6 Sol High is the normal project reasoning, design-governance, repository-work, recursive-audit, and continuity surface.

Astra/Codex is a scarce external specialist. Use it only for a tightly bounded high-leverage task when its local/batch repository environment, otherwise unavailable runtime/browser/toolchain capability, or deliberately independent falsification perspective materially exceeds what is available in Sol High. Astra output is evidence/advice, never authority, and must be reconciled and recursively audited here before adoption.

Do not pause ordinary project work because Astra capacity is unavailable.

## Earned-approval law

Within the website/brand/design lane:

> Clean recursive audit = earned approval.

Correct material defects, restart the relevant audit, and advance only after one complete pass is clean. Record:

`APPROVED BY STANDING DIRECTOR DELEGATION — CLEAN RECURSIVE AUDIT.`

Do not request a redundant Director approval for a clean in-lane gate. This never creates product, engineering, security, runtime, Store, or other outside-lane authority.

## Repository topology

The repository uses one authoritative history on `main` and three explicit operational planes:

- `site/`: **deployable website data plane**. The only subtree that may be configured as the public Cloudflare Workers project root or contain production website source/Wrangler configuration.
- `intelligence/`: **non-public website/design control plane**. A front door for repository/design intelligence and cross-repository authority. It does not absorb or duplicate the product backend from `Rylascoo/Ensemble-Project`.
- `updates/`: **non-deployable website change/release plane**. Holds change packets, deployment records and release notes; executable source remains in `site/`.

Existing canonical surfaces remain where they are:

- `CURRENT_STATE.md`: small volatile checkpoint only. Do not turn it into an archive.
- `AGENTS.md`: durable repository operating instructions.
- `docs/evidence/DESIGN_LEDGER.md`: durable closure/reopening ledger and anti-re-derivation record.
- `docs/`: design law, methods, handoffs, evaluations, and historical evidence. A document's historical presence does not make it current law.
- `prototypes/`: experimental/renderable research surfaces. Never publication source by implication.
- `assets/`: repository assets. Never publication source by implication.
- `tools/`: repository validation/design tooling. Never publication source by implication.

Do not mass-move `docs/`, `prototypes/`, `assets/` or `tools/` into the new front-door namespaces without a separately audited migration that preserves references and evidence identity.

## Cloudflare / website branch law

Cloudflare isolation is directory-based, not branch-based.

- The production repository branch is `main` unless a later explicit deployment decision changes it.
- The public Worker root directory is `site/` once a deployable site is authorized.
- Configure Cloudflare build watch paths to include `site/**` when available.
- Any public-site `wrangler.toml`, `wrangler.json`, or `wrangler.jsonc` belongs inside `site/`.
- The `site/` project must be self-contained; deployable files must not reach outside the subtree for `docs/`, `prototypes/`, `assets/`, `intelligence/`, `updates/` or `tools/` dependencies.
- A permanent branch named `site` is not authority and is not deployment isolation. New website work branches from current `main` using a scoped branch such as `site/<work-package>` and merges back after audit/validation.

The current `site/` directory is an intentionally non-deployable publication boundary until authorized production source/configuration exists there. Repository organization alone does not authorize deployment.

## Backend authority boundary

Do not create a second product/backend implementation inside this repository. Runtime orchestration, provider/backend intelligence, application services and engineering authority remain in `Rylascoo/Ensemble-Project` unless the Director explicitly changes repository ownership.

`intelligence/` in this repository means **website/design/repository intelligence**, not product runtime backend code.

## Authority and evidence discipline

- Preserve frozen criteria. Do not invent new scoring gates mid-program.
- Preserve pixels as post-render evidence; intent cannot rescue failed output.
- Preserve renderer isolation where the governing lane/method requires it.
- Preserve historical evidence without allowing stale status text to regain authority.
- Distinguish a carrier-specific failure from global falsification.
- Before repeating an experiment or reopening a closed question, check `DESIGN_LEDGER.md` and the cited evidence.
- Reopen a closed result only for new evidence, a direct contradiction, a changed governing contract, or an explicitly authorized new program.

## Design-ledger write trigger

The design ledger is part of closing the result, not optional later housekeeping.

Any design-lane event that:
- consumes an experimental/render round;
- closes or rejects a candidate;
- reopens a previously closed result;
- changes a program or direction termination state; or
- materially changes the lawful re-entry / next-design boundary

MUST append or update the applicable `docs/evidence/DESIGN_LEDGER.md` entry in the same logical result commit. A single ledger entry may cover coincident events, such as a failed round that simultaneously closes its candidate and establishes a successor-analysis boundary.

Whenever that event also changes the volatile current boundary, `CURRENT_STATE.md` MUST be updated in the same logical closure operation.

When the available repository write surface supports an atomic multi-file commit, the evaluation/closure evidence, ledger update and required current-state update belong in that same commit. If the connected write surface cannot create an atomic multi-file commit, those writes form one indivisible closure sequence: do not begin or commit the next design-stage artifact until all required continuity writes have landed, been read back, and survived the required recursive/hosted validation.

Preserve ledger history. Prefer append-only entries; correct an earlier ledger entry only when the entry itself contains a factual error, and make the correction explicit rather than rewriting historical sequence to look contemporaneously current.

This section establishes semantic workflow law only. It does not define or implement a mechanical enforcement guard; an independently authored guard may verify the law separately.

## Structural-reconciliation safeguards

Repository restructuring is organizational work, not redesign.

- do not change design scores or historical experiment outcomes by restructuring;
- do not rewrite history to make old documents appear contemporaneously correct;
- do not move or rewrite `prototypes/`, `assets/`, `docs/` or `tools/` without an explicit audited migration contract;
- do not delete a branch that contains any commit unique to that branch;
- before any permitted branch deletion, create the required archival tag and verify the branch is a strict ancestor with zero unique commits;
- do not change the Cloudflare publication root merely to silence a failing deployment;
- do not promote a historical prototype into `site/` merely because a production site is absent.

## Current-state size discipline

Keep `CURRENT_STATE.md` concise: authority, active checkpoint, exact next action, hard boundaries, and pointers. Durable history belongs in the ledger/evidence; workflow law belongs in durable authority files.

## Completion discipline

For one bounded objective, complete all logically coupled reads, edits, checks, evidence updates, recursive audit, readback, and continuity updates that are already authorized. Stop only at a real authority or unavailable external-validation boundary.
