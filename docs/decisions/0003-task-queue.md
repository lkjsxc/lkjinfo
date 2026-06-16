# 0003 Task Queue

## Purpose

Record that the blocker queue is the task source of truth.

## Context

Agents lose work when tasks live only in chat.

## Decision

docs/execution/current-blockers.md is dependency-ordered. Sessions take the
first open row unless the user names a task. active-session.md holds current work.

## Rejected Options

- Ad hoc task lists in chat.
- Parallel unbounded work without blockers.

## Consequences

Every session ends with a visible next task. Skipping requires evidence.

## Status

accepted
