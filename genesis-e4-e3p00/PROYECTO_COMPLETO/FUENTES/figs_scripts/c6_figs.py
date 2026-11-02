# -*- coding: utf-8 -*-
"""Capítulo 6 (Metodología): figuras c6_f01 a c6_f04. Datos: FICHA_MAESTRA §2, §4 y §6 (tramos, compuertas, red CPM, umbrales).
Uso: python3 c6_figs.py   -> figs/out/c6_f01..f04 (.png y .svg, fondo transparente)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import estilo as E
from matplotlib.patches import Polygon, FancyBboxPatch, Rectangle

T = E.TINTA
XL = (-3, 103)

def rombo(ax, cx, cy, w, h, texto, relleno=E.BLANCO, fs=9, bold=True):
    ax.add_patch(Polygon([(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)], closed=True, fc=relleno, ec=T, lw=1.3))
    if texto:
        ax.text(cx, cy, texto, ha="center", va="center", fontsize=fs, color=T, fontweight="bold" if bold else "normal")

def caja2(ax, x, y, w, h, titulo, cuerpo=None, relleno=E.CAJA, fs_t=9.5, fs_c=8.3, hatch=None, grosor=1.2):
    """Caja con título arriba y cuerpo abajo; la trama (segundo canal) se dibuja aparte para no restar legibilidad al texto."""
    if hatch:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=E.AZUL, lw=0, hatch=hatch))
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc="none", ec=T, lw=grosor))
    else:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=T, lw=grosor))
    if cuerpo:
        ax.text(x + w / 2, y + h - 1.2, titulo, ha="center", va="top", fontsize=fs_t, color=T, fontweight="bold", linespacing=1.2)
        ax.text(x + w / 2, y + 1.0, cuerpo, ha="center", va="bottom", fontsize=fs_c, color=T, linespacing=1.25)
    else:
        ax.text(x + w / 2, y + h / 2, titulo, ha="center", va="center", fontsize=fs_t, color=T, fontweight="bold", linespacing=1.2)

def barra(ax, x, y, w, h, relleno, hatch=None):
    if hatch:
        ax.add_patch(Rectangle((x, y), w, h, fc=relleno, ec=E.AZUL, lw=0, hatch=hatch))
        ax.add_patch(Rectangle((x, y), w, h, fc="none", ec=T, lw=1.2))
    else:
        ax.add_patch(Rectangle((x, y), w, h, fc=relleno, ec=T, lw=1.2))

def linea(ax, xs, ys, ls="-", lw=1.3):
    ax.plot(xs, ys, color=T, lw=lw, ls=ls, solid_capstyle="butt")

# ------------------------------------------------------------------ F6.1
def f01():
    fig, ax = E.lienzo_libre(h1="Cinco fases en tres tramos: dos compuertas condicionan cada compra",
                             h2="Fases construir-medir-aprender y actividades de la red CPM (semanas 0 a 104); tramos y compuertas por mes",
                             figsize=(10, 7), xlim=(-3, 106), ylim=(0, 72))
    fases = [
        ("Fase 1\nDiseñar y\nplanificar", "Semanas 0 a 14\nA0.1 · A1.1 · A2.1", E.CLARO, None),
        ("Fase 2\nConstruir", "Semanas 14 a 24\nA1.2 · A2.2\nA3.1 (desde sem. 12)", E.CLARO, None),
        ("Fase 3\nMedir", "Semanas 24 a 50\nA1.3 · A1.4\nC1 (medición)", E.MEDIO, None),
        ("Fase 4\nAprender y\ndecidir", "C1: sem. 48 a 50\nC2: sem. 68 a 70\npivotar o perseverar", E.AZUL, None),
        ("Fase 5\nEscalar", "Semanas 50 a 104\nA2.3 · A1.5 · A3.2 · C2\nA2.4 · A3.3 · A1.6 · A3.4", E.MEDIO, "///"),
    ]
    w, g, y0, h = 18.0, 2.5, 40, 22
    xs = [i * (w + g) for i in range(5)]
    for (t, c, col, ht), x in zip(fases, xs):
        caja2(ax, x, y0, w, h, t, c, relleno=col, hatch=ht, fs_t=9.5, fs_c=7.9)
    for i in range(4):
        E.flecha(ax, (xs[i] + w + 0.5, y0 + h / 2), (xs[i + 1] - 0.5, y0 + h / 2), lw=1.4)
    # pivotar: fase 4 -> fase 2 (arco por arriba)
    E.flecha(ax, (xs[3] + w / 2, y0 + h + 0.8), (xs[1] + w / 2, y0 + h + 0.8), ls="--", rad=0.25, lw=1.2)
    ax.text((xs[1] + xs[3] + w) / 2, y0 + h + 6.6, "pivotar: volver a construir o a medir", ha="center", fontsize=8.2, color=T)
    # tramos
    ax.text(0, 35.0, "Despliegue condicionado por tramos (meses 1 a 24)", fontsize=9.5, fontweight="bold", color=T, ha="left")
    ytr, htr = 19.5, 12.5
    tr = [("Tramo 1: piloto de contraste", "30 nodos · 3 gateways\nmeses 1 a 12", 0, 50, E.AZUL, None),
          ("Tramo 2: ampliación", "40 nodos · 4 gateways\nmeses 13 a 17", 50, 70.83, E.MEDIO, "///"),
          ("Tramo 3: consolidación", "30 nodos · 3 gateways\nmeses 18 a 24", 70.83, 100, E.CLARO, "...")]
    for t, c, a, b, col, ht in tr:
        barra(ax, a, ytr, b - a, htr, col, ht)
        # fondo del texto para legibilidad sobre trama
        ax.text((a + b) / 2, ytr + htr - 1.3, t, ha="center", va="top", fontsize=8.4, fontweight="bold", color=T,
                bbox=dict(boxstyle="round,pad=0.15", fc=col, ec="none", alpha=1.0))
        ax.text((a + b) / 2, ytr + 1.2, c, ha="center", va="bottom", fontsize=7.9, color=T, linespacing=1.2,
                bbox=dict(boxstyle="round,pad=0.15", fc=col, ec="none", alpha=1.0))
    for x, c1, c2 in ((50, "C1", "mes 12"), (70.83, "C2", "mes 17"), (100, "C3", "mes 24")):
        rombo(ax, x, ytr - 4.6, 7.6, 7.0, c1, fs=8.5)
        ax.text(x, ytr - 9.6, c2, ha="center", fontsize=7.8, color=T)
    ax.text(51.6, ytr - 13.4, "libera compra:\n48 nodos y 4 gateways", ha="left", fontsize=7.8, color=T, linespacing=1.2)
    ax.text(72.4, ytr - 13.4, "libera compra:\n36 nodos y 3 gateways", ha="left", fontsize=7.8, color=T, linespacing=1.2)
    ax.text(0, ytr - 13.4, "Fases 1 a 4: primer ciclo completo\n(compra del tramo 1: 36 nodos y 4 gateways)", ha="left", fontsize=7.8, color=T, linespacing=1.2)
    ax.text(0, 0.8, "Flecha continua: perseverar y avanzar. Flecha discontinua: pivotar. Rombo: compuerta que libera la compra del tramo siguiente.", fontsize=7.8, color=T, ha="left")
    E.guardar(fig, "c6_f01")

# ------------------------------------------------------------------ F6.2
def f02():
    fig, ax = E.lienzo_libre(h1="Cada tramo repite construir, medir y aprender y termina en una compuerta",
                             h2="Ciclo construir-medir-aprender por tramo; nodos y gateways acumulados; TRL propuesto (inicial 4, final 7)",
                             figsize=(10, 7), xlim=XL, ylim=(0, 72))
    filas = [
        (58, "Tramo 1", "meses 1 a 12", ("A1.2 · A2.2", "A1.3 · A1.4", "C1 (mes 12)"), "C1", "30 nodos · 3 gateways", "TRL 4 a 5"),
        (37, "Tramo 2", "meses 13 a 17", ("A2.3", "A1.5", "C2 (mes 17)"), "C2", "70 nodos · 7 gateways", "TRL 5 a 6"),
        (16, "Tramo 3", "meses 18 a 24", ("A2.4", "A1.6", "A3.4 (cierre)"), "C3", "100 nodos · 10 gateways", "TRL 6 a 7"),
    ]
    bx = [14, 31, 48]; bw = 13; bh = 8
    tit = [("Construir", E.CLARO, None), ("Medir", E.MEDIO, "///"), ("Aprender", E.AZUL, None)]
    compras = {"C1": "perseverar: libera la compra\nde 48 nodos y 4 gateways", "C2": "perseverar: libera la compra\nde 36 nodos y 3 gateways"}
    for k, (cy, nom, meses, acts, gate, acum, trl) in enumerate(filas):
        ax.text(0, cy + 1.2, nom, ha="left", va="center", fontsize=10.5, fontweight="bold", color=T)
        ax.text(0, cy - 2.2, meses, ha="left", va="center", fontsize=8.2, color=T)
        for i, (nm, col, ht) in enumerate(tit):
            caja2(ax, bx[i], cy - bh / 2, bw, bh, nm, relleno=col, hatch=ht, fs_t=9.5)
            ax.text(bx[i] + bw / 2, cy - bh / 2 - 1.4, acts[i], ha="center", va="top", fontsize=8.0, color=T)
        E.flecha(ax, (bx[0] + bw + 0.6, cy), (bx[1] - 0.6, cy), lw=1.4)
        E.flecha(ax, (bx[1] + bw + 0.6, cy), (bx[2] - 0.6, cy), lw=1.4)
        # pivotar: de aprender a construir (arco por arriba)
        E.flecha(ax, (bx[2] + bw / 2, cy + bh / 2 + 0.5), (bx[0] + bw / 2, cy + bh / 2 + 0.5), ls="--", rad=0.2, lw=1.1)
        ax.text((bx[0] + bx[2] + bw) / 2, cy + bh / 2 + 4.4, "pivotar", ha="center", fontsize=7.8, color=T)
        # compuerta
        E.flecha(ax, (bx[2] + bw + 0.6, cy), (66.3, cy), lw=1.4)
        rombo(ax, 69.5, cy, 7.0, 8.0, gate, fs=9)
        ax.text(78, cy + 3.2, acum, ha="left", va="center", fontsize=8.8, fontweight="bold", color=T)
        ax.text(78, cy - 0.8, trl + " (PROPUESTO)", ha="left", va="center", fontsize=8.3, color=T)
        if gate in compras:
            # camino hacia el siguiente tramo
            ys = cy - 9.5
            linea(ax, [69.5, 69.5, 11.5, 11.5], [cy - 4.2, ys, ys, cy - 21])
            E.flecha(ax, (11.5, cy - 21), (13.4, cy - 21), lw=1.3)
            ax.text(71.5, cy - 8.2, compras[gate], ha="left", va="top", fontsize=7.8, color=T, linespacing=1.2)
        else:
            ax.text(78, cy - 4.8, "cierra y transfiere", ha="left", va="center", fontsize=8.3, color=T)
    ax.text(0, 1.0, "Nodos y gateways acumulados según la ficha maestra; los niveles de madurez intermedios (TRL 5 y 6) son una propuesta de este capítulo.", fontsize=7.8, color=T)
    E.guardar(fig, "c6_f02")

# ------------------------------------------------------------------ F6.3
def f03():
    fig, ax = E.lienzo_libre(h1="Los aprendizajes pasan de la bitácora semanal a la decisión en compuerta",
                             h2="Flujo de captura durante 104 semanas: 104 cierres de bitácora, 52 retrospectivas y 24 sesiones de serendipia",
                             figsize=(10, 7), xlim=XL, ylim=(0, 72))
    ax.text(0, 64, "Fuentes de aprendizaje", fontsize=9.5, fontweight="bold", color=T)
    src = [("Colocalización y\ndatos de campo", 51), ("Comités y\ncustodios", 39), ("Exploración libre\n(20 % del tiempo)", 27)]
    for t, y in src:
        caja2(ax, 0, y, 22, 9, t, relleno=E.CAJA, fs_t=8.6)
    caja2(ax, 30, 36, 20, 19, "Bitácora semanal", "Cierre cada semana\n104 cierres\nplantilla de 10 campos", relleno=E.CLARO, fs_t=9.5, fs_c=8.0)
    caja2(ax, 57, 36, 19, 19, "Retrospectiva\nquincenal", "52 sesiones\nacciones y\nresponsables", relleno=E.MEDIO, fs_t=9.5, fs_c=8.0)
    caja2(ax, 81, 36, 19, 19, "Registro de\ndecisiones", "Qué se ajusta,\nquién y cuándo", relleno=E.CLARO, fs_t=9.5, fs_c=8.0)
    for y in (55.5, 43.5, 31.5):
        E.flecha(ax, (22.6, y), (29.5, 45.5), lw=1.2)
    E.flecha(ax, (50.6, 45.5), (56.4, 45.5), lw=1.4)
    E.flecha(ax, (76.6, 45.5), (80.4, 45.5), lw=1.4)
    caja2(ax, 30, 8, 20, 19, "Serendipia\nestructurada", "Sesión mensual\n24 sesiones\nclasificar hallazgos", relleno=E.AZUL, fs_t=9.2, fs_c=8.0)
    E.flecha(ax, (40, 35.4), (40, 27.8), lw=1.2)
    E.flecha(ax, (50.6, 24.0), (62, 35.4), lw=1.2, ls="--", rad=-0.1)
    ax.text(51.0, 17.5, "hallazgos con\nevidencia", fontsize=7.8, color=T, ha="left", linespacing=1.2)
    E.flecha(ax, (29.4, 20.0), (11, 26.4), lw=1.2, ls="--", rad=0.15)
    ax.text(12.0, 16.5, "temas por\nexplorar", fontsize=7.8, color=T, ha="left", linespacing=1.2)
    caja2(ax, 64, 8, 36, 19, "Revisión en compuerta",
          "Antes de C1 (sem. 44 a 48), de C2\n(sem. 64 a 68) y del cierre (sem. 94 a 98),\nlas decisiones se leen frente a los\numbrales y a los criterios de decisión",
          relleno=E.BLANCO, fs_t=9.2, fs_c=7.9)
    E.flecha(ax, (91, 35.4), (84, 27.8), lw=1.4)
    ax.text(0, 1.0, "Cada ajuste aprobado vuelve a las fuentes como nueva observación. Flecha discontinua: aporte secundario de la serendipia.", fontsize=7.8, color=T)
    E.guardar(fig, "c6_f03")

# ------------------------------------------------------------------ F6.4
def f04():
    fig, ax = E.lienzo_libre(h1="Las compuertas liberan la compra siguiente solo si se cumplen todos los criterios",
                             h2="Criterios de pivotar o perseverar en C1 (mes 12) y C2 (mes 17) con los umbrales de la ficha maestra",
                             figsize=(10, 7), xlim=XL, ylim=(0, 72))
    ax.text(0, 65, "Compuerta C1 (semanas 48 a 50)", fontsize=10, fontweight="bold", color=T)
    caja2(ax, 0, 50, 47, 11, "Criterio técnico", "R² ≥ 0,70 y NRMSE ≤ 30 % frente a la referencia\n(departamento fuera de muestra y partición temporal)", relleno=E.CLARO, fs_t=8.8, fs_c=8.0)
    ax.text(23.5, 47.2, "y", ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    caja2(ax, 0, 36, 47, 9, "Criterio de uso institucional", "≥ 50 % de los comités del tramo 1 usa el tablero", relleno=E.CLARO, fs_t=8.8, fs_c=8.0)
    rombo(ax, 23.5, 28.5, 32, 8, "¿Se cumplen ambos?", fs=8.6)
    E.flecha(ax, (23.5, 35.4), (23.5, 32.6), lw=1.3)
    caja2(ax, 0, 8, 22, 13, "Perseverar", "Liberar compra del tramo 2:\n48 nodos y 4 gateways", relleno=E.AZUL, fs_t=9.2, fs_c=7.9)
    caja2(ax, 25, 8, 22, 13, "Pivotar", "Cambiar de modelo\no ajustar el uso;\nno liberar compra", relleno=E.MEDIO, hatch="///", fs_t=9.2, fs_c=7.9)
    E.flecha(ax, (12.5, 25.0), (11, 21.8), lw=1.3); ax.text(3.5, 23.0, "sí", fontsize=8.5, fontweight="bold", color=T)
    E.flecha(ax, (34.5, 25.0), (36, 21.8), lw=1.3); ax.text(40.0, 23.0, "no", fontsize=8.5, fontweight="bold", color=T)
    ax.text(54, 65, "Compuerta C2 (semanas 68 a 70)", fontsize=10, fontweight="bold", color=T)
    caja2(ax, 54, 53, 46, 9, "Criterio técnico en los tres departamentos", "R² ≥ 0,70 y NRMSE ≤ 30 % en Caldas,\nCundinamarca y Valle del Cauca", relleno=E.CLARO, fs_t=8.6, fs_c=7.9)
    caja2(ax, 54, 44.5, 46, 7, "Criterio de disponibilidad", "Disponibilidad mensual de nodos ≥ 90 %", relleno=E.CLARO, fs_t=8.6, fs_c=7.9)
    caja2(ax, 54, 36, 46, 7, "Criterio de custodia", "Convenios de custodia con partida", relleno=E.CLARO, fs_t=8.6, fs_c=7.9)
    rombo(ax, 77, 28.5, 32, 8, "¿Se cumplen todos?", fs=8.6)
    E.flecha(ax, (77, 35.4), (77, 32.7), lw=1.3)
    caja2(ax, 54, 8, 22, 13, "Perseverar", "Liberar compra del tramo 3:\n36 nodos y 3 gateways", relleno=E.AZUL, fs_t=9.2, fs_c=7.9)
    caja2(ax, 79, 8, 21, 13, "Pivotar", "Reforzar la custodia\no reducir el alcance", relleno=E.MEDIO, hatch="///", fs_t=9.2, fs_c=7.9)
    E.flecha(ax, (66, 25.0), (65, 21.8), lw=1.3); ax.text(57.5, 23.0, "sí", fontsize=8.5, fontweight="bold", color=T)
    E.flecha(ax, (88, 25.0), (89, 21.8), lw=1.3); ax.text(93.5, 23.0, "no", fontsize=8.5, fontweight="bold", color=T)
    ax.text(0, 3.2, "Lectura con intervalos: cumple con holgura si el límite inferior del intervalo de confianza del 95 % alcanza el umbral;", fontsize=7.8, color=T)
    ax.text(0, 0.4, "cumple sin holgura si solo lo alcanza la estimación puntual, y entonces se verifica en A1.5 (tramo 2) o en A1.6 (tramo 3).", fontsize=7.8, color=T)
    E.guardar(fig, "c6_f04")

if __name__ == "__main__":
    f01(); f02(); f03(); f04()
    print("ok")
