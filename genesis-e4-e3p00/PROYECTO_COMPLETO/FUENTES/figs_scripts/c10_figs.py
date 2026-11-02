# -*- coding: utf-8 -*-
"""Figuras del capítulo 10 (Riesgos): c10_f01 (mapa de calor), c10_f02 (flujo de escalamiento) y c10_f03 (árbol de decisión pivotar o perseverar).
Datos: maestro.py (RISKS, RESERVA, TRAMOS, BUDGET E01/E02/E04, HITOS) y FICHA_MAESTRA §2 y §4 (umbrales y criterios de C1 y C2).
Sin componente aleatorio. Ejecución: python3 c10_figs.py"""
import os, sys, collections, textwrap
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "maestro")); sys.path.insert(0, os.path.join(RAIZ, "figs"))
import maestro as M
import estilo as E
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch

RISKS = M.RISKS
NIVELES = [("BAJO", 1, 5, E.GRIS), ("MEDIO", 6, 11, E.CLARO), ("ALTO", 12, 19, E.MEDIO), ("EXTREMO", 20, 25, E.AZUL)]

def nivel_de(score):
    return "EXTREMO" if score >= 20 else "ALTO" if score >= 12 else "MEDIO" if score >= 6 else "BAJO"

def _h2(fig, texto):
    fig.text(0.008, 0.925, texto, fontsize=10, color=E.TINTA, ha="left", va="center")

def corto(i):
    return i[2:] if i.startswith("R-") else i

# ------------------------------------------------------------------ F10.1 mapa de calor
def f01():
    cnt = collections.Counter(r["nivel"] for r in RISKS)
    fig, ax = E.lienzo(h1=f"{cnt['EXTREMO']} riesgo extremo y {cnt['ALTO']} altos concentran el registro; ninguno queda en nivel bajo",
                       h2=None, figsize=(10, 6.8), grid=False)
    fig.subplots_adjust(left=0.09, right=0.75, top=0.83, bottom=0.13)
    _h2(fig, "Matriz probabilidad-impacto de 5 por 5 con los 12 riesgos del registro; nivel = P × I (escala de 1 a 5, PROPUESTO)")
    celdas = collections.defaultdict(list)
    for r in RISKS: celdas[(r["I"], r["P"])].append(r)
    for P in range(1, 6):
        for I in range(1, 6):
            sc = P * I; niv = nivel_de(sc)
            col = [n[3] for n in NIVELES if n[0] == niv][0]
            ax.add_patch(Rectangle((I - 0.5, P - 0.5), 1, 1, facecolor=col, edgecolor=E.TINTA, linewidth=0.9,
                                   hatch="///" if niv == "EXTREMO" else ("..." if niv == "MEDIO" else ""), zorder=2))
            ax.text(I - 0.46, P + 0.44, f"{sc}", fontsize=7.5, color=E.TINTA, va="top", ha="left", zorder=4)
            rs = celdas.get((I, P), [])
            if rs:
                ax.add_patch(Rectangle((I - 0.44, P - 0.33), 0.88, 0.66, facecolor="white", edgecolor=E.TINTA, linewidth=0.6, zorder=3))
                ax.text(I, P, "\n".join(corto(r["id"]) for r in rs), ha="center", va="center", fontsize=8.0 if len(rs) < 3 else 7.2,
                        fontweight="bold", color=E.TINTA, zorder=5, linespacing=1.15)
    ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xticklabels(["1\nmuy bajo", "2\nbajo", "3\nmedio", "4\nalto", "5\nmuy alto"], fontsize=8.6)
    ax.set_yticklabels(["1 muy baja", "2 baja", "3 media", "4 alta", "5 muy alta"], fontsize=8.6)
    ax.set_xlabel("Impacto (I)", fontsize=10); ax.set_ylabel("Probabilidad (P)", fontsize=10)
    ax.tick_params(length=0)
    for s in ("left", "bottom"): ax.spines[s].set_visible(False)
    # panel de nivel y recuento
    x0 = 1.04
    ax.text(x0, 0.98, "Nivel y recuento de riesgos", transform=ax.transAxes, fontsize=9.5, fontweight="bold", color=E.TINTA, va="top")
    for j, (n, lo, hi, col) in enumerate(reversed(NIVELES)):
        y = 0.90 - j * 0.115
        ax.add_patch(Rectangle((x0, y - 0.05), 0.07, 0.07, transform=ax.transAxes, facecolor=col, edgecolor=E.TINTA, lw=0.9,
                               hatch="///" if n == "EXTREMO" else ("..." if n == "MEDIO" else ""), clip_on=False))
        ax.text(x0 + 0.095, y - 0.015, f"{n}: P × I de {lo} a {hi}\n{cnt.get(n, 0)} " + ("riesgo" if cnt.get(n, 0) == 1 else "riesgos"), transform=ax.transAxes, fontsize=8.6, va="center", color=E.TINTA)
    ax.text(x0, 0.40, "Identificadores:\nTEC técnico, ORG organizacional,\nEXT externo, FIN financiero,\nJUR jurídico, DAT datos", transform=ax.transAxes,
            fontsize=8.2, va="top", color=E.TINTA)
    return E.guardar(fig, "c10_f01")

