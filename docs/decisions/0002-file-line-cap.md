# 0002 File Line Cap

## Purpose

Record the 50-line cap on every repository file.

## Context

Small files fit 32k context and force clear ownership boundaries.

## Decision

Every file is capped at 50 lines with no exceptions. Split by ownership.
Enforce with scripts/check-lines.py.

## Rejected Options

- 200-line cap like sibling projects.
- Exceptions for generated or license files.

## Consequences

LICENSE is a short notice. Large topics use directories and README routing.

## Status

accepted
