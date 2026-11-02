# -*- coding: utf-8 -*-
"""Utilidades comunes de las figuras del Anexo 2 (secciones 13, 14, 16, 17, 18 y 19).
Importa la plantilla A2/figs/estilo.py (E.OUT = A2/figs/out) y las cifras de A2/v2/m2.py.

Regla de tamaño: el lienzo mide 10 pulgadas de ancho y se inserta a 16 cm (6,30 pulgadas), es decir a 0,63 de su
tamaño. Para que ninguna letra baje de 8 pt a 16 cm, toda letra mide al menos FS_MIN = 13 pt en el lienzo.
En los diagramas 1 unidad de datos = 0,1 pulgada (lienzo de 100 x 70 unidades para 10 x 7 pulgadas).
"""
import os, sys
A2 = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2"
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, A2 + "/figs")
sys.path.insert(0, A2 + "/v2")
import estilo as E
E.OUT = A2 + "/figs/out"
import m2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, FancyArrowPatch
from matplotlib.font_manager import FontProperties
from matplotlib.colors import to_hex
from matplotlib.text import Text

T, AZUL, MEDIO, CLARO, GRIS, CAJA, MARFIL, BLANCO = E.TINTA, E.AZUL, E.MEDIO, E.CLARO, E.GRIS, E.CAJA, E.MARFIL, E.BLANCO
PALETA = {c.lower() for c in E.COLORES_PERMITIDOS}

FS = 13.0            # cuerpo (8,2 pt a 16 cm)
FS_MIN = 13.0
FS_H1 = 15.5         # 9,8 pt a 16 cm
FS_H2 = 13.0
ANCHO_PAG_IN = 16 / 2.54
LH = 1.22            # interlineado


def num(v, dec=1):
    return E.num(v, dec)


def mm(v, d=1):
    """Millones de pesos con coma decimal y punto de miles."""
    return E.num(v / 1e6, d)


