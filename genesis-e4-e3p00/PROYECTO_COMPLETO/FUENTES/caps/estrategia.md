%% PREFIJO: X4
# Documento 1000X-04. Capítulo de estrategia

## Introducción

Este capítulo fundamenta la estrategia del proyecto con tres marcos teóricos y tres herramientas de planificación. Los marcos son la innovación por disrupción (Christensen, 2016), la gestión del cambio (Kotter, 2012) y el aprendizaje organizacional (Argyris, 1999). Las herramientas son el premortem, los escenarios y los planes de contingencia. Cada marco responde una pregunta distinta. Christensen indica dónde se ubica el proyecto frente a las soluciones existentes. Kotter ordena cómo se logra la adopción institucional. Argyris define cómo se corrigen los errores y los supuestos.

El proyecto implementa una red híbrida Edge-Cloud del Internet de las cosas (IoT) con gemelo digital. La red vigila material particulado (PM2,5 y PM10) en sitios de remoción de escombros posterremoto. Los sitios están en Caldas, Cundinamarca y Valle del Cauca (SUPUESTO). La red suma 100 nodos, 10 gateways y 3 monitores de referencia. Se despliega en tres tramos durante 24 meses. Dos compuertas, C1 en el mes 12 y C2 en el mes 17, condicionan la compra del tramo siguiente. El nivel de madurez tecnológica (TRL) pasa de 4 a 7 (PROPUESTO). El proyecto no promete efectos en salud. Promete mediciones verificadas, uso institucional y continuidad.

La base probatoria de esta estrategia presenta límites explícitos. El territorio y la alianza son SUPUESTO por instrucción del usuario. Los términos de referencia (TdR) de la Convocatoria de Emergencia, Decreto 1414 de 2026, no se aportaron, de modo que su contenido es NO_VERIFICADO. Los nombres de personas y entidades quedan como [DATO_USUARIO: nombre de la persona o de la entidad]. Toda cifra cardinal procede del libro maestro de datos del proyecto o del informe de vigilancia tecnológica y bibliometría (F-INF) con su página. Las decisiones de este capítulo son PROPUESTO y requieren ratificación. Los supuestos críticos SC-1 a SC-4 de la sección 4.4-MDR.8 cubren la medición, la energía y el enlace, el uso institucional y la custodia. Los objetivos específicos son OE1 a OE3.

El capítulo sigue seis secciones. La sección E1 posiciona el proyecto con el marco de Christensen. La sección E2 planifica la adopción con el marco de Kotter. La sección E3 diseña el aprendizaje con el marco de Argyris. La sección E4 aplica el premortem y los planes de contingencia. La sección E5 describe cuatro escenarios sin probabilidades, según la decisión DEC-F11 del registro de formulación. La sección E6 integra los tres marcos en un mapa estratégico y en un tablero de control. Los meses son relativos al acta de inicio, porque el calendario real de ejecución es VACIO. Los hitos H0 a H8 y las compuertas C1, C2 y C3 son los del cronograma del proyecto.

## E1 Posicionamiento estratégico según Christensen

### E1.1 Teoría de la innovación por disrupción

La teoría de Christensen separa dos trayectorias de innovación que exigen decisiones distintas. La innovación sostenida mejora productos existentes para clientes exigentes y sigue trayectorias de mejora predecibles (Christensen, 2016). La innovación por disrupción introduce productos más simples, más baratos o más accesibles. Estos productos rinden menos en los atributos que valora la corriente principal. Por eso atraen primero a segmentos desatendidos y mejoran después hasta competir con la oferta establecida (Christensen, 2016). La diferencia no reside en la novedad técnica. Reside en la base de competencia.

Christensen distingue dos tipos de disrupción. La disrupción de gama baja ataca la parte inferior del mercado con ofertas más económicas, suficientes para clientes a quienes la oferta establecida sobrepasa. La disrupción de mercado nuevo crea consumo donde antes no existía. Llega a personas que carecían del dinero o de la destreza para usar el producto establecido. Los dos tipos comparten un patrón. El producto nace peor en el atributo tradicional y mejor en costo, acceso o conveniencia (Christensen, 2016).

El debate sobre el alcance de la teoría enfrenta dos posiciones. Christensen (2016) sostiene que las empresas establecidas fracasan porque atienden a sus clientes más rentables y desatienden los segmentos de menor margen. Teece (1986) responde que capturar el valor de una innovación depende de los activos complementarios y del régimen de apropiabilidad. Una oferta más barata no basta. Las organizaciones combinan ideas internas y externas para crear y capturar valor (Chesbrough, 2003). La literatura de la vigilancia del aire discute un punto equivalente. Los sensores de bajo costo han ganado espacio en la gestión de la contaminación urbana (Kumar et al., 2015). Se discute hasta dónde han llegado sus aplicaciones (Morawska et al., 2018). Para el proyecto, el debate se reduce a una pregunta de desempeño: qué calidad de dato entrega un sensor barato una vez corregido.

El proyecto ocupa el lugar del entrante. La oferta establecida son las estaciones de referencia acreditadas. El Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM) las reconoce para el uso regulatorio (F-INF, §6.5). El nodo del proyecto cuesta 4,5 millones de pesos colombianos (COP). El monitor gravimétrico de referencia cuesta 85,0 millones de COP (DECLARADO, líneas E01 y E03 del presupuesto). La relación es de 18,9 a 1 (CALCULADO). El proyecto no reemplaza la referencia, sino que la usa. Tres monitores, uno por departamento, colocalizan y verifican 100 nodos, es decir, 33,3 nodos por monitor (CALCULADO).

Dos decisiones se derivan de esta lectura. Primera, la clasificación del proyecto se comprueba con evidencia de desempeño y no con el precio. Por eso las compuertas C1 y C2 usan umbrales de desempeño. Segunda, el valor del proyecto se apoya en activos complementarios (Teece, 1986). Son el protocolo de calibración, la custodia y los convenios, además del sensor. Esa apuesta coincide con la recomendación del informe de vigilancia. El informe propone competir en exactitud verificada y calibración mantenida, no en cantidad de nodos (F-INF, §6.4).

### E1.2 Clasificación del proyecto

La {T:t01} compara el proyecto con los tres tipos de innovación a partir de cinco criterios. La última columna expresa la clasificación como hipótesis de formulación (INFERIDO) y no como hecho verificado. Los costos unitarios provienen del presupuesto del proyecto (DECLARADO).

:::TABLA t01 | Clasificación del tipo de innovación del proyecto
| Criterio | Innovación sostenida | Disrupción de gama baja | Disrupción de mercado nuevo | Proyecto |
| --- | --- | --- | --- | --- |
| Mercado objetivo | Clientes actuales más exigentes | Segmento desatendido por ser menos rentable | No consumidores: personas que no podían acceder | Mercado nuevo: 12 municipios focalizados y 15 comités de gestión del riesgo sin medición con error conocido |
| Propuesta de valor | Mejor rendimiento en los atributos valorados | Suficientemente bueno a menor precio | Nueva forma de acceso y de conveniencia | Medición suficiente para decidir alertas (R² ≥ 0,70; NRMSE ≤ 30 %), con corrección en el gateway |
| Modelo de negocio | Compatible con el modelo existente | Requiere una estructura de costos diferente | Requiere un modelo completamente nuevo | Servicio público con custodia por tramos; nodo de 4,5 millones de COP frente a 85,0 millones de la referencia |
| Competencia | En los mismos atributos | En una base de competencia diferente | Sin competencia directa inicial | Estaciones de referencia y sensores sin calibrar; la base pasa de cobertura a exactitud verificada |
| Trayectoria | Mejora incremental predecible | Mejora desde abajo hacia arriba | Expansión del mercado total | Mejora desde abajo: del nodo no verificado (TRL 4) a la red verificada en entorno operativo (TRL 7) |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (identidad, solución, tramos y presupuesto) y de F-INF. Naturaleza: INFERIDO para la clasificación; DECLARADO para los costos unitarios E01 y E03. R²: coeficiente de determinación. NRMSE: error cuadrático medio normalizado. TRL: nivel de madurez tecnológica. Decimales con coma.

La tabla produce una clasificación mixta. El mercado objetivo y la trayectoria corresponden a una disrupción de mercado nuevo. La propuesta de valor y la competencia corresponden a una disrupción de gama baja. El modelo de negocio no encaja en ninguna columna, porque el proyecto no estima ingresos propios. Esa salvedad limita la analogía y se declara en el análisis siguiente.

**Análisis de clasificación.** El proyecto se clasifica como disrupción de mercado nuevo con rasgos de gama baja (INFERIDO). El argumento de mercado nuevo es el no consumo. De los 1.122 municipios de Colombia, 92 miden la calidad del aire (Rodríguez-Villamizar et al., 2022, p. 3). Solo 28 poseen estaciones utilizables para estimar la carga de mortalidad (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). Los 1.094 restantes carecen de ellas (CALCULADO: 1.122 menos 28). La cifra describe la utilidad para un fin específico, la estimación de carga, y no la utilidad para decidir alertas.

El argumento de gama baja es el desempeño. La evaluación multicriterio asigna a la estación de referencia una fiabilidad de 8 y a la red corregida una de 6. A la vez, otorga a la red corregida ventaja en costo, acceso, cobertura y escalabilidad (PROPUESTO, escala de 1 a 9). Ese patrón coincide con el descrito para el entrante (Christensen, 2016). El entrante cede el atributo tradicional y gana en los demás. El umbral de lo suficientemente bueno lo fija la Agencia de Protección Ambiental de Estados Unidos (EPA, 2021) para el uso informativo en sitio fijo. El proyecto adopta dos umbrales (PROPUESTO). El primero es un coeficiente de determinación (R²) de al menos 0,70. El segundo es un error cuadrático medio normalizado (NRMSE) de 30 % o menos.

La evidencia de que la corrección alcanza ese umbral es parcial. En Seúl, una corrección con estación cercana y 35 minutos de desfase elevó el R² de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8). En una mina a cielo abierto, la correlación entre las partículas y la humedad fue de 0,73 (Suresh et al., 2025, p. 30). Ninguno de los dos casos ocurre en sitios de remoción de escombros. La línea base propia es VACIO y se mide en el tramo 1.

Dos limitaciones acotan la clasificación. Primero, la teoría describe empresas con ingresos y márgenes, y el proyecto opera como servicio público con custodia distribuida. La aplicación es una analogía. Segundo, existe un precedente nacional de red de dos capas. El Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) integra 65 equipos acreditados y 450 sensores de bajo costo (Ruiz-Carrascal et al., 2026, pp. 3 y 8). El proyecto lleva ese diseño a territorios sin red previa y no lo inventa. La decisión es mantener la clasificación como hipótesis y revisarla en la compuerta C1 con la línea base medida.

La {F:f01} cuantifica el no consumo con las cifras del informe de vigilancia. El panel izquierdo cuenta municipios y el panel derecho cuenta estaciones.

:::FIGURA f01 | Solo 28 de 1.122 municipios cuentan con estaciones utilizables | Nota. Fuente: F-INF (Rodríguez-Villamizar et al., 2022, pp. 3 y 6; Murad Pedraza et al., 2026, pp. 5-6). Los 12 municipios focalizados provienen del libro maestro (SUPUESTO). Sin cálculo estadístico; gráfico de barras con valores exactos; matplotlib, tamaño 10 × 4,5 pulgadas. Script: cX4_figuras.py; sin semilla aleatoria.

La figura muestra la magnitud del territorio de mercado nuevo. Entre 1.122 municipios, 1.030 no miden la calidad del aire (CALCULADO: 1.122 menos 92). Los 12 municipios focalizados equivalen a 1,1 % del total (CALCULADO). Esa proporción justifica un diseño por tramos y de transferencia. El proyecto produce evidencia y protocolo replicable. No produce cobertura nacional.

La {F:f02} contrasta los atributos de la estación de referencia y de la red corregida según la evaluación multicriterio. Los puntajes son una propuesta sujeta a la ratificación del panel evaluador.

:::FIGURA f02 | La red corregida cede fiabilidad y gana costo, acceso y cobertura | Nota. Fuente: evaluación multicriterio del libro maestro (puntajes PROPUESTO, escala de 1 a 9; ALT-01 estaciones fijas de referencia; ALT-03 red híbrida con corrección en gateway). Puntaje total ponderado: ALT-01 4,33; ALT-03 5,81. Matplotlib, tamaño 10 × 7 pulgadas. Script: cX4_figuras.py; sin semilla aleatoria.

La diferencia mayor aparece en ubicuidad y escalabilidad, con cinco puntos en cada atributo. La viabilidad financiera y la accesibilidad suman tres puntos de ventaja. La referencia conserva una sola ventaja, la fiabilidad, con dos puntos. Este perfil replica la forma de la disrupción de gama baja. Por consiguiente, la estrategia debe proteger el atributo cedido, y la verificación colocalizada cumple esa función.

### E1.3 Trabajos por realizar (Jobs to be Done)

Christensen et al. (2016) proponen que las personas contratan productos para progresar en una circunstancia concreta. El trabajo por realizar (Jobs to be Done, JTBD) posee tres dimensiones: funcional, emocional y social. La dimensión funcional describe la tarea. La emocional describe cómo quiere sentirse la persona. La social describe cómo quiere ser percibida. Esta lectura desplaza la pregunta del perfil del cliente hacia la circunstancia que lo lleva a decidir.

