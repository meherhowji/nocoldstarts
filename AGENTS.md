# Project workspace instructions

## Purpose

This repository coordinates work on one implementation repository. The
coordination workspace is authoritative for plans, handoffs, and durable
decision rationale. The implementation repository is authoritative for code,
tests, and committed implementation history.

The repository directory, branch information, verification commands, and latest
verified commit are recorded in `.ai/CURRENT.md`.

## Recording policy

- Preserve the smallest set of facts needed to continue the project; do not
  reproduce session transcripts.
- Agents may summarize user direction, completed work, directly observed
  repository state, and verification they actually performed.
- Do not invent facts, decisions, commitments, dates, schedules, verification
  results, or rationale. Unknown information remains unknown.
- Identify material statements as user direction, an agent implementation
  choice within authorized scope, direct observation, or reconstruction from
  Git. Label reconstructions explicitly.
- Do not add, remove, reorder, or reschedule project commitments unless the user
  made that decision. An agent may decompose an authorized task without
  changing its scope or intent.

## Start every session

1. Read `.ai/README.md`.
2. Read `.ai/CURRENT.md`.
3. If an active initiative exists, read its `PLAN.md`.
4. Inspect the coordination repository status.
5. If the implementation repository exists, inspect its branch, commit, staged,
   unstaged, and untracked state without modifying it.
6. Reconcile observed state with `.ai/CURRENT.md` before editing.
7. Restate the last completed task, next task and readiness, blockers, pending
   decisions, and unverified behavior.

## Initialization mode

Initialization mode applies when `repository_state` is `setup_required`, the
implementation repository does not exist, or `verified_commit` is `null`.

The absence of an implementation commit is valid. It does not authorize the
agent to invent history or describe planned work as completed.

During initialization, an agent may:

- record project goals, constraints, priorities, and references supplied by the
  user;
- record facts directly observed from existing files, tools, or Git;
- create the first roadmap and initiative plan from authorized scope;
- identify decisions the user still needs to make;
- prepare the implementation repository or its first atomic task when asked.

During initialization, an agent must not:

- claim that implementation or verification occurred when it did not;
- invent a commit, branch, deadline, requirement, task order, or decision;
- set `repository_state: stable` without a completed, verified implementation
  checkpoint;
- treat generated scaffolding as accepted product scope unless the user
  authorized it.

If the implementation repository has no commit, leave `verified_commit: null`.
After the first coherent implementation task is committed and verified, record
that exact commit as the first stable checkpoint.

## Task readiness and atomic work

- Work on one atomic implementation task at a time.
- An unchecked plan item is not automatically ready. Apply the readiness fields
  defined by the active initiative plan.
- If a material product, design, content, or scope choice is missing, record it
  as pending and request user direction.
- Split work that cannot be completed, verified, and committed coherently
  without expanding its authorized scope.
- Never discard unexpected partial work without inspecting it first.

## Verification

Use the verification commands recorded in `.ai/CURRENT.md` and any additional
checks required by the active task. Record only commands actually run and their
observed outcomes. State failures, skipped checks, and unverified behavior
explicitly.

If no verification commands are recorded, do not invent them. Determine them
from authoritative project configuration or obtain user direction before
claiming a verified checkpoint.

## Completing a task and handing off

1. Complete the atomic task and its acceptance criteria.
2. Run and record relevant verification.
3. Show the final implementation diff summary and obtain user approval before
   committing or pushing, unless approval was already explicit.
4. Commit and push the implementation repository first.
5. Update the active `PLAN.md` and `.ai/CURRENT.md` with the exact commit,
   verification evidence, blockers, pending decisions, known issues, unverified
   behavior, and next unstarted task.
6. Commit the coordination checkpoint, including any implementation repository
   pointer when one is used, and push it.
7. Confirm both repositories are clean and synchronized.
8. Report the completed task, commit, checks, next task, blockers, pending
   decisions, and unverified items. Do not begin the next task.

A normal handoff requires:

- `repository_state: stable`
- `active_task: null`
- a completed and verified implementation commit
- a named next unstarted task, or an explicit record that none is authorized
- clean and pushed repositories

## Interrupted-work recovery

Inspect all partial state without discarding or overwriting it. If the
interrupted task can safely be completed as one coherent task, finish and
verify it before preparing a normal handoff. Otherwise set
`repository_state: recovery_required`, document the exact partial state and
safest next action, and stop for user direction.

## Repository boundaries

- Keep coordination records out of implementation repositories unless the
  user deliberately chose an embedded workspace.
- Do not add secrets, credentials, private transcripts, or unnecessary machine
  paths to either repository.
- Do not modify repositories outside the recorded repository directory unless
  the user explicitly expands scope.
- Do not force-push commits pinned by a coordination checkpoint.
