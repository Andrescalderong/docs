# -*- coding: utf-8 -*-
"""Capa de datos del capítulo 12 (indicadores PERS). Toda cifra sale de maestro.py e indicadores.py (ficha maestra).
Contiene: verificaciones cardinales (aserciones), trazabilidad indicador -> producto, ACT, hito y rubro (PROPUESTO),
campos de ficha que no existen en IND (texto de formulación, PROPUESTO) y valores calculados que usan el texto y las tablas."""
import sys, os, math, collections
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "maestro"))
sys.path.insert(0, os.path.join(RAIZ, "figs"))
import maestro as M
import indicadores as I

IND = {i["cod"]: i for i in I.IND}
ORDEN = [i["cod"] for i in I.IND]
B = {l["id"]: l for l in M.BUDGET}
RES = M.resumen()
HIT = {h[0]: dict(desc=h[1], mes=h[2], verif=h[3]) for h in M.HITOS}
MM = 1_000_000

# ------------------------------------------------------------------ formatos colombianos
def num(x, d=1):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def mm(v, d=1):
    """Millones de COP con coma decimal."""
    return M.mm(v, d)

def cop(v):
    return M.cop(v)

def pct(x, d=1):
    return f"{x * 100:.{d}f}".replace(".", ",")

# ------------------------------------------------------------------ verificaciones cardinales (coherencia con la ficha maestra)
ID = M.IDENT
assert ID["nodos"] == 100 and ID["gateways"] == 10 and ID["referencias"] == 3
assert ID["nodos_comprados"] == 120 and ID["gateways_comprados"] == 11
assert sum(t["nodos"] for t in M.TRAMOS) == 100 and sum(t["gateways"] for t in M.TRAMOS) == 10
assert I.UMBRALES["R2_min"] == 0.70 and I.UMBRALES["NRMSE_max"] == 0.30
assert I.UMBRALES["pendiente"] == (0.65, 1.35) and I.UMBRALES["sesgo_ug"] == (-5.0, 5.0)
assert "60.000" in IND["PERS-R05"]["mf"] and "60.000" in IND["PERS-R05"]["m1"]
assert "100 nodos y 10 gateways" in IND["PERS-R01"]["mf"] and "100 / 10" in IND["PERS-P01"]["mf"]
assert B["E03"]["cant"] == ID["referencias"]            # tres monitores gravimétricos de referencia
assert B["E01"]["cant"] == ID["nodos_comprados"] and B["E04"]["cant"] == ID["gateways_comprados"]
assert B["E06"]["cant"] == ID["gateways"]               # un módulo satelital por gateway operativo
assert B["S05"]["cant"] == ID["nodos"] + ID["gateways"]
assert (B["M05"]["cant"], B["V05"]["cant"], B["O02"]["cant"]) == (20, 20, 9)
assert "20 talleres y 9 jornadas" in IND["PERS-P04"]["mf"]
assert M.DURACION_SEMANAS == 104 and ID["duracion_meses"] == 24 and ID["horizonte_posproyecto_meses"] == 12
assert [t["compra_nodos"] for t in M.TRAMOS] == [36, 48, 36] and [t["compra_gw"] for t in M.TRAMOS] == [4, 4, 3]
assert len(IND) == 15
NIV = collections.Counter(i["nivel"] for i in I.IND)
assert (NIV["R"], NIV["P"], NIV["E"], NIV["S"]) == (6, 4, 3, 2)
TAX = {i["cod"]: i["tax"] for i in I.IND}
assert all(TAX[c] == "Output" for c in ORDEN if IND[c]["nivel"] in "RP")
assert all(TAX[c] == "Outcome" for c in ORDEN if IND[c]["nivel"] == "E")
assert all(TAX[c] == "Impact" for c in ORDEN if IND[c]["nivel"] == "S")

# ------------------------------------------------------------------ valores calculados para texto, tablas y figuras
SGR = RES["sgr"]; CONTRA = RES["contra"]; TOTAL = RES["total"]
HORAS_SEM = 168
SEM_A13 = M.ACTS["A1.3"]["dur"]                       # 16 semanas de colocalización y calibración en el piloto
NODOS_T1 = M.TRAMOS[0]["nodos"]                       # 30
R05_POSIBLES = SEM_A13 * HORAS_SEM * NODOS_T1         # 80.640
R05_META = 60_000
R05_FRAC = R05_META / R05_POSIBLES                    # 0,744
R05_MARGEN75 = 0.75 * R05_POSIBLES - R05_META         # 480
HORAS_MES = 720
R03_CAIDA_H = 0.01 * HORAS_MES                        # 7,2 horas
R04_TOL = 0.05 * SGR                                  # 463,363 M COP
FLUJO = RES["flujo_sgr_sem"]
R04_ACUM_S2 = sum(FLUJO[:2])
COMITES = 15
E01_N = {p: math.ceil(COMITES * p / 100 - 1e-9) for p in (50, 65, 75)}
E03_COSTO_PERS = B["S09"]["total"] / 60
S02_70 = math.ceil(0.70 * ID["nodos"] - 1e-9)
DEPTO = [("Caldas", 33), ("Cundinamarca", 34), ("Valle del Cauca", 33)]
assert sum(n for _, n in DEPTO) == 100
S02_DEPTO = {d: math.ceil(0.70 * n - 1e-9) for d, n in DEPTO}
RIESGO = collections.Counter(IND[c]["riesgo"] for c in ORDEN)
assert (RIESGO["Alto"], RIESGO["Medio"], RIESGO["Bajo"]) == (5, 7, 3)
RIESGO_ALTO = [c for c in ORDEN if IND[c]["riesgo"] == "Alto"]
assert all(IND[c]["nivel"] in "ES" for c in RIESGO_ALTO)
LB_VACIO = [c for c in ORDEN if IND[c]["lb_nat"] == "VACIO"]
assert LB_VACIO == ["PERS-R03", "PERS-E01", "PERS-E02", "PERS-S01", "PERS-S02"]
OE_N = collections.Counter(IND[c]["oe"] for c in ORDEN)

