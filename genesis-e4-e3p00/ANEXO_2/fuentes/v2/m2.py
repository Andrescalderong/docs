# -*- coding: utf-8 -*-
"""LIBRO MAESTRO v2 del Anexo 2: ajusta el libro maestro del proyecto (maestro.py) a los términos de referencia (TdR v1.6)
que se aportaron después de la corrida anterior. Fuente única de cifras del Anexo 2.
Cada ajuste se registra en AJUSTES con su fundamento en los TdR. Valores monetarios en pesos colombianos (enteros)."""
import sys, os, copy, math, collections
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/maestro")
import maestro as M0
import indicadores as I0

M = M0.M
L = M0.L

# ------------------------------------------------------------------ IDENTIDAD
IDENT = dict(M0.IDENT)
IDENT["titulo"] = ("Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo "
                   "por material particulado posterremoto")   # título registrado en el SIGP (código 143329) y en el Anexo 3 v5
IDENT["proceso"] = "Implementación"
IDENT["objeto"] = "red IoT híbrida Edge-Cloud y gemelo digital predictivo de demolición para la gestión anticipada del riesgo por material particulado posterremoto"
IDENT["localizacion"] = "Manizales (Caldas) y Calarcá (Quindío)"
IDENT["sigp"] = "143329"
IDENT["trl_final"] = 8
IDENT["trl_piso"] = 7
IDENT["fecha_corte"] = "23 de octubre de 2026"
IDENT["fecha_cierre_conv"] = "3 de noviembre de 2026"
IDENT["linea_principal"] = "5.1. Ciencia, tecnología e innovación para la gestión anticipada del riesgo y la seguridad de las regiones"
IDENT["tope_cop"] = 14_000_000_000
assert len(IDENT["titulo"]) <= 256, len(IDENT["titulo"])

# ------------------------------------------------------------------ RUBROS DEL TdR (numeral 12.2)
RUB = ["Talento Humano", "Equipos y software", "Capacitación y eventos", "Servicios tecnológicos y pruebas",
       "Materiales, insumos y documentación", "Protección del conocimiento y divulgación", "Gastos de viaje",
       "Infraestructura", "Administrativos", "Seguimiento", "Otros"]
RUBRO_DE = {  # línea del libro anterior -> rubro del TdR
    **{f"P{n:02d}": "Talento Humano" for n in range(1, 15)}, "P02a": "Talento Humano", "P02b": "Talento Humano",
    **{f"E{n:02d}": "Equipos y software" for n in range(1, 12)},
    "E12": "Servicios tecnológicos y pruebas", "S10": "Servicios tecnológicos y pruebas",
    "S01": "Servicios tecnológicos y pruebas", "S03": "Servicios tecnológicos y pruebas", "S06": "Servicios tecnológicos y pruebas",
    "S07": "Servicios tecnológicos y pruebas", "S08": "Servicios tecnológicos y pruebas",
    "S05": "Infraestructura",
    "S09": "Capacitación y eventos", "O02": "Capacitación y eventos", "V05": "Capacitación y eventos",
    "S02": "Protección del conocimiento y divulgación", "O03": "Protección del conocimiento y divulgación",
    "O01": "Protección del conocimiento y divulgación", "O06": "Protección del conocimiento y divulgación", "M04": "Protección del conocimiento y divulgación",
    **{f"M{n:02d}": "Materiales, insumos y documentación" for n in (1, 2, 3, 5, 6, 7)},
    "V01": "Gastos de viaje", "V02": "Gastos de viaje", "V03": "Gastos de viaje", "V04": "Gastos de viaje",
    "S11": "Administrativos", "O05a": "Administrativos", "O05b": "Seguimiento",
    # laboratorio de modelación predictiva de demolición
    "P15": "Talento Humano", "P16": "Talento Humano", "P17": "Talento Humano",
    **{f"E{n}": "Equipos y software" for n in (13, 14, 15, 16, 17)},
    "S12": "Servicios tecnológicos y pruebas", "S13": "Servicios tecnológicos y pruebas", "S14": "Servicios tecnológicos y pruebas", "S15": "Servicios tecnológicos y pruebas",
    "S16": "Capacitación y eventos", "S17": "Administrativos", "M08": "Materiales, insumos y documentación",
    "V06": "Gastos de viaje", "V07": "Gastos de viaje", "V08": "Gastos de viaje", "O07": "Protección del conocimiento y divulgación",
}

# ------------------------------------------------------------------ PRESUPUESTO SGR v2
AJUSTES = []
def ajuste(id_, tema, antes, despues, base):
    AJUSTES.append(dict(id=id_, tema=tema, antes=antes, despues=despues, base=base))

BUD = []
for r in M0.BUDGET:
    i = r["id"]
    if i == "X01":
        ajuste("AJ-01", "Reserva de contingencia", "636.000.000 COP como rubro del SGR",
               "Se elimina como rubro; el riesgo se atiende con unidades de reserva, compuertas y programación",
               "El numeral 12.2 no contempla la reserva como rubro y el numeral 14.3 exige justificar cada rubro con cotizaciones")
        continue
    if i == "S04":
        ajuste("AJ-02", "Póliza todo riesgo de equipos", "50.000.000 COP en servicios técnicos", "Se elimina del SGR",
               "El numeral 14.3 excluye los seguros del apoyo del SGR")
        continue
    if i == "O04":
        ajuste("AJ-03", "Pólizas y garantías", "60.000.000 COP en otros rubros", "Se elimina del SGR",
               "El numeral 14.3 excluye los seguros del apoyo del SGR")
        continue
    if i == "P03":
        r = dict(r); r.update(concepto="Doctor en estancia posdoctoral (1)", cant=24, vunit=12_920_000, total=24 * 12_920_000, nat="DOCUMENTADO",
                 just="Estancia posdoctoral de 24 meses con el monto del numeral 14.4 de los TdR; asesora a jóvenes y maestrantes y lidera el modelo de corrección.")
        ajuste("AJ-04", "Científico de datos senior (480.000.000 COP)", "24 persona-mes a 20.000.000 COP",
               "Doctor en estancia posdoctoral: 24 meses a 12.920.000 COP (310.080.000 COP)",
               "El numeral 9 exige un doctor en estancia posdoctoral y el numeral 14.4 fija su valor mensual")
    if i == "P01":
        r = dict(r); r.update(nat="DOCUMENTADO", just="Seis jóvenes investigadores e innovadores, estudiantes de pregrado, 12 meses cada uno a 2.000.000 COP (numeral 14.4); dos cohortes de tres.")
    if i == "P02":
        a = dict(r); a.update(id="P02a", concepto="Sostenimiento de estudiantes de maestría (2)", cant=48, vunit=4_350_000, total=48 * 4_350_000, nat="DOCUMENTADO",
                              just="Sostenimiento de 24 meses a 4.350.000 COP por estudiante (numeral 14.4).")
        b = dict(r); b.update(id="P02b", concepto="Matrícula de maestría en modalidad de investigación (2)", unidad="matrícula", cant=2, vunit=48_000_000,
                              total=2 * 48_000_000, nat="DOCUMENTADO", just="Matrícula hasta 48.000.000 COP por estudiante (numeral 14.4).")
        assert a["total"] + b["total"] == r["total"]
        BUD += [a, b]; continue
    if i == "O05":
        a = dict(r); a.update(id="O05a", concepto="Administración del proyecto (gastos administrativos y revisoría)", cant=24, vunit=7_000_000, total=24 * 7_000_000, nat="PROPUESTO",
                              just="Gastos administrativos del proyecto; no incluye porcentajes automáticos.")
        b = dict(r); b.update(id="O05b", concepto="Apoyo a la supervisión y plataforma de seguimiento", cant=24, vunit=8_000_000, total=24 * 8_000_000, nat="PROPUESTO",
                              just="Profesional de seguimiento técnico y financiero y plataforma de seguimiento; estimación por perfil y dedicación (numeral 19.1).")
        assert a["total"] + b["total"] == r["total"]
        ajuste("AJ-05", "Administración (360.000.000 COP en otros rubros)", "Un solo rubro de administración",
               "Se separa en Administrativos (168.000.000 COP) y Seguimiento (192.000.000 COP), con el mismo total",
               "Los numerales 12.2 y 14.3 exigen el rubro Seguimiento para la vigilancia del proyecto")
        BUD += [a, b]; continue
    BUD.append(dict(r))
