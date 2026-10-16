# -*- coding: utf-8 -*-
"""Cálculos compartidos del paquete 1000X (documentos X1 a X9). Todo dato sale de maestro.py, indicadores.py y alternativas.py.
Clasificaciones (directo/indirecto, fijo/variable, importado, dependiente del plazo) son PROPUESTAS y se declaran en el texto."""
import sys, os, collections, math
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "maestro"))
sys.path.insert(0, os.path.join(RAIZ, "figs"))
import maestro as M
import indicadores as I
import alternativas as A

MM = 1_000_000
B = {l["id"]: l for l in M.BUDGET}
RES = M.resumen()
SGR = RES["sgr"]; CONTRA = RES["contra"]; TOTAL = RES["total"]; TOPE = M.IDENT["tope_cop"]

def mm(v, d=1):
    """Millones de COP con coma decimal y punto de miles."""
    return M.mm(v, d)

def pct(x, d=1):
    s = f"{x * 100:.{d}f}"
    return s.replace(".", ",")

def num(x, d=1):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def suma(ids):
    return sum(B[i]["total"] for i in ids)

# ---------------------------------------------------------------- clasificaciones (PROPUESTO)
IDS_INDIRECTOS = ["P06", "S07", "O05"]            # gestión y control (WP0) salvo importación y reserva
IDS_RESERVA = ["X01"]
IDS_VARIABLES = ["E01", "E02", "E04", "E05", "E06", "E12", "M03", "M07", "S05", "S10", "S11", "V01", "V02", "V03"]
IDS_IMPORTADOS = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09"]   # equipos físicos
IDS_PLAZO = [l["id"] for l in M.BUDGET if l["rubro"] == "Personal"] + ["E10", "E11", "E12", "S10", "O05"]

def clase(l):
    if l["id"] in IDS_RESERVA: return "Reserva"
    return "Indirecto" if l["id"] in IDS_INDIRECTOS else "Directo"

def comportamiento(l):
    if l["id"] in IDS_RESERVA: return "Reserva"
    return "Variable" if l["id"] in IDS_VARIABLES else "Fijo"

RUBROS = list(RES["por_rubro"].keys())

def matriz_costos():
    """Rubro x (clase, comportamiento) en COP."""
    out = collections.OrderedDict()
    for r in RUBROS:
        out[r] = collections.Counter()
    for l in M.BUDGET:
        out[l["rubro"]][(clase(l), comportamiento(l))] += l["total"]
    return out

def por_clase():
    c = collections.Counter(); f = collections.Counter()
    for l in M.BUDGET:
        c[clase(l)] += l["total"]; f[comportamiento(l)] += l["total"]
    return c, f

def por_wp():
    c = collections.OrderedDict((k, 0) for k in ("WP0", "WP1", "WP2", "WP3"))
    for l in M.BUDGET: c[l["wbs"]] += l["total"]
    return c

# ---------------------------------------------------------------- años, semestres y meses
def contra_por_fuente_y_anio():
    """Contrapartida por fuente y año con la distribución uniforme del maestro."""
    res = collections.OrderedDict()
    for l in M.CONTRA:
        fl = M.spread(l)
        clave = {"C05": "Empresa tecnológica (efectivo)", "C06": "Empresa tecnológica (especie)"}.get(l["id"], "IES (especie)")
        a = res.setdefault(clave, [0.0, 0.0])
        a[0] += sum(fl[:12]); a[1] += sum(fl[12:])
    return res

SGR_MES = M.flujo_sgr()
CON_MES = M.flujo_contra()
SGR_SEM = M.por_periodo(SGR_MES, 6)
CON_SEM = M.por_periodo(CON_MES, 6)
SGR_ANIO = M.por_periodo(SGR_MES, 12)
CON_ANIO = M.por_periodo(CON_MES, 12)

# ---------------------------------------------------------------- nodos-año operados (red CPM)
SEM_INICIO_OPERACION = {1: M.ACTS["A1.2"]["EF"], 2: M.ACTS["A2.3"]["EF"], 3: M.ACTS["A2.4"]["EF"]}   # semanas 24, 62 y 82
NODO_SEMANAS = sum(t["nodos"] * (M.DURACION_SEMANAS - SEM_INICIO_OPERACION[t["id"]]) for t in M.TRAMOS)
NODO_ANIOS = NODO_SEMANAS / 52.0

# ---------------------------------------------------------------- costos unitarios
def costos_unitarios():
    wp = por_wp()
    n, g = M.IDENT["nodos"], M.IDENT["gateways"]
    marg_nodo = (B["E01"]["vunit"] + B["E02"]["vunit"] * 150 / 120 + B["E05"]["vunit"] + B["M03"]["vunit"] + B["S05"]["vunit"])
    marg_gw = (B["E04"]["vunit"] + B["E06"]["vunit"] + B["S05"]["vunit"] + B["E12"]["vunit"] * 24 + B["S10"]["vunit"] * 22)
    marginal = marg_nodo + marg_gw / 10
    comites_meta = math.ceil(0.75 * 15)
    return dict(
        sgr_nodo=SGR / n, tot_nodo=TOTAL / n, sgr_gw=SGR / g, tot_gw=TOTAL / g,
        sgr_nodo_anio=SGR / NODO_ANIOS, tot_nodo_anio=TOTAL / NODO_ANIOS,
        marg_nodo=marg_nodo, marg_gw=marg_gw, marginal=marginal,
        ciclo=wp["WP1"] / 6, hora_nodo=wp["WP1"] / 60000, actividad=wp["WP3"] / 29,
        persona=B["S09"]["total"] / 60, comite=wp["WP3"] / comites_meta, comites_meta=comites_meta,
        benef=TOTAL / 150, benef_sgr=SGR / 150, por_comite=TOTAL / 15)

