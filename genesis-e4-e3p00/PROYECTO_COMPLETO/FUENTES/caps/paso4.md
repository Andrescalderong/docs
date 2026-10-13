%% PREFIJO: F4
# Paso 4. Análisis causal completo

El Paso 4 identifica las causas del problema central, desmantela las ortodoxias que condicionan el diseño y establece qué afirmaciones causales admite la evidencia. Sigue la secuencia del metaprompt en nueve etapas. Las primeras son la identificación de causas (F4.1) y el desmantelamiento de ortodoxias (F4.2). Siguen la clasificación de variables para inferencia causal (F4.3) y el análisis estructural de Vester y MICMAC (F4.4). Después vienen la metodología integrada de decisión y resolución (F4.4-MDR) y el árbol de problemas (F4.5). Cierran los cinco porqués (F4.6), las causas priorizadas (F4.7) y la causa raíz (F4.8).

El análisis recorre 15 variables que E3-P01 definió y que esta formulación conserva. Ninguna relación entre variables se trata como efecto causal estimado. Todas son hipótesis de influencia estructural (estatuto HIE). El único estimando con identificación posible es el efecto del método de corrección sobre el error de medición. Solo es identificable si se ejecuta el sorteo semanal que propone el informe de vigilancia (estatuto IDC prospectivo). Las secciones F4.3 a F4.5 reproducen el análisis completo, con sus 105 fichas bidireccionales en el Anexo K.

## F4.1 Identificación de causas con evidencia

El metaprompt pide 15 causas en cinco categorías: tecnológicas, organizacionales, económicas, de ecosistema y territoriales o institucionales. El expediente E3-P00 respondió con sus 15 variables, que mezclan causas, condiciones y efectos. Esta sección asigna cada variable a una categoría y registra su evidencia con fuente y página, solo cuando el corpus la contiene. Donde el corpus calla, la tabla declara VACIO y no completa la celda con una cifra del expediente.

El diccionario no contiene variables económicas. El costo de calibrar, el costo de custodia y el financiamiento posproyecto se tratan en la sección F4.4-MDR y en el capítulo 14. Esa omisión es un límite del diccionario de 15 variables y no una ausencia de causas económicas. La {T:t01} presenta las variables agrupadas por categoría.

:::TABLA t01 | Identificación de las 15 causas y condiciones con su evidencia
| Código | Categoría | Descripción | Evidencia (fuente y página) | Magnitud | Naturaleza | Verificación |
| --- | --- | --- | --- | --- | --- | --- |
| V06 | Tecnológica | Error de medición de PM2,5 y PM10 frente a una referencia gravimétrica; problema central | Bang et al. (2026, pp. 6-8): con una estación cercana y un desfase de 35 minutos, el R² pasó de menos de 0,2 a 0,81 | Línea base propia: VACIO (se mide en el tramo 1). El expediente declara NMAE superior a 45 % sin localizador | DECLARADO | NO_VERIFICADO |
| V07 | Tecnológica | Frecuencia de calibración de los nodos, medida en ajustes por semana | Murad Pedraza et al. (2026, pp. 10-11 y 13) | 90,8 % de 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (cálculo del analista) | CALCULADO | PARCIALMENTE_VERIFICADO |
| V08 | Tecnológica | Latencia de datos entre el nodo y la nube | Bang et al. (2026, pp. 6-8): desfase sensor-estación de 35 minutos, que no equivale a latencia de red | VACIO: no hay medición de latencia de red | VACIO | NO_VERIFICADO |
| V09 | Tecnológica | Disponibilidad de nodos con energía y enlace | Tavella et al. (2026, p. 6) | 96 de 570 estaciones inactivas o sin estado en Brasil, 2022 a 2024: 16,8 % | DOCUMENTADO | NO_VERIFICADO |
| V10 | Tecnológica | Densidad efectiva del gemelo digital | VACIO: el corpus no reporta densidad efectiva | Diseño propuesto: 100 nodos y 10 gateways en 12 municipios | PROPUESTO | NO_APLICA |
| V01 | Ecosistema | Concentración de PM2,5 en el sitio | Informe de vigilancia, §3.1 (Suresh et al., 2025): cociente PM2,5/PM10 de 0,88 en una mina | Sin serie del territorio | VACIO | NO_VERIFICADO |
| V02 | Ecosistema | Concentración de PM10, con fracción gruesa | Informe de vigilancia, §3.1 (Suresh et al., 2025): régimen distinto del de escombros | Sin serie del territorio | INFERIDO | NO_VERIFICADO |
| V03 | Ecosistema | Humedad relativa en el sitio de medición | Suresh et al. (2025, p. 30) | Correlación de 0,73 entre partículas y humedad en una mina a cielo abierto | DOCUMENTADO | PARCIALMENTE_VERIFICADO |
| V04 | Ecosistema | Velocidad del viento superficial | Informe de vigilancia, §11.4: control del error normalizado | VACIO: sin serie del territorio | VACIO | NO_VERIFICADO |
| V05 | Territorial | Volumen de escombros removido (actividad en el sitio) | Premisa del caso por instrucción del usuario | [DATO_USUARIO: toneladas por día en cada sitio de remoción] | SUPUESTO | NO_VERIFICADO |
| V11 | Organizacional | Índice AQHI emitido, sin fórmula local validada | Liao et al. (2026, pp. 6 y 8) | 53 estudios de AQHI; 9,4 % con partición de datos y 11,3 % con análisis de sensibilidad | DOCUMENTADO | NO_VERIFICADO |
| V12 | Organizacional | Tasa de falsas alarmas | Informe de vigilancia, §1.3, hallazgo 2: ningún documento de alertas la reporta | VACIO | VACIO | NO_VERIFICADO |
| V13 | Organizacional | Anticipación del aviso, en horas | VACIO: sin línea base en el corpus | VACIO | VACIO | NO_VERIFICADO |
| V14 | Institucional | Personas bajo protección efectiva por alertas | VACIO: sin variable de resultado ni línea base | VACIO | VACIO | NO_VERIFICADO |
| V15 | Institucional | Adopción institucional del tablero | Supuesto crítico SC-3; sin medición de uso | VACIO: se mide desde el tramo 1 | SUPUESTO | NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el diccionario de la sección F4.4.2, la ficha maestra y el informe de vigilancia tecnológica (F-INF). Las citas con página proceden del informe, no de lectura de la fuente primaria.

De las 15 variables, 8 cuentan con una cita del corpus y 7 quedan sin evidencia propia. Las 8 citas tienen una limitación común. Provienen de entornos distintos del sitio de remoción de escombros, como una mina a cielo abierto, estaciones brasileñas o estudios de índices en China. Por esa razón, el proyecto no usa ninguna de estas cifras como línea base. Las usa como motivo para medir: la colocalización del tramo 1 produce la línea base propia de V06, V12 y V15.

### F4.1.1 Validación de la articulación territorial de las causas

El metaprompt exige un origen territorial para al menos dos causas. Las fuentes admitidas son tres. La primera es el diagnóstico del Plan de Desarrollo Departamental (PDD). La segunda son las demandas territoriales del Anexo 4. La tercera son los diagnósticos del Observatorio de Ciencia y Tecnología. Exige también que al menos 8 de 15 causas tengan un respaldo territorial. El expediente E3-P00 declara 10 causas articuladas. Cada una lleva un artículo del PDD, un indicador y un código de demanda. Lleva además una misión de la política de investigación e innovación orientada por misiones (PIIOM).

Ninguno de esos documentos se aportó. Los artículos, indicadores y códigos de la {T:t02} son declaraciones de E3 sin fuente verificable. Algunos códigos repiten el mismo patrón entre departamentos, y por ello la tabla los conserva como declarados. La regla de 8 de 15 se cumple en la declaración y no se cumple en la verificación: 0 de 15 respaldos verificados.

:::TABLA t02 | Articulación territorial declarada por E3 para cada causa
| Variable | PDD (artículo o eje) e indicador declarados | Código de demanda territorial declarado | Misión PIIOM declarada | Naturaleza | Verificación |
| --- | --- | --- | --- | --- | --- |
| V06 | PDD Caldas, Eje 2; «Sensores instalados» | Cal-11 | Misión 3 | DECLARADO | NO_VERIFICADO |
| V07 | PDD Valle del Cauca, Art. 45; «Nodos calibrados» | Val-7 | Misión 3 | DECLARADO | NO_VERIFICADO |
| V08 | Sin articulación declarada | No | Misión 2 | DECLARADO | NO_VERIFICADO |
| V09 | PDD Cundinamarca, Eje 3; «Cobertura de red IoT» | Cun-11 | Misión 3 | DECLARADO | NO_VERIFICADO |
| V10 | Sin articulación declarada | No | No | DECLARADO | NO_VERIFICADO |
| V01 | PDD Caldas, Eje 4; «Nivel PM2.5 anual» | No | Misión 5 | DECLARADO | NO_VERIFICADO |
| V02 | PDD Valle del Cauca, Art. 50; «Nivel PM10 anual» | No | Misión 5 | DECLARADO | NO_VERIFICADO |
| V03 | Sin articulación declarada | No | No | DECLARADO | NO_VERIFICADO |
| V04 | Sin articulación declarada | No | No | DECLARADO | NO_VERIFICADO |
| V11 | PDD Cundinamarca, Art. 12; «Índice de riesgo en salud» | Cun-11 | Misión 1 | DECLARADO | NO_VERIFICADO |
| V12 | Sin articulación declarada | No | No | DECLARADO | NO_VERIFICADO |
| V13 | PDD Caldas, Eje 2; «Tiempo de alerta temprana» | Cal-11 | Misión 3 | DECLARADO | NO_VERIFICADO |
| V05 | PDD Valle del Cauca, Eje 3; «Toneladas dispuestas» | Val-7 | Misión 5 | DECLARADO | NO_VERIFICADO |
| V14 | PDD Caldas, Art. 22; «Personas alertadas» | Cal-11 | Misión 1 | DECLARADO | NO_VERIFICADO |
| V15 | PDD Cundinamarca, Art. 30; «% de municipios con SAT» | Cun-11 | Misión 3 | DECLARADO | NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente E3-P00 (Tabla E3-4.1a). El PDD, el Anexo 4 de la convocatoria, la PIIOM y el diagnóstico del Observatorio no se aportaron. SAT: sistema de alerta temprana. Ver decisión DEC-F12.

La decisión DEC-F12 mantiene la formulación y registra la reserva R-ART. La corrida continúa por orden expresa del usuario. El cierre del documento lista los cinco documentos que el equipo formulador debe obtener antes de radicar: PDD de los tres departamentos, Anexo 4, PIIOM, diagnóstico del Observatorio y CONPES vigentes.

## F4.2 Desmantelamiento de ortodoxias

Una ortodoxia es un supuesto implícito que orienta el diseño sin haberse sometido a prueba. El método plantea tres preguntas para cada variable. Pregunta si la creencia perjudica el objetivo, si se puede imaginar una alternativa y qué ocurriría si el supuesto fuera falso. La {T:t03} aplica las tres preguntas a las 15 variables. Las decisiones posibles son mantener, cuestionar o eliminar el supuesto.

El expediente E3-P00 eliminó nueve de quince ortodoxias. Propuso alternativas técnicas específicas, como la inferencia en el chip del sensor o los nodos que duermen el 90 % del tiempo. Esta formulación revisa cada decisión contra el corpus y contra la arquitectura que adopta (corrección en el gateway). Una ortodoxia solo se elimina cuando existe evidencia en contra. Si la alternativa carece de respaldo, el supuesto se cuestiona y se pone a prueba en el piloto.

:::TABLA t03 | Análisis crítico de supuestos implícitos por variable
| Variable | Supuesto implícito | ¿Perjudicial? | Alternativa imaginable | Decisión | Fundamento |
| --- | --- | --- | --- | --- | --- |
| V06 | Un sensor de bajo costo nunca alcanza la calidad de una referencia. | Sí | Corrección con modelo entrenado por colocalización, evaluada con los umbrales de EPA (2021) | Cuestionar | Barkjohn et al. (2021) aplicaron una corrección que incorpora la humedad; el piloto del tramo 1 mide si el resultado se sostiene en escombros. |
| V07 | La calibración exige retirar el sensor al laboratorio. | Sí | Actualización remota del modelo de corrección en el gateway, con ciclos de colocalización | Eliminar | Murad Pedraza et al. (2026, pp. 10-11 y 13) reportan redes sin plan de calibración; el diseño separa la calibración del retiro físico. |
| V08 | Hay que transmitir el dato crudo continuamente a la nube. | Sí | Corrección en el gateway y envío del dato corregido con almacenamiento local de 7 días | Cuestionar | El valor de latencia es VACIO; el piloto la mide antes de optimizarla. |
| V09 | Los nodos fallan porque consumen mucha energía. | Sí | Autonomía mínima de 14 días sin sol y reserva de 20 nodos | Cuestionar | Tavella et al. (2026, p. 6) reportan 16,8 % de estaciones inactivas o sin estado; la causa de la inactividad no consta. |
| V10 | Un gemelo digital exige modelos numéricos de gran tamaño. | No | Estimación espacial por interpolación con la red de 100 nodos | Mantener | Sin evidencia propia; se evalúa en el tramo 2 con la densidad efectiva. |
| V01 | El PM2,5 se predice con variables climáticas simples. | Sí | Medir en el sitio con referencia colocalizada | Cuestionar | El proyecto mide y corrige; no predice. |
| V02 | El polvo de demolición equivale a la contaminación urbana. | Sí | Tratar V02 como fracción gruesa (PM10 menos PM2,5) | Eliminar | El cociente PM2,5/PM10 de 0,88 en una mina (Suresh et al., 2025) corresponde a otro régimen; la ficha de V02 propone la redefinición. |
| V03 | La humedad daña de forma irreversible el sensor óptico. | Sí | Corregir el sesgo higroscópico con el modelo | Eliminar | Jayaratne et al. (2018) y Barkjohn et al. (2021) muestran corrección posible con humedad; la carcasa mitiga el daño por condensación. |
| V04 | El viento superficial es constante en el sitio. | Sí | Registrar viento como variable de control | Cuestionar | No existe serie del territorio; E3 propone modelos de cizalladura, que el proyecto no adopta. |
| V11 | Un índice de calidad del aire mide el riesgo de salud. | Sí | AQHI con fórmula y umbrales validados localmente | Cuestionar | Liao et al. (2026, pp. 6 y 8): 9,4 % de los estudios usó partición de datos; la validación local es una tarea del proyecto. |
| V12 | Las falsas alarmas son inevitables con sensores baratos. | Sí | Medir la tasa de falsas alarmas y reducirla con la corrección | Cuestionar | Ningún documento de alertas del corpus la reporta. |
| V13 | Anticipar una hora salva pocas vidas. | Sí | Medir la anticipación y no afirmar efectos sobre vidas | Cuestionar | Sin línea base en el corpus; el proyecto no promete efectos en salud. |
| V05 | Los escombros son solo un problema logístico. | Sí | Tratar la remoción como fuente de exposición a partículas | Eliminar | Premisa del caso por instrucción del usuario (SUPUESTO). |
| V14 | Una alerta basta para que la población se proteja. | Sí | Protocolo con medidas y capacitación, medido como protección efectiva | Cuestionar | Sin variable de resultado; no se afirma protección. |
| V15 | Las alcaldías usarán el sistema solo por ser nuevo. | Sí | Convenios por tramo y compuertas que condicionan la ampliación | Eliminar | La adopción es el supuesto crítico SC-3 y se verifica en las compuertas C1 y C2. |
:::NOTA *Nota.* Elaboración propia con el expediente E3-P00 (Tabla E3-4.2), el informe de vigilancia y la ficha maestra. Naturaleza: PROPUESTO. Verificación: NO_VERIFICADO salvo donde se cita fuente.

El resultado difiere del expediente: 5 supuestos se eliminan, 9 se cuestionan y 1 se mantiene. La diferencia obedece a un criterio de prueba. Una creencia se elimina cuando una fuente la contradice. Se cuestiona cuando solo hay una alternativa plausible. Cuatro alternativas de E3 se retiran del diseño porque no tienen respaldo en el corpus. Son la inferencia en el chip del sensor y el silencio del 90 % de los nodos. También se retiran los modelos de cizalladura del viento y la provisión de mascarillas.

El registro de decisión de la {T:t04} cierra el nodo ND-06.

:::TABLA t04 | Registro de decisión GENESIS: ND-06 Desmantelamiento de ortodoxias
| Campo | Contenido |
| --- | --- |
| NODO | ND-06 Desmantelamiento de ortodoxias |
| CLASE | MAYOR. Determina qué supuestos de diseño sobreviven a la formulación. |
| DECISION | Eliminar 5 supuestos con evidencia en contra, cuestionar 9 y mantener 1; retirar del diseño las cuatro alternativas de E3 sin respaldo en el corpus. |
| DECIDE | Equipo formulador [DATO_USUARIO: responsable de la decisión]. La propuesta proviene de la instancia analítica. |
| EXCLUYE | Eliminar un supuesto por preferencia de diseño. Adoptar la inferencia en el chip del sensor, el silencio del 90 % de los nodos o los modelos de cizalladura del viento. |
| NODOS_BLANCOS | 3: corrección con humedad documentada (Jayaratne et al., 2018; Barkjohn et al., 2021); redes sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13); estaciones inactivas (Tavella et al., 2026, p. 6). |
| NODOS_GRISES | 4: latencia de red, línea base de error en escombros, tasa de falsas alarmas y adopción institucional. Ninguno tiene medición. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | PR-06 (patrón emergente): decidir por la existencia de una fuente que contradiga el supuesto. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. La alternativa de convenios por tramo supone capacidad institucional no verificada. |
| ESCENA_SIMULABLE | El equipo revisa en el mes 4 cada supuesto «cuestionado» con los datos del piloto y registra si se confirma o se retira. |
| EVIDENCIA_JH_A | Tres citas del corpus con página (tabla F4.3). |
| EVIDENCIA_JH_B | Ausencia de fuente para cuatro alternativas de E3: ninguna aparece en el informe de vigilancia. |
| CERCA_CONCEPTUAL | Eliminar un supuesto no prueba que la alternativa funcione. Solo el piloto del tramo 1 lo demuestra. |
| ESTATUTO_CAUSAL | HIE. Ninguna afirmación causal. |
| VEREDICTO | Decisión adoptada con reserva: los supuestos cuestionados se evalúan en el tramo 1. |
| RAZON_DEL_DESCARTE | Se descarta la eliminación en bloque de E3 porque cuatro alternativas carecen de respaldo. |
| RESULTADO | CIERRA con vacíos declarados (latencia, línea base, falsas alarmas, adopción). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS. Las referencias de las celdas corresponden a la lista del capítulo 19.


## F4.3 Clasificación de variables para inferencia causal

Esta sección declara el estimando antes de clasificar variables. Deriva los roles del grafo y no de la clase de Vester. La clasificación estructural de 4.4 aporta hipótesis de influencia (HIE). No sustituye la identificación causal (Pearl y Mackenzie, 2018). Todos los juicios son propuestas de la instancia analítica y carecen de ratificación.

### F4.3.1 Estimando antes del ajuste causal

El expediente E3 omitió esta sección. Los registros de decisión del documento asignan estatutos IDC y EST sin declarar estimando. Esta sección declara dos estimandos y evalúa si cada uno puede publicarse como efecto causal. Si algún campo es VACIO, no se publica un efecto causal.


La {T:i001} reúne los datos de «Estimando del efecto del método de corrección».

:::TABLA i001 | Estimando del efecto del método de corrección
| Campo | E1. Efecto técnico del método de corrección | E2. Efecto institucional de la adopción |
| --- | --- | --- |
| Intervención X | Nivel del método de corrección de los nodos: N1 corrección lineal fija; N2 referencia cercana con humedad; N3 N2 más alineación temporal; N4 N3 más ponderación por confianza o autocalibración por ventana estable (variante en el borde, ALT-03). Intensidad en el modelo: V07. | Adopción formal del tablero por la alcaldía (V15) mediante acto administrativo. |
| Resultado Y | V06: logaritmo del NMAE del PM2,5 de cada nodo frente a la referencia asignada, por semana. | V14: personas bajo protección efectiva. |
| Población | Nodos fijos del piloto (100 más 20 % de repuestos) en sitios de remoción de escombros. | Municipios con sitios de remoción. |
| Territorio | Caldas, Cundinamarca y Valle del Cauca (SUPUESTO). | Mismo (SUPUESTO). |
| Horizonte | Diseño alternado de 52 semanas dentro de los 24 meses de ejecución; el Hito 2 (mes 12) usa las primeras 30 jornadas de contraste. | 36 meses (24 de ejecución y 12 posproyecto). |
| Contraste causal | N4 frente a N1 (paquete de corrección en el borde frente a la lectura sin corrección dinámica). Contrastes secundarios: N4 frente a N2 y N4 en el borde frente a N4 en la nube. | VACIO: no existe grupo comparable ni regla de asignación. |
| Estimando | Efecto promedio en los tratados (ATT) sobre el logaritmo del NMAE, bajo sorteo semanal de nivel por nodo. | VACIO. |
| Unidad de análisis | Nodo-semana. | Municipio-mes (propuesta). |
| Resultado de la evaluación | Estimando completo. Identificable por diseño si se ejecuta el sorteo (IDC prospectivo). Sin datos: no se publica ningún efecto. | NO IDENTIFICADO CON LOS INSUMOS DISPONIBLES. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.


**Origen del diseño.** El informe_FINAL (sección 11.4 a 11.8) propone un diseño alternado con asignación aleatoria semanal, panel con efectos fijos por nodo y semana y 52 semanas. La propuesta nace en SIATA (Valle de Aburrá). Aquí se adapta a nodos de remoción de escombros. Las cuatro hipótesis del informe (H1 a H4) siguen sin evidencia propia.

**Estimando E3 (fuera de alcance).** El efecto del sistema de alerta sobre morbilidad respiratoria no tiene variable de resultado ni línea base en el modelo (VACIO-05 de E3-P20). No se declara estimando. Cualquier afirmación sobre morbilidad permanece como hipótesis.

### F4.3.2 Roles del DAG y regla de ajuste


La {T:i002} reúne los datos de «Roles del DAG y regla de ajuste».

:::TABLA i002 | Roles del DAG y regla de ajuste
| Rol | Definición operacional | Regla para el efecto total de X sobre Y |
| --- | --- | --- |
| CONFUSOR_PRE | Causa pretratamiento de X y de Y, o nodo que bloquea un camino trasero. | Candidato al conjunto de ajuste. |
| PREDICTOR_Y | Predice Y sin abrir caminos espurios. | Mejora precisión; no se incluye solo por correlación. |
| MEDIADOR | Está en el camino causal de X a Y. | No ajustar para el efecto total. |
| COLLIDER | Efecto común de dos nodos relevantes. | No condicionar sin justificación. |
| DESCENDIENTE_X | Variable causada por X. | No usar como control pretratamiento. |
| INSTRUMENTO | Afecta X y cumple relevancia, exclusión e independencia declaradas. | Solo bajo estrategia instrumental explícita. |
| LATENTE | Nodo no observado relevante. | Registrar amenaza de identificación; no fingir control. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.


La frase «correlacionada con X» no es un rol causal. El conjunto de ajuste se deriva del grafo y del estimando. Se retira la taxonomía universal A/B/C/E y el umbral del 50 % de caída del coeficiente como prueba de mediación.

### F4.3.3 Tabla de clasificación DAG para el estimando E1

La {T:i003} usa X = método de corrección (V07) y Y = V06. El estatuto de cada fila es HIE: ningún rol se estima con datos. La naturaleza de cada fila es INFERIDO y su verificación NO_VERIFICADO. Las relaciones provienen de las fichas de S2 (F4.4.4).


:::TABLA i003 | Tabla de clasificación DAG para el estimando E1
| Variable | Temporalidad respecto a X | Rol DAG | Caminos relevantes | ¿Ajustar? | Evidencia | Estatuto |
| --- | --- | --- | --- | --- | --- | --- |
| V01 PM2,5 | Simultánea; independiente de X | PREDICTOR_Y | V01→V06 (2); V05→V01→V06 | Sí, por precisión. No es necesario para identificar bajo sorteo. | Ficha V01→V06, confianza BAJA | HIE |
| V02 PM10 | Simultánea; independiente de X | PREDICTOR_Y | V02→V06 (3); V02→V09 (1); V05→V02 | Sí, por precisión. Evitar incluir V01 y V02 si son colineales por inclusión. | Ficha V02→V06, confianza MEDIA | HIE |
| V03 humedad | Simultánea; independiente de X | PREDICTOR_Y y moderador | V03→V06 (3); V03→V09 (1) | Sí, con interacción X por V03. | F-INF §3.1 (Suresh et al., 2025, p. 30), cita secundaria | HIE |
| V04 viento | Simultánea; independiente de X | PREDICTOR_Y débil | V04→V06 (1); V04→V01 y V04→V02 | Sí, como control. | Control del NMAE en F-INF §11.4 | HIE |
| V05 escombros | Pretratamiento de cada semana | PREDICTOR_Y indirecto; causa de atrición | V05→V01 y V05→V02→V06; V05→V09 | Depende: absorber con efectos fijos de nodo y semana. No condicionar sobre V09. | Fichas V05→V09 (MEDIA) y V05→V02 (ALTA) | HIE |
| V06 error de medición | Posterior a X | Resultado Y | X→V06 (3) | No aplica | Ficha V07→V06; F-INF §3.1 (Bang et al., 2026, pp. 6-8) | HIE |
| V07 calibración | Asignada al inicio de la semana | Exposición X (intensidad) | V07→V06; V07→V08; V07→V09 | No aplica | Sorteo semanal propuesto en F-INF §11.7 | IDC prospectivo |
| V08 latencia | Posterior a X | DESCENDIENTE_X; MEDIADOR si V08→V06 fuera positivo | V07→V08 (1) | No. Bajo la ficha V08→V06 = 0 no hay camino a Y. | Fichas V07→V08 y V08→V06 (dominio {0,1,2}) | HIE |
| V09 disponibilidad | Posterior a X | DESCENDIENTE_X y COLLIDER (V05→V09←X) para la muestra observada | V07→V09 (1); V05→V09 (2); V02→V09 (1) | No condicionar a nodos activos. Usar intención de tratar con ponderación. | Fichas V07→V09, V05→V09, V02→V09 | HIE |
| V10 densidad | Nominal: previa. Efectiva: posterior (depende de V09) | PREDICTOR_Y débil (nominal); DESCENDIENTE_X (efectiva) | V10→V06 (1); V09→V10 (3) | Depende: usar solo la densidad nominal de diseño. | Ficha V10→V06; VACIO V-DIC-02 | HIE |
| V11 AQHI | Posterior a Y | DESCENDIENTE de Y | V06→V11 (3) | No | Ficha V06→V11 | HIE |
| V12 falsas alarmas | Posterior a Y | DESCENDIENTE de Y | V06→V12 (2); V11→V12 (2) | No | Fichas V06→V12 y V11→V12 | HIE |
| V13 anticipación | Posterior a Y | DESCENDIENTE de Y (vía V10 y V08) | V08→V13; V10→V13 | No | Fichas V08→V13 y V10→V13 | HIE |
| V14 personas alertadas | Posterior a Y | DESCENDIENTE de Y | V11→V14; V13→V14; V12→V14 | No | Fichas de entrada de V14 | HIE |
| V15 adopción | Posterior; retroalimenta a X | DESCENDIENTE de Y; causa de X futuro si X no es aleatorizado | V06→V15; V12→V15; V15→V07 | No. Riesgo de confusión dependiente del tiempo sin sorteo. | Fichas V12→V15, V15→V07 | HIE |
| L1 distancia a la referencia | Previa | LATENTE (medible) | L1→V06 (H2 del informe) | Sí si hay medición y no hay sorteo | F-INF §11.4 y §11.6 | HIE |
| L2 edad del sensor | Previa | LATENTE (medible); moderador | L2→V06 (H4 del informe) | Sí si no hay sorteo | F-INF §11.4 y §11.6 | HIE |
| L3 episodio de humo | Simultánea | LATENTE; moderador | L3→V06 (H3 del informe) | Sí como interacción | F-INF §11.4 y §11.6 | HIE |
| L4 precipitación | Simultánea | LATENTE; no modelada | L4→V03, L4→V02, L4→V05 | Declarar como amenaza | VACIO V-LLUVIA-01 | HIE |
| U sorteo semanal | Previa | INSTRUMENTO y regla de asignación | U→X | No aplica | F-INF §11.7 | IDC prospectivo |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.


### F4.3.4 Identificación y DAGs rivales

El DAG principal se dibujó antes de cualquier estimación. La {F:dag} y su alternativa textual constan en DAG_E1.svg y DAG_E1.alt.md.

:::FIGURA dag | DAG principal del estimando E1 | Nota. Elaboración propia con la estructura de la sección F4.3. X: método de corrección (V07). Y: error de medición (V06). U: sorteo semanal. Los nodos latentes se dibujan con trazo discontinuo. Estatuto de todas las relaciones: HIE.

**Conjunto de ajuste mínimo bajo el DAG principal.** Con sorteo semanal por nodo, el conjunto de ajuste mínimo es vacío: X es independiente de las causas de Y por diseño. Para precisión se propone {V03 con interacción, V01 o V02, V04} más efectos fijos de nodo y de semana. No se incluyen V08, V09, V11, V12, V13, V14 ni V15.

**DAGs rivales y conjuntos de ajuste.**


La {T:i004} reúne los datos de «DAGs rivales y conjuntos de ajuste».

:::TABLA i004 | DAGs rivales y conjuntos de ajuste
| DAG rival | Hipótesis | Amenaza | Conjunto de ajuste | Resultado de identificación |
| --- | --- | --- | --- | --- |
| R1 | La distancia a la referencia explica más del error que el método y se asigna por conveniencia a sitios cercanos. | Confusión por selección de sitios (L1). | Con sorteo: ninguno. Sin sorteo: L1 medida. | Identificado con sorteo. Sin sorteo, NO IDENTIFICADO CON LOS INSUMOS DISPONIBLES. |
| R2 | La edad del sensor determina la deriva y los nodos viejos reciben más recalibración. | Confusión por L2. | Con sorteo: ninguno. Sin sorteo: L2 medida. | Igual que R1. |
| R3 | La pérdida de nodos por maquinaria (V05→V09) y el efecto de X sobre la energía (X→V09) abren un camino por V09. | Colisionador: condicionar a nodos activos sesga el efecto. | No condicionar sobre V09; intención de tratar y ponderación inversa por disponibilidad. | Identificado bajo intención de tratar. Efecto sobre nodos activos NO IDENTIFICADO. |
| R4 | La adopción institucional (V15) modifica el uso de X en el tiempo. | Retroalimentación: rompe la aciclicidad y la exogeneidad de X. | Sorteo como regla de asignación o instrumento con F de primera etapa mayor que 10. | Identificado solo con sorteo cumplido o instrumento válido. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.


**Declaración de identificación.** Con los insumos actuales no existe ningún dato del piloto, ni sorteo ejecutado, ni referencia para todos los nodos. El efecto de E1 queda NO IDENTIFICADO CON LOS INSUMOS DISPONIBLES para cualquier estimación observacional. Es identificable por diseño si se ejecutan el sorteo y los supuestos de F4.3.6. El estimando E2 no es identificable en este diseño.

### F4.3.5 Estatutos de afirmación causal


La {T:i005} reúne los datos de «Estatutos de afirmación causal».

:::TABLA i005 | Estatutos de afirmación causal
| Código | Estatuto | Lenguaje permitido |
| --- | --- | --- |
| HIE | Hipótesis de influencia estructural | «podría influir», «se prioriza como hipótesis» |
| IDC | Estimando causal identificado bajo supuestos | «efecto identificable si se cumplen…» |
| EST | Efecto estimado con datos y diseño | «se estimó…», con intervalo y sensibilidad |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.


Está prohibido pasar de HIE a IDC o a EST porque una variable resulte activa o crítica en Vester o ascienda en MICMAC. Las 210 puntuaciones de 4.4 y las clases de F4.4.8 son HIE. El estimando E1 es IDC prospectivo, condicionado al sorteo. Ninguna afirmación del proyecto es EST.

**Auditoría de los estatutos del documento previo.** El documento declara estatutos causales en sus registros RDG sin estimando ni datos.


La {T:i006} reúne los datos de «Auditoría de los estatutos del documento previo».

