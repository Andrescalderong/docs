%% PREFIJO: F7

# Paso 7. Sistema de indicadores PERS

El Paso 7 diseña el sistema de indicadores que verifica la alternativa seleccionada en el Paso 6. El sistema usa cuatro niveles de la sigla PERS: proceso (R), producto (P), efecto (E) y sostenibilidad (S). Contiene 15 indicadores: seis de proceso, cuatro de producto, tres de efecto y dos de sostenibilidad. El paso fija la taxonomía de producto, resultado e impacto (Output, Outcome e Impact) y valida su coherencia. Articula los indicadores con los criterios de la convocatoria. Comprueba que cada meta de producto tenga recurso y plazo. Las fichas técnicas completas de 12 campos se presentan en el capítulo 12, donde se desarrollan con su análisis. Este paso entrega el diseño y el registro.

El paso aplica la regla que más penalizan los evaluadores: no confundir un producto con un impacto. Un taller realizado es un producto (Funnell y Rogers, 2011). Un comité que usa el tablero para decidir es un resultado (Pawson y Tilley, 1997). Un protocolo que se activa de forma sostenida tras el cierre es un impacto institucional. El proyecto no promete cambios en salud, porque no incluye un diseño causal para medirlos. Los términos de referencia (TdR) no se aportaron, por lo que los pesos de evaluación son supuestos del metaprompt (NO_VERIFICADO). Los umbrales de desempeño de los productos de medición toman como ancla los protocolos de la U.S. Environmental Protection Agency [EPA] (2021) para sensores de partículas finas.


## F7.0 Taxonomía obligatoria: outputs, outcomes e impact

La taxonomía distingue tres niveles según lo que miden. Un producto mide lo que el proyecto hace y entrega. Un resultado mide cómo los destinatarios usan lo entregado y qué cambia en su comportamiento o su capacidad. Un impacto mide la transformación sostenida de las condiciones que justifican el proyecto. Funnell y Rogers (2011) describen esa secuencia como la cadena de resultados de un programa. La {T:t01} presenta los tres niveles con un ejemplo correcto del proyecto y un ejemplo incorrecto que el evaluador penalizaría.

:::TABLA t01 | Taxonomía Output, Outcome e Impact con ejemplos correctos e incorrectos del proyecto
| Nivel | Denominación en MinCiencias | Definición | Qué mide | Horizonte | Ejemplo correcto del proyecto | Ejemplo incorrecto (penalizado) |
| --- | --- | --- | --- | --- | --- | --- |
| Output | Productos y actividades | Bienes, servicios o hechos concretos, tangibles y verificables que resultan de transformar insumos mediante actividades. | El esfuerzo y la producción, no el cambio | Inmediato; durante la ejecución (meses 1 a 24) | Red de 100 nodos y 10 gateways operativa (PERS-P01) | Declarar los 29 talleres y jornadas realizados como impacto |
| Outcome | Resultados y efectos inmediatos | Efectos de corto plazo en los destinatarios tras recibir los productos. Reflejan adopción, uso o cambio inicial de comportamiento. | Cómo los destinatarios usan el producto | Corto plazo; 0 a 12 meses después del producto | 75 % o más de los 15 comités usa el tablero en decisiones documentadas (PERS-E01) | Declarar el número de nodos instalados como resultado |
| Impact | Impacto | Cambio sostenido en las condiciones que justifican el proyecto, como consecuencia de los productos y los resultados. | Si la condición cambió y se mantiene | Mediano plazo; meses 30 a 36, tras el cierre | Protocolo activado ante 80 % o más de las superaciones de umbral confirmadas (PERS-S01) | Declarar una reducción de morbilidad sin diseño causal que la identifique |
:::NOTA *Nota.* Elaboración propia con la taxonomía del metaprompt GENESIS-CTeI y los indicadores de la ficha maestra. La definición de impacto como cambio en las condiciones de una población procede del metaprompt y no se verificó contra el documento de MinCiencias que lo origina (NO_VERIFICADO). Los ejemplos del proyecto son PROPUESTO.