La {T:t02} aplica las tres dimensiones a dos actores del proyecto: el comité de gestión del riesgo y el operario de remoción. Los trabajos son INFERIDO a partir de datos secundarios. Se validarán en los talleres de co-diseño.

:::TABLA t02 | Análisis de trabajos por realizar del comité de gestión del riesgo y del operario de remoción
| Dimensión | Trabajo específico | Contexto de uso | Barreras actuales | Soluciones alternativas | Respuesta del proyecto |
| --- | --- | --- | --- | --- | --- |
| Funcional del comité | Decidir si emite, mantiene o levanta una alerta por PM2,5 y PM10 | Sesión del puesto de mando ante un pico de polvo o una queja comunitaria | Sin medición con error conocido; umbrales sin validación local; alertas sin tasas de detección | Estación oficial distante; sensores sin calibrar; juicio de campo | Nodos con corrección en el gateway; tablero con índice AQHI y umbrales validados localmente |
| Emocional del comité | Decidir con confianza, sin temor a una omisión ni a una falsa alarma | Decisión con responsabilidad legal sobre la alerta | Incertidumbre sobre la calidad del dato (INFERIDO) | Postergar la decisión o aplicar el protocolo general | Rango de incertidumbre publicado y registro de cada verificación |
| Social del comité | Aparecer ante la comunidad, la constructora y la gobernación como autoridad que decide con evidencia | Reunión con constructoras y comunidad por paros de obra | Presión de las constructoras por umbrales altos (4.4-MDR.5) | Informes de terceros sin referencia común | Registro público de cambios de umbral y acta de cada decisión |
| Funcional del operario | Saber cuándo reducir o detener la actividad y cuándo reanudarla | Cuadrilla en el frente de remoción | Alerta no comprensible en sitio; regla de reanudación sin definir (VACIO) | Mascarillas N95 y criterio del supervisor | Alerta comprensible en sitio y regla de reanudación acordada con el contratista |
| Emocional del operario | Trabajar con la certeza de que el aviso es creíble | Jornada de remoción con polvo visible | Desconfianza en avisos sin referencia (INFERIDO) | Equipo de protección personal | Verificación frente a la referencia y devolución de resultados a la cuadrilla |
| Social del operario | Ser reconocido como parte de la decisión sobre los umbrales | Taller de co-diseño con la cuadrilla | Participación no registrada (VACIO) | Charlas de seguridad industrial | Taller de colaboración activa con acta firmada |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.5 y 4.4-MDR.11 y del libro maestro (M06: 3.000 mascarillas N95, DECLARADO). Naturaleza: INFERIDO; los trabajos no provienen de entrevistas. AQHI: índice de calidad del aire y salud.

La tabla separa dos actores con trabajos distintos. El comité decide sobre la alerta. El operario actúa sobre ella. Ambos comparten una barrera: la medición disponible no informa su error. La participación del operario es VACIO en el expediente. Por eso el taller de co-diseño cumple una función de evidencia además de una función social.

**Análisis JTBD del proyecto.** El trabajo central del comité es decidir una alerta con una medición defendible. El proyecto supone 15 comités de gestión del riesgo, 12 municipales y 3 departamentales, con 150 funcionarios beneficiarios directos (SUPUESTO, 10 por comité). El número de operarios en sitios monitoreados es [DATO_USUARIO: operarios de remoción en sitios monitoreados]. Los trabajos se identificaron con datos secundarios y no con entrevistas ni observación. La sección 4.4-MDR.11 describe la conducta requerida en el punto de entrega. La cuadrilla reduce o detiene la actividad al superar el umbral. El funcionario del puesto de mando valida la alerta. El informe de vigilancia añade que ninguno de los cinco documentos del corpus que describen alertas reporta detección, falsas alarmas ni anticipación (F-INF, §1.3). Ninguno de los 53 estudios de índices de calidad del aire y salud proviene de América Latina (Liao et al., 2026, pp. 6 y 8).

El debate de fondo contrapone dos formas de explicar la adopción. Christensen et al. (2016) explican la contratación de un producto por la circunstancia y el progreso buscado. Davis (1989) la explica por la utilidad y la facilidad de uso percibidas. Venkatesh et al. (2003) unifican varios modelos de aceptación e incluyen la influencia social y las condiciones facilitadoras. La tasa de adopción depende también de cinco características percibidas de la innovación (Rogers, 2003). Las dos familias no se excluyen. La primera identifica qué trabajo debe resolver el tablero. La segunda mide si el funcionario percibe que lo resuelve.

Una advertencia vale para el operario. La participación nominal, sin poder real sobre la decisión, no equivale a colaboración (Arnstein, 1969). Por eso el proyecto exige talleres de colaboración activa con acta firmada para fijar los umbrales.

Tres decisiones metodológicas se derivan del análisis. Primera, los talleres de co-diseño (actividad A3.1, semanas 12 a 36) validan o corrigen los seis trabajos de la tabla con entrevistas y observación. El protocolo propone una entrevista por comité, es decir, 15 entrevistas, y una observación de cuadrilla por departamento, es decir, tres observaciones (PROPUESTO). Las diferencias entre los trabajos inferidos y los observados se registran como la primera lección del proyecto. Segunda, el indicador PERS-E01 mide el trabajo funcional del comité. Calcula la proporción de comités con decisiones documentadas con base en el tablero, con meta de 75 % o más al mes 24. Tercera, la encuesta trimestral incluye ítems de utilidad y facilidad de uso percibidas para detectar si el trabajo se resuelve pero no se valora.

La {F:f03} resume los trabajos de los dos actores en una sola vista. Cada celda corresponde a una fila de la {T:t02}.

:::FIGURA f03 | El comité y el operario contratan la medición para decidir y protegerse con evidencia defendible | Nota. Fuente: elaboración propia a partir de la tabla de trabajos por realizar (INFERIDO; sin entrevistas). Diagrama de cajas; matplotlib, tamaño 10 × 7 pulgadas; sin datos numéricos. Script: cX4_figuras.py; sin semilla aleatoria.

El diagrama muestra que los seis trabajos convergen en un mismo insumo: una medición con error conocido. Esa convergencia concentra el riesgo del proyecto en la verificación. Si la corrección falla en la compuerta C1, los seis trabajos quedan sin resolver. La estrategia de posicionamiento depende entonces de la evidencia técnica del tramo 1.

### E1.4 Implicaciones estratégicas

La clasificación del proyecto produce consecuencias de gestión en cinco decisiones: recursos, velocidad, métricas, alianzas y comunicación. Las consecuencias se derivan del patrón de disrupción de mercado nuevo con rasgos de gama baja (Christensen, 2016). Los mercados que no existen no pueden analizarse con antelación, y conviene planificar para aprender (Christensen, 2016). Esa premisa cambia la asignación de recursos y la medición del avance.

Dos posiciones de gestión compiten en este punto. Cooper (2008) propone un proceso de etapas y compuertas, en el que cada compuerta decide con criterios definidos si el proyecto continúa. Otra postura propone ciclos breves de construcción, medición y aprendizaje, con la decisión de perseverar o girar según la evidencia (Ries, 2011). Un tercer criterio es la reversibilidad. Conviene comprometer recursos de forma que el error se detecte pronto y se corrija a bajo costo (Collingridge, 1980). El proyecto combina las tres posturas. Las compuertas C1 y C2 son el mecanismo de Cooper. La decisión de perseverar o girar sigue la lógica de Ries. La compra por tramos aplica el criterio de Collingridge.

La {T:t03} traduce esas posturas en acciones. Cada fila usa cifras del libro maestro o decisiones del registro de formulación.

:::TABLA t03 | Implicaciones de la clasificación de innovación para la gestión del proyecto
| Decisión | Implicación según el tipo de innovación | Acción estratégica |
| --- | --- | --- |
| Recursos | El desempeño depende de la verificación y no de la sofisticación del sensor | Financiar tres monitores de referencia (255,0 millones de COP) y un banco de calibración (150,0 millones de COP) antes de ampliar la red |
| Velocidad | Los mercados nuevos se descubren con el uso; el avance se condiciona a la evidencia | Desplegar 30 nodos en 12 meses y liberar la compra del tramo 2 solo si C1 se supera |
| Métricas | El umbral de lo suficientemente bueno reemplaza la precisión máxima | Medir R² ≥ 0,70 y NRMSE ≤ 30 %; medir el uso con PERS-E01 y no solo la disponibilidad |
| Alianzas | La oferta establecida controla la referencia y la acreditación | Acordar con el IDEAM y el SIATA la colocalización y el protocolo de calibración, y con la empresa tecnológica la plataforma |
| Comunicación | El producto cede exactitud absoluta y la comunicación no puede prometerla | Publicar rangos de incertidumbre y el estado de la verificación en cada lectura del tablero |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (líneas E03 y E07 del presupuesto, tramos y compuertas; DECLARADO y PROPUESTO). Naturaleza de las acciones: PROPUESTO. El acuerdo con el IDEAM y el SIATA es una intención; no existe compromiso firmado.

La tabla vincula la clasificación con decisiones verificables. Las dos primeras filas muestran que el proyecto compra evidencia antes de comprar cobertura. La tercera fila evita medir solo la disponibilidad de nodos. Una red disponible con datos de calidad desconocida no resuelve ningún trabajo de la {T:t02}. Las dos últimas filas reconocen que el IDEAM y el SIATA controlan activos que el proyecto no posee. Esos activos son la acreditación y los datos de referencia (F-INF, §6.5).

## E2 Gestión del cambio según Kotter

### E2.1 Modelo de ocho pasos de Kotter

Kotter (2012) formuló un modelo de ocho pasos para liderar el cambio organizacional. Los pasos se agrupan en tres fases. La primera crea el clima para el cambio con la urgencia, la coalición guía y la visión con su estrategia. La segunda involucra y habilita a la organización con la comunicación de la visión, el empoderamiento de la acción y las victorias de corto plazo. La tercera implementa y sostiene el cambio con la consolidación de las ganancias y el anclaje en la cultura. Omitir pasos produce solo una ilusión de velocidad (Kotter, 2012). El modelo es una secuencia y no una lista de verificación.

El debate sobre su aplicabilidad enfrenta dos posiciones. Kotter parte de una organización con una coalición de liderazgo que conduce el cambio desde arriba. Lipsky (1980) y Elmore (1979) sostienen que el resultado de una política se decide en el punto de entrega. Allí el personal de primera línea ejerce discreción, y la conducta requerida determina los recursos y las reglas. La sección 4.4-MDR.8 recoge esa tensión. No adopta el modelo de transformación organizacional planificada como marco único, porque el sistema no depende de una sola organización. Elige un marco por eslabón. Para los incentivos usa la economía política con arquitectura de decisiones. Para la habilidad y el refuerzo del personal local usa ADKAR. Para el cumplimiento del protocolo usa el ciclo de mejora continua de planificar, ejecutar, verificar y actuar (Deming, 1986).

El proyecto reconcilia las dos posiciones con una decisión de alcance. Los ocho pasos organizan el cambio dentro de la coalición del proyecto y dentro de cada comité de gestión del riesgo. Los marcos de 4.4-MDR.8 cubren los cuellos que Kotter no resuelve, es decir, quién financia la operación y qué ocurre con la rotación del personal. La estructura de tramos refuerza esa lectura. El proyecto aplica la secuencia por comité y por tramo, no una sola vez para toda la red. El tramo 1 cubre los meses 1 a 12. El tramo 2 cubre los meses 13 a 17. El tramo 3 cubre los meses 18 a 24.

La {F:f04} ubica los ocho pasos en el calendario de 24 meses. Muestra también las compuertas C1, C2 y C3. Muestra las cinco victorias tempranas, codificadas QW1 a QW5, que se detallan más adelante.

:::FIGURA f04 | Los ocho pasos de Kotter se distribuyen en 24 meses y se anclan en las compuertas | Nota. Fuente: plan de cambio de este capítulo (meses PROPUESTO), con compuertas e hitos del cronograma del libro maestro. Barras por paso y fase; rombos para las victorias tempranas QW1 a QW5; matplotlib, tamaño 10 × 7 pulgadas. Script: cX4_figuras.py; sin semilla aleatoria.

La figura muestra que los pasos se superponen. La comunicación del paso 4 y el empoderamiento del paso 5 se extienden hasta el cierre, porque cada tramo exige nuevas personas formadas. Las compuertas funcionan como puntos de control de la secuencia. Ningún tramo se libera si el paso previo carece de evidencia, y esa regla aplica la advertencia de Kotter contra la omisión de pasos.

### E2.2 Aplicación al proyecto

La {T:t04} asigna a cada paso una acción concreta, un responsable por rol, un mes y un indicador de éxito. Los meses siguen los hitos H0 a H8 del cronograma. Los responsables se nombran por rol del equipo, y los nombres de las personas son [DATO_USUARIO: nombres del equipo de ejecución].

