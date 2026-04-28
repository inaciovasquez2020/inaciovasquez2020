#!/usr/bin/env python3
from pathlib import Path
import re

p = Path("docs/status/LEAN_PROOF_PORTFOLIO_CLASSIFICATION.md")
if not p.exists():
    raise SystemExit("missing docs/status/LEAN_PROOF_PORTFOLIO_CLASSIFICATION.md")

text = p.read_text(encoding="utf-8")

required = [
    "Portfolio class:",
    "Allowed description",
    "Forbidden description",
    "Classification rule",
    "Public sentence",
    "must not be described",
]

for needle in required:
    if needle not in text:
        raise SystemExit(f"missing required classification phrase: {needle}")

m = re.search(r"Portfolio class:\s+\*\*(.+?)\*\*", text)
if not m:
    raise SystemExit("missing portfolio class value")

if m.group(1) != "INFRASTRUCTURE_DOCUMENTATION":
    raise SystemExit("profile repo must be classified as INFRASTRUCTURE_DOCUMENTATION")

print("lean proof portfolio classification: PASS")
