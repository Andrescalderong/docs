# -*- coding: utf-8 -*-
"""Figuras del Anexo 2 del hilo principal: c15_f01 (cadena de valor), c21_f01 (Gantt), c22_f01 (matriz de riesgos),
c26_f01 (roles de la alianza), c28_f01 (presupuesto por rubro) y c28_f02 (flujo semestral). Cifras de A2/v2/m2.py y alianza.py."""
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/scripts")
from _comun import *
import alianza
from matplotlib.lines import Line2D


def leyenda(L, items, y, x0=1.0, gap=2.6, fs=FS, titulo=None, maxw=98.0):
    """Leyenda manual dentro del lienzo (sin objetos Legend). items: (tipo, color, etiqueta[, marcador]); tipo rect, rect_trama o marca."""
    x = x0; yy = y
    if titulo:
        L.t(x, yy, titulo, fs=fs, bold=True); x += L.ancho(titulo, fs, True) + gap
    for it in items:
        kind, color, label = it[:3]
        simb = 3.4 if kind.startswith("rect") else 2.6
        w = simb + 0.8 + L.ancho(label, fs)
        if x + w > maxw:
            x = x0; yy -= L.alto_linea(fs) + 0.8
        if kind == "rect":
            L.ax.add_patch(Rectangle((x, yy - 0.9), 3.0, 1.8, fc=color, ec=T, lw=1.0, zorder=5))
        elif kind == "rect_trama":
            L.ax.add_patch(Rectangle((x, yy - 0.9), 3.0, 1.8, fc=color, ec=T, lw=1.0, zorder=5))
            L.ax.add_patch(Rectangle((x, yy - 0.9), 3.0, 1.8, fc="none", ec=AZUL, lw=0, hatch="///", zorder=5.5))
        else:
            mk, ms, mfc = it[3], it[4] if len(it) > 4 else 9, it[5] if len(it) > 5 else BLANCO
            L.ax.plot([x + 1.0], [yy], marker=mk, ms=ms, mfc=mfc, mec=T, mew=1.3, ls="none", color=T, zorder=5)
        L.t(x + simb + 0.8, yy, label, fs=fs, ha="left")
        x += w + gap
    return yy


def rangos(ids):
    """Comprime una lista de actividades '1.1','1.2'... en '1.1 a 1.4, 1.6'."""
    out = []; i = 0
    key = lambda s: tuple(int(x) for x in s.split("."))
    ids = sorted(ids, key=key)
    while i < len(ids):
        j = i
        while j + 1 < len(ids) and key(ids[j + 1])[0] == key(ids[j])[0] and key(ids[j + 1])[1] == key(ids[j])[1] + 1:
            j += 1
        out.append(ids[i] if j == i else (f"{ids[i]}, {ids[j]}" if j == i + 1 else f"{ids[i]} a {ids[j]}"))
        i = j + 1
    return ", ".join(out)