class Lienzo:
    """Lienzo de diagrama: 1 unidad = 0,1 pulgada; eje y hacia arriba; cabecera con H1 (hallazgo) y H2."""

    def __init__(self, w=10.0, h=7.0, h1=None, h2=None):
        self.w, self.h = w, h
        self.W, self.H = w * 10, h * 10
        self.fig = plt.figure(figsize=(w, h))
        self.fig.patch.set_alpha(0)
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, self.W)
        self.ax.set_ylim(0, self.H)
        self.ax.axis("off")
        self.ax.patch.set_alpha(0)
        self.rend = self.fig.canvas.get_renderer()
        self.avisos = []
        self.cache = {}
        self.top = self.H - 1.0
        if h1:
            self.cabecera(h1, h2)

    # ---------------------------------------------------------------- medidas
    def ancho(self, s, fs=FS, bold=False, italic=False):
        k = (s, fs, bold, italic)
        if k not in self.cache:
            fp = FontProperties(size=fs, weight="bold" if bold else "normal", style="italic" if italic else "normal",
                                family=["DejaVu Sans"])
            w, h, d = self.rend.get_text_width_height_descent(s, fp, False)
            self.cache[k] = w / self.rend.dpi * 10.0
        return self.cache[k]

    def alto_linea(self, fs=FS):
        return fs * LH / 72.0 * 10.0

    def envolver(self, s, w, fs=FS, bold=False, italic=False):
        """Ajuste voraz de líneas al ancho w (unidades); respeta los saltos \n."""
        out = []
        for sym in ("≥ ", "≤ ", "± "):
            s = s.replace(sym, sym[0] + "\u00a0")
        s = s.replace(" %", "\u00a0%")
        for par in s.split("\n"):
            palabras = par.split(" ")
            lin = ""
            for p in palabras:
                prueba = (lin + " " + p).strip() if lin else p
                if self.ancho(prueba, fs, bold, italic) <= w or not lin:
                    lin = prueba
                else:
                    out.append(lin)
                    lin = p
            out.append(lin)
        return out

    def envolver_bal(self, s, w, fs=FS, bold=False):
        """Como envolver, pero con líneas de largo parecido (evita viudas de una palabra)."""
        base = self.envolver(s, w, fs, bold)
        n = len(base)
        if n == 1:
            return base
        lo, hi = w * 0.4, w
        for _ in range(30):
            mid = (lo + hi) / 2
            if len(self.envolver(s, mid, fs, bold)) <= n:
                hi = mid
            else:
                lo = mid
        return self.envolver(s, hi, fs, bold)

    # ---------------------------------------------------------------- cabecera
    def cabecera(self, h1, h2):
        x0 = 1.0
        w = self.W - 2.0
        y = self.H - 1.2
        for ln in self.envolver_bal(h1, w, FS_H1, True):
            self.ax.text(x0, y, ln, ha="left", va="top", fontsize=FS_H1, fontweight="bold", color=T)
            y -= self.alto_linea(FS_H1)
        y -= 0.8
        if h2:
            for ln in self.envolver_bal(h2, w, FS_H2):
                self.ax.text(x0, y, ln, ha="left", va="top", fontsize=FS_H2, color=T)
                y -= self.alto_linea(FS_H2)
        self.top = y - 1.0
        return self.top

    # ---------------------------------------------------------------- texto
    def t(self, x, y, s, fs=FS, bold=False, italic=False, ha="left", va="center", w=None, zorder=5, color=T):
        """Texto libre; si se da w (unidades) se envuelve. Devuelve el alto usado en unidades."""
        lines = self.envolver(s, w, fs, bold, italic) if w else s.split("\n")
        lh = self.alto_linea(fs)
        n = len(lines)
        tot = n * lh
        if va == "center":
            ytop = y + tot / 2
        elif va == "top":
            ytop = y
        else:
            ytop = y + tot
        for i, ln in enumerate(lines):
            self.ax.text(x, ytop - lh * (i + 0.5), ln, ha=ha, va="center", fontsize=fs, color=color,
                         fontweight="bold" if bold else "normal", fontstyle="italic" if italic else "normal", zorder=zorder)
        return tot

    # ---------------------------------------------------------------- cajas
    def caja(self, x, y, w, h, cuerpo="", titulo=None, fc=CAJA, ec=T, fs=FS, fs_t=None, lw=1.2, ls="-", trama=None,
             ha="center", va="center", pad=1.0, radio=1.0, marco=1.1, zorder=2, ec_trama=AZUL, bold_cuerpo=False):
        """Caja redondeada (sin relleno extra) con titulo en negrita y cuerpo; si no cabe, registra un aviso.
        trama: marco con trama (segundo canal) alrededor de un panel interior liso donde va el texto."""
        fs_t = fs_t or fs
        st = "round,pad=0,rounding_size=%s" % radio
        if trama:
            self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=st, fc=fc, ec=ec_trama, lw=0, hatch=trama, zorder=zorder))
            self.ax.add_patch(FancyBboxPatch((x + marco, y + marco), w - 2 * marco, h - 2 * marco, boxstyle="round,pad=0,rounding_size=0.5",
                                             fc=fc, ec="none", lw=0, zorder=zorder + 0.1))
            self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=st, fc="none", ec=ec, lw=lw, ls=ls, zorder=zorder + 0.2))
            pad = pad + marco
        else:
            self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=st, fc=fc, ec=ec, lw=lw, ls=ls, zorder=zorder))
        iw = w - 2 * pad
        lineas = []          # (texto, fs, negrita, hueco_previo)
        if titulo:
            for ln in self.envolver(titulo, iw, fs_t, True):
                lineas.append((ln, fs_t, True, 0.0))
        if cuerpo:
            for k, ln in enumerate(self.envolver(cuerpo, iw, fs, bold_cuerpo)):
                lineas.append((ln, fs, bold_cuerpo, 0.25 * self.alto_linea(fs) if (k == 0 and titulo) else 0.0))
        tot = sum(self.alto_linea(f) + g for _, f, _, g in lineas)
        disp = h - 2 * pad + 0.4
        nom = (titulo or cuerpo)[:40]
        if tot > disp + 1e-6:
            self.avisos.append("DESBORDE caja '%s': necesita %.1f y hay %.1f" % (nom, tot, disp))
        for ln, f, b, g in lineas:
            if self.ancho(ln, f, b) > iw + 1e-6:
                self.avisos.append("ANCHO caja '%s': línea '%s' %.1f > %.1f" % (nom, ln[:30], self.ancho(ln, f, b), iw))
        if va == "center":
            ycur = y + h / 2 + tot / 2
        elif va == "top":
            ycur = y + h - pad
        else:
            ycur = y + pad + tot
        tx = x + w / 2 if ha == "center" else x + pad
        for ln, f, b, g in lineas:
            lh = self.alto_linea(f)
            ycur -= g
            self.ax.text(tx, ycur - lh / 2, ln, ha=ha, va="center", fontsize=f, color=T, fontweight="bold" if b else "normal",
                         zorder=zorder + 1)
            ycur -= lh
        return (x, y, w, h)

    def necesita(self, w, cuerpo="", titulo=None, fs=FS, fs_t=None, pad=1.0, bold_cuerpo=False, trama=False, marco=1.1):
        """Alto mínimo (unidades) de una caja de ancho w para su texto."""
        fs_t = fs_t or fs
        if trama:
            pad = pad + marco
        iw = w - 2 * pad
        tot = 0.0
        if titulo:
            tot += len(self.envolver(titulo, iw, fs_t, True)) * self.alto_linea(fs_t)
        if cuerpo:
            tot += len(self.envolver(cuerpo, iw, fs, bold_cuerpo)) * self.alto_linea(fs)
            if titulo:
                tot += 0.25 * self.alto_linea(fs)
        return tot + 2 * pad - 0.4

    def rombo(self, cx, cy, w, h, texto, fc=BLANCO, fs=FS, bold=True, lw=1.4):
        self.ax.add_patch(Polygon([(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)], closed=True, fc=fc, ec=T,
                                  lw=lw, zorder=3))
        if texto:
            self.ax.text(cx, cy, texto, ha="center", va="center", fontsize=fs, color=T, fontweight="bold" if bold else "normal", zorder=4)
            if self.ancho(texto, fs, bold) > w * 0.62:
                self.avisos.append("ROMBO '%s' ancho %.1f > %.1f" % (texto, self.ancho(texto, fs, bold), w * 0.62))

    # ---------------------------------------------------------------- flechas
    def flecha(self, p0, p1, ls="-", lw=1.5, rad=0.0, estilo="-|>", zorder=3, ms=14):
        a = FancyArrowPatch(p0, p1, arrowstyle=estilo, mutation_scale=ms, color=T, lw=lw, ls=ls,
                            connectionstyle="arc3,rad=%s" % rad, zorder=zorder, shrinkA=0, shrinkB=0)
        self.ax.add_patch(a)
        return a

    def camino(self, pts, ls="-", lw=1.5, flecha=True, ms=14, zorder=3):
        """Polilínea ortogonal; el último tramo lleva punta de flecha."""
        for a, b in zip(pts[:-2], pts[1:-1]):
            self.ax.plot([a[0], b[0]], [a[1], b[1]], color=T, lw=lw, ls=ls, solid_capstyle="butt", zorder=zorder)
        if flecha:
            self.flecha(pts[-2], pts[-1], ls=ls, lw=lw, ms=ms, zorder=zorder)
        else:
            self.ax.plot([pts[-2][0], pts[-1][0]], [pts[-2][1], pts[-1][1]], color=T, lw=lw, ls=ls, zorder=zorder)

    # ---------------------------------------------------------------- cierre
    def revisar(self, nombre, ejes_extra=()):
        """Verifica fuentes, paleta y posición de los textos; devuelve la lista de avisos."""
        fig = self.fig
        fig.canvas.draw()
        rend = fig.canvas.get_renderer()
        avisos = list(self.avisos)
        textos = [t for t in fig.findobj(Text) if t.get_text().strip() and t.get_visible()]
        W, H = fig.get_size_inches() * fig.dpi
        cajas = []
        for t in textos:
            if t.get_fontsize() < FS_MIN - 1e-6:
                avisos.append("FUENTE %.1f < %.1f: '%s'" % (t.get_fontsize(), FS_MIN, t.get_text()[:30]))
            if to_hex(t.get_color()).lower() != T.lower():
                avisos.append("COLOR de texto %s: '%s'" % (to_hex(t.get_color()), t.get_text()[:30]))
            bb = t.get_window_extent(rend)
            if bb.x0 < -1 or bb.y0 < -1 or bb.x1 > W + 1 or bb.y1 > H + 1:
                avisos.append("FUERA del lienzo: '%s'" % t.get_text()[:40])
            cajas.append((t, bb))
        for i in range(len(cajas)):
            for j in range(i + 1, len(cajas)):
                a, b = cajas[i][1], cajas[j][1]
                ix = min(a.x1, b.x1) - max(a.x0, b.x0)
                iy = min(a.y1, b.y1) - max(a.y0, b.y0)
                if ix > 2 and iy > 3:
                    avisos.append("SOLAPE: '%s' con '%s'" % (cajas[i][0].get_text()[:30], cajas[j][0].get_text()[:30]))
        # paleta de los elementos gráficos
        for o in fig.findobj():
            for attr in ("get_facecolor", "get_edgecolor"):
                if hasattr(o, attr) and not isinstance(o, (Text,)):
                    try:
                        c = getattr(o, attr)()
                    except Exception:
                        continue
                    cs = np.atleast_2d(c) if not isinstance(c, str) else [c]
                    for ci in cs:
                        if isinstance(ci, str) and ci == "none":
                            continue
                        try:
                            rgba = tuple(ci)
                        except TypeError:
                            continue
                        if len(rgba) == 4 and rgba[3] == 0:
                            continue
                        if to_hex(rgba[:3]).lower() not in PALETA and to_hex(rgba[:3]).lower() != "#000000":
                            avisos.append("COLOR fuera de paleta %s en %s" % (to_hex(rgba[:3]), type(o).__name__))
        from matplotlib.lines import Line2D
        for o in fig.findobj(Line2D):
            if not o.get_visible():
                continue
            for c in (o.get_color(), o.get_markerfacecolor(), o.get_markeredgecolor()):
                if isinstance(c, str) and c in ("none", "None", "auto"):
                    continue
                try:
                    h = to_hex(c).lower()
                except Exception:
                    continue
                if h not in PALETA:
                    avisos.append("COLOR de línea fuera de paleta %s" % h)
        return avisos

    def guardar(self, nombre):
        av = self.revisar(nombre)
        ruta = E.guardar(self.fig, nombre, tight=False)
        print("== %s -> %s" % (nombre, ruta))
        for a in av:
            print("   AVISO:", a)
        if not av:
            print("   sin avisos")
        return ruta, av


