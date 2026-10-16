# -*- coding: utf-8 -*-
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

d = Doc("20")
M = D.M
R = D.resumen()
SGR = R["sgr"]
sgr = [r for r in D.BUDGET if r["fuente"] == "SGR"]

d.h(1, "Capítulo 20. Anexos Técnicos")
d.p("Este capítulo reúne los anexos que acompañan el documento técnico. Los anexos A a J corresponden a la lista del metaprompt. Los anexos K a M documentan el análisis estructural y la trazabilidad de los archivos. El anexo N cruza el documento con el Anexo 2 de la convocatoria. Para cada anexo de la lista A a J, el capítulo entrega el requisito, la estructura mínima y el estado. Indica también su vínculo con el resto del documento. Los documentos que solo poseen el usuario o terceros, como cartas, hojas de vida y cotizaciones, no se fabrican. Aparecen con su estado VACIO y con la información que cada uno debe contener.")
d.p("Dos reglas rigen los anexos. Ningún anexo sustituye un dato con una estimación sin declararlo. Toda cifra que provenga de otro capítulo conserva su naturaleza. Un documento entregado queda registrado en el anexo I con su huella SHA-256, de modo que cualquier cambio posterior sea detectable.")

# ---------------------------------------------------------------- A
d.h(2, "Anexo A. Cartas de compromiso y avales")
d.p("Las cartas de compromiso son la evidencia de que la alianza existe. El Anexo 2 de la convocatoria exige coherencia entre los aportes de cada integrante y tres documentos. Son la carta aval, el compromiso institucional y el modelo de gobernanza. Ninguna carta se aportó. La alianza entre la entidad ejecutora y la empresa tecnológica es un supuesto por instrucción del usuario. El metaprompt exige un control jurídico de las cartas. Emite una alerta de compromiso débil cuando una carta no fija objeto, aporte, vigencia, partida y representante facultado. La alerta persiste hasta el checklist final del documento 1000X-10. La {T:a01} registra los documentos requeridos y su estado.")
filas = [
 ("A1", "Institución de educación superior ejecutora", "Carta aval, compromiso institucional y certificación de la contrapartida en especie de 1.100 millones de COP", "Objeto; aportes de personal y laboratorios; vigencia de 24 meses; representante legal", "VACIO", "Activa"),
 ("A2", "Empresa tecnológica aliada", "Carta de compromiso y certificación de 210 millones de COP en efectivo y 800 millones en especie", "Objeto; aportes valorados; acuerdo de titularidad de la propiedad intelectual; vigencia", "VACIO", "Activa"),
 ("A3", "Alcaldías de los 12 municipios focalizados", "Cartas de intención de custodia con partida presupuestal por tramo", "Objeto; función de custodia; partida del plan operativo anual; vigencia que supere el cierre", "VACIO", "Activa; sin partida el compromiso es débil"),
 ("A4", "Gobernaciones de Caldas, Cundinamarca y Valle del Cauca", "Cartas de articulación con las unidades de gestión del riesgo y con el plan de desarrollo", "Objeto; articulación con el PDD; designación de interlocutor", "VACIO", "Activa"),
 ("A5", "Unidad Nacional para la Gestión del Riesgo de Desastres", "Carta de articulación del protocolo con el sistema nacional", "Objeto; articulación del protocolo de alerta; designación de interlocutor", "VACIO", "Activa"),
 ("A6", "Comités de gestión del riesgo (15)", "Cartas de participación en el co-diseño y el uso piloto", "Objeto; compromiso de sesiones periódicas; designación de personal", "VACIO", "Activa"),
 ("A7", "Autoridades ambientales", "Convenio de acceso a estaciones oficiales para contraste, si aplica", "Objeto; datos compartidos; vigencia", "VACIO", "No aplica hasta definir"),
 ("A8", "Laboratorio acreditado y laboratorio externo", "Cartas de intención de servicio gravimétrico y de ensayo de desempeño", "Objeto; acreditación; plazo; valor de referencia", "VACIO", "Activa")]
d.tabla("a01", "Registro de cartas de compromiso y avales requeridos con alerta de compromiso débil",
        ["Id", "Entidad", "Documento requerido", "Contenido mínimo", "Estado", "Alerta"], filas,
        "*Nota.* Elaboración propia con la ficha maestra §1 y §5, el análisis de participantes de la sección 4.4-MDR.5 y el Anexo 2 de la convocatoria (secciones 26 y 28). PDD: Plan de Desarrollo Departamental. Todos los documentos están en estado VACIO; los nombres de las entidades se definen por el usuario [DATO_USUARIO: nombres y representantes legales].")
