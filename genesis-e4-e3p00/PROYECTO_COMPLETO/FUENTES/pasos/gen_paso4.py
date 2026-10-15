# -*- coding: utf-8 -*-
"""Genera caps/paso4.md (Paso 4 completo) y caps/anexos_km.md (anexos K a M del análisis estructural)."""
import re, json, sys, zipfile, os
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/pasos"); sys.path.insert(0, RAIZ + "/maestro")
import imp4
from imp4 import rd, strip_head, convertir, cells
R = imp4.R
def esc(s): return s.replace("|", "\\|")
L = []; A = L.append
def tabla(tid, titulo, enc, filas, nota):
    A(f":::TABLA {tid} | {titulo}")
    A("| " + " | ".join(enc) + " |"); A("| " + " | ".join("---" for _ in enc) + " |")
    for r in filas: A("| " + " | ".join(esc(x) for x in r) + " |")
    A(":::NOTA " + nota); A("")

res = json.load(open(R + "/SECCION_4_4/RESULTADOS.json", encoding="utf-8"))
S2 = {d["id"]: d for d in res["escenarios"]["S_TRABAJO_PROPUESTO"]["directa"]}

A("%% PREFIJO: F4")
A("# Paso 4. Análisis causal completo")
A("")
A("El Paso 4 identifica las causas del problema central, desmantela las ortodoxias que condicionan el diseño y establece qué afirmaciones causales admite la evidencia. Sigue la secuencia del metaprompt: identificación de causas (F4.1), desmantelamiento de ortodoxias (F4.2), clasificación de variables para inferencia causal (F4.3), análisis estructural de Vester y MICMAC (F4.4), metodología integrada de decisión y resolución (F4.4-MDR), árbol de problemas (F4.5), cinco porqués (F4.6), causas priorizadas (F4.7) y causa raíz (F4.8).")
A("")
A("El análisis recorre 15 variables que E3-P01 definió y que esta formulación conserva. Ninguna relación entre variables se trata como efecto causal estimado. Todas son hipótesis de influencia estructural (estatuto HIE). El único estimando con identificación posible es el efecto del método de corrección sobre el error de medición, y solo si se ejecuta el sorteo semanal que propone el informe de vigilancia (estatuto IDC prospectivo). Las secciones F4.3 a F4.5 reproducen el análisis completo, con sus 105 fichas bidireccionales en el Anexo K.")
A("")
A("## F4.1 Identificación de causas con evidencia")
A("")
A("El metaprompt pide 15 causas en cinco categorías: tecnológicas, organizacionales, económicas, de ecosistema y territoriales o institucionales. El expediente E3-P00 respondió con sus 15 variables, que mezclan causas, condiciones y efectos. Esta sección asigna cada variable a una categoría y registra su evidencia con fuente y página, solo cuando el corpus la contiene. Donde el corpus calla, la tabla declara VACIO y no completa la celda con una cifra del expediente.")
A("")
A("El diccionario no contiene variables económicas. El costo de calibrar, el costo de custodia y el financiamiento posproyecto se tratan en la sección F4.4-MDR y en el capítulo 14. Esa omisión es un límite del diccionario de 15 variables y no una ausencia de causas económicas. La {T:t01} presenta las variables agrupadas por categoría.")
A("")
filas = [
 ("V06", "Tecnológica", "Error de medición de PM2,5 y PM10 frente a una referencia gravimétrica; problema central", "Bang et al. (2026, pp. 6-8): con una estación cercana y un desfase de 35 minutos, el R² pasó de menos de 0,2 a 0,81", "Línea base propia: VACIO (se mide en el tramo 1). El expediente declara NMAE superior a 45 % sin localizador", "DECLARADO", "NO_VERIFICADO"),
 ("V07", "Tecnológica", "Frecuencia de calibración de los nodos, medida en ajustes por semana", "Murad Pedraza et al. (2026, pp. 10-11 y 13)", "90,8 % de 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (cálculo del analista)", "CALCULADO", "PARCIALMENTE_VERIFICADO"),
 ("V08", "Tecnológica", "Latencia de datos entre el nodo y la nube", "Bang et al. (2026, pp. 6-8): desfase sensor-estación de 35 minutos, que no equivale a latencia de red", "VACIO: no hay medición de latencia de red", "VACIO", "NO_VERIFICADO"),
 ("V09", "Tecnológica", "Disponibilidad de nodos con energía y enlace", "Tavella et al. (2026, p. 6)", "96 de 570 estaciones inactivas o sin estado en Brasil, 2022 a 2024: 16,8 %", "DOCUMENTADO", "NO_VERIFICADO"),
 ("V10", "Tecnológica", "Densidad efectiva del gemelo digital", "VACIO: el corpus no reporta densidad efectiva", "Diseño propuesto: 100 nodos y 10 gateways en 12 municipios", "PROPUESTO", "NO_APLICA"),
 ("V01", "Ecosistema", "Concentración de PM2,5 en el sitio", "Informe de vigilancia, §3.1 (Suresh et al., 2025): cociente PM2,5/PM10 de 0,88 en una mina", "Sin serie del territorio", "VACIO", "NO_VERIFICADO"),
 ("V02", "Ecosistema", "Concentración de PM10, con fracción gruesa", "Informe de vigilancia, §3.1 (Suresh et al., 2025): régimen distinto del de escombros", "Sin serie del territorio", "INFERIDO", "NO_VERIFICADO"),
 ("V03", "Ecosistema", "Humedad relativa en el sitio de medición", "Suresh et al. (2025, p. 30)", "Correlación de 0,73 entre partículas y humedad en una mina a cielo abierto", "DOCUMENTADO", "PARCIALMENTE_VERIFICADO"),
 ("V04", "Ecosistema", "Velocidad del viento superficial", "Informe de vigilancia, §11.4: control del error normalizado", "VACIO: sin serie del territorio", "VACIO", "NO_VERIFICADO"),
 ("V05", "Territorial", "Volumen de escombros removido (actividad en el sitio)", "Premisa del caso por instrucción del usuario", "[DATO_USUARIO: toneladas por día en cada sitio de remoción]", "SUPUESTO", "NO_VERIFICADO"),
 ("V11", "Organizacional", "Índice AQHI emitido, sin fórmula local validada", "Liao et al. (2026, pp. 6 y 8)", "53 estudios de AQHI; 9,4 % con partición de datos y 11,3 % con análisis de sensibilidad", "DOCUMENTADO", "NO_VERIFICADO"),
 ("V12", "Organizacional", "Tasa de falsas alarmas", "Informe de vigilancia, §1.3, hallazgo 2: ningún documento de alertas la reporta", "VACIO", "VACIO", "NO_VERIFICADO"),
 ("V13", "Organizacional", "Anticipación del aviso, en horas", "VACIO: sin línea base en el corpus", "VACIO", "VACIO", "NO_VERIFICADO"),
 ("V14", "Institucional", "Personas bajo protección efectiva por alertas", "VACIO: sin variable de resultado ni línea base", "VACIO", "VACIO", "NO_VERIFICADO"),
 ("V15", "Institucional", "Adopción institucional del tablero", "Supuesto crítico SC-3; sin medición de uso", "VACIO: se mide desde el tramo 1", "SUPUESTO", "NO_VERIFICADO"),
]
tabla("t01", "Identificación de las 15 causas y condiciones con su evidencia",
      ["Código", "Categoría", "Descripción", "Evidencia (fuente y página)", "Magnitud", "Naturaleza", "Verificación"], filas,
      "*Nota.* Elaboración propia con el diccionario de la sección F4.4.2, la ficha maestra y el informe de vigilancia tecnológica (F-INF). Las citas con página proceden del informe, no de lectura de la fuente primaria.")
