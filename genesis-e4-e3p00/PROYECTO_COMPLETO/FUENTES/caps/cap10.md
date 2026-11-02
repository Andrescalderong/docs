%% PREFIJO: 10
# Capítulo 10. Gestión de riesgos

La gestión de riesgos del proyecto sigue el proceso de la norma ISO 31000. Este proceso establece el contexto, identifica, analiza, evalúa y trata los riesgos, con monitoreo y revisión continuos (Organización Internacional de Normalización [ISO], 2018). El Project Management Institute complementa ese proceso con técnicas de análisis cualitativo y cuantitativo, y con planes de respuesta por estrategia (Project Management Institute [PMI], 2021). Este capítulo aplica ambos marcos a 12 riesgos. Los conecta con tres elementos del proyecto. Son las variables del análisis causal, la reserva de contingencia y los hitos de decisión.

El registro tiene un rasgo que condiciona su lectura. La probabilidad y el impacto de cada riesgo son juicios del equipo formulador sobre escalas de 1 a 5, sin fuente externa. Los valores monetarios esperados se calculan con esos juicios y heredan su incertidumbre. El capítulo no oculta esa condición: trata los números como una forma ordenada de discutir prioridades, y no como una medida del riesgo real. La reserva de 636,0 millones de pesos colombianos (COP) es la suma de esos valores, y la sección 10.3 evalúa qué tan suficiente es.

## 10.1 Identificación de riesgos

### 10.1.1 Fuentes y categorías

Los riesgos provienen de tres fuentes. La primera es la sección 4.4-MDR.12, que aplicó un premortem: supuso que la estrategia de despliegue por tramos había fracasado y enumeró las causas probables. La segunda es el análisis de dependencias del cronograma del capítulo 9, que identificó las actividades críticas expuestas. La tercera es el supuesto crítico de cada compuerta, SC-1 a SC-4. El método del premortem parte de imaginar el fracaso y preguntar qué lo explicó, y reduce el exceso de confianza del equipo (Klein, 2007).

El registro agrupa los riesgos en seis categorías: técnica, organizacional, externa, financiera, jurídica y de datos. La {T:t01} los lista con su descripción, las variables del escenario S2 que los explican, la probabilidad, el impacto, el producto de ambos y el nivel. Los riesgos técnicos son cuatro y reúnen la mayor parte del valor esperado. Los organizacionales son dos, los externos dos, los financieros dos, uno jurídico y uno de datos.

:::TABLA t01 | Registro de los 12 riesgos identificados
| Id | Categoría | Riesgo | Variables de S2 | P | I | P × I | Nivel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-TEC-01 | Técnico | La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10. | V03, V02 | 4 | 5 | 20 | EXTREMO |
| R-TEC-02 | Técnico | Las baterías se agotan antes de 14 días sin sol y los nodos dejan de transmitir. | V05, V09 | 3 | 4 | 12 | ALTO |
| R-TEC-03 | Técnico | La red celular falla en el sitio y los gateways pierden el enlace con la nube. | V08 | 3 | 4 | 12 | ALTO |
| R-TEC-04 | Técnico | El modelo de corrección no generaliza entre departamentos. | V07, V06 | 3 | 4 | 12 | ALTO |
| R-ORG-01 | Organizacional | Los comités de gestión del riesgo no adoptan el tablero ni el protocolo. | V15 | 3 | 5 | 15 | ALTO |
| R-ORG-02 | Organizacional | Los custodios no asumen la operación en el posproyecto. | V15 | 4 | 4 | 16 | ALTO |
| R-EXT-01 | Externo | Deslizamientos o réplicas bloquean vías y retrasan la instalación. | V05 | 4 | 3 | 12 | ALTO |
| R-EXT-02 | Externo | Robo o vandalismo de nodos en sitios de remoción. | V09 | 3 | 3 | 9 | MEDIO |
| R-FIN-01 | Financiero | La devaluación del peso encarece los equipos importados. | — | 4 | 4 | 16 | ALTO |
| R-FIN-02 | Financiero | La contrapartida en especie no se certifica a tiempo. | — | 2 | 4 | 8 | MEDIO |
| R-JUR-01 | Jurídico | Una solicitud de patente de terceros afecta la libertad de operación. | — | 2 | 4 | 8 | MEDIO |
| R-DAT-01 | Datos | Un incidente de ciberseguridad compromete la plataforma. | V15 | 2 | 4 | 8 | MEDIO |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (RISKS) y de la ficha maestra §7. P e I son escalas de 1 a 5 (PROPUESTO, juicio del equipo formulador, sin fuente). Nivel: BAJO por debajo de 6; MEDIO de 6 a 11; ALTO de 12 a 19; EXTREMO desde 20. Un guion indica que el riesgo no se asocia a una variable de S2.

