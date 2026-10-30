# -*- coding: utf-8 -*-
"""Expansor de macros del Anexo 2: sustituye {{CLAVE}} por valores del libro maestro v2 y {{TABLA id generador}} por tablas.
Uso: python3 -I expand.py sec/s05.md  -> escribe out/s05.md (con directivas :::TABLA y :::FIGURA listas para ensamblar)."""
import sys, os, re, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import m2
from m2 import cop, mm, pct

# ---------------------------------------------------------------- números en letras (español, pesos)
U = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince",
     "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco",
     "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
D = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
C = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
def _menor_mil(n):
    if n == 0: return ""
    if n == 100: return "cien"
    c, r = divmod(n, 100); out = []
    if c: out.append(C[c])
    if r:
        if r < 30: out.append(U[r])
        else:
            d, u = divmod(r, 10); out.append(D[d] + (" y " + U[u] if u else ""))
    return " ".join(out)
def letras(n):
    n = int(n)
    if n == 0: return "cero"
    partes = []
    mill, resto = divmod(n, 1_000_000_000_000)
    for div, sing, plur in ((1_000_000_000, "mil millones", "mil millones"), (1_000_000, "millón", "millones"), (1_000, "mil", "mil")):
        q, n = divmod(n, div)
        if q == 0: continue
        if div == 1_000_000_000:
            # miles de millones: «ocho mil millones»
            partes.append("mil millones" if q == 1 else _menor_mil(q) + " mil millones")
        elif div == 1_000_000: partes.append("un millón" if q == 1 else _menor_mil(q) + " millones")
        else: partes.append("mil" if q == 1 else _menor_mil(q) + " mil")
    if n: partes.append(_menor_mil(n))
    s = " ".join(partes)
    s = s.replace("veintiuno mil", "veintiún mil").replace("uno mil", "un mil").replace("uno millones", "un millones")
    s = re.sub(r"\buno mil millones\b", "un mil millones", s)
    return s
def pesos_letras(n):
    s = letras(n)
    s = re.sub(r"\buno$", "un", s)
    return s + " pesos"