d.p("El orden de las alertas indica la prioridad de gestión. Las cartas de las alcaldías son las más débiles, porque sin partida presupuestal la custodia no tiene respaldo. La compuerta C2 exige convenios de custodia con partida, de modo que ese vacío bloquea el tramo 3. La {T:a02} define la estructura mínima de una carta de compromiso para que ninguna llegue incompleta.")
d.tabla("a02", "Estructura mínima de una carta de compromiso (modelo ILUSTRATIVO)",
        ["Campo", "Contenido requerido", "Dato"],
        [("Encabezado", "Entidad que compromete y representante legal facultado", "[DATO_USUARIO: nombre, cargo y documento]"),
         ("Objeto", "Título del proyecto, convocatoria y alcance del compromiso", "Título del proyecto y Decreto 1414 de 2026"),
         ("Aporte", "Tipo (efectivo, especie, técnico, talento humano), descripción y valor en COP", "[DATO_USUARIO: valor y descripción]"),
         ("Partida", "Rubro y vigencia presupuestal donde consta el aporte", "[DATO_USUARIO: código de partida]"),
         ("Vigencia", "Fechas de inicio y fin, con cobertura de los 24 meses y, para custodios, de los 12 meses posteriores", "[DATO_USUARIO: fechas]"),
         ("Titularidad", "Reglas de propiedad intelectual sobre software, datos y marca", "[DATO_USUARIO: proporción acordada]"),
         ("Responsable", "Persona interlocutora designada", "[DATO_USUARIO: nombre y contacto]"),
         ("Firma y fecha", "Firma del representante legal y fecha", "[DATO_USUARIO: firma y fecha]")],
        "*Nota.* Elaboración propia. El modelo es ILUSTRATIVO y no sustituye el formato de la convocatoria, que no se aportó. Los campos entre corchetes son VACIO.")

# ---------------------------------------------------------------- B
d.h(2, "Anexo B. Hojas de vida completas")
d.p("Las hojas de vida acreditan que el equipo tiene la capacidad que el presupuesto supone. El presupuesto de personal incluye 29 cargos y 624 persona-mes. Ninguna hoja de vida se aportó, porque los nombres quedan por definir. La {T:a03} lista los cargos con el perfil mínimo propuesto y la evidencia que cada persona debe presentar. Los perfiles son PROPUESTO y requieren ratificación de la entidad ejecutora y de los términos de referencia.")
perfil = {
 "P01": "Profesional recién graduado en ingeniería, ciencias ambientales o estadística; formación en investigación",
 "P02": "Profesional con admisión a maestría en un programa afín; dedicación al proyecto",
 "P03": "Doctorado o maestría con experiencia en series ambientales, aprendizaje automático y calibración de sensores",
 "P04": "Ingeniería electrónica, de telecomunicaciones o similar; experiencia en instalación de redes IoT",
 "P05": "Profesional en ciencias sociales o comunicación con experiencia en procesos de participación",
 "P06": "Profesional con experiencia en gerencia de proyectos de ciencia, tecnología e innovación con recursos públicos",
 "P07": "Ingeniería o física con experiencia en metrología, medición gravimétrica y trazabilidad",
 "P08": "Ingeniería de sistemas o software con experiencia en plataformas en la nube y ciberseguridad",
 "P09": "Ingeniería electrónica con experiencia en firmware y gestión de energía solar",
 "P10": "Técnico o tecnólogo con experiencia en mantenimiento de equipos de campo; residencia en el departamento",
 "P11": "Profesional en ciencias sociales con experiencia en co-diseño comunitario",
 "P12": "Profesional con experiencia en datos espaciales, interpolación y gemelos digitales",
 "P13": "Profesional en salud ambiental o calidad del aire con experiencia en índices y alertas",
 "P14": "Profesional en derecho o administración con experiencia en convenios y propiedad intelectual"}
fb = []
for r in sgr:
    if r["id"].startswith("P"):
        fb.append((r["id"], r["concepto"], num(r["cant"]), perfil[r["id"]], "Hoja de vida; CvLAC si aplica; soportes de formación y experiencia", "VACIO"))
