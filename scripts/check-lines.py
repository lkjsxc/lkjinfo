#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from files import iter_repo_files, read_lines, rel, repo_root

MAX = 50
errs = []
root = repo_root()
for path in iter_repo_files(root):
    n = len(read_lines(path))
    if n > MAX:
        errs.append(f"{rel(path, root)}: {n} lines")
if errs:
    print("check-lines failed:")
    for e in errs[:20]:
        print(e)
    if len(errs) > 20:
        print(f"... and {len(errs) - 20} more")
    sys.exit(1)
print("ok check-lines")
