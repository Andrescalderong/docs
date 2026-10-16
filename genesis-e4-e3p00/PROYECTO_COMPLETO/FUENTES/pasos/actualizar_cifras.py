# -*- coding: utf-8 -*-
"""Sustituye las cifras derivadas del presupuesto antiguo por las del presupuesto ajustado en capítulos escritos a mano y en generadores."""
import os, re, glob, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = [
 ("9.267.260.000", "8.729.840.000"), ("9.267,26", "8.729,84"), ("9.267,3", "8.729,8"),
 ("11.377.260.000", "10.839.840.000"), ("11.377,26", "10.839,84"), ("11.377,3", "10.839,8"),
 ("4.732.740.000", "5.270.160.000"), ("4.732,74", "5.270,16"), ("4.732,7", "5.270,2"),
 ("4.552,8", "4.382,9"), ("1.885,6 millones", "1.885,6 millones"),
 ("2.689,3", "2.557,9"), ("1.936,1", "1.804,7"), ("2.634,1", "2.497,2"), ("2.007,8", "1.869,9"),
 ("56 líneas", "54 líneas"), ("56 partidas", "54 partidas"),
]
def procesar(path, mapa):
    t = open(path, encoding="utf-8").read(); o = t
    for a, b in mapa: t = t.replace(a, b)
    if t != o:
        open(path, "w", encoding="utf-8").write(t); return True
    return False
if __name__ == "__main__":
    EXCL = {"soporte.md", "a2a.md", "a2b.md", "a2c.md", "a2d.md"}
    cambiados = []
    for f in sorted(glob.glob(os.path.join(RAIZ, "caps", "*.md"))):
        if os.path.basename(f) in EXCL or os.path.basename(f).endswith("_r.md"): continue
        if procesar(f, MAP): cambiados.append(os.path.basename(f))
    for f in sorted(glob.glob(os.path.join(RAIZ, "pasos", "gen_*.py")) + glob.glob(os.path.join(RAIZ, "figs", "scripts", "*.py"))):
        if os.path.basename(f) in ("gen_soporte.py", "gen_a2a.py", "gen_a2b.py", "gen_a2c.py"): continue
        if procesar(f, MAP): cambiados.append(os.path.relpath(f, RAIZ))
    print("modificados:", cambiados)