# ---------------------------------------------------------------- alternativas ALT-00 a ALT-03 (costo unitario por punto de medición)
def alternativas_costos():
    """Costo de la capa de medición por punto, en COP. ALT-01 usa un costo unitario de referencia PROPUESTO."""
    nodo = B["E01"]["vunit"] + B["E05"]["vunit"] + B["M03"]["vunit"] + B["S05"]["vunit"]
    gw_base = (B["E04"]["vunit"] + B["S05"]["vunit"]) / 10
    gw_sat = (B["E04"]["vunit"] + B["E06"]["vunit"] + B["S05"]["vunit"]) / 10
    verif_ref = (B["E03"]["total"] + B["S01"]["total"] + B["M01"]["total"]) / 100
    verif_full = verif_ref + (B["E07"]["total"] + B["S08"]["total"]) / 100
    est = B["E03"]["vunit"] + B["S05"]["vunit"]          # monitor de referencia + instalación
    est_enlace = B["E04"]["vunit"]                      # energía y enlace por estación (gateway como referencia)
    filas = [
        dict(id="ALT-00", nombre="Statu quo", equipo=nodo, enlace=0.0, verif=0.0, nat="CALCULADO"),
        dict(id="ALT-01", nombre="Estaciones fijas de referencia", equipo=est, enlace=est_enlace, verif=0.0, nat="PROPUESTO"),
        dict(id="ALT-02", nombre="Calibración centralizada en la nube", equipo=nodo, enlace=gw_base, verif=verif_ref, nat="PROPUESTO"),
        dict(id="ALT-03", nombre="Híbrida por tramos", equipo=nodo, enlace=gw_sat, verif=verif_full, nat="CALCULADO"),
    ]
    for f in filas:
        f["total"] = f["equipo"] + f["enlace"] + f["verif"]
        f["cien"] = f["total"] * 100
    # ALT-03 según presupuesto (incluye reserva de 20 nodos y un gateway)
    ids = ["E01", "E05", "M03", "S05", "E04", "E06", "E03", "S01", "M01", "E07", "S08"]
    pres_alt3 = suma(ids)
    return filas, pres_alt3, nodo

# ---------------------------------------------------------------- sensibilidad
def sensibilidad():
    base = SGR
    expo = {"Tipo de cambio de equipos importados": suma(IDS_IMPORTADOS),
            "Costo de personal": suma([l["id"] for l in M.BUDGET if l["rubro"] == "Personal"]),
            "Plazo de ejecución": suma(IDS_PLAZO),
            "Reserva de contingencia": B["X01"]["total"]}
    niveles = [-0.20, -0.10, 0.10, 0.20]
    filas = []
    for k, e in expo.items():
        filas.append(dict(nombre=k, expo=e, d={n: e * n for n in niveles}, swing=e * 0.40))
    filas.sort(key=lambda f: -f["swing"])
    pers = expo["Costo de personal"]; plz_otros = expo["Plazo de ejecución"] - pers; trm = expo["Tipo de cambio de equipos importados"]
    def esc(t, p, z, r=0.0):
        return trm * t + pers * ((1 + p) * (1 + z) - 1) + plz_otros * z + B["X01"]["total"] * r
    escenarios = [
        ("E0", "Base de la ficha", 0.0, 0.0, 0.0),
        ("E1", "Favorable: tipo de cambio −10 %", -0.10, 0.0, 0.0),
        ("E2", "Devaluación: tipo de cambio +20 %", 0.20, 0.0, 0.0),
        ("E3", "Presión de costos: personal +10 % y plazo +10 %", 0.0, 0.10, 0.10),
        ("E4", "Adverso combinado: tipo de cambio, personal y plazo +20 %", 0.20, 0.20, 0.20),
    ]
    out = []
    for cod, nom, t, p, z in escenarios:
        d = esc(t, p, z)
        out.append(dict(cod=cod, nombre=nom, delta=d, sgr=base + d, pct_tope=(base + d) / TOPE, por_nodo=(base + d) / M.IDENT["nodos"],
                        vs_reserva=B["X01"]["total"] - d))
    return filas, out, expo

# ---------------------------------------------------------------- riesgos
RIESGOS = M.RISKS
def riesgos_por_nivel():
    c = collections.OrderedDict((k, []) for k in ("EXTREMO", "ALTO", "MEDIO", "BAJO"))
    for r in RIESGOS: c[r["nivel"]].append(r)
    return c

