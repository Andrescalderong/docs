# -*- coding: utf-8 -*-
"""Figuras de la sección 13 del Anexo 2: c13_f01 (alternativas), c13_f02 (escalera TRL) y c13_f03 (arquitectura).
Cifras: puntajes y escenarios de RAIZ/maestro/alternativas.py; TRL, meses y cantidades de A2/v2/m2.py y de la especificación."""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/scripts")
from _comun import *
sys.path.insert(0, RAIZ + "/maestro")
import alternativas as A


# ============================================================ c13_f01
def f01():
    base = A.BASE
    # rango con perturbaciones de ±10 % relativo en cada uno de los 14 pesos, uno a la vez (28 escenarios)
    esc = []
    for rel in (-0.10, 0.10):
        for i in range(len(A.CRIT)):
            esc.append(A.escenario("x", [i], rel)[2])
    esc = np.array(esc)
    lo, hi = esc.min(0), esc.max(0)
    assert int(np.argmax(base)) == 3 and all(esc[k].argmax() == 3 for k in range(len(esc)))
    nombres = {0: "Statu quo", 1: "Estaciones fijas\nde referencia", 2: "Calibración centralizada\nen la nube",
               3: "Red híbrida por tramos\ncon custodia distribuida"}
    orden = [3, 2, 0, 1]

    L = Lienzo(10, 5.4, h1="La red híbrida por tramos obtiene el mayor puntaje entre cuatro alternativas",
               h2="Puntaje ponderado en escala de 1 a 9; marca negra: rango con ±10 % relativo en cada peso, uno a la vez")
    ax = eje_en_unidades(L, 32, 9.5, 97, L.top - 1)
    estilo_eje(ax)
    y = np.arange(4)
    for k, a in enumerate(orden):
        gan = a == 3
        ax.barh(k, base[a], height=0.56, color=AZUL if gan else CLARO, edgecolor=T, linewidth=1.2, zorder=3,
                hatch=None if gan else ("///" if a == 2 else ("..." if a == 0 else "\\\\\\")))
    # el hatch usa el color de borde (TINTA); se aclara con un segundo parche liso bajo la etiqueta
    for p in ax.patches:
        p.set_hatch(None)
    # segundo canal: trama distinta por alternativa no elegida, en AZUL y fuera del borde
    for k, a in enumerate(orden):
        if a == 3:
            continue
        ax.barh(k, base[a], height=0.56, color="none", edgecolor=AZUL, linewidth=0,
                hatch={2: "///", 0: "...", 1: "xxx"}[a], zorder=3.5)
        ax.barh(k, base[a], height=0.56, color="none", edgecolor=T, linewidth=1.2, zorder=3.6)
    for k, a in enumerate(orden):
        ax.plot([lo[a], lo[a]], [k - 0.2, k + 0.2], color=T, lw=2.6, solid_capstyle="butt", zorder=6)
        ax.plot([hi[a], hi[a]], [k - 0.2, k + 0.2], color=T, lw=2.6, solid_capstyle="butt", zorder=6)
        ax.plot([lo[a], hi[a]], [k, k], color=T, lw=2.6, solid_capstyle="butt", zorder=6)
        ax.annotate(num(base[a], 3), xy=(max(hi[a], base[a]), k), xytext=(9, 9), textcoords="offset points", ha="left", va="center",
                    fontsize=FS + 1, fontweight="bold", color=T)
        ax.annotate("rango %s a %s" % (num(lo[a], 2), num(hi[a], 2)), xy=(max(hi[a], base[a]), k), xytext=(9, -10),
                    textcoords="offset points", ha="left", va="center", fontsize=FS, color=T)
    ax.set_yticks(y)
    ax.set_yticklabels([nombres[a] for a in orden], fontsize=FS, color=T, linespacing=1.15)
    for lab, a in zip(ax.get_yticklabels(), orden):
        if a == 3:
            lab.set_fontweight("bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 9)
    ax.set_xticks(range(0, 10))
    ax.set_ylim(3.55, -0.55)
    ax.set_xlabel("Puntaje ponderado (escala de 1 a 9)", fontsize=FS, color=T, labelpad=6)
    ax.grid(axis="x", color=MEDIO, alpha=0.25, linestyle="--", linewidth=0.7)
    ax.grid(axis="y", visible=False)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    L.guardar("c13_f01")
    return dict(base=base, lo=lo, hi=hi)


# ============================================================ c13_f02
def f02():
    L = Lienzo(10, 7.4, h1="El TRL sube de 4 a 8 en 24 meses con verificaciones en los meses 10, 12, 19 y 23",
               h2="Nivel de madurez tecnológica (TRL) por mes del proyecto, meses 0 a 24; en cada peldaño, la evidencia de verificación")
    ax = eje_en_unidades(L, 11, 10.5, 97, L.top - 0.5)
    estilo_eje(ax)
    meses = [0, 10, 12, 19, 23, 24]
    trl = [4, 5, 6, 7, 8, 8]
    ax.fill_between(meses, 3.2, trl, step="post", color=CLARO, zorder=1, linewidth=0)
    ax.step(meses, trl, where="post", color=T, lw=2.8, zorder=4, solid_joinstyle="miter")
    ax.set_xlim(0, 24)
    ax.set_ylim(3.2, 9.05)
    ax.set_yticks([4, 5, 6, 7, 8])
    ax.set_yticklabels(["TRL %d" % k for k in (4, 5, 6, 7, 8)], fontsize=FS, fontweight="bold", color=T)
    ax.set_xticks(meses)
    ax.set_xticklabels([str(m) for m in meses], fontsize=FS, fontweight="bold", color=T)
    ax.set_xlabel("Mes del proyecto (cierre en el mes 24)", fontsize=FS, color=T, labelpad=6)
    ax.grid(axis="y", color=MEDIO, alpha=0.25, linestyle="--", linewidth=0.7)
    ax.set_axisbelow(True)
    # líneas de caída a los meses de verificación
    for m, lv in ((10, 5), (12, 6), (19, 7), (23, 8)):
        ax.plot([m, m], [3.2, lv], color=T, lw=1.0, ls=(0, (2, 3)), zorder=2)
    # marcadores: círculo en el inicio, rombo en cada verificación
    ax.plot(0, 4, marker="o", ms=11, mfc=BLANCO, mec=T, mew=2, zorder=6, ls="none", color=T, clip_on=False)
    for m, lv in ((10, 5), (12, 6), (19, 7), (23, 8)):
        ax.plot(m, lv, marker="D", ms=11, mfc=AZUL, mec=T, mew=2, zorder=6, ls="none", color=T, clip_on=False)
    # anillo del piso TRL 7
    ax.plot(19, 7, marker="o", ms=24, mfc="none", mec=T, mew=2, zorder=6, ls="none", color=T, clip_on=False)
    filas = [
        (4, "TRL 4 · mes 0", "Componentes validados en laboratorio", 9.6),
        (5, "TRL 5 · mes 10", "Colocalización del tramo 1 terminada", 11.6),
        (6, "TRL 6 · mes 12", "Modelo validado en el piloto (compuerta C1)", 18.6),
        (7, "TRL 7 · mes 19", "Sistema completo de 100 nodos y 10 gateways en operación", 22.6),
        (8, "TRL 8 · mes 23", "Ensayo independiente y evaluación externa; cierre en el mes 24", 23.8),
    ]
    xin = 0.35
    alto_eje = (L.top - 0.5) - 10.5
    u_por_nivel = alto_eje / (9.05 - 3.2)
    lh_dat = L.alto_linea(FS) / u_por_nivel
    for lv, t1, t2, xmax in filas:
        w_u = (xmax - xin) / 24 * (97 - 11)
        lines = L.envolver(t2, w_u - 1.0, FS)
        ybase = lv + 0.10
        n = len(lines) + 1
        ax.text(xin, ybase + lh_dat * (n - 0.5), t1, ha="left", va="center", fontsize=FS, fontweight="bold", color=T, zorder=7)
        for i, ln in enumerate(lines):
            ax.text(xin, ybase + lh_dat * (len(lines) - i - 0.5), ln, ha="left", va="center", fontsize=FS, color=T, zorder=7)
    # indicación del piso TRL 7
    ax.text(19.35, 6.55, "Piso TRL 7\nal mes 19", ha="left", va="center", fontsize=FS, fontweight="bold", color=T, zorder=7, linespacing=1.15)
    L.guardar("c13_f02")


# ============================================================ c13_f03
def f03():
    L = Lienzo(10, 8.3, h1="La corrección se aplica en 10 gateways y las mediciones llegan a 15 comités",
               h2="Arquitectura de la red completa (100 nodos, 10 gateways y 15 comités) y laboratorio de modelación, operativos desde el mes 19 hasta el cierre en el mes 24")
    x0, wt, wd = 1.0, 21.0, 44.0          # celda de título y celda de detalle
    h = 11.6
    gap = 5.4
    ytop = L.top - 1.0
    bandas = [
        ("100 nodos hoja", "PM2,5 y PM10, temperatura y humedad; panel solar y batería de 14 días", CLARO),
        ("10 gateways (borde)", "Modelo de corrección; almacenamiento local de 7 días; enlace celular con respaldo satelital", MEDIO),
        ("Nube", "Gemelo digital, base de datos, tablero del índice local y protocolo de alerta", AZUL),
        ("15 comités de gestión del riesgo", "12 municipales y 3 departamentales; reciben alertas con mediciones de error conocido", CAJA),
    ]
    ys = []
    for i, (tit, det, col) in enumerate(bandas):
        y = ytop - h - i * (h + gap)
        ys.append(y)
        L.caja(x0, y, wt, h, titulo=tit, fc=col, lw=1.4)
        L.caja(x0 + wt, y, wd, h, cuerpo=det, fc=BLANCO, lw=1.4, ha="left")
    etiquetas = ["LoRa", "red celular o enlace satelital", "tablero y alertas"]
    for i, e in enumerate(etiquetas):
        ya, yb = ys[i], ys[i + 1] + h
        xc = x0 + wt / 2
        L.flecha((xc, ya - 0.3), (xc, yb + 0.3), lw=1.8)
        L.t(xc + 2.2, (ya + yb) / 2, e, ha="left", va="center")
    # columna derecha: monitores de referencia y tramos
    xm, wm = 71.0, 28.0
    xr = x0 + wt + wd
    hm = h + gap
    L.caja(xm, ys[0] + h - hm, wm, hm, titulo="3 monitores gravimétricos de referencia",
           cuerpo="uno por departamento, colocalizados con los nodos", fc=GRIS, lw=1.4, ls=(0, (5, 3)), pad=1.2)
    L.flecha((xm - 0.3, ys[0] + h / 2), (xr + 0.5, ys[0] + h / 2), ls=(0, (5, 3)), lw=1.8)
    tr = m2.M0.TRAMOS
    cuerpo = "\n\n".join("Tramo %d, meses %d a %d\n%d nodos y %d gateways" % (t["id"], t["m_ini"], t["m_fin"], t["nodos"], t["gateways"]) for t in tr)
    assert sum(t["nodos"] for t in tr) == 100 and sum(t["gateways"] for t in tr) == 10
    yb = ys[2]
    ytop_r = ys[1] + h
    L.caja(xm, yb, wm, ytop_r - yb, titulo="Instalación por tramos", cuerpo=cuerpo, fc=BLANCO, lw=1.4, pad=1.2, va="top")
    # laboratorio de modelación: recibe de la nube las mediciones corregidas y devuelve escenarios al tablero
    hl = 19.0
    yl = ys[3] + h - hl
    L.caja(xm, yl, wm, hl, titulo="Laboratorio de modelación",
           cuerpo="Gemelo predictivo de demolición con servidor, 4 estaciones, dron y 2 monitores portátiles", fc=CLARO, lw=1.4, pad=1.2)
    ym = ys[2] + h / 2
    xa, xb = 69.4, 67.4
    # datos de la nube al laboratorio (arriba y a la derecha) y escenarios del laboratorio a la nube (abajo y a la izquierda)
    L.camino([(xr + 0.3, ym + 2.2), (xa, ym + 2.2), (xa, yl + hl * 0.78), (xm - 0.3, yl + hl * 0.78)], lw=1.6)
    L.camino([(xm - 0.3, yl + hl * 0.30), (xb, yl + hl * 0.30), (xb, ym - 2.2), (xr + 0.3, ym - 2.2)], lw=1.6, ls=(0, (5, 3)))
    L.guardar("c13_f03")


if __name__ == "__main__":
    f01(); f02(); f03()