:::TABLA i006 | Auditoría de los estatutos del documento previo
| Nodo | Estatuto declarado | Estatuto sostenible hoy | Motivo |
| --- | --- | --- | --- |
| ND-05 Brechas instanciadas | IDC | NO_APLICA (descriptivo) | Es un hallazgo bibliométrico; no declara estimando. |
| ND-06 Ortodoxias | HIE | HIE | Coincide. |
| ND-10 Causa raíz adoptada | IDC | HIE | No existe estimando ni identificación; la causa raíz es una hipótesis estructural. |
| ND-11 Enunciado tripartito | IDC | HIE | La ecuación Y = f(X1, X2, X3 \| M, C) no está identificada; X2 y X3 no actúan sobre V06 en el ledger E3. |
| ND-12 Autenticidad contrainductiva | HIE | HIE | Coincide. |
| ND-13 Pesos y puntajes MCDA | IDC | NO_APLICA | Es una evaluación multicriterio con pesos supuestos; no estima efectos. |
| ND-14 Metaheurística | EST | NO_APLICA | El código es una función de aptitud sin ejecución trazable; no estima un efecto con datos. |
| ND-15 Alternativa seleccionada | EST | HIE | La alternativa se selecciona por puntaje; no hay efecto estimado. |
| ND-16 Output, outcome e impact | IDC | HIE | La cadena hasta morbilidad no tiene resultado identificado (E3 en F4.3.1). |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.


### F4.3.6 Pruebas de robustez


La {T:i007} reúne los datos de «Pruebas de robustez».

:::TABLA i007 | Pruebas de robustez
| Prueba | Aplicación al diseño E1 | Estado |
| --- | --- | --- |
| Precedencia temporal | El nivel se asigna el lunes antes de la medición semanal. V01 a V04 se miden en la misma semana y no son causadas por X. | Diseño propuesto; NO_EJECUTADO |
| Positividad y solapamiento | Con 4 niveles y 52 semanas, cada nodo recibe cada nivel unas 13 veces en promedio. La positividad se cumple por diseño si el sorteo es estricto. | Diseño propuesto; NO_EJECUTADO |
| Medición | El denominador depende de una referencia. El presupuesto prevé 3 monitores gravimétricos (Capítulo 8, Tabla E3-8.3) para 100 nodos en tres departamentos. | VACIO: cobertura de referencias |
| Selección | Se espera pérdida de nodos por maquinaria (V05→V09). Se analiza por intención de tratar con ponderación por disponibilidad y se informa la atrición por nivel. | Diseño propuesto; NO_EJECUTADO |
| Datos faltantes | No se imputa Y. Se ponderan las observaciones y se informan cotas por escenarios de pérdida. | Diseño propuesto; NO_EJECUTADO |
| Confusión no observada | El sorteo la neutraliza si se cumple. Sin sorteo, se requiere análisis de sensibilidad a confusión no medida [conocimiento externo]. | No aplicable aún |
| Sensibilidad compatible con el diseño | Balance de covariables por nivel, prueba de arrastre con una semana de lavado, pruebas placebo con fechas falsas y modelos alternos M2 y M3 del informe_FINAL. | Diseño propuesto; NO_EJECUTADO |
| Potencia (recalculada) | Con desviación 0,25, efecto de diseño 3, 5.200 nodo-semanas y proporción 0,5, el error estándar es 0.0120 y la diferencia mínima detectable con 80 % de potencia es 0.0336 puntos de NMAE, cerca de 11.2 % de una línea base de 0,30. Premisas del informe_FINAL §11.8. | CALCULADO sobre premisas NO_VERIFICADAS |
| Predicción frente a causalidad | El modelo TinyML puede usar V03 y V01 como predictores de corrección. Que mejoren el ajuste no los convierte en causas de V06 ni valida el efecto del método. | Regla de interpretación |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.


**Factibilidad del sorteo.** El sorteo semanal exige control remoto del nivel de corrección en cada nodo. El expediente no describe actualización remota ni registro de asignación. La factibilidad es un VACIO que condiciona el estatuto IDC del estimando E1.

**Registro de decisión ND-07 (estimando, roles y conjunto de ajuste).**




La {T:i008} reúne los datos de «Registro de decisión GENESIS: ND-07 Estimando, roles y conjunto de ajuste».

:::TABLA i008 | Registro de decisión GENESIS: ND-07 Estimando, roles y conjunto de ajuste
| Campo | Contenido |
| --- | --- |
| NODO | ND-07 Estimando, roles y conjunto de ajuste |
| CLASE | MAYOR. Determina qué afirmaciones causales pueden publicarse. |
| DECISION | Declarar el estimando del efecto del método de corrección sobre el error de medición y adoptar el conjunto de ajuste mínimo que deriva del DAG. |
| DECIDE | Equipo formulador (rol POR_IDENTIFICAR). La propuesta proviene de la instancia analítica. |
| EXCLUYE | Publicar un efecto causal con datos observacionales. Ajustar por V08, V09, V11 a V15. Usar la clase de Vester como rol causal. |
| NODOS_BLANCOS | 6: diseño alternado con sorteo semanal (F-INF §11.7, T08); 5.200 nodo-semanas (F-INF §11.8, T09); diferencia mínima detectable 0,034 recalculada (T09); V03→V06 = 3 y V07→V06 = 3 (fichas de S2, T09); V05→V09 = 2 (ficha, T09); corrección por estación cercana con R2 de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8, T08). |
| NODOS_GRISES | 2: el sorteo semanal es operable en terreno; hay referencia gravimétrica para los nodos del sorteo (solo 3 monitores presupuestados). |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 1 (el estimando no alcanza V14; la cadena hasta personas protegidas permanece HIE y se declara). |
| PATRON_DOMINANTE | PR-06 (patrón emergente): exogeneidad condicionada al sorteo. La retroalimentación V15→V07 aparece en S2 (ciclos de F4.4.13) y justifica el patrón. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. El sorteo y las referencias exigen capacidad técnica y conectividad no verificadas en el territorio. |
| ESCENA_SIMULABLE | El ingeniero de campo de la IES registra cada lunes el nivel sorteado por nodo antes de ver los datos. El científico de datos compara en el mes 12 el NMAE del nivel 4 con el del nivel 1. |
| EVIDENCIA_JH_A | Acta semanal de asignación con listado de nodos por municipio (artefacto por producir; no existe aún). |
| EVIDENCIA_JH_B | Ecuación M1 del informe_FINAL §11.7, potencia recalculada y 3 monitores de referencia presupuestados (Tabla E3-8.3). |
| CERCA_CONCEPTUAL | El estimando no prueba que el sistema proteja personas. Mide el efecto del método de corrección sobre el error del sensor. |
| ESTATUTO_CAUSAL | IDC prospectivo para E1, condicionado al sorteo cumplido. HIE para toda otra relación. Ninguna EST. |
| VEREDICTO | Estimando E1 declarado. Conjunto de ajuste mínimo vacío bajo sorteo. E2 no identificado. |
| RAZON_DEL_DESCARTE | Se descarta estimar el efecto con comparaciones entre sitios sin sorteo, por confusión con la distancia a la referencia y la edad del sensor. |
| RESULTADO | CIERRA con vacíos declarados (factibilidad del sorteo; cobertura de referencias). |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.3.




## F4.4 Vester y MICMAC: protocolo paritario integrado

Sección generada con GENESIS-CTeI 36.10 RC2 / VM-PAR3-MDR3-CONT1. Contiene las catorce piezas MP-06, numeradas F4.4.1 a F4.4.14. Las piezas son subsecciones y no autorizan otras secciones. Los valores son propuestas no ratificadas. El análisis estructural expresa hipótesis de influencia (HIE), no efectos causales.

### F4.4.1 Procedencia, estado y alcance de los objetos

Esta pieza identifica los objetos que entran al análisis, su naturaleza y su estado de verificación. Separa el cálculo de la ratificación, como exige el canon paritario VM-PAR3.

**Identidad de la corrida.** Caso SGR_CONV56_AIRE. Implementación GENESIS-CTeI 36.10 RC2, revisión VM-PAR3-MDR3-CONT1. Fecha de corrida: 13 de octubre de 2026. Semilla del plan: 20261011. Corte principal: mediana. KMAX: 10. Ventana de estabilidad: 3.


La {T:i009} reúne los datos de «Identidad de la corrida».

:::TABLA i009 | Identidad de la corrida
| Objeto | Procedencia y localizador | Contenido | Naturaleza | Verificación y alcance | Estado |
| --- | --- | --- | --- | --- | --- |
| E3_ORIGINAL | Problematica_E3-P00.docx, E3-P04 §12 | 22 aristas positivas (ΣI = 53) y 188 ceros por «Regla Cero» | DECLARADO | PARCIALMENTE_VERIFICADO: aritmética recalculada (ΣI = ΣD = 53); contenido semántico NO_VERIFICADO | Conservado sin cambios |
| MID_FORMAL | Derivada de E3_ORIGINAL | 22 valores positivos como DECLARADO; 188 celdas U | DECLARADO y VACIO | NO_VERIFICADO. El cero por bloque no cumple la adjudicación individual que exige el contrato E3→E4 V2.1 | Matriz formal preservada; no se eleva |
| S0 | Mismo origen | Escenario histórico condicionado: 22 aristas, 188 ceros heredados | DECLARADO | VERIFICADO (aritmético) | Escenario independiente |
| S1 | Problematica_E3-P00.docx, Paso 4, F4.4.5 | 32 aristas, ΣI = 67 | PROPUESTO | VERIFICADO (aritmético). La narrativa asociada resulta CONTRADICTORIA con el cálculo (F4.4.11 y F4.4.12) | Escenario independiente |
| S2 (MID_TRABAJO) | Esta corrida, 105 fichas paritarias | 48 aristas, ΣI = 78 | PROPUESTO | Esquema VERIFICADO; contenido semántico NO_VERIFICADO | Escenario de trabajo; no ratificado |
| S3 y S4 | Esta corrida, dominios admisibles de las fichas | Valor mínimo y máximo admisible por dirección | CALCULADO | VERIFICADO (aritmético) | Envolventes de sensibilidad, no predictivas |
| Plantilla XLSX | Vester_MICMAC_Plantilla_15_vacia.xlsx | Nombres de las 15 variables y matriz idéntica a S1 (no está vacía) | DECLARADO | Coincidencia exacta con S1 VERIFICADA celda a celda | Usada como segunda implementación de cálculo |
| informe_FINAL | informe_FINAL.docx (42 documentos, consolidado al 30-09-2026) | Vigilancia tecnológica y bibliometría | DOCUMENTADO | PARCIAL: secciones 1, 2, 3.1, 4.1, 8.4, 11 y anexos; artículos originales NO leídos | Fuente secundaria |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Separación de dimensiones.** La autorrevisión no emite un veredicto global único. Cada dimensión tiene su estado.


La {T:i010} reúne los datos de «Separación de dimensiones».

:::TABLA i010 | Separación de dimensiones
| Dimensión | Estado | Evidencia y límite |
| --- | --- | --- |
| CÁLCULO | EJECUTADO | Motor genesis_paritario_vm.py con SHA-256 comprobado. Cinco escenarios. La plantilla XLSX, recalculada con LibreOffice, reproduce A¹ a A⁶ en S0, S1 y S2. Cinco permutaciones de filas y columnas dan resultados idénticos tras restaurar los IDs. |
| COMPLETITUD DE FICHAS | 105 de 105 fichas válidas por esquema | 210 direcciones únicas; 0 errores de esquema. El esquema no prueba mecanismo, intensidad ni fuentes. |
| RESPALDO DOCUMENTAL | PARCIAL | De 48 direcciones no nulas, 22 citan el informe_FINAL, 19 citan solo el expediente E3 y 7 se apoyan en premisas. Ninguna fuente primaria fue leída. Las 162 direcciones nulas se apoyan en premisas de frontera y mediación. |
| RATIFICACIÓN | PENDIENTE | Cero adjudicaciones documentadas. Todo valor es PROPUESTO por la instancia analítica de esta corrida, sin panel humano. |
| ALCANCE | 4.4 dentro de la cadena 4.3, 4.4, F4.4-MDR y 4.5 | La corrida no incluye los pasos 5 y 6 ni los 21 capítulos ni el paquete 1000X. |
| ARTEFACTOS | Ver F4.4.14 | XLSX oficial (artifact_tool): XLSX_PENDIENTE_POR_DEPENDENCIA. Se entregan CSV, JSON, SVG y tres libros derivados de la plantilla del usuario. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Conteos separados de fichas (H02).** Ningún contador mecánico equivale a verificación semántica.


La {T:i011} reúne los datos de «Conteos separados de fichas (H02)».

:::TABLA i011 | Conteos separados de fichas (H02)
| Contador | Valor |
| --- | --- |
| Fichas recibidas | 105 |
| Fichas bidireccionales válidas | 105 |
| Fichas con justificación declarada | 105 |
| Fichas con dos valores propuestos | 105 |
| Fichas con adjudicación documentada | 0 |
| Direcciones recibidas únicas | 210 |
| Direcciones con justificación declarada | 210 |
| Direcciones con valor propuesto | 210 |
| Direcciones con adjudicación documentada | 0 |
| Fichas verificadas semánticamente | no medido |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Naturaleza de las 48 direcciones no nulas.** INFERIDO: 27; PROPUESTO: 11; SUPUESTO: 8; DOCUMENTADO: 2. Las dos direcciones DOCUMENTADO (V03→V06 y V04→V01) se apoyan en citas secundarias del informe_FINAL.

**Reservas vigentes.**

- R-01. El territorio (Caldas, Cundinamarca, Valle del Cauca) y la alianza son SUPUESTO por instrucción del usuario. No existen términos de referencia en el expediente (F_TDR_MINCIENCIAS no aportado).

- R-02. Los valores heredados de E3 conservan su estado DECLARADO. El rótulo DOCUMENTADO de E3-P04 para V03→V01 y V03→V02 carece de localizador y no se acepta.

- R-03. VACIO V-DIC-01: el diccionario no precisa si V01 y V02 son concentración real o medida. VACIO V-DIC-02: V10 puede ser densidad nominal o efectiva. VACIO V-DIC-03: V06 puede referirse al sensor o al producto de red.

- R-04. VACIO V-AQHI-01: la fórmula local del índice V11 no figura en el expediente.

- R-05. VACIO V-LLUVIA-01 y V-VIENTO-01: no hay variable de precipitación ni umbral operativo de viento.

- R-06. La iteración previa atribuyó a la patente Ali et al. (2022) un respaldo empírico que el informe_FINAL niega; esa cita no respalda mecanismo alguno.

### F4.4.2 Diccionario revisado y tabla de escala con anclas y límites

El diccionario conserva los 15 identificadores y las definiciones operacionales de E3-P01. No se agregan ni se retiran variables. La revisión añade el sentido de aumento y las observaciones de ambigüedad.

**Frontera y horizonte.** Frontera: red IoT de material particulado en sitios de remoción de escombros, con territorio y alianza como SUPUESTO. Horizonte H: 24 meses de ejecución más 12 meses posproyecto (36 meses). El horizonte es una propuesta de esta corrida; E3 no lo fija.


La {T:i012} reúne los datos de «Frontera y horizonte».

:::TABLA i012 | Frontera y horizonte
| ID | Variable | Definición operacional (unidad) | Bloque | Sentido de aumento | Observación de revisión |
| --- | --- | --- | --- | --- | --- |
| V01 | Concentración PM2.5 | Masa de partículas <2,5 µm (µg/m³). | FIS | mayor concentración | Incluida en V02 por tamaño de partícula. |
| V02 | Concentración PM10 | Masa de partículas <10 µm (µg/m³). | FIS | mayor concentración | Incluye la masa de V01; se propone redefinirla como fracción gruesa (PM10 menos PM2,5) en una versión posterior. |
| V03 | Humedad relativa | Saturación de vapor de agua (%). | FIS | mayor humedad | Exógena; sin variable de precipitación en el modelo. |
| V04 | Velocidad del viento | Fuerza de dispersión eólica superficial (m/s). | FIS | mayor velocidad | Exógena; la dirección del viento no figura en el modelo. |
| V05 | Volumen de escombros | Residuos removidos tras el sismo (t/día). | FIS | mayor volumen removido | Variable de actividad; modificable por decisión institucional. |
| V06 | Error de medición IoT | Desfase metrológico del sensor láser (NMAE %). | TEC | mayor error | Se define para el sensor individual; el error del producto de red es otro objeto. |
| V07 | Frecuencia de calibración | Tasa de ajuste algorítmico del gemelo (ajustes/semana). | TEC | más ajustes por semana | Variable de operación; palanca de diseño. |
| V08 | Latencia de datos | Retraso en la transmisión a la nube central (minutos). | TEC | mayor retraso | No distingue retraso de red y desfase temporal sensor-estación. |
| V09 | Disponibilidad de nodos IoT | Porcentaje de la red de sensores activa y con energía (%). | TEC | más nodos activos con energía | Condiciona la lectura efectiva de V10. |
| V10 | Densidad del gemelo | Resolución del mapa predictivo espacial (nodos/km²). | TEC | mayor densidad efectiva o nominal (ambigua) | Ambigua entre densidad nominal de diseño y resolución efectiva. |
| V11 | Índice AQHI | Nivel de peligro de salud pública emitido (escala 1-10). | DEC | mayor peligro | Fórmula local no disponible en el expediente. |
| V12 | Falsas alarmas | Tasa de alertas emitidas sin superación de umbral real (%). | DEC | más alertas sin superación real | Depende del umbral del índice y del error de medición. |
| V13 | Anticipación | Tiempo de aviso preventivo antes del impacto (horas). | DEC | más horas de aviso | Sin línea base en el corpus. |
| V14 | Personas alertadas | Población y operarios bajo protección efectiva (conteo). | DEC | más personas protegidas | Mide protección efectiva; la definición no separa protección autónoma de la inducida por alerta. |
| V15 | Adopción institucional | Uso efectivo del tablero por alcaldías y UNGRD (%). | DEC | mayor uso efectivo | Variable de resultado institucional y de sostenibilidad. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Revisión de solapamiento.** Se examinaron los 105 pares posibles. Resultado: UNICA 101; SOLAPAMIENTO_DEFINICIONAL 1; AMBIGUEDAD_CONDICIONAL 2; DEPENDENCIA_FUNCIONAL 1. El archivo REVISION_SOLAPAMIENTO.csv registra los 105 veredictos. E3-P02 solo documentó 5 pares y declaró ÚNICA los otros 100 en bloque; esa revisión no examinó la inclusión de V01 en V02.

**Escala operacional 0 a 3.** La escala es ordinal. No expresa proporciones, probabilidades ni magnitudes métricas. Las anclas se fijan antes de puntuar las 210 direcciones.


La {T:i013} reúne los datos de «Escala operacional 0 a 3».

:::TABLA i013 | Escala operacional 0 a 3
| Valor | Definición operacional | Ancla del caso |
| --- | --- | --- |
| 0 | Ausencia de influencia directa dentro del modelo, por frontera, definición, mediación explícita o mecanismo ausente. No equivale a U. | V11->V04: el índice emitido en pantalla no altera el viento (ausencia por imposibilidad física). |
| 1 | Influencia directa débil: efecto gradual, parcial o mitigable por diseño dentro de H. | V03->V09: la humedad corroe y condensa; reduce la vida útil de los nodos a mediano plazo y la carcasa NEMA 4X lo mitiga (influencia débil). |
| 2 | Influencia directa moderada: altera el funcionamiento estándar y exige acción correctiva, sin determinarlo. | V08->V13: la latencia resta una fracción del tiempo útil de aviso; la relación es aritmética pero parcial (minutos frente a horas) (influencia moderada). |
| 3 | Influencia directa fuerte: determina la variable destino casi de forma mecánica, sin agente intermedio y sin explicar por qué 2 no representa la hipótesis. | V05->V02 y V06->V11: la remoción mecánica genera PM10 y el error del sensor entra al cálculo del índice sin acción humana intermedia (influencia fuerte). |
| null (U) | No existe fundamento para preferir un valor. Se conserva en la matriz formal y se documenta el conjunto plausible. | Celdas U de MID_FORMAL: 188 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Límites de la escala.** La confianza es otro eje y no multiplica la puntuación. Una fuente respalda el mecanismo que contiene, no un valor ordinal exacto. El documento previo usa V09→V10 como ancla del valor 2. Su propio ledger le asigna 3. Aquí se fijan anclas únicas.

### F4.4.3 Plan paritario completo, semilla y orden de ejecución

El plan contiene 105 pares no ordenados y 210 direcciones para n = 15. Semilla registrada: 20261011. Los bloques declarados son FIS (V01 a V05), TEC (V06 a V10) y DEC (V11 a V15). Hay 30 pares intrabloque y 75 pares interbloque.

El motor ordena al azar cada clase con la semilla y alterna un par interbloque con un par intrabloque mientras existan ambas clases. El plan se registró antes de valorar. La paridad es de atención analítica: ambos sentidos reciben su propia ficha, sin imponer simetría de valores.

**Primeros 15 pares del orden de ejecución.** El orden completo de los 105 pares consta en PLAN_PARITARIO.csv.


La {T:i014} reúne los datos de «Primeros 15 pares del orden de ejecución».

:::TABLA i014 | Primeros 15 pares del orden de ejecución
| Orden | Par | Clase |
| --- | --- | --- |
| 1 | V04__V08 | INTER |
| 2 | V07__V09 | INTRA |
| 3 | V06__V14 | INTER |
| 4 | V06__V08 | INTRA |
| 5 | V05__V10 | INTER |
| 6 | V14__V15 | INTRA |
| 7 | V03__V11 | INTER |
| 8 | V06__V07 | INTRA |
| 9 | V04__V14 | INTER |
| 10 | V03__V05 | INTRA |
| 11 | V03__V14 | INTER |
| 12 | V01__V03 | INTRA |
| 13 | V05__V11 | INTER |
| 14 | V12__V13 | INTRA |
| 15 | V09__V11 | INTER |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


Los lotes organizan el trabajo; no atribuyen independencia estadística entre fichas. La instancia analítica valoró las 105 fichas en esta corrida sin solicitar un comando por par.

### F4.4.4 Fichas bidireccionales con mecanismos, fundamentos y estados

Esta pieza contiene las 105 fichas paritarias en el orden del plan. Cada ficha valora los dos sentidos del par por separado. Ninguna ficha es una plantilla: cada dirección declara su mecanismo o la razón del cero, su fundamento, su justificación y la explicación rival.

**Campos uniformes en las 210 direcciones.** Horizonte: H = 24 meses de ejecución más 12 meses posproyecto (36 meses). Horizonte PROPUESTO por la corrida; el diccionario E3 no lo fija. Recorrido directo sin pasar por otra variable explícita del modelo. Frontera: Red IoT de material particulado en sitios de remoción de escombros. El territorio y la alianza son SUPUESTO por instrucción del usuario. El modelo incluye solo las variables V01 a V15. Quedan fuera la distancia a la referencia, la edad del sensor y el episodio de humo. Procedencia: Instancia analítica de GENESIS en esta corrida. Sin panel humano, sin adjudicación ni acta. Juicio PROPUESTO, sujeto a ratificación. Estado de todas las direcciones: PROPUESTO. El archivo FICHAS_PARITARIAS.json repite esos campos en cada dirección, como exige el esquema.

**Lectura de los rótulos.** «Valor» es la puntuación propuesta en la escala 0 a 3. «Admisibles» es el conjunto de valores que la instancia considera plausibles y alimenta la sensibilidad. «Naturaleza» y «verificación» son ejes independientes (NTC 1.1); todas las fichas tienen verificación semántica NO_VERIFICADO. Las fuentes F-INF y F-E3 son los archivos aportados por el usuario; las demás son citas secundarias dentro de F-INF. Los artículos y patentes originales no fueron leídos.

Las 105 fichas bidireccionales se reproducen en el Anexo K, en el orden del plan paritario. Cada ficha conserva sus dos direcciones, sus campos y sus estados.

### F4.4.5 Vester completa: matriz formal y matrices de trabajo por escenario

La matriz formal conserva los 22 valores heredados como DECLARADO y deja 188 celdas en U. Los vectores TA y TP no están definidos donde hay U. Cada escenario numérico usa los enteros 0 a 3 con diagonal cero. TA es la suma de la fila; TP es la suma de la columna.

**MID_FORMAL.**


La {T:i015} reúne los datos de «Matriz formal MID_FORMAL de 15 por 15 variables».

:::TABLA i015 | Matriz formal MID_FORMAL de 15 por 15 variables
| Origen \ Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | U | U | U | U | 2 | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V02 | U | 0 | U | U | U | 3 | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V03 | 1 | 1 | 0 | U | U | 3 | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V04 | 2 | 2 | U | 0 | U | U | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V05 | 3 | 3 | U | U | 0 | U | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V06 | U | U | U | U | U | 0 | U | U | U | U | 3 | 3 | U | U | U | PENDIENTE |
| V07 | U | U | U | U | U | 3 | 0 | U | 1 | U | U | U | U | U | U | PENDIENTE |
| V08 | U | U | U | U | U | U | U | 0 | U | U | U | U | 2 | U | U | PENDIENTE |
| V09 | U | U | U | U | U | U | U | U | 0 | 3 | U | U | U | U | U | PENDIENTE |
| V10 | U | U | U | U | U | 2 | U | U | U | 0 | 3 | U | U | U | U | PENDIENTE |
| V11 | U | U | U | U | U | U | U | U | U | U | 0 | 2 | U | 3 | U | PENDIENTE |
| V12 | U | U | U | U | U | U | U | U | U | U | U | 0 | U | U | 3 | PENDIENTE |
| V13 | U | U | U | U | U | U | U | U | U | U | U | U | 0 | 3 | U | PENDIENTE |
| V14 | U | U | U | U | U | U | U | U | U | U | U | U | U | 0 | 2 | PENDIENTE |
| V15 | U | U | U | U | U | U | U | U | U | U | U | U | U | U | 0 | PENDIENTE |
| TP | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Cotas aritméticas de la matriz formal (NO_PREDICTIVAS).** Reemplazar cada U por 0 y por 3 produce una envolvente que no discrimina variables. No es un diagnóstico plausible ni una adjudicación. Estado: NO_PRIORIZACION_ESTABLE con esa envolvente.


La {T:i016} reúne los datos de «Cotas aritméticas de la matriz formal (NO_PREDICTIVAS)».

:::TABLA i016 | Cotas aritméticas de la matriz formal (NO_PREDICTIVAS)
| ID | I inferior | I superior | D inferior | D superior |
| --- | --- | --- | --- | --- |
| V01 | 2 | 41 | 6 | 39 |
| V02 | 3 | 42 | 6 | 39 |
| V03 | 5 | 38 | 0 | 42 |
| V04 | 4 | 40 | 0 | 42 |
| V05 | 6 | 42 | 0 | 42 |
| V06 | 6 | 42 | 13 | 40 |
| V07 | 4 | 40 | 0 | 42 |
| V08 | 2 | 41 | 0 | 42 |
| V09 | 3 | 42 | 1 | 40 |
| V10 | 5 | 41 | 3 | 42 |
| V11 | 5 | 41 | 6 | 42 |
| V12 | 3 | 42 | 5 | 41 |
| V13 | 3 | 42 | 2 | 41 |
| V14 | 2 | 41 | 6 | 42 |
| V15 | 0 | 42 | 5 | 41 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S0. Ledger E3-P04 (22 aristas). Ceros heredados condicionados; no son adjudicaciones.** Total TA = TP = 53.


La {T:i017} reúne los datos de «Matriz de influencia directa del escenario S0 (ledger de E3-P04, 22 aristas)».

:::TABLA i017 | Matriz de influencia directa del escenario S0 (ledger de E3-P04, 22 aristas)
| Origen \ Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| V03 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V04 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| V05 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 6 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| V08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| V10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 5 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 5 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| TP | 6 | 6 | 0 | 0 | 0 | 13 | 0 | 0 | 1 | 3 | 6 | 5 | 2 | 6 | 5 | 53 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S1. Matriz S1_TRABAJO_PROPUESTO del Paso 4 (32 aristas). Iteración previa, no ratificada, sin fichas completas.** Total TA = TP = 67.


La {T:i018} reúne los datos de «Matriz de influencia directa del escenario S1 (32 aristas)».

:::TABLA i018 | Matriz de influencia directa del escenario S1 (32 aristas)
| Origen \ Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 |
| V03 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V04 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V05 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 6 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V08 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 4 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| V10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 5 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 5 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 4 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| TP | 6 | 6 | 0 | 0 | 0 | 15 | 2 | 2 | 6 | 3 | 7 | 5 | 2 | 8 | 5 | 67 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S2. MID_TRABAJO derivada de las 105 fichas de F4.4.4 (48 aristas). Juicios PROPUESTOS por la instancia analítica; no ratificados.** Total TA = TP = 78.


La {T:i019} reúne los datos de «Matriz de influencia directa del escenario S2 (48 aristas)».

:::TABLA i019 | Matriz de influencia directa del escenario S2 (48 aristas)
| Origen \ Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 6 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 7 |
| V03 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V04 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 8 |
| V05 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 3 | 2 | 0 | 0 | 1 | 8 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 4 |
| V10 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 5 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 1 | 5 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 4 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 2 | 0 | 7 |
| TP | 5 | 6 | 0 | 0 | 1 | 13 | 2 | 2 | 9 | 4 | 11 | 5 | 4 | 9 | 7 | 78 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S3. Cada dirección toma el mínimo de su conjunto admisible (21 aristas). Envolvente de sensibilidad, no predictiva.** Total TA = TP = 29.


La {T:i020} reúne los datos de «Matriz de influencia directa del escenario S3 (21 aristas)».

:::TABLA i020 | Matriz de influencia directa del escenario S3 (21 aristas)
| Origen \ Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 |
| V02 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V03 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V04 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V05 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 3 |
| V07 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| V10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 2 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| V15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 2 |
| TP | 3 | 3 | 0 | 0 | 0 | 7 | 0 | 0 | 2 | 0 | 5 | 2 | 1 | 4 | 2 | 29 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S4. Cada dirección toma el máximo de su conjunto admisible (60 aristas). Envolvente de sensibilidad, no predictiva.** Total TA = TP = 118.


La {T:i021} reúne los datos de «Matriz de influencia directa del escenario S4 (60 aristas)».

:::TABLA i021 | Matriz de influencia directa del escenario S4 (60 aristas)
| Origen \ Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 7 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 1 | 0 | 8 |
| V03 | 1 | 1 | 0 | 0 | 1 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| V04 | 3 | 3 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 13 |
| V05 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 10 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 3 | 3 | 0 | 0 | 1 | 10 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V08 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 1 | 0 | 3 | 0 | 1 | 8 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 5 |
| V10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 3 | 2 | 2 | 0 | 0 | 10 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 3 | 2 | 9 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 3 | 7 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 1 | 1 | 3 | 0 | 12 |
| TP | 7 | 7 | 1 | 0 | 3 | 17 | 4 | 3 | 14 | 4 | 15 | 9 | 9 | 14 | 11 | 118 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


Los vectores TA y TP de cada tabla se verificaron contra las celdas; ambos totales globales coinciden en los cinco escenarios. La igualdad es necesaria y no suficiente para validar el modelo.

### F4.4.6 Controles numéricos y metodológicos

Los controles describen la estructura de cada escenario. Ninguno impone densidad, simetría, mínimos de entradas o salidas ni límites a las variables exógenas. Las medidas de triangularidad y de reciprocidad son descriptivas y no constituyen un veto.


La {T:i022} reúne los datos de «Controles numéricos y metodológicos».

:::TABLA i022 | Controles numéricos y metodológicos
| Escenario | TA = TP | Aristas | Densidad | Ceros/1/2/3 | Ciclos | Sin entradas | Sin salidas | Estado MICMAC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S0 | 53 | 22 | 10,5 % | 188/3/7/12 | No | V03, V04, V05, V07, V08 | V15 | EXTINCION_DE_CAMINOS |
| S1 | 67 | 32 | 15,2 % | 178/9/11/12 | Sí | V03, V04, V05 | ninguna | SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX |
| S2 | 78 | 48 | 22,9 % | 162/25/16/7 | Sí | V03, V04 | ninguna | SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX |
| S3 | 29 | 21 | 10 % | 189/13/8/0 | Sí | V03, V04, V05, V07, V08, V10 | V09 | PERIODICIDAD_OBSERVADA |
| S4 | 118 | 60 | 28,6 % | 150/24/14/22 | Sí | V04 | ninguna | SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Estructura de S2.** La componente fuertemente conexa mayor contiene 13 variables. V03 y V04 quedan fuera como fuentes sin entradas. Ciclo testigo: V06 → V07 → V06. El grafo no es acíclico; el ciclo V06↔V07 corresponde a la regla de reentrenamiento propuesta en E3 (Tabla E3-10.4).

**Reciprocidad y direccionalidad en S2.** Los 105 pares se distribuyen en tres grupos. Cuatro pares tienen aristas en ambos sentidos (V06–V07, V09–V15, V11–V12, V14–V15). Cuarenta pares tienen una sola arista. Sesenta y un pares no tienen arista. Tres de los cuatro pares recíprocos tienen valores distintos entre sentidos. El análisis paritario no impone simetría.

