import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_cap as C
def largas(path, maxw=25):
    raw = open(path, encoding="utf-8").read()
    prose, tabs, figs, order = C.split_directives(raw)
    out = []
    fence = False
    for l in prose:
        s = l.strip()
        if s.startswith("```"): fence = not fence; continue
        if fence or not s or s.startswith("#") or s.startswith("|") or s.startswith("<!--") or s.startswith("%%"): continue
        t = re.sub(r"^([-*]|\d+\.)\s+", "", s); t = re.sub(r"\*+|\{[TF]:[^}]+\}", "", t)
        for sent in re.split(r"(?<=[.!?;:])\s+(?=[A-ZÁÉÍÓÚÑ¿¡(«\[])", t):
            n = len(re.findall(r"[\wÁÉÍÓÚÜÑáéíóúüñ%/.,:\-→]+", re.sub(r"\([^()]*\d{4}[^()]*\)", "", sent)))
            if n > maxw: out.append((n, sent))
    return out
if __name__ == "__main__":
    for n, s in largas(sys.argv[1]): print(n, "|", s, "\n")
