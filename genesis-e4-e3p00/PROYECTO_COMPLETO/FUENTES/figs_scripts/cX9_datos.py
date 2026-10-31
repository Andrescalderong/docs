# -*- coding: utf-8 -*-
"""Valores de prosa (V) y tablas (T) del documento 1000X-09 (tablero de riesgos), calculados con cX_comun.py (registro de la ficha §7)."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
M = C.MM
mm, pct, num = C.mm, C.pct, C.num
from cX6_datos import tabla

V = {}; T = {}
R = {r["id"]: r for r in C.RIESGOS}
CORTA = {
    "R-TEC-01": "Humedad y polvo sesgan las lecturas de partículas",
    "R-TEC-02": "Baterías se agotan antes de 14 días sin sol",
    "R-TEC-03": "Falla de red celular aísla gateways",
    "R-TEC-04": "Modelo no generaliza entre departamentos",
    "R-ORG-01": "Comités no adoptan el tablero ni el protocolo",
    "R-ORG-02": "Custodios no asumen la operación posproyecto",
    "R-EXT-01": "Vías bloqueadas retrasan la instalación",
    "R-EXT-02": "Robo o vandalismo de nodos",
    "R-FIN-01": "Devaluación encarece equipos importados",
    "R-FIN-02": "Contrapartida en especie sin certificar a tiempo",
    "R-JUR-01": "Patente de terceros limita la libertad de operación",
    "R-DAT-01": "Incidente de ciberseguridad en la plataforma",
}
rn = C.riesgos_por_nivel()
suma_emv = sum(r["emv"] for r in C.RIESGOS)
def emv(ids): return sum(R[i]["emv"] for i in ids)
rojo = [r["id"] for r in rn["EXTREMO"] + rn["ALTO"]]; amar = [r["id"] for r in rn["MEDIO"]]; verde = [r["id"] for r in rn["BAJO"]]
V["n_rojo"] = str(len(rojo)); V["n_amar"] = str(len(amar)); V["n_alto"] = str(len(rn["ALTO"])); V["n_ext"] = str(len(rn["EXTREMO"]))
V["emv_rojo"] = mm(emv(rojo)); V["pct_emv_rojo"] = pct(emv(rojo) / suma_emv); V["emv_amar"] = mm(emv(amar))

# ---- t01 indicadores y semáforo
filas = [
    ["Riesgos identificados", "12", "Todos los del registro de la ficha §7", "CALCULADO"],
    ["Riesgos activos", "12", "Todos requieren seguimiento desde el acta de inicio", "PROPUESTO"],
    ["Riesgos materializados", "0", "La ejecución no ha iniciado", "PROPUESTO"],
    ["Riesgos mitigados", "0", "Las medidas están PLANIFICADAS y sin ejecutar", "PROPUESTO"],
    ["Semáforo rojo (P×I ≥ 12)", str(len(rojo)), "EXTREMO: " + ", ".join(r["id"] for r in rn["EXTREMO"]) + ". ALTO: " + ", ".join(r["id"] for r in rn["ALTO"]), "CALCULADO"],
    ["Semáforo amarillo (P×I de 6 a 11)", str(len(amar)), "MEDIO: " + ", ".join(amar), "CALCULADO"],
    ["Semáforo verde (P×I ≤ 5)", str(len(verde)), "BAJO: ninguno", "CALCULADO"],
    ["EMV de los riesgos en rojo (millones de COP)", mm(emv(rojo)), f"{pct(emv(rojo) / suma_emv)} % de la suma de EMV", "CALCULADO"],
    ["EMV de los riesgos en amarillo (millones de COP)", mm(emv(amar)), f"{pct(emv(amar) / suma_emv)} % de la suma de EMV", "CALCULADO"],
]
T["t01"] = tabla("t01", "Indicadores y semáforo del registro de riesgos al inicio de la ejecución",
                 ["Indicador", "Valor", "Detalle", "Naturaleza"], filas,
                 "*Nota.* Elaboración propia con datos del registro de riesgos de la ficha maestra (§7). La probabilidad y el impacto son estimaciones PROPUESTAS; P×I y EMV son CALCULADOS. El estado inicial es la línea base del tablero. Decimales con coma.")

# ---- t02 top 5
top = C.top5()
estado = "PLANIFICADA"
filas = []
for k, r in enumerate(top, 1):
    filas.append([str(k), f"{r['id']}: {CORTA[r['id']]}", f"{r['score']} ({r['nivel']})", mm(r["emv"]), r["respuesta"], r["disp"].replace("TRM supera en 10 % la de la cotización", "El tipo de cambio supera en 10 % el de la cotización"), r["resp"], estado])
T["t02"] = tabla("t02", "Cinco riesgos principales con respuesta, disparador, responsable y estado",
                 ["Orden", "Riesgo", "P×I (nivel)", "EMV (millones de COP)", "Respuesta planificada", "Disparador", "Responsable (rol)", "Estado"], filas,
                 "*Nota.* Elaboración propia con datos del registro de la ficha maestra. Orden por P×I y, en empate, por EMV. Los responsables son roles del presupuesto; los nombres son [DATO_USUARIO: nombres del personal responsable]. Decimales con coma.")
emv_top = sum(r["emv"] for r in top)
V["emv_top"] = mm(emv_top); V["pct_top"] = pct(emv_top / suma_emv)
V["emv_fin_tec"] = mm(R["R-FIN-01"]["emv"] + R["R-TEC-01"]["emv"]); V["pct_fin_tec"] = pct((R["R-FIN-01"]["emv"] + R["R-TEC-01"]["emv"]) / suma_emv)
V["emv_fin01"] = mm(R["R-FIN-01"]["emv"]); V["emv_tec01"] = mm(R["R-TEC-01"]["emv"])

# ---- t03 matriz 5x5
cel = C.celdas_matriz()
enc = ["P (filas) e I (columnas)", "I = 1", "I = 2", "I = 3", "I = 4", "I = 5"]
filas = []
for p in (5, 4, 3, 2, 1):
    fila = [f"P = {p}"]
    for i in range(1, 6):
        ids = cel.get((p, i), [])
        fila.append(", ".join(ids) + f" ({C.nivel_de(p * i)}, {p * i})" if ids else f"vacía ({C.nivel_de(p * i)}, {p * i})")
    filas.append(fila)
T["t03"] = tabla("t03", "Posición de los riesgos en la matriz de probabilidad e impacto de 5 por 5",
                 enc, filas,
                 "*Nota.* Elaboración propia con P e I del registro de la ficha maestra. Cada celda indica los riesgos, el nivel y el producto P×I. Naturaleza: CALCULADO a partir de estimaciones PROPUESTAS.")
ni = collections.Counter(r["I"] for r in C.RIESGOS); np_ = collections.Counter(r["P"] for r in C.RIESGOS)
V["n_i4"] = str(ni[4]); V["n_i5"] = str(ni[5]); V["n_i3"] = str(ni[3]); V["n_p3"] = str(np_[3]); V["n_p4"] = str(np_[4]); V["n_p2"] = str(np_[2])

# ---- t04 tendencia
tf, idx = C.tendencia()
nom_gate = {1: "C1", 2: "C2", 3: "C3"}
filas = []
for f in tf:
    gates = ", ".join(nom_gate[g] for g in f["gates"]) or "Ninguna"
    vent = "Hasta el cierre" if f["ventana"] is None else f"Hasta el mes {f['ventana']}"
    filas.append([f["id"], f"P {f['P']} × I {f['I']} = {f['P'] * f['I']}", gates, vent] + [str(v) for v in f["vals"]])
filas.append(["Índice de riesgo (suma)", "", "", ""] + [str(v) for v in idx])
filas.append(["Porcentaje del índice inicial", "", "", ""] + [pct(v / idx[0]) for v in idx])
filas.append(["Variación frente al punto anterior (%)", "", "", "", "—"] + [("−" if idx[k] < idx[k - 1] else "+") + pct(abs(idx[k] / idx[k - 1] - 1)) for k in (1, 2, 3)])
T["t04"] = tabla("t04", "Trayectoria planificada del índice de riesgo por tramo (hipótesis PROPUESTA)",
                 ["Riesgo", "Valor inicial", "Compuertas que reducen P", "Ventana de exposición", "Inicio (mes 0)", "Cierre tramo 1 (C1, mes 12)", "Cierre tramo 2 (C2, mes 17)", "Cierre tramo 3 (C3, mes 24)"], filas,
                 "*Nota.* Elaboración propia. Regla PROPUESTA: P baja un nivel en la compuerta cuyo criterio verifica la mitigación, con piso P = 2; un riesgo sale del índice al terminar su exposición. El índice es la suma de P×I de los riesgos abiertos. No es una medición ni una probabilidad.")
V["idx0"] = str(idx[0]); V["idx1"] = str(idx[1]); V["idx2"] = str(idx[2]); V["idx3"] = str(idx[3])
V["d1"] = pct(1 - idx[1] / idx[0]); V["d2"] = pct(1 - idx[2] / idx[1]); V["d3"] = pct(1 - idx[3] / idx[2]); V["dtot"] = pct(1 - idx[3] / idx[0])
V["rel1"] = pct(idx[1] / idx[0]); V["rel2"] = pct(idx[2] / idx[0]); V["rel3"] = pct(idx[3] / idx[0])
V["pts1"] = str(idx[0] - idx[1]); V["pts2"] = str(idx[1] - idx[2]); V["pts3"] = str(idx[2] - idx[3])

# ---- t05 reserva
cat = collections.OrderedDict()
for r in C.RIESGOS: cat[r["cat"]] = cat.get(r["cat"], 0) + r["emv"]
res = C.RES["reserva"]
filas = [
    ["Reserva total (suma de EMV redondeada)", mm(res), pct(res / suma_emv), "CALCULADO"],
    ["Reserva utilizada al inicio", "0,0", "0,0", "PROPUESTO"],
    ["Reserva disponible", mm(res), pct(res / suma_emv), "CALCULADO"],
    ["Suma de EMV sin redondeo", mm(suma_emv), "100,0", "CALCULADO"],
]
for k, v in cat.items():
    nom = {"Técnico": "técnicos", "Organizacional": "organizacionales", "Externo": "externos", "Financiero": "financieros", "Jurídico": "jurídicos", "Datos": "de datos"}[k]
    filas.append([f"EMV de los riesgos {nom}", mm(v), pct(v / suma_emv), "CALCULADO"])
T["t05"] = tabla("t05", "Reserva de contingencia: total, utilizada y disponible, y composición por categoría de riesgo",
                 ["Concepto", "Millones de COP", "% de la suma de EMV", "Naturaleza"], filas,
                 f"*Nota.* Elaboración propia con datos de maestro.py. La reserva equivale a {pct(res / C.SGR)} % del SGR solicitado. Su admisibilidad como rubro depende de los términos de referencia (VACIO). Decimales con coma.")
V["res"] = mm(res); V["suma_emv"] = mm(suma_emv); V["pct_res_sgr"] = pct(res / C.SGR)
V["tec_fin"] = mm(cat["Técnico"] + cat["Financiero"]); V["pct_tec_fin"] = pct((cat["Técnico"] + cat["Financiero"]) / suma_emv)
V["impactos"] = mm(sum(r["impacto"] for r in C.RIESGOS)); V["cobertura"] = pct(res / sum(r["impacto"] for r in C.RIESGOS))
V["tec"] = mm(cat["Técnico"]); V["fin"] = mm(cat["Financiero"])

if __name__ == "__main__":
    for k in sorted(V): print(k, "=", V[k])
    for k in sorted(T): print(); print(T[k])
