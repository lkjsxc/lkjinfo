# Code Style

## Purpose

Tech-agnostic conventions for future product source code.

## Conventions

- Pure core, effects at edges where practical.
- Small modules under the 50-line file cap.
- Explicit errors over hidden failures.
- No fake success states in product paths.
- Tests at the behavior owner level.
- Avoid global mutable state unless the stack requires it and the choice is
  documented in [../decisions/](../decisions/README.md).

## Fixtures

Synthetic data is allowed only in tests. Label fixtures test-only. Never import
test fixtures into product paths.

## Stack Details

Language-specific style guides may be added under
[../architecture/](../architecture/README.md) after stack selection.

## Honesty

See [../agent/honest-state.md](../agent/honest-state.md).