# ------------------------------------------------------------------ LABORATORIO DE MODELACIÓN PREDICTIVA DE DEMOLICIÓN (dentro de los objetivos 1, 2 y 3)
# Decisión de la alianza del 23 de octubre de 2026: el proyecto incorpora un laboratorio, ubicado en la IES y validado por ella, que modela la emisión,
# la dispersión y la exposición esperada de polvo antes de demoler una edificación. No crea un objetivo específico adicional: su validación
# se ubica en el objetivo 1, su construcción en el objetivo 2 y su adopción en el objetivo 3. Los valores son estimaciones sujetas a cotización.
LAB_LINEAS = [
 L("P15", "Personal", "Investigador líder en modelación atmosférica y dispersión de contaminantes (1)", "persona-mes", 22, 13_000_000, "SGR", "PROPUESTO", "WP2", 3, 24,
   "Lidera el laboratorio de modelación, el modelo de emisión y de dispersión y la validación del gemelo predictivo."),
 L("P16", "Personal", "Ingeniero en dinámica de fluidos computacional y cómputo de alto rendimiento (1)", "persona-mes", 20, 10_000_000, "SGR", "PROPUESTO", "WP2", 7, 24,
   "Monta las simulaciones de calles y edificios y el modelo sustituto de respuesta rápida."),
 L("P17", "Personal", "Ingeniero en demolición y control de polvo en obra (1)", "persona-mes", 14, 9_000_000, "SGR", "PROPUESTO", "WP2", 3, 22,
   "Define el inventario de actividad de demolición, las medidas de control y las campañas de campo."),
 L("E13", "Equipos y software", "Servidor de cálculo de alto rendimiento y almacenamiento del laboratorio de modelación", "unidad", 1, 160_000_000, "SGR", "PROPUESTO", "WP2", 7, 9,
   "Ejecuta las simulaciones de dispersión y entrena el modelo sustituto."),
 L("E14", "Equipos y software", "Estaciones meteorológicas automáticas con anemómetro sónico, pluviómetro y radiómetro (3 departamentales y 1 móvil)", "unidad", 4, 32_000_000, "SGR", "PROPUESTO", "WP2", 7, 10,
   "Miden viento, lluvia y radiación en los sitios; el viento es el principal dato de entrada del modelo."),
 L("E15", "Equipos y software", "Dron con sensor LiDAR y cámara fotogramétrica y receptor GNSS RTK", "unidad", 1, 105_000_000, "SGR", "PROPUESTO", "WP2", 7, 9,
   "Levanta la geometría de las edificaciones y de su entorno para el modelo."),
 L("E16", "Equipos y software", "Monitores portátiles de material particulado de referencia equivalente para campañas de demolición", "unidad", 2, 72_000_000, "SGR", "PROPUESTO", "WP2", 8, 10,
   "Miden a distintas distancias de la demolición para validar el modelo."),
 L("E17", "Equipos y software", "Licencias de software de modelación urbana, de dispersión y SIG, de pago único con soporte durante la ejecución", "paquete", 1, 55_000_000, "SGR", "PROPUESTO", "WP2", 7, 24,
   "Complementa las herramientas de código abierto con soporte técnico."),
 L("S12", "Servicios técnicos", "Campañas de medición en demoliciones y remociones reales (logística, seguridad industrial y acceso)", "campaña", 9, 16_000_000, "SGR", "PROPUESTO", "WP1", 14, 22,
   "Nueve campañas para obtener al menos seis eventos válidos de validación."),
 L("S13", "Servicios técnicos", "Caracterización granulométrica y química del polvo de escombros en laboratorio acreditado", "muestra", 30, 1_100_000, "SGR", "PROPUESTO", "WP2", 5, 16,
   "Ajusta los factores de emisión y la distribución de tamaños con polvo del territorio."),
 L("S14", "Servicios técnicos", "Verificación y validación independiente del modelo predictivo", "servicio", 1, 48_000_000, "SGR", "PROPUESTO", "WP1", 21, 23,
   "Revisión externa del modelo y de sus métricas antes de la transferencia."),
 L("S15", "Servicios técnicos", "Cartografía de alta resolución y modelos digitales de terreno de los sitios", "paquete", 1, 20_000_000, "SGR", "PROPUESTO", "WP2", 5, 6,
   "Base geográfica del modelo."),
 L("S16", "Otros rubros", "Talleres de evaluación previa de demolición con comités y obras (6)", "taller", 6, 8_000_000, "SGR", "PROPUESTO", "WP3", 21, 24,
   "Dos talleres por departamento para leer el resultado y decidir medidas."),
 L("S17", "Otros rubros", "Importación y nacionalización de equipos del laboratorio de modelación", "servicio", 1, 25_000_000, "SGR", "PROPUESTO", "WP2", 7, 10,
   "Trámite de importación del servidor, el dron y los monitores portátiles."),
 L("M08", "Materiales e insumos", "Consumibles y repuestos de las campañas de medición (filtros, baterías y verificaciones de campo)", "lote", 1, 28_000_000, "SGR", "PROPUESTO", "WP1", 14, 22,
   "Insumos de las nueve campañas."),
 L("V06", "Viajes y viáticos", "Tiquetes aéreos nacionales de las campañas de demolición", "trayecto", 40, 600_000, "SGR", "PROPUESTO", "WP1", 14, 22, "Desplazamiento del equipo a los sitios."),
 L("V07", "Viajes y viáticos", "Viáticos de alojamiento y manutención de las campañas de demolición", "día-persona", 160, 350_000, "SGR", "PROPUESTO", "WP1", 14, 22, "Equipo de cuatro personas por campaña."),
 L("V08", "Viajes y viáticos", "Arrendamiento de vehículos 4x4 de las campañas de demolición", "día", 70, 450_000, "SGR", "PROPUESTO", "WP1", 14, 22, "Transporte de equipos de medición."),
 L("O07", "Otros rubros", "Registro del software y de los datos del modelo predictivo ante la DNDA", "paquete", 1, 10_000_000, "SGR", "PROPUESTO", "WP3", 22, 24, "Protección del software y de la base de datos."),
]
BUD += LAB_LINEAS
ajuste("AJ-10", "Laboratorio de modelación predictiva de demolición", "Sin módulo predictivo; el gemelo digital solo estimaba entre nodos",
       "Cinco actividades nuevas repartidas en los objetivos 1, 2 y 3 y 19 líneas nuevas del SGR",
       "Decisión de la alianza del 23 de octubre de 2026; responde al alcance 5.1.2 de los TdR (modelación avanzada, gemelos digitales y analítica predictiva)")
