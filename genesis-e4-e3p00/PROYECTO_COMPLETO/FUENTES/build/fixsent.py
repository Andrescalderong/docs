import re
def fix(path, prefix, new, count=1):
    t = open(path, encoding="utf-8").read()
    i = t.find(prefix)
    assert i >= 0, (path, prefix[:60])
    m = re.search(r"\.(?=\s|$)", t[i + len(prefix):])
    j = i + len(prefix) + (m.end() if m else 0)
    t = t[:i] + new + t[j:]
    open(path, "w", encoding="utf-8").write(t)