**Tríadas.** 94 tríadas A→B→C de S2 carecen de la arista A→C. La MID no se completa por transitividad; esas rutas se calculan en las potencias de F4.4.11.

**Medidas descriptivas dependientes del orden (S2).** Suma del triángulo superior: 55; inferior: 23. La razón no mide retroalimentación. Correlación de rangos entre posición e influencia: -0,552; entre posición y dependencia: 0,393. Son descriptivas y no prueban que el orden haya causado el patrón.

**Invarianza a permutaciones.** Se aplicaron 5 permutaciones simultáneas de filas y columnas con semilla 20261011. Tras restaurar los IDs, coincidieron los totales de las diez potencias, los vectores directos, las clases y los rangos indirectos: sí en todas.

**Objeciones metodológicas y respuesta (protocolo de auditoría Vester).**


La {T:i023} reúne los datos de «Objeciones metodológicas y respuesta (protocolo de auditoría Vester)».

:::TABLA i023 | Objeciones metodológicas y respuesta (protocolo de auditoría Vester)
| Objeción | Riesgo en este caso | Respuesta y límite |
| --- | --- | --- |
| Sesgo confirmacional | La instancia que redacta las fichas conoce la hipótesis ALT-03 y podría favorecerla. | V07→V06 recibe 3 con dominio {2,3}; V10→V06 baja de 2 a 1; V12→V15 baja de 3 a 2. La autorrevisión es una segunda pasada del mismo modelo, no un panel independiente. |
| Arrastre entre fichas | Las fichas de una misma variable comparten premisas. | Cada dirección tiene su ficha, rival y dominio. El arrastre no se mide; queda como reserva. |
| Inducción precipitada | Asignar flechas porque «tiene sentido» sin mecanismo. | 162 ceros declaran razón o mediación. Las 48 aristas declaran mecanismo; 7 se apoyan solo en premisas. |
| Escala temporal | Mezclar efectos de semanas con efectos de años. | Horizonte único H = 36 meses; los vínculos que solo actúan posproyecto (V15→V07) bajan a 1 con dominio {0,1,2}. |
| Directo frente a indirecto | Contar dos veces rutas mediadas (V06→V12 y V06→V11→V12). | V06→V12 baja de 3 a 2; las rutas por variables explícitas puntúan 0 con mediador declarado (31 ceros con mediador declarado). |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Cambios entre escenarios.** 34 celdas difieren entre S0, S1 y S2. S2 coincide con S0 en 177 de 210 celdas y con S1 en 184. S1 coincide con S0 en 200. La tabla lista cada celda con su motivo en las fichas.


La {T:i024} reúne los datos de «Cambios entre escenarios».

:::TABLA i024 | Cambios entre escenarios
| Origen→Destino | S0 | S1 | S2 |
| --- | --- | --- | --- |
| V01→V11 | 0 | 0 | 3 |
| V01→V14 | 0 | 1 | 1 |
| V02→V09 | 0 | 0 | 1 |
| V02→V11 | 0 | 0 | 2 |
| V02→V14 | 0 | 1 | 1 |
| V03→V09 | 0 | 1 | 1 |
| V04→V06 | 0 | 0 | 1 |
| V04→V08 | 0 | 1 | 1 |
| V04→V09 | 0 | 0 | 1 |
| V04→V13 | 0 | 0 | 1 |
| V05→V01 | 3 | 3 | 2 |
| V05→V09 | 0 | 2 | 2 |
| V06→V07 | 0 | 0 | 1 |
| V06→V09 | 0 | 0 | 1 |
| V06→V12 | 3 | 3 | 2 |
| V06→V15 | 0 | 0 | 1 |
| V07→V08 | 0 | 1 | 1 |
| V08→V06 | 0 | 2 | 0 |
| V09→V15 | 0 | 0 | 1 |
| V10→V06 | 2 | 2 | 1 |
| V10→V11 | 3 | 3 | 2 |
| V10→V12 | 0 | 0 | 1 |
| V10→V13 | 0 | 0 | 1 |
| V11→V14 | 3 | 3 | 2 |
| V11→V15 | 0 | 0 | 1 |
| V12→V11 | 0 | 1 | 1 |
| V12→V14 | 0 | 0 | 1 |
| V12→V15 | 3 | 3 | 2 |
| V13→V14 | 3 | 3 | 2 |
| V15→V05 | 0 | 0 | 1 |
| V15→V07 | 0 | 2 | 1 |
| V15→V09 | 0 | 2 | 2 |
| V15→V10 | 0 | 0 | 1 |
| V15→V14 | 0 | 0 | 2 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


### F4.4.7 Plano Vester por escenario

Cada escenario tiene su plano con la dependencia en el eje X y la influencia en el eje Y. Las variables con idéntica posición comparten etiqueta. Los ejes usan el porcentaje del total de cada eje y los cortes por mediana. El motor genera el SVG editable con fondo transparente y la nota de que el escenario no está ratificado.

**S0 (S0_HISTORICO_CONDICIONADO).** Cortes: influencia 3 y dependencia 3 (mediana); media 3,533. Igualdad con un corte implica FRONTERA.


La {F:vester_s0} reproduce «Plano Vester del escenario S0: ledger de E3-P04 con 22 aristas».

:::FIGURA vester_s0 | Plano Vester del escenario S0: ledger de E3-P04 con 22 aristas | Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Eje vertical: influencia activa. Eje horizontal: dependencia pasiva. Las líneas discontinuas marcan las medianas de influencia y de dependencia.

**S1 (S1_PREVIO_DOC).** Cortes: influencia 4 y dependencia 5 (mediana); media 4,467. Igualdad con un corte implica FRONTERA.


La {F:vester_s1} reproduce «Plano Vester del escenario S1: iteración previa con 32 aristas».

:::FIGURA vester_s1 | Plano Vester del escenario S1: iteración previa con 32 aristas | Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Las líneas discontinuas marcan las medianas.

**S2 (S_TRABAJO_PROPUESTO).** Cortes: influencia 5 y dependencia 5 (mediana); media 5,2. Igualdad con un corte implica FRONTERA.


La {F:vester_s2} reproduce «Plano Vester del escenario S2: escenario de trabajo con 48 aristas».

:::FIGURA vester_s2 | Plano Vester del escenario S2: escenario de trabajo con 48 aristas | Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Escenario de trabajo del proyecto. Las líneas discontinuas marcan las medianas.

**S3 (S3_ENVOLVENTE_ADMISIBLE_BAJA).** Cortes: influencia 2 y dependencia 2 (mediana); media 1,933. Igualdad con un corte implica FRONTERA.


La {F:vester_s3} reproduce «Plano Vester del escenario S3: envolvente admisible baja con 21 aristas».

:::FIGURA vester_s3 | Plano Vester del escenario S3: envolvente admisible baja con 21 aristas | Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Cada dirección toma el mínimo de su conjunto admisible.

**S4 (S4_ENVOLVENTE_ADMISIBLE_ALTA).** Cortes: influencia 8 y dependencia 7 (mediana); media 7,867. Igualdad con un corte implica FRONTERA.


La {F:vester_s4} reproduce «Plano Vester del escenario S4: envolvente admisible alta con 60 aristas».

:::FIGURA vester_s4 | Plano Vester del escenario S4: envolvente admisible alta con 60 aristas | Nota. Elaboración propia con RESULTADOS.json de la sección F4.4 (semilla 20261011). Cada dirección toma el máximo de su conjunto admisible.

**Nota de lectura.** Los cuadrantes clasifican posiciones estructurales. No acreditan causalidad ni prioridad de inversión. Los planos S3 y S4 son envolventes de sensibilidad.

### F4.4.8 Clasificación directa por variable, rangos y contraste media-mediana

La clasificación usa enteros exactos. Una variable es CRITICA si supera ambos cortes. Es ACTIVA si supera el de influencia y no el de dependencia. Es REACTIVA en el caso inverso y AUTONOMA_RELATIVA si queda por debajo de ambos. Igualar un corte es FRONTERA.

**S0.** Mediana de I = 3; mediana de D = 3; media = 3,533. Clases por mediana: ACTIVA 4, AUTONOMA_RELATIVA 1, CRITICA 2, FRONTERA 5, REACTIVA 3. Cambian con la media: V02, V09, V10, V12, V13.


La {T:i025} reúne los datos de «Clasificación directa de las variables en el escenario S0».

:::TABLA i025 | Clasificación directa de las variables en el escenario S0
| ID | Variable | I | D | Rango I | Rango D | Clase por mediana | Clase por media |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Concentración PM2.5 | 2 | 6 | 13 | 3,5 | REACTIVA | REACTIVA |
| V02 | Concentración PM10 | 3 | 6 | 9,5 | 3,5 | FRONTERA | REACTIVA |
| V03 | Humedad relativa | 5 | 0 | 4 | 13 | ACTIVA | ACTIVA |
| V04 | Velocidad del viento | 4 | 0 | 6,5 | 13 | ACTIVA | ACTIVA |
| V05 | Volumen de escombros | 6 | 0 | 1,5 | 13 | ACTIVA | ACTIVA |
| V06 | Error de medición IoT | 6 | 13 | 1,5 | 1 | CRITICA | CRITICA |
| V07 | Frecuencia de calibración | 4 | 0 | 6,5 | 13 | ACTIVA | ACTIVA |
| V08 | Latencia de datos | 2 | 0 | 13 | 13 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V09 | Disponibilidad de nodos IoT | 3 | 1 | 9,5 | 10 | FRONTERA | AUTONOMA_RELATIVA |
| V10 | Densidad del gemelo | 5 | 3 | 4 | 8 | FRONTERA | ACTIVA |
| V11 | Índice AQHI | 5 | 6 | 4 | 3,5 | CRITICA | CRITICA |
| V12 | Falsas alarmas | 3 | 5 | 9,5 | 6,5 | FRONTERA | REACTIVA |
| V13 | Anticipación | 3 | 2 | 9,5 | 9 | FRONTERA | AUTONOMA_RELATIVA |
| V14 | Personas alertadas | 2 | 6 | 13 | 3,5 | REACTIVA | REACTIVA |
| V15 | Adopción institucional | 0 | 5 | 15 | 6,5 | REACTIVA | REACTIVA |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S1.** Mediana de I = 4; mediana de D = 5; media = 4,467. Clases por mediana: ACTIVA 5, AUTONOMA_RELATIVA 1, CRITICA 2, FRONTERA 4, REACTIVA 3. Cambian con la media: V02, V08, V12, V15.


La {T:i026} reúne los datos de «Clasificación directa de las variables en el escenario S1».

:::TABLA i026 | Clasificación directa de las variables en el escenario S1
| ID | Variable | I | D | Rango I | Rango D | Clase por mediana | Clase por media |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Concentración PM2.5 | 3 | 6 | 13 | 5 | REACTIVA | REACTIVA |
| V02 | Concentración PM10 | 4 | 6 | 9,5 | 5 | FRONTERA | REACTIVA |
| V03 | Humedad relativa | 6 | 0 | 2,5 | 14 | ACTIVA | ACTIVA |
| V04 | Velocidad del viento | 5 | 0 | 5,5 | 14 | ACTIVA | ACTIVA |
| V05 | Volumen de escombros | 8 | 0 | 1 | 14 | ACTIVA | ACTIVA |
| V06 | Error de medición IoT | 6 | 15 | 2,5 | 1 | CRITICA | CRITICA |
| V07 | Frecuencia de calibración | 5 | 2 | 5,5 | 11 | ACTIVA | ACTIVA |
| V08 | Latencia de datos | 4 | 2 | 9,5 | 11 | FRONTERA | AUTONOMA_RELATIVA |
| V09 | Disponibilidad de nodos IoT | 3 | 6 | 13 | 5 | REACTIVA | REACTIVA |
| V10 | Densidad del gemelo | 5 | 3 | 5,5 | 9 | ACTIVA | ACTIVA |
| V11 | Índice AQHI | 5 | 7 | 5,5 | 3 | CRITICA | CRITICA |
| V12 | Falsas alarmas | 4 | 5 | 9,5 | 7,5 | FRONTERA | REACTIVA |
| V13 | Anticipación | 3 | 2 | 13 | 11 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V14 | Personas alertadas | 2 | 8 | 15 | 2 | REACTIVA | REACTIVA |
| V15 | Adopción institucional | 4 | 5 | 9,5 | 7,5 | FRONTERA | REACTIVA |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S2.** Mediana de I = 5; mediana de D = 5; media = 5,2. Clases por mediana: ACTIVA 3, AUTONOMA_RELATIVA 2, CRITICA 3, FRONTERA 5, REACTIVA 2. Cambian con la media: V01, V07, V10, V11, V12.


La {T:i027} reúne los datos de «Clasificación directa de las variables en el escenario S2».

:::TABLA i027 | Clasificación directa de las variables en el escenario S2
| ID | Variable | I | D | Rango I | Rango D | Clase por mediana | Clase por media |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Concentración PM2.5 | 6 | 5 | 6,5 | 7,5 | FRONTERA | ACTIVA |
| V02 | Concentración PM10 | 7 | 6 | 4 | 6 | CRITICA | CRITICA |
| V03 | Humedad relativa | 6 | 0 | 6,5 | 14,5 | ACTIVA | ACTIVA |
| V04 | Velocidad del viento | 8 | 0 | 1,5 | 14,5 | ACTIVA | ACTIVA |
| V05 | Volumen de escombros | 7 | 1 | 4 | 13 | ACTIVA | ACTIVA |
| V06 | Error de medición IoT | 8 | 13 | 1,5 | 1 | CRITICA | CRITICA |
| V07 | Frecuencia de calibración | 5 | 2 | 9 | 11,5 | FRONTERA | AUTONOMA_RELATIVA |
| V08 | Latencia de datos | 2 | 2 | 14 | 11,5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V09 | Disponibilidad de nodos IoT | 4 | 9 | 11,5 | 3,5 | REACTIVA | REACTIVA |
| V10 | Densidad del gemelo | 5 | 4 | 9 | 9,5 | FRONTERA | AUTONOMA_RELATIVA |
| V11 | Índice AQHI | 5 | 11 | 9 | 2 | FRONTERA | REACTIVA |
| V12 | Falsas alarmas | 4 | 5 | 11,5 | 7,5 | FRONTERA | AUTONOMA_RELATIVA |
| V13 | Anticipación | 2 | 4 | 14 | 9,5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V14 | Personas alertadas | 2 | 9 | 14 | 3,5 | REACTIVA | REACTIVA |
| V15 | Adopción institucional | 7 | 7 | 4 | 5 | CRITICA | CRITICA |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S3.** Mediana de I = 2; mediana de D = 2; media = 1,933. Clases por mediana: ACTIVA 1, AUTONOMA_RELATIVA 2, CRITICA 2, FRONTERA 9, REACTIVA 1. Cambian con la media: V02, V03, V04, V07, V09, V11, V12, V13, V15.


La {T:i028} reúne los datos de «Clasificación directa de las variables en el escenario S3».

:::TABLA i028 | Clasificación directa de las variables en el escenario S3
| ID | Variable | I | D | Rango I | Rango D | Clase por mediana | Clase por media |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Concentración PM2.5 | 3 | 3 | 2,5 | 4,5 | CRITICA | CRITICA |
| V02 | Concentración PM10 | 2 | 3 | 7 | 4,5 | FRONTERA | CRITICA |
| V03 | Humedad relativa | 2 | 0 | 7 | 12,5 | FRONTERA | ACTIVA |
| V04 | Velocidad del viento | 2 | 0 | 7 | 12,5 | FRONTERA | ACTIVA |
| V05 | Volumen de escombros | 5 | 0 | 1 | 12,5 | ACTIVA | ACTIVA |
| V06 | Error de medición IoT | 3 | 7 | 2,5 | 1 | CRITICA | CRITICA |
| V07 | Frecuencia de calibración | 2 | 0 | 7 | 12,5 | FRONTERA | ACTIVA |
| V08 | Latencia de datos | 1 | 0 | 12,5 | 12,5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V09 | Disponibilidad de nodos IoT | 0 | 2 | 15 | 7 | FRONTERA | REACTIVA |
| V10 | Densidad del gemelo | 1 | 0 | 12,5 | 12,5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V11 | Índice AQHI | 2 | 5 | 7 | 2 | FRONTERA | CRITICA |
| V12 | Falsas alarmas | 1 | 2 | 12,5 | 7 | FRONTERA | REACTIVA |
| V13 | Anticipación | 2 | 1 | 7 | 9 | FRONTERA | ACTIVA |
| V14 | Personas alertadas | 1 | 4 | 12,5 | 3 | REACTIVA | REACTIVA |
| V15 | Adopción institucional | 2 | 2 | 7 | 7 | FRONTERA | CRITICA |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S4.** Mediana de I = 8; mediana de D = 7; media = 7,867. Clases por mediana: ACTIVA 3, AUTONOMA_RELATIVA 1, CRITICA 3, FRONTERA 4, REACTIVA 4. Cambian con la media: V01, V02, V03, V08.


La {T:i029} reúne los datos de «Clasificación directa de las variables en el escenario S4».

:::TABLA i029 | Clasificación directa de las variables en el escenario S4
| ID | Variable | I | D | Rango I | Rango D | Clase por mediana | Clase por media |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Concentración PM2.5 | 7 | 7 | 10,5 | 8,5 | FRONTERA | AUTONOMA_RELATIVA |
| V02 | Concentración PM10 | 8 | 7 | 8 | 8,5 | FRONTERA | ACTIVA |
| V03 | Humedad relativa | 8 | 1 | 8 | 14 | FRONTERA | ACTIVA |
| V04 | Velocidad del viento | 13 | 0 | 1 | 15 | ACTIVA | ACTIVA |
| V05 | Volumen de escombros | 10 | 3 | 4 | 12,5 | ACTIVA | ACTIVA |
| V06 | Error de medición IoT | 10 | 17 | 4 | 1 | CRITICA | CRITICA |
| V07 | Frecuencia de calibración | 6 | 4 | 12 | 10,5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V08 | Latencia de datos | 8 | 3 | 8 | 12,5 | FRONTERA | ACTIVA |
| V09 | Disponibilidad de nodos IoT | 5 | 14 | 13 | 3,5 | REACTIVA | REACTIVA |
| V10 | Densidad del gemelo | 10 | 4 | 4 | 10,5 | ACTIVA | ACTIVA |
| V11 | Índice AQHI | 9 | 15 | 6 | 2 | CRITICA | CRITICA |
| V12 | Falsas alarmas | 7 | 9 | 10,5 | 6,5 | REACTIVA | REACTIVA |
| V13 | Anticipación | 3 | 9 | 14 | 6,5 | REACTIVA | REACTIVA |
| V14 | Personas alertadas | 2 | 14 | 15 | 3,5 | REACTIVA | REACTIVA |
| V15 | Adopción institucional | 12 | 11 | 2 | 5 | CRITICA | CRITICA |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Lectura condicional de S2.** Con corte por mediana, V02, V06, V15 quedan en el cuadrante crítico: ejercen y reciben influencia por encima de la mediana. V03, V04, V05 son activas. V09, V14 son reactivas. V08, V13 son autónomas relativas. V01, V07, V10, V11, V12 caen en FRONTERA porque igualan un corte.

El contraste con la media (5,2) cambia la clase de V01 a ACTIVA; V07 a AUTONOMA_RELATIVA; V10 a AUTONOMA_RELATIVA; V11 a REACTIVA; V12 a AUTONOMA_RELATIVA. La clasificación de esas variables depende del corte y no se interpreta como rol firme. La lectura vale solo para el escenario de trabajo propuesto.

**Registro de decisión ND-08 (cuadrantes y palancas de intervención).**




La {T:i030} reúne los datos de «Registro de decisión GENESIS: ND-08 Clasificación por cuadrantes y palancas de intervención».

:::TABLA i030 | Registro de decisión GENESIS: ND-08 Clasificación por cuadrantes y palancas de intervención
| Campo | Contenido |
| --- | --- |
| NODO | ND-08 Clasificación por cuadrantes y palancas de intervención |
| CLASE | MAYOR. Determina qué variables se proponen como objeto de intervención. |
| DECISION | Adoptar la clasificación por mediana de S2 como lectura condicional. No designar palancas por la posición en el cuadrante. Proponer V07 como candidata de intervención condicionada, sin estatus de palanca máxima. |
| DECIDE | Equipo formulador (rol POR_IDENTIFICAR). La propuesta proviene de la instancia analítica. |
| EXCLUYE | Designar palancas por cuadrante. Usar la clase como rol causal. Presentar V07 como palanca independiente máxima. |
| NODOS_BLANCOS | 5: S2 con cortes de influencia y dependencia iguales a 5 (F4.4.8); V07 con influencia 5, igual a la mediana, por eso FRONTERA (F4.4.8); ficha V07→V06 = 3 con dominio de 2 a 3 (F4.4.4); V07 pasa a AUTONOMA_RELATIVA si la ficha valiera 2 (F4.4.13); V05, V06 y V14 conservan su clase en los cinco escenarios (F4.4.13). |
| NODOS_GRISES | 2: el proyecto puede modificar V07, V09 y V10 en terreno (actualización remota, repuestos); V07 actúa sobre V06 con la magnitud asignada. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 1 (la clase no determina la controlabilidad; el límite se declara) |
| PATRON_DOMINANTE | PR-06 (patrón emergente): la prioridad de intervención depende de la frontera de clase y de la ratificación de las fichas. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. La controlabilidad exige conectividad y personal no verificados en el territorio. |
| ESCENA_SIMULABLE | Un analista de la IES recalcula cada trimestre la clase de V07 con las fichas ratificadas y registra si cambia. El equipo formulador revisa la prioridad de intervención con ese registro. |
| EVIDENCIA_JH_A | Acta de adjudicación de las fichas V07→V06 y V10→V06 con firmantes (artefacto por producir; no existe aún). |
| EVIDENCIA_JH_B | Tablas de F4.4.8 con influencia, dependencia, rangos y clases por mediana y por media, y perturbación de un enlace en F4.4.13 (87 cambios). |
| CERCA_CONCEPTUAL | La clasificación no es un orden de prioridad de inversión ni una prueba de causalidad. |
| ESTATUTO_CAUSAL | HIE. Ninguna afirmación pasa a IDC ni a EST por la clase. |
| VEREDICTO | Clasificación condicional. V07 es candidata de intervención, no palanca máxima. Ninguna variable técnica controlable es ACTIVA en S2. |
| RAZON_DEL_DESCARTE | Se descarta designar palancas por cuadrante porque las cuatro variables técnicas controlables (V07 a V10) cambian de clase entre los cinco escenarios. |
| RESULTADO | CIERRA con vacíos declarados (controlabilidad en terreno y ratificación de fichas). |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


### F4.4.9 MID de MICMAC idéntica a Vester dentro de cada escenario

MICMAC usa exactamente la matriz de Vester de cada escenario como A¹. No se puntúa de nuevo ni se completa por transitividad. La {T:i031} compara la huella SHA-256 de la matriz de Vester con la de la primera potencia y la igualdad celda por celda.


:::TABLA i031 | MID de MICMAC idéntica a Vester dentro de cada escenario
| Escenario | SHA-256 de la MID de Vester | SHA-256 de A¹ en MICMAC | Celda por celda |
| --- | --- | --- | --- |
| S0 | 719cc17f0a38cedb… | 719cc17f0a38cedb… | Idénticas |
| S1 | 65498ee94582a1e4… | 65498ee94582a1e4… | Idénticas |
| S2 | c36ed81b9bd96772… | c36ed81b9bd96772… | Idénticas |
| S3 | 62d8a1ee96b3f478… | 62d8a1ee96b3f478… | Idénticas |
| S4 | 7ba7240362ff9328… | 7ba7240362ff9328… | Idénticas |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


Las huellas se truncan a 16 caracteres en la tabla; los valores completos constan en MANIFIESTO.json y RESULTADOS.json. La igualdad comprueba que el cálculo usa una sola matriz; no valida los juicios.

### F4.4.10 Influencias potenciales (MIDP) y máscara

Estado: **NO_CONFIGURADA_NO_INFERIDA**. Una MIDP exige un horizonte posterior a H y condiciones explícitas que habiliten relaciones hoy ausentes. El expediente no declara ninguno: no hay contrato de operación posproyecto, presupuesto territorial comprometido ni plazo mayor de 36 meses.

El motor no infiere relaciones potenciales ni usa U para forzar enlaces. El vínculo V15→V07 podría valer 2 bajo la premisa PD-0 en la fase posproyecto. Ese valor consta como dominio admisible de la ficha y como sensibilidad en F4.4.13, no como MIDP. La ausencia de MIDP no bloquea el análisis actual.

### F4.4.11 Potencias completas A¹ a Aᵏ, terminales y estabilidad observada

Las potencias se calculan con enteros exactos: A¹ = A y A^(k+1) = A^k · A. El índice k mide la longitud de recorrido y no el tiempo. Las diagonales de las potencias pueden ser positivas por recorridos cerrados y no se fuerzan a cero. Cada potencia completa consta en los CSV con TA y TP, y en RESULTADOS.json.

**S0.** Estado: EXTINCION_DE_CAMINOS. Primera potencia nula: 7. Potencia de referencia: A^6 (última no nula).


La {T:i032} reúne los datos de «Estabilidad de las potencias de MICMAC en el escenario S0».

:::TABLA i032 | Estabilidad de las potencias de MICMAC en el escenario S0
| k | Total TA = TP | Celdas no nulas |
| --- | --- | --- |
| 1 | 53 | 22 |
| 2 | 189 | 23 |
| 3 | 672 | 27 |
| 4 | 1.521 | 19 |
| 5 | 1.548 | 7 |
| 6 | 216 | 1 |
| 7 | 0 | 0 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S1.** Estado: SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX. Primera potencia nula: ninguna hasta KMAX. Potencia de referencia: A^10.


La {T:i033} reúne los datos de «Estabilidad de las potencias de MICMAC en el escenario S1».

:::TABLA i033 | Estabilidad de las potencias de MICMAC en el escenario S1
| k | Total TA = TP | Celdas no nulas |
| --- | --- | --- |
| 1 | 67 | 32 |
| 2 | 280 | 47 |
| 3 | 1.205 | 68 |
| 4 | 4.855 | 95 |
| 5 | 19.154 | 122 |
| 6 | 80.500 | 136 |
| 7 | 349.230 | 143 |
| 8 | 1.484.060 | 148 |
| 9 | 6.071.508 | 150 |
| 10 | 24.573.040 | 150 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S2.** Estado: SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX. Primera potencia nula: ninguna hasta KMAX. Potencia de referencia: A^10.


La {T:i034} reúne los datos de «Estabilidad de las potencias de MICMAC en el escenario S2».

:::TABLA i034 | Estabilidad de las potencias de MICMAC en el escenario S2
| k | Total TA = TP | Celdas no nulas |
| --- | --- | --- |
| 1 | 78 | 48 |
| 2 | 403 | 99 |
| 3 | 1.974 | 151 |
| 4 | 9.427 | 179 |
| 5 | 45.846 | 189 |
| 6 | 224.551 | 192 |
| 7 | 1.101.608 | 195 |
| 8 | 5.373.011 | 195 |
| 9 | 26.172.826 | 195 |
| 10 | 127.613.540 | 195 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S3.** Estado: PERIODICIDAD_OBSERVADA. Primera potencia nula: ninguna hasta KMAX. Potencia de referencia: A^10.


La {T:i035} reúne los datos de «Estabilidad de las potencias de MICMAC en el escenario S3».

:::TABLA i035 | Estabilidad de las potencias de MICMAC en el escenario S3
| k | Total TA = TP | Celdas no nulas |
| --- | --- | --- |
| 1 | 29 | 21 |
| 2 | 58 | 26 |
| 3 | 100 | 31 |
| 4 | 133 | 32 |
| 5 | 167 | 31 |
| 6 | 169 | 32 |
| 7 | 167 | 31 |
| 8 | 169 | 32 |
| 9 | 167 | 31 |
| 10 | 169 | 32 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**S4.** Estado: SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX. Primera potencia nula: ninguna hasta KMAX. Potencia de referencia: A^10.


La {T:i036} reúne los datos de «Estabilidad de las potencias de MICMAC en el escenario S4».

:::TABLA i036 | Estabilidad de las potencias de MICMAC en el escenario S4
| k | Total TA = TP | Celdas no nulas |
| --- | --- | --- |
| 1 | 118 | 60 |
| 2 | 856 | 125 |
| 3 | 6.249 | 172 |
| 4 | 44.281 | 189 |
| 5 | 312.165 | 193 |
| 6 | 2.210.258 | 195 |
| 7 | 15.707.903 | 195 |
| 8 | 111.521.718 | 195 |
| 9 | 791.024.704 | 195 |
| 10 | 5.608.709.083 | 195 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Estabilidad observada en S2.** La ventana exige tres iteraciones consecutivas con igual rango de influencia y de dependencia. La tabla compara cada iteración con la anterior.


La {T:i037} reúne los datos de «Estabilidad observada en S2».

:::TABLA i037 | Estabilidad observada en S2
| k | Rango de influencia igual al anterior | Rango de dependencia igual al anterior |
| --- | --- | --- |
| 2 | no | no |
| 3 | no | no |
| 4 | no | no |
| 5 | no | sí |
| 6 | no | no |
| 7 | sí | no |
| 8 | sí | sí |
| 9 | sí | no |
| 10 | sí | sí |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


El rango de influencia se mantiene desde k = 7. El de dependencia alterna. No se observa estabilidad conjunta. Esta condición no demuestra convergencia ni su ausencia dinámica.

**Rangos de influencia por iteración en S2** (1 = mayor influencia; promedio en empates).


La {T:i038} reúne los datos de «Rangos de influencia por iteración en S2».

:::TABLA i038 | Rangos de influencia por iteración en S2
| ID | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 | k=9 | k=10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 6,5 | 6 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| V02 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| V03 | 6,5 | 2,5 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| V04 | 1,5 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| V05 | 4 | 2,5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| V06 | 1,5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| V07 | 9 | 7 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| V08 | 14 | 14,5 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| V09 | 11,5 | 10 | 10 | 11 | 12 | 12 | 12 | 12 | 12 | 12 |
| V10 | 9 | 9 | 9 | 9 | 10 | 9 | 9 | 9 | 9 | 9 |
| V11 | 9 | 12 | 11 | 12 | 9 | 10 | 10 | 10 | 10 | 10 |
| V12 | 11,5 | 11 | 12 | 10 | 11 | 11 | 11 | 11 | 11 | 11 |
| V13 | 14 | 14,5 | 14 | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| V14 | 14 | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 13 | 13 |
| V15 | 4 | 8 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Rangos de dependencia por iteración en S2.**


La {T:i039} reúne los datos de «Rangos de dependencia por iteración en S2».

:::TABLA i039 | Rangos de dependencia por iteración en S2
| ID | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 | k=9 | k=10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 7,5 | 12,5 | 13 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| V02 | 6 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 |
| V03 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 |
| V04 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 | 14,5 |
| V05 | 13 | 10 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| V06 | 1 | 5 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| V07 | 11,5 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| V08 | 11,5 | 12,5 | 12 | 13 | 13 | 13 | 13 | 13 | 13 | 13 |
| V09 | 3,5 | 6 | 5 | 3 | 3 | 4 | 4 | 4 | 4 | 4 |
| V10 | 9,5 | 7 | 6 | 5 | 5 | 5 | 6 | 6 | 5 | 5 |
| V11 | 2 | 1 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 3 |
| V12 | 7,5 | 4 | 3 | 6 | 6 | 6 | 5 | 5 | 6 | 6 |
| V13 | 9,5 | 9 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| V14 | 3,5 | 3 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| V15 | 5 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Terminal de S0.** Las potencias se extinguen en A^7. A^6 conserva un solo recorrido de seis aristas (V07→V09→V10→V06→V11→V14→V15), por lo que solo V07 tiene influencia indirecta positiva y las demás variables empatan. Los rangos indirectos de S0 no constituyen un ranking de importancia.

### F4.4.12 Plano indirecto, desplazamiento de rangos y variables ocultas

El plano indirecto usa la potencia de referencia de cada escenario. El ascenso es el rango directo menos el rango indirecto: un valor positivo indica que la variable gana posición al considerar recorridos largos.

**S2, referencia A^10.**


La {T:i040} reúne los datos de «Clasificación indirecta del escenario S2 con la potencia A^10».

