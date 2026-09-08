#!/usr/bin/env python3
"""Fail closed when website publication, continuity, or repository residency boundaries drift."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MAX_CURRENT_STATE_BYTES = 3 * 1024
MAX_CURRENT_STATE_DISTANCE = 3

REQUIRED_BOUNDARIES = (
    ROOT / "site" / "README.txt",
    ROOT / "intelligence" / "README.txt",
    ROOT / "updates" / "README.txt",
)
FORBIDDEN_ENGINEERING_ROOTS = ("src", "tests")
FORBIDDEN_ENGINEERING_FILES = ("Ensemble.sln", "Directory.Build.props")
WRANGLER_NAMES = {"wrangler.toml", "wrangler.json", "wrangler.jsonc"}
DEPLOYABLE_TEXT_SUFFIXES = {".html", ".css", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".json", ".jsonc", ".toml", ".yaml", ".yml"}
FORBIDDEN_SITE_ESCAPES = ("../docs", "../prototypes", "../assets", "../intelligence", "../updates", "../tools")


def fail(message: str) -> None:
    print(f"REPOSITORY BOUNDARY FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8").strip()


def check_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    raw = path.read_bytes()
    if len(raw) > MAX_CURRENT_STATE_BYTES:
        fail(f"CURRENT_STATE.md exceeds 3 KiB: {len(raw)} bytes")
    try:
        state_commit = git("log", "-1", "--format=%H", "--", "CURRENT_STATE.md")
        distance = int(git("rev-list", "--count", f"{state_commit}..HEAD"))
    except (subprocess.CalledProcessError, ValueError) as exc:
        fail(f"cannot determine CURRENT_STATE.md currency: {exc}")
    if distance > MAX_CURRENT_STATE_DISTANCE:
        fail(f"CURRENT_STATE.md is stale by {distance} commits; maximum allowed is {MAX_CURRENT_STATE_DISTANCE}")


def check_residency() -> None:
    for root_name in FORBIDDEN_ENGINEERING_ROOTS:
        if (ROOT / root_name).exists():
            fail(f"engineering-native top-level workspace {root_name}/ belongs in Rylascoo/Ensemble-Project")
    for file_name in FORBIDDEN_ENGINEERING_FILES:
        if (ROOT / file_name).exists():
            fail(f"engineering-native root file {file_name} belongs in Rylascoo/Ensemble-Project")


def main() -> None:
    check_current_state()
    check_residency()

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

    print("Repository publication/continuity/residency boundaries PASS")
    print("CURRENT_STATE_CAP=PASS")
    print("CURRENT_STATE_CURRENCY=PASS")
    print("CROSS_REPOSITORY_RESIDENCY=PASS")


if __name__ == "__main__":
    main()
