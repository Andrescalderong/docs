# -*- coding: utf-8 -*-
"""Figuras del Capítulo 2 (parte B): coocurrencia, cocitacion, cuadrantes, evolucion, complejidad, radar, heatmap, robustez.
Semilla 42; corpus de 42 documentos; año de corte 2026. Usa figs/estilo.py."""
import os, sys, collections, math, itertools, textwrap
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "..")); sys.path.insert(0, AQUI)
import numpy as np, networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Patch, PathPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib.lines import Line2D
import estilo as E
import c2_datos as D
PIE = "n = 42 documentos; año de corte 2026; semilla 42"
def pie(fig, txt=PIE): fig.text(0.01, 0.002, txt, fontsize=7.5, color=E.TINTA, ha="left", va="bottom")
MARC = ["o", "s", "^", "D", "P"]
COL5 = [E.AZUL, E.MEDIO, E.CLARO, E.GRIS, E.AZUL]
NOMB_COM = {0: "Pronóstico con aprendizaje automático", 1: "Salud, monitoreo y gestión", 2: "Contaminación, clima y patrimonio", 3: "Partículas, sensores y exposición", 4: "Meteorología, ciudad y gemelo digital"}

# ---------------------------------------------------------------- Red de co-ocurrencia (palabras de título)
def coocurrencia():
    G, cnt, com, mod = D.red_titulos(2)
    # diseño: comunidades en un pentágono; dentro de cada comunidad, spring_layout de su subgrafo (semilla 42)
    pos = {}
    R = 1.0
    for i, c in enumerate(com):
        ang = np.pi / 2 - 2 * np.pi * i / len(com)
        centro = np.array([1.38 * R * np.cos(ang), 0.98 * R * np.sin(ang)])
        orden = sorted(c, key=lambda w: (-cnt[w], w))
        pos[orden[0]] = centro
        resto = orden[1:]
        n1 = min(len(resto), 6 if len(c) > 8 else 5)
        r1 = 0.30; r2 = 0.56
        for j, w in enumerate(resto[:n1]):
            a = 2 * np.pi * j / n1 + 0.4
            pos[w] = centro + r1 * np.array([1.25 * np.cos(a), np.sin(a)])
        r_ = resto[n1:]
        for j, w in enumerate(r_):
            a = 2 * np.pi * j / max(len(r_), 1) + 0.9
            pos[w] = centro + r2 * np.array([1.25 * np.cos(a), np.sin(a)])
    fig, ax = E.lienzo(h1="La red de palabras de título forma cinco comunidades con estructura débil", h2="Co-ocurrencia de palabras de título (frecuencia mínima 2); 49 nodos, 260 aristas, modularidad Louvain de %s" % E.num(mod, 2), figsize=(10, 7), grid=False)
    ax.axis("off")
    wmax = max(d["weight"] for _, _, d in G.edges(data=True))
    comun = {w: i for i, c in enumerate(com) for w in c}
    for a_, b_, d in G.edges(data=True):
        intra = comun[a_] == comun[b_]
        if not intra and d["weight"] < 2: continue
        ax.plot([pos[a_][0], pos[b_][0]], [pos[a_][1], pos[b_][1]], color=E.TINTA if not intra else E.MEDIO, lw=0.3 + 1.6 * d["weight"] / wmax, alpha=0.30 if intra else 0.45, zorder=1, ls="-" if intra else (0, (3, 2)))
    for i, c in enumerate(com):
        xs = [pos[w][0] for w in c]; ys = [pos[w][1] for w in c]
        ax.scatter(xs, ys, s=[55 + 40 * cnt[w] for w in c], c=COL5[i], marker=MARC[i], edgecolor=E.TINTA, lw=1.0, zorder=3)
    for w in G.nodes:
        ax.text(pos[w][0], pos[w][1] + 0.075 + 0.003 * cnt[w], w, ha="center", va="bottom", fontsize=7.6 + 0.3 * min(cnt[w], 8), color=E.TINTA, zorder=4,
                bbox=dict(boxstyle="round,pad=0.06", fc="white", ec="none", alpha=0.7), fontweight="bold" if cnt[w] >= 4 else "normal")
    ax.set_xlim(-2.1, 2.1); ax.set_ylim(-1.55, 1.6)
    ax.legend(handles=[Line2D([], [], marker=MARC[i], ls="", markerfacecolor=COL5[i], markeredgecolor=E.TINTA, markersize=9, label=f"C{i+1}: {NOMB_COM[i]} ({len(c)} palabras)") for i, c in enumerate(com)],
              loc="lower center", fontsize=8, ncol=2, bbox_to_anchor=(0.5, -0.1))
    pie(fig, "Palabras de título, no palabras clave; 4 términos en español equiparados al inglés; trazo discontinuo = enlace entre comunidades con peso 2 o más; semilla 42; 42 documentos; corte 2026")
    return E.guardar(fig, "c2_coocurrencia")

