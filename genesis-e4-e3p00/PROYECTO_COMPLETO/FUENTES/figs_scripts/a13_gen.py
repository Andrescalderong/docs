# -*- coding: utf-8 -*-
"""Generador de los capítulos 21 (Project Charter) y 20 (Anexos A a J) de la asignación A13.
Toda cifra sale de maestro.py, indicadores.py y alternativas.py (mediante a11_datos.py); las tablas se construyen desde esos objetos.
La prosa vive en plantillas a13_cap21.tpl y a13_cap20.tpl con marcas @@TABLA id@@ y <<valor>>.
Uso: python3 a13_gen.py [21] [20]   (sin argumentos genera ambos)."""
import os, sys, re, datetime, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a11_datos as D
import alternativas as ALT

M, I = D.M, D.I
RAIZ = D.RAIZ
CAPS = os.path.join(RAIZ, "caps")
B, C, RES = D.B, D.C, D.RES
MM = 1_000_000
num, pct, mm, cop, cel = D.num, D.pct, D.mm, D.cop, D.cel

def miles(n):
    return f"{int(round(n)):,}".replace(",", ".")

PAL = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
def pal(n):
    return PAL[n] if n < 10 else str(n)

def limpia(s):
    s = str(s).replace("|desviación|", "desviación absoluta")
    return s[0].upper() + s[1:] if s.startswith("desviación") else s

