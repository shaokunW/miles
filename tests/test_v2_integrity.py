"""Deterministic V2 fixture/template integrity tests; no agent is executed."""
from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("miles_v2_validator", ROOT / "scripts/validate_skill.py")
assert spec is not None and spec.loader is not None
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class V2IntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / checker.NAME
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    def edit(self, name: str, old: str, new: str) -> None:
        path = self.root / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def edit_evals(self, action) -> None:
        path = self.root / "evals/scenarios.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        action(data)
        path.write_text(json.dumps(data), encoding="utf-8")

    def assert_error(self, fragment: str) -> None:
        self.assertTrue(any(fragment in e for e in checker.validate(self.root)), fragment)

    def test_clean_v2_package(self) -> None:
        self.assertEqual(checker.validate(self.root), [])

    def test_old_frontmatter_version_rejected(self) -> None:
        self.edit("SKILL.md", 'version: "2.0.0"', 'version: "1.1.0"')
        self.assert_error("Expected metadata.version 2.0.0")

    def test_missing_model_guide_rejected(self) -> None:
        (self.root / "references/experience-modeling.md").unlink()
        self.assert_error("Missing file: references/experience-modeling.md")

    def test_context_model_section_required(self) -> None:
        self.edit("templates/MILES_PROJECT_CONTEXT.md", "## Accepted experience model", "## Removed")
        self.assert_error("Missing template section ## Accepted experience model")

    def test_handoff_tracks_stay_separate(self) -> None:
        self.edit("templates/IMPLEMENTATION_HANDOFF.md", "## 6. Experience validation", "## Merged checks")
        self.assert_error("Missing template section ## 6. Experience validation")

    def test_declared_eval_count_matches(self) -> None:
        self.edit_evals(lambda d: d.update(case_count=999))
        self.assert_error("case_count must equal")

    def test_eval_release_matches(self) -> None:
        self.edit_evals(lambda d: d.update(package_version="1.1.0"))
        self.assert_error("package_version must match")

    def test_specs_keep_execution_status_honest(self) -> None:
        self.edit_evals(lambda d: d.update(execution_status="passed"))
        self.assert_error("retain not_run status")

    def test_duplicate_eval_ids_rejected(self) -> None:
        self.edit_evals(lambda d: d["cases"][-1].update(id=d["cases"][0]["id"]))
        self.assert_error("duplicate evaluation ID")

    def test_eval_expectations_are_text(self) -> None:
        self.edit_evals(lambda d: d["cases"][-1].update(expected=[17]))
        self.assert_error("entries must be nonempty strings")

    def test_external_tool_citation_rejected(self) -> None:
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n" + chr(0xe200) + "citation marker\n")
        self.assert_error("Tool-only citation marker")

    def test_link_escape_rejected(self) -> None:
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n[Escape](../outside.md)\n")
        self.assert_error("Link escapes package")


if __name__ == "__main__":
    unittest.main()
