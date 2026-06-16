#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from files import iter_repo_files, read_lines, rel, repo_root
from markdown import is_ascii, h1_then_purpose

errs = []
root = repo_root()
for path in iter_repo_files(root):
    if not path.endswith(".md"):
        continue
    lines = read_lines(path)
    text = "\n".join(lines)
    r = rel(path, root)
    if not h1_then_purpose(lines):
        errs.append(f"{r}: missing H1 or Purpose")
    if not is_ascii(text):
        errs.append(f"{r}: non-ASCII")
    if "TODO" in text:
        errs.append(f"{r}: contains TODO")
if errs:
    print("check-markdown failed:")
    for e in errs[:20]:
        print(e)
    sys.exit(1)
print("ok check-markdown")
