# -*- coding: utf-8 -*-
"""Datos derivados compartidos por los capítulos 17, 18, 20 y 21 (asignación A11).
Todo sale de maestro.py e indicadores.py (fuente única). Las clasificaciones de roles, pruebas y alcance son PROPUESTAS y se declaran en el texto.
Ejecución directa: python3 a11_datos.py  (imprime un resumen de control)."""
import sys, os, re, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "maestro"))
sys.path.insert(0, os.path.join(RAIZ, "figs"))
import maestro as M
import indicadores as I

MM = 1_000_000
B = {l["id"]: l for l in M.BUDGET}
C = {l["id"]: l for l in M.CONTRA}
RES = M.resumen()
IND = {i["cod"]: i for i in I.IND}

# ------------------------------------------------------------------ formato
def num(x, d=1):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def mm(v, d=1):
    return M.mm(v, d)

def pct(x, d=1):
    return num(x * 100, d) + " %"

def cop(v):
    return M.cop(v)

def cel(s):
    """Limpia una celda de tabla: sin barras verticales ni saltos."""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()

def nwords(s):
    return len(re.findall(r"\S+", s))

# ------------------------------------------------------------------ personal (P01 a P14) y contrapartida de personal (C01 a C03)
def personas(l):
    m = re.search(r"\((\d+)\)", l["concepto"])
    return int(m.group(1)) if m else 1

PERS = []
for l in M.BUDGET:
    if l["rubro"] != "Personal":
        continue
    n = personas(l)
    meses = l["m_fin"] - l["m_ini"] + 1
    PERS.append(dict(id=l["id"], concepto=l["concepto"], n=n, pm=l["cant"], meses=meses, ini=l["m_ini"], fin=l["m_fin"],
                     etc=l["cant"] / (n * meses), wp=l["wbs"], nat=l["nat"], total=l["total"]))
CPERS = [
    dict(id="C01", concepto="Investigador principal", n=1, etc=0.50, ini=1, fin=24, wp="WP0", nat=C["C01"]["nat"], total=C["C01"]["total"]),
    dict(id="C02", concepto="Coinvestigador técnico", n=1, etc=0.30, ini=1, fin=24, wp="WP1", nat=C["C02"]["nat"], total=C["C02"]["total"]),
    dict(id="C03", concepto="Coinvestigadores de ambiente y ciencias sociales", n=2, etc=0.20, ini=1, fin=24, wp="WP3", nat=C["C03"]["nat"], total=C["C03"]["total"]),
]
N_PERS = sum(p["n"] for p in PERS)                    # 29
PM_TOT = sum(p["pm"] for p in PERS)                   # 624
ETC_PROM = PM_TOT / M.IDENT["duracion_meses"]         # 26,0
N_CPERS = sum(p["n"] for p in CPERS)                  # 4
ETC_CPERS = sum(p["n"] * p["etc"] for p in CPERS)     # 1,2
PERFIL_MES = [0] * 24
for p in PERS:
    for m in range(p["ini"], p["fin"] + 1):
        PERFIL_MES[m - 1] += p["n"]
WP_PM = collections.OrderedDict()
WP_N = collections.OrderedDict()
WP_COP = collections.OrderedDict()
for wp in ("WP0", "WP1", "WP2", "WP3"):
    sel = [p for p in PERS if p["wp"] == wp]
    WP_PM[wp] = sum(p["pm"] for p in sel); WP_N[wp] = sum(p["n"] for p in sel); WP_COP[wp] = sum(p["total"] for p in sel)
assert N_PERS == 29 and PM_TOT == 624 and N_CPERS == 4
assert abs(sum(WP_COP.values()) - RES["por_rubro"]["Personal"]) < 1

CONTRA_IES = sum(l["total"] for l in M.CONTRA if l["fuente"] == "IES")      # 1.100 M
CONTRA_EMP_EF = C["C05"]["total"]                                           # 210 M
CONTRA_EMP_ES = C["C06"]["total"]                                           # 800 M
CONTRA_EMP = CONTRA_EMP_EF + CONTRA_EMP_ES
CONTRA_TOT = RES["contra"]
assert CONTRA_IES == 1_100_000_000 and CONTRA_EMP == 1_010_000_000 and CONTRA_TOT == CONTRA_IES + CONTRA_EMP
CONTRA_ESPECIE = CONTRA_TOT - CONTRA_EMP_EF

# ------------------------------------------------------------------ actividades por paquete
ACT_WP = collections.OrderedDict((wp, [a for a in M.ACT if a[4] == wp]) for wp in ("WP0", "WP1", "WP2", "WP3"))
WP_NOMBRE = {"WP0": "gestión, compuertas y cierre", "WP1": "medición verificada", "WP2": "red, energía y plataforma",
             "WP3": "uso institucional, apropiación y custodia"}