:::TABLA i040 | Clasificación indirecta del escenario S2 con la potencia A^10
| ID | Rango I directo | Rango I indirecto | Ascenso I | Rango D directo | Rango D indirecto | Ascenso D | Clase indirecta |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 6,5 | 7 | -0,5 | 7,5 | 12 | -4,5 | ACTIVA |
| V02 | 4 | 4 | 0 | 6 | 11 | -5 | ACTIVA |
| V03 | 6,5 | 3 | 3,5 | 14,5 | 14,5 | 0 | ACTIVA |
| V04 | 1,5 | 2 | -0,5 | 14,5 | 14,5 | 0 | ACTIVA |
| V05 | 4 | 1 | 3 | 13 | 9 | 4 | ACTIVA |
| V06 | 1,5 | 5 | -3,5 | 1 | 7 | -6 | CRITICA |
| V07 | 9 | 8 | 1 | 11,5 | 8 | 3,5 | FRONTERA |
| V08 | 14 | 15 | -1 | 11,5 | 13 | -1,5 | AUTONOMA_RELATIVA |
| V09 | 11,5 | 12 | -0,5 | 3,5 | 4 | -0,5 | REACTIVA |
| V10 | 9 | 9 | 0 | 9,5 | 5 | 4,5 | REACTIVA |
| V11 | 9 | 10 | -1 | 2 | 3 | -1 | REACTIVA |
| V12 | 11,5 | 11 | 0,5 | 7,5 | 6 | 1,5 | REACTIVA |
| V13 | 14 | 14 | 0 | 9,5 | 10 | -0,5 | AUTONOMA_RELATIVA |
| V14 | 14 | 13 | 1 | 3,5 | 2 | 1,5 | REACTIVA |
| V15 | 4 | 6 | -2 | 5 | 1 | 4 | CRITICA |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.



La {F:micmac_s2} reproduce «Plano MICMAC del escenario S2 con la potencia de referencia A^10».

:::FIGURA micmac_s2 | Plano MICMAC del escenario S2 con la potencia de referencia A^10 | Nota. Elaboración propia con RESULTADOS.json de la sección F4.4. Influencia y dependencia indirectas calculadas con potencias exactas de la matriz hasta k = 10.

**Candidatas a variables ocultas en S2 (umbral de ascenso en influencia, como sensibilidad y no como prueba).** Umbral 2: V03, V05. Umbral 3: V03, V05. Umbral 4: ninguna.

Descienden dos o más posiciones: V06 (-3,5), V15 (-2). Las candidatas V03 y V05 son exógenas o poco controlables: reciben poca influencia y alimentan cadenas largas. Su ascenso describe origen de recorridos, no una palanca de intervención.

**Cotejo de la iteración previa (S1) con el cálculo exacto.** El documento previo afirma tres cosas sobre la influencia indirecta. V05 cae al rango 12. V15 sube al rango 2. V14 sube al rango 6.


La {T:i041} reúne los datos de «Cotejo de la iteración previa (S1) con el cálculo exacto».

:::TABLA i041 | Cotejo de la iteración previa (S1) con el cálculo exacto
| ID | Rango I indirecto según el documento previo | Rango I indirecto exacto (A^10) | Coincide |
| --- | --- | --- | --- |
| V05 | 12 | 1 | No |
| V15 | 2 | 6 | No |
| V14 | 6 | 14 | No |
| V06 | 4 | 4 | Sí |
| V07 | 1 | 3 | No |
| V03 | 13 | 2 | No |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


Los totales de potencias del documento previo tampoco son reproducibles.


La {T:i042} reúne los datos de «Plano indirecto, desplazamiento de rangos y variables ocultas».

:::TABLA i042 | Plano indirecto, desplazamiento de rangos y variables ocultas
| k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Documento previo | 67 | 129 | 258 | 561 | 1.257 | 2.894 | 6.574 | 15.195 | 35.539 | 82.529 |
| Cálculo exacto | 67 | 280 | 1.205 | 4.855 | 19.154 | 80.500 | 349.230 | 1.484.060 | 6.071.508 | 24.573.040 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


Solo A¹ coincide. El rango de V05 resulta 1 y no 12; el de V03 resulta 2 y no 13. La narrativa del documento previo sobre la caída de las variables ambientales no resiste el cálculo.

### F4.4.13 Contraste directo-indirecto, escenarios, rutas explicativas y sensibilidad ordinal

**Rango de influencia indirecta por escenario (potencia de referencia).** En S0 solo V07 tiene influencia positiva en A^6; los demás empatan en 8,5 y no hay ranking.


La {T:i043} reúne los datos de «Rango de influencia indirecta por escenario (potencia de referencia)».

:::TABLA i043 | Rango de influencia indirecta por escenario (potencia de referencia)
| ID | S0 | S1 | S2 | S3 | S4 |
| --- | --- | --- | --- | --- | --- |
| V01 | 8,5 | 13 | 7 | 3 | 8 |
| V02 | 8,5 | 9 | 4 | 5 | 7 |
| V03 | 8,5 | 2 | 3 | 5 | 4 |
| V04 | 8,5 | 7 | 2 | 2 | 1 |
| V05 | 8,5 | 1 | 1 | 1 | 3 |
| V06 | 8,5 | 4 | 5 | 7 | 2 |
| V07 | 1 | 3 | 8 | 5 | 9 |
| V08 | 8,5 | 12 | 15 | 8,5 | 12 |
| V09 | 8,5 | 10 | 12 | 15 | 13 |
| V10 | 8,5 | 5 | 9 | 8,5 | 6 |
| V11 | 8,5 | 11 | 10 | 11,5 | 10 |
| V12 | 8,5 | 8 | 11 | 11,5 | 11 |
| V13 | 8,5 | 15 | 14 | 11,5 | 15 |
| V14 | 8,5 | 14 | 13 | 11,5 | 14 |
| V15 | 8,5 | 6 | 6 | 14 | 5 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Clase directa por mediana en los cinco escenarios.**


La {T:i044} reúne los datos de «Clase directa por mediana en los cinco escenarios».

:::TABLA i044 | Clase directa por mediana en los cinco escenarios
| ID | S0 | S1 | S2 | S3 | S4 | Estable en las cinco |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | REACTIVA | REACTIVA | FRONTERA | CRITICA | FRONTERA | No |
| V02 | FRONTERA | FRONTERA | CRITICA | FRONTERA | FRONTERA | No |
| V03 | ACTIVA | ACTIVA | ACTIVA | FRONTERA | FRONTERA | No |
| V04 | ACTIVA | ACTIVA | ACTIVA | FRONTERA | ACTIVA | No |
| V05 | ACTIVA | ACTIVA | ACTIVA | ACTIVA | ACTIVA | Sí |
| V06 | CRITICA | CRITICA | CRITICA | CRITICA | CRITICA | Sí |
| V07 | ACTIVA | ACTIVA | FRONTERA | FRONTERA | AUTONOMA_RELATIVA | No |
| V08 | AUTONOMA_RELATIVA | FRONTERA | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA | FRONTERA | No |
| V09 | FRONTERA | REACTIVA | REACTIVA | FRONTERA | REACTIVA | No |
| V10 | FRONTERA | ACTIVA | FRONTERA | AUTONOMA_RELATIVA | ACTIVA | No |
| V11 | CRITICA | CRITICA | FRONTERA | FRONTERA | CRITICA | No |
| V12 | FRONTERA | FRONTERA | FRONTERA | FRONTERA | REACTIVA | No |
| V13 | FRONTERA | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA | FRONTERA | REACTIVA | No |
| V14 | REACTIVA | REACTIVA | REACTIVA | REACTIVA | REACTIVA | Sí |
| V15 | REACTIVA | FRONTERA | CRITICA | FRONTERA | CRITICA | No |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


La clase directa permanece idéntica en los cinco escenarios solo para V05, V06, V14. Las demás variables cambian de clase al variar los juicios, lo que limita cualquier afirmación de rol firme.

**Sensibilidad ordinal en S2.** Se recodificó la escala con [0,1,2,3], [0,1,3,5] y [0,1,2,4]. La recodificación prueba la robustez de una escala ordinal; no aporta evidencia del territorio.


La {T:i045} reúne los datos de «Sensibilidad ordinal en S2».

:::TABLA i045 | Sensibilidad ordinal en S2
| ID | Clase [0, 1, 2, 3] | Clase [0, 1, 3, 5] | Clase [0, 1, 2, 4] | Rango I A^10 [0, 1, 2, 3] | Rango I A^10 [0, 1, 3, 5] | Rango I A^10 [0, 1, 2, 4] |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | FRONTERA | FRONTERA | FRONTERA | 7 | 6 | 8 |
| V02 | CRITICA | CRITICA | CRITICA | 4 | 4 | 3 |
| V03 | ACTIVA | ACTIVA | ACTIVA | 3 | 3 | 2 |
| V04 | ACTIVA | ACTIVA | ACTIVA | 2 | 2 | 4 |
| V05 | ACTIVA | ACTIVA | ACTIVA | 1 | 1 | 1 |
| V06 | CRITICA | CRITICA | CRITICA | 5 | 5 | 5 |
| V07 | FRONTERA | FRONTERA | FRONTERA | 8 | 8 | 6 |
| V08 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA | 15 | 15 | 15 |
| V09 | REACTIVA | REACTIVA | REACTIVA | 12 | 11 | 9 |
| V10 | FRONTERA | AUTONOMA_RELATIVA | FRONTERA | 9 | 12 | 10 |
| V11 | FRONTERA | FRONTERA | REACTIVA | 10 | 9 | 12 |
| V12 | FRONTERA | FRONTERA | FRONTERA | 11 | 10 | 11 |
| V13 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA | 14 | 14 | 14 |
| V14 | REACTIVA | REACTIVA | REACTIVA | 13 | 13 | 13 |
| V15 | CRITICA | CRITICA | CRITICA | 6 | 7 | 7 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


Cambian de clase directa con la recodificación: V10, V11. Los cinco primeros rangos de influencia indirecta (V05, V04, V03, V02, V06 en la codificación base) forman el mismo conjunto en las tres codificaciones. En [0,1,2,4] se permutan V02, V03 y V04.

**Perturbación de un enlace a la vez sobre los dominios admisibles.** Se evaluaron 87 cambios de un solo valor dentro del dominio admisible de cada dirección incierta. De ellos, 37 cambian la clase directa de alguna variable y 12 cambian la clase indirecta. Además, 10 alteran las tres primeras posiciones de influencia indirecta. El mayor desplazamiento de rango es 4,5 en el plano directo y 4 en el indirecto. No se asignan probabilidades a estos cambios.


La {T:i046} reúne los datos de «Perturbación de un enlace a la vez sobre los dominios admisibles».

:::TABLA i046 | Perturbación de un enlace a la vez sobre los dominios admisibles
| Enlace | Valor base → alterno | Clases directas que cambian | Clases indirectas que cambian | Desplazamiento máx. directo/indirecto | Altera top 3 indirecto |
| --- | --- | --- | --- | --- | --- |
| V05→V02 | 3 → 2 | V02 | — | 2 / 4 | Sí |
| V04→V01 | 2 → 1 | V12, V13 | — | 2 / 3 | Sí |
| V04→V02 | 2 → 1 | V02 | — | 2 / 3 | Sí |
| V04→V06 | 1 → 0 | — | — | 2 / 3 | Sí |
| V03→V01 | 1 → 0 | V03, V12, V13 | — | 2 / 2 | Sí |
| V03→V02 | 1 → 0 | V02, V03 | — | 2 / 2 | Sí |
| V03→V06 | 3 → 2 | V03 | — | 2 / 2 | Sí |
| V03→V09 | 1 → 0 | V03 | — | 2 / 2 | Sí |
| V04→V09 | 1 → 0 | — | — | 2 / 2 | Sí |
| V02→V11 | 2 → 3 | — | — | 2 / 1 | Sí |
| V15→V07 | 1 → 0 | — | V05, V07, V15 | 2 / 4 | No |
| V09→V10 | 3 → 0 | — | V05, V10 | 3,5 / 3,5 | No |
| V15→V05 | 1 → 0 | — | V15 | 2 / 4 | No |
| V07→V06 | 3 → 2 | V07 | V10 | 2 / 4 | No |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


Los enlaces de mayor efecto son V05→V02, V04→V01, V04→V02, V04→V06, V03→V01, V03→V02, V03→V06, V03→V09, V04→V09 y V02→V11. Todos tienen origen en variables físicas. Los enlaces que mueven las clases indirectas de las variables de gobernanza son V15→V07, V15→V05, V09→V10 y V07→V06. La revisión prioritaria de fichas debe empezar por esos enlaces.

**Ciclos.** S2 tiene 144 ciclos simples de hasta siete aristas. 140 contienen V15; 94 contienen V10; 84 contienen V06; 84 contienen V09. Los ciclos de dos aristas son V06↔V07, V09↔V15, V11↔V12 y V14↔V15. La concentración en V15 resulta de las cinco aristas que salen de V15 y de las cinco que le llegan. Depende de esas fichas y de sus dominios admisibles.

**Rutas explicativas.** La tabla lista las tres rutas simples de mayor producto de pesos entre pares seleccionados. El producto es un índice de intensidad ordinal y no un efecto estimado.


La {T:i047} reúne los datos de «Rutas explicativas».

:::TABLA i047 | Rutas explicativas
| Origen→Destino | Rutas simples más intensas (hasta cinco aristas; producto de pesos) |
| --- | --- |
| V05->V14 | V05 → V02 → V06 → V11 → V12 → V15 → V14 (216); V05 → V02 → V06 → V09 → V10 → V11 → V14 (108); V05 → V01 → V06 → V11 → V12 → V15 → V14 (96) |
| V05->V15 | V05 → V02 → V06 → V11 → V12 → V15 (108); V05 → V02 → V06 → V11 → V14 → V15 (108); V05 → V02 → V06 → V11 → V12 → V14 → V15 (108) |
| V03->V11 | V03 → V06 → V12 → V15 → V09 → V10 → V11 (144); V03 → V06 → V12 → V15 → V05 → V01 → V11 (72); V03 → V06 → V12 → V15 → V05 → V02 → V11 (72) |
| V04->V11 | V04 → V02 → V06 → V15 → V09 → V10 → V11 (72); V04 → V01 → V06 → V15 → V09 → V10 → V11 (48); V04 → V01 → V14 → V15 → V09 → V10 → V11 (48) |
| V07->V14 | V07 → V06 → V11 → V12 → V15 → V14 (72); V07 → V06 → V15 → V09 → V10 → V11 → V14 (72); V07 → V06 → V12 → V15 → V10 → V11 → V14 (48) |
| V07->V15 | V07 → V06 → V09 → V10 → V11 → V12 → V15 (72); V07 → V06 → V09 → V10 → V11 → V14 → V15 (72); V07 → V06 → V11 → V12 → V15 (36) |
| V15->V06 | V15 → V05 → V02 → V06 (9); V15 → V05 → V02 → V09 → V10 → V06 (9); V15 → V09 → V10 → V06 (6) |
| V15->V11 | V15 → V05 → V02 → V06 → V09 → V10 → V11 (54); V15 → V05 → V02 → V06 → V11 (27); V15 → V05 → V02 → V09 → V10 → V06 → V11 (27) |
| V09->V14 | V09 → V10 → V06 → V11 → V12 → V15 → V14 (72); V09 → V15 → V05 → V02 → V06 → V11 → V14 (54); V09 → V10 → V11 → V12 → V15 → V14 (48) |
| V10->V15 | V10 → V06 → V11 → V12 → V15 (12); V10 → V06 → V11 → V14 → V15 (12); V10 → V06 → V11 → V12 → V14 → V15 (12) |
| V02->V15 | V02 → V06 → V09 → V10 → V11 → V12 → V15 (72); V02 → V06 → V09 → V10 → V11 → V14 → V15 (72); V02 → V06 → V11 → V12 → V15 (36) |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


La ruta V05 → V02 → V06 → V11 → V12 → V15 explica por qué la remoción de escombros encabeza la influencia indirecta. Alcanza el resultado institucional por la cadena de medición y de índice. La ruta V15 → V05 → V02 → V06 muestra el único camino por el que el uso institucional retroalimenta la fuente.

**Coherencia de decisiones dependientes.** Este análisis no selecciona alternativa ni adjudica pesos. Aporta tres insumos a F4.4-MDR y 4.5: (i) V06 es crítica en los cinco escenarios y funciona como cuello de botella estructural en la hipótesis HIE; (ii) V07 no es una palanca independiente máxima en S2 (clase FRONTERA, rango indirecto 8); (iii) V15 concentra la retroalimentación. Ninguno de estos insumos eleva un estatuto HIE a IDC ni a EST.

**Registro de decisión ND-09 (prominencia directa e indirecta).**




La {T:i048} reúne los datos de «Registro de decisión GENESIS: ND-09 Reconciliación entre prominencia directa e indirecta».

:::TABLA i048 | Registro de decisión GENESIS: ND-09 Reconciliación entre prominencia directa e indirecta
| Campo | Contenido |
| --- | --- |
| NODO | ND-09 Reconciliación entre prominencia directa e indirecta |
| CLASE | MAYOR. Determina cuál lectura sustenta las hipótesis de intervención. |
| DECISION | Conservar ambas lecturas. No sustituir la directa por la indirecta. Reconciliar variable por variable y tratar las diferencias como sensibilidad al horizonte de recorridos. |
| DECIDE | Equipo formulador (rol POR_IDENTIFICAR). La propuesta proviene de la instancia analítica. |
| EXCLUYE | Presentar la clase indirecta como rol causal. Elegir la lectura que favorece a una variable. Interpretar el rango como importancia. |
| NODOS_BLANCOS | 15: clase directa e indirecta de S2 comparadas para las quince variables; coinciden V03, V04, V05, V06, V07, V08, V09, V13, V14, V15; cambian V01 de FRONTERA a ACTIVA; V02 de CRITICA a ACTIVA; V10 de FRONTERA a REACTIVA; V11 de FRONTERA a REACTIVA; V12 de FRONTERA a REACTIVA; el rango de dependencia de V06 pasa de 1 a 7 y el de V15 de 5 a 1 (F4.4.12). |
| NODOS_GRISES | 1: la dependencia indirecta de V15 refleja su presencia en ciclos y depende de cinco fichas de salida con confianza baja o media. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 1 (los recorridos miden longitud de caminos y no efectos; el límite se declara) |
| PATRON_DOMINANTE | PR-06 (patrón emergente): la posición indirecta depende de los ciclos del escenario y de k. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: Sí. |
| ESCENA_SIMULABLE | Un analista de la IES recalcula cada trimestre ambas lecturas con las fichas vigentes y registra las variables que cambian de clase. El equipo formulador decide con ese registro si revisa las hipótesis de intervención. |
| EVIDENCIA_JH_A | Registro trimestral de cambios de clase firmado por el analista (artefacto por producir; no existe aún). |
| EVIDENCIA_JH_B | Tabla de rangos indirectos por escenario, potencias hasta k = 10 y estabilidad observada (F4.4.11 a F4.4.13). |
| CERCA_CONCEPTUAL | Los recorridos no son tiempo ni efecto causal. La estabilidad observada no prueba convergencia. |
| ESTATUTO_CAUSAL | HIE. |
| VEREDICTO | Lectura reconciliada: V06 permanece crítica en ambas lecturas; cinco variables cambian de clase y su rol queda condicionado. |
| RAZON_DEL_DESCARTE | Se descarta sustituir la lectura directa por la indirecta, porque la segunda depende de ciclos con fichas de confianza baja. |
| RESULTADO | CIERRA con vacíos declarados (ratificación de fichas). |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


### F4.4.14 Interpretación estructural, límites, brechas, evidencias de ejecución y checkpoint

**Interpretación estructural.** Las afirmaciones siguientes valen para el escenario de trabajo S2 y sus envolventes. Son hipótesis de influencia estructural (estatuto HIE). Ninguna se eleva a efecto causal identificado ni estimado.

1. S2 contiene 48 aristas (7 de peso 3, 16 de peso 2 y 25 de peso 1) y suma 78 puntos. Frente a S0 (22 aristas, 53 puntos) y S1 (32 aristas, 67 puntos), S2 agrega 26 aristas que S0 codifica como cero. No elimina ninguna arista de S0. Modifica el valor de 7 aristas heredadas. Todos esos cambios tienen mecanismo declarado en las fichas. La densidad (22,9 %) no fue un objetivo; resulta de los juicios.

2. V06 (error de medición) queda en el cuadrante crítico en los cinco escenarios. Recibe de V01 a V04, V07 y V10 y transmite a V07, V09, V11, V12 y V15. En la hipótesis HIE, el error de medición actúa como cuello de botella estructural entre el entorno físico y las variables de decisión. El resultado es coherente con la selección de V06 como problema central en E3, pero se obtiene con otra matriz.

3. V07 (frecuencia de calibración) cae en FRONTERA en S2 (influencia 5, igual a la mediana) y ocupa el rango 8 de influencia indirecta. La afirmación previa de que V07 es la palanca independiente máxima no se sostiene con S2. V07→V06 recibe 3 con dominio {2,3}: si el valor fuera 2, V07 pasa a AUTONOMA_RELATIVA (influencia 4) y cambia la clase indirecta de V10.

4. V08 (latencia) ocupa el último lugar de influencia indirecta (rango 15) en S2 y es autónoma relativa. Su único vínculo de salida con peso positivo es V08→V13 (2). Los vínculos V08→V06 y V07→V08 son 0 y 1 con dominios amplios. La estructura de S2 no respalda que la latencia sea un polo estructural de la contradicción raíz CTR-01. Esa conclusión depende de V08→V06 y de la definición de V08; no es concluyente.

5. V15 (adopción institucional) es crítica en S2 y S4, FRONTERA en S1 y S3 y reactiva en S0, donde no tiene salidas. Es la variable con mayor dependencia indirecta (rango 1) y participa en 140 de 144 ciclos simples. La retroalimentación institucional exige cinco fichas de salida de V15, todas con confianza baja o media y dominios que incluyen valores menores. La conclusión sobre el papel de V15 es sensible a esas fichas.

6. V03, V04 y V05 encabezan la influencia indirecta. V03 y V04 no reciben influencia; V05 recibe una sola arista (V15→V05). Son fuentes de recorridos y no palancas de intervención del proyecto, salvo V05 mediante decisiones institucionales.

7. S0 (grafo acíclico) se extingue en A^7. El documento E3-P05 afirma dos cosas sobre esa extinción. Afirma haber probado matemáticamente que la arquitectura modelada es un grafo dirigido acíclico. Dice que valida «la linealidad termodinámica del problema de escombros». La extinción es una propiedad de las 22 aristas codificadas, que omiten entradas como V01→V11 y V02→V11 y retroalimentaciones como V15→V09. No demuestra linealidad del sistema.

**Límites.** (a) Los 210 juicios son PROPUESTOS por una instancia analítica y ninguno fue ratificado. (b) Las fuentes primarias no fueron leídas; 41 de 48 direcciones no nulas citan al menos un localizador secundario o interno. (c) La autorrevisión de las fichas no equivale a un panel independiente. (d) Los dominios admisibles expresan incertidumbre ordinal, no probabilidad. (e) La estabilidad observada de rangos no demuestra convergencia dinámica. (f) Las posiciones dependen de la definición de las variables y de tres ambigüedades del diccionario.

**Brechas específicas de 4.4 y ruta de resolución (¿Qué se me escapa?).**


La {T:i049} reúne los datos de «Brechas específicas de 4.4 y ruta de resolución (¿Qué se me escapa?)».

:::TABLA i049 | Brechas específicas de 4.4 y ruta de resolución (¿Qué se me escapa?)
| Brecha | Efecto sobre la decisión | Ruta de resolución | Tenedor |
| --- | --- | --- | --- |
| Panel humano ausente: ninguna ficha fue adjudicada | Impide certificar la MID y toda decisión que dependa de ella | Sesión de adjudicación con acta, comenzando por los 14 enlaces de mayor efecto (F4.4.13) | POR_IDENTIFICAR (equipo formulador) |
| Fuentes primarias no leídas | El respaldo de 41 direcciones es secundario | Leer Suresh 2025, Bang 2026, Ayala-Parra 2026 y Tavella 2026 con localizador de página | Analista documental |
| Variables omitidas del modelo: distancia a la referencia, edad del sensor, episodio de humo, precipitación | El informe_FINAL las trata como determinantes del error; su ausencia puede inflar la influencia de V03 y V07 | Evaluar ampliar a n = 19 o reemplazar variables débiles; rehacer 4.4 | Equipo formulador |
| Ambigüedades V-DIC-01, V-DIC-02 y V-DIC-03 | Cambian V06→V01, V09→V10 y V10→V06 | Aclarar en el diccionario antes de ratificar | Equipo formulador |
| Fórmula local del AQHI (V-AQHI-01) | V01→V11 y V02→V11 dependen de ella | Definir la fórmula y su validación (decisión D-05 del informe_FINAL) | Equipo formulador y autoridad de salud |
| Sin términos de referencia | No se verifica la tipología ni el horizonte | Aportar los TdR de la convocatoria | Entidad ejecutora (supuesta) |
| Exportación XLSX oficial no ejecutada | Falta el libro estándar del motor | Disponer de artifact_tool o aceptar los libros derivados de la plantilla | Usuario |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Evidencias de ejecución.**


La {T:i050} reúne los datos de «Evidencias de ejecución».

:::TABLA i050 | Evidencias de ejecución
| Control | Resultado | Alcance |
| --- | --- | --- |
| SHA-256 de 12 programas extraídos del metaprompt (11 PROGRAMA o validador, más arboles_mdr_svg.py) | 12 de 12 coinciden con la huella declarada | HASH_COMPROBADO; arboles_mdr_svg.py coincide tras retirar el primer salto de línea, como indica GEN-MDR-QA-06 |
| genesis_paritario_vm.py con 105 fichas, 5 escenarios, seed 20261011, kmax 10, ventana 3, corte mediana | Ejecutado; 0 errores de ficha | CÁLCULO EJECUTADO |
| Segunda implementación: plantilla XLSX del usuario recalculada con LibreOffice | A¹ a A⁶ idénticas al motor en S0, S1 y S2 | Verificación aritmética de seis potencias |
| Cinco permutaciones simultáneas de filas y columnas | 5 de 5 invariantes | Invarianza matemática |
| Perturbación de un enlace | 87 cambios evaluados | Sensibilidad ordinal, no probabilística |
| Control de alcance | Ver SECCION_4_4_scope_guard.json | Identidad, orden y encabezados; no suficiencia semántica |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Artefactos entregados de 4.4.**


La {T:i051} reúne los datos de «Artefactos entregados de 4.4».

:::TABLA i051 | Artefactos entregados de 4.4
| Archivo | Contenido |
| --- | --- |
| SECCION_4_4_SGR_CONV56_AIRE.md | Sección 4.4 con las 14 piezas (este archivo) |
| FICHAS_PARITARIAS.json y .csv | 105 fichas, 210 direcciones, esquema GENESIS_FICHA_PARITARIA_3_0 |
| RESULTADOS.json | Resultados completos del motor por escenario, con potencias, rangos y contraste |
| MID_FORMAL.csv, MID_<escenario>.csv | Matriz formal y matrices de cada escenario con TA y TP |
| potencias/<escenario>_A<k>.csv | Potencias exactas de cada escenario (S0: 6; S1, S2, S3, S4: 10 cada una) |
| REGISTRO_DIRECCIONES.csv, PLAN_PARITARIO.csv | Registro de 210 direcciones por escenario y orden de ejecución de los 105 pares |
| VESTER_<escenario>.svg, MICMAC_<escenario>.svg | Planos directo e indirecto editables, uno por escenario |
| SENSIBILIDAD_ORDINAL.json | Codificaciones [0,1,2,3], [0,1,3,5] y [0,1,2,4] por escenario |
| ANALISIS_COMPLEMENTARIO.json, RUTAS_Y_CICLOS.json | Diferencias, perturbación de un enlace, permutaciones, rutas y ciclos |
| REVISION_SOLAPAMIENTO.csv | 105 veredictos de solapamiento |
| xlsx/Vester_MICMAC_S2_trabajo_propuesto.xlsx (y S1, S0) | Plantilla del usuario con la matriz de cada escenario; Excel calcula al abrir. XLSX oficial del motor: XLSX_PENDIENTE_POR_DEPENDENCIA |
| CHECKPOINT_MOTOR.json y SECCION_4_4_SALIDA_CRUDA_DEL_MOTOR.md | Salida cruda del motor, conservada para auditoría; no sustituye esta sección |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4.


**Checkpoint de la sección 4.4.**

```json
{
 "ntc_version": "1.1",
 "estacion": "E4",
 "version_estacion": "36.10 RC2 / VM-PAR3-MDR3-CONT1",
 "tarea": "Seccion 4.4 Vester y MICMAC paritario",
 "estado": "BORRADOR_CON_VACIOS",
 "alcance_completado": "F4.4.1 a F4.4.14 con 105 fichas, 5 escenarios y potencias hasta k=10",
 "fuentes": [
  "F-INF",
  "F-E3"
 ],
 "decisiones": [],
 "vacios": [
  "V-DIC-01",
  "V-DIC-02",
  "V-DIC-03",
  "V-AQHI-01",
  "V-LLUVIA-01",
  "V-VIENTO-01",
  "RATIFICACION_PENDIENTE"
 ],
 "pendientes": [
  "Adjudicacion documentada de las fichas",
  "Lectura de fuentes primarias",
  "XLSX oficial por dependencia"
 ],
 "siguiente_accion": "Ejecutar F4.4-MDR dentro del alcance autorizado",
 "artefactos": [
  "SECCION_4_4_SGR_CONV56_AIRE.md",
  "FICHAS_PARITARIAS.json y .csv",
  "RESULTADOS.json",
  "MID_FORMAL.csv, MID_<escenario>.csv",
  "potencias/<escenario>_A<k>.csv",
  "REGISTRO_DIRECCIONES.csv, PLAN_PARITARIO.csv",
  "VESTER_<escenario>.svg, MICMAC_<escenario>.svg",
  "SENSIBILIDAD_ORDINAL.json",
  "ANALISIS_COMPLEMENTARIO.json, RUTAS_Y_CICLOS.json",
  "REVISION_SOLAPAMIENTO.csv",
  "xlsx/Vester_MICMAC_S2_trabajo_propuesto.xlsx (y S1, S0)",
  "CHECKPOINT_MOTOR.json y SECCION_4_4_SALIDA_CRUDA_DEL_MOTOR.md"
 ],
 "verificacion": {
  "calculo": "EJECUTADO",
  "fichas": {
   "fichas_recibidas": 105,
   "fichas_bidireccionales_validas": 105,
   "fichas_con_justificacion_declarada": 105,
   "fichas_con_dos_valores_propuestos": 105,
   "fichas_con_adjudicacion_documentada": 0,
   "direcciones_recibidas_unicas": 210,
   "direcciones_con_justificacion_declarada": 210,
   "direcciones_con_valor_propuesto": 210,
   "direcciones_con_adjudicacion_documentada": 0,
   "fichas_semanticamente_verificadas": null
  },
  "ratificacion": "PENDIENTE",
  "next_section_authorized_by_this_piece": false
 }
}
```

**Alcance de esta pieza.** La sección F4.4 termina aquí. Esta sección no autoriza por sí sola otra sección; la cadena 4.3, 4.4, F4.4-MDR y 4.5 se ejecuta bajo la autorización de la corrida completa.


## F4.4-MDR Metodología integrada de decisión y resolución

Esta sección aplica la metodología integrada de decisión y resolución al fenómeno de la vigilancia de material particulado en sitios de remoción de escombros. Se ejecuta en modo estándar, con perfil de proyecto de ciencia, tecnología e innovación. Las catorce piezas siguen este orden: síntesis, árboles, nueve análisis por fases, premortem y escenarios, valor y vacíos, y referencias. Utiliza los resultados de 4.3 y 4.4 sin modificarlos. Los departamentos y la alianza son SUPUESTO por instrucción del usuario. Los términos de referencia de la convocatoria no fueron aportados. El expediente técnico (fichas, métricas, señales, cálculos y pruebas) se entrega en archivos separados.

### F4.4-MDR.1 Síntesis decisional

**Decisión recomendada (condicionada).** El análisis recomienda la estrategia R4: desplegar la red por tramos, con un piloto de contraste y custodia distribuida por componente. No recomienda mantener R3 (transferencia a las alcaldías en el mes 25) como diseño base. Tampoco recomienda R0 (sin intervención). La recomendación es condicional: depende de cuatro supuestos críticos (SC-1 a SC-4) y de tres insumos ausentes. Los insumos ausentes son los términos de referencia, la ratificación de las fichas de 4.4 y la evidencia de capacidad de los custodios.

**Calificador.** CONDICIONALMENTE. La recomendación se apoya en juicios estructurales de influencia (estatuto HIE) y en supuestos declarados. El árbol de decisión es cualitativo porque ninguna probabilidad ni utilidad tiene fuente. Por eso el valor esperado es NO_CALCULABLE y el árbol no marca una rama elegida.

**Teoría del cambio en una oración.** Si la corrección local reduce el error verificado y las autoridades adoptan los umbrales, las alertas protegen a operarios y comunidades.

