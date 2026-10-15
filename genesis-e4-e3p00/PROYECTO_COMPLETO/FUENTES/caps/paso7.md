%% PREFIJO: F7
# Paso 7. Sistema de indicadores PERS

El Paso 7 diseña el sistema de indicadores que verifica la alternativa seleccionada. El sistema PERS reúne 15 indicadores en cuatro niveles: proceso (R), producto (P), efecto (E) y sostenibilidad (S). Este paso define la taxonomía, la estructura jerárquica, la articulación con los criterios del SGR y la validación entre metas y recursos. Presenta también la ficha técnica de cada indicador en dos tablas compactas. El capítulo 12 desarrolla cada ficha con sus 12 campos, su línea base y su cronograma de medición. Las dos presentaciones usan los mismos datos y no pueden diferir.

## F7.0 Taxonomía obligatoria: outputs, outcomes e impacts

Los evaluadores penalizan la confusión entre tres niveles. Un output es un bien, un servicio o un hecho verificable que agota un objetivo específico. Un outcome es el efecto inmediato en quienes reciben el output. Un impact es la transformación estructural y sostenida que se deriva de los outcomes. El error más frecuente consiste en presentar un indicador de gestión como si fuera un impacto. La {T:t01} aplica la taxonomía al proyecto con un ejemplo correcto y otro incorrecto de cada nivel.

:::TABLA t01 | Taxonomía Output-Outcome-Impact aplicada al proyecto
| Nivel | En MinCiencias | Definición | Mide | Horizonte | Ejemplo correcto del proyecto | Ejemplo incorrecto |
| --- | --- | --- | --- | --- | --- | --- |
| Output | Productos y actividades | Bienes, servicios o hechos concretos y verificables que agotan los objetivos específicos | El esfuerzo o la producción, no el cambio | Inmediato, durante la ejecución | 100 nodos y 10 gateways operativos al mes 24 (PERS-P01) | Declarar la instalación de la red como impacto del proyecto |
| Outcome | Resultados o efectos inmediatos | Efectos de corto plazo en los destinatarios tras recibir los outputs; reflejan adopción o uso | Cómo los beneficiarios usan el producto | De 0 a 12 meses posteriores al output | Al menos 75 % de los comités usa el tablero en decisiones documentadas (PERS-E01) | Declarar el número de personas capacitadas como resultado de uso |
| Impact | Impacto | Transformación sostenida que se deriva de los outcomes | Si el proyecto resolvió el problema | De 1 a 5 años posteriores al proyecto | Al menos 70 % de la red opera bajo custodia 12 meses después del cierre (PERS-S02) | Declarar una reducción de morbilidad sin línea base ni diseño causal |
:::NOTA *Nota.* Elaboración propia con la especificación del metaprompt y la ficha maestra (sección 8). El proyecto no promete efectos en salud: los impacts son de uso institucional y de continuidad.

La {F:f01} ordena los 15 indicadores en la cadena lógica. Los diez indicadores R y P son outputs, los tres E son outcomes y los dos S son impacts. Los impacts se miden entre 6 y 12 meses después del cierre y por una evaluación externa (decisión DEC-F10). Esa medición posterior exige una fuente de financiación que la línea S07 solo cubre hasta el mes 24.

:::FIGURA f01 | Diez outputs sostienen tres outcomes y dos impactos que se miden después del cierre | Nota. Elaboración propia con maestro/indicadores.py y maestro.py. Cadena lógica de los 15 indicadores PERS. Figura generada con matplotlib mediante cF7_figs.py; sin semilla ni corpus.

### F7.0.1 Validación bloqueante

El sistema verifica cuatro condiciones antes de avanzar. Cada output debe tener al menos un outcome asociado. Cada outcome debe conectarse con al menos un impacto. Ningún output puede clasificarse como impacto. Los impactos deben ser transformaciones medibles a mediano o largo plazo. La {T:t02} registra el resultado. Una condición obtiene PARCIAL: dos outputs de gestión, R04 y R06, no tienen un outcome propio.

