# -*- coding: utf-8 -*-
"""Figuras del capítulo 8 (Presupuesto): c8_f01 (distribución presupuestal), c8_f02 (curva S) y c8_f03 (cronograma de desembolsos).
Datos: maestro.py (BUDGET, CONTRA, TRAMOS, flujo_sgr, flujo_contra, resumen). Sin componente aleatorio.
Ejecución: python3 c8_figs.py"""
import os, sys, math, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "maestro")); sys.path.insert(0, os.path.join(RAIZ, "figs"))
import maestro as M
import estilo as E
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

MM = M.M
RES = M.resumen()
SGR, CONTRA, TOTAL = RES["sgr"], RES["contra"], RES["total"]

def pct(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")

def _h2(fig, texto):
    fig.text(0.008, 0.925, texto, fontsize=10, color=E.TINTA, ha="left", va="center")

# ------------------------------------------------------------------ F8.1 distribución
def _pie(ax, valores, etiquetas, colores, hatches, radio_etq=1.28, ang0=90, gap=0.34):
    ws, _ = ax.pie(valores, startangle=ang0, counterclock=False, colors=colores, radius=1.0,
                   wedgeprops=dict(edgecolor=E.TINTA, linewidth=0.9), labels=None)
    for w, h in zip(ws, hatches):
        w.set_hatch(h)
    pos = []
    for i, w in enumerate(ws):
        ang = math.radians((w.theta2 + w.theta1) / 2)
        pos.append([math.cos(ang), math.sin(ang), math.cos(ang) * radio_etq, math.sin(ang) * radio_etq])
    for lado in (1, -1):
        idx = sorted([i for i, p in enumerate(pos) if (p[0] >= 0) == (lado == 1)], key=lambda i: -pos[i][3])
        for k in range(1, len(idx)):
            prev = pos[idx[k - 1]][3]
            if pos[idx[k]][3] > prev - gap: pos[idx[k]][3] = prev - gap
    for i, p in enumerate(pos):
        ha = "left" if p[0] >= 0 else "right"
        xt = p[2] + (0.08 if p[0] >= 0 else -0.08)
        ax.annotate(etiquetas[i], xy=(p[0], p[1]), xytext=(xt, p[3]), ha=ha, va="center", fontsize=8.8, color=E.TINTA,
                    arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.7, shrinkA=0, shrinkB=0))
    ax.set_aspect("equal"); ax.axis("off")

def f01():
    rub = list(RES["por_rubro"].items())
    pers = RES["por_rubro"]["Personal"] / SGR * 100
    fig = plt.figure(figsize=(10, 6.2))
    fig.suptitle(f"El SGR financia {pct(SGR / TOTAL * 100)} % del proyecto y el personal absorbe {pct(pers)} % de lo solicitado",
                 fontsize=14, fontweight="bold", color=E.TINTA, x=0.01, ha="left", y=0.995)
    _h2(fig, "Valor total del proyecto por fuente (izquierda) y valor solicitado al SGR por rubro (derecha); millones de COP y porcentaje")
    a1 = fig.add_axes([0.04, 0.04, 0.38, 0.74]); a2 = fig.add_axes([0.49, 0.04, 0.46, 0.74])
    ies = sum(l["total"] for l in M.CONTRA if l["fuente"] == "IES"); emp = sum(l["total"] for l in M.CONTRA if l["fuente"] == "EMP")
    vals = [SGR, ies, emp]
    et = [f"SGR solicitado\n{M.mm(SGR)} M ({pct(SGR / TOTAL * 100)} %)", f"Contrapartida IES\n{M.mm(ies)} M ({pct(ies / TOTAL * 100)} %)",
          f"Contrapartida empresa\n{M.mm(emp)} M ({pct(emp / TOTAL * 100)} %)"]
    _pie(a1, vals, et, [E.AZUL, E.MEDIO, E.CLARO], ["", "///", "..."], radio_etq=1.25, ang0=90)
    a1.set_xlim(-1.5, 1.5); a1.set_ylim(-1.5, 1.5)
    fig.text(0.04 + 0.19, 0.80, f"Total del proyecto: {M.mm(TOTAL)} M COP", fontsize=10, fontweight="bold", color=E.TINTA, ha="center")
    vr = [v for _, v in rub]
    et2 = [f"{k}\n{M.mm(v)} M ({pct(v / SGR * 100)} %)" for k, v in rub]
    cols = [E.AZUL, E.MEDIO, E.CLARO, E.GRIS, E.AZUL, E.MEDIO, E.CLARO]
    hat = ["", "", "", "", "///", "...", "xx"]
    _pie(a2, vr, et2, cols, hat, radio_etq=1.22, ang0=90)
    a2.set_xlim(-1.5, 1.5); a2.set_ylim(-1.5, 1.5)
    fig.text(0.49 + 0.23, 0.80, f"Valor solicitado al SGR: {M.mm(SGR)} M COP", fontsize=10, fontweight="bold", color=E.TINTA, ha="center")
    return E.guardar(fig, "c8_f01")

