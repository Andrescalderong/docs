%% PREFIJO: A
# ANEXO A. ANÁLISIS DEL PROBLEMA PÚBLICO Y DE LA ESTRUCTURA CAUSAL

Este anexo documenta el análisis que sustenta las secciones 5, 12, 13, 14 y 17 del Anexo 2 y reúne cinco componentes: la construcción del problema público, el modelo estructural de quince variables, la clasificación de variables para la inferencia causal, el árbol de problemas completo y la teoría del cambio. El anexo no sustituye ninguna sección del Anexo 2 ni agrega compromisos al proyecto, y cada resultado indica la sección que lo usa. Se separa del cuerpo del documento para conservar la claridad del Anexo 2, cuyos títulos se mantienen textuales según el numeral 10.6 de los TdR.

## A.1. Propósito, alcance y lectura del anexo

Los términos de referencia exigen un problema central con causas y efectos (Ministerio de Ciencia, Tecnología e Innovación [MinCiencias], 2026). El Anexo 2 presenta el árbol resultante y sus indicadores. Este anexo muestra cómo se obtuvo y qué límites tiene. Así permite al evaluador verificar que el diseño del proyecto responde a una estructura de causas y no a una preferencia por una solución.

Dos reglas orientan la lectura. La primera se refiere al tipo de afirmación: una hipótesis de influencia estructural (HIE) es un juicio ordinal sobre cuánto una variable condiciona a otra dentro del modelo, y no un efecto estimado con datos (Pearl y Mackenzie, 2018). Todas las relaciones de este anexo son HIE, salvo que el texto indique otra cosa.

La segunda regla se refiere al origen de los valores: los valores de influencia son juicios de formulación, cada uno con su mecanismo, su explicación rival y su nivel de confianza, y ningún panel externo los ha adjudicado; la sección A.11 propone la ruta para hacerlo.

El análisis estructural cubre el problema de medición, con quince variables. El laboratorio de modelación atiende una brecha complementaria de predicción, que la sección 5.2.2 del Anexo 2 describe y que no integra la matriz. La subsección A.10.3 trata su teoría del cambio y sus supuestos críticos. No se le asignan fichas ni valores de influencia.

La {T:t01} relaciona cada apartado con la sección del Anexo 2 que lo usa.

:::TABLA t01 | Relación entre los apartados del anexo y las secciones del Anexo 2
| Sección del Anexo 2 | Qué toma del anexo | Apartado |
| --- | --- | --- |
| 5.1 y 5.4. Problema central y árbol de problemas | Construcción del problema, árbol completo con identificadores, pesos y límites | A.2 y A.9 |
| 12. Objetivos | Separación entre lo que el proyecto controla y lo que solo contribuye | A.7 y A.10 |
| 13. Análisis de las alternativas | Condiciones bajo las cuales cambia la elección entre alternativas | A.10 |
| 14.2. Técnicas, datos y validación | Postura frente a la inferencia causal y pruebas de robustez del diseño | A.8 |
| 17. Resultados e impactos | Techo de rendición de cuentas y cadena de resultados | A.10 |
| 22. Análisis de riesgos | Supuestos críticos, señales de activación y brechas del análisis | A.10 y A.11 |
:::NOTA *Nota.* Elaboración propia con la estructura del Anexo 2.

## A.2. Construcción del problema público

El problema público se construye antes de modelar sus causas, y por eso esta sección responde cinco preguntas: qué fenómeno se observa, quién lo representa y de qué manera, qué juicios lo sostienen, qué estructura tiene y en qué dominio causal se ubica.

### A.2.1 Delimitación del fenómeno

La {T:t02} delimita el fenómeno con un campo por característica. El enunciado describe un estado observable y no una solución. La solución preferida figura aparte, como hipótesis de intervención que A.10 examina.

:::TABLA t02 | Delimitación del fenómeno que el proyecto atiende
| Campo | Contenido |
| --- | --- |
| Fenómeno observado | En los sitios de remoción de escombros posteriores al sismo, la medición de PM2,5 y PM10 con sensores de bajo costo no se verifica frente a una referencia |
| Unidad decisora | El equipo formulador diseña la propuesta y el financiador decide la asignación. Los consejos de gestión del riesgo deciden las alertas |
| Población afectada | Operarios de remoción y comunidades colindantes. La cifra se documenta en la sección 11 |
| Territorio | Manizales (Caldas) y Calarcá (Quindío), con cuatro consejos de gestión del riesgo |
| Horizonte | 24 meses de ejecución y 12 meses posteriores al cierre, en total 36 meses |
| Nivel de agregación | Nodo y semana en la medición; municipio y mes en la adopción institucional |
| Síntoma | Lecturas con error no cuantificado en el territorio. La línea base propia se mide con la colocalización del tramo 1 |
| Problema como estado observable | En los sitios de remoción no se dispone de mediciones de PM2,5 y PM10 verificadas frente a una referencia ni de alertas incorporadas en protocolos de decisión |
| Explicación propuesta | El error de medición actúa como cuello de botella estructural entre el entorno físico y las variables de decisión. Es una HIE |
| Solución preferida | Red híbrida con corrección en el gateway y gemelo digital, desplegada por tramos. Es una hipótesis de intervención |
:::NOTA *Nota.* Elaboración propia con las secciones 5 y 11 del Anexo 2. El territorio y los consejos corresponden a la formulación vigente.

### A.2.2 Representación del problema y marcos rivales

Bacchi (2009) propone preguntar cómo se representa un problema, qué supuestos sostienen esa representación, qué queda sin problematizar y qué efectos produce, y Schön y Rein (1994) señalan que cada parte interesada encuadra de manera distinta una misma situación. Ambas lecturas orientan el análisis siguiente.

El problema se representa como una limitación técnica de medición y de comunicaciones, sostenida por tres supuestos: que la causa principal es metrológica y energética, que la respuesta es tecnológica y que los consejos adoptan el tablero mientras una entidad custodia la red. Quedan sin problematizar cuatro asuntos: la emisión en la fuente, las acciones que activa la alerta, el umbral normativo aplicable y la responsabilidad de contratistas y administradoras de riesgos laborales (ARL). La emisión en la fuente deja de estar del todo sin problematizar, porque el gemelo predictivo la estima antes de una demolición, aunque el proyecto no la controla.

La representación también produce un efecto sobre los afectados. Operarios y comunidades figuran como receptores de alertas. Para reducir ese efecto, el proyecto los vincula al co-diseño de los umbrales y del protocolo en los talleres de la sección 19. La {T:t03} registra los tres marcos rivales y el tratamiento que reciben.

:::TABLA t03 | Marcos rivales del problema y su tratamiento en el proyecto
| Marco rival | Portador | Qué sostendría | Tratamiento en el proyecto |
| --- | --- | --- | --- |
| Control en la fuente y salud ocupacional | Autoridades laborales y ARL | El problema es la emisión de polvo en obra y la medición es secundaria | Fuera del alcance en cuanto a ejecutar el control. El gemelo predictivo incorpora la estimación previa de la exposición en demoliciones (A.10.3). La medición verificada es condición previa de cualquier estimación de exposición |
| Gestión del riesgo de desastres como servicio | UNGRD y puestos de mando unificado | La alerta solo existe si un protocolo de mando la activa | Se incorpora: el protocolo de alerta se co-diseña con los consejos en el objetivo específico 3 |
| Metrología y acreditación | Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM) | Solo un equipo acreditado como referencia sustenta una alerta oficial | Se atiende con verificación gravimétrica en laboratorio acreditado y validación metrológica. La acreditación del sistema como referencia oficial queda fuera del alcance |
:::NOTA *Nota.* Elaboración propia con las secciones 5.1, 14 y 19 del Anexo 2.

