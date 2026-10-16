# -*- coding: utf-8 -*-
"""Biblioteca del documento técnico en formato Anexo 2: actividades, valoración por actividad, meses y números en letras."""
import sys, os, math
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

M = 1_000_000
SGR_T = D.resumen()["sgr"]; CON_T = D.resumen()["contra"]; TOT_T = SGR_T + CON_T

# ---------------------------------------------------------------- objetivos y actividades (17 + 3 de administración)
OE_ACT = {"OE1": ["A0.1", "A1.1", "A1.2", "A1.3", "A1.4", "C1", "A1.5", "A1.6", "ADM1"],
          "OE2": ["A2.1", "A2.2", "A2.3", "C2", "A2.4", "ADM2"],
          "OE3": ["A3.1", "A3.2", "A3.3", "A3.4", "ADM3"]}
NOM = {a[0]: a[1] for a in D.ACT}
NOM["ADM1"] = "Administración y apoyo a la supervisión (OE1)"
NOM["ADM2"] = "Administración y apoyo a la supervisión (OE2)"
NOM["ADM3"] = "Administración y apoyo a la supervisión (OE3)"
OE_DE = {a: oe for oe, l in OE_ACT.items() for a in l}
ORDEN = [a for oe in ("OE1", "OE2", "OE3") for a in OE_ACT[oe]]
DUR = {a[0]: a[2] for a in D.ACT}

def reparto(pesos):
    s = sum(pesos.values()); return {k: Fraction(v, s) for k, v in pesos.items()}
P_WP = {  # personal por paquete: proporcional a la duración de las actividades del paquete
    "WP0": reparto({k: DUR[k] for k in ("A0.1", "C1", "C2", "A3.4")}),
    "WP1": reparto({k: DUR[k] for k in ("A1.1", "A1.2", "A1.3", "A1.4", "A1.5", "A1.6")}),
    "WP2": reparto({k: DUR[k] for k in ("A2.1", "A2.2", "A2.3", "A2.4")}),
    "WP3": reparto({k: DUR[k] for k in ("A3.1", "A3.2", "A3.3")}),
}
N3 = reparto({"A1.2": 36, "A2.3": 48, "A2.4": 36})          # compras de nodos por tramo
G3 = reparto({"A1.2": 4, "A2.3": 4, "A2.4": 3})             # compras de gateways por tramo
O3 = reparto({"A1.3": 3, "A2.3": 4, "A2.4": 3})             # gateways en operación por tramo
S3 = reparto({"A1.3": 33, "A2.3": 44, "A2.4": 33})          # sitios por tramo
V3 = reparto({"A1.3": 16, "A2.3": 12, "A2.4": 12})
CAL = reparto({"A1.3": 16, "A1.5": 6, "A1.6": 16})
ASC3 = reparto({"A3.1": 24, "A3.2": 12, "A3.3": 16})
MAP = {
    "E01": N3, "E02": N3, "E05": N3, "M03": N3, "S11": N3, "E04": G3, "E06": O3, "E12": O3, "S10": O3, "S05": S3,
    "E03": {"A1.2": 1}, "E07": {"A1.2": 1}, "E08": {"A1.4": 1}, "E09": {"A1.1": 1}, "E10": {"A2.2": 1}, "E11": {"A2.2": 1},
    "M01": CAL, "M02": CAL, "S01": CAL, "M07": {"A2.3": Fraction(1, 2), "A2.4": Fraction(1, 2)},
    "S03": {"A2.3": Fraction(1, 2), "A2.4": Fraction(1, 2)}, "S06": {"A2.1": 1}, "S07": {"A3.4": 1}, "S08": {"A1.6": 1},
    "S09": {"A3.3": 1}, "S02": {"A3.3": 1}, "O03": {"A3.3": 1}, "O01": {"A1.6": 1}, "V04": {"A1.6": 1},
    "V01": V3, "V02": V3, "V03": V3, "M04": ASC3, "M05": ASC3, "M06": ASC3, "V05": ASC3, "O02": ASC3, "O06": ASC3,
    "O05": {"ADM1": Fraction(1, 3), "ADM2": Fraction(1, 3), "ADM3": Fraction(1, 3)},
    "X01": {"C1": Fraction(1, 2), "C2": Fraction(1, 2)},
}
VAL = {a: 0 for a in ORDEN}
LINEA_ACT = {}   # línea -> {actividad: valor}
for r in D.BUDGET:
    if r["fuente"] != "SGR": continue
    w = MAP.get(r["id"]) or P_WP[r["wbs"]]
    w = {k: Fraction(v) for k, v in w.items()}
    tot = r["total"]; asign = {}
    for k, f in w.items(): asign[k] = int(f * tot)
    resto = tot - sum(asign.values())
    kmax = max(w, key=lambda k: w[k]); asign[kmax] += resto
    LINEA_ACT[r["id"]] = asign
    for k, v in asign.items(): VAL[k] += v
