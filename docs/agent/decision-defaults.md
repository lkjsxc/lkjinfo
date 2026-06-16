# Decision Defaults

## Purpose

What agents may decide alone vs what must be surfaced.

## Decide Alone

- File splits under the 50-line cap.
- Naming consistent with existing docs.
- Test cases beyond contract minimum.
- Conservative stack details after a decision record exists.
- Small documentation fixes and dead link repairs.

## Surface To User

- Scope boundary changes in [../vision/scope.md](../vision/scope.md).
- Security-sensitive behavior.
- New external services or dependencies.
- Data deletion behavior.
- Major stack replacement.

## Surface Means

Write the question into the task file, record in
[../execution/open-questions.md](../execution/open-questions.md), hand off,
and stop that line unless an unblocked row exists.

## Default On Ambiguity

Fix the contract first; do not implement a hidden interpretation.
