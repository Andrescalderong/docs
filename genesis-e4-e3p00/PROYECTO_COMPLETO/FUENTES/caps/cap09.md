%% PREFIJO: 9

# Capítulo 9. Cronograma

Este capítulo programa las 17 actividades de la estructura de desglose del trabajo en una red de precedencias. El cálculo usa el método de la ruta crítica (CPM) sobre duraciones en semanas. La duración total es de 104 semanas, equivalentes a 24 meses, y coincide con la ruta crítica. El capítulo presenta el diagrama de Gantt, la matriz de hitos y la ruta crítica con sus holguras. Presenta también las sesiones de revisión que sostienen las decisiones de pivote o perseverancia. Todas las duraciones son PROPUESTO. Ninguna se verificó con términos de referencia, que no se aportaron.


## 9.1 Cronograma General (Gantt)

El cronograma organiza el trabajo en tres fases que coinciden con los tramos de despliegue. La fase 1 abarca las semanas 0 a 50 y termina en la compuerta C1. La fase 2 abarca las semanas 50 a 70 y termina en la compuerta C2. La fase 3 abarca las semanas 70 a 104 y termina con el cierre y la transferencia. El Project Management Institute [PMI] (2021) define el cronograma como un modelo que vincula actividades, duraciones, dependencias y restricciones. La {F:f01} presenta el diagrama de Gantt con las 17 actividades, los nueve hitos y las holguras.

:::FIGURA f01 | Una ruta crítica de 13 actividades ocupa las 104 semanas; 4 actividades tienen holgura | Nota. Elaboración propia con datos de maestro.py (red ACT calculada por CPM). Semanas desde el inicio en el eje inferior y meses de calendario en el eje superior; trama punteada: holgura. Python 3 y matplotlib; script c9_figs.py; sin semilla; corte del 13 de octubre de 2026.

La red tiene un diseño deliberadamente secuencial en su tronco. La contratación (A0.1, ocho semanas) precede al diseño de enlace y energía (A2.1, seis semanas). Después, la adquisición del lote 1 (A1.2) y el desarrollo de firmware (A2.2) corren en paralelo durante diez semanas. La colocalización del piloto (A1.3) dura 16 semanas, el entrenamiento del modelo (A1.4) dura ocho, y la compuerta C1 consume dos. Esa secuencia suma 50 semanas y condiciona la ampliación al tramo 2. El diseño favorece la evidencia sobre la velocidad, como en los procesos de etapas y compuertas (Cooper, 2008). Ninguna compra de tramo posterior se adelanta a una decisión.

Dos posiciones compiten sobre cómo programar un proyecto con incertidumbre técnica (Collingridge, 1980). La posición predictiva fija el plan completo desde el inicio y mide la desviación frente a él (PMI, 2021). La posición adaptativa recomienda ciclos cortos de construcción, medición y aprendizaje, con decisiones de pivote según los datos (Ries, 2011). El proyecto adopta una síntesis. El tronco de 104 semanas es predictivo, porque la compra de equipos importados exige plazos firmes. Las decisiones de las compuertas son adaptativas, porque dependen de datos que solo existen tras el piloto. La consecuencia es que el plan acepta modificaciones en cada compuerta, pero no entre ellas.

Las dependencias siguen la lógica de fin a inicio. Cada actividad comienza cuando termina su predecesora, sin adelantos ni retrasos programados. La única excepción de paralelismo es la pareja A1.2 y A2.2. La actividad A3.1, el co-diseño de umbrales con los comités, dura 24 semanas. Comienza en la semana 12, cuando termina la selección de sitios (A1.1). Debe terminar antes de la compuerta C1, porque el criterio de uso del tablero de C1 exige que los comités conozcan los umbrales. Su holgura de 12 semanas protege esa condición.