# ------------------------------------------------------------------ utilidades de diagrama
def diamante(ax, cx, cy, w, h, texto, fs=8.2, relleno=E.CLARO):
    ax.add_patch(Polygon([(cx - w / 2, cy), (cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2)], closed=True, fc=relleno, ec=E.AZUL, lw=1.5, zorder=3))
    ax.text(cx, cy, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, zorder=4, linespacing=1.2)

def codo(ax, pts, ls="-", lw=1.3, color=E.TINTA):
    for a, b in zip(pts[:-2], pts[1:-1]):
        ax.plot([a[0], b[0]], [a[1], b[1]], color=color, lw=lw, ls=ls, solid_capstyle="butt", zorder=1)
    ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=11, color=color, lw=lw, ls=ls, zorder=1))

def etq(ax, x, y, t, fs=8.2, bold=True, ha="center"):
    ax.text(x, y, t, ha=ha, va="center", fontsize=fs, fontweight="bold" if bold else "normal", color=E.TINTA,
            bbox=dict(facecolor="white", edgecolor="none", pad=0.8), zorder=5)

def envolver(t, n):
    t = t.replace(" %", "\u00a0%")
    return "\n".join(textwrap.fill(p, n) for p in t.split("\n"))

# ------------------------------------------------------------------ F10.2 escalamiento
def f02():
    cnt = collections.Counter(r["nivel"] for r in RISKS)
    fig, ax = E.lienzo_libre(h1="El nivel P × I fija quién decide: responsable, gerencia o comité directivo",
                             h2=None, figsize=(10, 7), xlim=(0, 100), ylim=(0, 74))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.89, bottom=0.01)
    _h2(fig, "Flujo de escalamiento de riesgos (PROPUESTO); niveles según la matriz de la Figura 10.1; reserva de contingencia de 636,0 M COP".replace("636,0", M.mm(M.RESERVA)))
    # fila superior
    E.caja(ax, 2, 61, 28, 8.5, envolver("1. Detección\nEl responsable del riesgo observa el disparador del plan de respuesta", 30), relleno=E.CAJA, borde=E.TINTA, fs=8.2, grosor=1.3)
    E.caja(ax, 36, 61, 28, 8.5, envolver("2. Registro y reevaluación\nBitácora semanal: actualiza P, I y valor monetario esperado", 30), relleno=E.CAJA, borde=E.TINTA, fs=8.2, grosor=1.3)
    E.caja(ax, 70, 61, 28, 8.5, envolver("3. Clasificación\nNivel = P × I frente a la matriz de riesgos", 30), relleno=E.MEDIO, borde=E.AZUL, fs=8.2, bold=False, grosor=1.6)
    E.flecha(ax, (30.4, 65.2), (35.6, 65.2)); E.flecha(ax, (64.4, 65.2), (69.6, 65.2))
    # fila media: tres niveles
    cols = [(2, "MEDIO (P × I de 6 a 11)", f"{cnt.get('MEDIO', 0)} riesgos", "Responde el responsable del riesgo.\nInforma en la retrospectiva quincenal."),
            (36, "ALTO (P × I de 12 a 19)", f"{cnt.get('ALTO', 0)} riesgos", "La gerencia de proyecto aprueba la respuesta y el uso de la reserva.\nInforma al comité directivo."),
            (70, "EXTREMO (P × I de 20 o más)", f"{cnt.get('EXTREMO', 0)} riesgo", "El comité directivo decide.\nEvalúa pivote y comunica al financiador.")]
    for i, (x, n, c, t) in enumerate(cols):
        fill = [E.CLARO, E.MEDIO, E.AZUL][i]
        E.caja(ax, x, 37, 28, 14, envolver(f"{n}\n{c}\n{t}", 32), relleno=fill, borde=E.TINTA, fs=8.0, grosor=1.3, hatch=None)
        codo(ax, [(84, 60.6), (84, 56), (x + 14, 56), (x + 14, 51.4)] if i != 2 else [(84, 60.6), (84, 51.4)])
    # decisión final
    diamante(ax, 50, 20, 52, 17, "¿El riesgo compromete una compuerta\n(C1 o C2) o supera la reserva?", fs=8.4)
    for i, (x, *_r) in enumerate(cols):
        codo(ax, [(x + 14, 36.6), (x + 14, 31.5), (50 if i == 1 else (x + 14), 31.5), (50, 28.6)] if i != 1 else [(x + 14, 36.6), (x + 14, 28.6)])
    # salidas
    E.caja(ax, 2, 2, 31, 11, envolver("Sí: revisión de compuerta con el árbol de decisión (Figura 10.3) o modificación del plan con el financiador [DATO_USUARIO: procedimiento de modificación]", 36), relleno=E.CAJA, borde=E.TINTA, fs=7.8, grosor=1.3)
    E.caja(ax, 67, 2, 31, 11, envolver("No: monitoreo del disparador; cierre del riesgo cuando deja de activarse y registro de la lección", 36), relleno=E.CAJA, borde=E.TINTA, fs=7.8, grosor=1.3)
    codo(ax, [(24.0, 20), (17.5, 20), (17.5, 13.4)]); etq(ax, 21.6, 22.0, "Sí")
    codo(ax, [(76.0, 20), (82.5, 20), (82.5, 13.4)]); etq(ax, 78.6, 22.0, "No")
    # bucle de aprendizaje
    codo(ax, [(98.6, 7.5), (99.6, 7.5), (99.6, 65.2), (98.4, 65.2)], ls="--", lw=1.0, color=E.AZUL)
    ax.text(99.0, 38, "Retrospectiva quincenal: lecciones al registro", rotation=90, fontsize=7.6, color=E.TINTA, ha="center", va="center",
            bbox=dict(facecolor="white", edgecolor="none", pad=1.0))
    return E.guardar(fig, "c10_f02")

