# -*- coding: utf-8 -*-
"""Figura c2_b_f02 (Capítulo 2, sección 2.5): hoja de ruta tecnológica del sector con la posición del proyecto.
Fuente: F-INF §4.8, Tabla 18 (p. 41), leída directamente de work/informe.md; criterio TRL 7 de F-INF §3.2 (Tabla 5, p. 22).
TRL inicial y final del proyecto: ficha maestra §1 (TRL 4 a 7, PROPUESTO). Sin aleatoriedad. Corpus de 42 documentos; año de corte 2026.
Salida: figs/out/c2_b_f02.png y .svg"""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import estilo as E

RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
INFORME = os.path.join(os.path.dirname(RAIZ), "work", "informe.md")

def leer_tabla18():
    txt = open(INFORME, encoding="utf-8").read()
    ini = txt.index("**Tabla 18**"); fin = txt.index("## 4.9", ini)
    filas = []
    for l in txt[ini:fin].split("\n"):
        m = re.match(r"^\s{2}(\S.+?)\s{2,}(\d+)\s{2,}([\d,]+|N/A)\s{2,}([\d,]+|N/A)\s*$", l)
        if m and m.group(3) != "N/A":
            filas.append((m.group(1).strip(), int(m.group(2)), float(m.group(3).replace(",", ".")), float(m.group(4).replace(",", ".")), m.group(3)))
    return filas

L = leer_tabla18()
assert len(L) == 12 and sum(f[1] for f in L) == 44, (len(L), sum(f[1] for f in L))   # 45 asignaciones con la línea de vigilancia de PI; las líneas no son excluyentes
L.sort(key=lambda f: f[2])   # ascendente para que la mayor madurez quede arriba en barras horizontales

# líneas con relación directa con el proyecto (lectura del proyecto, INFERIDO): sensores y calibración, alerta, índices y gemelo digital
RELEVANTES = {"Redes de sensores de bajo costo y calibración", "Sistemas de alerta temprana y gestión de desastres",
              "Índices y calificaciones de salud y salubridad", "Diagnóstico predictivo con gemelo digital"}

fig, ax = E.lienzo(h1="Ninguna línea del corpus alcanza un TRL medio de 7; el proyecto va de TRL 4 a TRL 7",
                   h2="TRL medio de 12 líneas tecnológicas (n de documentos entre paréntesis); corpus de 42 documentos, corte 2026; criterio de referencia TRL 7",
                   figsize=(10, 7))
ax.grid(axis="y", visible=False); ax.grid(axis="x")
y = list(range(len(L)))
cols = [E.AZUL if f[0] in RELEVANTES else E.MEDIO for f in L]
barras = ax.barh(y, [f[2] for f in L], color=cols, edgecolor=E.TINTA, linewidth=0.9, height=0.62, zorder=3)
for b, f in zip(barras, L):
    if f[0] in RELEVANTES:
        b.set_hatch("///")
    ax.text(f[2] + 0.07, b.get_y() + b.get_height() / 2, f[4] + f"  (n = {f[1]})",
            va="center", ha="left", fontsize=9, color=E.TINTA, fontweight="bold")
ax.set_xlim(0, 9.6); ax.set_xticks(range(0, 10))
ax.set_xlabel("Nivel de madurez tecnológica (TRL), media de la línea", fontsize=10)
ax.axvline(7, color=E.TINTA, lw=1.1, ls="--", zorder=2)
ax.text(7.07, len(L) - 0.5, "Criterio TRL 7", fontsize=9, color=E.TINTA, ha="left", va="center")

# fila del proyecto: rango de TRL 4 a TRL 7 (PROPUESTO), separada de las líneas del corpus
yp = len(L) + 0.35
ax.barh(yp, 3, left=4, color=E.CLARO, edgecolor=E.TINTA, linewidth=1.2, height=0.62, hatch="xx", zorder=3)
ax.text(3.93, yp, "TRL 4 inicial", fontsize=9, ha="right", va="center", color=E.TINTA, fontweight="bold")
ax.text(7.07, yp, "TRL 7 final", fontsize=9, ha="left", va="center", color=E.TINTA, fontweight="bold")
ax.set_yticks(y + [yp]); ax.set_yticklabels([f[0] for f in L] + ["Proyecto (PROPUESTO)"], fontsize=9)
ax.get_yticklabels()[-1].set_fontweight("bold")
ax.set_ylim(-0.6, yp + 0.7)
ax.legend(handles=[Patch(fc=E.AZUL, ec=E.TINTA, hatch="///", label="Línea con relación directa con el proyecto (INFERIDO)"),
                   Patch(fc=E.MEDIO, ec=E.TINTA, label="Otras líneas del corpus"),
                   Patch(fc=E.CLARO, ec=E.TINTA, hatch="xx", label="Rango de TRL del proyecto (PROPUESTO)")],
          loc="upper center", bbox_to_anchor=(0.4, -0.1), ncol=3, fontsize=8.2, frameon=False)
fig.text(0.01, -0.07, "Nota. Datos de F-INF §4.8 (p. 41). La línea de vigilancia de propiedad industrial no tiene TRL y se omite. "
         "Las líneas no son excluyentes (45 asignaciones para 42 documentos) y sus medias no representan tecnologías comerciales.", fontsize=7.5, color=E.TINTA, ha="left", va="top", wrap=True)
print(E.guardar(fig, "c2_b_f02"))
