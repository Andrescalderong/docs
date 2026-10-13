# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

d = Doc("20")
M = D.M
R = D.resumen(); SGR, TOT = R["sgr"], R["total"]
B = {l["id"]: l for l in D.BUDGET}
transf = B["S02"]["total"] + B["O03"]["total"] + B["S09"]["total"]
solo_pi = B["S02"]["total"] + B["O03"]["total"]

d.h(2, "Anexo N. Correspondencia con el Anexo 2 de la convocatoria")
d.p("El Anexo 2 de la convocatoria define la estructura mínima del documento técnico. Tiene 30 secciones y sigue la lógica del marco lógico de la Metodología General Ajustada (MGA). El usuario lo aportó después de la primera entrega. El documento se formuló con la estructura del metaprompt y no con la de la convocatoria. Este anexo cruza ambas estructuras. Indica, sección por sección, dónde está el contenido, qué estado tiene y qué falta. Los términos de referencia completos y los anexos 4, 10 y 12 siguen sin aportarse. La decisión DEC-F01 se actualiza. La estructura de 21 capítulos del metaprompt sigue vigente como estructura de trabajo. El Anexo 2 gobierna la estructura de radicación.")
d.p("La {T:n01} presenta la correspondencia de las 30 secciones. Los estados son CUBIERTO, cuando el contenido existe y coincide con lo pedido; PARCIAL, cuando existe con vacíos o con otro formato; y VACIO, cuando solo el usuario puede aportar el dato. La columna final indica la acción para la radicación.")
filas = [
 ("1", "Identificación del proyecto: nombre, entidades, SIGP, tiempo, localización, demanda, línea temática, grupos", "Paso 1; anexos A, D y J", "PARCIAL", "Faltan municipios, región SGR, categoría de las entidades, código SIGP, línea temática y grupos. El título no incluye la localización que el Anexo 2 sugiere."),
 ("2", "Resumen ejecutivo", "Documento 1000X-01", "CUBIERTO", "Ajustar a la extensión que fije el formulario de radicación."),
 ("3", "Palabras clave (máximo seis)", "Paso 1", "PARCIAL", "El Paso 1 lista siete. Se sugiere retirar TinyML, que no corresponde al diseño con corrección en el gateway."),
 ("4", "Alineación con la política pública y afectación por la emergencia", "Capítulo 5; Paso 5.0", "PARCIAL", "Falta el soporte oficial de afectación, los planes departamentales y municipales, y la alineación con el Plan Nacional de Desarrollo vigente."),
 ("5", "Problema central, descripción, magnitud y árbol de problemas", "Capítulo 1; Pasos 4 y 5; sección 4.5", "CUBIERTO", "La línea base de error se mide en el tramo 1 (VACIO)."),
 ("6", "Antecedentes", "Capítulos 1 y 2", "CUBIERTO", "Sin acción."),
 ("7", "Justificación", "Capítulo 5", "CUBIERTO", "Sin acción."),
 ("8", "Articulación con retos y demandas territoriales", "Paso 5.0", "VACIO", "Exige el Anexo 4 y los términos de referencia."),
 ("9", "Marco conceptual, de política y normativo", "Capítulo 4", "CUBIERTO", "Sin acción."),
 ("10", "Análisis de participantes: beneficiario, cooperante, oponente, perjudicado", "Documento 1000X-08; sección 4.4-MDR.5", "PARCIAL", "Reclasificar a las cuatro categorías. Verificar que ninguna entidad sea a la vez cooperante y beneficiaria."),
 ("11", "Población afectada, objetivo, características y enfoque diferencial", "Paso 1; capítulos 5 y 6", "PARCIAL", "Población afectada y enfoque diferencial son VACIO; la población objetivo es SUPUESTO (150 funcionarios, 15 comités)."),
 ("12", "Objetivos y árbol de objetivos", "Capítulo 3; Paso 6.1", "CUBIERTO", "Sin acción."),
 ("13", "Alternativas, análisis técnico y madurez tecnológica", "Paso 6; capítulos 2 y 6", "PARCIAL", "El Anexo 2 prioriza soluciones con TRL 9. El proyecto compromete TRL 7. Ver el hallazgo G1."),
 ("14", "Metodología con responsables, tareas, resultados y verificación", "Capítulo 6", "PARCIAL", "Falta la actividad Administración y apoyo a la supervisión por objetivo. Ver el hallazgo G3."),
 ("15", "Cadena de valor", "Capítulos 8, 11 y 18; Tabla 20.15", "PARCIAL", "La Tabla 20.15 propone el formato; los valores por actividad deben coincidir con el presupuesto."),
 ("16", "Sostenibilidad social y ambiental", "Capítulos 13 y 14", "CUBIERTO", "Sin acción."),
 ("17", "Resultados e impactos para el departamento", "Capítulos 11 y 13", "CUBIERTO", "Los impactos son institucionales; no se afirman efectos en salud."),
 ("18", "Transferencia, adopción y valoración tecnológica con 1 % de recursos", "Capítulo 15", "PARCIAL", "Falta el plan en el formato del Anexo 2. Ver el hallazgo G2."),
 ("19", "Apropiación social del conocimiento", "Capítulo 16", "PARCIAL", "Falta contrastar con el Anexo 10."),
 ("20", "Productos esperados del catálogo MGA, programa 3906", "Capítulo 11; Tabla 20.16", "PARCIAL", "La asignación de la Tabla 20.16 es PROPUESTO y exige verificar el catálogo."),
 ("21", "Cronograma en meses por objetivo, producto y actividad", "Capítulo 9; anexo H", "PARCIAL", "El cronograma está en semanas y trimestres. Convertir a meses en la radicación."),
 ("22", "Análisis de riesgos con tipo, probabilidad, impacto y mitigación", "Capítulo 10; Tabla 20.17", "PARCIAL", "La Tabla 20.17 convierte el registro al formato. Falta el riesgo sanitario del personal de campo."),
 ("23", "Indicadores de gestión: informes trimestrales", "Capítulo 12; PERS-R06", "CUBIERTO", "Hay 8 informes trimestrales y 24 mensuales."),
 ("24", "Indicadores de producto", "Capítulo 12; PERS-P01 a P04", "CUBIERTO", "Alinear los nombres con el catálogo MGA."),
 ("25", "Aspectos éticos", "Capítulo 6; anexo F", "PARCIAL", "Falta el aval de un comité de ética."),
 ("26", "Idoneidad y trayectoria de la entidad y los aliados", "Capítulo 17; anexos A y B", "VACIO", "Exige cartas, hojas de vida y trayectoria de las entidades."),
 ("27", "Licencias y permisos", "Tabla 20.18", "PARCIAL", "Los permisos de la Tabla 20.18 son PROPUESTO y NO_VERIFICADO."),
 ("28", "Resumen de fuentes de financiación", "Capítulos 8 y 21", "CUBIERTO", "Certificar la contrapartida."),
 ("29", "Bibliografía de obras citadas", "Capítulo 19", "CUBIERTO", "Verificar las referencias NO_VERIFICADO."),
 ("30", "Anexos de requisitos sectoriales", "Anexos A a M", "VACIO", "Seguir el portal de la MGA.")]