for r in D.CONTRA[:3]:
    fb.append((r["id"], r["concepto"] + " (contrapartida)", num(r["cant"]) + " " + r["unidad"], "Investigación principal y coinvestigación con trayectoria verificable en CvLAC y GrupLAC", "Hoja de vida; CvLAC; GrupLAC", "VACIO"))
d.tabla("a03", "Cargos del proyecto con perfil mínimo propuesto y evidencia requerida",
        ["Id", "Cargo", "Cantidad", "Perfil mínimo (PROPUESTO)", "Evidencia requerida", "Estado"], fb,
        "*Nota.* Elaboración propia con datos de maestro.py (líneas P01 a P14 y C01 a C03). La cantidad de los cargos del SGR es en persona-mes. CvLAC y GrupLAC: plataformas de MinCiencias. Los perfiles son PROPUESTO; las hojas de vida son VACIO [DATO_USUARIO: hojas de vida en el formato exigido]. Decimales con coma.")
d.p("Las hojas de vida se evaluarán contra el perfil de cada cargo. Si una persona no cumple el perfil mínimo, el cargo se reabre con un proceso de selección. El cambio se registra como modificación del equipo. El enfoque diferencial del Anexo 2 pide indicar si más de 50 % del equipo pertenece a una categoría de población diferencial. Ese dato depende del Anexo 12 de la convocatoria, que no se aportó, y por ahora queda sin determinar.")

# ---------------------------------------------------------------- C
d.h(2, "Anexo C. Cotizaciones de equipos")
d.p("Las cotizaciones respaldan los costos unitarios del presupuesto. Ningún costo unitario del presupuesto tiene cotización soportada. Los valores marcados DECLARADO provienen del expediente revisado, y los marcados PROPUESTO provienen de esta formulación. Por esa razón, 100 % del valor solicitado carece hoy de soporte de mercado. La {T:a04} lista las líneas de equipos y las demás líneas de mayor valor que requieren cotización. Para cada una indica el tipo de soporte exigido.")
cot = []
total_cot = 0
for r in sgr:
    if r["rubro"] == "Equipos y software" or (r["total"] >= 80 * M and r["rubro"] in ("Servicios técnicos", "Materiales e insumos")):
        total_cot += r["total"]
        tipo = "Tres cotizaciones comparables de proveedores distintos" if r["total"] >= 80 * M else "Una cotización vigente del proveedor"
        cot.append((r["id"], r["concepto"], f"{num(r['cant'], 0 if float(r['cant']).is_integer() else 1)} {r['unidad']}", cop(r["vunit"]), cop(r["total"]), r["nat"], tipo))
cot.append(("Total", "Líneas que requieren cotización", "", "", cop(total_cot), "CALCULADO", f"{num(100 * total_cot / SGR, 1)} % del valor solicitado al SGR"))
d.tabla("a04", "Líneas del presupuesto que requieren cotización y tipo de soporte",
        ["Id", "Concepto", "Cantidad", "Costo unitario (COP)", "Total (COP)", "Naturaleza", "Soporte requerido"], cot,
        "*Nota.* Elaboración propia con datos de maestro.py. Se incluyen todas las líneas de equipos y software, y las líneas de servicios técnicos y de materiales de 80 millones de COP o más. Las cotizaciones son VACIO [DATO_USUARIO: cotizaciones vigentes con fecha y proveedor]. Decimales con coma y miles con punto.")
d.p("Las cotizaciones deben llevar fecha, proveedor, vigencia, moneda y condiciones de entrega. Para equipos importados, la cotización debe indicar el tipo de cambio de referencia, porque el riesgo R-FIN-01 depende de él. La compra del tramo 1 ocurre en el mes 5. Las cotizaciones deben tener vigencia hasta esa fecha o renovarse. Si el costo real difiere más de 10 % de lo presupuestado, la gerencia informa al comité directivo. El comité decide si ajusta el tamaño del tramo.")

