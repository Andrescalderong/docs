# -*- coding: utf-8 -*-
"""Figuras de la sección 14 del Anexo 2: c14_f01 (fases, tramos y compuertas) y c14_f02 (decisión en las compuertas).
Cifras: tramos, compras y compuertas de m2.M0.TRAMOS; semanas de las fases de m2.ACTD y de la red de actividades (m2.M0.ACTS)."""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/scripts")
from _comun import *

TR = m2.M0.TRAMOS
ACTD = m2.ACTD
ACTS = m2.M0.ACTS


def _semanas():
    """Ventanas de semanas de cada fase, a partir de las actividades y de las compuertas del calendario."""
    f1 = (0, max(ACTD["1.1"]["ef"], ACTD["2.1"]["ef"]))
    f2 = (ACTD["1.2"]["es"], ACTD["1.2"]["ef"])
    f3 = (ACTD["1.3"]["es"], ACTD["1.4"]["ef"])
    f5 = (ACTD["2.3"]["es"], ACTD["3.4"]["ef"])
    c1 = (ACTS["C1"]["ES"], ACTS["C1"]["EF"])
    c2 = (ACTS["C2"]["ES"], ACTS["C2"]["EF"])
    assert f1 == (0, 14) and f2 == (14, 24) and f3 == (24, 50) and f5 == (50, 104) and c1 == (48, 50) and c2 == (68, 70)
    return f1, f2, f3, f5, c1, c2