# ---------------------------------------------------------------- valores
R = m2.resumen()
def fmt(n): return f"{int(round(n)):,}".replace(",", ".")
V = {
 "SGR": cop(m2.SGR), "SGR_N": fmt(m2.SGR), "SGR_MM": mm(m2.SGR) + " millones de COP", "SGR_LETRAS": pesos_letras(m2.SGR),
 "CON": cop(m2.CON), "CON_N": fmt(m2.CON), "CON_MM": mm(m2.CON) + " millones de COP", "CON_LETRAS": pesos_letras(m2.CON),
 "CON_EF": cop(m2.CON_EFECTIVO), "CON_EF_MM": mm(m2.CON_EFECTIVO) + " millones de COP", "PCT_EF": pct(R["pct_efectivo"], 2),
 "TOTAL": cop(m2.TOTAL), "TOTAL_N": fmt(m2.TOTAL), "TOTAL_MM": mm(m2.TOTAL) + " millones de COP", "TOTAL_LETRAS": pesos_letras(m2.TOTAL),
 "TOPE": cop(m2.IDENT["tope_cop"]), "PCT_TOPE": pct(R["pct_tope"], 3), "HOLGURA": cop(R["holgura"]),
 "TRANSFER": cop(m2.TRANSFER), "TRANSFER_MM": mm(m2.TRANSFER) + " millones de COP", "PCT_TRANSFER": pct(R["pct_transfer"], 2),
 "MOV": cop(m2.MOVILIDAD), "PCT_MOV": pct(R["pct_mov"], 2),
 "TITULO": m2.IDENT["titulo"], "NOMBRE_LEN": str(len(m2.IDENT["titulo"])),
 "NODOS": "100", "NODOS_COMP": "120", "GW": "10", "GW_COMP": "11", "REFS": "1", "MUN": "2", "COMITES": "4", "SIGP": m2.IDENT["sigp"], "MESES": "24", "SEMANAS": "104",
 "TRL0": "4", "TRL1": "8", "TRL_PISO": "7",
 "OE1_SGR": mm(m2.POR_OE["OE1"]["sgr"]), "OE2_SGR": mm(m2.POR_OE["OE2"]["sgr"]), "OE3_SGR": mm(m2.POR_OE["OE3"]["sgr"]),
 "PERSONAL": cop(m2.POR_RUBRO["Talento Humano"]), "PCT_PERSONAL": pct(m2.POR_RUBRO["Talento Humano"] / m2.SGR),
 "EQUIPOS": cop(m2.POR_RUBRO["Equipos y software"]), "PCT_EQUIPOS": pct(m2.POR_RUBRO["Equipos y software"] / m2.SGR),
 "ADMIN": cop(m2.POR_RUBRO["Administrativos"]), "SEGUIM": cop(m2.POR_RUBRO["Seguimiento"]),
 "R_TH": cop(m2.POR_RUBRO["Talento Humano"]), "R_EQ": cop(m2.POR_RUBRO["Equipos y software"]), "R_CAP": cop(m2.POR_RUBRO["Capacitación y eventos"]),
 "R_SERV": cop(m2.POR_RUBRO["Servicios tecnológicos y pruebas"]), "R_MAT": cop(m2.POR_RUBRO["Materiales, insumos y documentación"]),
 "R_PROT": cop(m2.POR_RUBRO["Protección del conocimiento y divulgación"]), "R_VIAJE": cop(m2.POR_RUBRO["Gastos de viaje"]),
 "R_INFRA": cop(m2.POR_RUBRO["Infraestructura"]), "R_ADMIN": cop(m2.POR_RUBRO["Administrativos"]), "R_SEG": cop(m2.POR_RUBRO["Seguimiento"]),
 "N_INFORMES": str(len(m2.INFORMES)), "ADM_ACT": cop(m2.ACTD["1.8"]["sgr"]), "N_ACT": str(len(m2.ACTD)), "N_PROB": str(sum(1 for r in m2.RIESGOS if r["n_prob"] == "Probable")), "N_MAYOR": str(sum(1 for r in m2.RIESGOS if r["n_imp"] == "Mayor")), "N_AMBOS": str(sum(1 for r in m2.RIESGOS if r["n_prob"] == "Probable" and r["n_imp"] == "Mayor")), "N_OTROS": str(len(m2.RIESGOS) - sum(1 for r in m2.RIESGOS if r["n_prob"] == "Probable" and r["n_imp"] == "Mayor")), "N_RIESGOS": str(len(m2.RIESGOS)), "LAB_SGR": cop(sum(r["total"] for r in m2.LAB_LINEAS)), "LAB_CONTRA": cop(next(r["total"] for r in m2.CONTRA if r["id"] == "EQ-22")), "LAB_PCT": pct(sum(r["total"] for r in m2.LAB_LINEAS) / m2.SGR),
 "FLUJO1": mm(m2.FLUJO_SEM[0]), "FLUJO2": mm(m2.FLUJO_SEM[1]), "FLUJO3": mm(m2.FLUJO_SEM[2]), "FLUJO4": mm(m2.FLUJO_SEM[3]),
}

# ---------------------------------------------------------------- tablas
def e(s): return str(s).replace("|", "\\|").replace("\n", " ")
def tabla(tid, titulo, enc, filas, nota=None):
    L = [f":::TABLA {tid} | {titulo}", "| " + " | ".join(enc) + " |", "| " + " | ".join("---" for _ in enc) + " |"]
    for r in filas: L.append("| " + " | ".join(e(x) for x in r) + " |")
    if nota: L.append(":::NOTA " + nota)
    return "\n".join(L)