**Arquitectura de sostenibilidad.** La solución se diseña con la premisa de que ninguna entidad pública puede sostenerla sola al cierre. Cada componente recibe un custodio por tramos, con una cláusula de apertura si ninguno demuestra capacidad. El costo total de sostenimiento y el índice de capacidad de absorción son NO_CALCULABLE por falta de insumos. El portafolio que declara el expediente E3 concentra 63,2 % en una fuente y arroja un índice HHI de 0,472 en el año 1. Ambas cifras superan las convenciones locales PROPUESTAS (50 % y 0,40).

**Principal riesgo.** La adopción institucional carece de evidencia. La variable V15 participa en 140 de 144 ciclos simples de S2 y tres de sus cinco fichas de salida tienen confianza baja. El expediente E3 asigna a las alcaldías la operación desde el mes 25 sin compromiso presupuestal firmado (E3-P17).

**Valor estratégico.** Permite decidir, antes de la compra masiva, si el diseño se ejecuta por tramos con evidencia o en bloque con un receptor supuesto. La utilidad es potencial: ningún resultado observado respalda todavía la recomendación.

**Estado de la entrega.** Borrador con vacíos. El expediente separado registra las nueve fichas, las métricas, las señales y las pruebas.

### F4.4-MDR.2 Árbol de decisión A-DEC y árbol de teoría del cambio A-TDC

Los dos árboles se emiten antes del análisis por fases. Comparten los códigos SC-1 a SC-4. Cada árbol incluye su JSON canónico, el SVG editable y su alternativa textual. El JSON regenera el SVG con la herramienta de referencia.

**Árbol A-DEC (decisión bajo incertidumbre, modalidad cualitativa).** El árbol compara tres estrategias. Cada una de las dos estrategias de despliegue enfrenta cuatro supuestos en cadena. El orden temporal es: medición (SC-1) en el Hito 2, energía y enlace (SC-2), uso institucional (SC-3) y custodia (SC-4). El árbol modela un camino crítico: la falla de un supuesto interrumpe la cadena. No modela la dependencia entre supuestos.

El JSON canónico de A-DEC se reproduce sin cambios en el Anexo L (L.1).


La {F:adec} reproduce «A-DEC: estrategia de resolución y custodia posproyecto».

:::FIGURA adec | A-DEC: estrategia de resolución y custodia posproyecto | Nota. Elaboración propia con ARBOL_1_SGR_CONV56_AIRE.json. Árbol de decisión cualitativo; las probabilidades y las utilidades no se declaran por falta de fuente.

**Alternativa textual de A-DEC.**

- Árbol 1 · Decisión bajo incertidumbre · rol A-DEC
- Pregunta: ¿Qué estrategia adopta el proyecto: no intervenir, transferir a un receptor público único o desplegar por tramos con custodia distribuida?
- Naturaleza: PROPUESTO

- Valor esperado en la raíz: NO_CALCULABLE


La {T:i052} reúne los datos de «Árbol A-DEC (decisión bajo incertidumbre, modalidad cualitativa)».

:::TABLA i052 | Árbol A-DEC (decisión bajo incertidumbre, modalidad cualitativa)
| Nodo | Tipo | Etiqueta | Supuesto | VE o valor | Umbral |
|---|---|---|---|---|---|
| D1 | DECISION | Estrategia de resolución y custodia |  | NO_CALCULABLE | — |
| A1 | AZAR | Medición: la corrección local reduce el error frente a la lectura sin corrección dinámica | SC-1 | NO_CALCULABLE | — |
| B1 | AZAR | Medición: la corrección local reduce el error frente a la lectura sin corrección dinámica | SC-1 | NO_CALCULABLE | — |
| C0 | TERMINAL | Se mantiene la línea base: sensores aislados sin corrección dinámica ni custodia |  | NO_CALCULABLE | — |
| A2 | AZAR | Energía y enlace: nodos activos suficientes bajo maquinaria y humedad | SC-2 | NO_CALCULABLE | — |
| AT1 | TERMINAL | Expansión detenida tras el piloto; inversión limitada al primer tramo; conocimiento negativo documentado |  | NO_CALCULABLE | — |
| B2 | AZAR | Energía y enlace: nodos activos suficientes bajo maquinaria y humedad | SC-2 | NO_CALCULABLE | — |
| BT1 | TERMINAL | Inversión completa comprometida sin evidencia de reducción del error; red desplegada |  | NO_CALCULABLE | — |
| A3 | AZAR | Uso: autoridades adoptan umbrales de alerta validados en sus protocolos | SC-3 | NO_CALCULABLE | — |
| AT2 | TERMINAL | Error reducido y verificado, con cobertura insuficiente; rediseño del enlace o la energía antes del segundo tramo |  | NO_CALCULABLE | — |
| B3 | AZAR | Uso: autoridades adoptan umbrales de alerta validados en sus protocolos | SC-3 | NO_CALCULABLE | — |
| BT2 | TERMINAL | Red parcialmente inoperante con la inversión completa realizada |  | NO_CALCULABLE | — |
| A4 | AZAR | Custodia: al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo | SC-4 | NO_CALCULABLE | — |
| AT3 | TERMINAL | Mediciones verificadas sin uso institucional; tramo siguiente condicionado a la adopción de umbrales |  | NO_CALCULABLE | — |
| B4 | AZAR | Custodia: al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo | SC-4 | NO_CALCULABLE | — |
| BT3 | TERMINAL | Mediciones sin uso institucional con la inversión completa realizada |  | NO_CALCULABLE | — |
| AT5 | TERMINAL | Servicio de vigilancia sostenido con custodia distribuida; protección contribuida con otros actores |  | NO_CALCULABLE | — |
| AT4 | TERMINAL | Uso institucional sin custodio demostrado; cláusula de apertura y servicio mínimo |  | NO_CALCULABLE | — |
| BT5 | TERMINAL | Servicio continuado con receptor público único; protección contribuida con otros actores |  | NO_CALCULABLE | — |
| BT4 | TERMINAL | Orfandad después del mes 24: la red queda sin receptor que la opere |  | NO_CALCULABLE | — |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Supuestos críticos para la decisión (distancia al umbral ≤ 0,15, regla PROPUESTA): ninguno.

- Errores de coherencia: ninguno detectado.
- Comprobaciones del SVG original del motor (la figura del documento es una versión redibujada con la plantilla visual): xml_bien_formado=True, viewbox=True, title=True, desc_no_vacio=True, rol_declarado=True, tipo_declarado=True, colores_fuera_de_paleta=[], sin_script_enlace_imagen=True, sin_transformaciones=True, ids_unicos=True, tamano_minimo_9_5=True

**Nota sobre la criticidad de los supuestos.** La frase «ninguno» de la alternativa textual indica que el generador no calculó umbrales, porque faltan probabilidades. La criticidad de SC-1 a SC-4 para la decisión es NO_CALCULABLE. La regla de distancia 0,15 queda sin aplicar.

**Árbol A-TDC (teoría del cambio).** El árbol tiene once resultados en cuatro niveles. El techo de rendición de cuentas separa los resultados bajo control del proyecto de aquellos a los que solo contribuye. Los supuestos SC-1 a SC-4 rotulan las flechas críticas y remiten a los nodos A1 a A4 y B1 a B4 de A-DEC.

El JSON canónico de A-TDC se reproduce sin cambios en el Anexo L (L.2).


La {F:atdc} reproduce «A-TDC: teoría del cambio de la red de vigilancia con custodia distribuida».

:::FIGURA atdc | A-TDC: teoría del cambio de la red de vigilancia con custodia distribuida | Nota. Elaboración propia con ARBOL_4_SGR_CONV56_AIRE.json. Cada nivel superior exige el cumplimiento del nivel inferior.

**Alternativa textual de A-TDC.**

- Árbol 4 · Teoría del cambio · rol A-TDC
- Pregunta: ¿Qué cadena causal lleva de los productos del proyecto a la protección de operarios y comunidades, y dónde termina la rendición de cuentas?
- Naturaleza: PROPUESTO


La {T:i053} reúne los datos de «Árbol A-TDC (teoría del cambio)».

:::TABLA i053 | Árbol A-TDC (teoría del cambio)
| Nivel | Nodo | Texto |
|---|---|---|
| Productos | P1 | Red de nodos con corrección local desplegada y repuestos disponibles |
| Productos | P2 | Referencia gravimétrica, protocolo de calibración y sorteo semanal en operación |
| Productos | P3 | Gemelo digital y tablero con umbrales de alerta propuestos |
| Productos | P4 | Acuerdos de custodia por tramos y portafolio de financiación constituidos |
| Resultados inmediatos | R1 | Error de medición reducido y verificable frente a la referencia |
| Resultados inmediatos | R2 | Datos suficientes: nodos activos y latencia dentro de lo especificado |
| Resultados inmediatos | R3 | Fórmula local del índice y umbrales validados con la autoridad de salud |
| Resultados intermedios | I1 | Protocolos de gestión del riesgo y de salud incorporan las alertas |
| Resultados intermedios | I2 | Alertas oportunas con falsas alarmas dentro del umbral acordado |
| Resultados intermedios | I3 | Servicio operando con custodios después del mes 24 |
| Impacto | IM | Operarios y comunidades de los sitios de remoción protegidos por alertas basadas en mediciones verificadas |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Relaciones: P3 → R3 (SC-3); P1 → R2 (SC-2); P1 → R1 (SC-1); P2 → R1 (SC-1); P4 → I3 (SC-4); R3 → I1 (SC-3); R1 → I2; R2 → I2; I1 → IM (SC-3); I2 → IM; I3 → IM (SC-4); I1 → P4.

SC-1: SI los nodos con corrección local se comparan por sorteo semanal con la lectura sin corrección dinámica y con una referencia gravimétrica ENTONCES el error normalizado de los nodos corregidos resulta menor y la diferencia es detectable PORQUE la humedad y el sesgo por tamaño de partícula explican parte del error (V03→V06 = 3 en S2) y la corrección local los compensa antes de la transmisión (SUPUESTO).

SC-2: SI los nodos conservan energía y enlace intermitente bajo maquinaria, polvo y humedad ENTONCES el gemelo digital recibe datos suficientes para el mapa y el tablero PORQUE la transmisión por eventos reduce el consumo, los nodos averiados se reponen y la maquinaria destruye nodos con peso 2 (V05→V09) que el plan de repuestos absorbe (SUPUESTO).

SC-3: SI la autoridad de salud valida una fórmula local del índice y los umbrales, y los puestos de mando los incorporan en sus protocolos ENTONCES las alertas inducen acciones de protección y aumenta la población protegida PORQUE una alerta sin portador de decisión no modifica la conducta; en S2 V11→V14 y V13→V14 tienen peso 2 y son hipótesis de influencia (SUPUESTO).

SC-4: SI al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo de transferencia ENTONCES el servicio continúa después del mes 24 sin receptor público único PORQUE cada tramo exige presupuesto aprobado, personal designado y competencia jurídica documentada; sin ellos rige la cláusula de apertura (SUPUESTO).

Enfoque: TdC anidada: ejecutiva y por componente para dominio COMPLICADO en la medición y COMPLEJO en la adopción y la custodia.

- Errores de coherencia: ninguno detectado.
- Comprobaciones del SVG original del motor (la figura del documento es una versión redibujada con la plantilla visual): xml_bien_formado=True, viewbox=True, title=True, desc_no_vacio=True, rol_declarado=True, tipo_declarado=True, colores_fuera_de_paleta=[], sin_script_enlace_imagen=True, sin_transformaciones=True, ids_unicos=True, tamano_minimo_9_5=True

**Revisión visual.** Las figuras del documento se redibujaron con la plantilla visual del proyecto a partir de los mismos datos y se revisaron como imágenes. Los textos se leen completos y ningún nodo se superpone.

### F4.4-MDR.3 Construcción y dominio del fenómeno

Esta pieza fija qué fenómeno existe, quién lo construye y en qué dominio causal se ubica. Reutiliza el problema de 4.3 y 4.4. No lo sustituye por la solución preferida. Las fuentes se identifican con dos códigos: F-INF es el informe_FINAL de vigilancia tecnológica y F-E3 es el expediente Problematica_E3-P00.

**Delimitación del fenómeno.**


La {T:i054} reúne los datos de «Delimitación del fenómeno».

:::TABLA i054 | Delimitación del fenómeno
| Campo | Contenido | Naturaleza y verificación |
| --- | --- | --- |
| Fenómeno observado | En sitios de remoción de escombros posteriores al sismo, la medición de PM2,5 y PM10 con sensores de bajo costo carece de verificación frente a una referencia. | DECLARADO en F-E3 (E3-P00, E3-P01); NO_VERIFICADO |
| Unidad decisora | El equipo formulador diseña la propuesta. El financiador decide la asignación. Rol del equipo: POR_IDENTIFICAR. | SUPUESTO |
| Población afectada | Operarios de remoción y comunidades colindantes. Cifras: VACIO. F-E3 (Cap. 14.3) menciona 87 municipios y 80 funcionarios sin fuente. | VACIO; NO_VERIFICADO |
| Territorio | Caldas, Cundinamarca y Valle del Cauca. | SUPUESTO por instrucción del usuario |
| Periodo y horizonte | 24 meses de ejecución y 12 meses posproyecto: 36 meses. | PROPUESTO |
| Nivel de agregación | Nodo-semana en la medición. Municipio-mes en la adopción. | PROPUESTO |
| Síntoma | Lecturas con error no cuantificado en el territorio. La línea base de error normalizado (NMAE) es VACIO. F-E3 cita 45 % sin localizador y fija tres metas distintas: menos de 30 %, 15 % o menos y menos de 15 %. | DOCUMENTADO en F-E3; CONTRADICTORIO |
| Problema como estado observable | En los sitios de remoción no se dispone de mediciones de PM2,5 y PM10 verificadas frente a una referencia ni de alertas incorporadas en protocolos de decisión. | PROPUESTO; NO_VERIFICADO |
| Explicación propuesta | El error de medición (V06) actúa como cuello de botella estructural entre el entorno físico y las variables de decisión. | INFERIDO (HIE en 4.4); NO_VERIFICADO |
| Solución preferida | Arquitectura híbrida con corrección local (ALT-03 de F-E3) y gemelo digital. Se registra como hipótesis de intervención. | DECLARADO en F-E3; se examina en el argumento |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


El enunciado del problema describe un estado observable. La solución preferida figura aparte, como hipótesis. Ninguna observación disponible mide hoy el estado descrito: la línea base es un vacío.

**Construcción discursiva.** La tabla responde las cuatro preguntas de análisis del discurso de Bacchi (2009) y de Schön y Rein (1994).


La {T:i055} reúne los datos de «Construcción discursiva».

:::TABLA i055 | Construcción discursiva
| Pregunta | Respuesta | Fuente |
| --- | --- | --- |
| ¿Cómo se representa el problema? | Como una limitación técnica de medición y de comunicaciones: el error del sensor y el consumo de energía impiden calibrar en terreno. | F-E3, E3-P07 (contradicción raíz CTR-01) |
| ¿Qué supuestos sostienen esa representación? | (a) La causa principal es metrológica y energética. (b) La respuesta es tecnológica. (c) Las alcaldías adoptan y sostienen el tablero. | F-E3, E3-P09, E3-P17 y Cap. 14 |
| ¿Qué queda sin problematizar? | La emisión en la fuente, las acciones que activa la alerta, el umbral normativo aplicable y la responsabilidad de contratistas y administradoras de riesgos laborales (ARL). | Ausencia en F-E3; INFERIDO |
| ¿Qué efectos produce sobre los afectados? | Operarios y comunidades figuran como receptores de alertas. F-E3 no registra su participación en el diseño de los umbrales. | E3-P17 (matriz RACI); INFERIDO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Marcos rivales.** Se registran tres marcos con su portador. Ninguno cuenta con evidencia verificada en esta corrida.


La {T:i056} reúne los datos de «Marcos rivales».

:::TABLA i056 | Marcos rivales
| Marco rival | Portador | Qué sostendría | Fuente y estado |
| --- | --- | --- | --- |
| Control en la fuente y salud ocupacional | Autoridades laborales y ARL | El problema es la emisión de polvo en obra. La medición es secundaria. | Conocimiento externo; INFERIDO; NO_VERIFICADO |
| Gestión del riesgo de desastres como servicio | UNGRD y puestos de mando unificado | La alerta solo existe si un protocolo de mando la activa. | F-E3, E3-P17; INFERIDO |
| Metrología y acreditación | IDEAM | Solo un equipo acreditado como referencia sustenta una alerta oficial. | F-INF §6.5 (Tabla E3-30); INFERIDO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Núcleo normativo.** El núcleo normativo identifica derechos, mandatos y compromisos que delimitan las soluciones admisibles (Dunn, 2018). Los términos de referencia de la convocatoria no fueron aportados. Por esa razón, ninguna restricción se registra como no negociable con fuente normativa. Las restricciones siguientes se rotulan según su estado real.


La {T:i057} reúne los datos de «Núcleo normativo».

:::TABLA i057 | Núcleo normativo
| Restricción | Estado | Portador o fuente |
| --- | --- | --- |
| Tope de 14.000 millones de COP y reglas de elegibilidad | DECLARADO en F-E3 (cita TdR pp. 7-8 y 25); NO_VERIFICADO | Convocante; TdR no aportados |
| Protección de la salud y de un ambiente sano | CANDIDATO_A_VERIFICAR | Constitución Política, arts. 49 y 79 [conocimiento externo] |
| Competencia territorial en gestión del riesgo | CANDIDATO_A_VERIFICAR | Ley 1523 de 2012 [conocimiento externo] |
| Prioridad de la salud sobre la continuidad de obra | Preferencia del analista | Sin portador declarado |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Sistema apreciativo.** Los juicios se separan en juicios de realidad, de valor e instrumentales, cada uno con su portador (Vickers, 1965).


La {T:i058} reúne los datos de «Sistema apreciativo».

:::TABLA i058 | Sistema apreciativo
| Tipo de juicio | Juicio | Portador y fuente | Estado |
| --- | --- | --- | --- |
| Realidad | El error normalizado supera 45 % sin corrección. | F-E3, Paso 1 (F_REV_SISTEMATICA sin localizador) | DECLARADO; NO_VERIFICADO |
| Realidad | La humedad sesga los sensores ópticos. F-INF §8.3 reporta correlación de 0,73. F-E3 usa 0,48 en 3.15, 4.6 y ND-11. | F-INF §8.3; F-E3 | CONTRADICTORIO entre fuentes |
| Valor | Evitar paros de obra por falsas alarmas. | Constructoras (F-E3, Tabla E3-14.2, lucro cesante) | DECLARADO; NO_VERIFICADO |
| Valor | Proteger primero a operarios y comunidades cuando se supera un umbral. | Sin portador declarado | VACIO |
| Instrumental | La corrección local reduce el error sin degradar energía ni latencia. | Equipo formulador (E3-P09, OP-03) | SUPUESTO |
| Instrumental | Las alcaldías operan el tablero desde el mes 25. | F-E3, E3-P17 y CLM-06 | SUPUESTO; NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Los dos juicios de valor sobre una misma alerta divergen: la protección inmediata y la continuidad de obra. El análisis conserva ambos. No los reconcilia por decisión del analista.

**Estructura del problema (Simon, 1973).**


La {T:i059} reúne los datos de «Estructura del problema (Simon, 1973)».

:::TABLA i059 | Estructura del problema (Simon, 1973)
| Condición | Evaluación | Evidencia |
| --- | --- | --- |
| C1. Criterio explícito para aceptar una solución | NO CUMPLE | Las metas del error son contradictorias y los TdR faltan. |
| C2. Estados y variables pertinentes identificados | CUMPLE con reserva | Quince variables con diccionario; cuatro variables latentes omitidas (4.3). |
| C3. Acciones disponibles identificadas | CUMPLE | Cuatro alternativas catalogadas en E3-P10. |
| C4. Relación entre acciones y resultados conocida con precisión | NO CUMPLE | Las relaciones son hipótesis de influencia sin datos del territorio. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Dos condiciones se cumplen. La clasificación PROPUESTA es PARCIALMENTE_ESTRUCTURADO. No se activan los rasgos de problema perverso, porque ese paso exige una clasificación MAL_ESTRUCTURADO.

**Escala.** El fenómeno se clasifica como PROBLEMA_PUBLICO (INFERIDO), según la distinción de Mills (1959). Sus efectos exceden el entorno de cada operario y afectan a comunidades colindantes. El alcance poblacional es VACIO.

**Dominio causal.** La clasificación sigue los dominios de Snowden y Boone (2007) y la tipología de Glouberman y Zimmerman (2002). Se hace por partes. Ninguna parte queda en confusión.


La {T:i060} reúne los datos de «Dominio causal».

:::TABLA i060 | Dominio causal
| Parte | Dominio | Evidencia | Observación que cambiaría la clasificación |
| --- | --- | --- | --- |
| Medición con corrección local | COMPLICADO | La relación causa-efecto existe y requiere análisis experto. La corrección con la estación cercana elevó el R² de menos de 0,2 a 0,81 en un caso (F-INF §8.3). En S2, V03→V06 = 3. | Si el efecto de la corrección cambiara de signo entre sitios o semanas sin patrón, pasaría a COMPLEJO. |
| Adopción institucional y custodia | COMPLEJO | S2 contiene 144 ciclos simples y 140 incluyen V15. El juego de bien público de F-INF §6.5 sugiere patrones emergentes. | Si tres de tres departamentos ejecutaran una partida recurrente con protocolo firmado, pasaría a COMPLICADO. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


La naturaleza de ambas clasificaciones es INFERIDO y su verificación es NO_VERIFICADO. La fase aguda del sismo queda fuera del alcance. Por eso no se asigna el dominio caótico. La correspondencia con los cuatro tipos de problemas de Smalley (2018) sería INFERIDA y no se usa para clasificar.

**Vacíos de la construcción.**

- Línea base de error de medición en el territorio: VACIO. Tenedor: equipo formulador. Vía: medición con referencia en el Hito 1.
- Términos de referencia: VACIO. Tenedor: entidad ejecutora supuesta. Vía: aportar el documento.
- Fórmula local del índice AQHI y umbrales (V-AQHI-01): VACIO. Tenedor: autoridad de salud. Vía: validación local.
- Población expuesta y carga de morbilidad: VACIO. Sin variable de resultado en el modelo.

### F4.4-MDR.4 Entorno estructural e institucional

Esta pieza registra qué estructuras y reglas habilitan o bloquean cada estrategia. Sus restricciones de continuidad alimentan la teoría del cambio y la sostenibilidad. Todas las filas conservan fuente y naturaleza.

**Contexto estructural.**


La {T:i061} reúne los datos de «Contexto estructural».

:::TABLA i061 | Contexto estructural
| Condicionante | Tipo | Efecto | Fuente | Naturaleza y verificación |
| --- | --- | --- | --- | --- |
| Humedad relativa alta y polvo higroscópico | Físico | Limita: sesga la lectura óptica | S2, V03→V06 = 3; F-INF §8.3 | INFERIDO; PARCIALMENTE_VERIFICADO |
| Maquinaria de remoción | Físico | Limita: daña nodos (V05→V09 = 2) | S2, ficha V05→V09 | INFERIDO; NO_VERIFICADO |
| Infraestructura eléctrica y celular colapsada | Tecnológico | Limita: afecta energía y enlace | F-E3, 4.6 (cinco porqués) | DECLARADO; NO_VERIFICADO |
| Estaciones oficiales de referencia | Recurso | Posible recurso para calibrar. Cobertura en el territorio: VACIO. | F-INF §6.5 (IDEAM) | DECLARADO; NO_VERIFICADO |
| Tope de 14.000 millones de COP | Recurso | Limita el alcance. El desglose de F-E3 (Cap. 8) documenta 4.448,7 millones; faltan 9.551,3. | F-E3, Cap. 8 | CALCULADO sobre cifras de F-E3; NO_VERIFICADO |
| Capacidad técnica local | Recurso | Meta de certificar 80 funcionarios. Línea base: VACIO. | F-E3, Cap. 14.3 | DECLARADO; NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


El mismo expediente contiene una contradicción de arquitectura. El problema declara el colapso de la infraestructura celular y eléctrica. La alternativa ALT-03 transmite por enlace celular 4G con 100 tarjetas SIM (F-E3, Cap. 8, Tabla E3-8.3) y no presupuesta enlace alterno. Esa contradicción sustenta el supuesto SC-2.

**Reglas institucionales.** Las reglas formales citan su norma controlante y las informales su evidencia de práctica (North, 1990; Ostrom, 2005).


La {T:i062} reúne los datos de «Reglas institucionales».

:::TABLA i062 | Reglas institucionales
| Regla | Tipo | Conducta que permite, exige o prohíbe | Fuente | Estado |
| --- | --- | --- | --- | --- |
| Términos de referencia de la convocatoria | Formal | Define elegibilidad, tope, madurez y gobernanza exigida. | F-E3 cita secciones 10.4, 10.6 y 10.16 | VACIO: TdR no aportados |
| Normas de gestión del riesgo y salud ocupacional | Formal | Asignan la competencia sobre la respuesta a una alerta. | Conocimiento externo | CANDIDATO_A_VERIFICAR |
| Anualidad presupuestal y vigencias futuras | Formal | Condicionan el compromiso de gasto recurrente después del cierre. | Conocimiento externo | CANDIDATO_A_VERIFICAR |
| Propiedad industrial: diez solicitudes PCT designan a Colombia | Formal | Condiciona la libertad de operación. Tres plazos de fase nacional siguen abiertos. | F-INF §8.3 (D-01) | DOCUMENTADO en F-INF; NO_VERIFICADO |
| Compra de sensores sin plan de calibración | Informal | Los compradores operan sin calibrar mientras ninguna regla lo exija. | F-INF §6.5 (Juego 1) y §8.3 | DOCUMENTADO en F-INF; fuente primaria no leída |
| Equipos que terminan en bodegas municipales | Informal | Práctica citada sin evidencia local. | F-E3, Cap. 14.3 (Murad Pedraza et al., 2026, p. 15, como se citó en F-E3) | DECLARADO; NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Selectividad estratégica.** La selectividad estratégica examina qué estrategias favorece el diseño institucional vigente (Jessop, 2008; Hay, 2002). Pregunta de control: ¿qué estrategia tendría éxito aquí sin ser la mejor técnicamente? El diseño institucional supuesto favorece las estrategias de la columna izquierda y penaliza las de la derecha. La lectura es INFERIDA, porque los criterios de evaluación de la convocatoria no se aportaron.


La {T:i063} reúne los datos de «Selectividad estratégica».

:::TABLA i063 | Selectividad estratégica
| Estrategia favorecida | Mecanismo de la selectividad |
| --- | --- |
| Propuesta con novedad tecnológica visible (corrección local con aprendizaje automático embebido) | Los criterios de impacto y novedad pesan más que la verificación. F-E3 asigna 0,40 al impacto con peso SUPUESTO (E3-P14). |
| Entrega de activos físicos antes que servicios | Los rubros de inversión se costean con facilidad. El gasto recurrente exige compromisos posteriores (CANDIDATO_A_VERIFICAR). |
| Asignar la operación a entidades territoriales en la matriz de responsabilidades | La convocatoria exige evidencia de alianza y de gobernanza. Un rol asignado en papel satisface el formato (E3-P17). |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.



La {T:i064} reúne los datos de «Selectividad estratégica (continuación 1)».

:::TABLA i064 | Selectividad estratégica (continuación 1)
| Estrategia penalizada | Mecanismo de la selectividad |
| --- | --- |
| Piloto previo y compra por tramos | Retrasa el despliegue visible y exige reglas de decisión anticipadas. |
| Control de polvo en la fuente | Su gasto se percibe como obra y no como ciencia y tecnología. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Respuesta de diseño.** La estrategia R4 declara la selectividad en lugar de ocultarla. Presenta el piloto como producto de conocimiento con resultado verificable y los tramos como evidencia de alianza ejecutable.

**Restricciones de continuidad.**


La {T:i065} reúne los datos de «Restricciones de continuidad».

:::TABLA i065 | Restricciones de continuidad
| Restricción | Efecto sobre la continuidad | Fuente | Estado |
| --- | --- | --- | --- |
| Anualidad presupuestal territorial | La partida para operar desde el mes 25 debe existir en el plan operativo anual del año fiscal respectivo. | Conocimiento externo | CANDIDATO_A_VERIFICAR |
| Calendario electoral | Las elecciones territoriales siguientes ocurren en octubre de 2027 y la posesión en enero de 2028. Si la ejecución empieza en 2027, el cambio de administración cae dentro de los 24 meses. | Conocimiento externo | CANDIDATO_A_VERIFICAR |
| Rotación de personal | La capacidad certificada se pierde con la salida de funcionarios. | F-E3, Cap. 14.3 | DECLARADO; NO_VERIFICADO |
| Plazos de liquidación y cierre | La transferencia se concentra en el cierre (compuerta G3, mes 24). | F-E3, E3-P17 | DECLARADO |
| Vencimientos de propiedad industrial | Tres plazos de fase nacional pueden afectar la operación. | F-INF §8.3 (D-01) | DOCUMENTADO en F-INF |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Vacíos del entorno.**

- Cobertura de estaciones de referencia en los tres departamentos: VACIO. Tenedor: IDEAM y autoridades ambientales (POR_IDENTIFICAR).
- Reglas del instrumento sobre gasto recurrente y compras por tramos: VACIO hasta aportar los TdR.
- Calendario real de inicio de la ejecución: VACIO. Determina si el cambio de administración cae dentro del proyecto.

### F4.4-MDR.5 Actores, poder e interdependencia

Esta pieza identifica quién decide, quién veta y quién custodia, y anticipa la reacción de cada actor. La alianza es SUPUESTO por instrucción del usuario. Ningún actor firmó compromiso alguno.

**Identificación y lógica de acción.** La tipología distingue actores con veto (Tsebelis, 2002). La lógica de acción distingue las consecuencias y lo apropiado (March y Olsen, 1989).


La {T:i066} reúne los datos de «Identificación y lógica de acción».

:::TABLA i066 | Identificación y lógica de acción
| Actor | Tipo | Fuente de autoridad o interés | Lógica de acción |
| --- | --- | --- | --- |
| Convocante y órganos de decisión del Sistema General de Regalías | DECISOR; ACTOR_CON_VETO; FINANCIADOR | Aprueba la asignación y los términos (F-E3, E3-P15) | De lo apropiado: cumplimiento de los términos. INFERIDO |
| Institución de educación superior ejecutora | EJECUTOR; CUSTODIO_POTENCIAL | Responde por la ejecución ante el control fiscal (E3-P17) | De las consecuencias: no tiene recursos permanentes (E3-P17, §13). DECLARADO |
| Empresa tecnológica aliada | EJECUTOR; CUSTODIO_POTENCIAL | Responde por propiedad intelectual y código (E3-P17) | De las consecuencias: modelo de negocio. INFERIDO |
| Alcaldías de municipios con remoción | ACTOR_CON_VETO; CUSTODIO_POTENCIAL; AFECTADO | Responden legalmente por actuar sobre la alerta (E3-P17) | De las consecuencias: presupuesto y ciclo electoral. INFERIDO |
| Gobernaciones y unidades departamentales de gestión del riesgo | CUSTODIO_POTENCIAL | F-E3, Tabla E3-14.3 las nombra como receptoras | Sin evidencia: NO_EVALUADO |
| UNGRD y puestos de mando unificado | DECISOR operativo; usuario | Reciben información en E3-P17 | De lo apropiado: protocolos de mando. INFERIDO |
| IDEAM y autoridades ambientales | Referencia metrológica | F-INF §6.5 (punto focal de acreditación) | De lo apropiado: acreditación. INFERIDO |
| Secretarías de salud, ADRES y ARL | FINANCIADOR potencial; beneficiario del ahorro | F-E3, Tabla E3-14.2 | Sin evidencia: NO_EVALUADO |
| Constructoras y contratistas de remoción | AFECTADO; generador de la emisión; FINANCIADOR potencial | F-E3, Tabla E3-14.2 (lucro cesante) | De las consecuencias: evitar paros. INFERIDO |
| Operarios y comunidades colindantes | AFECTADO | Exposición a PM2,5 y PM10 | No registrada: VACIO |
| Proveedores de sensores | EJECUTOR indirecto | F-INF §6.5 | De las consecuencias. INFERIDO |
| Órganos de control fiscal | Control | E3-P17 | De lo apropiado. INFERIDO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Relevancia (poder, legitimidad y urgencia).** La relevancia combina poder, legitimidad y urgencia (Mitchell et al., 1997). La evaluación exige evidencia. Solo el convocante cuenta con evidencia directa de poder en los documentos. El resto se registra como NO_EVALUADO, con la evidencia que lo resolvería.


