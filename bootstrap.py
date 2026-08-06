#!/usr/bin/env python3
"""Initialize a project coordination workspace without inventing project state."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CURRENT_PATH = ROOT / ".ai" / "CURRENT.md"
README_PATH = ROOT / "README.md"


def prompt(label: str, default: str | None = None, required: bool = False) -> str:
    while True:
        suffix = f" [default: {default}]" if default else ""
        value = input(f"{label}{suffix}: ").strip()
        if value:
            return value
        if default is not None:
            return default
        if not required:
            return ""
        print(f"{label} is required.", file=sys.stderr)


def absolute_workspace_path(value: str) -> str:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = ROOT / path
    return str(path.resolve(strict=False))


def yaml_scalar(value: str | None) -> str:
    return "null" if value is None or value == "" else json.dumps(value)


def render_current(
    project_name: str,
    repository_directory: str,
) -> str:
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")

    return f'''---
schema_version: 3
updated_at: {yaml_scalar(timestamp)}
updated_by: "bootstrap"
repository_state: setup_required
active_initiative: null
active_task: null
last_completed_task: null
next_task: null
repository_directory: {yaml_scalar(repository_directory)}
branch: null
verified_commit: null
verification_commands: []
---

# Current state

The coordination workspace for `{project_name}` is configured but has no
verified implementation checkpoint. No implementation or verification result
is claimed.

## Next action

Ask an agent to initialize the project according to `AGENTS.md`. Supply the
project goal, constraints, authoritative references, and any already-made
decisions. If the implementation repository has no commit, leave
`verified_commit` as `null` until the first coherent task is committed and
verified.

## Configuration

- Repository directory: `{repository_directory}`

## Blockers

No configuration blocker is recorded.

## Pending decisions

- Project goals and initial initiative are not recorded.

## Known issues

None recorded.

## Unverified

- No implementation commit has been verified.
- All implementation behavior is unverified.
'''


def render_project_readme(
    project_name: str,
    description: str,
    repository_directory: str,
) -> str:
    summary = description or "No project description has been recorded yet."
    return f'''# 🧭 {project_name} workspace

> {summary}

This workspace keeps plans, decisions, current state, and AI handoffs together
without mixing them into the implementation repository.

## 📍 Current setup

| Item | Value |
| --- | --- |
| Repository directory | `{repository_directory}` |
| Live project state | `.ai/CURRENT.md` |

## 🚀 Resume the project

1. Review `.ai/CURRENT.md`.
2. Start an AI agent from this workspace root.
3. Ask:

   > Initialize this project according to `AGENTS.md` and tell me what you need
   > before implementation begins.

> [!NOTE]
> Until a real implementation commit has been verified, the workspace remains
> in initialization mode and does not claim that anything was completed.

## 🗂️ Key files

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Agent workflow and recording rules |
| `.ai/CURRENT.md` | Latest state, blockers, and next action |
| `.ai/ROADMAP.md` | Authorized project direction |
| `.ai/initiatives/` | Active and completed plans |
| `.ai/decisions/` | Durable decisions and rationale |
| `.ai/README.md` | State model and sources of truth |

## 🔌 Connect the codebase

The `{repository_directory}` directory may contain a regular clone, Git
submodule, or symlink to an existing checkout. The workspace and codebase keep
independent Git histories: project context stays here; implementation changes
stay with the code.

Bootstrap does not create, clone, link, or modify the implementation
repository. Record branch and verification details in `.ai/CURRENT.md` when
they are known.
'''


def print_completion_summary(
    project_name: str,
    description: str,
    repository_directory: str,
) -> None:
    description_value = description or "not provided"
    absolute_repository_directory = absolute_workspace_path(repository_directory)

    print("\nWorkspace configuration saved:")
    print(
        f"- Project name: {project_name} "
        "(stored in README.md and .ai/CURRENT.md)"
    )
    print(f"- Project description: {description_value} (stored in README.md)")
    print(
        f"- Repository directory: {repository_directory} "
        "(stored in README.md and .ai/CURRENT.md)"
    )
    print(
        f"- Absolute directory on this machine: {absolute_repository_directory} "
        "(derived from the workspace location; not stored)"
    )
    print("\nCurrent status:")
    print("- Workspace details are recorded.")
    print("- Repository setup and project planning have not started.")

    print("\nWhat you need to do next:")
    print("- Review README.md and .ai/CURRENT.md; update them if needed.")
    print(
        "- Link an existing checkout with a symlink, or add the repository as a "
        "Git submodule inside the recorded repository directory."
    )
    print(
        "- Keep this workspace separate from the codebase. It can remain its own "
        "repository and serve as the project tracker for plans, decisions, "
        "state, and handoffs."
    )
    print("- Start an AI agent from this workspace directory.")
    print(
        '- Ask: "Initialize this project according to AGENTS.md and tell me what '
        'you need before implementation begins."'
    )

    print("\nWhat the AI agent needs to do next:")
    print("- Read AGENTS.md and .ai/CURRENT.md.")
    print("- Inspect or prepare the implementation repository when authorized.")
    print("- Ask for missing goals, constraints, references, and decisions.")
    print("- Prepare the roadmap and first implementation task.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Configure a project workspace without creating project history."
    )
    parser.add_argument("--project-name")
    parser.add_argument("--description", default=None)
    parser.add_argument(
        "--repository-directory",
        default=None,
        help="Workspace directory for the project repository. Defaults to 'repos'.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an already configured setup_required workspace.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    current = CURRENT_PATH.read_text(encoding="utf-8")
    already_configured = 'updated_by: "bootstrap"' in current
    if already_configured and not args.force:
        print(
            "Workspace was already bootstrapped. Use --force only after reviewing "
            "the existing state.",
            file=sys.stderr,
        )
        return 2

    interactive = sys.stdin.isatty()
    if not args.project_name and not interactive:
        print("--project-name is required in non-interactive mode.", file=sys.stderr)
        return 2

    if interactive:
        print("\n1. Project name")
        project_name = args.project_name or prompt("Your answer", required=True)

        print("\n2. Project description")
        description = (
            args.description
            if args.description is not None
            else prompt("Your answer", required=False)
        )

        print("\n3. Directory for the project repository")
        print(
            "- This directory lives inside the workspace and is where the "
            "project repository will reside."
        )
        print(
            "- Use a familiar name such as repos, apps, codebase, or projects."
        )
        repository_directory = args.repository_directory or prompt(
            "Your answer", default="repos"
        )
    else:
        project_name = args.project_name
        description = args.description or ""
        repository_directory = args.repository_directory or "repos"

    for directory in (
        ROOT / ".ai" / "initiatives" / "active",
        ROOT / ".ai" / "initiatives" / "completed",
        ROOT / ".ai" / "decisions",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    CURRENT_PATH.write_text(
        render_current(
            project_name,
            repository_directory,
        ),
        encoding="utf-8",
    )
    README_PATH.write_text(
        render_project_readme(
            project_name,
            description,
            repository_directory,
        ),
        encoding="utf-8",
    )

    print_completion_summary(
        project_name,
        description,
        repository_directory,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
