# -*- coding: utf-8 -*-
"""Figuras del capítulo 4 (Marco teórico y conceptual): c4_f01 (mapa conceptual de integración teórica),
c4_f02 (red conceptual de las 15 variables, matriz S2 de Vester) y c4_f03 (línea de tiempo de antecedentes).
Datos: FICHA_MAESTRA §2, §3 y §10; MID_S_TRABAJO_PROPUESTO.csv (SECCION_4_4 del repositorio; escenario de trabajo S2, 48 aristas);
años de publicación según BANCO_REFERENCIAS.md. Sin componente aleatorio. Ejecución: python3 c4_figs.py"""
import os, sys, csv
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import estilo as E

def _h2(fig, ax, texto):
    """H2 como texto de figura (el título izquierdo de un eje sin marco se desplaza por las marcas del eje)."""
    ax.set_title("", loc="left")
    fig.text(0.008, 0.925, texto, fontsize=10, color=E.TINTA, ha="left", va="center")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

CSV = "/home/user/docs/genesis-e4-e3p00/SECCION_4_4/MID_S_TRABAJO_PROPUESTO.csv"
ADJ = dict(left=0.005, right=0.995, top=0.90, bottom=0.01)

# ------------------------------------------------------------------ F4.1 Mapa conceptual de integración teórica
def f01():
    fig, ax = E.lienzo_libre(
        h1="Siete teorías sostienen una cadena de la medición verificada a la continuidad",
        h2=None,
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(**ADJ)
    _h2(fig, ax, "Mapa conceptual de integración teórica; las flechas indican dependencia entre componentes del proyecto")
    W = 22; H = 9
    xs = [1.5, 26, 50.5, 75]
    # fila superior: teorías de la medición, el borde, el gemelo y el riesgo
    T = ["Metrología y calibración de\nsensores de bajo costo\n(Giordano; Barkjohn; EPA)",
         "Computación en el borde,\nTinyML y LoRaWAN\n(Shi; Warden; Adelantado)",
         "Gemelos digitales\n(Grieves y Vickers; Tao)",
         "Gestión del riesgo y\nalerta temprana\n(Ley 1523; Sendái)"]
    A = ["Medición verificada\n(V06, V02, V03)", "Corrección en gateway\ny enlace redundante (V09)",
         "Gemelo digital: estimación\nespacial (V10)", "Alerta con umbrales\nlocales (V11, V12)"]
    for i in range(4):
        E.caja(ax, xs[i], 58, W, H, T[i], relleno=E.MEDIO, borde=E.AZUL, fs=8.3, grosor=1.6)
        E.caja(ax, xs[i], 40, W, 8, A[i], relleno=E.CAJA, borde=E.TINTA, fs=8.3, grosor=1.0)
        E.flecha(ax, (xs[i] + W / 2, 57.6), (xs[i] + W / 2, 48.6))
        if i < 3: E.flecha(ax, (xs[i] + W + 0.3, 44), (xs[i + 1] - 0.3, 44))
    # fila media: uso, custodia y compuertas (de derecha a izquierda)
    B = ["Uso institucional del\ntablero (V15; PERS-E01)", "Custodia por componente\ny por tramo (PERS-S02)", "Compuertas C1 y C2: revisión\nde umbrales y de diseño"]
    xb = [75, 50.5, 26]
    for i in range(3):
        E.caja(ax, xb[i], 22, W, 8, B[i], relleno=E.CAJA, borde=E.TINTA, fs=8.3, grosor=1.0)
    E.flecha(ax, (xs[3] + W / 2, 39.6), (xb[0] + W / 2, 30.6))
    E.flecha(ax, (xb[0] - 0.3, 26), (xb[1] + W + 0.3, 26))
    E.flecha(ax, (xb[1] - 0.3, 26), (xb[2] + W + 0.3, 26))
    # retroalimentación: compuertas -> corrección (doble bucle)
    E.flecha(ax, (xb[2] + W * 0.35, 30.6), (xs[1] + W * 0.35, 39.6), ls="--", color=E.AZUL, lw=1.8)
    ax.text(xs[1] - 1.5, 34.2, "Revisión de\nvariables de gobierno", fontsize=7.8, ha="right", va="center", color=E.TINTA)
    # fila inferior: teorías de adopción, custodia y aprendizaje
    C = ["Difusión y adopción de\ninnovaciones (Rogers;\nDavis; Venkatesh)", "Gobernanza de bienes comunes\ny custodia (Ostrom; North)", "Aprendizaje de doble bucle\n(Argyris y Schön)"]
    for i in range(3):
        E.caja(ax, xb[i], 3, W, 9, C[i], relleno=E.MEDIO, borde=E.AZUL, fs=8.3, grosor=1.6)
        E.flecha(ax, (xb[i] + W / 2, 12.6), (xb[i] + W / 2, 21.6))
    ax.text(2, 20, "Cuadros azules: teorías.\nCuadros claros: componentes\ndel proyecto.\nLínea discontinua: aprendizaje\nde doble bucle.", fontsize=8, va="top", ha="left", color=E.TINTA, linespacing=1.3)
    E.guardar(fig, "c4_f01")

# ------------------------------------------------------------------ F4.2 Red conceptual (matriz S2)
NOMBRES = {"V01": "PM2,5", "V02": "PM10", "V03": "Humedad relativa", "V04": "Velocidad del viento", "V05": "Volumen de escombros",
           "V06": "Error de medición IoT", "V07": "Frecuencia de calibración", "V08": "Latencia de datos", "V09": "Disponibilidad de nodos",
           "V10": "Densidad del gemelo", "V11": "Índice AQHI", "V12": "Falsas alarmas", "V13": "Anticipación", "V14": "Personas alertadas",
           "V15": "Adopción institucional"}

def leer_s2():
    with open(CSV, encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    cols = rows[0][1:16]
    aristas = []
    for r in rows[1:16]:
        o = r[0]
        for d, v in zip(cols, r[1:16]):
            if int(v) > 0: aristas.append((o, d, int(v)))
    return aristas

def f02():
    ar = leer_s2()
    assert len(ar) == 48
    fuertes = [a for a in ar if a[2] >= 2]
    n3 = sum(1 for a in ar if a[2] == 3); n2 = sum(1 for a in ar if a[2] == 2)
    v06 = [a for a in fuertes if "V06" in a[:2]]
    assert (len(fuertes), n3, n2, len(v06)) == (23, 7, 16, 6)
    fig, ax = E.lienzo_libre(
        h1="V06 participa en seis de las 23 relaciones directas de valor 3 o 2",
        h2=None,
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(**ADJ)
    _h2(fig, ax, "Red conceptual de las 15 variables; relaciones directas de influencia estructural del escenario S2 (hipótesis ordinales)")
    # posiciones (rejilla 6 x 4) obtenidas por recocido simulado que minimiza cruces (semilla 20261013)
    SLOT = {"V01": (1, 1), "V02": (0, 1), "V03": (0, 3), "V04": (0, 0), "V05": (1, 0), "V06": (1, 2), "V07": (0, 2), "V08": (1, 3),
            "V09": (3, 0), "V10": (3, 1), "V11": (2, 1), "V12": (2, 2), "V13": (2, 3), "V14": (4, 3), "V15": (5, 2)}
    pos = {v: (9 + sx * 16.4, 61 - sy * 10.5) for v, (sx, sy) in SLOT.items()}
    bloque = {v: ("FIS" if v in ("V01", "V02", "V03", "V04", "V05") else "TEC" if v in ("V06", "V07", "V08", "V09", "V10") else "DEC") for v in SLOT}
    fill = {"FIS": E.CLARO, "TEC": E.MEDIO, "DEC": E.GRIS}
    r = 3.3
    dd = {(o, d): w for o, d, w in fuertes}
    rads = {("V15", "V14"): 0.35, ("V14", "V15"): 0.35}
    for (o, d), w in dd.items():
        a = FancyArrowPatch(pos[o], pos[d], arrowstyle="-|>", mutation_scale=11, color=E.TINTA if w == 3 else E.AZUL,
                            lw=2.4 if w == 3 else 1.4, ls="-" if w == 3 else (0, (4, 2.5)),
                            connectionstyle=f"arc3,rad={rads.get((o, d), 0.08)}", shrinkA=r * 7.2, shrinkB=r * 7.2, zorder=2)
        ax.add_patch(a)
    for v, (x, y) in pos.items():
        c = plt.Circle((x, y), r, fc=fill[bloque[v]], ec=E.TINTA if v == "V06" else E.AZUL, lw=2.6 if v == "V06" else 1.2, zorder=3)
        ax.add_patch(c)
        ax.text(x, y, v, ha="center", va="center", fontsize=9, fontweight="bold" if v == "V06" else "normal", color=E.TINTA, zorder=4)
    # clave de variables por bloque
    titulos = {"FIS": "Bloque físico y de actividad", "TEC": "Bloque técnico", "DEC": "Bloque de decisión"}
    xk = {"FIS": 3, "TEC": 36, "DEC": 69}
    ax.plot([2, 98], [26, 26], color=E.MEDIO, lw=1.0)
    for b in ("FIS", "TEC", "DEC"):
        ax.add_patch(plt.Circle((xk[b] + 1.2, 23), 1.2, fc=fill[b], ec=E.AZUL, lw=1.0))
        ax.text(xk[b] + 3.6, 23, titulos[b], fontsize=9, fontweight="bold", va="center", color=E.TINTA)
        ids = [v for v in sorted(NOMBRES) if bloque[v] == b]
        for i, v in enumerate(ids):
            ax.text(xk[b] + 1, 18.5 - i * 3.3, f"{v}  {NOMBRES[v]}", fontsize=8.6, va="center", color=E.TINTA,
                    fontweight="bold" if v == "V06" else "normal")
    ax.plot([2, 9], [1.6, 1.6], color=E.TINTA, lw=2.4); ax.text(10, 1.6, "Influencia fuerte (valor 3): siete relaciones", va="center", fontsize=8.5, color=E.TINTA)
    ax.plot([52, 59], [1.6, 1.6], color=E.AZUL, lw=1.4, ls=(0, (4, 2.5))); ax.text(60, 1.6, "Influencia moderada (valor 2): 16 relaciones", va="center", fontsize=8.5, color=E.TINTA)
    E.guardar(fig, "c4_f02")

# ------------------------------------------------------------------ F4.3 Línea de tiempo de antecedentes
def f03():
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.suptitle("Los cinco antecedentes de red se publican en 2025 y 2026, tras el marco metrológico",
                 fontsize=13.5, fontweight="bold", color=E.TINTA, x=0.01, ha="left", y=0.995)
    fig.text(0.008, 0.925, "Línea de tiempo de antecedentes por año de publicación o expedición, 2012 a 2026", fontsize=10, color=E.TINTA, ha="left", va="center")
    fig.subplots_adjust(left=0.115, right=0.985, top=0.90, bottom=0.07)
    ax.set_xlim(2011.3, 2027.7); ax.set_ylim(-1.2, 8.9)
    for s_ in ("left", "top", "right"): ax.spines[s_].set_visible(False)
    ax.set_yticks([])
    ax.set_xticks(range(2012, 2027)); ax.tick_params(axis="x", labelsize=9)
    ax.grid(axis="x", color=E.MEDIO, alpha=0.25, ls="--", lw=0.6)
    carriles = {7.0: "Marco normativo\ny de política", 4.0: "Literatura\nmetrológica", 1.0: "Redes, diseños\ny casos"}
    for y, t in carriles.items():
        ax.axhline(y, color=E.MEDIO, lw=1.4, zorder=1)
        ax.text(2011.2, y, t, ha="right", va="center", fontsize=9, fontweight="bold", color=E.TINTA)
    # (año, carril, texto, desplazamiento vertical, marcador); los años provienen de BANCO_REFERENCIAS.md
    ev = [
        (2012, 7.0, "Ley 1523:\nsistema de gestión\ndel riesgo", +0.55, "s"), (2015, 7.0, "Marco de Sendái", -0.55, "s"),
        (2017, 7.0, "Resolución 2254:\ncalidad del aire", +0.55, "s"), (2018, 7.0, "CONPES 3943", -0.55, "s"),
        (2020, 7.0, "Ley 2056:\nregalías", +0.55, "s"), (2021, 7.0, "OMS (guías) y\nCONPES 4069", -0.55, "s"), (2023, 7.0, "Ley 2294:\nPND 2022-2026", +0.55, "s"),
        (2015, 4.0, "Kumar et al.", +0.55, "o"), (2017, 4.0, "Castell et al.", -0.55, "o"), (2018, 4.0, "Crilley et al.;\nJayaratne et al.", +0.55, "o"),
        (2019, 4.0, "Karagulian\net al.", -0.55, "o"), (2020, 4.0, "Magi et al.;\nMalings et al.", +0.55, "o"), (2021, 4.0, "Barkjohn et al.;\nGiordano et al.; EPA", -0.55, "o"),
        (2022, 1.0, "Rodríguez-Villamizar\net al.", +0.55, "^"), (2025, 1.0, "Suresh et al.:\nmina de carbón", +0.55, "^"),
        (2026, 1.0, "SIATA; Bang et al.;\nTavella et al.;\nMurad Pedraza et al.", -0.55, "^"),
    ]
    for (a, y, t, dy, m) in ev:
        ax.plot([a], [y], marker=m, ms=10 if m != "^" else 11, mfc=E.AZUL if m == "^" else (E.MEDIO if m == "o" else E.CLARO), mec=E.TINTA, mew=1.1, zorder=3, ls="none")
        ax.annotate(t, xy=(a, y), xytext=(a, y + dy), ha="center", va="bottom" if dy > 0 else "top", fontsize=7.8, color=E.TINTA,
                    arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=0.6, shrinkA=0, shrinkB=4))
    ax.axvline(2026, color=E.TINTA, lw=1.0, ls=(0, (2, 3)), zorder=0)
    ax.text(2026.2, 8.8, "Proyecto\nSGR_CONV56", fontsize=8.5, va="top", ha="left", color=E.TINTA, fontweight="bold")
    # leyenda de marcadores (segundo canal)
    ax.plot([2012.3], [-0.8], marker="s", ms=8, mfc=E.CLARO, mec=E.TINTA, ls="none"); ax.text(2012.6, -0.8, "Norma o política", va="center", fontsize=8.5, color=E.TINTA)
    ax.plot([2015.6], [-0.8], marker="o", ms=8, mfc=E.MEDIO, mec=E.TINTA, ls="none"); ax.text(2015.9, -0.8, "Estudio metrológico", va="center", fontsize=8.5, color=E.TINTA)
    ax.plot([2019.0], [-0.8], marker="^", ms=9, mfc=E.AZUL, mec=E.TINTA, ls="none"); ax.text(2019.3, -0.8, "Red, diseño o caso", va="center", fontsize=8.5, color=E.TINTA)
    E.guardar(fig, "c4_f03")

if __name__ == "__main__":
    f01(); f02(); f03()
    print("ok")
