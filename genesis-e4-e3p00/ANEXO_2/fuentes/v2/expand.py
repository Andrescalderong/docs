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
 "CON_EF": cop(m2.CON_EFECTIVO), "CON_EF_MM": mm(m2.CON_EFECTIVO) + " millones de COP", "PCT_EF": pct(R["pct_efectivo"]),
 "TOTAL": cop(m2.TOTAL), "TOTAL_N": fmt(m2.TOTAL), "TOTAL_MM": mm(m2.TOTAL) + " millones de COP", "TOTAL_LETRAS": pesos_letras(m2.TOTAL),
 "TOPE": cop(m2.IDENT["tope_cop"]), "PCT_TOPE": pct(R["pct_tope"]), "HOLGURA": cop(R["holgura"]),
 "TRANSFER": cop(m2.TRANSFER), "TRANSFER_MM": mm(m2.TRANSFER) + " millones de COP", "PCT_TRANSFER": pct(R["pct_transfer"], 2),
 "MOV": cop(m2.MOVILIDAD), "PCT_MOV": pct(R["pct_mov"], 2),
 "TITULO": m2.IDENT["titulo"], "NOMBRE_LEN": str(len(m2.IDENT["titulo"])),
 "NODOS": "100", "NODOS_COMP": "120", "GW": "10", "GW_COMP": "11", "REFS": "3", "MUN": "12", "COMITES": "15", "MESES": "24", "SEMANAS": "104",
 "TRL0": "4", "TRL1": "8", "TRL_PISO": "7",
 "OE1_SGR": mm(m2.POR_OE["OE1"]["sgr"]), "OE2_SGR": mm(m2.POR_OE["OE2"]["sgr"]), "OE3_SGR": mm(m2.POR_OE["OE3"]["sgr"]),
 "PERSONAL": cop(m2.POR_RUBRO["Talento Humano"]), "PCT_PERSONAL": pct(m2.POR_RUBRO["Talento Humano"] / m2.SGR),
 "EQUIPOS": cop(m2.POR_RUBRO["Equipos y software"]), "PCT_EQUIPOS": pct(m2.POR_RUBRO["Equipos y software"] / m2.SGR),
 "ADMIN": cop(m2.POR_RUBRO["Administrativos"]), "SEGUIM": cop(m2.POR_RUBRO["Seguimiento"]),
 "R_TH": cop(m2.POR_RUBRO["Talento Humano"]), "R_EQ": cop(m2.POR_RUBRO["Equipos y software"]), "R_CAP": cop(m2.POR_RUBRO["Capacitación y eventos"]),
 "R_SERV": cop(m2.POR_RUBRO["Servicios tecnológicos y pruebas"]), "R_MAT": cop(m2.POR_RUBRO["Materiales, insumos y documentación"]),
 "R_PROT": cop(m2.POR_RUBRO["Protección del conocimiento y divulgación"]), "R_VIAJE": cop(m2.POR_RUBRO["Gastos de viaje"]),
 "R_INFRA": cop(m2.POR_RUBRO["Infraestructura"]), "R_ADMIN": cop(m2.POR_RUBRO["Administrativos"]), "R_SEG": cop(m2.POR_RUBRO["Seguimiento"]),
 "N_INFORMES": str(len(m2.INFORMES)), "ADM_ACT": cop(m2.ACTD["1.7"]["sgr"]),
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
            "*Nota.* Elaboración propia. Las actividades de administración y apoyo a la supervisión se reparten por partes iguales entre los tres objetivos.")

def t_fuentes():
    f = [("Asignación de CTeI del SGR", "Asignación de CTeI del SGR", cop(m2.SGR)),
         ("Entidad proponente (universidad)", "Propios: especie", cop(sum(r["total"] for r in m2.CONTRA if r["fuente"] == "IES"))),
         ("Entidad aliada 1 (municipio)", "Propios: especie", cop(sum(r["total"] for r in m2.CONTRA if r["fuente"] == "ENT"))),
         ("Entidad aliada 2 (actor del SNCTI)", "Propios: especie", "[Diligenciar: valor certificado del aporte]"),
         ("Entidad aliada 3 (empresa tecnológica)", "Propios: efectivo y especie", cop(sum(r["total"] for r in m2.CONTRA if r["fuente"] == "EMP"))),
         ("**Total**", "", "**" + cop(m2.TOTAL) + "**")]
    return ("Resumen de las fuentes de financiación", ["Entidad", "Fuente de recursos", "Valor"], f,
            "*Nota.* Elaboración propia. Los aportes en especie y en efectivo requieren certificación firmada por el representante legal de cada entidad. El total no incluye el aporte del actor del SNCTI, que se suma cuando se certifique.")

