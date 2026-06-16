# Skill: Refactor

## Purpose

Behavior-preserving structural changes under the 50-line cap.

## Trigger

Code structure must change without changing observable behavior.

## Context

- [../../repository/refactor-policy.md](../../repository/refactor-policy.md)
- [../../repository/line-limits.md](../../repository/line-limits.md)
- [../../architecture/source-map.md](../../architecture/source-map.md)

## Procedure

1. Confirm contracts allow the structural change only.
2. Run existing focused tests before edits.
3. Refactor in small steps; split files approaching 50 lines.
4. Update source-map and contracts if paths change.
5. Re-run same tests; behavior must match prior evidence.

## Checks

Pre and post focused tests. `python scripts/check-lines.py`

## Must Not

Change behavior or scope without a new task. Leave files over 50 lines.

## Handoff

Tests run, files split, contracts updated, gate output.
