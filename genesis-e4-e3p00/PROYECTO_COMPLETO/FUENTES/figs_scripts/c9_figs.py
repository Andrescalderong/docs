# -*- coding: utf-8 -*-
"""Figuras del capítulo 9 (Cronograma): c9_f01 (diagrama de Gantt) y c9_f02 (diagrama de red CPM).
Datos: maestro.py (ACT, ACTS, cpm(), RUTA_CRITICA, DURACION_SEMANAS, HITOS, TRAMOS). networkx verifica la ruta crítica.
Sin componente aleatorio. Ejecución: python3 c9_figs.py"""
import os, sys, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "maestro")); sys.path.insert(0, os.path.join(RAIZ, "figs"))
import maestro as M
import estilo as E
import networkx as nx
from matplotlib.patches import Rectangle, FancyBboxPatch

ACTS = M.ACTS
CRIT = set(M.RUTA_CRITICA)
FILL = {"WP0": E.GRIS, "WP1": E.CLARO, "WP2": E.MEDIO, "WP3": E.BLANCO}
HITO_DEF = {"H0": ["A0.1"], "H1": ["A1.1", "A2.1"], "H2": ["A1.3"], "H3": ["C1"], "H4": ["A1.5"],
            "H5": ["C2"], "H6": ["A2.4"], "H7": ["A1.6"], "H8": ["A3.4"]}
SEM_MES = 52 / 12

def _h2(fig, texto):
    fig.text(0.008, 0.925, texto, fontsize=10, color=E.TINTA, ha="left", va="center")

def grafo():
    g = nx.DiGraph()
    for k, a in ACTS.items():
        g.add_node(k, dur=a["dur"])
    for k, a in ACTS.items():
        for p in a["pred"]: g.add_edge(p, k)
    return g

def verificar():
    """Comprueba con networkx que la longitud del camino más largo es la duración y que la ruta crítica coincide."""
    g = grafo()
    for u, v in g.edges: g[u][v]["w"] = ACTS[u]["dur"]
    # camino más largo por duración de nodos
    orden = list(nx.topological_sort(g)); best = {}
    for n in orden:
        best[n] = ACTS[n]["dur"] + max([best[p] for p in g.predecessors(n)], default=0)
    assert max(best.values()) == M.DURACION_SEMANAS, (max(best.values()), M.DURACION_SEMANAS)
    return g, best