### A.2.3 Núcleo normativo y sistema apreciativo

Los juicios que sostienen el problema son de tres tipos, de realidad, de valor e instrumentales (Vickers, 1965), y cada uno tiene un portador: los TdR fijan el tope de 14.000 millones de pesos, la duración máxima de 24 meses y las reglas de elegibilidad (MinCiencias, 2026), y la Ley 1523 de 2012 organiza la gestión del riesgo en los territorios. La {T:t04} reúne los juicios y su tratamiento.

:::TABLA t04 | Juicios de realidad, de valor e instrumentales que sostienen el problema
| Tipo | Juicio | Portador o respaldo | Tratamiento en el proyecto |
| --- | --- | --- | --- |
| Realidad | La humedad sesga la lectura de los sensores ópticos de bajo costo | Jayaratne et al. (2018); Suresh et al. (2025) | Se contrasta con los datos del tramo 1 |
| Realidad | La corrección con una estación cercana puede elevar el ajuste de una red | Bang et al. (2026) | Se adopta como hipótesis de método y se valida fuera de muestra |
| Valor | Proteger primero a operarios y comunidades cuando se supera un umbral | Sin portador declarado | Se decide en el protocolo co-diseñado con los consejos |
| Valor | Evitar paros de obra por falsas alarmas | Contratistas de obra | Se mide con la reducción relativa de falsas alarmas (indicador R4) |
| Instrumental | La corrección local reduce el error sin degradar energía ni disponibilidad | Equipo formulador | Criterio de las compuertas C1 y C2 |
| Instrumental | Una entidad custodia la red después del mes 24 | Alianza y entidades custodias | Convenios con partida (compuerta C2) |
:::NOTA *Nota.* Elaboración propia con las secciones 5, 14 y 17 del Anexo 2.

Los dos juicios de valor sobre una misma alerta divergen. La protección inmediata y la continuidad de la obra pueden entrar en conflicto. El análisis conserva ambos y no los reconcilia por decisión de formulación. El protocolo de alerta los resuelve con los consejos, que son quienes responden por la decisión.

### A.2.4 Estructura del problema y dominio causal

Simon (1973) distingue los problemas bien estructurados de los mal estructurados según cuatro condiciones, que la {T:t05} evalúa: dos se cumplen con reserva, una se cumple y una no, de modo que el problema es parcialmente estructurado.

:::TABLA t05 | Evaluación de las cuatro condiciones de estructura del problema
| Condición | Evaluación | Evidencia |
| --- | --- | --- |
| C1. Criterio explícito para aceptar una solución | Se cumple con reserva | Las compuertas fijan R² ≥ 0,70, NRMSE ≤ 30 % y uso del tablero en al menos 50 % de los consejos. Son umbrales propuestos por el proyecto y no por una norma |
| C2. Estados y variables pertinentes identificados | Se cumple con reserva | Quince variables con diccionario. Cuatro variables relevantes quedan fuera del modelo: distancia a la referencia, edad del sensor, episodios de humo y precipitación |
| C3. Acciones disponibles identificadas | Se cumple | Cuatro alternativas evaluadas en la sección 13 |
| C4. Relación entre acciones y resultados conocida con precisión | No se cumple | Las relaciones son HIE sin datos del territorio |
:::NOTA *Nota.* Elaboración propia con las condiciones de Simon (1973) y las secciones 13 y 14 del Anexo 2.

La escala del fenómeno corresponde a un problema público y no a una dificultad individual (Mills, 1959). Sus efectos exceden el entorno de cada operario y alcanzan a las comunidades colindantes. El alcance poblacional se documenta en la sección 11.

La clasificación del dominio causal sigue a Snowden y Boone (2007) y a Glouberman y Zimmerman (2002). Se hace por partes porque cada parte tiene una naturaleza distinta. La {T:t06} muestra la clasificación y la observación que la cambiaría. La fase aguda del sismo queda fuera del alcance, de modo que no se asigna el dominio caótico.

:::TABLA t06 | Dominio causal de cada parte del problema
| Parte | Dominio | Evidencia | Observación que cambiaría la clasificación |
| --- | --- | --- | --- |
| Medición con corrección local | Complicado | La relación de causa y efecto existe y requiere análisis experto. La corrección con la estación cercana elevó el R² de menos de 0,2 a 0,81 en un caso (Bang et al., 2026). En S2, V03→V06 pesa 3 | Si el efecto de la corrección cambiara de signo entre sitios o semanas sin patrón, pasaría a complejo |
| Adopción institucional y custodia | Complejo | S2 contiene 144 ciclos simples y 140 incluyen V15 | Si los dos municipios ejecutaran una partida recurrente con protocolo firmado, pasaría a complicado |
:::NOTA *Nota.* Elaboración propia. La clasificación es una inferencia del equipo formulador. Los ciclos se explican en A.5.

## A.3. Modelo estructural de quince variables

El modelo estructural reúne quince variables en tres bloques de cinco: físico, técnico y de decisión. No se agregan ni se retiran variables durante el análisis. La {T:t07} define cada variable con su unidad. La variable V02 incluye la masa de V01 por tamaño de partícula. Una versión posterior puede redefinirla como fracción gruesa, es decir, PM10 menos PM2,5.

{{TABLA t07 variables}}

Una revisión de los 105 pares posibles de variables examinó el solapamiento de las definiciones y halló 101 pares únicos, un solapamiento definicional (V01 y V02), dos ambigüedades condicionales y una dependencia funcional; las ambigüedades se registran en A.11.

La influencia directa se valora con una escala ordinal de 0 a 3. Los valores no expresan proporciones, probabilidades ni magnitudes. La {T:t08} presenta las anclas, que se fijaron antes de puntuar. La confianza en cada valor es un eje distinto y no multiplica el peso. Cada valor se acompaña de un dominio admisible.

:::TABLA t08 | Escala ordinal de influencia directa y anclas de comparación
| Valor | Definición operacional | Ancla del caso |
| --- | --- | --- |
| 0 | Ausencia de influencia directa dentro del modelo, por frontera, definición, mediación explícita o mecanismo ausente | V11→V04: el índice mostrado en pantalla no altera el viento |
| 1 | Influencia directa débil: efecto gradual, parcial o mitigable por diseño dentro del horizonte | V03→V09: la humedad corroe y condensa, pero la carcasa hermética lo mitiga |
| 2 | Influencia directa moderada: altera el funcionamiento estándar y exige acción correctiva, sin determinarlo | V08→V13: la latencia resta una fracción del tiempo útil de aviso; la relación es aritmética pero parcial |
| 3 | Influencia directa fuerte: determina la variable destino casi de forma mecánica, sin agente intermedio | V05→V02 y V06→V11: la remoción mecánica genera PM10 y el error del sensor entra al índice sin acción humana intermedia |
:::NOTA *Nota.* Elaboración propia. El valor 0 no equivale a un dato faltante: declara la razón de la ausencia.

