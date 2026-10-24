# -*- coding: utf-8 -*-
"""Figura del soporte inicial (S.1) y de la guía para explicar el proyecto: cS_f02, del terremoto del 10 de agosto a la decisión del comité.
Cifras de A2/v2/m2.py (nodos, gateways, referencias, comités, meses). Ejecución: python3 cS_figs.py -> A2/figs/out/cS_f02.png"""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/scripts")
from _comun import *

NODOS, GW, REFS = m2.IDENT["nodos"], m2.IDENT["gateways"], m2.IDENT["referencias"]
COMITES, MESES = 15, m2.IDENT.get("meses", 24)


def cS_f02(h=16.0, medir=False):
    L = Lienzo(10, h, h1="El terremoto del 10 de agosto dejó un riesgo que los comités hoy no pueden medir ni anticipar: el polvo de las demoliciones",
               h2="De la emergencia a la decisión del comité de gestión del riesgo: qué ocurre, qué falta y qué hace el proyecto")
    x0, W, g = 1.0, 98.0, 4.2
    y = L.top - 0.2
    # ---- fila A: cuatro eslabones de la cadena
    wa = (W - 3 * g) / 4
    A = [("1. El terremoto", "10 de agosto de 2026: edificaciones colapsadas o dañadas en los departamentos de la emergencia", CLARO),
         ("2. Demolición y escombros", "Se demuelen edificios y se retiran escombros dentro de los centros urbanos, durante semanas o meses", CLARO),
         ("3. Polvo en el aire", "El trabajo levanta polvo fino y grueso (PM2,5 y PM10) que respiran operarios y vecinos", CLARO),
         ("4. Una decisión", "El comité de gestión del riesgo decide: parar la obra, humedecer, desviar el tránsito o avisar a la comunidad", MEDIO)]
    ha = max(L.necesita(wa, cuerpo=c, titulo=t, pad=0.8) for t, c, _ in A) + 0.6
    for i, (t, c, col) in enumerate(A):
        x = x0 + i * (wa + g)
        L.caja(x, y - ha, wa, ha, cuerpo=c, titulo=t, fc=col, pad=0.8, lw=1.4)
        if i < 3:
            L.flecha((x + wa + 0.3, y - ha / 2), (x + wa + g - 0.3, y - ha / 2), lw=1.6)
    yA = y - ha
    # ---- fila B: lo que hoy falta (marco discontinuo con dos faltantes)
    gv = 4.6
    wb2 = (W - 2 * 1.4 - 1.6) / 2
    B = [("Un dato confiable de cuánto polvo hay", "Los sensores baratos se desvían con la humedad y con el polvo grueso, y en esos sitios no hay equipos de referencia"),
         ("Una estimación de cuánto polvo saldrá", "Antes de demoler un edificio, los comités no cuentan con un cálculo de cuánto polvo emitirá la obra ni hacia dónde se desplazará")]
    hb = max(L.necesita(wb2, cuerpo=c, titulo=t, pad=0.8) for t, c in B) + 0.6
    htit = 3.4
    hfr = htit + hb + 1.8
    yB = yA - gv - hfr
    L.caja(x0, yB, W, hfr, fc=BLANCO, ls=(0, (4, 3)), lw=1.4, radio=1.2)
    L.t(x0 + 1.4, yB + hfr - htit / 2 - 0.4, "Lo que hoy falta en esos sitios", bold=True)
    for i, (t, c) in enumerate(B):
        L.caja(x0 + 1.4 + i * (wb2 + 1.6), yB + 1.0, wb2, hb, cuerpo=c, titulo=t, fc=CAJA, pad=0.8, lw=1.2)
    L.flecha((x0 + W - wa / 2, yA - 0.3), (x0 + W - wa / 2, yB + hfr + 0.3), lw=1.6)
    # ---- fila C: tres respuestas del proyecto
    wc = (W - 2 * g) / 3
    C = [("Medir bien", f"{NODOS} sensores de bajo costo en los sitios de remoción de Caldas, Cundinamarca y Valle del Cauca, corregidos con {REFS} equipos de referencia"),
         ("Avisar a tiempo", f"Un tablero con el índice local del aire y un protocolo de alerta que los {COMITES} comités diseñan con el proyecto y usan"),
         ("Anticipar", "Un laboratorio de la universidad que calcula, antes de cada demolición, el polvo esperado y las medidas que lo reducen")]
    hc = max(L.necesita(wc, cuerpo=c, titulo=t, pad=0.8) for t, c in C) + 0.6
    yC = yB - gv - hc
    for i, (t, c) in enumerate(C):
        x = x0 + i * (wc + g)
        L.caja(x, yC, wc, hc, cuerpo=c, titulo=t, fc=AZUL, pad=0.8, lw=1.6)
        L.flecha((x + wc / 2, yB - 0.3), (x + wc / 2, yC + hc + 0.3), lw=1.6)
    L.t(x0 + wc / 2 + (wc + g) / 2, yB - gv / 2, "Respuesta del proyecto", ha="center", bold=True)
    # ---- fila D: resultado
    gd = 4.0
    d_txt = (f"Al mes {MESES}: los comités deciden con datos de calidad conocida y con una estimación previa del polvo; "
             "la red y el laboratorio quedan bajo custodia local, sin depender de una nueva financiación")
    hd = L.necesita(W, cuerpo=d_txt, titulo="Qué queda", pad=1.0) + 0.6
    yD = yC - gd - hd
    L.caja(x0, yD, W, hd, cuerpo=d_txt, titulo="Qué queda", fc=CLARO, pad=1.0, lw=1.6)
    for i in range(3):
        xx = x0 + i * (wc + g) + wc / 2
        L.flecha((xx, yC - 0.3), (xx, yD + hd + 0.3), lw=1.6)
    if medir:
        plt.close(L.fig)
        return L.H - yD + 1.0
    L.guardar("cS_f02")


if __name__ == "__main__":
    cS_f02(h=cS_f02(medir=True) / 10)
