# Skill: Implementation Slice

## Purpose

Build the narrowest source change that satisfies a task contract.

## Trigger

An execution task calls for source changes after contracts exist.

## Context

- Task file under [../../execution/tasks/](../../execution/tasks/README.md)
- [../../architecture/source-map.md](../../architecture/source-map.md)
- [../../repository/code-style.md](../../repository/code-style.md)
- [../../agent/honest-state.md](../../agent/honest-state.md)

## Procedure

1. Read contracts named by the task.
2. Touch only files listed or justified in the task.
3. Implement the smallest vertical behavior slice.
4. Keep every new file under 50 lines; split by ownership.
5. Update source-map if new areas appear.
6. Run the task focused gate.

## Checks

Task focused gate plus `python scripts/check-lines.py`

## Must Not

Add fake success paths. Expand scope beyond the task without a new blocker.

## Handoff

Name source paths, gate output, and next blocker.