:::TABLA t02 | Validación bloqueante de la cadena Output-Outcome-Impact
| Condición | Resultado | Evidencia |
| --- | --- | --- |
| Cada output tiene al menos un outcome | PARCIAL | R01, R03 y P01 alimentan E01 porque el uso exige datos disponibles. R02, R05, P02 y P03 alimentan E02 porque la corrección reduce falsas alarmas. P04 alimenta E01 y E03. R04 y R06 son outputs de gestión sin outcome propio. |
| Cada outcome se conecta con al menos un impact | CUMPLE | E01 y E02 conducen a S01 (activación del protocolo). E03 conduce a S02 (continuidad de la red bajo custodia). |
| Ningún output se clasifica como impact | CUMPLE | Los 10 indicadores R y P tienen taxonomía Output; los 5 indicadores E y S tienen Outcome e Impact. |
| Los impacts son transformaciones medibles | CUMPLE | S01 y S02 se miden a 12 meses del cierre con evaluación externa; ninguno es una actividad. |
:::NOTA *Nota.* Elaboración propia con maestro/indicadores.py. Las asociaciones outcome-output son PROPUESTO. El estado PARCIAL no bloquea el avance porque R04 y R06 son outputs de gestión por diseño.

Las metas de los indicadores siguen una regla de proporcionalidad. Los indicadores R se fijan en 100 % porque dependen de la ejecución propia. Los indicadores P se fijan en cantidades que el presupuesto y el cronograma sostienen, como lo demuestra la {T:t05}. Los indicadores E se fijan por debajo del 100 %, porque dependen de la decisión de terceros. Son 75 % de uso de los comités y 30 % de reducción relativa de falsas alarmas. Los indicadores S se fijan en 80 % y 70 %, porque dependen además de la custodia posterior.

Esa gradación evita una promesa común en los proyectos de ciencia, tecnología e innovación. Consiste en comprometer con la misma certeza lo que se controla y lo que no. Cuanto más lejos del control del ejecutor está el indicador, menor es la meta y mayor es la exigencia de evidencia independiente. Los indicadores E y S se verifican con evaluación externa y con el registro de decisiones de los comités. No se verifican con el reporte del propio equipo.

## F7.1 Estructura jerárquica PERS articulada con el SGR

Los cuatro niveles del sistema corresponden a niveles del marco lógico y a horizontes de medición distintos. La {T:t03} los presenta con su cantidad y su criterio de viabilidad ante el SGR. El nivel R verifica la ejecución presupuestal y de actividades. El nivel P exige productos verificables y tipificados según el modelo de medición de grupos (MMG 2021). El nivel E exige evidencia de adopción. El nivel S exige evidencia de continuidad y articulación territorial.

:::TABLA t03 | Estructura jerárquica PERS
| Nivel PERS | Marco lógico | Taxonomía MinCiencias | Cadena de valor | Horizonte | Cantidad | Viabilidad SGR |
| --- | --- | --- | --- | --- | --- | --- |
| R, proceso | Actividades | Outputs | Insumos a actividades | Corto (mensual) | 6 | Verificación de ejecución presupuestal y de actividades programadas |
| P, producto | Componentes | Outputs tipificados MMG 2021 | Actividades a productos | Mediano (trimestral) | 4 | Productos verificables en CvLAC y GrupLAC, registros de propiedad intelectual y certificaciones |
| E, efecto | Propósito | Outcomes | Productos a efectos | Mediano (semestral) | 3 | Evidencia de adopción, uso o cambio de comportamiento |
| S, sostenibilidad | Fin | Impact | Efectos a impactos | Largo (anual o posterior) | 2 | Continuidad de la red y activación del protocolo, articuladas con el PDD [DATO_USUARIO: indicadores del PDD] |
| Total |  |  |  |  | 15 |  |
:::NOTA *Nota.* Elaboración propia con la especificación del metaprompt y maestro/indicadores.py.

