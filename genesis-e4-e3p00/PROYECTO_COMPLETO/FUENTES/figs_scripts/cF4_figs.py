# -*- coding: utf-8 -*-
"""Figuras del Paso 4 (análisis causal) en la plantilla visual única (estilo.py).
Redibuja con matplotlib las diez figuras que el motor entregó en SVG con otra paleta. Mismos datos, sin valores nuevos.

Salidas (figs/out/*.png y .svg, fondo transparente):
  cF4_dag                       DAG principal del estimando E1       (SECCION_4_3/DAG_E1.svg y .alt.md)
  cF4_vester_s0 ... s4          Plano Vester directo por escenario   (SECCION_4_4/RESULTADOS.json)
  cF4_micmac_s2                 Plano MICMAC indirecto de S2, k = 10 (SECCION_4_4/RESULTADOS.json)
  cF4_adec, cF4_atdc            Árboles A-DEC y A-TDC                (SECCION_4_4_MDR/ARBOL_1 y ARBOL_4 .json)
  cF4_aprob                     Árbol de problemas A-PROB            (SECCION_4_5/ARBOL_5 .json)
Ejecución:  python3 -I cF4_figs.py          (genera las diez; con argumentos genera solo las nombradas)
Convenciones de Vester y MICMAC: influencia (activa) en y; dependencia (pasiva) en x; ambos ejes en porcentaje del total
de la matriz; líneas discontinuas en las medianas; clase por mediana (clase_mediana del JSON; en MICMAC, clase_indirecta).
"""
import os, sys, json, textwrap
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import estilo as E
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Polygon
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter, MultipleLocator

TINTA, AZUL, MEDIO, CLARO, GRIS, CAJA = E.TINTA, E.AZUL, E.MEDIO, E.CLARO, E.GRIS, E.CAJA
REPO = "/home/user/docs/genesis-e4-e3p00"
F_DAG = f"{REPO}/SECCION_4_3/DAG_E1.alt.md"
F_RES = f"{REPO}/SECCION_4_4/RESULTADOS.json"
F_A1 = f"{REPO}/SECCION_4_4_MDR/ARBOL_1_SGR_CONV56_AIRE.json"
F_A4 = f"{REPO}/SECCION_4_4_MDR/ARBOL_4_SGR_CONV56_AIRE.json"
F_A5 = f"{REPO}/SECCION_4_5/ARBOL_5_SGR_CONV56_AIRE.json"

AVISOS = []          # avisos de texto fuera de su caja (control de calidad al generar)


# ----------------------------------------------------------------------------------------------------------------
# utilidades comunes
# ----------------------------------------------------------------------------------------------------------------
def lista_y(items):
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " y " + items[-1]


def lienzo_u(h1, h2, figsize=(10, 7), top=0.86, left=0.0, right=1.0, bottom=0.0, pad_h2=8):
    """Lienzo libre cuyas unidades de datos son pulgadas (x de 0 a ancho; y de 0 a alto útil). Devuelve fig, ax."""
    fig, ax = E.lienzo_libre(h1=h1, h2=None, figsize=figsize)
    fig.subplots_adjust(left=left, right=right, bottom=bottom, top=top)
    W = figsize[0] * (right - left)
    H = figsize[1] * (top - bottom)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    if h2:
        E._h2(fig, ax, h2, pad_h2)
    return fig, ax


def _render(fig):
    fig.canvas.draw()
    return fig.canvas.get_renderer()


def medir(fig, texto, fs, bold=False, linespacing=1.2):
    """Ancho y alto en pulgadas de un texto (con saltos de línea) dibujado con la tipografía de la plantilla."""
    r = fig.canvas.get_renderer()
    t = fig.text(0, 0, texto, fontsize=fs, fontweight="bold" if bold else "normal", linespacing=linespacing)
    bb = t.get_window_extent(r)
    t.remove()
    return bb.width / fig.dpi, bb.height / fig.dpi


def envolver(fig, texto, ancho, fs, bold=False):
    """Parte un texto en líneas que no superen `ancho` pulgadas (voraz, por palabras, medido con la fuente real)."""
    lineas = []
    for parrafo in texto.split("\n"):
        actual = ""
        for pal in parrafo.split(" "):
            prueba = pal if not actual else actual + " " + pal
            if medir(fig, prueba, fs, bold)[0] <= ancho or not actual:
                actual = prueba
            else:
                lineas.append(actual)
                actual = pal
        lineas.append(actual)
    return lineas


def caja_u(ax, x, y, w, h, fc=CAJA, ec=TINTA, lw=1.3, ls="-", rs=0.09, hatch=None, z=2):
    """Caja redondeada exacta (sin relleno adicional); (x, y) es la esquina inferior izquierda.
    Si lleva trama, esta se dibuja con trazo suave (MEDIO) debajo de un borde TINTA sin relleno."""
    if hatch:
        plt.rcParams["hatch.linewidth"] = 0.6
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={rs}", fc=fc, ec=MEDIO, lw=0,
                                    hatch=hatch, zorder=z))
        fc = "none"
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={rs}", fc=fc, ec=ec, lw=lw, ls=ls, zorder=z + 0.1)
    ax.add_patch(p)
    return p


def nodo(ax, cx, cy, w, h, titulo, sub=None, fc=CAJA, ls="-", lw=1.3, fs_t=9.5, fs_s=8.3, hatch=None, subs_bold=False):
    """Caja con título en negrita y subtítulo (una o varias líneas); registra el texto para el control de ajuste."""
    p = caja_u(ax, cx - w / 2, cy - h / 2, w, h, fc=fc, ls=ls, lw=lw, hatch=hatch)
    sub_lines = sub.split("\n") if sub else []
    tt = ax.text(cx, cy + (0.065 * len(sub_lines) if sub else 0), titulo, ha="center", va="center", fontsize=fs_t,
                 fontweight="bold", color=TINTA, zorder=5)
    arts = [tt]
    if sub:
        ts = ax.text(cx, cy - 0.09 - 0.0 * len(sub_lines) + (0.0), sub, ha="center", va="top", fontsize=fs_s, color=TINTA,
                     linespacing=1.2, zorder=5)
        arts.append(ts)
    AVISOS.append((ax, arts, (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)))
    return p


def revisar(fig, nombre):
    """Comprueba que cada texto registrado queda dentro de su caja; informa de los que se salen."""
    _render(fig)
    malos = []
    for ax, arts, (x0, y0, x1, y1) in [a for a in AVISOS]:
        inv = ax.transData.inverted()
        for t in arts:
            bb = t.get_window_extent(fig.canvas.get_renderer())
            (a0, b0), (a1, b1) = inv.transform((bb.x0, bb.y0)), inv.transform((bb.x1, bb.y1))
            if a0 < x0 + 0.02 or a1 > x1 - 0.02 or b0 < y0 + 0.01 or b1 > y1 - 0.01:
                malos.append((t.get_text().replace("\n", " | ")[:60], round(a0 - x0, 2), round(x1 - a1, 2),
                              round(b0 - y0, 2), round(y1 - b1, 2)))
    AVISOS.clear()
    for m in malos:
        print(f"  AVISO [{nombre}] texto fuera de caja: {m}")
    return malos