:::TABLA t04 | Modelo de ocho pasos de Kotter aplicado al proyecto
| Paso | Nombre | Fase | Objetivo | Acción concreta | Responsable | Mes | Indicador de éxito |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Crear urgencia | Clima | Establecer la necesidad de mediciones verificadas | Presentar a los 15 comités los datos de F-INF (28 de 1.122 municipios con estaciones utilizables) y el caso del SIATA | Gerencia de proyecto y coordinación de apropiación social | 1 a 2 (H0 en el mes 2) | 15 de 15 comités con acta de sesión de apertura |
| 2 | Formar la coalición | Clima | Reunir el equipo de liderazgo | Designar por escrito los siete roles de la coalición guía y fijar su calendario de sesiones | Gerencia de proyecto | 2 a 3 | 7 de 7 roles designados con acta |
| 3 | Desarrollar la visión | Clima | Articular el futuro deseado: decidir alertas con mediciones de error conocido | Co-diseñar umbrales y protocolo de alerta con los comités (A3.1) y redactar el documento de visión | Coordinación de apropiación social y profesional en calidad del aire y salud ambiental | 3 a 9 | Protocolo y umbrales propuestos con acta firmada; 3 actividades de colaboración activa o más |
| 4 | Comunicar la visión | Habilitar | Difundir la visión a comités, custodios y comunidades | Publicar boletines trimestrales, distribuir 5.000 cartillas y realizar 9 jornadas públicas | Coordinación y profesionales de apropiación social | 3 a 24 | 29 actividades documentadas (PERS-P04); 5.000 cartillas distribuidas |
| 5 | Empoderar la acción | Habilitar | Remover las barreras de habilidad y de recursos | Formar a custodios y técnicos locales y entregar repuestos y autonomía para reponer nodos | Profesional de convenios y custodia y técnicos de campo | 6 a 24 | 20, 40 y 60 personas certificadas (PERS-E03) |
| 6 | Generar victorias tempranas | Habilitar | Demostrar progreso visible | Ejecutar las cinco victorias planificadas con su evidencia | Gerencia de proyecto | 7 a 17 | 5 de 5 victorias con evidencia |
| 7 | Consolidar las ganancias | Sostener | Acelerar y expandir con evidencia | Usar C1 y C2 para liberar los tramos 2 y 3 y reentrenar el modelo por departamento | Gerencia de proyecto y científico de datos | 12 a 19 | C1 y C2 superadas con acta; 100 nodos y 10 gateways operativos (H6) |
| 8 | Anclar en la cultura | Sostener | Institucionalizar el cambio | Firmar convenios de custodia por tramo, la cláusula de apertura y los actos que adoptan el protocolo | Profesional de convenios y custodia | 18 a 24 | Actas de entrega y cláusula firmada (H8); PERS-E01 ≥ 75 % |
:::NOTA *Nota.* Elaboración propia con datos del cronograma (hitos H0 a H8; actividades A3.1 y A3.3), del presupuesto (M04, S09) y de los indicadores PERS (metas intermedias y finales). Naturaleza: PROPUESTO. Nombres de personas: [DATO_USUARIO].

La tabla convierte el modelo en compromisos verificables. Cada indicador de éxito remite a un acta, a un hito o a un indicador PERS ya definido. El capítulo no crea cifras nuevas. Los responsables son roles con presupuesto asignado, lo que reduce el riesgo de pasos sin dueño.

**Pasos 1 a 3.** La urgencia exige evidencia creíble. El proyecto usa tres datos de F-INF. Solo 28 de 1.122 municipios cuentan con estaciones utilizables para estimar la carga (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). El 90,8 % de las 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13; cálculo del analista). El SIATA muestra que una red de dos capas opera con 65 equipos acreditados y 450 sensores de bajo costo (Ruiz-Carrascal et al., 2026, pp. 3 y 8). La presentación declara el límite de cada cifra, porque exagerar la urgencia erosiona la credibilidad que el paso 2 necesita. El informe de vigilancia modela la compra de sensores como un dilema del prisionero. En ese juego, ninguna autoridad calibra si nadie lo exige. Una regla que condicione la compra a un plan de calibración cambia el equilibrio (F-INF, §6.5). El tramo 1 cumple esa función de regla. La visión resultante es una frase verificable: los comités deciden alertas con mediciones de error conocido (PROPUESTO).

**Pasos 4 a 6.** La comunicación debe convertir la visión en práctica visible. La posibilidad de prueba y la observabilidad figuran entre las características que aceleran la adopción (Rogers, 2003). El tramo 1 ofrece la prueba a escala reducida: 30 nodos y 3 gateways en 12 meses. Las victorias tempranas ofrecen la observabilidad. El empoderamiento exige habilidad y recursos. El presupuesto asigna 150,0 millones de COP a la formación y el soporte de custodios por tramo (S09, PROPUESTO). Asigna 60,0 millones de COP a repuestos y consumibles de mantenimiento (M07, PROPUESTO). La meta de 60 personas certificadas (PERS-E03) mide la capacidad instalada. El personal de primera línea adapta las reglas a su carga de trabajo (Lipsky, 1980). Por eso el protocolo de alerta se diseña con los comités y no se impone.

**Pasos 7 y 8.** Consolidar significa decidir con evidencia y no declarar victoria antes de tiempo. La declaración prematura de victoria figura entre los errores que detienen un cambio (Kotter, 2012). Las compuertas C1 y C2 operan como el freno contra ese error. C1 exige R² de al menos 0,70 y NRMSE de 30 % o menos. Exige también uso del tablero en al menos 50 % de los comités del tramo 1. C2 exige los mismos umbrales en los tres departamentos, disponibilidad mensual de 90 % o más y convenios de custodia con partida. El paso 8 es el más expuesto. Las instituciones son las reglas del juego, formales e informales (North, 1990). Anclar el cambio exige reglas formales como convenios, actos administrativos y cláusula de apertura. El riesgo R-ORG-02, que los custodios no asuman la operación, presenta nivel ALTO y probabilidad de 50 % en el registro de riesgos.

### E2.3 Estrategia de victorias tempranas

Las victorias tempranas sostienen la credibilidad del cambio mientras los resultados finales maduran. Kotter (2012) las caracteriza con tres criterios. Una victoria es visible cuando muchas personas pueden ver el resultado. Es inequívoca cuando no admite interpretaciones alternativas. Está relacionada cuando se conecta de forma clara con el esfuerzo de cambio. Estos criterios filtran los logros que importan de los que solo ocupan espacio en un informe.

Una segunda posición advierte sobre el costo de proclamar logros. La acción con propósito produce consecuencias no anticipadas (Merton, 1936). En este proyecto, la sección 4.4-MDR.11 anticipa una de ellas, la falsa seguridad. Un sesgo residual produce lecturas bajas y las autoridades relajan la vigilancia. Una victoria declarada sin evidencia refuerza ese riesgo. La respuesta prevista es publicar rangos de incertidumbre y mantener la referencia. Por esa razón las victorias del proyecto se definen con evidencia verificable y no con percepciones.

La {T:t05} presenta las cinco victorias. Cada una incluye un mes, un indicador y una audiencia. Los meses son PROPUESTO y respetan las actividades del cronograma.

:::TABLA t05 | Victorias tempranas planificadas
| Victoria | Descripción | Mes | Indicador de éxito | Audiencia objetivo | Mecanismo de comunicación |
| --- | --- | --- | --- | --- | --- |
| QW1 | Primer nodo con dato pareado válido frente a la referencia | 7 | Al menos 1 nodo con horas-nodo válidas en PERS-R05 | Equipo del proyecto, financiador y comités del tramo 1 | Boletín técnico y vista del tablero |
| QW2 | Primera sesión de un comité con el tablero | 8 | Al menos 1 acta de comité que cita una lectura del tablero (numerador de PERS-E01) | Comités y gobernaciones de los tres departamentos | Sesión en el sitio con acta y registro fotográfico |
| QW3 | Línea base de error medida por departamento (H2) | 10 | NRMSE, R², pendiente y sesgo de línea base publicados para 3 de 3 departamentos | Comités, IDEAM y autoridades ambientales | Informe de línea base y sesión pública de presentación |
| QW4 | Primera corrección validada frente a la referencia (H3) | 12 | R² ≥ 0,70 y NRMSE ≤ 30 % en el piloto, con acta de compuerta C1 | Comités, financiador y evaluación externa | Acta de compuerta y jornada de resultados |
| QW5 | Primer convenio de custodia con partida presupuestal (H5) | 17 | Al menos 1 convenio firmado con partida identificada | Alcaldías, gobernaciones y custodios potenciales | Firma pública y cartilla del convenio |
:::NOTA *Nota.* Elaboración propia con datos del cronograma (A1.3, A1.4, A3.1, A3.2; hitos H2, H3 y H5) y de los indicadores PERS-R05 y PERS-E01. Naturaleza de los meses: PROPUESTO. Línea base de PERS-R05 y PERS-E01: VACIO hasta el tramo 1.

Las cinco victorias recorren la cadena completa del proyecto. QW1 y QW3 pertenecen a la medición. QW2 pertenece al uso. QW4 une medición y compuerta. QW5 pertenece a la custodia. La tercera victoria posee un valor especial. Cierra una línea base que hoy es VACIO, y con ella el equipo puede declarar éxito o fracaso con una cifra. Si una victoria no se logra en su mes, el equipo lo comunica a la misma audiencia. Además activa la revisión de doble bucle descrita en la sección E3.

### E2.4 Coalición guía

La coalición guía es el grupo que conduce el cambio y le otorga legitimidad. Sus miembros deben reunir cuatro atributos: poder de posición, experiencia, credibilidad y liderazgo (Kotter, 2012). Un grupo sin poder de posición no desbloquea decisiones. Un grupo sin experiencia toma decisiones erradas. Un grupo sin credibilidad no persuade. Un grupo sin liderazgo no coordina.

Dos enfoques distintos describen a los actores del proyecto. El primero compone un equipo, como propone Kotter. El segundo clasifica a quienes rodean el proyecto. Mitchell et al. (1997) identifican a los grupos de interés por su poder, su legitimidad y su urgencia. Scharpf (1997) analiza a los actores por sus capacidades y orientaciones dentro de instituciones. La sección 4.4-MDR.5 aplicó la primera clasificación. No encontró evidencia para evaluar el poder, la legitimidad ni la urgencia de las alcaldías, las constructoras ni los operarios. Solo el convocante cuenta con evidencia directa de poder.

La {T:t06} compone la coalición por roles. Los niveles de poder, credibilidad, liderazgo y experiencia son una propuesta de formulación y no una evaluación con evidencia.

:::TABLA t06 | Composición de la coalición guía por roles
| Rol | Cargo | Nombre y organización | Poder | Credibilidad | Liderazgo | Experiencia |
| --- | --- | --- | --- | --- | --- | --- |
| Patrocinador | Gerencia de proyecto con el investigador principal de la IES | [DATO_USUARIO: nombre y organización] | Alto | Alto | Alto | Gestión de proyectos y compuertas |
| Promotor técnico de medición | Especialista en metrología y científico de datos | [DATO_USUARIO: nombre y organización] | Medio | Alto | Medio | Metrología, calibración y modelo de corrección |
| Promotor técnico de red | Ingenieros IoT y de campo; ingeniero de firmware y energía | [DATO_USUARIO: nombre y organización] | Medio | Alto | Medio | Redes IoT, energía y enlace |
| Promotor usuario | Funcionario designado por un comité de gestión del riesgo | [DATO_USUARIO: nombre y organización] | Medio | Alto | Medio | Gestión del riesgo y protocolos de alerta |
| Facilitador | Coordinación de apropiación social | [DATO_USUARIO: nombre y organización] | Bajo | Medio | Alto | Co-diseño y formación |
| Enlace de custodia | Profesional de convenios y custodia | [DATO_USUARIO: nombre y organización] | Medio | Medio | Medio | Convenios y competencia jurídica |
| Aliado tecnológico | Representante de la empresa tecnológica | [DATO_USUARIO: nombre y organización] | Medio | Medio | Medio | Plataforma en la nube y operación |
:::NOTA *Nota.* Elaboración propia con los roles del presupuesto de personal (P03 a P14) y de la alianza supuesta. Naturaleza: PROPUESTO para los niveles; SUPUESTO para la alianza. IES: institución de educación superior. Nombres y organizaciones: [DATO_USUARIO].

La coalición reúne siete roles con funciones complementarias. El patrocinador combina poder y credibilidad. Los tres promotores aportan experiencia en medición, en red y en uso. El facilitador aporta liderazgo con poca autoridad formal, un perfil adecuado para el co-diseño. El enlace de custodia y el aliado tecnológico cubren los dos puntos donde el proyecto depende de terceros: la continuidad y la plataforma.

Tres reglas operan la coalición. Primera, los siete roles se designan por escrito en el acta de inicio (H0, mes 2). Segunda, la coalición revisa los supuestos críticos SC-1 a SC-4 en una sesión trimestral, como se detalla en la sección E3. Tercera, la evaluación de poder, legitimidad y urgencia de las alcaldías, las constructoras y los operarios se completa con evidencia durante el tramo 1. Hoy es NO_EVALUADO. Hasta entonces, el proyecto no clasifica a esos actores como aliados ni como obstáculos.

## E3 Aprendizaje organizacional según Argyris

### E3.1 Bucle simple y bucle doble

Argyris (1999) distingue dos tipos de aprendizaje organizacional. En el bucle simple, la organización detecta un error y corrige la acción sin cuestionar los supuestos que la guían. La pregunta que lo gobierna es si la acción se ejecuta bien. En el bucle doble, la organización cuestiona y modifica los supuestos, las normas y los objetivos. La pregunta que lo gobierna es si la acción es la correcta. La distinción se sustenta en la diferencia entre la teoría que una organización declara y la teoría que de hecho aplica (Argyris y Schön, 1978). La brecha entre ambas explica por qué una organización repite errores que sus miembros reconocen.

