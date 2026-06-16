# Quiet Output

## Purpose

Keep verification output small for agents with limited context.

## Pass

A passing gate prints exactly one line:

```text
ok <gate>
```

Example: `ok check-lines`

## Fail

A failing gate prints:
- The gate name.
- Bounded evidence (file paths, line numbers, short message).
- Exit code nonzero.

## Do Not

Print giant success logs. Dump entire file contents on pass.

## check-all

On full pass, print exactly:

```text
ok check-all
```

On failure, print the failing gate name and bounded output, then exit nonzero.
