# -*- coding: utf-8 -*-
"""Figura cX8_f01: matriz poder-interés de los 18 interesados (posiciones PROPUESTAS, escala de 1 a 10). Determinista."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
import cX8_datos as D
import estilo as E
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

def main():
    fig = plt.figure(figsize=(10, 7))
    n_cerca = int(D.V["n_cerca"]); n = int(D.V["n_total"])
    fig.suptitle(f"{n_cerca} de {n} interesados exigen gestión cercana y las alcaldías deben pasar a ese cuadrante antes de C2", fontsize=13.5,
                 fontweight="bold", color=E.TINTA, x=0.01, ha="left", y=0.995)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.55, 1], wspace=0.04)
    ax = fig.add_subplot(gs[0]); axl = fig.add_subplot(gs[1]); axl.axis("off"); axl.set_xlim(0, 1); axl.set_ylim(0, 1)
    ax.set_title("Posición PROPUESTA por poder e interés, escala de 1 a 10 (alto = 6 o más)", fontsize=9.5, loc="left", color=E.TINTA, pad=10)
    ax.set_xlim(0, 11); ax.set_ylim(0, 11.3)
    u = D.UMBRAL - 0.5
    fills = {"Gestionar de cerca": (E.CLARO, "..."), "Mantener satisfecho": (E.GRIS, ""), "Mantener informado": (E.GRIS, ""), "Monitorear": (E.BLANCO, "")}
    ax.add_patch(Rectangle((u, u), 11 - u, 11.3 - u, fc=E.CLARO, ec="none", alpha=0.55, hatch="...", zorder=0))
    ax.add_patch(Rectangle((0, u), u, 11.3 - u, fc=E.GRIS, ec="none", zorder=0))
    ax.add_patch(Rectangle((u, 0), 11 - u, u, fc=E.GRIS, ec="none", zorder=0))
    ax.axvline(u, color=E.TINTA, linewidth=1.0); ax.axhline(u, color=E.TINTA, linewidth=1.0)
    for txt, x, y, ha in (("MANTENER SATISFECHO", 0.15, 10.95, "left"), ("GESTIONAR DE CERCA", 10.85, 10.95, "right"),
                          ("MONITOREAR", 0.15, 0.4, "left"), ("MANTENER INFORMADO", 10.85, 0.4, "right")):
        ax.text(x, y, txt, ha=ha, va="center", fontsize=9, fontweight="bold", color=E.TINTA, bbox=dict(fc="white", ec="none", pad=2.0, alpha=0.9), zorder=5)
    # nota: eje x = interés, eje y = poder; "mantener informado" = interés alto y poder bajo (abajo a la derecha)
    marc = {"Interno": ("o", E.AZUL), "Externo primario": ("s", E.MEDIO), "Externo secundario": ("^", E.CLARO)}
    pos = {}
    for s in D.S:
        sid, grupo, _, _, _, poder, inter, corto = s
        m, col = marc[grupo]
        ax.scatter(inter, poder, marker=m, s=360, c=col, edgecolors=E.TINTA, linewidths=1.0, zorder=3)
        ax.annotate(sid, xy=(inter, poder), xytext=(0, 0), textcoords="offset points", ha="center", va="center", fontsize=7.6, fontweight="bold", color=E.TINTA, zorder=4)
        pos[sid] = (inter, poder)
    # movimiento buscado de las alcaldías (S10): de interés 4 a interés 7
    ax.annotate("", xy=(5.7, 8), xytext=(4.4, 8), arrowprops=dict(arrowstyle="-|>", color=E.TINTA, lw=1.3, ls="--"), zorder=2)
    ax.text(3.0, 8.8, "Meta antes de C2", ha="center", fontsize=8.5, color=E.TINTA)
    ax.set_xlabel("Interés (1 a 10)"); ax.set_ylabel("Poder (1 a 10)")
    ax.set_xticks(range(1, 11)); ax.set_yticks(range(1, 11)); ax.grid(False)
    # leyenda lateral
    axl.text(0.0, 0.995, "Interesados", fontsize=9.5, fontweight="bold", color=E.TINTA, va="top")
    y = 0.955
    for s in D.S:
        axl.text(0.0, y, f"{s[0]}  {s[7]}", fontsize=8.3, color=E.TINTA, va="top")
        y -= 0.0455
    axl.legend(handles=[Line2D([0], [0], marker="o", color="none", markerfacecolor=E.AZUL, markeredgecolor=E.TINTA, markersize=9, label="Interno"),
                        Line2D([0], [0], marker="s", color="none", markerfacecolor=E.MEDIO, markeredgecolor=E.TINTA, markersize=9, label="Externo primario"),
                        Line2D([0], [0], marker="^", color="none", markerfacecolor=E.CLARO, markeredgecolor=E.TINTA, markersize=9, label="Externo secundario")],
               loc="lower left", bbox_to_anchor=(0.0, -0.02), fontsize=8.5, frameon=False)
    E.guardar(fig, "cX8_f01")

if __name__ == "__main__":
    main()
    print("figura cX8_f01 generada")
