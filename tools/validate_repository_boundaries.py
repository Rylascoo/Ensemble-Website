#!/usr/bin/env python3
"""Fail closed when publication/control-plane repository boundaries drift."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_BOUNDARIES = (
    ROOT / "site" / "README.txt",
    ROOT / "intelligence" / "README.txt",
    ROOT / "updates" / "README.txt",
)

WRANGLER_NAMES = {"wrangler.toml", "wrangler.json", "wrangler.jsonc"}
DEPLOYABLE_TEXT_SUFFIXES = {
    ".html",
    ".css",
    ".js",
    ".mjs",
    ".cjs",
    ".ts",
    ".tsx",
    ".jsx",
    ".json",
    ".jsonc",
    ".toml",
    ".yaml",
    ".yml",
}
FORBIDDEN_SITE_ESCAPES = (
    "../docs",
    "../prototypes",
    "../assets",
    "../intelligence",
    "../updates",
    "../tools",
)


def fail(message: str) -> None:
    print(f"REPOSITORY BOUNDARY FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for boundary in REQUIRED_BOUNDARIES:
        if not boundary.is_file():
            fail(f"missing boundary declaration: {boundary.relative_to(ROOT)}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        rel = path.relative_to(ROOT)

        if path.name.lower() in WRANGLER_NAMES and rel.parts[0] != "site":
            fail(f"Cloudflare Wrangler configuration must live under site/: {rel}")

        if rel.parts[0] != "site":
            continue

        if path.is_symlink():
            fail(f"deployable site may not contain symlinks: {rel}")

        if path.suffix.lower() not in DEPLOYABLE_TEXT_SUFFIXES:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for escape in FORBIDDEN_SITE_ESCAPES:
            if escape in text:
                fail(f"deployable site source escapes publication root via {escape}: {rel}")

    print("Repository publication/intelligence/update boundaries PASS")


if __name__ == "__main__":
    main()