d.tabla("n01", "Correspondencia entre las 30 secciones del Anexo 2 y el documento",
        ["Sección", "Requisito del Anexo 2", "Ubicación en el documento", "Estado", "Brecha o acción"], filas,
        "*Nota.* Elaboración propia con el Anexo 2 de la convocatoria (documento técnico) y la estructura del documento. CUBIERTO: el contenido existe; PARCIAL: existe con vacíos o en otro formato; VACIO: depende de datos del usuario. MGA: Metodología General Ajustada; SIGP: plataforma de registro de proyectos; ASC: apropiación social del conocimiento.")
cuenta = {k: sum(1 for f in filas if f[3] == k) for k in ("CUBIERTO", "PARCIAL", "VACIO")}
d.p(f"El cruce da {cuenta['CUBIERTO']} secciones cubiertas, {cuenta['PARCIAL']} parciales y {cuenta['VACIO']} vacías. Las vacías dependen de documentos que el usuario no aportó. Las parciales se resuelven con trabajo de formato y con datos del usuario. Ninguna sección exige rehacer el diseño técnico, con la excepción de la madurez tecnológica, que plantea una decisión de fondo. La {{T:n02}} propone la cadena de valor en el formato del Anexo 2, y la {{T:n03}} asigna los productos del catálogo MGA.")