El equipo formulador valoró cada par en los dos sentidos, con una ficha por par, para un total de 105 fichas y 210 direcciones. Cada ficha declara el mecanismo o la razón del cero, el fundamento, el valor, la explicación rival, la confianza y el dominio admisible. El orden de las fichas se fijó al azar antes de valorar, con la semilla 20261011, y alterna pares de un mismo bloque y de bloques distintos; esa paridad es de atención y no impone simetría de valores.

De las 210 direcciones, 162 tienen valor 0 con la razón de ausencia o de mediación declarada. Las otras 48 tienen valor positivo: 25 de peso 1, 16 de peso 2 y 7 de peso 3. Cada valor es un juicio de formulación y ninguno fue adjudicado por un panel externo.

## A.4. Análisis de Vester

El método de Vester (2007) clasifica cada variable por su influencia total, que es la suma de la fila de la matriz, y su dependencia total, que es la suma de la columna. Una variable es crítica si supera la mediana en ambos ejes, activa si supera solo la de influencia, reactiva si supera solo la de dependencia y autónoma relativa si no supera ninguna; una variable que iguala un corte queda en la frontera.

### A.4.1 Escenarios de la matriz

El análisis usa cinco escenarios, que la {T:t09} resume. S2 es la matriz de trabajo y se deriva de las 105 fichas; S0 y S1 son matrices anteriores del equipo formulador que se conservan para comparar; y S3 y S4 toman el mínimo y el máximo admisible de cada vínculo y funcionan como envolventes de sensibilidad. Ninguno de los cinco predice resultados.

{{TABLA t09 escenarios}}

S2 agrega 26 vínculos que S0 codifica como cero, no elimina ninguno de los de S0 y modifica el valor de 7 vínculos heredados, todos con mecanismo declarado en las fichas. La densidad de S2, de {{CAUSAL_DENSIDAD}}, resulta de los juicios y no fue un objetivo.

### A.4.2 Matriz de trabajo S2

La {F:f01} muestra la matriz de influencia directa de S2 con sombreado por peso, y la {T:t10} la presenta con los valores exactos. La matriz tiene {{CAUSAL_ARISTAS}} vínculos no nulos, {{CAUSAL_W3}} de peso 3, {{CAUSAL_W2}} de peso 2 y {{CAUSAL_W1}} de peso 1, cuya suma de pesos es {{CAUSAL_SUMA}}.

:::FIGURA f01 | Siete vínculos de peso 3 y 16 de peso 2 concentran la influencia directa del escenario de trabajo | Nota. Elaboración propia con las 105 fichas bidireccionales. Los pesos son ordinales y las relaciones son hipótesis de influencia estructural. TA es la influencia total de la fila y TP la dependencia total de la columna. Software: Python 3 y matplotlib.

{{TABLA t10 matriz_s2}}

### A.4.3 Clasificación de las variables en S2

La {F:f02} ubica las variables en el plano de Vester de S2, con cortes por mediana en 5 en ambos ejes, y la {T:t11} detalla la influencia, la dependencia y la clase de cada una. Con ese corte, V02, V06 y V15 son críticas; V03, V04 y V05, activas; V09 y V14, reactivas; y V08 y V13, autónomas relativas, mientras que V01, V07, V10, V11 y V12 quedan en la frontera porque igualan un corte.

:::FIGURA f02 | V02, V06 y V15 quedan en el cuadrante crítico del escenario de trabajo | Nota. Elaboración propia con la matriz S2. Los cortes por mediana son 5 en ambos ejes. La clasificación describe posiciones estructurales y no acredita causalidad ni prioridad de inversión. Software: Python 3 y matplotlib.

{{TABLA t11 clases_s2}}

El contraste con la media cambia la clase de cinco variables. V01 pasa a activa, V07, V10 y V12 pasan a autónomas relativas y V11 pasa a reactiva. Por eso la clase de esas cinco variables depende del corte y no se interpreta como un rol firme. La clasificación vale solo para el escenario de trabajo.

### A.4.4 Estabilidad entre escenarios

La {F:f04} compara la clase por mediana de cada variable en los cinco escenarios, y la {T:t12} la lista. Solo tres variables conservan la clase en los cinco, V05 como activa, V06 como crítica y V14 como reactiva, y las demás cambian al variar los juicios. Esa inestabilidad limita cualquier afirmación sobre el papel de una variable concreta.

:::FIGURA f04 | Solo V05, V06 y V14 conservan su clase directa en los cinco escenarios | Nota. Elaboración propia con las matrices S0 a S4. La clase se calcula con el corte por mediana. El marco grueso marca las variables con clase estable. Software: Python 3 y matplotlib.

{{TABLA t12 clases_5esc}}

### A.4.5 Vínculos no nulos y su respaldo

La {T:t13} lista los 48 vínculos no nulos de S2 con su peso, su dominio admisible, su signo, su confianza, su mecanismo y su respaldo. Dos vínculos se apoyan en estudios publicados que cita el informe de vigilancia tecnológica, V03→V06 y V04→V01 (Equipo formulador, 2026); veintisiete se infieren de mecanismos físicos o técnicos conocidos; once son propuestas del equipo formulador; y ocho son supuestos de diseño.

La confianza es baja en 26 vínculos, media en 21 y alta en uno, y el respaldo es secundario o interno en 41, de modo que ninguna fuente primaria sustenta por sí sola un valor; esa limitación se declara en A.11. Los 162 pares restantes tienen peso 0, con la razón de ausencia o de mediación en la ficha.

{{TABLA t13 aristas}}

## A.5. Análisis de MICMAC

El método MICMAC eleva la matriz de influencia directa a potencias sucesivas (Godet, 2001). La potencia de orden k suma las influencias que viajan por recorridos de k vínculos. Así revela influencias indirectas que la matriz directa no muestra. Los recorridos miden longitud de caminos y no tiempo ni efectos causales.

El cálculo usa la misma matriz que el análisis de Vester dentro de cada escenario. No se puntúa de nuevo ni se completa por transitividad. Se calcularon las potencias exactas hasta k = 10. Una segunda implementación en hoja de cálculo reproduce las potencias de A¹ a A⁶ en S0, S1 y S2. Cinco permutaciones simultáneas de filas y columnas dan resultados idénticos.

### A.5.1 Influencia indirecta en S2

La {F:f03} compara los rangos directos con los indirectos de A¹⁰ en S2, y la {T:t14} da los valores y la clase indirecta. Las cinco primeras posiciones de influencia indirecta son V05, V04, V03, V02 y V06: V03 y V05 ganan 3,5 y 3 posiciones frente a la lectura directa, mientras que V06 y V15 pierden 3,5 y 2. En dependencia indirecta, V15 pasa del rango 5 al 1.

:::FIGURA f03 | Al considerar recorridos largos, V05 y V03 ganan posiciones de influencia y V06 y V15 las pierden | Nota. Elaboración propia con las potencias A¹ y A¹⁰ de S2. El rango 1 corresponde a la mayor influencia. Los empates comparten el promedio de sus posiciones. Software: Python 3 y matplotlib.

{{TABLA t14 micmac_s2}}

Dos variables califican como candidatas a variable oculta con un umbral de ganancia de dos o tres posiciones, V03 y V05, y ninguna lo hace con un umbral de cuatro. Ambas son exógenas o poco controlables, reciben poca influencia y alimentan cadenas largas, de modo que su ascenso describe el origen de los recorridos y no una palanca de intervención.

### A.5.2 Estabilidad de las potencias y rangos por escenario