# ============================================================ c14_f01
def f01():
    f1, f2, f3, f5, c1, c2 = _semanas()
    L = Lienzo(10, 10.4, h1="Cinco fases en tres tramos ordenan el trabajo y cada compuerta libera la compra siguiente",
               h2="Fases con las semanas de la ruta crítica (semanas 0 a 104), laboratorio de modelación por semanas y tramos con sus compuertas por mes (meses 1 a 24)")
    top = L.top
    fases = [
        ("Fase 1", "Diseñar y planificar", "Semanas\n%d a %d" % f1, "Actividades\n1.1 y 2.1", CLARO, None),
        ("Fase 2", "Construir", "Semanas\n%d a %d" % f2, "Actividades\n1.2, 2.2 y 3.1", CLARO, None),
        ("Fase 3", "Medir", "Semanas\n%d a %d" % f3, "Actividades\n1.3 y 1.4", MEDIO, None),
        ("Fase 4", "Aprender y decidir", "Compuerta C1:\nsemanas %d a %d\nCompuerta C2:\nsemanas %d a %d" % (c1 + c2), "", AZUL, None),
        ("Fase 5", "Escalar", "Semanas\n%d a %d" % f5, "Actividades 2.3, 1.5, 3.2, 2.4, 3.3, 1.6 y 3.4", MEDIO, "///"),
    ]
    gap = 1.8
    w = (98.0 - 4 * gap) / 5
    hb = 22.0
    ytop_box = top - 9.2
    yb_box = ytop_box - hb
    xs = [1.0 + i * (w + gap) for i in range(5)]
    for (num_, nom, sem, act, col, tr_), x in zip(fases, xs):
        cuerpo = sem + ("\n" + act if act else "")
        L.caja(x, yb_box, w, hb, titulo=num_ + "\n" + nom, cuerpo=cuerpo, fc=col, trama=tr_, va="top", pad=0.9)
    for i in range(4):
        yc = yb_box + hb / 2
        L.flecha((xs[i] + w + 0.1, yc), (xs[i + 1] - 0.1, yc), lw=1.6, ms=11)
    # ciclo de corrección: de la fase 4 a la fase 2 (arco por encima)
    L.flecha((xs[3] + w / 2, ytop_box + 0.6), (xs[1] + w / 2, ytop_box + 0.6), ls=(0, (5, 3)), rad=0.22, lw=1.5)
    L.t(xs[2] + w / 2, ytop_box + 6.9, "ciclo de corrección: volver a construir o a medir", ha="center", va="center")
    # laboratorio de modelación (semanas de m2.ACTD en la misma escala horizontal que los tramos)
    x_ini, x_fin = 1.0, 94.0
    def xw(w):
        return x_ini + w / 104.0 * (x_fin - x_ini)
    ylab_top = yb_box - 3.6
    L.t(1.0, ylab_top + 0.2, "Laboratorio de modelación (actividades 2.5, 2.6, 2.7, 1.7 y 3.5)", bold=True, ha="left", va="center")
    hA = 8.6
    yA = ylab_top - 2.2 - hA
    yB = yA - 1.2 - hA
    lab = [("2.5", yA, "Diseñar", None, CLARO, None), ("2.6", yA, "Dotar", "hito H9, mes 11", CLARO, None),
           ("2.7", yA, "Calibrar", "hito H10, mes 17", MEDIO, None), ("1.7", yB, "Validar con eventos", "hito H11, mes 22", AZUL, None),
           ("3.5", yA, "", None, CLARO, None)]
    for k, y, tit, hito, col, tr_ in lab:
        a, b = ACTD[k]["es"], ACTD[k]["ef"]
        if k == "3.5":
            L.caja(xw(a) + 0.15, y, xw(b) - xw(a) - 0.3, hA, titulo="3.5", fc=col, trama=tr_, pad=0.4, radio=0.6, marco=0.8)
            L.t(xw(a) - 0.8, y + hA / 2, "Adoptar y\ntransferir", ha="right", va="center")
            continue
        L.caja(xw(a) + 0.15, y, xw(b) - xw(a) - 0.3, hA, titulo="%s %s" % (k, tit), cuerpo=hito or "", fc=col, trama=tr_, pad=0.5, radio=0.6, marco=0.8)
    # tramos (proporcionales a los meses)
    def xm(m):
        return x_ini + m / 24.0 * (x_fin - x_ini)
    ytr_top = yB - 3.6
    L.t(1.0, ytr_top + 0.2, "Tramos de despliegue (meses 1 a 24)", bold=True, ha="left", va="center")
    htr = 15.5
    ytr = ytr_top - 2.2 - htr
    spec = [
        (0, 12, AZUL, None, "Tramo 1: piloto de contraste", "meses 1 a 12\n30 nodos y 3 gateways"),
        (12, 17, MEDIO, "///", "Tramo 2:\nampliación", "meses 13 a 17\n40 nodos y\n4 gateways"),
        (17, 24, CLARO, "...", "Tramo 3:\nconsolidación", "meses 18 a 24\n30 nodos y 3 gateways"),
    ]
    for (a, b, col, tr_, tit, cu), t in zip(spec, TR):
        assert (t["m_ini"] - 1, t["m_fin"]) == (a, b) and "%d nodos y" % t["nodos"] in cu and ("%d gateways" % t["gateways"]) in cu
        L.caja(xm(a) + 0.15, ytr, xm(b) - xm(a) - 0.3, htr, titulo=tit, cuerpo=cu, fc=col, trama=tr_, va="center", pad=0.7, radio=0.6,
               marco=0.8)
    # compuertas
    comp = [(12, "C1", "mes 12", "libera la compra:\n%d nodos y\n%d gateways" % (TR[1]["compra_nodos"], TR[1]["compra_gw"])),
            (17, "C2", "mes 17", "libera la compra:\n%d nodos y\n%d gateways" % (TR[2]["compra_nodos"], TR[2]["compra_gw"])),
            (24, "C3", "mes 24", "cierra y\ntransfiere")]
    for m, c, mes, txt in comp:
        cx = xm(m)
        L.rombo(cx, ytr - 0.3, 9.0, 8.2, c, fc=BLANCO, fs=FS)
        L.t(cx, ytr - 6.0, mes, bold=True, ha="center", va="center")
        L.t(cx, ytr - 7.8, txt, ha="center", va="top")
    # compra inicial
    L.t(1.0, ytr - 6.0, "Compra inicial:", ha="left", va="center", bold=True)
    L.t(1.0, ytr - 7.8, "%d nodos y %d gateways" % (TR[0]["compra_nodos"], TR[0]["compra_gw"]), ha="left", va="top", w=24)
    L.guardar("c14_f01")


