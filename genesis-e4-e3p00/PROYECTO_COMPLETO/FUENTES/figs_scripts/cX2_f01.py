# -*- coding: utf-8 -*-
"""Figura cX2_f01 (one-pager): arquitectura y despliegue por tramos. Cifras de la ficha maestra (maestro.py). Determinista."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
import estilo as E

def main():
    T = C.M.TRAMOS; ID = C.M.IDENT
    fig, ax = C.lienzo_libre2(h1=f"Una red de {ID['nodos']} nodos corrige en {ID['gateways']} gateways y entrega mediciones a 15 comités",
                             h2="Arquitectura y despliegue por tramos durante 24 meses; cifras de la ficha maestra", figsize=(10, 5.4), xlim=(0, 100), ylim=(0, 43))
    # fila superior
    textos = [
        (f"{ID['nodos']} nodos hoja\nPM2,5 y PM10,\ntemperatura\ny humedad\nPanel solar y batería\n(14 días sin sol)\nEnvío por LoRa", E.CLARO, 19),
        (f"{ID['gateways']} gateways\n(1 por cada 10 nodos)\nCorrección de humedad,\ntemperatura y fracción\ngruesa\nAlmacenamiento local\nde 7 días", E.MEDIO, 21),
        ("Enlace a la nube\nRed celular con\nenlace satelital\nalterno", E.CLARO, 14),
        ("Nube\nModelo de corrección\ny gemelo digital\nTablero del índice\nde calidad del aire\ny salud (AQHI)", E.MEDIO, 19),
        ("15 comités de\ngestión del riesgo\nProtocolo de alerta\ny decisiones\ndocumentadas", E.CLARO, 15),
    ]
    x = 1.0; gap = 2.5; pos = []
    for t, col, w in textos:
        E.caja(ax, x, 22, w, 18, t, relleno=col, fs=8.0)
        pos.append((x, w)); x += w + gap
    for (x0, w0), (x1, w1) in zip(pos[:-1], pos[1:]):
        E.flecha(ax, (x0 + w0 + 0.45, 31), (x1 - 0.45, 31))
    # referencias
    E.caja(ax, 1, 12.4, 42.5, 6.0, "3 monitores gravimétricos de referencia\n(uno por departamento) colocalizados\ncon los nodos para medir el error", relleno=E.GRIS, fs=8.0)
    E.flecha(ax, (10, 19.0), (10, 21.6), ls="--")
    E.flecha(ax, (33, 19.0), (33, 21.6), ls="--")
    # tramos
    total = 24
    x0 = 1; ancho = 98
    colores = [E.CLARO, E.MEDIO, E.CLARO]
    for t, col in zip(T, colores):
        w = ancho * (t["m_fin"] - t["m_ini"] + 1) / total
        txt = f"Tramo {t['id']} (meses {t['m_ini']} a {t['m_fin']})\n{t['nodos']} nodos y {t['gateways']} gateways\nCompuerta {t['compuerta']}, mes {t['mes_compuerta']}"
        E.caja(ax, x0 + 0.3, 1.5, w - 0.9, 7.5, txt, relleno=col, fs=8.0)
        x0 += w
    ax.text(1, 9.8, "Despliegue condicionado: cada compuerta libera la compra del tramo siguiente", fontsize=8.6, color=E.TINTA, fontweight="bold")
    E.guardar(fig, "cX2_f01")

if __name__ == "__main__":
    main(); print("figura cX2_f01 generada")