def t_contrapartida():
    f = []
    quien_d = {"IES": "Entidad proponente (universidad)", "EMP": "Entidad aliada 3 (empresa tecnológica)", "ENT": "Entidad aliada 1 (municipio)"}
    for r in m2.CONTRA:
        quien = quien_d[r["fuente"]]
        modo = "Efectivo" if r["rubro"] == "Efectivo" else "Especie"
        acts = ", ".join(k for k, v in r["por_act"].items() if v)
        f.append((r["id"], quien, r["concepto"], modo, cop(r["total"]), acts))
    f.append(("C08", "Entidad aliada 2 (actor del SNCTI)", "Horas de investigadores y uso de laboratorio del actor del SNCTI", "Especie", "[Diligenciar: valor certificado del aporte]", "1.1, 1.2, 1.4, 1.6, 3.3, 3.4"))
    f.append(("", "**Total**", "", "", "**" + cop(m2.CON) + "**", ""))
    return ("Contrapartida por aportante, modalidad y actividad financiada", ["Id", "Aportante", "Aporte", "Modalidad", "Valor (COP)", "Actividades"], f,
            "*Nota.* Elaboración propia. El aporte se cuantifica en términos monetarios y se sustenta con la certificación de cada entidad; el momento del aporte coincide con la ejecución de las actividades indicadas. El total no incluye el aporte C08, que se suma cuando el actor del SNCTI lo certifique.")

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
            "*Nota.* Elaboración propia. Los personales se reparten por duración de las actividades y los demás rubros por la actividad que los consume; el periodo resulta de convertir las semanas del cronograma a meses de 52/12 semanas.")

def t_cronograma():
    enc = ["Objetivo específico", "Producto", "Actividad"] + [str(m) for m in range(1, 25)]
    prod_oe = {"OE1": "Prototipo validado y documentos de investigación", "OE2": "Infraestructura de medición dotada y operando", "OE3": "Documentos de planeación, apropiación social y asistencia técnica"}
    f = []; prev = None
    for a in m2.ACTD.values():
        marks = ["x" if a["m_ini"] <= m <= a["m_fin"] else "" for m in range(1, 25)]
        oe = {"OE1": "OE1", "OE2": "OE2", "OE3": "OE3"}[a["oe"]]
        f.append((oe if oe != prev else "", prod_oe[a["oe"]] if oe != prev else "", f"{a['id']} {a['nombre']}") + tuple(marks)); prev = oe
    return ("Cronograma de actividades por objetivo específico, en meses", enc, f,
            "*Nota.* Elaboración propia con el cronograma de ruta crítica de 104 semanas. Las compuertas C1 y C2 se ejecutan al final de las actividades 1.4 y 1.5; la compuerta C3 cierra el mes 24. Las actividades de administración y apoyo a la supervisión abarcan los 24 meses.")

def t_hitos():
    f = [(h["id"], h["desc"], f"Mes {h['mes']}", h["verif"]) for h in m2.HITOS]
    return ("Hitos y compuertas del proyecto con su evidencia de verificación", ["Hito", "Descripción", "Mes", "Evidencia de verificación"], f,
            "*Nota.* Elaboración propia.")

def t_flujo():
    f = [(f"Semestre {i + 1} (meses {6 * i + 1} a {6 * i + 6})", cop(m2.FLUJO_SEM[i]), cop(m2.FLUJO_CON_SEM[i]), cop(m2.FLUJO_SEM[i] + m2.FLUJO_CON_SEM[i])) for i in range(4)]
    f.append(("**Total**", "**" + cop(m2.SGR) + "**", "**" + cop(m2.CON) + "**", "**" + cop(m2.TOTAL) + "**"))
    return ("Programación semestral de los recursos", ["Periodo", "SGR (COP)", "Contrapartida (COP)", "Total (COP)"], f,
            "*Nota.* Elaboración propia. Las compras de nodos, cabezales y gateways se programan en los meses 5, 13 y 18; los demás rubros se distribuyen de forma uniforme en su ventana de ejecución.")

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
        acts = ", ".join(k for k, v in r["por_act"].items() if v)
        f.append((r["id"], r["rubro_tdr"], r["concepto"], r["unidad"], fmt(r["cant"]), cop(r["vunit"]), cop(r["total"]), acts))
    f.append(("", "**Total**", "", "", "", "", "**" + cop(m2.SGR) + "**", ""))
    return ("Líneas del presupuesto solicitado al SGR con unidad, cantidad, costo unitario y actividades", ["N.º de línea", "Rubro", "Concepto", "Unidad", "Cantidad", "Costo unitario (COP)", "Total (COP)", "Actividades"], f,
            "*Nota.* Elaboración propia. Cada línea se soporta con al menos dos cotizaciones vigentes en el Anexo 3. Los valores excluyen impuestos propios y seguros, que los términos de referencia no financian con recursos del SGR.")

TABLAS = {k[2:]: v for k, v in globals().items() if k.startswith("t_")}
import alianza
alianza.cop = cop; alianza.pct = pct
TABLAS.update(alianza.TABLAS_ALIANZA)

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