### F7.1.1 Articulación con los criterios de viabilidad del SGR

Los términos de referencia no se aportaron. Por eso los pesos de los criterios de evaluación son los rangos por defecto del metaprompt (SUPUESTO). La {T:t04} vincula cada criterio con los indicadores que lo sustentan y con la evidencia que exige. Si los términos de referencia fijan otros pesos, el vínculo se conserva y solo cambia el peso.

:::TABLA t04 | Articulación de los indicadores PERS con los criterios de viabilidad del SGR
| Criterio SGR | Indicadores PERS vinculados | Evidencia requerida | Peso por defecto |
| --- | --- | --- | --- |
| Pertinencia y articulación territorial | PERS-S01 y PERS-S02 | Artículo del PDD y código de demanda territorial [DATO_USUARIO: artículos y códigos] | 20 a 25 % |
| Fortalecimiento de la CTeI regional | PERS-P01 a PERS-P04 | Productos tipificados MMG 2021 y nivel alcanzado de la escalera de apropiación social | 25 a 27 % |
| Calidad técnica | PERS-R01 a PERS-R06 | Metodología validada e indicadores con línea base | 20 a 25 % |
| Impacto esperado | PERS-E01 a PERS-E03, PERS-S01 y PERS-S02 | Cadena causal Output-Outcome-Impact verificable | 15 a 20 % |
| Viabilidad presupuestal | PERS-R con cruce al presupuesto | Cada meta P validada contra rubro y plazo | 10 a 15 % |
:::NOTA *Nota.* Elaboración propia con la especificación del metaprompt. Los pesos son rangos por defecto, SUPUESTO por falta de términos de referencia.

### F7.1.2 Validación entre meta, recurso y cronograma

Cada indicador de producto debe validarse contra el rubro que lo financia y contra el plazo del cronograma. La {T:t05} cruza las cuatro metas P con los rubros asociados, el monto asignado, la actividad y el mes. Los montos se calculan con los datos maestros. La regla del metaprompt detiene la generación del presupuesto si alguna coherencia falla. Ninguna falla en esta formulación: tres cumplen y una cumple con observación.

:::TABLA t05 | Validación cruzada de meta, recurso y cronograma para los indicadores de producto
| Indicador | Meta final | Rubros asociados | Monto (millones de COP) | Actividades | Plazo | Coherencia |
| --- | --- | --- | --- | --- | --- | --- |
| PERS-P01: Red de 100 nodos y 10 gateways operativa | 100 / 10 al mes 24 | E01, E04, E05, E06, M03 y S05 | 1.135,0 M | A1.2, A2.3 y A2.4 | Mes 19 | CUMPLE: la compra por tramos y la instalación coinciden con los hitos H4 y H6 |
| PERS-P02: Software de corrección y gemelo digital registrado | 1 registro vigente | O03 y S02 | 60,0 M | A2.2 y A1.4 | Mes 12 | CUMPLE con observación: el esfuerzo de desarrollo se financia en personal; el rubro propio cubre solo el registro |
| PERS-P03: Artículos científicos en revistas Q1 o Q2 | 2 sometidos y al menos 1 aceptado al mes 24 | O01 | 25,0 M | A1.4 y A1.6 | Mes 23 | CUMPLE: el primer artículo usa el piloto de C1; el segundo exige la verificación final y puede no aceptarse al mes 24 |
| PERS-P04: Actividades de apropiación social documentadas | 29 actividades (20 talleres y 9 jornadas) | M05, V05 y O02 | 132,0 M | A3.1 y A3.2 | Mes 17 | CUMPLE: 20 kits, 20 eventos y 9 jornadas coinciden con las 29 actividades |
:::NOTA *Nota.* Elaboración propia con maestro.py (BUDGET, ACT) y c12_datos.py. Los montos suman las líneas de rubro asociadas; la asociación indicador-rubro es PROPUESTO. M: millones de COP.

