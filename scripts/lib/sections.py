def section_order(lines, required):
    names = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("## ") and not s.startswith("### "):
            names.append(s[3:].strip())
    idx = 0
    for name in names:
        if idx < len(required) and name == required[idx]:
            idx += 1
        elif name == "Handoff":
            continue
    return idx == len(required)
