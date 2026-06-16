# CI

## Purpose

Continuous integration should run the same gates as local verification.

## Required Command

```sh
python scripts/check-all.py
```

## Expectation

- Exit 0 only when all kit gates pass.
- Output follows [quiet-output.md](quiet-output.md).

## Project Extensions

After task [../execution/tasks/06-verification-gate.md](../execution/tasks/06-verification-gate.md),
add stack-specific test commands to CI alongside check-all.

## Status

Documented. Workflow file is not-started until a project adds CI config.

## Must Not

Claim CI passes without a run log.
