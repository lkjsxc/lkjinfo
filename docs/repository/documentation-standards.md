# Documentation Standards

## Purpose

Markdown shape, README topology, links, statuses, and content rules.

## File Shape

- ASCII only. One H1, then `## Purpose` immediately after.
- Prose lines at or below 100 characters where practical.
- Tables at most 6 columns.
- Relative links for repository files.

## README Topology

- Every docs directory has exactly one README.md.
- README has `## Table of Contents` linking every direct child.
- At least two direct children besides README unless collapse is justified.

## Statuses

implemented, waiting-for-idea, design-only, not-started, blocked,
out-of-scope, open-question.

## Banned

- Hidden task markers in markdown (enforced by check-markdown).
- Vague future promises and claims of unbuilt behavior.
- Restating rules owned elsewhere; link the owner.

## Enforcement

`python scripts/check-markdown.py` and `python scripts/check-readmes.py`.
