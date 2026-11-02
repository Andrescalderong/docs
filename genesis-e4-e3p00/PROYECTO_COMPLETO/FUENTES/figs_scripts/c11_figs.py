# -*- coding: utf-8 -*-
"""Figuras del capítulo 11 (prefijo 11): c11_f01 (roadmap de productos) y c11_f02 (vinculación de estudiantes).
Datos: ficha maestra §8 e indicadores.py (PERS-P01 a P04, PERS-E03) y líneas P01, P02 del presupuesto. Sin semilla ni corpus."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import estilo as E
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def caja_trama(ax, x, y, w, h, texto, relleno, fs=9, trama="///", color_trama=None):
    """Caja con trama de segundo canal y texto legible sobre fondo sólido."""
    from matplotlib.patches import FancyBboxPatch
    ct = color_trama or E.AZUL
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=ct, lw=0, hatch=trama))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc="none", ec=E.TINTA, lw=1.2))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, linespacing=1.25,
            bbox=dict(boxstyle="round,pad=0.35", fc=relleno, ec="none"))

# ------------------------------------------------------------------ f01: roadmap
def f01():
    fig, ax = E.lienzo(h1="Los cinco productos cierran sus metas finales entre los meses 19 y 24",
                       h2="Hitos por tipología MMG, meses 1 a 24; compuertas C1 (mes 12), C2 (mes 17) y C3 (mes 24)",
                       figsize=(10, 4.5), grid=False)
    filas = [
        ("PROT-FUNC\nRed de nodos y gateways", [(12, "30 nodos y 3 gateways"), (17, "70 y 7"), (19, "100 y 10")], (24, "100 nodos y 10 gateways\nen operación")),
        ("SW-REG\nSoftware registrado", [(17, "1 solicitud radicada")], (24, "1 registro vigente")),
        ("ART-A1 / ART-A2\nArtículos Q1 o Q2", [(17, "1 sometido")], (24, "2 sometidos y\n1 aceptado como mínimo")),
        ("ASC-PART / COM / CIRC\nActividades de apropiación", [(12, "10 actividades")], (24, "29 actividades")),
        ("FORM\nPersonas certificadas", [(12, "20 personas"), (17, "40")], (24, "60 personas")),
    ]
    n = len(filas)
    ax.set_xlim(0, 35)
    ax.set_ylim(-1.15, n - 0.2)
    ax.invert_yaxis()
    for i, (nom, inter, fin) in enumerate(filas):
        ax.barh(i, 24, left=0.5, height=0.16, color=E.CLARO, edgecolor=E.TINTA, linewidth=0.6, zorder=2)
        for j, (m, t) in enumerate(inter):
            ax.plot(m, i, marker="o", ms=9, mfc=E.MEDIO, mec=E.TINTA, mew=1.0, zorder=4)
            arriba = (m != 17) if len(inter) > 1 else (i != 1 and i != 2)
            dy = -0.2 if arriba else 0.34
            va = "bottom" if arriba else "top"
            if m in (12, 17):
                ax.text(m - 0.3, i + dy, t, ha="right", va=va, fontsize=8.5, color=E.TINTA)
            else:
                ax.text(m, i + dy, t, ha="center", va=va, fontsize=8.5, color=E.TINTA)
        m, t = fin
        ax.plot(m, i, marker="s", ms=10, mfc=E.AZUL, mec=E.TINTA, mew=1.0, zorder=4)
        ax.text(m + 0.7, i, t, ha="left", va="center", fontsize=8.5, color=E.TINTA, fontweight="bold")
    ax.set_yticks(range(n))
    ax.set_yticklabels([f[0] for f in filas], fontsize=9)
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([1, 6, 12, 17, 19, 24])
    ax.set_xlabel("Mes de ejecución", fontsize=9.5)
    for mes, tag in ((12, "C1"), (17, "C2"), (24, "C3")):
        ax.axvline(mes, color=E.TINTA, linewidth=0.8, linestyle=(0, (4, 3)), zorder=1)
        ax.text(mes, -0.98, tag, ha="center", va="top", fontsize=9, fontweight="bold", color=E.TINTA)
    ax.spines["left"].set_visible(False)
    handles = [Line2D([0], [0], marker="o", ls="", mfc=E.MEDIO, mec=E.TINTA, ms=8, label="Hito intermedio"),
               Line2D([0], [0], marker="s", ls="", mfc=E.AZUL, mec=E.TINTA, ms=8, label="Meta final al mes 24")]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.0, -0.30), ncol=2, fontsize=8.5, frameon=False)
    E.guardar(fig, "c11_f01")

# ------------------------------------------------------------------ f02: vinculación de estudiantes
def f02():
    fig, ax = E.lienzo_libre(h1="Seis plazas cubren el tramo 1 y dos plazas de maestría cubren los tres tramos",
                             h2="Vinculación de estudiantes al paquete WP1, meses 1 a 24 (personas y persona-mes)",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    # columnas
    E.caja(ax, 3, 46, 27, 12, "Plazas de joven investigador\n6 personas, meses 1 a 12\n72 persona-mes (línea P01)", relleno=E.CLARO, fs=9)
    caja_trama(ax, 3, 26, 27, 12, "Estudiantes de maestría\n2 personas, meses 1 a 24\n48 persona-mes (línea P02)", E.CLARO, fs=9)
    E.caja(ax, 39, 33, 24, 18, "Paquete de trabajo WP1\nMedición verificada (OE1)\nColocalización, calibración\ny validación del modelo", relleno=E.MEDIO, fs=9, bold=False)
    E.caja(ax, 71, 51, 27, 9, "Protocolo de colocalización\ndocumentado (mes 12)", relleno=E.CAJA, fs=9)
    caja_trama(ax, 71, 36, 27, 9, "2 tesis de maestría\n(defensa al mes 24)", E.CAJA, fs=9)
    E.caja(ax, 71, 21, 27, 9, "Coautoría en 2 artículos\n(PERS-P03)", relleno=E.CAJA, fs=9)
    # flechas
    E.flecha(ax, (33.5, 52), (38.5, 44))
    E.flecha(ax, (33.5, 32), (38.5, 38))
    E.flecha(ax, (64, 46), (70.5, 55.5))
    E.flecha(ax, (64, 42), (70.5, 40.5))
    E.flecha(ax, (64, 38), (70.5, 25.5))
    # supervisión (PROPUESTO)
    E.caja(ax, 39, 14, 24, 11, "Supervisión académica\nCiencia de datos (P03) y\nmetrología (P07)", relleno=E.GRIS, fs=8.5, borde=E.TINTA, grosor=1.0)
    E.flecha(ax, (51, 25.5), (51, 32.5), ls="--")
    ax.text(52.5, 28.5, "PROPUESTO", fontsize=8, ha="left", va="center", color=E.TINTA)
    # población distinta: custodia
    E.caja(ax, 3, 3, 27, 9, "Personal contratado de WP3\n(líneas S09 y P14)", relleno=E.GRIS, fs=8.5, grosor=1.0)
    caja_trama(ax, 71, 3, 27, 9, "Al menos 60 personas\ncertificadas (PERS-E03)", E.CLARO, fs=9, trama="...")
    E.flecha(ax, (33.5, 7.5), (70.5, 7.5), ls="--")
    ax.text(52, 8.6, "Población distinta:\nno se suma a las ocho personas", fontsize=8.5, ha="center", va="bottom", color=E.TINTA)
    # nota de duración
    ax.text(3, 62.2, "Termina en el mes 12", fontsize=8.5, ha="left", va="bottom", color=E.TINTA)
    ax.text(3, 40.2, "Cubre los tramos 1, 2 y 3", fontsize=8.5, ha="left", va="bottom", color=E.TINTA)
    E.guardar(fig, "c11_f02")

if __name__ == "__main__":
    f01(); f02()
    print("ok")
