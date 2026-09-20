#!/usr/bin/env python3
"""Package-specific validation for Miles, using Python 3.10+ standard library.

Checks local structure and this package's simple metadata convention. It is
not a general YAML parser or official Agent Skills validator. Does not fetch
external URLs, resolve Markdown anchors, run agents, or prove behavioral quality.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Sequence
from urllib.parse import unquote, urlsplit

NAME = "miles-game-experience-designer"
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md", "README.md", "agents/openai.yaml", "CHANGELOG.md",
    "references/project-context.md", "references/player-experience.md",
    "references/onboarding.md", "references/interaction-and-feedback.md",
    "references/loops-progression-and-pacing.md", "references/decisions-and-validation.md",
    "references/foundations.md", "references/sources.md", "examples/README.md",
    "examples/classics/super-mario-bros-1-1.md", "examples/classics/portal-companion-cube.md",
    "examples/classics/breath-of-the-wild.md", "examples/classics/journey.md",
    "examples/classics/into-the-breach.md", "examples/classics/factorio.md",
    "examples/worked/first-expansion.md", "examples/worked/context-lifecycle.md",
    "examples/worked/tactical-ui-review.md", "templates/MILES_PROJECT_CONTEXT.md",
    "templates/MILES_DECISIONS.md", "templates/DESIGN_BRIEF.md", "templates/PLAYTEST_PLAN.md",
    "templates/AGENTS_SNIPPET.md", "scripts/init_project.py", "scripts/validate_skill.py",
    "tests/test_init_project.py", "evals/scenarios.json", "evals/README.md",
)
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def _outside_fences(text: str) -> str:
    output: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            output.append(line)
    return "\n".join(output)


def validate(root: Path) -> list[str]:
    """Return human-readable integrity errors without changing the package."""
    root = root.resolve()
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"Missing file: {relative}")
    skill = root / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append("SKILL.md requires opening YAML frontmatter.")
        else:
            front = parts[1]
            name = re.search(r"^name:\s*(\S+)\s*$", front, re.M)
            desc = re.search(r"^description: (.+)$", front, re.M)
            version = re.search(r'^  version: "([^"]+)"$', front, re.M)
            if not name or name.group(1) != NAME or root.name != NAME:
                errors.append("Skill name and parent directory must match the package name.")
            if not desc or not (1 <= len(desc.group(1)) <= 1024):
                errors.append("Description must be a nonempty single line of at most 1024 characters.")
            if not version or version.group(1) != "1.0.0":
                errors.append("Expected metadata.version 1.0.0 in the package convention.")
        if len(text.splitlines()) >= 500:
            errors.append("Keep SKILL.md below 500 lines.")

    ui = root / "agents/openai.yaml"
    if ui.is_file():
        text = ui.read_text(encoding="utf-8")
        if not text.startswith("interface:\n"):
            errors.append("UI metadata requires an interface mapping.")
        fields: dict[str, str] = {}
        for key in ("display_name", "short_description", "default_prompt"):
            match = re.search(rf'^  {key}: (".*")$', text, re.M)
            try:
                value = json.loads(match.group(1)) if match else ""
            except (ValueError, TypeError):
                value = ""
            if not isinstance(value, str) or not value.strip():
                errors.append(f"Missing or invalid UI field: {key}")
            else:
                fields[key] = value
        if "$" + NAME not in fields.get("default_prompt", ""):
            errors.append("Default prompt must explicitly reference the skill name.")

    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if "\ue200" in text or "\ue201" in text:
            errors.append(f"Tool-only citation marker in {path.relative_to(root)}")
        for match in LINK.finditer(_outside_fences(text)):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if root != resolved and root not in resolved.parents:
                errors.append(f"Link escapes package: {path.relative_to(root)} -> {target}")
            elif not resolved.exists():
                errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")

    for name in ("MILES_PROJECT_CONTEXT.md", "MILES_DECISIONS.md"):
        path = root / "templates" / name
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for token in ("{{PROJECT_ID}}", "{{PROJECT_NAME}}", "{{CREATED_DATE}}"):
                if token not in text:
                    errors.append(f"Missing template field {token}: {name}")

    eval_path = root / "evals/scenarios.json"
    if eval_path.is_file():
        try:
            data = json.loads(eval_path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            errors.append(f"Invalid evaluation JSON: {exc}")
        else:
            cases = data.get("cases") if isinstance(data, dict) else None
            if not isinstance(cases, list) or len(cases) < 12:
                errors.append("Provide at least 12 behavioral evaluation cases.")
            else:
                seen: set[str] = set()
                for case in cases:
                    if not isinstance(case, dict):
                        errors.append("Evaluation cases must be objects.")
                        continue
                    ident = case.get("id", "")
                    if not isinstance(ident, str) or not ident or ident in seen:
                        errors.append(f"Missing or duplicate evaluation ID: {ident}")
                    if isinstance(ident, str):
                        seen.add(ident)
                    for key in ("title", "prompt", "setup", "expected", "critical_failures"):
                        if not case.get(key):
                            errors.append(f"Evaluation {ident} needs {key}.")
                    if not isinstance(case.get("expected"), list):
                        errors.append(f"Evaluation {ident}: expected must be a list.")
                    if not isinstance(case.get("critical_failures"), list):
                        errors.append(f"Evaluation {ident}: critical_failures must be a list.")
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Path to the Miles skill directory.")
    args = parser.parse_args(argv)
    try:
        errors = validate(args.root)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Validation could not complete: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(REQUIRED)} required files, metadata, local-file links, templates, and eval fixtures.")
    print("External URL availability and live agent behavior are outside this check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