for r in BUD:
    r["rubro_tdr"] = RUBRO_DE[r["id"]]

# ------------------------------------------------------------------ CONTRAPARTIDA v2 (cada integrante aporta, numeral 3)
CONTRA = [dict(r) for r in M0.CONTRA]
CONTRA.append(L("C07", "Personal (especie)", "Municipio aliado: profesionales de gestión del riesgo y logística de acceso a sitios", "mes", 24, 5_000_000,
                "ENT", "PROPUESTO", "WP3", 1, 24,
                "Tres profesionales al 20 % durante 24 meses y apoyo logístico; valor sujeto a certificación del municipio aliado."))
CONTRA.append(L("C09", "Infraestructura (especie)", "Entidad proponente: espacio, energía, red y soporte técnico del laboratorio de modelación (24 meses)", "mes", 24, 6_000_000,
                "IES", "PROPUESTO", "WP2", 3, 24, "Espacio con control de acceso y climatización, energía, red y soporte del cómputo institucional; valor sujeto a certificación de la IES."))
ajuste("AJ-06", "Contrapartida de la entidad territorial", "Sin aporte (VACIO)", "120.000.000 COP en especie (PROPUESTO, pendiente de certificación)",
       "El numeral 3 exige que cada integrante de la alianza aporte una contrapartida cuantificada en términos monetarios")

# ------------------------------------------------------------------ ACTIVIDADES v2 (22) con semanas del CPM
# id Anexo 2, id CPM, nombre, OE
ACT = [
 ("1.1", "A1.1", "Seleccionar los sitios y diseñar la colocalización", "OE1"),
 ("1.2", "A1.2", "Adquirir y caracterizar el lote 1 de nodos y las referencias", "OE1"),
 ("1.3", "A1.3", "Instalar el tramo 1, colocalizar y calibrar en el piloto", "OE1"),
 ("1.4", "A1.4", "Entrenar y validar el modelo de corrección y decidir en la compuerta C1", "OE1"),
 ("1.5", "A1.5", "Reentrenar y verificar por municipio el tramo 2 y decidir en la compuerta C2", "OE1"),
 ("1.6", "A1.6", "Verificar el desempeño final y ejecutar el ensayo independiente", "OE1"),
 ("1.7", None,   "Validar el gemelo predictivo con demoliciones y remociones reales en los dos municipios", "OE1"),
 ("1.8", None,   "Administración y apoyo a la supervisión (objetivo específico 1)", "OE1"),
 ("2.1", "A2.1", "Diseñar la arquitectura de enlace y energía", "OE2"),
 ("2.2", "A2.2", "Desarrollar el firmware y la plataforma base (gemelo digital y tablero)", "OE2"),
 ("2.3", "A2.3", "Instalar el tramo 2", "OE2"),
 ("2.4", "A2.4", "Instalar el tramo 3", "OE2"),
 ("2.5", None,   "Diseñar el laboratorio de modelación y el inventario de emisión de demolición", "OE2"),
 ("2.6", None,   "Dotar el laboratorio y montar la cadena de modelación", "OE2"),
 ("2.7", None,   "Construir y calibrar el gemelo predictivo de demolición", "OE2"),
 ("2.8", None,   "Administración y apoyo a la supervisión (objetivo específico 2)", "OE2"),
 ("3.1", "A3.1", "Co-diseñar los umbrales y el protocolo de alerta con los comités", "OE3"),
 ("3.2", "A3.2", "Poner en uso el tablero con los comités", "OE3"),
 ("3.3", "A3.3", "Formar custodios y firmar los convenios por tramo", "OE3"),
 ("3.4", "A3.4", "Transferir, cerrar y evaluar", "OE3"),
 ("3.5", None,   "Adoptar el protocolo de evaluación previa de demolición y transferir el laboratorio", "OE3"),
 ("3.6", None,   "Administración y apoyo a la supervisión (objetivo específico 3)", "OE3"),
]
OE_NOMBRE = {"OE1": "Medición verificada", "OE2": "Disponibilidad de la red", "OE3": "Uso institucional y custodia"}
# actividades del laboratorio (fuera de la ruta crítica): semana de inicio, semana de fin y holgura en semanas
SEM_LAB = {"2.5": (8, 26, 6), "2.6": (26, 44, 6), "2.7": (44, 70, 6), "1.7": (60, 96, 4), "3.5": (90, 100, 4)}
# La Ley 1523 de 2012 denomina «consejos» a las instancias de gestión del riesgo; el Anexo 3 v5 escribe «comités» en 3.1 y 3.2.
ACT = [(a[0], a[1], a[2].replace("con los comités", "con los consejos"), a[3]) for a in ACT]
ACTD = collections.OrderedDict((a[0], dict(id=a[0], cpm=a[1], nombre=a[2], oe=a[3])) for a in ACT)
SEM_MES = 52 / 12
def mes_ini(sem): return int(math.floor(sem / SEM_MES + 1e-9)) + 1
def mes_fin(sem): return int(math.ceil(sem / SEM_MES - 1e-9))
# ventana de semanas por actividad (incluye las compuertas C1 y C2 cuando se adjuntan)
for k, a in ACTD.items():
    if a["cpm"]:
        c = M0.ACTS[a["cpm"]]; es, ef = c["ES"], c["EF"]
        if k == "1.4": ef = M0.ACTS["C1"]["EF"]
        if k == "1.5": ef = M0.ACTS["C2"]["EF"]
        a.update(es=es, ef=ef, holgura=c["holgura"], critica=(c["holgura"] == 0))
    elif k in SEM_LAB:
        a.update(es=SEM_LAB[k][0], ef=SEM_LAB[k][1], holgura=SEM_LAB[k][2], critica=False)
    else:
        a.update(es=0, ef=M0.DURACION_SEMANAS, holgura=0, critica=False)
    a["m_ini"] = mes_ini(a["es"]) if a["es"] > 0 else 1
    a["m_fin"] = min(24, mes_fin(a["ef"]))

# ------------------------------------------------------------------ ASIGNACIÓN DEL PRESUPUESTO A ACTIVIDADES
def dur(k): return max(1, ACTD[k]["ef"] - ACTD[k]["es"])
def por_duracion(keys):
    t = sum(dur(k) for k in keys); return {k: dur(k) / t for k in keys}