# ---------------------------------------------------------------- D
d.h(2, "Anexo D. Certificados de grupos de investigación")
d.p("Los grupos de investigación vinculados acreditan la capacidad científica del proyecto. El Anexo 2 de la convocatoria pide cuatro datos por grupo. Son el nombre, la entidad, las líneas de investigación y el número de investigadores con su nivel de formación. Indica además que se tendrán en cuenta los resultados de la convocatoria 894 de 2021 de reconocimiento y medición de grupos. Ningún dato de grupo se aportó. La {T:a05} reserva la estructura.")
d.tabla("a05", "Registro de grupos de investigación vinculados",
        ["Campo", "Contenido requerido", "Dato"],
        [("Nombre del grupo", "Nombre registrado en GrupLAC", "[DATO_USUARIO: nombre del grupo]"),
         ("Entidad", "Entidad a la que pertenece el grupo", "[DATO_USUARIO: entidad]"),
         ("Categoría de reconocimiento", "Resultado de la convocatoria 894 de 2021", "[DATO_USUARIO: categoría]"),
         ("Líneas de investigación", "Líneas a las que se vincula el proyecto", "[DATO_USUARIO: líneas]"),
         ("Investigadores y formación", "Número de investigadores y nivel de formación", "[DATO_USUARIO: número y nivel]"),
         ("Certificado", "Certificado de vigencia del grupo", "[DATO_USUARIO: certificado]")],
        "*Nota.* Elaboración propia con el Anexo 2 de la convocatoria, sección 1. Todos los datos son VACIO. Un proyecto puede vincular varios grupos; la tabla se repite por grupo.")

# ---------------------------------------------------------------- E
d.h(2, "Anexo E. Instrumentos de recolección")
d.p("Los instrumentos recogen los datos que alimentan los indicadores. Cada indicador de la ficha tiene una fuente y un instrumento. Seis instrumentos cubren los indicadores con línea base VACIO y los de mayor riesgo. La {T:a06} define sus campos mínimos. Los instrumentos son PROPUESTO y requieren validación antes del tramo 1. Davis (1989) y Venkatesh et al. (2003) sustentan que el uso de un sistema se mide con tres constructos. Son la utilidad percibida, la facilidad de uso y la intención de uso. El instrumento E5 los incorpora.")
filas = [
 ("E1", "Bitácora de colocalización", "PERS-R05, PERS-R02", "Nodo y sitio; fecha y hora; lectura del nodo; lectura de la referencia; humedad relativa; temperatura; marca de calidad del dato; técnico responsable", "Diaria, automática", "Especialista en metrología"),
 ("E2", "Acta de comité con decisión basada en el tablero", "PERS-E01", "Comité y municipio; fecha; lectura del tablero consultada; decisión adoptada; responsable; seguimiento", "Trimestral", "Coordinación de apropiación social"),
 ("E3", "Registro de alertas y verificación", "PERS-E02", "Alerta emitida; nodo; valor del tablero; valor de la referencia; confirmación de superación; clasificación de falsa alarma", "Por evento", "Profesional en calidad del aire"),
 ("E4", "Evaluación práctica de custodios", "PERS-E03", "Persona y entidad; módulo (mantenimiento, lectura, operación); criterios aprobados; puntaje; evaluador", "Por cohorte", "Profesional de convenios y custodia"),
 ("E5", "Cuestionario de uso del tablero", "PERS-E01", "Utilidad percibida; facilidad de uso; confianza en la medición; intención de uso; escala de 1 a 5 (PROPUESTO)", "Semestral", "Coordinación de apropiación social"),
 ("E6", "Registro de eventos de superación y medidas", "PERS-S01", "Evento confirmado; fecha; medida de protección activada; responsable; evidencia", "Por evento", "Custodios y secretarías de gestión del riesgo")]
d.tabla("a06", "Instrumentos de recolección con campos mínimos y periodicidad",
        ["Id", "Instrumento", "Indicador PERS", "Campos mínimos", "Periodicidad", "Responsable"], filas,
        "*Nota.* Elaboración propia con la ficha maestra §8 e indicadores.py. Los campos y las escalas son PROPUESTO. Los ítems del cuestionario E5 no se redactaron y requieren validación de contenido [DATO_USUARIO: instrumentos validados por la entidad ejecutora].")
d.p("Los instrumentos usan registros automáticos siempre que es posible. La bitácora de colocalización se alimenta de la plataforma y no exige captura manual. Las actas y los cuestionarios sí exigen captura, y por eso son los más expuestos a pérdida de datos. La mitigación es que la coordinación de apropiación social recoja las actas en cada sesión y las digitalice en una semana. La validación de los instrumentos se completa antes de la compuerta C1, y los resultados del tramo 1 ajustan los campos.")

