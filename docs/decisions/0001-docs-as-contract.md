# 0001 Docs As Contract

## Purpose

Record that documentation is the implementation contract.

## Context

Agents need a single authoritative source for behavior and structure.

## Decision

The docs/ tree is the contract. Code must match docs. Docs and code update in
the same change. current-state.md tracks honest status.

## Rejected Options

- Code as sole source of truth.
- Chat-only requirements.

## Consequences

Every slice updates contracts before or with source. Contradictions are first tasks.

## Status

accepted