A("De las 15 variables, 8 cuentan con una cita del corpus y 7 quedan sin evidencia propia. Las 8 citas tienen una limitación común: provienen de entornos distintos del sitio de remoción de escombros, como una mina a cielo abierto, estaciones brasileñas o estudios de índices en China. Por esa razón, el proyecto no usa ninguna de estas cifras como línea base. Las usa como motivo para medir: la colocalización del tramo 1 produce la línea base propia de V06, V12 y V15.")
A("")
A("### F4.1.1 Validación de la articulación territorial de las causas")
A("")
A("El metaprompt exige que al menos dos causas provengan del diagnóstico del Plan de Desarrollo Departamental (PDD), de las demandas territoriales del Anexo 4 o de los diagnósticos del Observatorio de Ciencia y Tecnología. Exige también que al menos 8 de 15 causas tengan un respaldo territorial. El expediente E3-P00 declara 10 causas articuladas, con artículo del PDD, indicador, código de demanda y misión de la política de investigación e innovación orientada por misiones (PIIOM).")
A("")
A("Ninguno de esos documentos se aportó. Los artículos, indicadores y códigos de la {T:t02} son declaraciones de E3 sin fuente verificable. Algunos códigos repiten el mismo patrón entre departamentos, y por ello la tabla los conserva como declarados. La regla de 8 de 15 se cumple en la declaración y no se cumple en la verificación: 0 de 15 respaldos verificados.")
A("")
filas = [
 ("V06", "PDD Caldas, Eje 2; «Sensores instalados»", "Cal-11", "Misión 3"),
 ("V07", "PDD Valle del Cauca, Art. 45; «Nodos calibrados»", "Val-7", "Misión 3"),
 ("V08", "Sin articulación declarada", "No", "Misión 2"),
 ("V09", "PDD Cundinamarca, Eje 3; «Cobertura de red IoT»", "Cun-11", "Misión 3"),
 ("V10", "Sin articulación declarada", "No", "No"),
 ("V01", "PDD Caldas, Eje 4; «Nivel PM2.5 anual»", "No", "Misión 5"),
 ("V02", "PDD Valle del Cauca, Art. 50; «Nivel PM10 anual»", "No", "Misión 5"),
 ("V03", "Sin articulación declarada", "No", "No"),
 ("V04", "Sin articulación declarada", "No", "No"),
 ("V11", "PDD Cundinamarca, Art. 12; «Índice de riesgo en salud»", "Cun-11", "Misión 1"),
 ("V12", "Sin articulación declarada", "No", "No"),
 ("V13", "PDD Caldas, Eje 2; «Tiempo de alerta temprana»", "Cal-11", "Misión 3"),
 ("V05", "PDD Valle del Cauca, Eje 3; «Toneladas dispuestas»", "Val-7", "Misión 5"),
 ("V14", "PDD Caldas, Art. 22; «Personas alertadas»", "Cal-11", "Misión 1"),
 ("V15", "PDD Cundinamarca, Art. 30; «% de municipios con SAT»", "Cun-11", "Misión 3"),
]
filas = [r + ("DECLARADO", "NO_VERIFICADO") for r in filas]
tabla("t02", "Articulación territorial declarada por E3 para cada causa",
      ["Variable", "PDD (artículo o eje) e indicador declarados", "Código de demanda territorial declarado", "Misión PIIOM declarada", "Naturaleza", "Verificación"], filas,
      "*Nota.* Elaboración propia con el expediente E3-P00 (Tabla E3-4.1a). El PDD, el Anexo 4 de la convocatoria, la PIIOM y el diagnóstico del Observatorio no se aportaron. SAT: sistema de alerta temprana. Ver decisión DEC-F12.")