## F7.2 Fichas técnicas de los indicadores

Las fichas de los 15 indicadores siguen los 12 campos del metaprompt. Para no duplicar el capítulo 12, este paso presenta los campos en dos tablas. La {T:t06} reúne identificación, fórmula, línea base, metas y periodicidad. La {T:t07} reúne fuente de datos, supuestos, riesgo de incumplimiento y verificación. Los campos de limitaciones, desagregación y metadata, junto con la justificación de las metas, figuran en las fichas completas del capítulo 12.

:::TABLA t06 | Fichas de los indicadores PERS: identificación, fórmula, línea base, metas y periodicidad
| Código | Nombre | OE | Fórmula | Unidad | Línea base | Metas | Frecuencia | Responsable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PERS-R01 | Cumplimiento del despliegue por tramo | OE2 | Nodos instalados y operativos ÷ nodos programados × 100 | % | 0 (CALCULADO) | 30 nodos (100 % del tramo 1); final: 100 nodos y 10 gateways (100 %) | Mensual | Ingenieros IoT y de campo |
| PERS-R02 | Ciclos de calibración ejecutados | OE1 | Número de ciclos completos de entrenamiento, validación y despliegue del modelo de corrección | ciclos | 0 (CALCULADO) | 2 ciclos (tramo 1); final: 6 ciclos (2 por tramo) | Mensual | Científico de datos |
| PERS-R03 | Disponibilidad de la plataforma en la nube | OE2 | Horas de servicio ÷ horas del mes × 100 | % | VACIO (VACIO) | ≥ 99,0 %; final: ≥ 99,0 % | Mensual | Ingenieros de software y nube |
| PERS-R04 | Desviación de la ejecución presupuestal | OE3 | (Ejecución acumulada − programación acumulada) ÷ programación acumulada × 100 | % | 0 (CALCULADO) | \|desviación\| ≤ 10 %; final: \|desviación\| ≤ 5 % al cierre | Mensual | Gerencia de proyecto |
| PERS-R05 | Horas-nodo de colocalización válidas | OE1 | Suma de horas con dato pareado entre nodo y referencia que cumplen el control de calidad | horas-nodo | 0 (CALCULADO) | ≥ 60.000 horas-nodo en el tramo 1; final: ≥ 60.000 y 4 rotaciones por departamento | Mensual | Especialista en metrología |
| PERS-R06 | Cumplimiento de informes de seguimiento | OE3 | Informes técnicos y financieros entregados a tiempo ÷ informes exigidos × 100 | % | 0 (CALCULADO) | 100 %; final: 100 % | Mensual | Gerencia de proyecto |
| PERS-P01 | Red de 100 nodos y 10 gateways operativa | OE2 | Nodos operativos con disponibilidad mensual ≥ 90 % y gateways con enlace principal o alterno activo | nodos / gateways | 0 / 0 (CALCULADO) | 30 / 3 al mes 12; final: 100 / 10 al mes 24 | Trimestral | Ingenieros IoT y de campo |
| PERS-P02 | Software de corrección y gemelo digital registrado | OE1 | Registros de software ante la DNDA (modelo de corrección, firmware y gemelo digital) | registros | 0 (CALCULADO) | 0; final: 1 registro vigente | Trimestral | Profesional de convenios y custodia |
| PERS-P03 | Artículos científicos en revistas Q1 o Q2 | OE1 | Artículos sometidos y aceptados con filiación del proyecto | artículos | 0 (CALCULADO) | 0; final: 2 sometidos y al menos 1 aceptado al mes 24 | Trimestral | Investigador principal |
| PERS-P04 | Actividades de apropiación social documentadas | OE3 | Talleres de co-diseño (nivel 3) más jornadas públicas (niveles 1 y 2) con acta y lista de asistencia | actividades | 0 (CALCULADO) | 10 actividades; final: 29 actividades (20 talleres y 9 jornadas) | Trimestral | Coordinación de apropiación social |
| PERS-E01 | Uso institucional del tablero y del protocolo | OE3 | Comités focalizados con al menos una decisión documentada por trimestre basada en el tablero ÷ comités focalizados × 100 | % | VACIO (VACIO) | ≥ 50 % (piloto); final: ≥ 75 % al mes 24 | Trimestral | Coordinación de apropiación social |
| PERS-E02 | Reducción relativa de falsas alarmas | OE3 | 1 − (tasa de falsas alarmas del periodo ÷ tasa de línea base medida en el tramo 1) | % | Se mide en el tramo 1 (VACIO) | Línea base medida; final: ≥ 30 % de reducción relativa | Trimestral | Profesional en calidad del aire |
| PERS-E03 | Capacidad instalada en custodios | OE3 | Personas con evaluación práctica aprobada en mantenimiento, lectura y operación ÷ personas formadas × 100, y número absoluto | personas | 0 (CALCULADO) | 20 personas; final: ≥ 60 personas certificadas | Semestral | Profesional de convenios y custodia |
| PERS-S01 | Activación del protocolo ante superación de umbral | OE3 | Eventos de superación de umbral con medida de protección activada y registrada ÷ eventos de superación confirmados × 100 | % | VACIO (VACIO) | No aplica (medición posproyecto); final: ≥ 80 % a los 12 meses posteriores al cierre | Anual, 6 a 12 meses tras el cierre | Custodios y secretarías de gestión del riesgo |
| PERS-S02 | Continuidad de la red bajo custodia | OE3 | Nodos operados por custodios con partida y competencia a los 12 meses del cierre ÷ nodos entregados × 100 | % | VACIO (VACIO) | No aplica; final: ≥ 70 % a los 12 meses posteriores al cierre | Anual, 12 meses tras el cierre | Profesional de convenios y custodia |
:::NOTA *Nota.* Elaboración propia con maestro/indicadores.py. Línea base VACIO se mide en el tramo 1. Naturaleza de las metas: PROPUESTO; de las líneas base: CALCULADO o VACIO según la celda.