La {F:f00} ubica los 15 indicadores en la cadena y marca el techo de rendición de cuentas. Los 10 indicadores de producto y proceso quedan bajo el techo. Sus metas son compromisos que el proyecto controla. Los tres de resultado y los dos de impacto quedan sobre el techo. Sus metas son de contribución y dependen de que se cumplan los supuestos de uso institucional y de custodia (SC-3 y SC-4). El techo no mide la importancia de los indicadores. Delimita qué puede prometer el proyecto sin depender de terceros.

:::FIGURA f00 | La cadena del proyecto separa 10 outputs, 3 outcomes y 2 impactos institucionales | Nota. Elaboración propia con datos de maestro.py (presupuesto y equipo) e indicadores.py (15 indicadores PERS). El techo separa las metas comprometidas de las metas de contribución. Python 3 y matplotlib; script cF7_figs.py; sin semilla; corte del 13 de octubre de 2026.

El nivel de impacto exige una lectura honesta. Gertler et al. (2016) sostienen que atribuir un cambio a un programa requiere un contrafactual, es decir, una estimación de lo ocurrido sin el programa. El proyecto no incluye ese diseño para la exposición de la población. Por eso los dos indicadores de sostenibilidad miden condiciones institucionales. PERS-S01 mide si el protocolo se activa ante una superación confirmada. PERS-S02 mide si la red continúa bajo custodia. Ambos son impactos institucionales de contribución. Mayne (2012) respalda esa lectura: el análisis de contribución sustenta que un programa contribuyó a un cambio sin atribuirle todo el efecto.

La validación bloqueante verifica cuatro condiciones antes de avanzar. La {T:t02} registra el resultado de cada una con su evidencia. Ninguna condición produce un error fatal. Dos producen una salvedad que se declara. Los indicadores de control R04 y R06 no tienen un resultado propio. La ruta de los artículos hacia el uso institucional es una hipótesis débil sin evidencia propia (VACIO).

:::TABLA t02 | Validación bloqueante de la cadena Output, Outcome e Impact
| Condición | Resultado | Evidencia | Salvedad |
| --- | --- | --- | --- |
| Cada producto tiene al menos un resultado asociado | CUMPLE | P01 y P02 alimentan E02; P01 y P04 alimentan E03; P04 alimenta E01; P03 alimenta E01 por una vía débil | PERS-R04 y PERS-R06 son indicadores de control sin resultado propio; alimentan a los productos |
| Cada resultado se conecta con al menos un impacto | CUMPLE | E01 y E02 alimentan S01; E03 alimenta S02 | Las conexiones son hipótesis de influencia (HIE), no efectos estimados |
| Ningún producto está clasificado como impacto | CUMPLE | Los 10 indicadores R y P tienen taxonomía Output; los 3 E, Outcome; los 2 S, Impact | Ninguna |
| Los impactos son transformaciones medibles a mediano plazo y no actividades | CUMPLE CON RESERVA | S01 y S02 se miden entre los meses 30 y 36 con evaluación externa | Miden condiciones institucionales, no cambio en salud ni en exposición (VACIO) |
:::NOTA *Nota.* Elaboración propia con la ficha maestra §8 y la taxonomía del metaprompt. Resultado: CUMPLE, CUMPLE CON RESERVA o NO CUMPLE. La reserva se explica en la columna de salvedad. Naturaleza: PROPUESTO.

El nodo ND-16 del protocolo de decisión asigna cada nivel PERS a un tipo de la taxonomía. El registro de la {T:t03} muestra el protocolo aplicado. El patrón central es PR-03: el cierre se define por la autonomía que adquieren los custodios, no por la ejecución presupuestal. La ausencia del antipatrón PR-04, la victoria pírrica, se verifica porque ningún indicador mejora a costa del destinatario. La ausencia de PR-05, el falso rescate, no se cumple: los indicadores de sostenibilidad suponen una capacidad de custodia que el territorio aún no demuestra.

