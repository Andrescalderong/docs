# -*- coding: utf-8 -*-
"""Figuras del capítulo 13 (Impactos). Genera c13_f00 a c13_f05 en figs/out/ (png y svg, fondo transparente).
Todos los datos provienen de FICHA_MAESTRA.md, de indicadores.py y de la sección 4.4-MDR.8 (A-TDC). Sin parámetros aleatorios."""
import os, sys, math, textwrap
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import estilo as E
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import matplotlib.pyplot as plt

T = E.TINTA


def caja2(ax, x, y, w, h, texto, relleno=E.CAJA, ls="-", fs=8.2, bold=False, lw=1.2, ha="center", va="center", pad=0.25):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={pad},rounding_size=0.8", fc=relleno, ec=T, lw=lw, ls=ls)
    ax.add_patch(p)
    tx = x + w / 2 if ha == "center" else x + 1.0
    ty = y + h / 2 if va == "center" else y + h - 1.0
    ax.text(tx, ty, texto, ha=ha, va=va, fontsize=fs, color=T, fontweight="bold" if bold else "normal", linespacing=1.25)
    return p


def etiqueta(ax, x, y, texto, fs=8, bold=True, fc=E.BLANCO):
    ax.text(x, y, texto, ha="center", va="center", fontsize=fs, color=T, fontweight="bold" if bold else "normal",
            bbox=dict(boxstyle="round,pad=0.25", fc=fc, ec=T, lw=0.8))


def flecha(ax, p0, p1, ls="-", lw=1.3, rad=0.0, color=T):
    a = FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11, color=color, lw=lw, ls=ls,
                        connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0)
    ax.add_patch(a)


