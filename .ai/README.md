# AI coordination workspace

This directory preserves enough verified state for a human or AI agent to
continue project work without access to an earlier conversation.

## Reading order

1. `../AGENTS.md`
2. `CURRENT.md`
3. The active initiative's `PLAN.md`, when one exists
4. Relevant records in `decisions/`
5. Initiative notes only when additional context exists

## Sources of truth

- Implementation: the repository found through the directory recorded in
  `CURRENT.md`
- Verified implementation checkpoint: `CURRENT.md.verified_commit`
- Current handoff or initialization state: `CURRENT.md`
- Initiative scope, readiness, and task status: the active `PLAN.md`
- Long-range authorized direction: `ROADMAP.md`
- Durable rationale: `decisions/`
- Historical implementation and coordination changes: Git

When documentation conflicts with Git, Git wins for repository facts. Reconcile
the documentation before continuing.

## State lifecycle

- `setup_required`: configuration, planning, repository creation, or the first
  verified implementation checkpoint is incomplete.
- `stable`: the latest completed implementation task is committed, verified,
  recorded, and clean at handoff.
- `recovery_required`: interrupted or ambiguous partial implementation must be
  reconciled before normal work continues.

`CURRENT.md` is a replaceable snapshot, not a journal. Initiative plans preserve
task completion, decision records preserve durable rationale, and Git preserves
history.

A stable implementation may still have a blocked or under-specified next task.
Record blockers, pending decisions, known issues, and unverified behavior
separately.

## Initiative lifecycle

Create an initiative only from authorized scope. Active initiatives live under
`initiatives/active/<id-name>/`. A plan should contain its objective, task
status, current task readiness, exit criteria, and explicitly excluded scope.

After the initiative's exit criteria are satisfied, move it to
`initiatives/completed/` and update `ROADMAP.md` and `CURRENT.md`.
