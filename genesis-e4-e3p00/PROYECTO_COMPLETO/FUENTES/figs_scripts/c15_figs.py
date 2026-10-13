# -*- coding: utf-8 -*-
"""Figuras del capítulo 15 (prefijo 15): c15_f01 (modelo de transferencia) y c15_f02 (ruta de comercialización).
Datos: sección 4.4-MDR.10 (componentes, hitos de transferencia y condiciones de recepción, cláusula de apertura), ficha maestra
(hitos de software y compuerta C3) e informe de vigilancia tecnológica (consulta de la SIC). Sin semilla ni corpus."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import estilo as E
from matplotlib.patches import FancyBboxPatch, Rectangle


def caja2(ax, x, y, w, h, texto, relleno=E.CAJA, fs=9, trama=None, borde=E.TINTA, lw=1.2, ls="-", bold=False):
    """Caja con texto legible; si hay trama, el fondo del texto es sólido."""
    if trama:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=E.AZUL, lw=0, hatch=trama))
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc="none", ec=borde, lw=lw, ls=ls))
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, linespacing=1.25,
                fontweight="bold" if bold else "normal", bbox=dict(boxstyle="round,pad=0.3", fc=relleno, ec="none"))
    else:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=borde, lw=lw, ls=ls))
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, linespacing=1.25,
                fontweight="bold" if bold else "normal")


def f01():
    fig, ax = E.lienzo_libre(h1="Cada hito transfiere un componente distinto y exige una condición de recepción",
                             h2="Componentes y hitos de transferencia en los meses 6, 12, 18 y 24; custodio POR_DEFINIR con ICAR",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 72))
    xs = [34, 50, 66, 82]
    w = 15
    heads = ["Hito 0\nmes 6", "Hito 1\nmes 12", "Hito 2\nmes 18", "Hito 3\nmes 24"]
    conds = ["Acuerdos firmados\nantes del segundo\nlote de nodos", "SC-1 verificado y\ncustodio con\nICAR de 2 o más",
             "Partida en el plan\noperativo y personal\ndesignado", "Competencia jurídica\ny primer pago\ndel servicio"]
    for x, h, c in zip(xs, heads, conds):
        caja2(ax, x, 60, w, 8, h, relleno=E.MEDIO, fs=9.5, bold=True)
        ax.text(x + w / 2, 58.6, c, ha="center", va="top", fontsize=8, color=E.TINTA, linespacing=1.2)
    filas = ["Gobernanza\ny acuerdos", "Protocolo de calibración\ny series de datos", "Nodos adicionales\ny repuestos", "Tablero\ny alertas", "Gemelo digital\ny operación"]
    y0 = 44
    alto = 7.0
    paso = 8.0
    # celdas: (fila, columna) -> (texto, tipo)
    celdas = {
        (0, 0): ("Acuerdo marco,\ncláusula de\napertura", "t"),
        (1, 1): ("Protocolo y\nseries de datos", "t"),
        (1, 3): ("Operación con\ncustodio", "o"),
        (2, 2): ("Nodos\nadicionales", "t"),
        (2, 3): ("Operación con\ncustodio", "o"),
        (3, 2): ("Tablero", "t"),
        (3, 3): ("Operación con\ncustodio", "o"),
        (4, 3): ("Gemelo digital\ny operación\n(inferido)", "i"),
    }
    for r, nombre in enumerate(filas):
        y = y0 - r * paso
        ax.text(2, y + alto / 2, nombre, ha="left", va="center", fontsize=9.5, color=E.TINTA, linespacing=1.2)
        for c, x in enumerate(xs):
            ax.add_patch(Rectangle((x, y), w, alto, fc="none", ec=E.MEDIO, lw=0.7, ls=(0, (3, 3))))
            if (r, c) in celdas:
                t, tipo = celdas[(r, c)]
                if tipo == "t":
                    caja2(ax, x + 0.4, y + 0.3, w - 0.8, alto - 0.6, t, relleno=E.MEDIO, fs=8.5)
                elif tipo == "o":
                    caja2(ax, x + 0.4, y + 0.3, w - 0.8, alto - 0.6, t, relleno=E.CLARO, fs=8.5, trama="///")
                else:
                    caja2(ax, x + 0.4, y + 0.3, w - 0.8, alto - 0.6, t, relleno=E.MEDIO, fs=8.5, ls=(0, (4, 2)))
    # leyenda y custodio
    yl = 1.8
    caja2(ax, 2, yl, 4, 3, "", relleno=E.MEDIO, fs=8)
    ax.text(7.5, yl + 1.5, "Transferencia en el hito", ha="left", va="center", fontsize=8.5, color=E.TINTA)
    caja2(ax, 30, yl, 4, 3, "", relleno=E.CLARO, fs=8, trama="///")
    ax.text(35.5, yl + 1.5, "Operación continua con custodio", ha="left", va="center", fontsize=8.5, color=E.TINTA)
    caja2(ax, 66, yl, 4, 3, "", relleno=E.MEDIO, fs=8, ls=(0, (4, 2)))
    ax.text(71.5, yl + 1.5, "Asignación inferida", ha="left", va="center", fontsize=8.5, color=E.TINTA)
    ax.text(2, 8.2, "Custodio asignado en todos los componentes: POR_DEFINIR con ICAR (NO_CALCULABLE sin evidencia en seis dimensiones).",
            ha="left", va="center", fontsize=8.5, color=E.TINTA)
    E.guardar(fig, "c15_f01")


def f02():
    fig, ax = E.lienzo_libre(h1="Ninguna licencia se decide antes de consultar la libertad de operación",
                             h2="Secuencia de decisiones de licenciamiento y comercialización, meses 1 a 24",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    caja2(ax, 2, 48, 27, 11, "Consulta de 10 expedientes PCT\nante la SIC (línea S02)\nPlazos abiertos: 10/12/2026,\n28/04/2027 y 28/08/2027", relleno=E.CLARO, fs=8.5)
    caja2(ax, 2, 32, 27, 9, "Acuerdo de titularidad\nIES y empresa tecnológica\n(antes del mes 6)", relleno=E.CLARO, fs=8.5)
    caja2(ax, 2, 15, 27, 11, "Registro de software ante la\nDNDA: solicitud al mes 17;\nregistro vigente al mes 24", relleno=E.CLARO, fs=8.5)
    E.flecha(ax, (15.5, 47.5), (15.5, 41.8))
    E.flecha(ax, (15.5, 31.5), (15.5, 26.3))
    caja2(ax, 38, 30, 21, 16, "Decisión de licencia\nCompuerta C3, mes 24\nÓrgano de gobierno\nde la alianza", relleno=E.MEDIO, fs=9, bold=True)
    E.flecha(ax, (30, 20.5), (37.5, 33.5))
    E.flecha(ax, (30, 36.5), (37.5, 37.5))
    E.flecha(ax, (30, 53.5), (37.5, 42.5))
    ax.text(79, 65.2, "Opciones de licenciamiento", ha="center", va="center", fontsize=9.5, fontweight="bold", color=E.TINTA)
    caja2(ax, 66, 51, 32, 10, "A. Licencia abierta\nRespaldo si se activa el disparador\nde la cláusula de apertura", relleno=E.CLARO, fs=8.5, trama="///")
    caja2(ax, 66, 37, 32, 10, "B. Licencia con condiciones\nRecomendación preliminar\n(PROPUESTO)", relleno=E.MEDIO, fs=8.5, bold=True)
    caja2(ax, 66, 24, 32, 9, "C. Servicio sin cesión del código", relleno=E.CAJA, fs=8.5)
    caja2(ax, 66, 11, 32, 9, "D. Reserva temporal\nHasta concluir la consulta", relleno=E.CAJA, fs=8.5)
    E.flecha(ax, (59.8, 42), (65.5, 56))
    E.flecha(ax, (59.8, 40), (65.5, 42))
    E.flecha(ax, (59.8, 36), (65.5, 28.5))
    E.flecha(ax, (59.8, 33), (65.5, 15.5))
    caja2(ax, 34, 2.5, 29, 11.5, "Empresa derivada solo con cuatro\ncondiciones: titularidad, demanda,\ncustodia y decisión en C3", relleno=E.CAJA, fs=8, ls=(0, (4, 2)))
    E.flecha(ax, (48.5, 29.5), (48.5, 14.6), ls="--")
    E.guardar(fig, "c15_f02")


if __name__ == "__main__":
    f01(); f02()
    print("ok")