Un riesgo no se asocia con una variable de S2 cuando su origen es externo al sistema modelado. Son los casos de la devaluación, la certificación de contrapartida y las solicitudes de patentes de terceros. Esos riesgos no desaparecen por no tener variable. Quedan fuera del modelo causal. Por eso la gerencia los vigila con indicadores propios del capítulo 12 y con el tablero de riesgos del paquete 1000X.

### 10.1.2 Distribución por nivel

El registro tiene un riesgo extremo, siete riesgos altos, cuatro riesgos medios y ningún riesgo bajo. El único riesgo extremo es R-TEC-01: la humedad y el polvo saturan los cabezales ópticos y sesgan las mediciones. Su probabilidad es de 4 y su impacto de 5, y el producto es 20. Los siete riesgos altos se reparten entre las categorías técnica, organizacional, externa y financiera. Ningún riesgo cae en nivel bajo, lo que indica un registro depurado de riesgos triviales y también un proyecto con poco margen.

## 10.2 Análisis cualitativo

### 10.2.1 Matriz de probabilidad e impacto

El análisis cualitativo clasifica cada riesgo por su probabilidad y su impacto. La {T:t02} ubica los 12 riesgos en la matriz de cinco por cinco. Los niveles son cuatro. Bajo corresponde a un producto menor que 6 y medio a un producto de 6 a 11. Alto corresponde a un producto de 12 a 19 y extremo a uno de 20 o más. La concentración de riesgos en las celdas de probabilidad 3 y 4 con impacto 4 refleja un juicio cauteloso. Pocos riesgos se consideran casi seguros o casi irrelevantes.

:::TABLA t02 | Matriz de probabilidad-impacto con los 12 riesgos
| Probabilidad | I = 1 | I = 2 | I = 3 | I = 4 | I = 5 |
| --- | --- | --- | --- | --- | --- |
| P = 5 | — | — | — | — | — |
| P = 4 | — | — | EXT-01 | ORG-02, FIN-01 | TEC-01 |
| P = 3 | — | — | EXT-02 | TEC-02, TEC-03, TEC-04 | ORG-01 |
| P = 2 | — | — | — | FIN-02, JUR-01, DAT-01 | — |
| P = 1 | — | — | — | — | — |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (RISKS). Cada celda lista los riesgos que ocupan esa combinación; un guion indica una celda vacía. Nivel por celda: EXTREMO si P × I ≥ 20; ALTO de 12 a 19; MEDIO de 6 a 11; BAJO por debajo de 6. Escalas PROPUESTO.

La {F:f01} presenta el mapa de calor. Muestra la distribución por nivel y las categorías que concentran cada uno. El mapa orienta una decisión práctica. El comité directivo atiende los riesgos de nivel extremo. La gerencia atiende los de nivel alto. El responsable de cada riesgo atiende los de nivel medio. Esa asignación de decisiones por nivel es parte del plan de escalamiento de la sección 10.4.

:::FIGURA f01 | Un riesgo extremo y siete altos concentran el registro; ninguno queda en nivel bajo | Nota. Elaboración propia con maestro.py (RISKS). Probabilidad e impacto en escalas de 1 a 5 (PROPUESTO, sin fuente). Niveles: bajo menor que 6; medio de 6 a 11; alto de 12 a 19; extremo desde 20. Figura generada con matplotlib mediante c10_figs.py; sin semilla ni corpus.

### 10.2.2 Sesgos que afectan el juicio

La calificación de probabilidad e impacto está expuesta a sesgos cognitivos documentados. La disponibilidad hace que se sobrestimen los riesgos recordados con facilidad, y el anclaje hace que una primera cifra condicione las siguientes (Tversky y Kahneman, 1974). El registro mitiga ambos sesgos de dos maneras. Cada calificación debe justificarse con un disparador observable en la tabla de respuestas. Además, el panel evaluador debe recalificar de forma independiente antes de que el equipo conozca la calificación original.

Esta limitación tiene una consecuencia para la lectura de los resultados. La clasificación de un riesgo en un nivel no equivale a una medida de su frecuencia. Un riesgo calificado en nivel alto con probabilidad 3 puede resultar irrelevante o decisivo, según lo que muestre la colocalización. Por eso el proyecto convierte las calificaciones en preguntas verificables en los hitos, como se muestra en la sección 10.5.