:::TABLA t03 | Registro de decisión GENESIS: ND-16 Asignación de output, outcome e impact
| Campo | Contenido |
| --- | --- |
| NODO | ND-16 Asignación de output, outcome e impact |
| CLASE | MAYOR. Fija qué promete el proyecto y qué solo contribuye a lograr. |
| DECISION | Asignar los niveles R y P a Output, el nivel E a Outcome y el nivel S a Impact institucional, con el techo de rendición de cuentas entre P y E. |
| DECIDE | Equipo formulador [DATO_USUARIO: responsable de la decisión]. La propuesta proviene de la instancia analítica. |
| EXCLUYE | Declarar un producto como impacto. Afirmar un efecto en salud sin diseño causal. Comprometer metas de contribución como si fueran de ejecución. |
| NODOS_BLANCOS | 4: 15 indicadores con taxonomía asignada; metas finales de la ficha maestra; umbrales de desempeño con ancla externa (EPA, 2021); cronograma de 104 semanas. |
| NODOS_GRISES | 3: que los comités usen el tablero; que los custodios asuman la operación; que la activación del protocolo reduzca la exposición evitable. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | PR-03 (triunfo soberano): el cierre depende de la autonomía de los custodios y no de la ejecución presupuestal. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. Los indicadores S01 y S02 suponen una capacidad de custodia no verificada. |
| ESCENA_SIMULABLE | Un técnico de la secretaría departamental recibe una alerta del tablero cuando un nodo supera el umbral, la contrasta con el monitor de referencia del sitio y registra la medida de protección activada. |
| EVIDENCIA_JH_A | Meta de 60 personas certificadas y 29 actividades de apropiación con actas firmadas por representantes comunitarios. |
| EVIDENCIA_JH_B | Fórmulas, unidades y líneas base de las 15 fichas del capítulo 12; validación cruzada entre meta, recurso y cronograma. |
| CERCA_CONCEPTUAL | El sistema no mide la salud de la población expuesta; mide mediciones verificadas, uso institucional y continuidad de la red. |
| ESTATUTO_CAUSAL | HIE. Ninguna relación entre niveles se estima como efecto causal. |
| VEREDICTO | Taxonomía adoptada con reserva sobre el nivel S. |
| RAZON_DEL_DESCARTE | Se descarta clasificar S01 y S02 como impacto en salud, porque no existe un diseño que lo identifique. |
| RESULTADO | CIERRA con vacíos declarados (línea base de cinco indicadores y capacidad de custodia). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS y la ficha maestra. EPA (2021): U.S. Environmental Protection Agency. Los nodos blancos tienen anclaje en la ficha maestra; los nodos grises son reglas de sentido común anticipadas.


## F7.1 Estructura jerárquica PERS articulada con el SGR

La estructura jerárquica relaciona cada nivel PERS con el marco lógico, la taxonomía y la cadena de valor. Los indicadores de proceso corresponden a las actividades y miden insumos y actividades. Los de producto corresponden a los componentes. Los de efecto corresponden al propósito. Los de sostenibilidad corresponden al fin. La {T:t04} presenta la estructura con el horizonte, la cantidad y el criterio de viabilidad del Sistema General de Regalías (SGR). Sigue la lógica de los modelos de programa (Weiss, 1995).

