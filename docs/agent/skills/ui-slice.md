# Skill: UI Slice

## Purpose

Implement UI work with real states only, no fake content.

## Trigger

A task touches user-visible UI components or pages.

## Context

- [../../product/surfaces.md](../../product/surfaces.md)
- [../../product/user-journeys.md](../../product/user-journeys.md)
- [../../agent/honest-state.md](../../agent/honest-state.md)
- [../../architecture/interfaces.md](../../architecture/interfaces.md)

## Procedure

1. Read surface contract and journey for the slice.
2. Wire UI to real data or explicit loading, unavailable, unsupported, denied.
3. Never render placeholder success or fake rows.
4. Add UI or integration tests for real and failure states.
5. Update surfaces.md status with evidence.

## Checks

Task focused gate plus UI tests named in task.

## Must Not

Show fake data, fake counters, or mock completed actions in product paths.

## Handoff

Surface status, tests, gate output, next UI slice if any.
