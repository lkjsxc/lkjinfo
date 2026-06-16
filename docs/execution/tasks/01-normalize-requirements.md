# Normalize Requirements

## Purpose

Turn the raw idea into goals, non-goals, constraints, risks, and acceptance draft.

## Status

not-started

## Depends On

[00-capture-idea.md](00-capture-idea.md)

## Files To Read

- [../../intake/raw-idea.md](../../intake/raw-idea.md)
- [../../vision/scope.md](../../vision/scope.md)
- [../../product/problem.md](../../product/problem.md)
- [../../agent/skills/contract-design.md](../../agent/skills/contract-design.md)

## Files To Touch

- [../../vision/north-star.md](../../vision/north-star.md)
- [../../vision/scope.md](../../vision/scope.md)
- [../../product/problem.md](../../product/problem.md)
- [../../product/users.md](../../product/users.md)
- [../../product/acceptance.md](../../product/acceptance.md)
- [../../execution/traceability.md](../../execution/traceability.md)

## Focused Gate

```sh
python scripts/check-all.py
```

## Acceptance

- Goals and non-goals written in scope.md.
- Problem and users drafted from raw idea.
- Acceptance draft in product/acceptance.md.
- Traceability rows updated. Blocker row 2 moves to done with evidence.

## Must Not

Claim normalized requirements before raw idea exists. Use fake user research.