La estimación de las duraciones exige una cautela explícita. Las duraciones de la red son estimaciones de esta formulación, y ninguna proviene de datos del proyecto. Tversky y Kahneman (1974) documentaron que las personas estiman con anclaje en valores iniciales y subestiman la incertidumbre. La mitigación consiste en contrastar cada duración con la experiencia del equipo. Cada duración se recalibra en la compuerta C1, con los datos de las primeras 50 semanas. Las actividades A1.3, A1.4 y A2.3 suman 36 semanas de la ruta crítica y concentran la incertidumbre técnica. Reciben la primera revisión.

Los hitos del cronograma son nueve y se denominan H0 a H8. H0 ocurre en el mes 2 con la contratación completa. H3 y H5 son las compuertas C1 y C2, en los meses 12 y 17. H8 cierra el proyecto en el mes 24. El mes de cada hito resulta de dividir las semanas entre 52/12 y redondear hacia arriba. Esa convención asigna cada hito al mes en que termina. Un hito puede ocurrir hasta cuatro semanas antes del cierre de ese mes. El acta de inicio debe fijar las fechas exactas [DATO_USUARIO: fecha del acta de inicio].


## 9.2 Hitos y Entregables

Cada hito se verifica con una evidencia definida antes de la ejecución. Funnell y Rogers (2011) recomiendan separar el producto verificable del esfuerzo que lo genera, y el cronograma sigue ese criterio. Un hito no se declara cumplido porque la actividad termine, sino porque la evidencia exista. La {T:t01} presenta la matriz de nueve hitos con su semana, su mes, las actividades que lo cierran, el aprobador y el criterio de verificación.

:::TABLA t01 | Matriz de hitos y entregables con criterio de verificación
| Hito | Entregable | Semana | Mes | Actividades que lo cierran | Aprobador | Criterio de verificación |
| --- | --- | --- | --- | --- | --- | --- |
| H0 | Acta de inicio y contratación completa | 8 | 2 | A0.1 | Gerencia de proyecto | Contratos, convenios y plan de trabajo aprobados |
| H1 | Sitios del tramo 1 y diseño de enlace y energía listos | 14 | 4 | A1.1, A2.1 | Gerencia de proyecto y dirección científica | Informe de sitios, de cobertura y de energía |
| H2 | Colocalización del tramo 1 finalizada | 40 | 10 | A1.3 | Dirección científica | Base de datos de colocalización y línea base de error medida |
| H3 | Compuerta C1: modelo validado en el piloto | 50 | 12 | C1 | Comité directivo | Acta de compuerta con NRMSE y R² frente a referencia |
| H4 | Tramo 2 instalado y verificado | 68 | 16 | A1.5 | Gerencia de proyecto | Informe de disponibilidad y desempeño del tramo 2 |
| H5 | Compuerta C2: uso institucional y desempeño | 70 | 17 | C2 | Comité directivo | Acta de compuerta con uso del tablero y convenios |
| H6 | Tramo 3 instalado | 82 | 19 | A2.4 | Gerencia de proyecto | Inventario de 100 nodos y 10 gateways operativos |
| H7 | Ensayo independiente y evaluación final | 98 | 23 | A1.6 | Dirección científica | Informe de laboratorio externo y evaluación externa |
| H8 | Transferencia y cierre del tramo 3 | 104 | 24 | A3.4 | Comité directivo | Actas de entrega a custodios y cláusula de apertura firmada |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (HITOS y ACT). La semana es el fin temprano de la actividad que define el hito. El aprobador es PROPUESTO y sigue la matriz RACI del capítulo 7. Decimales con coma.

La matriz distingue tres tipos de hito. Los hitos de preparación (H0, H1 y H6) acreditan que existen contratos, sitios o inventario. Los hitos de desempeño (H2, H4 y H7) acreditan mediciones frente a la referencia. Los hitos de decisión (H3, H5 y H8) acreditan que el comité directivo autorizó el paso siguiente. Solo los hitos de decisión liberan compras (Cooper, 2008). Esa asimetría es intencional: protege el presupuesto de desembolsos sin evidencia. La contrapartida es que tres decisiones concentran la responsabilidad del proyecto.

