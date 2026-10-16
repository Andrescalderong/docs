# -*- coding: utf-8 -*-
"""LIBRO MAESTRO DE DATOS del proyecto (fuente única de cifras cardinales, H36-03 / MCC36).
Todo capítulo, tabla y figura debe leer de aquí. Naturaleza NTC 1.1 por línea.
Valores monetarios en pesos colombianos (enteros)."""
import json, math, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ IDENTIDAD (claves maestras)
IDENT = {
    "caso": "SGR_CONV56_AIRE",
    "titulo": ("Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión "
               "anticipada del riesgo por material particulado posterremoto"),
    "titulo_corto": "Red IoT híbrida y gemelo digital para material particulado posterremoto",
    "convocatoria": "Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)",
    "financiador": "Sistema General de Regalías (SGR) / Ministerio de Ciencia, Tecnología e Innovación (MinCiencias)",
    "tipologia": "Investigación aplicada, desarrollo tecnológico e innovación",
    "ocde": "1.2 Ingeniería eléctrica, electrónica e informática",
    "territorio": "Departamentos de Caldas, Cundinamarca y Valle del Cauca",
    "fecha_corte": "13 de octubre de 2026",
    "fecha_limite": "3 de noviembre de 2026",
    "hora_limite": "4:00 p. m.",
    "tope_cop": 14_000_000_000,
    "duracion_meses": 24,
    "horizonte_posproyecto_meses": 12,
    "trl_inicial": 4,
    "trl_final": 7,
    "nodos": 100,
    "nodos_comprados": 120,
    "gateways": 10,
    "gateways_comprados": 11,
    "referencias": 3,
    "hash_maestro": "685a73f45ba1d3011a3b1ba3a1722482c46d8b9a68ffe5cbc4dbe131e4603ba8",
    "metaprompt": "GENESIS-CTeI 36.10 RC2 (VM-PAR3-MDR3-CONT1)",
    "ntc": "NTC 1.1",
}

# ------------------------------------------------------------------ TRAMOS (despliegue condicionado, estrategia R4 de 4.4-MDR)
TRAMOS = [
    {"id": 1, "nombre": "Tramo 1: piloto de contraste", "m_ini": 1, "m_fin": 12, "nodos": 30, "gateways": 3,
     "compra_nodos": 36, "compra_gw": 4, "compra_cabezales": 50, "compuerta": "C1", "mes_compuerta": 12, "mes_compra": 5},
    {"id": 2, "nombre": "Tramo 2: ampliación condicionada", "m_ini": 13, "m_fin": 17, "nodos": 40, "gateways": 4,
     "compra_nodos": 48, "compra_gw": 4, "compra_cabezales": 50, "compuerta": "C2", "mes_compuerta": 17, "mes_compra": 13},
    {"id": 3, "nombre": "Tramo 3: consolidación y transferencia", "m_ini": 18, "m_fin": 24, "nodos": 30, "gateways": 3,
     "compra_nodos": 36, "compra_gw": 3, "compra_cabezales": 50, "compuerta": "C3", "mes_compuerta": 24, "mes_compra": 18},
]
assert sum(t["nodos"] for t in TRAMOS) == IDENT["nodos"]
assert sum(t["gateways"] for t in TRAMOS) == IDENT["gateways"]
assert sum(t["compra_nodos"] for t in TRAMOS) == IDENT["nodos_comprados"]
assert sum(t["compra_gw"] for t in TRAMOS) == IDENT["gateways_comprados"]

# ------------------------------------------------------------------ OBJETIVOS
OG = ("Reducir el error de medición de material particulado de una red de 100 nodos de bajo costo, y asegurar su uso "
      "institucional en la gestión del riesgo, mediante calibración dinámica en gateways, operación con energía y enlace "
      "redundantes y custodia distribuida por tramos, en Caldas, Cundinamarca y Valle del Cauca, durante 24 meses.")