La {T:t15} muestra el rango indirecto de cada variable en los cinco escenarios: V05 ocupa el primer lugar en S1, S2 y S3, y V06 ocupa el cuarto, quinto, séptimo y segundo lugar en S1, S2, S3 y S4. En S1, S2 y S4 las potencias no se estabilizan hasta k = 10; en S0, que no tiene ciclos, los caminos se extinguen en A⁷; y en S3 se observa periodicidad. Por eso la estabilidad observada no demuestra convergencia dinámica.

{{TABLA t15 rangos_5esc}}

### A.5.3 Ciclos y retroalimentación

S2 contiene {{CAUSAL_CICLOS}} ciclos simples de hasta siete vínculos. La {T:t16} muestra las variables que más aparecen. {{CAUSAL_CICLOS_V15}} ciclos contienen V15. Los ciclos de dos vínculos son V06↔V07, V09↔V15, V11↔V12 y V14↔V15.

{{TABLA t16 ciclos}}

La componente fuertemente conexa mayor reúne 13 variables. V03 y V04 quedan fuera porque no reciben influencia. De los 105 pares, 4 tienen vínculos en ambos sentidos, 40 tienen un solo vínculo y 61 no tienen vínculo. Tres de los cuatro pares recíprocos tienen valores distintos según el sentido. La concentración de ciclos en V15 resulta de sus cinco vínculos de salida y sus cinco de entrada. Depende de esas fichas y de sus dominios admisibles.

### A.5.4 Rutas explicativas

La {T:t17} lista, para pares seleccionados, la ruta simple de mayor producto de pesos. El producto es un índice ordinal de intensidad y no un efecto estimado. La ruta V05 → V02 → V06 → V11 → V12 → V15 explica por qué la remoción de escombros encabeza la influencia indirecta. Alcanza el resultado institucional por la cadena de medición y de índice. La ruta V15 → V05 → V02 → V06 muestra el único camino por el que el uso institucional retroalimenta la fuente.

{{TABLA t17 rutas}}

## A.6. Sensibilidad del análisis estructural

### A.6.1 Perturbación de un vínculo a la vez

El análisis evalúa {{CAUSAL_OAT}} cambios de un solo valor dentro del dominio admisible de cada vínculo incierto, y la {T:t18} lista los vínculos cuyo cambio altera las tres primeras posiciones de influencia indirecta o la clase indirecta de alguna variable. De esos cambios, 37 alteran la clase directa de alguna variable, y el mayor desplazamiento de rango es 4,5 en el plano directo y 4 en el indirecto. No se asignan probabilidades a estos cambios.

{{TABLA t18 oat}}

Los diez vínculos que alteran el orden de los primeros lugares tienen origen en variables físicas (V02 a V05). Los que mueven la clase indirecta de las variables de gobernanza son V15→V07, V15→V05, V09→V10 y V07→V06. La revisión prioritaria de las fichas debe empezar por esos vínculos.

### A.6.2 Recodificación de la escala

La {T:t19} recodifica la escala ordinal con tres conjuntos de valores, [0, 1, 2, 3], [0, 1, 3, 5] y [0, 1, 2, 4], para probar la robustez de la escala, sin aportar evidencia del territorio. Solo V10 y V11 cambian de clase directa, y los cinco primeros rangos de influencia indirecta forman el mismo conjunto en las tres codificaciones, V05, V04, V03, V02 y V06, aunque en la tercera se permutan V02, V03 y V04.

{{TABLA t19 recodificacion}}

## A.7. Hallazgos estructurales y su uso en el diseño

Los siete hallazgos siguientes valen para el escenario de trabajo y sus envolventes, y todos son HIE, de modo que ninguno se eleva a efecto causal identificado ni estimado. La {T:t20} indica la decisión de diseño del Anexo 2 con la que se relaciona cada uno.

:::TABLA t20 | Hallazgos estructurales y decisiones de diseño relacionadas
| Hallazgo | Lectura estructural | Decisión de diseño en el Anexo 2 |
| --- | --- | --- |
| 1. V06 es crítica en los cinco escenarios | Recibe de V01 a V04, V07 y V10 y transmite a V07, V09, V11, V12 y V15. Actúa como cuello de botella entre el entorno físico y las variables de decisión | El objetivo específico 1 verifica la medición antes de comprar la red completa (compuerta C1, secciones 12 y 14) |
| 2. V07 cae en la frontera de S2 | Su influencia, de 5, iguala la mediana y su rango indirecto es 8. Si V07→V06 valiera 2, V07 pasaría a autónoma relativa. La calibración no es la palanca máxima | El proyecto actúa sobre las cuatro causas directas y no solo sobre la calibración: colocalización, rotación, modelo con humedad y recalibración por umbral (sección 14) |
| 3. V08 ocupa el último lugar de influencia indirecta | La latencia es autónoma relativa y su único vínculo de salida positivo es V08→V13. Que sea un polo estructural depende de V08→V06 y de la definición de V08, y no es concluyente | La latencia no condiciona la compra de tramos. La red registra disponibilidad y pérdida de paquetes (indicador R2, sección 24) |
| 4. V15 concentra la retroalimentación | Es crítica en S2 y S4, aparece en 140 de 144 ciclos y su dependencia indirecta es la mayor. Depende de cinco vínculos de salida con confianza baja o media | Co-diseño del tablero, convenios de custodia y criterio de uso en la compuerta C1 (secciones 14, 18 y 19) |
| 5. V03, V04 y V05 encabezan la influencia indirecta | V03 y V04 no reciben influencia y V05 recibe un solo vínculo. Son fuentes de recorridos y no palancas, salvo V05 mediante decisiones institucionales | El proyecto mide humedad y concentración como entradas del modelo y no controla la fuente de polvo (sección 5.1) |
| 6. S0 se extingue en A⁷ | Es propiedad de sus 22 vínculos, que omiten entradas como V01→V11 y V02→V11 y retroalimentaciones como V15→V09. No demuestra linealidad del sistema | Se adopta S2 como matriz de trabajo y se reportan S3 y S4 como sensibilidad |
| 7. Solo V05, V06 y V14 tienen clase estable | V14, la protección de personas, es reactiva en los cinco escenarios y no actúa sobre las demás | La protección de personas se trata como contribución y no como compromiso (sección 17) |
:::NOTA *Nota.* Elaboración propia con los resultados de A.4 a A.6 y las secciones indicadas del Anexo 2.

## A.8. Clasificación de variables para la inferencia causal

La clasificación estructural aporta hipótesis de influencia y no sustituye la identificación causal (Pearl y Mackenzie, 2018). Por eso los roles de las variables se derivan del grafo y del estimando, y no de la clase de Vester. Esta sección declara el estimando antes de clasificar y evalúa si cada uno puede publicarse como efecto causal.

### A.8.1 Estimandos

La {T:t21} declara dos estimandos: el efecto de la frecuencia de calibración sobre el error de medición y el efecto de la adopción institucional sobre la protección de personas. Si algún campo carece de definición, no se publica un efecto causal.

