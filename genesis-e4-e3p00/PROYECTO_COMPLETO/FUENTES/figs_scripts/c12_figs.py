# -*- coding: utf-8 -*-
"""Figuras del capítulo 12 (indicadores PERS): c12_f01 a c12_f05. Datos desde c12_datos.py (IND, TRAMOS, HITOS de la ficha maestra).
f01 cadena PERS y teoría del cambio; f02 matriz de productos por objetivo; f03 flujo causal Output-Outcome;
f04 dashboard con semáforo ex ante (riesgo de la ficha); f05 cronograma de medición con hitos H0-H8.
Ejecución: python3 c12_figs.py (sin semilla: diagramas sin componente aleatorio)."""
import os, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c12_datos as D
import estilo as E
import matplotlib as mpl
mpl.rcParams["hatch.linewidth"] = 0.5
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.pyplot as plt

IND = D.IND; M = D.M
W = lambda s, n: textwrap.fill(s, n)

def blanco(ax, x, y, texto, fs=7.4, bold=False, ha="center", va="center"):
    return ax.text(x, y, texto, ha=ha, va=va, fontsize=fs, fontweight="bold" if bold else "normal", color=E.TINTA, zorder=6,
                   bbox=dict(fc=E.BLANCO, ec="none", pad=0.8, alpha=0.95))


def libre(h1, h2, figsize=(10, 7), xlim=(0, 100), ylim=(0, 70), top=0.90):
    """Lienzo libre con el subtítulo H2 alineado al mismo margen que el H1 (fig.text en lugar del título del eje)."""
    fig, ax = E.lienzo_libre(h1=h1, h2=None, figsize=figsize, xlim=xlim, ylim=ylim)
    fig.subplots_adjust(left=0.005, right=0.995, top=top, bottom=0.01)
    fig.text(0.01, top + 0.012, h2, ha="left", va="bottom", fontsize=10, color=E.TINTA)
    return fig, ax

# ============================================================================== F12.1
CORTO = {"PERS-R01": "Despliegue por tramo", "PERS-R02": "Ciclos de calibración", "PERS-R03": "Disponibilidad de la nube",
         "PERS-R04": "Ejecución presupuestal", "PERS-R05": "Horas-nodo válidas", "PERS-R06": "Informes a tiempo",
         "PERS-P01": "Red de 100 nodos\ny 10 gateways", "PERS-P02": "Software y gemelo\ndigital registrado", "PERS-P03": "Artículos Q1 o Q2",
         "PERS-P04": "Actividades de\napropiación social", "PERS-E01": "Uso del tablero\ny del protocolo", "PERS-E02": "Reducción de\nfalsas alarmas",
         "PERS-E03": "Capacidad instalada\nen custodios", "PERS-S01": "Activación del\nprotocolo", "PERS-S02": "Continuidad de la\nred bajo custodia"}

