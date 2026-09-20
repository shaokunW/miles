#!/usr/bin/env python3
"""Create blank Miles records in an explicitly selected game project.

Python 3.10+, standard library only. Existing files are never overwritten.
This initializes files; it does not infer project facts or implement agent memory.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence

SKILL_ROOT = Path(__file__).resolve().parents[1]
TARGET_NAMES = ("MILES_PROJECT_CONTEXT.md", "MILES_DECISIONS.md")
LEGACY_NAMES = ("PROJECT_CONTEXT.md", "DECISIONS.md")
ID_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
TOKEN_PATTERN = re.compile(r"\{\{[A-Z_]+\}\}")


class InitializationError(RuntimeError):
    """A precondition or safe creation requirement could not be satisfied."""


def _validate_identity(project_id: str, project_name: str) -> None:
    if len(project_id) > 64 or not ID_PATTERN.fullmatch(project_id):
        raise InitializationError(
            "Project ID must be 1–64 lowercase letters/digits separated by single hyphens."
        )
    if not project_name.strip() or len(project_name) > 160:
        raise InitializationError("Project name must contain 1–160 characters.")
    if any(ord(c) < 32 or ord(c) == 127 for c in project_name):
        raise InitializationError("Project name must be a single line without control characters.")
    if TOKEN_PATTERN.search(project_name):
        raise InitializationError("Project name cannot contain template placeholder tokens.")


def _project_root(value: str | Path) -> Path:
    supplied = Path(value).expanduser()
    if any(ord(c) < 32 or ord(c) == 127 for c in str(supplied)):
        raise InitializationError("Project root cannot contain control characters.")
    if supplied.is_symlink():
        raise InitializationError("Supply the actual project directory, not a symlink root.")
    try:
        root = supplied.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise InitializationError(f"Project root must already exist: {supplied}") from exc
    if not root.is_dir():
        raise InitializationError(f"Project root must be a directory: {root}")
    skill_root = SKILL_ROOT.resolve()
    if root == skill_root or skill_root in root.parents:
        raise InitializationError("Game records belong outside this reusable skill directory.")
    pairs = set(zip(root.parts, root.parts[1:]))
    if (".agents", "skills") in pairs or (".codex", "skills") in pairs:
        raise InitializationError("Select the game root, outside a skill installation directory.")
    if (root / "SKILL.md").exists():
        raise InitializationError("This directory contains SKILL.md; select the active game root.")
    return root


def initialize(
    project_root: str | Path,
    project_id: str,
    project_name: str,
    *,
    dry_run: bool = False,
) -> list[Path]:
    """Validate the root and create the two templates, or preview their paths.

    On a handled creation failure, remove only files this call created whose
    inode identity is unchanged. No cross-file transaction or crash recovery is
    guaranteed. Existing files, including symlinks, are always refused.
    """
    _validate_identity(project_id, project_name)
    root = _project_root(project_root)
    for name in (*TARGET_NAMES, *LEGACY_NAMES):
        if os.path.lexists(root / name):
            raise InitializationError(
                f"Existing record found: {root / name}. Read and reuse the project's "
                "authoritative records; resolve migration explicitly. Nothing was overwritten."
            )

    values = {
        "{{PROJECT_ID}}": project_id,
        "{{PROJECT_NAME}}": project_name.strip(),
        "{{PROJECT_ROOT}}": str(root),
        "{{CREATED_DATE}}": datetime.now().astimezone().date().isoformat(),
    }
    rendered: dict[Path, str] = {}
    for name in TARGET_NAMES:
        template = SKILL_ROOT / "templates" / name
        try:
            text = template.read_text(encoding="utf-8")
        except OSError as exc:
            raise InitializationError(f"Cannot read template: {template}: {exc}") from exc
        for token, value in values.items():
            text = text.replace(token, value)
        if TOKEN_PATTERN.search(text):
            raise InitializationError(f"Unresolved placeholder in template: {template}")
        rendered[root / name] = text

    targets = list(rendered)
    if dry_run:
        return targets

    created: list[tuple[Path, int, int]] = []
    try:
        for path, text in rendered.items():
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
            stat = os.fstat(fd)
            created.append((path, stat.st_dev, stat.st_ino))
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
                stream.write(text)
                stream.flush()
                os.fsync(stream.fileno())
    except OSError as exc:
        cleanup_errors: list[str] = []
        for path, device, inode in reversed(created):
            try:
                current = path.lstat()
                if (current.st_dev, current.st_ino) == (device, inode):
                    path.unlink()
            except FileNotFoundError:
                pass
            except OSError as cleanup_exc:
                cleanup_errors.append(f"{path}: {cleanup_exc}")
        detail = ""
        if cleanup_errors:
            detail = " Inspect partial files; cleanup failed: " + "; ".join(cleanup_errors)
        raise InitializationError(f"Creation failed: {exc}.{detail}") from exc
    return targets


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True,
                        help="Existing active game directory, outside the skill installation.")
    parser.add_argument("--project-id", required=True, help="Stable lowercase project identifier.")
    parser.add_argument("--project-name", required=True, help="Single-line display name.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and preview; create nothing.")
    args = parser.parse_args(argv)
    try:
        paths = initialize(args.project_root, args.project_id, args.project_name,
                           dry_run=args.dry_run)
    except InitializationError as exc:
        parser.error(str(exc))
    verb = "Would create" if args.dry_run else "Created"
    for path in paths:
        print(f"{verb}: {path}")
    print("No gameplay facts inferred. Existing records were not modified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
