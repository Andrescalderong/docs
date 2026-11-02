# -*- coding: utf-8 -*-
"""Marca páginas casi vacías (poco texto de cuerpo) en un PDF. Uso: python3 build/paginas_vacias.py PDF [umbral_palabras]"""
import sys, subprocess
pdf = sys.argv[1]; umbral = int(sys.argv[2]) if len(sys.argv) > 2 else 25
txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout.split("\f")
cab = ("ANEXO 2 DE LOS TdR", "Av. Calle 26", "Código: M801", "Versión: 01", "Vigente desde", "Página ")
for i, t in enumerate(txt[:-1], 1):
    L = [l.strip() for l in t.split("\n") if l.strip() and not l.strip().startswith(cab) and "Ciencias" != l.strip()]
    pal = sum(len(l.split()) for l in L)
    if pal < umbral: print("pág", i, "palabras de cuerpo:", pal, "|", " / ".join(L)[:150])
