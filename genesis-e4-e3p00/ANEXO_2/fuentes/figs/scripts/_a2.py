# -*- coding: utf-8 -*-
"""Utilidades comunes de las figuras del Anexo 2 (módulo auxiliar de los scripts de A2/figs/scripts/).
Importa la plantilla A2/figs/estilo.py (E.OUT = A2/figs/out) y las cifras de A2/v2/m2.py.

Criterio de tamaño: las figuras se diseñan a 10 pulgadas de ancho y se publican a 16 cm de ancho (6,3 pulgadas). Todo tamaño de letra
se expresa en puntos a 16 cm y se multiplica por K (= 10 / 6,3) al dibujar, de modo que ningún texto baje de 8 pt en la página.
Las coordenadas de los diagramas son «unidades» isótropas: 100 unidades = ancho útil del lienzo."""
import os, sys, math
A2 = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2"
sys.path.insert(0, A2 + "/figs")
sys.path.insert(0, A2 + "/v2")
import estilo as E
E.OUT = A2 + "/figs/out"
os.makedirs(E.OUT, exist_ok=True)
import m2  # noqa: E402  (cifras únicas del Anexo 2)
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle  # noqa: E402

T, AZUL, MEDIO, CLARO, GRIS, CAJA, BLANCO, MARFIL = E.TINTA, E.AZUL, E.MEDIO, E.CLARO, E.GRIS, E.CAJA, E.BLANCO, E.MARFIL
W_IN = 10.0
K = W_IN / (16 / 2.54)          # factor de escala de 16 cm a 10 pulgadas (1,5875)
F_H1, F_H2, F_B, F_S = 10.5, 8.2, 8.2, 8.0   # puntos a 16 cm: título, subtítulo, cuerpo, mínimo
AX_W_IN = 9.9                    # ancho del eje en pulgadas (100 unidades)
UNIT = AX_W_IN / 100.0           # pulgadas por unidad
LH = 1.28                        # interlineado

def P(pt):
    """Puntos a 16 cm -> puntos en el lienzo de 10 pulgadas."""
    return pt * K

def num(v, dec=0):
    return E.num(v, dec)

# ------------------------------------------------------------------ medición y ajuste de texto
_M = {}
def _fig_med():
    if "fig" not in _M:
        _M["fig"] = plt.figure(figsize=(W_IN, 3))
        _M["r"] = _M["fig"].canvas.get_renderer()
        _M["c"] = {}
    return _M["fig"], _M["r"], _M["c"]

def medir(s, fs, bold=False, italic=False):
    """Ancho en pulgadas de una línea de texto con tamaño fs (puntos del lienzo)."""
    fig, r, c = _fig_med()
    k = (s, round(fs, 3), bold, italic)
    if k not in c:
        t = fig.text(0, 0, s, fontsize=fs, fontweight="bold" if bold else "normal", fontstyle="italic" if italic else "normal")
        c[k] = t.get_window_extent(r).width / fig.dpi
        t.remove()
    return c[k]

def _voraz(par, ancho, fs, bold, italic):
    out, linea = [], ""
    for w in par.split(" "):
        cand = (linea + " " + w).strip() if linea else w
        if (not linea) or medir(cand, fs, bold, italic) <= ancho:
            linea = cand
        else:
            out.append(linea); linea = w
    out.append(linea)
    return out

def envolver(s, ancho_in, fs, bold=False, italic=False, balance=True):
    """Parte s en líneas que caben en ancho_in (pulgadas); respeta los saltos \\n y equilibra la longitud de las líneas."""
    res = []
    for par in s.split("\n"):
        base = _voraz(par, ancho_in, fs, bold, italic)
        if balance and len(base) > 1:
            lo, hi = max(medir(w, fs, bold, italic) for w in par.split(" ")), ancho_in
            for _ in range(14):
                mid = (lo + hi) / 2
                if len(_voraz(par, mid, fs, bold, italic)) <= len(base):
                    hi = mid
                else:
                    lo = mid
            base = _voraz(par, hi + 1e-6, fs, bold, italic)
        res += base
    return res

