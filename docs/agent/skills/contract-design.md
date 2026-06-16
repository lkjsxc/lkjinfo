# Skill: Contract Design

## Purpose

Create or edit vision, product, and architecture contracts before code.

## Trigger

A task requires contract changes without or before source changes.

## Context

- [../../repository/documentation-standards.md](../../repository/documentation-standards.md)
- [../../repository/line-limits.md](../../repository/line-limits.md)
- [../../vision/](../../vision/README.md)
- [../../product/](../../product/README.md)
- [../../architecture/](../../architecture/README.md)
- [../../current-state.md](../../current-state.md)

## Procedure

1. Find the single owner file for the rule or behavior.
2. Edit with honest status values.
3. Update directory README tables of contents.
4. Add decision record if a settled choice moved.
5. Update current-state when status changes.
6. Run markdown and readme checks.

## Checks

`python scripts/check-markdown.py`
`python scripts/check-readmes.py`
`python scripts/check-links.py`

## Must Not

Restate rules owned elsewhere. Claim implemented without source and tests.

## Handoff

List contract paths changed and next implementation task.
