# -*- coding: utf-8 -*-
"""Sistema de indicadores PERS (15) y matriz de marco lógico. Fuente única para capítulos 11, 12, 13, 18 y 21."""

# campos: cod, nivel, taxonomia, nombre, oe, formula, unidad, lb, lb_nat, m1, m2, mf, frecuencia, fuente, resp, mmg, supuesto, riesgo, verificacion
IND = [
 dict(cod="PERS-R01", nivel="R", tax="Output", nombre="Cumplimiento del despliegue por tramo", oe="OE2",
      formula="Nodos instalados y operativos ÷ nodos programados × 100", unidad="%", lb="0", lb_nat="CALCULADO",
      m1="30 nodos (100 % del tramo 1)", m2="70 nodos adicionales (100 % de los tramos 2 y 3)", mf="100 nodos y 10 gateways (100 %)",
      frecuencia="Mensual", fuente="Inventario de la plataforma y actas de instalación", resp="Ingenieros IoT y de campo", mmg="—",
      supuesto="Acceso vial a los sitios en ventanas secas", riesgo="Medio", verificacion="Acta de instalación con coordenadas y número de serie"),
 dict(cod="PERS-R02", nivel="R", tax="Output", nombre="Ciclos de calibración ejecutados", oe="OE1",
      formula="Número de ciclos completos de entrenamiento, validación y despliegue del modelo de corrección", unidad="ciclos", lb="0", lb_nat="CALCULADO",
      m1="2 ciclos (tramo 1)", m2="4 ciclos acumulados", mf="6 ciclos (2 por tramo)",
      frecuencia="Mensual", fuente="Registro de versiones del modelo", resp="Científico de datos", mmg="—",
      supuesto="Datos de colocalización con completitud mayor o igual a 75 %", riesgo="Medio", verificacion="Informe de validación firmado por la metrología"),
 dict(cod="PERS-R03", nivel="R", tax="Output", nombre="Disponibilidad de la plataforma en la nube", oe="OE2",
      formula="Horas de servicio ÷ horas del mes × 100", unidad="%", lb="VACIO", lb_nat="VACIO",
      m1="≥ 99,0 %", m2="≥ 99,0 %", mf="≥ 99,0 %",
      frecuencia="Mensual", fuente="Monitor de servicio de la plataforma", resp="Ingenieros de software y nube", mmg="—",
      supuesto="Servicio contratado con acuerdo de nivel de servicio", riesgo="Bajo", verificacion="Reporte mensual del proveedor de nube"),
 dict(cod="PERS-R04", nivel="R", tax="Output", nombre="Desviación de la ejecución presupuestal", oe="OE3",
      formula="(Ejecución acumulada − programación acumulada) ÷ programación acumulada × 100", unidad="%", lb="0", lb_nat="CALCULADO",
      m1="|desviación| ≤ 10 %", m2="|desviación| ≤ 10 %", mf="|desviación| ≤ 5 % al cierre",
      frecuencia="Mensual", fuente="Sistema de seguimiento presupuestal", resp="Gerencia de proyecto", mmg="—",
      supuesto="Desembolsos oportunos por tramo", riesgo="Medio", verificacion="Informe financiero conciliado con el técnico"),
 dict(cod="PERS-R05", nivel="R", tax="Output", nombre="Horas-nodo de colocalización válidas", oe="OE1",
      formula="Suma de horas con dato pareado entre nodo y referencia que cumplen el control de calidad", unidad="horas-nodo", lb="0", lb_nat="CALCULADO",
      m1="≥ 60.000 horas-nodo en el tramo 1", m2="≥ 60.000 + rotaciones trimestrales", mf="≥ 60.000 y 4 rotaciones por departamento",
      frecuencia="Mensual", fuente="Base de datos de colocalización", resp="Especialista en metrología", mmg="—",
      supuesto="Tres referencias operando con completitud mayor o igual a 90 %", riesgo="Medio", verificacion="Bitácora de la referencia y tablero de calidad de datos"),
 dict(cod="PERS-R06", nivel="R", tax="Output", nombre="Cumplimiento de informes de seguimiento", oe="OE3",
      formula="Informes técnicos y financieros entregados a tiempo ÷ informes exigidos × 100", unidad="%", lb="0", lb_nat="CALCULADO",
      m1="100 %", m2="100 %", mf="100 %",
      frecuencia="Mensual", fuente="Sistema de seguimiento del financiador", resp="Gerencia de proyecto", mmg="—",
      supuesto="Calendario de informes definido por los términos de referencia (VACIO)", riesgo="Bajo", verificacion="Radicados de entrega"),
 dict(cod="PERS-P01", nivel="P", tax="Output", nombre="Red de 100 nodos y 10 gateways operativa", oe="OE2",
      formula="Nodos operativos con disponibilidad mensual ≥ 90 % y gateways con enlace principal o alterno activo", unidad="nodos / gateways", lb="0 / 0", lb_nat="CALCULADO",
      m1="30 / 3 al mes 12", m2="70 / 7 al mes 17 y 100 / 10 al mes 19", mf="100 / 10 al mes 24",
      frecuencia="Trimestral", fuente="Plataforma e inventario", resp="Ingenieros IoT y de campo", mmg="PROT-FUNC",
      supuesto="Compuertas C1 y C2 aprobadas", riesgo="Medio", verificacion="Inventario con huella de configuración y registro fotográfico"),
 dict(cod="PERS-P02", nivel="P", tax="Output", nombre="Software de corrección y gemelo digital registrado", oe="OE1",
      formula="Registros de software ante la DNDA (modelo de corrección, firmware y gemelo digital)", unidad="registros", lb="0", lb_nat="CALCULADO",
      m1="0", m2="1 solicitud radicada", mf="1 registro vigente",
      frecuencia="Trimestral", fuente="Certificado de la DNDA", resp="Profesional de convenios y custodia", mmg="SW-REG",
      supuesto="Acuerdo de titularidad firmado entre las partes", riesgo="Bajo", verificacion="Certificado de registro"),
 dict(cod="PERS-P03", nivel="P", tax="Output", nombre="Artículos científicos en revistas Q1 o Q2", oe="OE1",
      formula="Artículos sometidos y aceptados con filiación del proyecto", unidad="artículos", lb="0", lb_nat="CALCULADO",
      m1="0", m2="1 sometido", mf="2 sometidos y al menos 1 aceptado al mes 24",
      frecuencia="Trimestral", fuente="Plataformas editoriales y CvLAC", resp="Investigador principal", mmg="ART-A1 / ART-A2",
      supuesto="Tiempos editoriales compatibles con el cierre", riesgo="Medio", verificacion="Carta de aceptación y soporte de envío"),
 dict(cod="PERS-P04", nivel="P", tax="Output", nombre="Actividades de apropiación social documentadas", oe="OE3",
      formula="Talleres de co-diseño (nivel 3) más jornadas públicas (niveles 1 y 2) con acta y lista de asistencia", unidad="actividades", lb="0", lb_nat="CALCULADO",
      m1="10 actividades", m2="29 actividades acumuladas", mf="29 actividades (20 talleres y 9 jornadas)",
      frecuencia="Trimestral", fuente="Actas y listas de asistencia", resp="Coordinación de apropiación social", mmg="ASC-PART / ASC-COM / ASC-CIRC",
      supuesto="Participación comunitaria con consentimiento informado", riesgo="Medio", verificacion="Actas firmadas por representantes comunitarios"),
 dict(cod="PERS-E01", nivel="E", tax="Outcome", nombre="Uso institucional del tablero y del protocolo", oe="OE3",
      formula="Comités focalizados con al menos una decisión documentada por trimestre basada en el tablero ÷ comités focalizados × 100", unidad="%", lb="VACIO", lb_nat="VACIO",
      m1="≥ 50 % (piloto)", m2="≥ 65 %", mf="≥ 75 % al mes 24",
      frecuencia="Trimestral", fuente="Actas de los comités y registro de decisiones del tablero", resp="Coordinación de apropiación social", mmg="—",
      supuesto="Comités constituidos y con sesiones periódicas", riesgo="Alto", verificacion="Acta del comité con referencia a la lectura del tablero"),
 dict(cod="PERS-E02", nivel="E", tax="Outcome", nombre="Reducción relativa de falsas alarmas", oe="OE3",
      formula="1 − (tasa de falsas alarmas del periodo ÷ tasa de línea base medida en el tramo 1)", unidad="%", lb="Se mide en el tramo 1", lb_nat="VACIO",
      m1="Línea base medida", m2="≥ 15 %", mf="≥ 30 % de reducción relativa",
      frecuencia="Trimestral", fuente="Registro de alertas y verificación con referencia", resp="Profesional en calidad del aire", mmg="—",
      supuesto="Umbrales validados localmente en el co-diseño", riesgo="Alto", verificacion="Cruce entre alertas emitidas y mediciones de referencia"),
 dict(cod="PERS-E03", nivel="E", tax="Outcome", nombre="Capacidad instalada en custodios", oe="OE3",
      formula="Personas con evaluación práctica aprobada en mantenimiento, lectura y operación ÷ personas formadas × 100, y número absoluto", unidad="personas", lb="0", lb_nat="CALCULADO",
      m1="20 personas", m2="40 personas", mf="≥ 60 personas certificadas",
      frecuencia="Semestral", fuente="Registros de formación y evaluación práctica", resp="Profesional de convenios y custodia", mmg="FORM (capacitación)",
      supuesto="Custodios designan personal con permanencia", riesgo="Alto", verificacion="Certificados y actas de evaluación práctica"),
 dict(cod="PERS-S01", nivel="S", tax="Impact", nombre="Activación del protocolo ante superación de umbral", oe="OE3",
      formula="Eventos de superación de umbral con medida de protección activada y registrada ÷ eventos de superación confirmados × 100", unidad="%", lb="VACIO", lb_nat="VACIO",
      m1="No aplica (medición posproyecto)", m2="No aplica", mf="≥ 80 % a los 12 meses posteriores al cierre",
      frecuencia="Anual, 6 a 12 meses tras el cierre", fuente="Registro de eventos y de medidas", resp="Custodios y secretarías de gestión del riesgo", mmg="—",
      supuesto="Custodia operativa y datos disponibles", riesgo="Alto", verificacion="Evaluación externa posproyecto"),
 dict(cod="PERS-S02", nivel="S", tax="Impact", nombre="Continuidad de la red bajo custodia", oe="OE3",
      formula="Nodos operados por custodios con partida y competencia a los 12 meses del cierre ÷ nodos entregados × 100", unidad="%", lb="VACIO", lb_nat="VACIO",
      m1="No aplica", m2="No aplica", mf="≥ 70 % a los 12 meses posteriores al cierre",
      frecuencia="Anual, 12 meses tras el cierre", fuente="Convenios, presupuestos y plataforma", resp="Profesional de convenios y custodia", mmg="—",
      supuesto="Cláusula de apertura y financiación de custodios", riesgo="Alto", verificacion="Evaluación externa posproyecto"),
]
assert len(IND) == 15
assert [i["nivel"] for i in IND].count("R") == 6 and [i["nivel"] for i in IND].count("P") == 4
assert [i["nivel"] for i in IND].count("E") == 3 and [i["nivel"] for i in IND].count("S") == 2

