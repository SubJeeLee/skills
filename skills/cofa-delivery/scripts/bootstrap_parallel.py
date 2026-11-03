#!/usr/bin/env python3
"""Prepare local file-based coordination. Never launch agents or overwrite files."""

import argparse
from pathlib import Path
import sys


SKILL = Path(__file__).resolve().parents[1]
ASSETS = SKILL / "assets" / "parallel"
OUTPUTS = {
    "coordination.md": "coordination.md",
    "templates/task.md": "task.md",
    "templates/report.md": "report.md",
    "prompts/main.md": "main-prompt.md",
    "prompts/worker.md": "worker-prompt.md",
}
DIRECTORIES = ("tasks", "reports", "snapshots", "templates", "prompts")


def bootstrap(project_root):
    root = Path(project_root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("project-root must be an existing project directory")
    if root == SKILL or root.is_relative_to(SKILL):
        raise ValueError("use a task project, not the installed skill directory")
    destination = root / ".cofa"
    directories = [destination, *(destination / item for item in DIRECTORIES)]
    files = [destination / item for item in OUTPUTS]
    for path in [*directories, *files]:
        if path.is_symlink():
            raise ValueError(f"refusing symlink: {path}")
        if path.exists() and (path in directories) != path.is_dir():
            raise ValueError(f"unexpected path type: {path}")
        if path.exists() and path in files and not path.is_file():
            raise ValueError(f"expected regular file: {path}")
    # Load every resource before creating anything, including standalone installs.
    contents = {
        target: (ASSETS / source).read_text(encoding="utf-8")
        .replace("{{PROJECT_ROOT}}", str(root))
        .replace("{{SKILL_FILE}}", str(SKILL / "SKILL.md"))
        for target, source in OUTPUTS.items()
    }
    for path in directories:
        path.mkdir(exist_ok=True)
    created, preserved = [], []
    for target, content in contents.items():
        path = destination / target
        try:
            with path.open("x", encoding="utf-8") as handle:
                handle.write(content)
        except FileExistsError:
            preserved.append(str(path))
        else:
            created.append(str(path))
    return destination, created, preserved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    args = parser.parse_args()
    try:
        destination, created, preserved = bootstrap(args.project_root)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    for path in created:
        print(f"CREATED {path}")
    for path in preserved:
        print(f"PRESERVED {path}")
    print(f"NEXT: main fills {destination / 'coordination.md'} and tasks/R01.md.")
    print(f"WORKER PROMPT: {destination / 'prompts' / 'worker.md'}")
    print("No sessions launched; sharing not verified; no tools installed or task work completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