:::TABLA t21 | Estimandos declarados y evaluación de su identificación
| Campo | E1. Efecto de la calibración sobre el error de medición | E2. Efecto de la adopción institucional |
| --- | --- | --- |
| Intervención X | Frecuencia de calibración de los nodos (V07): calibración inicial por colocalización y recalibración tras cada rotación | Adopción formal del tablero por el consejo o la alcaldía (V15) mediante acto administrativo |
| Resultado Y | V06: error normalizado (NMAE) del PM2,5 de cada nodo frente a la referencia asignada, por semana | V14: personas bajo protección efectiva |
| Población | Nodos colocalizados con una referencia, en el tramo 1 y en las rotaciones de los tramos 2 y 3 | Municipios con sitios de remoción |
| Territorio | Manizales y Calarcá | Manizales y Calarcá |
| Horizonte | 24 meses de ejecución | 36 meses: 24 de ejecución y 12 posteriores al cierre |
| Contraste causal | Nivel de calibración alto frente a bajo en el mismo nodo | Sin grupo comparable ni regla de asignación |
| Estimando | Efecto promedio en los tratados sobre el logaritmo del NMAE | No definido |
| Unidad de análisis | Nodo y semana | Municipio y mes (propuesta) |
| Resultado de la evaluación | No identificado con el diseño del proyecto. Identificable por diseño si el nivel de calibración se asignara al azar | No identificado con los insumos disponibles |
:::NOTA *Nota.* Elaboración propia. Un tercer estimando, el efecto del sistema de alerta sobre la morbilidad respiratoria, queda fuera del alcance: el modelo no tiene variable de resultado ni línea base de morbilidad.

El informe de vigilancia tecnológica propone un diseño alternado que asigna al azar cada semana el nivel de corrección y usa un panel con efectos fijos por nodo y por semana (Equipo formulador, 2026). El proyecto no incorpora ese diseño, sino que valida los modelos de corrección con colocalización, rotación y particiones fuera de muestra, como describe la sección 14.2. La decisión es coherente con el alcance, pero limita la inferencia: el efecto de la calibración sobre el error queda como hipótesis y no como efecto identificado.

### A.8.2 Roles de las variables en el grafo

Las variables se clasifican por su papel causal. Un confusor es una causa previa de la exposición y del resultado; un mediador está en el camino causal de X a Y; un colisionador es el efecto común de dos variables, y condicionar sobre él abre un camino espurio; un descendiente de X es una variable que X causa; un moderador cambia la magnitud del efecto de X sobre Y; y una variable latente no se observa. La {T:t22} asigna un rol a cada variable y una regla de ajuste, y la {F:f05} dibuja el grafo.

:::TABLA t22 | Roles de las variables en el grafo del estimando E1 y regla de ajuste
| Variable | Temporalidad respecto de X | Rol en el grafo | Caminos relevantes | Regla de ajuste |
| --- | --- | --- | --- | --- |
| V01 PM2,5 | Simultánea; independiente de X | Predictor de Y | V01→V06 (2); V05→V01→V06 | Ajustar por precisión; no es necesario para identificar con asignación aleatoria |
| V02 PM10 | Simultánea; independiente de X | Predictor de Y | V02→V06 (3); V02→V09 (1); V05→V02 | Ajustar por precisión; evitar incluir V01 y V02 si son colineales por inclusión |
| V03 Humedad | Simultánea; independiente de X | Predictor de Y y moderador | V03→V06 (3); V03→V09 (1) | Ajustar, con interacción entre X y V03 |
| V04 Viento | Simultánea; independiente de X | Predictor débil de Y | V04→V06 (1); V04→V01 y V04→V02 | Ajustar como control |
| V05 Escombros | Previa a cada semana | Predictor indirecto de Y; causa de pérdida de nodos | V05→V01 y V05→V02→V06; V05→V09 | Absorber con efectos fijos de nodo y de semana; no condicionar sobre V09 |
| V06 Error de medición | Posterior a X | Resultado Y | X→V06 (3) | No aplica |
| V07 Calibración | Asignada al inicio de la semana | Exposición X | V07→V06; V07→V08; V07→V09 | No aplica |
| V08 Latencia | Posterior a X | Descendiente de X; mediador si V08→V06 fuera positivo | V07→V08 (1) | No ajustar; con V08→V06 igual a 0 no hay camino hacia Y |
| V09 Disponibilidad | Posterior a X | Descendiente de X y colisionador (V05→V09←X) | V07→V09 (1); V05→V09 (2); V02→V09 (1) | No condicionar a los nodos activos; analizar por intención de tratar con ponderación |
| V10 Densidad | Nominal: previa; efectiva: posterior | Predictor débil (nominal); descendiente (efectiva) | V10→V06 (1); V09→V10 (3) | Usar solo la densidad nominal de diseño |
| V11 Índice local | Posterior a Y | Descendiente de Y | V06→V11 (3) | No ajustar |
| V12 Falsas alarmas | Posterior a Y | Descendiente de Y | V06→V12 (2); V11→V12 (2) | No ajustar |
| V13 Anticipación | Posterior a Y | Descendiente de Y | V08→V13 (2); V10→V13 (1) | No ajustar |
| V14 Personas alertadas | Posterior a Y | Descendiente de Y | V11→V14 (2); V13→V14 (2); V12→V14 (1) | No ajustar |
| V15 Adopción | Posterior; retroalimenta a X | Descendiente de Y; causa de X futuro si X no es aleatorio | V06→V15 (1); V12→V15 (2); V15→V07 (1) | No ajustar; riesgo de confusión dependiente del tiempo sin asignación aleatoria |
| L1 Distancia a la referencia | Previa | Latente medible | L1→V06 | Ajustar si se mide y no hay asignación aleatoria |
| L2 Edad del sensor | Previa | Latente medible; moderador | L2→V06 | Ajustar si se mide y no hay asignación aleatoria |
| L3 Episodio de humo | Simultánea | Latente; moderador | L3→V06 | Ajustar como interacción |
| L4 Precipitación | Simultánea | Latente no modelada | L4→V02, L4→V03 y L4→V05 | Declarar como amenaza a la identificación |
:::NOTA *Nota.* Elaboración propia con la matriz S2. El número entre paréntesis es el peso del vínculo. Todos los roles son HIE: ningún rol se estima con datos.

:::FIGURA f05 | Sin asignación aleatoria, tres variables no medidas abren caminos alternativos entre la calibración y el error | Nota. Elaboración propia. X es la frecuencia de calibración (V07) e Y el error de medición (V06). V03 modera el efecto de X sobre Y. Las líneas discontinuas son variables no medidas y la retroalimentación de V15 hacia X. Software: Python 3 y matplotlib.

Los efectos fijos de nodo y de semana absorben las diferencias estables entre nodos y entre semanas. El análisis por intención de tratar evalúa cada nodo según el nivel asignado y no según su operación posterior.

Con asignación aleatoria del nivel de calibración, el conjunto mínimo de ajuste sería vacío, porque X sería independiente de las causas de Y por diseño. Para ganar precisión se propondrían V03 con interacción, V01 o V02 y V04, más efectos fijos de nodo y de semana. No se incluirían V08, V09 ni las variables posteriores a Y.

### A.8.3 Grafos rivales y declaración de identificación

La {T:t23} presenta cuatro grafos rivales, cada uno con una amenaza a la identificación y el conjunto de ajuste que la neutralizaría.

