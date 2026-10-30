# -*- coding: utf-8 -*-
"""Figuras del Anexo A (análisis del problema público y de la estructura causal): cA_f01 a cA_f07.
Las cifras salen de A2/v2/causal.py (cálculo estructural recalculado y verificado)."""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/scripts")
from _comun import *
import causal as C
from matplotlib.lines import Line2D

CORTO = {"V01": "PM2,5", "V02": "PM10", "V03": "Humedad", "V04": "Viento", "V05": "Escombros", "V06": "Error de medición", "V07": "Calibración",
         "V08": "Latencia", "V09": "Disponibilidad", "V10": "Densidad del gemelo", "V11": "Índice de calidad", "V12": "Falsas alarmas",
         "V13": "Anticipación", "V14": "Personas alertadas", "V15": "Adopción"}
RELLENO = {"CRITICA": AZUL, "ACTIVA": MEDIO, "REACTIVA": CLARO, "AUTONOMA_RELATIVA": GRIS, "FRONTERA": BLANCO}
MARCA = {"CRITICA": "s", "ACTIVA": "^", "REACTIVA": "v", "AUTONOMA_RELATIVA": "o", "FRONTERA": "D"}


def leyenda_marcas(L, y, x0=1.0, gap=3.0, fs=FS):
    x = x0
    for c in ("CRITICA", "ACTIVA", "REACTIVA", "AUTONOMA_RELATIVA", "FRONTERA"):
        L.ax.plot([x + 1.0], [y], marker=MARCA[c], ms=11, mfc=RELLENO[c], mec=T, mew=1.3, ls="none", color=T, zorder=6)
        lab = C.clase(c)
        L.t(x + 2.6, y, lab, fs=fs)
        x += 2.6 + L.ancho(lab, fs) + gap


# ============================================================ cA_f01: matriz de influencia directa
def cA_f01():
    A = C.mat("S2"); ids = C.IDS
    L = Lienzo(10, 8.1, "Siete vínculos de peso 3 y 16 de peso 2 concentran la influencia directa del escenario de trabajo",
               "Matriz de influencia directa S2: origen en las filas, destino en las columnas y peso ordinal de 0 a 3")
    cw, ch = 5.2, 3.5
    x0 = 9.5
    ytop = L.top - 6.0
    fill = {0: None, 1: CLARO, 2: MEDIO, 3: AZUL}
    # encabezados de bloque y de columna
    for nm, a, b in (("Físico", 0, 4), ("Técnico", 5, 9), ("Decisión", 10, 14)):
        xm = x0 + (a + b + 1) / 2 * cw
        L.t(xm, ytop + ch + 1.8, nm, bold=True, ha="center")
    for j in range(15):
        L.t(x0 + (j + 0.5) * cw, ytop + ch / 2, ids[j], ha="center", bold=True)
    L.t(x0 + 15 * cw + 3.0, ytop + ch / 2, "TA", ha="center", bold=True)
    for i in range(15):
        yb = ytop - (i + 1) * ch
        L.t(x0 - 0.8, yb + ch / 2, ids[i], ha="right", bold=True)
        for j in range(15):
            w = int(A[i, j]); xl = x0 + j * cw
            L.ax.add_patch(Rectangle((xl, yb), cw, ch, fc=fill[w] or "none", ec=MEDIO, lw=0.6, zorder=2))
            if w:
                L.t(xl + cw / 2, yb + ch / 2, str(w), ha="center", bold=(w == 3))
        L.t(x0 + 15 * cw + 3.0, yb + ch / 2, str(int(A[i].sum())), ha="center", bold=True)
    yb = ytop - 16 * ch
    L.t(x0 - 0.8, yb + ch / 2, "TP", ha="right", bold=True)
    for j in range(15):
        L.t(x0 + (j + 0.5) * cw, yb + ch / 2, str(int(A[:, j].sum())), ha="center", bold=True)
    L.t(x0 + 15 * cw + 3.0, yb + ch / 2, str(int(A.sum())), ha="center", bold=True)
    # separadores de bloque
    for k in (5, 10):
        L.ax.plot([x0 + k * cw] * 2, [ytop - 15 * ch, ytop], color=T, lw=1.8, zorder=4)
        L.ax.plot([x0, x0 + 15 * cw], [ytop - k * ch] * 2, color=T, lw=1.8, zorder=4)
    L.ax.plot([x0, x0 + 15 * cw], [ytop - 15 * ch] * 2, color=T, lw=1.2, zorder=4)
    L.ax.add_patch(Rectangle((x0, ytop - 15 * ch), 15 * cw, 15 * ch, fc="none", ec=T, lw=1.4, zorder=4))
    # leyenda
    yl = ytop - 16 * ch - 3.6
    x = x0
    for w, lab in ((0, "Sin vínculo directo"), (1, "Peso 1: débil"), (2, "Peso 2: moderado"), (3, "Peso 3: fuerte")):
        L.ax.add_patch(Rectangle((x, yl - 0.9), 3.0, 1.8, fc=fill[w] or "none", ec=T, lw=1.0, zorder=5))
        L.t(x + 3.8, yl, lab)
        x += 3.8 + L.ancho(lab) + 3.0
    return L.guardar("cA_f01")