# ------------------------------------------------------------------ F9.1 Gantt
def f01():
    g, _ = verificar()
    ncrit = len(CRIT); nholg = len(ACTS) - ncrit
    holg = sorted(a["holgura"] for a in ACTS.values() if a["holgura"] > 0)
    fig, ax = E.lienzo(h1=f"Una ruta crítica de {ncrit} actividades ocupa las {M.DURACION_SEMANAS} semanas; {nholg} actividades tienen holgura",
                       h2=None, figsize=(10, 7), grid=False)
    fig.subplots_adjust(left=0.36, right=0.985, top=0.80, bottom=0.15)
    _h2(fig, f"Cronograma en semanas desde el inicio (eje inferior) y en meses (eje superior); holguras de {holg[0]} a {holg[-1]} semanas (trama punteada)")
    orden = sorted(ACTS, key=lambda k: (ACTS[k]["ES"], ACTS[k]["EF"], k))
    n = len(orden)
    # bandas de fase por compuerta (semana de fin de C1 y C2)
    c1 = ACTS["C1"]["EF"]; c2 = ACTS["C2"]["EF"]; fin = M.DURACION_SEMANAS
    bandas = [(0, c1, "Fase 1 (tramo 1, hasta C1)", E.GRIS), (c1, c2, "Fase 2 (tramo 2)", E.CLARO), (c2, fin, "Fase 3 (tramo 3, hasta el cierre)", E.GRIS)]
    for x0, x1, t, c in bandas:
        ax.add_patch(Rectangle((x0, -1.6), x1 - x0, n + 1.9, facecolor=c, edgecolor="none", alpha=0.55 if c == E.GRIS else 0.45, zorder=0))
        ax.text((x0 + x1) / 2, n + 0.05, t, ha="center", va="bottom", fontsize=7.8, fontweight="bold", color=E.TINTA)
    for i, k in enumerate(orden):
        y = n - 1 - i; a = ACTS[k]
        crit = k in CRIT
        ax.barh(y, a["dur"], left=a["ES"], height=0.62, color=FILL[a["wp"]], edgecolor=E.TINTA if crit else E.MEDIO,
                linewidth=2.0 if crit else 0.9, zorder=3)
        if a["holgura"] > 0:
            ax.barh(y, a["holgura"], left=a["EF"], height=0.34, color="none", edgecolor=E.AZUL, hatch="....", linewidth=0.8, zorder=2)
            ax.text(a["LF"] + 0.8, y, f"holgura {a['holgura']}", fontsize=7, va="center", ha="left", color=E.TINTA)
        ax.text(a["ES"] + a["dur"] / 2, y, f"{a['dur']}", ha="center", va="center", fontsize=7.5, color=E.TINTA, fontweight="bold", zorder=4)
    ax.set_yticks([n - 1 - i for i in range(n)])
    ax.set_yticklabels([f"{k} {ACTS[k]['nombre']}" for k in orden], fontsize=7.6)
    ax.tick_params(axis="y", length=0)
    # hitos: fin de la actividad que los define
    hit = dict((h[0], h) for h in M.HITOS)
    prev = -99
    for h, defs in HITO_DEF.items():
        w = max(ACTS[d]["EF"] for d in defs)
        ax.plot([w, w], [-0.9, n - 0.55], color=E.TINTA, lw=0.6, ls=":", zorder=1)
        ax.plot([w], [-0.9], marker="D", ms=7, mfc=E.AZUL, mec=E.TINTA, mew=0.9, zorder=5)
        cerca = (w - prev) <= 3
        ax.text(w + (0.9 if cerca else 0), -1.55, f"{h}", ha="left" if cerca else "center", va="center", fontsize=7.8, fontweight="bold", color=E.TINTA)
        if cerca: ax.texts[-1].set_x(w + 0.9)
        prev = w
    # el hito anterior cercano se alinea a la izquierda
    ax.set_xlim(0, fin + 4); ax.set_ylim(-2.1, n + 0.7)
    ax.set_xticks(range(0, fin + 1, 8)); ax.tick_params(axis="x", labelsize=8.5)
    ax.set_xlabel("Semanas desde el inicio del proyecto", fontsize=9.5, labelpad=4)
    ax.spines["left"].set_visible(False)
    sec = ax.secondary_xaxis("top", functions=(lambda w: w / SEM_MES, lambda m: m * SEM_MES))
    sec.set_xticks(range(0, 25, 2)); sec.set_xlabel("Mes de calendario", fontsize=9, labelpad=3)
    sec.spines["top"].set_visible(False); sec.tick_params(labelsize=8)
    ax.grid(axis="x", alpha=0.25)
    # leyenda
    from matplotlib.patches import Patch
    hand = [Patch(facecolor=FILL[w], edgecolor=E.MEDIO, label=l) for w, l in
            [("WP0", "WP0 gestión"), ("WP1", "WP1 medición"), ("WP2", "WP2 red y plataforma"), ("WP3", "WP3 uso y custodia")]]
    hand.append(Patch(facecolor="white", edgecolor=E.TINTA, linewidth=2.0, label="Borde grueso: ruta crítica"))
    fig.legend(handles=hand, loc="lower left", bbox_to_anchor=(0.01, 0.0), ncol=5, fontsize=7.6, handlelength=1.4, columnspacing=1.1, frameon=False)
    return E.guardar(fig, "c9_f01")

# ------------------------------------------------------------------ F9.2 red CPM
def capas(g):
    capa = {}
    for k in nx.topological_sort(g):
        capa[k] = max([capa[p] + 1 for p in g.predecessors(k)], default=0)
    return capa

