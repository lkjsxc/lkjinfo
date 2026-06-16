#!/usr/bin/env python3
import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from files import read_lines, rel, repo_root

errs = []
root = repo_root()
trace = os.path.join(root, "docs", "execution", "traceability.md")
text = "\n".join(read_lines(trace))
if "waiting-for-idea" not in text and "| _(none)_ |" not in text:
    if "Idea Item" not in text:
        errs.append("traceability: missing matrix")
blockers = os.path.join(root, "docs", "execution", "current-blockers.md")
for ln in read_lines(blockers):
    if "| waiting-for-idea |" in ln or "| not-started |" in ln or "| open |" in ln:
        m = re.search(r"\[tasks/([^\]]+)\]", ln)
        if not m:
            errs.append(f"blockers: open row without task link: {ln[:60]}")
        else:
            p = os.path.join(root, "docs", "execution", "tasks", m.group(1))
            if not os.path.isfile(p):
                errs.append(f"blockers: missing task file {m.group(1)}")
if errs:
    print("check-trace failed:")
    for e in errs:
        print(e)
    sys.exit(1)
print("ok check-trace")
