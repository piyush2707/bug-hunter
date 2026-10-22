#!/usr/bin/env python3
"""Lightweight structural checks for Bug Hunter's documented example fixtures."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "examples/python-early-return.md": ["return None", "Medium", "Suggested fix"],
    "examples/javascript-authz.md": ["ownerId", "High", "Important caveat"],
    "examples/python-retry-loop.md": ["while True", "Medium", "Suggested fix"],
}

def main():
    errors = []
    for relative, markers in EXPECTED.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Missing fixture: {relative}")
            continue
        content = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                errors.append(f"{relative}: missing expected marker {marker!r}")
    skill = ROOT / "skills/bug-hunter/SKILL.md"
    if not skill.is_file():
        errors.append("Missing skills/bug-hunter/SKILL.md")
    else:
        content = skill.read_text(encoding="utf-8")
        for marker in ("name: bug-hunter", "description:", "Required output", "Do not change files"):
            if marker not in content:
                errors.append(f"SKILL.md: missing expected marker {marker!r}")
    if errors:
        print("FAIL")
        print("\\n".join(f"- {error}" for error in errors))
        raise SystemExit(1)
    print(f"PASS: {len(EXPECTED)} example fixtures and skill structure validated.")

if __name__ == "__main__":
    main()