# ------------------------------------------------------------------ lienzo con título H1 y subtítulo H2
def lienzo(h1, h2, H):
    """Figura de 10 pulgadas de ancho con H1 (negrita) y H2 (normal) a la izquierda y un eje libre de 100 x H unidades."""
    ancho_t = W_IN - 0.3
    l1 = envolver(h1, ancho_t, P(F_H1), bold=True, balance=True)
    l2 = envolver(h2, ancho_t, P(F_H2), balance=True)
    lh1, lh2 = P(F_H1) * 1.22 / 72, P(F_H2) * 1.25 / 72
    th = 0.06 + len(l1) * lh1 + 0.07 + len(l2) * lh2 + 0.12
    tot = th + H * UNIT + 0.04
    fig = plt.figure(figsize=(W_IN, tot))
    fig.patch.set_alpha(0)
    y1 = tot - 0.06
    fig.text(0.1 / W_IN, y1 / tot, "\n".join(l1), fontsize=P(F_H1), fontweight="bold", color=T, ha="left", va="top", linespacing=1.22)
    y2 = y1 - len(l1) * lh1 - 0.07
    fig.text(0.1 / W_IN, y2 / tot, "\n".join(l2), fontsize=P(F_H2), color=T, ha="left", va="top", linespacing=1.25)
    ax = fig.add_axes([(W_IN - AX_W_IN) / 2 / W_IN, 0.02 / tot, AX_W_IN / W_IN, H * UNIT / tot])
    ax.set_xlim(0, 100); ax.set_ylim(0, H); ax.axis("off"); ax.patch.set_alpha(0)
    return fig, ax

# ------------------------------------------------------------------ texto y cajas
def txt(ax, x, y, s, fs=F_B, bold=False, italic=False, ha="left", va="center", color=T, **kw):
    return ax.text(x, y, s, fontsize=P(fs), fontweight="bold" if bold else "normal", fontstyle="italic" if italic else "normal",
                   ha=ha, va=va, color=color, linespacing=LH, **kw)

def lineas(ax, x, y_top, s, fs=F_B, bold=False, italic=False, ha="left", ancho=None):
    """Dibuja s línea por línea desde y_top hacia abajo; devuelve la altura usada (unidades)."""
    ls = envolver(s, ancho * UNIT, P(fs), bold, italic) if ancho else s.split("\n")
    lh = P(fs) * LH / 72 / UNIT
    for i, l in enumerate(ls):
        txt(ax, x, y_top - (i + 0.5) * lh, l, fs, bold, italic, ha)
    return len(ls) * lh

def caja(ax, x, y, w, h, bloques, relleno=CAJA, borde=T, lw=1.5, ls="-", hatch=None, fs=F_B, ha="center", pad=1.1,
         valign="center", gap=0.0, zorder=2, radio=0.9, aviso=True):
    """Caja redondeada con texto ajustado al ancho. bloques: str o lista de (texto, estilo) con estilo 'n', 'b', 'i' o 'bi';
    un bloque puede llevar un tercer valor: tamaño de letra. Avisa si el texto no cabe."""
    if isinstance(bloques, str):
        bloques = [(bloques, "n")]
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={radio}", fc=relleno, ec=borde, lw=lw, ls=ls, hatch=hatch,
                       zorder=zorder)
    ax.add_patch(p)
    items = []
    for b in bloques:
        t, st = b[0], b[1]
        f = b[2] if len(b) > 2 else fs
        ls_ = envolver(t, (w - 2 * pad) * UNIT, P(f), "b" in st, "i" in st)
        lh = P(f) * LH / 72 / UNIT
        items += [(l, st, f, lh) for l in ls_]
    tot = sum(i[3] for i in items) + gap * (len(bloques) - 1)
    if aviso and tot > h - 0.8:
        print(f"  AVISO caja ({x:.0f},{y:.0f}) {w:.0f}x{h:.0f}: texto alto {tot:.1f} > {h - 0.8:.1f}: {items[0][0][:30]!r}")
    if valign == "center":
        yc = y + h / 2 + tot / 2
    else:
        yc = y + h - 0.6
    cur = yc
    # separación entre bloques
    idx = 0
    for b in bloques:
        t, st = b[0], b[1]
        f = b[2] if len(b) > 2 else fs
        ls_ = envolver(t, (w - 2 * pad) * UNIT, P(f), "b" in st, "i" in st)
        lh = P(f) * LH / 72 / UNIT
        for l in ls_:
            xx = x + w / 2 if ha == "center" else x + pad
            txt(ax, xx, cur - lh / 2, l, f, "b" in st, "i" in st, ha=ha, zorder=zorder + 1)
            cur -= lh
        cur -= gap
    return p