def t_presupuesto_rubro():
    f = [(k, cop(v), pct(v / m2.SGR)) for k, v in m2.POR_RUBRO.items() if v]
    f.append(("**Total solicitado al SGR**", "**" + cop(m2.SGR) + "**", "**100,0 %**"))
    return ("Valor solicitado al SGR por rubro del componente presupuestal", ["Rubro", "Valor (COP)", "Participación"], f,
            "*Nota.* Elaboración propia. Los rubros siguen el numeral 12.2 de los términos de referencia. Decimales con coma y miles con punto.")

def t_presupuesto_oe():
    f = []
    for oe, nm in (("OE1", "OE1. Medición verificada"), ("OE2", "OE2. Disponibilidad de la red"), ("OE3", "OE3. Uso institucional y custodia")):
        v = m2.POR_OE[oe]; f.append((nm, cop(v["sgr"]), cop(v["contra"]), cop(v["sgr"] + v["contra"])))
    f.append(("**Total**", "**" + cop(m2.SGR) + "**", "**" + cop(m2.CON) + "**", "**" + cop(m2.TOTAL) + "**"))
    return ("Valor del proyecto por objetivo específico", ["Objetivo específico", "SGR (COP)", "Contrapartida (COP)", "Total (COP)"], f,
            "*Nota.* Elaboración propia con el Anexo 3. Cada partida se asigna a su actividad principal, como en la hoja «Cronograma financiero» del Anexo 3; la administración y el seguimiento se registran en la actividad 1.8.")

def t_fuentes():
    def s(c): return cop(sum(r["total"] for r in m2.CONTRA if r["fuente"] == c))
    f = [("Asignación de CTeI del SGR", "Asignación de CTeI del SGR", cop(m2.SGR)),
         ("Universidad Santo Tomás, sede Villavicencio (proponente)", "Propios: especie", s("IES")),
         ("Municipio de Manizales", "Propios: especie", s("MAN")),
         ("Municipio de Calarcá", "Propios: especie", s("CAL")),
         ("Avanciencia (actor del SNCTI)", "Propios: especie", s("AVA")),
         ("**Total**", "", "**" + cop(m2.TOTAL) + "**")]
    return ("Resumen de las fuentes de financiación", ["Entidad", "Fuente de recursos", "Valor"], f,
            "*Nota.* Elaboración propia con el Anexo 3. Los aportes en especie y en efectivo requieren certificación firmada por el representante legal de cada entidad.")

def t_contrapartida():
    f = []
    quien_d = {"IES": "Universidad Santo Tomás", "MAN": "Municipio de Manizales", "CAL": "Municipio de Calarcá", "AVA": "Avanciencia"}
    for r in m2.CONTRA:
        quien = quien_d[r["fuente"]]
        modo = "Efectivo" if r["rubro"] == "Efectivo" else "Especie"
        acts = ", ".join(k for k, v in r["por_act"].items() if v)
        f.append((r["id"], quien, r["concepto"], modo, cop(r["total"]), acts))
    f.append(("", "**Total**", "", "", "**" + cop(m2.CON) + "**", ""))
    return ("Contrapartida por aportante, modalidad y actividad financiada", ["Código del Anexo 3", "Aportante", "Aporte", "Modalidad", "Valor (COP)", "Actividad"], f,
            "*Nota.* Elaboración propia con el Anexo 3. Cada aporte se cuantifica en términos monetarios y se sustenta con la certificación del representante legal de su entidad; el momento del aporte coincide con la ejecución de la actividad indicada.")

def t_talento():
    f = []
    for t in m2.TALENTO:
        f.append((t["cat"], str(t["n"]), f"{t['dur']} meses", cop(t["mensual"]), cop(t["total"]), t["cohortes"], t["productos"]))
    return ("Talento humano de formación vinculado al proyecto según el numeral 9 de los términos de referencia",
            ["Categoría", "Número", "Duración", "Valor mensual (COP)", "Valor total (COP)", "Vinculación", "Productos por persona"], f,
            "*Nota.* Elaboración propia con los montos del numeral 14.4 de los términos de referencia. El valor total de la maestría incluye la matrícula de hasta 48.000.000 COP por estudiante.")