# ---------------------------------------------------------------- Acoplamiento bibliográfico / base intelectual (F-INF §7.7, Tabla 39)
ACOP = [("Moura2025", "Tavella2026", 12), ("Nelson2026", "Essamlali2024", 6), ("Moura2025", "RodrguezVillamizar2022", 6), ("Moura2025", "Kumar2026", 5),
        ("Botezat2025", "Tavella2026", 4), ("Huang2025", "Wei2026", 4), ("RodrguezVillamizar2022", "Liao2026", 4), ("Kumar2026", "Liao2026", 3),
        ("Becerra2021", "VlezPereira2025", 3), ("Essamlali2024", "Haris2026", 3), ("Bang2026", "Tavella2026", 3), ("Pedraza2026", "Tavella2026", 3)]
def era_de(y): return 1 if y <= 2023 else (2 if y <= 2025 else 3)
ETIQ = {"Moura2025": "De Moura 2025", "Tavella2026": "Tavella 2026", "Nelson2026": "Nelson 2026", "Essamlali2024": "Essamlali 2024", "RodrguezVillamizar2022": "Rodríguez-Villamizar 2022",
        "Kumar2026": "Kumar 2026", "Botezat2025": "Botezat 2025", "Huang2025": "Huang 2025", "Wei2026": "Wei 2026", "Liao2026": "Liao 2026", "Becerra2021": "Becerra 2021",
        "VlezPereira2025": "Vélez-Pereira 2025", "Haris2026": "Haris 2026", "Bang2026": "Bang 2026", "Pedraza2026": "Murad Pedraza 2026"}