# ============================================================ cA_f02: plano de Vester
def cA_f02():
    s = C.S("S2"); dd = {d["id"]: d for d in s["directa"]}
    L = Lienzo(10, 8.0, "V02, V06 y V15 quedan en el cuadrante crítico del escenario de trabajo",
               "Plano de Vester S2: dependencia en el eje horizontal, influencia en el vertical y cortes por mediana en 5")
    x0, x1 = 9.5, 62.0
    y0, y1 = 13.0, L.top - 2.0
    ax = eje_en_unidades(L, x0, y0, x1, y1)
    ax.set_xlim(-0.8, 14.6); ax.set_ylim(1.0, 9.2)
    estilo_eje(ax)
    ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14]); ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ax.axvline(5, color=T, lw=1.2, ls="--", zorder=1); ax.axhline(5, color=T, lw=1.2, ls="--", zorder=1)
    ax.add_patch(Rectangle((5, 5), 9.6, 4.2, fc=GRIS, ec="none", zorder=0))
    ax.set_xlabel("Dependencia (suma de la columna)", fontsize=FS, color=T)
    ax.set_ylabel("Influencia (suma de la fila)", fontsize=FS, color=T)
    for txt, x, y, ha, va in (("Activa", -0.5, 9.0, "left", "top"), ("Crítica", 14.4, 9.0, "right", "top"),
                             ("Autónoma\nrelativa", -0.5, 1.2, "left", "bottom"), ("Reactiva", 14.4, 1.2, "right", "bottom")):
        ax.text(x, y, txt, fontsize=FS, fontweight="bold", color=T, ha=ha, va=va, zorder=3)
    off = {"V01": (0.38, 0.30), "V02": (0.0, 0.52), "V03": (0.35, 0.0), "V04": (0.35, 0.0), "V05": (0.35, 0.0), "V06": (-0.35, 0.0), "V07": (0.0, 0.52),
           "V08": (0.0, 0.52), "V09": (0.35, 0.0), "V10": (0.0, -0.55), "V11": (0.0, 0.52), "V12": (0.38, -0.12), "V13": (0.0, 0.52), "V14": (0.35, 0.0), "V15": (0.35, 0.0)}
    for v in C.IDS:
        d = dd[v]; c = d["clase_mediana"]; x, y = d["dependencia"], d["influencia"]
        ax.plot([x], [y], marker=MARCA[c], ms=13, mfc=RELLENO[c], mec=T, mew=1.3, ls="none", color=T, zorder=5)
        dx, dy = off[v]
        ha = "center" if dx == 0 else ("right" if dx < 0 else "left")
        ax.text(x + dx, y + dy, v, fontsize=FS, color=T, ha=ha, va="center", zorder=6)
    # clave de variables
    xk = 66.0
    L.t(xk, y1 + 0.5, "Variables", bold=True)
    yk = y1 - 2.2
    for v in C.IDS:
        L.t(xk, yk, f"{v}  {CORTO[v]}", w=33.0)
        yk -= 2.55
    leyenda_marcas(L, 4.6, x0=1.0, gap=2.4)
    return L.guardar("cA_f02")