:::TABLA t23 | Grafos rivales, amenaza a la identificación y resultado
| Grafo rival | Hipótesis | Amenaza | Conjunto de ajuste | Resultado de identificación |
| --- | --- | --- | --- | --- |
| R1 | La distancia a la referencia explica más del error que la calibración y los sitios cercanos reciben más recalibración | Confusión por selección de sitios (L1) | Con asignación aleatoria, ninguno; sin ella, L1 medida | Identificado con asignación aleatoria; sin ella, no identificado con los insumos disponibles |
| R2 | La edad del sensor determina la deriva y los nodos viejos reciben más recalibración | Confusión por L2 | Con asignación aleatoria, ninguno; sin ella, L2 medida | Igual que R1 |
| R3 | La pérdida de nodos por maquinaria (V05→V09) y el efecto de X sobre la energía (X→V09) abren un camino por V09 | Colisionador: condicionar a nodos activos sesga el efecto | No condicionar sobre V09; intención de tratar y ponderación inversa por disponibilidad | Identificado por intención de tratar; el efecto sobre nodos activos no se identifica |
| R4 | La adopción institucional (V15) modifica el uso de X en el tiempo | Retroalimentación que rompe la aciclicidad y la exogeneidad de X | Asignación aleatoria como regla o un instrumento válido y suficientemente fuerte | Identificado solo con asignación aleatoria cumplida o con un instrumento válido |
:::NOTA *Nota.* Elaboración propia con el grafo de la {F:f05}.

Con el diseño actual del proyecto no existe asignación aleatoria ni una referencia para todos los nodos, de modo que el efecto de E1 queda no identificado para cualquier estimación observacional; sería identificable por diseño si se asignara al azar el nivel de calibración y se cumplieran los supuestos de A.8.5. El estimando E2 no es identificable en este diseño.

### A.8.4 Estatutos de afirmación causal

La {T:t24} fija tres estatutos y el lenguaje que cada uno permite. Pasar de HIE a IDC o a EST porque una variable resulte crítica en Vester o ascienda en MICMAC no está permitido. Las 210 puntuaciones y las clases son HIE. Ninguna afirmación del proyecto alcanza el estatuto IDC o EST.

:::TABLA t24 | Estatutos de afirmación causal y lenguaje permitido
| Código | Estatuto | Lenguaje permitido |
| --- | --- | --- |
| HIE | Hipótesis de influencia estructural | «podría influir», «se prioriza como hipótesis» |
| IDC | Estimando causal identificado bajo supuestos | «el efecto es identificable si se cumplen…» |
| EST | Efecto estimado con datos y diseño | «se estimó…», con intervalo y sensibilidad |
:::NOTA *Nota.* Elaboración propia con Pearl y Mackenzie (2018).

### A.8.5 Pruebas de robustez compatibles con el diseño

El proyecto no estima efectos causales, pero sí aplica pruebas que protegen la validez de sus mediciones. La {T:t25} las relaciona con la sección donde se detallan.

:::TABLA t25 | Pruebas de robustez que el diseño contempla
| Prueba | Aplicación en el proyecto | Sección |
| --- | --- | --- |
| Plan de análisis preestablecido | Criterios de selección de sitios, métricas, reglas de dato válido y umbrales de aceptación se fijan antes del primer dato | 14.3 |
| Referencia de medición | Conjunto de referencia rotativo, con monitor beta, monitor óptico y muestreador gravimétrico, para 100 nodos y 240 muestras gravimétricas | 14.2 |
| Sincronización | El desfase de cada par nodo y referencia se estima por correlación cruzada y se corrige antes de calcular las métricas | 14.2 |
| Validación fuera de muestra | Particiones por municipio y por periodo; todas las métricas se calculan fuera de muestra | 14.2 |
| Valores atípicos | Se marcan y no se eliminan sin causa instrumental documentada | 14.2 |
| Pérdida de nodos | Una reserva de 20 nodos y un gateway absorbe las fallas por maquinaria; la pérdida se informa por tramo | 13 y 14 |
| Datos faltantes | Con completitud de pares de 75 %, el diseño ofrece 60.480 horas-nodo, y la trayectoria de horas válidas se controla cada semana | 14.2 |
| Predicción frente a causalidad | Que una variable mejore el ajuste del modelo no la convierte en causa del error | A.8 |
:::NOTA *Nota.* Elaboración propia con las secciones 13 y 14 del Anexo 2.

## A.9. Árbol de problemas completo

El árbol de problemas usa los resultados de A.4 a A.8 y conserva en sus nodos los identificadores de las variables. No selecciona una alternativa ni sustituye al árbol de objetivos de la sección 12, y todas sus relaciones son HIE.

El problema central es V06, el error de medición sin verificar, y se toma de dos observaciones independientes: V06 es crítica en los cinco escenarios de A.4, y la construcción del fenómeno en A.2 define como problema la ausencia de mediciones verificadas. El árbol sigue cinco criterios.

- Cada nodo es una variable del modelo, formulada como estado problemático y rotulada con su identificador.
- Las causas se ubican debajo del problema central y los efectos encima.
- Se dibujan las relaciones de peso 2 o 3 que unen niveles contiguos sin compartir trazos ambiguos.
- No se dibujan bucles, que se registran aparte.
- No se agrega ninguna causa que el modelo no contenga.

La {T:t26} relaciona los enunciados del árbol de la sección 5.4 con los nodos del modelo. La {F:f06} dibuja el árbol con los identificadores y los pesos. La {T:t27} da la explicación rival de cada relación dibujada.

:::TABLA t26 | Correspondencia entre el árbol de la sección 5.4 y los nodos del modelo
| Nivel | Enunciado de la sección 5.4 | Nodo | Observación |
| --- | --- | --- | --- |
| Efectos indirectos | 1.1. Población y personal de remoción sin protección efectiva ante alertas poco confiables | V14 | Mide protección efectiva sin separar la autónoma de la inducida por alerta |
| Efectos indirectos | 1.2. Baja adopción institucional del tablero y de las alertas | V15 | Variable de resultado institucional y de sostenibilidad |
| Efectos directos | 2.1. Índice local de calidad del aire sin fórmula validada y con error de entrada | V11 | La fórmula local del índice está por definir |
| Efectos directos | 2.2. Tasa de falsas alarmas sin medir | V12 | Depende del umbral del índice y del error de medición |
| Problema central | Los consejos no disponen de mediciones de PM2,5 y PM10 con error conocido | V06 | La sección 5.4 formula el estado observable; V06 es el error del sensor |
| Causas directas | 3.1. Humedad relativa alta en los sitios | V03 | Exógena; sin variable de precipitación en el modelo |
| Causas directas | 3.2. Fracción gruesa de PM10 sin corrección | V02 | V02 incluye la masa de V01 y se lee como fracción gruesa |
| Causas directas | 3.3. PM2,5 sin referencia colocalizada | V01 | V01 es la concentración de PM2,5. Su efecto sobre el error solo se cuantifica con una referencia colocalizada |
| Causas directas | 3.4. Calibración baja o nula | V07 | Variable de operación y palanca de diseño |
| Causas indirectas | 4.1. Remoción de escombros en curso | V05 | Variable de actividad; modificable por decisión institucional |
:::NOTA *Nota.* Elaboración propia con la sección 5.4 del Anexo 2 y el diccionario de variables de A.3.

:::FIGURA f06 | El error de medición sin verificar (V06) conecta cuatro causas directas con dos efectos directos | Nota. Elaboración propia con las fichas bidireccionales. El número sobre cada flecha es el peso del vínculo en S2 y el signo indica influencia negativa. Las relaciones son hipótesis de influencia estructural y no efectos estimados. Software: Python 3 y matplotlib.

