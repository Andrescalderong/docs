# -*- coding: utf-8 -*-
"""Utilidades de generación de capítulos con directivas (:::TABLA, :::FIGURA, {T:id}, {F:id})."""
import os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "maestro"))
sys.path.insert(0, os.path.join(RAIZ, "figs", "scripts"))
import maestro as D

def esc(s): return str(s).replace("|", "\\|")

class Doc:
    def __init__(self, prefijo):
        self.L = []; self.pref = prefijo
        self.L.append(f"%% PREFIJO: {prefijo}")
    def h(self, nivel, texto):
        self.L += ["", "#" * nivel + " " + texto, ""]
    def p(self, texto):
        self.L += [texto.strip(), ""]
    def tabla(self, tid, titulo, enc, filas, nota):
        self.L.append(f":::TABLA {tid} | {titulo}")
        self.L.append("| " + " | ".join(enc) + " |")
        self.L.append("| " + " | ".join("---" for _ in enc) + " |")
        for r in filas:
            assert len(r) == len(enc), (tid, r)
            self.L.append("| " + " | ".join(esc(x) for x in r) + " |")
        self.L.append(":::NOTA " + nota.strip())
        self.L.append("")
    def fig(self, fid, titulo, nota):
        self.L += [f":::FIGURA {fid} | {titulo} | {nota.strip()}", ""]
    def raw(self, texto):
        self.L += [texto.rstrip(), ""]
    def guardar(self, ruta):
        txt = "\n".join(self.L).rstrip() + "\n"
        open(ruta, "w", encoding="utf-8").write(txt)
        return txt

def num(n, d=0):
    s = f"{n:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def mm(n, d=1): return D.mm(n, d)
def cop(n): return D.cop(n)
