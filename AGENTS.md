<!-- D-R1-STATUS: ACTIVE LAW -->

# Ensemble Website / Kymaean — Repository Agent Authority

Status: ACTIVE REPOSITORY WORKFLOW LAW
Updated: 2026-09-08

## Purpose

This file is the durable bootstrap for any agent or fresh chat working in `Rylascoo/Ensemble-Website`. It governs repository workflow and continuity; it does not replace design law, product law, or the active checkpoint.

## Fresh-chat reconciliation

Before substantive work:

1. Resolve live branch refs and the exact active HEAD from GitHub. Default-branch search and chat memory are discovery aids, not load-bearing evidence.
2. Read `CURRENT_STATE.md` at that exact ref first. It is the only volatile phase/current-boundary authority in this repository. If a live work branch diverges from `main`, compare its state surface before relying on a volatile fact.
3. Verify `CURRENT_STATE.md` remains within the mechanical 3 KiB size cap and N=3 commit-distance currency boundary. Passing those checks does not prove the prose correct; reconcile load-bearing claims against exact evidence.
4. Read `docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md` — design-gate and recursive-audit authority.
5. Read `docs/PROJECT_REASONING_TASK_SCOPE_OPTIMIZATION_PROTOCOL.md` — Sol High task-scope and external-specialist allocation law.
6. Read `docs/evidence/DESIGN_LEDGER.md` — durable closure, prior-result, and re-derivation guardrail.
7. Read the active handoff/evidence named by `CURRENT_STATE.md`, then `docs/DESIGN_CONTINUITY.md` only for durable design law/lineage; historical status there cannot override current state.
8. Read `Rylascoo/Ensemble-Project/CURRENT_STATE.md` at its exact active engineering ref only when current product/engineering truth materially matters.
9. Use Google Drive `Ensemble Project` for visual-master assets/provenance when required.
10. Inspect any suspicious cross-lane artifact before adopting it: design/UI/website/visual work belongs here/Drive; engineering source/tests/provider/runtime/validation implementation belongs in `Ensemble-Project`; central product/policy/ODR decisions belong in `Ensemble-Project` even when raised by Design Sol.

Do not reconstruct current authority from branch names, old handoffs, historical approvals, attractive recent work, default-branch search alone, or chat summaries.

## Exact-ref and self-healing rule

A fresh chat should detect continuity/residency drift automatically, classify it, and repair deterministic in-lane defects already covered by standing authority. It must not silently move an ambiguous artifact, rewrite design history, promote evidence into product authority, discard unique branch work, or change an outside-lane decision. If authority is genuinely ambiguous, surface the Director decision rather than guessing.

`tools/generate_docs_index.py` and D-R1 status law govern Markdown documents. Non-Markdown evidence such as `.txt`, `.json`, `.svg`, or render artifacts does not become active law merely because it lacks a D-R1 header; resolve its role through `CURRENT_STATE.md`, `DESIGN_LEDGER.md`, governing evidence references, and the applicable method contract.

## Primary reasoning surface

GPT-5.6 Sol High is the normal project reasoning, design-governance, repository-work, recursive-audit, and continuity surface.

Astra/Codex is a scarce external specialist. Use it only for a tightly bounded high-leverage task when its local/batch repository environment, otherwise unavailable runtime/browser/toolchain capability, or deliberately independent falsification perspective materially exceeds what is available in Sol High. Astra output is evidence/advice, never authority, and must be reconciled and recursively audited here before adoption. Do not pause ordinary project work because Astra capacity is unavailable.

## Earned-approval law

Within the website/brand/design lane:

> Clean recursive audit = earned approval.

Correct material defects, restart the relevant audit, and advance only after one complete pass is clean. Record:

`APPROVED BY STANDING DIRECTOR DELEGATION — CLEAN RECURSIVE AUDIT.`

Do not request redundant Director approval for a clean in-lane gate. This never creates product, engineering, security, runtime, Store, or other outside-lane authority.

## Repository topology

The repository uses one authoritative history on `main` and three explicit operational planes:

- `site/`: **deployable website data plane**; only subtree eligible as public Cloudflare Workers root or production website source/configuration.
- `intelligence/`: **non-public website/design control plane**; repository/design intelligence and cross-repository authority references, never a duplicate product backend.
- `updates/`: **non-deployable website change/release plane**; change packets/deployment records/release notes, not executable website source.