A("La decisión DEC-F12 mantiene la formulación y registra la reserva R-ART. La corrida continúa por orden expresa del usuario, y el cierre del documento lista los cinco documentos que el equipo formulador debe obtener antes de radicar: PDD de los tres departamentos, Anexo 4, PIIOM, diagnóstico del Observatorio y CONPES vigentes.")
A("")
A("## F4.2 Desmantelamiento de ortodoxias")
A("")
A("Una ortodoxia es un supuesto implícito que orienta el diseño sin haberse sometido a prueba. El método pregunta, para cada variable, si la creencia perjudica el objetivo, si se puede imaginar una alternativa y qué ocurriría si el supuesto fuera falso. La {T:t03} aplica las tres preguntas a las 15 variables. Las decisiones posibles son mantener, cuestionar o eliminar el supuesto.")
A("")
A("El expediente E3-P00 eliminó nueve de quince ortodoxias con alternativas técnicas específicas, como la inferencia en el chip del sensor o los nodos que duermen el 90 % del tiempo. Esta formulación revisa cada decisión contra el corpus y contra la arquitectura que adopta (corrección en el gateway). Una ortodoxia solo se elimina cuando existe evidencia en contra; si la alternativa carece de respaldo, el supuesto se cuestiona y se pone a prueba en el piloto.")
A("")
dec = [
 ("V06", "Un sensor de bajo costo nunca alcanza la calidad de una referencia.", "Sí", "Corrección con modelo entrenado por colocalización, evaluada con los umbrales de EPA (2021)", "Cuestionar", "Barkjohn et al. (2021) aplicaron una corrección que incorpora la humedad; el piloto del tramo 1 mide si el resultado se sostiene en escombros."),
 ("V07", "La calibración exige retirar el sensor al laboratorio.", "Sí", "Actualización remota del modelo de corrección en el gateway, con ciclos de colocalización", "Eliminar", "Murad Pedraza et al. (2026, pp. 10-11 y 13) reportan redes sin plan de calibración; el diseño separa la calibración del retiro físico."),
 ("V08", "Hay que transmitir el dato crudo continuamente a la nube.", "Sí", "Corrección en el gateway y envío del dato corregido con almacenamiento local de 7 días", "Cuestionar", "El valor de latencia es VACIO; el piloto la mide antes de optimizarla."),
 ("V09", "Los nodos fallan porque consumen mucha energía.", "Sí", "Autonomía mínima de 14 días sin sol y reserva de 20 nodos", "Cuestionar", "Tavella et al. (2026, p. 6) reportan 16,8 % de estaciones inactivas o sin estado; la causa de la inactividad no consta."),
 ("V10", "Un gemelo digital exige modelos numéricos de gran tamaño.", "No", "Estimación espacial por interpolación con la red de 100 nodos", "Mantener", "Sin evidencia propia; se evalúa en el tramo 2 con la densidad efectiva."),
 ("V01", "El PM2,5 se predice con variables climáticas simples.", "Sí", "Medir en el sitio con referencia colocalizada", "Cuestionar", "El proyecto mide y corrige; no predice."),
 ("V02", "El polvo de demolición equivale a la contaminación urbana.", "Sí", "Tratar V02 como fracción gruesa (PM10 menos PM2,5)", "Eliminar", "El cociente PM2,5/PM10 de 0,88 en una mina (Suresh et al., 2025) corresponde a otro régimen; la ficha de V02 propone la redefinición."),
 ("V03", "La humedad daña de forma irreversible el sensor óptico.", "Sí", "Corregir el sesgo higroscópico con el modelo", "Eliminar", "Jayaratne et al. (2018) y Barkjohn et al. (2021) muestran corrección posible con humedad; la carcasa mitiga el daño por condensación."),
 ("V04", "El viento superficial es constante en el sitio.", "Sí", "Registrar viento como variable de control", "Cuestionar", "No existe serie del territorio; E3 propone modelos de cizalladura, que el proyecto no adopta."),
 ("V11", "Un índice de calidad del aire mide el riesgo de salud.", "Sí", "AQHI con fórmula y umbrales validados localmente", "Cuestionar", "Liao et al. (2026, pp. 6 y 8): 9,4 % de los estudios usó partición de datos; la validación local es una tarea del proyecto."),
 ("V12", "Las falsas alarmas son inevitables con sensores baratos.", "Sí", "Medir la tasa de falsas alarmas y reducirla con la corrección", "Cuestionar", "Ningún documento de alertas del corpus la reporta."),
 ("V13", "Anticipar una hora salva pocas vidas.", "Sí", "Medir la anticipación y no afirmar efectos sobre vidas", "Cuestionar", "Sin línea base en el corpus; el proyecto no promete efectos en salud."),
 ("V05", "Los escombros son solo un problema logístico.", "Sí", "Tratar la remoción como fuente de exposición a partículas", "Eliminar", "Premisa del caso por instrucción del usuario (SUPUESTO)."),
 ("V14", "Una alerta basta para que la población se proteja.", "Sí", "Protocolo con medidas y capacitación, medido como protección efectiva", "Cuestionar", "Sin variable de resultado; no se afirma protección."),
 ("V15", "Las alcaldías usarán el sistema solo por ser nuevo.", "Sí", "Convenios por tramo y compuertas que condicionan la ampliación", "Eliminar", "La adopción es el supuesto crítico SC-3 y se verifica en las compuertas C1 y C2."),
]
n_el = sum(1 for x in dec if x[4] == "Eliminar"); n_cu = sum(1 for x in dec if x[4] == "Cuestionar"); n_ma = sum(1 for x in dec if x[4] == "Mantener")
assert n_el + n_cu + n_ma == 15
tabla("t03", "Análisis crítico de supuestos implícitos por variable",
      ["Variable", "Supuesto implícito", "¿Perjudicial?", "Alternativa imaginable", "Decisión", "Fundamento"], dec,
      "*Nota.* Elaboración propia con el expediente E3-P00 (Tabla E3-4.2), el informe de vigilancia y la ficha maestra. Naturaleza: PROPUESTO. Verificación: NO_VERIFICADO salvo donde se cita fuente.")
