# -*- coding: utf-8 -*-
"""Figuras de las secciones 16, 17, 18 y 19 del Anexo 2: c16_f01 (custodia), c17_f01 (cadena producto-resultado-impacto),
c18_f01 (matriz de transferencia), c19_f01 (escalera de apropiación social) y c19_f02 (etapas de la estrategia).
Cifras: A2/v2/m2.py (productos, indicadores de resultado e impacto, hitos, tramos) y A2/FIGS_A2.md.
Uso: python3 c16_17_18_19_figs.py [f16 f17 f18 f19a f19b]"""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/scripts")
from _comun import *

TR = m2.M0.TRAMOS


# ============================================================ c16_f01
def f16():
    L = Lienzo(10, 8.0, h1="Cada componente de la red pasa a un custodio con una condición de recepción",
               h2="Servicio de vigilancia con cinco componentes, posibles custodios por tipo e hitos de transferencia en los meses 6, 12, 18 y 24")
    top = L.top
    wb, hb, gv = 24.0, 11.8, 3.0
    xl, xr = 1.0, 75.0
    ycol_top = top - 1.0
    ys = [ycol_top - hb - i * (hb + gv) for i in range(3)]
    hcol = 3 * hb + 2 * gv
    # ---- caja central: componentes y mes de transferencia
    xc, wc = 30.5, 39.0
    hc = 35.0
    yc = ycol_top - hcol / 2 - hc / 2
    comp = ["Gobernanza y acuerdos · mes 6", "Protocolo de calibración · mes 12", "Nodos y repuestos · mes 18",
            "Tablero y alertas · mes 18", "Gemelo digital, laboratorio y datos · mes 24"]
    L.caja(xc, yc, wc, hc, titulo="Servicio de vigilancia de PM2,5 y PM10 con custodia distribuida",
           cuerpo="\n" + "\n\n".join(comp), fc=AZUL, lw=2.0, pad=1.4)
    izq = [("Empresa tecnológica", "nodos, repuestos y gemelo digital", MEDIO, "-"),
           ("Universidad proponente", "protocolo, datos y laboratorio", MEDIO, "-"),
           ("Actor del SNCTI", "repositorio de datos y formación de custodios", MEDIO, "-")]
    der = [("Municipio y unidades de gestión del riesgo", "tablero y alertas", MEDIO, "-"),
           ("Autoridad ambiental", "protocolo de calibración", MEDIO, "-"),
           ("Comunidad y operarios", "usuarios y red de soporte", CLARO, (0, (5, 3)))]
    for y, (tit, cu, col, ls) in zip(ys, izq):
        L.caja(xl, y, wb, hb, titulo=tit, cuerpo=cu, fc=col, ls=ls, lw=1.4, pad=0.9)
        L.flecha((xl + wb + 0.2, y + hb / 2), (xc - 0.2, y + hb / 2), estilo="<|-|>", lw=1.5, ms=12)
    for y, (tit, cu, col, ls) in zip(ys, der):
        L.caja(xr, y, wb, hb, titulo=tit, cuerpo=cu, fc=col, ls=ls, lw=1.4, pad=0.9)
        L.flecha((xc + wc + 0.2, y + hb / 2), (xr - 0.2, y + hb / 2), estilo="<|-|>", lw=1.5, ms=12, ls="-" if ls == "-" else (0, (5, 3)))
    # ---- hitos de transferencia
    ylab = ycol_top - hcol - 4.0
    L.t(1.0, ylab, "Hitos de transferencia", bold=True, ha="left", va="center")
    hitos = [("Mes 6", "acuerdo marco y cláusula de apertura"), ("Mes 12", "protocolo y series de datos"),
             ("Mes 18", "nodos adicionales y tablero"), ("Mes 24", "operación con custodio, gemelo digital y laboratorio")]
    wh, gh, hh = 23.0, 2.0, 11.4
    yh = ylab - 2.0 - hh
    for i, (m, tx) in enumerate(hitos):
        L.caja(1.0 + i * (wh + gh), yh, wh, hh, titulo=m, cuerpo=tx, fc=CAJA, lw=1.3, pad=0.9)
        if i < 3:
            L.flecha((1.0 + i * (wh + gh) + wh + 0.1, yh + hh / 2), (1.0 + (i + 1) * (wh + gh) - 0.1, yh + hh / 2), lw=1.4, ms=9)
    L.t(1.0, yh - 3.0, "Sin un custodio que cumpla la condición de recepción, el componente permanece bajo la alianza o pasa a la cláusula de apertura.",
        ha="left", va="top", w=98)
    L.guardar("c16_f01")