{{TABLA t27 arbol_relaciones}}

El árbol de problemas inicial del equipo formulador se contrastó con los resultados estructurales: coincide en el problema central y difiere en tres puntos. La calibración no es la palanca independiente máxima; la latencia no es un polo estructural de la contradicción de fondo; y la adopción institucional no es solo un efecto, porque retroalimenta a la fuente y a la calibración.

El árbol no representa seis elementos.

- **Bucles.** S2 contiene cuatro ciclos de dos vínculos. V15 retroalimenta a V05, V07, V09, V10 y V14.
- **Variables fuera del tronco.** V04, V08, V09, V10 y V13 no se dibujan: V04 y V10 tienen relaciones de confianza baja o de peso 1 con V06, V08 y V13 no se vinculan con V06 en S2, y V09 actúa sobre V10 y sobre V15.
- **Variables latentes omitidas.** La distancia a la referencia, la edad del sensor, los episodios de humo y la precipitación no tienen identificador y pueden alterar las relaciones dibujadas.
- **Marco rival de control en la fuente.** Su construcción exigiría otro problema central, la exposición, y ese árbol no se construyó. El gemelo predictivo incorpora la estimación previa de ese marco sin cambiar el árbol (A.10.3).
- **Continuidad posterior al proyecto.** El modelo no contiene una variable de continuidad, y el asunto se trata en la sección 18 y en A.10.
- **Morbilidad.** No existe variable de resultado en salud. Se declara como hipótesis y no como compromiso.

## A.10. Teoría del cambio, alternativas y condiciones de decisión

### A.10.1 Alternativas y condiciones de elección

El análisis evaluó seis alternativas con criterios registrados antes de comparar. La {T:t28} las relaciona con las cuatro de la sección 13. La alternativa 1 de esa sección, la red híbrida por tramos con custodia distribuida, corresponde a R4.

:::TABLA t28 | Alternativas del análisis y su correspondencia con la sección 13
| Código | Alternativa | Correspondencia con la sección 13 |
| --- | --- | --- |
| R0 | Sin intervención: sensores aislados que transmiten hasta agotar batería o crédito | Alternativa 3, statu quo |
| R1 | Estaciones fijas robustas con paneles solares y calibración manual trimestral | Alternativa 4, estaciones fijas de referencia |
| R2 | Malla de sensores con corrección centralizada en la nube | Alternativa 2, calibración centralizada en la nube |
| R3 | Red híbrida con corrección local y transferencia a las alcaldías en el mes 25 | Variante de la alternativa 1 que supone un receptor público único |
| R4 | La misma tecnología que R3, por tramos, con piloto de contraste y custodia distribuida | Alternativa 1, seleccionada |
| R5 | Control del polvo en la fuente con medición de referencia mínima | Marco rival (A.2); no se evalúa con datos. La estimación previa se incorpora como módulo (A.10.3) |
:::NOTA *Nota.* Elaboración propia con la sección 13 del Anexo 2.

La {T:t29} compara las alternativas sin agregar los criterios. La matriz describe propiedades de diseño y no resultados medidos. Por eso la sección 13 complementa este análisis con una matriz ponderada de 14 criterios y su sensibilidad. La elección de R4 no depende de ese ponderador.

:::TABLA t29 | Matriz de compensaciones sin agregación
| Alternativa | Verificabilidad de la medición | Operación sin infraestructura estable | Continuidad sin receptor único | Corregibilidad |
| --- | --- | --- | --- | --- |
| R0 | Sin referencia ni contraste | Sin corrección; sensores aislados | Sin servicio que sostener | Sin decisión que corregir |
| R1 | Calibración manual trimestral; sin contraste previsto | Paneles y radioenlaces propios | Operación costosa; custodio no definido | Compra en bloque |
| R2 | Corrección central con datos continuos | Depende del enlace continuo | Depende de contratos de nube; custodio no definido | Compra en bloque |
| R3 | Corrección local sin diseño de contraste | Transmisión por eventos; enlace celular sin alterno | Receptor público único supuesto | Compromiso total anticipado |
| R4 | Referencia gravimétrica, colocalización y validación fuera de muestra | El piloto verifica energía y enlace antes de cada tramo; enlace satelital de respaldo | Custodia por tramos y cláusula de apertura | Decisión de continuar o detener en cada compuerta |
| R5 | No mide el error del sensor; mide exposición con referencia mínima | Poca electrónica; depende de la maquinaria | Operación por contratistas; custodio por definir | Reversible |
:::NOTA *Nota.* Elaboración propia. La matriz no produce un ganador por sí sola, porque ninguna alternativa domina a otra en todos los criterios.

No se confirma ninguna relación de dominancia entre las alternativas. Por construcción del diseño, R4 no empeora a R3 en verificabilidad, operación, continuidad ni corregibilidad, y el costo del piloto y de la gobernanza se incorpora al presupuesto de la sección 28, dentro del tope de la convocatoria. Cuatro condiciones determinan cuándo cambia la elección.

- R4 se prefiere a R3 si el costo adicional del piloto, de la gobernanza y de los tramos cabe en el tope. Debe cumplirse además que la continuidad bajo custodia distribuida no sea menos probable que bajo un receptor único.
- R3 se prefiere a R4 si, antes de la firma, cada componente cuenta con una entidad territorial con compromiso presupuestal vinculante y competencia jurídica documentada.
- R5 se combina con R4 si la evidencia de emisión en la fuente muestra que la mayor parte de la exposición es controlable. Esa evidencia no existe todavía, y las campañas del laboratorio la producirán para los eventos medidos.
- R0 solo se admite si el financiador no acepta R3 ni R4.

### A.10.2 Teoría del cambio por componente

La teoría del cambio es anidada, con una versión ejecutiva y una cadena por componente (Funnell y Rogers, 2011). La parte de medición es de dominio complicado y la de adopción y custodia es de dominio complejo, por lo que cada componente revisa sus supuestos de manera periódica. La {F:f07} muestra las cuatro cadenas, medición, alertas y adopción, custodia y predicción, y los rombos representan los seis supuestos críticos.

:::FIGURA f07 | Cuatro cadenas llevan de los productos al uso y a la continuidad, y el proyecto se compromete hasta los resultados | Nota. Elaboración propia con las secciones 12, 14 y 17 del Anexo 2. R1 a R7 son los resultados al mes 24 e I1 e I2 los impactos a 12 meses del cierre. SC-1 a SC-6 son los supuestos críticos de la {T:t30}. La flecha discontinua indica que el uso institucional justifica la custodia. Software: Python 3 y matplotlib.

La línea discontinua vertical de la figura es el techo de rendición de cuentas. Los productos y los resultados R1 a R7 quedan bajo el techo: son responsabilidad del proyecto. Los impactos I1 e I2 quedan sobre el techo, porque dependen de decisiones de los consejos y de las entidades custodias. El proyecto contribuye a ellos y fija metas con esa condición, como establece la sección 17.

Cada supuesto crítico tiene un mecanismo y una verificación dentro del proyecto, que la {T:t30} presenta. Los cuatro primeros se verifican con criterios que las compuertas C1 y C2 ya aplican antes de liberar cada compra, y los dos últimos, con los hitos H10 y H11, que no liberan compras.

