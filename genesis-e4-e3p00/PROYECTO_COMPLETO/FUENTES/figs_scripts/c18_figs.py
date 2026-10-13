# -*- coding: utf-8 -*-
"""Figura del capítulo 18 (Marco Lógico): c18_f01 (diagrama de coherencia vertical y horizontal).
Datos: indicadores.py (MARCO_LOGICO, IND), maestro.py (ACT, RISKS) mediante a11_datos.py; las ocho pruebas se calculan en a11_datos.pruebas().
Ejecución: python3 c18_figs.py  (diagrama sin componente aleatorio; sin semilla)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11_datos as D
import estilo as E
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

PAL = {0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho"}

def caja(ax, x, y, w, h, texto, relleno=E.CAJA, borde=E.TINTA, fs=8.2, bold=False, lw=1.2, ls="-", hatch=None):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=borde, lw=lw, ls=ls, hatch=hatch)
    ax.add_patch(p)
    kw = dict(bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.92)) if hatch else {}
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA,
            fontweight="bold" if bold else "normal", linespacing=1.25, **kw)

def flecha(ax, p0, p1, lw=1.4, ls="-", head=True):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>" if head else "-", mutation_scale=11, color=E.TINTA, lw=lw, ls=ls,
                                 shrinkA=0, shrinkB=0))

def estilo_estado(est):
    if est == "CUMPLE":
        return dict(relleno=E.CLARO, borde=E.AZUL, hatch=None, lw=1.6)
    return dict(relleno=E.GRIS, borde=E.TINTA, hatch="///", lw=1.6)

def f01():
    P = {p["id"]: p for p in D.PRUEBAS}
    assert len(D.PRUEBAS) == 8
    h1 = f"{PAL[D.N_CUMPLE].capitalize()} de ocho pruebas de coherencia cumplen y {PAL[D.N_PARCIAL]} cumplen parcialmente"
    fig, ax = E.lienzo_libre(
        h1=h1,
        h2="Matriz 4 × 4 del marco lógico; pruebas verticales V1 a V4 y horizontales H1 a H4; estados CALCULADOS desde indicadores, cronograma y riesgos",
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    cols = [(11, 25), (39, 17), (59, 19), (81, 18.5)]
    enc = ["Resumen narrativo", "Indicadores", "Medios de verificación", "Supuestos"]
    for (x, w), t in zip(cols, enc):
        ax.text(x + w / 2, 67.6, t, ha="center", va="center", fontsize=9.6, fontweight="bold", color=E.TINTA)
    ni = {n: len(v) for n, v in D.NIVEL_IND.items()}
    nA = {w: len(v) for w, v in D.ACT_WP.items()}
    filas = [
        ("Fin", ["Menor exposición evitable\nmediante alertas basadas\nen mediciones verificadas", f"PERS-S01 y S02\n({ni['Fin']} indicadores)",
                 "Evaluación externa\nposproyecto", "SC-4: custodia con\npartida y competencia"]),
        ("Propósito", ["Comités deciden alertas con\nmediciones verificadas de\nPM2,5 y PM10 (100 nodos)", f"PERS-E01 a E03\n({ni['Propósito']} indicadores)",
                       "Actas de comité, registro\nde alertas y evaluaciones\nprácticas", "SC-1, SC-2 y SC-3: modelo,\nenergía y enlace, uso"]),
        ("Componentes", ["Modelo validado, red operativa\ny tablero con convenios\nde custodia", f"PERS-P01 a P04\n({ni['Componentes']} indicadores)",
                         "Inventario, certificado DNDA,\ncartas de aceptación y actas", "Equipos llegan en los\nplazos de importación"]),
        ("Actividades", [f"{len(D.M.ACT)} actividades en cuatro\npaquetes (WP0 {nA['WP0']}, WP1 {nA['WP1']},\nWP2 {nA['WP2']}, WP3 {nA['WP3']})", f"PERS-R01 a R06\n({ni['Actividades']} indicadores)",
                         "Informes de seguimiento\ny soportes financieros", "Acceso en ventanas secas\ny contratación oportuna"]),
    ]
    ys = [51, 38, 25, 12]; h = 8.6
    for (nivel, textos), y in zip(filas, ys):
        caja(ax, 0.8, y, 8.4, h, nivel, relleno=E.MEDIO, borde=E.AZUL, fs=8.0, bold=True, lw=1.6)
        for k, ((x, w), t) in enumerate(zip(cols, textos)):
            caja(ax, x, y, w, h, t, relleno=E.BLANCO if k else E.CAJA, borde=E.AZUL if k != 3 else E.TINTA, fs=7.5, lw=1.1)
        for k in range(3):
            x0 = cols[k][0] + cols[k][1] + 0.4; x1 = cols[k + 1][0] - 0.4
            flecha(ax, (x0, y + h / 2), (x1, y + h / 2), lw=1.0)
    # pruebas verticales (flechas ascendentes entre filas, columna de resumen)
    vert = [("V3", ys[0], ys[1]), ("V2", ys[1], ys[2]), ("V1", ys[2], ys[3])]
    cx = cols[0][0] + cols[0][1] / 2
    for pid, ysup, yinf in vert:
        yb = ysup - 0.4; ya = yinf + h + 0.4
        flecha(ax, (cx, ya), (cx, yb), lw=1.8)
        est = P[pid]["estado"]
        st = estilo_estado(est)
        caja(ax, cx + 2.4, (ya + yb) / 2 - 1.5, 31, 3.0, f"{pid} {P[pid]['nombre']}: {est}", relleno=st["relleno"], borde=st["borde"], fs=6.9, lw=1.3, hatch=st["hatch"])
    # V4 sobre la columna de supuestos
    x4 = cols[3][0] + cols[3][1] / 2
    st = estilo_estado(P["V4"]["estado"])
    caja(ax, cols[3][0] - 0.5, 62.2, cols[3][1] + 0.8, 3.0, f"V4 Supuestos por nivel: {P['V4']['estado']}", relleno=st["relleno"], borde=st["borde"], fs=6.9, lw=1.3, hatch=st["hatch"])
    # pruebas horizontales (franja inferior)
    ax.text(0.8, 8.6, "Pruebas horizontales (H1 a H4)", ha="left", va="center", fontsize=8.6, fontweight="bold", color=E.TINTA)
    xs = [1.5, 26, 50.5, 75]; wid = 23.5
    for pid, x in zip(["H1", "H2", "H3", "H4"], xs):
        est = P[pid]["estado"]; st = estilo_estado(est)
        caja(ax, x, 1.2, wid, 5.0, f"{pid} {P[pid]['nombre']}\n{est}", relleno=st["relleno"], borde=st["borde"], fs=7.0, lw=1.3, hatch=st["hatch"])
    E.guardar(fig, "c18_f01")

if __name__ == "__main__":
    f01(); print("ok")