:::TABLA t07 | Fichas de los indicadores PERS: fuente, supuestos, riesgo y verificación
| Código | Fuente de datos | Supuesto | Riesgo de incumplimiento | Medio de verificación | Tipo MMG |
| --- | --- | --- | --- | --- | --- |
| PERS-R01 | Inventario de la plataforma y actas de instalación | Acceso vial a los sitios en ventanas secas | Medio | Acta de instalación con coordenadas y número de serie | — |
| PERS-R02 | Registro de versiones del modelo | Datos de colocalización con completitud mayor o igual a 75 % | Medio | Informe de validación firmado por la metrología | — |
| PERS-R03 | Monitor de servicio de la plataforma | Servicio contratado con acuerdo de nivel de servicio | Bajo | Reporte mensual del proveedor de nube | — |
| PERS-R04 | Sistema de seguimiento presupuestal | Desembolsos oportunos por tramo | Medio | Informe financiero conciliado con el técnico | — |
| PERS-R05 | Base de datos de colocalización | Tres referencias operando con completitud mayor o igual a 90 % | Medio | Bitácora de la referencia y tablero de calidad de datos | — |
| PERS-R06 | Sistema de seguimiento del financiador | Calendario de informes definido por los términos de referencia (VACIO) | Bajo | Radicados de entrega | — |
| PERS-P01 | Plataforma e inventario | Compuertas C1 y C2 aprobadas | Medio | Inventario con huella de configuración y registro fotográfico | PROT-FUNC |
| PERS-P02 | Certificado de la DNDA | Acuerdo de titularidad firmado entre las partes | Bajo | Certificado de registro | SW-REG |
| PERS-P03 | Plataformas editoriales y CvLAC | Tiempos editoriales compatibles con el cierre | Medio | Carta de aceptación y soporte de envío | ART-A1 / ART-A2 |
| PERS-P04 | Actas y listas de asistencia | Participación comunitaria con consentimiento informado | Medio | Actas firmadas por representantes comunitarios | ASC-PART / ASC-COM / ASC-CIRC |
| PERS-E01 | Actas de los comités y registro de decisiones del tablero | Comités constituidos y con sesiones periódicas | Alto | Acta del comité con referencia a la lectura del tablero | — |
| PERS-E02 | Registro de alertas y verificación con referencia | Umbrales validados localmente en el co-diseño | Alto | Cruce entre alertas emitidas y mediciones de referencia | — |
| PERS-E03 | Registros de formación y evaluación práctica | Custodios designan personal con permanencia | Alto | Certificados y actas de evaluación práctica | FORM (capacitación) |
| PERS-S01 | Registro de eventos y de medidas | Custodia operativa y datos disponibles | Alto | Evaluación externa posproyecto | — |
| PERS-S02 | Convenios, presupuestos y plataforma | Cláusula de apertura y financiación de custodios | Alto | Evaluación externa posproyecto | — |
:::NOTA *Nota.* Elaboración propia con maestro/indicadores.py. El riesgo de incumplimiento es un juicio PROPUESTO. El tipo MMG 2021 se confirma con la convocatoria vigente [DATO_USUARIO: tipología MMG].