def tabla(id_, titulo, header, rows, nota):
    out = [f":::TABLA {id_} | {titulo}", "| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    for r in rows:
        assert len(r) == len(header), (id_, r)
        out.append("| " + " | ".join(cel(x) for x in r) + " |")
    out.append(f":::NOTA {nota}")
    return "\n".join(out)

# ------------------------------------------------------------------ valores comunes
ACTS, DUR, RC = M.ACTS, M.DURACION_SEMANAS, M.RUTA_CRITICA
HIT = {h[0]: h for h in M.HITOS}
RK = D.RK
SGR, CON, TOT = RES["sgr"], RES["contra"], RES["total"]
TOPE = M.IDENT["tope_cop"]
adm = B["O05"]["total"]
top5 = D.TOP5
emv_total = sum(r["emv"] for r in M.RISKS)
emv_top5 = sum(r["emv"] for r in top5)
emv_otros = emv_total - emv_top5
ids_otros = [r["id"] for r in sorted(M.RISKS, key=lambda r: r["id"]) if r["id"] not in {x["id"] for x in top5}]
d_corte = datetime.date(2026, 10, 13)
d_limite = datetime.date(2026, 11, 11)
hit_por_tramo = {t["id"]: sum(1 for h in M.HITOS if t["m_ini"] <= h[2] <= t["m_fin"]) for t in M.TRAMOS}
holg = [k for k, a in ACTS.items() if a["holgura"] > 0]
n_especie = D.CONTRA_ESPECIE
n_personas_total = D.N_PERS + D.N_CPERS
SEL = ["P01", "P02", "P10"]                                  # perfiles que se vinculan por selección posterior (capítulo 17)
n_sel = sum(p["n"] for p in D.PERS if p["id"] in SEL)
n_nombradas = n_personas_total - n_sel
perf_nombrados = len(D.PERS) + len(D.CPERS) - len(SEL)
ind_vacio = [i["cod"] for i in I.IND if i["lb_nat"] == "VACIO"]

V = dict(
    semanas=DUR, meses=M.IDENT["duracion_meses"], nodos=M.IDENT["nodos"], nodos_c=M.IDENT["nodos_comprados"],
    gw=M.IDENT["gateways"], gw_c=M.IDENT["gateways_comprados"], refs=pal(M.IDENT["referencias"]),
    nodos_res=M.IDENT["nodos_comprados"] - M.IDENT["nodos"], gw_res=M.IDENT["gateways_comprados"] - M.IDENT["gateways"],
    dias=(d_limite - d_corte).days,
    sgr_cop=miles(SGR), con_cop=miles(CON), tot_cop=miles(TOT), tope_cop=miles(TOPE), holgura_cop=miles(RES["holgura"]),
    pct_tope=num(RES["pct_tope"] * 100, 1), pct_sgr_tot=num(SGR / TOT * 100, 1), pct_con_tot=num(CON / TOT * 100, 1),
    pct_con_sgr=num(CON / SGR * 100, 1), pct_especie=num(n_especie / CON * 100, 1),
    res_cop=miles(RES["reserva"]), res_mm=mm(RES["reserva"]), res_pct=num(RES["reserva"] / SGR * 100, 1),
    vme_sum=mm(emv_total), adm_cop=miles(adm), adm_pct=num(adm / SGR * 100, 1),
    sgr_nodo=mm(SGR / M.IDENT["nodos"]), tot_nodo=mm(TOT / M.IDENT["nodos"]),
    alt03=num(ALT.BASE[3], 3), alt02=num(ALT.BASE[2], 3), alt00=num(ALT.BASE[0], 3), alt01=num(ALT.BASE[1], 3),
    n_rc=len(RC), n_act=len(M.ACT), n_hol=pal(len(holg)), hol_ids=", ".join(holg),
    h_t1=pal(hit_por_tramo[1]), h_t2=pal(hit_por_tramo[2]), h_t3=pal(hit_por_tramo[3]),
    f1=num(RES["flujo_sgr_sem"][0] / MM, 1), f2=num(RES["flujo_sgr_sem"][1] / MM, 1), f3=num(RES["flujo_sgr_sem"][2] / MM, 1), f4=num(RES["flujo_sgr_sem"][3] / MM, 1),
    c1=num(RES["flujo_con_sem"][0] / MM, 1),
    emv_top5=mm(emv_top5), emv_top5_pct=num(emv_top5 / emv_total * 100, 1), emv_otros=mm(emv_otros),
    emv_21=mm(RK["R-FIN-01"]["emv"] + RK["R-TEC-01"]["emv"]), emv_21_pct=num((RK["R-FIN-01"]["emv"] + RK["R-TEC-01"]["emv"]) / emv_total * 100, 1),
    emv_fin=mm(RK["R-FIN-01"]["emv"]), emv_tec=mm(RK["R-TEC-01"]["emv"]),
    n_pers=D.N_PERS, pm=D.PM_TOT, etc=num(D.ETC_PROM, 1),
    n_nombradas=n_nombradas, n_sel=n_sel, n_personas_total=n_personas_total, perf_nombrados=perf_nombrados,
    n_perfiles=len(D.PERS) + len(D.CPERS), n_ind_vacio=pal(len(ind_vacio)),
    mes_c1=M.TRAMOS[0]["mes_compuerta"], mes_c2=M.TRAMOS[1]["mes_compuerta"], mes_c3=M.TRAMOS[2]["mes_compuerta"],
    n_lineas=len(M.BUDGET), n_contra=len(M.CONTRA),
)

V.update(
    pct_pers=num(RES["por_rubro"]["Personal"] / SGR * 100, 1), pct_eq=num(RES["por_rubro"]["Equipos y software"] / SGR * 100, 1),
    etc_ip=num(D.CPERS[0]["etc"], 1),
)

# valores adicionales del capítulo 20
E_LINEAS = [B[k] for k in sorted(B) if k.startswith("E")]
eq_tot = sum(l["total"] for l in E_LINEAS)
top3 = [B["E01"], B["E04"], B["E03"]]
est_cost = B["S06"]["total"] + B["S07"]["total"] + B["S08"]["total"]
hol_por = collections.defaultdict(list)
for k, a in ACTS.items():
    if a["holgura"] > 0: hol_por[a["holgura"]].append(k)
V.update(
    n_cpers=D.N_CPERS, etc_ies=num(D.ETC_CPERS, 1),
    n_decl_e=pal(sum(1 for l in E_LINEAS if l["nat"] == "DECLARADO")), n_prop_e=pal(sum(1 for l in E_LINEAS if l["nat"] == "PROPUESTO")),
    eq_cop=miles(eq_tot), eq_pct=num(eq_tot / SGR * 100, 1),
    top3_cop=miles(sum(l["total"] for l in top3)), top3_pct=num(sum(l["total"] for l in top3) / eq_tot * 100, 1),
    e01=miles(B["E01"]["total"]), e04=miles(B["E04"]["total"]), e03=miles(B["E03"]["total"]),
    est_cop=miles(est_cost), est_pct=num(est_cost / SGR * 100, 1),
    s06=miles(B["S06"]["total"]), s07=miles(B["S07"]["total"]), s08=miles(B["S08"]["total"]),
    h2=", ".join(hol_por[2]), h6=", ".join(hol_por[6]), h12=" y ".join(hol_por[12]),
    c1_ini=ACTS["C1"]["ES"], c1_fin=ACTS["C1"]["EF"], c2_ini=ACTS["C2"]["ES"], c2_fin=ACTS["C2"]["EF"],
    n_resp_esp=int(round(0.8 * 150)),
    n_ret_a11=B["S05"]["cant"],
)

# ================================================================== CAPÍTULO 21
def t21_01():
    I_ = M.IDENT
    rows = [
        ["Título del proyecto", I_["titulo"], "DECLARADO"],
        ["Código del caso de formulación", I_["caso"], "PROPUESTO"],
        ["Código de radicación", "[DATO_USUARIO: código de radicación asignado por la convocatoria]", "VACIO"],
        ["Versión del acta", "1.0, versión de formulación para ratificación", "PROPUESTO"],
        ["Fecha de corte de los datos", I_["fecha_corte"], "DECLARADO"],
        ["Fecha límite de radicación", I_["fecha_limite"], "DECLARADO"],
        ["Fecha de aprobación del acta", "[DATO_USUARIO: fecha de aprobación por el comité directivo]", "VACIO"],
        ["Convocatoria", I_["convocatoria"], "DECLARADO"],
        ["Financiador", I_["financiador"], "DECLARADO"],
        ["Tipología", I_["tipologia"], "DECLARADO"],
        ["Área OCDE", I_["ocde"], "DECLARADO"],
        ["Territorio", I_["territorio"] + "; 12 municipios focalizados, 4 por departamento [DATO_USUARIO: lista de municipios]", "SUPUESTO"],
        ["Duración de ejecución", f"{I_['duracion_meses']} meses ({DUR} semanas); seguimiento posproyecto de {I_['horizonte_posproyecto_meses']} meses", "CALCULADO; seguimiento PROPUESTO"],
        ["Nivel de preparación tecnológica (TRL)", f"Inicial {I_['trl_inicial']}; final {I_['trl_final']}", "PROPUESTO"],
        ["Red de medición", f"{I_['nodos']} nodos y {I_['gateways']} gateways operativos; {I_['nodos_comprados']} nodos y {I_['gateways_comprados']} gateways comprados; {I_['referencias']} monitores de referencia", "PROPUESTO"],
        ["Valor solicitado al SGR", f"{cop(SGR)} ({num(RES['pct_tope'] * 100, 1)} % del tope declarado de {cop(TOPE)})", "CALCULADO; tope DECLARADO y NO_VERIFICADO"],
        ["Contrapartida", cop(CON), "DECLARADO; desglose de la IES PROPUESTO"],
        ["Total del proyecto", cop(TOT), "CALCULADO"],
        ["Entidad ejecutora", "[DATO_USUARIO: nombre de la IES ejecutora con acreditación de alta calidad]", "SUPUESTO"],
        ["Empresa tecnológica aliada", "[DATO_USUARIO: razón social de la empresa]", "SUPUESTO"],
        ["Director del proyecto", "[DATO_USUARIO: nombre del investigador principal]", "VACIO"],
        ["Metaprompt y norma", f"{I_['metaprompt']}; {I_['ntc']}", "DECLARADO"],
        ["Huella SHA-256 del libro maestro", I_["hash_maestro"], "CALCULADO"],
    ]
    return tabla("t01", "Ficha de identificación del proyecto", ["Campo", "Valor", "Naturaleza"], rows,
                 "*Nota.* Elaboración propia con maestro.py (IDENT, resumen) y la ficha maestra, secciones 1 y 5. Territorio y alianza son SUPUESTO por instrucción del usuario. "
                 "Los términos de referencia no se aportaron y el tope normativo no está verificado. SGR: Sistema General de Regalías. IES: institución de educación superior.")

def t21_02():
    g = lambda c: limpia(D.IND[c]["mf"])
    rows = [
        ["1", "Red operativa de nodos y gateways con energía solar y enlace alterno", f"PERS-P01: {g('PERS-P01')}", "WP2", "H6 y H8", "PROPUESTO"],
        ["2", "Modelo de corrección validado y aplicado en los gateways", f"{M.OE[0]['meta']}; PERS-R02: {g('PERS-R02')}", "WP1", "H3, H4 y H7", "PROPUESTO"],
        ["3", "Base de datos de colocalización y línea base de error medida", f"PERS-R05: {g('PERS-R05')}", "WP1", "H2", "PROPUESTO"],
        ["4", "Gemelo digital y software de corrección registrado", f"PERS-P02: {g('PERS-P02')}", "WP2", "Mes 24 (capítulo 9)", "PROPUESTO"],
        ["5", "Tablero del AQHI y protocolo de alerta con umbrales validados localmente", f"PERS-E01: {g('PERS-E01')}; PERS-E02: {g('PERS-E02')}", "WP3", "H3, H5 y mes 24", "PROPUESTO"],
        ["6", "Convenios de custodia y personal custodio certificado", f"PERS-E03: {g('PERS-E03')}; PERS-S02: {g('PERS-S02')}", "WP3", "H5 y H8", "PROPUESTO"],
        ["7", "Actividades de apropiación social documentadas", f"PERS-P04: {g('PERS-P04')}", "WP3", "Seguimiento trimestral; cierre en H8", "PROPUESTO"],
        ["8", "Artículos científicos en revistas Q1 o Q2", f"PERS-P03: {g('PERS-P03')}", "WP1", "Mes 24 (capítulo 9)", "PROPUESTO"],
        ["9", "Evaluación externa independiente y ensayo con laboratorio externo",
         f"{B['S07']['cant']} evaluaciones (meses {B['S07']['m_ini']} y {B['S07']['m_fin']}) y {B['S08']['cant']} campaña de ensayo (meses {B['S08']['m_ini']} a {B['S08']['m_fin']})", "WP0 y WP1", "H7", "PROPUESTO"],
    ]
    V["n_entreg"] = pal(len(rows))
    for w in ("WP0", "WP1", "WP2", "WP3"):
        V["n_" + w.lower()] = pal(sum(1 for r in rows if w in r[3]))
    return tabla("t02", "Lista de entregables principales y su verificación", ["N.º", "Entregable", "Indicador y meta final", "Paquete", "Hito de verificación", "Naturaleza"], rows,
                 "*Nota.* Elaboración propia con indicadores.py (IND), maestro.py (OE, HITOS y líneas S07 y S08) y la ficha maestra, secciones 3, 6 y 8. "
                 "WP0: gestión, compuertas y cierre; WP1: medición verificada; WP2: red, energía y plataforma; WP3: uso institucional, apropiación y custodia. AQHI: índice de calidad del aire y salud.")

def t21_03():
    g = lambda c, k: limpia(D.IND[c][k])
    def meta_int(c):
        a, b = g(c, "m1"), g(c, "m2")
        if a.startswith("No aplica"): return "No aplica: medición posproyecto"
        return a if a == b else f"{a}; {b}"
    def lb(c):
        i = D.IND[c]; return f"{i['lb']} ({i['lb_nat']})"
    rows = [
        ["OE1", "Desempeño de la corrección frente a referencia: R² y NRMSE", "Se mide en el tramo 1 (VACIO)",
         "Compuerta C1: umbrales en el piloto; compuerta C2: umbrales en los tres departamentos", M.OE[0]["meta"], "Compuertas C1, C2 y ensayo final"],
        ["OE1", f"PERS-R05 {g('PERS-R05', 'nombre')}", lb("PERS-R05"), meta_int("PERS-R05"), g("PERS-R05", "mf"), g("PERS-R05", "frecuencia")],
        ["OE1", f"PERS-R02 {g('PERS-R02', 'nombre')}", lb("PERS-R02"), meta_int("PERS-R02"), g("PERS-R02", "mf"), g("PERS-R02", "frecuencia")],
        ["OE2", "Disponibilidad mensual de nodos y pérdida de paquetes", "Se mide en el tramo 1 (VACIO)", "Compuerta C2: disponibilidad mensual de 90 % o más", M.OE[1]["meta"], "Mensual"],
        ["OE2", f"PERS-P01 {g('PERS-P01', 'nombre')}", lb("PERS-P01"), meta_int("PERS-P01"), g("PERS-P01", "mf"), g("PERS-P01", "frecuencia")],
        ["OE2", f"PERS-R03 {g('PERS-R03', 'nombre')}", lb("PERS-R03"), meta_int("PERS-R03"), g("PERS-R03", "mf"), g("PERS-R03", "frecuencia")],
        ["OE3", f"PERS-E01 {g('PERS-E01', 'nombre')}", lb("PERS-E01"), meta_int("PERS-E01"), g("PERS-E01", "mf"), g("PERS-E01", "frecuencia")],
        ["OE3", f"PERS-E02 {g('PERS-E02', 'nombre')}", lb("PERS-E02"), meta_int("PERS-E02"), g("PERS-E02", "mf"), g("PERS-E02", "frecuencia")],
        ["OE3", f"PERS-E03 {g('PERS-E03', 'nombre')}", lb("PERS-E03"), meta_int("PERS-E03"), g("PERS-E03", "mf"), g("PERS-E03", "frecuencia")],
        ["OE3", f"PERS-S01 {g('PERS-S01', 'nombre')}", lb("PERS-S01"), meta_int("PERS-S01"), g("PERS-S01", "mf"), g("PERS-S01", "frecuencia")],
        ["OE3", f"PERS-S02 {g('PERS-S02', 'nombre')}", lb("PERS-S02"), meta_int("PERS-S02"), g("PERS-S02", "mf"), g("PERS-S02", "frecuencia")],
        ["Gestión", f"PERS-R04 {g('PERS-R04', 'nombre')}", lb("PERS-R04"), meta_int("PERS-R04"), g("PERS-R04", "mf"), g("PERS-R04", "frecuencia")],
    ]
    V["n_criterios"] = len(rows)
    return tabla("t03", "Criterios de éxito medibles y metas del proyecto", ["Objetivo", "Indicador", "Línea base", "Meta intermedia", "Meta final", "Frecuencia"], rows,
                 "*Nota.* Elaboración propia con indicadores.py (IND), maestro.py (OE) y la ficha maestra, secciones 2, 3 y 8. Las metas son PROPUESTO. "
                 "Las líneas base VACIO se miden en el tramo 1 (DEC-F10). Los indicadores de impacto (PERS-S) se miden entre 6 y 12 meses después del cierre.")

def t21_04():
    nod, gwc = M.IDENT["nodos"], M.IDENT["gateways"]
    rows = [
        ["Medición", f"PM2,5 y PM10 con {M.IDENT['referencias']} monitores gravimétricos de referencia (uno por departamento) y corrección aplicada en el gateway",
         "Otros contaminantes; sustitución de la medición regulatoria de la Resolución 2254 de 2017", "La línea base de error se mide en el tramo 1"],
        ["Red", f"{nod} nodos y {gwc} gateways operativos en 12 municipios ({M.IDENT['nodos_comprados']} nodos y {M.IDENT['gateways_comprados']} gateways comprados)",
         "Más nodos, un cuarto tramo y un año adicional de custodia: opciones sin presupuestar (DEC-F06)", "Acceso a los sitios en ventanas secas"],
        ["Energía y enlace", "Autonomía mínima de 14 días sin sol, enlace celular con enlace satelital alterno y almacenamiento local de 7 días",
         "Infraestructura eléctrica o de telecomunicaciones de terceros", "Cobertura verificada en el estudio de cobertura (S06)"],
        ["Plataforma", "Gemelo digital, tablero del AQHI y umbrales validados localmente con los comités",
         "Operación de la plataforma después del mes 24, salvo la custodia entregada", "Cláusula de apertura y salida ordenada firmada en H8"],
        ["Uso institucional", "Co-diseño y formación con 15 comités (12 municipales y 3 departamentales) y 150 funcionarios beneficiarios directos",
         "Las decisiones de los comités: el protocolo apoya la decisión y no la sustituye", "Comités y funcionarios son SUPUESTO"],
        ["Salud", "Reporte de mediciones, de uso institucional y de continuidad", "Estimación de exposición individual, de morbilidad o de mortalidad", "Sin grupo de comparación ni contrafactual"],
        ["Custodia y transferencia", "Convenios por tramo, formación de al menos 60 personas y entrega a custodios en el mes 24",
         "Financiación de la operación posterior al cierre, a cargo de los custodios", "Costo de sostenimiento NO_CALCULABLE"],
        ["Gestión y verificación", "Compuertas C1, C2 y C3; evaluación externa (S07); ensayo con laboratorio externo (S08); registro del software",
         "Calificación independiente que sustente el TRL 8", "TRL final 7 (DEC-F05)"],
        ["Apropiación social", "29 actividades documentadas: 20 talleres y 9 jornadas", "Actividades adicionales a las 29 y comunicación fuera de los municipios focalizados", "Participación con consentimiento informado"],
    ]
    V["n_alcance"] = pal(len(rows))
    return tabla("t04", "Matriz de alcance: dentro, fuera y supuestos o restricciones asociadas", ["Componente", "Dentro del alcance", "Fuera del alcance", "Supuesto o restricción"], rows,
                 "*Nota.* Elaboración propia con la ficha maestra, secciones 2 a 6 y 11 (DEC-F05 y DEC-F06). Naturaleza: la frontera de alcance es PROPUESTO. "
                 "TRL: nivel de preparación tecnológica. AQHI: índice de calidad del aire y salud.")

def t21_05():
    rows = []
    for r in top5:
        rows.append([r["id"], r["desc"], f"{r['P']} × {r['I']} = {r['score']}", r["nivel"], str(r["prob"]), num(r["impacto"] / MM, 1), num(r["emv"] / MM, 1),
                     f"{r['estrategia']}: {r['respuesta'][0].lower() + r['respuesta'][1:]}", r["disp"]])
    rows.append(["Otros siete", "Los siete riesgos restantes: " + ", ".join(ids_otros) + ".", "—", "MEDIO a ALTO", "—", "—", num(emv_otros / MM, 1), "Mitigar, evitar o transferir según el capítulo 10", "Según cada riesgo"])
    return tabla("t05", "Riesgos de alto nivel: los cinco de mayor valor monetario esperado", ["Id", "Riesgo", "P × I", "Nivel", "Prob. (%)", "Impacto (M COP)", "VME (M COP)", "Estrategia preliminar", "Disparador"], rows,
                 f"*Nota.* Elaboración propia con maestro.RISKS (CALCULADO). P: probabilidad de 1 a 5; I: impacto de 1 a 5; VME: valor monetario esperado, igual a probabilidad por impacto monetario. M COP: millones de pesos colombianos. "
                 f"Los 12 riesgos suman {mm(emv_total)} millones de COP; la reserva se redondea a {mm(RES['reserva'])} millones. Orden por VME y, en empate, por P × I. Decimales con coma.")

def _nat(rubro):
    ns = sorted({l["nat"] for l in M.BUDGET if l["rubro"] == rubro})
    if len(ns) == 1: return ns[0]
    return " y ".join(ns)

def t21_06():
    rows = []
    for k, v in RES["por_rubro"].items():
        rows.append(["SGR", k, mm(v), num(v / SGR * 100, 1), num(v / TOT * 100, 1), _nat(k)])
    rows.append(["SGR", "Subtotal solicitado al SGR", mm(SGR), "100,0", num(SGR / TOT * 100, 1), "CALCULADO"])
    rows.append(["Contrapartida IES", "Aportes C01 a C04, en especie", mm(D.CONTRA_IES), num(D.CONTRA_IES / CON * 100, 1), num(D.CONTRA_IES / TOT * 100, 1), "DECLARADO y PROPUESTO"])
    rows.append(["Contrapartida empresa", "Aporte C05, en efectivo", mm(D.CONTRA_EMP_EF), num(D.CONTRA_EMP_EF / CON * 100, 1), num(D.CONTRA_EMP_EF / TOT * 100, 1), "DECLARADO"])
    rows.append(["Contrapartida empresa", "Aporte C06, infraestructura en la nube, en especie", mm(D.CONTRA_EMP_ES), num(D.CONTRA_EMP_ES / CON * 100, 1), num(D.CONTRA_EMP_ES / TOT * 100, 1), "DECLARADO"])
    rows.append(["Alcaldías", "Sin aporte declarado", "0,0", "0,0", "0,0", "VACIO"])
    rows.append(["Contrapartida", "Subtotal de contrapartida", mm(CON), "100,0", num(CON / TOT * 100, 1), "DECLARADO y PROPUESTO"])
    rows.append(["Proyecto", "Total del proyecto", mm(TOT), "—", "100,0", "CALCULADO"])
    return tabla("t06", "Resumen presupuestal por fuente y por rubro", ["Fuente", "Rubro o aporte", "Valor (M COP)", "% de la fuente", "% del total", "Naturaleza"], rows,
                 f"*Nota.* Elaboración propia con maestro.resumen(), BUDGET y CONTRA. M COP: millones de pesos colombianos. Valores exactos: SGR {cop(SGR)}; contrapartida {cop(CON)}; total {cop(TOT)}. "
                 "La contrapartida está pendiente de certificación. Los porcentajes se redondean a un decimal. Decimales con coma.")

def t21_07():
    rows = [
        ["Patrocinador", "Aprueba la asignación y fija los términos de la convocatoria", "[DATO_USUARIO: nombre y cargo de quien representa al convocante]", "", "[DATO_USUARIO: fecha de firma]"],
        ["Representante legal de la entidad ejecutora", "Compromete la ejecución legal y la contrapartida de la IES", "[DATO_USUARIO: nombre y cargo]", "", "[DATO_USUARIO: fecha de firma]"],
        ["Representante legal de la empresa tecnológica", "Compromete la contrapartida de la empresa y el acuerdo de titularidad", "[DATO_USUARIO: nombre y cargo]", "", "[DATO_USUARIO: fecha de firma]"],
        ["Director del proyecto", "Certifica el criterio técnico de cada compuerta", "[DATO_USUARIO: nombre del investigador principal]", "", "[DATO_USUARIO: fecha de firma]"],
        ["Gerente del proyecto", "Certifica presupuesto, cronograma y riesgos de cada compuerta", "[DATO_USUARIO: nombre de la persona a cargo de la gerencia]", "", "[DATO_USUARIO: fecha de firma]"],
    ]
    return tabla("t07", "Firmas de autorización del acta de constitución", ["Rol", "Responsabilidad en la autorización", "Nombre y cargo", "Firma", "Fecha"], rows,
                 "*Nota.* Elaboración propia. Ninguna persona firmó el acta: los nombres y las fechas son datos que solo el usuario posee. "
                 "Los roles son PROPUESTO y se ratifican en el comité directivo.")

T21 = dict(t01=t21_01, t02=t21_02, t03=t21_03, t04=t21_04, t05=t21_05, t06=t21_06, t07=t21_07)

# ================================================================== CAPÍTULO 20
PERFIL_COMP = {   # competencia verificable por perfil (capítulo 17, tabla de perfiles; PROPUESTO)
    "C01": "Dirección de proyectos que llevaron un desarrollo de laboratorio a entorno operativo",
    "C02": "Validación de sensores frente a referencia con R², NRMSE, pendiente y sesgo",
    "C03": "Diseño participativo con instituciones y análisis de gestión del riesgo",
    "P01": "Procesamiento de series de sensores y registro de bitácoras de campo",
    "P02": "Tesis sobre el modelo de corrección o la validación con datos del proyecto",
    "P03": "Modelos de corrección con validación cruzada por departamento y partición temporal",
    "P04": "Instalación de redes LoRa con gateways, energía solar y enlace celular o satelital",
    "P05": "Facilitación de talleres de co-diseño y actas con comunidades e instituciones",
    "P06": "Control de alcance, cronograma, presupuesto y compuertas con informes de seguimiento",
    "P07": "Trazabilidad frente a la referencia gravimétrica y manejo del banco de calibración",
    "P08": "Plataformas en la nube, bases de series temporales y tableros con pruebas de seguridad",
    "P09": "Firmware de bajo consumo y dimensionamiento solar para 14 días sin sol",
    "P10": "Instalación, mantenimiento y reposición de nodos en sitios de remoción con trabajo seguro",
    "P11": "Talleres de co-diseño con comités y materiales para comunidades",
    "P12": "Estimación espacial de PM2,5 y PM10 y validación del gemelo digital",
    "P13": "Índice de calidad del aire y salud con umbrales locales y protocolo de alerta",
    "P14": "Convenios por tramo, cláusula de apertura y titularidad de propiedad intelectual",
}

def t20_01():   # Anexo A
    rows = [
        ["A1", "Certificación de la contrapartida de la IES", "Representante legal o instancia financiera de la IES",
         f"Identificación de la IES; valor de {cop(D.CONTRA_IES)} en especie; desglose C01 a C04; periodo de {V['meses']} meses; método de valoración",
         "Contrapartida C01 a C04; riesgo R-FIN-02; hito H0", "[DATO_USUARIO: certificación firmada de la IES]"],
        ["A2", "Carta de compromiso de la empresa tecnológica con certificación de aportes", "Representante legal de la empresa",
         f"Razón social y NIT; {cop(D.CONTRA_EMP_EF)} en efectivo y {cop(D.CONTRA_EMP_ES)} en especie; forma y calendario de entrega",
         "Contrapartida C05 y C06; riesgo R-FIN-02", "[DATO_USUARIO: carta y certificación firmadas por la empresa]"],
        ["A3", "Acuerdo de titularidad de la propiedad intelectual y cláusula de apertura", "IES y empresa tecnológica",
         "Titularidad del modelo de corrección, del firmware y del gemelo digital; destino de los datos y de la infraestructura al cierre; salida ordenada",
         "Líneas O03 y S02; perfil P14; indicador PERS-P02; hito H8", "[DATO_USUARIO: acuerdo firmado por ambas partes]"],
        ["A4", "Cartas de compromiso de las alcaldías de los municipios focalizados (12)", "Alcaldesa o alcalde de cada municipio",
         "Aceptación del tablero y del protocolo; custodia por tramo; partida presupuestal y competencia para operar los nodos",
         "OE3; compuerta C2; riesgo R-ORG-02; indicador PERS-S02", "[DATO_USUARIO: 12 cartas firmadas y lista de municipios]"],
        ["A5", "Cartas de compromiso de las gobernaciones y de las unidades departamentales de gestión del riesgo (3)", "Gobernadora o gobernador de cada departamento",
         "Participación del comité departamental; aceptación del protocolo; custodia potencial y partida",
         "OE3; comités departamentales; indicador PERS-E01", "[DATO_USUARIO: 3 cartas firmadas]"],
        ["A6", "Carta de aceptación del protocolo de alerta", "UNGRD y puestos de mando unificado",
         "Reconocimiento del tablero como fuente informativa; criterios de activación del protocolo; canal de comunicación",
         "OE3; indicador PERS-S01; entregable 5 del capítulo 21", "[DATO_USUARIO: carta firmada de la UNGRD]"],
        ["A7", "Convenio o carta de referencia metrológica", "IDEAM y autoridades ambientales",
         "Acceso a estaciones o a sitios de referencia; condiciones de colocalización; intercambio de datos",
         f"Línea E03 ({B['E03']['cant']} monitores de referencia); indicador PERS-R05", "[DATO_USUARIO: convenio o carta firmada]"],
        ["A8", "Autorizaciones de predios o de la autoridad para instalar nodos y gateways", "Persona propietaria del predio o autoridad competente",
         "Identificación del predio; autorización de instalación y acceso de los técnicos; periodo; condiciones de custodia local",
         f"Línea S05 ({B['S05']['cant']} sitios); criterios de inclusión de sitios", "[DATO_USUARIO: acta de autorización por sitio]"],
    ]
    return tabla("t01", "Lista de verificación del Anexo A: cartas de compromiso y avales", ["Id", "Documento", "Quién lo emite", "Contenido mínimo", "Línea del proyecto que lo exige", "Dato por aportar"], rows,
                 "*Nota.* Elaboración propia con las líneas C01 a C06 y S05 del presupuesto, las compuertas del cronograma y el análisis de actores de 4.4-MDR.5. "
                 "Ningún actor firmó compromiso alguno (alianza SUPUESTO). Los contenidos mínimos son PROPUESTO y dependen de los términos de referencia. UNGRD: Unidad Nacional para la Gestión del Riesgo de Desastres.")

def t20_02():   # Anexo B
    rows = []
    for p in D.CPERS + D.PERS:
        sel = p["id"] in SEL
        rows.append([p["id"], p["concepto"], str(p["n"]), "Por selección posterior a la aprobación" if sel else "Desde la radicación", PERFIL_COMP[p["id"]],
                     "[DATO_USUARIO: nombre y hoja de vida o proceso de selección]" if sel else "[DATO_USUARIO: nombre y hoja de vida]"])
    rows.append(["Total", f"{len(rows)} perfiles", str(n_personas_total), f"{perf_nombrados} perfiles ({n_nombradas} personas) desde la radicación", "—", "—"])
    return tabla("t02", "Lista de verificación del Anexo B: hojas de vida por perfil", ["Id", "Perfil", "Personas", "Vinculación", "Competencia verificable", "Dato por aportar"], rows,
                 "*Nota.* Elaboración propia con las líneas P01 a P14 y C01 a C03 de maestro.py y los perfiles del capítulo 17. Las competencias son PROPUESTO. "
                 f"Las personas del SGR suman {D.N_PERS} y las de la contrapartida de la IES suman {D.N_CPERS}. Los perfiles P01, P02 y P10 se vinculan por selección posterior a la aprobación.")

def t20_03():   # Anexo C
    rows = []
    for k in sorted(l for l in B if l.startswith("E")):
        l = B[k]
        rows.append([k, l["concepto"], l["unidad"], miles(l["cant"]), cop(l["vunit"]), cop(l["total"]), l["nat"], "[DATO_USUARIO: cotización vigente, proveedor y fecha]"])
    tot = sum(B[k]["total"] for k in B if k.startswith("E"))
    assert tot == RES["por_rubro"]["Equipos y software"]
    rows.append(["Total", "Equipos y software", "—", "—", "—", cop(tot), "CALCULADO", "—"])
    return tabla("t03", "Lista de verificación del Anexo C: cotizaciones de equipos y software", ["Línea", "Equipo o software", "Unidad", "Cantidad", "Valor unitario de formulación", "Valor total de formulación", "Naturaleza", "Cotización por aportar"], rows,
                 "*Nota.* Elaboración propia con las líneas E01 a E12 de maestro.BUDGET. Los valores son de formulación y no son cotizaciones. COP: pesos colombianos; miles con punto. "
                 "El número mínimo de cotizaciones por línea es [DATO_USUARIO: requisito de los términos de referencia].")

CAP_GRUPOS = [
    ("Calibración y metrología de partículas", "P07, C02, C04, E03, E07"),
    ("Modelado y ciencia de datos", "P03, P12, E08"),
    ("Sistemas embebidos, energía y comunicaciones", "P04, P09, P10, E01 a E06"),
    ("Calidad del aire y salud ambiental", "P13, C03"),
    ("Gestión del riesgo y apropiación social", "P05, P11, P14, C03"),
]

def t20_04():   # Anexo D
    rows = []
    for i, (cap, lineas) in enumerate(CAP_GRUPOS, 1):
        rows.append([f"D{i}", cap, "Certificado de existencia y de categoría vigente del grupo, con carta de vinculación al proyecto",
                     "Entidad que clasifica los grupos [DATO_USUARIO: entidad emisora] y representante legal de la IES",
                     "Código y nombre del grupo; categoría y fecha de la medición; líneas de investigación; integrantes que participan", f"Líneas {lineas}", "[DATO_USUARIO: nombre, código y certificado del grupo]"])
    rows.append([f"D{len(CAP_GRUPOS) + 1}", "Requisito de categoría mínima", "Constancia del cumplimiento del requisito de los términos de referencia", "Entidad que clasifica los grupos y la IES",
                 "Categoría exigida frente a la categoría vigente", "Admisibilidad de la propuesta", "[DATO_USUARIO: requisito de categoría de los términos de referencia]"])
    return tabla("t04", "Lista de verificación del Anexo D: certificados de grupos de investigación", ["Id", "Capacidad requerida", "Documento", "Quién lo emite", "Contenido mínimo", "Línea del proyecto que lo exige", "Dato por aportar"], rows,
                 "*Nota.* Elaboración propia con las cinco capacidades de investigación del capítulo 17 (PROPUESTO). Los grupos concretos y sus categorías son datos que solo el usuario posee.")

LISTA_COTEJO = [
    ("El nodo coincide con el número de serie y las coordenadas del acta de instalación.", "Acta de instalación y fotografía de la placa", "PERS-R01"),
    ("El cerramiento conserva el sello contra polvo y agua.", "Fotografía del sello y del interior del cerramiento", "R-TEC-01"),
    ("El cabezal óptico está limpio y la toma de aire está libre.", "Fotografía de la toma de aire", "R-TEC-01"),
    ("El panel solar está libre de sombra y de suciedad que reduzca la carga.", "Fotografía del panel y lectura de carga", "R-TEC-02"),
    ("La batería conserva la autonomía mínima de 14 días sin sol en el registro de energía.", "Registro de energía de la plataforma", "OE2; R-TEC-02"),
    ("El nodo transmite por LoRa al gateway asignado y registra paquetes en las últimas 24 horas.", "Registro de paquetes de la plataforma", "PERS-P01"),
    ("El mástil está firme y el nodo está a la altura de toma definida en el diseño del sitio.", "Informe de sitio y fotografía", "Criterios de inclusión de sitios"),
    ("El gateway mantiene el enlace celular activo y el enlace satelital alterno en prueba.", "Prueba de enlace registrada", "R-TEC-03"),
    ("El gateway conserva el almacenamiento local de 7 días y la versión vigente del modelo, con su huella digital.", "Registro de versión del modelo", "PERS-R02; OE1"),
    ("El sitio está protegido contra manipulación y una persona custodia conoce el procedimiento de aviso.", "Acta de custodia local", "R-EXT-02; OE3"),
]

def t20_05():   # Anexo E.1
    rows = [[str(i), t, "Sí, no o no aplica", ev, rel] for i, (t, ev, rel) in enumerate(LISTA_COTEJO, 1)]
    V["n_cotejo"] = len(rows)
    return tabla("t05", "Lista de cotejo de instalación y mantenimiento de nodos y gateways", ["N.º", "Ítem de verificación", "Respuesta", "Evidencia que se adjunta", "Indicador o riesgo asociado"], rows,
                 "*Nota.* Elaboración propia con la sección 6.3 y la matriz de técnicas del capítulo 6, el riesgo de la ficha maestra (sección 7) y los indicadores PERS. Naturaleza: PROPUESTO. "
                 "Los ítems 2 y 3 reproducen los ejemplos del capítulo 6. La periodicidad es mensual. LoRa: radio de largo alcance.")

ENCUESTA = [
    ("Utilidad percibida", "El tablero me ayuda a decidir cuándo emitir una alerta.", "Davis (1989)"),
    ("Utilidad percibida", "Las lecturas del tablero mejoran las decisiones de mi comité.", "Davis (1989)"),
    ("Facilidad de uso", "Leer el tablero me resulta sencillo.", "Davis (1989)"),
    ("Facilidad de uso", "Comprendo el error residual que el tablero muestra junto con cada valor.", "Davis (1989)"),
    ("Influencia social", "Las personas cuya opinión valoro en mi comité usan el tablero.", "Venkatesh et al. (2003)"),
    ("Influencia social", "La presidencia de mi comité espera que se consulte el tablero antes de decidir.", "Venkatesh et al. (2003)"),
    ("Condiciones facilitadoras", "Mi comité dispone de tiempo y equipos para consultar el tablero en sus sesiones.", "Venkatesh et al. (2003)"),
    ("Condiciones facilitadoras", "Recibí formación suficiente para usar el tablero y el protocolo de alerta.", "Venkatesh et al. (2003)"),
    ("Uso en decisiones", "Mi comité cita las lecturas del tablero en las actas de sus decisiones.", "PERS-E01"),
    ("Continuidad bajo custodia", "Mi entidad puede asumir el mantenimiento de los nodos de su territorio después del cierre.", "PERS-S02"),
]

def t20_06():   # Anexo E.2
    rows = [[str(i), c, t, "1 a 5", f] for i, (c, t, f) in enumerate(ENCUESTA, 1)]
    V["n_encuesta"] = len(rows)
    return tabla("t06", "Encuesta de uso institucional del tablero y del protocolo de alerta", ["N.º", "Constructo", "Ítem", "Escala", "Fundamento"], rows,
                 "*Nota.* Elaboración propia con la sección 6.3 del capítulo 6. Escala de 1 (totalmente en desacuerdo) a 5 (totalmente de acuerdo). Los ítems 1, 3 y 7 reproducen los ejemplos del capítulo 6. "
                 "Naturaleza: PROPUESTO. La unidad de decisión es el comité y la unidad de encuesta es la persona.")

def t20_08():   # Anexo F: datos tratados
    rows = [
        ["Nombre, cargo y comité", "Identificar a la persona participante y atribuir sus respuestas al comité", "Seudónimo por comité y por persona; llave guardada aparte", "Ejecución y 12 meses de seguimiento"],
        ["Datos de contacto", "Convocar a talleres, entrevistas y jornadas", "Control de acceso por rol", "Ejecución y 12 meses de seguimiento"],
        ["Respuestas de cuestionarios", "Medir el uso institucional y la aceptación del tablero", "Cifrado en almacenamiento y en tránsito; resultados agregados por comité", "Ejecución y 12 meses de seguimiento"],
        ["Grabaciones de audio", "Transcribir entrevistas y sesiones de co-diseño", "Autorización expresa; eliminación del audio tras la transcripción [DATO_USUARIO: plazo de eliminación]", "Según la autorización"],
        ["Registros fotográficos", "Documentar talleres, jornadas e instalaciones", "Autorización expresa; sin publicación de rostros sin permiso", "Ejecución y 12 meses de seguimiento"],
    ]
    return tabla("t08", "Datos personales del proyecto, finalidad y medidas de protección", ["Dato", "Finalidad", "Medida de protección", "Conservación"], rows,
                 "*Nota.* Elaboración propia con la sección 6.5.3 del capítulo 6 y la Ley 1581 de 2012. Las medidas y los plazos son PROPUESTO. El proyecto no recoge documentos de identidad, muestras biológicas ni datos de salud.")

def t20_07():   # Anexo F: firma
    rows = [
        ["Persona participante", "", "", "", "", ""],
        ["Representante del responsable del tratamiento", "[DATO_USUARIO: nombre y cargo]", "No aplica", "No aplica", "", ""],
    ]
    return tabla("t07", "Bloque de firma del consentimiento informado", ["Quién firma", "Nombre completo, cargo y comité", "Autoriza audio (sí o no)", "Autoriza fotografía (sí o no)", "Firma", "Fecha"], rows,
                 "*Nota.* Elaboración propia. Los espacios en blanco los diligencia cada persona participante. El código de seudónimo lo asigna el proyecto después de la firma.")

def t20_09():   # Anexo G
    header = ["Id", "Rubro", "Concepto", "Unidad", "Cantidad", "Costo unitario", "Total SGR", "Fuente", "Naturaleza", "WP", "Mes inicial", "Mes final"]
    rows = []
    for l in M.BUDGET:
        rows.append([l["id"], l["rubro"], l["concepto"], l["unidad"], miles(l["cant"]), cop(l["vunit"]), cop(l["total"]), l["fuente"], l["nat"], l["wbs"], str(l["m_ini"]), str(l["m_fin"])])
    assert sum(l["total"] for l in M.BUDGET) == SGR
    rows.append(["Total", "SGR", "Valor solicitado al SGR", "—", "—", "—", cop(SGR), "SGR", "CALCULADO", "—", "—", "—"])
    return tabla("t09", "Presupuesto detallado del valor solicitado al SGR", header, rows,
                 f"*Nota.* Elaboración propia con maestro.BUDGET ({len(M.BUDGET)} líneas). Valores en pesos colombianos (COP), miles con punto. WP: paquete de trabajo. "
                 "Mes inicial y mes final: meses de ejecución de la línea. Las cotizaciones por proveedor son [DATO_USUARIO: cotizaciones vigentes de equipos, servicios y software].")

def t20_10():   # Anexo G: rubro x WP
    wps = ["WP0", "WP1", "WP2", "WP3"]
    rows = []
    for rub in RES["por_rubro"]:
        vals = [sum(l["total"] for l in M.BUDGET if l["rubro"] == rub and l["wbs"] == w) for w in wps]
        assert sum(vals) == RES["por_rubro"][rub]
        rows.append([rub] + [cop(v) if v else "—" for v in vals] + [cop(sum(vals))])
    tw = [sum(l["total"] for l in M.BUDGET if l["wbs"] == w) for w in wps]
    rows.append(["Total SGR"] + [cop(v) for v in tw] + [cop(sum(tw))])
    V["wp0"], V["wp1"], V["wp2"], V["wp3"] = [num(v / SGR * 100, 1) for v in tw]
    return tabla("t10", "Valor solicitado al SGR por rubro y por paquete de trabajo", ["Rubro", "WP0", "WP1", "WP2", "WP3", "Total"], rows,
                 "*Nota.* Elaboración propia con maestro.BUDGET. Valores en pesos colombianos (COP). WP0: gestión, compuertas y cierre; WP1: medición verificada; WP2: red, energía y plataforma; WP3: uso institucional, apropiación y custodia. Naturaleza: CALCULADO.")

def t20_11():   # Anexo G: contrapartida
    rows = []
    for l in M.CONTRA:
        forma = "Efectivo" if l["rubro"] == "Efectivo" else "Especie"
        rows.append([l["id"], l["concepto"], l["fuente"], forma, cop(l["total"]), l["nat"], "[DATO_USUARIO: certificación]"])
    rows.append(["Total", "Contrapartida", "IES y empresa", "—", cop(CON), "DECLARADO y PROPUESTO", "—"])
    return tabla("t11", "Contrapartida detallada", ["Id", "Aporte", "Fuente", "Forma", "Total", "Naturaleza", "Certificación pendiente"], rows,
                 "*Nota.* Elaboración propia con maestro.CONTRA. IES: institución de educación superior; EMP: empresa tecnológica. Las alcaldías no declaran aporte (VACIO). Valores en pesos colombianos (COP).")

def t20_12():   # Anexo H
    rows = []
    for k, a in ACTS.items():
        rows.append([k, a["nombre"], a["wp"], str(a["dur"]), ", ".join(a["pred"]) if a["pred"] else "—", str(a["ES"]), str(a["EF"]), str(a["holgura"]), "Sí" if a["holgura"] == 0 else "No"])
    return tabla("t12", "Cronograma detallado: actividades, duración, predecesoras, holgura y ruta crítica", ["Id", "Actividad", "WP", "Duración (sem.)", "Predecesoras", "Inicio (sem.)", "Fin (sem.)", "Holgura (sem.)", "Crítica"], rows,
                 f"*Nota.* Elaboración propia con maestro.cpm() (CALCULADO). Semanas contadas desde la semana 0 del acta de inicio; vínculos de fin a inicio. Duración total: {DUR} semanas. "
                 "Inicio y fin son tempranos. Predecesoras: actividades que deben terminar antes.")

def t20_13():   # Anexo I: estudios disponibles
    rows = [
        ["I1", "Informe de vigilancia tecnológica y bibliometría (F-INF)", "Corpus de 42 documentos: 26 artículos, 15 patentes y un informe institucional, consolidado el 30 de septiembre de 2026",
         "F-INF §3.1 (p. 19)", "Estado del campo, brechas y madurez: 267 brechas, 72 críticas (F-INF §5.1, p. 43)", "DECLARADO; NO_VERIFICADO"],
        ["I2", "Vigilancia de propiedad industrial del informe", "Diez solicitudes designan a Colombia; ninguna de las 15 patentes tiene solicitante colombiano; ecuaciones de búsqueda propuestas y no ejecutadas",
         "F-INF §6.2 (p. 61), Anexo C (p. 221) y Anexo D (p. 222)", "Libertad de operación y riesgo R-JUR-01", "DECLARADO; NO_VERIFICADO"],
        ["I3", "Sección F4.3: clasificación de variables para inferencia causal", "Declara dos estimandos antes de clasificar las variables y deriva los roles del grafo",
         "Paso 4, sección F4.3", "Límite de las afirmaciones causales: ningún efecto estimado", "INFERIDO; propuesta sin ratificación"],
        ["I4", "Sección F4.4: Vester y MICMAC", "15 variables, 105 fichas bidireccionales (Anexo K) y escenario de trabajo S2 con 48 aristas y ΣI = ΣD = 78",
         "Paso 4, sección F4.4; Anexo K", "Problema central V06 y causas priorizadas V02, V03, V05, V07 y V15", "INFERIDO; hipótesis de influencia estructural"],
        ["I5", "Sección F4.4-MDR: metodología integrada de decisión y resolución", "Estrategia R4 por tramos, cuatro supuestos críticos SC-1 a SC-4, sostenibilidad, premortem y escenarios",
         "Paso 4, sección F4.4-MDR; Anexo L (árboles A-DEC y A-TDC)", "Compuertas C1 y C2 y custodia distribuida", "INFERIDO; costo de sostenimiento NO_CALCULABLE"],
        ["I6", "Sección F4.5: árbol de problemas completo", "Árbol con nodos de las 15 variables y relaciones con estatuto de hipótesis de influencia estructural",
         "Paso 4, sección F4.5; Anexo L (árbol A-PROB)", "Problema central y efectos para los capítulos 1 y 13", "INFERIDO; sin efecto estimado"],
    ]
    return tabla("t13", "Estudios previos que existen y su aporte al proyecto", ["Id", "Estudio", "Alcance", "Fuente y localizador", "Aporte al proyecto", "Naturaleza y verificación"], rows,
                 "*Nota.* Elaboración propia con F-INF (informe de vigilancia tecnológica y bibliometría) y las secciones F4.3 a F4.5 del Paso 4. El informe se tomó como fue aportado y sus cifras no se verificaron de forma independiente.")

def t20_14():   # Anexo I: estudios que se producen
    rows = [
        ["Línea base de error de medición por departamento", "Se mide con la colocalización del tramo 1", "Actividad A1.3 y hito H2 (mes 10)", "Compuerta C1 (mes 12)", "Sin línea propia en el presupuesto"],
        ["Estudio de cobertura y de enlace en tres departamentos", "No existe estudio de cobertura en los sitios", f"Línea S06, meses {B['S06']['m_ini']} a {B['S06']['m_fin']}; hito H1", "Compra del tramo 1 (mes 5)", cop(B["S06"]["total"])],
        ["Línea base de uso institucional (PERS-E01)", "No existe medición previa en los comités", "Inicio de la actividad A3.1, semana 12", "Compuerta C1 (mes 12)", "Sin línea propia en el presupuesto"],
        ["Evaluación externa independiente", "Se exige verificación ajena al equipo ejecutor", f"Línea S07, meses {B['S07']['m_ini']} y {B['S07']['m_fin']}", "Hitos H3 y H7", cop(B["S07"]["total"])],
        ["Ensayo de desempeño con laboratorio externo", "Se exige verificación independiente de los umbrales", f"Línea S08, meses {B['S08']['m_ini']} a {B['S08']['m_fin']}; hito H7", "Cierre del tramo 3 (mes 24)", cop(B["S08"]["total"])],
        ["Cotizaciones formales de equipos", "No existen; los costos son de formulación", "Anexo C", "Radicación (11 de noviembre de 2026)", "Sin línea propia en el presupuesto"],
    ]
    return tabla("t14", "Estudios que no existen y que el proyecto produce durante la ejecución", ["Estudio", "Por qué falta", "Dónde se produce", "Decisión que alimenta", "Costo (COP)"], rows,
                 "*Nota.* Elaboración propia con maestro.py (BUDGET, ACT y HITOS), la ficha maestra (secciones 6 y 8) y el capítulo 6. Costos en pesos colombianos; miles con punto. Naturaleza: PROPUESTO.")

def t20_15():   # Anexo J
    rows = [
        ["J1", "Términos de referencia de la convocatoria y sus anexos", "Convocante", "Requisitos habilitantes, formatos y calendario de informes", "Estructura de 21 capítulos y requisitos (DEC-F01)", "[DATO_USUARIO: términos de referencia completos]"],
        ["J2", "Aval del comité de ética de la entidad ejecutora", "Comité de ética de la IES", "Clasificación del riesgo de la investigación; fecha del aval; protocolo revisado", "Sección 6.5.1; antes de la actividad A3.1 (semana 12)", "[DATO_USUARIO: nombre del comité y fecha del aval]"],
        ["J3", "Autorización de tratamiento de datos personales y política de la entidad", "Entidad responsable del tratamiento", "Responsable, finalidad, derechos, vigencia y canal de reclamos", "Anexo F; sección 6.5.3; Ley 1581 de 2012", "[DATO_USUARIO: política de tratamiento y razón social]"],
        ["J4", f"Pólizas y garantías del SGR y póliza de equipos", "Aseguradora", "Amparos, vigencia, valor asegurado y beneficiarios", f"Líneas O04 ({cop(B['O04']['total'])}) y S04 ({cop(B['S04']['total'])})", "[DATO_USUARIO: pólizas o cotizaciones de las aseguradoras]"],
        ["J5", "Cotizaciones y alcance de acreditación de laboratorios", "Laboratorio acreditado y laboratorio externo", "Alcance de acreditación para PM2,5 y PM10; precio por muestra y por campaña", f"Líneas S01 ({B['S01']['cant']} muestras) y S08", "[DATO_USUARIO: cotizaciones y certificados de acreditación]"],
        ["J6", "Certificados de existencia y representación legal y requisitos habilitantes", "Cámara de comercio e IES", "Vigencia, objeto social y facultades del representante", "Contrapartida y convenios; Anexo A", "[DATO_USUARIO: certificados vigentes]"],
        ["J7", "Acta de constitución del proyecto firmada", "Patrocinador, entidades y gerencia", "Firmas de la sección 21.10 y fecha de autorización", "Capítulo 21", "[DATO_USUARIO: acta firmada]"],
        ["J8", "Formularios y certificaciones adicionales de la convocatoria", "Convocante y entidades", "Los que fijen los términos de referencia", "Sin evidencia: VACIO", "[DATO_USUARIO: lista de formularios exigidos]"],
    ]
    return tabla("t15", "Lista de verificación del Anexo J: otros documentos según la convocatoria", ["Id", "Documento", "Quién lo emite", "Contenido mínimo", "Línea del proyecto que lo exige", "Dato por aportar"], rows,
                 "*Nota.* Elaboración propia con los capítulos 6, 8 y 15 y la ficha maestra (DEC-F01). Los términos de referencia no se aportaron, por lo cual la lista es PROPUESTO y no sustituye los requisitos de la convocatoria. Los documentos del Anexo J son datos que solo el usuario posee.")

T20 = dict(t01=t20_01, t02=t20_02, t03=t20_03, t04=t20_04, t05=t20_05, t06=t20_06, t07=t20_07, t08=t20_08, t09=t20_09, t10=t20_10,
           t11=t20_11, t12=t20_12, t13=t20_13, t14=t20_14, t15=t20_15)

# ================================================================== ensamblaje
def generar(cap):
    tpl = open(os.path.join(HERE, f"a13_cap{cap}.tpl"), encoding="utf-8").read()
    tablas = {k: f() for k, f in (T21 if cap == "21" else T20).items()}   # evalúa y llena V
    usados = set()
    def rt(m):
        usados.add(m.group(1)); return tablas[m.group(1)]
    out = re.sub(r"@@TABLA (\S+)@@", rt, tpl)
    def rv(m):
        k = m.group(1)
        if k not in V: raise KeyError(f"valor sin definir: {k}")
        return str(V[k])
    out = re.sub(r"<<([A-Za-z0-9_]+)>>", rv, out)
    sin = set(tablas) - usados
    if sin: print(f"AVISO cap{cap}: tablas sin usar {sorted(sin)}")
    ruta = os.path.join(CAPS, f"cap{cap}.md")
    open(ruta, "w", encoding="utf-8").write(out)
    print("escrito", ruta)

if __name__ == "__main__":
    args = sys.argv[1:] or ["21", "20"]
    for c in args: generar(c)
