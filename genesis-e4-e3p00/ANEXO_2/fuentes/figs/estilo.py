# -*- coding: utf-8 -*-
"""Plantilla visual única del proyecto (instrucción del usuario del 13-oct-2026 + SISTEMA_FIGURAS del metaprompt).
Uso:  import sys; sys.path.insert(0, '<ruta>/figs'); import estilo as E
      fig, ax = E.lienzo(h1='Hallazgo clave', h2='Variable, periodo y unidades')
      ... dibujar con E.AZUL, E.MEDIO, E.CLARO, E.TINTA ...
      E.guardar(fig, 'f2_1')            # exporta figs/out/f2_1.png y .svg con fondo transparente
Reglas: fondo transparente; todo texto en TINTA (#2A3439); sin borde superior ni derecho; cuadrícula horizontal fina
(alpha 0,25, instrucción del usuario); etiquetas directas; máximo cuatro colores de datos; segundo canal (trama, marcador o
etiqueta) para no depender solo del color."""
import os, matplotlib
matplotlib.use("Agg")
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

TINTA = "#2A3439"; AZUL = "#6699CC"; MEDIO = "#9EB9D4"; CLARO = "#B9D9EB"
GRIS = "#F5F5F5"; CAJA = "#F7F7F7"; MARFIL = "#FEFEFA"; BLANCO = "#FFFFFF"
SERIES = [AZUL, MEDIO, CLARO, GRIS]
HATCH = ["", "///", "...", "xx"]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

def aplicar():
    mpl.rcParams.update({
        "figure.figsize": (10, 7), "figure.facecolor": "none", "axes.facecolor": "none",
        "savefig.facecolor": "none", "savefig.transparent": True, "savefig.dpi": 220,
        "font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans", "Liberation Sans", "Arial"],
        "font.size": 11, "text.color": TINTA, "axes.labelcolor": TINTA, "xtick.color": TINTA, "ytick.color": TINTA,
        "axes.edgecolor": TINTA, "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
        "grid.color": MEDIO, "grid.alpha": 0.25, "grid.linestyle": "--", "grid.linewidth": 0.6,
        "svg.fonttype": "none", "axes.titleweight": "bold", "legend.frameon": False,
    })
aplicar()

def _h2(fig, ax, texto, pad):
    """Subtítulo H2 alineado a la izquierda de la figura (mismo borde que H1), en peso normal."""
    pos = ax.get_position()
    ax.set_title(texto, fontsize=10, color=TINTA, loc="left", pad=pad, fontweight="normal", x=(0.01 - pos.x0) / pos.width)

def lienzo(h1=None, h2=None, figsize=(10, 7), grid=True, ejes=True):
    """Crea figura con jerarquía tipográfica: H1 (hallazgo) en negrita a la izquierda; H2 (variable/periodo/unidades)."""
    fig, ax = plt.subplots(figsize=figsize)
    if h1: fig.suptitle(h1, fontsize=14, fontweight="bold", color=TINTA, x=0.01, ha="left", y=0.995)
    if h2: _h2(fig, ax, h2, 12)
    if grid: ax.grid(axis="y")
    ax.set_axisbelow(True)
    if not ejes:
        ax.axis("off")
    return fig, ax

def lienzo_libre(h1=None, h2=None, figsize=(10, 7), xlim=(0, 100), ylim=(0, 70)):
    """Lienzo sin ejes para diagramas (cajas y flechas) en coordenadas arbitrarias; el eje y crece hacia arriba."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.axis("off")
    if h1: fig.suptitle(h1, fontsize=14, fontweight="bold", color=TINTA, x=0.01, ha="left", y=0.995)
    if h2: _h2(fig, ax, h2, 8)
    return fig, ax

def caja(ax, x, y, w, h, texto, relleno=CAJA, borde=TINTA, fs=9.5, bold=False, grosor=1.2, hatch=None, ha="center"):
    """Caja redondeada con texto centrado (texto siempre en TINTA)."""
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=borde, lw=grosor,
                       hatch=hatch)
    ax.add_patch(p)
    tx = x + w / 2 if ha == "center" else x + 0.8
    ax.text(tx, y + h / 2, texto, ha=ha, va="center", fontsize=fs, color=TINTA, fontweight="bold" if bold else "normal",
            wrap=True, linespacing=1.25)
    return p

def flecha(ax, p0, p1, color=TINTA, estilo="-|>", lw=1.3, ls="-", rad=0.0, texto=None, fs=8.5):
    a = FancyArrowPatch(p0, p1, arrowstyle=estilo, mutation_scale=12, color=color, lw=lw, ls=ls,
                        connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)
    if texto:
        ax.text((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + 0.8, texto, ha="center", va="bottom", fontsize=fs, color=TINTA)
    return a

def etiquetar_barras(ax, barras, fmt="{:,.0f}", dy=3, fs=9.5, horizontal=False, dec=","):
    """Etiqueta directa sobre cada barra (valor exacto)."""
    for b in barras:
        v = b.get_width() if horizontal else b.get_height()
        txt = fmt.format(v)
        if dec == ",":
            txt = txt.replace(",", "X").replace(".", ",").replace("X", ".")
        if horizontal:
            ax.annotate(txt, xy=(v, b.get_y() + b.get_height() / 2), xytext=(dy, 0), textcoords="offset points",
                        ha="left", va="center", fontsize=fs, fontweight="bold", color=TINTA)
        else:
            ax.annotate(txt, xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, dy), textcoords="offset points",
                        ha="center", va="bottom", fontsize=fs, fontweight="bold", color=TINTA)

def guardar(fig, nombre, tight=True):
    """Exporta SVG y PNG con fondo transparente en figs/out/."""
    for ext in ("svg", "png"):
        fig.savefig(os.path.join(OUT, f"{nombre}.{ext}"), format=ext, transparent=True,
                    bbox_inches="tight" if tight else None, dpi=220)
    plt.close(fig)
    return os.path.join(OUT, f"{nombre}.png")

def num(v, dec=1):
    """Formato colombiano: miles con punto y decimales con coma."""
    s = f"{v:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

COLORES_PERMITIDOS = {TINTA, AZUL, MEDIO, CLARO, GRIS, CAJA, MARFIL, BLANCO}