La madurez tecnológica añade un criterio de lectura. H2 y H4 verifican el desempeño en un entorno relevante, que corresponde a los niveles 5 y 6 de madurez tecnológica. H6 y H7 verifican la demostración en entorno operativo, que corresponde al nivel 7 (Mankins, 1995). El proyecto parte del nivel 4 y no promete el nivel 8, que exige una calificación independiente fuera del plazo. Esa correspondencia es PROPUESTO y debe confirmarse con la evaluación externa del mes 12.

La {T:t02} convierte los hitos y los indicadores en un calendario de entregas al financiador y a los comités. Incluye los informes periódicos del sistema de indicadores PERS, las evaluaciones externas, el ensayo independiente y las mediciones posteriores al cierre. La frecuencia de cada informe sigue la ficha del indicador. El calendario real depende de los términos de referencia [DATO_USUARIO: calendario de informes exigido por el financiador].

:::TABLA t02 | Calendario de entregas e informes del proyecto
| Entrega | Frecuencia | Cantidad | Meses | Responsable | Naturaleza |
| --- | --- | --- | --- | --- | --- |
| Informe mensual de seguimiento (PERS-R01 a R06) | Mensual | 24 | Meses 1 a 24 | Gerencia de proyecto | PROPUESTO |
| Informe trimestral de producto y efecto (PERS-P01 a P04, E01, E02) | Trimestral | 8 | Meses 3, 6, 9, 12, 15, 18, 21 y 24 | Gerencia de proyecto | PROPUESTO |
| Informe semestral de capacidad instalada (PERS-E03) | Semestral | 4 | Meses 6, 12, 18 y 24 | Profesional de convenios y custodia | PROPUESTO |
| Acta de compuerta C1 | Una vez | 1 | Mes 12 | Comité directivo | PROPUESTO |
| Acta de compuerta C2 | Una vez | 1 | Mes 17 | Comité directivo | PROPUESTO |
| Evaluación externa independiente (línea S07) | Dos veces | 2 | Meses 12 y 24 | Evaluador externo | PROPUESTO |
| Ensayo de desempeño con laboratorio externo (línea S08) | Una campaña | 1 | Meses 20 a 24 | Laboratorio externo | PROPUESTO |
| Acta de entrega a custodios y cierre (C3) | Una vez | 1 | Mes 24 | Comité directivo | PROPUESTO |
| Medición posproyecto de PERS-S01 y PERS-S02 | Anual | 2 | Meses 30 y 36 | Evaluador externo | PROPUESTO |
:::NOTA *Nota.* Elaboración propia con datos de la ficha maestra §6 y §8 y del capítulo 12. Las mediciones de los meses 30 y 36 ocurren después del cierre y no se financian con el presupuesto SGR. Naturaleza: PROPUESTO. Decimales con coma.

El calendario suma 24 informes mensuales, ocho trimestrales y cuatro semestrales durante la ejecución. Esa carga equivale a 36 entregas periódicas en 24 meses, además de las actas y las evaluaciones. La carga de reporte consume tiempo de la gerencia y de los profesionales de convenios (PMI, 2021). El presupuesto asigna un cargo de gerencia (línea P06) y uno de convenios y custodia (línea P14). Si los términos de referencia exigen una frecuencia mayor, la gerencia necesita apoyo adicional que el presupuesto no incluye.


## 9.3 Ruta Crítica

La ruta crítica es la secuencia más larga de actividades dependientes y fija la duración mínima del proyecto (PMI, 2021). En esta red suma 104 semanas y comprende 13 de las 17 actividades. Dos ramas críticas corren en paralelo entre las semanas 14 y 24: la adquisición del lote 1 (A1.2) y el desarrollo de firmware (A2.2). Las dos duran diez semanas y no tienen holgura. La {T:t03} presenta el cálculo completo y la {F:f02} muestra el diagrama de red.