def t_actividades():
    f = []
    for a in m2.ACTD.values():
        f.append((a["id"], a["nombre"], a["oe"], f"M{a['m_ini']}–M{a['m_fin']}", cop(a["sgr"]), cop(a["contra"])))
    f.append(("", "**Total**", "", "", "**" + cop(m2.SGR) + "**", "**" + cop(m2.CON) + "**"))
    return ("Actividades del proyecto, periodo y valor por fuente", ["N.º", "Actividad", "Objetivo", "Periodo", "SGR (COP)", "Contrapartida (COP)"], f,
            "*Nota.* Elaboración propia con el Anexo 3. Cada partida se asigna completa a su actividad principal, como en la hoja «Cronograma financiero» del Anexo 3; por eso las actividades 1.5, 2.4, 2.7, 2.8 y 3.6 no tienen asignación directa y se ejecutan con personal y bienes asignados a otras actividades del mismo objetivo.")

def t_cronograma():
    enc = ["Objetivo específico", "Producto", "Actividad"] + [str(m) for m in range(1, 25)]
    prod_oe = {"OE1": "Prototipo validado y documentos de investigación", "OE2": "Infraestructura de medición y de modelación dotada y operando", "OE3": "Documentos de planeación, apropiación social y asistencia técnica"}
    f = []; prev = None
    for a in m2.ACTD.values():
        marks = ["x" if a["m_ini"] <= m <= a["m_fin"] else "" for m in range(1, 25)]
        oe = {"OE1": "OE1", "OE2": "OE2", "OE3": "OE3"}[a["oe"]]
        f.append((oe if oe != prev else "", prod_oe[a["oe"]] if oe != prev else "", f"{a['id']} {a['nombre']}") + tuple(marks)); prev = oe
    return ("Cronograma de actividades por objetivo específico, en meses", enc, f,
            "*Nota.* Elaboración propia con el cronograma de ruta crítica de 104 semanas. Las compuertas C1 y C2 se ejecutan al final de las actividades 1.4 y 1.5; la compuerta C3 cierra el mes 24. Las actividades del laboratorio de modelación (1.7, 2.5, 2.6, 2.7 y 3.5) tienen holgura de 4 a 6 semanas y no integran la ruta crítica. Las actividades de administración y apoyo a la supervisión abarcan los 24 meses.")

def t_hitos():
    f = [(h["id"], h["desc"], f"Mes {h['mes']}", h["verif"]) for h in m2.HITOS]
    return ("Hitos y compuertas del proyecto con su evidencia de verificación", ["Hito", "Descripción", "Mes", "Evidencia de verificación"], f,
            "*Nota.* Elaboración propia.")

def t_flujo():
    f = [(f"Semestre {i + 1} (meses {6 * i + 1} a {6 * i + 6})", cop(m2.FLUJO_SEM[i]), cop(m2.FLUJO_CON_SEM[i]), cop(m2.FLUJO_SEM[i] + m2.FLUJO_CON_SEM[i])) for i in range(4)]
    f.append(("**Total**", "**" + cop(m2.SGR) + "**", "**" + cop(m2.CON) + "**", "**" + cop(m2.TOTAL) + "**"))
    return ("Programación semestral de los recursos", ["Periodo", "SGR (COP)", "Contrapartida (COP)", "Total (COP)"], f,
            "*Nota.* Elaboración propia con la hoja «Cronograma financiero» del Anexo 3. Los semestres coinciden con los cuatro giros del SGR de la proyección financiera del Anexo 3.")

