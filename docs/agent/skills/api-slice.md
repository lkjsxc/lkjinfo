# Skill: API Slice

## Purpose

Implement API or integration boundaries with explicit failure states.

## Trigger

A task adds or changes HTTP, RPC, CLI protocol, or external integration.

## Context

- [../../architecture/interfaces.md](../../architecture/interfaces.md)
- [../../architecture/security.md](../../architecture/security.md)
- [../../agent/honest-state.md](../../agent/honest-state.md)
- [../../agent/decision-defaults.md](../../agent/decision-defaults.md)

## Procedure

1. Document request, response, and error shapes in interfaces.md.
2. Implement handler with explicit errors; no fake protocol results.
3. Surface new external services in decision-defaults surfacing rules.
4. Add tests for success and representative failure paths.
5. Run task focused gate.

## Checks

Task focused gate and interface contract update in same change.

## Must Not

Return synthetic success when upstream failed. Hide errors as empty success.

## Handoff

Interface paths, external deps surfaced, gate output.
