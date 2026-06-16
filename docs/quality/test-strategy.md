# Test Strategy

## Purpose

Tech-agnostic approach to tests for the future product.

## Principles

- Tests live at the behavior owner named in source-map.
- Test real behavior and explicit failure paths.
- Synthetic fixtures are test-only and labeled.
- No test asserts behavior the product does not implement.

## Levels

- Unit: pure logic and small modules.
- Integration: boundaries between components.
- End-to-end: user journeys from product contracts.

## When To Add Tests

Every implementation slice adds or updates tests before task acceptance.

## Kit Tests

The instruction kit is verified by `python scripts/check-all.py`.

## Gate

Task focused gate names the minimum test command for each slice.