## 10.3 Análisis cuantitativo

### 10.3.1 Valor monetario esperado

El valor monetario esperado (VME) de un riesgo es el producto de su probabilidad por su impacto monetario. La {T:t03} presenta el VME de los 12 riesgos, ordenados de mayor a menor. La suma exacta es de 636,5 millones de COP, y la reserva se fija en 636,0 millones por redondeo a millones. La exposición bruta, que suma los impactos sin ponderar por probabilidad, es de 1.450,0 millones. La reserva cubre 43,9 % de esa exposición.

:::TABLA t03 | Análisis cuantitativo: valor monetario esperado por riesgo
| Riesgo | Probabilidad (%) | Impacto (millones de COP) | VME (millones de COP) | % del VME | % acumulado |
| --- | --- | --- | --- | --- | --- |
| R-FIN-01 | 55 | 300,0 | 165,0 | 25,9 | 25,9 |
| R-TEC-01 | 60 | 250,0 | 150,0 | 23,6 | 49,5 |
| R-EXT-01 | 50 | 120,0 | 60,0 | 9,4 | 58,9 |
| R-ORG-02 | 50 | 120,0 | 60,0 | 9,4 | 68,3 |
| R-ORG-01 | 40 | 90,0 | 36,0 | 5,7 | 74,0 |
| R-TEC-04 | 35 | 90,0 | 31,5 | 4,9 | 78,9 |
| R-TEC-03 | 40 | 70,0 | 28,0 | 4,4 | 83,3 |
| R-EXT-02 | 40 | 60,0 | 24,0 | 3,8 | 87,1 |
| R-TEC-02 | 30 | 80,0 | 24,0 | 3,8 | 90,9 |
| R-FIN-02 | 25 | 80,0 | 20,0 | 3,1 | 94,0 |
| R-JUR-01 | 20 | 100,0 | 20,0 | 3,1 | 97,2 |
| R-DAT-01 | 20 | 90,0 | 18,0 | 2,8 | 100,0 |
| Suma de VME | — | 1.450,0 | 636,5 | 100,0 | — |
| Reserva de contingencia (redondeada) | — | — | 636,0 | — | — |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (RISKS y RESERVA). VME = probabilidad por impacto (CALCULADO). Probabilidad e impacto son PROPUESTO, sin fuente. La suma exacta es 636,5 millones de COP; la reserva se fija en 636,0 millones de COP por la regla de redondeo al par entero (ficha maestra §7). El redondeo convencional de la mitad hacia arriba daría 637,0 millones; la diferencia de 1,0 millón no altera las conclusiones (PROPUESTO).

Los valores se concentran en pocos riesgos. R-FIN-01 aporta 165,0 millones de COP, equivalentes a 25,9 % del VME. R-TEC-01 aporta 150,0 millones, equivalentes a 23,6 %. Los dos mayores suman 49,5 % y los cuatro primeros suman 68,3 %. Por categoría, los riesgos técnicos aportan 233,5 millones (36,7 %). Los financieros aportan 185,0 millones (29,1 %). Los organizacionales aportan 96,0 millones (15,1 %). Los externos aportan 84,0 millones (13,2 %). Los jurídicos y los de datos aportan 20,0 y 18,0 millones (3,1 % y 2,8 %).

### 10.3.2 Suficiencia de la reserva

El VME es un promedio, y una reserva igual al promedio no cubre los resultados por encima de él. Para medir la suficiencia se calculó la distribución exacta de la pérdida total bajo el supuesto de que los 12 riesgos ocurren de forma independiente. El supuesto es discutible: algunos riesgos se correlacionan, como la devaluación y el costo de los equipos. Aun así, ofrece una referencia. La pérdida mediana es de 640,0 millones de COP, y la probabilidad de que la pérdida supere la reserva es de 50,6 %. Los percentiles 80, 90 y 95 son 850,0, 940,0 y 1.020,0 millones.

La lectura es directa y requiere honestidad. La reserva cubre la pérdida esperada. Tiene cerca de la mitad de probabilidad de ser insuficiente si todos los riesgos se comportan como se calificaron. Cubrir el percentil 80 exigiría 214,0 millones adicionales, equivalentes a 4,5 % del valor solicitado. Esa cifra cabe dentro de la holgura no solicitada de 4.732,7 millones. Por eso el equipo formulador debe decidir con el panel si adopta un percentil mayor como criterio de reserva. Aquí no se adopta, porque la reserva más alta no es admisible hasta conocer los términos de referencia.