# ============================================================ cA_f03: desplazamiento de rangos (MICMAC)
def cA_f03():
    con = C.S("S2")["micmac"]["contraste"]; ids = [d["id"] for d in con]
    L = Lienzo(10, 7.9, "Al considerar recorridos largos, V05 y V03 ganan posiciones de influencia y V06 y V15 las pierden",
               "Rango de influencia directo (A¹) e indirecto (A¹⁰) en S2; el rango 1 corresponde a la mayor influencia")
    xl, xr = 32.0, 68.0
    dy = 3.55
    ytop = L.top - 7.0
    L.t(xl, ytop + 4.2, "Directo (A¹)", bold=True, ha="center")
    L.t(xr, ytop + 4.2, "Indirecto (A¹⁰)", bold=True, ha="center")
    pos_d = {v: k for k, v in enumerate(sorted(ids, key=lambda v: (con[ids.index(v)]["rango_I_directo"], v)))}
    pos_i = {v: k for k, v in enumerate(sorted(ids, key=lambda v: (con[ids.index(v)]["rango_I_indirecto"], v)))}
    for v in ids:
        d = con[ids.index(v)]
        yd = ytop - pos_d[v] * dy; yi = ytop - pos_i[v] * dy
        fuerte = abs(d["ascenso_I"]) >= 2
        L.ax.plot([xl, xr], [yd, yi], color=AZUL if fuerte else MEDIO, lw=3.2 if fuerte else 1.6, zorder=3 if fuerte else 2, solid_capstyle="round")
        for x, y in ((xl, yd), (xr, yi)):
            L.ax.plot([x], [y], marker="o", ms=7, mfc=AZUL if fuerte else MEDIO, mec=T, mew=1.0, ls="none", color=T, zorder=4)
        L.t(xl - 1.8, yd, f"{v}   {C._r(d['rango_I_directo'])}", ha="right", bold=fuerte)
        L.t(xr + 1.8, yi, f"{C._r(d['rango_I_indirecto'])}   {v}", ha="left", bold=fuerte)
    yl = ytop - 14 * dy - 4.0
    L.ax.plot([1.5, 6.0], [yl, yl], color=AZUL, lw=3.2)
    L.t(7.2, yl, "Cambio de dos o más posiciones")
    L.ax.plot([48.0, 52.5], [yl, yl], color=MEDIO, lw=1.6)
    L.t(53.7, yl, "Cambio menor")
    return L.guardar("cA_f03")


# ============================================================ cA_f04: estabilidad de la clase en cinco escenarios
def cA_f04():
    L = Lienzo(10, 7.8, "Solo V05, V06 y V14 conservan su clase directa en los cinco escenarios",
               "Clase por mediana de cada variable en los escenarios S0 a S4; el marco grueso indica clase estable")
    ids = C.IDS
    x0, cw = 36.0, 11.2
    ch = 3.55
    ytop = L.top - 5.0
    for k, (e, _) in enumerate(C.ESC):
        L.t(x0 + (k + 0.5) * cw, ytop + ch / 2 + 0.4, e, ha="center", bold=True)
    cls = {e: {d["id"]: d["clase_mediana"] for d in C.S(e)["directa"]} for e, _ in C.ESC}
    CORTA = {"CRITICA": "Crítica", "ACTIVA": "Activa", "REACTIVA": "Reactiva", "AUTONOMA_RELATIVA": "Autónoma", "FRONTERA": "Frontera"}
    for i, v in enumerate(ids):
        yb = ytop - (i + 1) * ch
        L.t(x0 - 1.0, yb + ch / 2, f"{v}  {CORTO[v]}", ha="right")
        for k, (e, _) in enumerate(C.ESC):
            c = cls[e][v]
            L.ax.add_patch(Rectangle((x0 + k * cw, yb), cw, ch, fc=RELLENO[c], ec=T, lw=0.8, zorder=2))
            L.t(x0 + (k + 0.5) * cw, yb + ch / 2, CORTA[c], ha="center")
        if len({cls[e][v] for e, _ in C.ESC}) == 1:
            L.ax.add_patch(Rectangle((x0 - 0.3, yb - 0.1), 5 * cw + 0.6, ch + 0.2, fc="none", ec=T, lw=3.0, zorder=5))
    yl = ytop - 15 * ch - 3.6
    x = 1.0
    for c in ("CRITICA", "ACTIVA", "REACTIVA", "AUTONOMA_RELATIVA", "FRONTERA"):
        L.ax.add_patch(Rectangle((x, yl - 0.9), 3.0, 1.8, fc=RELLENO[c], ec=T, lw=1.0, zorder=5))
        lab = C.clase(c); L.t(x + 3.8, yl, lab)
        x += 3.8 + L.ancho(lab) + 2.8
    return L.guardar("cA_f04")