# ============================================================ c15_f01
def c15_f01():
    OE = [("OE1", "Medición verificada", ["Prototipo validado: 1 sistema de 100 nodos y 10 gateways", "Documentos de investigación: 9",
                                           "Maestría en investigación: 2 personas", "Estancia posdoctoral: 1 persona", "Jóvenes investigadores: 6 personas"],
           ["1.1 Sitios y colocalización", "1.2 Lote 1 y referencias", "1.3 Tramo 1 y piloto", "1.4 Modelo y compuerta C1", "1.5 Tramo 2 y compuerta C2",
            "1.6 Desempeño final y ensayo", "1.7 Administración y supervisión"]),
          ("OE2", "Disponibilidad de la red", ["Infraestructura de medición: 1 infraestructura integrada"],
           ["2.1 Enlace y energía", "2.2 Firmware y plataforma", "2.3 Tramo 2", "2.4 Tramo 3", "2.5 Administración y supervisión"]),
          ("OE3", "Uso institucional y custodia", ["Documentos de planeación: 2", "Apropiación social: 29 actividades", "Asistencia técnica: 60 personas y 15 comités"],
           ["3.1 Umbrales y protocolo", "3.2 Uso del tablero", "3.3 Custodios y convenios", "3.4 Transferencia y cierre", "3.5 Administración y supervisión"])]
    h1 = "Tres objetivos específicos, nueve productos y 17 actividades se financian con %s millones del SGR" % num(m2.SGR / 1e6, 0)
    L = Lienzo(10, 10.2, h1=h1, h2="Valor solicitado al SGR por objetivo específico, en millones de pesos colombianos (COP); cada producto se cuenta una sola vez")
    xo, wo, xp, wp, xa, wa = 1.0, 24.0, 29.5, 33.0, 67.0, 32.0
    # encabezados de columna
    y = L.top - 0.5
    for x, w, s in ((xo, wo, "Objetivo específico"), (xp, wp, "Productos"), (xa, wa, "Actividades")):
        L.t(x, y, s, bold=True, va="center")
    y -= 3.2
    gap = 1.2
    for oe, nom, prods, acts in OE:
        hp = [L.necesita(wp, cuerpo=p, pad=0.8) for p in prods]
        ha = [L.necesita(wa, cuerpo=a, pad=0.8, trama=("Administración" in a), marco=0.9) for a in acts]
        sp = sum(hp) + 0.7 * (len(hp) - 1); sa = sum(ha) + 0.7 * (len(ha) - 1)
        H = max(sp, sa, 14)
        top = y
        # objetivo
        v = m2.POR_OE[oe]["sgr"] / 1e6
        L.caja(xo, top - H, wo, H, cuerpo="SGR: %s millones" % num(v, 1), titulo="%s. %s" % (oe, nom), fc=CLARO, fs=FS, pad=1.0)
        yy = top - (H - sp) / 2
        for p, h in zip(prods, hp):
            L.caja(xp, yy - h, wp, h, cuerpo=p, fc=CAJA, pad=0.8, ha="left")
            yy -= h + 0.7
        yy = top - (H - sa) / 2
        for a, h in zip(acts, ha):
            adm = "Administración" in a
            L.caja(xa, yy - h, wa, h, cuerpo=a, fc=MEDIO if adm else BLANCO, pad=0.8, ha="left", trama="///" if adm else None, marco=0.9)
            yy -= h + 0.7
        L.flecha((xo + wo, top - H / 2), (xp, top - H / 2), lw=1.4)
        L.flecha((xp + wp, top - H / 2), (xa, top - H / 2), lw=1.4)
        y = top - H - gap
    L.guardar("c15_f01")


