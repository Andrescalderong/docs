# -*- coding: utf-8 -*-
"""Figuras del capítulo 7 (EDT): c7_f01 (EDT completa de cinco niveles) y c7_f02 (organigrama del proyecto).
Datos: maestro.py (ACT/ACTS, HITOS, TRAMOS, BUDGET, CONTRA). Sin componente aleatorio.
Ejecución: python3 c7_figs.py
Regla de pertenencia (derivada de la red ACT): una actividad pertenece al primer hito alcanzable aguas abajo
desde ella misma; los hitos se definen por las actividades que usa HITOS en maestro.py."""
import os, sys, re, collections, textwrap
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "maestro")); sys.path.insert(0, os.path.join(RAIZ, "figs"))
import maestro as M
import estilo as E

# Actividades que definen cada hito en maestro.py (fin de la actividad = mes del hito)
HITO_DEF = {"H0": ["A0.1"], "H1": ["A1.1", "A2.1"], "H2": ["A1.3"], "H3": ["C1"], "H4": ["A1.5"],
            "H5": ["C2"], "H6": ["A2.4"], "H7": ["A1.6"], "H8": ["A3.4"]}
ORDEN_HITO = list(HITO_DEF)

def _h2(fig, ax, texto):
    ax.set_title("", loc="left")
    fig.text(0.008, 0.925, texto, fontsize=10, color=E.TINTA, ha="left", va="center")

def sucesores(a):
    return [k for k, v in M.ACTS.items() if a in v["pred"]]

def hito_de(a):
    """Primer hito alcanzable (incluida la propia actividad) aguas abajo en la red."""
    vistos = set(); cola = [a]; mejor = None
    while cola:
        x = cola.pop(0)
        if x in vistos: continue
        vistos.add(x)
        for h, defs in HITO_DEF.items():
            if x in defs and (mejor is None or ORDEN_HITO.index(h) < ORDEN_HITO.index(mejor)):
                mejor = h
        cola.extend(sucesores(x))
    return mejor

def fase_de(h):
    mes = dict((x[0], x[2]) for x in M.HITOS)[h]
    for t in M.TRAMOS:
        if t["m_ini"] <= mes <= t["m_fin"]: return t["id"]
    raise ValueError(h)

def estructura():
    """Devuelve {fase: {hito: {wp: [actividades ordenadas por inicio temprano]}}}."""
    est = collections.OrderedDict((t["id"], collections.OrderedDict()) for t in M.TRAMOS)
    for h in ORDEN_HITO:
        est[fase_de(h)][h] = collections.OrderedDict()
    for k in sorted(M.ACTS, key=lambda z: (M.ACTS[z]["ES"], z)):
        h = hito_de(k)
        est[fase_de(h)][h].setdefault(M.ACTS[k]["wp"], []).append(k)
    return est

FILL = {"WP0": E.GRIS, "WP1": E.CLARO, "WP2": E.MEDIO, "WP3": E.BLANCO}
CRIT = set(M.RUTA_CRITICA)

def conector(ax, x0, y0, x1, y1):
    xm = (x0 + x1) / 2
    ax.plot([x0, xm, xm, x1], [y0, y0, y1, y1], color=E.TINTA, lw=0.8, solid_capstyle="butt")