La {T:i067} reúne los datos de «Relevancia (poder, legitimidad y urgencia)».

:::TABLA i067 | Relevancia (poder, legitimidad y urgencia)
| Actor | Poder | Legitimidad | Urgencia | Evidencia que falta |
| --- | --- | --- | --- | --- |
| Convocante | ALTO (aprueba y fija términos; DECLARADO) | NO_EVALUADA | NO_EVALUADA | Términos de referencia |
| Alcaldías | NO_EVALUADO | NO_EVALUADA | NO_EVALUADA | Cartas de compromiso con partida y competencia |
| Constructoras | NO_EVALUADO | NO_EVALUADA | NO_EVALUADA | Contratos de obra y cláusulas ambientales |
| Operarios y comunidades | NO_EVALUADO | NO_EVALUADA | NO_EVALUADA | Línea base de exposición y consulta |
| IDEAM y autoridades ambientales | NO_EVALUADO | NO_EVALUADA | NO_EVALUADA | Convenio de referencia con estaciones |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Una constructora con poder de paralizar la obra y sin legitimidad sobre el umbral de alerta se registra como riesgo, no como aliada. La condición se evaluará cuando exista evidencia.

**Reacciones previstas (anticipación cualitativa).** Sin pagos monetarios especificables, las reacciones son anticipaciones cualitativas INFERIDAS.


La {T:i068} reúne los datos de «Reacciones previstas (anticipación cualitativa)».

:::TABLA i068 | Reacciones previstas (anticipación cualitativa)
| Actor | Reacción prevista ante R4 | Reacción prevista ante R3 |
| --- | --- | --- |
| Alcaldías | Aceptan tramos si reciben capacidad demostrada y no asumen costos antes de recibirla | Aceptan la designación en la matriz y pueden no presupuestar la operación |
| Institución ejecutora | Mantiene el servicio mínimo si la cláusula de apertura le permite liberar activos | Queda como responsable de hecho si ninguna alcaldía asume la operación |
| Constructoras | Cofinancian si la alerta reduce paros por falsas alarmas | Presionan por umbrales altos para evitar paros |
| Convocante | Evalúa el costo adicional del piloto frente al riesgo de abandono | Valida el formato de alianza sin evidencia de ejecución |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Interdependencia estratégica.** Un juego exige jugadores, estrategias y pagos especificados (Scharpf, 1997). El informe F-INF §6.5 modela como juego de bien público la decisión de calibrar y mantener sensores. Esta pieza adopta su estructura por analogía y la aplica a la custodia. Los jugadores son dos entidades territoriales candidatas. Las estrategias son asumir la operación y el mantenimiento (A) o no asumirlos (N).


La {T:i069} reúne los datos de «Interdependencia estratégica».

:::TABLA i069 | Interdependencia estratégica
| Pagos ordinales (4 mejor, 1 peor): fila, columna | Columna asume (A) | Columna no asume (N) |
| --- | --- | --- |
| Fila asume (A) | (3, 3) | (1, 4) |
| Fila no asume (N) | (4, 1) | (2, 2) |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


El equilibrio de Nash es (N, N): ninguna entidad asume la operación. Ese resultado es peor para ambas que (A, A). Supuestos declarados: pagos ordinales tomados de F-INF §6.5, juego de una sola ronda, información completa y sin transferencias. Naturaleza: INFERIDO. Verificación: NO_VERIFICADO.

**Implicación de diseño.** Una regla que condiciona cada tramo de transferencia a la capacidad demostrada cambia los pagos de N. Ese es el mecanismo de R4. R3 deja intacto el equilibrio (N, N) y por eso depende de un compromiso externo.

**Red de actores.** No existen datos relacionales con fuente. No se infiere centralidad por percepción.

**Vacíos de actores.**

- Compromisos escritos de alcaldías, gobernaciones y aliados: VACIO. Tenedor: equipo formulador.
- Evaluación de poder, legitimidad y urgencia con evidencia: VACIO.
- Participación de operarios y comunidades en la definición de umbrales: VACIO.

### F4.4-MDR.6 Encuadre y modelo decisional

Esta pieza elige el procedimiento de decisión que corresponde al entendimiento, al conflicto y al cambio requeridos. Puntúa los cuatro ejes con evidencia antes de mirar los modelos.

**Ejes del encuadre.**


La {T:i070} reúne los datos de «Ejes del encuadre».

:::TABLA i070 | Ejes del encuadre
| Eje | Valor | Evidencia y derivación | Naturaleza |
| --- | --- | --- | --- |
| Entendimiento causal | MEDIO en la medición; BAJO en la adopción y la custodia; BAJO en la decisión integrada | La condición C4 no se cumple. El estimando E1 es identificable solo por diseño prospectivo y E2 no es identificable (4.3). Todas las relaciones de 4.4 son hipótesis de influencia. | INFERIDO |
| Magnitud del cambio | INCREMENTAL en la medición; ESTRUCTURAL en la custodia | La medición mejora un método existente. La custodia cambia quién opera y quién financia. Se deriva de la decisión requerida. | INFERIDO |
| Acuerdo sobre metas | MEDIO | Las metas del error son contradictorias en F-E3. Los valores sobre la alerta divergen (protección inmediata y continuidad de obra). | INFERIDO |
| Reversibilidad | PARCIALMENTE_REVERSIBLE | Los nodos y los datos se reutilizan con la cláusula de apertura. Los contratos de nube y los compromisos territoriales son difíciles de revertir. | INFERIDO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Matriz de Braybrooke y Lindblom (1963) y contraste con el dominio.**


La {T:i071} reúne los datos de «Matriz de Braybrooke y Lindblom (1963) y contraste con el dominio».

:::TABLA i071 | Matriz de Braybrooke y Lindblom (1963) y contraste con el dominio
| Parte | Entendimiento × magnitud | Cuadrante | Dominio causal | Cuadrantes esperados | Resultado |
| --- | --- | --- | --- | --- | --- |
| Medición con corrección local | MEDIO × INCREMENTAL | Frontera entre Q1 y Q3: se examinan ambos | COMPLICADO | Q1 o Q2 | Coherente con Q1 |
| Adopción institucional y custodia | BAJO × ESTRUCTURAL | Q4: exploración, protección de la reversibilidad y aprendizaje | COMPLEJO | Q3 o Q4 | Coherente |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


No existe discrepancia entre cuadrante y dominio. Por eso no se reabre la clasificación del dominio ni el eje de entendimiento.

**Matriz de Thompson y Tuden (1959), como contraste.** Acuerdo MEDIO y entendimiento BAJO ubican la decisión integrada en la frontera entre T3 (negociación y compromiso) y T4 (recomposición del problema). La frontera respalda tratar la custodia como una negociación con condiciones, no como una asignación unilateral.

**Modelos compatibles.**


La {T:i072} reúne los datos de «Modelos compatibles».

:::TABLA i072 | Modelos compatibles
| Modelo | Condiciones | Evaluación con evidencia |
| --- | --- | --- |
| Racionalidad sinóptica | Metas acordadas, alternativas enumerables, consecuencias estimables con datos y tiempo suficiente | No se cumple. Las consecuencias no son estimables con datos. F-E3 usó una suma ponderada con pesos SUPUESTO; se conserva como dato. |
| Racionalidad limitada y satisfacción (Simon, 1955) | Información limitada y aspiraciones definibles | Se cumple con reserva. Las aspiraciones son en gran parte VACIO. |
| Incrementalismo desarticulado (Lindblom, 1959) | Entendimiento bajo y cambio incremental | No se cumple: la custodia es un cambio estructural. |
| Exploración mixta (Etzioni, 1967) | Coexisten decisiones fundamentales e incrementales | Se cumple. La custodia es fundamental; la calibración y el despliegue de nodos son incrementales. |
| Óptimo normativo (Dror, 1968) | Alto alcance y capacidad de invertir en el proceso | No hay evidencia de esa capacidad. |
| Estructuración participativa (Rosenhead y Mingers, 2001) | Acuerdo bajo, varios actores y problema mal estructurado | Se cumple solo para la custodia. La clasificación global es parcialmente estructurada. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Modelo seleccionado: exploración mixta.** El procedimiento barre las alternativas fundamentales (R0 a R5 y las formas de custodia). Luego examina en detalle las áreas críticas. Las áreas críticas son la medición con contraste (SC-1) y la capacidad de los custodios (SC-4).

**Modelo rival más cercano: racionalidad limitada y satisfacción.** Se conserva como regla de parada de los tramos: el proyecto avanza al tramo siguiente solo cuando se cumplen aspiraciones fijadas antes de buscar. No se adopta como modelo principal porque las aspiraciones no están definidas. La estructuración participativa complementa la exploración mixta en la parte de custodia.

**Tensión registrada.** El modelo es técnicamente adecuado. La selectividad estratégica (F4.4-MDR.4) lo penaliza, porque retrasa el despliegue visible. El calendario electoral limita además el margen del piloto. La tensión permanece abierta y condiciona la factibilidad de R4.

### F4.4-MDR.7 Alternativas, método, sensibilidad y sesgos

Esta pieza evalúa las alternativas con los insumos disponibles. No declara ejecutado un método que carece de insumos. No anticipa un ganador. Reutiliza las alternativas del expediente E3 con su procedencia y agrega dos alternativas propuestas en esta corrida.

**Criterios y aspiraciones registrados antes de evaluar (versión 1.0).** Los criterios siguientes se registraron antes de la matriz de compensaciones y no se modificaron después. Un criterio añadido luego se rotularía POSTERIOR.


La {T:i073} reúne los datos de «Criterios y aspiraciones registrados antes de evaluar (versión 1.0)».

:::TABLA i073 | Criterios y aspiraciones registrados antes de evaluar (versión 1.0)
| Código | Criterio | Nivel de aspiración | Naturaleza |
| --- | --- | --- | --- |
| CR-1 | Verificabilidad de la medición frente a una referencia, con diseño de contraste | La meta del error la fija el término de referencia: VACIO. F-E3 propone menos de 30 %, 15 % o menos y menos de 15 %. | PROPUESTO |
| CR-2 | Operación sin infraestructura pública estable | Disponibilidad de nodos mayor o igual que un umbral por fijar: VACIO. F-E3 cita 90 % y 95 % de tiempo de silencio del nodo, sin fuente. | PROPUESTO |
| CR-3 | Continuidad sin receptor público único | Máxima participación de una fuente de 50 % o menos e índice HHI de 0,40 o menos; prueba de orfandad superada | PROPUESTO (convenciones locales) |
| CR-4 | Corregibilidad: costo de reversión y tiempo de detección del error | Decisión de continuar o detener en el Hito 2 con evidencia | PROPUESTO |
| CR-5 | Compatibilidad con la convocatoria: tope, elegibilidad y madurez | Términos de referencia: VACIO | VACIO |
| CR-6 | Identificabilidad del efecto técnico | Sorteo semanal ejecutado y registrado (4.3) | PROPUESTO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Los criterios C1 a C4 de F-E3 (E3-P14) se conservan como dato con su estado original. Sus pesos (0,40; 0,30; 0,15 y 0,15) son SUPUESTO y las utilidades carecen de evidencia. No se reutilizan como pesos de esta corrida.

**Alternativas.**


La {T:i074} reúne los datos de «Alternativas».

:::TABLA i074 | Alternativas
| Código | Alternativa | Origen | Diseñada bajo la premisa sin receptor único |
| --- | --- | --- | --- |
| R0 | Sin intervención: sensores aislados que transmiten hasta agotar batería o crédito | ALT-00 de F-E3 (E3-P10) | No aplica: no hay servicio que sostener |
| R1 | Estaciones fijas robustas con paneles solares y calibración manual trimestral | ALT-01 de F-E3 | No |
| R2 | Malla de sensores con corrección centralizada en la nube | ALT-02 de F-E3 | No |
| R3 | Red híbrida con corrección local y transferencia a las alcaldías en el mes 25 | ALT-03 de F-E3 con la asignación de E3-P17 | No: supone un receptor |
| R4 | La misma tecnología que R3, por tramos, con piloto de contraste y custodia distribuida | PROPUESTA en esta corrida | Sí |
| R5 | Control del polvo en la fuente con medición de referencia mínima | PROPUESTA; deriva del marco rival de F4.4-MDR.3 | Sí |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


R5 no cuenta con evidencia aportada y no se evalúa con datos. Se incluye para impedir que la elección parta de la solución preferida.

**Método ejecutado: matriz de compensaciones.** La matriz muestra desempeños sin agregarlos. La naturaleza de cada celda es INFERIDO y su verificación es NO_VERIFICADO, porque describe propiedades de diseño y no resultados medidos.


La {T:i075} reúne los datos de «Método ejecutado: matriz de compensaciones».

:::TABLA i075 | Método ejecutado: matriz de compensaciones
| Alternativa | CR-1 Verificabilidad | CR-2 Operación sin infraestructura estable | CR-3 Continuidad sin receptor único | CR-4 Corregibilidad | CR-5 Convocatoria | CR-6 Identificabilidad |
| --- | --- | --- | --- | --- | --- | --- |
| R0 | Sin referencia ni contraste | Sin corrección; sensores aislados | Sin servicio que sostener | Sin decisión que corregir | NO_EVALUADO | Sin diseño de contraste |
| R1 | Calibración manual trimestral; sin contraste previsto | Paneles y radioenlaces propios | Operación costosa; custodio no definido | Compra en bloque | NO_EVALUADO | Sin sorteo previsto |
| R2 | Corrección central con datos continuos | Depende del enlace continuo | Depende de contratos de nube; custodio no definido | Compra en bloque | NO_EVALUADO | Sin sorteo previsto |
| R3 | Corrección local sin diseño de contraste en F-E3 | Transmisión por eventos; enlace 4G sin alterno | Receptor público único supuesto | Compromiso total anticipado | NO_EVALUADO | Sin sorteo en F-E3; admite agregarlo |
| R4 | Referencia gravimétrica y sorteo semanal | El piloto verifica energía y enlace antes de cada tramo; enlace alterno por diseñar | Custodia por tramos y cláusula de apertura | Decisión de continuar o detener en el Hito 2 | NO_EVALUADO: costo del piloto y de la gobernanza sin estimar | Sorteo semanal previsto |
| R5 | No mide el error del sensor; mide exposición con referencia mínima | Poca electrónica; depende de la maquinaria | Operación por contratistas; custodio por definir | Reversible | NO_EVALUADO | No aplica al estimando E1 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Dominancia.** No se confirma ninguna relación de dominancia. R4 no empeora a R3 en CR-1, CR-2, CR-3, CR-4 ni CR-6 por construcción del diseño. Sin embargo, CR-5 es NO_EVALUADO: el costo del piloto y de la gobernanza no se estimó. Sin dominancia, la matriz no produce ganador.

**Métodos no ejecutados.**


La {T:i076} reúne los datos de «Métodos no ejecutados».

:::TABLA i076 | Métodos no ejecutados
| Método | Estado | Motivo |
| --- | --- | --- |
| Árbol de decisión cuantitativo (Raiffa, 1968) | NO_CALCULABLE; árbol cualitativo entregado | Sin probabilidades ni utilidades con fuente |
| Métodos multicriterio (AHP, BWM, TOPSIS, suma ponderada) | NO_EJECUTADO | Los pesos carecen de procedencia y las utilidades de evidencia |
| Análisis costo-beneficio | NO_CALCULABLE | Sin flujos con fuente ni tasa de descuento |
| Análisis de robustez | NO_CALCULABLE | El criterio de aceptabilidad depende de los TdR |
| Análisis estructural Vester/MICMAC | Recibido, no recalculado | Resultados de 4.4 (S2) con identidad registrada en el expediente. Son hipótesis de influencia. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Estructura del cálculo pendiente.** Sean p1 a p4 las probabilidades de SC-1 a SC-4 y v1 a v5 los valores de los resultados de una rama. El valor esperado de esa rama es:

```text
VE = p1·[p2·(p3·(p4·v5 + (1 − p4)·v4) + (1 − p3)·v3) + (1 − p2)·v2] + (1 − p1)·v1
```

Con probabilidades declaradas, la herramienta de referencia barre 2.000 pasos y rotula los umbrales como aproximados.

**Resultado multicriterio de F-E3.** La suma ponderada de E3-P14 arroja 0,795 para ALT-03; 0,535 para ALT-02; 0,460 para ALT-00 y 0,325 para ALT-01. La aritmética se recalculó y es correcta (CALCULADO). Los pesos son SUPUESTO y las utilidades carecen de evidencia. Por eso el resultado no se usa como ganador.

**Sensibilidad y condiciones de elección.** El resultado de la matriz no depende de probabilidades ni de pesos. La sensibilidad se traslada a las condiciones bajo las cuales cambia la elección.

- **R4 se prefiere a R3** cuando se cumplen dos condiciones. El costo adicional del piloto, de la gobernanza y de los tramos cabe en el tope (CR-5). La probabilidad de SC-4 bajo custodia distribuida no es menor que bajo receptor único.
- **R3 se prefiere a R4** cuando, antes de la firma, cada componente cuenta con una entidad territorial con compromiso presupuestal vinculante y competencia jurídica. Esa condición equivale a capacidad de absorción 3 en las seis dimensiones.
- **R5 se combina con R4** si la evidencia de emisión en la fuente muestra que la mayor parte de la exposición es controlable. Esa evidencia no existe todavía.
- **R0 solo se admite** si el financiador no acepta R3 ni R4.

Umbral de cambio de la recomendación: NO_CALCULABLE, porque ninguna probabilidad tiene fuente.

**Auditoría de sesgos.** La auditoría cubre ocho sesgos, entre ellos el anclaje y la disponibilidad (Tversky y Kahneman, 1974) y la racionalización a posteriori (Festinger, 1957). Se aplica al decisor, al analista y al modelo de lenguaje.


La {T:i077} reúne los datos de «Auditoría de sesgos».

:::TABLA i077 | Auditoría de sesgos
| Sesgo | Decisor (expediente E3) | Analista y modelo de lenguaje (esta corrida) |
| --- | --- | --- |
| Confirmación | DETECTADO: los criterios del índice de cierre lógico derivan de la contradicción raíz que ALT-03 resuelve por construcción (E3-P11). | NO_EVALUADO. Contramedida aplicada: se conservaron R0, R1 y R2 y se enumeraron refutaciones. |
| Anclaje | DETECTADO: la cifra de 100 nodos y el 45 % de error orientan el diseño sin referencia independiente. | DETECTADO: se heredaron las cifras de F-E3 como punto de partida. Contramedida: se rotularon DECLARADO y NO_VERIFICADO. |
| Costo hundido | NO_DETECTADO: método de lectura dirigida de F-E3; no hay inversión previa documentada. | NO_DETECTADO por el mismo método. |
| Racionalización a posteriori | DETECTADO: E3-P09 impone tres operadores antes de evaluar alternativas y E3-P11 descarta las demás de forma definitiva. | Contramedida: criterios registrados antes de evaluar (versión 1.0). |
| Pensamiento desiderativo | DETECTADO: cifras favorables sin fuente (90 %, 20 %, 35 minutos como latencia). | Contramedida: rótulo SUPUESTO y NO_CALCULABLE. |
| Exceso de confianza | DETECTADO: expresiones de garantía y de prueba matemática en E3-P05, E3-P09 y E3-P19. | Contramedida: calificador CONDICIONALMENTE y refutaciones enumeradas. |
| Disponibilidad | NO_EVALUADO: falta una tasa base de episodios de PM en remoción de escombros. | NO_EVALUADO. |
| Supuesto de receptor | DETECTADO: E3-P17 y el Capítulo 14 suponen que las alcaldías reciben y sostienen. | Contramedida: premisa sin receptor único y estrategia R4. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


El modelo de lenguaje que redacta tiende a completar los vacíos con prosa coherente. La contramedida es declarar VACIO y NO_CALCULABLE donde faltan insumos.

### F4.4-MDR.8 Teoría del cambio, supuestos, techo y matriz de efectos

Esta pieza explicita cómo y por qué la estrategia R4 produciría el cambio buscado. La teoría del cambio es provisional: usa el problema y las hipótesis de 4.3 y 4.4 y no exige un árbol de problemas terminado. Si 4.5 cambia la representación del problema, se versiona esta pieza.

**Impacto y horizonte.** El cambio de largo plazo se formula como estado observable con población, territorio y horizonte (Weiss, 1995; Taplin y Clark, 2012). El impacto es el problema central de la construcción, invertido. En 36 meses, operarios y comunidades de los sitios de remoción están protegidos por alertas basadas en mediciones verificadas. El territorio es SUPUESTO. La línea base de protección es VACIO.

**Mapeo inverso.** Cada fila responde: ¿qué debe ser cierto antes para que el nivel superior ocurra?


La {T:i078} reúne los datos de «Mapeo inverso».

:::TABLA i078 | Mapeo inverso
| Nodo | Resultado | Precondiciones | Variables de S2 |
| --- | --- | --- | --- |
| IM | Operarios y comunidades protegidos | I1, I2 e I3 | V14 |
| I1 | Protocolos de gestión del riesgo y de salud incorporan las alertas | R3 y la adopción (SC-3) | V15 |
| I2 | Alertas oportunas con falsas alarmas dentro del umbral | R1 y R2 | V12, V13 |
| I3 | Servicio operando con custodios después del mes 24 | P4 y la capacidad de los custodios (SC-4) | V15, V09 |
| R1 | Error reducido y verificable | P1 y P2 (SC-1) | V06 |
| R2 | Datos suficientes | P1 (SC-2) | V09, V08 |
| R3 | Fórmula local del índice y umbrales validados | P3 y la validación (SC-3) | V11, V12 |
| P1 | Nodos con corrección local y repuestos | Compra y despliegue por tramos | V07, V09, V10 |
| P2 | Referencia, protocolo y sorteo | Referencia gravimétrica y registro de asignación | V06 |
| P3 | Gemelo digital y tablero con umbrales propuestos | Desarrollo y datos de R2 | V10, V11 |
| P4 | Acuerdos de custodia y portafolio | Negociación por componente | V15 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Arquitectura según el dominio.** La parte de medición es COMPLICADO y la parte de adopción y custodia es COMPLEJO. La arquitectura elegida es la teoría del cambio anidada: una ejecutiva y una cadena por componente.


La {T:i079} reúne los datos de «Arquitectura según el dominio».

:::TABLA i079 | Arquitectura según el dominio
| Dominio | Arquitectura | Celda de desajuste | Decisión |
| --- | --- | --- | --- |
| COMPLICADO | Anidada | ADECUADA | Elegida para la medición |
| COMPLEJO | Anidada | ADMISIBLE_CON_AJUSTE: cada componente revisa sus supuestos periódicamente | Elegida con revisión trimestral de supuestos |
| COMPLEJO | Sistémica | ADECUADA | Arquitectura rival |
| COMPLICADO | Sistémica | RIESGO_SOBRECOSTO | Rechazada para la medición |
| COMPLEJO | Lineal | RIESGO_RIGIDEZ | Rechazada |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Motivo del rechazo de la arquitectura sistémica.** Exigiría modelar bucles con fichas de salida de confianza baja. Su complejidad excedería la información disponible. La retroalimentación principal (el uso institucional que justifica contratos) se conserva como bucle en la teoría anidada. Se reexamina si el piloto revela patrones emergentes.

**Anidamiento.** La teoría ejecutiva cabe en una página y se desacopla por componente (Funnell y Rogers, 2011). Tiene once nodos. Las cadenas por componente son tres.


La {T:i080} reúne los datos de «Anidamiento».

:::TABLA i080 | Anidamiento
| Componente | Cadena | Nodos |
| --- | --- | --- |
| Medición | Referencia y corrección local, error verificable, alertas fiables | P1, P2, R1, R2, I2 |
| Alertas y adopción | Umbrales propuestos, validados, incorporados en protocolos | P3, R3, I1, IM |
| Custodia y financiación | Acuerdos por tramos, servicio con custodios | P4, I3, IM |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Supuestos críticos.** Cada supuesto tiene mecanismo (PORQUE) y su naturaleza es SUPUESTO. Ninguno se declara INCOMPLETO. Ninguno tiene probabilidad en A-DEC.

**SC-1 (medición).**
- SI: los nodos con corrección local se comparan por sorteo semanal con la lectura sin corrección dinámica y con una referencia gravimétrica.
- ENTONCES: el error normalizado de los nodos corregidos resulta menor y la diferencia es detectable.
- PORQUE: la humedad y el sesgo por tamaño de partícula explican parte del error (V03→V06 = 3 en S2) y la corrección local los compensa antes de la transmisión.
- Evidencia: ficha V03→V06; F-INF §8.3 y §11.7; potencia recalculada en F4.3.6 (diferencia mínima detectable de 0,034 puntos de NMAE, CALCULADO sobre premisas NO_VERIFICADAS).
- Nodo de A-DEC: A1 y B1.

**SC-2 (energía y enlace).**
- SI: los nodos conservan energía y enlace intermitente bajo maquinaria, polvo y humedad.
- ENTONCES: el gemelo digital recibe datos suficientes para el mapa y el tablero.
- PORQUE: la transmisión por eventos reduce el consumo, los nodos averiados se reponen y la maquinaria destruye nodos con peso 2 (V05→V09) que el plan de repuestos absorbe.
- Evidencia: ficha V05→V09; F-E3, E3-P09 (OP-02). F-INF no contiene respaldo de la corrección en el borde.
- Nodo de A-DEC: A2 y B2.

**SC-3 (uso institucional).**
- SI: la autoridad de salud valida una fórmula local del índice y los umbrales, y los puestos de mando los incorporan en sus protocolos.
- ENTONCES: las alertas inducen acciones de protección y aumenta la población protegida.
- PORQUE: una alerta sin portador de decisión no modifica la conducta. En S2, V11→V14 y V13→V14 tienen peso 2 y son hipótesis de influencia.
- Evidencia: fichas de entrada de V14; F-INF §8.3 (D-04): ningún documento de alerta del corpus reporta detección, falsas alarmas ni anticipación.
- Nodo de A-DEC: A3 y B3.

**SC-4 (custodia).**
- SI: al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo de transferencia.
- ENTONCES: el servicio continúa después del mes 24 sin receptor público único.
- PORQUE: cada tramo exige presupuesto aprobado, personal designado y competencia jurídica documentada. Sin ellos rige la cláusula de apertura.
- Evidencia: F-E3, E3-P17 (§13) y Tabla E3-14.2. No existe compromiso firmado.
- Nodo de A-DEC: A4 y B4.

**Techo de rendición de cuentas.** El techo separa lo que el proyecto controla de aquello a lo que solo contribuye. Las metas comprometidas se ubican bajo el techo. El término «techo de rendición de cuentas» es una convención de práctica sin atribución localizada.


La {T:i081} reúne los datos de «Techo de rendición de cuentas».

:::TABLA i081 | Techo de rendición de cuentas
| Zona | Nodos | Qué puede comprometer el proyecto |
| --- | --- | --- |
| Bajo el techo | P1 a P4, R1 a R3 | Nodos desplegados; error frente a la referencia; disponibilidad y latencia especificadas; umbrales propuestos y sometidos a validación |
| Sobre el techo | I1 a I3, IM | Solo contribución: adopción por las autoridades, alertas oportunas, servicio con custodios y protección de personas |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


F-E3 compromete como indicadores de impacto la morbilidad (reducción de 15 %, PERS-S01) y la apropiación local del gasto operativo (PERS-S02). Ambos se ubican sobre el techo. Se reformulan como contribución.

**Cuellos de adopción y marcos de cambio.**


La {T:i082} reúne los datos de «Cuellos de adopción y marcos de cambio».

:::TABLA i082 | Cuellos de adopción y marcos de cambio
| Eslabón que puede fallar | Evidencia | Marco de cambio elegido | Motivo |
| --- | --- | --- | --- |
| Incentivos y pagos: quién financia la operación | Juego de bien público con equilibrio (N, N) (F4.4-MDR.5) | Economía política con arquitectura de decisiones: los tramos condicionados funcionan como opción por defecto | El cuello es de intereses, no de conocimiento |
| Habilidad y refuerzo del personal local | Rotación de personal (F4.4-MDR.4) | ADKAR (Hiatt, 2006) | Identifica si falla la habilidad o el refuerzo |
| Cumplimiento del protocolo de calibración | Dependencia de un estándar operativo | PDCA (Deming, 1986) | El cuello es de ejecución de un estándar |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


No se elige el modelo de transformación organizacional planificada, porque el sistema no depende de una sola organización.

**Efectos del enfoque sobre el proyecto.**


La {T:i083} reúne los datos de «Efectos del enfoque sobre el proyecto».

:::TABLA i083 | Efectos del enfoque sobre el proyecto
| Dimensión | Efecto de la teoría anidada | Aplicación al proyecto |
| --- | --- | --- |
| Formulación | Teoría ejecutiva y por componente | Once nodos y tres cadenas |
| Presupuesto | Por componente, con reasignación interna regulada | Tramos condicionados a la evidencia |
| Indicadores | Por componente y agregados | Metas comprometidas solo bajo el techo |
| Evaluación | Contribución por componente y contrafactual donde aplique | Sorteo en la medición; contribución en adopción y custodia |
| Gobernanza | Comités por componente y comité integrador | Revisión trimestral de supuestos |
| Sostenibilidad | Custodia distribuida por componente | Cláusula de apertura |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Riesgo de una clasificación errónea.** Si la adopción fuera CLARA, la revisión trimestral generaría sobrecosto. Si fuera CAOTICA, la coordinación por componente sería lenta.

**Traducción a los formatos obligatorios.** El instrumento puede exigir la matriz de marco lógico o un formato de proyecto. Su vigencia es CANDIDATO_A_VERIFICAR. La teoría del cambio gobierna y el formato es su proyección operativa. El formato no expresa tres elementos: el bucle de demanda (I1 hacia P4), la condicionalidad de los tramos (SC-4) y el sorteo semanal. Se documentan aparte.

**Vacíos de la teoría del cambio.**

- Evidencia primaria de SC-2 y SC-3: VACIO. Vía: lectura de fuentes primarias y piloto.
- Mecanismo de cobertura de referencias: solo hay tres monitores gravimétricos presupuestados (F-E3, Tabla E3-8.3) para 100 nodos.

### F4.4-MDR.9 Validación argumentativa

Esta pieza somete la decisión y cada supuesto crítico a la estructura de Toulmin (1958), adaptada por Dunn (2018). Responde qué sostiene la propuesta y bajo qué condiciones falla.

**Argumento de la decisión.** **Información (I).**
1. S2 clasifica V06 como crítica en los cinco escenarios y V15 participa en 140 de 144 ciclos simples. Sus fichas de salida tienen confianza baja o media (F4.4.13 y F4.4.14). CALCULADO; estatuto HIE.
2. F-E3 afirma que, si las alcaldías no asumen la responsabilidad de operar, la red termina en el mes 25 (E3-P17, §13). Ningún compromiso está firmado. DOCUMENTADO; NO_VERIFICADO.
3. F-INF §6.5 modela la calibración y el mantenimiento como un juego de bien público con equilibrio (N, N). INFERIDO.
4. F-INF §8.3 recomienda una fase 0 de 12 meses antes de la compra masiva y un protocolo de calibración colocalizada. DOCUMENTADO en F-INF; fuente primaria no leída.
5. 4.3 declara el estimando E1 identificable por diseño con sorteo semanal. CALCULADO sobre premisas NO_VERIFICADAS.

**Afirmación (C).** El proyecto ejecuta R4 antes que R3 como estrategia base y decide continuar o detener en el Hito 2 según la evidencia del piloto.

**Justificación (W).** Cuando el resultado depende de supuestos no verificados, se prefiere la opción de menor costo de reversión y menor tiempo de detección (Collingridge, 1980). La corrección tardía es costosa. Cuando la continuidad depende de un actor sin compromiso ejecutable, el diseño no lo supone.

**Respaldo (B).** Collingridge (1980) y Shediac-Rizkallah y Bone (1998) respaldan los dos principios. Ninguna de las dos obras se consultó en esta corrida.

**Calificador (Q).** CONDICIONALMENTE. C depende de los supuestos SC-1 a SC-4, que son SUPUESTO.

**Refutación (R).** C no se sostiene si ocurre alguna de estas condiciones observables:
1. Los términos de referencia prohíben el piloto o la compra por tramos.
2. El costo adicional del piloto y de la gobernanza excede el margen del tope de 14.000 millones de COP.
3. Cada componente cuenta con un custodio con compromiso presupuestal vinculante y competencia jurídica, con capacidad de absorción 3. Entonces R3 pasa a ser admisible.
4. En el Hito 2, el error normalizado de los nodos corregidos no resulta menor que el de la lectura sin corrección dinámica. Entonces R4 se detiene.