def cocitacion():
    yr = {r["key"]: r["year"] for r in D.CORPUS}
    G = nx.Graph()
    for a, b, w in ACOP: G.add_edge(a, b, weight=w)
    pos = {}
    comps = sorted(nx.connected_components(G), key=lambda c: -len(c))
    centros = [(-0.45, 0.35), (0.85, 0.75), (0.85, -0.25), (-0.15, -0.95)]
    escs = [0.62, 0.30, 0.30, 0.30]
    for c, ce, es in zip(comps, centros, escs):
        sub = G.subgraph(c); ps = nx.spring_layout(sub, seed=D.SEED, k=1.2 / math.sqrt(len(c)), iterations=400)
        for n, v in ps.items(): pos[n] = np.array(ce) + es * np.array(v) * (1.4 if len(c) > 2 else 0.9)
    fig = plt.figure(figsize=(10, 7)); fig.suptitle("Los pares más acoplados comparten entre 3 y 12 referencias", fontsize=14, fontweight="bold", color=E.TINTA, x=0.01, ha="left", y=0.995)
    ax = fig.add_axes([0.01, 0.08, 0.64, 0.80]); ax.axis("off")
    ax.set_title("Acoplamiento bibliográfico por texto entre artículos (12 pares principales de 102); color por era de publicación", fontsize=9.5, loc="left", color=E.TINTA)
    colera = {1: E.CLARO, 2: E.MEDIO, 3: E.AZUL}
    for a, b, d in G.edges(data=True):
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=E.TINTA, lw=0.8 + 0.55 * d["weight"], alpha=0.55, zorder=1, solid_capstyle="round")
        ax.text((pos[a][0] + pos[b][0]) / 2, (pos[a][1] + pos[b][1]) / 2, str(d["weight"]), fontsize=8.5, fontweight="bold", ha="center", va="center", color=E.TINTA, bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9), zorder=3)
    for n in G.nodes:
        e = era_de(yr[n])
        ax.scatter([pos[n][0]], [pos[n][1]], s=240 + 40 * G.degree(n, weight="weight") ** 0.7 * 3, color=colera[e], edgecolor=E.TINTA, lw=1.2, marker="o" if e == 3 else ("s" if e == 2 else "^"), zorder=4)
        ax.text(pos[n][0], pos[n][1] - 0.10, ETIQ[n], ha="center", va="top", fontsize=8.2, color=E.TINTA, zorder=5, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.75))
    ax.set_xlim(-1.4, 1.5); ax.set_ylim(-1.45, 1.35)
    ax.legend(handles=[Line2D([], [], marker="^", ls="", markerfacecolor=E.CLARO, markeredgecolor=E.TINTA, markersize=10, label="Era fundacional (hasta 2023)"),
                       Line2D([], [], marker="s", ls="", markerfacecolor=E.MEDIO, markeredgecolor=E.TINTA, markersize=10, label="Era de crecimiento (2024 y 2025)"),
                       Line2D([], [], marker="o", ls="", markerfacecolor=E.AZUL, markeredgecolor=E.TINTA, markersize=10, label="Era de aceleración (2026)")], loc="lower left", fontsize=8.3, bbox_to_anchor=(0.0, -0.02))
    ax2 = fig.add_axes([0.73, 0.18, 0.25, 0.62])
    ax2.set_title("Referencias citadas por varios artículos", fontsize=9.5, loc="left", color=E.TINTA, pad=10)
    vals = [("Guía de la OMS de 2021", 9), ("Revisión sobre efectos\nambientales y en salud", 5)]
    b = ax2.bar([0, 1], [v for _, v in vals], color=[E.AZUL, E.MEDIO], edgecolor=E.TINTA, hatch=["", "///"][0], width=0.6)
    b[1].set_hatch("///")
    for i, (t, v) in enumerate(vals): ax2.text(i, v + 0.2, str(v), ha="center", fontsize=11, fontweight="bold", color=E.TINTA)
    ax2.set_xticks([0, 1]); ax2.set_xticklabels([t for t, _ in vals], fontsize=8); ax2.set_ylim(0, 11); ax2.set_ylabel("Artículos que la citan (de 26)")
    ax2.grid(axis="y")
    pie(fig, "Fuente: F-INF §7.7, Tabla 39 (p. 95); aproximación por fragmentos de título de siete palabras; sin co-citación de autores; 42 documentos; corte 2026")
    return E.guardar(fig, "c2_cocitacion")

# ---------------------------------------------------------------- Cuadrantes estratégicos (F-INF §7.5, Tabla 37)
COM = [(1, 195, 31461.54, 875310, "aire, calidad, contaminantes"), (2, 136, 33518.38, 881650, "datos, sensores, dispositivos"), (3, 94, 30410.64, 700890, "modelo, tiempo, valor"),
       (4, 59, 54844.07, 479950, "salud, activos, motores"), (5, 48, 20495.83, 279920, "temperatura, viento, partículas"), (6, 29, 21855.17, 218480, "edificios, espacio, urbano"),
       (7, 13, 25238.46, 73660, "conjuntos, índices, métricas"), (8, 10, 8330.0, 10640, "fechas de publicación")]