# ------------------------------------------------------------------ trazabilidad (PROPUESTO): producto, ACT, hitos y líneas BUDGET por indicador
COMPONENTES = {
    "C1": "Componente C1: modelo de corrección validado",
    "C2": "Componente C2: red operativa con energía y enlace redundantes",
    "C3": "Componente C3: tablero, protocolo y convenios de custodia",
}
TRAZA = {
    "PERS-R01": dict(prod=["C2"], act=["A1.2", "A2.3", "A2.4"], hitos=["H4", "H6"], rub=["E01", "E04", "S05"]),
    "PERS-R02": dict(prod=["C1"], act=["A1.4", "A1.5", "A1.6"], hitos=["H3", "H4", "H7"], rub=["P03", "P07", "E07", "E08", "M02"]),
    "PERS-R03": dict(prod=["C2", "C3"], act=["A2.1", "A2.2"], hitos=["H2"], rub=["P08", "E10", "E11"]),
    "PERS-R04": dict(prod=["C1", "C2", "C3"], act=["A0.1", "C1", "C2", "A3.4"], hitos=["H0", "H3", "H5", "H8"], rub=["P06", "O05"]),
    "PERS-R05": dict(prod=["C1"], act=["A1.1", "A1.2", "A1.3"], hitos=["H2"], rub=["P07", "E03", "M01", "S01"]),
    "PERS-R06": dict(prod=["C1", "C2", "C3"], act=["A0.1", "A3.4"], hitos=["H0", "H8"], rub=["P06"]),
    "PERS-P01": dict(prod=["C2"], act=["A1.2", "A2.3", "A2.4"], hitos=["H4", "H6"], rub=["E01", "E04", "E05", "E06", "M03", "S05"]),
    "PERS-P02": dict(prod=["C1"], act=["A2.2", "A1.4"], hitos=["H3"], rub=["O03", "S02"]),
    "PERS-P03": dict(prod=["C1"], act=["A1.4", "A1.6"], hitos=["H3", "H7"], rub=["O01"]),
    "PERS-P04": dict(prod=["C3"], act=["A3.1", "A3.2"], hitos=["H3", "H5"], rub=["M05", "V05", "O02"]),
    "PERS-E01": dict(prod=["C3"], act=["A3.1", "A3.2"], hitos=["H3", "H5", "H8"], rub=["P05", "P11", "P13"]),
    "PERS-E02": dict(prod=["C1", "C3"], act=["A1.3", "A3.1", "A3.2"], hitos=["H2", "H3", "H5"], rub=["P12", "P13", "E03"]),
    "PERS-E03": dict(prod=["C3"], act=["A3.3"], hitos=["H5", "H8"], rub=["S09", "P14"]),
    "PERS-S01": dict(prod=["C3"], act=["A3.3", "A3.4"], hitos=["H8"], rub=["S07"]),
    "PERS-S02": dict(prod=["C2", "C3"], act=["A3.3", "A3.4"], hitos=["H8"], rub=["S09", "P14", "S07"]),
}
assert set(TRAZA) == set(IND)
for c, t in TRAZA.items():
    assert all(a in M.ACTS for a in t["act"]) and all(h in HIT for h in t["hitos"]) and all(r in B for r in t["rub"])

def monto(ids):
    return sum(B[i]["total"] for i in ids)

def lista_y(items):
    items = list(items)
    if len(items) <= 1: return "".join(items)
    return ", ".join(items[:-1]) + " y " + items[-1]

def act_texto(c):
    out = []
    for a in TRAZA[c]["act"]:
        x = M.ACTS[a]
        out.append(f"{a} (semanas {x['ES']} a {x['EF']})")
    return lista_y(out)

def hitos_texto(c):
    return lista_y([f"{h} (mes {HIT[h]['mes']})" for h in TRAZA[c]["hitos"]])

def rubros_texto(c):
    ids = TRAZA[c]["rub"]
    return f"{lista_y(ids)}: {mm(monto(ids))} millones de COP (CALCULADO)"

