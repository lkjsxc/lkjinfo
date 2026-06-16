# Refactor Policy

## Purpose

Rules for behavior-preserving structural changes under the 50-line cap.

## Requirements

- Refactors require unchanged behavior evidence: same tests pass, same
  acceptance criteria met.
- Update contracts if names or module boundaries change.
- Split files approaching 50 lines during refactor, not after.

## Procedure

Use skill [../agent/skills/refactor.md](../agent/skills/refactor.md).

## Allowed Alone

File splits, rename for clarity, extract module with same public behavior.

## Not Allowed Without Task

Behavior change, new features, or scope change disguised as refactor.

## Gate

Focused tests for touched behavior plus `python scripts/check-lines.py`.
