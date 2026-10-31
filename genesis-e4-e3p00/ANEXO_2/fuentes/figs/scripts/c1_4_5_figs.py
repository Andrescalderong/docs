# -*- coding: utf-8 -*-
"""Figuras del Anexo 2: c1_f01 (territorio y tramos), c4_f01 (cadena de la emergencia a la decisión), c5_f01 (municipios y estaciones),
c5_f02 (árbol de problemas). Cifras: A2/v2/m2.py (tramos, nodos, gateways, consejos) y A2/FIGS_A2.md (nodos por departamento y
cifras del informe de vigilancia). Ejecución: python3 c1_4_5_figs.py  -> A2/figs/out/c1_f01.png, c4_f01.png, c5_f01.png, c5_f02.png"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _a2 as A
from _a2 import T, AZUL, MEDIO, CLARO, GRIS, CAJA, BLANCO, P, F_B, F_S
import matplotlib.pyplot as plt

TR = A.m2.M0.TRAMOS
NODOS, GW = A.m2.IDENT["nodos"], A.m2.IDENT["gateways"]
COMP_NODOS, COMP_GW = A.m2.IDENT["nodos_comprados"], A.m2.IDENT["gateways_comprados"]
DEP = [("Manizales", "Caldas, región Eje Cafetero", 50), ("Calarcá", "Quindío, región Eje Cafetero", 50)]
assert sum(d[2] for d in DEP) == NODOS == sum(t["nodos"] for t in TR) and sum(t["gateways"] for t in TR) == GW
MUN, COMITES = 2, 4


# ------------------------------------------------------------------ c1_f01
def c1_f01():
    H = 70.5
    fig, ax = A.lienzo("Dos municipios de dos departamentos reciben 100 nodos en tres tramos",
                       "Esquema sin escala: nodos operativos por municipio y por tramo, meses 1 a 24", H)
    w, x0 = 29.0, 1.0
    gap = (98 - 3 * w) / 2
    y = H - 0.5
    hd = 16.0
    wm, gm = 44.0, 98 - 2 * 44.0
    for i, (nom, reg, n) in enumerate(DEP):
        A.caja(ax, x0 + i * (wm + gm), y - hd, wm, hd,
               [(nom, "b", 9.4), (reg, "n"), (f"{n} nodos operativos", "b"), ("5 gateways y su consejo municipal", "n"), ("Conjunto de referencia rotativo", "n")],
               relleno=CLARO, gap=0.5)
    y -= hd + 1.8
    # llave de total bajo las tres cajas
    ax.plot([x0, x0, x0 + 98, x0 + 98], [y + 0.8, y, y, y + 0.8], color=T, lw=1.3)
    y -= 0.9
    h_tot = A.lineas(ax, 50, y, f"Total: {NODOS} nodos operativos, {GW} gateways, 1 conjunto de referencia rotativo, "
                     f"{MUN} municipios y {COMITES} consejos de gestión del riesgo", F_B, False, ha="center", ancho=96)
    y -= h_tot + 0.6
    A.flecha(ax, (50, y), (50, y - 4.2))
    A.txt(ax, 52.5, y - 2.1, "Se despliegan en tres tramos", F_B, ha="left")
    y -= 5.4
    ht = 32.0
    marc = [("o", AZUL), ("s", MEDIO), ("^", CLARO)]
    for i, t in enumerate(TR):
        x = x0 + i * (w + gap)
        nombre = t["nombre"].split(": ")
        A.caja(ax, x, y - ht, w, ht, "", relleno=CAJA)
        A.lineas(ax, x + w / 2, y - 1.0, f"{nombre[0]}:\n{nombre[1]}", F_B, True, ha="center", ancho=w - 3)
        A.txt(ax, x + w / 2, y - 10.2, f"Meses {t['m_ini']} a {t['m_fin']}", F_B, ha="center")
        filas = t["nodos"] // 10
        m, c = marc[i]
        for r in range(filas):
            for cc in range(10):
                ax.plot(x + w / 2 + (cc - 4.5) * 2.4, y - 14.2 - r * 2.5, m, ms=7.6, mfc=c, mec=T, mew=0.8, zorder=3)
        A.txt(ax, x + w / 2, y - ht + 7.2, f"{t['nodos']} nodos y {t['gateways']} gateways", F_B, True, ha="center")
        A.txt(ax, x + w / 2, y - ht + 3.8, f"Compuerta {t['compuerta']} (mes {t['mes_compuerta']})", F_B, ha="center")
        if i < 2:
            A.flecha(ax, (x + w + 0.4, y - ht / 2), (x + w + gap - 0.4, y - ht / 2))
    y -= ht + 1.4
    A.lineas(ax, 50, y, f"Cada compuerta libera la compra del tramo siguiente.\nSe compran {COMP_NODOS} nodos y {COMP_GW} gateways, "
             "con la reserva incluida.", F_B, ha="center", ancho=96)
    return A.guardar(fig, "c1_f01")


# ------------------------------------------------------------------ c4_f01
def c4_f01():
    H = 52
    fig, ax = A.lienzo("La emergencia genera una brecha de medición que el proyecto cierra con productos verificables",
                       "Cadena del evento a la decisión, de izquierda a derecha y de arriba abajo", H)
    w, gap, x0 = 29.0, 5.5, 1.0
    h = 18.5
    y1 = H - 0.8 - h
    y2 = 1.0
    cajas = [
        ("1. Terremoto del 10 de agosto y declaratoria de emergencia", "", CAJA, 1.5),
        ("2. Demolición y remoción de escombros", "Emiten y resuspenden material particulado", CAJA, 1.5),
        ("3. Brecha de CTeI", "PM2,5 y PM10 sin error conocido, sin uso institucional y sin estimación previa en demoliciones", AZUL, 2.6),
        ("4. Solución del proyecto", "Red híbrida con corrección en el gateway, gemelo digital y laboratorio de modelación", MEDIO, 1.5),
        ("5. Productos verificables", "Prototipos validados, infraestructura, documentos y formación", CLARO, 1.5),
        ("6. Resultado", f"Decisiones de alerta con datos de error conocido y evaluación previa de demoliciones en {COMITES} consejos", CLARO, 1.5),
    ]
    pos = []
    for k, (tit, cuerpo, col, lw) in enumerate(cajas):
        fila = 0 if k < 3 else 1
        x = x0 + (k % 3) * (w + gap)
        yb = y1 if fila == 0 else y2
        bl = [(tit, "b")] + ([(cuerpo, "n")] if cuerpo else [])
        A.caja(ax, x, yb, w, h, bl, relleno=col, lw=lw, gap=0.8)
        pos.append((x, yb))
    for k in (0, 1, 3, 4):
        x, yb = pos[k]
        A.flecha(ax, (x + w + 0.4, yb + h / 2), (x + w + gap - 0.4, yb + h / 2))
    # conector de la brecha a la solución
    xa, ya = pos[2][0] + w / 2, pos[2][1]
    xb, yb = pos[3][0] + w / 2, pos[3][1] + h
    ymid = (ya + yb) / 2
    A.ruta(ax, [(xa, ya - 0.3), (xa, ymid), (xb, ymid), (xb, yb + 0.4)])
    A.txt(ax, (xa + xb) / 2, ymid + 1.9, "El proyecto responde a la brecha", F_B, ha="center")
    return A.guardar(fig, "c4_f01")


# ------------------------------------------------------------------ c5_f01
def c5_f01():
    H = 64
    fig, ax = A.lienzo("Solo 28 de 1.122 municipios cuentan con estaciones utilizables",
                       "Municipios de Colombia y estaciones de calidad del aire, número de unidades", H)
    plt.rcParams["hatch.linewidth"] = 0.7
    # panel de municipios
    A.txt(ax, 1, H - 2.0, "Municipios de Colombia", F_B, True)
    etiq = ["Municipios del país", "Municipios que miden la calidad del aire",
            "Municipios con estaciones utilizables para estimar la carga", "Municipios focalizados por el proyecto"]
    val = [1122, 92, 28, 2]
    col = [AZUL, MEDIO, CLARO, GRIS]
    hat = ["", "///", "...", "xx"]
    a1 = A.subeje(fig, ax, 38, H - 31.5, 97, H - 4.0)
    ys = list(range(4))[::-1]
    for yv, v, c, h in zip(ys, val, col, hat):
        a1.barh(yv, v, height=0.62, color=c, edgecolor=T, linewidth=1.0, hatch=h, zorder=3)
        a1.annotate(E_num(v), xy=(v, yv), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=P(F_B), fontweight="bold", color=T)
    a1.set_yticks(ys)
    a1.set_yticklabels(["\n".join(A.envolver(e, 31.5 * A.UNIT, P(F_B))) for e in etiq], fontsize=P(F_B), color=T, linespacing=1.2)
    a1.set_xlim(0, 1400); a1.set_ylim(-0.55, 3.55)
    a1.set_xticks([0, 250, 500, 750, 1000, 1250])
    a1.set_xticklabels([E_num(v) for v in (0, 250, 500, 750, 1000, 1250)])
    a1.grid(axis="x", zorder=0); a1.tick_params(axis="y", length=0)
    a1.set_xlabel("Número de municipios", fontsize=P(F_B), color=T)
    a1.annotate(f"Los otros {E_num(1122 - 28)} municipios no cuentan\ncon estaciones utilizables", xy=(28, ys[2]), xytext=(150, ys[2]),
                textcoords="data", ha="left", va="center", fontsize=P(F_B), color=T, linespacing=1.25)
    # panel de estaciones
    A.txt(ax, 1, 21.2, "Estaciones del país: 192 fijas y 17 indicativas", F_B, True)
    et2 = ["Estaciones reportadas", "Estaciones integradas a un sistema de vigilancia"]
    v2 = [209, 154]
    a2 = A.subeje(fig, ax, 38, 7.5, 97, 18.5)
    for yv, v, c, h in zip([1, 0], v2, [AZUL, MEDIO], ["", "///"]):
        a2.barh(yv, v, height=0.6, color=c, edgecolor=T, linewidth=1.0, hatch=h, zorder=3)
        a2.annotate(E_num(v), xy=(v, yv), xytext=(4, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=P(F_B), fontweight="bold", color=T)
    a2.set_yticks([1, 0])
    a2.set_yticklabels(["\n".join(A.envolver(e, 31.5 * A.UNIT, P(F_B))) for e in et2], fontsize=P(F_B), color=T, linespacing=1.2)
    a2.set_xlim(0, 300); a2.set_ylim(-0.55, 1.55)
    a2.set_xticks([0, 50, 100, 150, 200, 250, 300])
    a2.set_xticklabels([E_num(v) for v in (0, 50, 100, 150, 200, 250, 300)])
    a2.grid(axis="x", zorder=0); a2.tick_params(axis="y", length=0)
    a2.set_xlabel("Número de estaciones", fontsize=P(F_B), color=T)
    return A.guardar(fig, "c5_f01")


def E_num(v):
    return A.num(v, 0)


# ------------------------------------------------------------------ c5_f02
def c5_f02():
    H = 78
    fig, ax = A.lienzo("El error de medición sin verificar es el problema central: tiene cuatro causas directas y dos efectos directos",
                       "Árbol de problemas del proyecto; las flechas van de la causa al efecto", H)
    xl, xr, wl = 15.0, 99.0, 14.0
    gapv = 6.4
    alt = [10.0, 10.0, 13.5, 11.0, 6.0]
    ytop = [H - 0.6]
    for a in alt[:-1]:
        ytop.append(ytop[-1] - a - gapv)
    yb = [t - a for t, a in zip(ytop, alt)]     # base de cada fila
    nombres = ["Efectos\nindirectos", "Efectos\ndirectos", "Problema\ncentral", "Causas\ndirectas", "Causa\nindirecta"]
    for k, nm in enumerate(nombres):
        A.txt(ax, 1, yb[k] + alt[k] / 2, nm, F_B, True, va="center")
    # efectos indirectos y directos
    wb = 39.0
    xs2 = [16.0, 60.0]
    ei = ["Población y trabajadores sin protección efectiva ante alertas poco confiables",
          "Baja adopción institucional del tablero y de las alertas"]
    ed = ["Índice local de calidad del aire sin fórmula validada y con error de entrada", "Tasa de falsas alarmas sin medir"]
    for x, t in zip(xs2, ei):
        A.caja(ax, x, yb[0], wb, alt[0], t, relleno=CAJA)
    for x, t in zip(xs2, ed):
        A.caja(ax, x, yb[1], wb, alt[1], t, relleno=CLARO)
    # problema central
    xc, wc = 26.0, 63.0
    A.caja(ax, xc, yb[2], wc, alt[2],
           [("Los consejos de gestión del riesgo no disponen de mediciones de PM2,5 y PM10 con error conocido en los sitios de remoción de escombros", "b")],
           relleno=AZUL, lw=2.6, fs=F_B)
    # causas directas
    wcau, gcau = 19.5, 2.0
    cau = ["Humedad relativa alta en los sitios", "Fracción gruesa de PM10 sin corrección", "PM2,5 sin referencia colocalizada",
           "Calibración baja o nula"]
    xcs = [xl + i * (wcau + gcau) for i in range(4)]
    for x, t in zip(xcs, cau):
        A.caja(ax, x, yb[3], wcau, alt[3], t, relleno=MEDIO)
    # causa indirecta
    xi, wi = 40.5, 34.0
    A.caja(ax, xi, yb[4], wi, alt[4], "Remoción de escombros en curso", relleno=CAJA, ls=(0, (4, 2.5)))
    # flechas causa -> efecto
    for k in range(2):
        A.flecha(ax, (xs2[k] + wb / 2, yb[1] + alt[1] + 0.3), (xs2[k] + wb / 2, yb[0] - 0.3))
    for xe, xd in zip((xs2[0] + wb / 2, xs2[1] + wb / 2), (xc + 18, xc + wc - 18)):
        A.flecha(ax, (xd, yb[2] + alt[2] + 0.3), (xe, yb[1] - 0.3))
    for x, xe in zip(xcs, (xc + 7, xc + 22, xc + 41, xc + 56)):
        A.flecha(ax, (x + wcau / 2, yb[3] + alt[3] + 0.3), (xe, yb[2] - 0.3))
    for xdest in (xcs[1] + wcau / 2, xcs[2] + wcau / 2):
        A.flecha(ax, (xdest, yb[4] + alt[4] + 0.3), (xdest, yb[3] - 0.3))
    return A.guardar(fig, "c5_f02")


if __name__ == "__main__":
    only = sys.argv[1:] or ["c1_f01", "c4_f01", "c5_f01", "c5_f02"]
    for f in only:
        globals()[f]()