def ruta(ax, pts, color=TINTA, ls="-", lw=1.4, ms=13, cabeza=True, z=3, ls_cabeza="-"):
    """Polilínea ortogonal o recta con punta de flecha sólida en el último punto (trazo `ls` en la línea)."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, ls=ls, lw=lw, zorder=z, solid_capstyle="butt", dash_capstyle="butt")
    if cabeza:
        (x0, y0), (x1, y1) = pts[-2], pts[-1]
        d = max(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5, 1e-6)
        ux, uy = (x1 - x0) / d, (y1 - y0) / d
        a = FancyArrowPatch((x1 - ux * 0.04, y1 - uy * 0.04), (x1, y1), arrowstyle="-|>", mutation_scale=ms, color=color,
                            lw=lw, ls="-", shrinkA=0, shrinkB=0, zorder=z + 1)
        ax.add_patch(a)


def etiqueta(ax, x, y, s, fs=8.5, bold=False, ha="center", va="center", **kw):
    return ax.text(x, y, s, fontsize=fs, fontweight="bold" if bold else "normal", color=TINTA, ha=ha, va=va, zorder=6, **kw)


# ----------------------------------------------------------------------------------------------------------------
# 1. DAG principal del estimando E1
# ----------------------------------------------------------------------------------------------------------------
def cf4_dag():
    # estructura textual (DAG_E1.alt.md): se comprueba que la alternativa siga diciendo lo que dibujamos
    alt = open(F_DAG, encoding="utf-8").read()
    for frase in ["U (sorteo semanal) determina X", "X causa Y (log NMAE de V06), V08 y V09",
                  "V01, V02, V03 y V04 causan Y; V03 modera el efecto de X", "V05 causa V01, V02 y V09",
                  "Y causa V11 y V12, y ambas causan V15", "V15 causa X cuando X no se aleatoriza",
                  "V09 es colisionador entre X y V05"]:
        assert frase in alt, frase
    fig, ax = lienzo_u(
        "El sorteo semanal fija X; V15 retroalimenta a X solo cuando X no se aleatoriza",
        "DAG principal del estimando E1: efecto del método de corrección (X) sobre el error de medición (Y = V06), escenario S2.\n"
        "Trazo continuo: relación dirigida. Discontinuo: retroalimentación o amenaza de identificación. Punteado: moderación.",
        figsize=(10, 7), top=0.855, pad_h2=8)
    H = ax.get_ylim()[1]
    # --- nodos (centro x, centro y, ancho, alto) en pulgadas
    yC, yM, yL, yB = 5.05, 3.55, 2.38, 0.85
    N = {}
    N["U"] = (0.95, yM, 1.55, 0.78)
    N["X"] = (3.0, yM, 1.95, 0.9)
    N["Y"] = (5.75, yM, 1.85, 0.9)
    N["V03"] = (3.45, yC, 1.45, 0.66)
    N["V04"] = (5.0, yC, 1.2, 0.66)
    N["V01"] = (6.3, yC, 1.2, 0.66)
    N["V02"] = (7.6, yC, 1.2, 0.66)
    N["V05"] = (9.15, yC, 1.55, 0.66)
    N["L"] = (5.75, yL, 2.3, 0.92)
    N["V11"] = (8.05, 4.05, 1.6, 0.66)
    N["V12"] = (8.05, 2.95, 1.6, 0.66)
    N["V15"] = (8.05, 1.75, 1.6, 0.66)
    N["V08"] = (1.75, yB, 1.55, 0.66)
    N["V09"] = (3.95, yB, 2.3, 0.78)
    nodo(ax, *N["U"], "U. Sorteo semanal", "asignación aleatoria", fc=CAJA, ls=(0, (5, 3)))
    nodo(ax, *N["X"], "X. Método de corrección", "V07 como intensidad", fc=AZUL, lw=1.6)
    nodo(ax, *N["Y"], "Y. V06", "log NMAE por nodo-semana", fc=AZUL, lw=1.6)
    nodo(ax, *N["V03"], "V03 humedad", "control y moderador", fc=MEDIO)
    nodo(ax, *N["V04"], "V04 viento", "control", fc=MEDIO)
    nodo(ax, *N["V01"], "V01 PM2,5", "control", fc=MEDIO)
    nodo(ax, *N["V02"], "V02 PM10", "control", fc=MEDIO)
    nodo(ax, *N["V05"], "V05 escombros", "causa de V01, V02 y V09", fc=MEDIO)
    nodo(ax, *N["L"], "Latentes L1 a L3", "distancia a la referencia, edad del\nsensor, episodio de humo", fc=GRIS,
         ls=(0, (5, 3)), hatch="///")
    nodo(ax, *N["V11"], "V11 AQHI", "descendiente de Y", fc=CLARO)
    nodo(ax, *N["V12"], "V12 falsas alarmas", "descendiente de Y", fc=CLARO)
    nodo(ax, *N["V15"], "V15 adopción", "retroalimenta a X", fc=CLARO)
    nodo(ax, *N["V08"], "V08 latencia", "descendiente de X", fc=CLARO)
    nodo(ax, *N["V09"], "V09 disponibilidad", "colisionador entre X y V05\nen la muestra observada", fc=CLARO)

    def borde(k, lado):
        cx, cy, w, h = N[k]
        return {"l": cx - w / 2, "r": cx + w / 2, "t": cy + h / 2, "b": cy - h / 2}[lado]

    # --- aristas continuas
    ruta(ax, [(borde("U", "r"), yM), (borde("X", "l"), yM)])                                  # U -> X
    ruta(ax, [(borde("X", "r"), yM), (borde("Y", "l"), yM)])                                  # X -> Y
    yt = borde("Y", "t")
    for k, xo, xd in [("V03", 3.85, 5.0), ("V04", 5.0, 5.45), ("V01", 6.3, 5.95), ("V02", 7.45, 6.5)]:
        ruta(ax, [(xo, borde(k, "b")), (xd, yt)])                                             # V03, V04, V01, V02 -> Y
    ruta(ax, [(borde("V05", "l"), yC), (borde("V02", "r"), yC)])                              # V05 -> V02
    ruta(ax, [(9.3, borde("V05", "t")), (9.3, 5.72), (6.3, 5.72), (6.3, borde("V01", "t"))])  # V05 -> V01
    ruta(ax, [(9.75, borde("V05", "b")), (9.75, yB), (borde("V09", "r"), yB)])                # V05 -> V09
    ruta(ax, [(2.55, borde("X", "b")), (2.55, borde("V08", "t"))])                            # X -> V08
    ruta(ax, [(3.4, borde("X", "b")), (3.4, borde("V09", "t"))])                              # X -> V09
    xs = borde("Y", "r")
    yV11, yV12, yV15 = N["V11"][1], N["V12"][1], N["V15"][1]
    ax.plot([7.05, 7.05], [yV12, yV11], color=TINTA, lw=1.4, zorder=3)
    ruta(ax, [(xs, yM), (7.05, yM)], cabeza=False)
    ruta(ax, [(7.05, yV11), (borde("V11", "l"), yV11)])                                       # Y -> V11
    ruta(ax, [(7.05, yV12), (borde("V12", "l"), yV12)])                                       # Y -> V12
    ruta(ax, [(borde("V12", "r"), yV12), (9.05, yV12), (9.05, yV15 + 0.17), (borde("V15", "r"), yV15 + 0.17)])  # V12 -> V15
    ruta(ax, [(borde("V11", "r"), yV11), (9.35, yV11), (9.35, yV15 - 0.17), (borde("V15", "r"), yV15 - 0.17)])  # V11 -> V15
    # --- amenazas y retroalimentación (discontinuas)
    ruta(ax, [(borde("V15", "l"), yV15), (3.7, yV15), (3.7, borde("X", "b"))], ls=(0, (5, 3)))   # V15 -> X
    ruta(ax, [(5.75, borde("L", "t")), (5.75, borde("Y", "b"))], ls=(0, (5, 3)))                 # L -> Y
    # --- moderación: V03 modula la arista X -> Y (punteada hacia el punto medio de la arista)
    xm = (borde("X", "r") + borde("Y", "l")) / 2
    ruta(ax, [(3.62, borde("V03", "b")), (xm, yM + 0.03)], ls=(0, (1, 2.2)), lw=1.6)
    etiqueta(ax, 3.7, 4.2, "modera X → Y", fs=8.3, ha="left")
    etiqueta(ax, 5.85, yV15 - 0.17, "retroalimentación si X no se aleatoriza", fs=8.3, ha="center", va="top")
    # --- leyenda
    items = [("Asignación", CAJA, (0, (5, 3)), None), ("Intervención y resultado", AZUL, "-", None),
             ("Control", MEDIO, "-", None), ("Descendiente", CLARO, "-", None),
             ("Latente", GRIS, (0, (5, 3)), "///")]
    x = 0.12
    for txt, fc, ls, ha in items:
        caja_u(ax, x, 0.13, 0.30, 0.2, fc=fc, ls=ls, lw=1.1, rs=0.04, hatch=ha)
        etiqueta(ax, x + 0.38, 0.23, txt, fs=8.6, ha="left")
        x += 0.38 + medir(fig, txt, 8.6)[0] + 0.32
    revisar(fig, "cF4_dag")
    E.guardar(fig, "cF4_dag")


# ----------------------------------------------------------------------------------------------------------------
# 2. Planos Vester y MICMAC
# ----------------------------------------------------------------------------------------------------------------
ESC = {  # clave de figura -> (id en RESULTADOS.json, etiqueta corta, frase del escenario para H1)
    "s0": ("S0_HISTORICO_CONDICIONADO", "S0", "del escenario histórico S0"),
    "s1": ("S1_PREVIO_DOC", "S1", "del escenario previo S1"),
    "s2": ("S_TRABAJO_PROPUESTO", "S2", "del escenario de trabajo S2"),
    "s3": ("S3_ENVOLVENTE_ADMISIBLE_BAJA", "S3", "de la envolvente baja S3"),
    "s4": ("S4_ENVOLVENTE_ADMISIBLE_ALTA", "S4", "de la envolvente alta S4"),
}
CLASES = {"CRITICA": "crítica", "ACTIVA": "activa", "REACTIVA": "reactiva", "AUTONOMA_RELATIVA": "autónoma relativa",
          "FRONTERA": "frontera"}


def nombre_var(v):
    return v["nombre"].replace("PM2.5", "PM2,5")


def pct_fmt(v, _=None):
    return E.num(v, 0) + " %"


def colocar_etiquetas(fig, ax, pts, fijos, fs=9.2):
    """Coloca la etiqueta de cada punto en la posición (de ocho candidatas) con menos solapamientos.
    pts: lista de dicts con x, y, txt, bold; fijos: textos ya colocados (obstáculos)."""
    r = _render(fig)
    dpi = fig.dpi
    rad = 8.0 * dpi / 72 * 0.9
    centros = [ax.transData.transform((p["x"], p["y"])) for p in pts]
    cajas_pts = [(cx - rad, cy - rad, cx + rad, cy + rad) for cx, cy in centros]
    ocupadas = [t.get_window_extent(r) for t in fijos]
    ejes = ax.get_window_extent(r)
    cand = [("left", "bottom", (6, 4)), ("left", "top", (6, -4)), ("right", "bottom", (-6, 4)), ("right", "top", (-6, -4)),
            ("center", "bottom", (0, 8)), ("center", "top", (0, -8)), ("left", "center", (9, 0)), ("right", "center", (-9, 0))]

    def solape(a, b):
        w = min(a[2], b[2]) - max(a[0], b[0])
        h = min(a[3], b[3]) - max(a[1], b[1])
        return w * h if (w > 0 and h > 0) else 0.0

    orden = sorted(range(len(pts)), key=lambda i: -sum(1 for j in range(len(pts)) if j != i and
                   abs(centros[i][0] - centros[j][0]) < 60 and abs(centros[i][1] - centros[j][1]) < 40))
    colocados = []
    for i in orden:
        p = pts[i]
        mejor = None
        for k, (ha, va, off) in enumerate(cand):
            t = ax.annotate(p["txt"], xy=(p["x"], p["y"]), xytext=off, textcoords="offset points", ha=ha, va=va,
                            fontsize=fs, fontweight="bold" if p.get("bold") else "normal", color=TINTA, zorder=6,
                            annotation_clip=False)
            bb = t.get_window_extent(r)
            caja = (bb.x0, bb.y0, bb.x1, bb.y1)
            costo = 0.35 * k
            for j, c in enumerate(cajas_pts):
                costo += 6 * solape(caja, c) / 100.0 * (3 if j == i else 1)
            for o in ocupadas:
                costo += 8 * solape(caja, (o.x0, o.y0, o.x1, o.y1)) / 100.0
            if caja[0] < ejes.x0 - 4 or caja[2] > ejes.x1 + 4 or caja[1] < ejes.y0 - 2 or caja[3] > ejes.y1 + 2:
                costo += 400
            if mejor is None or costo < mejor[0]:
                if mejor is not None:
                    mejor[1].remove()
                mejor = (costo, t, bb)
            else:
                t.remove()
        # eliminar candidatas perdedoras ya removidas; conservar la mejor
        ocupadas.append(mejor[2])
        colocados.append(mejor[1])
    # quitar duplicados: las candidatas que mejoraron luego fueron reemplazadas pero siguen en el eje
    return colocados


def colocar_cuadrantes(fig, ax, pts, cx, cy, xmax, ymax):
    """Nombra los cuatro cuadrantes en la esquina de su región con menos choques con los marcadores."""
    r = _render(fig)
    rad = 10.0 * fig.dpi / 72
    marc = [ax.transData.transform((x, y)) for (_, x, y, _) in pts]
    reg = {"CRÍTICA": ((cx, xmax), (cy, ymax), ["se", "ne", "sw", "nw"]),
           "ACTIVA": ((0, cx), (cy, ymax), ["nw", "sw", "ne", "se"]),
           "REACTIVA": ((cx, xmax), (0, cy), ["se", "ne", "sw", "nw"]),
           "AUTÓNOMA\nRELATIVA": ((0, cx), (0, cy), ["sw", "nw", "se", "ne"])}
    # preferencia de esquinas: la exterior del cuadrante primero
    pref = {"CRÍTICA": ["ne", "nw", "se", "sw"], "ACTIVA": ["nw", "ne", "sw", "se"],
            "REACTIVA": ["se", "sw", "ne", "nw"], "AUTÓNOMA\nRELATIVA": ["sw", "se", "nw", "ne"]}
    ocupadas = []
    out = []
    for nombre, ((x0, x1), (y0, y1), _) in reg.items():
        mejor = None
        for k, esq in enumerate(pref[nombre]):
            xx = x1 if "e" in esq else x0
            yy = y1 if "n" in esq else y0
            ha = "right" if "e" in esq else "left"
            va = "top" if "n" in esq else "bottom"
            off = (-6 if ha == "right" else 6, -5 if va == "top" else 5)
            t = ax.annotate(nombre, xy=(xx, yy), xytext=off, textcoords="offset points", ha=ha, va=va, fontsize=9.5,
                            fontweight="bold", color=TINTA, zorder=2, linespacing=1.15, annotation_clip=False)
            bb = t.get_window_extent(r)
            costo = 0.5 * k
            for (mx, my) in marc:
                w = min(bb.x1, mx + rad) - max(bb.x0, mx - rad)
                h = min(bb.y1, my + rad) - max(bb.y0, my - rad)
                if w > 0 and h > 0:
                    costo += w * h / 30.0
            for o in ocupadas:
                if min(bb.x1, o.x1) > max(bb.x0, o.x0) and min(bb.y1, o.y1) > max(bb.y0, o.y0):
                    costo += 50
            if mejor is None or costo < mejor[0]:
                if mejor is not None:
                    mejor[1].remove()
                mejor = (costo, t, bb)
            else:
                t.remove()
        ocupadas.append(mejor[2])
        out.append(mejor[1])
    return out


def plano_scatter(nombre, h1, h2, pts, clases, cortes, totales, ejes_lbl, nota, filas_clave, cab_clave, ylim_extra=1.20):
    """Plano de cuadrantes (Vester o MICMAC). pts: lista (id, x%, y%, clase)."""
    fig, ax = E.lienzo(h1=h1, h2=None, figsize=(10, 7), grid=False)
    fig.subplots_adjust(left=0.085, right=0.70, bottom=0.15, top=0.87)
    E._h2(fig, ax, h2, 10)
    xs = [p[1] for p in pts]
    ys = [p[2] for p in pts]
    xmax = max(xs) * 1.10 + 0.4
    ymax = max(ys) * ylim_extra + 0.4
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    step = 2 if xmax <= 18 else 5
    ax.xaxis.set_major_locator(MultipleLocator(step))
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.xaxis.set_major_formatter(FuncFormatter(pct_fmt))
    ax.yaxis.set_major_formatter(FuncFormatter(pct_fmt))
    ax.tick_params(labelsize=9.5)
    ax.set_xlabel(ejes_lbl[0], fontsize=10, labelpad=6)
    ax.set_ylabel(ejes_lbl[1], fontsize=10, labelpad=6)
    cx, cy = cortes
    ax.axvline(cx, color=TINTA, ls=(0, (5, 3)), lw=1.0, zorder=1)
    ax.axhline(cy, color=TINTA, ls=(0, (5, 3)), lw=1.0, zorder=1)
    # cuadrante crítico sombreado (CLARO) con trama para no depender solo del color
    ax.add_patch(Rectangle((cx, cy), xmax - cx, ymax - cy, fc=CLARO, ec="none", alpha=0.22, zorder=0))
    # nombres de los cuadrantes (se colocan tras fijar los límites, evitando los marcadores)
    fijos = colocar_cuadrantes(fig, ax, pts, cx, cy, xmax, ymax)
    # marcadores
    estilo = {"CRITICA": dict(marker="o", s=125, fc=AZUL, lw=1.4, z=5),
              "FRONTERA": dict(marker="D", s=70, fc=MEDIO, lw=1.2, z=4),
              "OTRA": dict(marker="o", s=75, fc=CLARO, lw=1.2, z=4)}
    # agrupar puntos coincidentes
    grupos = {}
    for (vid, x, y, c) in pts:
        grupos.setdefault((round(x, 6), round(y, 6)), []).append((vid, c))
    lista = []
    for (x, y), g in grupos.items():
        c = "CRITICA" if any(cc == "CRITICA" for _, cc in g) else ("FRONTERA" if any(cc == "FRONTERA" for _, cc in g) else "OTRA")
        st = estilo[c]
        ax.scatter([x], [y], marker=st["marker"], s=st["s"], c=st["fc"], edgecolors=TINTA, linewidths=st["lw"], zorder=st["z"],
                   clip_on=False)
        lista.append(dict(x=x, y=y, txt=", ".join(v for v, _ in g), bold=(c == "CRITICA")))
    n_antes = len(ax.texts)
    colocar_etiquetas(fig, ax, lista, fijos)
    depurar_anotaciones(ax, n_antes, lista)
    # ----- panel derecho: clave de variables
    ak = fig.add_axes([0.715, 0.15, 0.275, 0.72])
    ak.axis("off")
    ak.set_xlim(0, 1)
    ak.set_ylim(0, 1)
    n = len(filas_clave)
    ak.text(0.0, 1.0, cab_clave, fontsize=9.2, fontweight="bold", va="top", ha="left", color=TINTA, linespacing=1.25)
    y0 = 0.915
    pitch = 0.0445
    for i, (vid, nom, c, dato) in enumerate(filas_clave):
        yy = y0 - i * pitch
        k = "CRITICA" if c == "CRITICA" else ("FRONTERA" if c == "FRONTERA" else "OTRA")
        st = estilo[k]
        ak.scatter([0.03], [yy], marker=st["marker"], s=st["s"] * 0.55, c=st["fc"], edgecolors=TINTA, linewidths=0.9,
                   zorder=5, clip_on=False)
        ak.text(0.08, yy, f"{vid} {nom}", fontsize=8.4, va="center", ha="left", color=TINTA,
                fontweight="bold" if c == "CRITICA" else "normal")
        ak.text(1.0, yy, dato, fontsize=8.4, va="center", ha="right", color=TINTA,
                fontweight="bold" if c == "CRITICA" else "normal")
    yl = y0 - n * pitch - 0.035
    ak.add_line(Line2D([0.0, 1.0], [yl + 0.022, yl + 0.022], color=TINTA, lw=0.6))
    leyenda = [("CRITICA", "crítica (en negrita)"), ("FRONTERA", "frontera: coincide con una mediana"),
               ("OTRA", "activa, reactiva o autónoma relativa")]
    for i, (k, txt) in enumerate(leyenda):
        yy = yl - i * 0.044
        st = estilo[k]
        ak.scatter([0.03], [yy], marker=st["marker"], s=st["s"] * 0.55, c=st["fc"], edgecolors=TINTA, linewidths=0.9,
                   zorder=5, clip_on=False)
        ak.text(0.08, yy, txt, fontsize=8.4, va="center", ha="left", color=TINTA)
    yy = yl - 3 * 0.044
    ak.add_line(Line2D([0.0, 0.06], [yy, yy], color=TINTA, lw=1.0, ls=(0, (5, 3))))
    ak.text(0.08, yy, "mediana de cada eje (corte)", fontsize=8.4, va="center", ha="left", color=TINTA)
    fig.text(0.01, 0.045, nota, fontsize=8.6, color=TINTA, ha="left", va="center", linespacing=1.3)
    E.guardar(fig, nombre)


def depurar_anotaciones(ax, n_antes, lista):
    """colocar_etiquetas deja las candidatas perdedoras eliminadas; aquí no hay nada más que depurar (compatibilidad)."""
    return None


def datos_vester(clave):
    res = json.load(open(F_RES, encoding="utf-8"))
    vid_esc = ESC[clave][0]
    esc = res["escenarios"][vid_esc]
    nombres = {v["id"]: nombre_var(v) for v in res["variables"]}
    tot = esc["total"]
    filas = []
    for r in esc["directa"]:
        filas.append(dict(id=r["id"], I=r["influencia"], D=r["dependencia"], clase=r["clase_mediana"],
                          x=r["dependencia"] / tot * 100, y=r["influencia"] / tot * 100, nombre=nombres[r["id"]]))
    return res, esc, filas


def cf4_vester(clave):
    res, esc, filas = datos_vester(clave)
    vid_esc, corto, frase = ESC[clave]
    crit = [f["id"] for f in filas if f["clase"] == "CRITICA"]
    assert crit, clave
    tot = esc["total"]
    aristas = esc["diagnosticos"]["aristas_positivas"]
    mi, md = esc["mediana_I"], esc["mediana_D"]
    h1 = f"{lista_y(crit)} son las variables críticas {frase}"
    h2 = (f"Plano de Vester directo, {corto} ({vid_esc}): {aristas} aristas con peso mayor que cero; corte por mediana "
          f"(influencia = {mi}, dependencia = {md}; suma total = {tot}).\nJuicios PROPUESTOS, NO RATIFICADOS.")
    pts = [(f["id"], f["x"], f["y"], f["clase"]) for f in filas]
    cortes = (md / tot * 100, mi / tot * 100)
    clave_filas = [(f["id"], f["nombre"], f["clase"], f"{f['I']}; {f['D']}") for f in filas]
    plano_scatter(f"cF4_vester_{clave}", h1, h2, pts, None, cortes, tot,
                  (f"Dependencia (pasiva): % de la suma total de la matriz (total = {tot})",
                   f"Influencia (activa): % de la suma total (total = {tot})"),
                  "Los cuadrantes describen la posición estructural en la matriz y no acreditan causalidad.\n"
                  "Los puntos coincidentes comparten etiqueta. La clase se asigna con el corte por mediana.",
                  clave_filas, "Variable\n(influencia; dependencia)")
    return crit


def cf4_micmac_s2():
    res = json.load(open(F_RES, encoding="utf-8"))
    esc = res["escenarios"]["S_TRABAJO_PROPUESTO"]
    m = esc["micmac"]
    nombres = {v["id"]: nombre_var(v) for v in res["variables"]}
    k = m["k_referencia"]
    tI = sum(c["I_indirecta"] for c in m["contraste"])
    tD = sum(c["D_indirecta"] for c in m["contraste"])
    assert tI == tD
    filas = []
    for c in m["contraste"]:
        filas.append(dict(id=c["id"], x=c["D_porcentaje_indirecta"], y=c["I_porcentaje_indirecta"], clase=c["clase_indirecta"],
                          rI=c["rango_I_indirecto"]))
    cortes = (m["corte_D_exacto"] / tD * 100, m["corte_I_exacto"] / tI * 100)
    crit = [f["id"] for f in filas if f["clase"] == "CRITICA"]
    lider = max(filas, key=lambda f: f["y"])
    assert lider["rI"] == 1.0
    h1 = f"Con k = {k}, {lista_y(crit)} son críticas y {lider['id']} es la más influyente"
    h2 = (f"Plano MICMAC indirecto, S2 (S_TRABAJO_PROPUESTO): potencia de referencia k = {k} "
          f"(estado: sin estabilidad observada hasta kmax = {m['kmax']}); corte por mediana.\nJuicios PROPUESTOS, NO RATIFICADOS.")
    pts = [(f["id"], f["x"], f["y"], f["clase"]) for f in filas]
    clave_filas = [(f["id"], nombres[f["id"]], f["clase"], f"{E.num(f['y'], 1)}; {E.num(f['x'], 1)}") for f in filas]
    plano_scatter("cF4_micmac_s2", h1, h2, pts, None, cortes, tI,
                  (f"Dependencia indirecta (pasiva): % del total de recorridos (k = {k})",
                   f"Influencia indirecta (activa): % del total (k = {k})"),
                  "Longitudes de recorridos entre variables, no unidades de tiempo ni efectos causales. Los cuadrantes no acreditan causalidad.\n"
                  "Los puntos coincidentes comparten etiqueta. Clase indirecta por el corte por mediana de cada eje.",
                  clave_filas, "Variable\n(influencia %; dependencia %)")
    return crit, lider["id"]


# ----------------------------------------------------------------------------------------------------------------
# 3. Árboles (A-PROB, A-TDC, A-DEC): texto íntegro del JSON canónico
# ----------------------------------------------------------------------------------------------------------------
def h2_arbol(d, extra=None):
    """H2 del árbol: título del JSON, naturaleza y fuente; opcionalmente la pregunta."""
    t = f"{d['titulo']}.\nNaturaleza: {d['naturaleza']}. Fuente: {d['fuente']}."
    if extra:
        t += "\n" + extra
    return t


def alto_texto(fig, ancho, partes, interlin=0.035):
    """partes: [(texto, fs, bold)] -> (lista de (lineas, fs, bold, alto), alto total)."""
    plan, tot = [], 0.0
    for txt, fs, bold in partes:
        lineas = envolver(fig, txt, ancho, fs, bold)
        _, h = medir(fig, "\n".join(lineas), fs, bold)
        plan.append((lineas, fs, bold, h))
        tot += h
    tot += interlin * (len(partes) - 1)
    return plan, tot


def dibujar_partes(ax, x, ytop, plan, interlin=0.035, ha="left", cx=None):
    y = ytop
    for lineas, fs, bold, h in plan:
        ax.text(x if ha == "left" else cx, y, "\n".join(lineas), ha=ha, va="top", fontsize=fs,
                fontweight="bold" if bold else "normal", color=TINTA, linespacing=1.2, zorder=5)
        y -= h + interlin
    return y


def icono(ax, kind, x, y, ms=6.8):
    mk = {"decision": "s", "azar": "o", "terminal": "<"}[kind]
    ax.plot([x], [y], marker=mk, ms=ms, mfc=CAJA if kind != "decision" else CAJA, mec=TINTA, mew=1.1, zorder=6, ls="none")


def nodo_arbol(fig, ax, x, ytop, w, partes, fc, kind=None, lw=1.2, ls="-", h=None, pad=0.07, fs_pad=0.0):
    """Nodo de árbol con texto alineado a la izquierda (admite icono de decisión, azar o resultado)."""
    sangria = 0.2 if kind else 0.0
    plan, tot = alto_texto(fig, w - 2 * pad - sangria, partes)
    alto = h if h else tot + 2 * pad + 0.02
    caja_u(ax, x, ytop - alto, w, alto, fc=fc, lw=lw, ls=ls, rs=0.07)
    dibujar_partes(ax, x + pad + sangria, ytop - pad - 0.01, plan)
    if kind:
        icono(ax, kind, x + pad + 0.07, ytop - pad - 0.075)
    return alto


# ---- A-PROB ----------------------------------------------------------------------------------------------------
def cf4_aprob():
    d = json.load(open(F_A5, encoding="utf-8"))
    nodos = {n["id"]: n for n in d["nodos"]}
    niveles = d["niveles"]
    assert len(nodos) == 10 and len(d["enlaces"]) == 10
    fig, ax = lienzo_u("El error de medición sin verificar (V06) une cuatro causas con dos efectos",
                       h2_arbol(d), figsize=(10, 8), top=0.885)
    H = ax.get_ylim()[1]
    ylev = {0: H - 0.75, 1: H - 2.05, 2: H - 3.35, 3: H - 4.65, 4: H - 5.95}
    cx5 = 5.7
    X = {"V03": 2.6, "V02": 4.65, "V01": 6.7, "V07": 8.75}
    pos = {"V14": (4.2, 0), "V15": (7.2, 0), "V11": (4.2, 1), "V12": (7.2, 1), "V06": (cx5, 2),
           "V03": (X["V03"], 3), "V02": (X["V02"], 3), "V01": (X["V01"], 3), "V07": (X["V07"], 3), "V05": (cx5, 4)}
    assert set(pos) == set(nodos)
    fill = {0: GRIS, 1: CLARO, 2: AZUL, 3: MEDIO, 4: GRIS}
    ancho = {k: (3.3 if k == "V06" else 2.45) for k in nodos}
    ancho.update({"V03": 1.95, "V02": 1.95, "V01": 1.95, "V07": 1.95})
    geo = {}
    for k, (cx, lv) in pos.items():
        w = ancho[k]
        bold = (k == "V06")
        plan, tot = alto_texto(fig, w - 0.2, [(nodos[k]["texto"], 9.6, bold)])
        h = max(0.78, tot + 0.2)
        geo[k] = (cx, ylev[lv], w, h)
        caja_u(ax, cx - w / 2, ylev[lv] - h / 2, w, h, fc=fill[lv], lw=2.2 if bold else 1.3,
               ls=(0, (5, 3)) if lv == 4 else "-", rs=0.08)
        dibujar_partes(ax, cx, ylev[lv] + tot / 2, plan, ha="center", cx=cx)
    for lv, nm in enumerate(niveles):
        ax.text(0.12, ylev[lv], nm.replace(" ", "\n", 1), fontsize=9.6, fontweight="bold", color=TINTA, va="center",
                ha="left", linespacing=1.2)

    def top(k): return geo[k][1] + geo[k][3] / 2
    def bot(k): return geo[k][1] - geo[k][3] / 2
    ylo = lambda a, b: (bot(a) + top(b)) / 2 if False else None
    # relaciones: de causa a efecto (flecha hacia arriba)
    yb2 = (top("V07") + bot("V06")) / 2           # bus entre causas directas y problema central
    for a, xa in [("V03", None), ("V02", None), ("V01", None), ("V07", None)]:
        xo = geo[a][0]
        xd = {"V03": 4.6, "V02": 5.35, "V01": 6.05, "V07": 6.8}[a]
        ruta(ax, [(xo, top(a)), (xo, yb2 if abs(xo - xd) > 0.01 else top(a)), (xd, yb2), (xd, bot("V06"))] if abs(xo - xd) > 0.01
             else [(xo, top(a)), (xd, bot("V06"))], ms=14)
    yb1 = (top("V05") + bot("V01")) / 2
    for b, xo, xd in [("V02", 5.3, geo["V02"][0]), ("V01", 6.1, geo["V01"][0])]:
        ruta(ax, [(xo, top("V05")), (xo, yb1), (xd, yb1), (xd, bot(b))], ms=14)
    yb3 = (top("V06") + bot("V11")) / 2
    for b, xo in [("V11", 4.95), ("V12", 6.45)]:
        ruta(ax, [(xo, top("V06")), (xo, yb3), (geo[b][0], yb3), (geo[b][0], bot(b))], ms=14)
    ruta(ax, [(geo["V11"][0], top("V11")), (geo["V11"][0], bot("V14"))], ms=14)
    ruta(ax, [(geo["V12"][0], top("V12")), (geo["V12"][0], bot("V15"))], ms=14)
    # las diez relaciones del JSON coinciden con las dibujadas
    dib = {("V05", "V02"), ("V05", "V01"), ("V03", "V06"), ("V02", "V06"), ("V01", "V06"), ("V07", "V06"), ("V06", "V11"),
           ("V06", "V12"), ("V11", "V14"), ("V12", "V15")}
    assert dib == {(e["de"], e["a"]) for e in d["enlaces"]}
    # leyenda y notas
    yl = 0.62
    items = [("Problema central", AZUL, "-"), ("Causa directa", MEDIO, "-"), ("Efecto directo", CLARO, "-"),
             ("Causa o efecto indirecto", GRIS, "-")]
    x = 0.12
    for txt, fc, ls in items:
        caja_u(ax, x, yl - 0.1, 0.3, 0.2, fc=fc, lw=1.1, rs=0.04, ls=("-" if txt != "Causa o efecto indirecto" else "-"))
        etiqueta(ax, x + 0.38, yl, txt, fs=8.8, ha="left")
        x += 0.38 + medir(fig, txt, 8.8)[0] + 0.3
    ruta(ax, [(x, yl - 0.07), (x + 0.5, yl - 0.07)], ms=12)
    etiqueta(ax, x + 0.58, yl - 0.07, "Relación causa → efecto", fs=8.8, ha="left")
    ax.text(0.12, 0.25, f"Pregunta: {d['pregunta']}", fontsize=8.8, color=TINTA, ha="left", va="center")
    ax.text(0.12, 0.05, "Todas las relaciones son hipótesis de influencia estructural sin efecto estimado; las causas van debajo "
                        "del problema central y los efectos encima.", fontsize=8.8, color=TINTA, ha="left", va="center")
    E.guardar(fig, "cF4_aprob")


# ---- A-TDC -----------------------------------------------------------------------------------------------------
def cf4_atdc():
    d = json.load(open(F_A4, encoding="utf-8"))
    nodos = {n["id"]: n for n in d["nodos"]}
    niveles = d["niveles"]
    assert len(nodos) == 11 and len(d["enlaces"]) == 12 and d["techo_despues_de"] == 1
    fig, ax = lienzo_u("El techo de rendición de cuentas queda tras los resultados inmediatos",
                       h2_arbol(d, f"Pregunta: {d['pregunta']}"), figsize=(10, 8), top=0.865)
    H = ax.get_ylim()[1]
    colx = {0: 1.12, 1: 3.82, 2: 6.58, 3: 9.1}
    colw = {0: 2.0, 1: 2.0, 2: 2.0, 3: 1.6}
    y0 = H - 0.78
    pit = 0.92
    ypos = {"P1": y0, "P2": y0 - pit, "P3": y0 - 2 * pit, "P4": y0 - 3 * pit,
            "R2": y0, "R1": y0 - pit, "R3": y0 - 2 * pit,
            "I2": y0 - 0.5 * pit, "I1": y0 - 2 * pit, "I3": y0 - 3 * pit, "IM": y0 - 1.5 * pit}
    assert set(ypos) == set(nodos)
    fill = {0: GRIS, 1: CLARO, 2: MEDIO, 3: AZUL}
    geo = {}
    for k, n in nodos.items():
        lv = n["nivel"]
        w = colw[lv]
        bold = bool(n.get("destacado"))
        plan, tot = alto_texto(fig, w - 0.2, [(n["texto"], 8.9 if not bold else 9.2, bold)])
        h = max(0.64, tot + 0.2)
        geo[k] = (colx[lv], ypos[k], w, h)
        caja_u(ax, colx[lv] - w / 2, ypos[k] - h / 2, w, h, fc=fill[lv], lw=1.9 if bold else 1.3, rs=0.08)
        dibujar_partes(ax, colx[lv], ypos[k] + tot / 2, plan, ha="center", cx=colx[lv])
    # encabezados de nivel
    for lv, nm in enumerate(niveles):
        ax.text(colx[lv], H - 0.2, nm, ha="center", va="center", fontsize=10, fontweight="bold", color=TINTA)

    L = lambda k: geo[k][0] - geo[k][2] / 2
    R = lambda k: geo[k][0] + geo[k][2] / 2
    T = lambda k: geo[k][1] + geo[k][3] / 2
    B = lambda k: geo[k][1] - geo[k][3] / 2
    Y = lambda k: geo[k][1]
    rutas = {}
    rutas[("P1", "R2")] = [(R("P1"), Y("P1")), (L("R2"), Y("R2"))]
    rutas[("P1", "R1")] = [(R("P1"), Y("P1") - 0.2), (L("R1"), Y("R1") + 0.18)]
    rutas[("P2", "R1")] = [(R("P2"), Y("P2") - 0.05), (L("R1"), Y("R1") - 0.12)]
    rutas[("P3", "R3")] = [(R("P3"), Y("P3")), (L("R3"), Y("R3"))]
    rutas[("P4", "I3")] = [(R("P4"), Y("P4")), (L("I3"), Y("I3"))]
    rutas[("R2", "I2")] = [(R("R2"), Y("R2") - 0.1), (L("I2"), Y("I2") + 0.17)]
    rutas[("R1", "I2")] = [(R("R1"), Y("R1") + 0.1), (L("I2"), Y("I2") - 0.17)]
    rutas[("R3", "I1")] = [(R("R3"), Y("R3")), (L("I1"), Y("I1"))]
    xim = L("IM") - 0.38
    rutas[("I2", "IM")] = [(R("I2"), Y("I2")), (xim, Y("I2")), (xim, Y("IM") + 0.28), (L("IM"), Y("IM") + 0.28)]
    rutas[("I1", "IM")] = [(R("I1"), Y("I1")), (L("IM"), Y("I1") + 0.0)]
    rutas[("I3", "IM")] = [(R("I3"), Y("I3")), (xim, Y("I3")), (xim, Y("IM") - 0.28), (L("IM"), Y("IM") - 0.28)]
    for (a, b), pts in rutas.items():
        ruta(ax, pts, ms=13)
    # retroalimentación I1 -> P4 (discontinua)
    yfb = (B("P3") + T("P4")) / 2
    xfb = geo["P4"][0]
    ruta(ax, [(geo["I1"][0] - 0.55, B("I1")), (geo["I1"][0] - 0.55, yfb), (xfb, yfb), (xfb, T("P4"))], ls=(0, (5, 3)), ms=13)
    # supuestos críticos como rótulos de flecha
    sc = {(e["de"], e["a"]): e.get("supuesto") for e in d["enlaces"]}
    assert set(sc) == set(rutas) | {("I1", "P4")}
    pos_sc = {("P1", "R2"): (2.47, Y("P1") + 0.11), ("P1", "R1"): (2.62, (Y("P1") + Y("R1")) / 2 + 0.2),
              ("P2", "R1"): (2.47, Y("P2") - 0.2), ("P3", "R3"): (2.47, Y("P3") + 0.11),
              ("P4", "I3"): (3.0, Y("P4") - 0.12), ("R3", "I1"): (4.99, Y("R3") + 0.11),
              ("I1", "IM"): (xim + 0.18, Y("I1") + 0.12), ("I3", "IM"): (xim + 0.08, Y("IM") - 0.52)}
    for (a, b), (x, y) in pos_sc.items():
        if sc[(a, b)]:
            etiqueta(ax, x, y, sc[(a, b)], fs=8.8, bold=True)
    for (a, b), v in sc.items():
        if v and (a, b) not in pos_sc and (a, b) != ("I1", "P4"):
            print("  AVISO atdc: supuesto sin rótulo", a, b, v)
    etiqueta(ax, 3.7, yfb - 0.0 + 0.0, "retroalimentación", fs=8.6, ha="center", va="center")
    # techo de rendición de cuentas
    xt = (R("R1") + L("I1")) / 2
    ax.plot([xt, xt], [H - 0.35, 2.82 + 0.0], color=TINTA, lw=1.5, ls=(0, (6, 3, 1.5, 3)), zorder=2)
    etiqueta(ax, xt - 0.12, 2.92, "Bajo control del proyecto", fs=9, bold=True, ha="right")
    etiqueta(ax, xt + 0.12, 2.92, "Contribución con otros actores", fs=9, bold=True, ha="left")
    etiqueta(ax, xt, 2.74, "Techo de rendición de cuentas", fs=8.8, ha="center")
    # supuestos críticos (texto íntegro del JSON)
    ytop = 2.56
    ax.text(0.12, ytop, "Supuestos críticos (SI … ENTONCES … PORQUE …)", fontsize=9.6, fontweight="bold", color=TINTA, va="top")
    y = ytop - 0.22
    for sp in d["supuestos"]:
        txt = (f"{sp['id']} · SI {sp['si']} ENTONCES {sp['entonces']} PORQUE {sp['porque']} · {sp['naturaleza']} · "
               f"nodo de A-DEC: {sp['nodo_arbol']}")
        plan, tot = alto_texto(fig, 9.7, [(txt, 8.0, False)])
        ax.text(0.14, y, "\n".join(plan[0][0]), fontsize=8.0, color=TINTA, va="top", ha="left", linespacing=1.2)
        y -= tot + 0.055
    ysc_fin = y
    # leyenda
    yl = max(ysc_fin - 0.12, 0.25)
    x = 0.12
    for txt, fc in [("Producto", GRIS), ("Resultado inmediato", CLARO), ("Resultado intermedio", MEDIO), ("Impacto", AZUL)]:
        caja_u(ax, x, yl - 0.1, 0.3, 0.2, fc=fc, lw=1.1, rs=0.04)
        etiqueta(ax, x + 0.38, yl, txt, fs=8.6, ha="left")
        x += 0.38 + medir(fig, txt, 8.6)[0] + 0.28
    ruta(ax, [(x, yl), (x + 0.45, yl)], ms=11)
    etiqueta(ax, x + 0.53, yl, "Relación causal", fs=8.6, ha="left")
    x += 0.53 + medir(fig, "Relación causal", 8.6)[0] + 0.28
    ruta(ax, [(x, yl), (x + 0.45, yl)], ms=11, ls=(0, (5, 3)))
    etiqueta(ax, x + 0.53, yl, "Retroalimentación", fs=8.6, ha="left")
    x += 0.53 + medir(fig, "Retroalimentación", 8.6)[0] + 0.28
    ax.plot([x, x + 0.45], [yl, yl], color=TINTA, lw=1.5, ls=(0, (6, 3, 1.5, 3)))
    etiqueta(ax, x + 0.53, yl, "Techo de rendición de cuentas", fs=8.6, ha="left")
    ax.text(0.12, yl - 0.24, "Mapeo inverso: se construye desde el impacto hacia las precondiciones. Cada flecha rotulada remite a un "
            "supuesto SC-n verificable.", fontsize=8.4, color=TINTA, ha="left", va="center")
    print("  atdc: fondo del bloque de supuestos y =", round(ysc_fin, 2), "leyenda y =", round(yl, 2))
    E.guardar(fig, "cF4_atdc")


# ---- A-DEC -----------------------------------------------------------------------------------------------------
def cf4_adec():
    d = json.load(open(F_A1, encoding="utf-8"))
    raiz = d["raiz"]
    assert raiz["tipo"] == "DECISION" and len(raiz["hijos"]) == 3
    fig, ax = lienzo_u("Sin probabilidades ni utilidades, A-DEC no marca ninguna rama elegida",
                       h2_arbol(d), figsize=(10, 8), top=0.885)
    H = ax.get_ylim()[1]
    NIV = {"PRODUCTO": GRIS, "RESULTADO_INMEDIATO": CLARO, "RESULTADO_INTERMEDIO": MEDIO, "IMPACTO": AZUL}
    FS = 8.0
    # --- estructura: cada opción es una cadena de nodos de azar; "falla" sale a un resultado, "se cumple" sigue
    def cadena(nodo):
        azar, fallas, final = [], [], None
        cur = nodo
        while cur["tipo"] == "AZAR":
            azar.append(cur)
            ok = [h for h in cur["hijos"] if h["rama"].endswith("se cumple")]
            ko = [h for h in cur["hijos"] if h["rama"].endswith("falla")]
            assert len(ok) == 1 and len(ko) == 1
            fallas.append((ko[0]["rama"], ko[0]["nodo"]))
            cur = ok[0]["nodo"]
            final_rama = ok[0]["rama"]
        return azar, fallas, (final_rama, cur)
    opciones = {}
    for h in raiz["hijos"]:
        if h["nodo"]["tipo"] == "AZAR":
            opciones[h["rama"][:2]] = (h["rama"], cadena(h["nodo"]))
        else:
            opciones[h["rama"][:2]] = (h["rama"], h["nodo"])
    assert set(opciones) == {"R4", "R3", "R0"}
    ids_json = set()

    def recoge(n):
        ids_json.add(n["id"])
        for h in n.get("hijos", []):
            recoge(h["nodo"])
    recoge(raiz)
    assert len(ids_json) == 20
    # --- geometría en pulgadas
    wc, wt, gap = 1.95, 2.05, 0.75
    xA, xB = 0.10, 5.15
    # alto requerido por cada nodo
    def partes_azar(n):
        return [(f"{n['id']} · Azar · {n['supuesto']}", FS + 0.2, True), (n["etiqueta"], FS, False)]

    def partes_term(n):
        return [(f"{n['id']} · {n['etiqueta']} [{n['nivel_tdc']}]", FS, False), (f"Resultado: {n['resultado']}", FS, True)]
    filas = []
    for i in range(4):
        ha = alto_texto(fig, wc - 0.34, partes_azar(opciones["R4"][1][0][i]))[1] + 0.16
        hb = alto_texto(fig, wc - 0.34, partes_azar(opciones["R3"][1][0][i]))[1] + 0.16
        ta = alto_texto(fig, wt - 0.34, partes_term(opciones["R4"][1][1][i][1]))[1] + 0.16
        tb = alto_texto(fig, wt - 0.34, partes_term(opciones["R3"][1][1][i][1]))[1] + 0.16
        filas.append(max(ha, hb, ta, tb))
    fa = alto_texto(fig, wc - 0.34, partes_term(opciones["R4"][1][2][1]))[1] + 0.16
    fb = alto_texto(fig, wc - 0.34, partes_term(opciones["R3"][1][2][1]))[1] + 0.16
    filas.append(max(fa, fb))
    vgap = 0.27
    y_d1 = H - 0.38
    y_first = H - 1.05
    ytops = []
    y = y_first
    for h in filas:
        ytops.append(y)
        y -= h + vgap
    y_end = y + vgap
    print("  adec: filas", [round(f, 2) for f in filas], "fondo de ladders y =", round(y_end, 2))
    # --- D1
    plan = [("D1 · Decisión", FS + 0.4, True), (raiz["etiqueta"], FS, False)]
    wd = 2.5
    hd = alto_texto(fig, wd - 0.34, plan)[1] + 0.16
    nodo_arbol(fig, ax, 5.0 - wd / 2, y_d1 + hd / 2, wd, plan, CAJA, kind="decision", lw=1.8, h=hd)
    # --- ladders
    centros = {}
    for key, x0 in [("R4", xA), ("R3", xB)]:
        rama, (azar, fallas, (rama_ok, term_ok)) = opciones[key]
        xc, xt = x0, x0 + wc + gap
        for i in range(4):
            h = filas[i]
            nodo_arbol(fig, ax, xc, ytops[i], wc, partes_azar(azar[i]), CAJA, kind="azar", lw=1.3, h=h)
            nT = fallas[i][1]
            nodo_arbol(fig, ax, xt, ytops[i], wt, partes_term(nT), NIV[nT["nivel_tdc"]], kind="terminal", lw=1.2, h=h)
            # flecha de falla y rótulo de rama
            ym = ytops[i] - h / 2
            ruta(ax, [(xc + wc, ym), (xt, ym)], ms=12)
            etiqueta(ax, (xc + wc + xt) / 2, ym + 0.05, fallas[i][0].replace("SC-", "SC-"), fs=7.8, ha="center", va="bottom")
            centros[azar[i]["id"]] = (xc + wc / 2, ytops[i], h)
        # resultado final de la cadena (se cumple SC-4) en la columna de azar
        nodo_arbol(fig, ax, xc, ytops[4], wc, partes_term(term_ok), NIV[term_ok["nivel_tdc"]], kind="terminal", lw=1.2, h=filas[4])
        # flechas verticales "se cumple"
        okr = []
        for i in range(4):
            cur = azar[i]
            rama_i = [h["rama"] for h in cur["hijos"] if h["rama"].endswith("se cumple")][0]
            okr.append(rama_i)
            yb = ytops[i] - filas[i]
            ytn = ytops[i + 1]
            xa = xc + wc * 0.5
            ruta(ax, [(xa, yb), (xa, ytn)], ms=12)
            etiqueta(ax, xa + 0.07, (yb + ytn) / 2, rama_i, fs=7.8, ha="left")
        # rama desde D1
        xa = xc + wc * 0.5
        yline = y_d1
        if key == "R4":
            ruta(ax, [(5.0 - wd / 2, yline), (xa, yline), (xa, ytops[0])], ls=(0, (5, 3)), ms=12)
            txt = rama
            lin = envolver(fig, txt, 3.0, 8.4)
            ax.text(5.0 - wd / 2 - 0.1, yline + 0.06, "\n".join(lin), ha="right", va="bottom", fontsize=8.4, color=TINTA, linespacing=1.2)
        else:
            ruta(ax, [(5.0 + wd / 2, yline), (xa, yline), (xa, ytops[0])], ls=(0, (5, 3)), ms=12)
            lin = envolver(fig, rama, 3.0, 8.4)
            ax.text(5.0 + wd / 2 + 0.1, yline + 0.06, "\n".join(lin), ha="left", va="bottom", fontsize=8.4, color=TINTA, linespacing=1.2)
    # --- R0: línea por el centro hasta C0
    rama0, c0 = opciones["R0"]
    pl0 = [(f"{c0['id']} · {c0['etiqueta']} [{c0['nivel_tdc']}]", FS, False), (f"Resultado: {c0['resultado']}", FS, True)]
    wc0 = 3.9
    hc0 = alto_texto(fig, wc0 - 0.34, pl0)[1] + 0.16
    yc0 = y_end - 0.5
    ruta(ax, [(5.0, y_d1 - hd / 2), (5.0, yc0)], ls=(0, (5, 3)), ms=12)
    ax.text(5.1, y_end - 0.2, rama0, ha="left", va="center", fontsize=8.4, color=TINTA)
    nodo_arbol(fig, ax, 5.0 - wc0 / 2, yc0, wc0, pl0, NIV[c0["nivel_tdc"]], kind="terminal", lw=1.2, h=hc0)
    ybot = yc0 - hc0
    print("  adec: fondo de C0 y =", round(ybot, 2))
    # --- leyenda (a la izquierda de C0) y notas
    yl = yc0 - 0.02
    ax.text(0.12, yl, "Leyenda", fontsize=8.6, fontweight="bold", color=TINTA, va="center")
    leg = [("decision", "Decisión"), ("azar", "Azar o supuesto SC"), ("terminal", "Resultado")]
    yy = yl - 0.2
    for k, t in leg:
        icono(ax, k, 0.2, yy)
        etiqueta(ax, 0.34, yy, t, fs=8.2, ha="left")
        yy -= 0.19
    xl = 1.75
    yy = yl - 0.2
    for t, fc in [("PRODUCTO", GRIS), ("RESULTADO_INMEDIATO", CLARO), ("RESULTADO_INTERMEDIO", MEDIO), ("IMPACTO", AZUL)]:
        caja_u(ax, xl - 0.0, yy - 0.065, 0.2, 0.13, fc=fc, lw=1.0, rs=0.03)
        etiqueta(ax, xl + 0.28, yy, t, fs=7.6, ha="left")
        yy -= 0.17
        if t == "RESULTADO_INMEDIATO":
            pass
    # trazos
    ruta(ax, [(7.2, yl - 0.2), (7.65, yl - 0.2)], ms=10)
    etiqueta(ax, 7.72, yl - 0.2, "Rama de azar", fs=8.0, ha="left")
    ruta(ax, [(7.2, yl - 0.39), (7.65, yl - 0.39)], ms=10, ls=(0, (5, 3)))
    etiqueta(ax, 7.72, yl - 0.39, "Rama de decisión (no elegida)", fs=8.0, ha="left")
    ax.text(0.12, 0.30 if ybot > 0.5 else 0.12, "", fontsize=8)
    pregunta = f"Pregunta: {d['pregunta']}"
    ax.text(0.12, ybot - 0.12 if False else 0.22, pregunta, fontsize=8.2, color=TINTA, ha="left", va="center")
    ax.text(0.12, 0.04, "Sin probabilidades ni utilidades declaradas, el valor esperado es NO_CALCULABLE y no se marca ninguna rama "
            "elegida. SC-n: supuesto crítico de la teoría del cambio.", fontsize=8.2, color=TINTA, ha="left", va="center")
    E.guardar(fig, "cF4_adec")


# ----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pedidas = set(sys.argv[1:])
    hechas = []
    todo = {"cF4_dag": cf4_dag}
    for c in ["s0", "s1", "s2", "s3", "s4"]:
        todo[f"cF4_vester_{c}"] = (lambda c=c: cf4_vester(c))
    todo["cF4_micmac_s2"] = cf4_micmac_s2
    todo["cF4_adec"] = cf4_adec
    todo["cF4_atdc"] = cf4_atdc
    todo["cF4_aprob"] = cf4_aprob
    for nombre, fn in todo.items():
        if pedidas and nombre not in pedidas:
            continue
        r = fn()
        hechas.append(nombre)
        print(nombre, "->", r if r is not None else "ok")
    print("generadas:", ", ".join(hechas))
