# -*- coding: utf-8 -*-
"""Figuras del documento 1000X-06 (análisis financiero): cX6_f01 a cX6_f04. Datos: maestro.py vía cX_comun.py. Sin semilla (determinista)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
import estilo as E
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
M = C.MM

def f01():
    mc = C.matriz_costos()
    rubros = list(mc.keys())[::-1]
    dir_ = [mc[r][("Directo", "Fijo")] + mc[r][("Directo", "Variable")] for r in rubros]
    ind = [mc[r][("Indirecto", "Fijo")] + mc[r][("Indirecto", "Variable")] for r in rubros]
    res = [mc[r][("Reserva", "Reserva")] for r in rubros]
    tot = [a + b + c for a, b, c in zip(dir_, ind, res)]
    top2 = (C.RES["por_rubro"]["Personal"] + C.RES["por_rubro"]["Equipos y software"]) / C.SGR
    fig, ax = E.lienzo(h1=f"El personal y los equipos suman {C.pct(top2)} % del valor solicitado al SGR",
                       h2="Valor solicitado al SGR por rubro y clase de costo, millones de pesos colombianos (COP)", figsize=(10, 6.2))
    y = np.arange(len(rubros))
    ax.barh(y, [v / M for v in dir_], color=E.AZUL, edgecolor=E.TINTA, linewidth=0.8, label="Directo")
    ax.barh(y, [v / M for v in ind], left=[v / M for v in dir_], color=E.MEDIO, edgecolor=E.TINTA, linewidth=0.8, hatch="///", label="Indirecto")
    ax.barh(y, [v / M for v in res], left=[(a + b) / M for a, b in zip(dir_, ind)], color=E.CLARO, edgecolor=E.TINTA, linewidth=0.8, hatch="...", label="Reserva de contingencia")
    for i, r in enumerate(rubros):
        ax.annotate(f"{E.num(tot[i] / M, 1)}  ({C.pct(tot[i] / C.SGR)} %)", xy=(tot[i] / M, i), xytext=(5, 0), textcoords="offset points",
                    va="center", ha="left", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.set_yticks(y); ax.set_yticklabels(rubros)
    ax.set_xlim(0, max(tot) / M * 1.25)
    ax.set_xlabel("Millones de COP")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: E.num(v, 0)))
    ax.grid(axis="x", alpha=0.25); ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right", fontsize=9.5)
    E.guardar(fig, "cX6_f01")

def f02():
    filas, pres3, nodo = C.alternativas_costos()
    filas = filas[::-1]
    fig, ax = E.lienzo(h1=f"La estación fija de referencia cuesta {C.num(filas[2]['total'] / filas[0]['total'], 1)} veces el costo por punto de la red híbrida",
                       h2="Costo unitario de la capa de medición por punto, millones de COP (ALT-01 y ALT-02: costo de referencia PROPUESTO)", figsize=(10, 5.6))
    y = np.arange(len(filas))
    comp = [("equipo", "Equipo de medición e instalación", E.AZUL, ""), ("enlace", "Energía y enlace", E.MEDIO, "///"), ("verif", "Verificación frente a referencia", E.CLARO, "...")]
    left = np.zeros(len(filas))
    for k, nom, col, h in comp:
        vals = np.array([f[k] / M for f in filas])
        ax.barh(y, vals, left=left, color=col, edgecolor=E.TINTA, linewidth=0.8, hatch=h, label=nom)
        left += vals
    for i, f in enumerate(filas):
        ax.annotate(f"{E.num(f['total'] / M, 1)}", xy=(f["total"] / M, i), xytext=(5, 0), textcoords="offset points", va="center",
                    fontsize=10.5, fontweight="bold", color=E.TINTA)
    ax.set_yticks(y); ax.set_yticklabels([f"{f['id']}: {f['nombre']}" for f in filas])
    ax.set_xlim(0, 135); ax.set_xlabel("Millones de COP por punto de medición")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: E.num(v, 0)))
    ax.grid(axis="x", alpha=0.25); ax.grid(axis="y", visible=False)
    ax.legend(loc="lower right", fontsize=9.5, bbox_to_anchor=(1.0, 0.0))
    E.guardar(fig, "cX6_f02")

def f03():
    filas, esc, expo = C.sensibilidad()
    filas = filas[::-1]
    mayor = filas[-1]
    fig, ax = E.lienzo(h1=f"El plazo mueve el valor solicitado hasta ±{E.num(mayor['expo'] * 0.2 / M, 1)} millones con una variación de ±20 %",
                       h2="Variación del valor solicitado al SGR frente a la base de 8.729,8 millones de COP, una variable a la vez", figsize=(10, 5.6))
    y = np.arange(len(filas))
    for i, f in enumerate(filas):
        e = f["expo"] / M
        # ±10 % interior y 10 % a 20 % exterior
        ax.barh(i, e * 0.10, left=0, color=E.AZUL, edgecolor=E.TINTA, linewidth=0.8)
        ax.barh(i, e * 0.10, left=e * 0.10, color=E.AZUL, edgecolor=E.TINTA, linewidth=0.8, hatch="///")
        ax.barh(i, -e * 0.10, left=0, color=E.CLARO, edgecolor=E.TINTA, linewidth=0.8)
        ax.barh(i, -e * 0.10, left=-e * 0.10, color=E.CLARO, edgecolor=E.TINTA, linewidth=0.8, hatch="///")
        ax.annotate("+" + E.num(e * 0.20, 1), xy=(e * 0.20, i), xytext=(5, 0), textcoords="offset points", va="center", fontsize=10, fontweight="bold", color=E.TINTA)
        ax.annotate("−" + E.num(e * 0.20, 1), xy=(-e * 0.20, i), xytext=(-5, 0), textcoords="offset points", va="center", ha="right", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.axvline(0, color=E.TINTA, linewidth=1.0)
    ax.set_yticks(y); ax.set_yticklabels([f"{f['nombre']}\n(base expuesta {E.num(f['expo'] / M, 1)})" for f in filas], fontsize=10)
    ax.set_xlim(-1400, 1400); ax.set_xlabel("Variación del valor solicitado, millones de COP")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: E.num(v, 0)))
    ax.grid(axis="x", alpha=0.25); ax.grid(axis="y", visible=False)
    ax.legend(handles=[Patch(fc=E.AZUL, ec=E.TINTA, label="Aumento de 0 a 10 %"), Patch(fc=E.AZUL, ec=E.TINTA, hatch="///", label="Aumento de 10 a 20 %"),
                       Patch(fc=E.CLARO, ec=E.TINTA, label="Reducción de 0 a 10 %"), Patch(fc=E.CLARO, ec=E.TINTA, hatch="///", label="Reducción de 10 a 20 %")],
              loc="upper center", bbox_to_anchor=(0.5, -0.14), fontsize=9, ncol=4)
    E.guardar(fig, "cX6_f03")

def f04():
    meses = np.arange(1, 25)
    s = np.cumsum(C.SGR_MES) / M; c = np.cumsum(C.CON_MES) / M; t = s + c
    tot = t[-1]
    fig, ax = E.lienzo(h1=f"El {C.pct(t[11] / tot)} % de la inversión programada se ejecuta en los primeros 12 meses",
                       h2="Ejecución acumulada programada por mes, millones de COP (distribución uniforme por línea y compras por tramo)", figsize=(10, 6))
    ax.plot(meses, t, color=E.AZUL, linewidth=2.4, marker="o", markersize=5, markeredgecolor=E.TINTA, label="Total del proyecto")
    ax.plot(meses, s, color=E.MEDIO, linewidth=2.0, marker="s", markersize=5, markeredgecolor=E.TINTA, label="SGR")
    ax.plot(meses, c, color=E.CLARO, linewidth=2.0, marker="^", markersize=5.5, markeredgecolor=E.TINTA, linestyle="--", label="Contrapartida")
    ax.annotate(f"Total {E.num(tot, 1)}", xy=(24, tot), xytext=(-4, 8), textcoords="offset points", ha="right", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.annotate(f"SGR {E.num(s[-1], 1)}", xy=(24, s[-1]), xytext=(-4, 8), textcoords="offset points", ha="right", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.annotate(f"Contrapartida {E.num(c[-1], 1)}", xy=(24, c[-1]), xytext=(-4, 8), textcoords="offset points", ha="right", fontsize=10, fontweight="bold", color=E.TINTA)
    for mes, nom in ((12, "C1"), (17, "C2"), (24, "C3")):
        ax.axvline(mes, color=E.TINTA, linewidth=0.8, linestyle=":")
        ax.text(mes - 0.2, tot * 1.075, f"{nom} (mes {mes})", ha="right", va="bottom", fontsize=9.5, color=E.TINTA)
    for tr in C.M.TRAMOS:
        m = tr["mes_compra"]
        ax.annotate(f"Compra del tramo {tr['id']}", xy=(m, t[m - 1]), xytext=(m - 4.2, t[m - 1] + tot * 0.17), fontsize=9,
                    arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.8), color=E.TINTA)
    ax.set_xlim(0.5, 24.8); ax.set_ylim(0, tot * 1.17)
    ax.set_xticks(range(0, 25, 2)); ax.set_xlabel("Mes de ejecución")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: E.num(v, 0)))
    ax.set_ylabel("Millones de COP acumulados")
    ax.legend(loc="upper left", fontsize=9.5)
    E.guardar(fig, "cX6_f04")

if __name__ == "__main__":
    f01(); f02(); f03(); f04()
    print("figuras cX6 generadas")