def cuadrantes():
    cen = np.array([c[3] for c in COM]); den = np.array([c[2] for c in COM]); mc, md = float(np.median(cen)), float(np.median(den))
    fig, ax = E.lienzo(h1="Cuatro comunidades de términos son motoras y cuatro quedan emergentes o marginales", h2="Centralidad (suma de enlaces externos) y densidad (fuerza de enlaces internos) de 8 comunidades de co-palabras; tamaño = términos; 584 nodos", figsize=(10, 7), grid=False)
    ax.axvline(mc, color=E.TINTA, ls="--", lw=1); ax.axhline(md, color=E.TINTA, ls="--", lw=1)
    ax.set_xlim(-30000, 1050000); ax.set_ylim(0, 62000)
    ax.text(1045000, 61000, "Motor", ha="right", va="top", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.text(-25000, 61000, "Nicho", ha="left", va="top", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.text(-25000, 1000, "Emergente o en declive", ha="left", va="bottom", fontsize=10, fontweight="bold", color=E.TINTA)
    ax.text(1045000, 1000, "Básico o transversal", ha="right", va="bottom", fontsize=10, fontweight="bold", color=E.TINTA)
    for i, (n, nt, d, c, t) in enumerate(COM):
        motor = c > mc and d > md
        ax.scatter([c], [d], s=nt * 9 + 90, color=E.AZUL if motor else E.CLARO, edgecolor=E.TINTA, lw=1.2, marker=MARC[0] if motor else MARC[1], hatch="" if motor else "...", zorder=3, alpha=0.95)
        dx, dy, ha = 18000, 1900, "left"
        if n == 2: dx, dy, ha = 0, 4200, "center"
        if n == 1: dx, dy, ha = 0, -6800, "center"
        if n == 3: dx, dy, ha = -10000, 3600, "right"
        if n == 7: dx, dy, ha = 20000, 2100, "left"
        if n == 8: dx, dy, ha = 20000, -2300, "left"
        ax.text(c + dx, d + dy, f"C{n}: {t} ({nt})", fontsize=8.4, ha=ha, va="center", color=E.TINTA, bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.8))
    ax.set_xlabel("Centralidad de Callon (suma de enlaces con otras comunidades)"); ax.set_ylabel("Densidad de Callon (fuerza de enlaces internos)")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: E.num(v, 0))); ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: E.num(v, 0)))
    ax.grid(axis="both")
    pie(fig, "Fuente: F-INF §7.5, Tabla 37 (p. 88); cortes en las medianas (centralidad %s; densidad %s); Louvain, 8 comunidades; 42 documentos; corte 2026" % (E.num(mc, 0), E.num(md, 0)))
    return E.guardar(fig, "c2_cuadrantes")

# ---------------------------------------------------------------- Evolución temática: aluvial de composición por grupo y era
def evolucion():
    yr = {r["key"]: r["year"] for r in D.CORPUS}
    eras = [("Fundacional\n1995 a 2023", lambda y: y <= 2023), ("Crecimiento\n2024 y 2025", lambda y: 2024 <= y <= 2025), ("Aceleración\n2026", lambda y: y >= 2026)]
    NG = {1: "G1 Pronóstico con aprendizaje automático", 2: "G2 Monitoreo y alerta", 3: "G3 Exposición y salud", 4: "G4 Patentes de sensores y activos", 5: "G5 Patentes de espacios interiores y SIC"}
    cnt = [{g: sum(1 for k in D.GRUPOS[g] if f(yr[k])) for g in D.GRUPOS} for _, f in eras]
    estilo = {1: (E.AZUL, ""), 2: (E.MEDIO, "///"), 3: (E.CLARO, "..."), 4: (E.GRIS, "xx"), 5: (E.AZUL, "\\\\")}
    fig, ax = E.lienzo(h1="En 2026 el monitoreo y la exposición suman 12 de los 17 documentos", h2="Documentos por grupo documental en tres eras; el listón une el mismo grupo entre eras y no representa migración de documentos; n = 42", figsize=(10, 7), grid=False)
    ax.axis("off")
    xs = [0.0, 4.0, 8.0]; bw = 1.1; esc = 0.46
    tops = []
    for ei, c in enumerate(cnt):
        y0 = 0; seg = {}
        for g in [4, 5, 1, 3, 2]:
            h = c[g] * esc; seg[g] = (y0, y0 + h); y0 += h
        tops.append(seg)
    for ei in range(2):
        for g in D.GRUPOS:
            a0, a1 = tops[ei][g]; b0, b1 = tops[ei + 1][g]
            if a1 - a0 == 0 and b1 - b0 == 0: continue
            xa, xb = xs[ei] + bw, xs[ei + 1]
            xm = (xa + xb) / 2
            verts = [(xa, a0), (xm, a0), (xm, b0), (xb, b0), (xb, b1), (xm, b1), (xm, a1), (xa, a1), (xa, a0)]
            codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY]
            col, hat = estilo[g]
            ax.add_patch(PathPatch(Path(verts, codes), fc=col, ec=E.TINTA, lw=0.6, alpha=0.55, hatch=hat))
    for ei, c in enumerate(cnt):
        for g in D.GRUPOS:
            y0, y1 = tops[ei][g]
            if y1 - y0 == 0: continue
            col, hat = estilo[g]
            ax.add_patch(Rectangle((xs[ei], y0), bw, y1 - y0, fc=col, ec=E.TINTA, lw=1.1, hatch=hat))
            ax.text(xs[ei] + bw / 2, (y0 + y1) / 2, str(c[g]), ha="center", va="center", fontsize=10, fontweight="bold", color=E.TINTA, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.85))
        n = sum(c.values())
        ax.text(xs[ei] + bw / 2, -0.4, f"{eras[ei][0]}\n{n} documentos ({E.num(100*n/42,1)} %)", ha="center", va="top", fontsize=9, fontweight="bold", color=E.TINTA)
    ax.legend(handles=[Patch(fc=estilo[g][0], ec=E.TINTA, hatch=estilo[g][1], label=NG[g]) for g in (1, 2, 3, 4, 5)], loc="upper left", fontsize=8.6, bbox_to_anchor=(0.0, 1.0))
    ax.set_xlim(-0.6, 9.8); ax.set_ylim(-2.4, 8.4)
    pie(fig, "Fuente: F-INF §4.3 (p. 34) y §10.1, Tabla 46 (p. 124); eras por segmentación óptima en tres tramos; 42 documentos; corte 2026; semilla 42")
    return E.guardar(fig, "c2_evolucion")