# ---------------------------------------------------------------- cadena de valor
cv = [
 ("OE1: medición verificada", "Documentos de investigación (programa 3906)", "Número de artículos aceptados o sometidos", "2 sometidos y al menos 1 aceptado", "A1.4, A1.6"),
 ("OE1: medición verificada", "[DATO_USUARIO: producto del catálogo para el modelo de corrección y el software registrado]", "Registros de software vigentes", "1", "A1.2, A1.3, A1.4, A1.5, A2.2"),
 ("OE1: medición verificada", "Administración y apoyo a la supervisión del objetivo 1", "Informes de supervisión", "8 trimestrales", "Actividad nueva; valor por asignar a WP0"),
 ("OE2: disponibilidad de la red", "Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos", "Prototipo funcional de red operativa", "100 nodos y 10 gateways", "A2.1, A2.3, A2.4, A1.6"),
 ("OE2: disponibilidad de la red", "Administración y apoyo a la supervisión del objetivo 2", "Informes de supervisión", "8 trimestrales", "Actividad nueva; valor por asignar a WP0"),
 ("OE3: uso institucional", "Servicio de apropiación social del conocimiento", "Actividades de apropiación documentadas", "29 (20 talleres y 9 jornadas)", "A3.1, A3.2"),
 ("OE3: uso institucional", "Servicio de asistencia técnica", "Personas certificadas en operación y mantenimiento", "60 personas o más", "A3.3"),
 ("OE3: uso institucional", "Documentos de planeación", "Convenios de custodia con partida", "3 (uno por tramo)", "A3.3, A3.4"),
 ("OE3: uso institucional", "Administración y apoyo a la supervisión del objetivo 3", "Informes de supervisión", "8 trimestrales", "Actividad nueva; valor por asignar a WP0")]
d.tabla("n02", "Cadena de valor propuesta en el formato del Anexo 2",
        ["Objetivo específico", "Producto", "Medido a través de", "Cantidad o meta", "Actividades asociadas"], cv,
        "*Nota.* Elaboración propia con el Anexo 2 (sección 15), la ficha maestra y el cronograma del capítulo 9. Los nombres de producto MGA proceden de la lista que cita el Anexo 2 y requieren verificación contra el catálogo (NO_VERIFICADO). El Anexo 2 no permite repetir productos ni mezclar programas. Las actividades de administración son PROPUESTO y su valor debe coincidir con la línea O05 y las líneas de gerencia.")
d.p("La cadena de valor muestra que el proyecto cubre seis productos del catálogo y deja uno sin asignar. El modelo de corrección y el software registrado no tienen un producto evidente en la lista que cita el Anexo 2. Esa asignación depende del catálogo completo. La tabla evita repetir el producto de prototipos entre los objetivos 1 y 2, porque la MGA no admite productos repetidos. La red operativa se asigna al objetivo 2 como prototipo funcional.")
mga = [
 ("PERS-P01", "Red de 100 nodos y 10 gateways operativa", "PROT-FUNC", "Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos", "PROPUESTO"),
 ("PERS-P02", "Software de corrección y gemelo digital registrado", "SW-REG", "[DATO_USUARIO: producto del catálogo para software]", "VACIO"),
 ("PERS-P03", "Artículos científicos en revistas Q1 o Q2", "ART-A1 / ART-A2", "Documentos de investigación", "PROPUESTO"),
 ("PERS-P04", "Actividades de apropiación social documentadas", "ASC-PART / ASC-COM / ASC-CIRC", "Servicio de apropiación social del conocimiento", "PROPUESTO"),
 ("PERS-E03", "Capacidad instalada en custodios", "FORM (capacitación)", "Servicio de asistencia técnica", "PROPUESTO"),
 ("Convenios de custodia", "Convenios por tramo con partida", "—", "Documentos de planeación", "PROPUESTO"),
 ("Líneas P02 (maestría)", "Dos estudiantes de maestría en el equipo", "—", "Servicio de apoyo financiero para la formación de maestría, modalidad de investigación", "PROPUESTO"),
 ("Líneas P01 (jóvenes)", "Seis jóvenes investigadores en el equipo", "—", "Servicio de apoyo financiero para el fortalecimiento de las vocaciones científicas en CTI", "PROPUESTO")]
d.tabla("n03", "Asignación propuesta de productos del catálogo MGA, sector 39 y programa 3906",
        ["Origen", "Producto del proyecto", "Código MMG 2021", "Producto del catálogo MGA", "Naturaleza"], mga,
        "*Nota.* Elaboración propia con el Anexo 2 (sección 20) y los indicadores de la ficha maestra. La lista de productos MGA es la que reproduce el Anexo 2; el catálogo completo no se aportó. El MMG de 2021 y el catálogo MGA son clasificaciones distintas y no se igualan. NO_VERIFICADO.")

