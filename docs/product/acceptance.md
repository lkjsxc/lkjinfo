# Product Acceptance

## Purpose

Product-level acceptance criteria for the future application.

## Status

waiting-for-idea

## Levels

See [../quality/acceptance-levels.md](../quality/acceptance-levels.md) for
design, source, product, and release acceptance.

## Placeholder Criteria

After intake, list testable criteria such as:
- A named user can complete journey X with real data.
- Failure state Y is explicit, not hidden behind fake success.

## Gate

Product acceptance requires focused tests plus
`python scripts/check-all.py` unless a project-specific gate replaces it in
task 06.

## Must Not

Do not mark criteria met before evidence exists.