:::TABLA t03 | Análisis de ruta crítica por actividad
| Id | Actividad | WP | Duración (sem.) | Inicio temprano | Fin temprano | Inicio tardío | Fin tardío | Holgura (sem.) | Crítica |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0.1 | Contratar equipo y firmar convenios de ejecución | WP0 | 8 | 0 | 8 | 0 | 8 | 0 | Sí |
| A1.1 | Seleccionar sitios y diseñar la colocalización | WP1 | 4 | 8 | 12 | 10 | 14 | 2 | No |
| A2.1 | Diseñar arquitectura de enlace y energía | WP2 | 6 | 8 | 14 | 8 | 14 | 0 | Sí |
| A3.1 | Co-diseñar umbrales y protocolo de alerta con comités | WP3 | 24 | 12 | 36 | 24 | 48 | 12 | No |
| A1.2 | Adquirir y caracterizar lote 1 de nodos y referencias | WP1 | 10 | 14 | 24 | 14 | 24 | 0 | Sí |
| A2.2 | Desarrollar firmware y plataforma base | WP2 | 10 | 14 | 24 | 14 | 24 | 0 | Sí |
| A1.3 | Colocalizar y calibrar en el piloto (tramo 1) | WP1 | 16 | 24 | 40 | 24 | 40 | 0 | Sí |
| A1.4 | Entrenar y validar el modelo de corrección | WP1 | 8 | 40 | 48 | 40 | 48 | 0 | Sí |
| C1 | Compuerta C1: decisión de ampliación al tramo 2 | WP0 | 2 | 48 | 50 | 48 | 50 | 0 | Sí |
| A2.3 | Instalar tramo 2 (40 nodos, 4 gateways) | WP2 | 12 | 50 | 62 | 50 | 62 | 0 | Sí |
| A3.2 | Poner en uso el tablero con los comités | WP3 | 12 | 50 | 62 | 56 | 68 | 6 | No |
| A1.5 | Reentrenar y verificar por departamento (tramo 2) | WP1 | 6 | 62 | 68 | 62 | 68 | 0 | Sí |
| C2 | Compuerta C2: decisión de consolidación al tramo 3 | WP0 | 2 | 68 | 70 | 68 | 70 | 0 | Sí |
| A2.4 | Instalar tramo 3 (30 nodos, 3 gateways) | WP2 | 12 | 70 | 82 | 70 | 82 | 0 | Sí |
| A3.3 | Formar custodios y firmar convenios por tramo | WP3 | 16 | 70 | 86 | 82 | 98 | 12 | No |
| A1.6 | Verificar desempeño final y ensayo independiente | WP1 | 16 | 82 | 98 | 82 | 98 | 0 | Sí |
| A3.4 | Transferir, cerrar y evaluar | WP0 | 6 | 98 | 104 | 98 | 104 | 0 | Sí |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (función cpm). Duraciones en semanas, PROPUESTO. Inicio y fin tempranos y tardíos, holgura y ruta crítica, CALCULADO por pasada hacia adelante y hacia atrás. Una actividad es crítica si su holgura total es cero. Decimales con coma.

:::FIGURA f02 | 13 de 17 actividades forman la ruta crítica; las demás tienen holguras de 2 a 12 semanas | Nota. Elaboración propia con datos de maestro.py (red ACT). ES y EF: inicio y fin tempranos; LS y LF: inicio y fin tardíos; H: holgura, en semanas. Línea continua gruesa: dependencia crítica. Python 3 y matplotlib; script c9_figs.py; sin semilla; corte del 13 de octubre de 2026.

Cuatro actividades tienen holgura: A1.1 con dos semanas, A3.2 con seis, y A3.1 y A3.3 con doce cada una. Las tres últimas pertenecen al paquete de uso institucional (WP3). Esa distribución indica que el proyecto absorbe retrasos de apropiación social sin afectar el plazo, pero no retrasos de medición, de red o de gestión. Por consiguiente, tres riesgos amenazan más el cronograma. Son R-TEC-01 (saturación de cabezales), R-EXT-01 (bloqueos viales) y R-FIN-01 (devaluación, que alarga la compra). Los tres están en nivel alto o extremo.

