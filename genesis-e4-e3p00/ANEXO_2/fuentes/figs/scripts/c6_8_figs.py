# -*- coding: utf-8 -*-
"""Figuras del Anexo 2: c6_f01 (línea de tiempo de antecedentes 2012-2026), c6_f02 (dispersión TRL por IRL de los 41 documentos del
corpus, con la banda del proyecto de TRL 4 a 8) y c8_f01 (demanda territorial, proyecto, resultado y plan de desarrollo por departamento).
Datos: A2/v2/m2.py (nodos, consejos, tramos), tabla de TRL e IRL del informe de vigilancia tecnológica (work/informe.md, filas G-01 a G-42;
la misma lectura de la figura de la línea base) y años de las obras del banco cerrado de referencias (A2/refs/BANCO_REFERENCIAS.md).
Ejecución: python3 c6_8_figs.py  -> A2/figs/out/c6_f01.png, c6_f02.png, c8_f01.png"""
import os, sys, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _a2 as A
from _a2 import T, AZUL, MEDIO, CLARO, GRIS, CAJA, BLANCO, P, F_B
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INFORME = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/work/informe.md"
PUNTEADO = (0, (1.2, 2.6))
DISCONT = (0, (5, 3))


# ------------------------------------------------------------------ c6_f01
def c6_f01():
    H = 72
    fig, ax = A.lienzo("Los antecedentes de red y de calibración se concentran entre 2015 y 2026, después del marco metrológico de 2012 a 2021",
                       "Antecedentes por año de publicación o expedición, 2012 a 2026", H)
    X0, X1 = 22.0, 95.0
    xa = lambda yr: X0 + (yr - 2012) * (X1 - X0) / 14
    paso = (X1 - X0) / 14
    ya = 5.0                                # eje de años
    y3, y2, y1 = 18.5, 40.0, 60.0           # centros de los carriles
    # zona de 2015 a 2026 y cuadrícula anual
    zona_y0, zona_y1 = ya - 1.6, H - 0.5
    ax.add_patch(Rectangle((xa(2015) - paso / 2, zona_y0), xa(2026) - xa(2015) + paso, zona_y1 - zona_y0, fc=GRIS, ec="none", zorder=0))
    A.txt(ax, (xa(2015) + xa(2026)) / 2, H - 1.8, "2015 a 2026: antecedentes de red y de calibración", F_B, True, ha="center")
    for yr in range(2012, 2027):
        ax.plot([xa(yr)] * 2, [ya, y1 + 3], color=MEDIO, lw=0.7, alpha=0.5, ls=(0, (4, 3)), zorder=1)
        A.txt(ax, xa(yr), ya - 1.8, str(yr), F_B, ha="center")
    ax.plot([X0 - 3, X1 + 3], [ya, ya], color=T, lw=1.3, zorder=2)
    carriles = [(y1, "Marco normativo\ny de política", "s", CLARO), (y2, "Literatura\nmetrológica", "o", MEDIO), (y3, "Redes, diseños\ny casos", "^", AZUL)]
    for y, nom, m, c in carriles:
        ax.plot([X0 - 3, X1 + 3], [y, y], color=MEDIO, lw=2.0, zorder=1)
        A.lineas(ax, 1, y + 3.5, nom, F_B, True, ancho=19.0)
    # (año, carril, texto, lado, alineación) ; los años provienen del banco cerrado de referencias
    ev = [
        (2012, y1, "Ley 1523:\ngestión del riesgo", "u", "l", "s", CLARO), (2015, y1, "Marco de Sendái", "d", "c", "s", CLARO),
        (2017, y1, "Resolución 2254:\ncalidad del aire", "u", "c", "s", CLARO), (2018, y1, "CONPES 3943", "d", "c", "s", CLARO),
        (2020, y1, "Ley 2056:\nregalías", "u", "c", "s", CLARO), (2021, y1, "OMS (guías) y\nCONPES 4069", "d", "c", "s", CLARO),
        (2023, y1, "Ley 2294:\nPND 2022-2026", "u", "c", "s", CLARO),
        (2015, y2, "Kumar et al.", "u", "r", "o", MEDIO), (2017, y2, "Castell et al.", "d", "r", "o", MEDIO),
        (2018, y2, "Crilley et al.;\nJayaratne et al.", "u", "c", "o", MEDIO), (2019, y2, "Karagulian\net al.", "d", "c", "o", MEDIO),
        (2020, y2, "Magi et al.;\nMalings et al.", "u", "l", "o", MEDIO), (2021, y2, "Barkjohn et al.;\nGiordano et al.;\nEPA", "d", "l", "o", MEDIO),
        (2022, y3, "Rodríguez-Villamizar\net al.", "u", "r", "^", AZUL), (2025, y3, "Suresh et al.:\nmina de carbón", "u", "c", "^", AZUL),
        (2026, y3, "SIATA; Bang et al.;\nTavella et al.;\nMurad Pedraza et al.", "d", "r", "^", AZUL),
    ]
    lh = P(F_B) * A.LH / 72 / A.UNIT
    for (yr, y, tx, lado, al, m, c) in ev:
        x = xa(yr)
        n = len(tx.split("\n"))
        if lado == "u":
            y_txt0 = y + 3.4
            ax.plot([x, x], [y + 0.9, y_txt0], color=T, lw=0.9, zorder=2)
            for i, l in enumerate(tx.split("\n")[::-1]):
                A.txt(ax, x + {"l": -0.5, "r": 0.5, "c": 0}[al], y_txt0 + (i + 0.5) * lh, l, F_B, ha={"l": "left", "r": "right", "c": "center"}[al])
        else:
            y_txt0 = y - 3.4
            ax.plot([x, x], [y - 0.9, y_txt0], color=T, lw=0.9, zorder=2)
            for i, l in enumerate(tx.split("\n")):
                A.txt(ax, x + {"l": -0.5, "r": 0.5, "c": 0}[al], y_txt0 - (i + 0.5) * lh, l, F_B, ha={"l": "left", "r": "right", "c": "center"}[al])
        ax.plot([x], [y], m, ms=10 if m != "^" else 11, mfc=c, mec=T, mew=1.1, zorder=4)
    return A.guardar(fig, "c6_f01")


