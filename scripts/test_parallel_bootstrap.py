#!/usr/bin/env python3
"""Exercise file preparation in disposable projects; never call models or COFA."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "cofa-delivery"


def run_bootstrap(skill, project):
    return subprocess.run(
        [sys.executable, str(skill / "scripts" / "bootstrap_parallel.py"),
         "--project-root", str(project)],
        capture_output=True, text=True,
    )


def file_bytes(directory):
    return {str(path.relative_to(directory)): path.read_bytes()
            for path in directory.rglob("*") if path.is_file()}


class ParallelBootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="cofa-parallel-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.project = self.base / "프로젝트 with spaces"
        self.project.mkdir()

    def test_creates_coordination_without_changing_product_or_starting_work(self):
        product = self.project / "app.py"
        product.write_text("print('existing product')\n", encoding="utf-8")
        result = run_bootstrap(SKILL, self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        cofa = self.project / ".cofa"
        self.assertEqual(len(file_bytes(cofa)), 5)
        self.assertEqual(list((cofa / "tasks").iterdir()), [])
        self.assertEqual(list((cofa / "reports").iterdir()), [])
        self.assertEqual(product.read_text(), "print('existing product')\n")
        for content in file_bytes(cofa).values():
            self.assertNotIn(b"{{PROJECT_ROOT}}", content)
            self.assertNotIn(b"{{SKILL_FILE}}", content)
        self.assertIn(str(self.project.resolve()),
                      (cofa / "prompts" / "main.md").read_text())

    def test_repeat_preserves_edits_assignments_and_completed_reports(self):
        self.assertEqual(run_bootstrap(SKILL, self.project).returncode, 0)
        cofa = self.project / ".cofa"
        (cofa / "coordination.md").write_text("Human-reviewed project state\n")
        (cofa / "tasks" / "R01.md").write_text("Assigned implementation\n")
        (cofa / "reports" / "R01.md").write_text("Finished report\n")
        before = file_bytes(self.project)
        result = run_bootstrap(SKILL, self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(file_bytes(self.project), before)

    def test_standalone_project_skill_install_has_no_sibling_dependency(self):
        installed = self.project / ".agents" / "skills" / "cofa-delivery"
        shutil.copytree(SKILL, installed)
        result = run_bootstrap(installed, self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        worker = (self.project / ".cofa" / "prompts" / "worker.md").read_text()
        self.assertIn(str(installed / "SKILL.md"), worker)
        self.assertTrue((self.project / ".cofa" / "templates" / "task.md").is_file())

    def test_rejects_symlink_destinations_without_writing_outside_project(self):
        for relative in (".cofa", ".cofa/prompts", ".cofa/coordination.md"):
            with self.subTest(relative=relative):
                case = self.base / relative.replace("/", "-").replace(".", "")
                case.mkdir()
                target = self.base / (case.name + "-external")
                target.mkdir()
                sentinel = target / "sentinel.txt"
                sentinel.write_text("preserve\n")
                link = case / relative
                link.parent.mkdir(parents=True, exist_ok=True)
                link.symlink_to(target, target_is_directory=True)
                result = run_bootstrap(SKILL, case)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(file_bytes(target), {"sentinel.txt": b"preserve\n"})
                self.assertFalse((case / ".cofa" / "tasks").exists())

    def test_rejects_path_type_conflict_before_creating_other_files(self):
        conflict = self.project / ".cofa" / "coordination.md"
        conflict.mkdir(parents=True)
        result = run_bootstrap(SKILL, self.project)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(conflict.is_dir())
        self.assertFalse((self.project / ".cofa" / "tasks").exists())

    def test_missing_resource_fails_before_creating_coordination(self):
        installed = self.base / "incomplete-skill"
        shutil.copytree(SKILL, installed)
        (installed / "assets" / "parallel" / "worker-prompt.md").unlink()
        result = run_bootstrap(installed, self.project)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.project / ".cofa").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