def t_tramos():
    f = []
    for t in m2.M0.TRAMOS:
        f.append((t["nombre"], f"{t['m_ini']} a {t['m_fin']}", str(t["nodos"]), str(t["gateways"]), f"{t['compra_nodos']} / {t['compra_gw']}", t["compuerta"] + f" (mes {t['mes_compuerta']})"))
    f.append(("**Total**", "", "**100**", "**10**", "**120 / 11**", ""))
    return ("Tramos de despliegue de la red", ["Tramo", "Meses", "Nodos operativos", "Gateways operativos", "Compra de nodos / gateways", "Compuerta"], f,
            "*Nota.* Elaboración propia. Las compras incluyen 20 nodos y 1 gateway de reserva.")

def t_riesgos():
    f = []
    for r in m2.RIESGOS:
        f.append((r["tipo"], r["desc"], r["n_prob"], r["n_imp"], r["respuesta"]))
    return ("Análisis de riesgos del proyecto", ["Tipo de riesgo", "Descripción del riesgo", "Probabilidad", "Impacto", "Medidas de mitigación"], f,
            "*Nota.* Elaboración propia. Probabilidad: raro (menos de 20 %), improbable (20 a 39 %) o probable (40 % o más). Impacto: menor, moderado o mayor según la escala de 1 a 5 del registro de riesgos (4 o 5 es mayor). Las probabilidades son estimaciones de formulación sin serie histórica.")

def t_lineas_presupuesto():
    f = []
    for r in m2.BUD:
        q = r["cant"]; qs = fmt(q) if float(q).is_integer() else str(q).replace(".", ",")
        f.append((r["id"], r["rubro_tdr"], r["concepto"], r["unidad"], qs, cop(r["vunit"]), cop(r["total"]), r["act"], f"M{r['m_ini']}–M{r['m_fin']}"))
    f.append(("", "**Total**", "", "", "", "", "**" + cop(m2.SGR) + "**", "", ""))
    return ("Líneas del presupuesto solicitado al SGR con unidad, cantidad, costo unitario, actividad principal y periodo", ["Código del Anexo 3", "Rubro", "Concepto", "Unidad", "Cantidad", "Costo unitario (COP)", "Total (COP)", "Actividad principal", "Periodo"], f,
            "*Nota.* Elaboración propia con el Anexo 3. Los códigos, las cantidades, los valores, la actividad principal y el periodo son los del Anexo 3. Cada línea se soporta con un análisis de costos y al menos dos cotizaciones, que se cargan al radicar. Los valores incluyen el IVA cuando aplica y excluyen impuestos propios y seguros.")

TABLAS = {k[2:]: v for k, v in globals().items() if k.startswith("t_")}
import alianza
alianza.cop = cop; alianza.pct = pct
TABLAS.update(alianza.TABLAS_ALIANZA)
_mun = alianza.por_municipio(); _t = [sum(v[i] for v in _mun.values()) for i in range(3)]
V.update({"MUN_MAN": cop(_t[0]), "MUN_CAL": cop(_t[1]), "MUN_COMUN": cop(_t[2]), "PCT_MUN_COMUN": pct(_t[2] / m2.SGR), "PCT_MUN_LOC": pct((_t[0] + _t[1]) / m2.SGR),
          "TRAYECTOS": str(sum(r["cant"] for r in m2.BUD if r["id"] in ("VI-01", "VI-06"))), "DIAS_VEH": str(sum(r["cant"] for r in m2.BUD if r["id"] in ("VI-03", "VI-08"))),
          "SGR_M0": fmt(round(m2.SGR / 1e6)), "PCT_ESPECIE": pct((m2.CON - m2.CON_EFECTIVO) / m2.CON), "LICENCIAS_ANUAL": cop(next(r["total"] for r in m2.BUD if r["id"] == "EQ-21") / 2)})

_PAL = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce",
        15: "quince", 16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve", 20: "veinte", 21: "veintiuno", 22: "veintidós", 23: "veintitrés", 24: "veinticuatro", 25: "veinticinco"}