:::TABLA t30 | Supuestos críticos de la teoría del cambio y su verificación en el proyecto
| Supuesto | Si | Entonces | Porque | Verificación |
| --- | --- | --- | --- | --- |
| SC-1. Medición | El modelo de corrección se valida fuera de muestra frente a la referencia colocalizada | El error normalizado cumple R² ≥ 0,70 y NRMSE ≤ 30 % | La humedad y el sesgo por tamaño de partícula explican parte del error (V03→V06 pesa 3) y la corrección los compensa | Compuertas C1 y C2; indicador R1 |
| SC-2. Energía y enlace | Los nodos conservan energía y enlace bajo maquinaria, polvo y humedad | El gemelo digital recibe datos suficientes: disponibilidad ≥ 90 % y pérdida de paquetes ≤ 10 % | La transmisión por eventos reduce el consumo y los nodos averiados se reponen (V05→V09 pesa 2) | Compuerta C2; indicador R2 |
| SC-3. Uso institucional | La autoridad valida el índice local y los umbrales, y los consejos los incorporan en sus protocolos | Las alertas inducen acciones de protección | Una alerta sin portador de decisión no modifica la conducta. V11→V14 y V13→V14 pesan 2 y son HIE | Compuerta C1 (uso en al menos 50 % de los consejos); indicadores R3 e I1 |
| SC-4. Custodia | Al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo | El servicio continúa después del mes 24 sin un receptor público único | Cada tramo exige presupuesto aprobado, personal designado y competencia jurídica documentada. Sin ellos rige la cláusula de apertura | Compuerta C2 (convenios con partida); indicadores R5 e I2 |
| SC-5. Acceso y desempeño del modelo | Se miden al menos seis eventos válidos con acceso acordado y el modelo se calibra con polvo del territorio | El gemelo alcanza FAC2 ≥ 0,5 y sesgo fraccional absoluto ≤ 0,3 fuera de muestra | La emisión depende de la distancia y del viento y se contrasta con mediciones (Dorevitch et al., 2006). El modelo se evalúa con métricas estándar (Chang y Hanna, 2004) | Hitos H10 y H11; indicador R6 |
| SC-6. Uso de la evaluación previa | La entidad territorial o el propietario solicitan la evaluación antes de demoler y la leen como insumo | Se entregan al menos 12 evaluaciones y las medidas sugeridas entran en la decisión | Una estimación sin solicitante no modifica la decisión. El protocolo define quién solicita y cómo se usa | Hito H11, acta de adopción del protocolo e indicador R7 |
:::NOTA *Nota.* Elaboración propia con las secciones 14, 17 y 24 del Anexo 2. Los umbrales de las compuertas son los de la sección 14.1.

### A.10.3 Teoría del cambio del módulo predictivo

El módulo predictivo no integra el modelo estructural de quince variables, porque no actúa sobre el error de medición. Su cadena tiene cinco eslabones: los datos de entrada, que son la geometría, el material, el método y la meteorología; los modelos de emisión y de dispersión, que producen una estimación con su incertidumbre; la evaluación previa, que la compara con los valores guía y con escenarios de control; la decisión de la entidad territorial sobre el método y las medidas; y la exposición real, que depende de lo que ejecute la obra.

La rendición de cuentas llega hasta los resultados R6 y R7. El desempeño del modelo y la entrega de las evaluaciones dependen del proyecto. La decisión de la entidad y la reducción real de la exposición quedan sobre el techo, porque dependen de terceros. El proyecto no estima efectos en la salud. El efecto esperado de una medida de control es un supuesto mientras una campaña no lo verifique. Los supuestos SC-5 y SC-6 de la {T:t30} fijan las condiciones de la cadena y los hitos H10 y H11 las verifican.

## A.11. Límites, brechas y ruta de resolución

El análisis tiene siete límites: los 210 juicios son de formulación y ninguno fue adjudicado por un panel externo; las fuentes primarias de los vínculos no se leyeron con localizador de página; la autorrevisión de las fichas no equivale a una revisión independiente; los dominios admisibles expresan incertidumbre ordinal y no probabilidad; la estabilidad observada de los rangos no demuestra convergencia dinámica; las posiciones dependen de la definición de las variables y de tres ambigüedades del diccionario; y el módulo predictivo se trata con una teoría del cambio y no con una matriz.

La {T:t31} registra las brechas, su efecto sobre las conclusiones y la ruta para resolverlas. Las rutas son propuestas de la formulación y se ejecutan con recursos ya presupuestados del proyecto, salvo que se indique otra cosa.

:::TABLA t31 | Brechas del análisis, efecto y ruta de resolución
| Brecha | Efecto sobre las conclusiones | Ruta de resolución | Responsable |
| --- | --- | --- | --- |
| Ninguna ficha fue adjudicada por un panel externo | Impide certificar la matriz y toda decisión que dependa de ella | Sesión de adjudicación con acta, que comience por los vínculos de la {T:t18} | Equipo formulador, con un panel externo de expertos |
| Fuentes primarias sin lectura con localizador | El respaldo de 41 vínculos es secundario o interno | Leer Suresh et al. (2025), Bang et al. (2026), Ayala-Parra et al. (2026) y Tavella et al. (2026) con localizador de página | Universidad |
| Variables omitidas: distancia a la referencia, edad del sensor, episodio de humo y precipitación | Pueden inflar la influencia de V03 y V07 | Evaluar la ampliación del modelo a 19 variables y rehacer A.4 y A.5 | Equipo formulador |
| Ambigüedades del diccionario: V01 y V02 por inclusión, V10 nominal o efectiva y V06 del sensor o de la red | Cambian los vínculos V06→V01, V09→V10 y V10→V06 | Aclarar el diccionario antes de ratificar las fichas | Equipo formulador |
| Fórmula local del índice de calidad del aire y salud (Stieb et al., 2008) | Los vínculos V01→V11 y V02→V11 dependen de ella | Definir la fórmula y validarla con la autoridad de salud | Municipios aliados y autoridad de salud |
| Diseño sin asignación aleatoria | El efecto de la calibración sobre el error queda como HIE | Si la alianza lo decide, asignar al azar el nivel de calibración por semana en los nodos colocalizados, con registro de la asignación | Universidad Santo Tomás |
| Gemelo predictivo sin evaluación con eventos reales al formular el proyecto | El desempeño del modelo y su dominio de validez no se conocen | Validar con al menos seis eventos y declarar el dominio (actividad 1.7) | Universidad |
| Efecto de las medidas de control sin evidencia local | Las reducciones de emisión son supuestos | Medir el efecto cuando el contratista aplique la medida durante una campaña | Universidad y contratistas |
| Población expuesta y carga de morbilidad sin variable de resultado | El modelo no alcanza la protección de las personas | Documentar la población en la sección 11 y mantener la morbilidad como hipótesis | Universidad |
| Dependencia de los juicios durante la ejecución | Las clases pueden cambiar al ratificar las fichas | Recalcular cada trimestre las clases directa e indirecta con las fichas vigentes y registrar las variables que cambian | Gerencia del proyecto |
:::NOTA *Nota.* Elaboración propia con los resultados de A.3 a A.10.

Las mediciones del tramo 1, disponibles en el mes 12, aportan la primera línea base de error con una referencia independiente. Con ellas se actualizan los vínculos que involucran a V06 y se repite el análisis de A.4 a A.6. El equipo formulador conserva las 105 fichas, las matrices de cada escenario y las potencias exactas, y las entrega al evaluador que las solicite.