Tres escenarios de materialización ilustran el límite. Si los tres riesgos de mayor impacto ocurren juntos, la pérdida suma 670,0 millones y supera la reserva. Si ocurren los dos mayores, la pérdida suma 550,0 millones y consume 86,5 % de la reserva. Si ocurre solo el mayor, la pérdida suma 300,0 millones y consume 47,2 %. La probabilidad conjunta de tres eventos es de 16,5 %, bajo independencia. Los eventos son la devaluación, la saturación de cabezales y el abandono de la custodia. El impacto de R-FIN-01 equivale a 15,9 % del presupuesto de equipos.

## 10.4 Plan de respuesta

### 10.4.1 Respuestas por riesgo

El plan de respuesta asigna a cada riesgo una estrategia, una acción, un responsable, un disparador y una línea de presupuesto. La {T:t04} lo presenta. Las estrategias siguen las cuatro respuestas clásicas de amenazas: mitigar, evitar, transferir y aceptar. Domina la mitigación, con nueve de 12 riesgos; hay un riesgo con aceptación y mitigación, uno con transferencia y mitigación, y uno con evitación.

:::TABLA t04 | Plan de respuesta a los riesgos
| Riesgo | Estrategia | Acción de respuesta | Responsable (rol) | Disparador | Línea de presupuesto |
| --- | --- | --- | --- | --- | --- |
| R-TEC-01 | Mitigar | Modelo de corrección por humedad, banco de calibración y reposición de cabezales. | Especialista en metrología | NRMSE > 30 % en dos verificaciones consecutivas | E07 (150,0 M) |
| R-TEC-02 | Mitigar | Kits solares dimensionados, modo de bajo consumo y repuestos de batería. | Ingeniero de firmware | Disponibilidad mensual < 90 % | E05 (78,0 M), M07 (60,0 M) |
| R-TEC-03 | Mitigar | Enlace satelital de respaldo y almacenamiento local de 7 días. | Ingenieros IoT | Pérdida de paquetes > 10 % durante 72 horas | E06 (35,0 M), S10 (55,0 M) |
| R-TEC-04 | Mitigar | Validación cruzada por departamento y reentrenamiento por tramo. | Científico de datos | R² < 0,70 en el conjunto de validación externo | Sin línea propia |
| R-ORG-01 | Mitigar | Co-diseño de umbrales, formación por comité y uso piloto con registro de decisiones. | Coordinación de apropiación | Menos de 50 % de uso en el tramo 1 | Sin línea propia |
| R-ORG-02 | Mitigar | Convenios por tramo, formación de custodios y cláusula de apertura. | Profesional de convenios | Convenio sin partida al cierre del tramo 2 | S09 (150,0 M) |
| R-EXT-01 | Aceptar y mitigar | Instalación en ventanas secas, técnicos locales y holgura en el cronograma. | Gerencia de proyecto | Retraso de instalación > 3 semanas | Sin línea propia |
| R-EXT-02 | Transferir y mitigar | Póliza todo riesgo, cerramientos y custodia local por sitio. | Técnicos de campo | Dos o más nodos perdidos en un mes | S04 (50,0 M) |
| R-FIN-01 | Mitigar | Compra por tramo con cobertura cambiaria y cotizaciones vigentes. | Gerencia de proyecto | TRM supera en 10 % la de la cotización | Sin línea propia |
| R-FIN-02 | Evitar | Certificación de la IES y de la empresa antes del acta de inicio. | Gerencia de proyecto | Certificación pendiente al mes 2 | Sin línea propia |
| R-JUR-01 | Mitigar | Análisis de libertad de operación y diseño alternativo del módulo afectado. | Consultoría en propiedad intelectual | Solicitud con fase nacional abierta que reivindique el método | S02 (45,0 M) |
| R-DAT-01 | Mitigar | Pruebas de penetración, segmentación y copias de respaldo. | Ingenieros de software | Hallazgo crítico en la auditoría | S03 (30,0 M) |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (RISKS y BUDGET). Los roles y la asociación con líneas de presupuesto son PROPUESTO. M = millones de COP.

