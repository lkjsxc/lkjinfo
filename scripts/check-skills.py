#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from files import read_lines, rel, repo_root
from sections import section_order

REQ = ["Purpose", "Trigger", "Context", "Procedure", "Checks", "Must Not"]
errs = []
root = repo_root()
skill_dir = os.path.join(root, "docs", "agent", "skills")
for name in sorted(os.listdir(skill_dir)):
    if not name.endswith(".md") or name == "README.md":
        continue
    path = os.path.join(skill_dir, name)
    lines = read_lines(path)
    if not lines[0].startswith("# Skill:"):
        errs.append(f"{rel(path, root)}: bad H1")
    if not section_order(lines, REQ):
        errs.append(f"{rel(path, root)}: bad section order")
if errs:
    print("check-skills failed:")
    for e in errs:
        print(e)
    sys.exit(1)
print("ok check-skills")
