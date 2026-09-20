"""Standard-library tests; all game files are created in temporary directories."""
from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


init = load_module("miles_init", ROOT / "scripts/init_project.py")
checker = load_module("miles_validate", ROOT / "scripts/validate_skill.py")


class InitializerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.game = self.base / "game"
        self.game.mkdir()

    def create(self, **kwargs):
        return init.initialize(self.game, "test-game", "Test Game", **kwargs)

    def test_creates_exactly_two_empty_records(self):
        paths = self.create()
        self.assertEqual({p.name for p in paths}, set(init.TARGET_NAMES))
        self.assertEqual(len(list(self.game.iterdir())), 2)
        context = paths[0].read_text(encoding="utf-8")
        decisions = paths[1].read_text(encoding="utf-8")
        self.assertIn("Project ID: test-game", context)
        self.assertIn("No confirmed rules yet.", context)
        self.assertIn("No decisions recorded yet.", decisions)
        self.assertIn(str(self.game), context)
        self.assertNotIn("{{", context + decisions)
        for sample in ("WeChat", "360 × 800", "Paper Lantern", "fixed construction points"):
            self.assertNotIn(sample, context + decisions)

    def test_dry_run_creates_nothing(self):
        paths = self.create(dry_run=True)
        self.assertEqual(len(paths), 2)
        self.assertEqual(list(self.game.iterdir()), [])

    def test_dry_run_matches_actual_targets(self):
        self.assertEqual(self.create(dry_run=True), self.create())

    def test_repeat_run_refuses_and_preserves_bytes(self):
        paths = self.create()
        before = {p: p.read_bytes() for p in paths}
        with self.assertRaises(init.InitializationError):
            self.create()
        self.assertEqual(before, {p: p.read_bytes() for p in paths})

    def test_either_existing_target_prevents_both_writes(self):
        for name in init.TARGET_NAMES:
            with self.subTest(name=name):
                path = self.game / name
                path.write_text("valuable existing context", encoding="utf-8")
                with self.assertRaises(init.InitializationError):
                    self.create()
                self.assertEqual(path.read_text(), "valuable existing context")
                self.assertEqual(len(list(self.game.iterdir())), 1)
                path.unlink()

    def test_legacy_records_require_explicit_resolution(self):
        for name in init.LEGACY_NAMES:
            with self.subTest(name=name):
                path = self.game / name
                path.write_text("legacy authority", encoding="utf-8")
                with self.assertRaises(init.InitializationError):
                    self.create()
                self.assertEqual(list(self.game.iterdir()), [path])
                path.unlink()

    def test_existing_unrelated_files_are_preserved(self):
        readme = self.game / "README.md"
        readme.write_text("game docs", encoding="utf-8")
        self.create()
        self.assertEqual(readme.read_text(), "game docs")

    def test_missing_root_is_not_created(self):
        missing = self.base / "missing"
        with self.assertRaises(init.InitializationError):
            init.initialize(missing, "a-game", "A Game")
        self.assertFalse(missing.exists())

    def test_file_root_is_refused(self):
        path = self.base / "file.txt"
        path.write_text("x", encoding="utf-8")
        with self.assertRaises(init.InitializationError):
            init.initialize(path, "a-game", "A Game")

    def test_paths_with_spaces_and_unicode_name(self):
        root = self.base / "my game space"
        root.mkdir()
        result = init.initialize(root, "space-game", "Game Café")
        self.assertIn("Game Café", result[0].read_text(encoding="utf-8"))

    def test_invalid_identifiers_are_refused(self):
        for value in ("", "UPPER", "../other", "a b", "a--b", "-a", "a-", "a\nb", "a" * 65):
            with self.subTest(value=value), self.assertRaises(init.InitializationError):
                init.initialize(self.game, value, "Game")
        self.assertEqual(list(self.game.iterdir()), [])

    def test_invalid_names_are_refused(self):
        for value in ("", "  ", "Game\nInjected", "Game\x00", "x" * 161, "{{PROJECT_ID}}"):
            with self.subTest(value=value), self.assertRaises(init.InitializationError):
                init.initialize(self.game, "a-game", value)

    def test_skill_root_is_refused(self):
        with self.assertRaises(init.InitializationError):
            init.initialize(ROOT, "a-game", "A Game")

    def test_another_skill_directory_is_refused(self):
        (self.game / "SKILL.md").write_text("a skill", encoding="utf-8")
        with self.assertRaises(init.InitializationError):
            self.create()

    def test_skill_installation_descendant_is_refused(self):
        nested = self.base / ".agents" / "skills" / "other" / "data"
        nested.mkdir(parents=True)
        with self.assertRaises(init.InitializationError):
            init.initialize(nested, "a-game", "A Game")

    @unittest.skipUnless(hasattr(os, "symlink"), "Symlinks unavailable")
    def test_symlink_root_is_refused(self):
        link = self.base / "linked-game"
        try:
            link.symlink_to(self.game, target_is_directory=True)
        except OSError as exc:
            self.skipTest(str(exc))
        with self.assertRaises(init.InitializationError):
            init.initialize(link, "a-game", "A Game")
        self.assertEqual(list(self.game.iterdir()), [])

    @unittest.skipUnless(hasattr(os, "symlink"), "Symlinks unavailable")
    def test_broken_target_symlink_is_refused(self):
        path = self.game / init.TARGET_NAMES[0]
        missing = self.base / "elsewhere"
        try:
            path.symlink_to(missing)
        except OSError as exc:
            self.skipTest(str(exc))
        with self.assertRaises(init.InitializationError):
            self.create()
        self.assertTrue(path.is_symlink())
        self.assertFalse(missing.exists())

    def test_failed_second_creation_rolls_back_own_first_file(self):
        original_open = os.open

        def fail_second(path, *args, **kwargs):
            if Path(path).name == init.TARGET_NAMES[1]:
                raise PermissionError("simulated second-file failure")
            return original_open(path, *args, **kwargs)

        with patch.object(init.os, "open", side_effect=fail_second):
            with self.assertRaises(init.InitializationError):
                self.create()
        self.assertEqual(list(self.game.iterdir()), [])

    def test_concurrently_created_file_is_preserved(self):
        original_open = os.open
        external = self.game / init.TARGET_NAMES[1]

        def concurrent_writer(path, *args, **kwargs):
            if Path(path) == external and not external.exists():
                external.write_text("another process", encoding="utf-8")
            return original_open(path, *args, **kwargs)

        with patch.object(init.os, "open", side_effect=concurrent_writer):
            with self.assertRaises(init.InitializationError):
                self.create()
        self.assertEqual(external.read_text(), "another process")
        self.assertFalse((self.game / init.TARGET_NAMES[0]).exists())

    def test_missing_template_is_detected_before_writes(self):
        fake = self.base / "fake-skill"
        fake.mkdir()
        with patch.object(init, "SKILL_ROOT", fake):
            with self.assertRaises(init.InitializationError):
                self.create()
        self.assertEqual(list(self.game.iterdir()), [])

    def test_cli_dry_run(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/init_project.py"),
             "--project-root", str(self.game), "--project-id", "cli-game",
             "--project-name", "CLI Game", "--dry-run"],
            capture_output=True, text=True, timeout=10, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Would create", result.stdout)
        self.assertEqual(list(self.game.iterdir()), [])