# ---------------------------------------------------------------- riesgos
def clase_p(p): return "Raro" if p == 1 else ("Improbable" if p == 2 else "Probable")
def clase_i(i): return "Mayor" if i >= 4 else ("Moderado" if i == 3 else "Menor")
tipo = {"R-TEC-01": "Operacionales", "R-TEC-02": "Operacionales", "R-TEC-03": "Operacionales", "R-TEC-04": "Operacionales",
        "R-ORG-01": "Operacionales", "R-ORG-02": "Financieros", "R-EXT-01": "De calendario", "R-EXT-02": "Operacionales",
        "R-FIN-01": "De costos", "R-FIN-02": "Financieros", "R-JUR-01": "Legales", "R-DAT-01": "Operacionales"}
rk = [(r["id"], tipo[r["id"]], r["desc"], clase_p(r["P"]), clase_i(r["I"]), r["respuesta"]) for r in D.RISKS]
d.p("La {T:n04} convierte el registro de riesgos del capítulo 10 al formato del Anexo 2. La conversión usa una regla simple. La probabilidad 1 es rara, la 2 es improbable y de 3 en adelante es probable. El impacto 4 o 5 es mayor, el 3 es moderado y de 1 a 2 es menor. La regla es PROPUESTO y pierde la resolución de la escala de cinco niveles. El tipo de riesgo se asigna por la naturaleza de la causa.")
d.tabla("n04", "Registro de riesgos convertido al formato del Anexo 2",
        ["Riesgo", "Tipo (Anexo 2)", "Descripción", "Probabilidad", "Impacto", "Medida de mitigación"], rk,
        "*Nota.* Elaboración propia con datos de maestro.py (RIESGOS) y el Anexo 2 (sección 22). Probabilidad y impacto convertidos desde la escala de 1 a 5: probabilidad 1 rara, 2 improbable, 3 a 5 probable; impacto 4 y 5 mayor, 3 moderado, 1 y 2 menor. Los tipos son operacionales, administrativos, sanitarios, legales, financieros, de costos y de calendario. El registro no incluye un riesgo sanitario.")

# ---------------------------------------------------------------- licencias
lic = [
 ("Uso del espectro radioeléctrico para LoRa y enlace satelital", "Operación de los nodos y los gateways", "Verificar las condiciones de uso de bandas con la autoridad competente", "NO_VERIFICADO"),
 ("Autorización de los propietarios o administradores de cada sitio", "Instalación de 100 nodos y 10 gateways", "Acta de autorización por sitio, firmada por el titular", "PROPUESTO"),
 ("Permisos municipales para mástiles y obra menor", "Línea S05, instalación en sitio", "Verificar con cada alcaldía si se requiere licencia o permiso", "NO_VERIFICADO"),
 ("Nacionalización de equipos importados", "Línea S11, tres lotes", "Declaración y trámite aduanero con el agente designado", "PROPUESTO"),
 ("Protección de datos personales", "Talleres, encuestas y ubicaciones de nodos", "Cumplimiento de la Ley 1581 de 2012; evaluar el registro de bases de datos", "PROPUESTO"),
 ("Consentimiento informado", "29 actividades de apropiación social", "Formulario del anexo F por participante", "PROPUESTO"),
 ("Consulta previa con comunidades étnicas", "Sitios en territorios de comunidades", "Verificar si algún sitio se ubica en territorio colectivo; hoy no se identifica", "NO_VERIFICADO"),
 ("Licencia ambiental, acceso a recursos genéticos y colecciones biológicas", "No aplica a una red de sensores de partículas", "Confirmar la no aplicabilidad con la autoridad ambiental", "NO_VERIFICADO")]
d.p("La {T:n05} cubre la sección 27 del Anexo 2. Lista los permisos y licencias que el diseño podría requerir. Ninguno se verificó con una autoridad. La lista identifica los que probablemente aplican, los que probablemente no aplican y la acción de verificación. El documento no afirma que un permiso exista o no exista.")
d.tabla("n05", "Licencias y permisos identificados con su acción de verificación",
        ["Requisito", "Origen en el proyecto", "Acción de verificación", "Estado"], lic,
        "*Nota.* Elaboración propia con el Anexo 2 (sección 27) y el diseño del proyecto. Todos los requisitos son PROPUESTO o NO_VERIFICADO. La Ley 1581 de 2012 está en el banco de referencias; las demás normas no se citan porque no se verificaron [DATO_USUARIO: normativa vigente de espectro y de permisos locales].")

