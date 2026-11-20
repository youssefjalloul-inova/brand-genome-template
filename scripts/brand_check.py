#!/usr/bin/env python3
"""Brand check: runs on every pull request.

1. brand.json parses and has the required top-level keys.
2. Every fact id cited in brand.json exists, with a valid status.
3. Relative links in Markdown files point to files that exist.
4. Banned names/words don't appear in content (campaigns, kits, messages).
Exit code 1 on any failure.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []

# 1. brand.json
try:
    brand = json.loads((ROOT / "brand.json").read_text(encoding="utf-8"))
except Exception as e:  # noqa: BLE001
    print(f"brand.json does not parse: {e}")
    sys.exit(1)
for key in ["meta", "foundations", "lean_canvas", "blue_ocean", "corner", "story", "identity", "voice", "messages", "facts", "guardrails"]:
    if key not in brand:
        errors.append(f"brand.json: missing key '{key}'")

# 2. facts
valid = {"ready", "framed", "needs-source", "conflict"}
for f in brand.get("facts", []):
    if f.get("status") not in valid:
        errors.append(f"brand.json: fact {f.get('id')} has invalid status {f.get('status')}")

# 3. relative links
link = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
for md in ROOT.rglob("*.md"):
    if "node_modules" in md.parts:
        continue
    for target in link.findall(md.read_text(encoding="utf-8")):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (md.parent / target).exists():
            errors.append(f"{md.relative_to(ROOT)}: broken link -> {target}")

# 4. banned words in content that gets published
BANNED = [r"\brevolutionary\b", r"\bcutting-edge\b", r"\bgame-changer\b", r"in today's rapidly evolving", r"let's dive in"]  # add your own banned words
CONTENT = [ROOT / "10-library" / "campaigns", ROOT / "07-content-kits" / "social" / "hook-bank.md"]
for base in CONTENT:
    files = [base] if base.is_file() else list(base.rglob("*")) if base.exists() else []
    for f in files:
        if f.is_file() and f.suffix in {".md", ".txt", ".srt", ".json", ".html"}:
            text = f.read_text(encoding="utf-8", errors="ignore")
            for pat in BANNED:
                if re.search(pat, text, re.I):
                    errors.append(f"{f.relative_to(ROOT)}: banned term /{pat}/")

if errors:
    print("Brand check failed:\n- " + "\n- ".join(errors))
    sys.exit(1)
print("Brand check passed.")
