# -*- coding: utf-8 -*-
"""Figura F0.1: paleta y funciones de color de la plantilla visual (instrucción del usuario del 13-oct-2026)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
import estilo as E
from matplotlib.patches import Rectangle
fig, ax = E.lienzo_libre(h1="Seis colores cumplen seis funciones fijas en todas las figuras y tablas",
                         h2="Códigos hexadecimales y uso asignado en la plantilla visual del proyecto",
                         figsize=(10, 5.6), xlim=(0, 100), ylim=(0, 52))
filas = [
    (E.TINTA, "#2A3439", "Texto, estructura y máximo contraste", "Títulos, ejes, filetes de tabla, texto de cuerpo", E.BLANCO),
    (E.AZUL, "#6699CC", "Acento", "Categoría principal, punto más alto, filete bajo el encabezado de tabla", E.TINTA),
    (E.MEDIO, "#9EB9D4", "Serie secundaria", "Segunda serie de datos y líneas de apoyo", E.TINTA),
    (E.CLARO, "#B9D9EB", "Apoyo y baja prioridad", "Relleno del encabezado de tabla y categorías de menor prioridad", E.TINTA),
    (E.CAJA, "#F5F5F5 y #F7F7F7", "Rellenos neutros", "Cajas, filas alternas de tabla y fondos de anotación", E.TINTA),
    (E.MARFIL, "#FFFFFF y #FEFEFA", "Contraste limpio", "Texto sobre fondos oscuros y separación de elementos", E.TINTA),
]
y = 44.0
for color, hexa, rol, uso, tcol in filas:
    ax.add_patch(Rectangle((2, y - 3.2), 22, 6.4, facecolor=color, edgecolor=E.TINTA, linewidth=1.0))
    ax.text(13, y, hexa, ha="center", va="center", fontsize=9.6, fontweight="bold", color=tcol)
    ax.text(27, y + 1.3, rol, ha="left", va="center", fontsize=11, fontweight="bold", color=E.TINTA)
    ax.text(27, y - 1.9, uso, ha="left", va="center", fontsize=9.6, color=E.TINTA)
    y -= 7.4
E.guardar(fig, "cF0_f01")