# ---------------------------------------------------------------- F13.0 teoría del cambio
def f00():
    fig, ax = E.lienzo_libre(h1="El proyecto responde por los niveles 1 y 2; los niveles 3 y 4 son contribución",
                             h2="Teoría del cambio A-TDC: 11 nodos, 12 relaciones y 4 supuestos críticos (SC-1 a SC-4); naturaleza PROPUESTO",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    colx = [1.5, 28.5, 55.5, 81.0]
    colw = [19, 19, 19, 18.0]
    bh = 9
    nodos = {
        "P1": (0, 50, "P1 Red de nodos con\ncorrección local y\nrepuestos"),
        "P2": (0, 39, "P2 Referencia,\nprotocolo y sorteo\nsemanal"),
        "P3": (0, 27, "P3 Gemelo digital y\ntablero con umbrales\npropuestos"),
        "P4": (0, 11, "P4 Acuerdos de custodia\ny portafolio de\nfinanciación"),
        "R2": (1, 53, "R2 Datos suficientes:\nnodos activos y\nlatencia especificada"),
        "R1": (1, 42, "R1 Error reducido y\nverificable frente\na la referencia"),
        "R3": (1, 27, "R3 Fórmula local del\níndice y umbrales\nvalidados"),
        "I2": (2, 50, "I2 Alertas oportunas\ncon falsas alarmas\ndentro del umbral"),
        "I1": (2, 27, "I1 Protocolos de gestión\ndel riesgo incorporan\nlas alertas"),
        "I3": (2, 11, "I3 Servicio con custodios\ndespués del mes 24"),
        "IM": (3, 33, "IM Operarios y\ncomunidades\nprotegidos por\nalertas basadas en\nmediciones\nverificadas"),
    }
    pos = {}
    for k, (c, yc, txt) in nodos.items():
        h = 17 if k == "IM" else bh
        x = colx[c]; w = colw[c]; y = yc - h / 2
        bajo = c <= 1
        caja2(ax, x, y, w, h, txt, relleno=E.MEDIO if bajo else E.CLARO, ls="-" if bajo else (0, (4, 2)), bold=False)
        pos[k] = (x, y, w, h)

    def der(k): x, y, w, h = pos[k]; return (x + w + 0.25, y + h / 2)
    def izq(k): x, y, w, h = pos[k]; return (x - 0.25, y + h / 2)

    # relaciones (de, a, supuesto)
    rel = [("P1", "R2", "SC-2"), ("P1", "R1", "SC-1"), ("P2", "R1", "SC-1"), ("P3", "R3", "SC-3"), ("P4", "I3", "SC-4"),
           ("R3", "I1", "SC-3"), ("R1", "I2", None), ("R2", "I2", None), ("I1", "IM", "SC-3"), ("I2", "IM", None), ("I3", "IM", "SC-4")]
    for de, a, sc in rel:
        p0 = der(de); p1 = izq(a)
        if a == "IM":
            x, y, w, h = pos["IM"]
            yy = {"I1": y + 4.0, "I2": y + h - 3.0, "I3": y + 1.5}[de]
            p1 = (x - 0.25, yy)
        if (de, a) == ("P1", "R1"): p0 = (p0[0], p0[1] - 1.5); p1 = (p1[0], p1[1] + 1.2)
        if (de, a) == ("P1", "R2"): p0 = (p0[0], p0[1] + 1.5)
        if (de, a) == ("R1", "I2"): p0 = (p0[0], p0[1] + 1.5); p1 = (p1[0], p1[1] - 1.5)
        if (de, a) == ("R2", "I2"): p0 = (p0[0], p0[1] - 1.5); p1 = (p1[0], p1[1] + 1.5)
        flecha(ax, p0, p1)
        if sc:
            if (de, a) == ("P4", "I3"): mx, my = 40, p0[1]
            elif a == "IM": mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
            else: mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
            etiqueta(ax, mx, my, sc)
    # bucle de demanda I1 -> P4
    x1, y1, w1, h1 = pos["I1"]; x4, y4, w4, h4 = pos["P4"]
    yb = 19.0
    ax.plot([x1 + w1 / 2, x1 + w1 / 2], [y1 - 0.25, yb], color=T, lw=1.3, ls=(0, (4, 2)))
    ax.plot([x1 + w1 / 2, x4 + w4 / 2], [yb, yb], color=T, lw=1.3, ls=(0, (4, 2)))
    flecha(ax, (x4 + w4 / 2, yb), (x4 + w4 / 2, y4 + h4 + 0.25), ls=(0, (4, 2)))
    etiqueta(ax, 38, yb, "Bucle de demanda", bold=False)
    # techo
    ax.plot([52, 52], [3.5, 64.5], color=T, lw=1.6, ls=(0, (6, 3)))
    ax.text(52, 66.8, "Techo de rendición de cuentas", ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    ax.text(26, 3.4, "Bajo el techo: el proyecto responde", ha="center", va="center", fontsize=8.5, color=T)
    ax.text(77, 3.4, "Sobre el techo: contribución", ha="center", va="center", fontsize=8.5, color=T)
    encabezados = ["Nivel 1\nProductos", "Nivel 2\nResultados inmediatos", "Nivel 3\nResultados intermedios", "Nivel 4\nImpacto"]
    for i, t in enumerate(encabezados):
        ax.text(colx[i] + colw[i] / 2, 61.6, t, ha="center", va="center", fontsize=8.8, fontweight="bold", color=T)
    ax.text(50, 0.4, "Borde continuo: bajo el techo. Borde discontinuo: contribución. SC-1 a SC-4: supuestos (SUPUESTO).",
            ha="center", va="center", fontsize=8, color=T)
    return E.guardar(fig, "c13_f00")


# ---------------------------------------------------------------- F13.1 cadena social con escalera ASC
def f01():
    fig, ax = E.lienzo_libre(h1="El proyecto compromete los peldaños 1 a 3; el peldaño 4 es aspiracional y posterior al cierre",
                             h2="Escalera de apropiación social (ASC), indicadores PERS y metas de la ficha de indicadores; naturaleza DECLARADO",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    x0 = [1.5, 26.5, 51.5, 76.5]
    w = 22
    alt = [28, 34, 40, 46]
    rell = [E.CLARO, E.CLARO, E.MEDIO, E.GRIS]
    ls = ["-", "-", "-", (0, (4, 2))]
    contenido = [
        ("Nivel 1\nInformación", "ASC-COM", "Boletines, cartillas y\npágina del proyecto", "Meta: 100 % durante el\nprimer tercio de la ejecución", "PERS-P04"),
        ("Nivel 2\nConsulta", "ASC-COM y ASC-PART", "Grupos focales,\nencuestas y foros", "Meta: 100 % durante la\nprimera mitad", "PERS-P04"),
        ("Nivel 3\nColaboración activa", "ASC-PART", "Co-diseño de umbrales,\nvalidación comunitaria\ny comité asesor", "Meta: mínimo 3 actividades\ncon acta firmada", "PERS-E01, PERS-E02\ny PERS-E03"),
        ("Nivel 4\nEmpoderamiento", "ASC-PART y formación", "Formación de formadores\nlocales y observatorio\ncomunitario", "Aspiracional: 1 actividad\ncon plan de sostenibilidad", "PERS-S01 y PERS-S02\n(6 a 12 meses tras cierre)"),
    ]
    base = 4
    for i in range(4):
        caja2(ax, x0[i], base, w, alt[i], "", relleno=rell[i], ls=ls[i])
        tit, cod, act, meta, pers = contenido[i]
        top = base + alt[i]
        ax.text(x0[i] + w / 2, top - 3.4, tit, ha="center", va="center", fontsize=9, fontweight="bold", color=T, linespacing=1.2)
        ax.text(x0[i] + w / 2, top - 7.4, cod, ha="center", va="center", fontsize=8, color=T)
        ytxt = top - 10.0
        ax.text(x0[i] + 1.2, ytxt, act, ha="left", va="top", fontsize=8, color=T, linespacing=1.25)
        n_act = act.count("\n") + 1
        ytxt2 = ytxt - 1.6 * n_act - 2.0
        ax.text(x0[i] + 1.2, ytxt2, meta, ha="left", va="top", fontsize=8, color=T, linespacing=1.25)
        n_meta = meta.count("\n") + 1
        ax.text(x0[i] + 1.2, ytxt2 - 1.6 * n_meta - 2.0, pers, ha="left", va="top", fontsize=8, fontweight="bold", color=T, linespacing=1.25)
    # llaves superiores
    def llave(xa, xb, y, texto):
        ax.plot([xa, xb], [y, y], color=T, lw=1.4)
        ax.plot([xa, xa], [y, y - 1.2], color=T, lw=1.4)
        ax.plot([xb, xb], [y, y - 1.2], color=T, lw=1.4)
        ax.text((xa + xb) / 2, y + 2.0, texto, ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    llave(x0[0], x0[1] + w, 58.5, "Productos sociales (niveles 1 y 2)")
    llave(x0[2], x0[2] + w, 58.5, "Efectos sociales (nivel 3)")
    llave(x0[3], x0[3] + w, 58.5, "Impacto social (nivel 4)")
    ax.text(50, 0.8, "Borde discontinuo: aspiracional y medido después del cierre. La salud no se mide ni se atribuye (H36-11).",
            ha="center", va="center", fontsize=8.2, color=T)
    return E.guardar(fig, "c13_f01")


# ---------------------------------------------------------------- F13.2 modelo de impacto económico
def f02():
    fig = plt.figure(figsize=(10, 7))
    fig.suptitle("El costo se calcula por rubro; los beneficios y el ROI no se pueden calcular", fontsize=14, fontweight="bold",
                 color=T, x=0.01, ha="left", y=0.995)
    ax = fig.add_axes([0.20, 0.10, 0.31, 0.74])
    rubros = [("Personal", 4382.9, 50.2), ("Equipos y software", 1885.6, 21.6), ("Servicios técnicos", 846.0, 9.7),
              ("Reserva de contingencia", 636.0, 7.3), ("Otros rubros", 532.0, 6.1), ("Materiales e insumos", 242.9, 2.8),
              ("Viajes y viáticos", 204.5, 2.3)]
    rubros = rubros[::-1]
    ys = range(len(rubros))
    barras = ax.barh(list(ys), [r[1] for r in rubros], color=E.MEDIO, edgecolor=T, height=0.62)
    for b, r in zip(barras, rubros):
        if r[0].startswith("Reserva"):
            b.set_hatch("///"); b.set_facecolor(E.CLARO)
    ax.set_yticks(list(ys)); ax.set_yticklabels([r[0] for r in rubros], fontsize=9)
    for b, r in zip(barras, rubros):
        ax.annotate(f"{E.num(r[1], 1)} ({E.num(r[2], 1)} %)", xy=(b.get_width(), b.get_y() + b.get_height() / 2), xytext=(4, 0),
                    textcoords="offset points", ha="left", va="center", fontsize=8.5, fontweight="bold", color=T)
    ax.set_xlim(0, 8400)
    ax.set_xticks([0, 2000, 4000]); ax.set_xticklabels(["0", "2.000", "4.000"], fontsize=8.5)
    ax.set_title("Costos calculables\nSGR por rubro, millones de COP\nTotal: 8.729,84", fontsize=9.5, loc="left", pad=10, color=T, fontweight="bold")
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    # panel derecho: estructura de beneficios
    bx = fig.add_axes([0.58, 0.10, 0.41, 0.74]); bx.set_xlim(0, 40); bx.set_ylim(0, 70); bx.axis("off")
    bx.set_title("Beneficios candidatos\nEstructura, sin valores", fontsize=9.5, loc="left", pad=10, color=T, fontweight="bold")
    ben = [("Costos de parada de obra evitados\npor menos falsas alarmas", "Sin cifra: lucro cesante declarado en E3"),
           ("Ahorro frente a redes sin calibración\nque deben reponerse", "Sin fuente"),
           ("Valor de la información para la\ngestión del riesgo", "Sin fuente"),
           ("Costos de salud evitados", "No atribuible (H36-11)")]
    yb = 60
    for t, n in ben:
        caja2(bx, 0.5, yb - 7, 24, 8.5, t, relleno=E.CAJA, ls=(0, (4, 2)), fs=8.2)
        bx.text(26.0, yb - 2.75, "NO_CALCULABLE", ha="left", va="center", fontsize=8.2, fontweight="bold", color=T)
        bx.text(26.0, yb - 5.6, n, ha="left", va="center", fontsize=7.3, color=T, wrap=True)
        yb -= 11.5
    caja2(bx, 0.5, 6.0, 38, 10.5, "ROI = (B − C) ÷ C\nC: 10.839,84 millones de COP (total del proyecto, CALCULADO)\nB: NO_CALCULABLE, por tanto ROI: NO_CALCULABLE",
          relleno=E.CLARO, fs=8.2)
    fig.text(0.01, 0.02, "Trama: reserva de contingencia (suma de 12 valores esperados). Elaboración propia con la ficha maestra, sección 5. Los beneficios no se monetizan por falta de fuente.", fontsize=8, color=T)
    return E.guardar(fig, "c13_f02")


# ---------------------------------------------------------------- F13.3 contribución a ODS
def f03():
    fig, ax = E.lienzo(h1="El ODS 11 y el Marco de Sendái concentran el mayor peso relativo propuesto",
                       h2="Peso relativo cualitativo (PROPUESTO) y número de indicadores PERS vinculados (conteo propio)", figsize=(10, 5.2))
    datos = [("ODS 11 Ciudades y comunidades\nsostenibles (principal)", 3, "Alto", 4),
             ("Marco de Sendái\n(complementario)", 3, "Alto", 2),
             ("ODS 9 Industria, innovación\ne infraestructura", 2, "Medio", 3),
             ("ODS 3 Salud y bienestar", 2, "Medio", 2),
             ("ODS 17 Alianzas para lograr\nlos objetivos", 2, "Medio", 2)]
    datos = datos[::-1]
    ys = list(range(len(datos)))
    barras = ax.barh(ys, [d[1] for d in datos], color=[E.AZUL if d[2] == "Alto" else E.MEDIO for d in datos], edgecolor=T, height=0.58)
    for b, d in zip(barras, datos):
        if d[2] == "Medio": b.set_hatch("///")
        ax.annotate(f"{d[2]}; {d[3]} indicadores PERS", xy=(b.get_width(), b.get_y() + b.get_height() / 2), xytext=(5, 0),
                    textcoords="offset points", ha="left", va="center", fontsize=9, fontweight="bold", color=T)
    ax.set_yticks(ys); ax.set_yticklabels([d[0] for d in datos], fontsize=9)
    ax.set_xlim(0, 5.6); ax.set_xticks([1, 2, 3]); ax.set_xticklabels(["Bajo", "Medio", "Alto"], fontsize=9)
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    ax.set_xlabel("Peso relativo cualitativo (escala ordinal; la longitud no mide magnitud de efecto)", fontsize=9)
    return E.guardar(fig, "c13_f03")


# ---------------------------------------------------------------- F13.4 mapa de articulación territorial
def f04():
    fig, ax = E.lienzo_libre(h1="La articulación con el PDD y con las demandas queda sin verificar hasta aportar los documentos",
                             h2="12 municipios, 15 comités y 100 nodos en tres departamentos (SUPUESTO); nodos por departamento: PROPUESTO",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    ax.text(12.5, 62, "Demanda territorial\n(Anexo 4)", ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    ax.text(40, 62, "Proyecto: recursos\npor departamento", ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    ax.text(68, 62, "Impacto declarado\n(indicador PERS)", ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    ax.text(90, 62, "Plan de desarrollo\ndepartamental (PDD)", ha="center", va="center", fontsize=9, fontweight="bold", color=T)
    deptos = [("Caldas", 33, 50), ("Cundinamarca", 34, 37), ("Valle del Cauca", 33, 24)]
    for nombre, nodos, yc in deptos:
        caja2(ax, 1.5, yc - 4.5, 22, 9, "[DATO_USUARIO]\ncódigo de la demanda", relleno=E.CAJA, ls=(0, (4, 2)), fs=8)
        caja2(ax, 29, yc - 5, 22, 10, f"{nombre}\n4 municipios y 5 comités\n{nodos} nodos y 1 monitor\nde referencia", relleno=E.MEDIO, fs=8)
        caja2(ax, 83, yc - 4.5, 15.5, 9, "[DATO_USUARIO]\nartículo e indicador", relleno=E.CAJA, ls=(0, (4, 2)), fs=8)
        flecha(ax, (24, yc), (28.5, yc), ls=(0, (4, 2)))
        flecha(ax, (51.5, yc), (58, yc))
        flecha(ax, (78, yc), (82.5, yc), ls=(0, (4, 2)))
    caja2(ax, 58, 19.5, 20, 35.5, "PERS-E01\nUso institucional\ndel tablero\n\nPERS-E02\nFalsas alarmas\n\nPERS-S01\nActivación del\nprotocolo", relleno=E.CLARO, fs=8.2)
    ax.text(50, 9.6, "Marco nacional identificado solo por título: Ley 1523 de 2012, CONPES 3943, CONPES 4069 y Ley 2294 de 2023.",
            ha="center", va="center", fontsize=8.2, color=T)
    ax.text(50, 6.4, "Metas, artículos e indicadores: no aportados. Estado de la articulación: NO_VERIFICADO (decisión DEC-F12).",
            ha="center", va="center", fontsize=8.2, color=T)
    ax.text(50, 2.8, "Borde discontinuo y flecha discontinua: dato del usuario pendiente. Comités por departamento: 4 municipales y 1 departamental.",
            ha="center", va="center", fontsize=8, color=T)
    return E.guardar(fig, "c13_f04")


# ---------------------------------------------------------------- F13.5 ciclo de gestión adaptativa
def f05():
    fig, ax = E.lienzo_libre(h1="El ciclo adaptativo vincula la medición con la decisión en cada compuerta",
                             h2="Cadencias: trimestral, meses 12 y 17 (compuertas), meses 12 y 24 (evaluación externa), 6 y 12 meses tras el cierre",
                             figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    cx, cy, rx, ry = 50, 34, 31, 21
    pasos = [("1 Medir", "Línea base en el tramo 1\ny seguimiento mensual", 90),
             ("2 Evaluar", "Revisión trimestral de\nlos supuestos SC-1 a SC-4", 18),
             ("3 Decidir", "Compuertas C1 y C2 y\nevaluación externa", -54),
             ("4 Ajustar", "Reasignación interna\nregulada de recursos", -126),
             ("5 Aprender", "Registro de aprendizajes y\nrevisión de la teoría", 162)]
    cen = []
    hw, hh = 13.0, 6.0
    for t, d, ang in pasos:
        a = math.radians(ang)
        x = cx + rx * math.cos(a); y = cy + ry * math.sin(a)
        cen.append((x, y))
        caja2(ax, x - hw, y - hh, 2 * hw, 2 * hh, f"{t}\n{d}", relleno=E.MEDIO if t[0] in "123" else E.CLARO, fs=8.2, bold=False)
    for i in range(5):
        (x0, y0), (x1, y1) = cen[i], cen[(i + 1) % 5]
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        def m(ux, uy):
            tx = hw / abs(ux) if abs(ux) > 1e-9 else 1e9
            ty = hh / abs(uy) if abs(uy) > 1e-9 else 1e9
            return min(tx, ty) + 1.2
        mm = m(ux, uy)
        flecha(ax, (x0 + ux * mm, y0 + uy * mm), (x1 - ux * mm, y1 - uy * mm), rad=-0.18)
    ax.text(cx, cy + 3.5, "Bucle simple:\ncorrige la acción", ha="center", va="center", fontsize=8.8, fontweight="bold", color=T)
    ax.text(cx, cy - 4.5, "Bucle doble:\nrevisa la teoría del cambio", ha="center", va="center", fontsize=8.8, fontweight="bold", color=T)
    ax.text(cx, 4.5, "Tras el cierre, los custodios continúan el ciclo con cortes a los 6 y a los 12 meses.",
            ha="center", va="center", fontsize=8.5, color=T)
    return E.guardar(fig, "c13_f05")


if __name__ == "__main__":
    for f in (f00, f01, f02, f03, f04, f05):
        print(f())
