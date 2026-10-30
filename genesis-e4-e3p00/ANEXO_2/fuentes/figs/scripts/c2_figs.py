# -*- coding: utf-8 -*-
"""Resumen gráfico del resumen ejecutivo (sección 2): problema y solución tecnológica. Salida: A2/figs/out/c2_f01.png"""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/scripts")
from _comun import *


def c2_f01(h=16.0, medir=False):
    L = Lienzo(10, h, h1="El polvo de las demoliciones posterremoto se mide con error conocido, se anticipa y se usa para decidir",
               h2="Resumen gráfico del problema y de la solución tecnológica en Manizales (Caldas) y Calarcá (Quindío)")
    x0, W = 1.0, 98.0
    wl, gap = 41.0, 16.0
    xr = x0 + wl + gap
    wr = W - wl - gap
    y = L.top - 0.4
    ht = 3.6
    L.caja(x0, y - ht, wl, ht, titulo="Problema", fc=MEDIO, pad=0.7, lw=1.4)
    L.caja(xr, y - ht, wr, ht, titulo="Solución tecnológica", fc=AZUL, pad=0.7, lw=1.4)
    y -= ht + 2.6
    P = [("Terremoto del 10 de agosto de 2026", "Edificaciones colapsadas o dañadas en los centros urbanos de Manizales y Calarcá"),
         ("Demolición y remoción de escombros", "Obras que duran semanas o meses dentro de la ciudad"),
         ("Polvo PM2,5 y PM10", "Material particulado que respiran operarios y vecinos de los sitios"),
         ("Decisión sin datos", "Los consejos de gestión del riesgo no tienen una medición con error conocido ni una estimación previa del polvo")]
    S = [("Red IoT híbrida Edge-Cloud", "100 nodos y 10 gateways; corrección en el gateway frente a un conjunto de referencia rotativo y un banco de calibración"),
         ("Plataforma geoespacial y gemelo digital", "Índice local de calidad del aire, tablero de los consejos y protocolo de alerta co-diseñado"),
         ("Laboratorio de modelación", "Gemelo predictivo que estima, antes de demoler, la emisión, la dispersión y la exposición esperadas")]
    gv = 3.2
    hp = [L.necesita(wl, cuerpo=c, titulo=t, pad=0.8) + 0.4 for t, c in P]
    hs = [L.necesita(wr, cuerpo=c, titulo=t, pad=0.8) + 0.4 for t, c in S]
    tot_p = sum(hp) + gv * (len(P) - 1)
    tot_s = sum(hs) + gv * (len(S) - 1)
    alto = max(tot_p, tot_s)
    gvs = (alto - sum(hs)) / (len(S) - 1)
    gvp = (alto - sum(hp)) / (len(P) - 1)
    yy = y
    cp = []
    for (t, c), hh in zip(P, hp):
        L.caja(x0, yy - hh, wl, hh, cuerpo=c, titulo=t, fc=CLARO if t != "Decisión sin datos" else MEDIO, pad=0.8, lw=1.3)
        cp.append((yy - hh, hh))
        yy -= hh + gvp
    for i in range(len(P) - 1):
        a = cp[i]; b = cp[i + 1]
        L.flecha((x0 + wl / 2, a[0] - 0.2), (x0 + wl / 2, b[0] + b[1] + 0.2), lw=1.5)
    yy = y
    cs = []
    for (t, c), hh in zip(S, hs):
        L.caja(xr, yy - hh, wr, hh, cuerpo=c, titulo=t, fc=AZUL, pad=0.8, lw=1.5)
        cs.append((yy - hh, hh))
        yy -= hh + gvs
    for i in range(len(S) - 1):
        a = cs[i]; b = cs[i + 1]
        L.flecha((xr + wr / 2, a[0] - 0.2), (xr + wr / 2, b[0] + b[1] + 0.2), lw=1.5)
    ymid = y - alto / 2
    L.flecha((x0 + wl + 1.0, ymid), (xr - 1.0, ymid), lw=2.6, ms=22)
    L.t(x0 + wl + gap / 2, ymid + 3.4, "responde", ha="center", italic=True)
    ybot = y - alto - 4.0
    d_txt = ("Decisiones de alerta con R² ≥ 0,70 y NRMSE ≤ 30 % frente a la referencia; 12 evaluaciones previas de demolición; "
             "red en TRL 8 y gemelo predictivo en TRL 6; equipos y protocolos bajo custodia local")
    hd = L.necesita(W, cuerpo=d_txt, titulo="Resultado al mes 24", pad=1.0) + 0.4
    L.caja(x0, ybot - hd, W, hd, cuerpo=d_txt, titulo="Resultado al mes 24", fc=CLARO, pad=1.0, lw=1.5)
    L.flecha((xr + wr / 2, cs[-1][0] - 0.2), (xr + wr / 2, ybot + 0.2), lw=1.5)
    if medir:
        plt.close(L.fig)
        return L.H - (ybot - hd) + 1.0
    L.guardar("c2_f01")


if __name__ == "__main__":
    c2_f01(h=c2_f01(medir=True) / 10)