def f01():
    n_out = D.NIV["R"] + D.NIV["P"]
    assert (n_out, D.NIV["E"], D.NIV["S"]) == (10, 3, 2)
    fig, ax = libre("Diez outputs, tres outcomes y dos impactos: solo los outputs quedan bajo el techo",
                    "Cadena de resultados PERS con taxonomía MinCiencias, marco lógico y supuestos críticos SC-1 a SC-4; 15 indicadores")
    X = [1, 22, 43, 64, 85]; Wd = 14.5
    # banda de taxonomía
    bandas = [("OUTPUTS: 10 indicadores (R y P)", X[1], X[2] + Wd, E.CLARO, None),
              ("OUTCOMES: 3 (E)", X[3], X[3] + Wd, E.MEDIO, None),
              ("IMPACT: 2 (S)", X[4], X[4] + Wd, E.MEDIO, "///")]
    for t, x0, x1, fc, h in bandas:
        ax.add_patch(FancyBboxPatch((x0, 59.2), x1 - x0, 4.6, boxstyle="round,pad=0.2,rounding_size=0.6", fc=fc, ec=E.AZUL, lw=1.4, hatch=h))
        blanco(ax, (x0 + x1) / 2, 61.5, t, fs=8.3, bold=True)
    # encabezados de columna
    heads = [("Insumos", "", E.GRIS), ("R · Proceso", "Actividades", E.CLARO), ("P · Producto", "Componentes", E.CLARO),
             ("E · Efecto", "Propósito", E.MEDIO), ("S · Sostenibilidad", "Fin", E.MEDIO)]
    for i, (a, b, fc) in enumerate(heads):
        ax.add_patch(FancyBboxPatch((X[i], 50.0), Wd, 6.6, boxstyle="round,pad=0.2,rounding_size=0.6", fc=fc, ec=E.TINTA, lw=1.2))
        ax.text(X[i] + Wd / 2, 54.2 if b else 53.3, a, ha="center", va="center", fontsize=9, fontweight="bold", color=E.TINTA)
        if b: ax.text(X[i] + Wd / 2, 51.7, f"({b})", ha="center", va="center", fontsize=8, color=E.TINTA)
    # flechas entre columnas con supuestos
    etiq = ["Actividades", "Productos\nSC-2", "Uso\nSC-1 y SC-3", "Continuidad\nSC-3 y SC-4"]
    for i in range(4):
        E.flecha(ax, (X[i] + Wd + 0.4, 53.3), (X[i + 1] - 0.4, 53.3), color=E.TINTA, lw=1.3)
        blanco(ax, X[i] + Wd + 3.25, 57.6 if i != 2 else 57.6, etiq[i], fs=6.8)
    # chips
    def chip(col, k, cod, h=5.7, top=46.8, step=6.7):
        y = top - k * step - h
        ax.add_patch(FancyBboxPatch((X[col], y), Wd, h, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.BLANCO, ec=E.AZUL, lw=1.2))
        ax.text(X[col] + Wd / 2, y + h - 1.15, cod.replace("PERS-", ""), ha="center", va="center", fontsize=8, fontweight="bold", color=E.TINTA)
        ax.text(X[col] + Wd / 2, y + (h - 2.0) / 2, CORTO[cod], ha="center", va="center", fontsize=7.1, color=E.TINTA, linespacing=1.05)
    for col, niv in ((1, "R"), (2, "P"), (3, "E"), (4, "S")):
        for k, c in enumerate([c for c in D.ORDEN if IND[c]["nivel"] == niv]):
            chip(col, k, c)
    # insumos
    ins = [("Presupuesto SGR", f"{D.mm(D.SGR)} millones de COP"), ("Contrapartida", f"{D.mm(D.CONTRA)} millones de COP"),
           ("Ejecución", "24 meses y 104 semanas\n3 tramos, 3 compuertas")]
    for k, (a, b) in enumerate(ins):
        h = 5.7; y = 46.8 - k * 6.7 - h
        ax.add_patch(FancyBboxPatch((X[0], y), Wd, h, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.BLANCO, ec=E.MEDIO, lw=1.2))
        ax.text(X[0] + Wd / 2, y + h - 1.15, a, ha="center", va="center", fontsize=8, fontweight="bold", color=E.TINTA)
        ax.text(X[0] + Wd / 2, y + (h - 2.0) / 2, b, ha="center", va="center", fontsize=7.1, color=E.TINTA, linespacing=1.05)
    # techo de rendición de cuentas
    xt = (X[2] + Wd + X[3]) / 2
    ax.plot([xt, xt], [5.3, 66.2], color=E.TINTA, lw=1.4, ls=(0, (5, 3)), zorder=2)
    blanco(ax, xt, 67.6, "Techo de rendición de cuentas", fs=8.2, bold=True)
    ax.text(X[1] + Wd + 3, 3.0, "Bajo el techo: metas que el proyecto compromete", ha="center", va="center", fontsize=8, color=E.TINTA, fontweight="bold")
    ax.text(X[3] + Wd + 3, 3.0, "Sobre el techo: metas de contribución,\ncondicionadas por SC-3 y SC-4", ha="center", va="center", fontsize=8, color=E.TINTA, fontweight="bold")
    # marcador de riesgo alto (segundo canal): borde grueso en chips E y S
    E.guardar(fig, "c12_f01")