# ---------------------------------------------------------------- Complejidad vs adopción (TRL × IRL, F-INF §4.1 Tabla 13)
def complejidad():
    celdas = collections.Counter()
    for gid, k, trl, irl, drl in D.TABLA13:
        if trl is None: continue
        celdas[(trl, irl, D.VALLE[gid] == "V4")] += 1
    fig, ax = E.lienzo(h1="El valle de componentes sin integración reúne 13 de 41 documentos", h2="Documentos por nivel de preparación tecnológica (TRL) e integración (IRL), escala de 1 a 9; tamaño = número de documentos; n = 41 con TRL e IRL", figsize=(10, 7), grid=False)
    ax.add_patch(Rectangle((3.5, 0.5), 2.0, 3.0, fc=E.CLARO, ec=E.TINTA, lw=1, ls="--", alpha=0.40, hatch="..."))
    ax.text(4.5, 0.62, "Región TRL 4 a 5\ncon IRL de 3 o menos:\n14 documentos, 9 en V4", ha="center", va="bottom", fontsize=8.3, fontweight="bold", color=E.TINTA)
    ax.axvline(7, color=E.TINTA, ls=":", lw=1.1); ax.axhline(6, color=E.TINTA, ls=":", lw=1.1)
    ax.text(7.05, 8.75, "Criterio TRL 7", fontsize=8.3, ha="left", color=E.TINTA); ax.text(1.5, 6.12, "Criterio IRL 6", fontsize=8.3, ha="left", color=E.TINTA)
    for (trl, irl, v4), n in celdas.items():
        dx = -0.16 if v4 else 0.16
        if not any(k[0] == trl and k[1] == irl and k[2] != v4 for k in celdas): dx = 0
        ax.scatter([trl + dx], [irl], s=75 * n + 70, color=E.AZUL if v4 else E.MEDIO, edgecolor=E.TINTA, lw=1.1, marker="o" if v4 else "s", hatch="" if v4 else "///", zorder=3)
        ax.text(trl + dx, irl, str(n), ha="center", va="center", fontsize=8.5, fontweight="bold", color=E.TINTA, zorder=4, bbox=dict(boxstyle="round,pad=0.05", fc="white", ec="none", alpha=0.75))
    ax.annotate("Sistema de alerta SIATA\n(TRL 9, IRL 8)", xy=(9, 8), xytext=(7.1, 8.0), fontsize=8.5, color=E.TINTA, ha="right", va="center", arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.8))
    ax.annotate("Sistema de lahares\n(TRL 7, IRL 5)", xy=(7, 5), xytext=(7.5, 3.6), fontsize=8.5, color=E.TINTA, ha="left", va="center", arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.8))
    ax.set_xlim(1.4, 9.7); ax.set_ylim(0.5, 9.2); ax.set_xticks(range(2, 10)); ax.set_yticks(range(1, 10))
    ax.set_xlabel("Nivel de preparación tecnológica (TRL) como proxy de sofisticación"); ax.set_ylabel("Nivel de integración (IRL) como proxy de adopción")
    ax.grid(axis="both")
    ax.legend(handles=[Line2D([], [], marker="o", ls="", markerfacecolor=E.AZUL, markeredgecolor=E.TINTA, markersize=9, label="Documentos del valle V4 (13)"), Line2D([], [], marker="s", ls="", markerfacecolor=E.MEDIO, markeredgecolor=E.TINTA, markersize=9, label="Documentos de otros valles (28)")], loc="upper left", fontsize=8.5)
    pie(fig, "Fuente: F-INF §4.1, Tabla 13 (p. 29) y §4.6, Tabla 17 (p. 38); la complejidad no se midió en el corpus; el informe institucional carece de TRL e IRL; 42 documentos; corte 2026")
    return E.guardar(fig, "c2_complejidad")