# Umbrales de desempeño de la corrección (PROPUESTO; ancla externa: protocolos de la EPA de EE. UU. para sensores de PM2,5)
UMBRALES = {
    "R2_min": 0.70, "NRMSE_max": 0.30, "pendiente": (0.65, 1.35), "sesgo_ug": (-5.0, 5.0),
    "meta_aspiracional_NMAE": 0.15,
    "nota": "El umbral del plan es el de la EPA (2021) para uso informativo en sitio fijo; la meta de NMAE ≤ 15 % es aspiracional y no condiciona las compuertas.",
}

# Marco lógico 4x4 (Fin, Propósito, Componentes, Actividades)
MARCO_LOGICO = {
 "Fin": dict(res="Reducción de la exposición evitable de operarios y población a material particulado por remoción de escombros, mediante alertas basadas en mediciones verificadas.",
             ind="PERS-S01 y PERS-S02", med="Evaluación externa posproyecto", sup="Los custodios financian la operación y los comités mantienen el protocolo."),
 "Propósito": dict(res="Los comités de gestión del riesgo usan mediciones verificadas de PM2,5 y PM10 de una red de 100 nodos para decidir alertas.",
             ind="PERS-E01, PERS-E02 y PERS-E03", med="Actas de comité; registro de alertas; evaluaciones prácticas", sup="Las compuertas C1 y C2 se aprueban y el enlace alterno funciona."),
 "Componentes": dict(res="C1: modelo de corrección validado. C2: red operativa con energía y enlace redundantes. C3: tablero, protocolo y convenios de custodia.",
             ind="PERS-P01 a PERS-P04", med="Inventario, certificados DNDA, cartas de aceptación y actas", sup="Los equipos llegan en los plazos de importación previstos."),
 "Actividades": dict(res="WP0 gestión; WP1 medición verificada; WP2 red, energía y plataforma; WP3 uso institucional, apropiación y custodia (Tabla de EDT).",
             ind="PERS-R01 a PERS-R06", med="Informes de seguimiento y soportes financieros", sup="Acceso a los sitios en ventanas secas y contratación oportuna."),
}

# Alineación de apropiación social (Escalera ASC)
ASC = [
 ("Nivel 1: Información", "ASC-COM", "Boletines, cartillas, página del proyecto", "100 % durante el primer tercio de la ejecución"),
 ("Nivel 2: Consulta", "ASC-COM y ASC-PART", "Grupos focales, encuestas, foros", "100 % durante la primera mitad de la ejecución"),
 ("Nivel 3: Colaboración activa", "ASC-PART", "Co-diseño de umbrales, validación comunitaria, comité asesor", "Mínimo 3 actividades documentadas con acta firmada (compromiso obligatorio)"),
 ("Nivel 4: Empoderamiento", "ASC-PART y formación", "Formación de formadores locales, observatorio comunitario", "Aspiracional: 1 actividad con plan de sostenibilidad"),
]

if __name__ == "__main__":
    for i in IND: print(i["cod"], i["nivel"], i["tax"], i["nombre"], "|", i["mf"])