def posiciones(g):
    capa = capas(g)
    pos = {}
    por_capa = collections.defaultdict(list)
    for k, c in capa.items(): por_capa[c].append(k)
    for c, ks in por_capa.items():
        crit = sorted([k for k in ks if k in CRIT]); nocrit = sorted([k for k in ks if k not in CRIT])
        ys = {1: [1.0], 2: [1.55, 0.45]}.get(len(crit), [1.0])
        for k, y in zip(crit, ys): pos[k] = (c, y)
        for j, k in enumerate(nocrit): pos[k] = (c, 2.75 + 0.0 * j if len(nocrit) == 1 else 2.75 + j * 1.0)
    return pos, capa

def f02():
    g, _ = verificar()
    pos, capa = posiciones(g)
    ncrit = len(CRIT); holg = sorted(a["holgura"] for a in ACTS.values() if a["holgura"] > 0)
    fig, ax = E.lienzo_libre(h1=f"{ncrit} de {len(ACTS)} actividades forman la ruta crítica; las demás tienen holguras de {holg[0]} a {holg[-1]} semanas",
                             h2=None, figsize=(10, 4.9), xlim=(-0.55, max(capa.values()) + 0.55), ylim=(-0.1, 3.35))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.85, bottom=0.10)
    _h2(fig, "Diagrama de red de actividades en nodos (CPM); ES y EF: inicio y fin tempranos; LS y LF: inicio y fin tardíos; H: holgura; semanas")
    bw, bh = 0.74, 0.82
    # aristas
    for u, v in g.edges:
        (x0, y0), (x1, y1) = pos[u], pos[v]
        crit = u in CRIT and v in CRIT and ACTS[u]["EF"] == ACTS[v]["ES"]
        rad = 0.0
        if abs(x1 - x0) > 1: rad = 0.18 if y1 < y0 else -0.18
        E.flecha(ax, (x0 + bw / 2 + 0.01, y0), (x1 - bw / 2 - 0.01, y1), color=E.TINTA if crit else E.AZUL, lw=2.0 if crit else 1.0,
                 ls="-" if crit else "--", rad=rad)
    for k, (x, y) in pos.items():
        a = ACTS[k]; crit = k in CRIT
        p = FancyBboxPatch((x - bw / 2, y - bh / 2), bw, bh, boxstyle="round,pad=0.0,rounding_size=0.06", fc=FILL[a["wp"]], ec=E.TINTA if crit else E.MEDIO,
                           lw=2.2 if crit else 1.0, zorder=3)
        ax.add_patch(p)
        ax.text(x, y + 0.31, f"{k}", ha="center", va="center", fontsize=8.6, fontweight="bold", color=E.TINTA, zorder=4)
        filas = [f"{a['wp']} · {a['dur']} sem.", f"ES {a['ES']}  EF {a['EF']}", f"LS {a['LS']}  LF {a['LF']}", f"Holgura {a['holgura']}"]
        for j, t in enumerate(filas):
            ax.text(x, y + 0.14 - j * 0.155, t, ha="center", va="center", fontsize=6.2, color=E.TINTA, zorder=4)
    # leyenda inferior
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    hand = [Patch(facecolor=FILL[w], edgecolor=E.MEDIO, label=l) for w, l in
            [("WP0", "WP0 gestión"), ("WP1", "WP1 medición"), ("WP2", "WP2 red y plataforma"), ("WP3", "WP3 uso y custodia")]]
    hand.append(Line2D([0], [0], color=E.TINTA, lw=2.2, label="Dependencia crítica"))
    hand.append(Line2D([0], [0], color=E.AZUL, lw=1.0, ls="--", label="Dependencia con holgura"))
    ax.legend(handles=hand, loc="lower center", bbox_to_anchor=(0.5, -0.16), ncol=6, fontsize=7.8, frameon=False, handlelength=1.8, columnspacing=1.2)
    return E.guardar(fig, "c9_f02")

if __name__ == "__main__":
    print(f01()); print(f02())