**Objeción (O).** La estrategia por tramos retrasa el despliegue en una emergencia y la gobernanza distribuida eleva los costos de coordinación. La respuesta parcial es que el piloto corre dentro de los 24 meses y que el Hito 2 ocurre en el mes 12. El costo adicional no se estimó. La objeción permanece ABIERTA.

**Pruebas de argumento.**


La {T:i084} reúne los datos de «Pruebas de argumento».

:::TABLA i084 | Pruebas de argumento
| Prueba | Resultado | Motivo |
| --- | --- | --- |
| Pertinencia | CUMPLE para I(1), I(2) e I(5); NO_CUMPLE para I(3) e I(4) | I(3) e I(4) provienen de otro territorio y se usan como antecedente. Por eso Q no sube. |
| Autorización | CUMPLE | C es una decisión de diseño bajo incertidumbre. No se infiere causalidad de una correlación. |
| Respaldo | NO_EJECUTADO | B es localizable, pero no se consultó su edición ni su aplicabilidad. |
| Proporción | CUMPLE | Q no excede la fuerza de I y B. |
| Refutabilidad | CUMPLE | R enumera cuatro condiciones observables. |
| Rival | CUMPLE | O existe y queda registrada como abierta. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Validación de los supuestos críticos.**


La {T:i085} reúne los datos de «Validación de los supuestos críticos».

:::TABLA i085 | Validación de los supuestos críticos
| Supuesto | Información | Justificación (PORQUE) | Respaldo | Calificador | Refutación observable | Objeción principal |
| --- | --- | --- | --- | --- | --- | --- |
| SC-1 | Ficha V03→V06 (confianza media); potencia recalculada | La humedad y el tamaño sesgan la lectura | F-INF §8.3 (cita secundaria) | CONDICIONALMENTE | La diferencia entre N4 y N1 no se distingue de cero con el sorteo completo | La mejora proviene de la cercanía a la referencia (DAG rival R1); se responde con el sorteo |
| SC-2 | Ficha V05→V09; contradicción del enlace 4G | La transmisión por eventos reduce el consumo | F-E3, E3-P09; sin respaldo en F-INF | PLAUSIBLEMENTE | Disponibilidad de nodos bajo el umbral en tres meses consecutivos | El enlace celular colapsa con el entorno; ABIERTA |
| SC-3 | Fichas de entrada de V14 | Una alerta sin portador no cambia la conducta | F-INF §8.3 (D-04): ausencia de reportes | PLAUSIBLEMENTE | Ningún puesto de mando incorpora los umbrales en 12 meses | La gobernación impone el uso sin fórmula local validada; ABIERTA |
| SC-4 | F-E3, E3-P17 y Tabla E3-14.2 | Cada tramo exige presupuesto, personal y competencia | Shediac-Rizkallah y Bone (1998) | CONDICIONALMENTE | Ningún custodio alcanza capacidad 2 al cierre del Hito 2 | Una ordenanza departamental sostendría sin tramos; ABIERTA |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Argumento de sostenibilidad.**


La {T:i086} reúne los datos de «Argumento de sostenibilidad».

:::TABLA i086 | Argumento de sostenibilidad
| Afirmación | Calificador | Motivo |
| --- | --- | --- |
| La red continúa operando después del mes 24 | NO_SOSTENIDO | La información disponible no incluye respaldo financiero ni institucional. |
| Las alcaldías asumen el gasto operativo de la nube desde el año 3 (CLM-06 de F-E3) | NO_SOSTENIDO | Es un SUPUESTO sin aval ni partida. |
| Si ningún custodio demuestra capacidad, el diseño preserva datos, código y conocimiento | CONDICIONALMENTE | Depende de que la cláusula de apertura se firme antes del primer tramo. |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Dialéctica de la controversia sobre la custodia.** **Tesis.** Las alcaldías deben recibir la operación, porque responden legalmente por actuar sobre la alerta (E3-P17). La evidencia es la asignación de responsabilidad y la competencia territorial en gestión del riesgo.

**Antítesis.** Ninguna entidad pública puede sostener la solución por sí sola al cierre. Tres hechos la respaldan: no hay compromiso firmado, la institución ejecutora carece de recursos permanentes y el equilibrio del juego es (N, N).

**Síntesis.** La transferencia se hace por tramos a los custodios que demuestran capacidad. Las alcaldías conservan la competencia legal sobre la alerta. La operación técnica y el financiamiento se distribuyen. La síntesis conserva lo que cada posición explica. La tesis explica quién responde ante la ley. La antítesis explica por qué la responsabilidad legal no basta para sostener la operación.

**Control de pensamiento grupal.** Las contramedidas siguen a Janis (1982). Una sola instancia analítica ejecutó todas las funciones. No existe un evaluador crítico independiente. Se declara AUTORREVISION. Las objeciones abiertas se conservan sin resolver. La revisión humana de los cuatro supuestos y de la objeción principal es la condición de aceptación.

**Reentradas.** La prueba de pertinencia fallida para I(3) e I(4) no reabre una fase: limita el calificador. La prueba de respaldo no ejecutada se registra como vacío.

### F4.4-MDR.10 Sostenibilidad posproyecto

Esta pieza diseña la continuidad de la solución con la premisa de diseño PD-0: ninguna entidad pública puede asumir su sostenimiento al cierre. PD-0 es un SUPUESTO de diseño. No afirma la incapacidad de una entidad concreta; obliga a que la solución sobreviva sin depender de esa capacidad. Los umbrales de concentración y de capacidad de absorción son convenciones locales PROPUESTAS, no requisitos oficiales.

**Evidencia de antecedentes.** El usuario declara que existen antecedentes de baja sostenibilidad pública. Esa afirmación conserva el estado DECLARADO para proyectos de ciencia, tecnología e innovación en Colombia. La búsqueda en los archivos aportados encontró evidencia parcial sobre redes de monitoreo.


La {T:i087} reúne los datos de «Evidencia de antecedentes».

:::TABLA i087 | Evidencia de antecedentes
| Evidencia | Alcance | Fuente | Estado |
| --- | --- | --- | --- |
| 90,8 % de las estaciones de la red nacional propuesta carecería de plan de calibración | Propuesta de red de bajo costo | F-INF §8.3 (Murad Pedraza et al., 2026, como se citó en F-INF) | DOCUMENTADO en F-INF; fuente primaria no leída |
| 16,8 % de las estaciones brasileñas inactivas o sin estado | Redes de monitoreo en Brasil | F-INF §6.5 (Tavella et al., 2026, como se citó en F-INF) | DOCUMENTADO en F-INF; fuente primaria no leída |
| Equipos que terminan en bodegas municipales | Entidades territoriales colombianas | F-E3, Cap. 14.3 | DECLARADO; NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Ninguna fuente aportada evalúa la continuidad de proyectos financiados con regalías. La afirmación del usuario permanece sin respaldo propio en esta corrida.

**Inventario de componentes.**


La {T:i088} reúne los datos de «Inventario de componentes».

:::TABLA i088 | Inventario de componentes
| Componente | Tipo | Función | Dependencias | Costo anual con fuente |
| --- | --- | --- | --- | --- |
| Nodos sensoriales (M1) | ACTIVOS_FISICOS | Miden PM2,5, PM10, humedad y viento | Energía; enlace de radio de largo alcance | VACIO por componente; línea agregada de repuestos en F-E3 |
| Gateways con corrección local (M2) | ACTIVOS_FISICOS; SOFTWARE | Corrigen el error en sitio y despachan picos | Energía estable; enlace celular | VACIO |
| Gemelo digital (M3) | SOFTWARE; DATOS | Mapa de dispersión y reentrenamiento | Nube; datos de M2 | Línea agregada de operación en F-E3 |
| Tablero de alertas (M4) | SOFTWARE; SERVICIO | Índice local y alertas | M3; fórmula local validada | VACIO |
| Series de datos | DATOS | Base maestra de mediciones | Licencia y propiedad | VACIO |
| Protocolo de calibración y sorteo | CONOCIMIENTO | Referencia y contraste | Monitores gravimétricos | VACIO |
| Operación y soporte | SERVICIO | Mantenimiento y soporte algorítmico | Personal certificado | Línea agregada de personal en F-E3 |
| Usuarios institucionales | RED_DE_USUARIOS | Uso del tablero en protocolos | Acuerdos y capacitación | VACIO |
| Modelos y código | PROPIEDAD_INTELECTUAL | Corrección local y gemelo | Libertad de operación (F-INF §8.3, D-01) | VACIO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Costo total de sostenimiento y nivel mínimo de servicio.** La fórmula es CTS anual = suma de operación, personal, licencias, mantenimiento, reposición y gobernanza. La reposición anual es el costo del activo dividido por su vida útil (Shediac-Rizkallah y Bone, 1998). F-E3 declara tres de los seis rubros en la Tabla E3-14.2. Faltan licencias, reposición y gobernanza.

**Resultado.** CTS anual es NO_CALCULABLE. Solo existe una cota inferior declarada: 190,00; 208,25 y 226,91 millones de COP en los años 1, 2 y 3 posteriores al proyecto. La naturaleza es PROPUESTO y la verificación es NO_VERIFICADO. Esa cifra no incluye el ahorro ni la inversión inicial.

**Nivel mínimo de servicio viable (propuesta).** El nivel mínimo comprende cuatro elementos: nodos de referencia verificados, un tablero con umbrales vigentes, conservación y publicación de datos, y mantenimiento correctivo. Su costo mínimo anual es NO_CALCULABLE, porque ningún rubro está desagregado por componente.

**Índice de capacidad de absorción de los custodios (ICAR).** El índice puntúa de 0 a 3 seis dimensiones por custodio: financiera, talento, jurídica, técnica, continuidad y demanda. El resultado es el mínimo de las seis, sin compensación. Ningún candidato cuenta con evidencia en las seis dimensiones.


La {T:i089} reúne los datos de «Índice de capacidad de absorción de los custodios (ICAR)».

:::TABLA i089 | Índice de capacidad de absorción de los custodios (ICAR)
| Custodio candidato | Evidencia disponible | ICAR |
| --- | --- | --- |
| Alcaldías | Responden legalmente por actuar sobre la alerta (E3-P17). Sin partida ni compromiso. DECLARADO | NO_CALCULABLE |
| Gobernaciones y unidades de gestión del riesgo | Tabla E3-14.3 de F-E3 propone ordenanzas. No existen. | NO_CALCULABLE |
| UNGRD | Aporte en especie de personal (Tabla E3-14.2) sin aval | NO_CALCULABLE |
| IDEAM y autoridades ambientales | Referencia metrológica (F-INF §6.5). Sin convenio. | NO_CALCULABLE |
| Institución ejecutora | CONTRADICTORIO: sin recursos permanentes (E3-P17, §13) frente a personal en especie (Tabla E3-14.2) | NO_CALCULABLE |
| Empresa aliada | Responsable de código y propiedad intelectual (E3-P17). Sin modelo de negocio. | NO_CALCULABLE |
| ARL y corporación autónoma | Convenio de cofinanciación declarado en la Tabla E3-14.2 sin evidencia | NO_CALCULABLE |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


No se asigna ningún valor por defecto. Un custodio sin evidencia queda NO_EVALUADO, no en cero.

**Custodia distribuida.** Ningún componente queda sin custodio o sin cláusula de apertura. La asignación de custodios es NO_CALCULABLE sin ICAR. La tabla fija las exigencias por componente y los candidatos. Ninguna entidad se asigna por defecto.


La {T:i090} reúne los datos de «Custodia distribuida».

:::TABLA i090 | Custodia distribuida
| Componente | Dimensiones que exige | Candidatos | Custodio asignado |
| --- | --- | --- | --- |
| Nodos y repuestos | Técnica; talento | Empresa aliada; institución ejecutora | POR_DEFINIR con ICAR |
| Gemelo digital y datos | Financiera; técnica | Institución ejecutora; empresa aliada | POR_DEFINIR con ICAR |
| Tablero y alertas | Jurídica; demanda | Unidades de gestión del riesgo; alcaldías | POR_DEFINIR con ICAR |
| Protocolo de calibración | Técnica; continuidad | Autoridad ambiental; institución ejecutora | POR_DEFINIR con ICAR |
| Gobernanza y acuerdos | Jurídica; continuidad | Órgano de gobierno de la alianza | POR_DEFINIR |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Motor financiero y concentración.** La tabla usa las cifras que F-E3 declara en la Tabla E3-14.2, en millones de COP. Son PROPUESTAS y NO_VERIFICADAS. El cálculo es exacto sobre ellas. Se rotula CALCULADO sobre cifras NO_VERIFICADAS.


La {T:i091} reúne los datos de «Motor financiero y concentración».

:::TABLA i091 | Motor financiero y concentración
| Fuente declarada | Año 1 | Participación | Año 2 | Participación | Año 3 | Participación |
| --- | --- | --- | --- | --- | --- | --- |
| Secretarías TIC municipales (operación de nube e IoT) | 45,00 | 23,7 % | 47,25 | 22,7 % | 49,61 | 21,9 % |
| Convenio de ARL y corporación autónoma (mantenimiento y repuestos) | 25,00 | 13,2 % | 35,00 | 16,8 % | 45,00 | 19,8 % |
| IES regional y UNGRD en especie (personal técnico y soporte) | 120,00 | 63,2 % | 126,00 | 60,5 % | 132,30 | 58,3 % |
| Total declarado (costo parcial) | 190,00 | 100,0 % | 208,25 | 100,0 % | 226,91 | 100,0 % |
| Participación máxima | — | 63,2 % | — | 60,5 % | — | 58,3 % |
| Índice HHI | — | 0,472 | — | 0,446 | — | 0,427 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Lectura.** La participación máxima supera 50 % y el índice HHI supera 0,40 en los tres años. Ambos resultados incumplen las convenciones locales PROPUESTAS. La fuente concentrada es el personal técnico en especie. Ese aporte contradice la falta de recursos permanentes de la institución ejecutora (E3-P17).

**Fondo patrimonial.** El capital requerido es K = CTS cubierto / r_real, donde r_real es la rentabilidad real anual con fuente. K es NO_CALCULABLE: ni el CTS completo ni r_real tienen fuente.

**Prueba de orfandad.** Para cada fuente se compara la suma de las demás con el costo mínimo del servicio. Si la suma es menor, la fuente es CRITICA. El costo mínimo es NO_CALCULABLE. Por eso se calcula el umbral que lo vuelve crítico, con las cifras del año 1.


La {T:i092} reúne los datos de «Prueba de orfandad».

:::TABLA i092 | Prueba de orfandad
| Fuente | Suma de las demás fuentes, año 1 (millones de COP) |
| --- | --- |
| IES regional y UNGRD en especie | 70 |
| Secretarías TIC municipales | 145 |
| ARL y corporación autónoma | 165 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Una fuente es CRITICA si el costo mínimo anual supera la suma de las demás.

La fuente en especie incluye a la UNGRD, que es una entidad pública. Esa fuente resulta CRITICA con cualquier nivel mínimo de servicio que cueste más de 70 millones de COP al año. El soporte técnico declarado cuesta 120. Si el nivel mínimo incluye ese soporte, la prueba invalida el portafolio declarado y reabre la asignación de custodia y el motor financiero. La conclusión es condicional al costo mínimo, que falta.

**Transferencia por tramos condicionados.** Cada tramo exige presupuesto aprobado, personal designado y competencia jurídica documentada. Los hitos son PROPUESTOS. Los meses toman como referencia los hitos de F-E3 (Capítulo 9).


La {T:i093} reúne los datos de «Transferencia por tramos condicionados».

:::TABLA i093 | Transferencia por tramos condicionados
| Tramo | Mes | Qué se transfiere | Condición de recepción |
| --- | --- | --- | --- |
| 0 | 6 | Nada. Se firman acuerdos de custodia y la cláusula de apertura. | Acuerdos firmados antes de comprar el segundo lote de nodos |
| 1 | 12 | Protocolo de calibración y series de datos | Evidencia del contraste (SC-1) y custodio con capacidad de absorción 2 o más |
| 2 | 18 | Nodos adicionales y tablero a los custodios con capacidad demostrada | Partida en el plan operativo anual y personal designado |
| 3 | 24 | Operación continua de los componentes con custodio | Competencia jurídica documentada y primer pago del servicio |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Un componente sin custodio que cumpla la condición permanece bajo la alianza o pasa a la cláusula de apertura.

**Cláusula de apertura y salida ordenada.** Si el motor financiero falla, los datos, el código y el conocimiento se liberan con una licencia definida. Los activos físicos pasan a un custodio académico o comunitario con un manual de reactivación.

- **Disparador (PROPUESTO).** La cobertura del costo mínimo es menor que 100 % durante dos trimestres consecutivos.
- **Licencia.** La elección de la licencia de datos y código es un VACIO que decide el equipo formulador y la empresa aliada. La libertad de operación sobre propiedad industrial requiere la consulta recomendada en F-INF §8.3 (D-01).
- **Manual de reactivación.** Contiene el inventario de activos, los procedimientos de calibración, la estructura de datos y las credenciales de custodia.

**Gobernanza.**


La {T:i094} reúne los datos de «Gobernanza».

:::TABLA i094 | Gobernanza
| Miembro del órgano | Naturaleza | Función |
| --- | --- | --- |
| Institución ejecutora | Académica | Ejecución técnica y custodia del conocimiento |
| Empresa aliada | Privada | Desarrollo y mantenimiento tecnológico |
| Alcaldías y gobernaciones | Territorial | Uso de la alerta y competencia legal |
| Autoridad ambiental o IDEAM | Nacional o regional | Referencia metrológica |
| ARL o constructoras | Sector productivo | Cofinanciación y uso del dato |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Regla de decisión PROPUESTA: mayoría calificada y veto de cada custodio sobre su propio componente. Rendición: informe anual público con tres indicadores de continuidad (capacidad de absorción de cada custodio, cobertura del costo mínimo y disponibilidad de nodos). Condición de caducidad: la cláusula de apertura se activa si la cobertura cae bajo el disparador.

**Instrumentos de contexto.** Los instrumentos siguientes son CANDIDATO_A_VERIFICAR. No se consultó su fuente controlante. No se afirma su vigencia.


La {T:i095} reúne los datos de «Instrumentos de contexto».

:::TABLA i095 | Instrumentos de contexto
| Instrumento | Uso posible |
| --- | --- |
| Vigencias futuras | Comprometer el gasto recurrente después del cierre |
| Asociaciones público-privadas | Operación con una empresa por contrato |
| Convenios de cofinanciación | Aportes de ARL y autoridades ambientales |
| Pago por resultados | Pago ligado a disponibilidad y verificación |
| Corporaciones mixtas de ciencia, tecnología e innovación | Vehículo operador de la red |
| Obras por impuestos y beneficios tributarios | Financiación por el sector privado |
| Reglas de operación y mantenimiento de proyectos con regalías | Límites al gasto recurrente |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Vacíos de sostenibilidad.**

- Costos por componente, licencias, reposición y gobernanza: VACIO. Vía: cotización y vida útil por activo.
- Evidencia por dimensión del índice para cada custodio: VACIO. Vía: cartas de compromiso, actos administrativos y certificados.
- Rentabilidad real del fondo patrimonial: VACIO.
- Evidencia de continuidad de proyectos con regalías: VACIO.

### F4.4-MDR.11 Ejecución, evaluación y aprendizaje

Esta pieza define qué evidencia obliga a corregir la decisión o la teoría del cambio, y cómo se corrige. Entrega el protocolo para el responsable. No promete vigilancia posterior.

**Hipótesis de intervención.** Si se ejecuta R4 durante 24 meses, en el horizonte de 36 meses se espera observar tres resultados. Primero, una diferencia detectable del logaritmo del error normalizado entre los nodos con corrección local y los nodos sin corrección dinámica, en el indicador nodo-semana. Segundo, al menos un tramo de custodia recibido por un custodio con capacidad de absorción 2 o más. Tercero, al menos un puesto de mando que incorpore los umbrales validados.

**Acción estratégica (Hay, 2002).** El equipo formulador busca financiar una solución verificable. Lee un contexto que premia la novedad visible (F4.4-MDR.4). Elige presentar el piloto como producto de conocimiento y los tramos como evidencia de alianza ejecutable.

**Implementación de abajo hacia arriba.** La conducta requerida en el punto de entrega determina los recursos y las reglas (Lipsky, 1980; Elmore, 1979).


La {T:i096} reúne los datos de «Implementación de abajo hacia arriba».

:::TABLA i096 | Implementación de abajo hacia arriba
| Punto de entrega | Conducta requerida | Recursos necesarios | Reglas necesarias |
| --- | --- | --- | --- |
| Cuadrilla de remoción | Reduce o detiene la actividad al superar el umbral | Alerta comprensible en sitio | Protocolo con el contratista y regla de reanudación |
| Funcionario del puesto de mando | Valida la alerta y activa el protocolo | Acceso al tablero y capacitación | Mandato y umbrales con portador |
| Técnico de campo | Registra la asignación semanal y repone nodos | Repuestos; acta de asignación; actualización remota de nodos (VACIO) | Registro previo a la lectura de datos |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Consecuencias no deseadas.** Ninguna anticipación es exhaustiva (Merton, 1936). El plan exige monitoreo, no previsión total.


La {T:i097} reúne los datos de «Consecuencias no deseadas».

:::TABLA i097 | Consecuencias no deseadas
| Efecto plausible | Mecanismo | Señal que lo revelaría | Respuesta prevista |
| --- | --- | --- | --- |
| Falsa seguridad | Un sesgo residual produce lecturas bajas y las autoridades relajan la vigilancia | Casos respiratorios sin alerta previa | Publicar rangos de incertidumbre y mantener la referencia |
| Presión para subir umbrales | Las alertas generan paros de obra costosos | Solicitudes de cambio de umbral después de cada alerta | Umbral con portador y registro público de cambios |
| Desplazamiento de recursos | La medición sustituye el control del polvo en la fuente | Ausencia de medidas de supresión en obra | Combinar R4 con R5 |
| Pérdida de nodos | La maquinaria y el hurto reducen la disponibilidad | Caída de la disponibilidad por sitio | Repuestos y reubicación |
| Dependencia del proveedor | El código cerrado impide el cambio de custodio | Cláusulas de licencia restrictivas | Cláusula de apertura |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Corregibilidad.** Entre alternativas comparables se prefiere la de menor costo de reversión y menor tiempo de detección del error (Collingridge, 1980). R4 detecta una falla de SC-1 en el mes 12. R3 la detectaría después de comprometer la inversión completa.

**Ruta evaluativa.** La elección responde a la pregunta evaluativa y no al prestigio del método. La secuencia recorre cada pregunta con su condición.


La {T:i098} reúne los datos de «Ruta evaluativa».

:::TABLA i098 | Ruta evaluativa
| Pregunta evaluativa | Condición | Ruta elegida | Motivo |
| --- | --- | --- | --- |
| ¿Cuál es el efecto promedio del método de corrección sobre el error de medición? | Grupo de comparación válido por sorteo y casos suficientes (5.200 nodo-semanas, 4.3) | Diseño contrafactual experimental con análisis de la teoría del cambio | El sorteo semanal intra-nodo genera el grupo de comparación |
| ¿Por qué, para quién y en qué contexto se adoptan las alertas? | Pregunta por mecanismo y contexto (Pawson y Tilley, 1997) | Evaluación realista | Tres departamentos con contextos distintos |
| ¿Contribuyó el proyecto a proteger personas? | Pocos casos con teoría previa y atribución difícil (Mayne, 2012; Befani y Mayne, 2014) | Análisis de contribución o rastreo de procesos | E2 no es identificable (4.3) |
| ¿Qué combinaciones causales explican la custodia? | Varios casos comparables (Ragin, 1987) | No aplica | Tres casos no bastan |
| ¿Qué resultados emergieron sin teoría previa? | Ausencia de teoría del cambio (Wilson-Grau, 2019) | No aplica | La teoría del cambio existe |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Supuestos priorizados, frecuencia y revisión.** La criticidad por umbral es NO_CALCULABLE. La priorización es PROPUESTA: se monitorean primero SC-2 y SC-3, con el calificador más bajo, y SC-1, que activa el punto de reversión. Frecuencia PROPUESTA de revisión: trimestral para adopción y custodia (dominio complejo); anual para la medición (dominio complicado), con corte en el mes 12.

**Aprendizaje de bucle doble.** Cuando los datos contradicen un supuesto, se revisan el supuesto, las metas y la teoría en uso (Argyris y Schön, 1978). La revisión no se limita a las actividades. Cada revisión se registra como una nueva versión de la teoría del cambio.

**Plan de ejecución, evaluación y aprendizaje.**


La {T:i099} reúne los datos de «Plan de ejecución, evaluación y aprendizaje».

:::TABLA i099 | Plan de ejecución, evaluación y aprendizaje
| Elemento | Contenido | Naturaleza |
| --- | --- | --- |
| Indicador principal | Logaritmo del error normalizado por nodo-semana | PROPUESTO |
| Línea base | VACIO: medición con referencia en el primer hito | VACIO |
| Umbral de detención de R4 | El intervalo de confianza de 95 % de la diferencia entre N4 y N1 incluye cero con el sorteo completo | PROPUESTO |
| Umbral de revisión de la disponibilidad | Menor que 80 % durante tres meses consecutivos | PROPUESTO; sin fuente |
| Umbral de falsas alarmas | Habilidad frente a una línea base de persistencia, según F-INF §8.3 (D-04) | PROPUESTO |
| Punto de reversión | Hito 2 (mes 12): detener la expansión si SC-1 falla | PROPUESTO |
| Prueba piloto | Sorteo semanal durante 52 semanas con 100 nodos y 20 % de repuestos | PROPUESTO (4.3) |
| Responsable | RESPONSABLE_POR_DESIGNAR | VACIO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Los umbrales no provienen de normas ni de metas aprobadas, porque los términos de referencia faltan. Por esa razón son PROPUESTOS.

**Vacíos de ejecución.**

- Línea base de error de medición, disponibilidad y falsas alarmas: VACIO.
- Mecanismo de actualización remota del nivel de corrección en cada nodo: VACIO. Condiciona el sorteo.
- Responsable del seguimiento: VACIO.

### F4.4-MDR.12 Premortem y escenarios

**Premortem.** Se supone que la decisión R4 fracasó en el horizonte de 36 meses (Klein, 2007). La tabla enumera las causas por fase de origen, con señal temprana, contención y responsable.


La {T:i100} reúne los datos de «Premortem».

:::TABLA i100 | Premortem
| Fase de origen | Causa del fracaso | Señal temprana | Contención | Responsable |
| --- | --- | --- | --- | --- |
| Construcción | La línea base y la meta del error no se fijaron y no se puede declarar éxito | Metas distintas en documentos del mismo expediente | Fijar meta y método antes del primer hito | Equipo formulador (POR_IDENTIFICAR) |
| Entorno | Los TdR prohíben el piloto o la compra por tramos | Observaciones del convocante al formato | Presentar el piloto como producto de conocimiento | Equipo formulador |
| Actores | Las alcaldías no presupuestan la operación; el cambio de administración rompe el compromiso | Cartas de compromiso sin partida | Acuerdos por tramos y ordenanzas como condición | Gobernaciones (POR_IDENTIFICAR) |
| Encuadre | El dominio se clasificó mal y la revisión de supuestos resulta lenta o costosa | Ajustes frecuentes del plan sin resultado | Revisión trimestral con regla de parada | Comité integrador |
| Alternativas | La elección racionalizó una alternativa preferida | Criterios nuevos después de evaluar | Criterios registrados con versión | Analista |
| Teoría del cambio (SC-1) | La corrección local no reduce el error frente a la lectura sin corrección | Diferencia no distinta de cero a mitad del piloto | Detener la expansión en el mes 12 | Equipo científico |
| Teoría del cambio (SC-2) | Los nodos pierden energía o enlace y el gemelo no recibe datos | Disponibilidad bajo el umbral | Repuestos y enlace alterno | Empresa aliada |
| Argumento | La refutación no era observable y el fallo se detecta tarde | Refutaciones sin indicador | Indicadores por condición de refutación | Evaluador |
| Sostenibilidad (pérdida de custodia) | Ningún custodio alcanza capacidad 2 y la fuente principal desaparece | Cobertura del costo mínimo menor que 100 % | Cláusula de apertura | Órgano de gobierno |
| Ejecución | Los umbrales de revisión no se aplican por falta de responsable | Revisión trimestral omitida | Designar responsable en el acuerdo de alianza | Comité integrador |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Tres futuros.** Los futuros son combinaciones de supuestos y no pronósticos. Cada uno declara qué supuestos se cumplen y cómo se comportan la teoría del cambio y la sostenibilidad. Las nueve opciones por futuro son PROPUESTAS hasta su aprobación. Las opciones de un objetivo difieren en mecanismo, no solo en intensidad.

**Futuro conservador.** SC-1 y SC-2 se cumplen; SC-3 y SC-4 fallan. La teoría del cambio llega a los resultados inmediatos. La sostenibilidad activa la cláusula de apertura.


La {T:i101} reúne los datos de «Futuro conservador».

:::TABLA i101 | Futuro conservador
| Objetivo | Opción y mecanismo | Condición de viabilidad | Riesgo principal |
| --- | --- | --- | --- |
| 1. Consolidar una medición verificada | 1a. Ampliar el sorteo a más nodos con la misma referencia (más réplicas de contraste) | Monitores gravimétricos suficientes | Cobertura de referencias: solo tres monitores presupuestados |
|  | 1b. Co-ubicar nodos con estaciones oficiales (referencia externa) | Convenio con la autoridad ambiental | Representatividad de los sitios |
|  | 1c. Corrección por reglas fijas con humedad, sin aprendizaje embebido (método más simple) | El error se mantiene aceptable con reglas fijas | Deriva no corregida |
| 2. Dar uso técnico sin adopción pública | 2a. Tablero para la interventoría y la institución ejecutora (usuarios técnicos) | Acuerdo con el contratista | Conflicto de interés del contratista |
|  | 2b. Informes a ARL y constructoras para el control de exposición ocupacional | Convenio con la ARL | Uso para eludir responsabilidades |
|  | 2c. Publicación abierta de series y boletines para universidades y comunidades | Licencia abierta de datos | Lectura sin protocolo de respuesta |
| 3. Preservar activos y conocimiento | 3a. Servicio mínimo con un custodio académico (custodia única) | Recursos del custodio para el servicio mínimo | Falta de recursos permanentes |
|  | 3b. Liberación abierta de datos y código con manual de reactivación (apertura) | Licencia definida antes del primer tramo | Pérdida de la capacidad de operación |
|  | 3c. Contrato de servicios con constructoras y ARL para mantener nodos de referencia (financiación privada) | Contratos con vigencia superior al proyecto | Dependencia de pocos clientes |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Futuro base.** SC-1, SC-2 y SC-3 se cumplen; SC-4 se cumple en parte de los componentes. La teoría del cambio llega a la incorporación de protocolos y a un servicio parcial. La sostenibilidad ejecuta tramos parciales.


La {T:i102} reúne los datos de «Futuro base».

:::TABLA i102 | Futuro base
| Objetivo | Opción y mecanismo | Condición de viabilidad | Riesgo principal |
| --- | --- | --- | --- |
| 1. Mantener el error verificado en operación | 1a. Recalibración por ventana estable con referencia permanente en un subconjunto de nodos (algorítmico) | Referencias permanentes financiadas | Deriva entre recalibraciones |
|  | 1b. Recalibración periódica manual con técnicos locales certificados (humano) | Técnicos con permanencia | Rotación de personal |
|  | 1c. Reentrenamiento con datos de referencia compartidos entre sitios (colaborativo) | Acuerdo de datos entre custodios | Sesgo por sitio |
| 2. Incorporar umbrales en los protocolos | 2a. Protocolo piloto en un departamento y expansión por evidencia (secuencia territorial) | Un departamento con capacidad | Aprendizaje no transferible |
|  | 2b. Acto administrativo departamental que adopta los umbrales (normativo) | Competencia jurídica de la gobernación | Cambio de administración |
|  | 2c. Cláusulas ambientales en contratos de obra que citan los umbrales (contractual) | Cooperación de las entidades contratantes | Cumplimiento formal sin conducta |
| 3. Sostener el servicio por componente | 3a. Contrato de servicio entre alcaldías y la institución ejecutora (pago por servicio) | Partida en el plan operativo anual | Anualidad presupuestal |
|  | 3b. Cofinanciación de repuestos por ARL y autoridad ambiental (convenio) | Convenio con vigencia plurianual | Concentración en una fuente |
|  | 3c. Tablero a la unidad de gestión del riesgo y protocolo de calibración a la autoridad ambiental (custodia por función) | Mandato y personal designado | Capacidad insuficiente |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Futuro ambicioso.** SC-1 a SC-4 se cumplen. La teoría del cambio alcanza el impacto en forma de contribución. La sostenibilidad completa la transferencia por tramos con un motor financiero diversificado.


