# Work Loop

## Purpose

The session loop from first read to handoff.

## The Loop

1. Read [../current-state.md](../current-state.md).
2. Take the user-named task or first open blocker in
   [../execution/current-blockers.md](../execution/current-blockers.md).
3. Write the active task to [../execution/active-session.md](../execution/active-session.md).
4. Load one matching skill from [skills/README.md](skills/README.md).
5. Read files named by the task and skill.
6. Update or create contracts before source changes.
7. Implement the narrowest slice.
8. Add or update tests.
9. Run the focused gate.
10. Update current state, traceability, blocker, task, and done log.
11. Run pre-handoff checks (`python scripts/check-all.py` when docs/scripts change).
12. Hand off with evidence and the next executable step per [handoff.md](handoff.md).

## Discipline

One blocker per session unless trivially coupled. Contradictions become the
first task. Never leave the next task undefined.