# ============================================================ c21_f01
def c21_f01():
    cortos = {"1.1": "Sitios y colocalización", "1.2": "Lote 1 y referencias", "1.3": "Tramo 1 y piloto", "1.4": "Modelo y compuerta C1",
              "1.5": "Tramo 2 y compuerta C2", "1.6": "Desempeño final y ensayo", "1.7": "Administración y supervisión",
              "2.1": "Enlace y energía", "2.2": "Firmware y plataforma", "2.3": "Instalar tramo 2", "2.4": "Instalar tramo 3",
              "2.5": "Administración y supervisión", "3.1": "Umbrales y protocolo", "3.2": "Uso del tablero", "3.3": "Custodios y convenios",
              "3.4": "Transferencia y cierre", "3.5": "Administración y supervisión"}
    filas = []  # (tipo, texto, datos)
    for oe, nom in (("OE1", "Objetivo específico 1"), ("OE2", "Objetivo específico 2"), ("OE3", "Objetivo específico 3")):
        filas.append(("grupo", nom, None))
        for a in m2.ACTD.values():
            if a["oe"] == oe: filas.append(("act", f"{a['id']} {cortos[a['id']]}", a))
    filas.append(("relleno", "", None))
    filas.append(("hitos", "Hitos y compuertas", None))
    n = len(filas)
    L = Lienzo(10, 9.0, h1="Diecisiete actividades ocupan 24 meses y tres compuertas ordenan los hitos",
               h2="Cronograma mensual: actividades de ruta crítica, con holgura y de administración; compuertas C1, C2 y C3 e hitos H0 a H8")
    ax = eje_en_unidades(L, 34, 12.0, 98.5, L.top - 3.5)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(T)
    ax.set_xlim(0, 24); ax.set_ylim(n + 0.4, -0.8)
    ax.set_xticks([0, 3, 6, 9, 12, 15, 18, 21, 24]); ax.set_xticklabels(["0", "3", "6", "9", "12", "15", "18", "21", "24"], fontsize=FS, color=T)
    ax.set_yticks([]); ax.tick_params(axis="x", colors=T, length=4)
    ax.set_xlabel("Mes del proyecto", fontsize=FS, color=T, labelpad=4)
    ax.grid(axis="x", color=MEDIO, alpha=0.3, linestyle="--", linewidth=0.7); ax.set_axisbelow(True)
    for m in (12, 17, 24):
        ax.axvline(m, color=T, lw=1.0, ls=":", zorder=1)
    yhit = None
    for k, (tipo, txt, a) in enumerate(filas):
        if tipo == "grupo":
            ax.text(-0.4, k, txt, ha="right", va="center", fontsize=FS, fontweight="bold", color=T, clip_on=False)
            ax.axhline(k - 0.5, color=MEDIO, lw=0.8, zorder=0)
        elif tipo == "act":
            adm = a["id"].endswith(("7", "5")) and a["m_ini"] == 1 and a["m_fin"] == 24
            ax.text(-0.4, k, txt, ha="right", va="center", fontsize=FS, color=T, clip_on=False)
            x0, w = a["m_ini"] - 1, a["m_fin"] - a["m_ini"] + 1
            if adm:
                ax.barh(k, w, left=x0, height=0.56, color=MEDIO, edgecolor=T, linewidth=1.0, zorder=3)
                ax.barh(k, w, left=x0, height=0.56, color="none", edgecolor=AZUL, linewidth=0, hatch="///", zorder=3.5)
            else:
                crit = a["critica"]
                ax.barh(k, w, left=x0, height=0.56, color=AZUL if crit else CLARO, edgecolor=T, linewidth=1.0, zorder=3)
        else:
            yhit = k
            ax.text(-0.4, k, txt, ha="right", va="center", fontsize=FS, fontweight="bold", color=T, clip_on=False)
            ax.axhline(k - 0.5, color=MEDIO, lw=0.8, zorder=0)
    # hitos
    hit = [(h["id"], h["mes"]) for h in m2.HITOS]
    cmap = {"C3": 24}
    for i, (hid, mes) in enumerate(hit):
        if hid == "C3":
            continue
        comp = hid in ("H3", "H5")
        ax.plot([mes - 0.5], [yhit], marker="D" if comp else "o", ms=11 if comp else 8, mfc=T if comp else BLANCO, mec=T, mew=1.4, ls="none", color=T, zorder=6)
        up = (i % 2 == 0)
        ax.annotate(hid, xy=(mes - 0.5, yhit), xytext=(0, 14 if up else -15), textcoords="offset points", ha="center", va="center",
                    fontsize=FS, color=T, zorder=7)
    # compuerta C3 coincide con H8: rombo lleno en el mes 24
    ax.plot([24 - 0.5], [yhit], marker="D", ms=11, mfc=T, mec=T, ls="none", color=T, zorder=6)
    for m, s in ((12, "C1"), (17, "C2"), (24, "C3")):
        ax.text(m - 0.5, -0.55, s, ha="center", va="bottom", fontsize=FS, fontweight="bold", color=T, clip_on=False)
    # leyenda
    from matplotlib.patches import Patch
    leyenda(L, [("rect", AZUL, "Ruta crítica"), ("rect", CLARO, "Con holgura"), ("rect_trama", MEDIO, "Administración y supervisión"),
                ("marca", T, "Compuerta", "D", 10, T), ("marca", T, "Hito", "o", 8, BLANCO)], y=1.6, gap=2.0)
    L.guardar("c21_f01")


