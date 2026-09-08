<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# W1 text corpus coverage

Base: `548c16906786268fec397ed27ef2660638465835`.
Branch: `renovation/w1-txt-corpus-coverage`.

Before: 282 Markdown documents; 36 text records (not inventoried).
After: 283 Markdown documents; 36 text records inventoried for visibility only.
No text-record status, authority or classification is inferred.

Verification used the bundled Python executable because python3 was not on PATH.
The two unchanged test suites ran with -B to suppress bytecode artifacts.

Generator stdout (exit 0):
```
Generated docs/INDEX.md
```

Generator --check stdout (exit 0):
```
PASS: docs/INDEX.md is byte-for-byte up to date
```

Document validator stdout (exit 0):
```
PASS: 283 Markdown documents; 36 text records; headers and index valid
42 ACTIVE LAW / 9 SUPERSEDED / 221 HISTORICAL EVIDENCE / 11 UNCLASSIFIED
```

Unchanged regression suites:
- tools/test_stage6m_maquette.py: exit 0; stdout empty; stderr reports 13 tests, OK.
- tools/test_stage6m_core_bypass.py: exit 0; stdout empty; stderr reports 2 tests, OK.

Fail-closed probe: created docs/evidence/_W1_PROBE.txt without regenerating the index.
Validator exit 1; stdout empty; exact stderr:
```
FAIL: docs/INDEX.md: differs from the canonical corpus index; regenerate it
```
Removed the probe and reran the validator: exit 0; exact stdout:
```
PASS: 283 Markdown documents; 36 text records; headers and index valid
42 ACTIVE LAW / 9 SUPERSEDED / 221 HISTORICAL EVIDENCE / 11 UNCLASSIFIED
```
The probe is absent from disk and git status and is not committed.

Scope readback: only the generator, validator, document-status workflow, generated
index and this new evidence record changed. Existing text records and excluded
paths are unchanged. The index was generated, never hand-edited. Markdown marker
validation and --check byte equality remain unchanged. No stop condition fired.
No commit, push or merge was performed.