# ============================================================ c17_f01
def f17(h=16.0, medir=False):
    """Con medir=True devuelve el alto del contenido (unidades); el dibujo final usa esa altura."""
    P = {p["n"]: p for p in m2.PRODUCTOS}
    assert P[1]["meta"].startswith("2 prototipos") and P[6]["meta"].startswith("1 infraestructura") and P[7]["meta"] == "3" and P[8]["meta"] == "29"
    prods = ["Prototipos validados: 2 (red y gemelo predictivo)", "Documentos de investigación: 9", "Maestría apoyada: 2 personas", "Estancia posdoctoral: 1",
             "Jóvenes investigadores: 6", "Infraestructura de medición y de modelación: 1", "Documentos de planeación: 3", "Actividades de apropiación: 29",
             "Asistencia técnica: 60 personas y 15 comités"]
    res = [r for r in m2.IND_RES if r["nivel"] == "Resultado"]
    imp = [r for r in m2.IND_RES if r["nivel"] == "Impacto"]
    assert [r["cod"] for r in res] == ["R1", "R2", "R3", "R4", "R5", "R6", "R7"] and [r["cod"] for r in imp] == ["I1", "I2"]
    L = Lienzo(10, h, h1="Nueve productos sostienen siete resultados y dos impactos que se miden después del cierre",
               h2="Productos y metas (meses 1 a 24), resultados con su meta al mes 24 e impactos a 12 meses del cierre")
    top = L.top
    x1, w1 = 1.0, 31.0
    x2, w2 = 36.0, 39.0
    x3, w3 = 79.5, 19.5
    yh = top - 0.6
    cab = [(x1, w1, "Productos", "meses 1 a 24", CLARO), (x2, w2, "Resultados", "al mes 24", MEDIO),
           (x3, w3, "Impactos", "12 meses después del cierre", AZUL)]
    hh = max(L.necesita(w, cuerpo=c, titulo=t, pad=0.9) for _, w, t, c, _ in cab) + 0.4
    for x, w, t, c, col in cab:
        L.caja(x, yh - hh, w, hh, titulo=t, cuerpo=c, fc=col, lw=1.6, pad=0.9)
    ycur = yh - hh - 1.4
    y_prod_top = ycur
    txt_red = "100 nodos, 10 gateways, 3 monitores de referencia y laboratorio de modelación"
    hred = L.necesita(w1, cuerpo=txt_red, titulo="Red operativa y laboratorio", pad=0.9) + 0.4
    hprod = [L.necesita(w1, cuerpo=t, pad=0.9) + 0.5 for t in prods]
    hres = [L.necesita(w2, cuerpo=r["meta"], titulo="%s · %s" % (r["cod"], r["nombre"]), pad=0.7) + 0.2 for r in res]
    need_prod = hred + 1.2 + sum(hprod) + 0.9 * (len(prods) - 1)
    need_res = sum(hres) + 0.8 * (len(res) - 1)
    tall = max(need_prod, need_res)
    y_prod_bot = y_prod_top - tall
    # ---- productos
    L.caja(x1, ycur - hred, w1, hred, titulo="Red operativa y laboratorio", cuerpo=txt_red, fc=BLANCO, lw=1.6, pad=0.9)
    ycur -= hred + 1.2
    gp = (tall - hred - 1.2 - sum(hprod)) / (len(prods) - 1)
    for t, hbx in zip(prods, hprod):
        L.caja(x1, ycur - hbx, w1, hbx, cuerpo=t, fc=CLARO, lw=1.2, pad=0.9)
        ycur -= hbx + gp
    # ---- resultados
    gap = (tall - sum(hres)) / (len(res) - 1)
    yy = y_prod_top
    for r, hbx in zip(res, hres):
        L.caja(x2, yy - hbx, w2, hbx, titulo="%s · %s" % (r["cod"], r["nombre"]), cuerpo=r["meta"], fc=MEDIO, lw=1.2, pad=0.7)
        yy -= hbx + gap
    # ---- impactos
    himp = [L.necesita(w3, cuerpo=r["meta"], titulo="%s · %s" % (r["cod"], r["nombre"]), pad=0.9) + 0.4 for r in imp]
    gi = 3.0
    tot = sum(himp) + gi
    ymid = (y_prod_top + y_prod_bot) / 2
    yy = ymid + tot / 2
    for r, hbx in zip(imp, himp):
        L.caja(x3, yy - hbx, w3, hbx, titulo="%s · %s" % (r["cod"], r["nombre"]), cuerpo=r["meta"], fc=AZUL, lw=1.6, pad=0.9)
        yy -= hbx + gi
    # llaves: todos los productos sostienen todos los resultados; los resultados sostienen los impactos
    for xa, xb, ya, yb in ((x1 + w1, x2, y_prod_top - 1.0, y_prod_bot + 1.0), (x2 + w2, x3, y_prod_top - 1.0, y_prod_bot + 1.0)):
        xm_ = xa + 1.6
        L.ax.plot([xa + 0.3, xm_, xm_, xa + 0.3], [ya, ya, yb, yb], color=T, lw=1.8, solid_joinstyle="miter", zorder=3)
        L.flecha((xm_, ymid), (xb - 0.3, ymid), lw=2.0, ms=15)
    if medir:
        plt.close(L.fig)
        return L.H - y_prod_bot + 1.2
    L.guardar("c17_f01")


