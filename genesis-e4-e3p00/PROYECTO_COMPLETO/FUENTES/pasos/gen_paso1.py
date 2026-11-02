# -*- coding: utf-8 -*-
import sys
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/maestro")
import maestro as M
def esc(s): return s.replace("|", "\\|")
L = []; A = L.append
def tabla(tid, titulo, filas, nota):
    A(f":::TABLA {tid} | {titulo}")
    A("| Campo | Respuesta del expediente E3-P00 | Valor adoptado en esta formulación | Naturaleza | Verificación |")
    A("| --- | --- | --- | --- | --- |")
    for r in filas: A("| " + " | ".join(esc(x) for x in r) + " |")
    A(":::NOTA " + nota)
    A("")
A("%% PREFIJO: F1")
A("# Paso 1. Información básica del proyecto")
A("")
A("El sistema se configura para la Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56). La entidad financiadora es el Sistema General de Regalías (SGR), con el Ministerio de Ciencia, Tecnología e Innovación (MinCiencias). La tipología es investigación aplicada, desarrollo tecnológico e innovación. La fecha límite declarada es el 11 de noviembre de 2026. El Paso 1 se organiza en cinco secciones: identificación, caracterización del problema, hipótesis de solución, contexto y alcance, y capacidades. Cada sección contrasta la respuesta del expediente E3-P00 con el valor adoptado en esta formulación. Cada fila declara la naturaleza del dato y su estado de verificación.")
A("")
A("## F1.1 Identificación del proyecto (Sección A)")
A("")
A("La {T:t01} reúne los seis campos de identificación. El título adoptado cumple el límite de 20 palabras y reemplaza «post-sismo» por «posterremoto». La madurez final baja de TRL 8 a TRL 7 por la decisión DEC-F05. El proyecto demuestra el sistema en entorno operativo. El plazo no cubre la calificación independiente que exige el nivel 8.")
A("")
tabla("t01", "Identificación del proyecto", [
 ("Título del proyecto", "Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado post-sismo", M.IDENT["titulo"], "DECLARADO", "NO_APLICA"),
 ("Sector principal (OCDE)", "1.2 Ingeniería eléctrica, electrónica e informática", "1.2 Ingeniería eléctrica, electrónica e informática", "DECLARADO", "NO_VERIFICADO"),
 ("Clasificación", "Investigación aplicada y desarrollo tecnológico", "Investigación aplicada, desarrollo tecnológico e innovación (la innovación en servicio se mantiene del Paso 1 del usuario)", "DECLARADO", "NO_APLICA"),
 ("Palabras clave", "Internet of Things (IoT), Edge Computing, TinyML, Gemelo Digital, Material Particulado, Gestión del Riesgo, Calibración Dinámica", "Internet de las cosas, computación en el borde, TinyML, gemelo digital, material particulado, gestión del riesgo, calibración dinámica", "DECLARADO", "NO_APLICA"),
 ("TRL inicial", "TRL 4: validación de componentes en laboratorio", "TRL 4", "DECLARADO", "NO_VERIFICADO"),
 ("TRL final", "TRL 8: sistema completo y calificado en condiciones reales", "TRL 7: demostración del sistema en entorno operativo (DEC-F05)", "PROPUESTO", "NO_APLICA"),
], "*Nota.* Elaboración propia con el expediente E3-P00 (Paso 1, Sección A) y la ficha maestra (sección 1).")
A("## F1.2 Caracterización del problema (Sección B)")
A("")
A("### F1.2.1 Descripción del problema")
A("")
A("El problema se origina en la falta de verificación de las mediciones de material particulado en los sitios de remoción de escombros. Los sensores ópticos de bajo costo estiman la masa de partículas a partir de la luz dispersada. Esa señal cambia con la humedad relativa y con el tamaño de la partícula. Por ello el error de lectura varía entre sitios y entre horas. Jayaratne et al. (2018) documentaron que la humedad altera la respuesta de un sensor de bajo costo, y Barkjohn et al. (2021) aplicaron una corrección nacional que incorpora la humedad. En el corpus de vigilancia, una estación cercana y un desfase de 35 minutos elevaron el R² de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8).")
A("")
A("El expediente E3-P00 declara un error normalizado superior a 45 % en sensores sin calibración dinámica en alta humedad. La cifra carece de localizador y no se verificó. Por esa razón, esta formulación no la usa como línea base. La línea base de error se mide en el tramo 1, durante la colocalización con equipos de referencia gravimétricos. Un resultado propio, con intervalo de confianza, sustituye así a una declaración sin fuente.")
A("")
A("La segunda dimensión del problema es institucional. Los comités de gestión del riesgo deciden con el índice de calidad del aire y salud (AQHI, por sus siglas en inglés). El índice se calcula con datos de calidad desconocida. Si el dato carece de error conocido, la alerta emitida puede ser una falsa alarma o una omisión. El efecto sobre la confianza es acumulativo: una falsa alarma reduce el uso posterior del tablero. El análisis estructural de las secciones 4.3 y 4.4 identificó la adopción institucional (V15) como variable crítica. Esa variable aparece en 140 de 144 ciclos simples del escenario de trabajo.")
A("")
A("La tercera dimensión es la disponibilidad de la red. Los sitios de remoción exponen los cabezales al polvo y a la humedad, y con frecuencia carecen de energía estable y de cobertura celular. La literatura del corpus describe una correlación de 0,73 entre las partículas y la humedad en una mina a cielo abierto (Suresh et al., 2025, p. 30). El contexto nacional agrava la restricción. Hay 209 estaciones reportadas y 154 integradas a un sistema de vigilancia. Solo 28 de 1.122 municipios cuentan con estaciones utilizables para estimar la carga de enfermedad (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). En la red nacional propuesta, 90,8 % de las 5.076 estaciones serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13). El 90,8 % es un cálculo del analista sobre las cifras del documento.")
A("")
A("El expediente declara un sismo del 10 de agosto y el Decreto 1261 de 2026 como origen de la demanda. El usuario autorizó tratar el territorio, el evento y la alianza como supuestos de trabajo. Ninguno se verificó con una fuente normativa. El proyecto no promete efectos en la salud de la población. Promete mediciones con error conocido, uso institucional documentado y continuidad de la red bajo custodia.")
A("")
A("La {T:t02} compara cada campo de la Sección B con el valor adoptado. Los campos «problema trascendente» y «deficiencia oculta» se conservan con ajuste de redacción. Ambos describen una disyuntiva de diseño entre exactitud y continuidad. La arquitectura propuesta la resuelve con la corrección en el gateway.")
A("")
tabla("t02", "Caracterización del problema", [
 ("Problema trascendente", "Tensión entre precisión metrológica (alto procesamiento) y supervivencia de la red (bajo consumo de batería y de ancho de banda)", "Disyuntiva entre exactitud de la medición, que exige procesamiento, y continuidad de la red, que exige bajo consumo de energía y de ancho de banda", "DECLARADO", "NO_APLICA"),
 ("Deficiencia oculta", "El sector público tolera la fatiga de alarmas y supone que los sensores no se calibran sin un técnico en campo", "Los comités toleran falsas alarmas porque suponen que la calibración exige visitas técnicas; la corrección remota en el gateway elimina esa condición", "INFERIDO", "NO_VERIFICADO"),
 ("Población afectada", "Población urbana y rural y operarios de remoción en polígonos de afectación sísmica severa de Caldas, Cundinamarca y Valle del Cauca", "Operarios de remoción y población expuesta en 12 municipios focalizados, 4 por departamento [DATO_USUARIO: lista de municipios y polígonos]", "SUPUESTO", "NO_VERIFICADO"),
 ("Magnitud del problema", "Error normalizado superior a 45 % en alta humedad frente a estaciones gravimétricas", "Línea base propia: [VACIO: se mide en el tramo 1]. Cifra de E3: DECLARADO sin localizador", "DECLARADO y VACIO", "NO_VERIFICADO"),
 ("Causas preliminares", "Cinco causas: interferencia de humedad, obstrucción por macropartículas, calibración estática, latencia de datos crudos y consumo de energía", "Quince variables del sistema, con el problema central V06 y cinco causas directas o indirectas (Paso 4)", "INFERIDO", "NO_VERIFICADO"),
 ("Efectos observados", "Índices AQHI sesgados, evacuaciones innecesarias, omisión de alertas y descarte de la tecnología por los comités", "Se conservan como hipótesis de efecto; ninguna se cuantifica sin línea base (V11, V12, V14, V15)", "DECLARADO", "NO_VERIFICADO"),
], "*Nota.* Elaboración propia con el expediente E3-P00 (Paso 1, Sección B) y la ficha maestra (secciones 10 y 10c).")
A("## F1.3 Hipótesis de solución (Sección C)")
A("")
A("La hipótesis de solución afirma que una red de 100 nodos de bajo costo alcanza un desempeño verificado frente a referencia. Para ello, el modelo de corrección se aplica en el gateway y se entrena con colocalización. La arquitectura separa tres capas. Los nodos hoja miden PM2,5 y PM10 con temperatura y humedad, y transmiten por LoRa. Los diez gateways corrigen la lectura con el modelo vigente, almacenan siete días de datos y reenvían por red celular con enlace satelital alterno. La nube entrena el modelo, aloja el gemelo digital que estima la distribución espacial y publica el tablero del AQHI.")
A("")
A("El expediente E3-P00 propone 90 % de nodos hoja pasivos y 10 % de gateways. Además, ubica la corrección en tres lugares distintos: el sensor, el microcontrolador del nodo y el gateway. Esta formulación conserva la proporción de 10 gateways por cada 100 nodos y fija un solo lugar de corrección, el gateway (DEC-F02). La razón es la trazabilidad: un solo modelo vigente por gateway permite auditar qué corrección produjo cada dato.")
A("")
A("El desempeño se mide con los umbrales de la Agencia de Protección Ambiental de Estados Unidos para sensores en sitio fijo (U.S. Environmental Protection Agency [EPA], 2021). El coeficiente de determinación debe ser mayor o igual que 0,70. El error cuadrático medio normalizado debe ser menor o igual que 30 %. El error absoluto medio normalizado (NMAE) de 15 % es aspiracional y no condiciona las compuertas (DEC-F04). La {T:t03} resume la sección.")
A("")
tabla("t03", "Hipótesis de solución", [
 ("Solución propuesta", "Arquitectura híbrida de computación en el borde y TinyML (ALT-03); 90 % de nodos hoja y 10 % de gateways con calibración local", "Red de 100 nodos, 10 gateways y 3 monitores de referencia, con corrección en el gateway, despliegue por tramos y custodia distribuida", "PROPUESTO", "NO_APLICA"),
 ("TRL inicial de la solución", "TRL 4 en algoritmos de calibración higroscópica", "TRL 4 (componentes validados en laboratorio por el grupo ejecutor [DATO_USUARIO: evidencia de la validación de laboratorio])", "DECLARADO", "NO_VERIFICADO"),
 ("Tipo de innovación", "Producto (hardware y gemelo digital) y servicio (alertas de gestión del riesgo)", "Producto, proceso (calibración dinámica en el borde) y servicio (tablero y protocolo de alerta)", "PROPUESTO", "NO_APLICA"),
], "*Nota.* Elaboración propia con el expediente E3-P00 (Paso 1, Sección C) y la ficha maestra (sección 2).")
A("## F1.4 Contexto y alcance (Sección D)")
A("")
A("La Sección D fija territorio, duración, presupuesto y participantes. La {T:t04} contiene los siete campos. El valor solicitado al SGR se reduce de 14.000 millones al monto justificado por actividad, " + M.cop(M.total(M.BUDGET)) + " COP. Ese monto equivale a 66,2 % del tope declarado (DEC-F06). La diferencia no se solicita y se describe como opciones de ampliación condicionadas a los términos de referencia. Los beneficiarios directos se cuantifican por comité: 15 comités y 150 funcionarios, a razón de 10 por comité (SUPUESTO).")
A("")
tabla("t04", "Contexto y alcance", [
 ("Ubicación geográfica", "Caldas, Cundinamarca y Valle del Cauca, en zonas con declaratoria de calamidad por escombros (Anexo 8)", "Caldas (33 nodos), Cundinamarca (34) y Valle del Cauca (33); 12 municipios [DATO_USUARIO: lista y polígonos]", "SUPUESTO", "NO_VERIFICADO"),
 ("Duración estimada", "24 meses (límite normativo de los TdR)", "24 meses (104 semanas) más 12 meses de seguimiento posproyecto", "DECLARADO y PROPUESTO", "NO_VERIFICADO"),
 ("Presupuesto estimado", "$ 14.000.000.000 COP (límite normativo)", f"Solicitado al SGR: {M.cop(M.total(M.BUDGET))} COP; contrapartida: {M.cop(M.total(M.CONTRA))} COP; total: {M.cop(M.total(M.BUDGET) + M.total(M.CONTRA))} COP", "CALCULADO", "NO_VERIFICADO"),
 ("Entidad ejecutora", "Institución de educación superior con acreditación de alta calidad (por definir)", "[DATO_USUARIO: nombre de la entidad ejecutora]; institución de educación superior con acreditación de alta calidad", "SUPUESTO", "NO_VERIFICADO"),
 ("Co-ejecutores", "Empresa tecnológica y alcaldías municipales", "Empresa tecnológica [DATO_USUARIO: razón social y NIT]; las alcaldías participan como custodios y no aportan contrapartida (VACIO)", "SUPUESTO", "NO_VERIFICADO"),
 ("Beneficiarios directos", "Operarios de rescate y funcionarios de la Defensa Civil y la UNGRD que usan los tableros", "150 funcionarios de 15 comités de gestión del riesgo; operarios de remoción [DATO_USUARIO: número de operarios en sitios monitoreados]", "SUPUESTO", "NO_VERIFICADO"),
 ("Beneficiarios indirectos", "Habitantes de municipios afectados expuestos a la pluma de partículas", "[DATO_USUARIO: población de los 12 municipios según el DANE]", "VACIO", "NO_VERIFICADO"),
], "*Nota.* Elaboración propia con el expediente E3-P00 (Paso 1, Sección D), la ficha maestra (secciones 1, 4 y 5) y maestro.py. COP: pesos colombianos.")
A("## F1.5 Capacidades y antecedentes (Sección E)")
A("")
A("La Sección E describe lo que el ejecutor aporta. El expediente declara dos proyectos de CTeI previos, un grupo de categoría A1 o A y laboratorios de calibración óptica. Ninguna de esas declaraciones tiene soporte documental en los archivos del usuario. La formulación las conserva como declaradas y exige su acreditación antes de radicar. La {T:t05} lista cada capacidad y el documento que la acredita.")
A("")
tabla("t05", "Capacidades y antecedentes", [
 ("Experiencia del equipo", "Al menos dos proyectos de CTeI en telecomunicaciones o monitoreo ambiental", "[DATO_USUARIO: dos certificaciones de proyectos ejecutados, con entidad, valor y fechas]", "DECLARADO", "NO_VERIFICADO"),
 ("Grupos de investigación", "Grupo de telecomunicaciones y señales, categoría A1 o A", "[DATO_USUARIO: nombre, código y categoría vigente del grupo en la plataforma de MinCiencias]", "DECLARADO", "NO_VERIFICADO"),
 ("Infraestructura disponible", "Laboratorios de calibración óptica de la institución y servidores en la nube de la empresa", "Laboratorio de la institución (aporte valorado en 300 millones de pesos) y nube de la empresa (800 millones en especie); [DATO_USUARIO: inventario de equipos y certificados de calibración]", "DECLARADO y PROPUESTO", "NO_VERIFICADO"),
 ("Proyectos previos relacionados", "Redes urbanas de calidad del aire como línea base de comparación de fallos", "Estado del arte del capítulo 2 y análisis de la sección 4.3; [DATO_USUARIO: proyectos propios del ejecutor]", "DOCUMENTADO", "PARCIALMENTE_VERIFICADO"),
 ("Alianzas existentes", "Acuerdos en estructuración: carta unificada de aval y gobernanza (Anexo 1)", "Alianza entre institución, empresa y entidades territoriales como supuesto; [DATO_USUARIO: cartas de compromiso firmadas]", "SUPUESTO", "NO_VERIFICADO"),
], "*Nota.* Elaboración propia con el expediente E3-P00 (Paso 1, Sección E) y la ficha maestra (sección 5, contrapartida).")
A("## F1.6 Verificación de completitud del paso")
A("")
A("El Paso 1 exige completar todas las secciones. La {T:t06} verifica la cobertura de los 27 campos de la plantilla del metaprompt y señala cuántos valores dependen de datos que solo el usuario posee. El resultado alimenta el registro de vacíos del cierre del documento.")
A("")
A(":::TABLA t06 | Verificación de completitud del Paso 1")
A("| Sección | Campos de la plantilla | Campos con valor adoptado | Campos con marcador DATO_USUARIO | Observación |")
A("| --- | --- | --- | --- | --- |")
for r in [
 ("A. Identificación", "6", "6", "0", "Título de 20 palabras; TRL final ajustado a 7"),
 ("B. Problema", "7", "7", "2", "Línea base propia pendiente del tramo 1; lista de municipios"),
 ("C. Hipótesis de solución", "3", "3", "1", "Evidencia del TRL 4"),
 ("D. Contexto y alcance", "7", "7", "5", "Entidad ejecutora, empresa, municipios, operarios y población"),
 ("E. Capacidades", "5", "5", "5", "Certificaciones, grupo, inventario, proyectos y cartas"),
 ("Total", "28", "28", "13", "Los 28 campos tienen valor adoptado; 13 filas requieren documento del usuario"),
]: A("| " + " | ".join(esc(x) for x in r) + " |")
A(":::NOTA *Nota.* Elaboración propia. La plantilla del metaprompt tiene 28 campos: 6 + 7 + 3 + 7 + 5. Los marcadores se cuentan por fila, no por aparición en el texto.")
A("")
A("El Paso 1 crea valor al separar lo que el expediente declara de lo que esta formulación adopta y de lo que falta. Esa separación impide trasladar al documento final cifras sin localizador, como el error de 45 %. Además, entrega a la entidad ejecutora una lista cerrada de certificaciones por reunir.")
open(RAIZ + "/caps/paso1.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("ok")