# ============================================================ c14_f02
def f02():
    t2, t3 = TR[1], TR[2]
    L = Lienzo(10, 8.1, h1="En cada compuerta se aplican tres criterios y un ciclo de corrección antes de liberar la compra",
               h2="Criterios de las compuertas C1 (mes 12) y C2 (mes 17); si se cumplen, se libera la compra del tramo siguiente en nodos y gateways")
    top = L.top
    xg, wg = 1.0, 14.5          # compuerta
    xc, wc = 19.0, 41.0         # criterios
    xs_, ws = 66.0, 33.0        # resultado
    gap = 4.3
    hs = 11.0
    h1c, hcor, h2c = 14.2, 10.0, 20.6
    # --- carril C1
    y1 = top - 0.5 - h1c
    L.caja(xg, y1, wg, h1c, titulo="Compuerta C1", cuerpo="mes 12", fc=MEDIO, lw=1.5)
    L.caja(xc, y1, wc, h1c, titulo="¿Se cumplen todos los criterios?",
           cuerpo="1. R² ≥ 0,70 y NRMSE ≤ 30 % frente a la referencia en el piloto\n2. Uso del tablero en al menos 50 % de los comités del tramo",
           fc=CLARO, lw=1.4, ha="left", va="center")
    L.flecha((xg + wg + 0.2, y1 + h1c / 2), (xc - 0.2, y1 + h1c / 2), lw=1.6)
    L.caja(xs_, y1 + h1c / 2 - hs / 2, ws, hs, titulo="Se libera la compra\ndel tramo 2",
           cuerpo="%d nodos y %d gateways" % (t2["compra_nodos"], t2["compra_gw"]), fc=AZUL, lw=1.6)
    L.flecha((xc + wc + 0.2, y1 + h1c / 2), (xs_ - 0.2, y1 + h1c / 2), lw=1.6)
    L.t((xc + wc + xs_) / 2, y1 + h1c / 2 + 2.3, "Sí", bold=True, ha="center", va="center")
    # --- ciclo de corrección (compartido por las dos compuertas)
    ycor = y1 - 2 * gap - hcor
    L.caja(xc, ycor, 80.0, hcor, titulo="Ciclo de corrección",
           cuerpo="Reentrenar por departamento, reforzar energía y enlace, o reforzar el co-diseño con los comités; "
                  "nueva verificación antes de comprar",
           fc=BLANCO, lw=1.6, ls=(0, (6, 3)), ha="left", va="center", pad=1.2)
    xn, xv = xc + 8.0, xc + 30.0
    L.flecha((xn, y1 - 0.1), (xn, ycor + hcor + 0.1), lw=1.6)
    L.t(xn + 1.6, y1 - gap, "No", bold=True, ha="left", va="center")
    L.flecha((xv, ycor + hcor + 0.1), (xv, y1 - 0.1), ls=(0, (4, 3)), lw=1.6)
    L.t(xv + 1.6, y1 - gap, "nueva verificación", ha="left", va="center")
    # --- carril C2
    y2 = ycor - 2 * gap - h2c
    L.caja(xg, y2, wg, h2c, titulo="Compuerta C2", cuerpo="mes 17", fc=MEDIO, lw=1.5)
    L.caja(xc, y2, wc, h2c, titulo="¿Se cumplen todos los criterios?",
           cuerpo="1. R² ≥ 0,70 y NRMSE ≤ 30 % frente a la referencia en los tres departamentos\n"
                  "2. Uso del tablero en al menos 50 % de los comités del tramo\n"
                  "3. Disponibilidad mensual ≥ 90 % y convenios de custodia con partida",
           fc=CLARO, lw=1.4, ha="left", va="center")
    L.flecha((xg + wg + 0.2, y2 + h2c / 2), (xc - 0.2, y2 + h2c / 2), lw=1.6)
    L.caja(xs_, y2 + h2c / 2 - hs / 2, ws, hs, titulo="Se libera la compra\ndel tramo 3",
           cuerpo="%d nodos y %d gateways" % (t3["compra_nodos"], t3["compra_gw"]), fc=AZUL, lw=1.6)
    L.flecha((xc + wc + 0.2, y2 + h2c / 2), (xs_ - 0.2, y2 + h2c / 2), lw=1.6)
    L.t((xc + wc + xs_) / 2, y2 + h2c / 2 + 2.3, "Sí", bold=True, ha="center", va="center")
    L.flecha((xn, y2 + h2c + 0.1), (xn, ycor - 0.1), lw=1.6)
    L.t(xn + 1.6, ycor - gap, "No", bold=True, ha="left", va="center")
    L.flecha((xv, ycor - 0.1), (xv, y2 + h2c + 0.1), ls=(0, (4, 3)), lw=1.6)
    L.t(xv + 1.6, ycor - gap, "nueva verificación", ha="left", va="center")
    L.t(1.0, y2 - 3.4, "El alcance de 100 nodos y 10 gateways no cambia: las compuertas ordenan la secuencia de compra.", ha="left",
        va="center", w=98)
    L.guardar("c14_f02")


