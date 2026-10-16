# -*- coding: utf-8 -*-
"""Actualiza los documentos 1000X escritos con valores V y tablas T: sustituye valores y bloques de tabla del presupuesto antiguo por los nuevos."""
import json, re, os, sys, collections
S = sys.argv[1]; RAIZ = sys.argv[2]
o = json.load(open(os.path.join(S, "vt_old.json"))); n = json.load(open(os.path.join(S, "vt_new.json")))
ARCH = {"cX1_datos": "x01.md", "cX2_datos": "x02.md", "cX5_datos": "x05.md", "cX6_datos": "x06.md", "cX7_datos": "x07.md", "cX8_datos": "x08.md", "cX9_datos": "x09.md"}
for m, fn in ARCH.items():
    path = os.path.join(RAIZ, "caps", fn); t = open(path, encoding="utf-8").read(); t0 = t
    # tablas completas
    nt = 0
    for k, v in o[m].get("T", {}).items():
        nv = n[m]["T"].get(k)
        if nv is not None and v != nv:
            if v in t: t = t.replace(v, nv); nt += 1
            else: print(f"  [{fn}] tabla {k}: bloque antiguo no encontrado literalmente")
    # valores
    mapa = {}; conflicto = []
    for k, v in o[m].get("V", {}).items():
        nv = n[m]["V"].get(k)
        if nv is None or v == nv or not v: continue
        if v in mapa and mapa[v] != nv: conflicto.append((k, v, mapa[v], nv))
        mapa[v] = nv
    if conflicto: print(f"  [{fn}] conflictos:", conflicto)
    if mapa:
        patron = re.compile(r"(?<![\d.,])(" + "|".join(re.escape(x) for x in sorted(mapa, key=len, reverse=True)) + r")(?!\d)")
        t, cnt = patron.subn(lambda mo: mapa[mo.group(1)], t)
    else: cnt = 0
    if t != t0: open(path, "w", encoding="utf-8").write(t)
    print(f"{fn}: tablas {nt}, valores sustituidos {cnt}")
