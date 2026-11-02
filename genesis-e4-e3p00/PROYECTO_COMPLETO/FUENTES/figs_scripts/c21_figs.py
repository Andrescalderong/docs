# -*- coding: utf-8 -*-
"""Figuras del capítulo 21 (Project Charter): c21_f01 (línea de tiempo de hitos H0 a H8) y c21_f02 (mapa de stakeholders).
Datos: maestro.HITOS, maestro.TRAMOS y maestro.ACTS (CPM) mediante a11_datos.py; actores de 4.4-MDR.5 (sin nombres de personas).
Ejecución: python3 c21_figs.py  (diagramas sin componente aleatorio; sin semilla)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11_datos as D
import estilo as E
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

M = D.M

def caja(ax, x, y, w, h, texto, relleno=E.CAJA, borde=E.TINTA, fs=7.6, bold=False, lw=1.2, ls="-", hatch=None, ha="center"):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=borde, lw=lw, ls=ls, hatch=hatch)
    ax.add_patch(p)
    kw = dict(bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.92)) if hatch else {}
    ax.text(x + w / 2, y + h / 2, texto, ha=ha, va="center", fontsize=fs, color=E.TINTA,
            fontweight="bold" if bold else "normal", linespacing=1.25, **kw)

def linea(ax, p0, p1, lw=1.2, ls="-", color=E.TINTA, head=False):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>" if head else "-", mutation_scale=10, color=color, lw=lw, ls=ls, shrinkA=0, shrinkB=0))

# ------------------------------------------------------------------ F21.1 Línea de tiempo
CORTO = {
    "H0": "Acta de inicio y\ncontratación completa", "H1": "Sitios, enlace y\nenergía listos", "H2": "Colocalización del\ntramo 1 finalizada",
    "H3": "Compuerta C1:\nmodelo validado", "H4": "Tramo 2 instalado\ny verificado", "H5": "Compuerta C2:\nuso y desempeño",
    "H6": "Tramo 3 instalado", "H7": "Ensayo independiente\ny evaluación final", "H8": "Transferencia y\ncierre (C3)",
}

def f01():
    hit = {h[0]: h[2] for h in M.HITOS}
    assert [hit[k] for k in ("H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8")] == [2, 4, 10, 12, 16, 17, 19, 23, 24]
    fig, ax = E.lienzo_libre(
        h1="Nueve hitos entre el mes 2 y el mes 24; C1 y C2 liberan los tramos 2 y 3",
        h2=f"Línea de tiempo en meses de calendario (1 mes = 52/12 semanas); hitos H0 a H8 del cronograma CPM de {M.DURACION_SEMANAS} semanas",
        figsize=(10, 4.5), xlim=(0, 100), ylim=(0, 50))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.88, bottom=0.01)
    x0, x1 = 3.0, 97.0
    X = lambda m: x0 + (x1 - x0) * m / 24.0
    ya, ha_ = 18.0, 8.6
    fills = [(E.CLARO, None), (E.MEDIO, "///"), (E.GRIS, "..")]
    for t, (fc, ht) in zip(M.TRAMOS, fills):
        xa, xb = X(t["m_ini"] - 1), X(t["m_fin"])
        ax.add_patch(Rectangle((xa, ya), xb - xa, ha_, fc=fc, ec=E.AZUL, lw=1.2, hatch=ht))
        nom = {1: "Tramo 1: piloto de contraste", 2: "Tramo 2: ampliación", 3: "Tramo 3: consolidación"}[t["id"]]
        ax.text((xa + xb) / 2, ya + ha_ / 2, f"{nom}\n{t['nodos']} nodos · {t['gateways']} gateways\nmeses {t['m_ini']} a {t['m_fin']}",
                ha="center", va="center", fontsize=7.4, color=E.TINTA, linespacing=1.3,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9))
    # escala de meses
    for m in range(0, 25):
        ax.plot([X(m), X(m)], [ya - 0.9, ya], color=E.TINTA, lw=0.8)
    for m in (0, 3, 6, 9, 12, 15, 18, 21, 24):
        ax.text(X(m), ya - 2.4, str(m), ha="center", va="top", fontsize=8, color=E.TINTA)
    ax.text(x0 - 2.0, ya - 2.4, "Mes", ha="right", va="top", fontsize=8, color=E.TINTA, fontweight="bold")
    # hitos
    alto = ["H0", "H2", "H4", "H8"]; bajo_alto = ["H6"]; abajo = ["H1", "H3", "H5", "H7"]
    comp = {"H3": "C1", "H5": "C2", "H8": "C3"}
    for k, m in hit.items():
        xm = X(m)
        if k in alto:
            yl, yt = ya + ha_, 40.0; va = "bottom"; yb = ya + ha_ + 0.4
        elif k in bajo_alto:
            yl, yt = ya + ha_, 32.5; va = "bottom"; yb = ya + ha_ + 0.4
        else:
            yl, yt = ya - 4.2, 9.8; va = "top"; yb = ya - 4.2
        if k in alto or k in bajo_alto:
            ax.plot([xm, xm], [ya + ha_, yt], color=E.TINTA, lw=0.9, ls=":")
        else:
            ax.plot([xm, xm], [ya, yt + 0.2], color=E.TINTA, lw=0.9, ls=":")
        mk = "D" if k in comp else "o"
        ym = ya + ha_ if (k in alto or k in bajo_alto) else ya
        ax.plot([xm], [ym], marker=mk, ms=9.5, mfc=E.AZUL if k not in comp else E.TINTA, mec=E.TINTA, mew=1.0, zorder=5)
        etiqueta = f"{k} · mes {m}" + (f" · {comp[k]}" if k in comp else "") + "\n" + CORTO[k]
        ha = "right" if k == "H8" else ("left" if k == "H0" else "center")
        xt = xm + (1.2 if k == "H8" else 0)
        if k == "H8": xt = xm + 2.6
        if k == "H0": xt = xm - 2.6
        ax.text(xt, yt if k in alto or k in bajo_alto else yt, etiqueta, ha=ha, va="bottom" if (k in alto or k in bajo_alto) else "top",
                fontsize=7.4, color=E.TINTA, linespacing=1.3, fontweight="normal",
                bbox=dict(boxstyle="round,pad=0.3", fc=E.BLANCO, ec=E.MEDIO, lw=0.9))
    ax.plot([2], [0.8], marker="o", ms=8, mfc=E.AZUL, mec=E.TINTA); ax.text(3.3, 0.8, "Hito", va="center", fontsize=7.8, color=E.TINTA)
    ax.plot([11], [0.8], marker="D", ms=8, mfc=E.TINTA, mec=E.TINTA); ax.text(12.3, 0.8, "Compuerta de decisión (C1, C2 y C3)", va="center", fontsize=7.8, color=E.TINTA)
    E.guardar(fig, "c21_f01")

# ------------------------------------------------------------------ F21.2 Mapa de stakeholders
GRUPOS = [
    ("Decide y financia", "A", [("Convocante y órganos del SGR", "Decisor con veto; poder ALTO (DECLARADO)", True)]),
    ("Ejecuta", "B", [("Institución de educación superior ejecutora", "Ejecutor; custodio potencial", False),
                      ("Empresa tecnológica aliada", "Ejecutor; custodio potencial", False),
                      ("Proveedores de sensores", "Ejecutor indirecto", False)]),
    ("Custodia y usa", "C", [("Alcaldías de municipios con remoción", "Veto; custodio potencial; afectado", True),
                             ("Gobernaciones y unidades departamentales", "Custodio potencial", False),
                             ("UNGRD y puestos de mando unificado", "Decisor operativo; usuario", False)]),
    ("Afectados y posibles financiadores", "D", [("Operarios y comunidades colindantes", "Afectado", False),
                                                  ("Constructoras y contratistas de remoción", "Afectado; generador de emisión", False),
                                                  ("Secretarías de salud, ADRES y ARL", "Financiador potencial", False)]),
    ("Referencia y control", "E", [("IDEAM y autoridades ambientales", "Referencia metrológica", False),
                                   ("Órganos de control fiscal", "Control", False)]),
]

def f02():
    n_act = sum(len(g[2]) for g in GRUPOS)
    assert n_act == 12
    fig, ax = E.lienzo_libre(
        h1="Doce actores sin relevancia evaluada; solo el convocante tiene poder documentado",
        h2="Mapa de stakeholders por tipo de relación (4.4-MDR.5); sin nombres de personas; poder, legitimidad y urgencia NO_EVALUADO salvo el convocante",
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    caja(ax, 36, 28.5, 28, 9.4, "Proyecto: red IoT híbrida\ny gemelo digital\npara material particulado", relleno=E.MEDIO, borde=E.AZUL, fs=8.6, bold=True, lw=2.0)
    pos = {"A": (33, 51.5, 34), "B": (1, 41, 30), "C": (69, 41, 30), "D": (1, 3, 30), "E": (69, 3, 30)}
    alto_act = 5.2; sep = 1.2
    cen = {}
    for nombre, clave, acts in GRUPOS:
        x, y, w = pos[clave]
        n = len(acts)
        hg = 5.0 + n * alto_act + (n - 1) * sep + 1.2
        if clave in ("D", "E"):
            hg_ = 5.0 + 3 * alto_act + 2 * sep + 1.2
            y = y; hg = hg_
        ax.add_patch(FancyBboxPatch((x, y), w, hg, boxstyle="round,pad=0.25,rounding_size=0.8", fc=E.GRIS, ec=E.AZUL, lw=1.1, ls="--"))
        ax.text(x + 0.9, y + hg - 1.9, nombre, ha="left", va="center", fontsize=8.3, fontweight="bold", color=E.TINTA)
        for k, (nom, rol, veto) in enumerate(acts):
            ya = y + hg - 5.0 - (k + 1) * alto_act - k * sep
            caja(ax, x + 1.0, ya, w - 2.0, alto_act, f"{nom}\n{rol}", relleno=E.BLANCO, borde=E.TINTA if veto else E.AZUL, fs=6.9,
                 lw=2.2 if veto else 1.1)
        cen[clave] = (x, y, w, hg)
    # conectores con el proyecto
    def borde_centro(px, py):
        return px, py
    xA, yA, wA, hA = cen["A"]; linea(ax, (50, yA - 0.3), (50, 38.2))
    xB, yB, wB, hB = cen["B"]; linea(ax, (xB + wB + 0.3, yB + 6), (35.6, 35.5))
    xC, yC, wC, hC = cen["C"]; linea(ax, (xC - 0.3, yC + 6), (64.4, 35.5))
    xD, yD, wD, hD = cen["D"]; linea(ax, (xD + wD + 0.3, yD + hD - 6), (35.6, 30.5))
    xE, yE, wE, hE = cen["E"]; linea(ax, (xE - 0.3, yE + hE - 6), (64.4, 30.5))
    ax.text(50, 14.5, "Borde grueso: actor con veto.\nRelevancia (poder, legitimidad y urgencia):\nNO_EVALUADO, salvo el poder del convocante.\nNingún actor firmó compromiso alguno\n(alianza SUPUESTO por instrucción del usuario).",
            ha="center", va="center", fontsize=7.8, color=E.TINTA, linespacing=1.4)
    E.guardar(fig, "c21_f02")

if __name__ == "__main__":
    f01(); f02(); print("ok")