:::TABLA t04 | Estructura jerárquica PERS con marco lógico, taxonomía, cadena de valor y viabilidad SGR
| Nivel PERS | Marco lógico | Taxonomía | Cadena de valor | Horizonte | Cantidad | Viabilidad SGR |
| --- | --- | --- | --- | --- | --- | --- |
| R: proceso | Actividades | Output (productos de gestión) | Insumos a actividades | Corto plazo; medición mensual | 6 | Verifica la ejecución presupuestal y las actividades programadas |
| P: producto | Componentes | Output (productos tipificados MMG 2021) | Actividades a productos | Mediano plazo; medición trimestral | 4 | Productos verificables en CvLAC o GrupLAC, registros de propiedad intelectual y certificaciones |
| E: efecto | Propósito | Outcome (resultados inmediatos) | Productos a efectos | Mediano plazo; medición trimestral o semestral | 3 | Evidencia de adopción, uso y cambio de comportamiento en los destinatarios |
| S: sostenibilidad | Fin | Impact (impacto institucional) | Efectos a impactos | Largo plazo; medición anual tras el cierre | 2 | Cambio sostenido articulado con el PDD y con los indicadores territoriales |
| Total |  |  |  |  | 15 |  |
:::NOTA *Nota.* Elaboración propia con la estructura del metaprompt y la ficha maestra §8. MMG: Modelo de Medición de Grupos. PDD: Plan de Desarrollo Departamental. Las cantidades son CALCULADAS desde indicadores.py. La viabilidad SGR describe el criterio de verificación y es PROPUESTO.


### F7.1.1 Articulación con los criterios de viabilidad del SGR

La articulación vincula cada indicador con el criterio de evaluación que sustenta. Los pesos provienen del metaprompt y se tratan como supuesto, porque los TdR no se aportaron. La Ley 2056 de 2020 regula la organización y el funcionamiento del SGR (Congreso de la República, 2020). La política nacional de ciencia, tecnología e innovación orienta el fortalecimiento regional (Departamento Nacional de Planeación [DNP], 2021). La {T:t05} muestra la correspondencia, la evidencia que cada criterio exige y el rango de peso.

:::TABLA t05 | Articulación de los indicadores PERS con los criterios de viabilidad del SGR
| Criterio SGR | Indicadores PERS vinculados | Evidencia requerida | Peso en la evaluación (metaprompt) |
| --- | --- | --- | --- |
| Pertinencia y articulación territorial | PERS-S01 y PERS-S02 | Artículo del PDD y código de la demanda territorial del Anexo 4 [DATO_USUARIO: documentos del PDD y del Anexo 4] | 20 a 25 % |
| Fortalecimiento regional de CTeI | PERS-P01 a PERS-P04 | Productos tipificados MMG 2021 y nivel alcanzado en la escalera de apropiación | 25 a 27 % |
| Calidad técnica | PERS-R01 a PERS-R06 | Metodología validada e indicadores con línea base | 20 a 25 % |
| Impacto esperado | PERS-E01 a PERS-E03, PERS-S01 y PERS-S02 | Cadena de producto, resultado e impacto verificable con indicadores específicos | 15 a 20 % |
| Viabilidad presupuestal | PERS-R04 y la validación cruzada de los PERS-P | Cada meta de producto validada contra un rubro del presupuesto y un plazo del cronograma | 10 a 15 % |
:::NOTA *Nota.* Elaboración propia con los criterios y los rangos del metaprompt GENESIS-CTeI, que son SUPUESTO y NO_VERIFICADO porque los TdR no se aportaron. CTeI: ciencia, tecnología e innovación. Los vínculos entre indicadores y criterios son PROPUESTO.


### F7.1.2 Validación meta-recurso-cronograma

La validación cruzada comprueba que cada meta de producto tenga un rubro del presupuesto y una actividad del cronograma coherentes (PMI, 2021). El sistema detiene la generación si alguna fila resulta incoherente. La {T:t06} aplica el control a los cuatro indicadores de producto con las líneas de presupuesto del capítulo 8 y las actividades del capítulo 9. Los montos no son aditivos, porque una línea puede servir a más de un indicador.