def celdas_matriz():
    c = collections.defaultdict(list)
    for r in RIESGOS: c[(r["P"], r["I"])].append(r["id"])
    return c

def top5():
    return sorted(RIESGOS, key=lambda r: (-r["score"], -r["emv"], r["id"]))[:5]

def nivel_de(score):
    return "EXTREMO" if score >= 20 else "ALTO" if score >= 12 else "MEDIO" if score >= 6 else "BAJO"

# Tendencia planificada del índice de riesgo (PROPUESTO). Regla: la probabilidad P baja un nivel en cada compuerta cuyo criterio
# verifica la medida de mitigación del riesgo, con piso en P = 2 (ningún riesgo se elimina antes de la evidencia posproyecto).
# Ventana de exposición: el riesgo se retira del índice cuando termina la actividad que lo expone.
COMPUERTAS = [("Inicio", 0), ("Cierre del tramo 1 (C1, mes 12)", 12), ("Cierre del tramo 2 (C2, mes 17)", 17), ("Cierre del tramo 3 (C3, mes 24)", 24)]
PASOS = {   # riesgo: compuertas (índices 1..3) en las que P baja un nivel; ventana: mes final de exposición (None = hasta el cierre)
    "R-TEC-01": ([1, 2], None), "R-TEC-02": ([2], None), "R-TEC-03": ([2], None), "R-TEC-04": ([2], None),
    "R-ORG-01": ([1], None), "R-ORG-02": ([2], None), "R-EXT-01": ([], 19), "R-EXT-02": ([], None),
    "R-FIN-01": ([], 18), "R-FIN-02": ([], 2), "R-JUR-01": ([], None), "R-DAT-01": ([], None),
}

def tendencia():
    filas = []
    for r in RIESGOS:
        gates, ventana = PASOS[r["id"]]
        piso = 2
        p = r["P"]; vals = []
        for k, (nom, mes) in enumerate(COMPUERTAS):
            if k > 0 and k in gates: p = max(piso, p - 1)
            activo = (ventana is None) or (mes < ventana) or (k == 0)
            vals.append(p * r["I"] if activo else 0)
        filas.append(dict(id=r["id"], P=r["P"], I=r["I"], vals=vals, gates=gates, ventana=ventana))
    idx = [sum(f["vals"][k] for f in filas) for k in range(len(COMPUERTAS))]
    return filas, idx

if __name__ == "__main__":
    print("SGR", mm(SGR), "contra", mm(CONTRA), "total", mm(TOTAL))
    print("nodo-semanas", NODO_SEMANAS, "nodo-años", round(NODO_ANIOS, 2))
    cu = costos_unitarios()
    for k, v in cu.items(): print(" ", k, round(v / MM, 3) if isinstance(v, (int, float)) and v > 1000 else v)
    c, f = por_clase(); print({k: round(v / MM, 2) for k, v in c.items()}, {k: round(v / MM, 2) for k, v in f.items()})
    print({k: round(v / MM, 2) for k, v in por_wp().items()})
    fl, p3, nodo = alternativas_costos()
    for x in fl: print(x["id"], round(x["equipo"] / MM, 3), round(x["enlace"] / MM, 3), round(x["verif"] / MM, 3), round(x["total"] / MM, 3), round(x["cien"] / MM, 1))
    print("ALT-03 presupuesto por punto", round(p3 / MM / 100, 3))
    filas, esc, expo = sensibilidad()
    for x in filas: print(x["nombre"], round(x["expo"] / MM, 2), {k: round(v / MM, 1) for k, v in x["d"].items()})
    for e in esc: print(e["cod"], e["nombre"], round(e["delta"] / MM, 1), round(e["sgr"] / MM, 1), round(e["pct_tope"] * 100, 1), round(e["vs_reserva"] / MM, 1))
    print(contra_por_fuente_y_anio())
    print("SGR sem", [round(x / MM, 1) for x in SGR_SEM], "anio", [round(x / MM, 1) for x in SGR_ANIO])
    print({k: [r["id"] for r in v] for k, v in riesgos_por_nivel().items()})
    print(dict(celdas_matriz()))
    print([r["id"] for r in top5()])
    tf, idx = tendencia(); print(idx)
    for f_ in tf: print(f_["id"], f_["vals"])


def lienzo_libre2(h1, h2, figsize=(10, 7), xlim=(0, 100), ylim=(0, 70), top=0.89):
    """Lienzo sin ejes a sangre completa: H1 en negrita (hallazgo) y H2 (variable, periodo, unidades) como texto de figura."""
    import estilo as E
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=figsize)
    fig.subplots_adjust(left=0.005, right=0.995, bottom=0.01, top=top)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.axis("off")
    fs = 14 if len(h1) <= 84 else 13 if len(h1) <= 92 else 12
    fig.text(0.005, 0.985, h1, fontsize=fs, fontweight="bold", color=E.TINTA, ha="left", va="top")
    fig.text(0.005, 0.985 - 0.058 * (7.0 / figsize[1]), h2, fontsize=10, color=E.TINTA, ha="left", va="top")
    return fig, ax