# ============================================================ cA_f05: DAG del efecto de la calibración sobre el error
def cA_f05():
    L = Lienzo(10, 7.8, "Sin asignación aleatoria, tres variables no medidas abren caminos alternativos entre la calibración y el error",
               "Grafo acíclico dirigido del efecto de X (calibración, V07) sobre Y (error de medición, V06); las líneas discontinuas son variables no medidas y retroalimentación")
    T0 = L.top
    hA, hB, hC = 9.0, 9.0, 11.0
    yA = T0 - 1.0 - hA
    yB = yA - 17.0 - hB
    yC = yB - 15.0 - hC
    xv5, wv5 = 3.0, 22.0
    xE, wE = 42.0, 24.0
    xM, wM = 75.0, 23.0
    # fila superior
    L.caja(xv5, yA, wv5, hA, "V05 Remoción de escombros", fc=CAJA)
    L.caja(xE, yA, wE, hA, "V01 y V02 Concentración de PM2,5 y PM10", fc=CAJA)
    L.caja(xM, yA, wM, hA, "V03 Humedad (modera) y V04 Viento", fc=CAJA)
    # fila central
    L.caja(xv5, yB, wv5, hB, "X · V07 Frecuencia de calibración", fc=MEDIO, lw=1.8)
    L.caja(xE, yB, wE, hB, "Y · V06 Error de medición", fc=AZUL, lw=2.2)
    L.caja(xM, yB, wM, hB, "V11 y V12 Índice y falsas alarmas; V15 Adopción", fc=CLARO)
    # fila inferior: no medidas
    L.caja(xv5, yC, 63.0, hC, "L1 distancia a la referencia, L2 edad del sensor y L3 episodios de humo", titulo="Variables no medidas", fc=CAJA, ls=(0, (4, 2.5)))
    # flechas
    L.flecha((xv5 + wv5, yA + hA / 2), (xE, yA + hA / 2))
    L.flecha((xE + wE / 2, yA), (xE + wE / 2, yB + hB))
    L.flecha((xM + 3.0, yA), (xE + wE - 3.0, yB + hB))
    L.flecha((xv5 + wv5, yB + hB / 2), (xE, yB + hB / 2), lw=2.2)
    L.t((xv5 + wv5 + xE) / 2, yB + hB / 2 + 3.6, "efecto\nde interés", ha="center")
    L.flecha((xE + wE, yB + hB / 2), (xM, yB + hB / 2))
    L.flecha((xv5 + 7.0, yC + hC), (xv5 + 7.0, yB), ls=(0, (4, 2.5)))
    L.flecha((xv5 + 15.0, yC + hC), (xv5 + 15.0, yB), ls=(0, (4, 2.5)))
    L.flecha((xE + wE / 2, yC + hC), (xE + wE / 2, yB), ls=(0, (4, 2.5)))
    # retroalimentación de V15 hacia X
    xr = xM + wM / 2; yr = yB - 7.5
    L.camino([(xr, yB), (xr, yr), (xv5 + wv5 - 3.0, yr), (xv5 + wv5 - 3.0, yB)], ls=(0, (4, 2.5)))
    L.t(xE + wE + 2.0, yr - 2.7, "V15 retroalimenta a X", ha="left")
    return L.guardar("cA_f05")