# ============================================================ c14_f03
def f03():
    L = Lienzo(10, 8.6, h1="La cadena de modelación combina inventario, emisión, dispersión y evaluación previa, y se valida con mediciones en eventos reales",
               h2="Cuatro módulos del gemelo predictivo de demolición, sus entradas y el ciclo de validación con eventos reales")
    top = L.top
    w, gap = 22.0, 3.3
    xs = [1.0 + i * (w + gap) for i in range(4)]
    hin, hmod, hval = 22.5, 16.5, 15.5
    y_in = top - 0.4 - hin
    y_mod = y_in - 5.0 - hmod
    y_val = y_mod - 9.0 - hval
    ent = [("Entradas de emisión", "Inventario de la demolición: volumen, material, método, altura y calendario. Polvo del territorio: granulometría y composición"),
           ("Entradas de dispersión", "Geometría con dron LiDAR y cartografía; terreno; 4 estaciones meteorológicas y pronóstico"),
           ("Entradas del sustituto", "Casos tipo de geometría, material y viento simulados con el modelo de dispersión"),
           ("Criterios de lectura", "Valores guía de 24 horas de la OMS (2021) y escenarios de medidas de control")]
    mods = [("1. Emisión", "Factores de la EPA (1995) ajustados con el polvo local", CLARO),
            ("2. Dispersión", "AERMOD y simulación del flujo entre edificios", MEDIO),
            ("3. Modelo sustituto", "Aprendizaje supervisado entrenado con las simulaciones", MEDIO),
            ("4. Evaluación previa", "Concentración esperada con incertidumbre en los receptores", AZUL)]
    for x, (t, c), (tm, cm, col) in zip(xs, ent, mods):
        L.caja(x, y_in, w, hin, titulo=t, cuerpo=c, fc=CAJA, lw=1.3, va="center", pad=0.9)
        L.caja(x, y_mod, w, hmod, titulo=tm, cuerpo=cm, fc=col, lw=1.5, pad=0.9)
        L.flecha((x + w / 2, y_in - 0.2), (x + w / 2, y_mod + hmod + 0.2), lw=1.6)
    for i in range(3):
        yc = y_mod + hmod / 2
        L.flecha((xs[i] + w + 0.15, yc), (xs[i + 1] - 0.15, yc), lw=1.8, ms=12)
    # validación con eventos reales: recalibra los módulos 1 a 3
    wv = 3 * w + 2 * gap
    L.caja(xs[0], y_val, wv, hval, titulo="Validación con eventos reales",
           cuerpo="Nueve campañas con monitores portátiles a barlovento y a sotavento; FAC2 y sesgo fraccional por evento; validación cruzada dejando un evento fuera; verificación independiente",
           fc=BLANCO, lw=1.6, ls=(0, (6, 3)), pad=1.2)
    for i in range(3):
        L.flecha((xs[i] + w / 2, y_val + hval + 0.2), (xs[i] + w / 2, y_mod - 0.2), ls=(0, (4, 3)), lw=1.6, ms=12)
    L.t(xs[0] + w / 2 + 2.0, (y_mod + y_val + hval) / 2, "compara y recalibra", ha="left", va="center")
    # salida: informe y decisión
    L.caja(xs[3], y_val, w, hval, titulo="Informe de evaluación previa",
           cuerpo="El comité o la entidad territorial decide; no es una autorización", fc=CAJA, lw=1.5, pad=1.0)
    L.flecha((xs[3] + w / 2, y_mod - 0.2), (xs[3] + w / 2, y_val + hval + 0.2), lw=1.8)
    L.guardar("c14_f03")


if __name__ == "__main__":
    f01(); f02(); f03()