El debate se concentra en cuándo basta el bucle simple. Una posición fundamenta la mejora continua en ciclos de planificación, ejecución, verificación y ajuste sobre procesos estables (Deming, 1986). Schön y Rein (1994) sostienen que las controversias persistentes nacen de marcos en conflicto y no de falta de información. Corregir la acción no las resuelve. Los problemas mal estructurados carecen de un criterio definido para probar una solución (Simon, 1973). Los sistemas complicados, donde la receta se repite, difieren de los complejos, donde cada caso es distinto (Glouberman y Zimmerman, 2002).

El proyecto contiene los dos tipos de sistema. La sección 4.4-MDR.8 clasifica la medición como COMPLICADO y la adopción y la custodia como COMPLEJO. La medición admite el bucle simple. El error de los nodos se compara cada mes con la referencia y se corrige con un nuevo ciclo de calibración. La adopción y la custodia exigen el bucle doble, porque los supuestos SC-3 y SC-4 pueden resultar falsos aunque la medición funcione. La sección 4.4-MDR.11 lo establece así. Cuando los datos contradicen un supuesto, se revisan el supuesto, las metas y la teoría en uso. Cada revisión se registra como una versión nueva de la teoría del cambio.

La decisión metodológica es ligar cada bucle a un momento del cronograma. El bucle simple opera cada mes con los indicadores de resultado PERS-R01 a PERS-R06. El bucle doble opera en tres instancias. Son las compuertas C1 (mes 12) y C2 (mes 17), la sesión trimestral de supuestos y la evaluación externa.

La {F:f05} representa los dos bucles y su vínculo con las compuertas.

:::FIGURA f05 | El bucle simple corrige la acción cada mes y el bucle doble revisa los supuestos en las compuertas | Nota. Fuente: elaboración propia a partir de Argyris y Schön (1978) y de la sección 4.4-MDR.11; compuertas y evaluaciones externas del cronograma y del presupuesto (S07). Diagrama de cajas y flechas; matplotlib, tamaño 10 × 7 pulgadas; sin datos numéricos. Script: cX4_figuras.py; sin semilla aleatoria.

La figura muestra que ambos bucles comparten la misma acción y el mismo resultado. Se diferencian en lo que cuestionan. El bucle simple modifica la acción cuando el desvío supera el umbral. El bucle doble modifica los supuestos SC-1 a SC-4 cuando el desvío persiste. Esa distinción evita un error frecuente: continuar la recalibración de nodos cuando el problema reside en la hipótesis de diseño.

### E3.2 Mecanismos de aprendizaje del proyecto

La {T:t07} enumera los mecanismos de aprendizaje por tipo de bucle. Cada mecanismo incluye una frecuencia, participantes, un entregable y un vínculo con el cronograma. Las frecuencias son PROPUESTO.

:::TABLA t07 | Mecanismos de aprendizaje por tipo de bucle
| Tipo de bucle | Pregunta clave | Mecanismo | Frecuencia | Participantes | Entregable | Vínculo con el cronograma |
| --- | --- | --- | --- | --- | --- | --- |
| Simple | ¿La acción se ejecuta bien? | Retrospectiva del equipo técnico | Mensual | Especialista en metrología, científico de datos e ingenieros | Acciones de mejora registradas | Cadencia de los indicadores PERS-R |
| Simple | ¿La acción se ejecuta bien? | Revisión posterior a la acción (AAR) | Tras cada hito H0 a H8 | Equipo ampliado | Lecciones aprendidas | Hitos H0 a H8 |
| Simple | ¿La acción se ejecuta bien? | Revisión de indicadores | Mensual | Gerencia de proyecto | Informe de avance | PERS-R01 a PERS-R06 |
| Doble | ¿La acción es la correcta? | Revisión de compuerta | Meses 12, 17 y 24 | Coalición guía y comité directivo | Decisión de perseverar, ajustar o detener | Compuertas C1, C2 y C3 |
| Doble | ¿La acción es la correcta? | Sesión de reflexión sobre los supuestos SC-1 a SC-4 | Trimestral | Coalición guía | Nueva versión de la teoría del cambio | Revisión trimestral de 4.4-MDR.11 |
| Doble | ¿La acción es la correcta? | Evaluación externa independiente | Meses 12 y 24 | Evaluación externa | Recomendaciones estratégicas | Servicio S07; hito H7 en el mes 23 |
:::NOTA *Nota.* Elaboración propia con datos del cronograma (hitos y compuertas), del presupuesto (S07) y de 4.4-MDR.11. Naturaleza: PROPUESTO. AAR: revisión posterior a la acción, por sus siglas en inglés.

La tabla muestra tres mecanismos de bucle simple y tres de bucle doble, con igual peso. Los primeros son frecuentes y baratos. Los segundos son escasos y decisivos. La evaluación externa cumple una función adicional. Aporta la mirada independiente que 4.4-MDR.9 declara ausente, porque una sola instancia analítica ejecutó todas las funciones de esa sección.

Dos posiciones orientan el diseño de la evaluación. Pawson y Tilley (1997) proponen la evaluación realista, que pregunta qué funciona, para quién y en qué contexto. Patton (2011) propone la evaluación de desarrollo, que acompaña la innovación en contextos complejos y apoya su adaptación. El ciclo de construcción, medición y aprendizaje añade la decisión de perseverar o girar (Ries, 2011). La sección 4.4-MDR.11 elige una ruta por pregunta. Usa el diseño contrafactual para el efecto de la corrección. Usa la evaluación realista para la adopción. Usa el análisis de contribución para la protección de personas. El proyecto añade a esa ruta la lógica de desarrollo. Revisa cada trimestre la adopción y la custodia, y revisa cada año la medición, con corte en el mes 12.

La consecuencia es una agenda concreta. El equipo realiza 24 retrospectivas mensuales y nueve revisiones posteriores a la acción, una por hito. La coalición realiza ocho sesiones trimestrales de supuestos en 24 meses (CALCULADO a partir de la cadencia propuesta). La evaluación externa revisa el proyecto dos veces.

### E3.3 Preguntas de doble bucle

Las preguntas de doble bucle examinan el marco del proyecto y no su ejecución. Schön y Rein (1994) explican que una controversia persistente indica marcos en conflicto. Una posición contraria sostiene que quien decide con información limitada busca una solución satisfactoria y no la mejor (Simon, 1955). Más información reduce entonces la disputa. Ambas posiciones influyen en el proyecto. Cuando falta un dato, la solución es medir. Cuando dos actores leen el mismo dato de forma distinta, la solución es revisar el marco.

Un caso concreto ilustra la primera pregunta. El expediente aportado por el usuario declaraba como causa raíz una arquitectura dependiente de la nube. Ninguna de las 15 variables del análisis causal la representa, por lo que el proyecto la trata como hipótesis rival (INFERIDO). La causa raíz adoptada es otra: la red de bajo costo opera sin protocolo de calibración colocalizada ni corrección en el borde con custodia institucional. La pregunta de problema obliga a revisar esa elección con los datos del tramo 1.

La {T:t08} reúne diez preguntas con su indicador de alerta y su acción. Siete provienen del esquema general de áreas y tres de los supuestos SC-2, SC-3 y SC-4.

:::TABLA t08 | Preguntas para las revisiones de doble bucle
| Área | Pregunta de doble bucle | Indicador de alerta | Acción si hay alerta |
| --- | --- | --- | --- |
| Problema | ¿El error de medición sin verificar (V06) es el problema que los comités necesitan resolver? | La línea base del tramo 1 ya cumple R² ≥ 0,70 y NRMSE ≤ 30 % sin corrección, o los comités señalan otro problema principal | Volver a la caracterización con los comités y revisar la causa raíz frente a la hipótesis rival |
| Solución | ¿La corrección en el gateway sigue siendo la solución más apropiada? | NRMSE > 30 % en dos verificaciones consecutivas (disparador de R-TEC-01) | Evaluar una alternativa técnica en C1 y no liberar la compra del tramo 2 |
| Beneficiarios | ¿La red llega a quienes más la necesitan? | Sitios con operarios expuestos sin nodo, o perfil de usuarios distinto del planeado | Reubicar nodos y ajustar la lista de 12 municipios [DATO_USUARIO: lista de municipios] |
| Metodología (SC-1) | ¿La corrección reduce el error frente a la lectura sin corrección dinámica? | La diferencia entre ambos métodos no se distingue de cero con el sorteo completo | Revisar el diseño de la colocalización y detener la expansión en el mes 12 |
| Red y energía (SC-2) | ¿Los nodos conservan energía y enlace bajo polvo, humedad y maquinaria? | Disponibilidad mensual menor que 80 % durante tres meses consecutivos (umbral de revisión de 4.4-MDR.11) | Activar el enlace alterno y el plan de repuestos; revisar el diseño de energía |
| Uso (SC-3) | ¿Los comités incorporan los umbrales en sus protocolos? | Ningún puesto de mando incorpora los umbrales en 12 meses | Rediseñar el co-diseño con los comités y revisar la fórmula local del índice |
| Custodia (SC-4) | ¿Algún custodio demuestra capacidad de absorción antes de cada tramo? | Ningún custodio alcanza capacidad de absorción de 2 o más en el índice de 0 a 3 | Activar la cláusula de apertura y buscar un custodio académico |
| Indicadores | ¿Se mide lo que importa? | La disponibilidad cumple (≥ 90 %) pero el uso del tablero es menor que 50 % (PERS-E01) | Rediseñar el sistema de medición y sumar la evaluación de falsas alarmas (PERS-E02) |
| Equipo | ¿El equipo posee las capacidades correctas? | Retrasos recurrentes en las actividades críticas A1.3, A1.4 y A2.3 | Incorporar talento o alianzas con cargo a la reserva de contingencia |
| Entorno | ¿Cambiaron las condiciones del entorno? | Cambio en los TdR, en la norma de calidad del aire, en la TRM (+10 %) o en la administración local | Analizar el impacto y ajustar los tramos y los convenios |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.9 (refutaciones observables de SC-1 a SC-4), 4.4-MDR.11 (umbral de revisión de la disponibilidad), del registro de riesgos (disparadores de R-TEC-01 y R-FIN-01) y de los indicadores PERS. Naturaleza: PROPUESTO. TRM: tasa representativa del mercado. La meta de disponibilidad de 90 % y el umbral de revisión de 80 % tienen funciones distintas.

La tabla distingue la meta de la revisión. La meta de disponibilidad es de 90 % y activa el plan de contingencia del riesgo R-TEC-02. El umbral de 80 % durante tres meses consecutivos activa la revisión del supuesto SC-2. Esa revisión es una pregunta de doble bucle sobre el diseño de energía y enlace. Las diez preguntas se incorporan como lista de verificación de las compuertas y de las sesiones trimestrales. Ninguna alerta se resuelve con más datos si el problema es el marco.

### E3.4 Rutinas defensivas y su mitigación

Las rutinas defensivas bloquean el aprendizaje de doble bucle. Se definen como políticas y acciones que protegen a las personas de la vergüenza y de la amenaza (Argyris, 1999). A la vez, impiden identificar y eliminar las causas de ambas. Esas rutinas se apoyan en un modelo de acción que busca controlar la situación, ganar y evitar sentimientos negativos (Argyris, 1999). El resultado es información que circula filtrada.

Existen dos explicaciones rivales del fenómeno. Argyris atribuye las defensas a rutinas organizacionales y sociales que se aprenden y se refuerzan. Otra explicación atribuye los errores de juicio a heurísticas cognitivas individuales que producen sesgos sistemáticos (Tversky y Kahneman, 1974). Una tercera explica la conducta de los grupos cohesionados. La búsqueda de consenso suprime la disidencia (Janis, 1982). Las tres explicaciones convergen en una conclusión de diseño. Conviene separar la evaluación de quien ejecuta, y las contramedidas deben ser estructurales y no apelar a la buena voluntad.

La sección 4.4-MDR.9 aplicó ese criterio con una salvedad. Declaró autorrevisión, porque una sola instancia analítica ejecutó todas las funciones, y dejó la revisión humana de los cuatro supuestos como condición de aceptación. El proyecto traslada esa lógica a la ejecución. La {T:t09} identifica cinco rutinas probables en el proyecto, su manifestación, su mitigación y su responsable.

:::TABLA t09 | Rutinas defensivas probables y su mitigación
| Rutina defensiva | Manifestación en el proyecto | Estrategia de mitigación | Responsable |
| --- | --- | --- | --- |
| Evitar la retroalimentación negativa | Reportar la red como disponible cuando los datos pareados no cumplen R² ni NRMSE | Espacio protegido para reportar fallas en la retrospectiva mensual, sin sanción | Gerencia de proyecto |
| Culpar a factores externos | Atribuir la baja disponibilidad a las lluvias o a las vías (R-EXT-01) sin revisar el diseño de energía (R-TEC-02) | Análisis de causa raíz con causas internas y externas en cada revisión posterior a la acción | Ingenieros IoT y de campo |
| Defender posiciones | Sostener que la corrección en el gateway es la única opción, sin considerar la hipótesis rival | Ejercicio de abogado del diablo con la hipótesis rival antes de C1 | Facilitador de la coalición y evaluación externa |
| Información selectiva | Reportar el R² del conjunto de entrenamiento y omitir el del conjunto de validación externo (R-TEC-04) | Indicadores balanceados con meta y brecha; reporte obligatorio del conjunto externo | Científico de datos y especialista en metrología |
| Evitar el conflicto | No cuestionar la decisión de ampliar al tramo 2 ante resultados ambiguos | Registrar la discrepancia en el acta de compuerta; el patrocinador expresa primero su duda | Patrocinador |
:::NOTA *Nota.* Elaboración propia con datos del registro de riesgos (R-EXT-01, R-TEC-02, R-TEC-04) y de la sección 4.4-MDR.9. Naturaleza: INFERIDO para las manifestaciones; PROPUESTO para las mitigaciones. Responsables por rol.