# ============================================================ cA_f06: árbol de problemas con identificadores y pesos
def cA_f06():
    L = Lienzo(10, 9.2, "El error de medición sin verificar (V06) conecta cuatro causas directas con dos efectos directos",
               "Árbol de problemas con los identificadores del modelo; sobre cada flecha, el peso del vínculo en S2 y su signo cuando es negativo")
    T0 = L.top
    alt = [9.0, 9.0, 12.0, 12.0, 6.5]; gap = 7.5
    yt = [T0 - 0.5]
    for a in alt[:-1]: yt.append(yt[-1] - a - gap)
    yb = [t - a for t, a in zip(yt, alt)]
    nombres = ["Efectos\nindirectos", "Efectos\ndirectos", "Problema\ncentral", "Causas\ndirectas", "Causa\nindirecta"]
    for k, nm in enumerate(nombres):
        L.t(1.0, yb[k] + alt[k] / 2, nm, bold=True)
    wb = 38.0; xs2 = [15.0, 58.0]
    L.caja(xs2[0], yb[0], wb, alt[0], "V14 Personas sin protección efectiva por alertas poco confiables", fc=CAJA)
    L.caja(xs2[1], yb[0], wb, alt[0], "V15 Baja adopción institucional del tablero y de las alertas", fc=CAJA)
    L.caja(xs2[0], yb[1], wb, alt[1], "V11 Índice local sin fórmula validada y con error de entrada", fc=CLARO)
    L.caja(xs2[1], yb[1], wb, alt[1], "V12 Tasa de falsas alarmas sin medir", fc=CLARO)
    xc, wc = 27.0, 56.0
    L.caja(xc, yb[2], wc, alt[2], "V06 Los consejos no disponen de mediciones de PM2,5 y PM10 con error conocido en los sitios de remoción", fc=AZUL, lw=2.4, bold_cuerpo=True)
    wcau, g = 19.5, 2.0
    cau = ["V03 Humedad relativa alta en los sitios", "V02 Fracción gruesa de PM10 sin corregir", "V01 PM2,5 sin referencia colocalizada", "V07 Calibración baja o nula"]
    xcs = [15.0 + i * (wcau + g) for i in range(4)]
    for x, t in zip(xcs, cau):
        L.caja(x, yb[3], wcau, alt[3], t, fc=MEDIO)
    xi, wi = 39.0, 36.0
    L.caja(xi, yb[4], wi, alt[4], "V05 Remoción de escombros en curso", fc=CAJA, ls=(0, (4, 2.5)))
    # flechas con peso
    def lab(x, y, s): L.t(x, y, s, ha="left", bold=True)
    for k, (v, w) in enumerate((("V11", "2"), ("V12", "2 (−)"))):
        xm = xs2[k] + wb / 2
        L.flecha((xm, yb[1] + alt[1]), (xm, yb[0]))
        lab(xm + 1.2, (yb[1] + alt[1] + yb[0]) / 2, w)
    for xe, xd, w in ((xs2[0] + wb / 2, xc + 17.0, "3"), (xs2[1] + wb / 2, xc + wc - 17.0, "2")):
        L.flecha((xd, yb[2] + alt[2]), (xe, yb[1]))
        lab((xd + xe) / 2 + 1.2, (yb[2] + alt[2] + yb[1]) / 2, w)
    for x, xe, w in zip(xcs, (xc + 7.0, xc + 21.0, xc + 40.0, xc + 51.0), ("3", "3", "2", "3 (−)")):
        L.flecha((x + wcau / 2, yb[3] + alt[3]), (xe, yb[2]))
        lab((x + wcau / 2 + xe) / 2 + 1.0, (yb[3] + alt[3] + yb[2]) / 2, w)
    for xdest, w in ((xcs[1] + wcau / 2, "3"), (xcs[2] + wcau / 2, "2")):
        L.flecha((xdest, yb[4] + alt[4]), (xdest, yb[3]))
        lab(xdest + 1.2, (yb[4] + alt[4] + yb[3]) / 2, w)
    return L.guardar("cA_f06")