# ------------------------------------------------------------------ flujos por grupo (réplica de flujo_sgr)
GRUPOS = ["Personal", "Equipos y software", "Otros rubros de ejecución", "Reserva de contingencia"]
def grupo(l):
    if l["rubro"] == "Personal": return GRUPOS[0]
    if l["rubro"] == "Equipos y software": return GRUPOS[1]
    if l["rubro"] == "Reserva de contingencia": return GRUPOS[3]
    return GRUPOS[2]

def flujo_grupos():
    fg = {g: [0.0] * 24 for g in GRUPOS}
    for r in M.BUDGET:
        if r["id"] in ("E01", "E02", "E04"): continue
        for i, v in enumerate(M.spread(r)): fg[grupo(r)][i] += v
    for i, v in enumerate(M.flujo_equipos_por_tramo()): fg[GRUPOS[1]][i] += v
    tot = [sum(fg[g][i] for g in GRUPOS) for i in range(24)]
    assert all(abs(a - b) < 1e-3 for a, b in zip(tot, M.flujo_sgr())), "los grupos no suman el flujo del maestro"
    return fg, tot

# ------------------------------------------------------------------ F8.2 curva S
def f02():
    fs = M.flujo_sgr(); fc = M.flujo_contra()
    cs = []; cc = []; a = 0; b = 0
    for x, y in zip(fs, fc):
        a += x; b += y; cs.append(a / SGR * 100); cc.append(b / CONTRA * 100)
    meses = list(range(0, 25))
    ys = [0] + cs; yc = [0] + cc
    c1 = cs[11]; c2 = cs[16]
    fig, ax = E.lienzo(h1=f"El SGR se ejecuta {pct(c1)} % hasta la compuerta C1 y {pct(c2)} % hasta C2",
                       h2=None, figsize=(10, 6.2))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.86, bottom=0.11)
    _h2(fig, "Ejecución acumulada por mes, en porcentaje del valor de cada fuente (SGR: 8.729,8 M COP; contrapartida: 2.110,0 M COP)".replace("8.729,8", M.mm(SGR)).replace("2.110,0", M.mm(CONTRA)))
    ax.plot(meses, ys, color=E.AZUL, lw=2.4, marker="o", ms=4.2, mfc=E.AZUL, mec=E.TINTA, mew=0.6, label="SGR", zorder=3)
    ax.plot(meses, yc, color=E.MEDIO, lw=2.0, ls="--", marker="s", ms=3.8, mfc=E.CLARO, mec=E.TINTA, mew=0.6, label="Contrapartida", zorder=2)
    # compuertas
    for t in M.TRAMOS[:2]:
        mes = t["mes_compuerta"]
        ax.axvline(mes, color=E.TINTA, lw=0.9, ls=":", zorder=1)
        ax.text(mes + 0.15, 4, f"{t['compuerta']} (mes {mes})", rotation=90, va="bottom", ha="left", fontsize=8.8, color=E.TINTA)
    # saltos de compra por tramo
    for t in M.TRAMOS:
        mes = t["mes_compra"]
        ax.annotate(f"Compra tramo {t['id']}\n(mes {mes})", xy=(mes, cs[mes - 1]), xytext=(mes - 3.6 if t["id"] != 1 else mes - 3.4, cs[mes - 1] + (13 if t["id"] != 1 else 14)),
                    fontsize=8.4, color=E.TINTA, ha="center", arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.7))
    ax.annotate(f"SGR: {pct(cs[11])} %\nen el mes 12", xy=(12, cs[11]), xytext=(12.5, cs[11] - 20), fontsize=8.8, color=E.TINTA, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.7))
    ax.annotate(f"SGR: {pct(cs[16])} % en el mes 17", xy=(17, cs[16]), xytext=(19.0, cs[16] - 17), fontsize=8.8, color=E.TINTA, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.7))
    ax.text(24.2, 100, "SGR 100 %", fontsize=9, fontweight="bold", color=E.TINTA, va="center", ha="left")
    ax.text(24.2, 93.0, "Contrapartida\n100 %", fontsize=8.6, color=E.TINTA, va="center", ha="left")
    ax.set_xlim(0, 24); ax.set_ylim(0, 105)
    ax.set_xticks(range(0, 25, 2)); ax.set_xlabel("Mes de ejecución", fontsize=10)
    ax.set_ylabel("Ejecución acumulada (%)", fontsize=10)
    ax.set_yticks(range(0, 101, 20))
    ax.grid(axis="y")
    fig.subplots_adjust(right=0.88)
    ax.legend(loc="upper left", fontsize=9, bbox_to_anchor=(0.01, 0.97))
    return E.guardar(fig, "c8_f02")