:::TABLA t06 | Validación meta-recurso-cronograma de los indicadores de producto
| Indicador | Meta | Rubro asociado | Monto asignado (COP) | Actividad en el cronograma | Plazo | Coherencia |
| --- | --- | --- | --- | --- | --- | --- |
| PERS-P01 | 100 nodos y 10 gateways | E01, E04, E05, E06, M03, S05 | $ 1.135.000.000 | A1.2, A2.3, A2.4 | Meses 1 a 24 | COHERENTE: 120 nodos, 11 gateways, 10 módulos y 110 sitios cubren la meta |
| PERS-P02 | 1 registro vigente | O03, S02 | $ 60.000.000 | A2.2, A1.4 | Meses 1 a 24 | COHERENTE: el registro inicia en el mes 12, tras la validación de C1 |
| PERS-P03 | 2 sometidos y al menos 1 aceptado | O01 | $ 25.000.000 | A1.4, A1.6 | Meses 14 a 24 | COHERENTE CON OBSERVACIÓN: la autoría usa contrapartida, no una línea SGR |
| PERS-P04 | 29 actividades | M05, V05, O02 | $ 132.000.000 | A3.1, A3.2 | Meses 2 a 24 | COHERENTE CON OBSERVACIÓN: la meta del mes 17 iguala la meta final |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (presupuesto SGR y cronograma). Los montos son CALCULADOS como suma de las líneas indicadas. La asignación de líneas a indicadores es PROPUESTO. Ninguna fila activa la alerta bloqueante. Decimales con coma y miles con punto.

Ninguna fila resulta incoherente, por lo que el paso continúa. Dos filas llevan una observación. PERS-P03 no tiene una línea SGR de autoría. El tiempo de investigación es contrapartida de la entidad ejecutora, y su cumplimiento depende de una certificación pendiente. PERS-P04 alcanza en el mes 17 la meta final de 29 actividades, y el mes 24 no añade actividades. Esa decisión adelanta el cumplimiento, pero deja los últimos siete meses sin meta adicional de apropiación.


## F7.2 Registro de las fichas técnicas de los 15 indicadores

Cada indicador tiene una ficha técnica de 12 campos: identificación, definición, fórmula, línea base, metas, periodicidad, fuente de datos, desagregación, limitaciones, supuestos, verificación y metadata. El capítulo 12 presenta las 15 fichas completas, una por tabla, desde la Tabla 12.2 hasta la Tabla 12.18, excepto las Tablas 12.12 y 12.13. Este paso registra los campos centrales de cada indicador en dos tablas. La {T:t07} reúne la identificación, la fórmula y la línea base. La {T:t08} reúne las metas, la periodicidad, la fuente y la verificación.

