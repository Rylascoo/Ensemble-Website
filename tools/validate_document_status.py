#!/usr/bin/env python3
"""Validate document structure, not design correctness or creative authority."""

import sys

sys.dont_write_bytecode = True
from generate_docs_index import INDEX, ROOT, STATUSES, collect_statuses, render_index, text_paths


def main():
    try:
        statuses = collect_statuses(ROOT)
        texts = text_paths(ROOT)
        if INDEX not in statuses:
            raise ValueError(f"{INDEX}: missing")
        # The canonical rendering includes the actual total and each path exactly
        # once in its header's group. Byte equality also rejects missing entries,
        # duplicate entries, cross-group duplicates, bad counts and ordering drift.
        if (ROOT / INDEX).read_bytes() != render_index(statuses, texts):
            raise ValueError(f"{INDEX}: differs from the canonical corpus index; regenerate it")
        print(f"PASS: {len(statuses)} Markdown documents; {len(texts)} text records; headers and index valid")
        print(" / ".join(f"{sum(value == status for value in statuses.values())} {status}" for status in STATUSES))
        return 0
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