# ---------------------------------------------------------------- F
d.h(2, "Anexo F. Consentimientos informados")
d.p("El consentimiento informado protege a las personas cuyos datos y opiniones el proyecto recoge. La Ley 1581 de 2012 exige autorización previa, expresa e informada del titular para tratar datos personales (Congreso de la República, 2012b). El proyecto recoge datos de asistencia a talleres, opiniones en encuestas, imágenes en jornadas públicas y ubicaciones de los nodos, que pueden asociarse con viviendas. La {T:a07} define los elementos del formulario de consentimiento. El texto final y su aprobación por un comité de ética son pendientes [DATO_USUARIO: acta del comité de ética o equivalente].")
d.tabla("a07", "Elementos mínimos del formulario de consentimiento informado",
        ["Elemento", "Contenido", "Aplicación en el proyecto"],
        [("Identificación del responsable", "Entidad ejecutora y contacto para ejercer derechos", "[DATO_USUARIO: razón social y contacto]"),
         ("Finalidad", "Para qué se recogen los datos y por cuánto tiempo", "Co-diseño de umbrales, evaluación de uso y seguimiento del proyecto"),
         ("Datos recogidos", "Lista de datos y su carácter sensible o no", "Nombre, institución, cargo, opiniones; sin datos de salud"),
         ("Voluntariedad", "Participar no es obligatorio y se puede retirar el consentimiento", "Aplica a talleres, encuestas y jornadas"),
         ("Derechos del titular", "Conocer, actualizar, rectificar y suprimir los datos", "Canal de atención definido por la entidad ejecutora"),
         ("Uso de imágenes", "Autorización separada para fotografías y grabaciones", "Aplica a jornadas públicas y laboratorios ciudadanos"),
         ("Menores y poblaciones diferenciales", "Autorización del representante y adaptación del formato", "Aplica cuando participen menores o comunidades étnicas"),
         ("Firma y fecha", "Firma, huella o registro electrónico", "[DATO_USUARIO: mecanismo de aceptación]")],
        "*Nota.* Elaboración propia con la Ley 1581 de 2012 y el análisis de licencias y permisos del Anexo 2 (sección 27). El formulario completo es VACIO. Naturaleza de los elementos: PROPUESTO.")
d.p("El proyecto planea 20 talleres de co-diseño y 9 jornadas públicas, que suman 29 actividades de apropiación social. Cada una requiere un formulario por participante o un registro colectivo con autorización. Las lecturas de los nodos no son datos personales en sí mismas, pero su ubicación puede serlo si identifica una vivienda. Por eso la plataforma publica las lecturas agregadas por zona y protege las coordenadas exactas, y la auditoría de ciberseguridad verifica esa regla.")

# ---------------------------------------------------------------- G
d.h(2, "Anexo G. Presupuesto detallado (formato entidad)")
d.p("El presupuesto detallado por línea está en el capítulo 8, en las Tablas 8.3, 8.5 y 8.7 a 8.10. Este anexo presenta dos cruces que el formato de la entidad suele exigir. El primero es el valor por rubro y semestre. El segundo es el valor por paquete de trabajo y rubro. La {T:a08} distribuye el valor solicitado al SGR por semestre y la {T:a09} lo distribuye por paquete.")
fl = D.flujo_sgr()
rub_sem = collections.OrderedDict()
for r in sgr:
    if r["id"] in ("E01", "E02", "E04"): continue
    ps = D.por_periodo(D.spread(r), 6)
    acc = rub_sem.setdefault(r["rubro"], [0.0] * 4)
    for i, v in enumerate(ps): acc[i] += v
eq_tr = D.por_periodo(D.flujo_equipos_por_tramo(), 6)
for i, v in enumerate(eq_tr): rub_sem["Equipos y software"][i] += v
fil8 = []
for k in ["Personal", "Equipos y software", "Materiales e insumos", "Servicios técnicos", "Viajes y viáticos", "Otros rubros", "Reserva de contingencia"]:
    v = rub_sem[k]
    fil8.append((k,) + tuple(mm(x) for x in v) + (mm(sum(v)),))