OE = [
    {"id": "OE1", "causa": "V06 (crítica), V02 (crítica), V03 (activa)", "sc": "SC-1",
     "texto": ("Corregir la interferencia de humedad y de fracción gruesa en las mediciones de PM2,5 y PM10 mediante "
               "colocalización con equipos de referencia y un modelo de corrección aplicado en gateways, hasta cumplir "
               "los umbrales de desempeño fijados en el piloto del tramo 1 y verificados al mes 24."),
     "meta": "R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia en los tres tramos"},
    {"id": "OE2", "causa": "V05 (activa) → V09 (reactiva)", "sc": "SC-2",
     "texto": ("Mantener la disponibilidad de 100 nodos y 10 gateways ante polvo, humedad y fallas de energía y de enlace, "
               "mediante autonomía mínima de 14 días sin sol y un enlace alterno con almacenamiento local de 7 días."),
     "meta": "Disponibilidad mensual de nodos ≥ 90 % y pérdida de paquetes ≤ 10 %"},
    {"id": "OE3", "causa": "V15 (crítica)", "sc": "SC-3 y SC-4",
     "texto": ("Lograr el uso del tablero y del protocolo de alerta por los comités de gestión del riesgo, con umbrales "
               "validados localmente y custodia por componente, mediante co-diseño, formación y convenios por tramo."),
     "meta": "≥ 75 % de los comités focalizados usan el tablero en decisiones documentadas al mes 24"},
]

# ------------------------------------------------------------------ PRESUPUESTO
M = 1_000_000
def L(id, rubro, concepto, unidad, cant, vunit, fuente, nat, wbs, m_ini, m_fin, just, ref=""):
    return dict(id=id, rubro=rubro, concepto=concepto, unidad=unidad, cant=cant, vunit=int(vunit),
                total=int(round(cant * vunit)), fuente=fuente, nat=nat, wbs=wbs, m_ini=m_ini, m_fin=m_fin,
                just=just, ref=ref)

R_PERS, R_EQ, R_MAT, R_SERV, R_VIAJ, R_OTR, R_RES = (
    "Personal", "Equipos y software", "Materiales e insumos", "Servicios técnicos",
    "Viajes y viáticos", "Otros rubros", "Reserva de contingencia")