:::TABLA t07 | Registro de indicadores: identificación, fórmula y línea base
| Código | Nombre | Nivel PERS | Taxonomía | OE | Fórmula | Unidad | Línea base (naturaleza) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PERS-R01 | Cumplimiento del despliegue por tramo | Proceso (R) | Output | OE2 | Nodos instalados y operativos ÷ nodos programados × 100 | % | 0 (CALCULADO) |
| PERS-R02 | Ciclos de calibración ejecutados | Proceso (R) | Output | OE1 | Número de ciclos completos de entrenamiento, validación y despliegue del modelo de corrección | ciclos | 0 (CALCULADO) |
| PERS-R03 | Disponibilidad de la plataforma en la nube | Proceso (R) | Output | OE2 | Horas de servicio ÷ horas del mes × 100 | % | VACIO (VACIO) |
| PERS-R04 | Desviación de la ejecución presupuestal | Proceso (R) | Output | OE3 | (Ejecución acumulada − programación acumulada) ÷ programación acumulada × 100 | % | 0 (CALCULADO) |
| PERS-R05 | Horas-nodo de colocalización válidas | Proceso (R) | Output | OE1 | Suma de horas con dato pareado entre nodo y referencia que cumplen el control de calidad | horas-nodo | 0 (CALCULADO) |
| PERS-R06 | Cumplimiento de informes de seguimiento | Proceso (R) | Output | OE3 | Informes técnicos y financieros entregados a tiempo ÷ informes exigidos × 100 | % | 0 (CALCULADO) |
| PERS-P01 | Red de 100 nodos y 10 gateways operativa | Producto (P) | Output | OE2 | Nodos operativos con disponibilidad mensual ≥ 90 % y gateways con enlace principal o alterno activo | nodos / gateways | 0 / 0 (CALCULADO) |
| PERS-P02 | Software de corrección y gemelo digital registrado | Producto (P) | Output | OE1 | Registros de software ante la DNDA (modelo de corrección, firmware y gemelo digital) | registros | 0 (CALCULADO) |
| PERS-P03 | Artículos científicos en revistas Q1 o Q2 | Producto (P) | Output | OE1 | Artículos sometidos y aceptados con filiación del proyecto | artículos | 0 (CALCULADO) |
| PERS-P04 | Actividades de apropiación social documentadas | Producto (P) | Output | OE3 | Talleres de co-diseño (nivel 3) más jornadas públicas (niveles 1 y 2) con acta y lista de asistencia | actividades | 0 (CALCULADO) |
| PERS-E01 | Uso institucional del tablero y del protocolo | Efecto (E) | Outcome | OE3 | Comités focalizados con al menos una decisión documentada por trimestre basada en el tablero ÷ comités focalizados × 100 | % | VACIO (VACIO) |
| PERS-E02 | Reducción relativa de falsas alarmas | Efecto (E) | Outcome | OE3 | 1 − (tasa de falsas alarmas del periodo ÷ tasa de línea base medida en el tramo 1) | % | Se mide en el tramo 1 (VACIO) |
| PERS-E03 | Capacidad instalada en custodios | Efecto (E) | Outcome | OE3 | Personas con evaluación práctica aprobada en mantenimiento, lectura y operación ÷ personas formadas × 100, y número absoluto | personas | 0 (CALCULADO) |
| PERS-S01 | Activación del protocolo ante superación de umbral | Sostenibilidad (S) | Impact | OE3 | Eventos de superación de umbral con medida de protección activada y registrada ÷ eventos de superación confirmados × 100 | % | VACIO (VACIO) |
| PERS-S02 | Continuidad de la red bajo custodia | Sostenibilidad (S) | Impact | OE3 | Nodos operados por custodios con partida y competencia a los 12 meses del cierre ÷ nodos entregados × 100 | % | VACIO (VACIO) |
:::NOTA *Nota.* Elaboración propia con datos de indicadores.py. Cinco líneas base son VACIO: PERS-R03, PERS-E01, PERS-E02, PERS-S01 y PERS-S02; se miden en el tramo 1 o en el primer trimestre completo de operación. Las demás son CALCULADAS como cero al inicio de la ejecución. OE: objetivo específico.