La {T:i103} reúne los datos de «Futuro ambicioso».

:::TABLA i103 | Futuro ambicioso
| Objetivo | Opción y mecanismo | Condición de viabilidad | Riesgo principal |
| --- | --- | --- | --- |
| 1. Extender la verificación a más sitios | 1a. Red de referencia compartida con estaciones oficiales y universidades (infraestructura común) | Acuerdos de datos y mantenimiento | Dependencia de terceros |
|  | 1b. Nodos de referencia itinerantes (movilidad) | Personal y logística | Cobertura temporal discontinua |
|  | 1c. Auditoría independiente periódica con muestreo gravimétrico (control externo) | Contratación recurrente | Costo recurrente |
| 2. Integrar alertas en las rutinas de salud y gestión del riesgo | 2a. Integración al sistema de información de las ARL (ocupacional) | Convenio e interoperabilidad | Uso limitado a empresas afiliadas |
|  | 2b. Integración al protocolo de emergencia departamental (gestión del riesgo) | Mandato departamental | Sobrecarga del protocolo |
|  | 2c. Mensajes de riesgo con guía por grupo para comunidades (comunicación) | Validación local del mensaje | Interpretación errónea del mensaje |
| 3. Consolidar el motor financiero y la transferencia completa | 3a. Fondo patrimonial o reserva de mantenimiento con rendimiento real (capital) | Rentabilidad real con fuente | Capital requerido elevado |
|  | 3b. Licenciamiento del servicio a otras entidades territoriales (ingreso propio) | Demanda de otras entidades | Competencia con servicios gratuitos |
|  | 3c. Pago por resultados ligado a disponibilidad y verificación (desempeño) | Indicadores verificables y pagador | Disputas por la medición |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Los escenarios aportan a la decisión porque muestran qué cadena se rompe en cada combinación de supuestos y qué opciones sobreviven. El análisis no asigna probabilidades a los futuros.

### F4.4-MDR.13 Valor, vacíos y consecuencias para el árbol de problemas

**Valor estratégico.** La entrega habilita una decisión previa a la compra masiva: ejecutar el diseño por tramos con evidencia o comprometerlo en bloque con un receptor supuesto. Habilita además tres trabajos. El primero es una sesión de revisión humana de los cuatro supuestos. El segundo es una lista de insumos que condicionan el uso de la recomendación. El tercero es un registro de contraste para 4.5. La utilidad es potencial. Ningún resultado observado respalda todavía la recomendación. No se afirman ahorros ni impactos medidos.

**¿Qué se me escapa?.** La tabla registra los vacíos y las contradicciones con efecto material. No se inventaron vacíos para completar el apartado.


La {T:i104} reúne los datos de «Vacíos y contradicciones con efecto material y ruta de resolución».

:::TABLA i104 | Vacíos y contradicciones con efecto material y ruta de resolución
| Vacío o contradicción | Efecto sobre la decisión | Tenedor | Vía de obtención | Plazo |
| --- | --- | --- | --- | --- |
| Términos de referencia no aportados | Impide evaluar compatibilidad, tope y tramos (CR-5) | Entidad ejecutora supuesta | Aportar el documento | NO_ESTIMADO |
| Fichas de 4.4 sin ratificación | Los supuestos SC-1 a SC-4 descansan en hipótesis estructurales | Equipo formulador | Sesión de adjudicación con acta, desde los 14 enlaces de mayor efecto | NO_ESTIMADO |
| Sin compromiso de custodios | Impide calcular la capacidad de absorción y la prueba de orfandad | Alcaldías, gobernaciones y aliados | Cartas con partida y competencia jurídica | NO_ESTIMADO |
| Costo total de sostenimiento incompleto | Impide calcular el motor financiero y el capital del fondo | Equipo formulador | Cotizar licencias, reposición y gobernanza | NO_ESTIMADO |
| Línea base de error y metas contradictorias | Impide declarar éxito del piloto | Equipo formulador | Medición con referencia y meta de los TdR | NO_ESTIMADO |
| Fórmula local del índice y umbrales | Impide que las alertas sean accionables | Autoridad de salud (POR_IDENTIFICAR) | Validación local con desenlaces | NO_ESTIMADO |
| Enlace y energía en entorno colapsado | El diseño usa enlace celular sin alterno | Empresa aliada | Diseñar enlace alterno y presupuestarlo | NO_ESTIMADO |
| Cuatro versiones de dónde se calibra | Cambia la arquitectura, el costo y el sorteo | Equipo formulador | Fijar una sola definición en el diccionario | NO_ESTIMADO |
| Desglose presupuestal que no concilia | Documenta 4.448,7 de 14.000 millones | Equipo formulador | Reconciliar el Capítulo 8 con el tope | NO_ESTIMADO |
| Participación de operarios y comunidades | Los umbrales carecen de portador de valor | Equipo formulador | Consulta antes de fijar umbrales | NO_ESTIMADO |
| Libertad de operación sobre propiedad industrial | Puede afectar la operación | Equipo formulador | Consulta de solicitudes PCT (F-INF §8.3, D-01) | Plazos de fase nacional abiertos |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


Las cuatro versiones sobre el lugar de calibración son:

- En el chip del sensor (E3-P09).
- En el gateway (E3-P15).
- En un diez por ciento de gateways (Paso 1).
- En el microcontrolador de cada nodo (Paso 6).

**Consecuencias para el árbol de problemas (4.5).** El árbol de problemas expresa estados problemáticos, causas y efectos sustentados. No invierte la teoría del cambio de forma mecánica y no añade una causa para justificar la estrategia preferida. Cada enlace conserva su evidencia o su naturaleza de hipótesis. Los códigos causales son los de las variables V01 a V15.


La {T:i105} reúne los datos de «Consecuencias para el árbol de problemas (4.5)».

:::TABLA i105 | Consecuencias para el árbol de problemas (4.5)
| Enlace de la teoría del cambio | Estado problemático candidato | Relación en S2 | Evidencia previa | Marco rival | Acción para 4.5 |
| --- | --- | --- | --- | --- | --- |
| P1, P2 hacia R1 | Error de medición no verificado (V06) | V03→V06, V02→V06, V07→V06 con peso 3; V01→V06 con 2; V04→V06 y V10→V06 con 1 | Fichas con confianza baja a media | Control en la fuente | Mantener las seis causas con su peso y su estatuto HIE |
| P1 hacia R2 | Disponibilidad y latencia insuficientes (V09, V08) | V05→V09 = 2; V08→V13 = 2; V08→V06 = 0 | Ficha V08→V06 con dominio de 0 a 2 | Ninguno | No tratar la latencia como causa de V06 sin evidencia |
| P3 hacia R3 | Índice sin fórmula local (V11) | V06→V11 = 3; V01→V11 = 3 | Vacío de la fórmula del índice | Metrología | Registrar la fórmula local como vacío, no como causa |
| R3 hacia I1 | Baja adopción institucional (V15) | V12→V15 = 2; V15 en 140 de 144 ciclos | Fichas de salida con confianza baja | Gestión del riesgo | Registrar V15 como efecto y como causa retroalimentada |
| P4 hacia I3 | Orfandad después del cierre | Sin variable en el modelo | Vacío: sin variable de resultado | Gestión del riesgo | Registrar como hipótesis fuera del modelo |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Desacuerdos que 4.5 debe conservar.** El expediente E3 afirma que la causa raíz es la arquitectura que depende de la nube. Ninguna variable de las quince representa esa arquitectura y la matriz no la deriva. 4.5 la trata como hipótesis. El expediente E3 también presenta V07 como palanca máxima. S2 la clasifica como frontera, con influencia indirecta de rango 8.

**Efectos propuestos sobre capítulos posteriores.** Los efectos son dependencias futuras. Esta salida no autoriza escribir esos capítulos.


La {T:i106} reúne los datos de «Efectos propuestos sobre capítulos posteriores».

:::TABLA i106 | Efectos propuestos sobre capítulos posteriores
| Capítulos | Efecto propuesto |
| --- | --- |
| 1, 3, 5 y 6 | Reformular el problema como estado observable, los objetivos como conversión del problema central y el método con piloto de contraste |
| 8, 10, 12, 13 y 18 | Presupuestar por tramos con reserva; tratar SC-1 a SC-4 como riesgos; ubicar metas bajo el techo y reformular como contribución las que lo exceden; construir el marco lógico desde la teoría del cambio |
| 14, 15, 16 y 21 | Sustituir la asunción de operación por las alcaldías con custodia por tramos, cláusula de apertura y portafolio verificado |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.4-MDR.


**Autorización.** Esta sección no muta la autorización contractual ni selecciona la alternativa final. La recomendación es una propuesta condicionada y no un acuerdo institucional.



## F4.5 ÁRBOL DE PROBLEMAS COMPLETO

Esta sección construye el árbol de problemas (tipo 5, rol A-PROB). Utiliza los resultados causales de 4.3 y 4.4 y el registro de contraste de F4.4-MDR. Los nodos conservan los identificadores de las quince variables del modelo. El árbol no sustituye al árbol de decisión ni al de teoría del cambio. No selecciona una alternativa. Todas las relaciones tienen estatuto HIE (hipótesis de influencia estructural): ninguna es un efecto estimado. Las fuentes se identifican con dos códigos: F-INF es el informe_FINAL de vigilancia tecnológica y F-E3 es el expediente Problematica_E3-P00.

### F4.5.1 Problema central y criterios de construcción

**Problema central.** Error de medición de PM2,5 y PM10 sin verificar frente a una referencia (V06). Se toma de dos observaciones independientes de la alternativa preferida. Primero, S2 clasifica V06 como crítica en los cinco escenarios de F4.4.13. Segundo, la construcción del fenómeno en F4.4-MDR.3 define como problema la ausencia de mediciones verificadas. El expediente E3 eligió el mismo nodo con otra matriz.

**Alcance del problema central.** El problema de F4.4-MDR.3 tiene dos partes: la medición sin verificar y la ausencia de alertas incorporadas en protocolos. El árbol representa la primera como problema central. La segunda aparece como efecto (V15) y como bucle que el árbol no dibuja.

**Criterios de construcción.**

- Cada nodo es una variable del modelo, formulada como estado problemático y rotulada con su identificador.
- Las causas se ubican debajo del problema central y los efectos encima.
- Se dibujan las relaciones de peso 2 o 3 en S2 que unen niveles contiguos sin compartir trazos ambiguos. Las demás permanecen en el registro de contraste.
- No se dibujan bucles. El registro los conserva.
- No se añade ninguna causa que el modelo no contenga. Las hipótesis externas figuran en F4.5.5.

### F4.5.2 Árbol A-PROB

El árbol tiene diez nodos y diez relaciones. El JSON canónico precede al SVG y la alternativa textual lo sigue.

El JSON canónico de A-PROB se reproduce sin cambios en el Anexo L (L.3).


La {F:aprob} reproduce «A-PROB: árbol de problemas de la vigilancia de material particulado».

:::FIGURA aprob | A-PROB: árbol de problemas de la vigilancia de material particulado | Nota. Elaboración propia con ARBOL_5_SGR_CONV56_AIRE.json. El problema central es V06; las flechas indican la dirección causa a efecto y su estatuto es HIE.

**Alternativa textual de A-PROB.**

- Árbol 5 · Árbol de problemas · rol A-PROB
- Pregunta: ¿Qué estados problemáticos, causas y efectos sustentan el error de medición sin verificar como problema central?
- Naturaleza: PROPUESTO


La {T:i107} reúne los datos de «Estados problemáticos del árbol A-PROB por nivel».

:::TABLA i107 | Estados problemáticos del árbol A-PROB por nivel
| Nivel | Nodo | Texto |
|---|---|---|
| Efectos indirectos | V14 | Personas sin protección efectiva por alertas confiables (V14) |
| Efectos indirectos | V15 | Baja adopción institucional del tablero y de las alertas (V15) |
| Efectos directos | V11 | Índice AQHI sin fórmula local validada y con error de entrada (V11) |
| Efectos directos | V12 | Tasa de falsas alarmas sin medir (V12) |
| Problema central | V06 | Error de medición de PM2,5 y PM10 sin verificar frente a una referencia (V06) |
| Causas directas | V03 | Humedad relativa alta en los sitios de remoción (V03) |
| Causas directas | V02 | Concentración de PM10 con fracción gruesa (V02) |
| Causas directas | V01 | Concentración de PM2,5 (V01) |
| Causas directas | V07 | Frecuencia de calibración de los nodos baja o nula (V07) |
| Causas indirectas | V05 | Remoción de escombros en curso (V05) |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.5.


Relaciones causa → efecto: V05 → V02; V05 → V01; V03 → V06; V02 → V06; V01 → V06; V07 → V06; V06 → V11; V06 → V12; V11 → V14; V12 → V15.

- Errores de coherencia: ninguno detectado.
- Comprobaciones del SVG original del motor (la figura del documento es una versión redibujada con la plantilla visual): xml_bien_formado=True, viewbox=True, title=True, desc_no_vacio=True, rol_declarado=True, tipo_declarado=True, colores_fuera_de_paleta=[], sin_script_enlace_imagen=True, sin_transformaciones=True, ids_unicos=True, tamano_minimo_9_5=True

**Revisión visual.** Las figuras del documento se redibujaron con la plantilla visual del proyecto a partir de los mismos datos y se revisaron como imágenes. Los textos se leen completos y ningún nodo se superpone.

### F4.5.3 Nodos y relaciones con su evidencia

**Nodos.**


La {T:i108} reúne los datos de «Nodos del árbol A-PROB con su evidencia».

:::TABLA i108 | Nodos del árbol A-PROB con su evidencia
| Nodo | Estado problemático | Nivel | Evidencia del estado | Naturaleza y verificación |
| --- | --- | --- | --- | --- |
| V06 | Error de medición sin verificar frente a una referencia | Problema central | La línea base es VACIO. F-E3 cita 45 % sin localizador. | DECLARADO; NO_VERIFICADO |
| V03 | Humedad relativa alta | Causa directa | F-E3 describe el entorno; sin serie medida | DECLARADO; NO_VERIFICADO |
| V02 | Concentración de PM10 con fracción gruesa | Causa directa | F-INF §3.1 (cociente PM2,5/PM10 de 0,88 en una mina); régimen distinto en escombros | INFERIDO; NO_VERIFICADO |
| V01 | Concentración de PM2,5 | Causa directa | Sin serie del territorio | VACIO |
| V07 | Frecuencia de calibración baja o nula | Causa directa | F-E3, E3-P10: los sensores aislados carecen de protocolo de ajuste dinámico | DECLARADO; NO_VERIFICADO |
| V05 | Remoción de escombros en curso | Causa indirecta | F-E3: premisa del caso | SUPUESTO por instrucción del usuario |
| V11 | Índice AQHI sin fórmula local validada | Efecto directo | F-INF §8.4 (D-05) recomienda validar un índice local | DOCUMENTADO en F-INF; fuente primaria no leída |
| V12 | Tasa de falsas alarmas sin medir | Efecto directo | F-INF §1.3 hallazgo 2: ningún documento de alertas la reporta | DOCUMENTADO en F-INF |
| V15 | Baja adopción institucional | Efecto indirecto | Sin medición de uso; el supuesto de adopción es SC-3 | SUPUESTO; NO_VERIFICADO |
| V14 | Personas sin protección efectiva por alertas confiables | Efecto indirecto | Sin variable de resultado ni línea base | VACIO |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.5.


**Relaciones dibujadas.** La columna «Peso» muestra el valor de S2 y, entre paréntesis, el dominio admisible. Todas las relaciones tienen estatuto HIE y verificación NO_VERIFICADO.


La {T:i109} reúne los datos de «Relaciones del árbol A-PROB y su fuente».

:::TABLA i109 | Relaciones del árbol A-PROB y su fuente
| Relación | Peso | Signo | Confianza | Naturaleza | Fuente principal | Explicación rival principal |
| --- | --- | --- | --- | --- | --- | --- |
| V05→V02 | 3 (2, 3) | + | ALTA | INFERIDO | F-E3, E3-P04 §12 | El rociado y los cerramientos actúan sobre V05, no sobre la relación |
| V05→V01 | 2 (2, 3) | + | MEDIA | INFERIDO | F-E3, E3-P04 §12; F-INF §1.4 | Con maquinaria eléctrica o rociado de agua el valor sería menor |
| V03→V06 | 3 (2, 3) | + | MEDIA | DOCUMENTADO | F-INF §1.3 y §3.1 (Suresh et al., 2025, p. 30, como se citó en F-INF) | La correlación de 0,73 podría reflejar covariación estacional |
| V02→V06 | 3 (2, 3) | + | MEDIA | INFERIDO | F-INF §3.1 (Suresh et al., 2025, como se citó en F-INF); F-E3, E3-P04 §12 | El inlet protegido y la limpieza programada reducen el efecto |
| V01→V06 | 2 (1, 2, 3) | + | BAJA | INFERIDO | F-E3, E3-P04 §12 | El error normalizado puede bajar al subir la concentración; signo mixto |
| V07→V06 | 3 (2, 3) | - | MEDIA | INFERIDO | F-INF §3.1 (Bang et al., 2026, pp. 6-8, como se citó en F-INF) y §11.6 | El método y la distancia a la referencia explican más que la frecuencia |
| V06→V11 | 3 (2, 3) | + | MEDIA | INFERIDO | F-E3, E3-P04 §12; F-INF §1.3 hallazgo 5 | Filtros de calidad de dato amortiguarían la propagación |
| V06→V12 | 2 (1, 2, 3) | + | MEDIA | INFERIDO | F-E3, E3-P04 §12; F-INF §1.3 hallazgo 2 | Si las alertas parten del índice agregado, el valor directo sería 0 o 1 |
| V11→V14 | 2 (1, 2, 3) | + | MEDIA | PROPUESTO | F-E3, E3-P04 §12 y E3-P18 | Un protocolo obligatorio con medidas automáticas daría 3 |
| V12→V15 | 2 (1, 2, 3) | - | MEDIA | INFERIDO | F-E3, E3-P04 §12 y E3-P18 | Si un municipio suspende el uso tras dos episodios, el valor sería 3 |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.5.


**Sensibilidad.** La perturbación de un enlace a la vez (F4.4.13) identifica a V05→V02 y V03→V06 entre los de mayor efecto sobre las clases. El enlace V07→V06, si bajara de 3 a 2, convertiría a V07 en autónoma relativa y cambiaría la clase indirecta de V10. Ningún valor recibe probabilidad.

### F4.5.4 Contraste con el árbol de problemas del expediente E3

El árbol de E3 (sección F4.5 del expediente, con sus tablas 4.6 a 4.8) se contrasta con los resultados de 4.4. La {T:i110} conserva los desacuerdos. No ajusta el problema a una solución preferida.


:::TABLA i110 | Contraste con el árbol de problemas del expediente E3
| Afirmación de F-E3 | Resultado en 4.4 (S0, S1 y S2) | Tratamiento en esta sección |
| --- | --- | --- |
| V06 es el problema central | Coincide: V06 es crítica en los cinco escenarios | Se conserva con otra matriz |
| V06 tiene TA 6 y TP 15 | S0: 6 y 13. S1: 6 y 15. S2: 8 y 13 | Los valores coinciden con S1 y dependen del escenario |
| V07 tiene rango indirecto 1,0 («pilar oculto») | S0 en A⁶: único con influencia positiva. S1: rango 3. S2: rango 8 | El rango 1,0 coincide con S0. La tabla de F-E3 combina dos matrices |
| V08 (latencia) es polo de la contradicción raíz y tiene rango 3,0 | S2: rango 15 (último). V08→V06 = 0 con dominio de 0 a 2 | No se dibuja V08 como causa de V06 |
| La causa raíz es la arquitectura que depende de la nube | Ninguna variable de las quince la representa. La matriz no la deriva | Se trata como hipótesis fuera del modelo (F4.5.5) |
| La extinción en A⁷ demuestra un grafo acíclico | Solo S0 se extingue. S2 tiene 144 ciclos simples | La extinción es propiedad de las 22 aristas de S0 |
| V12 y V15 son reactivas y forman el follaje | S2: V12 es frontera y V15 es crítica. Solo V14 es reactiva en los cinco escenarios | Se dibujan como efectos con la reserva de clase |
| V15 es solo un efecto | S2: V15 tiene cinco aristas de salida y participa en 140 de 144 ciclos | El efecto se dibuja. El bucle queda en el registro |
:::NOTA *Nota.* Elaboración propia con el expediente de la sección F4.5.


### F4.5.5 Lo que el árbol no representa

- **Bucles.** S2 contiene cuatro ciclos de dos aristas: V06 y V07, V09 y V15, V11 y V12, V14 y V15. V15 retroalimenta a V05, V07, V09, V10 y V14. El árbol no dibuja bucles.
- **Variables fuera del tronco.** V04, V08, V09, V10 y V13 no se dibujan. V04 y V10 tienen relaciones de confianza baja o de peso 1 con V06. V08 y V13 no se vinculan con V06 en S2. V09 actúa sobre V10 y sobre V15.
- **Variables latentes omitidas del modelo.** La distancia a la referencia, la edad del sensor, los episodios de humo y la precipitación no tienen identificador (4.3). Pueden alterar las relaciones dibujadas.
- **Marco rival de control en la fuente.** El árbol no representa la emisión de polvo en obra como causa. Su construcción exigiría otro problema central: la exposición, no el error de medición. Ese árbol no se construyó.
- **Hipótesis de F-E3 sin variable.** La dependencia de la nube como causa raíz no figura. Se conserva como hipótesis a contrastar con el piloto.
- **Continuidad posproyecto y morbilidad.** No existen variables en el modelo. Permanecen como hipótesis y vacíos (F4.4-MDR.13).

### F4.5.6 Estado y consecuencias

El árbol queda como borrador con vacíos. Sus relaciones requieren la sesión de adjudicación de las fichas de 4.4, comenzando por los enlaces de mayor efecto. Un cambio de ficha obliga a reconstruir solo los nodos y enlaces afectados. Esta sección no modifica las decisiones de F4.4-MDR ni selecciona la alternativa final. La formalización del problema y la generación de alternativas dependen de este árbol, pero no se ejecutan aquí.



## F4.6 Técnica de los cinco porqués

La técnica de los cinco porqués recorre la cadena de causas desde el problema central hasta una causa estructural. Cada respuesta se apoya en las relaciones del escenario S2 (sección F4.4) y en la evidencia del corpus. Ninguna respuesta afirma un efecto causal estimado. Todas son hipótesis de influencia estructural (HIE). El rol DAG de la última columna proviene de la tabla de clasificación de la sección F4.3.

La {T:t05} presenta las cinco preguntas. La quinta respuesta es una hipótesis de diseño y compite con la causa raíz que declara E3, la arquitectura dependiente de la nube. Ninguna de las 15 variables representa esa arquitectura, de modo que esta formulación la trata como hipótesis rival y no como causa raíz.

:::TABLA t05 | Aplicación de los cinco porqués a la causa crítica principal
| Nivel | Pregunta | Respuesta | Evidencia | Rol DAG (F4.3) |
| --- | --- | --- | --- | --- |
| P1 | ¿Por qué existe el problema central? | Las lecturas ópticas de PM2,5 y PM10 no se verifican frente a una referencia en los sitios de remoción (V06). | Línea base VACIO; el expediente declara NMAE superior a 45 % sin localizador | Resultado Y |
| P2 | ¿Por qué el error de lectura es alto? | La humedad relativa (V03) y la fracción gruesa (V02) alteran la respuesta óptica sin corrección local. En S2, V03→V06 = 3 y V02→V06 = 3. | Suresh et al. (2025, p. 30): correlación de 0,73 con la humedad; Bang et al. (2026, pp. 6-8): R² de menos de 0,2 a 0,81 con corrección | Predictor de Y y moderador |
| P3 | ¿Por qué no hay corrección local? | La calibración es estática o inexistente (V07→V06 = 3) y no hay referencias colocalizadas. | Murad Pedraza et al. (2026, pp. 10-11 y 13): 90,8 % de 5.076 estaciones sin plan de calibración (cálculo del analista) | Exposición X |
| P4 | ¿Por qué no se calibra en el sitio? | La calibración depende de referencias costosas, de energía y de enlace estables. La remoción (V05) degrada la disponibilidad de nodos (V05→V09 = 2) y expone los cabezales al polvo. | Ficha V05→V09 de la sección F4.4.4; Tavella et al. (2026, p. 6) | Predictor indirecto y causa de atrición |
| P5 | ¿Por qué ocurre lo anterior? | Causa raíz (hipótesis de diseño): la red de bajo costo opera sin un protocolo de calibración colocalizada y de corrección en el borde, con custodia institucional, adaptado a sitios de remoción de escombros. | INFERIDO; sin estimando identificado | No aplica (hipótesis estructural) |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (sección 10b) y el escenario S2 de la sección F4.4. Estatuto: HIE. Los valores V03→V06 y los demás son puntuaciones PROPUESTAS de la escala 0 a 3.

## F4.7 Causas priorizadas para intervención

La priorización usa el escenario de trabajo S2 con corte por mediana (influencia y dependencia con mediana de 5). La clasificación de Vester ordena variables por su posición estructural y no estima efectos. La {T:t06} reúne las cinco causas que el análisis prioriza. La variable V04 (viento) tiene influencia 8 y dependencia 0, pero es exógena. El proyecto no puede intervenir sobre ella y por eso no integra la lista.

:::TABLA t06 | Cinco causas críticas o activas priorizadas para intervención
| Código | Nombre | Influencia (TA) | Dependencia (TP) | Cuadrante (mediana) | Estatuto | Justificación | Intervención |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V06 | Error de medición IoT | 8 | 13 | critica | HIE | Problema central: mayor dependencia del sistema y crítica en los cinco escenarios. | Colocalización con referencia gravimétrica y corrección en el gateway (OE1) |
| V02 | Concentración de PM10 con fracción gruesa | 7 | 6 | critica | HIE | Influye con peso 3 sobre V06 y depende de la remoción. | Modelo con fracción gruesa e inlet protegido (OE1) |
| V15 | Adopción institucional | 7 | 7 | critica | HIE | Aparece en 140 de 144 ciclos simples del escenario; sostiene el supuesto SC-3. | Co-diseño con los comités, formación y convenios por tramo (OE3) |
| V03 | Humedad relativa | 6 | 0 | activa | HIE | Moderador de la respuesta óptica; exógena. | Modelo de corrección con interacción por humedad (OE1) |
| V05 | Volumen de escombros | 7 | 1 | activa | HIE | Fuente de PM10 y causa de atrición de nodos. | Energía y enlace redundantes, ubicación de nodos y mantenimiento (OE2) |
:::NOTA *Nota.* Elaboración propia con RESULTADOS.json de la sección F4.4, escenario S2 (semilla 20261011). Los cinco puntajes de influencia y dependencia son totales de fila y de columna de la matriz de 15 por 15. Naturaleza: CALCULADO sobre juicios PROPUESTOS.

Las tres variables críticas (V02, V06 y V15) y las dos activas (V03 y V05) coinciden con los tres objetivos específicos del proyecto. V06, V02 y V03 conducen a OE1; V05 conduce a OE2 a través de V09; V15 conduce a OE3. Esa correspondencia es un resultado de diseño: los objetivos se formularon después de la priorización y no antes.

## F4.8 Causa raíz identificada

**Formulación.** La red de bajo costo opera sin un protocolo de calibración colocalizada y de corrección en el borde. Ese protocolo debe tener custodia institucional y estar adaptado a sitios de remoción de escombros. Por ello entrega mediciones de error desconocido y reduce el uso institucional de las alertas.

**Evidencia.** Tres fuentes respaldan la formulación. Primera, Bang et al. (2026, pp. 6-8) muestran que una corrección local con estación cercana eleva el R² de menos de 0,2 a 0,81. Segunda, Murad Pedraza et al. (2026, pp. 10-11 y 13) reportan que 90,8 % de las estaciones de la red nacional propuesta serían sensores sin plan de calibración. La cifra es un cálculo del analista sobre las cifras del documento. Tercera, Suresh et al. (2025, p. 30) reportan una correlación de 0,73 entre partículas y humedad en una mina a cielo abierto.

**Clasificación de inferencia causal.** La causa raíz es una hipótesis estructural (HIE) y no un efecto estimado. Debe incluirse en el modelo como exposición X (método de corrección) y no como mecanismo, porque el proyecto la manipula por diseño. El estimando E1 es identificable solo si se ejecuta el sorteo semanal descrito en la sección F4.3.

**Validación contra las ortodoxias desmanteladas.** La formulación no depende de las creencias eliminadas en la {T:t03}. No supone inferencia en el chip del sensor, ni nodos silenciosos al 90 %, ni modelos de cizalladura. Depende de dos supuestos aún no verificados. El primero es que la corrección con colocalización generaliza a sitios de remoción (R-TEC-04). El segundo es que los comités adoptan el tablero (SC-3).

La {T:t07} registra la decisión sobre la causa raíz (nodo ND-10).

:::TABLA t07 | Registro de decisión GENESIS: ND-10 Causa raíz adoptada
| Campo | Contenido |
| --- | --- |
| NODO | ND-10 Causa raíz adoptada |
| CLASE | MAYOR. Orienta la selección de alternativas del Paso 6. |
| DECISION | Adoptar como causa raíz la ausencia de un protocolo de calibración colocalizada y corrección en el borde con custodia institucional, y tratar la arquitectura dependiente de la nube como hipótesis rival. |
| DECIDE | Equipo formulador [DATO_USUARIO: responsable de la decisión]. La propuesta proviene de la instancia analítica. |
| EXCLUYE | Declarar causa raíz una arquitectura que ninguna de las 15 variables representa. Pasar de HIE a IDC por posición en Vester o ascenso en MICMAC. |
| NODOS_BLANCOS | 3: Bang et al. (2026, pp. 6-8); Murad Pedraza et al. (2026, pp. 10-11 y 13); Suresh et al. (2025, p. 30). |
| NODOS_GRISES | 3: generalización a sitios de remoción; línea base de error propia; adopción institucional. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 1 (la cadena hasta personas protegidas permanece HIE). |
| PATRON_DOMINANTE | PR-06 (patrón emergente): causa raíz como hipótesis de diseño falsable en el piloto. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. La custodia depende de entidades cuya capacidad no se verificó. |
| ESCENA_SIMULABLE | En el mes 12, la compuerta C1 compara el NMAE y el R² del piloto con los umbrales; si no se cumplen, la hipótesis se revisa. |
| EVIDENCIA_JH_A | Tres citas del corpus con página. |
| EVIDENCIA_JH_B | Escenario S2: V06 es crítica en los cinco escenarios (sección F4.4.8). |
| CERCA_CONCEPTUAL | La causa raíz no prueba que la corrección reduzca el error en escombros. El piloto del tramo 1 lo mide. |
| ESTATUTO_CAUSAL | HIE. Ninguna afirmación EST. |
| VEREDICTO | Causa raíz adoptada como hipótesis de diseño, con la hipótesis rival registrada. |
| RAZON_DEL_DESCARTE | Se descarta la «arquitectura dependiente de la nube» como causa raíz: carece de variable que la represente en el modelo de 15 variables. |
| RESULTADO | CIERRA con vacíos declarados (generalización, línea base y adopción). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS y la ficha maestra (sección 10b).

Los pasos siguientes parten de esta hipótesis. El Paso 5 la formaliza en tres niveles y el Paso 6 genera las alternativas que la resuelven. Un último control cierra el paso: la {T:t08} verifica la completitud de las secciones.

:::TABLA t08 | Verificación de completitud del Paso 4
| Sección | Contenido exigido | Estado | Dónde |
| --- | --- | --- | --- |
| F4.1 | 15 causas con evidencia y validación territorial | Completa; evidencia con vacíos declarados; articulación territorial NO_VERIFICADO | Tablas F4.1 y F4.2 |
| F4.2 | Desmantelamiento de ortodoxias | Completa; 15 de 15 supuestos analizados | Tabla F4.3 |
| F4.3 | Estimando, DAG, DAG rivales y estatutos | Completa | Sección F4.3 |
| F4.4 | Vester y MICMAC en cinco escenarios con 105 fichas | Completa; fichas en el Anexo K | Sección F4.4 y Anexo K |
| F4.4-MDR | Metodología de decisión, teoría del cambio, sostenibilidad, premortem y escenarios | Completa | Sección F4.4-MDR |
| F4.5 | Árbol de problemas | Completa; JSON en el Anexo L | Sección F4.5 y Anexo L |
| F4.6 a F4.8 | Cinco porqués, causas priorizadas y causa raíz | Completa | Tablas F4.5 a F4.7 |
:::NOTA *Nota.* Elaboración propia. Las tablas importadas de las secciones F4.3 a F4.5 se numeran con el prefijo F4 en orden de aparición.