class ValidatorTests(unittest.TestCase):
    def test_distribution_passes(self):
        self.assertEqual(checker.validate(ROOT), [])

    def copy_distribution(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        copied = Path(temporary.name) / checker.NAME
        shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        return copied

    def test_broken_local_link_is_detected(self):
        copied = self.copy_distribution()
        readme = copied / "README.md"
        readme.write_text(readme.read_text() + "\n[broken](missing-file.md)\n", encoding="utf-8")
        self.assertTrue(any("Broken local link" in e for e in checker.validate(copied)))

    def test_missing_required_file_is_detected(self):
        copied = self.copy_distribution()
        (copied / "references/onboarding.md").unlink()
        self.assertTrue(any("Missing file: references/onboarding.md" in e
                            for e in checker.validate(copied)))

    def test_malformed_eval_json_is_detected(self):
        copied = self.copy_distribution()
        (copied / "evals/scenarios.json").write_text("{", encoding="utf-8")
        self.assertTrue(any("Invalid evaluation JSON" in e for e in checker.validate(copied)))

    def test_mismatched_directory_name_is_detected(self):
        copied = self.copy_distribution()
        wrong = copied.with_name("wrong-name")
        copied.rename(wrong)
        self.assertTrue(any("name and parent directory" in e for e in checker.validate(wrong)))


if __name__ == "__main__":
    unittest.main()