Las mitigaciones comparten un rasgo: transforman la conducta defensiva en un procedimiento con registro. El acta de compuerta consigna la discrepancia. El reporte del conjunto externo impide la selección de información favorable. El abogado del diablo se ejecuta antes de la decisión y no después. El proyecto no depende de que las personas reconozcan sus defensas, sino de que el procedimiento las exponga.

### E3.5 Indicadores de aprendizaje organizacional

Un proyecto que declara aprender necesita medir ese aprendizaje. Los indicadores de capacidad de aprendizaje miden la captura de lecciones, su implementación, la rapidez de respuesta, la participación y la calidad de la reflexión. El aprendizaje se vincula con la detección y la corrección de errores, lo que invita a contar las correcciones efectivas (Argyris, 1999). Sin embargo, en contextos de innovación, la cuenta de actividades no sustituye el juicio sobre la profundidad del aprendizaje (Patton, 2011). El proyecto combina ambas posturas. Usa indicadores cuantitativos y una rúbrica cualitativa evaluada por la evaluación externa.

La {T:t10} presenta seis indicadores. Los valores de meta son de referencia, PROPUESTO, y la coalición guía los ratifica en el mes 3. La línea base es VACIO y se mide en el tramo 1.

:::TABLA t10 | Indicadores de capacidad de aprendizaje
| Indicador | Definición | Meta | Frecuencia de medición |
| --- | --- | --- | --- |
| Tasa de captura de lecciones | Lecciones documentadas ÷ hitos completados | ≥ 2 por hito (18 lecciones en los 9 hitos H0 a H8) | Trimestral |
| Tasa de implementación | Lecciones implementadas ÷ lecciones capturadas | ≥ 70 % | Semestral |
| Tiempo de respuesta a alertas | Días entre el disparador y la acción correctiva | ≤ 14 días | Continuo |
| Participación en retrospectivas | Porcentaje del equipo que participa de forma activa | ≥ 80 % | Mensual |
| Calidad de reflexión | Profundidad del análisis en una escala de 1 a 5, evaluada con rúbrica por la evaluación externa | ≥ 3,5 | Trimestral |
| Revisiones de supuestos registradas | Sesiones de revisión de SC-1 a SC-4 con nueva versión de la teoría del cambio | 8 sesiones en 24 meses (CALCULADO) | Trimestral |
:::NOTA *Nota.* Elaboración propia. Las metas de los cinco primeros indicadores son valores de referencia del metaprompt GENESIS-CTeI y su naturaleza es PROPUESTO. La meta del sexto indicador es CALCULADO a partir de la cadencia trimestral. Línea base: VACIO, se mide en el tramo 1.

La tabla separa el aprendizaje que se documenta del que se aplica. La captura mide el registro. La implementación y el tiempo de respuesta miden el efecto. La rúbrica de reflexión mide la profundidad. El sexto indicador ata el aprendizaje al ciclo de la teoría del cambio, porque una revisión de supuestos sin nueva versión no deja trazabilidad. Si la tasa de implementación cae bajo la meta durante dos semestres, la coalición revisa si el problema es de capacidad o de rutinas defensivas.

## E4 Premortem estratégico

### E4.1 Metodología del premortem

El premortem es una técnica de planificación que parte del fracaso como hecho consumado. Klein (2007) propone que el equipo imagine que el proyecto fracasó y escriba las razones. Así se revelan riesgos que el optimismo del plan oculta. A diferencia del análisis de riesgos convencional, el premortem no pregunta qué puede salir mal. Pregunta por qué salió mal. Ese cambio de pregunta legitima la disidencia dentro del equipo.

Dos posiciones se disputan el método. La gestión del riesgo normalizada, como la que describe la norma ISO 31000 (ISO, 2018), recorre un proceso. Identifica, analiza, evalúa y trata el riesgo con criterios definidos y registro formal. El premortem, en cambio, busca romper el consenso. Tversky y Kahneman (1974) explican por qué esa ruptura es necesaria: los juicios sobre probabilidad se apoyan en heurísticas que producen sesgos sistemáticos. La cohesión del grupo suprime la crítica (Janis, 1982). Las dos posiciones no compiten, porque cubren fases distintas. El registro normalizado ordena el riesgo conocido. El premortem busca el riesgo que el grupo no se atrevió a nombrar.

El proyecto cuenta con dos registros. El primero es el registro cuantitativo de 12 riesgos, con probabilidad, impacto y valor monetario esperado (EMV, por sus siglas en inglés). La suma de los EMV es de 636,5 millones de COP. La reserva de contingencia se fijó en 636,0 millones de COP por redondeo (CALCULADO). La admisibilidad de esa reserva como rubro depende de los TdR (VACIO). El segundo registro es el premortem de la sección 4.4-MDR.12, que enumera diez causas por fase de origen. Los dos registros no se solapan por completo, y por eso el capítulo los integra.

La decisión metodológica es usar cada registro para lo que mide. El registro cuantitativo alimenta las acciones preventivas y los planes de contingencia con cargo a la reserva. El premortem estratégico alimenta los procedimientos de revisión. Sus causas, como un marco mal elegido o un indicador sin responsable, no se resuelven con dinero. Las secciones E4.2 y E4.3 desarrollan esa división.

### E4.2 Ejercicio de premortem

El ejercicio sitúa al equipo en el mes 30 del calendario relativo, seis meses después del cierre del mes 24. El horizonte posproyecto de seguimiento es de 12 meses (PROPUESTO), de modo que el mes 30 cae dentro de él. En ese momento el proyecto ha fracasado. No se alcanzaron los objetivos OE1 a OE3. Los recursos se agotaron antes de tiempo. Los comités de gestión del riesgo no adoptaron el tablero. La pregunta del ejercicio es qué ocurrió.

La {T:t11} responde con las causas de fracaso del registro cuantitativo. Cada fila vincula la causa con su riesgo, su nivel, su señal de alerta temprana, su acción preventiva y su responsable por rol. La señal de alerta es el disparador que define el registro.

:::TABLA t11 | Análisis de premortem: causas de fracaso del registro de riesgos
| Categoría | Causa de fracaso | Riesgo | Nivel y probabilidad | Señal de alerta temprana | Acción preventiva | Responsable |
| --- | --- | --- | --- | --- | --- | --- |
| Técnica | La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10 | R-TEC-01 | EXTREMO; 60 % | NRMSE > 30 % en dos verificaciones consecutivas | Modelo de corrección por humedad, banco de calibración y reposición de cabezales | Especialista en metrología |
| Técnica | El modelo de corrección no generaliza entre departamentos | R-TEC-04 | ALTO; 35 % | R² < 0,70 en el conjunto de validación externo | Validación cruzada por departamento y reentrenamiento por tramo | Científico de datos |
| Técnica | Las baterías se agotan antes de 14 días sin sol y los nodos dejan de transmitir | R-TEC-02 | ALTO; 30 % | Disponibilidad mensual < 90 % | Kits solares dimensionados, modo de bajo consumo y repuestos de batería | Ingeniero de firmware |
| Técnica | La red celular falla y los gateways pierden el enlace con la nube | R-TEC-03 | ALTO; 40 % | Pérdida de paquetes > 10 % durante 72 horas | Enlace satelital de respaldo y almacenamiento local de 7 días | Ingenieros IoT |
| Adopción | Los comités no adoptan el tablero ni el protocolo | R-ORG-01 | ALTO; 40 % | Menos de 50 % de uso en el tramo 1 | Co-diseño de umbrales, formación por comité y uso piloto con registro de decisiones | Coordinación de apropiación |
| Adopción | Los custodios no asumen la operación en el posproyecto | R-ORG-02 | ALTO; 50 % | Convenio sin partida al cierre del tramo 2 | Convenios por tramo, formación de custodios y cláusula de apertura | Profesional de convenios |
| Externa | Deslizamientos o réplicas bloquean vías y retrasan la instalación | R-EXT-01 | ALTO; 50 % | Retraso de instalación > 3 semanas | Instalación en ventanas secas, técnicos locales y holgura en el cronograma | Gerencia de proyecto |
| Externa | Robo o vandalismo de nodos en sitios de remoción | R-EXT-02 | MEDIO; 40 % | Dos o más nodos perdidos en un mes | Cerramientos, custodia local por sitio y seguro de equipos de la entidad ejecutora, fuera del presupuesto SGR | Técnicos de campo |
| Recursos | La devaluación del peso encarece los equipos importados | R-FIN-01 | ALTO; 55 % | TRM supera en 10 % la de la cotización | Compra por tramo con cobertura cambiaria y cotizaciones vigentes | Gerencia de proyecto |
| Recursos | La contrapartida en especie no se certifica a tiempo | R-FIN-02 | MEDIO; 25 % | Certificación pendiente al mes 2 | Certificación de la IES y de la empresa antes del acta de inicio | Gerencia de proyecto |
| Jurídica | Una solicitud de patente de terceros afecta la libertad de operación | R-JUR-01 | MEDIO; 20 % | Solicitud con fase nacional abierta que reivindique el método | Análisis de libertad de operación y diseño alternativo del módulo afectado | Consultoría en propiedad intelectual |
| Datos | Un incidente de ciberseguridad compromete la plataforma | R-DAT-01 | MEDIO; 20 % | Hallazgo crítico en la auditoría | Pruebas de penetración, segmentación y copias de respaldo | Ingenieros de software |
:::NOTA *Nota.* Elaboración propia con datos del registro de riesgos del libro maestro (probabilidad, impacto, nivel y disparador). La probabilidad y el impacto son juicios de formulación sin frecuencia observada. TRM: tasa representativa del mercado. IES: institución de educación superior.

La tabla agrupa seis categorías de causa. Las causas técnicas son cuatro y las de adopción, externas, de recursos, jurídicas y de datos suman ocho. Cada causa presenta una señal medible, lo que permite activar la respuesta con un criterio verificable y no con una percepción. Los niveles también ordenan la atención: un riesgo EXTREMO, siete ALTOS y cuatro MEDIOS.

La literatura respalda la plausibilidad de las causas técnicas y de custodia. La humedad influye en el desempeño de un sensor de masa de partículas de bajo costo (Jayaratne et al., 2018). Calibrar ese tipo de sensor plantea retos conocidos (Giordano et al., 2021). El informe de vigilancia ubica una red en una mina y un sistema de lahares en el valle de tecnología sin negocio (F-INF, §4.6; Suresh et al., 2025; Espinoza et al., 2026). En Brasil, 16,8 % de las estaciones están inactivas o sin estado (Tavella et al., 2026, p. 6). Esos antecedentes indican que la humedad y la custodia no son riesgos marginales, y justifican que reciban la mayor atención del proyecto.

La {F:f06} muestra cuánto pesa cada riesgo en el valor monetario esperado. El orden de las barras define la prioridad de la reserva.

:::FIGURA f06 | Dos riesgos concentran 49,5 % del valor monetario esperado de la reserva | Nota. Fuente: registro de riesgos del libro maestro (EMV CALCULADO como probabilidad por impacto, en millones de COP; suma de 636,5 y reserva de 636,0 millones de COP). Barras horizontales ordenadas; el nivel se distingue por color y trama; matplotlib, tamaño 10 × 7 pulgadas. Script: cX4_figuras.py; sin semilla aleatoria.

La figura muestra una distribución concentrada. La devaluación del peso (R-FIN-01) aporta 165,0 millones de COP y la saturación de los cabezales (R-TEC-01) aporta 150,0 millones de COP. Juntas suman 315,0 millones de COP, es decir, 49,5 % del total (CALCULADO). Por categoría, el riesgo técnico pesa 36,7 % y el financiero 29,1 % (CALCULADO). La estrategia debe vigilar dos puntos con mayor atención. Son el desempeño de la corrección frente al umbral y el tipo de cambio en cada orden de compra por tramo.

La sección 4.4-MDR.12 aporta las causas que el registro cuantitativo no captura. La {T:t12} las presenta por fase de origen y las vincula con el riesgo del registro cuando existe. Las causas sin riesgo asociado carecen de EMV y no cuentan con cargo a la reserva.

