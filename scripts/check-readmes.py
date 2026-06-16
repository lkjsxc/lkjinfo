#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from files import read_lines, rel, repo_root

errs = []
root = repo_root()
docs = os.path.join(root, "docs")
for dirpath, dirnames, filenames in os.walk(docs):
    if "README.md" not in filenames:
        errs.append(f"{rel(dirpath, root)}: missing README.md")
        continue
    readme = os.path.join(dirpath, "README.md")
    text = "\n".join(read_lines(readme))
    if "## Table of Contents" not in text:
        errs.append(f"{rel(readme, root)}: missing TOC")
    children = [c for c in os.listdir(dirpath) if c != "README.md"]
    if len(children) < 2:
        errs.append(f"{rel(dirpath, root)}: needs >=2 children")
    for child in children:
        if child not in text:
            errs.append(f"{rel(readme, root)}: unlinked {child}")
if errs:
    print("check-readmes failed:")
    for e in errs[:20]:
        print(e)
    sys.exit(1)
print("ok check-readmes")
