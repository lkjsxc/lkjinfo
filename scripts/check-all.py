#!/usr/bin/env python3
import subprocess
import sys
import os

CHECKS = [
    "check-lines", "check-markdown", "check-readmes", "check-links",
    "check-skills", "check-tasks", "check-trace",
]
here = os.path.dirname(os.path.abspath(__file__))
for name in CHECKS:
    path = os.path.join(here, f"{name}.py")
    r = subprocess.run([sys.executable, path], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"check-all failed at {name}")
        out = (r.stdout + r.stderr).strip()
        if out:
            lines = out.splitlines()
            for ln in lines[:15]:
                print(ln)
            if len(lines) > 15:
                print(f"... {len(lines) - 15} more lines")
        sys.exit(1)
print("ok check-all")