El plan tiene un límite visible: de los 12 riesgos, cinco no tienen línea de presupuesto propia. Su respuesta consiste en acciones de gestión sin costo adicional. Son ejemplos la certificación previa de la contrapartida, el diseño de convenios y la instalación en ventanas secas. Las respuestas con línea de presupuesto suman 653,0 millones de COP, equivalentes a 7,0 % del valor solicitado. Abarcan siete riesgos y nueve líneas. La reserva de contingencia cubre los efectos que las respuestas no evitan. La respuesta a R-EXT-01 incluye holgura en el cronograma, pero esa holgura existe solo en las actividades A1.1, A3.1, A3.2 y A3.3. Las instalaciones de los tramos 2 y 3 (A2.3 y A2.4) están en la ruta crítica sin holgura. Por ello, un bloqueo vial durante esas instalaciones retrasa la fecha final salvo que las ventanas secas y los técnicos locales lo absorban.

### 10.4.2 Escalamiento

El escalamiento define quién decide cuando un disparador se activa. La {F:f02} muestra el flujo. Un riesgo de nivel medio lo decide su responsable. Uno de nivel alto escala a la gerencia de proyecto en un plazo corto. Uno de nivel extremo escala al comité directivo, que puede liberar la reserva, reordenar actividades o convocar una compuerta adicional. La regla busca evitar dos fallas habituales. La primera es que un riesgo alto quede en manos de quien no puede decidir. La segunda es que el comité se sature con riesgos menores.

:::FIGURA f02 | El nivel P × I fija quién decide: responsable, gerencia o comité directivo | Nota. Elaboración propia con maestro.py (RISKS). Los plazos de escalamiento son PROPUESTO y se ajustan al reglamento del comité directivo [DATO_USUARIO: reglamento]. Figura generada con matplotlib mediante c10_figs.py; sin semilla ni corpus.

Las consecuencias no previstas de una respuesta también se gestionan. Toda acción de mitigación puede producir efectos no anticipados, y ninguna anticipación es exhaustiva (Merton, 1936). El plan exige entonces monitoreo, no solo previsión. Cada retrospectiva quincenal revisa si una respuesta generó un riesgo nuevo. El registro se actualiza con su probabilidad e impacto antes de la siguiente compuerta.

## 10.5 Verificación de alineación estratégica

### 10.5.1 Lista de verificación por hito

La verificación de alineación estratégica pregunta, en cada hito, si el proyecto sigue siendo coherente con su estrategia. La {T:t05} presenta nueve preguntas, una por hito. Cada pregunta enlaza con un supuesto crítico o un riesgo, exige una evidencia y fija un criterio de pivote. El criterio de pivote responde a la pregunta de qué decisión se toma si la evidencia no aparece. Es el mecanismo que transforma un registro de riesgos en una herramienta de decisión.

:::TABLA t05 | Lista de verificación de alineación estratégica por hito
| Hito y mes | Pregunta de alineación | Supuesto o riesgo vigilado | Evidencia exigida | Criterio de pivote |
| --- | --- | --- | --- | --- |
| H0, mes 2 | ¿Los contratos y convenios fijan una sola arquitectura (corrección en el gateway) y la contrapartida está certificada? | SC-1 y SC-2; R-FIN-02 | Contratos, convenios y plan de trabajo aprobados; certificaciones de contrapartida | Certificación pendiente al mes 2: replantear la contrapartida antes de comprar |
| H1, mes 4 | ¿El estudio de cobertura sostiene el enlace celular, con respaldo satelital, en los sitios del tramo 1? | SC-2; R-TEC-03 | Informe de sitios, de cobertura y de energía | Sitios sin enlace viable: reubicar el sitio o reforzar el respaldo |
| H2, mes 10 | ¿La colocalización generó una línea base de error por departamento con horas-nodo válidas suficientes? | SC-1; R-TEC-01 | Base de datos de colocalización; al menos 60.000 horas-nodo válidas y cuatro rotaciones por departamento | Datos insuficientes: ampliar la colocalización antes de la compuerta |
| H3, mes 12 | ¿El modelo cumple los umbrales y los comités del tramo 1 usan el tablero? | SC-1 y SC-3; R-TEC-04; R-ORG-01 | Acta de C1 con R² ≥ 0,70, NRMSE ≤ 30 % y uso en al menos 50 % de los comités | Incumplimiento de cualquier criterio: no se libera el tramo 2 (Figura 10.3) |
| H4, mes 16 | ¿El tramo 2 mantiene disponibilidad y desempeño bajo polvo, humedad y fallas de energía? | SC-1 y SC-2; R-TEC-02; R-EXT-01 | Informe de disponibilidad y desempeño del tramo 2; disponibilidad mensual ≥ 90 % | Disponibilidad menor que 90 %: reforzar energía y enlace antes de C2 |
| H5, mes 17 | ¿El uso institucional y los convenios de custodia sostienen la consolidación del tramo 3? | SC-3 y SC-4; R-ORG-01; R-ORG-02 | Acta de C2 con umbrales en los tres departamentos, disponibilidad ≥ 90 % y convenios con partida | Convenio sin partida: activar custodia por función o cláusula de apertura |
| H6, mes 19 | ¿La red completa de 100 nodos y 10 gateways quedó operativa y asegurada? | SC-2; R-EXT-02; R-FIN-01 | Inventario de 100 nodos y 10 gateways operativos; pólizas vigentes | Pérdida de nodos sobre el repuesto: reponer con la reserva de nodos y revisar la custodia local |
| H7, mes 23 | ¿Una verificación independiente confirma el desempeño frente a la referencia? | SC-1; argumento y ejecución del premortem | Informe de laboratorio externo y evaluación externa; pendiente 0,65 a 1,35 y sesgo ±5,0 µg/m³ | Umbrales no confirmados: declarar el TRL alcanzado y limitar el alcance de la transferencia |
| H8, mes 24 | ¿Los custodios reciben la red con capacidad, presupuesto y cláusula de apertura firmada? | SC-4; sostenibilidad del premortem; R-ORG-02 | Actas de entrega a custodios y cláusula de apertura firmada | Ningún custodio con capacidad: regir la cláusula de apertura y salida ordenada |
:::NOTA *Nota.* Elaboración propia con datos de la ficha maestra §2, §4 y §6, de maestro.py (HITOS, RISKS) y del premortem de 4.4-MDR.12. Las preguntas y los criterios de pivote son PROPUESTO; los umbrales de desempeño y los criterios de C1 y C2 son los de la ficha.