OE1 = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"]; OE2 = ["2.1", "2.2", "2.3", "2.4"]; OE3 = ["3.1", "3.2", "3.3", "3.4"]
LAB = ["2.5", "2.6", "2.7", "1.7", "3.5"]   # actividades del laboratorio de modelación (objetivos 2, 1 y 3)
ADM = ["1.8", "2.8", "3.6"]
TERCIOS = {k: 1 / 3 for k in ADM}
TR = {"1.2": 36 / 120, "2.3": 48 / 120, "2.4": 36 / 120}   # por tramo de compra de nodos (36, 48, 36)
TRG = {"1.2": 4 / 11, "2.3": 4 / 11, "2.4": 3 / 11}        # gateways comprados (4, 4, 3)
SIT = {"1.3": 33 / 110, "2.3": 44 / 110, "2.4": 33 / 110}  # sitios por tramo
VIAJE = {"1.3": .30, "2.3": .25, "2.4": .20, "3.1": .10, "3.2": .075, "3.3": .075}
ALLOC = {
 "P01": por_duracion(OE1), "P02a": por_duracion(OE1), "P02b": por_duracion(OE1), "P03": por_duracion(OE1), "P07": por_duracion(OE1),
 "P04": por_duracion(OE2), "P08": por_duracion(OE2), "P09": por_duracion(OE2), "P10": por_duracion(OE2), "P12": por_duracion(OE2),
 "P05": por_duracion(OE3), "P11": por_duracion(OE3), "P13": por_duracion(OE3), "P14": por_duracion(OE3),
 "P06": TERCIOS,
 "E01": TR, "E02": {"1.2": 50 / 150, "2.3": 50 / 150, "2.4": 50 / 150}, "E03": {"1.2": 1.0}, "E04": TRG, "E05": TR,
 "E06": {"1.3": .3, "2.3": .4, "2.4": .3}, "E07": {"1.2": 1.0}, "E08": {"1.4": 1.0}, "E09": {"1.3": 1.0},
 "E10": {"2.2": 1.0}, "E11": {"2.2": 1.0}, "E12": {"1.3": .3, "2.3": .4, "2.4": .3}, "S10": {"1.3": .3, "2.3": .4, "2.4": .3},
 "M01": {"1.3": .6, "1.6": .4}, "M02": {"1.2": .5, "1.3": .5}, "M03": TR, "M04": {"3.2": .6, "3.3": .4}, "M05": {"3.1": 1.0},
 "M06": SIT, "M07": {"2.3": .5, "2.4": .5},
 "S01": {"1.3": .5, "1.5": .2, "1.6": .3}, "S02": {"3.4": 1.0}, "S03": {"2.2": .5, "2.4": .5}, "S05": SIT, "S06": {"2.1": 1.0},
 "S07": {"1.4": .5, "3.4": .5}, "S08": {"1.6": 1.0}, "S09": {"3.3": 1.0}, "S11": {"1.2": 1 / 3, "2.3": 1 / 3, "2.4": 1 / 3},
 "V01": VIAJE, "V02": VIAJE, "V03": VIAJE, "V04": {"3.4": 1.0}, "V05": {"3.1": 1.0},
 "O01": {"1.6": 1.0}, "O02": {"3.2": 4 / 9, "3.3": 3 / 9, "3.4": 2 / 9}, "O03": {"3.4": 1.0}, "O05a": TERCIOS, "O05b": TERCIOS,
 "O06": {"3.2": .4, "3.4": .6},
 # laboratorio de modelación predictiva
 "P15": {"2.5": .15, "2.6": .15, "2.7": .30, "1.7": .30, "3.5": .10}, "P16": {"2.6": .25, "2.7": .45, "1.7": .30}, "P17": {"2.5": .30, "1.7": .55, "3.5": .15},
 "E13": {"2.6": 1.0}, "E14": {"2.6": 1.0}, "E15": {"2.6": 1.0}, "E16": {"2.6": 1.0}, "E17": {"2.6": .5, "2.7": .5},
 "S12": {"1.7": 1.0}, "S13": {"2.5": .4, "2.7": .6}, "S14": {"1.7": .6, "3.5": .4}, "S15": {"2.5": 1.0}, "S16": {"3.5": 1.0}, "S17": {"2.6": 1.0},
 "M08": {"1.7": 1.0}, "V06": {"1.7": .8, "3.5": .2}, "V07": {"1.7": .8, "3.5": .2}, "V08": {"1.7": .8, "3.5": .2}, "O07": {"3.5": 1.0},
}
CALLOC = {  # contrapartida
 "C01": TERCIOS, "C02": por_duracion(OE1), "C03": por_duracion(OE3), "C04": por_duracion(OE1),
 "C05": {"2.3": .5, "2.4": .5}, "C06": {"2.2": 1.0}, "C07": por_duracion(OE3), "C09": por_duracion(LAB),
}
def repartir(total, shares):
    """Reparte un total entero según proporciones; el residuo va a la mayor participación (suma exacta)."""
    ks = list(shares); out = {k: int(round(total * shares[k])) for k in ks}
    dif = total - sum(out.values())
    kmax = max(ks, key=lambda k: shares[k]); out[kmax] += dif
    return out
for r in BUD:
    assert abs(sum(ALLOC[r["id"]].values()) - 1) < 1e-9, r["id"]
    r["por_act"] = repartir(r["total"], ALLOC[r["id"]])
for r in CONTRA:
    assert abs(sum(CALLOC[r["id"]].values()) - 1) < 1e-9, r["id"]
    r["por_act"] = repartir(r["total"], CALLOC[r["id"]])
# ------------------------------------------------------------------ PRESUPUESTO APROBADO v5 (Anexo 3 v5: fuente única desde el 29 de octubre de 2026)
# Cada partida se asigna completa a su actividad principal, como en la hoja «Cronograma financiero» del Anexo 3 v5.
import v5 as _v5
_P5 = _v5.partidas()
_FUENTE = {"IES": "IES", "MAN": "MAN", "CAL": "CAL", "AVA": "AVA", "GMA": "GMA"}
BUD = []
CONTRA = []
for p in _P5:
    base = dict(id=p["id"], concepto=p["concepto"], unidad=p["unidad"], cant=p["cant"], vunit=p["vunit"], m_ini=p["m_ini"], m_fin=p["m_fin"],
                rubro_tdr=p["rubro_tdr"], act=p["act"], texto=p["texto"], resp=p["resp"], nat="ANEXO 3 v7", wp=None, just="")
    if p["sgr"]:
        r = dict(base, total=p["sgr"], fuente="SGR", rubro=p["rubro_tdr"]); r["por_act"] = {p["act"]: p["sgr"]}; BUD.append(r)
    for k, v in p["contra"].items():
        if p["id"] in _v5.SIN_APORTANTE: continue      # aportes de DreamGIS: sin aportante desde el 29 de octubre de 2026
        ent, modo = k.split("_")
        r = dict(base, total=v, fuente=_FUENTE[ent], rubro=("Efectivo" if modo == "EF" else "Especie"), unidad="aporte", cant=1, vunit=v)
        r["por_act"] = {p["act"]: v}; CONTRA.append(r)
assert sum(r["total"] for r in BUD) == 13_999_405_215 and sum(r["total"] for r in CONTRA) == 1_774_000_000
# partidas del laboratorio de modelación predictiva de demolición en el Anexo 3 v5
LAB_IDS = ["TH-23", "TH-24", "TH-25", "EQ-17", "EQ-18", "EQ-19", "EQ-20", "EQ-21", "ST-08", "ST-09", "ST-10", "ST-11", "CA-04", "MA-07", "VI-06", "VI-07", "VI-08", "PD-06"]
LAB_LINEAS = [r for r in BUD if r["id"] in LAB_IDS]
ajuste("AJ-11", "Presupuesto, alianza y territorio del Anexo 3 v5", "SGR de 10.022.840.000 COP, cuatro integrantes y doce municipios en tres departamentos",
       "SGR de 13.999.405.215 COP, cinco integrantes y dos municipios (Manizales y Calarcá) en dos departamentos",
       "Cambios aprobados por la alianza (Anexo 3 v7 del 30 de octubre de 2026, código SIGP 143329)")
for a in ACTD.values():
    a["sgr"] = sum(r["por_act"].get(a["id"], 0) for r in BUD)
    a["contra"] = sum(r["por_act"].get(a["id"], 0) for r in CONTRA)
    a["total"] = a["sgr"] + a["contra"]