# ---------------------------------------------------------------- Radar por grupo (F-INF §3.2 Tabla 6 y Tabla 5)
PERFIL = {1: (4.0, 2.56, 2.22, 4.54, 6.33), 2: (5.12, 3.88, 3.88, 4.12, 6.62), 3: (3.67, 2.56, 3.11, 4.32, 6.44), 4: (3.25, 2.62, 3.0, 3.54, 4.25), 5: (3.14, 2.86, 3.12, 2.97, 4.88)}
CRIT = (7, 6, 5, 7, 7)   # TRL, IRL, DRL, robustez, valor (F-INF §3.2, Tabla 5)
EJES = ["TRL", "IRL", "DRL", "Robustez", "Valor\nestratégico"]
CORPUS_MEDIA = (3.85, 2.88, 3.05, 3.93, 5.74)
def radar():
    fig = plt.figure(figsize=(10, 7))
    fig.suptitle("Ningún grupo documental alcanza el 100 % del criterio en ningún indicador", fontsize=14, fontweight="bold", color=E.TINTA, x=0.01, ha="left", y=0.995)
    fig.text(0.01, 0.945, "Media de cada grupo como porcentaje del criterio de referencia (TRL 7, IRL 6, DRL 5, robustez 7, valor 7); línea discontinua = corpus de 42 documentos", fontsize=9.5, color=E.TINTA)
    ang = np.linspace(0, 2 * np.pi, 5, endpoint=False); ang2 = np.concatenate([ang, [ang[0]]])
    nombres = {1: "G1 Pronóstico (9)", 2: "G2 Monitoreo y alerta (8)", 3: "G3 Exposición y salud (9)", 4: "G4 Patentes de sensores y activos (8)", 5: "G5 Patentes interiores y SIC (8)"}
    cm = np.array([v / c for v, c in zip(CORPUS_MEDIA, CRIT)]) * 100
    estilo = {1: (E.AZUL, ""), 2: (E.MEDIO, "///"), 3: (E.CLARO, "..."), 4: (E.GRIS, "xx"), 5: (E.AZUL, "\\\\")}
    posiciones = [(0.05, 0.53, 0.26, 0.31), (0.37, 0.53, 0.26, 0.31), (0.69, 0.53, 0.26, 0.31), (0.05, 0.08, 0.26, 0.31), (0.37, 0.08, 0.26, 0.31)]
    for g, rect in zip((1, 2, 3, 4, 5), posiciones):
        ax = fig.add_axes(rect, projection="polar")
        v = np.array([x / c for x, c in zip(PERFIL[g], CRIT)]) * 100
        v2 = np.concatenate([v, [v[0]]])
        ax.set_theta_offset(np.pi / 2); ax.set_theta_direction(-1)
        ax.set_ylim(0, 100); ax.set_yticks([25, 50, 75, 100]); ax.set_yticklabels(["25", "50", "75", "100 %"], fontsize=6.5, color=E.TINTA)
        ax.set_xticks(ang); ax.set_xticklabels(EJES, fontsize=7.6, color=E.TINTA); ax.tick_params(axis="x", pad=9)
        ax.grid(color=E.MEDIO, alpha=0.5, lw=0.6); ax.spines["polar"].set_color(E.TINTA)
        ax.plot(ang2, np.concatenate([cm, [cm[0]]]), color=E.TINTA, ls="--", lw=1.0)
        col, hat = estilo[g]
        ax.fill(ang2, v2, color=col, alpha=0.6, hatch=hat, edgecolor=E.TINTA, lw=1.4)
        ax.plot(ang2, v2, color=E.TINTA, lw=1.4, marker=MARC[g - 1], ms=4.5)
        for a, val in zip(ang, v): ax.text(a, min(val + 12, 108), f"{E.num(val,0)}", fontsize=7.4, ha="center", va="center", color=E.TINTA, fontweight="bold")
        ax.set_title(nombres[g], fontsize=8.8, fontweight="bold", color=E.TINTA, pad=18)
    fig.text(0.70, 0.24, "Lectura: cada eje muestra el porcentaje\ndel criterio; el SRL se excluye porque\nsolo tres grupos tienen datos.\nLos seis ejes financiero, estratégico, de recursos,\nde riesgo, de partes interesadas y de sostenibilidad\nde la especificación no se midieron\nen el corpus.", fontsize=8.5, color=E.TINTA, va="center")
    pie(fig, "Fuente: F-INF §3.2, Tablas 5 y 6 (p. 22); n por grupo entre paréntesis; 42 documentos; corte 2026")
    return E.guardar(fig, "c2_radar")