# ============================================================ c18_f01
def f18():
    L = Lienzo(10, 8.3, h1="La transferencia avanza por cuatro hitos desde el acuerdo marco hasta la operación con custodio",
               h2="Entregas por componente y mes de transferencia, con la condición de recepción de cada una")
    top = L.top
    filas = ["Gobernanza y acuerdos", "Protocolo de calibración y series de datos", "Nodos adicionales y repuestos", "Tablero y alertas",
             "Gemelo digital, laboratorio y operación"]
    meses = [6, 12, 18, 24]
    OP = "Operación con custodio"
    celdas = {
        (0, 0): ("t", "Acuerdos firmados antes del segundo lote de nodos"),
        (1, 1): ("t", "Desempeño verificado y custodio con capacidad"),
        (1, 3): ("o", OP),
        (2, 2): ("t", "Partida en el plan operativo y personal designado"),
        (2, 3): ("o", OP),
        (3, 2): ("t", "Partida en el plan operativo y personal designado"),
        (3, 3): ("o", OP),
        (4, 3): ("t", "Competencia jurídica, partida y sostenimiento del laboratorio"),
    }
    xl, wl = 1.0, 20.0
    x0, wcel, g = 22.0, 18.9, 0.5
    hcab = 5.6
    ycab = top - 0.3 - hcab
    for j, m in enumerate(meses):
        L.caja(x0 + j * (wcel + g), ycab, wcel, hcab, titulo="Mes %d" % m, fc=MEDIO, lw=1.5, pad=0.6)
    hf, gf = 11.0, 0.8
    for i, nombre in enumerate(filas):
        y = ycab - 1.2 - (i + 1) * hf - i * gf
        L.t(xl, y + hf / 2, nombre, bold=True, ha="left", va="center", w=wl - 0.5)
        for j in range(4):
            x = x0 + j * (wcel + g)
            if (i, j) in celdas:
                tp, tx = celdas[(i, j)]
                if tp == "t":
                    L.caja(x, y, wcel, hf, cuerpo=tx, fc=MEDIO, lw=1.5, pad=0.8)
                else:
                    L.caja(x, y, wcel, hf, cuerpo=tx, fc=CLARO, lw=1.5, pad=0.8, trama="///", marco=1.0)
            else:
                L.ax.add_patch(FancyBboxPatch((x, y), wcel, hf, boxstyle="round,pad=0,rounding_size=1.0", fc="none", ec=MEDIO, lw=1.2,
                                              ls=(0, (3, 3)), zorder=1))
    yfin = ycab - 1.2 - 5 * hf - 4 * gf
    L.t(1.0, yfin - 1.4, "Cada celda indica la condición de recepción. Sin un custodio que la cumpla, el componente permanece bajo la alianza "
        "o pasa a la cláusula de apertura.", ha="left", va="top", w=98)
    L.guardar("c18_f01")


