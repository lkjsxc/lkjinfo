# Skill: Maintenance

## Purpose

Update the lkjinfo instruction system: docs, skills, scripts, templates.

## Trigger

Stale docs, check gaps, line-cap pressure, or repeated agent friction.

## Context

- [../../agent/maintenance.md](../../agent/maintenance.md)
- [../../repository/line-limits.md](../../repository/line-limits.md)
- [../../operations/verification.md](../../operations/verification.md)
- [../../../scripts/check-all.py](../../../scripts/check-all.py)

## Procedure

1. Identify the defect or friction with evidence.
2. Fix docs, split files, or extend checks in one verified slice.
3. Update README tables of contents for touched directories.
4. Run full `python scripts/check-all.py`.
5. Record change in done-log if task-bound.

## Checks

`python scripts/check-all.py`

## Must Not

Weaken honest-state rules. Add files over 50 lines. Skip gate evidence.

## Handoff

What was fixed, checks added, gate output.