# ------------------------------------------------------------------ riesgos asignados a un nivel del marco lógico (PROPUESTO)
NIVEL_RIESGO = collections.OrderedDict([
    ("Fin", ["R-ORG-02"]),
    ("Propósito", ["R-ORG-01", "R-TEC-04", "R-DAT-01"]),
    ("Componentes", ["R-TEC-01", "R-TEC-02", "R-TEC-03", "R-FIN-01", "R-JUR-01"]),
    ("Actividades", ["R-EXT-01", "R-EXT-02", "R-FIN-02"]),
])
RK = {r["id"]: r for r in M.RISKS}
assert sorted(sum(NIVEL_RIESGO.values(), [])) == sorted(RK)
SUPUESTO_CRITICO = collections.OrderedDict([
    ("SC-1", ("Medición verificada", "Propósito")), ("SC-2", ("Energía y enlace", "Propósito")),
    ("SC-3", ("Uso institucional", "Propósito")), ("SC-4", ("Custodia", "Fin")),
])

def emv_nivel(n):
    return sum(RK[i]["emv"] for i in NIVEL_RIESGO[n]) / MM

# ------------------------------------------------------------------ marco lógico con nombres de componente sin ambigüedad con las compuertas
def ml_res(nivel):
    t = I.MARCO_LOGICO[nivel]["res"]
    t = t.replace("C1: ", "Componente 1: ").replace("C2: ", "Componente 2: ").replace("C3: ", "Componente 3: ")
    return t

def meta_ind(cod):
    return IND[cod]["mf"].replace("|desviación|", "desviación absoluta")

NIVEL_IND = collections.OrderedDict([
    ("Fin", [c for c in IND if c.startswith("PERS-S")]),
    ("Propósito", [c for c in IND if c.startswith("PERS-E")]),
    ("Componentes", [c for c in IND if c.startswith("PERS-P")]),
    ("Actividades", [c for c in IND if c.startswith("PERS-R")]),
])
assert [len(v) for v in NIVEL_IND.values()] == [2, 3, 4, 6]