def palabra(n, cap=False):
    t = _PAL[int(n)]
    return t[0].upper() + t[1:] if cap else t
V.update({"N_PROB_P": palabra(V["N_PROB"], True), "N_RIESGOS_P": palabra(V["N_RIESGOS"]), "N_MAYOR_P": palabra(V["N_MAYOR"]), "N_ACT_P": palabra(V["N_ACT"], True)})
import causal
TABLAS.update(causal.TABLAS_CAUSAL)
V.update(causal.resumen())

# ---------------------------------------------------------------- v5: equipos e infraestructura del Anexo 3
import json as _json
_PART5 = {p["id"]: p for p in _json.load(open(os.path.join(os.path.dirname(HERE), "data_v5", "partidas.json"), encoding="utf-8"))}
def _acts_prods(pid):
    c = _PART5[pid]["campos"]
    j = str(c.get("JUSTIFICACIÓN") or c.get("Justificación") or c.get("DESCRIPCION") or c.get("JUSTIFICACION") or "")
    pre = j.split("·")[0] if "·" in j else j[:60]
    if pid == "IN-01":
        j = str(c.get("Descripción", "")).split("Justificación:")[-1]; pre = j.split("·")[0]
    acts = sorted(set(re.findall(r"(\d\.\d)", pre)), key=lambda x: (int(x[0]), int(x[2])))
    resto = j.split("·")[1] if "·" in j else ""
    prods = sorted(set(re.findall(r"\bP(\d)\b", resto[:40]) + re.findall(r"productos? (\d)", resto[:40])))
    return acts, prods
def t_equipos():
    import v5 as _v5
    f = []
    for r in m2.BUD:
        if r["rubro_tdr"] not in ("Equipos y software", "Infraestructura"): continue
        c = _PART5[r["id"]]["campos"]
        esp = _v5.ren(c.get("ESPECIFICACIONES TÉCNICAS") or c.get("Descripción") or "").split("\n")[0].replace("trazabilidad verificada por el actor del SNCTI", "trazabilidad metrológica verificada")
        acts, prods = _acts_prods(r["id"])
        q = r["cant"]; qs = fmt(q) if float(q).is_integer() else str(q).replace(".", ",")
        f.append((r["id"], r["concepto"], f"{qs} {r['unidad']}", esp, ", ".join(acts) or r["act"], ", ".join(prods) or "—", cop(r["total"])))
    tot = sum(r["total"] for r in m2.BUD if r["rubro_tdr"] in ("Equipos y software", "Infraestructura"))
    f.append(("", "**Total**", "", "", "", "", "**" + cop(tot) + "**"))
    return ("Equipos, software e infraestructura que se adquieren con recursos del SGR",
            ["Código del Anexo 3", "Bien", "Cantidad", "Especificación", "Actividades", "Productos", "Valor SGR (COP)"], f,
            "*Nota.* Elaboración propia con el Anexo 3. Las especificaciones, las cantidades, las actividades y los productos son los que declara el Anexo 3 para cada partida. Los productos se numeran como en la sección 20.")
TABLAS["equipos"] = t_equipos

def _expandir_tabla(m):
    tid, gen = m.group(1), m.group(2)
    t, enc, filas, nota = TABLAS[gen]()
    return tabla(tid, t, enc, filas, nota)

def expand(text):
    text = re.sub(r"^\{\{TABLA\s+(\S+)\s+(\S+)\}\}\s*$", _expandir_tabla, text, flags=re.M)
    def rv(m):
        k = m.group(1)
        if k not in V: raise KeyError(f"macro desconocida: {k}")
        return V[k]
    return re.sub(r"\{\{([A-Z0-9_]+)\}\}", rv, text)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        t = open(p, encoding="utf-8").read()
        out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(p))), "out_md", os.path.basename(p))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(expand(t)); print("ok", out)