# ============================================================ cA_f07: teoría del cambio por componente y techo de rendición de cuentas
def cA_f07():
    L = Lienzo(10, 9.4, "Cuatro cadenas llevan de los productos al uso y a la continuidad, y el proyecto se compromete hasta los resultados",
               "Teoría del cambio por componente; los rombos son supuestos críticos y la línea discontinua vertical es el techo de rendición de cuentas")
    T0 = L.top
    h, gap = 14.0, 6.0
    ys = [T0 - 1.0 - (k + 1) * h - k * gap for k in range(4)]
    xt, wt = 1.0, 12.0
    xp, wp = 15.0, 22.0
    xr, wr = 47.0, 22.0
    xi, wi = 77.0, 22.0
    lanes = [
        ("Medición", "Red de 100 nodos y 10 gateways con corrección local; 3 referencias y banco de calibración",
         "R1 Error frente a la referencia y R2 disponibilidad de nodos", None),
        ("Alertas y adopción", "Gemelo digital, tablero y protocolo de alerta",
         "R3 Uso institucional y R4 menos falsas alarmas", "I1 Activación del protocolo ante superación de umbral"),
        ("Custodia", "Convenios de custodia por tramos y plan de sostenibilidad",
         "R5 Capacidad instalada en custodios", "I2 Continuidad de la red bajo custodia"),
        ("Predicción", "Laboratorio de modelación y gemelo predictivo de demolición",
         "R6 Desempeño del gemelo y R7 evaluaciones previas entregadas", "Decisión de la entidad sobre método y control (sin indicador)"),
    ]
    for (nm, p, r, i_), y in zip(lanes, ys):
        L.t(xt, y + h / 2, nm, bold=True, w=wt)
        L.caja(xp, y, wp, h, p, fc=CAJA)
        L.caja(xr, y, wr, h, r, fc=MEDIO)
        if i_:
            L.caja(xi, y, wi, h, i_, fc=CLARO, ls=(0, (4, 2.5)))
    # supuestos críticos sobre las flechas
    def rombo_flecha(x0, x1, y, txt):
        xm = (x0 + x1) / 2
        L.ax.plot([x0, xm - 4.2], [y, y], color=T, lw=1.5, zorder=3); L.rombo(xm, y, 8.4, 6.4, txt, fs=FS, bold=True); L.flecha((xm + 4.2, y), (x1, y))
    ym = [y + h / 2 for y in ys]
    # lane 1: dos supuestos
    rombo_flecha(xp + wp, xr, ys[0] + h - 3.5, "SC-1")
    rombo_flecha(xp + wp, xr, ys[0] + 3.5, "SC-2")
    L.flecha((xp + wp, ym[1]), (xr, ym[1]))
    L.flecha((xp + wp, ym[2]), (xr, ym[2]))
    rombo_flecha(xr + wr, xi, ym[1], "SC-3")
    rombo_flecha(xr + wr, xi, ym[2], "SC-4")
    rombo_flecha(xp + wp, xr, ym[3], "SC-5")
    rombo_flecha(xr + wr, xi, ym[3], "SC-6")
    # la medición alimenta las alertas
    L.flecha((xr + wr / 2, ys[0]), (xr + wr / 2, ys[1] + h))
    # el uso justifica la custodia
    L.flecha((xi + wi / 2, ys[1]), (xi + wi / 2, ys[2] + h), ls=(0, (4, 2.5)))
    # techo de rendición de cuentas
    xtecho = xr + wr + 3.0 - 0.0
    xtecho = (xr + wr + xi) / 2 + 0.0
    L.ax.plot([xtecho, xtecho], [ys[3] - 2.0, T0 - 1.0 + 0.5], color=T, lw=1.6, ls=(0, (6, 3)), zorder=1)
    L.t(xtecho - 1.0, ys[3] - 3.4, "El proyecto compromete", ha="right", bold=True)
    L.t(xtecho + 1.0, ys[3] - 3.4, "El proyecto contribuye", ha="left", bold=True)
    return L.guardar("cA_f07")


if __name__ == "__main__":
    only = sys.argv[1:] or ["cA_f01", "cA_f02", "cA_f03", "cA_f04", "cA_f05", "cA_f06", "cA_f07"]
    for f in only:
        globals()[f]()
