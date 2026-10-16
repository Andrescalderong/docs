# -*- coding: utf-8 -*-
"""Figura cX3_f01 (figura-resumen del pitch deck): las 15 diapositivas en cuatro actos, con la cifra de respaldo de cada una.
Cifras de la ficha maestra y de F-INF con página. Determinista."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import textwrap
import cX_comun as C
import estilo as E
from matplotlib.patches import Patch

def main():
    r = C.RES
    d = [
        (1, "Portada", "Convocatoria de\nEmergencia, Decreto\n1414 de 2026", 0),
        (2, "El problema", "90,8 % de 5.076\nestaciones sin plan\nde calibración", 0),
        (3, "Magnitud", "28 de 1.122\nmunicipios con estaciones\nutilizables", 0),
        (4, "Nuestra solución", "100 nodos,\n10 gateways y\n3 referencias", 1),
        (5, "¿Por qué es diferente?", "ALT-03: 5,81\nfrente a 5,15\nde ALT-02", 1),
        (6, "¿Cómo funciona?", "Medir, corregir,\nenviar, estimar\ny decidir", 1),
        (7, "Avance TRL", "TRL 4 a 7;\nTRL 8\ncondicionado", 1),
        (8, "Resultados esperados", "Red, software,\n2 artículos y\n29 actividades", 1),
        (9, "Impacto", "≥ 75 % de los\n15 comités usan\nel tablero", 2),
        (10, "El equipo", "14 líneas de\npersonal del\npresupuesto", 2),
        (11, "Alianzas", f"Contrapartida\nde {C.mm(C.CONTRA, 0)}\nmillones", 2),
        (12, "Cronograma", "24 meses, 104\nsemanas y compuertas\nC1, C2 y C3", 2),
        (13, "Presupuesto", f"SGR {C.mm(C.SGR, 1)}\nmillones; total\n{C.mm(C.TOTAL, 1)}", 3),
        (14, "Sostenibilidad", "Continuidad ≥ 70 %\na los 12 meses\ndel cierre", 3),
        (15, "Solicitud", f"Aprobar {C.mm(C.SGR, 1)}\nmillones y las\ncompuertas", 3),
    ]
    actos = [("Por qué (1 a 3)", E.CLARO, ""), ("Qué (4 a 8)", E.MEDIO, ""), ("Quién y cuándo (9 a 12)", E.CLARO, "///"), ("Cuánto y qué se pide (13 a 15)", E.MEDIO, "///")]
    fig, ax = C.lienzo_libre2(h1="Quince diapositivas llevan del problema medido a una solicitud concreta de $ 8.729,8 millones",
                             h2="Estructura del pitch deck en cuatro actos, con la cifra de respaldo de cada diapositiva", figsize=(10, 7.0), xlim=(0, 100), ylim=(0, 70), top=0.90)
    cols = 5; w = 18.0; h = 17.0; gx = 1.7; gy = 3.2; x0 = 1.6; y0 = 70 - 4 - h
    for k, (n, tit, dato, acto) in enumerate(d):
        fila, col = divmod(k, cols)
        x = x0 + col * (w + gx); y = y0 - fila * (h + gy)
        _, rel, ha = actos[acto]
        E.caja(ax, x, y, w, h, "", relleno=rel, hatch=ha or None)
        ax.text(x + 1.0, y + h - 0.9, f"{n}", ha="left", va="top", fontsize=14, fontweight="bold", color=E.TINTA,
                bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.9))
        ax.text(x + 5.4, y + h - 1.0, textwrap.fill(tit, 14), ha="left", va="top", fontsize=8.4, fontweight="bold", color=E.TINTA, linespacing=1.15,
                bbox=dict(fc="white", ec="none", pad=1.2, alpha=0.9))
        ax.text(x + w / 2, y + 5.2, dato, ha="center", va="center", fontsize=7.8, color=E.TINTA, bbox=dict(fc="white", ec="none", pad=1.4, alpha=0.9))
    ax.legend(handles=[Patch(fc=c, ec=E.TINTA, hatch=h_, label=n) for n, c, h_ in actos], loc="lower center", ncol=4, fontsize=8.8, bbox_to_anchor=(0.5, -0.04), frameon=False)
    E.guardar(fig, "cX3_f01")

if __name__ == "__main__":
    main(); print("figura cX3_f01 generada")