# ============================================================ c22_f01
def c22_f01():
    R = m2.RIESGOS
    pr = ["Probable", "Improbable", "Raro"]; im = ["Menor", "Moderado", "Mayor"]
    prob = sum(r["n_prob"] == "Probable" for r in R); mayor = sum(r["n_imp"] == "Mayor" for r in R)
    ambos = sum(r["n_prob"] == "Probable" and r["n_imp"] == "Mayor" for r in R)
    pal = {1: "Siete", 7: "siete", 12: "doce", 15: "quince"}
    assert (prob, mayor, len(R), ambos) == (7, 12, 15, 5)
    L = Lienzo(10, 8.0, h1="Siete de quince riesgos son probables y doce tienen impacto mayor, y cada uno tiene una respuesta asignada",
               h2="Matriz de probabilidad (raro, improbable, probable) e impacto (menor, moderado, mayor) de los 15 riesgos del registro")
    x0, y0 = 13.0, 21.0
    cw, ch = 28.0, 11.5
    top = L.top - 3.2
    ch = (top - y0) / 3
    sev = {(0, 2): AZUL, (0, 1): MEDIO, (1, 2): MEDIO, (0, 0): CLARO, (1, 1): CLARO, (2, 2): CLARO, (1, 0): GRIS, (2, 1): GRIS, (2, 0): GRIS}
    for i in range(3):
        for j in range(3):
            fc = sev[(i, j)]
            L.ax.add_patch(Rectangle((x0 + j * cw, top - (i + 1) * ch), cw, ch, fc=fc, ec=T, lw=1.2, zorder=1))
    for i, s in enumerate(pr):
        L.t(x0 - 1.2, top - (i + 0.5) * ch, s, ha="right", bold=True)
    for j, s in enumerate(im):
        L.t(x0 + (j + 0.5) * cw, y0 - 2.2, s, ha="center", bold=True)
    L.t(x0 + 1.5 * cw, y0 - 5.2, "Impacto", ha="center", bold=False)
    L.t(1.0, top + 1.6, "Probabilidad", ha="left", bold=False)
    marcador = {"Operacionales": "o", "Administrativos": "s", "Sanitarios": "^", "Legales": "D", "Financieros": "P", "De costos": "*", "De calendario": "X"}
    celdas = {}
    for r in R:
        celdas.setdefault((pr.index(r["n_prob"]), im.index(r["n_imp"])), []).append(r)
    for (i, j), lst in celdas.items():
        lst.sort(key=lambda r: r["id"])
        n = len(lst)
        cols = 2 if n > 3 else 1
        rows = (n + cols - 1) // cols
        wcol = (cw - 2) / cols
        for k, r in enumerate(lst):
            c, rr = k % cols, k // cols
            xx = x0 + j * cw + 1.5 + c * wcol
            yy = top - i * ch - (ch / (rows + 1)) * (rr + 1)
            L.ax.plot([xx + 1.0], [yy], marker=marcador[r["tipo"]], ms=9 if r["tipo"] != "De costos" else 12, mfc=BLANCO, mec=T, mew=1.3, ls="none", color=T, zorder=5)
            L.t(xx + 2.8, yy, r["id"], ha="left")
    leyenda(L, [("marca", T, tp, mk, 9 if tp != "De costos" else 12) for tp, mk in marcador.items()], y=y0 - 11.0, titulo="Tipo de riesgo:", gap=2.2)
    L.guardar("c22_f01")


