# -*- coding: utf-8 -*-
"""Figuras del documento 1000X-04 (capítulo de estrategia), prefijo X4.
Genera figs/out/cX4_f01 ... cX4_f08 (.png y .svg) con la plantilla única estilo.py.
Todos los valores provienen del libro maestro (maestro.py, alternativas.py) o de F-INF con página; no hay semilla aleatoria.
Uso: python3 cX4_figuras.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(RAIZ, "figs"))
sys.path.insert(0, os.path.join(RAIZ, "maestro"))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Patch
import estilo as E
import maestro as M
import alternativas as A

T = E.TINTA


def n(v, dec=0):
    return E.num(v, dec)


def titulo(fig, h1):
    fig.suptitle(h1, fontsize=14, fontweight="bold", color=T, x=0.01, ha="left", y=0.995)


# ------------------------------------------------------------------ f01: no consumo (datos F-INF)
def f01():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={"width_ratios": [1.7, 1]})
    titulo(fig, "Solo 28 de 1.122 municipios cuentan con estaciones utilizables")
    etiquetas = ["Municipios del país", "Municipios que miden\nla calidad del aire", "Municipios con estaciones\nutilizables para estimar la carga",
                 "Municipios focalizados\npor el proyecto"]
    valores = [1122, 92, 28, 12]
    colores = [E.AZUL, E.MEDIO, E.CLARO, E.GRIS]
    tramas = ["", "///", "...", "xx"]
    y = np.arange(len(valores))[::-1]
    barras = ax1.barh(y, valores, color=colores, edgecolor=T, linewidth=0.9, height=0.62)
    for b, h in zip(barras, tramas):
        b.set_hatch(h)
    ax1.set_yticks(y)
    ax1.set_yticklabels(etiquetas, fontsize=9.5)
    E.etiquetar_barras(ax1, barras, fmt="{:,.0f}", horizontal=True, dy=4)
    ax1.set_xlim(0, 1350)
    ax1.set_xlabel("Número de municipios", fontsize=10)
    ax1.grid(axis="x"); ax1.grid(axis="y", visible=False)
    ax1.set_title("Municipios de Colombia, cifras del informe de vigilancia (F-INF)", fontsize=10, loc="left", pad=10)
    ax1.annotate("1.094 sin estaciones utilizables\n(CALCULADO: 1.122 menos 28)", xy=(1122, y[0]), xytext=(1150, y[1] - 0.15),
                 fontsize=9, color=T, ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color=T, lw=0.8))
    # panel B
    et2 = ["Estaciones\nreportadas", "Integradas a un sistema\nde vigilancia"]
    val2 = [209, 154]
    y2 = np.arange(2)[::-1]
    b2 = ax2.barh(y2, val2, color=[E.AZUL, E.MEDIO], edgecolor=T, linewidth=0.9, height=0.55)
    b2[1].set_hatch("///")
    ax2.set_yticks(y2); ax2.set_yticklabels(et2, fontsize=9.5)
    E.etiquetar_barras(ax2, b2, fmt="{:,.0f}", horizontal=True, dy=4)
    ax2.set_xlim(0, 260)
    ax2.set_xlabel("Número de estaciones", fontsize=10)
    ax2.grid(axis="x"); ax2.grid(axis="y", visible=False)
    ax2.set_title("Estaciones del país (192 fijas y 17 indicativas)", fontsize=10, loc="left", pad=10)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return E.guardar(fig, "cX4_f01")


# ------------------------------------------------------------------ f02: atributos ALT-01 frente a ALT-03
def f02():
    crit = {c[0]: c[2] for c in A.CRIT}
    attrs = [("PAFU: fiable", "Fiabilidad"), ("Viabilidad financiera", "Viabilidad financiera"), ("PAFU: accesible", "Accesibilidad"),
             ("Escalabilidad", "Escalabilidad"), ("PAFU: ubicua", "Ubicuidad")]
    v01 = [crit[a[0]][1] for a in attrs]
    v03 = [crit[a[0]][3] for a in attrs]
    nombres = [a[1] for a in attrs]
    fig, ax = E.lienzo(h1="La red corregida cede fiabilidad y gana costo, acceso y cobertura",
                       h2="Puntaje por atributo, escala de 1 (menor) a 9 (mayor); evaluación multicriterio, valores PROPUESTO", grid=False)
    y = np.arange(len(attrs))[::-1].astype(float)
    h = 0.34
    b1 = ax.barh(y + h / 2, v01, height=h, color=E.MEDIO, edgecolor=T, linewidth=0.9, hatch="///")
    b3 = ax.barh(y - h / 2, v03, height=h, color=E.AZUL, edgecolor=T, linewidth=0.9)
    E.etiquetar_barras(ax, b1, fmt="{:.0f}", horizontal=True, dy=4, fs=11)
    E.etiquetar_barras(ax, b3, fmt="{:.0f}", horizontal=True, dy=4, fs=11)
    ax.set_yticks(y); ax.set_yticklabels(nombres, fontsize=11)
    ax.set_xlim(0, 12.8); ax.set_xticks(range(0, 10))
    ax.set_xlabel("Puntaje (escala de 1 a 9)", fontsize=10.5)
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    # etiquetas directas de serie en el grupo superior
    ax.text(v01[0] + 0.75, y[0] + h / 2, "ALT-01: estación de referencia", fontsize=9.5, va="center", color=T)
    ax.text(v03[0] + 0.75, y[0] - h / 2, "ALT-03: red corregida en gateway", fontsize=9.5, va="center", color=T)
    tot = A.BASE
    ax.text(12.6, -0.78, f"Puntaje total ponderado: ALT-01 {n(tot[1], 2)}; ALT-03 {n(tot[3], 2)}", fontsize=9.5, ha="right", va="center", color=T)
    ax.set_ylim(-1.1, len(attrs) - 0.45)
    return E.guardar(fig, "cX4_f02")


# ------------------------------------------------------------------ f03: trabajos por realizar
def f03():
    fig, ax = E.lienzo_libre(h1="El comité y el operario contratan la medición para decidir y protegerse con evidencia defendible",
                             h2="Trabajos funcional, emocional y social por actor; INFERIDO de datos secundarios, sin entrevistas",
                             xlim=(0, 100), ylim=(0, 72))
    cols = [(21, "Funcional", E.AZUL), (47, "Emocional", E.MEDIO), (73, "Social", E.CLARO)]
    wcol = 24
    for x, nom, col in cols:
        E.caja(ax, x, 58, wcol, 7, nom, relleno=col, fs=11, bold=True)
    filas = [
        (38, "Comité de\ngestión del riesgo\n(15 comités,\nSUPUESTO)", E.CLARO,
         ["Decidir si emite, mantiene\no levanta una alerta\npor PM2,5 y PM10", "Decidir con confianza,\nsin temor a omitir\nni a dar falsa alarma",
          "Aparecer como autoridad\nque decide con evidencia\nante la comunidad"]),
        (18, "Operario de\nremoción", E.MEDIO,
         ["Saber cuándo reducir,\ndetener o reanudar\nla actividad", "Trabajar con la certeza\nde que el aviso\nes creíble",
          "Ser reconocido\nen la decisión\nsobre los umbrales"]),
    ]
    for y0, rot, col, textos in filas:
        E.caja(ax, 1.5, y0, 16.5, 15, rot, relleno=col, fs=9, bold=True)
        for (x, nom, c), tx in zip(cols, textos):
            E.caja(ax, x, y0, wcol, 15, tx, relleno=E.CAJA, fs=9.5)
    E.caja(ax, 21, 0.8, 76, 9, "Insumo común de los seis trabajos: una medición de PM2,5 y PM10\ncon error conocido frente a una referencia", relleno=E.GRIS, fs=10, bold=True)
    for x, nom, c in cols:
        E.flecha(ax, (x + wcol / 2, 17.6), (x + wcol / 2, 10.4))
    ax.text(1.5, 5.2, "Sin entrevistas ni\nobservación todavía:\nse validan en A3.1\n(meses 3 a 9)", fontsize=8.5, va="center", ha="left", color=T)
    return E.guardar(fig, "cX4_f03")


# ------------------------------------------------------------------ f04: ocho pasos de Kotter en 24 meses
def f04():
    pasos = [("1. Crear urgencia", 1, 2, 0), ("2. Formar la coalición guía", 2, 3, 0), ("3. Desarrollar visión y estrategia", 3, 9, 0),
             ("4. Comunicar la visión", 3, 24, 1), ("5. Empoderar la acción", 6, 24, 1), ("6. Generar victorias tempranas", 7, 17, 1),
             ("7. Consolidar las ganancias", 12, 19, 2), ("8. Anclar en la cultura", 18, 24, 2)]
    cols = [E.AZUL, E.MEDIO, E.CLARO]
    tramas = ["", "///", "..."]
    fig, ax = E.lienzo(h1="Los ocho pasos de Kotter se distribuyen en 24 meses y se anclan en las compuertas",
                       h2="Mes de ejecución (1 a 24); meses PROPUESTO; compuertas C1, C2 y C3 del cronograma del proyecto", grid=False)
    nfil = len(pasos)
    for i, (nom, a, b, f) in enumerate(pasos):
        y = nfil - i
        ax.barh(y, b - a + 1, left=a - 0.5, height=0.52, color=cols[f], edgecolor=T, linewidth=0.9, hatch=tramas[f])
        ax.text(a - 0.5 + (b - a + 1) + 0.25, y, f"mes {a}" if a == b else f"meses {a} a {b}", fontsize=8.5, va="center", ha="left", color=T)
    ax.set_yticks([nfil - i for i in range(nfil)])
    ax.set_yticklabels([p[0] for p in pasos], fontsize=10)
    ax.set_xlim(0, 28.5); ax.set_ylim(0.2, nfil + 1.35)
    ax.set_xticks([1, 3, 6, 9, 12, 15, 17, 21, 24])
    ax.set_xlabel("Mes de ejecución", fontsize=10.5)
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    for mes, nom in [(12, "C1"), (17, "C2"), (24, "C3")]:
        ax.axvline(mes + 0.5, color=T, linestyle="--", linewidth=1.0, ymax=0.93)
        ax.text(mes + 0.5, nfil + 1.12, f"{nom} (mes {mes})", fontsize=9, ha="center", va="bottom", fontweight="bold", color=T)
    qw = [(7, "QW1", "right"), (8, "QW2", "left"), (10, "QW3", "center"), (12, "QW4", "center"), (17, "QW5", "center")]
    yq = nfil - 5
    for mes, nom, ha in qw:
        ax.plot([mes], [yq], marker="D", markersize=8, markerfacecolor=E.BLANCO, markeredgecolor=T, markeredgewidth=1.2, zorder=5)
        dx = -0.15 if ha == "right" else 0.15 if ha == "left" else 0
        ax.text(mes + dx, yq + 0.42, nom, fontsize=8, ha=ha, va="bottom", color=T, fontweight="bold")
    from matplotlib.lines import Line2D
    handles = [Patch(facecolor=cols[0], edgecolor=T, hatch=tramas[0], label="Fase 1: crear el clima"),
               Patch(facecolor=cols[1], edgecolor=T, hatch=tramas[1], label="Fase 2: involucrar y habilitar"),
               Patch(facecolor=cols[2], edgecolor=T, hatch=tramas[2], label="Fase 3: implementar y sostener"),
               Line2D([0], [0], marker="D", color="none", markerfacecolor=E.BLANCO, markeredgecolor=T, markersize=8, label="Victoria temprana (QW1 a QW5)")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, -0.12), ncol=4, fontsize=9, frameon=False, columnspacing=1.2, handlelength=1.6)
    return E.guardar(fig, "cX4_f04")


# ------------------------------------------------------------------ f05: bucles de aprendizaje
def f05():
    fig, ax = E.lienzo_libre(h1="El bucle simple corrige la acción cada mes y el bucle doble revisa los supuestos en las compuertas",
                             h2="Bucles de aprendizaje del proyecto (Argyris y Schön, 1978; 4.4-MDR.11); diagrama conceptual sin datos numéricos",
                             xlim=(0, 100), ylim=(0, 72))
    def ruta(pts, ls="-"):
        xs_, ys_ = zip(*pts)
        ax.plot(xs_[:-1], ys_[:-1], color=T, lw=1.3, ls=ls, solid_capstyle="butt")
        E.flecha(ax, pts[-2], pts[-1], ls=ls)
    # bucle simple
    ax.text(2, 67.5, "BUCLE SIMPLE: ¿la acción se ejecuta bien? (mensual)", fontsize=11, fontweight="bold", color=T, va="center")
    E.caja(ax, 3, 46, 24, 14, "Acción:\noperar nodos, gateways\ny corrección", relleno=E.CLARO)
    E.caja(ax, 38, 46, 27, 14, "Resultado:\nNRMSE, R², disponibilidad\ny pérdida de paquetes", relleno=E.CLARO)
    E.caja(ax, 76, 46, 21, 14, "¿Desvío frente\nal umbral?", relleno=E.MEDIO, bold=True)
    E.flecha(ax, (27.6, 53), (37.4, 53))
    E.flecha(ax, (65.6, 53), (75.4, 53))
    ruta([(82, 45.6), (82, 41.2), (15, 41.2), (15, 45.4)])
    ax.text(48.5, 38.9, "Sí: ajustar la acción (retrospectiva e indicadores mensuales)", fontsize=9.5, ha="center", va="center", color=T)
    ruta([(86.5, 60.4), (86.5, 64.2), (15, 64.2), (15, 60.6)])
    ax.text(50, 65.4, "No: continuar la acción", fontsize=9.5, ha="center", va="center", color=T)
    # bucle doble
    ax.text(2, 31.5, "BUCLE DOBLE: ¿la acción es la correcta? (compuertas, sesión trimestral, evaluación externa)", fontsize=11, fontweight="bold", color=T, va="center")
    E.caja(ax, 3, 12, 22, 14, "Supuestos y metas:\nSC-1 a SC-4", relleno=E.MEDIO, bold=True)
    E.caja(ax, 34, 12, 16, 14, "Acción", relleno=E.CLARO)
    E.caja(ax, 58, 12, 16, 14, "Resultado", relleno=E.CLARO)
    E.caja(ax, 80, 12, 17, 14, "¿Desvío\npersistente?", relleno=E.MEDIO, bold=True)
    E.flecha(ax, (25.6, 19), (33.4, 19))
    E.flecha(ax, (50.6, 19), (57.4, 19))
    E.flecha(ax, (74.6, 19), (79.4, 19))
    ruta([(86, 11.6), (86, 7.6), (14, 7.6), (14, 11.4)])
    ax.text(50, 4.6, "Sí: cuestionar los supuestos en C1 (mes 12), C2 (mes 17) y evaluaciones externas (meses 12 y 24)", fontsize=9.5, ha="center", va="center", color=T)
    E.flecha(ax, (93, 45.6), (93, 26.6), ls="--")
    ax.text(91.8, 36.2, "Si persiste", fontsize=9, ha="right", va="center", color=T)
    return E.guardar(fig, "cX4_f05")


# ------------------------------------------------------------------ f06: EMV por riesgo
def f06():
    riesgos = sorted(M.RISKS, key=lambda r: -r["emv"])
    cortos = {"R-FIN-01": "Devaluación del peso", "R-TEC-01": "Saturación de cabezales", "R-ORG-02": "Custodios sin partida",
              "R-EXT-01": "Vías bloqueadas", "R-ORG-01": "Comités sin adopción", "R-TEC-04": "Modelo sin generalización",
              "R-TEC-03": "Enlace celular caído", "R-TEC-02": "Baterías agotadas", "R-EXT-02": "Robo o vandalismo",
              "R-FIN-02": "Contrapartida sin certificar", "R-JUR-01": "Patente de terceros", "R-DAT-01": "Incidente de ciberseguridad"}
    total = sum(r["emv"] for r in riesgos) / M.M
    top2 = (riesgos[0]["emv"] + riesgos[1]["emv"]) / M.M
    pct = top2 / total * 100
    fig, ax = E.lienzo(h1=f"Dos riesgos concentran {n(pct, 1)} % del valor monetario esperado de la reserva",
                       h2="Valor monetario esperado (EMV) por riesgo, en millones de COP; etiqueta: EMV (probabilidad)", grid=False)
    y = np.arange(len(riesgos))[::-1]
    estilo = {"EXTREMO": (E.AZUL, ""), "ALTO": (E.MEDIO, "///"), "MEDIO": (E.CLARO, "...")}
    barras = []
    for yy, r in zip(y, riesgos):
        c, t = estilo[r["nivel"]]
        b = ax.barh(yy, r["emv"] / M.M, color=c, edgecolor=T, linewidth=0.9, height=0.66, hatch=t)
        barras.append(b[0])
        ax.text(r["emv"] / M.M + 3, yy, f"{n(r['emv'] / M.M, 1)} ({r['prob']} %)", fontsize=9.5, fontweight="bold", va="center", color=T)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{r['id']}  {cortos[r['id']]}" for r in riesgos], fontsize=10)
    ax.set_xlim(0, 235)
    ax.set_xlabel("EMV en millones de COP", fontsize=10.5)
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    # llave de los dos primeros
    ax.annotate("", xy=(197, y[0] + 0.33), xytext=(197, y[1] - 0.33), arrowprops=dict(arrowstyle="-", color=T, lw=1.2))
    ax.text(201, (y[0] + y[1]) / 2, f"{n(top2, 1)} millones\n= {n(pct, 1)} % del total", fontsize=9.5, va="center", ha="left", color=T)
    handles = [Patch(facecolor=estilo[k][0], edgecolor=T, hatch=estilo[k][1], label=f"Nivel {k}") for k in ("EXTREMO", "ALTO", "MEDIO")]
    ax.legend(handles=handles, loc="lower right", fontsize=9.5, frameon=False, bbox_to_anchor=(1.0, 0.12))
    ax.text(232, -0.95, f"Suma de EMV: {n(total, 1)}; reserva de contingencia: {n(M.RESERVA / M.M, 1)} (millones de COP)", fontsize=9.5, ha="right", va="center", color=T)
    ax.set_ylim(-1.35, len(riesgos) - 0.4)
    return E.guardar(fig, "cX4_f06")


# ------------------------------------------------------------------ f07: matriz de escenarios
def f07():
    fig, ax = E.lienzo_libre(h1="Los escenarios se distinguen por el cumplimiento de los supuestos de medición y de custodia",
                             h2="Plano de supuestos críticos de 4.4-MDR.8; la posición indica supuestos cumplidos y no una probabilidad (DEC-F11)",
                             xlim=(0, 100), ylim=(0, 72))
    xl, xr, wcol = 17, 59, 37
    filas = {"top": (46, 15), "mid": (29, 14), "bot": (12, 14)}
    # cabeceras de columna
    ax.text(xl + wcol / 2, 64.5, "SC-1 y SC-2 no se cumplen", fontsize=10, ha="center", va="center", fontweight="bold", color=T)
    ax.text(xr + wcol / 2, 64.5, "SC-1 y SC-2 se cumplen", fontsize=10, ha="center", va="center", fontweight="bold", color=T)
    ax.text(xl + wcol + 2, 68.5, "Eje horizontal: supuestos de medición y de red (SC-1 y SC-2)", fontsize=9.5, ha="center", va="center", color=T)
    ax.text(1.5, 62.5, "Eje vertical:\nsupuestos de uso\ny de custodia\n(SC-3 y SC-4)", fontsize=9, ha="left", va="center", color=T)
    # cabeceras de fila
    ax.text(1.5, filas["top"][0] + 7.5, "SC-3 y SC-4\nse cumplen", fontsize=9.5, ha="left", va="center", fontweight="bold", color=T)
    ax.text(1.5, filas["mid"][0] + 7, "SC-4 se cumple\nen parte", fontsize=9.5, ha="left", va="center", fontweight="bold", color=T)
    ax.text(1.5, filas["bot"][0] + 7, "SC-3 y SC-4\nfallan", fontsize=9.5, ha="left", va="center", fontweight="bold", color=T)
    # celdas
    E.caja(ax, xr, filas["top"][0], wcol, filas["top"][1], "OPTIMISTA\nSC-1 a SC-4 se cumplen", relleno=E.MEDIO, fs=11, bold=True)
    E.caja(ax, xr, filas["mid"][0], wcol, filas["mid"][1], "BASE\nSC-1 a SC-3 se cumplen", relleno=E.CLARO, fs=11, bold=True)
    E.caja(ax, xr, filas["bot"][0], wcol, filas["bot"][1], "PESIMISTA\nfuturo conservador:\nSC-3 y SC-4 fallan", relleno=E.GRIS, fs=10.5, bold=True)
    E.caja(ax, xl, filas["bot"][0], wcol, filas["bot"][1], "PESIMISTA\nrama de falla de SC-1:\nC1 detiene el tramo 2", relleno=E.GRIS, fs=10.5, bold=True)
    # celda no escenario (discontinua)
    p = FancyBboxPatch((xl, filas["mid"][0]), wcol, filas["top"][0] + filas["top"][1] - filas["mid"][0], boxstyle="round,pad=0.25,rounding_size=0.8",
                       fc="none", ec=T, lw=1.2, ls="--")
    ax.add_patch(p)
    ax.text(xl + wcol / 2, (filas["mid"][0] + filas["top"][0] + filas["top"][1]) / 2,
            "Uso sin medición verificada:\nriesgo de falsa seguridad,\nno es un escenario del plan", fontsize=10, ha="center", va="center", color=T)
    # disrupción
    p2 = FancyBboxPatch((xl, 0.8), wcol * 2 + (xr - xl - wcol), 6.2, boxstyle="round,pad=0.25,rounding_size=0.8", fc=E.BLANCO, ec=T, lw=1.2, ls="--")
    ax.add_patch(p2)
    ax.text((xl + xr + wcol) / 2, 3.9, "DISRUPCIÓN: un evento externo (TdR, TRM, vías bloqueadas, cambio normativo)\npuede desplazar el proyecto a cualquier celda",
            fontsize=9.5, ha="center", va="center", fontweight="bold", color=T)
    for xx in (xl + wcol / 2, xr + wcol / 2):
        E.flecha(ax, (xx, 8.4), (xx, 11.2), estilo="<|-|>", ls="--")
    return E.guardar(fig, "cX4_f07")


# ------------------------------------------------------------------ f08: mapa estratégico
def f08():
    fig, ax = E.lienzo_libre(h1="Los tres marcos transforman capacidades en resultados verificables y contribuyen a un impacto de continuidad",
                             h2="Mapa estratégico por niveles; metas del libro maestro (DECLARADO o PROPUESTO); el impacto es contribución sobre el techo de rendición de cuentas",
                             xlim=(0, 100), ylim=(0, 72))
    niveles = [("IMPACTO\n(12 meses tras\nel cierre)", 56), ("RESULTADOS\n(mes 24)", 38.5), ("PROCESOS\nINTERNOS", 22), ("CAPACIDADES\nY RECURSOS", 4.5)]
    for nom, y in niveles:
        ax.text(1.2, y + 5.2, nom, fontsize=9.5, fontweight="bold", va="center", ha="left", color=T)
    xs = [17, 46, 75]
    w = 24
    # capacidades
    cap = ["Equipo: 14 líneas\nde personal", "Alianzas: IES, empresa\ntecnológica, alcaldías\ny UNGRD (SUPUESTO)", "Recursos: SGR 9.267,26\n+ contrapartida 2.110\n(millones de COP)"]
    for x, t in zip(xs, cap):
        E.caja(ax, x, 4.5, w, 11, t, relleno=E.CAJA, fs=9)
    # procesos
    pro = [("Christensen:\nposicionamiento", E.MEDIO), ("Kotter:\ncambio institucional", E.MEDIO), ("Argyris:\naprendizaje", E.MEDIO)]
    for x, (t, c) in zip(xs, pro):
        E.caja(ax, x, 22, w, 11, t, relleno=c, fs=10, bold=True)
        E.flecha(ax, (x + w / 2, 16.3), (x + w / 2, 21.4))
    # resultados (4 cajas)
    res_x = [17, 38.5, 60, 81.5]
    wr = 17.5
    res = ["OE1: R² ≥ 0,70 y\nNRMSE ≤ 30 %;\nTRL 7", "OE2: disponibilidad\n≥ 90 %; 100 nodos\ny 10 gateways", "OE3: uso ≥ 75 %\nde los comités;\n≥ 60 personas", "Conocimiento:\n2 artículos sometidos\ny 1 registro"]
    for x, t in zip(res_x, res):
        E.caja(ax, x, 38.5, wr, 12, t, relleno=E.CLARO, fs=8.8)
    # flechas procesos -> resultados
    E.flecha(ax, (xs[0] + w / 2, 33.4), (res_x[0] + wr / 2, 37.9))
    E.flecha(ax, (xs[1] + w / 2, 33.4), (res_x[2] + wr / 2, 37.9))
    for rx in res_x:
        E.flecha(ax, (xs[2] + w / 2, 33.4), (rx + wr / 2, 37.9), ls="--")
    # impacto
    p1 = FancyBboxPatch((17, 56), 36, 11, boxstyle="round,pad=0.25,rounding_size=0.8", fc=E.BLANCO, ec=T, lw=1.2, ls="--")
    p2 = FancyBboxPatch((58, 56), 38, 11, boxstyle="round,pad=0.25,rounding_size=0.8", fc=E.BLANCO, ec=T, lw=1.2, ls="--")
    ax.add_patch(p1); ax.add_patch(p2)
    ax.text(35, 61.5, "PERS-S01: protocolo activado\nante superación de umbral ≥ 80 %", fontsize=9.3, ha="center", va="center", color=T)
    ax.text(77, 61.5, "PERS-S02: red operada bajo\ncustodia con partida ≥ 70 %", fontsize=9.3, ha="center", va="center", color=T)
    for rx in res_x[:3]:
        E.flecha(ax, (rx + wr / 2, 50.9), (35, 55.4), ls="--")
    for rx in (res_x[2], res_x[3]):
        E.flecha(ax, (rx + wr / 2, 50.9), (77, 55.4), ls="--")
    return E.guardar(fig, "cX4_f08")


if __name__ == "__main__":
    for f in (f01, f02, f03, f04, f05, f06, f07, f08):
        print(f())
