#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from files import iter_repo_files, read_lines, rel, repo_root
from markdown import extract_relative_links

errs = []
root = repo_root()
for path in iter_repo_files(root):
    if not path.endswith(".md"):
        continue
    text = "\n".join(read_lines(path))
    base = os.path.dirname(path)
    for link in extract_relative_links(text):
        target = os.path.normpath(os.path.join(base, link))
        if not os.path.exists(target):
            errs.append(f"{rel(path, root)}: broken link {link}")
if errs:
    print("check-links failed:")
    for e in errs[:20]:
        print(e)
    sys.exit(1)
print("ok check-links")
