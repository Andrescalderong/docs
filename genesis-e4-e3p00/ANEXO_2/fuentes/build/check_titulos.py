# -*- coding: utf-8 -*-
"""Compara los títulos de nivel 1 y 2 del DOCX (en orden, solo la parte del Anexo 2) con TITULOS.md. Uso: python3 build/check_titulos.py ARCHIVO.docx"""
import sys, os, re, unicodedata, docx
HERE = os.path.dirname(os.path.abspath(__file__)); A2 = os.path.dirname(HERE)
def norm(s): return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip()
esperados = []
for l in open(os.path.join(A2, "TITULOS.md"), encoding="utf-8"):
    m = re.match(r"^(#{1,2}) (.*)$", l.rstrip("\n"))
    if m and not l.startswith("# TÍTULOS"): esperados.append((len(m.group(1)), norm(m.group(2))))
d = docx.Document(sys.argv[1])
obt = []
for p in d.paragraphs:
    st = p.style.name
    if st in ("Heading 1", "Título 1", "Heading 2", "Título 2"):
        nivel = 1 if st.endswith("1") else 2
        obt.append((nivel, norm(p.text)))
# recorta: desde "1. IDENTIFICACIÓN" hasta "30. ANEXOS"
ini = next(i for i, (n, t) in enumerate(obt) if t.startswith("1. IDENTIFICACIÓN DEL PROYECTO"))
fin = next(i for i, (n, t) in enumerate(obt) if t.startswith("30. ANEXOS"))
obt = obt[ini:fin + 1]
# los títulos oficiales deben aparecer textualmente, con su nivel y en el mismo orden; se admiten subtítulos adicionales entre ellos
j = 0; faltan = []
for e in esperados:
    k = j
    while k < len(obt) and obt[k] != e: k += 1
    if k == len(obt): faltan.append(e)
    else: j = k + 1
ok = not faltan
print("títulos oficiales:", len(esperados), "encabezados de nivel 1 y 2 en el documento:", len(obt), "oficiales hallados en orden:", len(esperados) - len(faltan), "->", "OK" if ok else "FALTAN")
for f in faltan: print("  falta:", f)
sys.exit(0 if ok else 1)
