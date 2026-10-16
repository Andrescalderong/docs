# -*- coding: utf-8 -*-
"""Documento técnico en formato Anexo 2, secciones 18 a 28, 30 (la 29 es la bibliografía del capítulo 19)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from a2lib import *
import indicadores as IM

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = Doc("D")
LB = {r["id"]: r for r in D.BUDGET if r["fuente"] == "SGR"}
def lin(*ids): return sum(LB[i]["total"] for i in ids)

# ============================================================== 18
d.raw("# 18. COMPONENTE TRANSVERSAL DE TRANSFERENCIA, ADOPCIÓN Y VALORACIÓN TECNOLÓGICA DEL CONOCIMIENTO")
d.p("El componente aplica al proyecto sin excepción. Su propósito es que los resultados se adopten, se apliquen y se sostengan con evidencia de uso. El proyecto destina a este componente un valor superior al mínimo de 1 % del valor total que exige el Anexo 2. La sección 18.4 calcula la proporción.")
d.h(2, "18.1 Plan de transferencia, adopción y valoración tecnológica del conocimiento")
d.p("El plan se articula con los objetivos, actividades, cronograma y presupuesto del proyecto. Sus siete elementos mínimos están en las secciones 18.2 a 18.5. El plan se actualiza durante la ejecución según los resultados de las compuertas C1 y C2.")
d.h(2, "18.2 Resultados, usuarios y oportunidades de transferencia")
d.p("La {T:t19} identifica los resultados con potencial de uso, sus usuarios, la oportunidad de aprovechamiento y el activo de propiedad intelectual. Ningún activo cuenta con un acuerdo de titularidad firmado.")
d.tabla("t19", "Resultados, usuarios y oportunidades de transferencia",
        ["Resultado, conocimiento o tecnología", "Potencial de uso o aplicación", "Usuario, beneficiario o receptor potencial", "Oportunidad de aprovechamiento o transferencia", "Activo de propiedad intelectual"],
        [("Modelo de corrección en el gateway", "Corregir lecturas de sensores ópticos por humedad y fracción gruesa", "Autoridades ambientales, redes municipales de vigilancia y fabricantes de sensores", "Licencia no exclusiva o codesarrollo, previa definición de la titularidad", "Software: registro ante la DNDA"),
         ("Protocolo de calibración colocalizada y series de datos", "Calibrar redes de bajo costo en sitios sin estación de referencia", "Autoridades ambientales y universidades", "Publicación abierta, capacitación y réplica", "Conocimiento documentado; base de datos con licencia de datos"),
         ("Red de nodos y gateways", "Vigilancia en sitios de emergencia", "Comités de gestión del riesgo y UNGRD", "Réplica con la unidad de expansión: un gateway con 10 nodos, de 120,08 millones de COP", "Diseño y firmware: registro de software"),
         ("Gemelo digital y tablero", "Presentar la medición con su error residual a quien decide", "Comités de gestión del riesgo", "Convenio de operación y licencia con la institución custodia", "Software y marca del tablero"),
         ("Medición del error de sensores en polvo de escombros", "Nuevo conocimiento sobre desempeño bajo condiciones extremas", "Comunidad científica e industria de sensores", "Artículos y datos abiertos", "Artículos; datos")],
        "*Nota.* Elaboración propia con la sección 15.2 del expediente. Titularidad y vía de protección: PROPUESTO; acuerdos pendientes.")
d.h(2, "18.3 Estrategia o ruta de transferencia, adopción y valoración tecnológica")
d.p("La {T:t20} describe la estrategia y las barreras. El proyecto transfiere primero conocimiento y datos, luego equipos y tablero, y al final la operación continua.")
d.tabla("t20", "Ruta de transferencia y principales barreras",
        ["Campo", "Descripción"],
        [("Ruta o estrategia propuesta", "Transferencia por tramos condicionados con convenios de custodia y partida. Registro de software y licenciamiento no exclusivo. Cláusula de apertura que publica datos y código si ningún custodio demuestra capacidad. Actores: Universidad, empresa, actor reconocido y municipios. Acciones: consulta de libertad de operación, acuerdos de titularidad, formación de custodios y convenios por tramo."),
         ("Principales barreras o retos", "Acuerdos de titularidad sin firmar. Custodios sin capacidad de absorción demostrada. Solicitudes de patente de terceros que designan a Colombia: diez, de las cuales tres siguen abiertas. Mercado no estudiado. Capacidades limitadas de los municipios. Marco regulatorio que no reconoce datos de sensores como medición oficial.")],
        "*Nota.* Elaboración propia con las secciones 15.1 a 15.3 del expediente. Las barreras de patentes provienen del informe de vigilancia tecnológica.")
d.h(2, "18.4 Actividades, productos, indicadores y presupuesto")
p_ip = lin("S02", "O03"); p_cus = lin("S09"); p_conv = lin("P14"); p_tot = p_ip + p_cus + p_conv
d.p("La {T:t21} presenta las tres actividades del plan con su presupuesto. Suman " + cop(p_tot) + ", equivalentes a " + num(p_tot / SGR_T * 100, 2) + " % del valor SGR y a " + num(p_tot / TOT_T * 100, 2) + " % del valor total. El mínimo de 1 % del valor total es " + cop(TOT_T * 0.01) + ". El proyecto lo supera. Las publicaciones y los talleres de apropiación social no se cuentan.")
d.tabla("t21", "Actividades, productos, indicadores y presupuesto del plan de transferencia",
        ["Actividad", "Resultado asociado", "Producto o evidencia", "Indicador", "Responsable", "Periodo", "Presupuesto"],
        [("Gestión de propiedad intelectual y libertad de operación (líneas S02 y O03)", "Activos protegidos y libertad de operación verificada", "Concepto jurídico y certificado de registro de software", "1 registro vigente (PERS-P02); 10 solicitudes clasificadas", "Universidad, con la empresa", "Meses 1 a 24", cop(p_ip)),
         ("Formación y soporte a custodios por tramo (línea S09)", "Capacidad instalada para la operación posproyecto", "Certificados y actas de evaluación práctica", "60 personas certificadas (PERS-E03)", "Actor reconocido por MinCiencias", "Meses 6 a 24", cop(p_cus)),
         ("Estructuración de convenios de custodia, licencia y partida (línea P14)", "Custodia formalizada por componente", "Convenios firmados con partida", "3 convenios, uno por tramo; continuidad de 70 % o más (PERS-S02)", "Universidad, con los municipios", "Meses 1 a 24", cop(p_conv)),
         ("TOTAL", "", "", "", "", "", cop(p_tot))],
        "*Nota.* Elaboración propia con las líneas del presupuesto SGR. La vigilancia tecnológica y el estudio de mercado no tienen línea presupuestal propia (VACIO). Los valores son CALCULADOS.")
d.h(2, "18.5 Continuidad del proceso")
d.p("La continuidad depende de los custodios. Doce meses después del cierre, una evaluación externa mide la activación del protocolo y la continuidad de la red (PERS-S01 y PERS-S02). Si un custodio no demuestra capacidad, opera la cláusula de apertura y la salida es ordenada. Los costos de sostenimiento son NO_CALCULABLE hasta que los custodios aporten sus datos.")

# ============================================================== 19
d.raw("# 19. COMPONENTE TRANSVERSAL DE APROPIACIÓN SOCIAL DEL CONOCIMIENTO (ASC)")
d.p("La estrategia de apropiación social del conocimiento es transversal al proyecto. Se articula con la problemática, los objetivos, las actividades, los productos y el presupuesto. El Anexo 10 de los términos de referencia no se aportó. La estrategia se formula con los siete componentes mínimos del Anexo 2 (NO_VERIFICADO frente al Anexo 10).")
d.h(2, "19.1 Estrategia de apropiación social del conocimiento")
d.p("La estrategia entiende la apropiación como participación, diálogo de saberes y co-creación. Los comités no reciben un producto terminado. Co-diseñan los umbrales y el protocolo de alerta y validan el tablero. La {T:t22} describe los siete componentes.")
d.tabla("t22", "Componentes de la estrategia de apropiación social",
        ["Componente", "Descripción en el proyecto"],
        [("A. Análisis y reconocimiento del contexto", "Diagnóstico participativo de los 12 municipios en el tramo 1: sitios de remoción, rutinas de alerta y canales de comunicación existentes"),
         ("B. Identificación y caracterización de actores", "15 comités de gestión del riesgo, 150 funcionarios, cuadrillas de remoción, comunidades expuestas y contratistas; el mapa de interesados está en el documento X7"),
         ("C. Identificación de saberes, conocimientos y capacidades", "Conocimiento local sobre polvo, lluvia y humedad en cada sitio; experiencia de los operarios; capacidades técnicas de los comités"),
         ("D. Mecanismos de participación", "20 talleres de colaboración (4 en el tramo 1, 8 en el tramo 2 y 8 en el tramo 3), 3 jornadas de información y 6 de consulta"),
         ("E. Enfoque de colaboración y co-creación", "Co-diseño de umbrales y protocolo en la actividad A3.1; validación del tablero con los comités; cartillas revisadas por los usuarios"),
         ("F. Articulación con el ciclo de ejecución", "La compuerta C1 exige uso del tablero por al menos 50 % de los comités del tramo 1; la C2 y el cierre verifican el avance hacia 75 %"),
         ("G. Sistematización", "Actas firmadas, bitácora de aprendizajes, informe por tramo y 29 actividades documentadas (PERS-P04)")],
        "*Nota.* Elaboración propia con el capítulo 16 del expediente. Las cantidades por tramo son PROPUESTAS.")
asc = lin("M04", "M05", "M06", "V05", "O02", "O06", "P05", "P11")
d.p("El presupuesto de apropiación social suma " + cop(asc) + ", equivalentes a " + num(asc / SGR_T * 100, 1) + " % del valor SGR. Incluye la coordinación y los profesionales sociales. Incluye también cartillas, kits de talleres y elementos de protección personal. Incluye la logística de ferias y las publicaciones de divulgación (líneas P05, P11, M04, M05, M06, V05, O02 y O06).")

# ============================================================== 20
d.raw("# 20. PRODUCTOS ESPERADOS")
d.p("La {T:t23} sigue la tabla del Anexo 2 con el programa 3906 del sector 39 de la MGA. Los productos y los indicadores se proponen con la clasificación del catálogo, que debe validarse en la plataforma MGA. No se repite ningún producto.")
d.tabla("t23", "Productos esperados (programa 3906)",
        ["Programa", "Producto", "Medido a través de", "Indicador de producto", "Unidad de medida"],
        [("3906", "Documentos de investigación", "Documentos de investigación elaborados", "2 artículos sometidos y al menos 1 aceptado (PERS-P03)", "Número"),
         ("3906", "Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos", "Prototipos generados", "1 red de 100 nodos y 10 gateways (PERS-P01); 1 software registrado (PERS-P02)", "Número"),
         ("3906", "Servicio de apoyo financiero para programas y proyectos de infraestructura científica y tecnológica", "Equipos de infraestructura científica adquiridos", "1 banco de calibración y 3 monitores de referencia", "Número"),
         ("3906", "Servicios de apoyo financiero para programas y proyectos de CTI que promueven la innovación, la transferencia tecnológica y el emprendimiento", "Convenios de transferencia firmados", "3 convenios de custodia, uno por tramo", "Número"),
         ("3906", "Documentos de política: documentos de planeación", "Documentos de planeación elaborados", "1 protocolo de alerta con umbrales validados localmente", "Número"),
         ("3906", "Servicio de apropiación social del conocimiento", "Actividades de apropiación realizadas", "29 actividades: 20 talleres y 9 jornadas (PERS-P04)", "Número"),
         ("3906", "Servicio de asistencia técnica", "Entidades asistidas técnicamente", "15 comités con tablero en uso; 60 personas certificadas (PERS-E03)", "Número"),
         ("3906", "Servicio de apoyo financiero para el fortalecimiento de las vocaciones científicas en CTI", "Jóvenes investigadores apoyados", "6", "Número"),
         ("3906", "Servicio de apoyo financiero para la formación de maestría, en modalidad de investigación", "Beneficiarios de maestría", "2", "Número"),
         ("3906", "Servicio de apoyo financiero de estancias de investigación", "No aplica", "No aplica", "—"),
         ("Productos adicionales", "Ninguno", "—", "—", "—")],
        "*Nota.* Elaboración propia con la ficha maestra y la tabla del Anexo 2. Los nombres de los indicadores MGA son PROPUESTOS y NO_VERIFICADOS frente al catálogo vigente.")

# ============================================================== 21
d.raw("# 21. CRONOGRAMA")
d.p("La {T:t24} muestra el tiempo de ejecución de cada actividad descrita en la sección 14. Los meses se calculan con el método de la ruta crítica sobre 104 semanas. La ruta crítica coincide con la duración del proyecto. Las actividades de administración se ejecutan durante los 24 meses.")
PROD = {"A0.1": "Equipo y convenios", "A1.1": "Plan de colocalización", "A1.2": "Lote 1 caracterizado", "A1.3": "Base de colocalización",
        "A1.4": "Modelo validado", "C1": "Decisión de ampliar", "A1.5": "Modelo por departamento", "A1.6": "Ensayo independiente",
        "A2.1": "Diseño de enlace", "A2.2": "Plataforma y firmware", "A2.3": "Tramo 2", "C2": "Decisión de consolidar", "A2.4": "Tramo 3",
        "A3.1": "Protocolo de alerta", "A3.2": "Tablero en uso", "A3.3": "Custodios y convenios", "A3.4": "Transferencia y cierre"}
enc = ["OE", "Producto", "Actividad"] + [str(m) for m in range(1, 25)]
filas = []
for oe in ("OE1", "OE2", "OE3"):
    for a in OE_ACT[oe]:
        i, f = meses(a)
        filas.append((oe, PROD.get(a, "Gestión"), a) + tuple("x" if i <= m <= f else "" for m in range(1, 25)))
d.tabla("t24", "Cronograma de actividades por mes", enc, filas,
        "*Nota.* Elaboración propia con el cronograma de la ficha maestra. x: mes de ejecución de la actividad. Los nombres de las actividades están en la {T:t16}. Los hitos H0 a H8 ocurren en los meses 2, 4, 10, 12, 16, 17, 19, 23 y 24.")

# ============================================================== 22
d.raw("# 22. ANÁLISIS DE RIESGOS")
d.p("La {T:t25} analiza los riesgos con las categorías del Anexo 2. La probabilidad y el impacto se expresan en las escalas de la plantilla. Se derivan de las escalas de 1 a 5 del análisis cuantitativo del expediente, que calcula una reserva de contingencia de 636 millones de COP.")
def prob(p): return "Raro" if p <= 1 else ("Improbable" if p == 2 else "Probable")
def imp(i): return "Mayor" if i >= 4 else ("Moderado" if i == 3 else "Menor")
TIPO = {"R-TEC-01": "Operacionales", "R-TEC-02": "Operacionales", "R-TEC-03": "Operacionales", "R-TEC-04": "Operacionales",
        "R-ORG-01": "Operacionales", "R-ORG-02": "Financieros", "R-EXT-01": "De calendario", "R-EXT-02": "Operacionales",
        "R-FIN-01": "De costos", "R-FIN-02": "Financieros", "R-JUR-01": "Legales", "R-DAT-01": "Operacionales"}
filas = []
for r in D.RISKS:
    filas.append((TIPO[r["id"]], r["desc"], prob(r["P"]), imp(r["I"]), r["respuesta"]))
filas.append(("Administrativos", "Retrasos en la contratación del personal del proyecto", "Improbable", "Moderado", "Iniciar con anticipación los procesos con la oficina jurídica de la Universidad y definir perfiles antes del acta de inicio."))
filas.append(("De calendario", "Incumplimiento en la entrega de actividades de la ruta crítica", "Improbable", "Moderado", "Seguimiento semanal de las 13 actividades críticas y compuertas con criterios objetivos."))
filas.append(("Sanitarios", "Exposición del personal de campo al polvo de los sitios de remoción", "Probable", "Moderado", "Elementos de protección personal (línea M06) y protocolos de seguridad en campo. El riesgo biológico de la plantilla no aplica."))
d.tabla("t25", "Análisis de riesgos", ["Tipo de riesgo", "Descripción del riesgo", "Probabilidad", "Impacto", "Medidas de mitigación"], filas,
        "*Nota.* Elaboración propia con los 12 riesgos cuantificados del capítulo 10 del expediente y tres riesgos adicionales PROPUESTOS. Escalas: probabilidad 1 raro, 2 improbable, 3 a 5 probable; impacto 4 y 5 mayor, 3 moderado, 1 y 2 menor.")

# ============================================================== 23
d.raw("# 23. INDICADORES DE GESTIÓN")
d.p("La {T:t26} incluye el indicador sugerido por el Anexo 2 y los cinco indicadores de gestión del sistema PERS. Los informes de gestión son trimestrales: cuatro por cada año, ocho en el proyecto.")
filas = [("Informes de supervisión del proyecto", "8 informes (número)", "Trimestral: meses 3, 6, 9, 12, 15, 18, 21 y 24")]
for r in IM.IND:
    if r["nivel"] == "R": filas.append((f"{r['cod']} {r['nombre']}", r["mf"], r["frecuencia"]))
d.tabla("t26", "Indicadores de gestión", ["Indicador", "Medida o meta", "Fecha de entrega de acuerdo con el cronograma"], filas,
        "*Nota.* Elaboración propia con los indicadores PERS-R01 a PERS-R06 de la ficha maestra. Los informes del Anexo 2 corresponden al cumplimiento de PERS-R06.")

# ============================================================== 24
d.raw("# 24. INDICADORES DE PRODUCTO")
d.p("La {T:t27} lista los indicadores de producto y de resultado, con su meta y su medio de verificación. Los indicadores de impacto se miden después del cierre.")
filas = []
for r in IM.IND:
    if r["nivel"] in ("P", "E", "S"): filas.append((r["cod"], r["nombre"], r["mf"], r["frecuencia"], r["verificacion"]))
d.tabla("t27", "Indicadores de producto, de efecto y de sostenibilidad", ["Código", "Indicador", "Meta", "Frecuencia", "Medio de verificación"], filas,
        "*Nota.* Elaboración propia con el sistema PERS de la ficha maestra. Las líneas base marcadas como VACIO se miden en el tramo 1.")

# ============================================================== 25
d.raw("# 25. ASPECTOS ÉTICOS")
d.p("El proyecto no experimenta con seres humanos ni con muestras biológicas. Su ética se concentra en cuatro frentes. El primero es el consentimiento informado de quienes participan en talleres y cuestionarios, que se recoge por escrito. El segundo es la protección de datos personales según la Ley 1581 de 2012 (Congreso de la República, 2012b). El tercero es la transparencia sobre el error de la medición, que el tablero muestra junto con cada valor. El cuarto es la seguridad del personal en los sitios de remoción.")
d.p("La Universidad somete el protocolo a su comité de ética [DATO_USUARIO: comité de ética y fecha del aval]. Los datos ambientales se abren con la cláusula de apertura. Los datos de personas permanecen restringidos y se publican solo resultados agregados. Las alertas del proyecto no sustituyen las decisiones de las autoridades de salud ni la medición regulatoria.")

# ============================================================== 26
d.raw("# 26. IDONEIDAD Y TRAYECTORIA DE LA ENTIDAD PROPONENTE Y DEMÁS PARTICIPANTES")
d.p("La {T:t28} describe el aporte individual de cada integrante de la alianza. El Anexo 2 exige tres tipos de aporte: financieros, técnicos o tecnológicos y de talento humano de alto nivel. La trayectoria de cada entidad está pendiente. Debe coincidir con la carta aval, el compromiso institucional y el modelo de gobernanza [DATO_USUARIO: trayectoria y soportes de cada entidad].")
d.tabla("t28", "Aportes de cada integrante de la alianza",
        ["Integrante", "Aporte financiero", "Aporte técnico o tecnológico", "Talento humano de alto nivel", "Trayectoria"],
        [("Universidad proponente", "1.100 millones de COP en especie (reconstruida; certificación pendiente)", "Laboratorios, banco de calibración y estaciones de trabajo", "Investigador principal (50 %), coinvestigadores y doctor en estancia posdoctoral", "[DATO_USUARIO: proyectos y grupo reconocido]"),
         ("Actor reconocido por MinCiencias", "[DATO_USUARIO: contrapartida, si aplica]", "Laboratorio y referencias gravimétricas", "Especialista en metrología y profesional en calidad del aire", "[DATO_USUARIO: reconocimiento y proyectos]"),
         ("Empresa aliada", "210 millones de COP en efectivo y 800 millones en especie", "Infraestructura en la nube, hardware IoT y plataforma", "Ingenieros de software, de firmware y de campo", "[DATO_USUARIO: experiencia de la empresa]"),
         ("Municipio focal y municipios focalizados", "Sin aporte (beneficiarios)", "Acceso a sitios y comités de gestión del riesgo", "Funcionarios de gestión del riesgo", "[DATO_USUARIO: trayectoria del comité]")],
        "*Nota.* Elaboración propia con la ficha maestra y la sección S.8. Las contrapartidas de la Universidad y de la empresa se verifican con las cartas de compromiso.")

# ============================================================== 27
d.raw("# 27. ANÁLISIS DE LICENCIAS Y PERMISOS")
d.p("La {T:t29} enumera los requerimientos previos o durante la ejecución. El proyecto no interviene recursos genéticos, ni especímenes, ni colecciones biológicas, ni adecuación de infraestructura. Las verificaciones dependen de la normativa vigente y de las autoridades competentes.")
d.tabla("t29", "Licencias, permisos y requerimientos",
        ["Requerimiento", "Aplica", "Responsable", "Momento", "Estado"],
        [("Licencia ambiental", "No aplica: no hay obra ni aprovechamiento de recursos", "—", "—", "NO_APLICA"),
         ("Acceso a recursos genéticos, colecciones biológicas y especímenes", "No aplica", "—", "—", "NO_APLICA"),
         ("Consulta previa con comunidades indígenas y afrodescendientes", "Por verificar si hay resguardos o consejos comunitarios en los sitios", "Municipios y Universidad", "Antes de instalar", "VACIO"),
         ("Consentimiento informado en talleres y cuestionarios", "Aplica", "Universidad", "Cada actividad", "PROPUESTO"),
         ("Autorización de tratamiento de datos personales (Ley 1581 de 2012)", "Aplica", "Universidad", "Antes de recoger datos", "PROPUESTO"),
         ("Autorización de los predios y sitios de instalación", "Aplica", "Municipios", "Meses 2 a 4", "VACIO"),
         ("Uso de espectro y homologación de equipos de radio (LoRa y enlace satelital)", "Verificar", "Empresa", "Antes de comprar", "NO_VERIFICADO"),
         ("Importación y nacionalización de equipos", "Aplica", "Empresa y Universidad", "Meses 1 a 18", "PROPUESTO"),
         ("Licencia urbanística para mástiles y obra menor", "Verificar con la curaduría o la secretaría de planeación", "Empresa y municipios", "Antes de instalar", "NO_VERIFICADO"),
         ("Decreto 1203 de 2017 (adecuación de infraestructura)", "No aplica: sin adecuación de infraestructura", "—", "—", "NO_APLICA")],
        "*Nota.* Elaboración propia con la lista de ejemplos del Anexo 2. Las normas de espectro y de licencias urbanísticas no se consultaron en esta corrida.")

# ============================================================== 28
d.raw("# 28. RESUMEN DE FUENTES DE FINANCIACIÓN")
d.p("La {T:t30} resume las fuentes de financiación. El aporte de cada cooperante coincide con el presupuesto y debe coincidir con la carta aval, el compromiso institucional y el modelo de gobernanza.")
d.tabla("t30", "Resumen de fuentes de financiación",
        ["Entidad", "Fuente de recursos", "Valor"],
        [("Asignación de CTeI del SGR", "Asignación de CTeI del SGR", cop(SGR_T)),
         ("Entidad proponente: Universidad", "Propios, en especie", cop(con_ies := sum(r["total"] for r in D.CONTRA if r["fuente"] == "IES"))),
         ("Entidad aliada: empresa", "Propios, en efectivo (210 millones) y en especie (800 millones)", cop(sum(r["total"] for r in D.CONTRA if r["fuente"] == "EMP"))),
         ("Entidad aliada: actor reconocido por MinCiencias", "Propios [DATO_USUARIO: valor, si aplica]", "$ 0"),
         ("Total", "", cop(TOT_T))],
        "*Nota.* Elaboración propia con la ficha maestra (CALCULADO). La contrapartida de la Universidad es una reconstrucción PROPUESTA y la de la empresa es DECLARADA en el expediente E3.")
d.p("Los valores incorporan los ajustes de la verificación presupuestal. La contrapartida del actor reconocido queda en blanco hasta que la alianza la defina.")
d.p("**Valor total de recursos solicitados a la Asignación de CTeI del SGR:** " + pesos_letras(SGR_T) + ".")
d.p("**Valor total contrapartida:** " + pesos_letras(CON_T) + ".")
d.p("**Valor total del proyecto:** " + pesos_letras(TOT_T) + ".")

d.guardar(os.path.join(RAIZ, "caps", "a2c.md"))

# ============================================================== 30 (archivo aparte, después de la bibliografía)
e = Doc("D")
e.raw("# 30. ANEXOS REQUISITOS SECTORIALES QUE LE SEAN APLICABLES")
e.p("La {T:t31} lista los anexos que el Anexo 2 menciona y su estado. Los documentos exigidos por los términos de referencia no se aportaron al proyecto. El expediente de formulación que sigue a esta sección contiene los análisis de soporte y los anexos técnicos A a N.")
e.tabla("t31", "Anexos requeridos y estado",
        ["Anexo", "Contenido", "Estado"],
        [("Carta aval, compromiso institucional y modelo de gobernanza", "Compromiso de cada integrante de la alianza y reglas de decisión", "VACIO: se obtiene en la reunión con la Universidad"),
         ("Anexo 4", "Plan bienal de convocatorias: retos estratégicos y demandas territoriales", "VACIO: no aportado"),
         ("Anexo 10", "Lineamientos para integrar la apropiación social del conocimiento", "VACIO: no aportado"),
         ("Anexo 12", "Categorías de enfoque diferencial e interseccional del personal", "VACIO: no aportado"),
         ("Reporte oficial de afectación y lista de municipios afectados", "Soporte de la demanda territorial", "VACIO: no aportado"),
         ("Requisitos sectoriales aplicables", "Los que fijen los términos de referencia", "VACIO"),
         ("Expediente de formulación (anexos A a N, capítulo 20)", "Análisis de soporte, trazabilidad y verificadores", "Incluido a continuación")],
        "*Nota.* Elaboración propia con el Anexo 2 de la convocatoria.")
e.guardar(os.path.join(RAIZ, "caps", "a2d.md"))
print("a2c y a2d ok")
