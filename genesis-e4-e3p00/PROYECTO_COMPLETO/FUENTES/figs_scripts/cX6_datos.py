# -*- coding: utf-8 -*-
"""Valores de prosa (V) y tablas (T) del documento 1000X-06, calculados con cX_comun.py (maestro.py). Reproducible, sin semilla."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
M = C.MM
mm, pct, num = C.mm, C.pct, C.num

def tabla(id_, titulo, enc, filas, nota):
    out = [f":::TABLA {id_} | {titulo}", "| " + " | ".join(enc) + " |", "| " + " | ".join(["---"] * len(enc)) + " |"]
    for f in filas:
        out.append("| " + " | ".join(str(c) for c in f) + " |")
    out.append(f":::NOTA {nota}")
    return "\n".join(out)

V = {}; T = {}
tot = C.TOTAL; sgr = C.SGR; con = C.CONTRA
V["pct_sgr_tot"] = pct(sgr / tot); V["pct_con_tot"] = pct(con / tot)
V["sgr_a1"] = mm(C.SGR_ANIO[0]); V["sgr_a2"] = mm(C.SGR_ANIO[1])
V["tot_a1"] = mm(C.SGR_ANIO[0] + C.CON_ANIO[0]); V["tot_a2"] = mm(C.SGR_ANIO[1] + C.CON_ANIO[1])

# ---- t01 inversión por fuente y año
cf = C.contra_por_fuente_y_anio()
filas = [["SGR", "CALCULADO", mm(C.SGR_ANIO[0]), mm(C.SGR_ANIO[1]), mm(sgr), pct(sgr / tot)]]
nats = {"IES (especie)": "DECLARADO; desglose PROPUESTO", "Empresa tecnológica (efectivo)": "DECLARADO", "Empresa tecnológica (especie)": "DECLARADO"}
for k, (a1, a2) in cf.items():
    filas.append([k, nats[k], mm(a1), mm(a2), mm(a1 + a2), pct((a1 + a2) / tot)])
filas.append(["Alcaldías", "VACIO", "0,0", "0,0", "0,0", "0,0"])
filas.append(["Total del proyecto", "CALCULADO", mm(C.SGR_ANIO[0] + C.CON_ANIO[0]), mm(C.SGR_ANIO[1] + C.CON_ANIO[1]), mm(tot), "100,0"])
T["t01"] = tabla("t01", "Distribución de la inversión por fuente y año de ejecución, en millones de COP",
                 ["Fuente", "Naturaleza", "Año 1 (meses 1 a 12)", "Año 2 (meses 13 a 24)", "Total", "% del total"], filas,
                 "*Nota.* Elaboración propia con datos de la ficha maestra y de maestro.py. La contrapartida se distribuye de forma uniforme en 24 meses. Las compras de nodos, cabezales y gateways siguen las fechas de cada tramo. Decimales con coma.")

# ---- t02 costos por rubro y clase
mc = C.matriz_costos()
filas = []; col = collections.Counter()
for r in C.RUBROS:
    d_fijo = mc[r][("Directo", "Fijo")]; d_var = mc[r][("Directo", "Variable")]; ind = mc[r][("Indirecto", "Fijo")] + mc[r][("Indirecto", "Variable")]; res = mc[r][("Reserva", "Reserva")]
    t_ = d_fijo + d_var + ind + res
    for k, v in (("a", d_fijo), ("b", d_var), ("c", ind), ("d", res), ("e", t_)): col[k] += v
    filas.append([r, mm(d_fijo), mm(d_var), mm(ind), mm(res), mm(t_), pct(t_ / sgr)])
filas.append(["Total SGR", mm(col["a"]), mm(col["b"]), mm(col["c"]), mm(col["d"]), mm(col["e"]), "100,0"])
filas.append(["% del SGR", pct(col["a"] / sgr), pct(col["b"] / sgr), pct(col["c"] / sgr), pct(col["d"] / sgr), "100,0", "—"])
T["t02"] = tabla("t02", "Costos del SGR por rubro, clase y comportamiento, en millones de COP",
                 ["Rubro", "Directo fijo", "Directo variable", "Indirecto", "Reserva", "Total", "% del SGR"], filas,
                 "*Nota.* Elaboración propia con datos de maestro.py. Clasificación PROPUESTA: indirectos P06, S04, S07, O04 y O05; variables E01, E02, E04, E05, E06, E12, M03, M07, S05, S10, S11 y V01 a V03. Naturaleza: CALCULADO. Decimales con coma.")
V["directos"] = mm(col["a"] + col["b"]); V["pct_directos"] = pct((col["a"] + col["b"]) / sgr)
V["indirectos"] = mm(col["c"]); V["pct_indirectos"] = pct(col["c"] / sgr)
V["fijos"] = mm(col["a"] + col["c"]); V["pct_fijos"] = pct((col["a"] + col["c"]) / sgr)
V["variables"] = mm(col["b"]); V["pct_variables"] = pct(col["b"] / sgr)
V["pct_reserva"] = pct(col["d"] / sgr)
nat = collections.Counter()
for l in C.M.BUDGET: nat[l["nat"]] += l["total"]
V["pct_decl"] = pct(nat["DECLARADO"] / sgr); V["pct_prop"] = pct(nat["PROPUESTO"] / sgr)
V["decl"] = mm(nat["DECLARADO"]); V["prop"] = mm(nat["PROPUESTO"])
pers = [l for l in C.M.BUDGET if l["rubro"] == "Personal"]
V["pers_decl"] = mm(sum(l["total"] for l in pers if l["nat"] == "DECLARADO")); V["pers_prop"] = mm(sum(l["total"] for l in pers if l["nat"] == "PROPUESTO"))
V["expo_fx"] = mm(C.suma(C.IDS_IMPORTADOS)); V["pct_expo_fx"] = pct(C.suma(C.IDS_IMPORTADOS) / sgr)

# ---- t03 costos unitarios
cu = C.costos_unitarios(); wp = C.por_wp()
V["nodo_anios"] = num(C.NODO_ANIOS, 1); V["nodo_sem"] = num(C.NODO_SEMANAS, 0)
filas = [
    ["Costo por nodo operativo (SGR)", "SGR ÷ 100 nodos", mm(cu["sgr_nodo"]), "CALCULADO"],
    ["Costo por nodo operativo (total del proyecto)", "Total ÷ 100 nodos", mm(cu["tot_nodo"]), "CALCULADO"],
    ["Costo por gateway operativo (SGR)", "SGR ÷ 10 gateways", mm(cu["sgr_gw"]), "CALCULADO"],
    ["Costo por gateway operativo (total del proyecto)", "Total ÷ 10 gateways", mm(cu["tot_gw"]), "CALCULADO"],
    ["Costo por nodo-año operado (SGR)", f"SGR ÷ {num(C.NODO_ANIOS, 1)} nodos-año", mm(cu["sgr_nodo_anio"]), "CALCULADO"],
    ["Costo por nodo-año operado (total del proyecto)", f"Total ÷ {num(C.NODO_ANIOS, 1)} nodos-año", mm(cu["tot_nodo_anio"]), "CALCULADO"],
    ["Costo marginal de un nodo adicional", "Equipo, instalación y fracción de gateway y conectividad", mm(cu["marginal"]), "PROPUESTO"],
    ["Costo por output PERS-R02: ciclo de calibración", "WP1 ÷ 6 ciclos", mm(cu["ciclo"]), "CALCULADO"],
    ["Costo máximo por output PERS-R05: hora-nodo válida", "WP1 ÷ 60.000 horas-nodo (en COP)", num(cu["hora_nodo"], 0), "CALCULADO"],
    ["Costo por output PERS-P04: actividad de apropiación", "WP3 ÷ 29 actividades", mm(cu["actividad"]), "CALCULADO"],
    ["Costo esperado por outcome PERS-E03: persona certificada", "S09 ÷ 60 personas", mm(cu["persona"]), "CALCULADO"],
    ["Costo esperado por outcome PERS-E01: comité que usa el tablero", f"WP3 ÷ {cu['comites_meta']} comités", mm(cu["comite"]), "CALCULADO"],
    ["Costo por beneficiario directo (SUPUESTO)", "Total ÷ 150 funcionarios", mm(cu["benef"]), "CALCULADO"],
]
T["t03"] = tabla("t03", "Costos unitarios y costos por output y por outcome esperado, en millones de COP salvo indicación",
                 ["Indicador de costo", "Base de cálculo", "Valor", "Naturaleza"], filas,
                 f"*Nota.* Elaboración propia con datos de maestro.py e indicadores.py. WP1 = {mm(wp['WP1'])} y WP3 = {mm(wp['WP3'])} millones, sin gestión ni reserva. Los costos por outcome son costos esperados frente a la meta, no observados. Los costos por gateway y por nodo no son aditivos. Decimales con coma.")
V["nodo_tot"] = mm(cu["tot_nodo"]); V["nodo_sgr"] = mm(cu["sgr_nodo"]); V["marginal"] = mm(cu["marginal"]); V["pct_marginal"] = pct(cu["marginal"] / cu["tot_nodo"])
V["nodo_anio_tot"] = mm(cu["tot_nodo_anio"]); V["nodo_anio_sgr"] = mm(cu["sgr_nodo_anio"])
V["ciclo"] = mm(cu["ciclo"]); V["persona"] = mm(cu["persona"]); V["comite"] = mm(cu["comite"]); V["actividad"] = mm(cu["actividad"])
V["hora_nodo"] = num(cu["hora_nodo"], 0); V["benef"] = mm(cu["benef"]); V["wp1"] = mm(wp["WP1"]); V["wp3"] = mm(wp["WP3"])
V["comites_meta"] = str(cu["comites_meta"])

# ---- t04 alternativas
filas_a, pres3, nodo = C.alternativas_costos()
pts = dict(zip(["ALT-00", "ALT-01", "ALT-02", "ALT-03"], [round(x + 1e-9, 2) for x in C.A.BASE]))
a3 = [f for f in filas_a if f["id"] == "ALT-03"][0]["total"]
filas = []
for f in filas_a:
    filas.append([f"{f['id']}: {f['nombre']}", mm(f["equipo"], 2), mm(f["enlace"], 2), mm(f["verif"], 2), mm(f["total"], 2), mm(f["cien"], 1),
                  num(f["total"] / a3, 2), num(pts[f["id"]], 2), f["nat"]])
T["t04"] = tabla("t04", "Costo unitario de la capa de medición por punto en las alternativas ALT-00 a ALT-03, en millones de COP",
                 ["Alternativa", "Equipo e instalación", "Energía y enlace", "Verificación", "Total por punto", "Costo de 100 puntos", "Razón frente a ALT-03", "Puntaje multicriterio", "Naturaleza"], filas,
                 f"*Nota.* Elaboración propia con datos de maestro.py y alternativas.py. El costo de ALT-01 es un valor de referencia PROPUESTO: monitor de referencia (E03) más instalación (S05) más gateway como energía y enlace (E04). El presupuesto de ALT-03 incluye 20 nodos y un gateway de reserva: {mm(pres3 / 100, 2)} por punto. Los puntajes son PROPUESTOS y están sujetos a ratificación. Decimales con coma.")
V["alt00"] = mm(filas_a[0]["total"], 1); V["alt01"] = mm(filas_a[1]["total"], 1); V["alt02"] = mm(filas_a[2]["total"], 1); V["alt03"] = mm(a3, 1)
V["alt01_100"] = mm(filas_a[1]["cien"], 1); V["alt03_100"] = mm(a3 * 100, 1); V["alt00_100"] = mm(filas_a[0]["cien"], 1); V["alt02_100"] = mm(filas_a[2]["cien"], 1)
V["razon01"] = num(filas_a[1]["total"] / a3, 1); V["razon03_00"] = num(a3 / filas_a[0]["total"], 1); V["razon02"] = pct(filas_a[2]["total"] / a3, 0)
V["alt03_pres"] = mm(pres3 / 100, 1); V["nodo_inst"] = mm(nodo, 1)
V["n_alt01"] = str(int(C.RES["por_rubro"]["Equipos y software"] // (filas_a[1]["total"])))
V["eq_rubro"] = mm(C.RES["por_rubro"]["Equipos y software"])

# ---- t05 y t06 sensibilidad
filas_s, esc, expo = C.sensibilidad()
reglas = {"Plazo de ejecución": "Personal, E10, E11, E12, S04, S10, O04 y O05",
          "Costo de personal": "Líneas P01 a P14",
          "Tipo de cambio de equipos importados": "Equipos físicos E01 a E09",
          "Reserva de contingencia": "Línea X01"}
filas = []
for f in filas_s:
    d = f["d"]
    filas.append([f["nombre"], mm(f["expo"]), "−" + mm(-d[-0.2]), "−" + mm(-d[-0.1]), "+" + mm(d[0.1]), "+" + mm(d[0.2]), mm(f["swing"]), reglas[f["nombre"]]])
T["t05"] = tabla("t05", "Variación del valor solicitado al SGR por variable y nivel de cambio, en millones de COP",
                 ["Variable", "Base expuesta", "−20 %", "−10 %", "+10 %", "+20 %", "Intervalo total", "Líneas expuestas"], filas,
                 "*Nota.* Elaboración propia con datos de maestro.py. Una variable cambia a la vez y las demás permanecen en su base. El plazo y el personal comparten líneas de costo. Naturaleza: CALCULADO con reglas de exposición PROPUESTAS. Decimales con coma.")
V["plazo20"] = mm(filas_s[0]["d"][0.2]); V["pers20"] = mm(filas_s[1]["d"][0.2]); V["fx20"] = mm(filas_s[2]["d"][0.2]); V["res20"] = mm(filas_s[3]["d"][0.2])
V["plazo_expo"] = mm(filas_s[0]["expo"]); V["pers_expo"] = mm(filas_s[1]["expo"])
V["mes_plazo"] = mm(filas_s[0]["expo"] / 24); V["mes_pers"] = mm(filas_s[1]["expo"] / 24)
V["pct_plazo20"] = pct(filas_s[0]["d"][0.2] / sgr)
V["meses_plazo20"] = num(24 * 0.2, 1)
filas = []
for e in esc:
    cobertura = "No aplica" if e["cod"] == "E0" else ("Cubre la reserva" if e["vs_reserva"] >= 0 and e["delta"] > 0 else ("Sin uso de reserva" if e["delta"] <= 0 else f"Déficit de {mm(-e['vs_reserva'])}"))
    d = "0,0" if e["cod"] == "E0" else (("+" if e["delta"] > 0 else "−") + mm(abs(e["delta"])))
    filas.append([e["cod"], e["nombre"], d, mm(e["sgr"]), pct(e["pct_tope"]), mm(e["por_nodo"], 1), cobertura])
T["t06"] = tabla("t06", "Escenarios de sensibilidad del valor solicitado al SGR, en millones de COP",
                 ["Código", "Escenario", "Variación", "SGR resultante", "% del tope declarado", "SGR por nodo", "Frente a la reserva de 636,0"], filas,
                 "*Nota.* Elaboración propia con datos de maestro.py. El tope de $ 14.000.000.000 es DECLARADO y NO_VERIFICADO. El SGR por nodo divide entre 100 nodos operativos. Los escenarios son ILUSTRATIVOS y no tienen probabilidad asignada. Decimales con coma.")
e = {x["cod"]: x for x in esc}
V["e2_delta"] = mm(e["E2"]["delta"]); V["e3_delta"] = mm(e["E3"]["delta"]); V["e4_delta"] = mm(e["E4"]["delta"]); V["e1_delta"] = mm(-e["E1"]["delta"])
V["e2_sgr"] = mm(e["E2"]["sgr"]); V["e3_sgr"] = mm(e["E3"]["sgr"]); V["e4_sgr"] = mm(e["E4"]["sgr"])
V["e3_def"] = mm(-e["E3"]["vs_reserva"]); V["e4_def"] = mm(-e["E4"]["vs_reserva"]); V["e4_pct"] = pct(e["E4"]["pct_tope"]); V["e3_pct"] = pct(e["E3"]["pct_tope"])
V["impactos"] = mm(sum(r["impacto"] for r in C.RIESGOS)); V["razon_imp"] = num(sum(r["impacto"] for r in C.RIESGOS) / C.RES["reserva"], 1)

# ---- t07 rentabilidad
filas = [
    ["Valor presente neto (VPN)", "NO_APLICA", "El proyecto no genera ingresos propios"],
    ["Tasa interna de retorno (TIR)", "NO_APLICA", "Sin flujos de ingreso no existe tasa que anule el VPN"],
    ["Período de recuperación", "NO_APLICA", "Sin ingresos no hay recuperación de la inversión"],
    ["Retorno sobre la inversión (ROI)", "NO_APLICA", "Sin ingresos ni beneficios monetizados"],
    ["Punto de equilibrio", "NO_APLICA", "No hay venta de producto ni de servicio"],
    ["Razón costo-beneficio", "NO_CALCULABLE", "Ninguna fuente valora en pesos los beneficios; el proyecto no promete efectos en salud"],
    ["Costo-efectividad (MCE36)", "CALCULADO", "Costo por output y por outcome esperado en la tabla de costos unitarios"],
]
T["t07"] = tabla("t07", "Estado de los indicadores de rentabilidad y de costo-beneficio",
                 ["Indicador", "Estado", "Razón"], filas,
                 "*Nota.* Elaboración propia. El modelo de negocio es de valor público: financiación durante el proyecto y custodia posterior, sin ingresos inventados. Naturaleza: PROPUESTO.")

# ---- t08 flujo de caja semestral
sg, cn = C.SGR_SEM, C.CON_SEM
ac = 0; filas_f = []
egr = [a + b for a, b in zip(sg, cn)]
acum = []; s_ = 0
for x in egr: s_ += x; acum.append(s_)
cols = lambda lst, tot_=None: [mm(x) for x in lst] + [mm(tot_ if tot_ is not None else sum(lst))]
filas = [
    ["Egresos SGR"] + cols(sg),
    ["Egresos de contrapartida"] + cols(cn),
    ["Egresos totales"] + cols(egr),
    ["Ingresos propios", "0,0", "0,0", "0,0", "0,0", "0,0"],
    ["Egreso total acumulado"] + [mm(x) for x in acum] + [mm(acum[-1])],
    ["Ejecución acumulada (%)"] + [pct(x / tot) for x in acum] + ["—"],
]
T["t08"] = tabla("t08", "Flujo de caja semestral del proyecto, en millones de COP",
                 ["Concepto", "Semestre 1 (meses 1 a 6)", "Semestre 2 (meses 7 a 12)", "Semestre 3 (meses 13 a 18)", "Semestre 4 (meses 19 a 24)", "Total"], filas,
                 "*Nota.* Elaboración propia con datos de maestro.py. Egreso programado, no desembolso: la programación de desembolsos del SGR no se aportó (VACIO). La reserva de contingencia se distribuye de forma uniforme. Naturaleza: CALCULADO. Decimales con coma.")
V["s1_pct"] = pct(acum[0] / tot); V["s2_pct"] = pct(acum[1] / tot); V["s3_pct"] = pct(acum[2] / tot)
V["s1"] = mm(sg[0]); V["s2"] = mm(sg[1]); V["s3"] = mm(sg[2]); V["s4"] = mm(sg[3])
V["pico5"] = mm(C.SGR_MES[4]); V["pico13"] = mm(C.SGR_MES[12]); V["pico18"] = mm(C.SGR_MES[17])
V["res_mes"] = mm(C.B["X01"]["total"] / 24); V["sgr_sin_res"] = mm(sgr - C.B["X01"]["total"])

if __name__ == "__main__":
    for k in sorted(V): print(k, "=", V[k])
    for k in sorted(T): print(); print(T[k])