:::TABLA t12 | Causas estratégicas de fracaso según el premortem de 4.4-MDR.12
| Fase de origen | Causa de fracaso | Riesgo vinculado | Señal temprana | Contención | Responsable |
| --- | --- | --- | --- | --- | --- |
| Construcción | La línea base y la meta del error no se fijaron y no se puede declarar éxito | Ninguno | Metas distintas en documentos del mismo expediente | Fijar R², NRMSE y método antes del primer hito; medir la línea base en el tramo 1 | Gerencia de proyecto y especialista en metrología |
| Entorno | Los TdR prohíben el piloto o la compra por tramos | Ninguno | Observaciones del convocante al formato | Presentar el piloto como producto de conocimiento y los tramos como evidencia de alianza ejecutable | Gerencia de proyecto |
| Actores | Las alcaldías no presupuestan la operación y el cambio de administración rompe el compromiso | R-ORG-02 | Cartas de compromiso sin partida | Acuerdos por tramos y ordenanzas como condición de recepción | Profesional de convenios y custodia |
| Encuadre | El dominio se clasificó mal y la revisión de supuestos resulta lenta o costosa | Ninguno | Ajustes frecuentes del plan sin resultado | Revisión trimestral con regla de parada | Coalición guía |
| Alternativas | La elección racionalizó una alternativa preferida | Ninguno | Criterios nuevos después de evaluar | Criterios registrados con versión y ratificación del panel evaluador | Gerencia de proyecto y evaluación externa |
| Teoría del cambio (SC-1) | La corrección local no reduce el error frente a la lectura sin corrección | R-TEC-01 y R-TEC-04 | Diferencia no distinta de cero a mitad del piloto | Detener la expansión en la compuerta C1 | Científico de datos y especialista en metrología |
| Teoría del cambio (SC-2) | Los nodos pierden energía o enlace y el gemelo no recibe datos | R-TEC-02 y R-TEC-03 | Disponibilidad bajo el umbral | Repuestos y enlace alterno | Ingenieros IoT y de campo |
| Argumento | La refutación no era observable y el fallo se detecta tarde | Ninguno | Refutaciones sin indicador | Indicadores por condición de refutación | Evaluación externa |
| Sostenibilidad | Ningún custodio alcanza capacidad de absorción 2 y la fuente principal desaparece | R-ORG-02 | Cobertura del costo mínimo menor que 100 % | Cláusula de apertura | Profesional de convenios y custodia |
| Ejecución | Los umbrales de revisión no se aplican por falta de responsable | Ninguno | Revisión trimestral omitida | Designar responsable en el acuerdo de alianza | Gerencia de proyecto |
| Equipo | La rotación del personal local y de los custodios rompe la capacidad instalada | Ninguno | Bajas de personas certificadas | Formación continua hasta 60 personas certificadas y documentación de procedimientos | Profesional de convenios y custodia |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.12 (diez causas por fase) y de 4.4-MDR.8 (rotación de personal como eslabón de adopción). Los responsables de 4.4-MDR.12 estaban por identificar; esta tabla propone roles del proyecto. Naturaleza: PROPUESTO.

La tabla revela una asimetría. De 11 causas, siete carecen de riesgo vinculado en el registro cuantitativo. Cinco de ellas corresponden a decisiones de marco, de criterio o de seguimiento. Su contención es un procedimiento, como fijar la meta antes del primer hito, registrar criterios con versión, exigir indicadores por refutación o designar un responsable. Esa asimetría confirma la división propuesta en E4.1. El dinero cubre lo que se mide, y el procedimiento cubre lo que se decide.

### E4.3 Plan de contingencia por causa crítica

Un plan de contingencia convierte una causa en una respuesta ejecutable con un disparador, un recurso y un plazo. La norma ISO 31000 (ISO, 2018) integra el tratamiento del riesgo en la gobernanza y recomienda fijar criterios para decidir. Collingridge (1980) plantea una objeción de fondo. Ningún plan anticipa todos los fallos. Por eso conviene elegir opciones de bajo costo de reversión, cuyo error se detecte pronto. La primera posición confía en la anticipación. La segunda confía en la corregibilidad.

El proyecto aplica ambas. La anticipación se materializa en los disparadores y en la reserva. La corregibilidad se materializa en las compuertas, porque cada una libera la compra del tramo siguiente. La estrategia R4 de 4.4-MDR es el despliegue por tramos con piloto de contraste y custodia distribuida. R4 detecta una falla de SC-1 en el mes 12, antes de comprometer 48 nodos y 4 gateways del tramo 2. Esa estructura limita la exposición. Una devaluación o una saturación de cabezales descubierta en el tramo 1 afecta 36 nodos comprados y no los 120 del total.

La {T:t13} presenta el plan para las 12 causas del registro. Los recursos requeridos equivalen al EMV de cada riesgo y se financian con la reserva de contingencia. Los plazos se expresan respecto de la cadencia del proyecto y no con cifras nuevas.

:::TABLA t13 | Planes de contingencia por causa y recursos con cargo a la reserva
| Causa | Disparador de activación | Plan de contingencia | Recursos requeridos (millones de COP) | Plazo de respuesta | Responsable |
| --- | --- | --- | --- | --- | --- |
| R-FIN-01: devaluación | TRM supera en 10 % la de la cotización | Aplicar cobertura cambiaria, renegociar cotizaciones y ajustar la compra de reserva sin reducir los 100 nodos y 10 gateways operativos | 165,0 | Antes de emitir la orden de compra del tramo | Gerencia de proyecto |
| R-TEC-01: saturación de cabezales | NRMSE > 30 % en dos verificaciones consecutivas | Reentrenar con una nueva ventana de colocalización, reponer cabezales, repetir el ciclo en el banco de calibración y no liberar el tramo 2 | 150,0 | Antes de la verificación mensual siguiente | Especialista en metrología |
| R-ORG-02: custodios sin partida | Convenio sin partida al cierre del tramo 2 | Activar la cláusula de apertura, negociar con un custodio académico o con la autoridad ambiental y condicionar la entrega del tramo 3 | 60,0 | En la sesión de la compuerta C2 | Profesional de convenios y custodia |
| R-EXT-01: vías bloqueadas | Retraso de instalación > 3 semanas | Reprogramar a ventanas secas, contratar técnicos locales y arrendar vehículos 4x4; solicitar ajuste de plazo si el retraso afecta la ruta crítica | 60,0 | Antes de la siguiente ventana seca | Gerencia de proyecto |
| R-ORG-01: comités sin adopción | Menos de 50 % de uso en el tramo 1 | Rediseñar la presentación del tablero con los comités, agregar talleres de co-diseño y registrar decisiones en cada sesión | 36,0 | Antes de la compuerta C1 | Coordinación de apropiación |
| R-TEC-04: modelo sin generalización | R² < 0,70 en el conjunto de validación externo | Reentrenar por departamento, sumar rotaciones de referencia y evaluar variables omitidas | 31,5 | En el siguiente ciclo de calibración | Científico de datos |
| R-TEC-03: enlace celular caído | Pérdida de paquetes > 10 % durante 72 horas | Conmutar al enlace satelital de respaldo y recuperar los datos del almacenamiento local de 7 días | 28,0 | De inmediato; cierre en la verificación mensual | Ingenieros IoT |
| R-TEC-02: baterías agotadas | Disponibilidad mensual < 90 % | Reponer baterías desde los repuestos, activar el modo de bajo consumo y revisar el dimensionamiento solar | 24,0 | En la siguiente visita de campo | Ingeniero de firmware |
| R-EXT-02: robo o vandalismo | Dos o más nodos perdidos en un mes | Reponer desde los 20 nodos de reserva, activar el seguro de equipos de la entidad ejecutora y reforzar la custodia local | 24,0 | En la siguiente visita de campo | Técnicos de campo |
| R-FIN-02: contrapartida sin certificar | Certificación pendiente al mes 2 | Obtener la certificación de la IES y de la empresa antes del acta de inicio y registrar su estado en C1 | 20,0 | Antes del acta de inicio en el mes 2 | Gerencia de proyecto |
| R-JUR-01: patente de terceros | Solicitud con fase nacional abierta que reivindique el método | Ejecutar el análisis de libertad de operación y rediseñar el módulo afectado | 20,0 | Antes del vencimiento del plazo de fase nacional | Consultoría en propiedad intelectual |
| R-DAT-01: incidente de ciberseguridad | Hallazgo crítico en la auditoría | Aislar el componente, restaurar desde copias de respaldo y repetir la auditoría externa | 18,0 | En la sesión siguiente al hallazgo | Ingenieros de software |
:::NOTA *Nota.* Elaboración propia con datos del registro de riesgos (disparador, respuesta, responsable y EMV) y del presupuesto (reserva X01 de 636,0 millones de COP; suma de EMV sin redondeo de 636,5). Naturaleza: PROPUESTO para los planes; CALCULADO para los recursos. Decimales con coma.

La tabla ordena los planes por recurso requerido y no por categoría. Los cuatro primeros planes absorben 435,0 millones de COP, es decir, 68,3 % de la suma de EMV (CALCULADO). Dos limitaciones acompañan el plan. Primera, el cronograma carece de holgura en la ruta crítica de 104 semanas. Un retraso de instalación en actividades críticas desplaza el cierre. Solo se compensa con recursos o con un ajuste de plazo, cuya admisibilidad depende de los TdR (VACIO). Segunda, la reserva cubre solo riesgos cuantificados. No cubre las causas estratégicas de la {T:t12}, que se tratan con procedimiento.

La regla de uso de la reserva completa el plan. Un recurso se libera solo en tres condiciones. El disparador se activó. La gerencia de proyecto y la coalición guía aprueban el plan. El gasto queda registrado en el acta. Esa regla protege el indicador PERS-R04, que exige una desviación de la ejecución presupuestal de 5 % o menos al cierre. Si los TdR no admiten la reserva como rubro, el proyecto debe gestionar con el financiador una reasignación entre rubros. Las reglas de esa reasignación son VACIO.

## E5 Escenarios estratégicos

### E5.1 Metodología de escenarios

Los escenarios son herramientas de preparación y no pronósticos. Godet (2001) define un escenario como la descripción de una situación futura. Incluye la secuencia de eventos que conduce a ella desde la situación de origen. La definición exige coherencia interna y un camino identificable. No exige una probabilidad. El proyecto desarrolla cuatro escenarios: optimista, base, pesimista y de disrupción. Cada uno incluye una condición de activación, tres objetivos y tres acciones por objetivo.

El debate metodológico se centra en el peso que se asigna a cada escenario. El informe de vigilancia tecnológica asigna probabilidades subjetivas a sus escenarios, de 30, 50 y 20 %, y calcula valores esperados. Declara que son juicios del analista y no frecuencias estimadas con datos (F-INF, §9.1). El metaprompt sugiere probabilidades de 25, 50, 20 y 5 %. Snowden y Boone (2007) sostienen otra postura. En contextos complejos, la causa y el efecto solo se reconocen en retrospectiva. El líder prueba, percibe y responde en lugar de predecir. El proyecto sigue la segunda postura. Omite las probabilidades, porque ninguna cuenta con fuente, según la decisión DEC-F11 del registro de formulación y la Norma Transversal CTeI (NTC 1.1).

La definición de los escenarios se apoya en los cuatro supuestos críticos de la sección 4.4-MDR.8. SC-1 afirma que la corrección local reduce el error frente a la lectura sin corrección dinámica. SC-2 afirma que los nodos conservan energía y enlace. SC-3 afirma que los comités incorporan los umbrales en sus protocolos. SC-4 afirma que al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo. La sección 4.4-MDR.12 formuló tres futuros como combinaciones de esos supuestos. Este capítulo los adopta y añade un cuarto escenario, definido por un evento externo y no por un supuesto interno.

La {T:t14} define las condiciones de activación. Una condición de activación es una evidencia documental, no una percepción. Cada escenario se activa en una compuerta o en una sesión no programada de la coalición guía.

:::TABLA t14 | Condiciones de activación de los escenarios estratégicos
| Escenario | Supuestos críticos | Condición de activación | Evidencia que la confirma | Instancia y momento de decisión |
| --- | --- | --- | --- | --- |
| Optimista | SC-1 a SC-4 se cumplen | C1 y C2 superadas; al menos un custodio con capacidad de absorción de 2 o más; uso del tablero en trayectoria hacia 75 % | Actas de C1 y C2; índice de capacidad de absorción; PERS-E01 | Compuerta C2 en el mes 17 y evaluación externa del mes 24 |
| Base | SC-1 a SC-3 se cumplen; SC-4 se cumple en parte de los componentes | C1 y C2 superadas; convenios con partida para parte de los componentes | Actas de compuerta; convenios por componente | Compuerta C2 en el mes 17 |
| Pesimista | SC-3 y SC-4 fallan; SC-1 puede fallar | C1 no superada, uso del tablero menor que 50 % en el tramo 1 o convenio sin partida al cierre del tramo 2 | Acta de C1; PERS-E01; convenios | Compuerta C1 en el mes 12 y compuerta C2 en el mes 17 |
| Disrupción | Un evento externo altera varios supuestos a la vez | TdR que prohíben el piloto o los tramos; TRM sobre el disparador de forma sostenida; vías bloqueadas con retraso mayor que 3 semanas; cambio normativo | Documento del convocante; serie de la TRM; reporte de la autoridad de gestión del riesgo; acto administrativo | Sesión no programada de la coalición guía |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.8 (supuestos SC-1 a SC-4), 4.4-MDR.12 (tres futuros), del cronograma (compuertas) y del registro de riesgos (disparadores de R-FIN-01 y R-EXT-01). Naturaleza: PROPUESTO. Sin probabilidades, según DEC-F11. TRM: tasa representativa del mercado.