assert sum(VAL.values()) == SGR_T, (sum(VAL.values()), SGR_T)
VOE = {oe: sum(VAL[a] for a in l) for oe, l in OE_ACT.items()}
assert sum(VOE.values()) == SGR_T

# ---------------------------------------------------------------- meses de cada actividad (semana -> mes)
def meses(a):
    if a.startswith("ADM"): return 1, 24
    s = D.ACTS[a]
    ini = int(s["ES"] * 12 / 52) + 1; fin = math.ceil(s["EF"] * 12 / 52)
    return max(1, ini), min(24, fin)

# ---------------------------------------------------------------- números
def mil(n, d=1):
    return num(n / M, d)

U = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce",
     "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro",
     "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
DEC = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
CEN = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

def _menor_mil(n):
    if n == 0: return ""
    if n == 100: return "cien"
    c, r = divmod(n, 100); out = []
    if c: out.append(CEN[c])
    if r:
        if r < 30: out.append(U[r])
        else:
            d, u = divmod(r, 10); out.append(DEC[d] + (" y " + U[u] if u else ""))
    return " ".join(out)

def _apo(t):
    """Apócope de 'uno' ante sustantivo masculino (un, veintiún)."""
    if t.endswith("veintiuno"): return t[:-9] + "veintiún"
    if t.endswith(" uno") or t == "uno": return t[:-3] + "un"
    return t

def letras(n):
    """Entero positivo en letras (hasta billones)."""
    if n == 0: return "cero"
    partes = []
    bill, n = divmod(n, 10**12); mm_total, n = divmod(n, 10**6); mil_, n = divmod(n, 10**3)
    if bill: partes.append("un billón" if bill == 1 else _apo(_menor_mil(bill)) + " billones")
    if mm_total:
        if mm_total == 1: partes.append("un millón")
        else:
            a, b = divmod(mm_total, 1000); t = []
            if a: t.append("mil" if a == 1 else _apo(_menor_mil(a)) + " mil")
            if b: t.append(_apo(_menor_mil(b)))
            partes.append(" ".join(t) + " millones")
    if mil_: partes.append("mil" if mil_ == 1 else _apo(_menor_mil(mil_)) + " mil")
    if n: partes.append(_menor_mil(n))
    return " ".join(partes)

def pesos_letras(n):
    de = " de" if n % 10**6 == 0 else ""
    return f"{letras(n)}{de} pesos ({cop(n)})"

if __name__ == "__main__":
    for oe, l in OE_ACT.items():
        print(oe, mil(VOE[oe]))
        for a in l: print("  ", a, NOM[a][:55], meses(a), mil(VAL[a]))
    print(pesos_letras(9267260000)); print(pesos_letras(2110000000)); print(pesos_letras(11377260000))
    print(letras(1100000000), '|', letras(210000000), '|', letras(21000000))
