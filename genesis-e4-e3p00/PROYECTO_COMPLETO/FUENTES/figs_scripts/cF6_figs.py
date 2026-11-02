# -*- coding: utf-8 -*-
"""Figuras del Paso 6: F6.1 árbol de objetivos; F6.2 puntaje ponderado por alternativa y escenarios de sensibilidad.
Datos: maestro/maestro.py (OG, OE) y maestro/alternativas.py (CRIT, totales, ESCENARIOS)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, RAIZ + "/maestro")
import estilo as E
import maestro as M
import alternativas as A

def f01():
    fig, ax = E.lienzo_libre(
        h1="Los tres objetivos específicos convierten las causas priorizadas en medios verificables",
        h2="Árbol de objetivos derivado del árbol de problemas A-PROB; los códigos V corresponden a las variables del Paso 4",
        figsize=(10, 7.4), xlim=(0, 100), ylim=(0, 76))
    # fines
    ax.text(1, 72.5, "Fines", fontsize=10.5, fontweight="bold", color=E.TINTA)
    E.caja(ax, 6, 62, 40, 8, "Fin 1: decisiones de riesgo con datos\nde error conocido (V11, V12)", relleno=E.CLARO, fs=9)
    E.caja(ax, 54, 62, 40, 8, "Fin 2: uso institucional y continuidad de la\nvigilancia bajo custodia (V14, V15)", relleno=E.CLARO, fs=9)
    # objetivo general
    E.caja(ax, 14, 44, 72, 12, "OBJETIVO GENERAL\nReducir el error de medición de una red de 100 nodos y asegurar su uso\ninstitucional mediante calibración en gateways, energía y enlace\nredundantes y custodia distribuida (V06)", relleno=E.AZUL, fs=9, bold=True)
    for x in (26, 74): E.flecha(ax, (50, 56.4), (x, 61.6), lw=1.2)
    # objetivos específicos
    ax.text(1, 40, "Objetivos específicos", fontsize=10.5, fontweight="bold", color=E.TINTA)
    oe = [
        (3, "OE1: corregir la interferencia de\nhumedad y de fracción gruesa\nR² ≥ 0,70 y NRMSE ≤ 30 %\n(V03, V02, V01, V07)"),
        (36.5, "OE2: mantener la disponibilidad\nde 100 nodos y 10 gateways\ndisponibilidad ≥ 90 %\n(V05 → V09)"),
        (70, "OE3: lograr el uso del tablero\ny del protocolo por los comités\n≥ 75 % de 15 comités\n(V15)"),
    ]
    for x, t in oe:
        E.caja(ax, x, 26, 27, 11, t, relleno=E.MEDIO, fs=8.6)
        E.flecha(ax, (x + 13.5, 37.4), (50, 43.6), lw=1.2)
    # medios
    ax.text(1, 22, "Medios", fontsize=10.5, fontweight="bold", color=E.TINTA)
    medios = [
        (3, "Medio 1: colocalización con\n3 monitores de referencia y\nmodelo de corrección en gateway"),
        (36.5, "Medio 2: energía solar con 14 días\nde autonomía, enlace satelital\ny almacenamiento local de 7 días"),
        (70, "Medio 3: co-diseño con los\ncomités, formación y convenios\nde custodia por tramo"),
    ]
    for x, t in medios:
        E.caja(ax, x, 6, 27, 11, t, relleno=E.CAJA, fs=8.2)
        E.flecha(ax, (x + 13.5, 17.4), (x + 13.5, 25.6), lw=1.2)
    ax.text(50, 1.5, "Los medios conservan el estatuto de hipótesis de influencia estructural (HIE); ninguno se estima como efecto causal.",
            ha="center", fontsize=8.5, color=E.TINTA)
    E.guardar(fig, "cF6_f01")

def f02():
    nombres = ["ALT-00 Statu quo", "ALT-01 Estaciones fijas\nde referencia", "ALT-02 Calibración\ncentralizada", "ALT-03 Red híbrida\npor tramos"]
    base = A.BASE
    fig, ax = E.lienzo(h1="ALT-03 obtiene el mayor puntaje ponderado en el caso base y en los cinco escenarios de sensibilidad",
                       h2="Puntaje ponderado en escala ordinal de desempeño de 1 a 9; caso base con pesos por defecto y rango de cinco perturbaciones de +10 % relativo",
                       figsize=(10, 6.2))
    cols = [E.CLARO, E.CLARO, E.MEDIO, E.AZUL]
    barras = ax.barh(range(4), base, color=cols, edgecolor=E.TINTA, linewidth=0.8, height=0.55)
    for b, h in zip(barras, ["...", "xx", "..", ""]):
        b.set_hatch(h if h != "..." else "")
    ax.set_yticks(range(4)); ax.set_yticklabels(nombres, fontsize=9.5); ax.invert_yaxis()
    ax.set_xlim(0, 10.5); ax.set_xlabel("Puntaje ponderado (1 a 9)", fontsize=10)
    ax.grid(axis="y", visible=False); ax.grid(axis="x")
    import numpy as np
    tot = np.array([t for _, _, t in A.ESCENARIOS])
    for i, v in enumerate(base):
        lo, hi = tot[:, i].min(), tot[:, i].max()
        ax.plot([lo, hi], [i, i], color=E.TINTA, linewidth=2.2, solid_capstyle="butt", zorder=3)
        ax.annotate(f"{E.num(v, 3)}  (escenarios: {E.num(lo, 2)} a {E.num(hi, 2)})", xy=(max(hi, v), i), xytext=(8, 0), textcoords="offset points",
                    va="center", fontsize=9.6, fontweight="bold", color=E.TINTA)
    ax.text(0.99, -0.15, "La línea negra sobre cada barra marca el rango del puntaje en los cinco escenarios de sensibilidad.",
            transform=ax.transAxes, ha="right", fontsize=8.6, color=E.TINTA)
    E.guardar(fig, "cF6_f02")

if __name__ == "__main__":
    f01(); f02()
