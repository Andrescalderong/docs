# -*- coding: utf-8 -*-
"""Figura c2_b_f01 (Capítulo 2, sección 2.5): mapa de posicionamiento TRL por IRL de los 41 documentos con ambos niveles.
Fuente: F-INF §4.1, Tabla 13 (p. 29), leída directamente de work/informe.md (filas G-01 a G-42).
Sin aleatoriedad: no usa semilla. Corpus de 42 documentos (41 con TRL e IRL); año de corte 2026.
Salida: figs/out/c2_b_f01.png y .svg"""
import os, re, sys, collections
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import estilo as E

RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
INFORME = os.path.join(os.path.dirname(RAIZ), "work", "informe.md")

# Identificadores G de las 15 patentes (clase del banco: tipo = patente); el informe institucional es G-42
PATENTES = {"G-01", "G-02", "G-03", "G-04", "G-07", "G-09", "G-11", "G-14", "G-15", "G-16", "G-23", "G-24", "G-25", "G-40", "G-41"}

def leer_tabla13():
    filas = {}
    for linea in open(INFORME, encoding="utf-8"):
        m = re.match(r"^\s+(G-\d\d)\s{2,}(.+?)\s{2,}(\d|N/A)\s+(\S+)\s+(\S+)\s+(\d|N/A)\s+(\d|N/A)\s+(\S+)\s+(\S+)\s*$", linea)
        if m:
            g, cita, trl, mrl, brl, irl, drl = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6), m.group(7)
            filas[g] = (cita.strip(), None if trl == "N/A" else int(trl), None if irl == "N/A" else int(irl))
    return filas

T13 = leer_tabla13()
assert len(T13) == 42, len(T13)
datos = {g: v for g, v in T13.items() if v[1] is not None and v[2] is not None}
assert len(datos) == 41
n_trl4 = sum(1 for v in datos.values() if v[1] <= 4)
n_trl7 = sum(1 for v in datos.values() if v[1] >= 7)
n_irl3 = sum(1 for v in datos.values() if v[2] <= 3)
assert (n_trl4, n_trl7, n_irl3) == (34, 2, 33), (n_trl4, n_trl7, n_irl3)

cuenta = {"art": collections.Counter(), "pat": collections.Counter()}
for g, (cita, trl, irl) in datos.items():
    cuenta["pat" if g in PATENTES else "art"][(trl, irl)] += 1
assert sum(cuenta["pat"].values()) == 15 and sum(cuenta["art"].values()) == 26

fig, ax = E.lienzo(h1="34 de 41 documentos están en TRL 4 o menos y solo dos alcanzan el TRL 7",
                   h2="Documentos del corpus por nivel de madurez tecnológica (TRL, eje x) y de integración (IRL, eje y); tamaño = número de documentos; n = 41",
                   figsize=(10, 7))
ax.grid(axis="x")
ax.set_xlim(1.4, 9.8); ax.set_ylim(0.2, 9.9)
ax.set_xticks(range(2, 10)); ax.set_yticks(range(1, 10))
ax.set_xlabel("Nivel de madurez tecnológica (TRL)", fontsize=10)
ax.set_ylabel("Nivel de integración (IRL)", fontsize=10)

# criterios de referencia del informe: TRL 7 e IRL 6
ax.axvline(7, color=E.TINTA, lw=1.0, ls="--")
ax.axhline(6, color=E.TINTA, lw=1.0, ls="--")
ax.text(7.08, 0.45, "Criterio TRL 7", fontsize=8.5, color=E.TINTA, ha="left", va="bottom")
ax.text(1.5, 6.1, "Criterio IRL 6", fontsize=8.5, color=E.TINTA, ha="left", va="bottom")

# banda del proyecto (TRL 4 a 7, PROPUESTO)
ax.axvspan(4, 7, ymin=0.935, ymax=0.99, color=E.MEDIO, alpha=0.85, lw=0)
ax.text(5.5, 9.58, "Proyecto: TRL 4 a 7 (PROPUESTO)", fontsize=9.5, ha="center", va="center", color=E.TINTA, fontweight="bold")

DESP = 0.3
for (trl, irl), n in sorted(cuenta["art"].items()):
    dx = -DESP if (trl, irl) in cuenta["pat"] else 0
    ax.scatter(trl + dx, irl, s=95 * n + 40, marker="o", facecolor=E.AZUL, edgecolor=E.TINTA, linewidth=1.0, zorder=3)
    ax.text(trl + dx, irl, str(n), ha="center", va="center", fontsize=8.5, fontweight="bold", color=E.TINTA, zorder=4)
for (trl, irl), n in sorted(cuenta["pat"].items()):
    dx = DESP if (trl, irl) in cuenta["art"] else 0
    ax.scatter(trl + dx, irl, s=95 * n + 40, marker="s", facecolor=E.CLARO, edgecolor=E.TINTA, linewidth=1.0, zorder=3)
    ax.text(trl + dx, irl, str(n), ha="center", va="center", fontsize=8.5, fontweight="bold", color=E.TINTA, zorder=4)

# etiquetas directas de los documentos del nicho
def rotular(g, texto, dx, dy, ha="left"):
    _, trl, irl = T13[g]
    ax.annotate(texto, xy=(trl, irl), xytext=(trl + dx, irl + dy), fontsize=8.5, color=E.TINTA, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.7))
ax.annotate("SIATA\n(Ruiz-Carrascal et al., 2026)", xy=(9, 8), xytext=(9.75, 7.2), fontsize=8.5, color=E.TINTA, ha="right", va="center",
            arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.7))
rotular("G-33", "Sistema de lahares, Perú (Espinoza et al., 2026)", 0.2, 0.55)
rotular("G-20", "Mina de carbón (Suresh et al., 2025)", 0.2, -0.8)
rotular("G-31", "Red de Seúl (Bang et al., 2026)", 0.0, 1.2, ha="center")
ax.annotate("Diseño nacional\n(Murad Pedraza et al., 2026)", xy=(2.7, 2.0), xytext=(1.55, 0.58), fontsize=8.5, color=E.TINTA, ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.7))

leyenda = [Line2D([0], [0], marker="o", color="none", markerfacecolor=E.AZUL, markeredgecolor=E.TINTA, markersize=10, label="Artículos (26)"),
           Line2D([0], [0], marker="s", color="none", markerfacecolor=E.CLARO, markeredgecolor=E.TINTA, markersize=10, label="Patentes (15)")]
ax.legend(handles=leyenda, loc="upper left", bbox_to_anchor=(0.0, 0.90), fontsize=9, frameon=False)

fig.text(0.01, -0.02, "Nota. Datos de F-INF §4.1 (p. 29): 41 de 42 documentos con TRL e IRL; el informe de la SIC (2026) no tiene niveles. "
         "Las patentes se agrupan en TRL 2 a 4. El rango del proyecto (4 a 7) es PROPUESTO y no representa un nivel IRL.",
         fontsize=7.5, color=E.TINTA, ha="left", va="top", wrap=True)
print(E.guardar(fig, "c2_b_f01"))
