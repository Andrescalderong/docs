# -*- coding: utf-8 -*-
"""Figuras del capítulo 16 (prefijo 16): c16_f01 (mapa de canales), c16_f02 (cronograma de divulgación),
c16_f03 (Escalera ASC) y c16_f04 (alineación con la Teoría del Cambio).
Datos: ficha maestra (PERS-P04: 29 actividades, 20 talleres y 9 jornadas; compromisos por nivel; hitos H0 a H8; compuertas C1, C2, C3)
e indicadores.py (ASC y marco lógico). La distribución por tramos (4, 8 y 8 talleres; 3, 3 y 3 jornadas) es PROPUESTO. Sin semilla ni corpus."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import estilo as E
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D


def caja2(ax, x, y, w, h, texto, relleno=E.CAJA, fs=9, trama=None, borde=E.TINTA, lw=1.2, ls="-", bold=False):
    if trama:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=E.AZUL, lw=0, hatch=trama))
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc="none", ec=borde, lw=lw, ls=ls))
        if texto:
            ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, linespacing=1.25,
                    fontweight="bold" if bold else "normal", bbox=dict(boxstyle="round,pad=0.3", fc=relleno, ec="none"))
    else:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=borde, lw=lw, ls=ls))
        if texto:
            ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, linespacing=1.25,
                    fontweight="bold" if bold else "normal")


# ------------------------------------------------------------------ f01: mapa de canales por nivel
def f01():
    fig, ax = E.lienzo(h1="Los canales unidireccionales sirven al nivel 1 y los interactivos al nivel 3",
                       h2="Canales por nivel de la Escalera ASC: principal y complementario (diseño PROPUESTO)", figsize=(10, 7), grid=False)
    canales = [
        ("Cartillas impresas", {1: "P", 2: "C", 3: "C"}),
        ("Página del proyecto y boletines", {1: "P", 2: "C"}),
        ("Redes sociales", {1: "P"}),
        ("Emisoras y carteleras comunitarias", {1: "P", 2: "C"}),
        ("Jornadas públicas", {1: "P", 2: "P"}),
        ("Grupos focales y encuestas", {2: "P"}),
        ("Buzón de sugerencias", {2: "P"}),
        ("Talleres y laboratorios ciudadanos", {3: "P"}),
        ("Sesiones de comité con el tablero", {2: "C", 3: "P"}),
        ("Formación de personas formadoras locales", {3: "C", 4: "P"}),
        ("Artículos, seminarios y congresos", {"CIRC": "P"}),
    ]
    cols = [1, 2, 3, 4, "CIRC"]
    nombres = ["Nivel 1\nInformación", "Nivel 2\nConsulta", "Nivel 3\nColaboración", "Nivel 4\nEmpoderamiento", "ASC-CIRC\n(circulación)"]
    n = len(canales)
    ax.set_xlim(-0.2, 5.7)
    ax.set_ylim(n - 0.3, -2.0)
    ax.axis("off")
    rellenos = [E.CLARO, E.MEDIO, E.MEDIO, E.GRIS, E.CAJA]
    for j, (c, nom) in enumerate(zip(cols, nombres)):
        x0 = 1.9 + j * 0.8
        ax.add_patch(FancyBboxPatch((x0 - 0.36, -1.55), 0.72, 1.0, boxstyle="round,pad=0.02,rounding_size=0.06", fc=rellenos[j], ec=E.TINTA, lw=1.4 if c == 3 else 0.9))
        ax.text(x0, -1.05, nom, ha="center", va="center", fontsize=8.2, color=E.TINTA, fontweight="bold" if c == 3 else "normal", linespacing=1.15)
    for i, (nombre, marcas) in enumerate(canales):
        ax.text(1.5, i, nombre, ha="right", va="center", fontsize=9.3, color=E.TINTA)
        ax.plot([1.55, 5.4], [i + 0.5, i + 0.5], color=E.MEDIO, lw=0.6, alpha=0.5)
        for j, c in enumerate(cols):
            x0 = 1.9 + j * 0.8
            m = marcas.get(c)
            if m == "P":
                ax.plot(x0, i, marker="o", ms=13, mfc=E.AZUL, mec=E.TINTA, mew=1.1, zorder=3)
            elif m == "C":
                ax.plot(x0, i, marker="o", ms=13, mfc="none", mec=E.TINTA, mew=1.3, zorder=3)
    handles = [Line2D([0], [0], marker="o", ls="", mfc=E.AZUL, mec=E.TINTA, ms=10, label="Canal principal"),
               Line2D([0], [0], marker="o", ls="", mfc="none", mec=E.TINTA, ms=10, label="Canal complementario")]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.30, -0.04), ncol=2, fontsize=9, frameon=False)
    E.guardar(fig, "c16_f01")


# ------------------------------------------------------------------ f02: cronograma de divulgación
def f02():
    fig, ax = E.lienzo(h1="El nivel 3 concentra 20 de las 29 actividades y se extiende hasta el mes 24",
                       h2="Actividades de apropiación por nivel, meses 1 a 24; compuertas C1 (mes 12), C2 (mes 17) y C3 (mes 24)",
                       figsize=(10, 7), grid=False)
    filas = ["Hitos del proyecto", "Línea base y consentimiento", "Nivel 1: piezas y jornadas", "Nivel 2: consulta",
             "Nivel 3: talleres de co-diseño", "Nivel 2: devolución y continuidad", "Nivel 4: formación de personas formadoras",
             "Medición semestral", "Acumulado de actividades"]
    n = len(filas)
    ax.set_xlim(0, 25.5)
    ax.set_ylim(n - 0.3, -1.1)
    ax.set_yticks(range(n))
    ax.set_yticklabels(filas, fontsize=9.3)
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([1, 4, 8, 12, 17, 20, 24])
    ax.set_xlabel("Mes de ejecución", fontsize=9.5)
    ax.spines["left"].set_visible(False)
    alto = 0.34

    def barra(fila, ini, fin, color, texto, trama=None, lw=1.0):
        ax.barh(fila, fin - ini + 1, left=ini - 0.5, height=alto, color=color, edgecolor=E.TINTA, linewidth=lw, hatch=trama, zorder=3)
        ax.text(ini - 0.4, fila - alto / 2 - 0.06, texto, ha="left", va="bottom", fontsize=8.3, color=E.TINTA)

    # hitos
    for m, t in ((2, "H0"), (4, "H1"), (10, "H2"), (16, "H4"), (19, "H6"), (23, "H7")):
        ax.plot(m, 0, marker="v", ms=8, mfc=E.MEDIO, mec=E.TINTA, zorder=4)
        ax.text(m, -0.38, t, ha="center", va="bottom", fontsize=8, color=E.TINTA)
    for m, t in ((12, "C1"), (17, "C2"), (24, "C3")):
        ax.axvline(m, color=E.TINTA, lw=0.8, ls=(0, (4, 3)), zorder=1)
        ax.plot(m, 0, marker="s", ms=9, mfc=E.AZUL, mec=E.TINTA, zorder=5)
        ax.text(m + 0.35, -0.38, t, ha="left", va="bottom", fontsize=8.5, fontweight="bold", color=E.TINTA)
    barra(1, 3, 4, E.CAJA, "Línea base (meses 3 y 4)")
    barra(2, 4, 8, E.CLARO, "3 jornadas y cartilla inicial (meses 4 a 8)")
    barra(3, 6, 12, E.MEDIO, "3 jornadas de consulta (meses 6 a 12)")
    barra(4, 4, 12, E.AZUL, "4 talleres")
    barra(4, 13, 17, E.AZUL, "8 talleres")
    barra(4, 18, 24, E.AZUL, "8 talleres")
    barra(5, 22, 24, E.MEDIO, "3 jornadas")
    barra(6, 18, 24, E.GRIS, "1 actividad con plan (aspiracional)", trama="///")
    for m in (6, 12, 18, 24):
        ax.plot(m, 7, marker="D", ms=8, mfc=E.CLARO, mec=E.TINTA, zorder=4)
    ax.text(0.7, 7 - alto / 2 - 0.06, "Meses 6, 12, 18 y 24", ha="left", va="bottom", fontsize=8.3, color=E.TINTA)
    for m, v in ((12, "10"), (17, "18"), (24, "29")):
        ax.plot(m, 8, marker="s", ms=17, mfc=E.CLARO, mec=E.TINTA, zorder=4)
        ax.text(m, 8, v, ha="center", va="center", fontsize=8.5, fontweight="bold", color=E.TINTA, zorder=6)
    ax.text(0.7, 8 - alto / 2 - 0.06, "Talleres más jornadas, acumulados", ha="left", va="bottom", fontsize=8.3, color=E.TINTA)
    E.guardar(fig, "c16_f02")


# ------------------------------------------------------------------ f03: Escalera ASC
def f03():
    fig, ax = E.lienzo_libre(h1="Cuatro niveles ascendentes: el tercero es obligatorio y el cuarto es aspiracional",
                             h2="Escalera de Apropiación Social del Conocimiento; compromisos por nivel de la ficha maestra",
                             figsize=(10, 6.2), xlim=(0, 100), ylim=(0, 58))
    base = 8
    w = 21
    textos = [
        "Nivel 1: Información\nASC-COM\nCompromiso: 100 % entre\nlos meses 1 y 8\n3 jornadas; 5.000 cartillas",
        "Nivel 2: Consulta\nASC-COM y ASC-PART\nCompromiso: 100 % entre\nlos meses 1 y 12\n6 jornadas",
        "Nivel 3: Colaboración\nactiva\nASC-PART\nOBLIGATORIO: mínimo 3\nactas firmadas\n20 talleres programados",
        "Nivel 4: Empoderamiento\nASC-PART y FORM\nASPIRACIONAL: 1 actividad\ncon plan de sostenibilidad",
    ]
    rell = [E.CLARO, E.MEDIO, E.AZUL, E.GRIS]
    for i in range(4):
        x = 3 + 23.5 * i
        h = 9 + 9 * i
        lw = 2.6 if i == 2 else 1.2
        ls = (0, (4, 2)) if i == 3 else "-"
        ax.add_patch(Rectangle((x, base), w, h, fc=rell[i], ec=E.TINTA, lw=lw, ls=ls, hatch="///" if i == 3 else None))
        ax.text(x + 0.4, base + h + 1.2, textos[i], ha="left", va="bottom", fontsize=8.7, color=E.TINTA, linespacing=1.3,
                fontweight="bold" if i == 2 else "normal")
    E.flecha(ax, (4, 4.5), (96, 4.5), lw=1.6)
    ax.text(50, 5.3, "Mayor participación y poder de decisión de la comunidad", ha="center", va="bottom", fontsize=9, color=E.TINTA)
    E.guardar(fig, "c16_f03")


# ------------------------------------------------------------------ f04: alineación con la Teoría del Cambio
def f04():
    fig, ax = E.lienzo_libre(h1="El nivel 3 conecta los productos de apropiación con el uso institucional del tablero",
                             h2="Niveles ASC frente a la cadena de resultados del proyecto; relaciones hipotéticas (INFERIDO)",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    xs = [3, 27.5, 52, 76.5]
    w = 20.5
    top = ["Actividades\nWP3; PERS-R01 a PERS-R06", "Productos\nPERS-P01 a PERS-P04", "Efectos\nPERS-E01 a PERS-E03", "Impactos\nPERS-S01 y PERS-S02\n(12 meses tras el cierre)"]
    for x, t in zip(xs, top):
        caja2(ax, x, 48, w, 12, t, relleno=E.CAJA, fs=9)
    for i in range(3):
        E.flecha(ax, (xs[i] + w + 0.5, 54), (xs[i + 1] - 0.5, 54), lw=1.5)
    ax.text(50, 63.5, "Cadena de resultados del proyecto", ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=E.TINTA)
    bot = ["Nivel 1\nInformación", "Nivel 2\nConsulta", "Nivel 3\nColaboración activa\n(obligatorio)", "Nivel 4\nEmpoderamiento\n(aspiracional)"]
    rell = [E.CLARO, E.MEDIO, E.MEDIO, E.GRIS]
    for i, (x, t) in enumerate(zip(xs, bot)):
        if i == 3:
            caja2(ax, x, 8, w, 13, t, relleno=rell[i], fs=9, trama="///", ls=(0, (4, 2)))
        else:
            caja2(ax, x, 8, w, 13, t, relleno=rell[i], fs=9, lw=2.4 if i == 2 else 1.2, bold=(i == 2))
    ax.text(3, 5.0, "Niveles de la Escalera ASC", ha="left", va="center", fontsize=9.5, fontweight="bold", color=E.TINTA)
    # enlaces hipotéticos
    E.flecha(ax, (xs[0] + w / 2, 21.6), (xs[1] + 5, 47.4), ls="--")
    E.flecha(ax, (xs[1] + w / 2, 21.6), (xs[1] + w / 2, 47.4), ls="--")
    E.flecha(ax, (xs[2] + w / 2, 21.6), (xs[2] + w / 2, 47.4), ls="--", lw=2.0)
    E.flecha(ax, (xs[3] + 4, 21.6), (xs[2] + w - 3, 47.4), ls="--")
    E.flecha(ax, (xs[3] + w - 4, 21.6), (xs[3] + w - 4, 47.4), ls="--")
    ax.text(xs[0] + 1, 33, "cartillas y\njornadas", fontsize=8, ha="left", va="center", color=E.TINTA)
    ax.text(xs[1] + w / 2 + 1, 33, "actas de\nconsulta", fontsize=8, ha="left", va="center", color=E.TINTA)
    ax.text(xs[2] + w / 2 - 1, 36, "umbrales co-diseñados:\nPERS-E01 y PERS-E02", fontsize=8, ha="right", va="center", color=E.TINTA, fontweight="bold")
    ax.text(xs[3] + 1, 29, "PERS-E03", fontsize=8, ha="left", va="center", color=E.TINTA)
    ax.text(xs[3] + w - 5, 40, "PERS-S02", fontsize=8, ha="right", va="center", color=E.TINTA)
    ax.text(3, 1.6, "Todas las relaciones son hipótesis (INFERIDO) sin efecto estimado. Riesgo asociado: R-ORG-01, comités que no adoptan el tablero (probabilidad de 40 %).",
            fontsize=8.3, ha="left", va="center", color=E.TINTA)
    E.guardar(fig, "c16_f04")


if __name__ == "__main__":
    f01(); f02(); f03(); f04()
    print("ok")