tot_sem = [sum(rub_sem[k][i] for k in rub_sem) for i in range(4)]
fil8.append(("Total SGR",) + tuple(mm(x) for x in tot_sem) + (mm(sum(tot_sem)),))
assert abs(sum(tot_sem) - SGR) < 5
d.tabla("a08", "Valor solicitado al SGR por rubro y semestre, en millones de COP",
        ["Rubro", "Semestre 1", "Semestre 2", "Semestre 3", "Semestre 4", "Total"], fil8,
        "*Nota.* Elaboración propia con datos de maestro.py (spread y flujo de equipos por tramo). Las compras de nodos, cabezales y gateways se asignan a los meses 5, 13 y 18. Los totales por semestre son 2.557,9; 1.804,7; 2.497,2 y 1.869,9 millones de COP. Naturaleza: CALCULADO. Decimales con coma.")
wp = collections.OrderedDict((k, collections.OrderedDict()) for k in ["WP0", "WP1", "WP2", "WP3"])
for r in sgr:
    wp[r["wbs"]][r["rubro"]] = wp[r["wbs"]].get(r["rubro"], 0) + r["total"]
rubs = ["Personal", "Equipos y software", "Materiales e insumos", "Servicios técnicos", "Viajes y viáticos", "Otros rubros", "Reserva de contingencia"]
fil9 = []
for k, v in wp.items():
    fil9.append((k,) + tuple(mm(v.get(x, 0)) for x in rubs) + (mm(sum(v.values())),))
fil9.append(("Total",) + tuple(mm(sum(wp[k].get(x, 0) for k in wp)) for x in rubs) + (mm(SGR),))
d.tabla("a09", "Valor solicitado al SGR por paquete de trabajo y rubro, en millones de COP",
        ["WP", "Personal", "Equipos", "Materiales", "Servicios", "Viajes", "Otros", "Reserva", "Total"], fil9,
        "*Nota.* Elaboración propia con datos de maestro.py (campo wbs de cada línea). Equipos: equipos y software; Materiales: materiales e insumos; Servicios: servicios técnicos; Viajes: viajes y viáticos; Otros: otros rubros; Reserva: reserva de contingencia. La reserva se asigna a WP0. Naturaleza: CALCULADO. Decimales con coma.")
d.p("El formato de la entidad puede exigir códigos presupuestales propios, que la ficha no contiene [DATO_USUARIO: códigos presupuestales del formato de la entidad]. El archivo de hoja de cálculo reúne las 54 líneas del SGR y las seis de contrapartida. Se genera a partir del libro maestro cuando el usuario fije el formato.")

# ---------------------------------------------------------------- H
d.h(2, "Anexo H. Cronograma detallado")
d.p("El cronograma detallado asigna cada actividad a los trimestres de ejecución. La {T:a10} cruza las 17 actividades con los ocho trimestres y marca con una X los trimestres en los que cada actividad está en curso. Las semanas son las del cálculo de la ruta crítica del capítulo 9. El archivo de Microsoft Project o de hoja de cálculo se genera desde el libro maestro cuando el usuario fije el formato. El Anexo 2 pide que el número de actividades del cronograma coincida con el de la metodología y la cadena de valor.")
fil10 = []
for k in sorted(D.ACTS, key=lambda z: (D.ACTS[z]["ES"], z)):
    a = D.ACTS[k]
    marcas = []
    for q in range(8):
        a0, b0 = q * 13.0, (q + 1) * 13.0
        marcas.append("X" if (a["ES"] < b0 and a["EF"] > a0) else "")
    nom = {x[0]: x[1] for x in D.ACT}[k]
    fil10.append((k, nom, a["wp"], str(a["ES"]), str(a["EF"])) + tuple(marcas))