# ============================================================ c19_f01
def f19a():
    P8 = [p for p in m2.PRODUCTOS if p["n"] == 8][0]
    assert P8["meta"] == "29" and "20 talleres de co-diseño y 9 jornadas" in P8["indicador"]
    L = Lienzo(10, 6.5, h1="Cuatro niveles de apropiación social llevan a la comunidad de la información a la co-creación",
               h2="Compromisos medibles por nivel: 29 actividades (20 talleres de co-diseño y 9 jornadas públicas), meses 1 a 24")
    top = L.top
    w, g = 23.5, 1.6
    xs = [1.0 + i * (w + g) for i in range(4)]
    base = 8.5
    hs = [19.0, 25.0, 35.5, 41.0]
    cont = [
        ("Nivel 1\nInformación", "Se informa a la comunidad\n\n5.000 cartillas", CLARO, None, "-", 1.5),
        ("Nivel 2\nConsulta", "Se consulta su opinión", MEDIO, None, "-", 1.5),
        ("Nivel 3\nColaboración activa\nObligatorio", "Se co-diseñan umbrales y protocolo\n\nAl menos 3 actas firmadas de co-diseño\n\n60 personas certificadas",
         AZUL, None, "-", 2.6),
        ("Nivel 4\nEmpoderamiento\nAspiración", "La comunidad decide y lidera; se verifica después del cierre", GRIS, "///", (0, (5, 3)), 1.5),
    ]
    for i, (tit, cu, col, tr_, ls, lw) in enumerate(cont):
        L.caja(xs[i], base, w, hs[i], titulo=tit, cuerpo="\n" + cu, fc=col, trama=tr_, ls=ls, lw=lw, va="top", pad=1.0)
    # llaves de compromisos medibles compartidos
    def llave(xa, xb, y, texto):
        L.ax.plot([xa, xa, xb, xb], [y - 1.3, y, y, y - 1.3], color=T, lw=1.8, solid_joinstyle="miter", zorder=3)
        L.t((xa + xb) / 2, y + 1.9, texto, bold=True, ha="center", va="center")
    llave(xs[0], xs[1] + w, base + hs[1] + 2.6, "9 jornadas públicas")
    llave(xs[2], xs[2] + w, base + hs[2] + 2.6, "20 talleres de co-diseño")
    # flecha de participación creciente
    L.flecha((1.5, 3.2), (98.5, 3.2), lw=1.8, ms=15)
    L.t(50, 6.0, "Mayor participación y poder de decisión de la comunidad", ha="center", va="center")
    L.guardar("c19_f01")