La tabla permite decidir con evidencia en tres momentos: los meses 12, 17 y 24. Los tres primeros escenarios se activan por el resultado de las compuertas. El cuarto se activa por un hecho externo y su decisión no espera a una compuerta. Un escenario no excluye a otro en el tiempo. El proyecto puede ser base hasta el mes 17 y pesimista después, si C2 no se supera por falta de convenios con partida.

La {F:f07} ubica los escenarios en un plano definido por los dos pares de supuestos. El eje horizontal agrupa SC-1 y SC-2, que describen la medición y la red. El eje vertical agrupa SC-3 y SC-4, que describen el uso y la custodia. Cada escenario ocupa una región del plano.

:::FIGURA f07 | Los escenarios se distinguen por el cumplimiento de los supuestos de medición y de custodia | Nota. Fuente: elaboración propia a partir de 4.4-MDR.8 y 4.4-MDR.12. Sin ejes numéricos ni probabilidades (DEC-F11); la posición indica el cumplimiento de supuestos y no una frecuencia. Diagrama de cuadrantes; matplotlib, tamaño 10 × 7 pulgadas. Script: cX4_figuras.py; sin semilla aleatoria.

La figura aclara dos puntos. Primero, el escenario optimista exige el cumplimiento de los cuatro supuestos, y el base acepta un cumplimiento parcial de SC-4. Segundo, el cuadrante de uso institucional sin medición verificada no es un escenario del plan, sino un riesgo. Corresponde a la consecuencia no deseada de falsa seguridad que anticipa 4.4-MDR.11. El proyecto lo previene con rangos de incertidumbre y con la referencia permanente.

### E5.2 Escenario optimista

El escenario optimista corresponde al futuro ambicioso de 4.4-MDR.12. Los cuatro supuestos críticos se cumplen. La teoría del cambio alcanza el impacto en forma de contribución, y la sostenibilidad completa la transferencia por tramos con un motor financiero diversificado. La condición de activación es que C1 y C2 se superen y que al menos un custodio demuestre capacidad de absorción de 2 o más.

La difusión de una innovación sigue una curva por categorías de adoptantes, y la observabilidad y la compatibilidad aceleran la adopción (Rogers, 2003). Si el optimismo se confirma, la demanda de réplica puede superar la capacidad del proyecto. La expansión rápida produce consecuencias no anticipadas (Merton, 1936). La tensión entre ambas posiciones se resuelve con una regla de alcance. El proyecto solicitó 8.729,84 millones de COP, que equivalen a 62,4 % del tope declarado de 14.000 millones de COP. La holgura de 5.270,16 millones de COP no se solicitó. Esa holgura se describe como opciones de ampliación condicionadas a los TdR: más nodos, un cuarto tramo y un año adicional de custodia. Ninguna se presupuesta (DEC-F06).

La {T:t15} presenta tres objetivos con tres acciones cada uno. Las acciones son opciones PROPUESTO de 4.4-MDR.12, complementadas con las opciones de ampliación.

:::TABLA t15 | Plan para el escenario optimista
| Objetivo | Acción 1 | Acción 2 | Acción 3 |
| --- | --- | --- | --- |
| O1: Extender la verificación a más sitios | Compartir la red de referencia con estaciones oficiales y universidades | Desplegar nodos de referencia itinerantes | Solicitar al convocante la ampliación con más nodos o un cuarto tramo, sin presupuestar antes de los TdR |
| O2: Integrar las alertas en las rutinas de salud y de gestión del riesgo | Integrar el tablero al sistema de información de las ARL | Integrar los umbrales al protocolo de emergencia departamental | Validar localmente mensajes de riesgo con guía por grupo para las comunidades |
| O3: Consolidar el motor financiero y la transferencia completa | Constituir un fondo patrimonial o una reserva de mantenimiento con rendimiento real y fuente | Licenciar el servicio a otras entidades territoriales | Pactar un pago por resultados ligado a la disponibilidad y a la verificación |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.12 (futuro ambicioso) y del libro maestro (DEC-F06: holgura sin presupuestar). Naturaleza: PROPUESTO. ARL: administradoras de riesgos laborales. TdR: términos de referencia.

El plan aprovecha el éxito sin comprometer recursos no solicitados. El objetivo O1 amplía la verificación, la condición que sostiene la credibilidad del dato. El objetivo O2 amplía el uso, la condición que justifica el gasto público. El objetivo O3 resuelve la continuidad, el punto más débil del proyecto según el registro de riesgos. Cada acción exige una condición de viabilidad, como un convenio, un mandato o un indicador verificable, y ninguna se ejecuta sin ella. La continuidad de un programa depende del diseño del proyecto, del entorno organizacional y del entorno comunitario (Shediac-Rizkallah y Bone, 1998).

### E5.3 Escenario base

El escenario base corresponde al futuro base de 4.4-MDR.12. SC-1, SC-2 y SC-3 se cumplen, y SC-4 se cumple en parte de los componentes. La teoría del cambio llega a la incorporación de protocolos y a un servicio parcial. La sostenibilidad ejecuta tramos parciales. Es el escenario de trabajo del proyecto: el que sigue el plan con ajustes menores y exige la menor intervención estratégica.

Dos posturas describen cómo se decide en este escenario. Lindblom (1959) defiende las comparaciones sucesivas limitadas, en las que el decisor avanza por ajustes pequeños desde la situación actual. Etzioni (1967) propone el rastreo mixto: un examen general de las opciones para detectar cambios mayores y un examen detallado de las opciones que lo ameritan. El proyecto adopta una versión de la segunda. La revisión mensual de indicadores es el ajuste incremental. La revisión trimestral de supuestos y las compuertas son el examen general.

El escenario base exige tres cuidados. El primero es no confundir un cumplimiento parcial de SC-4 con un cumplimiento total. Los componentes sin custodio con capacidad demostrada permanecen bajo la alianza o pasan a la cláusula de apertura. El segundo es mantener el error verificado en operación, porque la deriva de los sensores no se corrige sola. El tercero es incorporar los umbrales en protocolos con efecto jurídico y no solo con acuerdos verbales.

La {T:t16} presenta el plan base. Sus acciones provienen del futuro base de 4.4-MDR.12 y son PROPUESTO.

:::TABLA t16 | Plan para el escenario base
| Objetivo | Acción 1 | Acción 2 | Acción 3 |
| --- | --- | --- | --- |
| O1: Mantener el error verificado en operación | Recalibrar por ventana estable con referencia permanente en un subconjunto de nodos | Recalibrar de forma periódica con técnicos locales certificados | Reentrenar el modelo con datos de referencia compartidos entre sitios |
| O2: Incorporar los umbrales en los protocolos | Ejecutar el protocolo piloto en un departamento y ampliarlo por evidencia | Obtener un acto administrativo departamental que adopte los umbrales | Incluir cláusulas ambientales que citen los umbrales en los contratos de obra |
| O3: Sostener el servicio por componente | Pactar un contrato de servicio entre las alcaldías y la institución ejecutora | Cofinanciar repuestos con las ARL y la autoridad ambiental mediante convenio | Entregar el tablero a la unidad de gestión del riesgo y el protocolo de calibración a la autoridad ambiental |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.12 (futuro base). Naturaleza: PROPUESTO. ARL: administradoras de riesgos laborales.

Las nueve acciones comparten un criterio: cada una transfiere una función a quien posee competencia para sostenerla. La recalibración con técnicos locales certificados se apoya en la meta de 60 personas certificadas (PERS-E03). El acto administrativo departamental se apoya en la competencia jurídica de la gobernación. Las reglas formales fijan la conducta esperada (North, 1990). El contrato de servicio se apoya en la partida del plan operativo anual. Si alguna condición falta, la función permanece bajo la alianza y el escenario se acerca al pesimista.

### E5.4 Escenario pesimista

El escenario pesimista toma el futuro conservador de 4.4-MDR.12. En ese futuro, SC-1 y SC-2 se cumplen y SC-3 y SC-4 fallan. El escenario añade la rama de falla de SC-1. Tres condiciones lo activan. La primera es una compuerta no superada. La segunda es un uso del tablero menor que 50 % en el tramo 1. La tercera es un convenio sin partida al cierre del tramo 2. La teoría del cambio llega solo a los resultados inmediatos y la sostenibilidad activa la cláusula de apertura.

La literatura sobre decisión bajo riesgo advierte sobre un riesgo de este escenario. Kahneman y Tversky (1979) describen que, frente a pérdidas, las personas tienden a aceptar mayor riesgo para evitarlas. Esa tendencia favorece continuar con una inversión que ya muestra señales de fracaso. El criterio opuesto prefiere las opciones de menor costo de reversión y de detección más temprana del error (Collingridge, 1980). Las compuertas del proyecto institucionalizan el segundo criterio. Si C1 no se supera, la compra del tramo 2, de 48 nodos y 4 gateways, no se libera. El proyecto limita así la pérdida y no la agrava.

Este escenario no equivale a un proyecto sin valor. Conserva tres productos con utilidad propia. Son una línea base de error medida con referencia en el tramo 1, un protocolo de calibración colocalizada y un uso técnico del tablero. La sección 4.4-MDR.12 los reconoce como objetivos del futuro conservador. El proyecto los trata como un piso de resultados, y su declaración exige honestidad sobre lo que no se logró.

La {T:t17} resume el plan pesimista. Las acciones provienen del futuro conservador de 4.4-MDR.12 y son PROPUESTO.

:::TABLA t17 | Plan para el escenario pesimista
| Objetivo | Acción 1 | Acción 2 | Acción 3 |
| --- | --- | --- | --- |
| O1: Consolidar una medición verificada con alcance reducido | Ampliar el sorteo a más nodos con la misma referencia, es decir, más réplicas de contraste | Co-ubicar nodos con estaciones oficiales como referencia externa | Aplicar corrección por reglas fijas con humedad, sin aprendizaje embebido, si el error se mantiene aceptable |
| O2: Dar uso técnico sin adopción pública | Entregar el tablero a la interventoría y a la institución ejecutora | Emitir informes a las ARL y a las constructoras para el control de la exposición ocupacional | Publicar series y boletines abiertos para universidades y comunidades |
| O3: Preservar los activos y el conocimiento | Mantener un servicio mínimo con un custodio académico | Liberar datos y código con licencia abierta y un manual de reactivación | Contratar servicios con constructoras y ARL para mantener nodos de referencia |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.12 (futuro conservador) y del cronograma (compuerta C1). Naturaleza: PROPUESTO. ARL: administradoras de riesgos laborales.

El plan reduce el alcance, pero conserva el aprendizaje y los activos. Cada objetivo conlleva un riesgo propio que el proyecto debe declarar. El objetivo O1 depende de solo tres monitores de referencia presupuestados. El objetivo O2 enfrenta el riesgo de que las constructoras usen el tablero para eludir responsabilidades. El objetivo O3 depende de contratos con vigencia superior al proyecto y de un número reducido de clientes. Por esa razón el escenario exige comunicar de forma proactiva las dificultades al convocante y a los comités. La sección 4.4-MDR.5 ya advierte sobre un caso. Una constructora con poder para paralizar la obra y sin legitimidad sobre el umbral es un riesgo y no un aliado (Mitchell et al., 1997).

### E5.5 Escenario de disrupción

El escenario de disrupción describe un evento externo que cambia el contexto del proyecto con independencia de su desempeño interno. Los eventos considerados provienen del registro de riesgos y del premortem. Son cinco. Los TdR pueden prohibir el piloto o la compra por tramos. El peso puede sufrir una devaluación sostenida. Deslizamientos o réplicas pueden bloquear el acceso a los sitios. Puede cambiar la norma. Puede aparecer una tecnología alterna certificada. La norma nacional de calidad del aire es la Resolución 2254 de 2017 (Ministerio de Ambiente y Desarrollo Sostenible, 2017). Un cambio de sus umbrales alteraría el diseño del índice. Una réplica sísmica añadiría escombros y polvo. Un desastre con escombros tiene consecuencias ambientales y de salud documentadas (Landrigan et al., 2004).

En una crisis, el líder actúa primero para estabilizar, percibe después y responde (Snowden y Boone, 2007). Para el desarrollo ordenado de productos rige lo contrario. La decisión en cada compuerta se toma con criterios definidos (Cooper, 2008). El escenario exige combinar ambas posturas. La primera orienta las primeras horas del evento. La segunda orienta la decisión formal sobre la continuidad. El proyecto separa la contención inmediata de la decisión estratégica para no improvisar la segunda bajo la presión de la primera.

El proyecto cuenta con dos defensas estructurales. La primera es la compra por tramos, que limita la exposición: ningún tramo se compra antes de superar la compuerta previa. La segunda es la cláusula de apertura y de salida ordenada de 4.4-MDR.10. Permite liberar datos, código y conocimiento con una licencia definida. Permite también trasladar los activos físicos a un custodio con un manual de reactivación. La gestión de desastres con sistemas heterogéneos, como el que integra nodos, gateways, nube y comités, es un campo de revisión reciente (Haris et al., 2026). Una desventaja es el calendario. La ruta crítica carece de holgura, y por eso cualquier evento que bloquee actividades críticas desplaza el cierre.

La {T:t18} presenta tres objetivos con tres acciones. Las acciones son PROPUESTO y no existen en 4.4-MDR.12, que no formuló este escenario.