# ============================================================================== F12.2
def f02():
    prods = [c for c in D.ORDEN if IND[c]["nivel"] == "P"]
    oes = ["OE1", "OE2", "OE3"]
    asign = {c: IND[c]["oe"] for c in prods}
    cnt = {o: sum(1 for c in prods if asign[c] == o) for o in oes}
    assert cnt == {"OE1": 2, "OE2": 1, "OE3": 1}
    metas = {"PERS-P01": "100 nodos y 10 gateways\nal mes 24", "PERS-P02": "1 registro vigente\nal mes 24",
             "PERS-P03": "2 sometidos y al menos\n1 aceptado al mes 24", "PERS-P04": "29 actividades: 20 talleres\ny 9 jornadas"}
    assert "100 / 10" in IND["PERS-P01"]["mf"] and "1 registro" in IND["PERS-P02"]["mf"]
    fig, ax = libre("Cuatro productos tipificados cubren los tres objetivos; OE1 aporta dos",
                    "Matriz de productos PERS-P por objetivo específico, con código MMG 2021 propuesto, meta final y costo directo asociado",
                    figsize=(10, 4.8), ylim=(0, 50), top=0.84)
    x0 = 19.0; cw = 19.2; gap = 1.3
    for j, c in enumerate(prods):
        x = x0 + j * (cw + gap)
        ax.add_patch(FancyBboxPatch((x, 38.4), cw, 10.2, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.MEDIO, ec=E.TINTA, lw=1.2))
        ax.text(x + cw / 2, 46.6, c.replace("PERS-", ""), ha="center", va="center", fontsize=8.4, fontweight="bold", color=E.TINTA)
        ax.text(x + cw / 2, 44.2, IND[c]["mmg"].replace(" / ", "/"), ha="center", va="center", fontsize=7.2, fontweight="bold", color=E.TINTA)
        ax.text(x + cw / 2, 40.9, W(IND[c]["nombre"], 26), ha="center", va="center", fontsize=6.8, color=E.TINTA, linespacing=1.05)
    ys = [26.2, 14.2, 2.2]; hh = 10.6
    for i, o in enumerate(oes):
        y = ys[i]
        ax.add_patch(FancyBboxPatch((1, y), 16.2, hh, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.GRIS, ec=E.TINTA, lw=1.2))
        ax.text(9.1, y + hh - 2.2, o, ha="center", va="center", fontsize=10, fontweight="bold", color=E.TINTA)
        ax.text(9.1, y + hh / 2 - 1.2, f"{D.OE_N[o]} indicadores PERS\n{cnt[o]} de producto", ha="center", va="center", fontsize=7.6, color=E.TINTA, linespacing=1.1)
        for j, c in enumerate(prods):
            x = x0 + j * (cw + gap)
            if asign[c] == o:
                ax.add_patch(FancyBboxPatch((x, y), cw, hh, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.CLARO, ec=E.AZUL, lw=2.0))
                costo = f"{D.mm(D.monto(D.TRAZA[c]['rub']))} millones de COP"
                ax.text(x + cw / 2, y + hh / 2 + 1.3, metas[c], ha="center", va="center", fontsize=7.8, fontweight="bold", color=E.TINTA, linespacing=1.1)
                ax.text(x + cw / 2, y + 1.7, costo, ha="center", va="center", fontsize=7.4, color=E.TINTA)
            else:
                ax.add_patch(FancyBboxPatch((x, y), cw, hh, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.GRIS, ec=E.MEDIO, lw=0.9, hatch="///"))
                blanco(ax, x + cw / 2, y + hh / 2, "Sin producto P", fs=7.4)
    E.guardar(fig, "c12_f02")