Las compuertas C1 y C2 son los puntos de mayor consecuencia. La compuerta C1, en el mes 12, condiciona la compra del tramo 2 a tres criterios. El R² debe ser de 0,70 o más. El NRMSE debe ser de 30 % o menos. El tablero debe usarse en 50 % o más de los comités del tramo 1. La compuerta C2, en el mes 17, condiciona la consolidación a tres requisitos. Los umbrales deben cumplirse en los tres departamentos. La disponibilidad mensual debe ser de 90 % o más. Deben existir convenios de custodia con partida. La {F:f03} presenta el árbol de decisión de pivotar o perseverar.

:::FIGURA f03 | C1 y C2 liberan la compra del tramo siguiente solo si se cumplen todos los criterios | Nota. Elaboración propia con la ficha maestra §4 y §7. Los criterios son PROPUESTO; los umbrales de desempeño proceden de EPA (2021) y se aplican a los resultados del piloto. Figura generada con matplotlib mediante c10_figs.py; sin semilla ni corpus.

La estructura de decisión reconoce que perseverar y pivotar son decisiones distintas, y que ambas exigen evidencia. Un pivote puede consistir en reubicar sitios, reforzar el enlace, ampliar la colocalización o declarar el nivel de madurez realmente alcanzado. Una decisión de perseverar sin cumplir los criterios es posible, pero exige un acta con la justificación y la aceptación explícita del riesgo residual. El enfoque coincide con la práctica de desarrollo por etapas con compuertas, donde cada compuerta tiene criterios, entregables y una decisión explícita (Cooper, 2008).

### 10.5.2 Riesgo residual

El riesgo residual es el que permanece después de aplicar las respuestas. El registro no lo califica con una escala propia, y esa omisión es un vacío declarado. Los candidatos a conservar un nivel alto son los de mayor valor esperado (INFERIDO). Son la devaluación, la saturación de cabezales por humedad y el abandono de la custodia. Su gestión depende de factores que el proyecto controla de forma parcial. La humedad se gestiona con el modelo y el banco de calibración. La devaluación se gestiona con la compra por tramos. La custodia se gestiona con convenios, y ese factor depende de decisiones de entidades externas. El panel evaluador debe calificar el riesgo residual de cada riesgo antes de radicar. La calificación usa la misma escala de probabilidad e impacto. Después se compara el resultado con la reserva.

## 10.6 Valor y límites del capítulo

El capítulo crea valor porque vincula cada riesgo con un responsable, un disparador y una decisión. Además, expone la limitación de la reserva en vez de ocultarla. Sus límites son cuatro. Las probabilidades y los impactos carecen de fuente externa. La distribución de pérdidas supone independencia entre riesgos. La admisibilidad de la reserva depende de los términos de referencia. Y los plazos de escalamiento requieren el reglamento del comité directivo, que no existe aún.