def flecha(ax, p0, p1, ls="-", lw=1.5, color=T, ms=14, estilo="-|>", rad=0.0, zorder=3):
    a = FancyArrowPatch(p0, p1, arrowstyle=estilo, mutation_scale=ms, color=color, lw=lw, ls=ls,
                        connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0, zorder=zorder)
    ax.add_patch(a)
    return a

def ruta(ax, pts, ls="-", lw=1.5, color=T, ms=14, zorder=3):
    """Poligonal con punta de flecha en el último tramo."""
    xs, ys = zip(*pts)
    ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, ls=ls, solid_capstyle="butt", zorder=zorder)
    flecha(ax, pts[-2], pts[-1], ls=ls, lw=lw, color=color, ms=ms, zorder=zorder)

def subeje(fig, ax, x0, y0, x1, y1):
    """Eje cartesiano (con ticks y cuadrícula) ubicado en las coordenadas de unidades del eje libre ax."""
    p = ax.get_position(); xl, yl = ax.get_xlim(), ax.get_ylim()
    fx = lambda x: p.x0 + (x - xl[0]) / (xl[1] - xl[0]) * p.width
    fy = lambda y: p.y0 + (y - yl[0]) / (yl[1] - yl[0]) * p.height
    a = fig.add_axes([fx(x0), fy(y0), fx(x1) - fx(x0), fy(y1) - fy(y0)])
    a.patch.set_alpha(0)
    for sp in ("top", "right"):
        a.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        a.spines[sp].set_color(T); a.spines[sp].set_linewidth(1.0)
    a.tick_params(colors=T, labelsize=P(F_B), width=0.9, length=3.5)
    a.set_axisbelow(True)
    return a

# ------------------------------------------------------------------ verificación de texto
def _bbox(t, r):
    return t.get_window_extent(r)

def chequear(fig, nombre, ejes=None, tol=1.0):
    """Cuenta solapes entre textos, textos fuera del lienzo, tamaños menores de 8 pt a 16 cm y colores distintos de TINTA."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    axs = ejes or fig.axes
    textos = [t for a in axs for t in a.texts if t.get_text().strip()]
    textos += [t for a in axs if a.axison for t in list(a.get_xticklabels()) + list(a.get_yticklabels()) if t.get_text().strip() and t.get_visible()]
    textos += [t for t in fig.texts if t.get_text().strip()]
    for a in axs:
        if a.get_legend() is not None:
            textos += [t for t in a.get_legend().get_texts()]
        for t in (a.xaxis.label, a.yaxis.label, a.title, a._left_title):
            if a.axison and t.get_text().strip():
                textos.append(t)
    malos = 0
    W, Hh = fig.canvas.get_width_height()
    bb = [(t, _bbox(t, r)) for t in textos]
    for t, b in bb:
        fs = t.get_fontsize() / K
        if fs < F_S - 0.05:
            print(f"  [{nombre}] letra de {fs:.1f} pt a 16 cm: {t.get_text()[:40]!r}"); malos += 1
        if t.get_color() not in (T, "#2A3439", "#2a3439"):
            print(f"  [{nombre}] color {t.get_color()} en {t.get_text()[:30]!r}"); malos += 1
        if b.x0 < -1 or b.y0 < -1 or b.x1 > W + 1 or b.y1 > Hh + 1:
            print(f"  [{nombre}] texto fuera del lienzo: {t.get_text()[:40]!r}"); malos += 1
    for i in range(len(bb)):
        for j in range(i + 1, len(bb)):
            a, b = bb[i][1], bb[j][1]
            if a.x0 + tol < b.x1 and b.x0 + tol < a.x1 and a.y0 + tol < b.y1 and b.y0 + tol < a.y1:
                print(f"  [{nombre}] solape: {bb[i][0].get_text()[:30]!r} / {bb[j][0].get_text()[:30]!r}"); malos += 1
    return malos

def guardar(fig, nombre):
    malos = chequear(fig, nombre)
    ruta_png = E.guardar(fig, nombre)
    print(f"{nombre}: {ruta_png} (avisos de texto: {malos})")
    return ruta_png