# ============================================================================== F12.3
def f03():
    fig, ax = libre("Tres rutas conectan productos y efectos; la de los artículos es la más débil",
                    "Flujo causal Output (PERS-P) a Outcome (PERS-E) con mecanismo y supuesto crítico; mecanismos INFERIDOS")
    XO, WO = 1, 27; XM, WM = 37, 31; XE, WE = 78, 21
    for x, w, t in ((XO, WO, "Output (PERS-P)"), (XM, WM, "Mecanismo de cambio (INFERIDO)"), (XE, WE, "Outcome (PERS-E)")):
        ax.text(x + w / 2, 67.3, t, ha="center", va="center", fontsize=9.5, fontweight="bold", color=E.TINTA)
    def pchip(y, c, h=7.2, borde=E.AZUL, ls="-", hatch=None):
        ax.add_patch(FancyBboxPatch((XO, y), WO, h, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.GRIS if hatch else E.CLARO, ec=borde, lw=1.4, ls=ls))
        ax.text(XO + 1.0, y + h - 1.5, c.replace("PERS-", ""), ha="left", va="center", fontsize=8, fontweight="bold", color=E.TINTA)
        ax.text(XO + WO / 2, y + (h - 2.4) / 2, W(IND[c]["nombre"], 30), ha="center", va="center", fontsize=7.4, color=E.TINTA, linespacing=1.05)
        return (XO + WO + 0.2, y + h / 2)
    def mbox(yc, txt, h=12.5):
        ax.add_patch(FancyBboxPatch((XM, yc - h / 2), WM, h, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.GRIS, ec=E.TINTA, lw=1.2))
        ax.text(XM + WM / 2, yc, W(txt, 44), ha="center", va="center", fontsize=7.9, color=E.TINTA, linespacing=1.1)
    def ebox(yc, c, nxt, h=10.5):
        ax.add_patch(FancyBboxPatch((XE, yc - h / 2), WE, h, boxstyle="round,pad=0.2,rounding_size=0.6", fc=E.MEDIO, ec=E.TINTA, lw=1.4))
        ax.text(XE + 1.0, yc + h / 2 - 1.6, c.replace("PERS-", ""), ha="left", va="center", fontsize=8.4, fontweight="bold", color=E.TINTA)
        ax.text(XE + WE / 2, yc - 0.6, W(IND[c]["nombre"], 20), ha="center", va="center", fontsize=7.6, color=E.TINTA, linespacing=1.05)
        ax.text(XE + WE / 2, yc - h / 2 - 1.8, nxt, ha="center", va="center", fontsize=7, color=E.TINTA)
    lanes = [
        dict(yc=51.5, ps=[("PERS-P01", 54.6), ("PERS-P02", 45.2)], mech="Las lecturas corregidas en el gateway tienen error conocido y llegan en cantidad suficiente; los umbrales se fijan sobre datos verificados.",
             e="PERS-E02", nxt="alimenta PERS-S01", sc="SC-1 y SC-2", dash=[]),
        dict(yc=30.5, ps=[("PERS-P04", 33.4), ("PERS-P03", 23.0)], mech="El co-diseño de umbrales eleva la utilidad percibida y la facilidad de uso del tablero. La revisión por pares eleva la confianza (vía débil).",
             e="PERS-E01", nxt="alimenta PERS-S01", sc="SC-3", dash=["PERS-P03"]),
        dict(yc=9.8, ps=[("PERS-P01", 12.6), ("PERS-P04", 3.2)], mech="La práctica supervisada sobre la red y el tablero reales instala las competencias de mantenimiento, lectura y operación.",
             e="PERS-E03", nxt="alimenta PERS-S02", sc="SC-4", dash=[]),
    ]
    for ln in lanes:
        mbox(ln["yc"], ln["mech"])
        for c, y in ln["ps"]:
            weak = c in ln["dash"]
            p0 = pchip(y, c, ls=(0, (4, 3)) if weak else "-", hatch="///" if weak else None)
            E.flecha(ax, p0, (XM - 0.4, ln["yc"]), color=E.TINTA, lw=1.1 if weak else 1.5, ls=(0, (4, 3)) if weak else "-")
        ebox(ln["yc"], ln["e"], ln["nxt"])
        E.flecha(ax, (XM + WM + 0.4, ln["yc"]), (XE - 0.4, ln["yc"]), color=E.TINTA, lw=1.5)
        blanco(ax, (XM + WM + XE) / 2, ln["yc"] + 2.3, "Supuesto\n" + ln["sc"], fs=7.3, bold=True)
    ax.text(1, -0.4, "Línea continua: ruta con mecanismo plausible. Línea discontinua y recuadro gris: hipótesis débil sin evidencia propia en el corpus (VACIO).",
            ha="left", va="center", fontsize=7.6, color=E.TINTA)
    E.guardar(fig, "c12_f03")