def f01():
    est = estructura()
    hitos = dict((x[0], x) for x in M.HITOS)
    n_act = len(M.ACT); n_hit = len(M.HITOS); n_seg = sum(len(v) for f in est.values() for v in f.values())
    n_fase = len(est)
    fig, ax = E.lienzo_libre(
        h1=f"La EDT descompone el proyecto en {n_fase} fases, {n_hit} entregables, {n_seg} segmentos de paquete y {n_act} actividades",
        h2=None, figsize=(10, 7.6), xlim=(0, 100), ylim=(0, 76))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.90, bottom=0.01)
    _h2(fig, ax, "Cinco niveles: proyecto, fase (tramo), entregable (hito), paquete de trabajo (WP) y actividad (ACT); borde grueso = ruta crítica")
    # cabeceras de nivel
    xs = {1: (0.5, 10.5), 2: (12.5, 27.5), 3: (30, 52), 4: (54.5, 61), 5: (63.5, 99.5)}
    etiquetas = {1: "Nivel 1\nProyecto", 2: "Nivel 2\nFase", 3: "Nivel 3\nEntregable", 4: "Nivel 4\nPaquete", 5: "Nivel 5\nActividad"}
    for n, (x0, x1) in xs.items():
        ax.text((x0 + x1) / 2, 72.8, etiquetas[n], ha="center", va="center", fontsize=8.5, fontweight="bold", color=E.TINTA)
        ax.plot([x0, x1], [70.6, 70.6], color=E.AZUL, lw=1.5)
    # filas de hojas
    hojas = []
    for f, hs in est.items():
        for h, wps in hs.items():
            for wp, acts in wps.items():
                for a in acts: hojas.append((f, h, wp, a))
    paso = 3.55; y0 = 68.0
    ypos = {}
    for i, (f, h, wp, a) in enumerate(hojas):
        ypos[(f, h, wp, a)] = y0 - i * paso
    # hojas (actividades)
    for (f, h, wp, a), y in ypos.items():
        act = M.ACTS[a]
        txt = f"{a} {act['nombre']} ({act['dur']} sem.)"
        E.caja(ax, xs[5][0], y - 1.25, xs[5][1] - xs[5][0], 2.5, txt, relleno=FILL[wp], borde=E.TINTA if a in CRIT else E.MEDIO,
               fs=6.6, grosor=2.2 if a in CRIT else 0.9, ha="left")
    # paquetes (hito, wp)
    centros_wp = {}
    for f, hs in est.items():
        for h, wps in hs.items():
            for wp, acts in wps.items():
                ys = [ypos[(f, h, wp, a)] for a in acts]; yc = sum(ys) / len(ys)
                centros_wp[(f, h, wp)] = yc
                E.caja(ax, xs[4][0], yc - 1.25, xs[4][1] - xs[4][0], 2.5, wp, relleno=FILL[wp], borde=E.MEDIO, fs=7.5, bold=True, grosor=1.0)
                for a in acts:
                    conector(ax, xs[4][1] + 0.25, yc, xs[5][0] - 0.25, ypos[(f, h, wp, a)])
    # entregables (hitos)
    centros_h = {}
    for f, hs in est.items():
        for h, wps in hs.items():
            yc_list = [centros_wp[(f, h, wp)] for wp in wps]
            yc = sum(yc_list) / len(yc_list); centros_h[(f, h)] = yc
            _, desc, mes, _v = hitos[h]
            E.caja(ax, xs[3][0], yc - 1.45, xs[3][1] - xs[3][0], 2.9, textwrap.fill(f"{h}, mes {mes}: {desc}", 46), relleno=E.CAJA, borde=E.AZUL, fs=6.4, grosor=1.2)
            for wp in wps:
                conector(ax, xs[3][1] + 0.25, yc, xs[4][0] - 0.25, centros_wp[(f, h, wp)])
    # fases
    centros_f = {}
    for t in M.TRAMOS:
        f = t["id"]
        ycs = [centros_h[(f, h)] for h in est[f]]
        yc = sum(ycs) / len(ycs); centros_f[f] = yc
        E.caja(ax, xs[2][0], yc - 2.2, xs[2][1] - xs[2][0], 4.4,
               f"Fase {f}\n{t['nombre'].split(': ')[1].capitalize()}\nMeses {t['m_ini']} a {t['m_fin']}; {t['compuerta']}",
               relleno=E.CLARO, borde=E.AZUL, fs=6.5, bold=False, grosor=1.5)
        for h in est[f]:
            conector(ax, xs[2][1] + 0.25, yc, xs[3][0] - 0.25, centros_h[(f, h)])
    # proyecto
    yp = sum(centros_f.values()) / len(centros_f)
    E.caja(ax, xs[1][0], yp - 4.5, xs[1][1] - xs[1][0], 9, f"Red IoT híbrida\ny gemelo digital\n({M.IDENT['duracion_meses']} meses,\n{M.DURACION_SEMANAS} semanas)", relleno=E.MEDIO, borde=E.AZUL, fs=6.9, bold=True, grosor=2)
    for f in centros_f:
        conector(ax, xs[1][1] + 0.25, yp, xs[2][0] - 0.25, centros_f[f])
    # leyenda de WP
    lx = 0.5; ly = 2.2
    ax.text(lx, ly + 1.8, "Relleno por paquete de trabajo", fontsize=7.2, fontweight="bold", color=E.TINTA, ha="left")
    nombres = {"WP0": "WP0 gestión", "WP1": "WP1 medición", "WP2": "WP2 red y plataforma", "WP3": "WP3 uso y custodia"}
    for i, wp in enumerate(["WP0", "WP1", "WP2", "WP3"]):
        x = lx + i * 17.5
        E.caja(ax, x, ly - 1.6, 3.2, 1.8, "", relleno=FILL[wp], borde=E.MEDIO, fs=6, grosor=0.9)
        ax.text(x + 4.2, ly - 0.7, nombres[wp], fontsize=7, color=E.TINTA, va="center", ha="left")
    return E.guardar(fig, "c7_f01")