Existing canonical surfaces remain:
- `CURRENT_STATE.md`: small volatile checkpoint only;
- `AGENTS.md`: durable operating instructions;
- `docs/evidence/DESIGN_LEDGER.md`: durable closure/reopening ledger;
- `docs/`: design law, methods, handoffs, evaluations, historical evidence;
- `prototypes/`: experimental/renderable research, never publication source by implication;
- `assets/`: repository design assets, never deployable merely by presence;
- `tools/`: repository validation/design tooling.

Do not mass-move `docs/`, `prototypes/`, `assets/` or `tools/` without a separately audited migration preserving references and evidence identity.

## Cross-repository residency

One artifact has one canonical home. Do not copy an authoritative engineering document here to improve continuity; link the exact engineering source instead. Do not place app UI designs, website prototypes, brand assets, or design-specific evidence into `Ensemble-Project` merely because engineering may consume them. Central Director/product/policy/ODR decisions remain in `Ensemble-Project`, with this repository referencing them when needed.

If a misplaced artifact is found: record original repo/path/commit, classify authority, identify canonical destination, audit inbound references, verify the destination, then remove the misplaced active copy only after provenance and links are safe. Subject matter alone is not enough to move a file.

## Cloudflare / website branch law

Cloudflare isolation is directory-based, not branch-based.

- Production branch is `main` unless later explicit deployment authority changes it.
- Public Worker root is `site/` once deployable source is authorized.
- Use `site/**` build watch when available.
- Public-site Wrangler configuration belongs inside `site/`.
- `site/` must be self-contained; deployable files may not reach into `../docs`, `../prototypes`, `../assets`, `../intelligence`, `../updates`, or `../tools`.
- A permanent `site` branch is not authority. Website work branches from current `main`, uses a scoped name such as `site/<work-package>`, and merges back after audit/validation.

The current `site/` directory remains intentionally non-deployable until authorized production source/configuration exists. Repository organization alone does not authorize deployment.

## Backend authority boundary

Do not create a second product/backend implementation here. Runtime orchestration, provider/backend intelligence, application services, engineering source/tests, and engineering validation remain in `Rylascoo/Ensemble-Project` unless the Director explicitly changes ownership. `intelligence/` means website/design/repository intelligence, not product runtime backend code.

## Authority and evidence discipline

- Preserve frozen criteria; do not invent scoring gates mid-program.
- Preserve pixels as post-render evidence; intent cannot rescue failed output.
- Preserve renderer isolation where the governing lane/method requires it.
- Preserve historical evidence without letting stale status text regain authority.
- Distinguish carrier-specific failure from global falsification.
- Check `DESIGN_LEDGER.md` before repeating an experiment or reopening a closed question.
- Reopen only for new evidence, direct contradiction, changed governing contract, or explicitly authorized new program.

## Design-ledger write trigger

The design ledger is part of closing the result, not optional housekeeping. Any design-lane event that consumes a render round; closes/rejects a candidate; reopens a closed result; changes a program/direction termination state; or materially changes lawful re-entry/next-design boundary MUST append/update the applicable `docs/evidence/DESIGN_LEDGER.md` entry in the same logical result commit.

When that event changes the volatile current boundary, `CURRENT_STATE.md` MUST be updated in the same logical closure. Prefer one atomic multi-file commit. If the connected write surface cannot do that, the writes form one indivisible closure sequence and the next design-stage artifact cannot begin until all continuity writes land, are read back, and pass hosted/recursive validation.

Preserve ledger history. Correct an earlier entry only for factual error and make the correction explicit.

## Structural safeguards

Repository restructuring is organization, not redesign:
- do not change design scores or historical outcomes;
- do not rewrite history to make old documents appear contemporaneously correct;
- do not move/rewrite `prototypes/`, `assets/`, `docs/` or `tools/` without an audited migration contract;
- do not delete a branch containing unique commits;
- before permitted branch deletion, create/verify the required archival tag and strict-ancestor/zero-unique condition;
- do not change Cloudflare root merely to silence deployment failure;
- do not promote a historical prototype into `site/` because production source is absent.

## Current-state discipline

Keep `CURRENT_STATE.md` at or below **3 KiB** and within **3 commits** of the active branch head. It contains only authority, active checkpoint, exact next action, hard boundaries, and pointers. Durable history belongs in ledger/evidence; workflow law belongs here. The N=3 rule is a staleness ceiling, not a requirement to embed HEAD in state and create self-referential commits.

## Completion discipline

For one bounded objective, complete all logically coupled reads, edits, checks, evidence updates, recursive audit, readback, and continuity updates already authorized. Stop only at a real authority or unavailable external-validation boundary. Before closeout, check exact-ref continuity, branch lifecycle, cross-repo residency, state size/currency, and whether the next action remains singular and lawful.