# ============================================================================== F12.4
def f04():
    n = D.RIESGO
    fig, ax = libre("Los cinco indicadores de riesgo alto son los de efecto y sostenibilidad",
                    f"Semáforo ex ante de 15 indicadores PERS al 13 de octubre de 2026: riesgo de la ficha (alto {n['Alto']}, medio {n['Medio']}, bajo {n['Bajo']})")
    metas = {"PERS-R01": "100 nodos y 10 gateways", "PERS-R02": "6 ciclos", "PERS-R03": "≥ 99,0 %", "PERS-R04": "|desviación| ≤ 5 %",
             "PERS-R05": "≥ 60.000 horas-nodo", "PERS-R06": "100 %", "PERS-P01": "100 / 10 al mes 24", "PERS-P02": "1 registro vigente",
             "PERS-P03": "2 sometidos, ≥ 1 aceptado", "PERS-P04": "29 actividades", "PERS-E01": "≥ 75 % al mes 24", "PERS-E02": "≥ 30 % de reducción",
             "PERS-E03": "≥ 60 personas", "PERS-S01": "≥ 80 % a 12 meses", "PERS-S02": "≥ 70 % a 12 meses"}
    assert "99,0" in IND["PERS-R03"]["mf"] and "5 %" in IND["PERS-R04"]["mf"] and "29 actividades" in IND["PERS-P04"]["mf"]
    assert "75 %" in IND["PERS-E01"]["mf"] and "30 %" in IND["PERS-E02"]["mf"] and "60 personas" in IND["PERS-E03"]["mf"]
    assert "80 %" in IND["PERS-S01"]["mf"] and "70 %" in IND["PERS-S02"]["mf"] and "6 ciclos" in IND["PERS-R02"]["mf"]
    sem = {"Alto": ("ROJO · alto", E.AZUL, "xx"), "Medio": ("AMARILLO · medio", E.MEDIO, "///"), "Bajo": ("VERDE · bajo", E.GRIS, "...")}
    cx = dict(cod=1.0, nom=11.0, sem=48.5, lb=67.0, mf=83.0)
    H = 3.05; y = 66.2
    for k, t in (("cod", "Código"), ("nom", "Indicador"), ("sem", "Semáforo ex ante"), ("lb", "Línea base"), ("mf", "Meta final")):
        ax.text(cx[k], y, t, ha="left", va="center", fontsize=8.4, fontweight="bold", color=E.TINTA)
    ax.plot([0.5, 99.5], [y - 1.7, y - 1.7], color=E.TINTA, lw=1.2)
    y -= 3.5
    grupos = {"R": "R · Proceso · Output · frecuencia mensual", "P": "P · Producto · Output · frecuencia trimestral",
              "E": "E · Efecto · Outcome · frecuencia trimestral o semestral", "S": "S · Sostenibilidad · Impact · frecuencia anual tras el cierre"}
    for niv in "RPES":
        ax.add_patch(Rectangle((0.5, y - H / 2 + 0.2), 99, H - 0.4, fc=E.GRIS, ec="none"))
        ax.text(cx["cod"], y, grupos[niv], ha="left", va="center", fontsize=8.0, fontweight="bold", color=E.TINTA)
        y -= H
        for c in [c for c in D.ORDEN if IND[c]["nivel"] == niv]:
            i = IND[c]
            ax.text(cx["cod"], y, c, ha="left", va="center", fontsize=7.6, fontweight="bold", color=E.TINTA)
            ax.text(cx["nom"], y, i["nombre"], ha="left", va="center", fontsize=7.6, color=E.TINTA)
            lab, fc, hh = sem[i["riesgo"]]
            ax.add_patch(Rectangle((cx["sem"], y - 1.2), 17.5, 2.4, fc=fc, ec=E.TINTA, lw=0.9, hatch=hh))
            blanco(ax, cx["sem"] + 8.75, y, lab, fs=6.9, bold=True)
            lb = i["lb"]
            if lb == "VACIO": lbt = "VACIO"
            elif lb.startswith("Se mide"): lbt = "VACIO: se mide en tramo 1"
            else: lbt = f"{lb} ({i['lb_nat']})"
            ax.text(cx["lb"], y, lbt, ha="left", va="center", fontsize=7.4, color=E.TINTA, fontweight="bold" if "VACIO" in lbt else "normal")
            ax.text(cx["mf"], y, metas[c], ha="left", va="center", fontsize=7.4, color=E.TINTA)
            y -= H
    # leyenda
    yl = 2.2
    for k, (lab, fc, hh) in enumerate([sem["Alto"], sem["Medio"], sem["Bajo"]]):
        xk = 1 + k * 25
        ax.add_patch(Rectangle((xk, yl - 1.0), 5, 2.0, fc=fc, ec=E.TINTA, lw=0.9, hatch=hh))
        cnt = {0: n["Alto"], 1: n["Medio"], 2: n["Bajo"]}[k]
        ax.text(xk + 6, yl, f"{lab.split(' · ')[0]}: riesgo {lab.split(' · ')[1]} ({cnt})", ha="left", va="center", fontsize=7.6, color=E.TINTA)
    ax.text(77, yl, "El semáforo es ex ante: no es un avance medido.", ha="left", va="center", fontsize=7.4, color=E.TINTA)
    E.guardar(fig, "c12_f04")

