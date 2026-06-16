#!/usr/bin/env python3
import sys
import os
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from files import read_lines, rel, repo_root
from sections import section_order

REQ = [
    "Purpose", "Status", "Depends On", "Files To Read", "Files To Touch",
    "Focused Gate", "Acceptance", "Must Not",
]
errs = []
root = repo_root()
task_dir = os.path.join(root, "docs", "execution", "tasks")
for name in sorted(os.listdir(task_dir)):
    if not name.endswith(".md") or name == "README.md":
        continue
    path = os.path.join(task_dir, name)
    lines = read_lines(path)
    if not lines[0].startswith("# "):
        errs.append(f"{rel(path, root)}: bad H1")
    if not section_order(lines, REQ):
        errs.append(f"{rel(path, root)}: bad section order")
blockers = os.path.join(root, "docs", "execution", "current-blockers.md")
bt = "\n".join(read_lines(blockers))
for name in sorted(os.listdir(task_dir)):
    if name == "README.md":
        continue
    if name not in bt:
        errs.append(f"blockers: missing link to {name}")
if errs:
    print("check-tasks failed:")
    for e in errs:
        print(e)
    sys.exit(1)
print("ok check-tasks")