# ------------------------------------------------------------------ F10.3 árbol de decisión
def compra_tramo(id_):
    t = [x for x in M.TRAMOS if x["id"] == id_][0]
    B = {l["id"]: l for l in M.BUDGET}
    return t["compra_nodos"] * B["E01"]["vunit"] + t["compra_cabezales"] * B["E02"]["vunit"] + t["compra_gw"] * B["E04"]["vunit"], t

def f03():
    c2, t2 = compra_tramo(2); c3, t3 = compra_tramo(3)
    fig, ax = E.lienzo_libre(h1="C1 y C2 liberan la compra del tramo siguiente solo si se cumplen todos los criterios",
                             h2=None, figsize=(10, 7.4), xlim=(0, 100), ylim=(0, 76))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    _h2(fig, "Árbol de decisión pivotar o perseverar con los umbrales de la ficha maestra (C1 y C2); respuestas de pivote PROPUESTO (4.4-MDR.12)")
    def decision(x, y, t, w=26, h=9):
        E.caja(ax, x, y, w, h, envolver(t, 30), relleno=E.CLARO, borde=E.AZUL, fs=8.0, grosor=1.6)
    def resultado(x, y, titulo, t, tipo, w=25.5, h=9.5):
        fill = {"Perseverar": E.CLARO, "Pivotar": E.MEDIO, "Detener": E.GRIS}[tipo]
        E.caja(ax, x, y, w, h, envolver(f"{titulo}\n{t}", 31), relleno=fill, borde=E.TINTA, fs=7.6, grosor=2.0 if tipo == "Perseverar" else 1.0)
    # ----- bloque C1
    E.caja(ax, 1, 56, 13, 8, "Compuerta C1\nmes 12 (H3)", relleno=E.MEDIO, borde=E.AZUL, fs=8.2, bold=True, grosor=1.8)
    decision(18, 55.5, "¿El modelo cumple R² ≥ 0,70 y NRMSE ≤ 30 % frente a la referencia en el piloto?")
    decision(49, 55.5, "¿Al menos 50 % de los comités del tramo 1 usa el tablero?", w=22)
    resultado(74, 66, "Pivotar la medición o detener", "No se libera el tramo 2; revisar el método (opciones 1b y 1c)", "Pivotar")
    resultado(74, 55, "Pivotar el uso", "Tablero técnico y refuerzo del co-diseño (opción 2a); tramo 2 en espera", "Pivotar")
    resultado(74, 44, "Perseverar", f"Se libera la compra del tramo 2: {M.mm(c2)} M COP ({t2['compra_nodos']} nodos, {t2['compra_gw']} gateways)", "Perseverar")
    E.flecha(ax, (14.4, 60), (17.6, 60))
    codo(ax, [(44.4, 60), (48.6, 60)]); etq(ax, 46.5, 62.0, "Sí")
    codo(ax, [(31, 64.9), (31, 70.75), (73.6, 70.75)]); etq(ax, 31, 67.8, "No")
    codo(ax, [(71.4, 60), (73.6, 60)]); etq(ax, 72.5, 62.0, "No")
    codo(ax, [(60, 55.1), (60, 48.75), (73.6, 48.75)]); etq(ax, 60, 51.8, "Sí")
    # puente a C2
    codo(ax, [(86.75, 43.6), (86.75, 42.2), (7.5, 42.2), (7.5, 29.5)], ls="--", lw=1.0, color=E.AZUL)
    ax.text(47, 42.2, "continúa al tramo 2 y a la compuerta C2", fontsize=7.8, color=E.TINTA, ha="center", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=1.0))
    # ----- bloque C2
    E.caja(ax, 1, 21, 13, 8, "Compuerta C2\nmes 17 (H5)", relleno=E.MEDIO, borde=E.AZUL, fs=8.2, bold=True, grosor=1.8)
    decision(18, 20.5, "¿Se cumplen los umbrales en los tres departamentos y la disponibilidad mensual es ≥ 90 %?")
    decision(49, 20.5, "¿Hay convenios de custodia con partida?", w=22)
    resultado(74, 31, "Pivotar la red", "Reentrenar por departamento; reforzar energía y enlace; tramo 3 en espera", "Pivotar")
    resultado(74, 20, "Pivotar la custodia", "Cláusula de apertura y custodia por función (opción 3b); tramo 3 en espera", "Pivotar")
    resultado(74, 9, "Perseverar", f"Se libera la compra del tramo 3: {M.mm(c3)} M COP ({t3['compra_nodos']} nodos, {t3['compra_gw']} gateways)", "Perseverar")
    E.flecha(ax, (14.4, 25), (17.6, 25))
    codo(ax, [(44.4, 25), (48.6, 25)]); etq(ax, 46.5, 27.0, "Sí")
    codo(ax, [(31, 29.9), (31, 35.75), (73.6, 35.75)]); etq(ax, 31, 32.8, "No")
    codo(ax, [(71.4, 25), (73.6, 25)]); etq(ax, 72.5, 27.0, "No")
    codo(ax, [(60, 20.1), (60, 13.75), (73.6, 13.75)]); etq(ax, 60, 16.8, "Sí")
    # C3
    E.caja(ax, 1, 1, 56, 6, envolver("Compuerta C3, mes 24 (H8): cierra y transfiere; la cláusula de apertura rige si ningún custodio demuestra capacidad", 70), relleno=E.GRIS, borde=E.MEDIO, fs=7.6, grosor=1.0)
    codo(ax, [(86.75, 8.6), (86.75, 4.0), (57.6, 4.0)], ls="--", lw=1.0, color=E.AZUL)
    return E.guardar(fig, "c10_f03")

if __name__ == "__main__":
    print(f01()); print(f02()); print(f03())