:::TABLA t08 | Registro de indicadores: metas, periodicidad, fuente y verificación
| Código | Meta al mes 12 | Meta al mes 17 | Meta final | Frecuencia | Responsable de medición | Fuente de datos | Medio de verificación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PERS-R01 | 30 nodos (100 % del tramo 1) | 70 nodos adicionales (100 % de los tramos 2 y 3) | 100 nodos y 10 gateways (100 %) | Mensual | Ingenieros IoT y de campo | Inventario de la plataforma y actas de instalación | Acta de instalación con coordenadas y número de serie |
| PERS-R02 | 2 ciclos (tramo 1) | 4 ciclos acumulados | 6 ciclos (2 por tramo) | Mensual | Científico de datos | Registro de versiones del modelo | Informe de validación firmado por la metrología |
| PERS-R03 | ≥ 99,0 % | ≥ 99,0 % | ≥ 99,0 % | Mensual | Ingenieros de software y nube | Monitor de servicio de la plataforma | Reporte mensual del proveedor de nube |
| PERS-R04 | \|desviación\| ≤ 10 % | \|desviación\| ≤ 10 % | \|desviación\| ≤ 5 % al cierre | Mensual | Gerencia de proyecto | Sistema de seguimiento presupuestal | Informe financiero conciliado con el técnico |
| PERS-R05 | ≥ 60.000 horas-nodo en el tramo 1 | ≥ 60.000 + rotaciones trimestrales | ≥ 60.000 y 4 rotaciones por departamento | Mensual | Especialista en metrología | Base de datos de colocalización | Bitácora de la referencia y tablero de calidad de datos |
| PERS-R06 | 100 % | 100 % | 100 % | Mensual | Gerencia de proyecto | Sistema de seguimiento del financiador | Radicados de entrega |
| PERS-P01 | 30 / 3 al mes 12 | 70 / 7 al mes 17 y 100 / 10 al mes 19 | 100 / 10 al mes 24 | Trimestral | Ingenieros IoT y de campo | Plataforma e inventario | Inventario con huella de configuración y registro fotográfico |
| PERS-P02 | 0 | 1 solicitud radicada | 1 registro vigente | Trimestral | Profesional de convenios y custodia | Certificado de la DNDA | Certificado de registro |
| PERS-P03 | 0 | 1 sometido | 2 sometidos y al menos 1 aceptado al mes 24 | Trimestral | Investigador principal | Plataformas editoriales y CvLAC | Carta de aceptación y soporte de envío |
| PERS-P04 | 10 actividades | 29 actividades acumuladas | 29 actividades (20 talleres y 9 jornadas) | Trimestral | Coordinación de apropiación social | Actas y listas de asistencia | Actas firmadas por representantes comunitarios |
| PERS-E01 | ≥ 50 % (piloto) | ≥ 65 % | ≥ 75 % al mes 24 | Trimestral | Coordinación de apropiación social | Actas de los comités y registro de decisiones del tablero | Acta del comité con referencia a la lectura del tablero |
| PERS-E02 | Línea base medida | ≥ 15 % | ≥ 30 % de reducción relativa | Trimestral | Profesional en calidad del aire | Registro de alertas y verificación con referencia | Cruce entre alertas emitidas y mediciones de referencia |
| PERS-E03 | 20 personas | 40 personas | ≥ 60 personas certificadas | Semestral | Profesional de convenios y custodia | Registros de formación y evaluación práctica | Certificados y actas de evaluación práctica |
| PERS-S01 | No aplica (medición posproyecto) | No aplica | ≥ 80 % a los 12 meses posteriores al cierre | Anual, 6 a 12 meses tras el cierre | Custodios y secretarías de gestión del riesgo | Registro de eventos y de medidas | Evaluación externa posproyecto |
| PERS-S02 | No aplica | No aplica | ≥ 70 % a los 12 meses posteriores al cierre | Anual, 12 meses tras el cierre | Profesional de convenios y custodia | Convenios, presupuestos y plataforma | Evaluación externa posproyecto |
:::NOTA *Nota.* Elaboración propia con datos de indicadores.py. Las metas de los meses 12 y 17 corresponden a las compuertas C1 y C2. Las metas son PROPUESTO. La medición de PERS-S01 y PERS-S02 ocurre fuera de la ejecución y su financiación es VACIO. Decimales con coma y miles con punto.

Los dos registros muestran tres regularidades. Primero, las metas de producto y proceso son numéricas y verificables. Cuatro de las cinco metas de efecto y sostenibilidad dependen de una línea base aún inexistente. Segundo, los responsables de medición coinciden con cargos del presupuesto. Tercero, casi ninguna fuente depende de un tercero. Las actas de los comités y los registros de eventos de los custodios son la excepción, y exigen un acuerdo de datos. Esa dependencia explica por qué los cinco indicadores de mayor riesgo son los de efecto y sostenibilidad.

El Paso 7 crea valor al convertir una lista de metas en un sistema auditable. Cada indicador tiene una definición, una fórmula, una línea base con su naturaleza y una evidencia de verificación. La taxonomía impide que el proyecto prometa como impacto lo que solo es un producto. El capítulo 12 desarrolla las fichas completas, y los capítulos 13 y 18 los conectan con la cadena causal y el marco lógico.
