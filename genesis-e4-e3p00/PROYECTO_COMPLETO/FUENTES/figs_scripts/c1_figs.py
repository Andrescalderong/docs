# -*- coding: utf-8 -*-
"""Figuras del capítulo 1 (prefijo 1): F1.1 localización esquemática, F1.2 árbol A-PROB, F1.3 modelo relacional.
Datos: FICHA_MAESTRA §4 (tramos, distribución por departamento), SECCION_4_5/ARBOL_5_SGR_CONV56_AIRE.json (nodos y enlaces),
FICHA_MAESTRA §10c (variables del problema formal). No se inventa ningún valor.
Ejecución: python3 c1_figs.py   (genera figs/out/c1_f01, c1_f02 y c1_f03 en .png y .svg)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import estilo as E
from matplotlib.patches import Rectangle

TINTA, AZUL, MEDIO, CLARO, GRIS = E.TINTA, E.AZUL, E.MEDIO, E.CLARO, E.GRIS
ARBOL = "/home/user/docs/genesis-e4-e3p00/SECCION_4_5/ARBOL_5_SGR_CONV56_AIRE.json"


def caja_texto(ax, cx, cy, w, h, lineas, relleno, bold=False, grosor=1.2, fs=9, dashed=False):
    p = E.caja(ax, cx - w / 2, cy - h / 2, w, h, "\n".join(lineas), relleno=relleno, fs=fs, bold=bold, grosor=grosor)
    if dashed:
        p.set_linestyle((0, (4, 2)))
    return p


def f01():
    fig, ax = E.lienzo_libre(
        h1="Tres departamentos concentran 100 nodos que se despliegan en tres tramos condicionados",
        h2="Esquema de localización, no mapa a escala. Nodos operativos por departamento (PROPUESTO)\ny por tramo (ficha maestra, meses 1 a 24)",
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 72))
    ax.text(1, 66.8, "Territorio (SUPUESTO por instrucción del usuario)", fontsize=10, fontweight="bold", color=TINTA)
    deps = [("Caldas", 33), ("Cundinamarca", 34), ("Valle del Cauca", 33)]
    x0, w, gap = 2, 29, 4.5
    for i, (nombre, n) in enumerate(deps):
        x = x0 + i * (w + gap)
        E.caja(ax, x, 44, w, 18, "", relleno=CLARO, grosor=1.3)
        ax.text(x + w / 2, 58.2, nombre, ha="center", va="center", fontsize=12, fontweight="bold", color=TINTA)
        ax.text(x + w / 2, 53.4, f"{n} nodos operativos", ha="center", va="center", fontsize=10.5, color=TINTA)
        ax.text(x + w / 2, 49.6, "4 municipios focalizados", ha="center", va="center", fontsize=9.5, color=TINTA)
        ax.text(x + w / 2, 46.4, "1 monitor de referencia", ha="center", va="center", fontsize=9.5, color=TINTA)
    ax.text(50, 40.6, "Total: 100 nodos operativos, 10 gateways, 3 monitores de referencia, 12 municipios y 15 comités (SUPUESTO)",
            ha="center", va="center", fontsize=9.3, color=TINTA)
    E.flecha(ax, (50, 38.6), (50, 33.8), lw=1.3)
    ax.text(52, 36.2, "Asignación de cada tramo por departamento: [DATO_USUARIO]", fontsize=8.6, color=TINTA, va="center")
    tramos = [
        (["Tramo 1:", "piloto de contraste"], "Meses 1 a 12", 30, 3, "o", AZUL, "C1 (mes 12)"),
        (["Tramo 2:", "ampliación condicionada"], "Meses 13 a 17", 40, 4, "s", MEDIO, "C2 (mes 17)"),
        (["Tramo 3:", "consolidación y transferencia"], "Meses 18 a 24", 30, 3, "^", CLARO, "C3 (mes 24)"),
    ]
    xs = [2, 35.5, 69]
    wbox = 29
    for (titulo, meses, nodos, gws, mk, col, comp), x in zip(tramos, xs):
        ax.add_patch(Rectangle((x, 5), wbox, 27.5, fc=E.CAJA, ec=TINTA, lw=1.1))
        ax.text(x + wbox / 2, 29.6, "\n".join(titulo), ha="center", va="center", fontsize=9, fontweight="bold", color=TINTA, linespacing=1.2)
        ax.text(x + wbox / 2, 25.2, meses, ha="center", va="center", fontsize=9, color=TINTA)
        filas = nodos // 10
        for r in range(filas):
            for c in range(10):
                ax.plot(x + 3.2 + c * 2.5, 21.6 - r * 2.5, mk, ms=6.0, mfc=col, mec=TINTA, mew=0.7)
        ytxt = 21.6 - (filas - 1) * 2.5 - 3.4
        ax.text(x + wbox / 2, ytxt, f"{nodos} nodos y {gws} gateways", ha="center", va="center", fontsize=9, fontweight="bold", color=TINTA)
        ax.text(x + wbox / 2, ytxt - 2.8, f"Compuerta {comp}", ha="center", va="center", fontsize=9, color=TINTA)
    E.flecha(ax, (31.2, 18), (35.3, 18), lw=1.3)
    E.flecha(ax, (64.7, 18), (68.8, 18), lw=1.3)
    ax.text(50, 2.0, "Cada compuerta libera la compra del tramo siguiente. Se compran 120 nodos y 11 gateways (reserva incluida).",
            ha="center", va="center", fontsize=8.8, color=TINTA)
    E.guardar(fig, "c1_f01")


def f02():
    d = json.load(open(ARBOL, encoding="utf-8"))
    fig, ax = E.lienzo_libre(
        h1="El error de medición sin verificar une cuatro causas directas con dos efectos directos",
        h2="Árbol de problemas A-PROB: 10 nodos y 10 relaciones de peso 2 o 3 en el escenario S2\n(hipótesis de influencia estructural; PROPUESTO)",
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 72))
    texto = {
        "V14": ["Personas sin protección", "efectiva por alertas", "confiables (V14)"],
        "V15": ["Baja adopción", "institucional del tablero", "y de las alertas (V15)"],
        "V11": ["Índice AQHI sin fórmula", "local validada y con error", "de entrada (V11)"],
        "V12": ["Tasa de falsas alarmas", "sin medir (V12)"],
        "V06": ["Error de medición de PM2,5 y PM10", "sin verificar frente a", "una referencia (V06)"],
        "V03": ["Humedad relativa alta", "en los sitios de", "remoción (V03)"],
        "V02": ["Concentración de PM10", "con fracción gruesa", "(V02)"],
        "V01": ["Concentración de", "PM2,5 (V01)"],
        "V07": ["Frecuencia de calibración", "de los nodos baja", "o nula (V07)"],
        "V05": ["Remoción de escombros", "en curso (V05)"],
    }
    assert {n["id"] for n in d["nodos"]} == set(texto), "los nodos del JSON no coinciden con el dibujo"
    assert len(d["enlaces"]) == 10
    ypos = {0: 62, 1: 48.5, 2: 35, 3: 21.5, 4: 8}
    X = {"V03": 26, "V02": 46.5, "V01": 67, "V07": 87.5}
    xmid = (X["V03"] + X["V07"]) / 2
    pos = {"V14": (42, 0), "V15": (71.5, 0), "V11": (42, 1), "V12": (71.5, 1), "V06": (xmid, 2),
           "V03": (X["V03"], 3), "V02": (X["V02"], 3), "V01": (X["V01"], 3), "V07": (X["V07"], 3), "V05": (xmid, 4)}
    cx = {k: v[0] for k, v in pos.items()}
    cy = {k: ypos[v[1]] for k, v in pos.items()}
    nivel = {k: v[1] for k, v in pos.items()}
    relleno = {0: GRIS, 1: CLARO, 2: AZUL, 3: MEDIO, 4: GRIS}
    h = 9.2
    ancho = {k: (33 if k == "V06" else 19.5) for k in texto}
    for k in texto:
        caja_texto(ax, cx[k], cy[k], ancho[k], h, texto[k], relleno[nivel[k]], bold=(k == "V06"),
                   grosor=2.4 if k == "V06" else 1.2, fs=8.4, dashed=(nivel[k] == 4))
    for e in d["enlaces"]:
        a, b = e["de"], e["a"]
        p0 = (cx[a], cy[a] + h / 2 + 0.4)
        p1 = (cx[b], cy[b] - h / 2 - 0.4)
        if a == "V05":
            p0 = (cx[a] + (-5 if b == "V02" else 5), cy[a] + h / 2 + 0.4)
            p1 = (cx[b] + (2 if b == "V02" else -2), cy[b] - h / 2 - 0.4)
        if b == "V06":
            p1 = (cx[b] + {"V03": -11, "V02": -4, "V01": 4, "V07": 11}[a], cy[b] - h / 2 - 0.4)
            if a in ("V03", "V07"):
                p0 = (cx[a] + (6 if a == "V03" else -6), cy[a] + h / 2 + 0.4)
        if a == "V06":
            p0 = (cx[a] + {"V11": -5, "V12": 5}[b], cy[a] + h / 2 + 0.4)
        E.flecha(ax, p0, p1, lw=1.4)
    nombres = {0: ["Efectos", "indirectos"], 1: ["Efectos", "directos"], 2: ["Problema", "central"], 3: ["Causas", "directas"], 4: ["Causa", "indirecta"]}
    for n, y in ypos.items():
        ax.text(0.8, y, "\n".join(nombres[n]), fontsize=8.8, fontweight="bold", color=TINTA, va="center", linespacing=1.2)
    ax.text(50, 0.6, "Las flechas van de la causa al efecto. Los bucles de S2 no se dibujan y permanecen en el registro de contraste de la sección 4.5.",
            ha="center", va="center", fontsize=8.2, color=TINTA)
    E.guardar(fig, "c1_f02")


def f03():
    fig, ax = E.lienzo_libre(
        h1="Tres variables explicativas se relacionan con el error de medición, con moderación y controles",
        h2="Modelo relacional del problema formal (ficha maestra §10c). Signos de S2: hipótesis de\ninfluencia estructural (PROPUESTO)",
        figsize=(10, 6.4), xlim=(0, 100), ylim=(0, 62))
    caja_texto(ax, 79, 31, 38, 17, ["Y: NRMSE de los nodos frente", "a la referencia colocalizada (V06)", "Meta: NRMSE ≤ 30 % y R² ≥ 0,70", "Valor actual: VACIO (tramo 1)"], AZUL, bold=True, grosor=2.2, fs=8.6)
    caja_texto(ax, 19, 48, 35, 9.5, ["X1: humedad relativa (V03)", "Moderadora de la respuesta óptica"], MEDIO, fs=8.8)
    caja_texto(ax, 19, 31, 35, 9.5, ["X2: fracción gruesa (V02 menos V01)", "PM10 menos PM2,5"], MEDIO, fs=8.8)
    caja_texto(ax, 19, 14, 35, 9.5, ["X3: frecuencia y calidad de", "calibración (V07)"], MEDIO, fs=8.8)
    caja_texto(ax, 79, 54, 34, 9, ["M: disponibilidad de nodos (V09)", "Variable moderadora"], CLARO, fs=8.8, dashed=True)
    caja_texto(ax, 80, 8, 36, 11, ["C: temperatura, edad del cabezal y", "distancia a la referencia", "(variables omitidas del modelo de 15)"], GRIS, fs=8.8, dashed=True)
    E.flecha(ax, (36.8, 48), (59.6, 36.5), lw=1.5)
    ax.text(48, 45.2, "+", fontsize=15, fontweight="bold", color=TINTA)
    E.flecha(ax, (36.8, 31), (59.6, 31), lw=1.5)
    ax.text(48, 32.2, "+", fontsize=15, fontweight="bold", color=TINTA)
    E.flecha(ax, (36.8, 14), (59.6, 25.5), lw=1.5)
    ax.text(48, 14.8, "−", fontsize=17, fontweight="bold", color=TINTA)
    E.flecha(ax, (79, 49.2), (79, 39.8), lw=1.3, ls="--")
    E.flecha(ax, (79, 13.8), (79, 22.2), lw=1.3, ls="--")
    ax.text(1, 3.4, "Signo: efecto esperado sobre Y (+ aumenta el error; − lo reduce).", fontsize=8.4, color=TINTA, va="center")
    ax.text(1, 0.8, "Línea continua: influencia sobre Y. Línea discontinua: moderación o control.", fontsize=8.4, color=TINTA, va="center")
    E.guardar(fig, "c1_f03")


if __name__ == "__main__":
    f01(); f02(); f03()
    print("c1_f01, c1_f02, c1_f03 generadas")
