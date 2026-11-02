# -*- coding: utf-8 -*-
"""Figuras del capítulo 17 (Equipo de Trabajo): c17_f01 (organigrama) y c17_f02 (mapa de alianzas).
Datos: maestro.py (BUDGET P01 a P14, CONTRA C01 a C06, RES) mediante a11_datos.py; actores de 4.4-MDR.5.
Ejecución: python3 c17_figs.py  (diagramas sin componente aleatorio; sin semilla)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11_datos as D
import estilo as E
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def caja(ax, x, y, w, h, texto, relleno=E.CAJA, borde=E.TINTA, fs=8.2, bold=False, lw=1.2, ls="-", hatch=None):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=relleno, ec=borde, lw=lw, ls=ls, hatch=hatch)
    ax.add_patch(p)
    kw = dict(bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.92)) if hatch else {}
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA,
            fontweight="bold" if bold else "normal", linespacing=1.25, **kw)
    return p

def linea(ax, p0, p1, color=E.TINTA, lw=1.3, ls="-", flecha=True, rad=0.0):
    a = FancyArrowPatch(p0, p1, arrowstyle="-|>" if flecha else "-", mutation_scale=11, color=color, lw=lw, ls=ls,
                        connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0)
    ax.add_patch(a)

# ------------------------------------------------------------------ F17.1 Organigrama
SHORT = {
    "P01": "Jóvenes investigadores", "P02": "Estudiantes de maestría", "P03": "Científico de datos senior",
    "P04": "Ingenieros IoT y de campo", "P05": "Coordinación de apropiación social", "P06": "Gerencia de proyecto",
    "P07": "Especialista en metrología", "P08": "Ingenieros de software y nube", "P09": "Ingeniero de firmware y energía",
    "P10": "Técnicos de campo departamentales", "P11": "Profesionales de apropiación social",
    "P12": "Analista de datos espaciales", "P13": "Profesional en calidad del aire", "P14": "Profesional de convenios y custodia",
}
PP = {p["id"]: p for p in D.PERS}

def f01():
    assert D.N_PERS == 29 and D.N_CPERS == 4
    fig, ax = E.lienzo_libre(
        h1="29 personas del SGR y 4 de la IES se organizan en cuatro paquetes",
        h2="Organigrama funcional; personas por rol (líneas P01 a P14 y C01 a C03); borde continuo DECLARADO, discontinuo PROPUESTO, trama contrapartida",
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    # nivel 1: comité directivo y órganos externos
    caja(ax, 31, 61, 38, 6.4, "Comité directivo (PROPUESTO)\nDecide las compuertas C1, C2 y C3", relleno=E.MEDIO, borde=E.AZUL, fs=8.6, bold=True, lw=1.6, ls="--")
    caja(ax, 1.5, 61, 25, 6.4, "Evaluación externa independiente\n(meses 12 y 24; línea S07)", relleno=E.BLANCO, borde=E.MEDIO, fs=8, ls="--")
    caja(ax, 73.5, 61, 25, 6.4, "Comité asesor comunitario\n(nivel 3 de la escalera ASC)", relleno=E.BLANCO, borde=E.MEDIO, fs=8, ls="--")
    linea(ax, (26.9, 64.2), (30.6, 64.2), flecha=False, ls=":"); linea(ax, (69.4, 64.2), (73.1, 64.2), flecha=False, ls=":")
    # nivel 2: dirección y gerencia
    caja(ax, 9, 49, 38, 7.4, "Dirección científica\nInvestigador principal (C01)\n1 persona · 0,5 ETC · IES", relleno=E.CLARO, borde=E.AZUL, fs=8.4, lw=1.6, hatch="///")
    caja(ax, 53, 49, 38, 7.4, "Gerencia de proyecto (P06 · WP0)\n1 persona · 1,0 ETC · gestión,\ncompuertas y cierre", relleno=E.CLARO, borde=E.AZUL, fs=8.4, lw=1.6)
    linea(ax, (44, 60.7), (28, 56.9)); linea(ax, (56, 60.7), (72, 56.9))
    # barra de enlace entre dirección, gerencia y paquetes
    linea(ax, (28, 48.6), (28, 46.8), flecha=False); linea(ax, (72, 48.6), (72, 46.8), flecha=False)
    linea(ax, (16.5, 46.8), (83.5, 46.8), flecha=False)
    # nivel 3: paquetes
    X = [1.5, 35, 68.5]; W = 30
    enc = [
        "WP1 Medición verificada (OE1)\nLíder: coinvestigador técnico (C02)\n10 personas · 168 persona-mes",
        "WP2 Red, energía y plataforma (OE2)\nLíder: ingeniería IoT y de campo (P04)\n13 personas · 312 persona-mes",
        "WP3 Uso institucional y custodia (OE3)\nLíder: coordinación social (P05)\n5 personas · 120 persona-mes",
    ]
    for i in range(3):
        caja(ax, X[i], 37.5, W, 7.6, enc[i], relleno=E.MEDIO, borde=E.AZUL, fs=7.7, lw=1.6)
        cx = X[i] + W / 2
        linea(ax, (cx, 46.8), (cx, 45.4))
    roles = [
        [("P03", 1), ("P07", 1), ("P01", 6), ("P02", 2)],
        [("P04", 3), ("P08", 2), ("P09", 1), ("P10", 6), ("P12", 1)],
        [("P05", 1), ("P11", 2), ("P13", 1), ("P14", 1), ("C03", 2)],
    ]
    for i, lista in enumerate(roles):
        for k, (cod, n) in enumerate(lista):
            y = 31.2 - k * 5.6
            if cod == "C03":
                txt = "C03 Coinvestigadores de ambiente\ny ciencias sociales (2 · 0,2 ETC)"
                caja(ax, X[i], y - 0.4, W, 4.8, txt, relleno=E.BLANCO, borde=E.AZUL, fs=7.0, lw=1.3, ls="--", hatch="///")
            else:
                p = PP[cod]
                nat_ls = "-" if p["nat"] == "DECLARADO" else "--"
                caja(ax, X[i], y, W, 4.0, f"{cod} {SHORT[cod]} ({n})", relleno=E.BLANCO, borde=E.AZUL, fs=7.3, lw=1.3, ls=nat_ls)
        # línea de enlace entre el encabezado y los roles
    # leyenda
    ax.text(1.5, 2.6, "Totales: SGR 29 personas, 624 persona-mes y 26,0 ETC promedio (CALCULADO); contrapartida IES 4 personas y 1,2 ETC.",
            fontsize=8.2, color=E.TINTA, ha="left")
    ax.text(1.5, 0.2, "ETC: equivalente de tiempo completo. Cifras de P01 a P14 y C01 a C03 tomadas del presupuesto y de la contrapartida.",
            fontsize=7.6, color=E.TINTA, ha="left")
    E.guardar(fig, "c17_f01")

# ------------------------------------------------------------------ F17.2 Mapa de alianzas
def f02():
    ies = D.mm(D.CONTRA_IES); ef = D.mm(D.CONTRA_EMP_EF); es = D.mm(D.CONTRA_EMP_ES); sgr = D.mm(D.RES["sgr"])
    fig, ax = E.lienzo_libre(
        h1="Dos aliados aportan 2.110 millones de COP; los demás no tienen compromiso",
        h2="Mapa de alianzas; aportes en millones de COP (CALCULADO desde la contrapartida); alianza empresa-IES SUPUESTO por instrucción del usuario",
        figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    cx, cy, cw, ch = 34, 29, 32, 10
    caja(ax, cx, cy, cw, ch, "Proyecto: red IoT híbrida\ny gemelo digital\n24 meses · tres tramos", relleno=E.MEDIO, borde=E.AZUL, fs=9.2, bold=True, lw=2.0)
    # actores
    A = {
        "sgr": (34, 58, 32, 7.2, f"Financiador: SGR / MinCiencias\nSolicitado: {sgr} M", E.CLARO, E.AZUL, "-", 1.8, None),
        "ies": (1, 47, 30, 8.6, f"IES ejecutora\nContrapartida: {ies} M\nen especie (C01 a C04)", E.CLARO, E.AZUL, "-", 1.8, "///"),
        "emp": (69, 47, 30, 8.6, f"Empresa tecnológica\n{ef} M en efectivo\n+ {es} M en especie", E.CLARO, E.AZUL, "-", 1.8, "///"),
        "alc": (1, 29, 28, 8.4, "Alcaldías de 12 municipios\nSin aporte: VACIO\nCustodios potenciales", E.BLANCO, E.TINTA, "--", 1.2, None),
        "gob": (71, 29, 28, 8.4, "Gobernaciones y unidades\ndepartamentales\nSin evidencia: NO_EVALUADO", E.BLANCO, E.TINTA, "--", 1.2, None),
        "ung": (1, 11.5, 28, 8.4, "UNGRD y puestos de mando\nunificado\nUsuarios (INFERIDO)", E.BLANCO, E.TINTA, "--", 1.2, None),
        "com": (35, 11.5, 30, 8.4, "Comités de gestión del riesgo (15)\n12 municipales y 3 departamentales\nUsuarios del tablero (SUPUESTO)", E.GRIS, E.TINTA, ":", 1.2, None),
        "ide": (71, 11.5, 28, 8.4, "IDEAM y autoridades\nambientales\nReferencia (INFERIDO)", E.BLANCO, E.TINTA, "--", 1.2, None),
    }
    for k, (x, y, w, h, t, fc, ec, ls, lw, hat) in A.items():
        caja(ax, x, y, w, h, t, relleno=fc, borde=ec, fs=8.0, lw=lw, ls=ls, hatch=hat)
    def cen(k):
        x, y, w, h = A[k][:4]; return (x + w / 2, y + h / 2)
    # aportes (flechas hacia el proyecto)
    linea(ax, (50, 58), (50, 39.6), color=E.AZUL, lw=2.6)
    linea(ax, (31.3, 49.5), (cx + 3, cy + ch), color=E.AZUL, lw=2.6)
    linea(ax, (68.7, 49.5), (cx + cw - 3, cy + ch), color=E.AZUL, lw=2.6)
    # relaciones sin compromiso
    linea(ax, (29.4, 33.2), (cx - 0.3, 33.2), color=E.TINTA, lw=1.2, ls="--", flecha=False)
    linea(ax, (70.6, 33.2), (cx + cw + 0.3, 33.2), color=E.TINTA, lw=1.2, ls="--", flecha=False)
    linea(ax, (29.4, 18.5), (cx + 4, cy - 0.3), color=E.TINTA, lw=1.2, ls="--", flecha=False)
    linea(ax, (70.6, 18.5), (cx + cw - 4, cy - 0.3), color=E.TINTA, lw=1.2, ls="--", flecha=False)
    linea(ax, (50, 20.1), (50, cy - 0.3), color=E.TINTA, lw=1.2, ls=":", flecha=False)
    ax.text(51.2, 50, f"{sgr} M", fontsize=8.4, fontweight="bold", color=E.TINTA, ha="left", va="center")
    ax.text(22, 43.2, f"{ies} M", fontsize=8.4, fontweight="bold", color=E.TINTA, ha="center", va="center")
    ax.text(78, 43.2, f"{D.mm(D.CONTRA_EMP)} M", fontsize=8.4, fontweight="bold", color=E.TINTA, ha="center", va="center")
    # leyenda
    ax.plot([1, 9], [6.2, 6.2], color=E.AZUL, lw=2.6); ax.text(10, 6.2, "Aporte con cifra (DECLARADO; desglose de la IES PROPUESTO)", va="center", fontsize=8, color=E.TINTA)
    ax.plot([1, 9], [3.6, 3.6], color=E.TINTA, lw=1.2, ls="--"); ax.text(10, 3.6, "Relación sin compromiso escrito ni aporte", va="center", fontsize=8, color=E.TINTA)
    ax.plot([1, 9], [1.0, 1.0], color=E.TINTA, lw=1.2, ls=":"); ax.text(10, 1.0, "Uso del tablero y del protocolo", va="center", fontsize=8, color=E.TINTA)
    ax.text(55, 5.2, f"Servicios contratados con el SGR (no son alianzas): laboratorio acreditado S01 ({D.mm(D.B["S01"]["total"])} M),\nlaboratorio externo S08 ({D.mm(D.B["S08"]["total"])} M) y evaluación externa S07 ({D.mm(D.B["S07"]["total"])} M).",
            fontsize=7.8, color=E.TINTA, ha="left", va="center", linespacing=1.3)
    E.guardar(fig, "c17_f02")

if __name__ == "__main__":
    f01(); f02(); print("ok")