A(f"El resultado difiere del expediente: {n_el} supuestos se eliminan, {n_cu} se cuestionan y {n_ma} se mantiene. La diferencia obedece a un criterio de prueba: una creencia se elimina cuando una fuente la contradice, y se cuestiona cuando solo hay una alternativa plausible. Cuatro alternativas de E3 se retiran del diseño porque no tienen respaldo en el corpus: la inferencia en el chip del sensor, el silencio del 90 % de los nodos, los modelos de cizalladura del viento y la provisión de mascarillas.")
A("")
A("El registro de decisión de la {T:t04} cierra el nodo ND-06.")
A("")
tabla("t04", "Registro de decisión GENESIS: ND-06 Desmantelamiento de ortodoxias", ["Campo", "Contenido"], [
 ("NODO", "ND-06 Desmantelamiento de ortodoxias"),
 ("CLASE", "MAYOR. Determina qué supuestos de diseño sobreviven a la formulación."),
 ("DECISION", f"Eliminar {n_el} supuestos con evidencia en contra, cuestionar {n_cu} y mantener {n_ma}; retirar del diseño las cuatro alternativas de E3 sin respaldo en el corpus."),
 ("DECIDE", "Equipo formulador [DATO_USUARIO: responsable de la decisión]. La propuesta proviene de la instancia analítica."),
 ("EXCLUYE", "Eliminar un supuesto por preferencia de diseño. Adoptar la inferencia en el chip del sensor, el silencio del 90 % de los nodos o los modelos de cizalladura del viento."),
 ("NODOS_BLANCOS", "3: corrección con humedad documentada (Jayaratne et al., 2018; Barkjohn et al., 2021); redes sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13); estaciones inactivas (Tavella et al., 2026, p. 6)."),
 ("NODOS_GRISES", "4: latencia de red, línea base de error en escombros, tasa de falsas alarmas y adopción institucional. Ninguno tiene medición."),
 ("RUPTURAS", "R-01: 0 | R-02: 0 | R-03: 0 | R-04: 0 | R-05: 0."),
 ("PATRON_DOMINANTE", "PR-06 (patrón emergente): decidir por la existencia de una fuente que contradiga el supuesto."),
 ("ANTIPATRONES_PR", "PR-04 ausente: Sí. PR-05 ausente: No. La alternativa de convenios por tramo supone capacidad institucional no verificada."),
 ("ESCENA_SIMULABLE", "El equipo revisa en el mes 4 cada supuesto «cuestionado» con los datos del piloto y registra si se confirma o se retira."),
 ("EVIDENCIA_JH_A", "Tres citas del corpus con página (tabla F4.3)."),
 ("EVIDENCIA_JH_B", "Ausencia de fuente para cuatro alternativas de E3: ninguna aparece en el informe de vigilancia."),
 ("CERCA_CONCEPTUAL", "Eliminar un supuesto no prueba que la alternativa funcione. Solo el piloto del tramo 1 lo demuestra."),
 ("ESTATUTO_CAUSAL", "HIE. Ninguna afirmación causal."),
 ("VEREDICTO", "Decisión adoptada con reserva: los supuestos cuestionados se evalúan en el tramo 1."),
 ("RAZON_DEL_DESCARTE", "Se descarta la eliminación en bloque de E3 porque cuatro alternativas carecen de respaldo."),
 ("RESULTADO", "CIERRA con vacíos declarados (latencia, línea base, falsas alarmas, adopción)."),
], "*Nota.* Elaboración propia con el protocolo de decisión GENESIS. Las referencias de las celdas corresponden a la lista del capítulo 19.")

# ---- imports 4.3 a 4.5 ----
fig_map = {
 'DAG_E1': ('dag', 'DAG principal del estimando E1', 'Nota. Elaboración propia con la estructura de la sección F4.3. X: método de corrección (V07). Y: error de medición (V06). U: sorteo semanal. Los nodos latentes se dibujan con trazo discontinuo. Estatuto de todas las relaciones: HIE.'),
 'VESTER_S0_HISTORICO_CONDICIONADO': ('vester_s0', 'Plano Vester del escenario S0: ledger de E3-P04 con 22 aristas', 'Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Eje vertical: influencia activa. Eje horizontal: dependencia pasiva. Las líneas discontinuas marcan las medianas de influencia y de dependencia.'),
 'VESTER_S1_PREVIO_DOC': ('vester_s1', 'Plano Vester del escenario S1: iteración previa con 32 aristas', 'Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Las líneas discontinuas marcan las medianas.'),
 'VESTER_S_TRABAJO_PROPUESTO': ('vester_s2', 'Plano Vester del escenario S2: escenario de trabajo con 48 aristas', 'Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Escenario de trabajo del proyecto. Las líneas discontinuas marcan las medianas.'),
 'VESTER_S3_ENVOLVENTE_ADMISIBLE_BAJA': ('vester_s3', 'Plano Vester del escenario S3: envolvente admisible baja con 21 aristas', 'Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Cada dirección toma el mínimo de su conjunto admisible.'),
 'VESTER_S4_ENVOLVENTE_ADMISIBLE_ALTA': ('vester_s4', 'Plano Vester del escenario S4: envolvente admisible alta con 60 aristas', 'Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Cada dirección toma el máximo de su conjunto admisible.'),
 'MICMAC_S_TRABAJO_PROPUESTO': ('micmac_s2', 'Plano MICMAC del escenario S2 con la potencia de referencia A^10', 'Nota. Elaboración propia con RESULTADOS.json de la sección F4.4. Influencia y dependencia indirectas calculadas con potencias exactas de la matriz hasta k = 10.'),
 'ARBOL_1_SGR_CONV56_AIRE': ('adec', 'A-DEC: estrategia de resolución y custodia posproyecto', 'Nota. Elaboración propia con ARBOL_1_SGR_CONV56_AIRE.json. Árbol de decisión cualitativo; las probabilidades y las utilidades no se declaran por falta de fuente.'),
 'ARBOL_4_SGR_CONV56_AIRE': ('atdc', 'A-TDC: teoría del cambio de la red de vigilancia con custodia distribuida', 'Nota. Elaboración propia con ARBOL_4_SGR_CONV56_AIRE.json. Cada nivel superior exige el cumplimiento del nivel inferior.'),
 'ARBOL_5_SGR_CONV56_AIRE': ('aprob', 'A-PROB: árbol de problemas de la vigilancia de material particulado', 'Nota. Elaboración propia con ARBOL_5_SGR_CONV56_AIRE.json. El problema central es V06; las flechas indican la dirección causa a efecto y su estatuto es HIE.'),
}
TIT_OVR = {
 't015': 'Matriz formal MID_FORMAL de 15 por 15 variables',
 't017': 'Matriz de influencia directa del escenario S0 (ledger de E3-P04, 22 aristas)',
 't018': 'Matriz de influencia directa del escenario S1 (32 aristas)',
 't019': 'Matriz de influencia directa del escenario S2 (48 aristas)',
 't020': 'Matriz de influencia directa del escenario S3 (21 aristas)',
 't021': 'Matriz de influencia directa del escenario S4 (60 aristas)',
 't025': 'Clasificación directa de las variables en el escenario S0', 't026': 'Clasificación directa de las variables en el escenario S1',
 't027': 'Clasificación directa de las variables en el escenario S2', 't028': 'Clasificación directa de las variables en el escenario S3',
 't029': 'Clasificación directa de las variables en el escenario S4',
 't032': 'Estabilidad de las potencias de MICMAC en el escenario S0', 't033': 'Estabilidad de las potencias de MICMAC en el escenario S1',
 't034': 'Estabilidad de las potencias de MICMAC en el escenario S2', 't035': 'Estabilidad de las potencias de MICMAC en el escenario S3',
 't036': 'Estabilidad de las potencias de MICMAC en el escenario S4',
 't040': 'Clasificación indirecta del escenario S2 con la potencia A^10',
 't001': 'Estimando del efecto del método de corrección',
 't104': 'Vacíos y contradicciones con efecto material y ruta de resolución',
 't107': 'Estados problemáticos del árbol A-PROB por nivel', 't108': 'Nodos del árbol A-PROB con su evidencia', 't109': 'Relaciones del árbol A-PROB y su fuente',
}
ctx = {'n': 0, 'usados': {}, 'sec': '4.3'}
# los ids de t01-t04 propios ya existen; los importados usan t1xx para evitar colisiones
def importar(ruta, sec, quitar_refs=True):
    ctx['sec'] = sec
    t = strip_head(rd(ruta))
    refs = ''
    m = re.search(r'\n\*\*Referencias de la sección[^\n]*\*\*.*', t, re.S)
    if m: refs = m.group(0); t = t[:m.start()] + '\n'
    m = re.search(r'\n### 4\.5\.7 Referencias.*', t, re.S)
    if m: refs = m.group(0); t = t[:m.start()] + '\n'
    m = re.search(r'\n### 4\.4-MDR\.14 Referencias APA 7.*', t, re.S)
    if m: refs = m.group(0); t = t[:m.start()] + '\n'
    return t, refs