La {T:t08} registra la decisión sobre la asignación de niveles (nodo ND-16).

:::TABLA t08 | Registro de decisión GENESIS: ND-16 Asignación output, outcome e impact
| Campo | Contenido |
| --- | --- |
| NODO | ND-16 Asignación output, outcome e impact |
| CLASE | MAYOR. Determina qué se promete como resultado y qué como impacto. |
| DECISION | Clasificar los 10 indicadores R y P como outputs, los 3 E como outcomes y los 2 S como impacts, sin promesa de efecto en salud. |
| DECIDE | Equipo formulador [DATO_USUARIO: responsable de la decisión]. |
| EXCLUYE | Presentar outputs como impactos. Prometer reducción de morbilidad sin línea base ni diseño causal. |
| NODOS_BLANCOS | 3: el diseño de cada indicador usa fórmula, unidad y fuente; las metas de desempeño usan umbrales de EPA (2021); el presupuesto respalda cada meta P. |
| NODOS_GRISES | 3: líneas base VACIO de E y S; capacidad de los custodios; articulación con el PDD. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | PR-06 (patrón emergente): medir uso y continuidad, no efectos que el diseño no identifica. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. Los impacts dependen de la custodia por entidades externas. |
| ESCENA_SIMULABLE | Un evaluador pide el impacto del proyecto. El documento responde con S01 y S02 medidos a 12 meses del cierre. |
| EVIDENCIA_JH_A | Tabla F7.2: validación bloqueante. |
| EVIDENCIA_JH_B | Tabla F7.5: cruce de metas P con presupuesto y cronograma. |
| CERCA_CONCEPTUAL | Un indicador de uso no prueba un cambio en la salud de la población. |
| ESTATUTO_CAUSAL | HIE. |
| VEREDICTO | Asignación adoptada; R04 y R06 se conservan como outputs de gestión. |
| RAZON_DEL_DESCARTE | Se descarta un indicador de morbilidad por falta de línea base y de diseño causal. |
| RESULTADO | CIERRA con vacíos declarados (líneas base de E y S). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS.

El Paso 7 crea valor al convertir cada promesa del proyecto en un indicador con fórmula, fuente, responsable y plazo. También separa lo que el proyecto entrega de lo que otros deben sostener. El Paso 8 desarrolla los 21 capítulos del documento con estas definiciones.
