# 0005 Small Model Context

## Purpose

Record design choices for ~20B parameter agents with 32k context.

## Context

Medium models need narrow reads and durable file state.

## Decision

Optimize for correctness and task continuity: short files, README routing,
explicit read order in AGENTS.md, ledger files, and quiet check output.

## Rejected Options

- Large monolithic docs.
- Chat as durable state.

## Consequences

context-policy.md guides sessions. Skills are trigger-indexed under 50 lines.

## Status

accepted