refs_removidas = {}
fichas_texto = ''; json_blocks = []
t43, r43 = importar('SECCION_4_3/SECCION_4_3_SGR_CONV56_AIRE.md', '4.3'); refs_removidas['4.3'] = r43
t44, r44 = importar('SECCION_4_4/SECCION_4_4_SGR_CONV56_AIRE.md', '4.4'); refs_removidas['4.4'] = r44
tmd, rmd = importar('SECCION_4_4_MDR/SECCION_4_4_MDR_SGR_CONV56_AIRE.md', 'F4.4-MDR'); refs_removidas['MDR'] = rmd
t45, r45 = importar('SECCION_4_5/SECCION_4_5_SGR_CONV56_AIRE.md', '4.5'); refs_removidas['4.5'] = r45
# fichas al Anexo K
a = t44.index('**Ficha 001'); b = t44.index('### 4.4.5 ')
fichas_texto = t44[a:b]
t44 = t44[:a] + ('Las 105 fichas bidireccionales se reproducen en el Anexo K, en el orden del plan paritario. Cada ficha conserva sus dos direcciones, sus campos y sus estados.\n\n') + t44[b:]
nf = len(re.findall(r'^\*\*Ficha \d{3} · ', fichas_texto, flags=re.M)); assert nf == 105, nf
# JSON grandes al Anexo L
def sacar_json(t, etiquetas):
    bl = []
    def sub(m):
        body = m.group(0)
        if body.count('\n') > 40:
            bl.append(body); return etiquetas[len(bl) - 1]
        return body
    t = re.sub(r'```json\n.*?\n```', sub, t, flags=re.S)
    return t, bl
tmd, jm = sacar_json(tmd, ['El JSON canónico de A-DEC se reproduce sin cambios en el Anexo L (L.1).', 'El JSON canónico de A-TDC se reproduce sin cambios en el Anexo L (L.2).']); assert len(jm) == 2, len(jm)
t45, j5 = sacar_json(t45, ['El JSON canónico de A-PROB se reproduce sin cambios en el Anexo L (L.3).']); assert len(j5) == 1

imported = {}
for key, texto in (('4.3', t43), ('4.4', t44), ('MDR', tmd), ('4.5', t45)):
    ctx['sec'] = {'4.3': 'F4.3', '4.4': 'F4.4', 'MDR': 'F4.4-MDR', '4.5': 'F4.5'}[key]
    # ids únicos: prefijo 'x' + contador global
    out, tabs = convertir(texto, 'F4', fig_map, ctx)
    imported[key] = (out, tabs)
# renombra ids t001.. -> i001.. para no colisionar con t01..t04 propios, y aplica sobrescrituras de título
def retitular(lines, tabs):
    txt = '\n'.join(lines)
    for tid, tit in tabs:
        nuevo = TIT_OVR.get(tid, tit)
        txt = txt.replace(f':::TABLA {tid} | {tit}', f':::TABLA i{tid[1:]} | {nuevo}')
        txt = txt.replace('{T:' + tid + '}', '{T:i' + tid[1:] + '}')
        txt = txt.replace(f'reúne los datos de «{tit}»', f'reúne los datos de «{nuevo}»')
        txt = txt.replace(f'La {{T:i{tid[1:]}}} presenta {tit[:1].lower() + tit[1:]}.', f'La {{T:i{tid[1:]}}} reúne los datos de «{nuevo}».')
    return txt
cuerpo = {}
for key, (out, tabs) in imported.items():
    cuerpo[key] = retitular(out, tabs)
# frases de mención genéricas de las figuras: forma «reproduce»
for key in cuerpo:
    cuerpo[key] = re.sub(r'La \{F:(\w+)\} presenta ([^\n]*)\.', lambda m: f'La {{F:{m.group(1)}}} reproduce «{m.group(2)[:1].upper() + m.group(2)[1:]}».', cuerpo[key])
    cuerpo[key] = re.sub(r'La \{T:(i\d+)\} presenta ([^\n]*)\.', lambda m: f'La {{T:{m.group(1)}}} reúne los datos de «{m.group(2)[:1].upper() + m.group(2)[1:]}».', cuerpo[key])