def plazo_lineas(ids):
    return min(B[i]["m_ini"] for i in ids), max(B[i]["m_fin"] for i in ids)

# ------------------------------------------------------------------ nombres de nivel
NIVEL_PERS = {"R": "Proceso (R)", "P": "Producto (P)", "E": "Efecto (E)", "S": "Sostenibilidad (S)"}
MARCO = {"R": "Actividades", "P": "Componentes", "E": "Propósito", "S": "Fin"}
OE_NOMBRE = {
    "OE1": "OE1: corregir la interferencia de humedad y de fracción gruesa en PM2,5 y PM10",
    "OE2": "OE2: mantener la disponibilidad de 100 nodos y 10 gateways",
    "OE3": "OE3: lograr el uso del tablero y del protocolo de alerta por los comités",
}
for o in M.OE:
    assert o["texto"].lower().startswith(OE_NOMBRE[o["id"]].split(": ")[1][:30].lower())

CRITERIO = {
    "R": "Calidad técnica (20–25 %); Viabilidad presupuestal (10–15 %)",
    "P": "Fortalecimiento CTeI regional (25–27 %); Viabilidad presupuestal (10–15 %)",
    "E": "Impacto esperado (15–20 %)",
    "S": "Pertinencia y articulación territorial (20–25 %); Impacto esperado (15–20 %)",
}

# ------------------------------------------------------------------ campos de ficha ausentes en IND (PROPUESTO; sin cifras nuevas)
FECHA = "2026-10-13"
AUTOR = "[DATO_USUARIO: nombre del equipo formulador de la entidad ejecutora]"
REP_R = "Mensual a la gerencia del proyecto; al financiador según los TdR [DATO_USUARIO: calendario de informes]"
REP_T = "Trimestral a la gerencia del proyecto; al financiador según los TdR [DATO_USUARIO: calendario de informes]"