# ---------------------------------------------------------------- Heatmap por línea tecnológica (F-INF §4.8 Tabla 18)
LINEAS = [("Sistemas de alerta temprana y gestión de desastres", 4, 5.75, 4.5), ("Pronóstico con aprendizaje automático", 9, 4.0, 2.56), ("Valorización de residuos por gasificación", 1, 4.0, 3.0),
          ("Exposición ocupacional", 2, 4.0, 3.0), ("Redes de sensores de bajo costo y calibración", 5, 3.8, 3.0), ("Índices y calificaciones de salud y salubridad", 4, 3.75, 3.0),
          ("Teledetección de incendios, humo y transporte regional", 3, 3.67, 2.33), ("Carga de enfermedad y exposición", 5, 3.6, 2.4), ("Patrimonio y materiales", 2, 3.5, 3.0),
          ("Diagnóstico predictivo con gemelo digital", 3, 3.33, 3.0), ("Medición de partículas y calibración (patentes)", 3, 3.0, 2.33), ("Energía, carbono y control de interiores", 3, 2.67, 2.67)]
def heatmap():
    M = np.array([[t / 7 * 100, i / 6 * 100, (t - i)] for _, _, t, i in LINEAS])
    fig = plt.figure(figsize=(10, 7))
    fig.suptitle("Solo los sistemas de alerta temprana superan el 60 % del criterio de integración", fontsize=14, fontweight="bold", color=E.TINTA, x=0.01, ha="left", y=0.995)
    fig.text(0.01, 0.945, "Madurez media por línea tecnológica como porcentaje del criterio (TRL 7 e IRL 6); 12 líneas con datos; un documento puede pertenecer a más de una línea", fontsize=9.5, color=E.TINTA)
    ax = fig.add_axes([0.40, 0.07, 0.58, 0.76]); ax.set_xlim(0, 3); ax.set_ylim(len(LINEAS), 0); ax.axis("off")
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("az", ["#FFFFFF", E.CLARO, E.AZUL])
    for r, (nom, n, t, i) in enumerate(LINEAS):
        for c, (val, txt) in enumerate([(M[r, 0], f"TRL {E.num(t,2)}  ({E.num(M[r,0],0)} %)"), (M[r, 1], f"IRL {E.num(i,2)}  ({E.num(M[r,1],0)} %)")]):
            ax.add_patch(Rectangle((c, r), 1, 1, fc=cmap(val / 100), ec=E.TINTA, lw=0.8))
            ax.text(c + 0.5, r + 0.5, txt, ha="center", va="center", fontsize=8.8, color=E.TINTA, fontweight="bold" if val >= 60 else "normal")
        ax.add_patch(Rectangle((2, r), 1, 1, fc="white", ec=E.TINTA, lw=0.8))
        ax.text(2.5, r + 0.5, f"{E.num(M[r,2],2)} niveles", ha="center", va="center", fontsize=8.8, color=E.TINTA)
        ax.text(-0.03, r + 0.5, f"{textwrap.fill(nom, 40)}  (n = {n})", ha="right", va="center", fontsize=8.4, color=E.TINTA, linespacing=0.95)
    for c, t in enumerate(["Madurez tecnológica\n(porcentaje de TRL 7)", "Integración\n(porcentaje de IRL 6)", "Brecha TRL menos IRL\n(niveles)"]):
        ax.text(c + 0.5, -0.25, t, ha="center", va="bottom", fontsize=9, fontweight="bold", color=E.TINTA)
    pie(fig, "Fuente: F-INF §4.8, Tabla 18 (p. 41); la línea de vigilancia de propiedad industrial no tiene TRL ni IRL; brecha = TRL menos IRL (CALCULADO); corte 2026")
    return E.guardar(fig, "c2_heatmap")