d.tabla("a10", "Cronograma detallado por actividad y trimestre",
        ["Id", "Actividad", "WP", "Semana inicial", "Semana final", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"], fil10,
        "*Nota.* Elaboración propia con datos de maestro.py (ACTS). Cada trimestre equivale a 13 semanas. X: la actividad está en curso durante al menos una semana del trimestre. Naturaleza: CALCULADO sobre duraciones PROPUESTO.")
d.p("La actividad de administración y apoyo a la supervisión que el Anexo 2 exige por objetivo no figura como actividad separada en la red. Está distribuida en el paquete WP0 y en la línea O05 del presupuesto. El anexo N propone separarla en tres actividades, una por objetivo, antes de la radicación, con los mismos valores del presupuesto.")

# ---------------------------------------------------------------- I
d.h(2, "Anexo I. Estudios previos")
d.p("Los estudios previos son los documentos que sustentan la formulación. Se registran con su huella SHA-256 para que cualquier modificación sea detectable. Los tres primeros son entradas que aportó el usuario. Los siguientes son productos de esta corrida. Dos entradas llegaron después de la primera entrega: el metaprompt completo y el Anexo 2 de la convocatoria. La {T:a11} registra cada estudio con su alcance y su estado.")
fil11 = [
 ("Problematica_E3-P00.docx", "Expediente E3-P00 con pasos 1 a 6 y capítulos del usuario", "Entrada del usuario", "ad06c90bd70a4d9217567f8eb4aff4771f3c92b5d961b7e60e8d90a126bd6801", "DECLARADO; revisado en 36 hallazgos"),
 ("informe_FINAL.docx", "Vigilancia tecnológica y bibliometría de 42 documentos", "Entrada del usuario", "29f443a909e831b751fb39f0f43d5aec838a55177b32a5a89eb34cbbd7b4fc0b", "DECLARADO; no verificado de forma independiente"),
 ("Vester_MICMAC_Plantilla_15_vacia.xlsx", "Plantilla de 15 variables para el análisis estructural", "Entrada del usuario", "9155d355c7cc29b02eeb2c64b826768deb605a3bac6e59a84c87b2927ede1497", "Plantilla vacía"),
 ("anexo_2._documento_tecnico_15.docx", "Anexo 2 de la convocatoria: documento técnico", "Entrada del usuario", "f2b93ddb5ed2937ac624d7d33f69bbae1a9a50976ae4d55d023fd668bc920699", "DECLARADO; recibido después de la primera entrega"),
 ("GENESIS_CTeI_v36_10_RC2 (XML completo)", "Metaprompt GENESIS-CTeI 36.10 RC2", "Entrada del usuario", "9838e6d8318c5a7c0b209bdeb029ac806fbe635de7c97dac72800ed42e3b1260", "Archivo completo; la huella del texto extraído en la primera corrida era 685a73f45ba1d3011a3b1ba3a1722482c46d8b9a68ffe5cbc4dbe131e4603ba8"),
 ("00_INFORME_DE_REVISION_E3-P00.md", "Revisión del expediente: 36 hallazgos, compuertas GS-01 a GS-08", "Producto de la corrida", "464e140dcff3bacb9943636646445b43e9ec838f203449ab003ef267fddd4ee2", "Borrador con vacíos"),
 ("01_ADMISION_TV1_GATE0_Y_ALCANCE.md", "Admisión TV-1, Gate 0 y alcance", "Producto de la corrida", "3ed7940d51c80a6bc857ec5e517675c50c3a499cf0aaac1e7f07e2ed02113ad4", "Gate 0 no aprobado"),
 ("SECCION_4_3_SGR_CONV56_AIRE.md", "Clasificación de variables para inferencia causal", "Producto de la corrida", "819ac18380f5957060adabdc7b04ffbcc44b835f1d6d00114035792307417ab4", "Borrador con vacíos"),
 ("SECCION_4_4_SGR_CONV56_AIRE.md", "Vester y MICMAC paritario: 105 fichas, cinco escenarios", "Producto de la corrida", "623ae50cf0472b7bf6b4a38283ad733713d1b85dd0acbad39fd477e6eac516ea", "Sin ratificación de fichas"),
 ("SECCION_4_4_MDR_SGR_CONV56_AIRE.md", "Metodología integrada de decisión y resolución", "Producto de la corrida", "534e3535d16e81318c0918ad547dbb8a35ccb9e7d6d5a3052e570cf502bdf5ad", "Probabilidades sin fuente"),
 ("EXPEDIENTE_MDR_SGR_CONV56_AIRE.md", "Expediente técnico de 4.4-MDR (K01 a K32, S01 a S40)", "Producto de la corrida", "ab1fb035d5862c602c7944d88872c5b8547fdbca57df829a014bb67ad00a0fe2", "Borrador con vacíos"),
 ("SECCION_4_5_SGR_CONV56_AIRE.md", "Árbol de problemas A-PROB", "Producto de la corrida", "a34185340e5924e71e812fe96eb9ba0ac86b5ec5ce10fbdc9922a23a84e580b3", "Borrador con vacíos"),
 ("RESPALDO_SGR_CONV56_AIRE_CP_20261013_E4_4_5_01.zip", "Respaldo de continuidad con inventario y huellas", "Producto de la corrida", "9453917c8301d109f24a79bf340a288fef8a8b4ef5dc408240d04277e8d58ed2", "Vigente"),
 ("DOCUMENTO_UNIFICADO_SGR_CONV56_AIRE.docx", "Documento unificado de las secciones 4.3 a 4.5 (vista derivada)", "Producto de la corrida", "d1013c4dca9702fab42b811a5d9859112d674ed8283be65adae2a5f1fc7a90d5", "Vista derivada"),
 ("DOCUMENTO_UNIFICADO_SGR_CONV56_AIRE.pdf", "Versión de lectura fija del documento unificado", "Producto de la corrida", "08f9ce77802f0733ecc863471e157bdcc066a8160c66f14af76d31f1731296d0", "Vista derivada")]
d.tabla("a11", "Registro de estudios previos con huella SHA-256",
        ["Archivo", "Alcance", "Origen", "SHA-256", "Estado"], fil11,
        "*Nota.* Elaboración propia. Las huellas se calcularon con SHA-256 sobre los archivos tal como están en el repositorio y en la entrega del usuario. La diferencia entre las dos huellas del metaprompt se explica porque la primera corrida extrajo el texto de la conversación y no el archivo completo; no se afirma equivalencia entre ambas.")
d.p("El registro muestra que la formulación descansa en cinco insumos del usuario y en diez productos de la corrida. Ningún insumo del usuario se verificó de forma independiente. El expediente E3-P00 se revisó y se corrigió en 36 hallazgos, pero sus cifras no corregidas siguen DECLARADO. El informe de vigilancia tecnológica sustenta el estado del arte. Su corpus de 42 documentos incluye patentes y artículos de 2025 y 2026 que se citan con la página del informe.")

# ---------------------------------------------------------------- J
d.h(2, "Anexo J. Otros documentos según convocatoria")
d.p("El Anexo 2 de la convocatoria remite a otros documentos que forman parte de los términos de referencia. Esos documentos no se aportaron y condicionan elementos de la formulación. La {T:a12} los lista con la sección del Anexo 2 que los menciona y el efecto de su ausencia.")
fil12 = [
 ("J1", "Términos de referencia completos de la convocatoria", "Notas generales; secciones 8 y 14", "Línea temática, alcance de los componentes, topes y rubros admisibles sin verificar"),
 ("J2", "Anexo 4: plan bienal de convocatorias 2023-2024, retos y demandas territoriales", "Sección 8", "La demanda territorial del proyecto queda sin código"),
 ("J3", "Anexo 10: lineamientos para el enfoque de apropiación social del conocimiento", "Sección 19", "La estrategia de ASC se formuló con el metaprompt y no con el anexo"),
 ("J4", "Anexo 12: categorías de enfoque diferencial e interseccional", "Sección 11.4", "El porcentaje de equipo con enfoque diferencial queda sin determinar"),
 ("J5", "Carta aval, compromiso institucional y modelo de gobernanza", "Secciones 26 y 28", "La coherencia entre aportes y presupuesto no se verifica"),
 ("J6", "Reportes oficiales de afectación por la emergencia y diagnósticos técnicos sectoriales", "Secciones 1 y 4", "La afectación y su relación con la emergencia quedan sin soporte oficial"),
 ("J7", "Planes de desarrollo departamental y municipal vigentes", "Sección 4", "La alineación con política pública queda sin verificar"),
 ("J8", "Catálogo de productos de la MGA, sector 39, programa 3906", "Sección 20", "La asignación de productos MGA es PROPUESTO"),
 ("J9", "Código SIGP del proyecto", "Sección 1", "El proyecto no tiene código de registro"),
 ("J10", "Certificados de existencia y representación, RUT o NIT de las entidades", "Requisitos administrativos", "La habilitación jurídica de las entidades no se verifica"),
 ("J11", "Análisis de licencias y permisos específicos del proyecto", "Sección 27", "Se identifican como PROPUESTO en el anexo N")]
d.tabla("a12", "Documentos de la convocatoria no aportados y efecto de su ausencia",
        ["Id", "Documento", "Sección del Anexo 2", "Efecto de la ausencia"], fil12,
        "*Nota.* Elaboración propia con el Anexo 2 de la convocatoria. Todos los documentos están en estado VACIO [DATO_USUARIO: documentos de la convocatoria]. MGA: Metodología General Ajustada; SIGP: plataforma de registro de proyectos mencionada en el Anexo 2.")
d.guardar(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps", "cap20.md"))
print("ok", mm(total_cot))
