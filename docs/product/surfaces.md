# Surfaces

## Purpose

List user-visible surfaces and their honest implementation status.

## Status

waiting-for-idea

## Surface Table

| Surface | Description | Status |
| --- | --- | --- |
| _(after intake)_ | | not-started |

## Implementation Rule

A surface is implemented only when:
- Contract text matches shipped behavior.
- Source exists at the path named in [../architecture/source-map.md](../architecture/source-map.md).
- Tests or checks prove the behavior.
- Focused gate evidence is recorded in handoff.

## Allowed States

loading, unavailable, unsupported, denied, and real success data. No fake
placeholder rows. See [../agent/honest-state.md](../agent/honest-state.md).