:::TABLA t18 | Plan para el escenario de disrupción
| Objetivo | Acción 1 | Acción 2 | Acción 3 |
| --- | --- | --- | --- |
| O1: Evaluar la viabilidad de continuidad | Analizar el impacto del evento sobre los sitios, los TdR, los costos y el calendario | Consultar al convocante, a los comités y a los custodios | Decidir por acta si el proyecto continúa, se pausa o termina, con el criterio de menor costo de reversión |
| O2: Considerar un giro mayor | Identificar una aplicación alterna de la calibración colocalizada y de la corrección en el gateway | Reformular el alcance, por ejemplo con el tramo 1 como producto de conocimiento | Negociar con el convocante el cambio de enfoque |
| O3: Ejecutar un cierre ordenado si es necesario | Documentar el trabajo realizado y conservar las series de datos | Activar la cláusula de apertura y trasladar los activos físicos con un manual de reactivación | Comunicar la decisión a los comités, a los operarios, a las comunidades y al convocante |
:::NOTA *Nota.* Elaboración propia con datos de 4.4-MDR.10 (cláusula de apertura y salida ordenada), del registro de riesgos y de 4.4-MDR.12 (causa de entorno). Naturaleza: PROPUESTO. Sin probabilidad, según DEC-F11.

El plan separa tres decisiones que un evento externo suele mezclar: continuar, girar o cerrar. El primer objetivo exige una decisión formal con acta y no una reacción. El segundo reconoce que las capacidades del proyecto, la calibración colocalizada y la corrección en el borde, pueden servir en otra aplicación. El tercero asegura que, incluso si el proyecto termina, los datos, el código y el conocimiento no se pierden. Así se protege el uso del dinero público.

## E6 Síntesis estratégica

### E6.1 Mapa estratégico integrado

El mapa estratégico organiza en cuatro niveles lo que el capítulo desarrolló por separado. Las capacidades y los recursos sostienen los tres procesos internos: el posicionamiento de Christensen, el cambio de Kotter y el aprendizaje de Argyris. Los procesos producen resultados verificables. Los resultados contribuyen a un impacto que el proyecto no controla por completo. Esta estructura retoma la lógica de una teoría del cambio, base de la evaluación de iniciativas comunitarias complejas (Weiss, 1995).

Dos lecturas rivales compiten sobre la forma del mapa. Funnell y Rogers (2011) proponen teorías del cambio y modelos lógicos con cadenas de resultados que se pueden anidar y desacoplar por componente. Los sistemas complejos no responden a recetas lineales (Glouberman y Zimmerman, 2002). La sección 4.4-MDR.8 resolvió el dilema con una arquitectura anidada. Descartó la arquitectura sistémica, porque exigiría modelar bucles con fichas de baja confianza. Conservó como bucle la retroalimentación principal, que es el uso institucional que justifica los contratos. El mapa de este capítulo respeta esa decisión.

El proyecto cuenta con recursos definidos para cada nivel. La base incluye tres recursos. El primero es el equipo de 14 líneas de personal del presupuesto. El segundo son las alianzas (SUPUESTO). Participan la institución ejecutora, la empresa tecnológica, las alcaldías y la Unidad Nacional para la Gestión del Riesgo de Desastres (UNGRD). El tercero son los recursos financieros. El valor solicitado al Sistema General de Regalías (SGR) es de 8.729,84 millones de COP. La contrapartida es de 2.110 millones de COP. El total del proyecto es de 10.839,84 millones de COP. Los resultados son las metas de los tres objetivos específicos y de los productos PERS. El impacto se ubica sobre el techo de rendición de cuentas de 4.4-MDR.8, es decir, como contribución y no como compromiso.

La {F:f08} presenta el mapa con sus metas.

:::FIGURA f08 | Los tres marcos transforman capacidades en resultados verificables y contribuyen a un impacto de continuidad | Nota. Fuente: elaboración propia con datos del libro maestro (presupuesto, objetivos específicos, indicadores PERS) y 4.4-MDR.8 (techo de rendición de cuentas). Metas DECLARADO o PROPUESTO según el libro maestro. Diagrama por niveles; matplotlib, tamaño 10 × 7 pulgadas. Script: cX4_figuras.py; sin semilla aleatoria.

La figura muestra que cada marco alimenta un resultado distinto y que el aprendizaje de Argyris alimenta a todos. Ese es el diseño intencional del capítulo. El posicionamiento fija el umbral de desempeño. El cambio logra el uso. El aprendizaje corrige los dos y genera conocimiento. El nivel de impacto aparece con trazo discontinuo. Se mide entre 6 y 12 meses después del cierre. Depende de custodios que hoy carecen de compromiso firmado.

La {T:t19} cierra la integración. Relaciona cada marco con su mecanismo y con la compuerta o el hito donde actúa. Añade el supuesto crítico que protege, el objetivo específico y el indicador que lo mide.

:::TABLA t19 | Correspondencia entre los marcos, las compuertas, los supuestos y los indicadores
| Marco | Pregunta que responde | Mecanismo del proyecto | Compuerta o hito | Supuesto crítico | Objetivo | Indicador |
| --- | --- | --- | --- | --- | --- | --- |
| Christensen: posicionamiento | ¿Dónde se ubica el proyecto frente a la referencia? | Umbral de lo suficientemente bueno (R² ≥ 0,70; NRMSE ≤ 30 %) | C1 en el mes 12 | SC-1 | OE1 | PERS-R02 y PERS-R05 |
| Christensen: trabajos por realizar | ¿Qué trabajo resuelve el tablero? | Co-diseño con los comités y registro de decisiones | C1 y C2 | SC-3 | OE3 | PERS-E01 y PERS-E02 |
| Kotter: adopción | ¿Cómo se logra el uso institucional? | Ocho pasos y cinco victorias tempranas | H0 a H5 | SC-3 | OE3 | PERS-P04 y PERS-E03 |
| Kotter: anclaje | ¿Cómo se asegura la continuidad? | Convenios por tramo y cláusula de apertura | H8 en el mes 24 | SC-4 | OE3 | PERS-S02 |
| Argyris: bucle simple | ¿La acción se ejecuta bien? | Retrospectiva e indicadores mensuales | Cada mes | SC-2 | OE2 | PERS-R01 y PERS-P01 |
| Argyris: bucle doble | ¿La acción es la correcta? | Revisión de supuestos y evaluación externa | C1, C2, C3 y meses 12 y 24 | SC-1 a SC-4 | OE1 a OE3 | Indicadores de aprendizaje |
| Premortem y contingencia | ¿Qué puede causar el fracaso y qué se hace? | 12 disparadores y reserva de 636,0 millones de COP | Todas | SC-1 a SC-4 | OE1 a OE3 | PERS-R04 |
| Escenarios | ¿Qué futuros exigen decisiones distintas? | Cuatro escenarios con condiciones de activación | C1, C2 y C3 | SC-1 a SC-4 | OE1 a OE3 | Actas de compuerta |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (objetivos, compuertas, hitos e indicadores PERS) y de 4.4-MDR.8 (supuestos críticos). Naturaleza: PROPUESTO para la correspondencia.

La tabla muestra que los supuestos SC-1 y SC-3 concentran el mayor número de mecanismos. SC-1 sostiene el posicionamiento de Christensen y SC-3 sostiene tanto los trabajos por realizar como el modelo de Kotter. Esa concentración explica por qué las compuertas C1 y C2 miden desempeño y uso al mismo tiempo. Un proyecto que cumple una condición sin la otra queda en el escenario pesimista. Las dos condiciones se evalúan juntas.

### E6.2 Indicadores estratégicos clave

Un tablero de control estratégico debe medir lo que cada marco promete. La mejora se fundamenta en el conocimiento de la variación del proceso, lo que exige medir con regularidad (Deming, 1986). En contextos de innovación, los indicadores deben revisarse a medida que cambia el entendimiento (Patton, 2011). El proyecto adopta una síntesis. Fija pocos indicadores, los vincula con el sistema PERS, y revisa su pertinencia en cada sesión trimestral de supuestos.

La {T:t20} presenta nueve indicadores. Tres corresponden a Christensen, tres a Kotter, dos a Argyris y uno a la gestión. Las líneas base marcadas VACIO se miden en el tramo 1. Las metas provienen del sistema de indicadores PERS cuando existe uno equivalente.

:::TABLA t20 | Tablero de control estratégico
| Marco | Indicador clave | Línea base | Meta | Frecuencia | Responsable |
| --- | --- | --- | --- | --- | --- |
| Christensen | Desempeño suficiente frente al umbral: R² y NRMSE por departamento | VACIO (se mide en el tramo 1) | R² ≥ 0,70 y NRMSE ≤ 30 % en los tres departamentos | En C1, en C2 y en el mes 24 | Especialista en metrología |
| Christensen | Trabajo resuelto: comités con decisiones documentadas con el tablero (PERS-E01) | VACIO (se mide en el tramo 1) | ≥ 50 % en C1 y ≥ 75 % al mes 24 | Trimestral | Coordinación de apropiación social |
| Christensen | Reducción relativa de falsas alarmas (PERS-E02) | VACIO (se mide en el tramo 1) | ≥ 30 % de reducción relativa | Trimestral | Profesional en calidad del aire y salud ambiental |
| Kotter | Cumplimiento de las victorias tempranas con evidencia | 0 de 5 (CALCULADO) | 5 de 5 | Por hito | Gerencia de proyecto |
| Kotter | Personas certificadas en los custodios (PERS-E03) | 0 (CALCULADO) | ≥ 60 personas | Semestral | Profesional de convenios y custodia |
| Kotter | Convenios de custodia con partida | 0 (CALCULADO) | Al menos 1 en el mes 17 y convenios por tramo al mes 24 | Por compuerta | Profesional de convenios y custodia |
| Argyris | Lecciones capturadas e implementadas | 0 de 0 (CALCULADO) | ≥ 2 por hito y ≥ 70 % implementadas | Trimestral | Gerencia de proyecto |
| Argyris | Decisiones de doble bucle registradas con acta | 0 (CALCULADO) | 3 de 3 compuertas y 8 sesiones trimestrales | Semestral | Coalición guía |
| Gestión | Desviación de la ejecución presupuestal (PERS-R04) | 0 (CALCULADO) | Desviación absoluta de 5 % o menos al cierre | Mensual | Gerencia de proyecto |
:::NOTA *Nota.* Elaboración propia con datos del sistema de indicadores PERS (metas DECLARADO o PROPUESTO) y de las tablas de este capítulo. Línea base VACIO: se mide en el tramo 1. La meta de convenios y la de doble bucle son PROPUESTO. Decimales con coma.

El tablero ofrece una lectura rápida por marco. Tres indicadores dependen de una línea base que hoy es VACIO. El proyecto no puede afirmar ningún avance sobre ellos antes del tramo 1. Los demás parten de cero por construcción. La tabla incluye un indicador de gestión, la desviación presupuestal, porque la reserva de contingencia exige disciplina de ejecución. Si un indicador cambia de pertinencia, la coalición guía lo ajusta con una nueva versión y deja constancia en el acta.

### E6.3 Conclusiones del capítulo

La estrategia del proyecto integra tres marcos con una misma lógica de decisión por evidencia. Christensen (2016) permite clasificar el proyecto como una disrupción de mercado nuevo con rasgos de gama baja. Esa clasificación es una hipótesis (INFERIDO). Se apoya en el no consumo de 1.094 municipios sin estaciones utilizables para estimar la carga (CALCULADO; Rodríguez-Villamizar et al., 2022, pp. 3 y 6). Se apoya también en un perfil de atributos que cede fiabilidad y gana costo, acceso y cobertura. El umbral de lo suficientemente bueno es un R² de al menos 0,70 y un NRMSE de 30 % o menos. Ese umbral convierte la clasificación en una prueba verificable en la compuerta C1.

Kotter (2012) aporta la secuencia para lograr el uso institucional. Los ocho pasos se distribuyen en 24 meses, con responsables por rol y con indicadores que remiten al sistema PERS. Las cinco victorias tempranas empiezan con el primer nodo con dato pareado en el mes 7. Terminan con el primer convenio de custodia con partida en el mes 17. La coalición guía de siete roles reúne poder, credibilidad, liderazgo y experiencia. El proyecto no puede evaluar con evidencia a las alcaldías, a las constructoras ni a los operarios antes del tramo 1.

Argyris (1999) aporta el mecanismo de corrección. El bucle simple ajusta la acción cada mes. El bucle doble revisa los supuestos SC-1 a SC-4 en las compuertas, en una sesión trimestral y en dos evaluaciones externas. El premortem y los escenarios completan el marco. El primero identifica 12 causas cuantificadas y 11 causas estratégicas, y asigna 636,0 millones de COP de reserva a las primeras. Los segundos describen cuatro futuros sin probabilidades, cada uno con su condición de activación, tres objetivos y tres acciones.

Tres límites acotan estas conclusiones. Primero, los términos de referencia no se aportaron, de modo que la admisibilidad de la compra por tramos y de la reserva es VACIO. Segundo, son VACIO la participación de operarios y comunidades y la evidencia de los custodios. También son VACIO las líneas base de error, de uso y de falsas alarmas. Tercero, este capítulo es una propuesta de formulación que una sola instancia analítica redactó. La revisión humana de sus metas, meses y niveles es condición de aceptación. El proyecto no promete efectos en salud. Promete mediciones verificadas, uso institucional y continuidad.