# ------------------------------------------------------------------ c6_f02
PATENTES = {"G-01", "G-02", "G-03", "G-04", "G-07", "G-09", "G-11", "G-14", "G-15", "G-16", "G-23", "G-24", "G-25", "G-40", "G-41"}

def leer_tabla13():
    filas = {}
    for linea in open(INFORME, encoding="utf-8"):
        m = re.match(r"^\s+(G-\d\d)\s{2,}(.+?)\s{2,}(\d|N/A)\s+(\S+)\s+(\S+)\s+(\d|N/A)\s+(\d|N/A)\s+(\S+)\s+(\S+)\s*$", linea)
        if m:
            filas[m.group(1)] = (m.group(2).strip(), None if m.group(3) == "N/A" else int(m.group(3)), None if m.group(6) == "N/A" else int(m.group(6)))
    return filas


def c6_f02():
    t13 = leer_tabla13()
    assert len(t13) == 42
    datos = {g: v for g, v in t13.items() if v[1] is not None and v[2] is not None}
    n = len(datos)
    n_trl4 = sum(1 for v in datos.values() if v[1] <= 4)
    n_trl7 = sum(1 for v in datos.values() if v[1] >= 7)
    assert (n, n_trl4, n_trl7) == (41, 34, 2)
    cuenta = {"art": collections.Counter(), "pat": collections.Counter()}
    for g, (cita, trl, irl) in datos.items():
        cuenta["pat" if g in PATENTES else "art"][(trl, irl)] += 1
    n_art, n_pat = sum(cuenta["art"].values()), sum(cuenta["pat"].values())
    assert (n_art, n_pat) == (26, 15)
    H = 74
    fig, ax = A.lienzo(f"De {n} documentos del corpus, {n_trl4} están en TRL 4 o menos y solo dos alcanzan el TRL 7",
                       "Documentos por nivel de madurez tecnológica (TRL, eje x) y de integración (IRL, eje y); el tamaño indica el número de documentos",
                       H)
    a = A.subeje(fig, ax, 9, 8.5, 99, H - 1.5)
    a.set_xlim(1.4, 9.9); a.set_ylim(0.2, 9.9)
    a.set_xticks(range(2, 10)); a.set_yticks(range(1, 10))
    a.grid(True, alpha=0.25, ls="--", lw=0.6, color=MEDIO)
    a.set_xlabel("Nivel de madurez tecnológica (TRL)", fontsize=P(F_B), color=T)
    a.set_ylabel("Nivel de integración (IRL)", fontsize=P(F_B), color=T)
    # criterios y banda del proyecto
    a.axvline(7, color=T, lw=1.2, ls=PUNTEADO, zorder=2)
    a.axhline(6, color=T, lw=1.0, ls=DISCONT, zorder=2)
    a.text(7.08, 0.4, "Criterio TRL 7", fontsize=P(F_B), color=T, ha="left", va="bottom")
    a.text(1.5, 6.08, "Criterio IRL 6", fontsize=P(F_B), color=T, ha="left", va="bottom")
    a.add_patch(Rectangle((4, 9.2), 4, 0.7, fc=MEDIO, ec=T, lw=1.0, zorder=2))
    a.text(4.1, 9.55, "Proyecto: TRL 4 a 8", fontsize=P(F_B), fontweight="bold", color=T, ha="left", va="center", zorder=3)
    DESP = 0.3
    esc = lambda k: 120 * k + 200
    for (trl, irl), k in sorted(cuenta["art"].items()):
        dx = -DESP if (trl, irl) in cuenta["pat"] else 0
        a.scatter(trl + dx, irl, s=esc(k), marker="o", facecolor=AZUL, edgecolor=T, linewidth=1.1, zorder=4)
        a.text(trl + dx, irl, str(k), ha="center", va="center", fontsize=P(F_B), fontweight="bold", color=T, zorder=5)
    for (trl, irl), k in sorted(cuenta["pat"].items()):
        dx = DESP if (trl, irl) in cuenta["art"] else 0
        a.scatter(trl + dx, irl, s=esc(k), marker="s", facecolor=CLARO, edgecolor=T, linewidth=1.1, zorder=4)
        a.text(trl + dx, irl, str(k), ha="center", va="center", fontsize=P(F_B), fontweight="bold", color=T, zorder=5)
    # leyenda directa
    a.scatter([1.65], [9.55], s=230, marker="o", facecolor=AZUL, edgecolor=T, linewidth=1.1, zorder=4)
    a.text(1.85, 9.55, f"Artículos ({n_art})", fontsize=P(F_B), color=T, va="center")
    a.scatter([1.65], [8.9], s=230, marker="s", facecolor=CLARO, edgecolor=T, linewidth=1.1, zorder=4)
    a.text(1.85, 8.9, f"Patentes ({n_pat})", fontsize=P(F_B), color=T, va="center")
    # etiquetas directas de los documentos del nicho
    def rot(xy, xyt, s, ha):
        a.annotate(s, xy=xy, xytext=xyt, fontsize=P(F_B), color=T, ha=ha, va="center", linespacing=1.25,
                   arrowprops=dict(arrowstyle="-", color=T, lw=0.9, shrinkA=2, shrinkB=9))
    rot((9, 8), (8.45, 8.05), "SIATA\n(Ruiz-Carrascal et al., 2026)", "right")
    rot((7, 5), (7.3, 5.0), "Sistema de lahares, Perú\n(Espinoza et al., 2026)", "left")
    rot((6, 4), (7.3, 3.4), "Mina de carbón\n(Suresh et al., 2025)", "left")
    rot((4, 4), (3.35, 5.35), "Red de Seúl\n(Bang et al., 2026)", "center")
    return A.guardar(fig, "c6_f02")