# ============================================================ c19_f02
def f19b():
    A3 = {k: m2.ACTD[k] for k in ("3.1", "3.2", "3.3", "3.4")}
    v = {k: (a["m_ini"], a["m_fin"]) for k, a in A3.items()}
    assert v == {"3.1": (3, 9), "3.2": (12, 15), "3.3": (17, 20), "3.4": (23, 24)}
    ind8 = [r for r in m2.IND_PROD if r["n"] == 8][0]
    assert ind8["periodo"] == "Meses 3 a 24"
    gates = {h["id"]: h["mes"] for h in m2.HITOS if h["id"] in ("H3", "H5", "C3")}
    assert gates == {"H3": 12, "H5": 17, "C3": 24}
    L = Lienzo(10, 7.9, h1="Las siete etapas de la estrategia de apropiación social se articulan con los tres tramos",
               h2="Etapas A a G por mes de ejecución (meses 1 a 24); barras: actividades 3.1 a 3.4 del cronograma; rombos: compuertas")
    top = L.top
    etapas = ["Reconocimiento del contexto", "Caracterización de actores", "Identificación de saberes y capacidades",
              "Mecanismos de participación", "Colaboración y co-creación", "Articulación con el ciclo de ejecución", "Sistematización"]
    letras = "ABCDEFG"
    x0, cw = 36.0, (96.0 - 36.0) / 24.0
    def xm(m):          # inicio del mes m
        return x0 + (m - 1) * cw
    # ---- encabezado de tramos
    ytr = top - 0.3
    htr = 11.2
    tr = [(1, 12, AZUL, None, "Tramo 1", "meses 1 a 12"), (13, 17, MEDIO, "///", "Tramo 2", "meses 13 a 17"),
          (18, 24, CLARO, "...", "Tramo 3", "meses 18 a 24")]
    for a, b, col, tr_, t1, t2 in tr:
        L.caja(xm(a) + 0.15, ytr - htr, xm(b + 1) - xm(a) - 0.3, htr, titulo=t1, cuerpo=t2, fc=col, trama=tr_, pad=0.5, marco=0.7, radio=0.6)
    yfila0 = ytr - htr - 1.2
    hr = 6.7
    ymax = yfila0 - 7 * hr
    for i, (le, et) in enumerate(zip(letras, etapas)):
        y = yfila0 - (i + 1) * hr
        if i % 2 == 0:
            L.ax.add_patch(Rectangle((1.0, y), 98.0, hr, fc=CAJA, ec="none", zorder=0))
        L.caja(1.5, y + hr / 2 - 2.0, 4.0, 4.0, titulo=le, fc=BLANCO, lw=1.2, pad=0.2, radio=0.5)
        L.t(7.0, y + hr / 2, et, ha="left", va="center", w=x0 - 8.5)
    for m in (13, 18):
        L.ax.plot([xm(m), xm(m)], [ymax, yfila0], color=T, lw=1.2, ls=(0, (4, 3)), zorder=1)
    def barra(i, a, b, texto, col=AZUL):
        y = yfila0 - (i + 1) * hr
        xa, xb = xm(a) + 0.12, xm(b + 1) - 0.12
        L.ax.add_patch(FancyBboxPatch((xa, y + 1.0), xb - xa, hr - 2.0, boxstyle="round,pad=0,rounding_size=0.5", fc=col, ec=T, lw=1.3, zorder=3))
        L.t((xa + xb) / 2, y + hr / 2, texto, bold=True, ha="center", va="center", zorder=6)
    def rombo(i, m, texto, izq=False):
        y = yfila0 - (i + 1) * hr
        cx = xm(m) + cw / 2
        L.rombo(cx, y + hr / 2, 6.6, hr - 0.6, "", fc=BLANCO)
        if izq:
            L.t(cx - 4.0, y + hr / 2, texto, ha="right", va="center", bold=True, zorder=6)
        else:
            L.t(cx + 4.0, y + hr / 2, texto, ha="left", va="center", bold=True, zorder=6)
    for i in (0, 1, 2):
        barra(i, *v["3.1"], "3.1")
    barra(3, 3, 24, "3.1 a 3.4", col=CLARO)
    barra(4, *v["3.1"], "3.1")
    barra(4, *v["3.2"], "3.2")
    barra(4, *v["3.3"], "3.3")
    rombo(5, gates["H3"], "C1")
    rombo(5, gates["H5"], "C2")
    rombo(5, gates["C3"], "C3", izq=True)
    barra(6, *v["3.4"], "3.4")
    for m in (1, 3, 6, 9, 12, 15, 17, 20, 24):
        negrita = m in (12, 17, 24)
        cx = xm(m) + cw / 2
        L.ax.plot([cx, cx], [ymax - 0.2, ymax - 1.2], color=T, lw=1.2, zorder=2)
        L.t(cx, ymax - 3.0, str(m), bold=negrita, ha="center", va="center")
    L.ax.plot([xm(1), xm(25)], [ymax - 0.2, ymax - 0.2], color=T, lw=1.2, zorder=2)
    L.t(1.0, ymax - 3.0, "Mes", bold=True, ha="left", va="center")
    L.guardar("c19_f02")


TODAS = {"f16": f16, "f17": f17, "f18": f18, "f19a": f19a, "f19b": f19b}

if __name__ == "__main__":
    sel = sys.argv[1:] or list(TODAS)
    for k in sel:
        if k == "f17":
            f17(h=f17(medir=True) / 10)
        else:
            TODAS[k]()