# ------------------------------------------------------------------ TOTALES Y CONTROLES
def total(rows): return sum(r["total"] for r in rows)
SGR = total(BUD); CON = total(CONTRA); TOTAL = SGR + CON
CON_EFECTIVO = sum(r["total"] for r in CONTRA if r["rubro"] == "Efectivo")
POR_RUBRO = collections.OrderedDict((k, sum(r["total"] for r in BUD if r["rubro_tdr"] == k)) for k in RUB)
assert sum(POR_RUBRO.values()) == SGR
assert sum(a["sgr"] for a in ACTD.values()) == SGR and sum(a["contra"] for a in ACTD.values()) == CON
POR_OE = {oe: dict(sgr=sum(a["sgr"] for a in ACTD.values() if a["oe"] == oe), contra=sum(a["contra"] for a in ACTD.values() if a["oe"] == oe)) for oe in ("OE1", "OE2", "OE3")}
TRANSFER = sum(r["total"] for r in BUD if r["id"] in ("CA-01", "PD-02", "PD-04", "CA-04", "PD-06"))
MOVILIDAD = sum(r["total"] for r in BUD if r["id"] == "VI-04")
assert TRANSFER >= 0.01 * TOTAL, (TRANSFER, TOTAL)
assert MOVILIDAD <= 0.02 * SGR
assert SGR <= IDENT["tope_cop"]

def cop(n): return "$ " + f"{int(round(n)):,}".replace(",", ".")
def pct(x, d=1): return f"{x * 100:.{d}f}".replace(".", ",") + " %"
def mm(n, d=1):
    s = f"{n / M:,.{d}f}"; return s.replace(",", "X").replace(".", ",").replace("X", ".")

# flujo semestral SGR
def flujo(rows, months=24):
    f = [0.0] * months
    for r in rows:
        if r["id"] in ("E01", "E02", "E04", "E05", "M03", "S11"):
            # compras por tramo en el mes de compra
            continue
        n = r["m_fin"] - r["m_ini"] + 1
        for m in range(r["m_ini"], r["m_fin"] + 1): f[m - 1] += r["total"] / n
    for r in rows:
        if r["id"] in ("E01", "E02", "E04", "E05", "M03", "S11"):
            sh = {"E01": ("compra_nodos", r["vunit"]), "E02": ("compra_cabezales", r["vunit"]), "E04": ("compra_gw", r["vunit"]),
                  "E05": ("compra_nodos", r["vunit"]), "M03": ("compra_nodos", r["vunit"])}
            for t in M0.TRAMOS:
                mes = t["mes_compra"]
                if r["id"] in sh: f[mes - 1] += t[sh[r["id"]][0]] * sh[r["id"]][1]
                else: f[mes - 1] += r["total"] / 3  # S11 importación: un tercio por lote
    return f
_MENS = _v5.mensual_por_item()
FLUJO_SGR = [sum(_MENS[r["concepto"]][i] for r in BUD) for i in range(24)]
FLUJO_CON = [sum(_MENS[r["concepto"]][i] for r in CONTRA) for i in range(24)]
assert abs(sum(FLUJO_SGR) - SGR) < 1, (sum(FLUJO_SGR), SGR)
assert abs(sum(FLUJO_CON) - CON) < 1, (sum(FLUJO_CON), CON)
def por_periodo(f, size): return [sum(f[i:i + size]) for i in range(0, len(f), size)]
FLUJO_SEM = por_periodo(FLUJO_SGR, 6)
FLUJO_CON_SEM = por_periodo(FLUJO_CON, 6)

# ------------------------------------------------------------------ RIESGOS v2 (tipos del formato del Anexo 2)
def nivel_prob(p): return "Probable" if p >= 40 else ("Improbable" if p >= 20 else "Raro")
def nivel_imp(i): return "Mayor" if i >= 4 else ("Moderado" if i == 3 else "Menor")
TIPO = {"Técnico": "Operacionales", "Organizacional": "Operacionales", "Externo": "Operacionales", "Financiero": "Financieros",
        "Jurídico": "Legales", "Datos": "Operacionales"}
RIESGOS = []
for (id_, cat, desc, causa, P, I, prob, imp, est, resp, own, trig) in M0.RIESGOS:
    tipo = TIPO[cat]
    if id_ == "R-FIN-01": tipo = "De costos"
    RIESGOS.append(dict(id=id_, cat=cat, tipo=tipo, desc=desc, P=P, I=I, prob=prob, imp=imp, estrategia=est, respuesta=resp, resp=own, disparador=trig,
                        n_prob=nivel_prob(prob), n_imp=nivel_imp(I)))
RIESGOS_NUEVOS = [
 dict(id="R-ADM-01", cat="Administrativo", tipo="Administrativos", desc="La contratación del equipo y la firma de los convenios de ejecución se demoran más de ocho semanas.",
      P=3, I=4, prob=30, imp=0, estrategia="Mitigar", respuesta="Convenio marco previo entre la universidad, los municipios y Avanciencia, plan de contratación con lista de elegibles y seguimiento semanal de la gerencia.",
      resp="Gerencia de proyecto", disparador="Equipo sin contratar al finalizar la semana 8", n_prob="Improbable", n_imp="Mayor"),
 dict(id="R-CAL-01", cat="Calendario", tipo="De calendario", desc="La entrega en Colombia de un lote de equipos importados por el proveedor excede doce semanas.",
      P=3, I=4, prob=35, imp=0, estrategia="Mitigar", respuesta="Orden anticipada por lote, entrega en Colombia incluida en el precio cotizado, plazo pactado en la orden de compra y lote de reserva de cabezales en el país.",
      resp="Gerencia de proyecto", disparador="Lote sin entregar a la semana 10 de su orden", n_prob="Improbable", n_imp="Mayor"),
 dict(id="R-SAN-01", cat="Sanitario", tipo="Sanitarios", desc="El personal de campo se expone al polvo y a los escombros durante la instalación y el mantenimiento.",
      P=3, I=3, prob=30, imp=0, estrategia="Mitigar", respuesta="Protocolo de seguridad y salud con respiradores N95, inducción previa y ventanas de trabajo fuera de la remoción activa.",
      resp="Ingenieros IoT y de campo", disparador="Incidente de salud reportado o sitio sin protocolo firmado", n_prob="Improbable", n_imp="Moderado"),
 dict(id="R-MOD-01", cat="Externo", tipo="Operacionales", desc="Los propietarios o las autoridades no permiten medir en un número suficiente de demoliciones o remociones reales entre los meses 13 y 22.",
      P=4, I=4, prob=40, imp=0, estrategia="Mitigar", respuesta="Acuerdo con comités y municipios para anunciar cada demolición con 15 días de antelación, uso de remociones de menor escala y de sitios de prueba como respaldo, y regla mínima de seis eventos válidos en nueve campañas.",
      resp="Municipio aliado y líder del laboratorio", disparador="Menos de tres campañas ejecutadas al mes 16", n_prob="Probable", n_imp="Mayor"),
 dict(id="R-MOD-02", cat="Técnico", tipo="Operacionales", desc="El gemelo predictivo no alcanza el desempeño fijado (FAC2 ≥ 0,5 y sesgo fraccional absoluto ≤ 0,3 en promedios de 24 horas).",
      P=3, I=4, prob=35, imp=0, estrategia="Mitigar", respuesta="Calibración por etapas con la campaña piloto, comparación del modelo sustituto con el modelo físico, verificación independiente y restricción del uso del resultado al dominio validado, con el desempeño real informado.",
      resp="Investigador líder en modelación", disparador="Desempeño por debajo de la meta en los tres primeros eventos de validación", n_prob="Improbable", n_imp="Mayor"),
 dict(id="R-MOD-03", cat="Datos", tipo="Operacionales", desc="Los datos de entrada del modelo (geometría, material, método de demolición o meteorología) faltan o son de baja calidad.",
      P=3, I=3, prob=30, imp=0, estrategia="Mitigar", respuesta="Levantamiento con dron antes de cada evento, cuatro estaciones meteorológicas propias, inventario de emisión expresado en rangos y resultados presentados como escenarios.",
      resp="Ingeniero en demolición y control de polvo", disparador="Evento sin geometría o sin viento medido", n_prob="Improbable", n_imp="Moderado"),
 dict(id="R-JUR-02", cat="Jurídico", tipo="Legales", desc="El resultado del laboratorio se interpreta como autorización de demolición, licencia o prueba de responsabilidad.",
      P=3, I=4, prob=25, imp=0, estrategia="Evitar", respuesta="El protocolo define el resultado como estimación de apoyo a la decisión, con advertencia expresa de alcance, convenio de uso con el municipio y revisión jurídica previa a la adopción.",
      resp="Gerencia de proyecto y municipio aliado", disparador="Solicitud de usar el informe como requisito o como prueba", n_prob="Improbable", n_imp="Mayor"),
]
RIESGOS += RIESGOS_NUEVOS
# riesgos que cambian por los ajustes de los TdR
for r in RIESGOS:
    if r["id"] == "R-TEC-04": r["resp"] = "Analista de datos espaciales y gemelo digital"
    if r["id"] == "R-FIN-01":
        r["respuesta"] = "Compra por tramo con cotizaciones vigentes, orden de compra anticipada y cobertura cambiaria del proveedor; la contrapartida en efectivo cubre variaciones menores."
    if r["id"] == "R-EXT-02":
        r["estrategia"] = "Mitigar"
        r["respuesta"] = "Cerramientos y mástiles protegidos, custodia local por sitio, 20 nodos y 1 gateway de reserva y convenio de custodia con el municipio aliado."
    if r["id"] == "R-EXT-01":
        r["respuesta"] = "Instalación en ventanas secas, técnicos locales y holgura en las actividades 1.1, 3.1, 3.2 y 3.3; las instalaciones de los tramos 2 y 3 se programan con acceso previamente verificado."

