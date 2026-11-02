# -*- coding: utf-8 -*-
"""Figuras del capítulo 14 (Sostenibilidad). Genera c14_f01 y c14_f02 en figs/out/ (png y svg, fondo transparente).
Datos: sección 4.4-MDR.10 (cifras del expediente E3, PROPUESTO y NO_VERIFICADO). Sin parámetros aleatorios."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import estilo as E
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.pyplot as plt

T = E.TINTA


def caja2(ax, x, y, w, h, texto, relleno=E.CAJA, ls="-", fs=8.2, bold=False, lw=1.2):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=T, lw=lw, ls=ls)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=T,
            fontweight="bold" if bold else "normal", linespacing=1.25)


def f01():
    fig = plt.figure(figsize=(10, 5.8))
    fig.suptitle("Una sola fuente en especie concentra 63,2 % del costo parcial declarado en el año 1", fontsize=14,
                 fontweight="bold", color=T, x=0.01, ha="left", y=0.995)
    ax = fig.add_axes([0.07, 0.17, 0.45, 0.63])
    anios = ["Año 1", "Año 2", "Año 3"]
    ies = [120.00, 126.00, 132.30]
    arl = [25.00, 35.00, 45.00]
    tic = [45.00, 47.25, 49.61]
    tot = [190.00, 208.25, 226.91]
    maxp = ["63,2 %", "60,5 %", "58,3 %"]
    hhi = ["0,472", "0,446", "0,427"]
    x = range(3)
    b1 = ax.bar(x, ies, color=E.AZUL, edgecolor=T, width=0.55, label="IES y UNGRD en especie")
    b2 = ax.bar(x, arl, bottom=ies, color=E.MEDIO, edgecolor=T, width=0.55, hatch="///", label="ARL y corporación autónoma")
    b3 = ax.bar(x, tic, bottom=[a + b for a, b in zip(ies, arl)], color=E.CLARO, edgecolor=T, width=0.55, hatch="...",
                label="Secretarías TIC municipales")
    for i in x:
        ax.text(i, ies[i] / 2, E.num(ies[i], 2), ha="center", va="center", fontsize=8.5, fontweight="bold", color=T,
                bbox=dict(boxstyle="round,pad=0.2", fc=E.BLANCO, ec="none"))
        ax.text(i, ies[i] + arl[i] / 2, E.num(arl[i], 2), ha="center", va="center", fontsize=8.5, fontweight="bold", color=T,
                bbox=dict(boxstyle="round,pad=0.2", fc=E.BLANCO, ec="none"))
        ax.text(i, ies[i] + arl[i] + tic[i] / 2, E.num(tic[i], 2), ha="center", va="center", fontsize=8.5, fontweight="bold",
                color=T, bbox=dict(boxstyle="round,pad=0.2", fc=E.BLANCO, ec="none"))
        ax.text(i, tot[i] + 6, f"Total {E.num(tot[i], 2)}", ha="center", va="bottom", fontsize=9, fontweight="bold", color=T)
    ax.set_xticks(list(x)); ax.set_xticklabels([f"{a}\nMáx. {m}; HHI {h}" for a, m, h in zip(anios, maxp, hhi)], fontsize=8.5)
    ax.set_ylim(0, 300); ax.set_yticks([0, 50, 100, 150, 200]); ax.set_yticklabels(["0", "50", "100", "150", "200"], fontsize=8.5)
    ax.set_title("Costo parcial declarado por fuente, años 1 a 3 posproyecto\nMillones de COP; CALCULADO, NO_VERIFICADO",
                 fontsize=9.5, loc="left", pad=8, color=T, fontweight="bold")
    ax.legend(loc="upper left", fontsize=8, frameon=False)
    # panel derecho
    bx = fig.add_axes([0.66, 0.17, 0.31, 0.63])
    fuentes = [("IES y UNGRD\nen especie", 70), ("Secretarías TIC\nmunicipales", 145), ("ARL y corporación\nautónoma", 165)]
    fuentes = fuentes[::-1]
    ys = range(3)
    bars = bx.barh(list(ys), [f[1] for f in fuentes], color=E.MEDIO, edgecolor=T, height=0.55)
    bars[-1].set_hatch("///")
    bars[-1].set_facecolor(E.CLARO)
    for b, f in zip(bars, fuentes):
        bx.annotate(f"{f[1]}", xy=(b.get_width(), b.get_y() + b.get_height() / 2), xytext=(4, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=9, fontweight="bold", color=T)
    bx.set_yticks(list(ys)); bx.set_yticklabels([f[0] for f in fuentes], fontsize=8.5)
    bx.set_xlim(0, 210); bx.set_xticks([0, 50, 100, 150]); bx.set_xticklabels(["0", "50", "100", "150"], fontsize=8.5)
    bx.grid(axis="x"); bx.grid(axis="y", visible=False)
    bx.set_title("Prueba de orfandad, año 1\nSuma de las demás fuentes (millones de COP; CALCULADO)", fontsize=9.5, loc="left",
                 pad=8, color=T, fontweight="bold")
    bx.set_xlabel("Una fuente es CRITICA si el costo mínimo anual supera este valor.\nEl costo mínimo es NO_CALCULABLE.", fontsize=8)
    fig.text(0.01, 0.004, "Elaboración propia con la sección 4.4-MDR.10. HHI: índice de Herfindahl-Hirschman. Trama: fuente en especie con la menor suma de las demás.",
             fontsize=7.8, color=T)
    return E.guardar(fig, "c14_f01")


def f02():
    fig, ax = E.lienzo_libre(h1="Cada componente posee candidatos a custodio y ninguno está asignado todavía",
                             h2="Ecosistema de sostenibilidad según 4.4-MDR.10 (PROPUESTO); custodio asignado: POR_DEFINIR con el ICAR",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))

    def flecha(p0, p1, ls="-"):
        ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="<|-|>", mutation_scale=10, color=T, lw=1.3, ls=ls))

    caja2(ax, 33, 30, 34, 12, "Servicio de vigilancia de\nPM2,5 y PM10 con\ncustodia distribuida", relleno=E.AZUL, fs=9.5, bold=True)
    sup = [(3, "Nodos y repuestos", "Candidatos: empresa aliada\ne institución ejecutora"),
           (36.5, "Gemelo digital y datos", "Candidatos: institución ejecutora\ny empresa aliada"),
           (70, "Tablero y alertas", "Candidatos: unidades de gestión\ndel riesgo y alcaldías")]
    for x, t1, d in sup:
        caja2(ax, x, 50, 27, 12, f"{t1}\n{d}", relleno=E.MEDIO, fs=8.2)
    flecha((40, 42.5), (16.5, 49.5)); flecha((50, 42.5), (50, 49.5)); flecha((60, 42.5), (83.5, 49.5))
    inf = [(12, "Protocolo de calibración", "Candidatos: autoridad ambiental\ne institución ejecutora"),
           (61, "Gobernanza y acuerdos", "Órgano de gobierno\nde la alianza")]
    for x, t1, d in inf:
        caja2(ax, x, 10, 27, 12, f"{t1}\n{d}", relleno=E.MEDIO, fs=8.2)
    flecha((42, 29.5), (25.5, 22.5)); flecha((58, 29.5), (74.5, 22.5))
    caja2(ax, 1, 30, 27, 12, "Comunidad y operarios\nUsuarios y red de soporte\n(escalera ASC, niveles 3 y 4)", relleno=E.CLARO, ls=(0, (4, 2)), fs=8.2)
    caja2(ax, 72, 30, 27, 12, "Financiación posproyecto\nPortafolio condicionado\n(CANDIDATO_A_VERIFICAR)", relleno=E.CLARO, ls=(0, (4, 2)), fs=8.2)
    flecha((28.6, 36), (32.4, 36), ls=(0, (4, 2))); flecha((71.4, 36), (67.6, 36), ls=(0, (4, 2)))
    ax.text(50, 5.0, "Sin custodio que cumpla la condición de recepción, el componente permanece bajo la alianza\no pasa a la cláusula de apertura.",
            ha="center", va="center", fontsize=8.2, color=T)
    ax.text(50, 65.5, "Cinco componentes con custodia distribuida", ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    return E.guardar(fig, "c14_f02")


if __name__ == "__main__":
    for f in (f01, f02):
        print(f())