REEMP = [
 ("La figura y su alternativa textual constan en DAG_E1.svg y DAG_E1.alt.md.", "La figura se presenta redibujada con la plantilla visual del proyecto. El SVG original del motor y su alternativa textual constan en el repositorio, en DAG_E1.svg y DAG_E1.alt.md."),
 ("Dice que «demuestra matemáticamente que la arquitectura modelada es un Grafo Dirigido Acíclico».", "Afirma haber probado matemáticamente que la arquitectura modelada es un grafo dirigido acíclico."),
 ("DETECTADO: «garantiza matemáticamente» y «demuestra matemáticamente» en E3-P05, E3-P09 y E3-P19.", "DETECTADO: expresiones de garantía y de prueba matemática en E3-P05, E3-P09 y E3-P19."),
 ("Estado: NO_PRIORIZACION_ROBUSTA con esa envolvente.", "Estado: NO_PRIORIZACION_ESTABLE con esa envolvente."),
 ("Comprobaciones del SVG:", "Comprobaciones del SVG original del motor (la figura del documento es una versión redibujada con la plantilla visual):"),
 ("Pedraza et al. (2026", "Murad Pedraza et al. (2026"),
]
for k in cuerpo:
    for a, b in REEMP:
        cuerpo[k] = cuerpo[k].replace(a, b)
    cuerpo[k] = cuerpo[k].replace("Murad Murad Pedraza", "Murad Pedraza")
    cuerpo[k] = re.sub(r"\*\*Revisión visual\.\*\*[^\n]*", "**Revisión visual.** Las figuras del documento se redibujaron con la plantilla visual del proyecto a partir de los mismos datos y se revisaron como imágenes. Los textos se leen completos y ningún nodo se superpone.", cuerpo[k])
for k in cuerpo:
    cuerpo[k] = re.sub(r"(?m)^(Árbol \d · .*|Pregunta: .*|Naturaleza: .*|Valor esperado en la raíz: .*|Errores de coherencia: .*|Comprobaciones del SVG.*)$", lambda m: "- " + m.group(1).rstrip(), cuerpo[k])
A("")
CMP = "::::::::: {custom-style=\"CuerpoCompacto\"}"
for k_ in ('4.3', '4.4', 'MDR', '4.5'):
    A(CMP); A(cuerpo[k_]); A(":::::::::"); A("")

