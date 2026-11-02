# -*- coding: utf-8 -*-
"""Figuras del capítulo 3 (Objetivos): c3_f01 (árbol de objetivos) y c3_f02 (contribución a los ODS).
Datos: FICHA_MAESTRA §3 (objetivos), §8 (indicadores PERS), §10 (causas priorizadas) y ONU (2015) para los nombres de los ODS.
Ejecución: python3 c3_figs.py  (sin semilla: figuras de diagrama, sin componente aleatorio)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import estilo as E

def _h2(fig, ax, texto):
    """H2 como texto de figura (el título izquierdo de un eje sin marco se desplaza por las marcas del eje)."""
    ax.set_title("", loc="left")
    fig.text(0.008, 0.925, texto, fontsize=10, color=E.TINTA, ha="left", va="center")
from matplotlib.patches import FancyBboxPatch

# ------------------------------------------------------------------ F3.1 Árbol de objetivos
def f01():
    fig, ax = E.lienzo_libre(
        h1="Cada objetivo específico invierte una causa priorizada y responde a un supuesto crítico",
        h2=None,
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    _h2(fig, ax, "Árbol de objetivos derivado del árbol de problemas; causas según Vester (escenario S2); indicadores PERS")
    X = [15, 42, 69]; W = 26
    # etiquetas de nivel (columna izquierda)
    niveles = [("Fin", 64), ("Objetivo\ngeneral", 53), ("Objetivos\nespecíficos", 40.5), ("Causas\ninvertidas", 31.5), ("Medios y\nproductos", 15)]
    for t, y in niveles:
        ax.text(1, y, t, ha="left", va="center", fontsize=9.5, fontweight="bold", color=E.TINTA, linespacing=1.15)
    # Fin
    E.caja(ax, 15, 61, 80, 6, "Fin: protocolo activado ante superación de umbral y red operada por custodios\n después del cierre (PERS-S01 y PERS-S02)",
           relleno=E.GRIS, borde=E.AZUL, fs=9)
    # Objetivo general
    E.caja(ax, 15, 49, 80, 8, "Objetivo general: reducir el error de medición de PM2,5 y PM10 de una red de 100 nodos de bajo costo\n y asegurar su uso institucional en la gestión del riesgo, en Caldas, Cundinamarca\n y Valle del Cauca, durante 24 meses",
           relleno=E.MEDIO, borde=E.AZUL, fs=9, bold=True, grosor=2)
    # flechas fin <- OG
    E.flecha(ax, (55, 57.4), (55, 60.6))
    oes = [
        "OE1. Corregir la interferencia de\nhumedad y de fracción gruesa:\nR² ≥ 0,70 y NRMSE ≤ 30 %",
        "OE2. Mantener la disponibilidad de\nnodos y gateways: disponibilidad\nmensual ≥ 90 % y pérdida ≤ 10 %",
        "OE3. Lograr el uso del tablero y\ndel protocolo: ≥ 75 % de los comités\nfocalizados, en decisiones al mes 24",
    ]
    causas = ["Causas: V06, V02 y V03\nSupuesto crítico: SC-1", "Causas: V05 y V09\nSupuesto crítico: SC-2", "Causa: V15\nSupuestos críticos: SC-3 y SC-4"]
    medios = [
        ["Colocalización con tres referencias\ngravimétricas (PERS-R05)", "Modelo de corrección en gateway:\nhumedad, temperatura y fracción gruesa", "Seis ciclos de calibración,\ndos por tramo (PERS-R02)"],
        ["Autonomía mínima de 14 días\nsin sol en cada nodo", "Enlace celular con satelital alterno\ny almacenamiento local de 7 días", "Red de 100 nodos y 10 gateways\nen tres tramos (PERS-P01)"],
        ["Co-diseño de umbrales y protocolo\ncon los comités (PERS-E01)", "Formación de custodios: ≥ 60 personas\ncertificadas (PERS-E03)", "Convenios de custodia por tramo\n(PERS-S02)"],
    ]
    for i in range(3):
        cx = X[i] + W / 2
        E.caja(ax, X[i], 36, W, 9, oes[i], relleno=E.CLARO, borde=E.AZUL, fs=7.7, bold=False, grosor=1.5)
        E.flecha(ax, (cx, 45.4), (cx if i == 1 else (55 + (cx - 55) * 0.55), 48.6))
        E.caja(ax, X[i], 28.5, W, 5, causas[i], relleno=E.CAJA, borde=E.TINTA, fs=7.6, grosor=0.9, hatch="///" if False else None)
        E.flecha(ax, (cx, 33.7), (cx, 35.6))
        ys = [21, 13.5, 6]
        for j, t in enumerate(medios[i]):
            E.caja(ax, X[i], ys[j], W, 5.6, t, relleno=E.BLANCO, borde=E.MEDIO, fs=7.3, grosor=1.1)
        E.flecha(ax, (cx, 26.9), (cx, 28.0))
    # franja de compuertas
    E.caja(ax, 15, 0.3, 80, 3.4, "Compuertas: C1 (mes 12) y C2 (mes 17) liberan las compras del tramo siguiente; C3 (mes 24) cierra y transfiere",
           relleno=E.GRIS, borde=E.MEDIO, fs=8.3, grosor=0.9)
    E.guardar(fig, "c3_f01")

# ------------------------------------------------------------------ F3.2 Contribución a los ODS
ODS = [
    ("ODS 3. Salud y bienestar", "Meta general: reducir enfermedades y muertes\npor contaminación del aire. El proyecto\nno promete efectos en salud"),
    ("ODS 9. Industria, innovación e infraestructura", "Meta general: infraestructura fiable y resiliente;\ncapacidades científicas y tecnológicas"),
    ("ODS 11. Ciudades y comunidades sostenibles", "Meta general: menos personas afectadas por\ndesastres; atención a la calidad del aire"),
    ("ODS 13. Acción por el clima", "Meta general: resiliencia y capacidad institucional\nante riesgos y desastres"),
]
OEB = [("OE1", "Medición verificada de PM2,5 y PM10"), ("OE2", "Red disponible con energía\ny enlace redundantes"), ("OE3", "Uso institucional y custodia por tramos")]
# (objetivo, ods, tipo) tipo: D directa, I indirecta (PROPUESTO)
LINKS = [(1, 0, "D"), (2, 2, "D"), (0, 0, "I"), (0, 1, "I"), (0, 2, "I"), (1, 3, "I"), (2, 0, "I"), (2, 3, "I")]
# (objetivo, ods) con índices: OE1=0, OE2=1, OE3=2; ODS3=0, ODS9=1, ODS11=2, ODS13=3
LINKS = [(1, 1, "D"), (2, 2, "D"), (0, 0, "I"), (0, 1, "I"), (0, 2, "I"), (1, 3, "I"), (2, 0, "I"), (2, 3, "I")]

def f02():
    nd = sum(1 for l in LINKS if l[2] == "D"); ni = len(LINKS) - nd
    pal = {2: "Dos", 6: "seis"}
    fig, ax = E.lienzo_libre(
        h1="Dos contribuciones directas y seis indirectas vinculan los objetivos con cuatro ODS",
        h2=None,
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    _h2(fig, ax, "Diagrama de contribución a los Objetivos de Desarrollo Sostenible (Agenda 2030); tipo de contribución PROPUESTO")
    assert (nd, ni) == (2, 6)
    yo = [52, 35, 18]; yd = [57, 43, 29, 15]
    ax.text(3, 66, "Objetivos específicos", fontsize=10, fontweight="bold", color=E.TINTA, ha="left")
    ax.text(60, 66, "Objetivos de Desarrollo Sostenible", fontsize=10, fontweight="bold", color=E.TINTA, ha="left")
    for i, (c, t) in enumerate(OEB):
        E.caja(ax, 3, yo[i] - 5, 30, 10, f"{c}\n{t}", relleno=E.MEDIO, borde=E.AZUL, fs=9.2, bold=False, grosor=1.6)
    for j, (t, d) in enumerate(ODS):
        E.caja(ax, 60, yd[j] - 5.2, 38, 10.4, t + "\n" + d, relleno=E.CLARO, borde=E.AZUL, fs=8.2, grosor=1.2)
    for (o, d, tp) in LINKS:
        x0, y0 = 33.4, yo[o]; x1, y1 = 59.6, yd[d]
        if tp == "D":
            E.flecha(ax, (x0, y0), (x1, y1), color=E.AZUL, lw=3.0, ls="-")
        else:
            E.flecha(ax, (x0, y0), (x1, y1), color=E.TINTA, lw=1.2, ls=(0, (4, 3)))
    # leyenda
    ax.plot([3, 13], [5, 5], color=E.AZUL, lw=3.0); ax.text(14.5, 5, "Contribución directa (2)", va="center", fontsize=9, color=E.TINTA)
    ax.plot([42, 52], [5, 5], color=E.TINTA, lw=1.2, ls=(0, (4, 3))); ax.text(53.5, 5, "Contribución indirecta (6)", va="center", fontsize=9, color=E.TINTA)
    ax.text(3, 0.6, "Directa: el producto del objetivo es el medio principal de la meta. Indirecta: el producto es un insumo de otra acción.", fontsize=8, color=E.TINTA)
    E.guardar(fig, "c3_f02")

if __name__ == "__main__":
    f01(); f02()
    print("ok")