def eje_en_unidades(L, x0, y0, x1, y1):
    """Crea un eje de matplotlib dentro del lienzo L con esquinas dadas en unidades (0,1 pulgada)."""
    ax = L.fig.add_axes([x0 / L.W, y0 / L.H, (x1 - x0) / L.W, (y1 - y0) / L.H])
    ax.patch.set_alpha(0)
    return ax


def estilo_eje(ax, fs=FS):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(T)
        ax.spines[s].set_linewidth(1.0)
    ax.tick_params(colors=T, labelsize=fs, length=4, width=1.0)
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_color(T)


def verificar_png(nombre):
    """Verificación independiente del PNG: dimensiones, esquinas transparentes y paleta de los píxeles opacos."""
    from PIL import Image
    ruta = os.path.join(E.OUT, nombre + ".png")
    im = Image.open(ruta)
    assert im.mode == "RGBA", im.mode
    a = np.asarray(im)
    alfa = a[..., 3]
    esq = [alfa[0, 0], alfa[0, -1], alfa[-1, 0], alfa[-1, -1]]
    transp = float((alfa == 0).mean())
    op = a[alfa == 255][:, :3].astype(int)
    pal = np.array([[int(c[i:i + 2], 16) for i in (1, 3, 5)] for c in sorted(PALETA)])
    # distancia al color más cercano de la paleta
    if len(op):
        idx = np.random.default_rng(0).choice(len(op), size=min(len(op), 200000), replace=False)
        d = np.sqrt(((op[idx][:, None, :] - pal[None, :, :]) ** 2).sum(-1)).min(1)
        exacto = float((d <= 2).mean())
        lejos = float((d > 40).mean())
    else:
        exacto = lejos = float("nan")
    ancho_cm_en_pagina = 16.0
    return dict(archivo=nombre + ".png", px=im.size, pulgadas=(round(im.size[0] / 220, 2), round(im.size[1] / 220, 2)),
                alto_a_16cm=round(16.0 * im.size[1] / im.size[0], 1), esquinas_alfa=esq, transparente=round(transp, 3),
                opacos_en_paleta=round(exacto, 4), opacos_lejos_de_paleta=round(lejos, 5))