# ---- 4.6 a 4.8 ----
A("## F4.6 Técnica de los cinco porqués")
A("")
A("La técnica de los cinco porqués recorre la cadena de causas desde el problema central hasta una causa estructural. Cada respuesta se apoya en las relaciones del escenario S2 (sección F4.4) y en la evidencia del corpus. Ninguna respuesta afirma un efecto causal estimado. Todas son hipótesis de influencia estructural (HIE). El rol DAG de la última columna proviene de la tabla de clasificación de la sección F4.3.")
A("")
A("La {T:t05} presenta las cinco preguntas. La quinta respuesta es una hipótesis de diseño y compite con la causa raíz que declara E3, la arquitectura dependiente de la nube. Ninguna de las 15 variables representa esa arquitectura, de modo que esta formulación la trata como hipótesis rival y no como causa raíz.")
A("")
tabla("t05", "Aplicación de los cinco porqués a la causa crítica principal", ["Nivel", "Pregunta", "Respuesta", "Evidencia", "Rol DAG (F4.3)"], [
 ("P1", "¿Por qué existe el problema central?", "Las lecturas ópticas de PM2,5 y PM10 no se verifican frente a una referencia en los sitios de remoción (V06).", "Línea base VACIO; el expediente declara NMAE superior a 45 % sin localizador", "Resultado Y"),
 ("P2", "¿Por qué el error de lectura es alto?", "La humedad relativa (V03) y la fracción gruesa (V02) alteran la respuesta óptica sin corrección local. En S2, V03→V06 = 3 y V02→V06 = 3.", "Suresh et al. (2025, p. 30): correlación de 0,73 con la humedad; Bang et al. (2026, pp. 6-8): R² de menos de 0,2 a 0,81 con corrección", "Predictor de Y y moderador"),
 ("P3", "¿Por qué no hay corrección local?", "La calibración es estática o inexistente (V07→V06 = 3) y no hay referencias colocalizadas.", "Murad Pedraza et al. (2026, pp. 10-11 y 13): 90,8 % de 5.076 estaciones sin plan de calibración (cálculo del analista)", "Exposición X"),
 ("P4", "¿Por qué no se calibra en el sitio?", "La calibración depende de referencias costosas, de energía y de enlace estables. La remoción (V05) degrada la disponibilidad de nodos (V05→V09 = 2) y expone los cabezales al polvo.", "Ficha V05→V09 de la sección F4.4.4; Tavella et al. (2026, p. 6)", "Predictor indirecto y causa de atrición"),
 ("P5", "¿Por qué ocurre lo anterior?", "Causa raíz (hipótesis de diseño): la red de bajo costo opera sin un protocolo de calibración colocalizada y de corrección en el borde, con custodia institucional, adaptado a sitios de remoción de escombros.", "INFERIDO; sin estimando identificado", "No aplica (hipótesis estructural)"),
], "*Nota.* Elaboración propia con la ficha maestra (sección 10b) y el escenario S2 de la sección F4.4. Estatuto: HIE. Los valores V03→V06 y los demás son puntuaciones PROPUESTAS de la escala 0 a 3.")
A("## F4.7 Causas priorizadas para intervención")
A("")
A("La priorización usa el escenario de trabajo S2 con corte por mediana (influencia y dependencia con mediana de 5). La clasificación de Vester ordena variables por su posición estructural y no estima efectos. La {T:t06} reúne las cinco causas que el análisis prioriza. La variable V04 (viento) tiene influencia 8 y dependencia 0, pero es exógena: el proyecto no puede intervenir sobre ella y por eso no integra la lista.")
A("")
def fila_cuadrante(v): return S2[v]["clase_mediana"].replace("_", " ").lower()
tabla("t06", "Cinco causas críticas o activas priorizadas para intervención", ["Código", "Nombre", "Influencia (TA)", "Dependencia (TP)", "Cuadrante (mediana)", "Estatuto", "Justificación", "Intervención"], [
 ("V06", "Error de medición IoT", str(S2["V06"]["influencia"]), str(S2["V06"]["dependencia"]), fila_cuadrante("V06"), "HIE", "Problema central: mayor dependencia del sistema y crítica en los cinco escenarios.", "Colocalización con referencia gravimétrica y corrección en el gateway (OE1)"),
 ("V02", "Concentración de PM10 con fracción gruesa", str(S2["V02"]["influencia"]), str(S2["V02"]["dependencia"]), fila_cuadrante("V02"), "HIE", "Influye con peso 3 sobre V06 y depende de la remoción.", "Modelo con fracción gruesa e inlet protegido (OE1)"),
 ("V15", "Adopción institucional", str(S2["V15"]["influencia"]), str(S2["V15"]["dependencia"]), fila_cuadrante("V15"), "HIE", "Aparece en 140 de 144 ciclos simples del escenario; sostiene el supuesto SC-3.", "Co-diseño con los comités, formación y convenios por tramo (OE3)"),
 ("V03", "Humedad relativa", str(S2["V03"]["influencia"]), str(S2["V03"]["dependencia"]), fila_cuadrante("V03"), "HIE", "Moderador de la respuesta óptica; exógena.", "Modelo de corrección con interacción por humedad (OE1)"),
 ("V05", "Volumen de escombros", str(S2["V05"]["influencia"]), str(S2["V05"]["dependencia"]), fila_cuadrante("V05"), "HIE", "Fuente de PM10 y causa de atrición de nodos.", "Energía y enlace redundantes, ubicación de nodos y mantenimiento (OE2)"),
], "*Nota.* Elaboración propia con RESULTADOS.json de la sección F4.4, escenario S2 (semilla 20261011). Los cinco puntajes de influencia y dependencia son totales de fila y de columna de la matriz de 15 por 15. Naturaleza: CALCULADO sobre juicios PROPUESTOS.")
A("Las tres variables críticas (V02, V06 y V15) y las dos activas (V03 y V05) coinciden con los tres objetivos específicos del proyecto. V06, V02 y V03 conducen a OE1; V05 conduce a OE2 a través de V09; V15 conduce a OE3. Esa correspondencia es un resultado de diseño: los objetivos se formularon después de la priorización y no antes.")
A("")
A("## F4.8 Causa raíz identificada")
A("")
A("**Formulación.** La red de bajo costo opera sin un protocolo de calibración colocalizada y de corrección en el borde, con custodia institucional, adaptado a sitios de remoción de escombros. Por ello entrega mediciones de error desconocido y reduce el uso institucional de las alertas.")
A("")
A("**Evidencia.** Tres fuentes respaldan la formulación. Primera, Bang et al. (2026, pp. 6-8) muestran que una corrección local con estación cercana eleva el R² de menos de 0,2 a 0,81. Segunda, Murad Pedraza et al. (2026, pp. 10-11 y 13) reportan que 90,8 % de las estaciones de la red nacional propuesta serían sensores sin plan de calibración, cálculo del analista sobre las cifras del documento. Tercera, Suresh et al. (2025, p. 30) reportan una correlación de 0,73 entre partículas y humedad en una mina a cielo abierto.")
A("")
A("**Clasificación de inferencia causal.** La causa raíz es una hipótesis estructural (HIE) y no un efecto estimado. Debe incluirse en el modelo como exposición X (método de corrección) y no como mecanismo, porque el proyecto la manipula por diseño. El estimando E1 es identificable solo si se ejecuta el sorteo semanal descrito en la sección F4.3.")
A("")
A("**Validación contra las ortodoxias desmanteladas.** La formulación no depende de las creencias eliminadas en la {T:t03}: no supone inferencia en el chip del sensor, ni nodos silenciosos al 90 %, ni modelos de cizalladura. Depende de dos supuestos aún no verificados: que la corrección con colocalización generaliza a sitios de remoción (R-TEC-04) y que los comités adoptan el tablero (SC-3).")
A("")
A("La {T:t07} registra la decisión sobre la causa raíz (nodo ND-10).")
A("")
tabla("t07", "Registro de decisión GENESIS: ND-10 Causa raíz adoptada", ["Campo", "Contenido"], [
 ("NODO", "ND-10 Causa raíz adoptada"),
 ("CLASE", "MAYOR. Orienta la selección de alternativas del Paso 6."),
 ("DECISION", "Adoptar como causa raíz la ausencia de un protocolo de calibración colocalizada y corrección en el borde con custodia institucional, y tratar la arquitectura dependiente de la nube como hipótesis rival."),
 ("DECIDE", "Equipo formulador [DATO_USUARIO: responsable de la decisión]. La propuesta proviene de la instancia analítica."),
 ("EXCLUYE", "Declarar causa raíz una arquitectura que ninguna de las 15 variables representa. Pasar de HIE a IDC por posición en Vester o ascenso en MICMAC."),
 ("NODOS_BLANCOS", "3: Bang et al. (2026, pp. 6-8); Murad Pedraza et al. (2026, pp. 10-11 y 13); Suresh et al. (2025, p. 30)."),
 ("NODOS_GRISES", "3: generalización a sitios de remoción; línea base de error propia; adopción institucional."),
 ("RUPTURAS", "R-01: 0 | R-02: 0 | R-03: 0 | R-04: 0 | R-05: 1 (la cadena hasta personas protegidas permanece HIE)."),
 ("PATRON_DOMINANTE", "PR-06 (patrón emergente): causa raíz como hipótesis de diseño falsable en el piloto."),
 ("ANTIPATRONES_PR", "PR-04 ausente: Sí. PR-05 ausente: No. La custodia depende de entidades cuya capacidad no se verificó."),
 ("ESCENA_SIMULABLE", "En el mes 12, la compuerta C1 compara el NMAE y el R² del piloto con los umbrales; si no se cumplen, la hipótesis se revisa."),
 ("EVIDENCIA_JH_A", "Tres citas del corpus con página."),
 ("EVIDENCIA_JH_B", "Escenario S2: V06 es crítica en los cinco escenarios (sección F4.4.8)."),
 ("CERCA_CONCEPTUAL", "La causa raíz no prueba que la corrección reduzca el error en escombros. El piloto del tramo 1 lo mide."),
 ("ESTATUTO_CAUSAL", "HIE. Ninguna afirmación EST."),
 ("VEREDICTO", "Causa raíz adoptada como hipótesis de diseño, con la hipótesis rival registrada."),
 ("RAZON_DEL_DESCARTE", "Se descarta la «arquitectura dependiente de la nube» como causa raíz: carece de variable que la represente en el modelo de 15 variables."),
 ("RESULTADO", "CIERRA con vacíos declarados (generalización, línea base y adopción)."),
], "*Nota.* Elaboración propia con el protocolo de decisión GENESIS y la ficha maestra (sección 10b).")
A("Los pasos siguientes parten de esta hipótesis. El Paso 5 la formaliza en tres niveles y el Paso 6 genera las alternativas que la resuelven. Un último control cierra el paso: la {T:t08} verifica la completitud de las secciones.")
A("")
tabla("t08", "Verificación de completitud del Paso 4", ["Sección", "Contenido exigido", "Estado", "Dónde"], [
 ("F4.1", "15 causas con evidencia y validación territorial", "Completa; evidencia con vacíos declarados; articulación territorial NO_VERIFICADO", "Tablas F4.1 y F4.2"),
 ("F4.2", "Desmantelamiento de ortodoxias", "Completa; 15 de 15 supuestos analizados", "Tabla F4.3"),
 ("F4.3", "Estimando, DAG, DAG rivales y estatutos", "Completa", "Sección F4.3"),
 ("F4.4", "Vester y MICMAC en cinco escenarios con 105 fichas", "Completa; fichas en el Anexo K", "Sección F4.4 y Anexo K"),
 ("F4.4-MDR", "Metodología de decisión, teoría del cambio, sostenibilidad, premortem y escenarios", "Completa", "Sección F4.4-MDR"),
 ("F4.5", "Árbol de problemas", "Completa; JSON en el Anexo L", "Sección F4.5 y Anexo L"),
 ("F4.6 a F4.8", "Cinco porqués, causas priorizadas y causa raíz", "Completa", "Tablas F4.5 a F4.7"),
], "*Nota.* Elaboración propia. Las tablas importadas de las secciones F4.3 a F4.5 se numeran con el prefijo F4 en orden de aparición.")
open(RAIZ + "/caps/paso4.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---- anexos K, L, M ----
K = []; B = K.append
B("%% PREFIJO: 20")
B("")
B("## Anexo K. Fichas bidireccionales del análisis estructural")
B("")
B("El Anexo K reproduce las 105 fichas bidireccionales de la sección F4.4.4 en el orden del plan paritario. Cada ficha registra los dos sentidos de influencia de un par de variables, con sus mecanismos, fundamentos, valores propuestos y estados. Los valores son juicios PROPUESTOS por la instancia analítica y ninguno equivale a una adjudicación independiente.")
B("")
B("::::::::: {custom-style=\"CuerpoCompacto\"}"); B(imp4.renum(fichas_texto).replace('\n\n\n', '\n\n')); B(":::::::::")
B("")
B("## Anexo L. JSON canónico de los árboles A-DEC, A-TDC y A-PROB")
B("")
B("Los tres árboles se regeneran con la herramienta de referencia a partir de su JSON canónico. El texto de cada bloque coincide con el del archivo correspondiente del repositorio.")
B("")
B("### L.1 JSON canónico del árbol A-DEC (ARBOL_1_SGR_CONV56_AIRE.json)")
B("")
B(jm[0].replace('```json', '```', 1)); B("")
B("### L.2 JSON canónico del árbol A-TDC (ARBOL_4_SGR_CONV56_AIRE.json)")
B("")
B(jm[1].replace('```json', '```', 1)); B("")
B("### L.3 JSON canónico del árbol A-PROB (ARBOL_5_SGR_CONV56_AIRE.json)")
B("")
B(j5[0].replace('```json', '```', 1)); B("")
z = zipfile.ZipFile(f'{R}/respaldo/RESPALDO_SGR_CONV56_AIRE_CP_20261013_E4_4_5_01.zip')
man = json.loads(z.read('MANIFIESTO.json'))
B("## Anexo M. Inventario de archivos de la sección 4")
B("")
B(f"El manifiesto del respaldo CP_20261013_E4_4_5_01 registra {man['file_count']} archivos con su huella SHA-256 calculada sobre los bytes. El manifiesto no incluye su propio hash. El método declarado es {man['checksum_method']}. La {{T:k01}} permite verificar que los archivos fuente del repositorio coinciden con los que originan las secciones F4.3 a F4.5.")
B("")
B(":::TABLA k01 | Inventario de archivos del respaldo con huella SHA-256")
B("| Archivo | Clase | Bytes | SHA-256 |"); B("| --- | --- | --- | --- |")
for f in man['files']:
    B(f"| {f['path'].replace('expediente/', '', 1)} | {f['kind']} | {f['bytes']} | {f['sha256']} |")
B(":::NOTA *Nota.* Elaboración propia con MANIFIESTO.json del respaldo RESPALDO_SGR_CONV56_AIRE_CP_20261013_E4_4_5_01.zip.")
B("")
open(RAIZ + "/caps/anexos_km.md", "w", encoding="utf-8").write("\n".join(K) + "\n")
open(RAIZ + "/pasos/refs_removidas_paso4.json", "w", encoding="utf-8").write(json.dumps(refs_removidas, ensure_ascii=False, indent=1))
print("ok", len(" ".join(L).split()), "palabras paso4;", len(" ".join(K).split()), "anexos")