EXTRA = {
 "PERS-R01": dict(
   desc="Mide la proporción de nodos instalados y operativos frente a los programados en cada tramo. El total es de 100 nodos y 10 gateways.",
   just="Controla el avance físico de la red, que condiciona los demás indicadores. Una instalación retrasada desplaza las compuertas C1 y C2.",
   vars="Numerador: nodos instalados y operativos. Denominador: nodos programados del tramo (30, 40 y 30). Factor: 100. Los gateways se cuentan igual (3, 4 y 3).",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero por definición al inicio de la ejecución (CALCULADO).",
   jm="La meta repite la programación por tramos. El tramo 1 compra 36 nodos y 4 gateways, el tramo 2 compra 48 y 4, y el tramo 3 compra 36 y 3, con 20 nodos y 1 gateway de reserva.",
   rep=REP_R, rrep="Gerencia de proyecto",
   fsec="Registro fotográfico y bitácoras de los técnicos departamentales", ins="Acta de instalación con coordenadas y número de serie", ubi="Plataforma en la nube del proyecto (línea E10) con copia de las actas",
   dterr="Tramo, departamento (Caldas 33, Cundinamarca 34 y Valle del Cauca 33 nodos; PROPUESTO) y municipio", dtemp="Mensual y acumulado por tramo", dpob="No aplica (indicador de infraestructura)", dotr="Tipo de equipo (nodo o gateway) y estado (instalado u operativo)",
   lmet="Un nodo instalado puede no estar operativo. El indicador exige operación verificada en la plataforma.", lcob="No mide la calidad del dato, que corresponde a PERS-R05 y a las compuertas.", lmit="Cruce mensual entre inventario, actas y última transmisión recibida.",
   cext="Acceso vial a los sitios en ventanas secas (R-EXT-01)", cins="Contratación completa en el mes 2 (H0) y compuertas aprobadas a tiempo",
   fmt="Acta firmada, registro fotográfico y extracto del inventario", rver="Gerencia de proyecto, con revisión de la evaluación externa (S07)", pver="Mensual"),
 "PERS-R02": dict(
   desc="Cuenta los ciclos completos de entrenamiento, validación y despliegue del modelo de corrección que se aplica en los gateways.",
   just="El modelo de corrección explica la reducción del error (SC-1). Sin ciclos completos no hay evidencia para decidir las compuertas.",
   vars="Numerador: ciclos completos registrados. Denominador: no aplica (conteo). Factor: 6 ciclos, 2 por tramo.",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero por definición al inicio de la ejecución (CALCULADO).",
   jm="La meta fija dos ciclos por tramo, y tres tramos suman seis. La composición de cada ciclo se define en el protocolo de calibración (PROPUESTO).",
   rep=REP_R, rrep="Gerencia de proyecto",
   fsec="Informes de validación con R², NRMSE, pendiente y sesgo frente a la referencia", ins="Registro de versiones del modelo y del informe de validación", ubi="Repositorio de código y modelos (línea E11)",
   dterr="Tramo y departamento", dtemp="Por ciclo y acumulado", dpob="No aplica", dotr="Variable corregida: humedad, temperatura y fracción gruesa",
   lmet="Un ciclo completo no implica desempeño suficiente. El criterio de calidad son los umbrales R² ≥ 0,70, NRMSE ≤ 30 %, pendiente entre 0,65 y 1,35 y sesgo entre −5,0 y 5,0 µg/m³.", lcob="El indicador cuenta ciclos y no mide el error, que se verifica en las compuertas C1 y C2.", lmit="Cada ciclo se cierra con un informe de validación firmado por la metrología.",
   cext="Disponibilidad de datos pareados de las tres referencias", cins="Especialista en metrología y científico de datos contratados desde el mes 2 (H0)",
   fmt="Informe de validación firmado y entrada del registro de versiones", rver="Especialista en metrología", pver="Mensual"),
 "PERS-R03": dict(
   desc="Mide el tiempo de servicio mensual de la plataforma que aloja el entrenamiento del modelo, el gemelo digital y el tablero.",
   just="El tablero y el gemelo digital sostienen el uso institucional. Una plataforma caída interrumpe PERS-E01 aunque los nodos transmitan.",
   vars="Numerador: horas de servicio. Denominador: horas del mes. Factor: 100.",
   lbf="Primer trimestre completo tras A2.2 (semana 24; PROPUESTO)", lbfu="Monitor de servicio de la plataforma", lbm="Se mide desde la primera versión desplegada y se fija con el primer trimestre completo (PROPUESTO).",
   jm="Una meta de 99,0 % admite hasta " + num(R03_CAIDA_H) + " horas de indisponibilidad en un mes de 720 horas (CALCULADO). Es más exigente que la disponibilidad mensual de nodos de 90 % porque los gateways conservan 7 días de datos locales.",
   rep=REP_R, rrep="Ingenieros de software y nube",
   fsec="Registros de incidentes y de mantenimiento", ins="Monitor de servicio con sondeos periódicos", ubi="Reportes del proveedor de nube (línea E10) y repositorio del proyecto",
   dterr="No aplica (servicio único)", dtemp="Mensual", dpob="No aplica", dotr="Componente: ingesta de datos, gemelo digital y tablero",
   lmet="El proveedor reporta su propia disponibilidad. La verificación independiente exige un monitor externo.", lcob="No mide la latencia ni la calidad del dato.", lmit="Monitor de servicio propio contrastado con el reporte del proveedor.",
   cext="Servicio de nube contratado con acuerdo de nivel de servicio", cins="Contrato de nube vigente durante los 24 meses y contrapartida de infraestructura de la empresa (C06)",
   fmt="Reporte mensual de disponibilidad con registro de incidentes", rver="Ingenieros de software y nube, con revisión de la gerencia", pver="Mensual"),
 "PERS-R04": dict(
   desc="Compara la ejecución acumulada con la programación acumulada del presupuesto SGR de " + cop(SGR) + ".",
   just="Controla la viabilidad presupuestal y activa la reprogramación antes de que la desviación comprometa las compras por tramo.",
   vars="Numerador: ejecución acumulada menos programación acumulada. Denominador: programación acumulada. Factor: 100.",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero por definición al inicio de la ejecución (CALCULADO).",
   jm="El límite de 5 % al cierre equivale a " + mm(R04_TOL) + " millones de COP sobre el SGR solicitado (CALCULADO). La reserva de contingencia es de " + mm(M.RESERVA) + " millones de COP y su admisibilidad depende de los TdR (VACIO).",
   rep=REP_R, rrep="Gerencia de proyecto",
   fsec="Informe financiero conciliado con el informe técnico", ins="Sistema de seguimiento presupuestal (línea O05)", ubi="Plataforma de seguimiento y soportes contables de la entidad ejecutora",
   dterr="Paquete de trabajo (WP0 a WP3) y rubro SGR", dtemp="Mensual y semestral (flujo programado de cuatro semestres)", dpob="No aplica", dotr="Fuente de financiación (SGR o contrapartida) y rubro (siete rubros SGR)",
   lmet="La programación depende del flujo semestral, y las compras por tramo concentran el gasto en los meses 5, 13 y 18.", lcob="El indicador no mide el valor entregado por cada peso ejecutado.", lmit="Reprogramación documentada en cada compuerta.",
   cext="Tipo de cambio estable frente a las cotizaciones (R-FIN-01)", cins="Gerencia de proyecto y plataforma de seguimiento activas desde el mes 1",
   fmt="Informe financiero conciliado y cuadro de ejecución por rubro", rver="Gerencia de proyecto, con revisión de la evaluación externa (S07)", pver="Mensual"),
 "PERS-R05": dict(
   desc="Suma las horas con dato pareado entre un nodo y una referencia gravimétrica que cumplen el control de calidad.",
   just="La colocalización alimenta el entrenamiento del modelo (SC-1). Sin horas suficientes y sin rotaciones, la corrección no generaliza entre departamentos (R-TEC-04).",
   vars="Numerador: horas pareadas válidas por nodo. Denominador: no aplica (suma). Unidad: horas-nodo.",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero por definición al inicio de la ejecución (CALCULADO).",
   jm="Las 60.000 horas-nodo equivalen a " + pct(R05_FRAC) + " % de las " + num(R05_POSIBLES, 0) + " posibles si los 30 nodos del tramo 1 permanecen pareados durante las 16 semanas de A1.3 (CALCULADO; SUPUESTO de cálculo).",
   rep=REP_R, rrep="Especialista en metrología",
   fsec="Bitácora de la referencia y análisis gravimétricos de laboratorio acreditado (línea S01)", ins="Tablero de calidad de datos con reglas de completitud y de rango", ubi="Base de datos de colocalización en la nube",
   dterr="Departamento (una referencia por departamento) y tramo", dtemp="Mensual y por rotación (cuatro por departamento)", dpob="No aplica", dotr="Par nodo-referencia y contaminante (PM2,5 y PM10)",
   lmet="Una hora válida depende de reglas de control de calidad que fija el protocolo. Sin ellas el conteo se infla.", lcob="Tres referencias cubren 100 nodos, de modo que la cobertura espacial de la colocalización es parcial.", lmit="Cuatro rotaciones por departamento y validación cruzada entre departamentos (R-TEC-04).",
   cext="Tres referencias operando con completitud mayor o igual a 90 %", cins="Referencias instaladas entre los meses 4 y 6 (línea E03)",
   fmt="Bitácora de la referencia y reporte del tablero de calidad de datos", rver="Especialista en metrología", pver="Mensual"),
 "PERS-R06": dict(
   desc="Mide la proporción de informes técnicos y financieros entregados a tiempo frente a los exigidos.",
   just="El cumplimiento de informes condiciona los desembolsos y la trazabilidad ante el financiador.",
   vars="Numerador: informes entregados a tiempo. Denominador: informes exigidos. Factor: 100.",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero informes entregados al inicio de la ejecución (CALCULADO).",
   jm="La meta es 100 % en los tres cortes. El número de informes exigidos depende de los TdR [DATO_USUARIO: calendario y número de informes exigidos].",
   rep=REP_R, rrep="Gerencia de proyecto",
   fsec="Actas de compuerta e informes de la evaluación externa (línea S07)", ins="Matriz de informes con fecha de vencimiento y radicado", ubi="Repositorio documental del proyecto",
   dterr="Proyecto en conjunto", dtemp="Mensual", dpob="No aplica", dotr="Tipo de informe: técnico o financiero",
   lmet="Cumplir el plazo no mide la calidad del contenido.", lcob="El calendario exigido no se conoce (VACIO).", lmit="Revisión de contenido por la gerencia antes de radicar.",
   cext="Calendario de informes fijado por los TdR (VACIO)", cins="Gerencia de proyecto vinculada desde el mes 1 (línea P06)",
   fmt="Radicado de entrega y copia del informe", rver="Gerencia de proyecto", pver="Mensual"),
 "PERS-P01": dict(
   desc="Cuenta los nodos operativos con disponibilidad mensual de al menos 90 % y los gateways con enlace principal o alterno activo.",
   just="La red es el producto tecnológico principal (PROT-FUNC) y la fuente de datos del tablero. La disponibilidad mensual de 90 % es la meta de OE2.",
   vars="Numerador: nodos con disponibilidad mensual mayor o igual a 90 % y gateways con enlace activo. Denominador: nodos y gateways programados. Factor: no aplica (conteo).",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero nodos y cero gateways por definición al inicio de la ejecución (CALCULADO).",
   jm="Los cortes siguen las compuertas: 30 nodos y 3 gateways al mes 12, 70 y 7 al mes 17, y 100 y 10 al mes 19, con sostenimiento hasta el mes 24.",
   rep=REP_T, rrep="Gerencia de proyecto",
   fsec="Registro de transmisión de la plataforma y bitácoras de mantenimiento", ins="Cálculo mensual de disponibilidad por nodo con los paquetes recibidos", ubi="Base de datos de la plataforma (línea E10)",
   dterr="Departamento (33, 34 y 33 nodos; PROPUESTO), tramo y gateway", dtemp="Mensual con corte trimestral", dpob="No aplica", dotr="Causa de la falla: energía, enlace o equipo",
   lmet="La disponibilidad se calcula con paquetes recibidos y puede subestimar la operación si el gateway guarda datos locales por 7 días.", lcob="Un nodo disponible puede medir con sesgo. La calidad del dato se verifica con PERS-R05 y las compuertas.", lmit="Reporte conjunto de disponibilidad y de pérdida de paquetes (meta de 10 % o menos).",
   cext="Cobertura celular o satelital en los sitios de los gateways (estudio de la línea S06)", cins="Compuertas C1 y C2 aprobadas",
   fmt="Inventario con huella de configuración y registro fotográfico", rver="Ingenieros IoT y de campo, con revisión de la evaluación externa (S07)", pver="Trimestral"),
 "PERS-P02": dict(
   desc="Cuenta los registros de software ante la Dirección Nacional de Derecho de Autor (DNDA) del modelo de corrección, el firmware y el gemelo digital.",
   just="El registro acredita la titularidad del activo de conocimiento y habilita la cláusula de apertura y la transferencia a los custodios.",
   vars="Numerador: registros vigentes. Denominador: no aplica. Factor: 1 registro.",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero registros por definición al inicio de la ejecución (CALCULADO).",
   jm="Una solicitud radicada al mes 17 y un registro vigente al mes 24. La partida O03 inicia en el mes 12, cuando la compuerta C1 valida el modelo.",
   rep=REP_T, rrep="Profesional de convenios y custodia",
   fsec="Acuerdo de titularidad entre las partes y repositorio de código", ins="Formulario de registro de la DNDA", ubi="Archivo jurídico del proyecto y repositorio de código (línea E11)",
   dterr="No aplica (registro nacional)", dtemp="Trimestral", dpob="No aplica", dotr="Componente registrado: modelo de corrección, firmware o gemelo digital",
   lmet="El registro acredita la titularidad del código y no la novedad del método.", lcob="El indicador cuenta un registro único aunque el software tenga tres componentes.", lmit="Acuerdo de titularidad firmado antes de radicar la solicitud.",
   cext="Trámite de la DNDA dentro del plazo del proyecto", cins="Acuerdo de titularidad firmado entre las partes",
   fmt="Certificado de registro y radicado de la solicitud", rver="Profesional de convenios y custodia", pver="Trimestral"),
 "PERS-P03": dict(
   desc="Cuenta los artículos sometidos y aceptados en revistas Q1 o Q2 con filiación del proyecto.",
   just="La revisión por pares ofrece un control externo de la corrección y cumple el requisito de nuevo conocimiento de la tipificación MMG.",
   vars="Numerador: artículos sometidos y aceptados. Denominador: no aplica. Factor: meta de 2 sometidos y al menos 1 aceptado.",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero artículos por definición al inicio de la ejecución (CALCULADO).",
   jm="El primer artículo usa los resultados del piloto validados en la compuerta C1 (mes 12). El segundo exige la verificación final (H7, mes 23), de modo que solo el primero puede aceptarse al mes 24 (INFERIDO).",
   rep=REP_T, rrep="Investigador principal",
   fsec="CvLAC y GrupLAC de las personas autoras", ins="Matriz de seguimiento editorial", ubi="Repositorio documental del proyecto",
   dterr="No aplica", dtemp="Trimestral", dpob="Sexo y vinculación de las personas autoras", dotr="Cuartil de la revista al someter (Q1 o Q2)",
   lmet="El cuartil de una revista varía con el año y con la base de consulta.", lcob="El indicador cuenta artículos y no su uso.", lmit="Verificar el cuartil al someter y conservar el soporte.",
   cext="Tiempos editoriales compatibles con el cierre", cins="Resultados del piloto disponibles tras C1 y tiempo del equipo investigador (contrapartida de la IES)",
   fmt="Carta de aceptación y soporte de envío", rver="Investigador principal", pver="Trimestral"),
 "PERS-P04": dict(
   desc="Cuenta las actividades de apropiación social documentadas: talleres de co-diseño (nivel 3) y jornadas públicas (niveles 1 y 2).",
   just="El nivel 3 de la Escalera ASC es un compromiso mínimo del proyecto (tres actividades con acta) y sustenta los umbrales locales del tablero.",
   vars="Numerador: talleres y jornadas con acta y lista de asistencia. Denominador: no aplica. Factor: 29 actividades (20 talleres y 9 jornadas).",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero actividades por definición al inicio de la ejecución (CALCULADO).",
   jm="Los 20 talleres coinciden con 20 kits (M05) y 20 eventos (V05), y las 9 jornadas con 9 eventos (O02) (CALCULADO). La meta del mes 17 iguala la final, mientras las líneas O02 y V05 se extienden hasta el mes 24.",
   rep=REP_T, rrep="Coordinación de apropiación social",
   fsec="Registro fotográfico y consentimientos informados", ins="Acta firmada por representantes comunitarios y lista de asistencia", ubi="Archivo documental del proyecto con custodia de datos personales",
   dterr="Departamento y municipio focalizado (12 municipios, 4 por departamento; SUPUESTO)", dtemp="Trimestral", dpob="Sexo, edad y pertenencia étnica de quienes participan, con consentimiento informado", dotr="Tipo de actividad (taller o jornada) y nivel de la Escalera ASC",
   lmet="Una actividad documentada mide ejecución. La calidad de la participación no se infiere del conteo.", lcob="La asistencia puede no representar a la población expuesta ni al personal operativo de remoción.", lmit="Encuesta de satisfacción de participantes y registro de decisiones incorporadas.",
   cext="Participación comunitaria con consentimiento informado", cins="Coordinación de apropiación social contratada desde el mes 1 (línea P05)",
   fmt="Acta firmada, lista de asistencia y registro fotográfico", rver="Coordinación de apropiación social", pver="Trimestral"),
 "PERS-E01": dict(
   desc="Mide la proporción de comités focalizados con al menos una decisión documentada por trimestre que se basa en el tablero.",
   just="Responde si los comités usan el producto. Es la meta de OE3 y el criterio de uso de la compuerta C1 (50 % o más de los comités del tramo 1).",
   vars="Numerador: comités con decisión documentada en el trimestre. Denominador: comités focalizados (15: 12 municipales y 3 departamentales; SUPUESTO). Factor: 100.",
   lbf="Antes de A3.2 (semana 50), durante el tramo 1", lbfu="Actas de los comités previas al uso del tablero", lbm="Revisión de las actas de los trimestres previos al tablero para contar decisiones basadas en datos de calidad del aire (PROPUESTO).",
   jm="El 65 % de 15 comités son " + str(E01_N[65]) + " comités y el 75 % son " + str(E01_N[75]) + " (CALCULADO con redondeo hacia arriba). Cada comité pesa 6,7 puntos porcentuales. El número de comités del tramo 1 es [DATO_USUARIO: comités del tramo 1].",
   rep=REP_T, rrep="Gerencia de proyecto",
   fsec="Registro de consultas y decisiones del tablero", ins="Matriz de revisión de actas con criterio de decisión basada en el tablero", ubi="Archivo de actas y registro del tablero",
   dterr="Comité (municipal o departamental), municipio y departamento", dtemp="Trimestral", dpob="No aplica; se reporta el número de funcionarios participantes (150; SUPUESTO)", dotr="Tipo de decisión documentada: alerta, comunicación o medida de protección",
   lmet="El indicador mide decisiones documentadas y no su calidad ni su efecto sobre la exposición.", lcob="Un comité puede decidir sin dejar acta. El registro del tablero cubre ese vacío solo si el uso queda trazado.", lmit="Doble fuente: acta del comité y registro de consultas al tablero.",
   cext="Comités constituidos y con sesiones periódicas", cins="Designación de personal de los comités con permanencia durante los 24 meses",
   fmt="Acta del comité con referencia a la lectura del tablero", rver="Coordinación de apropiación social, con revisión de la evaluación externa (S07)", pver="Trimestral"),
 "PERS-E02": dict(
   desc="Mide la reducción relativa de la tasa de falsas alarmas frente a la línea base que se mide en el tramo 1.",
   just="Es el efecto técnico de la medición verificada sobre la calidad de las alertas. Sin línea base no existe comparación.",
   vars="Numerador: tasa de falsas alarmas del periodo. Denominador: tasa de la línea base. Factor: 1 menos el cociente, por 100.",
   lbf="Meses 6 a 10 (A1.3, semanas 24 a 40)", lbfu="Lecturas sin corrección frente a la referencia colocalizada", lbm="Se cuentan las superaciones de umbral de las lecturas sin corrección que la referencia no confirma (PROPUESTO).",
   jm="La meta es relativa: 15 % al mes 17 y 30 % al mes 24. No fija un valor absoluto de falsas alarmas porque la línea base no existe todavía (VACIO).",
   rep=REP_T, rrep="Profesional en calidad del aire y salud ambiental",
   fsec="Registro de alertas y verificación con referencia", ins="Cruce entre alertas emitidas y mediciones de referencia", ubi="Base de datos de colocalización y registro de alertas",
   dterr="Departamento y sitio con referencia", dtemp="Trimestral", dpob="No aplica", dotr="Contaminante (PM2,5 y PM10) y umbral del índice",
   lmet="Verificar una falsa alarma exige una referencia en el sitio, y tres referencias no cubren los 100 nodos.", lcob="Fuera de los sitios con referencia, la reducción se estima con el gemelo digital y queda INFERIDA.", lmit="Muestreo rotativo de las referencias y validación del gemelo digital con las tres referencias.",
   cext="Variabilidad meteorológica sin cambios de régimen entre la línea base y la medición", cins="Umbrales validados localmente en el co-diseño",
   fmt="Informe de cruce entre alertas y referencia", rver="Profesional en calidad del aire y salud ambiental", pver="Trimestral"),
 "PERS-E03": dict(
   desc="Mide las personas custodias que aprueban la evaluación práctica en mantenimiento, lectura y operación, en número y en proporción de las formadas.",
   just="La continuidad después del mes 24 depende de competencias instaladas en los custodios (SC-4).",
   vars="Numerador: personas con evaluación práctica aprobada. Denominador: personas formadas. Factor: 100, y número absoluto.",
   lbf="2026-10 (valor de partida)", lbfu="Ficha maestra del proyecto", lbm="Cero personas certificadas por definición al inicio de la ejecución (CALCULADO).",
   jm="Las metas de 20, 40 y 60 personas equivalen a 20 por tramo. La formación cuesta " + mm(B["S09"]["total"]) + " millones de COP en tres tramos de 50,0 millones (línea S09), es decir " + mm(E03_COSTO_PERS) + " millones de COP por persona certificada (CALCULADO).",
   rep="Semestral a la gerencia del proyecto; al financiador según los TdR [DATO_USUARIO: calendario de informes]", rrep="Profesional de convenios y custodia",
   fsec="Planillas de formación y listas de asistencia", ins="Evaluación práctica con lista de verificación", ubi="Archivo de formación y base de datos de personas certificadas",
   dterr="Tramo, departamento y entidad custodia", dtemp="Semestral", dpob="Sexo y edad de las personas certificadas, con protección de datos personales", dotr="Competencia evaluada: mantenimiento, lectura u operación",
   lmet="Una evaluación práctica aprobada acredita la competencia en ese momento y no su permanencia.", lcob="Las personas certificadas pueden salir de la entidad custodia.", lmit="Cláusulas de reposición y recertificación de personal en los convenios por tramo (PROPUESTO).",
   cext="Rotación del personal local acotada", cins="Custodios que designan personal con permanencia",
   fmt="Certificados y actas de evaluación práctica", rver="Profesional de convenios y custodia", pver="Semestral"),
 "PERS-S01": dict(
   desc="Mide la proporción de eventos de superación de umbral confirmados en los que se activó y registró una medida de protección.",
   just="Es el cambio institucional sostenido que busca el proyecto: que una medición verificada produzca una acción registrada. No mide exposición ni salud.",
   vars="Numerador: eventos con medida activada y registrada. Denominador: eventos de superación confirmados. Factor: 100.",
   lbf="Meses 1 a 12 (tramo 1), con registro retrospectivo de eventos y medidas (PROPUESTO)", lbfu="Registros de los comités y de las secretarías de gestión del riesgo", lbm="Conteo de eventos de superación y de medidas registradas antes del uso del protocolo (PROPUESTO).",
   jm="La meta se mide a los 12 meses posteriores al cierre, es decir, en el mes 36. Ese punto coincide con el límite inferior del horizonte de 1 a 5 años que fija el metaprompt para el impacto.",
   rep="Anual al financiador y a los custodios, con informe de la evaluación externa posproyecto", rrep="Evaluación externa posproyecto",
   fsec="Informes de la evaluación externa posproyecto", ins="Registro de eventos y de medidas con verificación frente a la referencia", ubi="Plataforma entregada a los custodios, con respaldo del proyecto",
   dterr="Departamento y municipio", dtemp="Anual, en los meses 30 y 36", dpob="No se desagrega por persona; el indicador no estima efectos en salud", dotr="Tipo de medida de protección y contaminante",
   lmet="Confirmar un evento exige referencia. Con tres referencias, parte de los eventos se confirma con el gemelo digital (INFERIDO).", lcob="Sin custodia operativa no hay registro, de modo que el indicador depende de PERS-S02.", lmit="Evaluación externa con revisión de los registros de los comités.",
   cext="Eventos de superación ocurren en la ventana de medición; si no ocurren, el indicador no es calculable", cins="Custodia operativa y datos disponibles",
   fmt="Informe de evaluación externa con la muestra de eventos revisada", rver="Evaluación externa posproyecto", pver="Anual, 6 a 12 meses tras el cierre"),
 "PERS-S02": dict(
   desc="Mide la proporción de nodos entregados que los custodios siguen operando con partida presupuestal y competencia a los 12 meses del cierre.",
   just="Es la prueba de continuidad. Un nodo sin operador pierde el aporte del proyecto después del mes 24 (R-ORG-02).",
   vars="Numerador: nodos operados por custodios con partida y competencia a los 12 meses. Denominador: nodos entregados. Factor: 100.",
   lbf="Meses 6 a 12 (convenio del tramo 1; PROPUESTO)", lbfu="Convenios y presupuestos de los custodios del tramo 1", lbm="Estado de los convenios y de las partidas del tramo 1 al cierre del tramo (PROPUESTO).",
   jm="El 70 % equivale a " + str(S02_70) + " de 100 nodos si se entregan 100 (CALCULADO). Por departamento equivale a 24 nodos de 33 en Caldas, 24 de 34 en Cundinamarca y 24 de 33 en Valle del Cauca.",
   rep="Anual al financiador y a los custodios, con informe de la evaluación externa posproyecto", rrep="Evaluación externa posproyecto",
   fsec="Presupuestos de los custodios y actas de entrega (H8)", ins="Verificación en sitio de una muestra de nodos y revisión de convenios", ubi="Plataforma y archivo de convenios",
   dterr="Tramo, departamento y entidad custodia", dtemp="Anual, en el mes 36", dpob="No aplica", dotr="Componente en custodia: nodos, gateways, plataforma o tablero",
   lmet="Una partida aprobada no asegura el gasto efectivo.", lcob="El costo total de sostenimiento no es calculable (NO_CALCULABLE).", lmit="Cláusula de apertura y salida ordenada en los convenios.",
   cext="Restricción fiscal de los custodios (R-ORG-02)", cins="Cláusula de apertura y financiación de los custodios",
   fmt="Informe de evaluación externa con revisión de convenios y muestra de nodos", rver="Evaluación externa posproyecto", pver="Anual, 12 meses tras el cierre"),
}
assert set(EXTRA) == set(IND)
for c in IND:
    assert IND[c]["supuesto"].split(" (")[0][:20]  # sanity
