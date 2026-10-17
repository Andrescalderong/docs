# -*- coding: utf-8 -*-
"""Figuras del documento 1000X-09 (tablero de riesgos): cX9_f01 a cX9_f04. Datos: registro de riesgos de maestro.py (ficha §7).
La tendencia es una hipótesis PROPUESTA (reglas en cX_comun.py). Sin semilla (determinista)."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
import estilo as E
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Rectangle
M = C.MM
NIV = ["EXTREMO", "ALTO", "MEDIO", "BAJO"]
COL = {"EXTREMO": (E.AZUL, "xx"), "ALTO": (E.MEDIO, "///"), "MEDIO": (E.CLARO, "..."), "BAJO": (E.GRIS, "")}
CAT_ORDEN = ["Técnico", "Organizacional", "Externo", "Financiero", "Jurídico", "Datos"]

def corto(i):
    return i[2:]

def f01():
    rn = C.riesgos_por_nivel()
    n = {k: len(v) for k, v in rn.items()}
    rojo, amar, verde = n["EXTREMO"] + n["ALTO"], n["MEDIO"], n["BAJO"]
    fig = plt.figure(figsize=(10, 6.4))
    fig.suptitle(f"{rojo} de los {len(C.RIESGOS)} riesgos están en rojo y ninguno se ha materializado al inicio", fontsize=14, fontweight="bold",
                 color=E.TINTA, x=0.01, ha="left", y=0.995)
    gs = fig.add_gridspec(2, 2, height_ratios=[0.8, 2.2], hspace=0.38, wspace=0.28)
    # tarjetas de indicadores
    axk = fig.add_subplot(gs[0, :]); axk.set_xlim(0, 100); axk.set_ylim(0, 20); axk.axis("off")
    axk.set_title("Indicadores del registro de riesgos al inicio de la ejecución (línea base de formulación), número de riesgos", fontsize=10, loc="left", color=E.TINTA, pad=8)
    kp = [("Identificados", len(C.RIESGOS)), ("Activos", len(C.RIESGOS)), ("Materializados", 0), ("Mitigados", 0)]
    for i, (nom, v) in enumerate(kp):
        x0 = 1 + i * 24.5
        E.caja(axk, x0, 2, 21, 14, "", relleno=E.CAJA)
        axk.text(x0 + 10.5, 11.2, str(v), ha="center", va="center", fontsize=24, fontweight="bold", color=E.TINTA)
        axk.text(x0 + 10.5, 5.0, nom, ha="center", va="center", fontsize=11, color=E.TINTA)
    # semáforo
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.set_title("Semáforo por puntaje P×I, número de riesgos", fontsize=10, loc="left", color=E.TINTA, pad=10)
    nombres = ["ROJO\nP×I ≥ 12\n(EXTREMO y ALTO)", "AMARILLO\nP×I de 6 a 11\n(MEDIO)", "VERDE\nP×I ≤ 5\n(BAJO)"]
    stack = [(n["EXTREMO"], n["ALTO"]), (n["MEDIO"], 0), (n["BAJO"], 0)]
    x = np.arange(3)
    ax1.bar(x, [s[0] for s in stack], color=[COL["EXTREMO"][0], COL["MEDIO"][0], COL["BAJO"][0]], edgecolor=E.TINTA, linewidth=0.8,
            hatch=None)
    for i, h in enumerate([COL["EXTREMO"][1], COL["MEDIO"][1], COL["BAJO"][1]]):
        ax1.patches[i].set_hatch(h)
    ax1.bar([0], [n["ALTO"]], bottom=[n["EXTREMO"]], color=COL["ALTO"][0], edgecolor=E.TINTA, linewidth=0.8, hatch=COL["ALTO"][1])
    for i, tot in enumerate([rojo, amar, verde]):
        ax1.annotate(str(tot), xy=(i, tot), xytext=(0, 4), textcoords="offset points", ha="center", fontsize=13, fontweight="bold", color=E.TINTA)
    ax1.text(0, n["EXTREMO"] / 2, f"EXTREMO {n['EXTREMO']}", ha="center", va="center", fontsize=8.5, color=E.TINTA, bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85))
    ax1.text(0, n["EXTREMO"] + n["ALTO"] / 2, f"ALTO {n['ALTO']}", ha="center", va="center", fontsize=8.5, color=E.TINTA, bbox=dict(fc="white", ec="none", pad=1.5, alpha=0.85))
    ax1.set_xticks(x); ax1.set_xticklabels(nombres, fontsize=9)
    ax1.set_ylim(0, 10.2); ax1.grid(axis="y")
    # por categoría
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.set_title("Riesgos por categoría y nivel, número de riesgos", fontsize=10, loc="left", color=E.TINTA, pad=10)
    cat = collections.OrderedDict((c, collections.Counter()) for c in CAT_ORDEN)
    for r in C.RIESGOS: cat[r["cat"]][r["nivel"]] += 1
    y = np.arange(len(CAT_ORDEN))[::-1]
    left = np.zeros(len(CAT_ORDEN))
    for nv in NIV[:3]:
        vals = np.array([cat[c][nv] for c in CAT_ORDEN], dtype=float)
        ax2.barh(y, vals, left=left, color=COL[nv][0], edgecolor=E.TINTA, linewidth=0.8, hatch=COL[nv][1], label=nv)
        left += vals
    for yi, c in zip(y, CAT_ORDEN):
        ax2.annotate(str(sum(cat[c].values())), xy=(sum(cat[c].values()), yi), xytext=(5, 0), textcoords="offset points", va="center", fontsize=10.5, fontweight="bold", color=E.TINTA)
    ax2.set_yticks(y); ax2.set_yticklabels(CAT_ORDEN, fontsize=10)
    ax2.set_xlim(0, 5.2); ax2.grid(axis="x", alpha=0.25); ax2.grid(axis="y", visible=False)
    ax2.legend(loc="lower right", fontsize=9)
    E.guardar(fig, "cX9_f01")

def f02():
    cel = C.celdas_matriz()
    fig, ax = plt.subplots(figsize=(10, 7))
    n_alto = sum(1 for r in C.RIESGOS if r["nivel"] in ("ALTO", "EXTREMO"))
    fig.suptitle(f"{n_alto} de los {len(C.RIESGOS)} riesgos ocupan celdas de nivel ALTO o EXTREMO en la matriz 5×5", fontsize=14, fontweight="bold", color=E.TINTA, x=0.01, ha="left", y=0.995)
    ax.set_title("Posición por probabilidad (P) e impacto (I) de la ficha; nivel según P×I (EXTREMO ≥ 20, ALTO 12 a 19, MEDIO 6 a 11, BAJO < 6)",
                 fontsize=9, loc="left", color=E.TINTA, pad=12)
    for p in range(1, 6):
        for i in range(1, 6):
            nv = C.nivel_de(p * i)
            col, h = COL[nv]
            ax.add_patch(Rectangle((i - 0.5, p - 0.5), 1, 1, fc=col, ec=E.TINTA, lw=0.9, hatch=h))
            ax.text(i + 0.43, p - 0.43, str(p * i), ha="right", va="bottom", fontsize=8.5, color=E.TINTA)
            ids = cel.get((p, i), [])
            if ids:
                txt = "\n".join(corto(k) for k in ids)
                ax.text(i, p + 0.02, txt, ha="center", va="center", fontsize=9.5, fontweight="bold", color=E.TINTA,
                        bbox=dict(fc="white", ec=E.TINTA, lw=0.6, boxstyle="round,pad=0.25"))
    ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xlabel("Impacto (I), escala de 1 a 5"); ax.set_ylabel("Probabilidad (P), escala de 1 a 5")
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.set_aspect("equal")
    ax.legend(handles=[Patch(fc=COL[n][0], ec=E.TINTA, hatch=COL[n][1], label=n) for n in NIV], loc="upper left", bbox_to_anchor=(1.02, 1.0), fontsize=10, title="Nivel", title_fontsize=10)
    E.guardar(fig, "cX9_f02")

def f03():
    filas, idx = C.tendencia()
    etiquetas = ["Inicio\n(mes 0)", "Cierre tramo 1\n(C1, mes 12)", "Cierre tramo 2\n(C2, mes 17)", "Cierre tramo 3\n(C3, mes 24)"]
    comp = [collections.Counter() for _ in idx]
    for f in filas:
        for k, v in enumerate(f["vals"]):
            if v > 0: comp[k][C.nivel_de(v)] += v
    fig, ax = E.lienzo(h1=f"El índice de riesgo planificado baja de {idx[0]} a {idx[-1]} puntos, una reducción de {C.pct(1 - idx[-1] / idx[0], 1)} %",
                       h2="Índice de riesgo = suma de P×I de los riesgos abiertos, por nivel; trayectoria PROPUESTA, no medida", figsize=(10, 6))
    x = np.arange(len(idx)); bottom = np.zeros(len(idx))
    for nv in NIV[:3]:
        vals = np.array([comp[k][nv] for k in range(len(idx))], dtype=float)
        ax.bar(x, vals, bottom=bottom, color=COL[nv][0], edgecolor=E.TINTA, linewidth=0.8, hatch=COL[nv][1], width=0.55, label=nv)
        for k in range(len(idx)):
            if vals[k] > 0: ax.text(x[k], bottom[k] + vals[k] / 2, f"{int(vals[k])}", ha="center", va="center", fontsize=9, color=E.TINTA,
                                    bbox=dict(fc="white", ec="none", pad=1.2, alpha=0.85))
        bottom += vals
    for k, v in enumerate(idx):
        rel = v / idx[0] * 100
        ant = "" if k == 0 else f"  ({'−' if v < idx[k-1] else '+'}{abs(v - idx[k-1])} frente al punto anterior)"
        ax.annotate(f"{v} puntos\n{C.pct(v / idx[0], 1)} % del inicio" if k else f"{v} puntos\n100,0 % del inicio", xy=(k, v), xytext=(0, 5), textcoords="offset points",
                    ha="center", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.set_xticks(x); ax.set_xticklabels(etiquetas, fontsize=10)
    ax.set_ylim(0, idx[0] * 1.22); ax.set_ylabel("Puntos del índice de riesgo")
    ax.legend(loc="upper right", fontsize=9.5, title="Nivel del riesgo", title_fontsize=9.5)
    E.guardar(fig, "cX9_f03")

def f04():
    riesgos = sorted(C.RIESGOS, key=lambda r: (r["emv"], r["id"]))
    top = {r["id"] for r in C.top5()}
    suma = sum(r["emv"] for r in C.RIESGOS)
    fig, ax = E.lienzo(h1=f"La reserva de {E.num(C.RES['reserva'] / M, 1)} millones está disponible en su totalidad al inicio",
                       h2="Valor monetario esperado (EMV) por riesgo, millones de COP; la reserva redondeada es la suma de los 12 EMV", figsize=(10, 6.2))
    y = np.arange(len(riesgos))
    for i, r in enumerate(riesgos):
        ax.barh(i, r["emv"] / M, color=E.AZUL if r["id"] in top else E.CLARO, edgecolor=E.TINTA, linewidth=0.8, hatch="" if r["id"] in top else "...")
        ax.annotate(E.num(r["emv"] / M, 1), xy=(r["emv"] / M, i), xytext=(5, 0), textcoords="offset points", va="center", fontsize=9.5, fontweight="bold", color=E.TINTA)
    ax.set_yticks(y); ax.set_yticklabels([r["id"] for r in riesgos], fontsize=9.5)
    ax.set_xlim(0, 230); ax.set_xlabel("EMV, millones de COP")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: E.num(v, 0)))
    ax.grid(axis="x", alpha=0.25); ax.grid(axis="y", visible=False)
    ax.legend(handles=[Patch(fc=E.AZUL, ec=E.TINTA, label="Cinco riesgos principales"), Patch(fc=E.CLARO, ec=E.TINTA, hatch="...", label="Otros siete riesgos")],
              loc="lower right", fontsize=9.5, bbox_to_anchor=(1.0, 0.30))
    cuadro = (f"Reserva total: {E.num(C.RES['reserva'] / M, 1)}\nUtilizada: {E.num(0, 1)}\nDisponible: {E.num(C.RES['reserva'] / M, 1)}\n"
              f"Suma de EMV sin redondeo: {E.num(suma / M, 1)}")
    ax.text(0.98, 0.04, cuadro, transform=ax.transAxes, ha="right", va="bottom", fontsize=10.5, fontweight="bold", color=E.TINTA, linespacing=1.5,
            bbox=dict(fc=E.CAJA, ec=E.TINTA, lw=1.0, boxstyle="round,pad=0.5"))
    E.guardar(fig, "cX9_f04")

if __name__ == "__main__":
    f01(); f02(); f03(); f04()
    print("figuras cX9 generadas")