# ============================================================ c26_f01
def c26_f01():
    OEN = [("OE1", "Medición verificada"), ("OE2", "Disponibilidad de la red"), ("OE3", "Uso institucional y custodia")]
    lid = alianza.LIDERA
    nombres = {"IES": "Universidad proponente", "ENT": "Municipio aliado", "SNCTI": "Actor del SNCTI", "EMP": "Empresa tecnológica"}
    aportes = {"IES": "Contrapartida C01 a C04: 1.100 millones en especie", "ENT": "Contrapartida C07: 120 millones en especie",
               "SNCTI": "Contrapartida C08: valor por certificar", "EMP": "Contrapartida C05 y C06: 210 millones en efectivo y 800 millones en especie"}
    for ac, txt in (("IES", 1.1e9), ("ENT", 1.2e8)):
        tot = sum(r["total"] for r in m2.CONTRA if r["fuente"] == ac)
        assert abs(tot - txt) < 1, (ac, tot)
    L = Lienzo(10, 9.2, h1="La alianza reparte capacidades entre cuatro integrantes y ocho aportes de contrapartida",
               h2="Función de cada integrante por objetivo específico y actividades en que participa; aportes de contrapartida de cada uno")
    xl, wl = 1.0, 28.0
    xc0, wc, gp = 31.0, 22.0, 0.8
    y = L.top - 0.3
    hh = 9.0
    for j, (oe, nom) in enumerate(OEN):
        L.caja(xc0 + j * (wc + gp), y - hh, wc, hh, cuerpo=nom, titulo=oe, fc=CLARO, pad=0.8)
    L.t(xl, y - hh / 2, "Integrante y aporte", bold=True)
    y -= hh + 1.0
    rh = 13.2
    for ac in alianza.ACTORES:
        L.caja(xl, y - rh, wl, rh, cuerpo=aportes[ac], titulo=nombres[ac], fc=CAJA, pad=0.8, ha="left", fs=FS, fs_t=FS)
        for j, (oe, nom) in enumerate(OEN):
            acts = alianza._por_oe(ac, oe)
            x = xc0 + j * (wc + gp)
            if acts:
                rol = "Lidera" if oe in lid[ac] else "Participa"
                fc = AZUL if rol == "Lidera" else BLANCO
                L.caja(x, y - rh, wc, rh, cuerpo=rangos(acts), titulo=rol, fc=fc, pad=0.8, lw=1.6 if rol == "Lidera" else 1.2,
                       trama=None if rol == "Lidera" else "...", marco=0.9)
            else:
                L.caja(x, y - rh, wc, rh, cuerpo="Sin función", fc=GRIS, ls="--", pad=0.8, lw=1.0)
        y -= rh + 0.9
    # actores que rodean
    L.t(xl, y - 1.0, "Actores de cambio y proveedores: comités de gestión del riesgo, custodios, laboratorio acreditado, laboratorio externo y evaluador externo.",
        w=98, va="top")
    L.guardar("c26_f01")