# ---------------------------------------------------------------- hallazgos
d.p(f"El cruce produjo ocho hallazgos que el Anexo 2 hace visibles y que la primera entrega no podía ver. La {{T:n06}} los lista con su efecto y su ruta de solución. Dos son de fondo y seis son de forma. Los de fondo son la madurez tecnológica y el mínimo de recursos de transferencia. En el segundo, las líneas de propiedad intelectual suman {mm(solo_pi)} millones de COP, equivalentes a {num(100 * solo_pi / SGR, 2)} % del valor solicitado. Con la formación de custodios, línea S09, la suma sube a {mm(transf)} millones, es decir, {num(100 * transf / SGR, 2)} % del SGR y {num(100 * transf / TOT, 2)} % del total.")
fil = [
 ("G1", "Madurez tecnológica", "El Anexo 2 prioriza soluciones con TRL 9 que no dependan de fases posteriores. El proyecto compromete TRL 7 (DEC-F05) y condiciona el TRL 8 a una evaluación independiente. Además exige evidencias verificables del TRL de entrada, declarado como 4.", "Alto: puede afectar la elegibilidad o el puntaje", "Decidir con el usuario si se mantiene TRL 7 con justificación o se rediseña la ruta hacia TRL 8 o 9. Reunir evidencias del TRL 4 actual."),
 ("G2", "Mínimo de transferencia", f"El componente exige 1 % o más del valor total asignado a transferencia, adopción y valoración. El mínimo equivale a {mm(0.01 * SGR)} millones sobre el SGR o {mm(0.01 * TOT)} millones sobre el total. Solo las líneas de propiedad intelectual suman {mm(solo_pi)} millones. Con S09 suman {mm(transf)} millones.", "Medio: depende de que la formación de custodios se admita como adopción", "Redactar el plan de transferencia en el formato del Anexo 2 y rotular las líneas S02, O03 y S09 como componente de transferencia. Confirmar la base de cálculo con los términos de referencia."),
 ("G3", "Administración y apoyo a la supervisión", "El Anexo 2 exige una actividad con ese nombre en cada objetivo, coherente con la cadena de valor y el presupuesto. La red actual la tiene en WP0.", "Medio: incumplimiento de forma", "Dividir WP0 en tres actividades, una por objetivo, con valores que sumen las líneas de gerencia y administración."),
 ("G4", "Afectación por la emergencia", "El Anexo 2 exige municipios afectados por la emergencia y soporte oficial de la afectación. El territorio es un supuesto y no hay reportes oficiales.", "Alto: es condición de la convocatoria", "Aportar reportes oficiales y la lista de municipios afectados [DATO_USUARIO: municipios y reportes]."),
 ("G5", "Productos MGA", "Los productos deben seleccionarse del catálogo MGA, sector 39, programa 3906, sin repetirlos. El documento usa el MMG de 2021.", "Medio", "Adoptar la Tabla 20.16 tras verificar el catálogo completo."),
 ("G6", "Palabras clave", "El Anexo 2 admite seis palabras. El Paso 1 propone siete.", "Bajo", "Retirar TinyML."),
 ("G7", "Participantes", "Ninguna entidad puede ser a la vez cooperante y beneficiaria. El análisis usa otra clasificación.", "Bajo", "Reclasificar en el análisis de participantes y verificar el caso de las alcaldías."),
 ("G8", "Riesgo sanitario", "El formato incluye riesgos sanitarios. El registro no incluye el riesgo de exposición del personal de campo en sitios de remoción.", "Medio", "Añadir un riesgo con medidas de protección y póliza.")]
d.tabla("n06", "Hallazgos de cumplimiento derivados del Anexo 2 y ruta de solución",
        ["Id", "Tema", "Hallazgo", "Efecto", "Ruta de solución"], fil,
        "*Nota.* Elaboración propia con el Anexo 2 de la convocatoria y la ficha maestra. G1 y G2 son de fondo; G3 a G8 son de forma o de completitud. La base de cálculo del mínimo de 1 % (valor solicitado o total del proyecto) no se definió en el Anexo 2 y depende de los términos de referencia (NO_VERIFICADO). Decimales con coma.")
d.p("El hallazgo G1 merece una advertencia. La ficha maestra fijó el TRL final en 7 porque el sistema se demuestra en entorno operativo sin calificación formal. El plazo de 24 meses no cubre una evaluación independiente de nivel 8. Esa decisión fue razonable cuando los términos de referencia no se conocían. El Anexo 2 la pone en tensión. Cambiar el nivel exige rediseñar el cronograma, el presupuesto y los criterios de las compuertas. Por esa razón el documento no modifica las cifras y entrega la decisión al usuario con los datos necesarios.")
d.guardar(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps", "anexo_n.md"))
print("ok", cuenta, mm(transf), mm(solo_pi), num(100*transf/SGR,2), num(100*solo_pi/SGR,2))
