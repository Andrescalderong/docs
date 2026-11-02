# -*- coding: utf-8 -*-
import json, collections
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
corp = json.load(open(RAIZ + "/refs/corpus_informe.json", encoding="utf-8"))
cnt = collections.Counter(x["tipo"] for x in corp)
assert (cnt["articulo"], cnt["patente"], cnt["informe"]) == (26, 15, 1), cnt
def esc(s): return s.replace("|", "\\|")
L = []; A = L.append
def tabla(tid, titulo, enc, filas, nota):
    A(f":::TABLA {tid} | {titulo}")
    A("| " + " | ".join(enc) + " |"); A("| " + " | ".join("---" for _ in enc) + " |")
    for r in filas: A("| " + " | ".join(esc(x) for x in r) + " |")
    A(":::NOTA " + nota); A("")
A("%% PREFIJO: F2")
A("# Paso 2. Ecuaciones de búsqueda para la vigilancia tecnológica")
A("")
A("El Paso 2 define las palabras clave, las ecuaciones de búsqueda y el protocolo de selección que alimentan el procesamiento bibliométrico del Paso 3. El usuario aportó un corpus ya construido: 42 documentos analizados en el informe de vigilancia tecnológica. Ese informe propone dos ecuaciones en su Anexo D, con carácter de supuesto del analista. No documenta las ecuaciones con que se obtuvo el corpus. Por esa razón, las ecuaciones de este paso son PROPUESTAS y no se ejecutaron en esta corrida. El equipo formulador las usa para reproducir y actualizar la vigilancia en las bases con licencia.")
A("")
A("## F2.1 Palabras clave identificadas")
A("")
A("Las palabras clave se derivan de la formulación del problema y de los términos de la literatura del corpus. La {T:t01} separa cuatro categorías. Cada categoría incluye términos en inglés y en español. Las bases científicas indexan en inglés. Las bases regionales, como SciELO, admiten español y portugués.")
A("")
tabla("t01", "Palabras clave estructuradas", ["Categoría", "Palabras clave primarias", "Palabras clave secundarias", "Sinónimos y variantes"], [
 ("Temática principal", "particulate matter; PM2.5; PM10", "air quality; calidad del aire; AQHI", "material particulado; fine particles; aerosol mass"),
 ("Metodología y tecnología", "low-cost sensor; calibration; edge computing", "digital twin; TinyML; machine learning; LoRa", "optical particle counter; sensor network; correction model; gemelo digital"),
 ("Contexto geográfico", "Colombia; Latin America", "Andean region; América Latina", "Caldas; Cundinamarca; Valle del Cauca"),
 ("Sector y aplicación", "disaster risk management; debris removal", "earthquake; post-disaster; early warning", "construction dust; demolition; gestión del riesgo de desastres"),
], "*Nota.* Elaboración propia con la formulación del problema (Paso 1) y el informe de vigilancia tecnológica. Naturaleza: PROPUESTO. Los términos en español se usan en SciELO y en la búsqueda de patentes de la Superintendencia de Industria y Comercio.")
A("## F2.2 Ecuaciones para bases científicas")
A("")
A("Las ecuaciones combinan tres bloques con el operador Y: la variable medida, el instrumento y la técnica de corrección. Un cuarto bloque, el de contexto, se agrega en una segunda ejecución para medir la proporción de documentos sobre escenarios de desastre. La ventana temporal va de 2020 a 2026, y el corpus recibido contiene documentos hasta ese último año. Las ecuaciones siguientes se presentan por base de datos.")
A("")
A("**Scopus.**")
A("")
A("```")
A('TITLE-ABS-KEY(("particulate matter" OR "PM2.5" OR "PM10")')
A('  AND ("low-cost sensor*" OR "low cost sensor*" OR "optical particle counter*")')
A('  AND (calibrat* OR correct* OR "machine learning" OR "edge comput*" OR "digital twin"))')
A('AND PUBYEAR > 2019 AND (LIMIT-TO(DOCTYPE, "ar") OR LIMIT-TO(DOCTYPE, "re"))')
A("```")
A("")
A("**Web of Science.**")
A("")
A("```")
A('TS=(("particulate matter" OR "PM2.5" OR "PM10")')
A('  AND ("low-cost sensor*" OR "low cost sensor*" OR "optical particle counter*")')
A('  AND (calibrat* OR correct* OR "machine learning" OR "edge comput*" OR "digital twin"))')
A("AND PY=(2020-2026) AND DT=(Article OR Review)")
A("```")
A("")
A("**IEEE Xplore.**")
A("")
A("```")
A('("All Metadata":"particulate matter" OR "All Metadata":"PM2.5")')
A('AND ("All Metadata":"low-cost sensor" OR "All Metadata":"optical particle counter")')
A('AND ("All Metadata":calibration OR "All Metadata":"edge computing" OR "All Metadata":"digital twin")')
A("```")
A("")
A("**PubMed.**")
A("")
A("```")
A('("particulate matter"[Title/Abstract] OR "PM2.5"[Title/Abstract])')
A('AND ("low-cost sensor*"[Title/Abstract] OR "optical particle counter*"[Title/Abstract])')
A('AND ("2020"[Date - Publication] : "2026"[Date - Publication])')
A("```")
A("")
A("**SciELO.**")
A("")
A("```")
A('(ti:("material particulado" OR "PM2,5" OR "calidad del aire"))')
A('AND (ab:(sensor* OR calibraci* OR "bajo costo"))')
A('AND year_cluster:("2020" OR "2021" OR "2022" OR "2023" OR "2024" OR "2025" OR "2026")')
A("```")
A("")
A("**Google Scholar (complementaria).**")
A("")
A("```")
A('allintitle: "low-cost" sensors particulate calibration  after:2020')
A("```")
A("")
A("## F2.3 Ecuaciones para bases de patentes")
A("")
A("La vigilancia de patentes busca por texto y por clasificación. El procedimiento de la Superintendencia de Industria y Comercio (SIC) usa dos ecuaciones. Una contiene palabras clave y otra clases de la Clasificación Internacional de Patentes (Superintendencia de Industria y Comercio [SIC], 2026, pp. 4-9). El informe de vigilancia adapta ese procedimiento con las clases F24F, G01N33, B01D46, B01D53 y G08B21/12 (supuesto del analista del informe, Anexo D). Esta formulación conserva esas cinco clases y las combina con la ecuación de texto de la {T:t02}.")
A("")
tabla("t02", "Ecuaciones para bases de patentes", ["Base", "Ecuación", "Naturaleza"], [
 ("Google Patents", '("particulate matter" OR "PM2.5") AND ("low-cost sensor" OR "optical sensor") AND (calibration OR correction OR "digital twin") country:CO,US,EP,WO after:2019', "PROPUESTO"),
 ("Espacenet", 'ta = ("particulate matter" OR "PM2.5") AND ta = (sensor AND (calibration OR "machine learning")) AND pd >= 2020', "PROPUESTO"),
 ("USPTO", 'ABST/("particulate matter" OR "PM2.5") AND ABST/(sensor AND calibration)', "PROPUESTO"),
 ("WIPO PATENTSCOPE", 'FP:("particulate matter" OR "PM2.5") AND FP:(sensor AND calibration) AND DP:[2020 TO 2026]', "PROPUESTO"),
 ("SIC Colombia (clasificación)", "(F24F OR G01N33 OR B01D46 OR B01D53 OR G08B21/12) AND (CO2 OR PM2,5 OR «calidad del aire» OR «air quality»)", "SUPUESTO del analista del informe"),
 ("SIC Colombia (palabras clave)", "(«calidad del aire» OR «material particulado» OR «PM2,5» OR «air quality») AND (sensor OR monitor* OR calibraci* OR calibrat*), en título y resumen", "SUPUESTO del analista del informe"),
], "*Nota.* Elaboración propia. Las dos últimas filas reproducen las ecuaciones del Anexo D del informe de vigilancia tecnológica. Ninguna ecuación se ejecutó: el número de resultados por base queda como [DATO_USUARIO: resultados por base y fecha de corte de cada búsqueda].")
A("## F2.4 Protocolo PRISMA-VT de selección sistemática")
A("")
A("PRISMA-VT es una adaptación operativa de la declaración PRISMA 2020 (Page et al., 2021) a la vigilancia tecnológica. La declaración original es una guía para reportar revisiones sistemáticas en salud. Su finalidad no es la vigilancia tecnológica ni la selección de patentes. Por esa razón, el documento declara la adaptación como tal y no la presenta como cumplimiento del estándar. El protocolo tiene cuatro etapas y dos tablas de criterios.")
A("")
A("La {T:t03} describe las etapas. La columna final contrasta cada etapa con lo que se dispone en esta corrida. El diagrama de flujo con cifras reales de los 42 documentos del corpus se presenta en el Paso 3.")
A("")
tabla("t03", "Etapas PRISMA-VT para la vigilancia tecnológica", ["Etapa", "Acción", "Criterio de decisión", "Registro", "Estado en esta corrida"], [
 ("Identificación", "Búsqueda en seis bases científicas y cinco de patentes", "Todas las ecuaciones de las secciones F2.2 y F2.3", "Documentos recuperados por base", "No ejecutada; [DATO_USUARIO: resultados por base]"),
 ("Cribado", "Lectura de título y resumen", "Relevancia temática directa con el problema central", "Excluidos y motivo", "No documentada en el informe"),
 ("Elegibilidad", "Lectura de texto completo", "Calidad metodológica y pertinencia", "Excluidos y motivo", "Cada uno de los 42 documentos se leyó completo (informe, sección 1)"),
 ("Inclusión", "Corpus final", "Artículos, patentes e informes seleccionados", "Distribución por tipo y relevancia", "26 artículos, 15 patentes y 1 informe institucional"),
], "*Nota.* Elaboración propia con la especificación del metaprompt y el informe de vigilancia tecnológica. Naturaleza: PROPUESTO y DOCUMENTADO. Las siglas PRISMA-VT designan una adaptación y no un estándar publicado.")
A("Los criterios de inclusión y exclusión se detallan en la {T:t04}. El criterio de cuartil exige que al menos 60 % del corpus pertenezca a revistas Q1 o Q2. El informe no reporta cuartiles, de modo que ese criterio no se puede verificar con los archivos del usuario.")
A("")
tabla("t04", "Criterios de inclusión y exclusión", ["Tipo", "Criterio", "Especificación", "Evaluación sobre el corpus recibido"], [
 ("Inclusión", "Temporalidad", "Publicaciones de los últimos cinco a siete años; excepciones para obras fundacionales", "Años del corpus entre 1995 y 2026; 17 documentos de 2026 y 9 de 2025"),
 ("Inclusión", "Idioma", "Inglés, español o portugués", "Sin evaluación documentada"),
 ("Inclusión", "Tipo", "Artículos arbitrados, patentes concedidas o solicitadas, informes técnicos y tesis", "Sin tesis en el corpus"),
 ("Inclusión", "Calidad", "Al menos 60 % en cuartiles Q1 o Q2", "VACIO: el informe no reporta cuartiles"),
 ("Inclusión", "Citas", "Más de 10 citas para publicaciones de más de dos años", "VACIO: el informe no reporta citas recibidas"),
 ("Exclusión", "Duplicados", "Eliminar registros repetidos entre bases", "Sin registro de duplicados"),
 ("Exclusión", "Predatorios", "Excluir revistas de lista Beall o sin indexación verificable", "Sin verificación documentada"),
 ("Exclusión", "Irrelevantes", "Sin relación directa con el problema central", "El informe conserva patentes de otros dominios como contraste"),
 ("Exclusión", "Obsoletos", "Más de diez años, salvo referencia fundacional con más de 50 citas", "1 patente de 1995 (Reintjes et al., 1995)"),
 ("Exclusión", "Incompletos", "Sin resumen, metodología explícita o datos de soporte", "Sin registro de exclusión"),
], "*Nota.* Elaboración propia con la especificación del metaprompt y las cifras del informe de vigilancia tecnológica. La fila «Irrelevantes» corresponde a patentes de turbinas, gasificación y descarbonización de edificios, que el informe conserva como contraste.")
A("## F2.5 Métricas bibliométricas a registrar")
A("")
A("Cada documento del corpus final se registra con diez métricas. La {T:t05} señala cuáles reporta el informe de vigilancia y cuáles quedan vacías. Las métricas ausentes (cuartil, factor de impacto y citas) limitan la verificación de los criterios de calidad, y el Paso 3 las declara como límite.")
A("")
tabla("t05", "Métricas bibliométricas por documento", ["Métrica", "Descripción", "Obligatoria", "Disponibilidad en el informe"], [
 ("DOI o URL", "Identificador único", "Sí", "Disponible en la lista de referencias para los artículos; número de solicitud para las patentes"),
 ("Año", "Fecha de publicación", "Sí", "Disponible"),
 ("Cuartil SJR", "Q1, Q2, Q3 o Q4", "Sí (artículos)", "VACIO"),
 ("Factor de impacto o CiteScore", "Indicador de la revista", "Sí (artículos)", "VACIO"),
 ("Citas", "Citas recibidas", "Sí", "VACIO"),
 ("País de los autores", "Afiliación institucional", "Sí", "Disponible (análisis geográfico del Paso 3)"),
 ("Palabras clave", "Palabras clave del autor", "Sí", "Disponible (análisis de coocurrencia del Paso 3)"),
 ("IPC o CPC", "Clasificación de patentes", "Sí (patentes)", "VACIO: el informe no reporta la clasificación de las 15 patentes"),
 ("Tipo de documento", "Artículo, patente, informe o tesis", "Sí", "Disponible"),
 ("Relevancia", "Alta, media o baja", "Sí", "Disponible (agrupación en grupos documentales)"),
], "*Nota.* Elaboración propia con la especificación del metaprompt y el informe de vigilancia tecnológica. Los datos vacíos requieren acceso a Scopus, Web of Science o SJR [DATO_USUARIO: cuartiles y citas por documento].")
A("## F2.6 Requisitos de documentos")
A("")
A("El metaprompt exige entre 45 y 60 documentos distribuidos por tipo. La {T:t06} contrasta esa distribución con el corpus recibido. El corpus tiene 42 documentos y queda por debajo del mínimo de 45. Además, carece de tesis y de documentos de política en sentido estricto. El único informe institucional es el reporte de patentes en dominio público de la SIC.")
A("")
tabla("t06", "Distribución de documentos requeridos y disponibles", ["Tipo de documento", "Cantidad mínima requerida", "Prioridad", "Corpus recibido", "Brecha"], [
 ("Artículos Q1 y Q2", "15 a 20", "Alta", "26 artículos en total; cuartil VACIO", "No verificable"),
 ("Artículos Q3 y Q4", "10 a 15", "Media", "Incluidos en los 26 artículos", "No verificable"),
 ("Patentes relevantes", "5 a 10", "Alta", "15", "Cumple; 10 a 15 superan el máximo del rango"),
 ("Informes técnicos o institucionales", "5 a 8", "Media", "1", "4 por debajo del mínimo"),
 ("Tesis doctorales o de maestría", "3 a 5", "Media", "0", "3 por debajo del mínimo"),
 ("Documentos de política", "2 a 3", "Baja", "0", "2 por debajo del mínimo"),
 ("Total", "45 a 60", "", "42", "3 por debajo del mínimo"),
], "*Nota.* Elaboración propia con la especificación del metaprompt y las cifras del informe de vigilancia tecnológica (26 artículos, 15 patentes y 1 informe). Los documentos de política del proyecto (leyes, documentos CONPES y resoluciones) se incorporan en el capítulo 3 y no integran el corpus bibliométrico.")
A("## F2.7 Herramientas de análisis bibliométrico")
A("")
A("El procesamiento posterior usa cinco herramientas. La {T:t07} indica la función de cada una y el formato de entrada. El Paso 3 de este documento se generó con Python, matplotlib y networkx, con la paleta de la plantilla visual del proyecto.")
A("")
tabla("t07", "Herramientas de análisis bibliométrico", ["Herramienta", "Función principal", "Formato de entrada"], [
 ("VOSviewer (van Eck y Waltman, 2010)", "Mapas de cocitación, coocurrencia y acoplamiento bibliográfico", "RIS, BibTeX, CSV"),
 ("bibliometrix (Aria y Cuccurullo, 2017)", "Análisis integral: Lotka, Bradford, evolución temática y redes", "BibTeX, CSV"),
 ("CiteSpace", "Detección de ráfagas, frentes emergentes y evolución temporal", "Exportación de Web of Science"),
 ("Gephi", "Redes complejas de gran escala con métricas de centralidad", "GEXF, GraphML"),
 ("Python (matplotlib y networkx)", "Figuras con la paleta estandarizada", "CSV, JSON"),
], "*Nota.* Elaboración propia con la especificación del metaprompt. VOSviewer y bibliometrix se citan por sus artículos de referencia; CiteSpace y Gephi no se incorporan al banco de referencias.")
A("## F2.8 Instrucciones para el equipo y valor del paso")
A("")
A("El equipo formulador ejecuta siete acciones antes de actualizar la vigilancia. Primero, ejecuta las ecuaciones en las bases con licencia y registra los resultados por base y la fecha de corte. Segundo, aplica las etapas de la {T:t03} y los criterios de la {T:t04} y documenta cada exclusión con su motivo. Tercero, descarga los registros en formato RIS, BibTeX o CSV. Cuarto, consolida los documentos seleccionados. Quinto, completa las métricas faltantes: cuartil, factor de impacto y citas. Sexto, compara el nuevo corpus con los 42 documentos recibidos. Séptimo, repite el Paso 3 con el corpus actualizado.")
A("")
A("El Paso 2 crea valor porque vuelve reproducible una vigilancia que el informe recibido solo describe. Con las ecuaciones y los criterios registrados, otro equipo repite la búsqueda, mide su cobertura y detecta documentos que el corpus omitió. La brecha de tres documentos frente al mínimo y los datos vacíos de cuartil son las dos tareas prioritarias.")
open(RAIZ + "/caps/paso2.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("ok")