# ------------------------------------------------------------------ TALENTO HUMANO (numeral 9)
TALENTO = [
 dict(cat="Joven investigador e innovador (pregrado)", n=6, dur=12, mensual=2_000_000, total=6 * 12 * 2_000_000, linea="TH-01 y TH-02",
      cohortes="Cohorte A: meses 1 a 12 (3 personas). Cohorte B: meses 13 a 24 (3 personas).",
      productos="Un artículo en formato publicable en revista A1, A2, B o C de Publindex y un producto de divulgación pública de la ciencia por persona."),
 dict(cat="Estudiante de maestría en modalidad de investigación", n=2, dur=24, mensual=4_350_000, total=2 * (24 * 4_350_000 + 48_000_000), linea="TH-03 y TH-04",
      cohortes="Dos personas, meses 1 a 24; matrícula hasta 48.000.000 COP por persona.",
      productos="Un producto tipo TOP o tipo A sometido o publicado y un producto de divulgación pública de la ciencia por persona."),
 dict(cat="Doctor en estancia posdoctoral", n=1, dur=24, mensual=12_920_000, total=24 * 12_920_000, linea="TH-05",
      cohortes="Una persona, meses 1 a 24, sin vínculo laboral con las entidades de la alianza.",
      productos="Un producto tipo TOP o tipo A, un producto de divulgación pública de la ciencia y un informe técnico final."),
]
assert sum(t["total"] for t in TALENTO) == sum(r["total"] for r in BUD if r["id"] in ("TH-01", "TH-02", "TH-03", "TH-04", "TH-05"))

