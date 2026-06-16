# Workflow

## Purpose

Entry to the standard agent session loop for this repository.

## Session Loop

Follow [../agent/work-loop.md](../agent/work-loop.md). Summary:
1. Read current state and blockers.
2. Take user-named task or first open blocker.
3. Write [../execution/active-session.md](../execution/active-session.md).
4. Load one skill; read named files.
5. Update contracts, implement slice, test, verify, hand off.

## Modes

**Empty repo:** kit files are the whole repo until bootstrap.

**Existing project:** install kit at root; do not delete existing source unless
a task names integration paths.

## Verification

`python scripts/check-all.py` per [../operations/verification.md](../operations/verification.md).

## Commits

[commit-protocol.md](commit-protocol.md) when git is available.