# ------------------------------------------------------------------ c8_f01
def c8_f01():
    nodos = {"Manizales (Caldas)": 50, "Calarcá (Quindío)": 50}
    assert sum(nodos.values()) == A.m2.IDENT["nodos"]
    consejos = {"Manizales (Caldas)": "Consejo municipal de Manizales y consejo departamental de Caldas", "Calarcá (Quindío)": "Consejo municipal de Calarcá y consejo departamental del Quindío"}
    H = 60.0
    fig, ax = A.lienzo("Cada municipio conecta una demanda territorial con nodos, consejos y planes de desarrollo",
                       "Relación entre la demanda, el proyecto, el resultado medible y los planes de desarrollo de cada municipio", H)
    ga = 3.6
    wc = (98 - 3 * ga) / 4
    xs = [1.0 + i * (wc + ga) for i in range(4)]
    cab = ["Demanda territorial", "Proyecto", "Resultado medible", "Planes de desarrollo municipal y departamental"]
    y = H - 0.5
    for x, t in zip(xs, cab):
        A.lineas(ax, x + wc / 2, y, t, F_B, True, ha="center", ancho=wc)
    y -= 6.2
    hr = 21.5
    for dep in nodos:
        A.txt(ax, 1, y - 1.2, dep, F_B, True, ha="left")
        ax.plot([1, 99], [y - 3.0, y - 3.0], color=MEDIO, lw=1.0, zorder=1)
        yb = y - 3.6 - hr
        A.caja(ax, xs[0], yb, wc, hr, [("por diligenciar", "i")], relleno=CAJA, ls=PUNTEADO, lw=1.6)
        A.caja(ax, xs[1], yb, wc, hr, [(consejos[dep], "n"), (f"{nodos[dep]} nodos operativos", "b"),
                                       ("Conjunto de referencia rotativo", "n")], relleno=CLARO, gap=0.6)
        A.caja(ax, xs[2], yb, wc, hr, [("Uso institucional del tablero", "n"), ("Reducción de falsas alarmas", "n"),
                                       ("Activación del protocolo de alerta", "n")], relleno=MEDIO, gap=0.7)
        A.caja(ax, xs[3], yb, wc, hr, [("Planes por diligenciar", "i"), ("eje y programa de cada plan", "i")], relleno=CAJA, ls=PUNTEADO, lw=1.6, gap=0.8)
        for i in range(3):
            A.flecha(ax, (xs[i] + wc + 0.4, yb + hr / 2), (xs[i + 1] - 0.4, yb + hr / 2))
        y = yb - 1.4
    return A.guardar(fig, "c8_f01")


if __name__ == "__main__":
    only = sys.argv[1:] or ["c6_f01", "c6_f02", "c8_f01"]
    for f in only:
        globals()[f]()