# ------------------------------------------------------------------ PRODUCTOS (MGA, sector 39, programa 3906)
PRODUCTOS = [
 dict(n=1, oe="OE1", programa="3906", producto="Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos",
      medido="Prototipos validados en condiciones reales", indicador="Prototipos funcionales validados (red de nodos y gateways con modelo de corrección y gemelo predictivo de demolición)", unidad="Número", meta="2 prototipos: sistema de 100 nodos y 10 gateways y gemelo predictivo de demolición",
      act=["1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "2.3", "2.4", "2.7"], resp="IES ejecutora y empresa tecnológica"),
 dict(n=2, oe="OE1", programa="3906", producto="Documentos de investigación",
      medido="Documentos de investigación elaborados", indicador="Documentos de investigación elaborados (6 de jóvenes, 2 de maestría y 1 de posdoctorado)", unidad="Número", meta="9",
      act=["1.6", "3.4"], resp="IES ejecutora"),
 dict(n=3, oe="OE1", programa="3906", producto="Servicio de apoyo financiero para la formación de maestría ya sea nacional o en el exterior, en la modalidad de investigación",
      medido="Personas apoyadas con formación de maestría", indicador="Estudiantes de maestría en modalidad de investigación apoyados", unidad="Número", meta="2",
      act=["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"], resp="IES ejecutora"),
 dict(n=4, oe="OE1", programa="3906", producto="Servicio de apoyo financiero de estancias de investigación",
      medido="Estancias de investigación apoyadas", indicador="Doctores con estancia posdoctoral apoyados", unidad="Número", meta="1",
      act=["1.3", "1.4", "1.6"], resp="IES ejecutora"),
 dict(n=5, oe="OE1", programa="3906", producto="Servicio de apoyo financiero para el fortalecimiento de las vocaciones científicas en CTI",
      medido="Jóvenes investigadores e innovadores apoyados", indicador="Jóvenes investigadores e innovadores apoyados con beca-pasantía", unidad="Número", meta="6",
      act=["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"], resp="IES ejecutora"),
 dict(n=6, oe="OE2", programa="3906", producto="Servicio de apoyo financiero para programas y proyectos de infraestructura científica y tecnológica",
      medido="Infraestructura científica y tecnológica dotada", indicador="Equipos y plataformas de medición y de modelación dotados y en operación (3 referencias, 100 nodos, 10 gateways, plataforma y laboratorio de modelación)", unidad="Número", meta="1 infraestructura integrada",
      act=["2.1", "2.2", "2.3", "2.4", "2.5", "2.6"], resp="IES ejecutora y empresa tecnológica"),
 dict(n=7, oe="OE3", programa="3906", producto="Documentos de política: Documentos de planeación",
      medido="Documentos de planeación elaborados", indicador="Documentos de planeación elaborados (protocolo de alerta, plan de sostenibilidad con convenios de custodia y protocolo de evaluación previa de demolición)", unidad="Número", meta="3",
      act=["3.1", "3.3", "3.4", "3.5"], resp="IES ejecutora y municipio aliado"),
 dict(n=8, oe="OE3", programa="3906", producto="Servicio de apropiación social del conocimiento",
      medido="Actividades de apropiación social realizadas", indicador="Estrategias y actividades de apropiación social del conocimiento realizadas (20 talleres de co-diseño y 9 jornadas)", unidad="Número", meta="29",
      act=["3.1", "3.2", "3.3", "3.4"], resp="IES ejecutora y municipio aliado"),
 dict(n=9, oe="OE3", programa="3906", producto="Servicio de Asistencia Técnica",
      medido="Personas y entidades asistidas técnicamente", indicador="Personas de comités y custodios certificadas en el uso y la custodia de la red", unidad="Número", meta="60 personas y 15 comités",
      act=["3.2", "3.3", "3.4"], resp="IES ejecutora y empresa tecnológica"),
]
for p in PRODUCTOS:
    p["sgr"] = sum(ACTD[k]["sgr"] for k in p["act"]); p["contra"] = sum(ACTD[k]["contra"] for k in p["act"])

# ------------------------------------------------------------------ HITOS
HITOS = [dict(id=h[0], desc=h[1], mes=h[2], verif=h[3]) for h in M0.HITOS]
HITOS += [
    dict(id="H9", desc="Laboratorio de modelación dotado y con la cadena de cálculo en operación", mes=11,
         verif="Actas de recibo del servidor, las estaciones meteorológicas, el dron y los monitores portátiles; ejecución de un caso de prueba documentado"),
    dict(id="H10", desc="Gemelo predictivo calibrado con el polvo del territorio y la campaña piloto", mes=17,
         verif="Informe de calibración con el inventario de emisión, la caracterización del polvo y las métricas frente a la campaña piloto"),
    dict(id="H11", desc="Validación del gemelo con seis eventos reales y verificación independiente", mes=22,
         verif="Informe de validación con FAC2 y sesgo fraccional por evento e informe del verificador independiente"),
]
HITOS.sort(key=lambda h: (h["mes"], int(h["id"][1:])))
HITOS.append(dict(id="C3", desc="Compuerta C3: cierre y transferencia con evidencia del TRL 8", mes=24,
                  verif="Informe de evaluación final con el desempeño de los 100 nodos y acta de entrega a custodios"))

# ------------------------------------------------------------------ INDICADORES DE GESTIÓN
INFORMES = [3, 6, 9, 12, 15, 18, 21, 24]

# ------------------------------------------------------------------ RESUMEN
def resumen():
    return dict(sgr=SGR, contra=CON, total=TOTAL, contra_efectivo=CON_EFECTIVO, pct_tope=SGR / IDENT["tope_cop"], holgura=IDENT["tope_cop"] - SGR,
                transfer=TRANSFER, pct_transfer=TRANSFER / TOTAL, movilidad=MOVILIDAD, pct_mov=MOVILIDAD / SGR, pct_efectivo=CON_EFECTIVO / SGR,
                por_rubro=POR_RUBRO, por_oe=POR_OE)

if __name__ == "__main__":
    r = resumen()
    print("SGR", cop(SGR), "| contrapartida", cop(CON), "(efectivo", cop(CON_EFECTIVO) + ") | total", cop(TOTAL))
    print("tope %", pct(r["pct_tope"], 2), "| holgura", cop(r["holgura"]), "| transferencia", cop(TRANSFER), pct(r["pct_transfer"], 2), "| movilidad", pct(r["pct_mov"], 2), "| efectivo/SGR", pct(r["pct_efectivo"], 2))
    for k, v in POR_RUBRO.items(): print(f"  {k:48s} {cop(v):>20s} {pct(v / SGR):>8s}")
    print("por OE", {k: (cop(v['sgr']), cop(v['contra'])) for k, v in POR_OE.items()})
    for a in ACTD.values(): print(a["id"], f"M{a['m_ini']}-M{a['m_fin']}", cop(a["sgr"]), cop(a["contra"]), "crit" if a["critica"] else "", a["nombre"][:60])
    print("flujo sem", [mm(x) for x in FLUJO_SEM], "contra", [mm(x) for x in FLUJO_CON_SEM])
    print("productos", [(p["n"], cop(p["sgr"])) for p in PRODUCTOS])
    print("riesgos", len(RIESGOS), [(x["id"], x["tipo"], x["n_prob"], x["n_imp"]) for x in RIESGOS])

# ------------------------------------------------------------------ INDICADORES DE PRODUCTO Y DE RESULTADO
IND_PROD = [
 dict(n=1, prod="Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos", ind="Prototipos funcionales validados", unidad="Número",
      meta="2 prototipos: un sistema de 100 nodos y 10 gateways (30 y 3 al mes 12; 70 y 7 al mes 17; 100 y 10 al mes 19) y un gemelo predictivo de demolición validado al mes 22", resp="IES ejecutora y empresa tecnológica", periodo="Meses 4 a 24",
      evidencia="Inventario con coordenadas y número de serie; informes de validación frente a la referencia (R² ≥ 0,70 y NRMSE ≤ 30 %); informe del ensayo independiente; informe de validación del gemelo con seis eventos y verificación independiente", territorio="12 municipios de Caldas, Cundinamarca y Valle del Cauca"),
 dict(n=2, prod="Documentos de investigación", ind="Documentos de investigación elaborados", unidad="Número",
      meta="9: seis de jóvenes investigadores, dos de maestría y uno de posdoctorado; al menos 2 sometidos a revistas Q1 o Q2", resp="IES ejecutora", periodo="Meses 6 a 24",
      evidencia="Manuscritos con constancia de sometimiento o publicación", territorio="Tres departamentos"),
 dict(n=3, prod="Servicio de apoyo financiero para la formación de maestría ya sea nacional o en el exterior, en la modalidad de investigación", ind="Estudiantes de maestría apoyados", unidad="Número",
      meta="2", resp="IES ejecutora", periodo="Meses 1 a 24", evidencia="Certificados de admisión o matrícula, avance del trabajo de grado y producto TOP o tipo A sometido", territorio="Tres departamentos"),
 dict(n=4, prod="Servicio de apoyo financiero de estancias de investigación", ind="Doctores con estancia posdoctoral apoyados", unidad="Número",
      meta="1", resp="IES ejecutora", periodo="Meses 1 a 24", evidencia="Contrato o beca, producto TOP o tipo A, producto de divulgación e informe técnico final", territorio="Tres departamentos"),
 dict(n=5, prod="Servicio de apoyo financiero para el fortalecimiento de las vocaciones científicas en CTI", ind="Jóvenes investigadores e innovadores apoyados", unidad="Número",
      meta="6: tres en los meses 1 a 12 y tres en los meses 13 a 24", resp="IES ejecutora", periodo="Meses 1 a 24", evidencia="Contratos de beca-pasantía, CvLAC actualizado, artículo en formato publicable y producto de divulgación por persona", territorio="Tres departamentos"),
 dict(n=6, prod="Servicio de apoyo financiero para programas y proyectos de infraestructura científica y tecnológica", ind="Infraestructura de medición y de modelación dotada y en operación", unidad="Número",
      meta="1 infraestructura integrada: 3 monitores de referencia, banco de calibración, 100 nodos, 10 gateways, plataforma y laboratorio de modelación", resp="IES ejecutora y empresa tecnológica", periodo="Meses 2 a 19",
      evidencia="Actas de recibo, inventario con huella de configuración y registro fotográfico; acta de puesta en operación del laboratorio", territorio="12 municipios y laboratorio en la entidad proponente"),
 dict(n=7, prod="Documentos de política: Documentos de planeación", ind="Documentos de planeación elaborados", unidad="Número",
      meta="3: protocolo de alerta co-diseñado con los comités, plan de sostenibilidad con convenios de custodia y protocolo de evaluación previa de demolición", resp="IES ejecutora y municipio aliado", periodo="Meses 3 a 24",
      evidencia="Documentos adoptados por acta de cada comité y convenios de custodia firmados; protocolo de evaluación previa adoptado por acta de la entidad territorial", territorio="15 comités de gestión del riesgo"),
 dict(n=8, prod="Servicio de apropiación social del conocimiento", ind="Actividades de apropiación social del conocimiento realizadas", unidad="Número",
      meta="29: 20 talleres de co-diseño y 9 jornadas públicas", resp="IES ejecutora y municipio aliado", periodo="Meses 3 a 24", evidencia="Actas, listas de asistencia y piezas producidas con las comunidades", territorio="12 municipios"),
 dict(n=9, prod="Servicio de Asistencia Técnica", ind="Personas certificadas y comités asistidos", unidad="Número",
      meta="60 personas certificadas y 15 comités asistidos", resp="IES ejecutora y empresa tecnológica", periodo="Meses 6 a 24", evidencia="Certificados de formación y actas de asistencia técnica", territorio="15 comités de gestión del riesgo"),
]
IND_RES = [
 # R6 y R7 se anexan al final de la lista de resultados, antes de los indicadores de impacto

 dict(cod="R1", nombre="Error de medición frente a la referencia en los tres tramos", formula="NRMSE y R² de cada nodo corregido frente al monitor de referencia colocalizado", lb="Se mide en el tramo 1 (mes 12)", meta="R² ≥ 0,70 y NRMSE ≤ 30 % en 100 nodos al mes 24", nivel="Resultado"),
 dict(cod="R2", nombre="Disponibilidad mensual de nodos", formula="Horas con dato válido ÷ horas del mes", lb="0 %", meta="≥ 90 % y pérdida de paquetes ≤ 10 % al mes 24", nivel="Resultado"),
 dict(cod="R3", nombre="Uso institucional del tablero y del protocolo", formula="Comités con al menos una decisión documentada por trimestre ÷ comités focalizados × 100", lb="Sin uso documentado", meta="≥ 75 % al mes 24", nivel="Resultado"),
 dict(cod="R4", nombre="Reducción relativa de falsas alarmas", formula="1 − (tasa del periodo ÷ tasa medida en el tramo 1)", lb="Se mide en el tramo 1", meta="≥ 30 % de reducción relativa", nivel="Resultado"),
 dict(cod="R5", nombre="Capacidad instalada en custodios", formula="Personas certificadas en el uso y la custodia de la red", lb="0", meta="≥ 60 personas certificadas", nivel="Resultado"),
 dict(cod="R6", nombre="Desempeño del gemelo predictivo frente a mediciones en demoliciones reales", formula="Fracción de pares estimado y medido con razón entre 0,5 y 2 (FAC2) y sesgo fraccional, en promedios de 24 horas, por evento", lb="Sin modelo predictivo", meta="FAC2 ≥ 0,5 y sesgo fraccional absoluto ≤ 0,3 en al menos 6 eventos al mes 22", nivel="Resultado"),
 dict(cod="R7", nombre="Evaluaciones previas de demolición entregadas", formula="Informes de evaluación previa entregados a las entidades territoriales o a los responsables de obra", lb="0", meta="≥ 12 informes, con al menos 3 por departamento, al mes 24", nivel="Resultado"),
 dict(cod="I1", nombre="Activación del protocolo ante superación de umbral", formula="Activaciones documentadas ÷ superaciones de umbral × 100", lb="Sin protocolo", meta="≥ 80 % a los 12 meses posteriores al cierre", nivel="Impacto"),
 dict(cod="I2", nombre="Continuidad de la red bajo custodia", formula="Nodos operativos bajo custodia ÷ nodos entregados × 100", lb="0", meta="≥ 70 % a los 12 meses posteriores al cierre", nivel="Impacto"),
]

# ------------------------------------------------------------------ AJUSTE v5: territorio (Manizales y Calarcá), alianza de cinco integrantes y referencia rotativa
_REPL = [
 ("IES ejecutora y empresa tecnológica", "Universidad Santo Tomás"),
 ("IES ejecutora y municipio aliado", "Universidad Santo Tomás y municipios de Manizales y de Calarcá"),
 ("IES ejecutora", "Universidad Santo Tomás"),
 ("12 municipios y laboratorio en la entidad proponente", "Manizales y Calarcá; laboratorio en uno de los dos municipios"),
 ("15 comités de gestión del riesgo", "4 consejos de gestión del riesgo"),
 ("12 municipios de Caldas, Cundinamarca y Valle del Cauca", "Manizales (Caldas) y Calarcá (Quindío)"), ("Caldas, Cundinamarca y Valle del Cauca", "Manizales (Caldas) y Calarcá (Quindío)"),
 ("Tres departamentos", "Manizales y Calarcá"), ("tres departamentos", "dos municipios"), ("12 municipios", "Manizales y Calarcá"),
 ("3 monitores de referencia", "1 conjunto de referencia rotativo"), ("3 referencias, ", "1 conjunto de referencia rotativo, "),
 ("60 personas certificadas y 15 comités asistidos", "60 personas certificadas y 4 consejos asistidos"),
 ("60 personas y 15 comités", "60 personas y 4 consejos"),
 ("con al menos 3 por departamento", "con al menos 3 por municipio"),
 ("convenio de custodia con el municipio aliado", "convenios de custodia con los municipios aliados"),
 ("Municipio aliado y líder del laboratorio", "Municipios aliados y líder del laboratorio"),
 ("Gerencia de proyecto y municipio aliado", "Gerencia de proyecto y municipios aliados"),
 ("convenio de uso con el municipio", "convenio de uso con cada municipio"),
 ("Validación cruzada por departamento", "Validación cruzada por municipio"), ("no generaliza entre departamentos", "no generaliza entre municipios"),
 ("Certificación de la IES y de la empresa antes del acta de inicio.", "Certificación de cada integrante en el Anexo 1, antes de radicar."),
 ("Convenio marco previo con la IES y la empresa", "Convenio marco previo entre la universidad y los demás integrantes"),
 ("comités", "consejos"), ("Comités", "Consejos"), ("comité", "consejo"),
]
def _norm(s):
    if not isinstance(s, str): return s
    for a, b in _REPL: s = s.replace(a, b)
    return s
for _col in (PRODUCTOS, IND_PROD, IND_RES, HITOS, RIESGOS):
    for _d in _col:
        for _k in list(_d):
            if _k not in ("id", "cod", "n"): _d[_k] = _norm(_d[_k])
RIESGOS += [
 dict(id="R-REF-01", cat="Técnico", tipo="Operacionales", desc="El conjunto de referencia es único y rota entre los dos municipios, de modo que cada municipio tiene menos tiempo de colocalización.",
      P=3, I=4, prob=30, imp=0, estrategia="Mitigar", respuesta="Calendario de rotación con una ventana mínima por municipio en cada tramo, caracterización previa de cada lote en el banco de calibración y contraste en campo con los monitores portátiles de referencia equivalente.",
      resp="Especialista en metrología y calibración", disparador="Ventana de colocalización menor que la mínima en un municipio", n_prob="Improbable", n_imp="Mayor"),
 dict(id="R-PRO-01", cat="Financiero", tipo="De costos", desc="Las cotizaciones seleccionadas de nodos, banco de calibración y conjunto de referencia dependen de un proveedor por bien y pueden variar o no mantenerse.",
      P=3, I=4, prob=30, imp=0, estrategia="Mitigar", respuesta="Dos cotizaciones comparables por bien al radicar, especificación funcional abierta, compra por tramo y tasa de cambio presupuestal de 4.000 COP por dólar en el Anexo 3.",
      resp="Gerencia de proyecto", disparador="Variación mayor de 10 % entre la cotización y la orden de compra", n_prob="Improbable", n_imp="Mayor"),
]