# ============================================================================== F12.5
def f05():
    mes_fin = 24; seg = D.ID["horizonte_posproyecto_meses"]; fin = mes_fin + seg
    cortes_R = list(range(1, 25)); cortes_P = list(range(3, 25, 3)); cortes_E3 = list(range(6, 25, 6)); cortes_S = [30, 36]
    fig, ax = E.lienzo(h1="Los indicadores de impacto se miden en los meses 30 a 36, tras el cierre", h2=None, figsize=(10, 7), grid=False)
    fig.subplots_adjust(left=0.20, right=0.985, top=0.88, bottom=0.10)
    fig.text(0.01, 0.905, "Cortes de medición, hitos H0 a H8 y compuertas C1 a C3; meses 1 a 36 (24 de ejecución y 12 de seguimiento)", ha="left", va="bottom", fontsize=10, color=E.TINTA)
    ax.set_xlim(0, fin + 0.8); ax.set_ylim(0.2, 11.2)
    ax.spines["left"].set_visible(False); ax.set_yticks([])
    ax.axvspan(mes_fin, fin + 0.5, fc=E.GRIS, ec=E.MEDIO, hatch="///", lw=0.6, zorder=0)
    ax.text(mes_fin + 7.4, 10.85, "Seguimiento posproyecto (PROPUESTO)", ha="center", va="center", fontsize=7.8, fontweight="bold", color=E.TINTA, bbox=dict(fc="white", ec="none", pad=1.2))
    filas = {"tramos": 9.6, "hitos": 8.0, "R": 6.3, "P": 5.2, "E3": 4.1, "S": 3.0, "ext": 1.7}
    nombres = {"tramos": "Tramos de despliegue", "hitos": "Hitos H0 a H8", "R": f"R01 a R06: mensual\n({len(cortes_R)} cortes)", "P": f"P01 a P04, E01 y E02:\ntrimestral ({len(cortes_P)} cortes)",
               "E3": f"E03: semestral\n({len(cortes_E3)} cortes)", "S": f"S01 y S02: anual tras el cierre\n({len(cortes_S)} cortes)", "ext": "Verificación externa\n(S07 y S08)"}
    for k, y in filas.items():
        ax.text(-0.8, y, nombres[k], ha="right", va="center", fontsize=8.3, color=E.TINTA, fontweight="bold")
        ax.plot([0, fin + 0.5], [y - 0.55, y - 0.55], color=E.MEDIO, lw=0.5, zorder=1)
    # tramos
    fills = [E.CLARO, E.MEDIO, E.CLARO]
    for t, fc in zip(M.TRAMOS, fills):
        ax.add_patch(Rectangle((t["m_ini"] - 1, filas["tramos"] - 0.38), t["m_fin"] - t["m_ini"] + 1, 0.76, fc=fc, ec=E.TINTA, lw=0.9))
        ax.text((t["m_ini"] - 1 + t["m_fin"]) / 2, filas["tramos"], f"Tramo {t['id']}: {t['nodos']} nodos", ha="center", va="center", fontsize=7.4, color=E.TINTA)
    # compuertas
    for t in M.TRAMOS:
        x = t["mes_compuerta"]
        ax.plot([x, x], [0.7, 10.3], color=E.TINTA, lw=1.1, ls=(0, (5, 3)), zorder=2)
        ax.text(x, 10.85, t["compuerta"], ha="center", va="center", fontsize=8.5, fontweight="bold", color=E.TINTA)
    # hitos
    for h, d in D.HIT.items():
        ax.plot(d["mes"], filas["hitos"], marker="D", ms=7, mfc=E.AZUL, mec=E.TINTA, mew=1.0, ls="none", zorder=5)
        blanco(ax, d["mes"], filas["hitos"] + 0.66, h, fs=7.4, bold=True)
    # cortes
    ax.plot(cortes_R, [filas["R"]] * len(cortes_R), "o", ms=5.2, mfc=E.CLARO, mec=E.TINTA, mew=0.8, ls="none", zorder=4)
    ax.plot(cortes_P, [filas["P"]] * len(cortes_P), "s", ms=6.6, mfc=E.MEDIO, mec=E.TINTA, mew=0.8, ls="none", zorder=4)
    ax.plot(cortes_E3, [filas["E3"]] * len(cortes_E3), "^", ms=7.8, mfc=E.AZUL, mec=E.TINTA, mew=0.8, ls="none", zorder=4)
    ax.plot(cortes_S, [filas["S"]] * 2, "*", ms=11, mfc=E.AZUL, mec=E.TINTA, mew=0.8, ls="none", zorder=4)
    ax.text(30, filas["S"] + 0.62, "Mes 30: S01", ha="center", va="center", fontsize=7.2, color=E.TINTA)
    ax.text(36.4, filas["S"] - 0.62, "Mes 36: S01 y S02", ha="right", va="center", fontsize=7.2, color=E.TINTA)
    # verificación externa: evaluaciones S07 (12 y 24) y ensayo independiente S08 (meses 20 a 24)
    B_ = D.B
    assert B_["S07"]["m_ini"] == 12 and B_["S07"]["m_fin"] == 24 and (B_["S08"]["m_ini"], B_["S08"]["m_fin"]) == (20, 24)
    ax.add_patch(Rectangle((B_["S08"]["m_ini"] - 1, filas["ext"] - 0.22), B_["S08"]["m_fin"] - B_["S08"]["m_ini"] + 1, 0.44, fc=E.CLARO, ec=E.TINTA, lw=0.9, hatch="xx", zorder=3))
    ax.plot([12, 24], [filas["ext"]] * 2, "P", ms=8.5, mfc=E.AZUL, mec=E.TINTA, mew=0.8, ls="none", zorder=5)
    ax.text(12, filas["ext"] - 0.62, "Evaluación externa (mes 12)", ha="center", va="center", fontsize=7.0, color=E.TINTA)
    ax.text(21.6, filas["ext"] + 0.62, "Ensayo independiente S08 (meses 20 a 24)", ha="center", va="center", fontsize=7.0, color=E.TINTA)
    ax.text(fin + 0.45, filas["ext"] - 0.62, "Evaluación externa final (mes 24)", ha="right", va="center", fontsize=7.0, color=E.TINTA)
    ax.set_xticks([0, 3, 6, 9, 12, 17, 19, 24, 30, 36]); ax.set_xticklabels(["0", "3", "6", "9", "12", "17", "19", "24", "30", "36"], fontsize=8.5)
    ax.set_xlabel("Mes de calendario (0 = inicio de la ejecución; cada marca en el fin del mes)", fontsize=8.8)
    E.guardar(fig, "c12_f05")

if __name__ == "__main__":
    f01(); f02(); f03(); f04(); f05()
    print("ok")