# ------------------------------------------------------------------ F8.3 desembolsos
def f03():
    fg, tot = flujo_grupos()
    top = sorted(range(24), key=lambda i: -tot[i])[:3]
    meses_pico = sorted(i + 1 for i in top)
    compras = sorted(t["mes_compra"] for t in M.TRAMOS)
    assert meses_pico == compras, (meses_pico, compras)
    fig, ax = E.lienzo(h1=f"Tres picos de desembolso coinciden con las compras de los tramos 1, 2 y 3 (meses {meses_pico[0]}, {meses_pico[1]} y {meses_pico[2]})",
                       h2=None, figsize=(10, 6.4))
    fig.subplots_adjust(left=0.085, right=0.98, top=0.85, bottom=0.2)
    _h2(fig, "Desembolso mensual del SGR por grupo de rubros, en millones de COP (modelo de flujo de maestro.py)")
    x = list(range(1, 25)); base = [0.0] * 24
    estilos = [(E.AZUL, ""), (E.MEDIO, "///"), (E.CLARO, "..."), (E.GRIS, "xx")]
    for g, (c, h) in zip(GRUPOS, estilos):
        v = [z / MM for z in fg[g]]
        ax.bar(x, v, bottom=base, color=c, edgecolor=E.TINTA, linewidth=0.6, hatch=h, width=0.78, label=g, zorder=3)
        base = [a + b for a, b in zip(base, v)]
    for i in top:
        ax.annotate(f"{M.mm(tot[i])}", xy=(i + 1, tot[i] / MM), xytext=(0, 4), textcoords="offset points", ha="center", fontsize=9, fontweight="bold", color=E.TINTA)
    for t in M.TRAMOS[:2]:
        ax.axvline(t["mes_compuerta"] + 0.5, color=E.TINTA, lw=0.9, ls=":", zorder=1)
        ax.text(t["mes_compuerta"] + 0.38, max(base) * 1.08, f"{t['compuerta']}, mes {t['mes_compuerta']}", fontsize=8.8, color=E.TINTA, va="center", ha="right")
    ax.set_xticks(x); ax.set_xlabel("Mes de ejecución", fontsize=10); ax.set_ylabel("Millones de COP por mes", fontsize=10)
    ax.set_ylim(0, max(base) * 1.12)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=4, fontsize=8.8, handlelength=1.6)
    return E.guardar(fig, "c8_f03")

if __name__ == "__main__":
    print(f01()); print(f02()); print(f03())