El cálculo de la ruta crítica supone recursos suficientes para ejecutar en paralelo las actividades independientes. El PMI (2021) advierte que la nivelación de recursos puede alterar la ruta. En esta red el supuesto se cumple, porque las actividades paralelas usan cargos distintos. A1.2 emplea al equipo de medición (WP1). A2.2 emplea al equipo de red y plataforma (WP2). A3.1 emplea al equipo de apropiación (WP3). Ningún cargo figura en dos actividades simultáneas, y por tanto la nivelación no modifica la duración.

El cronograma no incluye una reserva de plazo explícita. Esa ausencia constituye una debilidad que el equipo reconoce. La duración de 104 semanas es la suma exacta de la ruta crítica. Cualquier retraso de una actividad crítica se traslada al cierre. Un ejemplo ilustra el efecto. La decisión DEC-F08 fija hasta 12 semanas de importación por lote. Si el pedido del lote 1 se emite en la semana 12, el equipo llega en la semana 24, cuando termina A1.2. Cualquier demora de aduana desplaza A1.3 y todo lo posterior.

Tres estrategias mitigan ese riesgo. La primera es emitir el pedido del lote 1 antes de A1.2, con una orden condicionada a la firma del contrato. Así el plazo de importación se solapa con A2.1. La segunda es instalar los tramos 2 y 3 en ventanas secas. Esa medida reduce la probabilidad del riesgo de bloqueos viales (Organización Internacional de Normalización [ISO], 2018). La tercera es mantener los 20 nodos de reserva y el gateway adicional en bodega regional. Así una falla no espera una importación. Ninguna de las tres estrategias agrega semanas al plan. Un análisis previo al hecho (Klein, 2007) debe confirmar estos supuestos antes del acta de inicio.

La ruta crítica también permite priorizar el seguimiento. El equipo revisa semanalmente las 13 actividades críticas y mensualmente las cuatro con holgura. Si una actividad no crítica consume más de la mitad de su holgura, el equipo la reclasifica como vigilada. Por ejemplo, si A3.1 termina después de la semana 42, ha consumido más de la mitad de su holgura y se informa a la gerencia. La regla es PROPUESTO y se ajusta con los primeros tres meses de datos reales.


## 9.4 Sesiones de Revisión y Aprendizaje

Las sesiones de revisión convierten el cronograma en un instrumento de aprendizaje y no solo de control. El proyecto programa tres tipos de sesión. Las retrospectivas quincenales reúnen al equipo operativo, 52 en las 104 semanas, y examinan qué funcionó, qué falló y qué se ajusta (Ries, 2011). Las revisiones de fase ocurren en las semanas 48, 68 y 104, antes de cada compuerta, con la gerencia y la dirección científica. Los puntos de decisión pivote o perseverancia ocurren en C1, C2 y C3 con el comité directivo y el financiador.

El fundamento teórico distingue dos niveles de aprendizaje. Argyris y Schön (1978) llaman aprendizaje de lazo simple al ajuste de acciones dentro de metas dadas. Llaman aprendizaje de lazo doble al cuestionamiento de las metas y los supuestos. Las retrospectivas quincenales pertenecen al primer nivel. Las revisiones de fase y las compuertas pertenecen al segundo, porque pueden cambiar el diseño. La mejora continua que Deming (1986) propone exige ambos niveles. Una retrospectiva que corrige la rutina no basta si el supuesto sobre la generalización del modelo entre departamentos (R-TEC-04) es falso.

Cada sesión deja un registro con tres campos: decisión, supuesto afectado y dato que la sustenta. Las lecciones aprendidas se incorporan al registro de riesgos y al diccionario de la EDT. Las compuertas usan las preguntas de alineación del capítulo 10 y el árbol de decisión pivote o perseverancia. Si el modelo no cumple los umbrales en C1, el comité puede detener el tramo 2, revisar el método o reforzar el co-diseño. Esas tres respuestas son PROPUESTO y provienen del análisis de decisión de la sección 4.4-MDR.
