import re

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_ascii(text):
    try:
        text.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def first_section(lines, level):
    prefix = "#" * level + " "
    deeper = "#" * (level + 1)
    for ln in lines:
        s = ln.strip()
        if s.startswith(prefix) and not s.startswith(deeper):
            return s[len(prefix):].strip()
    return None


def h1_then_purpose(lines):
    if first_section(lines, 1) is None:
        return False
    seen_h1 = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("# ") and not s.startswith("## "):
            seen_h1 = True
            continue
        if seen_h1 and s.startswith("## "):
            return s == "## Purpose"
    return False


def extract_relative_links(text):
    out = []
    for m in LINK_RE.finditer(text):
        t = m.group(1).strip()
        if "://" in t or t.startswith("#"):
            continue
        out.append(t.split("#")[0])
    return out