# ------------------------------------------------------------------ ocho pruebas de coherencia del marco lógico (cálculo desde los objetos)
def pruebas():
    out = []
    # V1 actividades -> componentes
    n_act = len(M.ACT)
    asign = sum(len(v) for v in ACT_WP.values())
    comp_ok = all(len(ACT_WP[w]) > 0 for w in ("WP1", "WP2", "WP3"))
    out.append(dict(id="V1", tipo="Vertical", nombre="Actividades producen componentes",
                    regla="Cada componente tiene actividades que lo producen y cada actividad tiene paquete",
                    evidencia=f"{asign} de {n_act} actividades con paquete; WP1 {len(ACT_WP['WP1'])}, WP2 {len(ACT_WP['WP2'])}, WP3 {len(ACT_WP['WP3'])}, WP0 {len(ACT_WP['WP0'])}",
                    estado="CUMPLE" if (asign == n_act and comp_ok) else "NO CUMPLE",
                    accion="Sin acción."))
    # V2 componentes -> propósito
    oe_p = collections.defaultdict(list)
    for c in NIVEL_IND["Componentes"]: oe_p[IND[c]["oe"]].append(c)
    ok2 = all(oe in oe_p for oe in ("OE1", "OE2", "OE3"))
    out.append(dict(id="V2", tipo="Vertical", nombre="Componentes alcanzan el propósito",
                    regla="Cada objetivo específico tiene al menos un indicador de producto",
                    evidencia="; ".join(f"{oe}: {', '.join(c.replace('PERS-', '') for c in oe_p[oe])}" for oe in sorted(oe_p)),
                    estado="CUMPLE" if ok2 else "NO CUMPLE", accion="Sin acción."))
    # V3 propósito -> fin
    oe_e = sorted({IND[c]["oe"] for c in NIVEL_IND["Propósito"]}); oe_s = sorted({IND[c]["oe"] for c in NIVEL_IND["Fin"]})
    sin = [oe for oe in ("OE1", "OE2", "OE3") if oe not in oe_e or oe not in oe_s]
    out.append(dict(id="V3", tipo="Vertical", nombre="Propósito contribuye al fin",
                    regla="Cada objetivo tiene indicador de efecto y de impacto",
                    evidencia=f"Efecto e impacto solo en {', '.join(sorted(set(oe_e) & set(oe_s)))}; sin cobertura: {', '.join(sin)}",
                    estado="CUMPLE" if not sin else "PARCIAL",
                    accion="Verificar R², NRMSE, pendiente y sesgo en las compuertas y en el ensayo independiente"))
    # V4 supuestos
    niveles_sup = [n for n in I.MARCO_LOGICO if I.MARCO_LOGICO[n]["sup"]]
    ok4 = len(niveles_sup) == 4 and len(SUPUESTO_CRITICO) == 4
    out.append(dict(id="V4", tipo="Vertical", nombre="Supuestos por nivel",
                    regla="Cada nivel declara supuestos y cada supuesto crítico tiene nivel",
                    evidencia=f"{len(niveles_sup)} de 4 niveles con supuesto; SC-1 a SC-4 asignados",
                    estado="CUMPLE" if ok4 else "NO CUMPLE", accion="Sin acción."))
    # H1 indicador con fórmula, unidad y meta
    n1 = sum(1 for i in I.IND if i["formula"] and i["unidad"] and i["mf"])
    out.append(dict(id="H1", tipo="Horizontal", nombre="Indicador con fórmula y meta",
                    regla="Cada indicador tiene fórmula, unidad y meta final",
                    evidencia=f"{n1} de {len(I.IND)} indicadores completos",
                    estado="CUMPLE" if n1 == len(I.IND) else "NO CUMPLE", accion="Sin acción."))
    # H2 línea base
    vac = [i["cod"].replace("PERS-", "") for i in I.IND if i["lb_nat"] == "VACIO"]
    out.append(dict(id="H2", tipo="Horizontal", nombre="Línea base",
                    regla="Cada indicador tiene línea base",
                    evidencia=f"{len(I.IND) - len(vac)} de {len(I.IND)} con línea base; VACIO: {', '.join(vac)}",
                    estado="CUMPLE" if not vac else "PARCIAL",
                    accion="Medir las líneas base en el tramo 1 (DEC-F10)"))
    # H3 medio, fuente, frecuencia, responsable
    n3 = sum(1 for i in I.IND if i["verificacion"] and i["fuente"] and i["frecuencia"] and i["resp"])
    out.append(dict(id="H3", tipo="Horizontal", nombre="Medio de verificación",
                    regla="Cada indicador tiene medio, fuente, frecuencia y responsable",
                    evidencia=f"{n3} de {len(I.IND)} indicadores completos",
                    estado="CUMPLE" if n3 == len(I.IND) else "NO CUMPLE", accion="Sin acción."))
    # H4 trazabilidad a riesgo y presupuesto
    wp_con = [wp for wp in ("WP0", "WP1", "WP2", "WP3") if any(l["wbs"] == wp for l in M.BUDGET)]
    asig = len(sum(NIVEL_RIESGO.values(), []))
    out.append(dict(id="H4", tipo="Horizontal", nombre="Trazabilidad a riesgos y presupuesto",
                    regla="Cada nivel enlaza riesgos y cada paquete tiene presupuesto",
                    evidencia=f"{asig} de {len(M.RISKS)} riesgos asignados a un nivel; {len(wp_con)} de 4 paquetes con líneas de presupuesto",
                    estado="CUMPLE" if (asig == len(M.RISKS) and len(wp_con) == 4) else "NO CUMPLE", accion="Sin acción."))
    return out

PRUEBAS = pruebas()
N_CUMPLE = sum(1 for p in PRUEBAS if p["estado"] == "CUMPLE")
N_PARCIAL = sum(1 for p in PRUEBAS if p["estado"] == "PARCIAL")
N_NO = sum(1 for p in PRUEBAS if p["estado"] == "NO CUMPLE")

# ------------------------------------------------------------------ top 5 de riesgos por EMV (desempate por P×I)
TOP5 = sorted(M.RISKS, key=lambda r: (-r["emv"], -r["score"], r["id"]))[:5]

if __name__ == "__main__":
    print("personas SGR", N_PERS, "persona-mes", PM_TOT, "ETC prom", ETC_PROM, "contrapartida", N_CPERS, ETC_CPERS)
    print("perfil mensual", PERFIL_MES[0], PERFIL_MES[12])
    print("WP", dict(WP_PM), dict(WP_N), {k: v / MM for k, v in WP_COP.items()})
    print("EMV por nivel", {n: emv_nivel(n) for n in NIVEL_RIESGO})
    for p in PRUEBAS: print(p["id"], p["estado"], "|", p["evidencia"])
    print("cumple", N_CUMPLE, "parcial", N_PARCIAL, "no", N_NO)
    print("TOP5", [(r["id"], r["emv"] / MM, r["score"]) for r in TOP5])
    print("contra IES/EMP/ESPECIE", CONTRA_IES, CONTRA_EMP, CONTRA_ESPECIE, CONTRA_ESPECIE / CONTRA_TOT, CONTRA_TOT / RES["sgr"], CONTRA_TOT / RES["total"])
