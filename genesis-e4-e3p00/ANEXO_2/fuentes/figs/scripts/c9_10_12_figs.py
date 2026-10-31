# -*- coding: utf-8 -*-
"""Figuras del Anexo 2: c9_f01 (mapa conceptual de las siete teorías), c10_f01 (matriz de poder e interés de los 18 interesados),
c12_f01 (árbol de objetivos) y c12_f02 (contribución de los objetivos específicos a los ODS).
Datos: A2/v2/m2.py (objetivo general y objetivos específicos con su meta: m2.M0.OG y m2.M0.OE; nodos y gateways); posiciones de poder e
interés de los interesados según la lista de interesados del proyecto (escala de 1 a 10); contribuciones a los ODS según A2/FIGS_A2.md
(directas: OE1 y OE2 a ODS 9, OE3 a ODS 11; indirectas: el resto de enlaces de la figura guía).
Ejecución: python3 c9_10_12_figs.py  -> A2/figs/out/c9_f01.png, c10_f01.png, c12_f01.png, c12_f02.png"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _a2 as A
from _a2 import T, AZUL, MEDIO, CLARO, GRIS, CAJA, BLANCO, P, F_B
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

OE = {o["id"]: o for o in A.m2.M0.OE}
OG = ("Reducir el error de medición de material particulado de una red de 100 nodos de bajo costo, y asegurar el uso institucional de esa medición y de un gemelo predictivo de demolición validado en la gestión del riesgo, "
      "mediante calibración dinámica en gateways, operación con energía y enlace redundantes, un laboratorio de modelación y custodia distribuida por tramos, en Manizales (Caldas) y Calarcá (Quindío), durante 24 meses.")
NODOS, GW = A.m2.IDENT["nodos"], A.m2.IDENT["gateways"]
DISCONT = (0, (4.5, 3))


# ------------------------------------------------------------------ c9_f01
def c9_f01():
    H = 68
    fig, ax = A.lienzo("Siete teorías sostienen la cadena de la medición verificada a la continuidad",
                       "Mapa conceptual de integración teórica; las flechas indican dependencia entre componentes del proyecto", H)
    w, gap, x0 = 21.8, 3.6, 1.0
    X = [x0 + i * (w + gap) for i in range(4)]
    h1, h2, h3, h4 = 11.5, 10.5, 10.5, 11.5
    gv = 6.0
    y1 = H - 0.6 - h1
    y2 = y1 - gv - h2
    y3 = y2 - 8.0 - h3
    y4 = y3 - gv - h4
    teorias = ["Metrología y calibración de sensores de bajo costo", "Computación en el borde y LoRaWAN", "Gemelos digitales",
               "Gestión del riesgo y alerta temprana"]
    comp = ["Medición verificada", "Corrección en el gateway y enlace redundante", "Gemelo digital: estimación espacial",
            "Alerta con umbrales locales"]
    for i in range(4):
        A.caja(ax, X[i], y1, w, h1, teorias[i], relleno=MEDIO, lw=2.2)
        A.caja(ax, X[i], y2, w, h2, comp[i], relleno=CAJA)
        A.flecha(ax, (X[i] + w / 2, y1 - 0.3), (X[i] + w / 2, y2 + h2 + 0.3))
        if i < 3:
            A.flecha(ax, (X[i] + w + 0.3, y2 + h2 / 2), (X[i + 1] - 0.3, y2 + h2 / 2))
    # fila 3: de derecha a izquierda (uso, custodia, compuertas)
    f3 = [(3, "Uso institucional del tablero"), (2, "Custodia por componente"), (1, "Compuertas de revisión")]
    f4 = [(3, "Difusión y adopción de innovaciones"), (2, "Gobernanza de bienes comunes y custodia"), (1, "Aprendizaje de doble bucle")]
    for c, t in f3:
        A.caja(ax, X[c], y3, w, h3, t, relleno=CAJA)
    for c, t in f4:
        A.caja(ax, X[c], y4, w, h4, t, relleno=MEDIO, lw=2.2)
        A.flecha(ax, (X[c] + w / 2, y4 + h4 + 0.3), (X[c] + w / 2, y3 - 0.3))
    A.flecha(ax, (X[3] + w / 2, y2 - 0.3), (X[3] + w / 2, y3 + h3 + 0.3))
    A.flecha(ax, (X[3] - 0.3, y3 + h3 / 2), (X[2] + w + 0.3, y3 + h3 / 2))
    A.flecha(ax, (X[2] - 0.3, y3 + h3 / 2), (X[1] + w + 0.3, y3 + h3 / 2))
    # retroalimentación de las compuertas a la corrección (doble bucle)
    xr = X[1] + w * 0.62
    A.flecha(ax, (xr, y3 + h3 + 0.3), (xr, y2 - 0.3), ls=DISCONT, lw=1.8)
    A.txt(ax, xr - 1.2, (y3 + h3 + y2) / 2, "Revisión de las\nvariables de gobierno", F_B, ha="right")
    # leyenda
    xl = x0
    yl = y3 + h3
    ax.add_patch(plt.Rectangle((xl, yl - 2.0), 3.6, 2.0, fc=MEDIO, ec=T, lw=2.0))
    A.txt(ax, xl + 5, yl - 1.0, "Teorías", F_B)
    ax.add_patch(plt.Rectangle((xl, yl - 6.0), 3.6, 2.0, fc=CAJA, ec=T, lw=1.2))
    A.txt(ax, xl + 5, yl - 5.0, "Componentes", F_B)
    ax.plot([xl, xl + 3.6], [yl - 9.4, yl - 9.4], color=T, lw=1.8, ls=DISCONT)
    A.lineas(ax, xl + 5, yl - 8.3, "Aprendizaje de doble bucle", F_B, ancho=15.2)
    return A.guardar(fig, "c9_f01")


# ------------------------------------------------------------------ c10_f01
# (nombre, grupo, poder, interés); grupo: I interno, P externo primario, S externo secundario. Valores de la tabla de interesados de la
# sección 10 (poder e interés en escala de 1 a 10; alto = 6 o más).
INTERESADOS = [
    ("Universidad Santo Tomás", "I", 8, 9), ("Gerencia de proyecto", "I", 7, 10), ("Equipo técnico y de formación", "I", 4, 9),
    ("Equipo de apropiación y convenios", "I", 3, 8),
    ("Municipios aliados", "P", 7, 8), ("Avanciencia", "P", 6, 8), ("Gestión y Medio Ambiente", "P", 4, 7), ("Financiador", "P", 10, 7),
    ("Consejos municipales", "P", 6, 8), ("Consejos departamentales", "P", 7, 7), ("UNGRD", "P", 8, 5),
    ("Gobernaciones", "P", 8, 4), ("Entidades custodias", "P", 6, 9), ("Personal operario de remoción", "P", 2, 9),
    ("Población expuesta", "P", 2, 6),
     ("Autoridades ambientales", "S", 7, 3), ("Laboratorios y evaluación externa", "S", 5, 3), ("Proveedores", "S", 3, 2),
    ("Comunidad científica", "S", 2, 4),
]
UMBRAL = 5.5


def _inter(a, b, m=0.0):
    w = min(a[2], b[2]) - max(a[0], b[0]) + m
    h = min(a[3], b[3]) - max(a[1], b[1]) + m
    return w * h if (w > 0 and h > 0) else 0.0


def _seg_rect(p, q, r, n=14):
    """True si el segmento pq pasa por el interior del rectángulo r (muestreo)."""
    for k in range(1, n):
        t = k / n
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        if r[0] < x < r[2] and r[1] < y < r[3]:
            return True
    return False


def _seg_seg(a, b, c, d):
    def o(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return o(a, b, c) * o(a, b, d) < 0 and o(c, d, a) * o(c, d, b) < 0


def colocar_etiquetas(fig, ax, puntos, nombres, r_pt, fijos=(), pasadas=8):
    """Coloca etiquetas directas (con línea guía cuando quedan lejos) sin solapes con marcadores, etiquetas, líneas de cuadrante ni bordes.
    Minimiza un costo por descenso de coordenadas; dibuja el resultado y devuelve la penalización de cada etiqueta."""
    import math, random
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    dpi = fig.dpi
    r = r_pt * dpi / 72.0
    pix = [tuple(ax.transData.transform(p)) for p in puntos]
    n = len(pix)
    marc = [(x - r, y - r, x + r, y + r) for x, y in pix]
    ax0, ay0 = ax.transData.transform((ax.get_xlim()[0], ax.get_ylim()[0]))
    ax1, ay1 = ax.transData.transform((ax.get_xlim()[1], ax.get_ylim()[1]))
    lx = ax.transData.transform((UMBRAL, 0))[0]
    ly = ax.transData.transform((0, UMBRAL))[1]
    cuad = lambda x, y: (x > lx, y > ly)

    def variantes(s):
        pal = s.split(" ")
        v = {s}
        for k in (2, 3):
            if len(pal) >= k:
                # reparto equilibrado en k líneas
                best, bs = None, None
                import itertools
                for cuts in itertools.combinations(range(1, len(pal)), k - 1):
                    seg = [" ".join(pal[a:b]) for a, b in zip((0,) + cuts, cuts + (len(pal),))]
                    sc = max(len(t) for t in seg)
                    if bs is None or sc < bs:
                        best, bs = seg, sc
                v.add("\n".join(best))
        return sorted(v, key=lambda t: t.count("\n"))

    tam = {}
    for nm in nombres:
        for v in variantes(nm):
            t = ax.text(0, 0, v, fontsize=P(F_B), ha="left", va="bottom", linespacing=1.15)
            b = t.get_window_extent(rend); t.remove()
            tam[v] = (b.width, b.height)
    d0 = r + 3.0
    angs = [k * math.pi / 8 for k in range(16)]
    dist = [d0, d0 * 1.9, d0 * 3.0, d0 * 4.4, d0 * 6.2]
    cands = []
    for i in range(n):
        cs = []
        for v in variantes(nombres[i]):
            w, h = tam[v]
            for di, d in enumerate(dist):
                for th in angs:
                    c, sn = math.cos(th), math.sin(th)
                    px, py = pix[i][0] + d * c, pix[i][1] + d * sn
                    ha = "left" if c > 0.45 else ("right" if c < -0.45 else "center")
                    va = "bottom" if sn > 0.45 else ("top" if sn < -0.45 else "center")
                    x0 = px - {"left": 0, "right": w, "center": w / 2}[ha]
                    y0 = py - {"bottom": 0, "top": h, "center": h / 2}[va]
                    bb = (x0 - 2, y0 - 1, x0 + w + 2, y0 + h + 1)
                    cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
                    # punto de la caja más cercano al marcador (inicio de la guía)
                    qx = min(max(pix[i][0], bb[0]), bb[2]); qy = min(max(pix[i][1], bb[1]), bb[3])
                    dd = math.hypot(qx - pix[i][0], qy - pix[i][1])
                    guia = None
                    if dd > r + 7:
                        ux, uy = (qx - pix[i][0]) / dd, (qy - pix[i][1]) / dd
                        guia = ((pix[i][0] + ux * r, pix[i][1] + uy * r), (qx, qy))
                    base = 0.0
                    if bb[0] < ax0 + 2 or bb[2] > ax1 - 2 or bb[1] < ay0 + 2 or bb[3] > ay1 - 2:
                        base += 1e6
                    if bb[0] < lx < bb[2]:
                        base += 4000
                    if bb[1] < ly < bb[3]:
                        base += 4000
                    if cuad(cx, cy) != cuad(*pix[i]):
                        base += 1500
                    base += 0.5 * (dd if guia else 0) + 6 * v.count("\n") + 3 * di
                    cs.append(dict(v=v, ha=ha, va=va, x=px, y=py, bb=bb, guia=guia, base=base))
        cands.append(cs)

    def costo(i, c, elegidos):
        pen = c["base"]
        for k, m in enumerate(marc):
            ov = _inter(c["bb"], m)
            if ov:
                pen += 60 * ov
        for fb in fijos:
            ov = _inter(c["bb"], fb)
            if ov:
                pen += 60 * ov
        if c["guia"]:
            for k, m in enumerate(marc):
                if k != i and _seg_rect(c["guia"][0], c["guia"][1], m):
                    pen += 500
            for fb in fijos:
                if _seg_rect(c["guia"][0], c["guia"][1], fb):
                    pen += 500
        for j, e in elegidos.items():
            if j == i:
                continue
            ov = _inter(c["bb"], e["bb"], 3)
            if ov:
                pen += 80 * ov
            if c["guia"] and _seg_rect(c["guia"][0], c["guia"][1], e["bb"]):
                pen += 600
            if e["guia"] and _seg_rect(e["guia"][0], e["guia"][1], c["bb"]):
                pen += 600
            if c["guia"] and e["guia"] and _seg_seg(c["guia"][0], c["guia"][1], e["guia"][0], e["guia"][1]):
                pen += 400
        return pen

    veci = [sum(1 for j, q in enumerate(pix) if j != i and abs(q[0] - pix[i][0]) < 6 * r and abs(q[1] - pix[i][1]) < 6 * r) for i in range(n)]
    orden = sorted(range(n), key=lambda i: -veci[i])
    elegidos = {}
    for i in orden:
        elegidos[i] = min(cands[i], key=lambda c: costo(i, c, elegidos))
    rnd = random.Random(7)
    for _ in range(pasadas):
        ch = False
        o = orden[:]; rnd.shuffle(o)
        for i in o:
            mejor = min(cands[i], key=lambda c: costo(i, c, elegidos))
            if costo(i, mejor, elegidos) < costo(i, elegidos[i], elegidos) - 1e-9:
                elegidos[i] = mejor; ch = True
        if not ch:
            break
    inv = ax.transData.inverted()
    pens = {}
    for i, c in elegidos.items():
        pos = inv.transform((c["x"], c["y"]))
        ax.text(pos[0], pos[1], c["v"], fontsize=P(F_B), ha=c["ha"], va=c["va"], color=T, linespacing=1.15, zorder=6)
        if c["guia"]:
            g0, g1 = inv.transform(c["guia"][0]), inv.transform(c["guia"][1])
            ax.plot([g0[0], g1[0]], [g0[1], g1[1]], color=T, lw=0.8, zorder=3)
        pens[nombres[i]] = costo(i, c, elegidos)
        if pens[nombres[i]] > 400:
            print(f"  AVISO etiqueta {nombres[i]!r}: penalización {pens[nombres[i]]:.0f}")
    return pens


def c10_f01():
    assert len(INTERESADOS) == 19
    cuadr = {}
    for (n, g, p, i) in INTERESADOS:
        q = "cerca" if (p >= 6 and i >= 6) else ("satisfecho" if p >= 6 else ("informado" if i >= 6 else "monitorear"))
        cuadr.setdefault(q, []).append(n)
    assert {k: len(v) for k, v in cuadr.items()} == {"cerca": 8, "satisfecho": 3, "informado": 5, "monitorear": 3}, cuadr
    H = 92
    fig, ax = A.lienzo("Ocho de diecinueve interesados exigen gestión cercana por su poder y su interés",
                       "Posición de cada interesado por interés (eje x) y poder (eje y), escala de 1 a 10; alto = 6 o más", H)
    a = A.subeje(fig, ax, 9, 11.5, 99, H - 1.0)
    a.set_xlim(0.4, 10.8); a.set_ylim(0.4, 10.8)
    a.set_xticks(range(1, 11)); a.set_yticks(range(1, 11))
    a.grid(False)
    a.set_xlabel("Interés (1 a 10)", fontsize=P(F_B), color=T)
    a.set_ylabel("Poder (1 a 10)", fontsize=P(F_B), color=T)
    x0, x1, y0, y1 = 0.4, 10.8, 0.4, 10.8
    a.add_patch(Rectangle((UMBRAL, UMBRAL), x1 - UMBRAL, y1 - UMBRAL, fc=CLARO, ec="none", zorder=0))
    a.add_patch(Rectangle((x0, UMBRAL), UMBRAL - x0, y1 - UMBRAL, fc=GRIS, ec="none", zorder=0))
    a.add_patch(Rectangle((UMBRAL, y0), x1 - UMBRAL, UMBRAL - y0, fc=GRIS, ec="none", zorder=0))
    a.axvline(UMBRAL, color=T, lw=1.1, zorder=1)
    a.axhline(UMBRAL, color=T, lw=1.1, zorder=1)
    nom = [("Mantener satisfecho (3)", 0.55, 10.55, "left"), ("Gestionar de cerca (8)", 10.65, 10.55, "right"),
           ("Monitorear (3)", 0.55, 0.75, "left"), ("Mantener informado (5)", 10.65, 0.75, "right")]
    qt = []
    for s, x, y, ha in nom:
        qt.append(a.text(x, y, s, fontsize=P(F_B), fontweight="bold", color=T, ha=ha, va="center", zorder=5))
    marc = {"I": ("o", AZUL), "P": ("s", MEDIO), "S": ("^", CLARO)}
    # los pares con la misma posición se separan ±0,2 en el eje de interés para que ambos marcadores se vean
    cuenta = {}
    for (_, _, p, i) in INTERESADOS:
        cuenta[(p, i)] = cuenta.get((p, i), 0) + 1
    visto = {}
    pts, nombres = [], []
    for (n, g, p, i) in INTERESADOS:
        k = visto.get((p, i), 0); visto[(p, i)] = k + 1
        dx = 0.0 if cuenta[(p, i)] == 1 else (-0.2 if k == 0 else 0.2)
        m, c = marc[g]
        a.scatter(i + dx, p, marker=m, s=170, facecolor=c, edgecolor=T, linewidth=1.1, zorder=4)
        pts.append((i + dx, p)); nombres.append(n)
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    fijos = [(b.x0 - 2, b.y0 - 2, b.x1 + 2, b.y1 + 2) for b in (t.get_window_extent(rend) for t in qt)]
    colocar_etiquetas(fig, a, pts, nombres, r_pt=P(F_B) * 0.62, fijos=fijos)
    # leyenda por tipo (marcadores)
    yl = 3.4
    for k, (m, c, t) in enumerate([("o", AZUL, "Interno"), ("s", MEDIO, "Externo primario"), ("^", CLARO, "Externo secundario")]):
        xx = 10.0 + [0, 17, 47][k]
        ax.plot([xx], [yl], m, ms=8.5, mfc=c, mec=T, mew=1.1)
        A.txt(ax, xx + 2.0, yl, t, F_B)
    return A.guardar(fig, "c10_f01")


# ------------------------------------------------------------------ c12_f01
def c12_f01():
    H = 96
    fig, ax = A.lienzo("Los tres objetivos específicos convierten las causas priorizadas en medios verificables",
                       "Árbol de objetivos: fines, objetivo general, objetivos específicos con su meta y medios", H)
    xl, xr = 15.0, 99.0
    alt = [9.5, 19.0, 29.0, 19.0]
    gv = 6.2
    ytop = [H - 0.6]
    for a_ in alt[:-1]:
        ytop.append(ytop[-1] - a_ - gv)
    yb = [t - a_ for t, a_ in zip(ytop, alt)]
    for k, nm in enumerate(["Fines", "Objetivo\ngeneral", "Objetivos\nespecíficos", "Medios"]):
        A.txt(ax, 1, yb[k] + alt[k] / 2, nm, F_B, True)
    # fines
    wf = 41.0
    fines = ["Decisiones de riesgo con datos de error conocido", "Uso institucional y continuidad de la vigilancia bajo custodia"]
    for x, t in zip((xl, xr - wf), fines):
        A.caja(ax, x, yb[0], wf, alt[0], t, relleno=CLARO)
    # objetivo general
    A.caja(ax, xl, yb[1], xr - xl, alt[1], [("Objetivo general", "b"), (OG, "n")], relleno=AZUL, lw=2.0, gap=0.5)
    for x in (xl + wf / 2, xr - wf / 2):
        A.flecha(ax, (xl + (xr - xl) / 2 + (-10 if x < 57 else 10), yb[1] + alt[1] + 0.3), (x, yb[0] - 0.3))
    # objetivos específicos y medios
    wo, go = 27.0, 1.5
    xo = [xl + i * (wo + go) for i in range(3)]
    corto = {"OE1": "Corregir la interferencia de humedad y de fracción gruesa y validar el gemelo predictivo",
             "OE2": f"Mantener la disponibilidad de {NODOS} nodos y {GW} gateways y poner en operación el laboratorio de modelación",
             "OE3": "Lograr el uso del tablero y del protocolo de alerta por los consejos y adoptar la evaluación previa de demolición"}
    metas = {"OE1": "R² ≥ 0,70 y NRMSE ≤ 30\u00a0%; FAC2 ≥ 0,5 en 6 eventos",
             "OE2": "Disponibilidad ≥ 90\u00a0%; laboratorio dotado al mes 11",
             "OE3": "Uso en 3 de los 4 consejos; 12 evaluaciones previas"}
    medios = ["Banco de calibración, conjunto de referencia rotativo y modelo de corrección en el gateway; validación con mediciones en demoliciones reales",
              "Energía con 14 días de autonomía, enlace satelital y almacenamiento local de 7 días; laboratorio de modelación con gemelo predictivo",
              "Co-diseño con los consejos, formación y convenios de custodia por tramo; protocolo de evaluación previa de demolición"]
    for i, k in enumerate(("OE1", "OE2", "OE3")):
        A.caja(ax, xo[i], yb[2], wo, alt[2], [(k, "b"), (corto[k], "n"), ("Meta: " + metas[k], "i")], relleno=MEDIO, gap=0.8)
        A.caja(ax, xo[i], yb[3], wo, alt[3], medios[i], relleno=CAJA)
        A.flecha(ax, (xo[i] + wo / 2, yb[3] + alt[3] + 0.3), (xo[i] + wo / 2, yb[2] - 0.3))
        A.flecha(ax, (xo[i] + wo / 2, yb[2] + alt[2] + 0.3), (xl + (xr - xl) / 2 + (i - 1) * 14, yb[1] - 0.3))
    return A.guardar(fig, "c12_f01")


# ------------------------------------------------------------------ c12_f02
def c12_f02():
    ods = [("ODS 3. Salud y bienestar", "Reducir enfermedades y muertes por contaminación del aire; el proyecto no promete efectos en salud"),
           ("ODS 9. Industria, innovación e infraestructura", "Infraestructura fiable y resiliente; capacidades científicas y tecnológicas"),
           ("ODS 11. Ciudades y comunidades sostenibles", "Menos personas afectadas por desastres; atención a la calidad del aire"),
           ("ODS 13. Acción por el clima", "Resiliencia y capacidad institucional ante riesgos y desastres")]
    oes = [("OE1", "Medición verificada de PM2,5 y PM10 y validación del gemelo predictivo"), ("OE2", "Red disponible y laboratorio de modelación"),
           ("OE3", "Uso institucional, custodia y evaluación previa de demolición")]
    # (OE, ODS, tipo): D directa, I indirecta
    links = [(0, 1, "D"), (1, 1, "D"), (2, 2, "D"), (0, 0, "I"), (0, 2, "I"), (1, 3, "I"), (2, 0, "I"), (2, 3, "I")]
    nd = sum(1 for l in links if l[2] == "D"); ni = len(links) - nd
    H = 86
    fig, ax = A.lienzo("Los objetivos específicos contribuyen a cuatro Objetivos de Desarrollo Sostenible",
                       "Contribución de cada objetivo específico a los ODS de la Agenda 2030", H)
    xo, wo = 1.0, 29.0
    xd, wd = 62.0, 37.0
    hd, gd = 14.5, 3.0
    ytop = H - 5.5
    A.txt(ax, xo, H - 1.6, "Objetivos específicos", F_B, True)
    A.txt(ax, xd, H - 1.6, "Objetivos de Desarrollo Sostenible", F_B, True)
    ydb = [ytop - (k + 1) * hd - k * gd for k in range(4)]
    span_c = (ytop + ydb[3]) / 2
    ho = 14.0
    yob = [span_c + (1 - k) * (hd + gd) * 1.35 - ho / 2 for k in range(3)]
    for k, (t, b) in enumerate(ods):
        A.caja(ax, xd, ydb[k], wd, hd, [(t, "b"), (b, "n")], relleno=CLARO, gap=0.5)
    for k, (c, t) in enumerate(oes):
        A.caja(ax, xo, yob[k], wo, ho, [(c, "b"), (t, "n")], relleno=MEDIO, gap=0.5)
    # puntos de salida y de llegada repartidos en el borde de cada caja
    sal = {k: sorted([l for l in links if l[0] == k], key=lambda l: l[1]) for k in range(3)}
    lle = {k: sorted([l for l in links if l[1] == k], key=lambda l: l[0]) for k in range(4)}
    def repartir(n, i, alto):
        paso = min(3.2, (alto - 4.0) / max(n - 1, 1)) if n > 1 else 0
        return (i - (n - 1) / 2) * paso
    for (o, d, tp) in sorted(links, key=lambda l: l[2] == "D"):
        i = sal[o].index((o, d, tp)); j = lle[d].index((o, d, tp))
        p0 = (xo + wo + 0.4, yob[o] + ho / 2 + repartir(len(sal[o]), i, ho))
        p1 = (xd - 0.4, ydb[d] + hd / 2 + repartir(len(lle[d]), j, hd))
        if tp == "D":
            A.flecha(ax, p0, p1, color=AZUL, lw=3.4, ms=17)
        else:
            A.flecha(ax, p0, p1, color=T, lw=1.3, ls=DISCONT, ms=13)
    yl = ydb[3] - 5.0
    ax.plot([xo, xo + 9], [yl, yl], color=AZUL, lw=3.4)
    A.txt(ax, xo + 10.5, yl, f"Contribución directa ({nd})", F_B)
    ax.plot([xd - 12, xd - 3], [yl, yl], color=T, lw=1.3, ls=DISCONT)
    A.txt(ax, xd - 1.5, yl, f"Contribución indirecta ({ni})", F_B)
    A.lineas(ax, xo, yl - 3.6, "Directa: el producto del objetivo es el medio principal de la meta.\nIndirecta: el producto es un insumo de otra acción.",
             F_B)
    return A.guardar(fig, "c12_f02")


if __name__ == "__main__":
    only = sys.argv[1:] or ["c9_f01", "c10_f01", "c12_f01", "c12_f02"]
    for f in only:
        globals()[f]()