# ---------------------------------------------------------------- Robustez por grupo (F-INF §2.2 y §3.2)
def robustez():
    fig, ax = E.lienzo(h1="La robustez media es 3,93 de 10 y ningún documento alcanza 7", h2="Robustez argumentativa (0 a 10) por grupo documental: media del grupo (F-INF) y valores individuales publicados (17 de 42 documentos)", figsize=(10, 7))
    nombres = {1: "G1 Pronóstico\n(n = 9)", 2: "G2 Monitoreo y alerta\n(n = 8)", 3: "G3 Exposición y salud\n(n = 9)", 4: "G4 Patentes de sensores\ny activos (n = 8)", 5: "G5 Patentes interiores\ny SIC (n = 8)"}
    rng = np.random.default_rng(D.SEED)
    for g in range(1, 6):
        mu, n = D.ROB_GRUPO[g]
        ax.bar(g, mu, color=E.CLARO, edgecolor=E.TINTA, lw=0.8, width=0.62, hatch="...", zorder=1)
        ax.plot([g - 0.31, g + 0.31], [mu, mu], color=E.TINTA, lw=2.2, zorder=4)
        ax.text(g, 0.3, f"media {E.num(mu,2)}", ha="center", va="bottom", fontsize=9, fontweight="bold", color=E.TINTA, zorder=6, bbox=dict(boxstyle="round,pad=0.15", fc="white", ec=E.TINTA, alpha=0.95))
        vals = [(D.ROB_CONOCIDA[k], k) for k in D.GRUPOS[g] if k in D.ROB_CONOCIDA]
        for j, (v, k) in enumerate(sorted(vals)):
            xj = g + (j - (len(vals) - 1) / 2) * 0.13
            ax.scatter([xj], [v], s=62, color=E.AZUL, edgecolor=E.TINTA, lw=1, zorder=5, marker=MARC[g - 1])
    ax.axhline(7, color=E.TINTA, ls="--", lw=1.2); ax.text(5.45, 7.08, "Criterio de referencia: 7", ha="right", va="bottom", fontsize=8.8, color=E.TINTA, fontweight="bold")
    ax.axhline(3.93, color=E.TINTA, ls=":", lw=1.2); ax.text(5.48, 4.02, "Media del corpus: 3,93", ha="right", va="bottom", fontsize=8.8, color=E.TINTA)
    ax.annotate("Nelson et al. (2026): 6,1\nmáximo del corpus", xy=(1 - 0.13, 6.1), xytext=(1.35, 6.4), fontsize=8.5, color=E.TINTA, arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.8), va="center")
    ax.annotate("Acosta y Horstmann (2026) y\nMachida y Ammendola (2025): 2,7\nmínimo del corpus", xy=(5 - 0.19, 2.7), xytext=(3.55, 1.5), fontsize=8.5, color=E.TINTA, arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.8), va="center", ha="center", bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9), zorder=7)
    ax.set_xticks(range(1, 6)); ax.set_xticklabels([nombres[g] for g in range(1, 6)], fontsize=8.6)
    ax.set_ylim(0, 8); ax.set_xlim(0.5, 5.5); ax.set_ylabel("Robustez argumentativa (0 a 10)")
    ax.legend(handles=[Patch(fc=E.CLARO, ec=E.TINTA, hatch="...", label="Media del grupo (F-INF)"), Line2D([], [], marker="o", ls="", markerfacecolor=E.AZUL, markeredgecolor=E.TINTA, markersize=8, label="Valor individual publicado en el informe de vigilancia")], loc="upper right", fontsize=8.3, bbox_to_anchor=(1.0, 0.86))
    pie(fig, "Fuente: F-INF §2.2 (p. 14), §3.2 (p. 22) y §13.1, Tabla 65 (p. 208); la distribución completa por documento no se publica, de modo que no hay violín; 42 documentos; corte 2026")
    return E.guardar(fig, "c2_robustez")

if __name__ == "__main__":
    for f in (coocurrencia, cocitacion, cuadrantes, evolucion, complejidad, radar, heatmap, robustez): print(f())