# ============================================================ c28_f01
def c28_f01():
    d = [(k, v) for k, v in m2.POR_RUBRO.items() if v > 0]
    d.sort(key=lambda kv: -kv[1])
    tot = m2.SGR
    top2 = (d[0][1] + d[1][1]) / tot
    assert abs(top2 - 0.7464) < 0.001
    L = Lienzo(10, 5.8, h1="El talento humano y los equipos suman tres cuartas partes del valor solicitado al SGR",
               h2="Valor solicitado al SGR por rubro, en millones de pesos colombianos (COP) y porcentaje del total")
    ax = eje_en_unidades(L, 40, 9.0, 83, L.top - 1.5)
    estilo_eje(ax)
    y = np.arange(len(d))
    for k, (r, v) in enumerate(d):
        ax.barh(k, v / 1e6, height=0.62, color=AZUL if k < 2 else CLARO, edgecolor=T, linewidth=1.1, zorder=3)
        ax.annotate("%s (%s %%)" % (num(v / 1e6, 1), num(v / tot * 100, 1)), xy=(v / 1e6, k), xytext=(7, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=FS, fontweight="bold", color=T)
    nom = {"Talento Humano": "Talento humano", "Equipos y software": "Equipos y software", "Capacitación y eventos": "Capacitación y eventos",
           "Servicios tecnológicos y pruebas": "Servicios tecnológicos\ny pruebas", "Materiales, insumos y documentación": "Materiales, insumos\ny documentación",
           "Protección del conocimiento y divulgación": "Protección del conocimiento\ny divulgación", "Gastos de viaje": "Gastos de viaje",
           "Infraestructura": "Infraestructura", "Administrativos": "Administrativos", "Seguimiento": "Seguimiento"}
    ax.set_yticks(y); ax.set_yticklabels([nom[r] for r, _ in d], fontsize=FS, color=T, linespacing=1.1)
    ax.invert_yaxis(); ax.set_ylim(len(d) - 0.4, -0.6)
    ax.set_xlim(0, 5400)
    ax.set_xticks([0, 1000, 2000, 3000, 4000, 5000]); ax.set_xticklabels(["0", "1.000", "2.000", "3.000", "4.000", "5.000"], fontsize=FS)
    ax.set_xlabel("Millones de COP", fontsize=FS, color=T, labelpad=5)
    ax.grid(axis="x", color=MEDIO, alpha=0.25, linestyle="--", linewidth=0.7); ax.set_axisbelow(True); ax.tick_params(axis="y", length=0)
    ax.text(4350, 6.2, "Talento humano\ny equipos: %s %%\ndel valor solicitado" % num(top2 * 100, 1), ha="center", va="center", fontsize=FS, fontweight="bold", color=T)
    L.guardar("c28_f01")


# ============================================================ c28_f02
def c28_f02():
    sg = [x / 1e6 for x in m2.FLUJO_SEM]; co = [x / 1e6 for x in m2.FLUJO_CON_SEM]
    tot = np.cumsum([a + b for a, b in zip(sg, co)])
    L = Lienzo(10, 5.5, h1="La ejecución del SGR se programa por semestres con picos en las compras de los tramos",
               h2="Valor por semestre en millones de pesos colombianos (COP): SGR y contrapartida; bajo cada semestre, el acumulado del total")
    ax = eje_en_unidades(L, 11, 13.0, 97, L.top - 1.5)
    estilo_eje(ax)
    x = np.arange(4)
    ax.bar(x, sg, width=0.55, color=AZUL, edgecolor=T, linewidth=1.1, zorder=3, label="SGR")
    ax.bar(x, co, bottom=sg, width=0.55, color=CLARO, edgecolor=T, linewidth=1.1, zorder=3, label="Contrapartida")
    ax.bar(x, co, bottom=sg, width=0.55, color="none", edgecolor=AZUL, linewidth=0, hatch="...", zorder=3.5)
    for i in range(4):
        ax.annotate(num(sg[i], 1), xy=(i, sg[i] / 2), ha="center", va="center", fontsize=FS, fontweight="bold", color=T, zorder=6,
                    bbox=dict(boxstyle="round,pad=0.15", fc=BLANCO, ec="none"))
        ax.annotate(num(co[i], 1), xy=(i, sg[i] + co[i] / 2), ha="center", va="center", fontsize=FS, color=T, zorder=6,
                    bbox=dict(boxstyle="round,pad=0.15", fc=BLANCO, ec="none"))
    ax.set_xticks(x); ax.set_xticklabels(["Semestre %d\nmeses %d a %d\nacumulado: %s" % (i + 1, 6 * i + 1, 6 * i + 6, num(tot[i], 0)) for i in range(4)], fontsize=FS, color=T)
    ax.set_ylim(0, 3900); ax.set_yticks([0, 1000, 2000, 3000]); ax.set_yticklabels(["0", "1.000", "2.000", "3.000"], fontsize=FS)
    ax.set_ylabel("Millones de COP por semestre", fontsize=FS, color=T, labelpad=6)
    ax.grid(axis="y", color=MEDIO, alpha=0.25, linestyle="--", linewidth=0.7); ax.set_axisbelow(True)
    leyenda(L, [("rect", AZUL, "SGR"), ("rect_trama", CLARO, "Contrapartida")], y=L.top - 1.0, x0=14.0, gap=3.0)
    L.guardar("c28_f02")


if __name__ == "__main__":
    which = sys.argv[1:] or ["c15", "c21", "c22", "c26", "c28a", "c28b"]
    for w in which:
        {"c15": c15_f01, "c21": c21_f01, "c22": c22_f01, "c26": c26_f01, "c28a": c28_f01, "c28b": c28_f02}[w]()