# ---------------------------------------------------------------- organigrama
def personas(l):
    m = re.search(r"\((\d+)\)", l["concepto"])
    return int(m.group(1)) if m else 1

def f02():
    P = {l["id"]: l for l in M.BUDGET if l["rubro"] == "Personal"}
    por_wp = collections.OrderedDict((wp, [l for l in P.values() if l["wbs"] == wp]) for wp in ["WP0", "WP1", "WP2", "WP3"])
    tot = sum(personas(l) for l in P.values())
    pm = sum(l["cant"] for l in P.values())
    fig, ax = E.lienzo_libre(
        h1=f"El equipo del SGR suma {tot} cargos y {int(pm)} persona-mes en tres líneas técnicas",
        h2=None, figsize=(10, 6.2), xlim=(0, 100), ylim=(6, 70))
    fig.subplots_adjust(left=0.005, right=0.995, top=0.89, bottom=0.01)
    _h2(fig, ax, "Organigrama funcional; roles PROPUESTO; entidades SUPUESTO; cargos y persona-mes de BUDGET (P01 a P14)")
    # nivel 0: gobierno
    E.caja(ax, 27, 62, 46, 5.2, "Comité directivo (PROPUESTO)\nentidad ejecutora (IES) y empresa tecnológica (SUPUESTO)", relleno=E.MEDIO, borde=E.AZUL, fs=8.2, bold=True, grosor=1.6)
    E.caja(ax, 1, 62, 22, 5.2, "Evaluación externa\nindependiente (S07)\nmeses 12 y 24", relleno=E.GRIS, borde=E.MEDIO, fs=7.4, grosor=1.0)
    E.flecha(ax, (23.4, 64.6), (26.6, 64.6), ls="--", estilo="-")
    E.caja(ax, 77, 62, 22, 5.2, "Usuarios: comités de gestión\ndel riesgo (15) (SUPUESTO)", relleno=E.GRIS, borde=E.MEDIO, fs=7.4, grosor=1.0)
    E.flecha(ax, (76.6, 64.6), (73.4, 64.6), ls="--", estilo="-")
    # nivel 1: dirección científica y gerencia
    cont = {c["id"]: c for c in M.CONTRA}
    E.caja(ax, 4, 50, 38, 6.2, "Dirección científica (contrapartida IES en especie)\nC01 investigador principal; C02 y C03 coinvestigadores", relleno=E.CAJA, borde=E.TINTA, fs=7.6, grosor=1.2)
    g = P["P06"]
    E.caja(ax, 52, 50, 38, 6.2, f"Gerencia de proyecto (WP0)\nP06: {personas(g)} cargo, {int(g['cant'])} persona-mes", relleno=E.GRIS, borde=E.TINTA, fs=7.8, bold=True, grosor=1.6)
    E.flecha(ax, (50, 61.6), (71, 56.8), estilo="-|>")
    E.flecha(ax, (44, 61.6), (23, 56.8), estilo="-|>")
    E.flecha(ax, (42.3, 53.1), (51.6, 53.1), estilo="<|-|>")
    # nivel 2: tres líneas
    lineas = [("WP1", "Medición verificada (OE1)", 1.5), ("WP2", "Red, energía y plataforma (OE2)", 35.2), ("WP3", "Uso institucional y custodia (OE3)", 68.9)]
    for wp, nombre, x in lineas:
        ls = por_wp[wp]
        cargos = sum(personas(l) for l in ls); pmm = sum(l["cant"] for l in ls)
        E.caja(ax, x, 38.5, 29.6, 5.6, f"{wp} {nombre}\n{cargos} cargos; {int(pmm)} persona-mes", relleno=FILL[wp], borde=E.AZUL, fs=7.6, bold=True, grosor=1.6)
        E.flecha(ax, (71, 49.6), (x + 14.8, 44.7), estilo="-|>")
        # roles
        y = 34.2
        for l in sorted(ls, key=lambda z: z["id"]):
            nombre_r = re.sub(r"\s*\(\d+\)", "", l["concepto"])
            E.caja(ax, x, y - 3.4, 29.6, 3.6, f"{l['id']} {nombre_r}: {personas(l)}", relleno=E.BLANCO, borde=E.MEDIO, fs=6.4, grosor=0.9, ha="left")
            y -= 4.5
    ax.text(0.5, 6.4, "Los nombres de las personas y de las entidades quedan por definir: [DATO_USUARIO: nombres de entidad ejecutora, empresa tecnológica y equipo].",
            fontsize=7.2, color=E.TINTA, ha="left", va="bottom")
    return E.guardar(fig, "c7_f02")

if __name__ == "__main__":
    print(f01()); print(f02())