BUDGET = [
    # --- Personal SGR (E3 = valores heredados del expediente revisado)
    L("P01", R_PERS, "Jóvenes investigadores (6)", "persona-mes", 72, 2.0 * M, "SGR", "DECLARADO", "WP1", 1, 12, "Requisito de formación de talento; valor del expediente E3 (Tabla 8.2)."),
    L("P02", R_PERS, "Estudiantes de maestría (2)", "persona-mes", 48, 6.35 * M, "SGR", "DECLARADO", "WP1", 1, 24, "Sostenimiento y matrícula; valor del expediente E3."),
    L("P03", R_PERS, "Doctor en estancia posdoctoral con perfil de ciencia de datos (1)", "persona-mes", 24, 12.92 * M, "SGR", "PROPUESTO", "WP1", 1, 24, "Perfil exigido por el numeral 9 de los TdR; apoyo mensual fijado en el numeral 14.4; modelo de corrección y validación."),
    L("P04", R_PERS, "Ingenieros IoT y de campo (3)", "persona-mes", 72, 9.0 * M, "SGR", "DECLARADO", "WP2", 1, 24, "Instalación y operación de la red; valor E3."),
    L("P05", R_PERS, "Coordinación de apropiación social (1)", "persona-mes", 24, 8.0 * M, "SGR", "DECLARADO", "WP3", 1, 24, "Escalera ASC niveles 1 a 4; valor E3."),
    L("P06", R_PERS, "Gerencia de proyecto (1)", "persona-mes", 24, 10.0 * M, "SGR", "DECLARADO", "WP0", 1, 24, "Seguimiento físico y financiero; valor E3."),
    L("P07", R_PERS, "Especialista en metrología y calibración (1)", "persona-mes", 24, 12.0 * M, "SGR", "PROPUESTO", "WP1", 1, 24, "Responsable de la trazabilidad frente a la referencia gravimétrica."),
    L("P08", R_PERS, "Ingenieros de software y nube (2)", "persona-mes", 48, 9.5 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Plataforma, gemelo digital y tablero."),
    L("P09", R_PERS, "Ingeniero de firmware y energía (1)", "persona-mes", 24, 9.0 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Autonomía de 14 días y modo de bajo consumo."),
    L("P10", R_PERS, "Técnicos de campo departamentales (6)", "persona-mes", 144, 4.5 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Dos por departamento; mantenimiento y reposición."),
    L("P11", R_PERS, "Profesionales de apropiación social (2)", "persona-mes", 48, 6.0 * M, "SGR", "PROPUESTO", "WP3", 1, 24, "Co-diseño con comités y comunidades."),
    L("P12", R_PERS, "Analista de datos espaciales y gemelo digital (1)", "persona-mes", 24, 10.0 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Modelo de estimación espacial y validación."),
    L("P13", R_PERS, "Profesional en calidad del aire y salud ambiental (1)", "persona-mes", 24, 10.0 * M, "SGR", "PROPUESTO", "WP3", 1, 24, "Umbrales locales del índice y protocolo de alerta."),
    L("P14", R_PERS, "Profesional de convenios y custodia (1)", "persona-mes", 24, 7.0 * M, "SGR", "PROPUESTO", "WP3", 1, 24, "Convenios por tramo, cláusula de apertura y propiedad intelectual."),
    # --- Equipos y software
    L("E01", R_EQ, "Nodos IoT de medición (100 + 20 de reserva)", "unidad", 120, 4.5 * M, "SGR", "DECLARADO", "WP2", 1, 24, "Compra por tramo: 36, 48 y 36 unidades; valor E3."),
    L("E02", R_EQ, "Cabezales ópticos de partículas", "unidad", 150, 1.2 * M, "SGR", "DECLARADO", "WP2", 1, 24, "Reposición por desgaste higroscópico; valor E3."),
    L("E03", R_EQ, "Monitores gravimétricos de referencia", "unidad", 3, 85.0 * M, "SGR", "DECLARADO", "WP1", 4, 6, "Uno por departamento para colocalización; valor E3."),
    L("E04", R_EQ, "Gateways con energía solar y respaldo (10 + 1 de reserva)", "unidad", 11, 28.0 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Aplican el modelo de corrección; compra por tramo: 4, 4 y 3."),
    L("E05", R_EQ, "Kits de energía solar y batería para nodos", "unidad", 120, 0.65 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Autonomía de 14 días sin sol."),
    L("E06", R_EQ, "Módulos de enlace satelital de respaldo", "unidad", 10, 3.5 * M, "SGR", "PROPUESTO", "WP2", 3, 24, "Enlace alterno ante falla celular."),
    L("E07", R_EQ, "Banco de calibración de laboratorio (cámara de humedad y generador de aerosol)", "unidad", 1, 150.0 * M, "SGR", "PROPUESTO", "WP1", 3, 5, "Caracterización previa de cada lote de cabezales."),
    L("E08", R_EQ, "Estaciones de trabajo para entrenamiento de modelos", "unidad", 2, 25.0 * M, "SGR", "PROPUESTO", "WP1", 1, 3, "Entrenamiento y validación del modelo de corrección."),
    L("E09", R_EQ, "Equipos de campo e instrumentación (lote)", "lote", 1, 30.0 * M, "SGR", "PROPUESTO", "WP2", 1, 3, "Herramientas, medidores y repuestos de uso general."),
    L("E10", R_EQ, "Instancias en la nube reservadas (24 meses)", "clúster", 1, 180.0 * M, "SGR", "DECLARADO", "WP2", 1, 24, "Gemelo digital, base de datos y tablero; valor E3."),
    L("E11", R_EQ, "Software de analítica y repositorios", "paquete", 1, 45.0 * M, "SGR", "DECLARADO", "WP2", 1, 24, "Entorno seguro de desarrollo y control de versiones; valor E3."),
    L("E12", R_EQ, "Planes de datos celulares M2M para gateways (12 SIM, 24 meses)", "SIM-mes", 288, 0.12 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Solo los gateways transmiten por red celular."),
    # --- Materiales
    L("M01", R_MAT, "Filtros de membrana PTFE para gravimetría", "unidad", 1200, 12_000, "SGR", "DECLARADO", "WP1", 3, 24, "Validación gravimétrica; valor E3."),
    L("M02", R_MAT, "Polvo de ensayo normalizado y consumibles del banco de calibración", "lote", 15, 2.8 * M, "SGR", "PROPUESTO", "WP1", 1, 24, "Sustituye los gases patrón del expediente E3, que no aplican a partículas."),
    L("M03", R_MAT, "Cerramientos NEMA 4X y mástiles para nodos", "unidad", 120, 350_000, "SGR", "DECLARADO", "WP2", 1, 24, "Protección contra intemperie; valor E3."),
    L("M04", R_MAT, "Cartillas impresas del índice y del protocolo de alerta", "unidad", 5000, 8_500, "SGR", "DECLARADO", "WP3", 3, 24, "Población sin acceso a internet; valor E3."),
    L("M05", R_MAT, "Kits de papelería para talleres de co-diseño", "kit", 20, 1.5 * M, "SGR", "DECLARADO", "WP3", 2, 24, "Mesas de co-creación; valor E3."),
    L("M06", R_MAT, "Elementos de protección personal (mascarillas N95)", "unidad", 3000, 4_000, "SGR", "DECLARADO", "WP3", 1, 24, "Bioseguridad en campo; valor E3."),
    L("M07", R_MAT, "Repuestos y consumibles de mantenimiento (baterías, cables, conectores)", "lote", 1, 60.0 * M, "SGR", "PROPUESTO", "WP2", 3, 24, "Existencias de reposición en cada departamento."),
    # --- Servicios técnicos
    L("S01", R_SERV, "Análisis gravimétrico en laboratorio acreditado", "muestra", 240, 350_000, "SGR", "DECLARADO", "WP1", 3, 24, "Lectura certificada de filtros; valor E3."),
    L("S02", R_SERV, "Consultoría jurídica en propiedad intelectual y libertad de operación", "hora", 150, 300_000, "SGR", "DECLARADO", "WP3", 1, 24, "Solicitudes PCT con Colombia designada; valor E3."),
    L("S03", R_SERV, "Auditoría externa de ciberseguridad", "servicio", 2, 15.0 * M, "SGR", "DECLARADO", "WP2", 8, 24, "Dos pruebas de penetración; valor E3."),
    L("S05", R_SERV, "Instalación en sitio, mástiles y obra menor (100 nodos y 10 gateways)", "sitio", 110, 1.2 * M, "SGR", "PROPUESTO", "WP2", 3, 24, "Ejecución por tramo."),
    L("S06", R_SERV, "Estudio de cobertura y de enlace en tres departamentos", "estudio", 3, 20.0 * M, "SGR", "PROPUESTO", "WP2", 1, 4, "Presupuesto de enlace de los gateways."),
    L("S07", R_SERV, "Evaluación externa independiente (meses 12 y 24)", "evaluación", 2, 60.0 * M, "SGR", "PROPUESTO", "WP0", 12, 24, "Verificación de resultados frente a la línea base."),
    L("S08", R_SERV, "Ensayo de desempeño con laboratorio externo", "campaña", 1, 90.0 * M, "SGR", "PROPUESTO", "WP1", 20, 24, "Verificación independiente del cumplimiento de los umbrales."),
    L("S09", R_SERV, "Formación y soporte a custodios por tramo", "tramo", 3, 50.0 * M, "SGR", "PROPUESTO", "WP3", 6, 24, "Capacidad de absorción de los custodios."),
    L("S10", R_SERV, "Planes de enlace satelital de respaldo (10 módulos, 22 meses)", "módulo-mes", 220, 250_000, "SGR", "PROPUESTO", "WP2", 3, 24, "Datos de respaldo."),
    L("S11", R_SERV, "Importación y nacionalización de equipos", "servicio", 1, 80.0 * M, "SGR", "PROPUESTO", "WP0", 1, 18, "Tres lotes de importación."),
    # --- Viajes
    L("V01", R_VIAJ, "Tiquetes aéreos nacionales", "trayecto", 50, 0.6 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Reducido para respetar el tope de movilidad de 2 % del valor SGR; técnicos residentes en cada departamento."),
    L("V02", R_VIAJ, "Viáticos de alojamiento y manutención", "día-persona", 250, 0.35 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Instalación, mantenimiento y talleres; el complemento lo cubre la logística de emergencia de la empresa (C05)."),
    L("V03", R_VIAJ, "Arrendamiento de vehículos 4x4", "día", 100, 0.45 * M, "SGR", "PROPUESTO", "WP2", 1, 24, "Acceso a sitios sin vía pavimentada; arrendamiento, no compra."),
    L("V04", R_VIAJ, "Viaje internacional para divulgación científica", "viaje", 1, 12.0 * M, "SGR", "DECLARADO", "WP3", 14, 24, "Presentación de resultados; valor E3; reducido de 2 a 1 viaje por el tope de movilidad."),
    L("V05", R_VIAJ, "Alimentación de laboratorios ciudadanos", "evento", 20, 1.5 * M, "SGR", "DECLARADO", "WP3", 2, 24, "Participación comunitaria; valor E3."),
    # --- Otros rubros
    L("O01", R_OTR, "Cargos de procesamiento de artículos de acceso abierto", "artículo", 2, 12.5 * M, "SGR", "DECLARADO", "WP3", 14, 24, "Dos artículos Q1 o Q2; valor E3 (sin duplicar en servicios)."),
    L("O02", R_OTR, "Logística de ferias y laboratorios de apropiación", "evento", 9, 8.0 * M, "SGR", "DECLARADO", "WP3", 4, 24, "Espacios, pantallas y moderación; valor E3."),
    L("O03", R_OTR, "Registro ante la DNDA y asesoría de propiedad intelectual", "paquete", 1, 15.0 * M, "SGR", "DECLARADO", "WP3", 12, 24, "Registro del software; valor E3."),
    L("O05", R_OTR, "Administración (revisoría y plataforma de seguimiento)", "mes", 24, 15.0 * M, "SGR", "DECLARADO", "WP0", 1, 24, "Valor E3; el tope porcentual de administración no se verificó."),
    L("O06", R_OTR, "Publicaciones de divulgación y eventos de socialización", "paquete", 1, 60.0 * M, "SGR", "PROPUESTO", "WP3", 6, 24, "Piezas audiovisuales y jornadas de cierre."),
]

CONTRA = [
    L("C01", "Personal (especie)", "Investigador principal, 50 % durante 24 meses", "mes", 24, 14_583_333.333, "IES", "DECLARADO", "WP0", 1, 24, "Valor E3, Tabla 8.2; certificación de la IES pendiente."),
    L("C02", "Personal (especie)", "Coinvestigador técnico, 30 % durante 24 meses", "mes", 24, 10_416_666.667, "IES", "DECLARADO", "WP1", 1, 24, "Valor E3, Tabla 8.2."),
    L("C03", "Personal (especie)", "Coinvestigadores de ambiente y ciencias sociales, 20 %", "mes", 48, 4_166_666.667, "IES", "PROPUESTO", "WP3", 1, 24, "Dos personas; valor sujeto a certificación de la IES."),
    L("C04", "Infraestructura (especie)", "Uso de laboratorios y equipos de la IES", "mes", 24, 12_500_000, "IES", "PROPUESTO", "WP1", 1, 24, "Laboratorio de calibración óptica; valor sujeto a certificación."),
    L("C05", "Efectivo", "Aporte de la empresa tecnológica: logística y viáticos de emergencia", "global", 1, 210.0 * M, "EMP", "DECLARADO", "WP2", 1, 24, "Valor E3, Tabla 8.1."),
    L("C06", "Infraestructura (especie)", "Infraestructura en la nube de la empresa", "global", 1, 800.0 * M, "EMP", "DECLARADO", "WP2", 1, 24, "Valor E3, Tabla 8.1."),
]

RUBROS11 = ["Talento humano", "Equipos y software", "Capacitación y eventos", "Servicios tecnológicos y pruebas",
            "Materiales, insumos y documentación", "Protección del conocimiento y divulgación", "Gastos de viaje", "Infraestructura",
            "Administrativos", "Seguimiento", "Otros"]
_R11 = {}
for _i in [f"P{n:02d}" for n in range(1, 15)]: _R11[_i] = 1
for _i in [f"E{n:02d}" for n in range(1, 12)]: _R11[_i] = 2
for _i in ["S09", "V05", "O02", "M05"]: _R11[_i] = 3
for _i in ["S01", "S03", "S05", "S06", "S08", "S10", "E12"]: _R11[_i] = 4
for _i in ["M01", "M02", "M03", "M06", "M07"]: _R11[_i] = 5
for _i in ["S02", "O03", "O01", "O06", "M04"]: _R11[_i] = 6
for _i in ["V01", "V02", "V03", "V04"]: _R11[_i] = 7
for _i in ["O05", "S07"]: _R11[_i] = 10
for _i in ["X01", "S11"]: _R11[_i] = 11

def bud_rows(rows):
    out = collections.OrderedDict()
    for r in rows:
        out.setdefault(r["rubro"], []).append(r)
    return out

def total(rows): return sum(r["total"] for r in rows)

# ------------------------------------------------------------------ RIESGOS
RIESGOS = [
    # id, categoría, descripción, causa (variable), P(1-5), I(1-5), prob %, impacto COP, estrategia, respuesta, responsable, disparador
    ("R-TEC-01", "Técnico", "La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10.", "V03, V02", 4, 5, 60, 250.0 * M, "Mitigar", "Modelo de corrección por humedad, banco de calibración y reposición de cabezales.", "Especialista en metrología", "NRMSE > 30 % en dos verificaciones consecutivas"),
    ("R-TEC-02", "Técnico", "Las baterías se agotan antes de 14 días sin sol y los nodos dejan de transmitir.", "V05, V09", 3, 4, 30, 80.0 * M, "Mitigar", "Kits solares dimensionados, modo de bajo consumo y repuestos de batería.", "Ingeniero de firmware", "Disponibilidad mensual < 90 %"),
    ("R-TEC-03", "Técnico", "La red celular falla en el sitio y los gateways pierden el enlace con la nube.", "V08", 3, 4, 40, 70.0 * M, "Mitigar", "Enlace satelital de respaldo y almacenamiento local de 7 días.", "Ingenieros IoT", "Pérdida de paquetes > 10 % durante 72 horas"),
    ("R-TEC-04", "Técnico", "El modelo de corrección no generaliza entre departamentos.", "V07, V06", 3, 4, 35, 90.0 * M, "Mitigar", "Validación cruzada por departamento y reentrenamiento por tramo.", "Científico de datos", "R² < 0,70 en el conjunto de validación externo"),
    ("R-ORG-01", "Organizacional", "Los comités de gestión del riesgo no adoptan el tablero ni el protocolo.", "V15", 3, 5, 40, 90.0 * M, "Mitigar", "Co-diseño de umbrales, formación por comité y uso piloto con registro de decisiones.", "Coordinación de apropiación", "Menos de 50 % de uso en el tramo 1"),
    ("R-ORG-02", "Organizacional", "Los custodios no asumen la operación en el posproyecto.", "V15", 4, 4, 50, 120.0 * M, "Mitigar", "Convenios por tramo, formación de custodios y cláusula de apertura.", "Profesional de convenios", "Convenio sin partida al cierre del tramo 2"),
    ("R-EXT-01", "Externo", "Deslizamientos o réplicas bloquean vías y retrasan la instalación.", "V05", 4, 3, 50, 120.0 * M, "Aceptar y mitigar", "Instalación en ventanas secas, técnicos locales y holgura en el cronograma.", "Gerencia de proyecto", "Retraso de instalación > 3 semanas"),
    ("R-EXT-02", "Externo", "Robo o vandalismo de nodos en sitios de remoción.", "V09", 3, 3, 40, 60.0 * M, "Transferir y mitigar", "Cerramientos, custodia local por sitio y seguro de equipos de la entidad ejecutora, fuera del presupuesto SGR.", "Técnicos de campo", "Dos o más nodos perdidos en un mes"),
    ("R-FIN-01", "Financiero", "La devaluación del peso encarece los equipos importados.", "—", 4, 4, 55, 300.0 * M, "Mitigar", "Compra por tramo con cobertura cambiaria y cotizaciones vigentes.", "Gerencia de proyecto", "TRM supera en 10 % la de la cotización"),
    ("R-FIN-02", "Financiero", "La contrapartida en especie no se certifica a tiempo.", "—", 2, 4, 25, 80.0 * M, "Evitar", "Certificación de la IES y de la empresa antes del acta de inicio.", "Gerencia de proyecto", "Certificación pendiente al mes 2"),
    ("R-JUR-01", "Jurídico", "Una solicitud de patente de terceros afecta la libertad de operación.", "—", 2, 4, 20, 100.0 * M, "Mitigar", "Análisis de libertad de operación y diseño alternativo del módulo afectado.", "Consultoría en propiedad intelectual", "Solicitud con fase nacional abierta que reivindique el método"),
    ("R-DAT-01", "Datos", "Un incidente de ciberseguridad compromete la plataforma.", "V15", 2, 4, 20, 90.0 * M, "Mitigar", "Pruebas de penetración, segmentación y copias de respaldo.", "Ingenieros de software", "Hallazgo crítico en la auditoría"),
]

def riesgos_calc():
    out = []
    for r in RIESGOS:
        id_, cat, desc, causa, P, I, pp, imp, est, resp, who, trig = r
        emv = int(round(pp / 100 * imp))
        score = P * I
        niv = "EXTREMO" if score >= 20 else "ALTO" if score >= 12 else "MEDIO" if score >= 6 else "BAJO"
        out.append(dict(id=id_, cat=cat, desc=desc, causa=causa, P=P, I=I, score=score, nivel=niv, prob=pp,
                        impacto=int(imp), emv=emv, estrategia=est, respuesta=resp, resp=who, disp=trig))
    return out

RISKS = riesgos_calc()
RESERVA = sum(r["emv"] for r in RISKS)
RESERVA = int(round(RESERVA / M)) * M   # redondeo a millones

BUDGET.append(L("X01", R_RES, "Reserva de contingencia (suma de valores monetarios esperados)", "global", 1, RESERVA, "SGR", "CALCULADO", "WP0", 1, 24,
                "Suma de EMV de la Tabla de riesgos; su admisibilidad como rubro depende de los términos de referencia (VACIO)."))
for _r in BUDGET: _r["rubro11"] = RUBROS11[_R11[_r["id"]] - 1]
assert len(_R11) == len(BUDGET), (len(_R11), len(BUDGET))

# ------------------------------------------------------------------ CALENDARIO Y FLUJO DE CAJA
def spread(line, months=24):
    """Distribuye el total de la línea de forma uniforme entre m_ini y m_fin (compra única si m_ini==m_fin)."""
    flow = [0.0] * months
    n = line["m_fin"] - line["m_ini"] + 1
    for m in range(line["m_ini"], line["m_fin"] + 1):
        flow[m - 1] += line["total"] / n
    return flow

def flujo(rows, months=24):
    f = [0.0] * months
    for r in rows:
        for i, v in enumerate(spread(r, months)): f[i] += v
    return f

def por_periodo(f, size):
    return [sum(f[i:i + size]) for i in range(0, len(f), size)]

# Compras de equipos por tramo (reasignación de flujos de E01, E02, E04 según TRAMOS)
def flujo_equipos_por_tramo():
    f = [0.0] * 24
    mapa = {"E01": ("compra_nodos", 4.5 * M), "E02": ("compra_cabezales", 1.2 * M), "E04": ("compra_gw", 28.0 * M)}
    for t in TRAMOS:
        mes = t["mes_compra"]
        for k, (campo, vu) in mapa.items():
            f[mes - 1] += t[campo] * vu
    return f

def flujo_sgr():
    f = [0.0] * 24
    for r in BUDGET:
        if r["id"] in ("E01", "E02", "E04"): continue
        for i, v in enumerate(spread(r)): f[i] += v
    for i, v in enumerate(flujo_equipos_por_tramo()): f[i] += v
    return f

def flujo_contra():
    return flujo(CONTRA)

# ------------------------------------------------------------------ CRONOGRAMA (red de actividades en semanas, CPM)
ACT = [
    # id, nombre, semanas, predecesoras, wp
    ("A0.1", "Contratar equipo y firmar convenios de ejecución", 8, [], "WP0"),
    ("A1.1", "Seleccionar sitios y diseñar la colocalización", 4, ["A0.1"], "WP1"),
    ("A2.1", "Diseñar arquitectura de enlace y energía", 6, ["A0.1"], "WP2"),
    ("A1.2", "Adquirir y caracterizar lote 1 de nodos y referencias", 10, ["A1.1", "A2.1"], "WP1"),
    ("A2.2", "Desarrollar firmware y plataforma base", 10, ["A2.1"], "WP2"),
    ("A1.3", "Colocalizar y calibrar en el piloto (tramo 1)", 16, ["A1.2", "A2.2"], "WP1"),
    ("A3.1", "Co-diseñar umbrales y protocolo de alerta con comités", 24, ["A1.1"], "WP3"),
    ("A1.4", "Entrenar y validar el modelo de corrección", 8, ["A1.3"], "WP1"),
    ("C1", "Compuerta C1: decisión de ampliación al tramo 2", 2, ["A1.4", "A3.1"], "WP0"),
    ("A2.3", "Instalar tramo 2 (40 nodos, 4 gateways)", 12, ["C1"], "WP2"),
    ("A1.5", "Reentrenar y verificar por departamento (tramo 2)", 6, ["A2.3"], "WP1"),
    ("A3.2", "Poner en uso el tablero con los comités", 12, ["C1"], "WP3"),
    ("C2", "Compuerta C2: decisión de consolidación al tramo 3", 2, ["A1.5", "A3.2"], "WP0"),
    ("A2.4", "Instalar tramo 3 (30 nodos, 3 gateways)", 12, ["C2"], "WP2"),
    ("A3.3", "Formar custodios y firmar convenios por tramo", 16, ["C2"], "WP3"),
    ("A1.6", "Verificar desempeño final y ensayo independiente", 16, ["A2.4"], "WP1"),
    ("A3.4", "Transferir, cerrar y evaluar", 6, ["A1.6", "A3.3"], "WP0"),
]

def cpm():
    acts = {a[0]: dict(id=a[0], nombre=a[1], dur=a[2], pred=a[3], wp=a[4]) for a in ACT}
    order = []
    seen = set()
    def visit(k):
        if k in seen: return
        for p in acts[k]["pred"]: visit(p)
        seen.add(k); order.append(k)
    for k in acts: visit(k)
    for k in order:
        a = acts[k]
        a["ES"] = max([acts[p]["EF"] for p in a["pred"]], default=0)
        a["EF"] = a["ES"] + a["dur"]
    fin = max(a["EF"] for a in acts.values())
    for k in reversed(order):
        a = acts[k]
        succ = [s for s in acts.values() if k in s["pred"]]
        a["LF"] = min([s["LS"] for s in succ], default=fin)
        a["LS"] = a["LF"] - a["dur"]
        a["holgura"] = a["LS"] - a["ES"]
    return acts, fin, [k for k in order if acts[k]["holgura"] == 0]

ACTS, DURACION_SEMANAS, RUTA_CRITICA = cpm()

# ------------------------------------------------------------------ HITOS
def mes_de(sem):  # semana (fin de actividad) -> mes de calendario (1 mes = 52/12 semanas)
    return int(math.ceil(sem / (52 / 12) - 1e-9))

HITOS = [
    ("H0", "Acta de inicio y contratación completa", mes_de(ACTS["A0.1"]["EF"]), "Contratos, convenios y plan de trabajo aprobados"),
    ("H1", "Sitios del tramo 1 y diseño de enlace y energía listos", mes_de(max(ACTS["A1.1"]["EF"], ACTS["A2.1"]["EF"])), "Informe de sitios, de cobertura y de energía"),
    ("H2", "Colocalización del tramo 1 finalizada", mes_de(ACTS["A1.3"]["EF"]), "Base de datos de colocalización y línea base de error medida"),
    ("H3", "Compuerta C1: modelo validado en el piloto", mes_de(ACTS["C1"]["EF"]), "Acta de compuerta con NRMSE y R² frente a referencia"),
    ("H4", "Tramo 2 instalado y verificado", mes_de(ACTS["A1.5"]["EF"]), "Informe de disponibilidad y desempeño del tramo 2"),
    ("H5", "Compuerta C2: uso institucional y desempeño", mes_de(ACTS["C2"]["EF"]), "Acta de compuerta con uso del tablero y convenios"),
    ("H6", "Tramo 3 instalado", mes_de(ACTS["A2.4"]["EF"]), "Inventario de 100 nodos y 10 gateways operativos"),
    ("H7", "Ensayo independiente y evaluación final", mes_de(ACTS["A1.6"]["EF"]), "Informe de laboratorio externo y evaluación externa"),
    ("H8", "Transferencia y cierre del tramo 3", mes_de(ACTS["A3.4"]["EF"]), "Actas de entrega a custodios y cláusula de apertura firmada"),
]

# ------------------------------------------------------------------ CÁLCULOS DE CONTROL
def resumen():
    sgr = [r for r in BUDGET if r["fuente"] == "SGR"]
    t_sgr = total(sgr)
    t_con = total(CONTRA)
    por_rubro = collections.OrderedDict((k, total(v)) for k, v in bud_rows(sgr).items())
    fs = por_periodo(flujo_sgr(), 6)
    fc = por_periodo(flujo_contra(), 6)
    return dict(sgr=t_sgr, contra=t_con, total=t_sgr + t_con, por_rubro=por_rubro, flujo_sgr_sem=fs, flujo_con_sem=fc,
                pct_tope=t_sgr / IDENT["tope_cop"], holgura=IDENT["tope_cop"] - t_sgr, reserva=RESERVA,
                duracion_semanas=DURACION_SEMANAS, ruta_critica=RUTA_CRITICA)

def cop(n):  # $ 1.234.567
    return "$ " + f"{int(round(n)):,}".replace(",", ".")

def mm(n, d=1):  # millones con coma decimal
    s = f"{n / M:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

if __name__ == "__main__":
    r = resumen()
    print("SGR", cop(r["sgr"]), f"{r['pct_tope']*100:.1f}% del tope; holgura", cop(r["holgura"]))
    print("Contrapartida", cop(r["contra"]), "Total", cop(r["total"]))
    for k, v in r["por_rubro"].items(): print(f"  {k:28s} {mm(v):>10s} M  {v / r['sgr'] * 100:5.1f}%")
    print("flujo SGR semestral (M):", [round(x / M, 1) for x in r["flujo_sgr_sem"]], round(sum(r["flujo_sgr_sem"]) / M, 1))
    print("flujo contrapartida (M):", [round(x / M, 1) for x in r["flujo_con_sem"]], round(sum(r["flujo_con_sem"]) / M, 1))
    print("Reserva", cop(RESERVA), "Duración semanas", DURACION_SEMANAS, "Ruta crítica:", RUTA_CRITICA)
    adm = sum(l["total"] for l in BUDGET if l["id"] == "O05")
    print("Administración % SGR:", f"{adm / r['sgr'] * 100:.2f}")
    print("Verificación flujo=total:", abs(sum(flujo_sgr()) - r["sgr"]) < 1)
    print("Personal SGR:", mm(r['por_rubro']['Personal']))
