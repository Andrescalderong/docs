# Informe de revisión de Problematica E3-P00

Caso: SGR_CONV56_AIRE. Fecha de corte: 13 de octubre de 2026. Naturaleza: revisión técnica ejecutada por una instancia analítica (modelo de lenguaje) con cálculo reproducible. No es un dictamen de un panel independiente.

## 1. Resumen

Se leyó completo el expediente Problematica_E3-P00. Incluye los pasos E3-P00 a E3-P21, los Pasos 1, 3, 4, 5 y 6, los capítulos 8 a 10 y 14, y la bibliografía. Se contrastó con el informe_FINAL de vigilancia tecnológica y con la plantilla Vester_MICMAC_Plantilla_15_vacia.xlsx. Se registraron 36 hallazgos: 19 críticos, 15 mayores y 2 menores.

El expediente no cumple las compuertas de superioridad GS-01 a GS-05 ni GS-07 del metaprompt. GS-06 y GS-08 quedan NO_EJECUTADO (sección 3). Su aritmética de índices es correcta. Su cadena causal y estructural no es reproducible, omite la sección 4.3 y la sección 4.4-MDR, y la sostenibilidad descansa en un receptor sin compromiso.

Esta corrida ejecutó las secciones que el expediente omite o calcula de manera no reproducible: 4.3, 4.4, 4.4-MDR y 4.5. Los resultados se entregan como borrador con vacíos. Ninguna ficha de 4.4 tiene ratificación independiente. Los términos de referencia no se aportaron.

## 2. Alcance, método y límites

| Elemento | Detalle |
| --- | --- |
| Documentos leídos | Problematica_E3-P00.docx (completo), informe_FINAL.docx (completo), plantilla XLSX (completa) |
| Cálculo | Motor paritario del metaprompt (huella verificada), cálculo independiente con aritmética exacta y recálculo de la plantilla con otro programa |
| Contraste | Cada cifra material del expediente se contrastó con su fuente interna y con el informe |
| Límites | No se leyeron fuentes primarias. No se aportaron términos de referencia, anexos ni planes de desarrollo. La verificación de normas y de vigencia queda como CANDIDATO_A_VERIFICAR |
| Severidad (PROPUESTA) | CRITICO: invalida una cifra, decisión o regla bloqueante. MAYOR: reduce verificabilidad o coherencia sin invalidar por sí solo. MENOR: formal o de estilo |

## 3. Resultado por compuerta de superioridad

| Compuerta | Estado | Fundamento |
| --- | --- | --- |
| GS-01 Errores bloqueantes igual a cero | NO_CUMPLE | Diecinueve hallazgos críticos |
| GS-02 Elegibilidad verificable de 100 % | NO_CUMPLE | Gate 0: cuatro elementos NO_CUMPLE y dos NO_EJECUTADO (documento 01) |
| GS-03 Trazabilidad de afirmaciones críticas de 100 % | NO_CUMPLE | HR-04, HR-15 y HR-16 |
| GS-04 Consistencia de cifras cardinales de 100 % | NO_CUMPLE | HR-05, HR-14 y HR-27 |
| GS-05 Consistencia entre actividad, producto, indicador, presupuesto y cronograma de 100 % | NO_CUMPLE | HR-10, HR-11 y HR-13 |
| GS-06 Citas inexistentes o no verificables igual a cero | NO_EJECUTADO | No se leyeron fuentes primarias; HR-16 documenta atribuciones erróneas |
| GS-07 Residuos conversacionales igual a cero | NO_CUMPLE | HR-19 |
| GS-08 Cambios de alcance sin autorización igual a cero | NO_EJECUTADO | Sin términos de referencia ni autorización documentada |

## 4. Resumen de hallazgos

| ID | Severidad | Ubicación | Hallazgo | Estado en esta corrida |
| --- | --- | --- | --- | --- |
| HR-01 | CRITICO | Paso 4 (encabezados 4.2, 4.4.2 a 4.4.13, 4.5) | Secuencia obligatoria incompleta | Corregido en esta corrida (secciones nuevas) |
| HR-02 | CRITICO | E3-P04 §12 (ledger de adjudicación) | 188 ceros adjudicados en bloque | Corregido como propuesta (fichas sin ratificación) |
| HR-03 | CRITICO | E3-P04 §12 y E3-P05 | El grafo acíclico es un artefacto de la codificación | Corregido en 4.4 (escenarios S0 a S4) |
| HR-04 | CRITICO | E3-P05, E3-P09, E3-P19 | Afirmaciones matemáticas desproporcionadas | Pendiente en el documento original |
| HR-05 | CRITICO | Paso 4, 4.4.4 a 4.4.12 (escenario S1) | Cifras de Vester y MICMAC no reproducibles | Corregido en 4.4 |
| HR-06 | CRITICO | E3-P06 y E3-P07 | La contradicción raíz CTR-01 no está soportada por su matriz | Corregido como hipótesis en 4.4 y 4.5 |
| HR-07 | CRITICO | E3-P11 y E3-P12 | Índice de cierre lógico circular | Corregido en 4.4-MDR |
| HR-08 | CRITICO | E3-P14 y Paso 6 (módulo MCDA) | Decisión multicriterio sin insumos | Corregido en 4.4-MDR |
| HR-09 | CRITICO | E3-P17 (§10, §12, §13), Tabla 14.2 y CLM-06 | Se supone un receptor público sin compromiso | Corregido como diseño propuesto con vacíos |
| HR-10 | CRITICO | Capítulo 8 (Tablas 8.1 a 8.8) | El presupuesto detallado no concilia con el tope | Pendiente (capítulo posterior) |
| HR-11 | CRITICO | Capítulos 9 y 10, E3-P19 y Tabla 5.3 | Cronograma y ruta crítica inconsistentes | Pendiente (capítulo posterior) |
| HR-12 | CRITICO | Paso 4 (4.6), Capítulo 8 (Tabla 8.3) y E3-P15 | Contradicción de arquitectura | Registrado como vacío en 4.4-MDR |
| HR-13 | CRITICO | E3-P09 (OP-03), E3-P15, Paso 1 y Paso 6 | Cuatro versiones del lugar donde se calibra | Registrado como vacío en 4.4-MDR |
| HR-14 | CRITICO | E3-P19 (K02), Paso 1, Paso 5 y Tabla 5.1 | Metas y línea base del error contradictorias | Registrado como vacío en 4.4-MDR |
| HR-15 | CRITICO | Tabla 5.0, E3-P16, E3-P20 y cierre del Paso 3 | Verificación afirmada sin fuente | Pendiente en el documento original |
| HR-16 | CRITICO | Paso 3 (Tabla 3.1), Capítulo 8 y 4.4 | El corpus y las cifras difieren del informe_FINAL | Parcialmente corregido en 4.3 y 4.4 (fichas con localizador) |
| HR-17 | CRITICO | Registros RDG ND-05, ND-10, ND-11, ND-13, ND-14, ND-15 y ND-16 | Estatutos causales sin estimando | Corregido en 4.3 |
| HR-18 | CRITICO | Registro de decisiones (RDG) de todo el documento | Registro de nodos incompleto y con contradicciones | Corregido para ND-01 a ND-09 en esta corrida |
| HR-19 | CRITICO | Todo el documento | Residuos de interfaz de conversación | Pendiente en el documento original |
| HR-20 | MAYOR | E3-P02 | Solapamiento sin evaluar | Corregido en 4.4 |
| HR-21 | MAYOR | E3-P02 a E3-P21 | Secciones finales ausentes | Pendiente en el documento original |
| HR-22 | MAYOR | E3-P03, E3-P05 y E3-P06 | Hipótesis previa refutada sin reporte y parámetro distinto | Corregido en 4.4 |
| HR-23 | MAYOR | E3-P08, E3-P09 y E3-P18 | Restricciones de solución tratadas como requisitos y cifras sin fuente | Registrado en 4.4-MDR (criterios y sesgos) |
| HR-24 | MAYOR | E3-P12 y E3-P13 | Índices de efectos inducidos y de riesgo residual con premisas débiles | Pendiente en el documento original |
| HR-25 | MAYOR | Capítulo 10 | Riesgos con identificadores duplicados y vacíos | Pendiente (capítulo posterior) |
| HR-26 | MAYOR | Capítulo 14 (Tabla 14.2) | Equilibrio social presentado como sostenibilidad financiera | Registrado en 4.4-MDR.10 |
| HR-27 | MAYOR | Paso 3 (texto, PRISMA y Tabla 3.1) | Estadísticas bibliométricas inconsistentes | Pendiente en el documento original |
| HR-28 | MAYOR | Paso 1 | Datos de contexto no verificables | Registrado como vacío |
| HR-29 | MAYOR | Paso 4 (4.5 a 4.8) y Paso 5 | Priorización y ecuación sin derivación de la matriz | Corregido en 4.5 |
| HR-30 | MAYOR | E3-P04 frente al Paso 4 | Dos matrices vigentes sin conciliar | Corregido en 4.4 |
| HR-31 | MAYOR | Paso 6, módulo de metaheurística | Código sin optimización trazable | Pendiente en el documento original |
| HR-32 | MAYOR | E3-P18 | Numeración ambigua | Pendiente en el documento original |
| HR-33 | MAYOR | E3-P21 (libro de 19 hojas) | Comprobaciones triviales y salidas prejuzgadas | Pendiente en el documento original |
| HR-34 | MAYOR | Insumo: Vester_MICMAC_Plantilla_15_vacia.xlsx | La plantilla no está vacía | Corregido en 4.4 (libros S0, S1 y S2) |
| HR-35 | MENOR | Paso 4, 4.4.2 a 4.4.12 | Lenguaje narrativo y enfático | Corregido en las secciones nuevas |
| HR-36 | MENOR | E3-P19 y Paso 5 | Datos fijos y magnitudes inconsistentes | Pendiente en el documento original |

## 5. Hallazgos con evidencia, corrección y prueba de cierre

Cada registro conserva la evidencia localizable, la corrección propuesta y la prueba que cerraría el hallazgo.

### HR-01 · CRITICO · Secuencia obligatoria incompleta

- **Ubicación:** Paso 4 (encabezados 4.2, 4.4.2 a 4.4.13, 4.5)
- **Evidencia:** El texto salta de 4.2 a 4.4.2. Faltan la sección 4.3, las piezas 4.4.1 y 4.4.14 y la sección 4.4-MDR (de 4.4.13 pasa a 4.5). La pieza 4.4.4 contiene 10 de 105 fichas.
- **Corrección:** Ejecutar 4.3, 4.4 con las catorce piezas y 4.4-MDR antes de 4.5.
- **Prueba de cierre:** El controlador de alcance devuelve ALCANCE_VERIFICADO para la cadena 4.3, 4.4, 4.4-MDR y 4.5.
- **Estado en esta corrida:** Corregido en esta corrida (secciones nuevas)

### HR-02 · CRITICO · 188 ceros adjudicados en bloque

- **Ubicación:** E3-P04 §12 (ledger de adjudicación)
- **Evidencia:** El ledger asigna 22 aristas positivas y adjudica 188 ceros con una «Regla Cero». El contrato V2.1 exige adjudicación individual (zero_requires_individual_adjudication=true).
- **Corrección:** Reemplazar los ceros en bloque por 105 fichas bidireccionales con mecanismo o razón del cero.
- **Prueba de cierre:** El motor acepta 105 fichas con 210 direcciones justificadas y 0 errores de ficha.
- **Estado en esta corrida:** Corregido como propuesta (fichas sin ratificación)

### HR-03 · CRITICO · El grafo acíclico es un artefacto de la codificación

- **Ubicación:** E3-P04 §12 y E3-P05
- **Evidencia:** Se codificaron como cero relaciones estructurales: V01→V11 y V02→V11 (el AQHI se calcula con PM), V04→V06, V09→V13 y V09→V14, V15→V07, V15→V09, V15→V10 y V12→V07. La extinción de caminos en A⁷ describe esas 22 aristas.
- **Corrección:** Calcular con la matriz S2 y conservar S0 como histórico condicionado.
- **Prueba de cierre:** S0 se extingue en A⁷ y S2 conserva 144 ciclos simples de hasta siete aristas.
- **Estado en esta corrida:** Corregido en 4.4 (escenarios S0 a S4)

### HR-04 · CRITICO · Afirmaciones matemáticas desproporcionadas

- **Ubicación:** E3-P05, E3-P09, E3-P19
- **Evidencia:** E3-P05 afirma que la extinción «demuestra matemáticamente» un grafo acíclico y «la linealidad termodinámica». E3-P09 afirma «garantiza matemáticamente». E3-P19 afirma «garantizando el éxito».
- **Corrección:** Reformular con el estatuto HIE y el calificador que autorizan la evidencia.
- **Prueba de cierre:** Búsqueda de «demuestra matemáticamente», «garantiza» y «garantizando» sin resultados en los entregables.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-05 · CRITICO · Cifras de Vester y MICMAC no reproducibles

- **Ubicación:** Paso 4, 4.4.4 a 4.4.12 (escenario S1)
- **Evidencia:** Con la misma matriz S1, el motor oficial y un cálculo independiente concuerdan. Dan potencias de 280; 1.205; 4.855; 19.154; 80.500; 349.230; 1.484.060; 6.071.508 y 24.573.040 (A² a A¹⁰). El documento da 129; 258; 561; 1.257; 2.894; 6.574; 15.195; 35.539 y 82.529. Los rangos indirectos de A¹⁰ divergen: V05 es 1 (documento: 12), V07 es 3 (documento: 1) y V15 es 6 (documento: 2). La ventana de tres rangos iguales no se cumple en k = 8, 9 y 10.
- **Corrección:** Sustituir las tablas por la salida del motor oficial y corregir la narrativa.
- **Prueba de cierre:** Motor oficial, cálculo independiente y plantilla XLSX recalculada coinciden de A¹ a A⁶.
- **Estado en esta corrida:** Corregido en 4.4

### HR-06 · CRITICO · La contradicción raíz CTR-01 no está soportada por su matriz

- **Ubicación:** E3-P06 y E3-P07
- **Evidencia:** Las tres contradicciones técnicas involucran pares con arista 0 en el ledger: V07→V08, V10→V07 y V13→V12. La contradicción raíz se declara con relaciones que el propio ledger niega.
- **Corrección:** Reformular CTR-01 como hipótesis y registrar qué ficha la sostendría.
- **Prueba de cierre:** 4.4.14 muestra V08 en el último lugar de influencia indirecta de S2 y V08→V06 con dominio de 0 a 2.
- **Estado en esta corrida:** Corregido como hipótesis en 4.4 y 4.5

### HR-07 · CRITICO · Índice de cierre lógico circular

- **Ubicación:** E3-P11 y E3-P12
- **Evidencia:** Los criterios C2 a C4 derivan de los polos de CTR-01 y ALT-03 se construyó con operadores que resuelven CTR-01. Resulta 1,00 por construcción. La regla propia «ante la duda, 0» no se aplica a ALT-03, que carece de piloto. D12 descarta de forma definitiva ALT-00 a ALT-02.
- **Corrección:** Registrar criterios independientes antes de evaluar y conservar las alternativas.
- **Prueba de cierre:** 4.4-MDR.7 registra seis criterios con versión 1.0 antes de la matriz de compensaciones.
- **Estado en esta corrida:** Corregido en 4.4-MDR

### HR-08 · CRITICO · Decisión multicriterio sin insumos

- **Ubicación:** E3-P14 y Paso 6 (módulo MCDA)
- **Evidencia:** Los pesos 0,40; 0,30; 0,15 y 0,15 son SUPUESTO y las utilidades carecen de evidencia. Los escenarios S3 y S4 no se renormalizan de forma proporcional. D15 usa el estado «DECISION_ADJUDICADA condicionada», inválido en el contrato V2.1. ND-13 cita «pesos exigidos en TdR» y «Panel Evaluador (Exploratorio)» a la vez. Los presupuestos de las alternativas no son comparables.
- **Corrección:** Conservar la tabla como dato con su estado y entregar compensaciones sin agregar.
- **Prueba de cierre:** La aritmética se recalculó y es correcta (0,460; 0,325; 0,535; 0,795). 4.4-MDR.7 no la usa como ganador.
- **Estado en esta corrida:** Corregido en 4.4-MDR

### HR-09 · CRITICO · Se supone un receptor público sin compromiso

- **Ubicación:** E3-P17 (§10, §12, §13), Tabla 14.2 y CLM-06
- **Evidencia:** E3-P17 afirma que, si las alcaldías no asumen la responsabilidad, la red termina en el mes 25. Ningún compromiso está firmado. La Tabla 14.2 asigna 120 millones de COP anuales al personal en especie de la institución ejecutora y la UNGRD. E3-P17 afirma que esa institución carece de recursos permanentes.
- **Corrección:** Diseñar con la premisa sin receptor único: custodia por tramos, portafolio y cláusula de apertura.
- **Prueba de cierre:** 4.4-MDR.10 calcula participación máxima 63,2 % y HHI 0,472 del portafolio declarado, y deja ICAR como NO_CALCULABLE.
- **Estado en esta corrida:** Corregido como diseño propuesto con vacíos

### HR-10 · CRITICO · El presupuesto detallado no concilia con el tope

- **Ubicación:** Capítulo 8 (Tablas 8.1 a 8.8)
- **Evidencia:** Los rubros detallados con cargo al SGR suman 4.448,7 millones (31,8 % de 14.000). Faltan 9.551,3 millones. La Tabla 8.8 (6.300; 3.500; 2.100; 1.400; 700) suma 14.000 pero no concilia con las tablas 8.2 a 8.7. La contrapartida de la institución ejecutora es 1.100 en 8.1 y 600 en 8.2. El APC aparece dos veces (2 × 12,5). No hay línea para diez gateways, paneles solares ni baterías. La reserva de contingencia de 585 millones no se presupuesta. El «Fondo de Mitigación Cambiaria» no figura en 8.4.
- **Corrección:** Reconciliar el Capítulo 8 con una sola estructura de costos por módulo y presupuestar los activos que el diseño exige.
- **Prueba de cierre:** La suma de rubros por tabla coincide con el tope y con la Tabla 8.8.
- **Estado en esta corrida:** Pendiente (capítulo posterior)

### HR-11 · CRITICO · Cronograma y ruta crítica inconsistentes

- **Ubicación:** Capítulos 9 y 10, E3-P19 y Tabla 5.3
- **Evidencia:** La ruta crítica suma 38 semanas (12 + 4 + 16 + 6) con holgura 0 en un proyecto de 104 semanas. Una ruta crítica debe igualar la duración. E3-P19 pone nodos en terreno el día 60 y tablero el día 90. El Capítulo 9 fija 12 semanas de importación, Hito 1 en el mes 6 y tablero entre los meses 12,5 y 18. Entrenar con datos sintéticos contradice la colocalización. El Hito 1 declara TRL 6 con criterio de «ping». La «Fase 0 de 12 meses» (D-03 del informe) no figura y R-FIN-01 ordena importar todos los nodos en la semana 2.
- **Corrección:** Reconstruir la red de actividades completa y alinear E3-P19, Capítulo 9 y Capítulo 10.
- **Prueba de cierre:** La ruta crítica calculada iguala la duración del proyecto y los hitos coinciden entre documentos.
- **Estado en esta corrida:** Pendiente (capítulo posterior)

### HR-12 · CRITICO · Contradicción de arquitectura

- **Ubicación:** Paso 4 (4.6), Capítulo 8 (Tabla 8.3) y E3-P15
- **Evidencia:** El problema declara el colapso de la infraestructura celular y eléctrica. ALT-03 transmite por enlace celular 4G con 100 tarjetas SIM y el nodo silencia su antena 4G. No se presupuesta enlace alterno, gateways, paneles ni baterías.
- **Corrección:** Diseñar el enlace alterno y la energía como parte del alcance o retirar la premisa de colapso.
- **Prueba de cierre:** El presupuesto contiene las líneas de enlace alterno y energía.
- **Estado en esta corrida:** Registrado como vacío en 4.4-MDR

### HR-13 · CRITICO · Cuatro versiones del lugar donde se calibra

- **Ubicación:** E3-P09 (OP-03), E3-P15, Paso 1 y Paso 6
- **Evidencia:** E3-P09 calibra en el chip del sensor. E3-P15 declara que M1 no procesa y que M2 corre el modelo. El Paso 1 asigna 10 % de gateways. El Paso 6 usa el microcontrolador de cada nodo. El silencio del nodo es 90 % en E3-P07, E3-P18 y el Paso 1, y 95 % en ND-12. La autonomía es 14 días, «años» y «tres años».
- **Corrección:** Fijar una definición en el diccionario y propagarla.
- **Prueba de cierre:** Una búsqueda del término de calibración devuelve una sola ubicación en los capítulos.
- **Estado en esta corrida:** Registrado como vacío en 4.4-MDR

### HR-14 · CRITICO · Metas y línea base del error contradictorias

- **Ubicación:** E3-P19 (K02), Paso 1, Paso 5 y Tabla 5.1
- **Evidencia:** La meta de V06 es menos de 30 % (K02), 15 % o menos (Paso 5) y menos de 15 % (Tabla 5.1). La línea base es NO_MEDIDO en K02, pero el Paso 1 afirma más de 45 % y el Paso 5 escribe «45 % (Estimado)».
- **Corrección:** Fijar la meta con los términos de referencia y medir la línea base con referencia.
- **Prueba de cierre:** Una sola meta y una línea base con método en todos los capítulos.
- **Estado en esta corrida:** Registrado como vacío en 4.4-MDR

### HR-15 · CRITICO · Verificación afirmada sin fuente

- **Ubicación:** Tabla 5.0, E3-P16, E3-P20 y cierre del Paso 3
- **Evidencia:** La Tabla 5.0 marca «8/8 verificado». Cita el PDD de Caldas (eje 2, artículo 22, línea base 12, meta 40), el PDD de Cundinamarca (68 %), el CONPES 4069 y la Misión de Sabios. Ninguna fuente se aportó. CLM-02 figura DOCUMENTADO y VERIFICADO sin referencia. CLM-01 usa actos administrativos no aportados. P16 declara «FIRMADO_TECNICAMENTE» sin firmante. El cierre del Paso 3 marca cumplimiento global mientras verificador_ntc.py figura PENDIENTE.
- **Corrección:** Rotular NO_VERIFICADO lo no consultado y registrar la fuente controlante con fecha.
- **Prueba de cierre:** Cada fila verificada cita documento, localizador y fecha de consulta.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-16 · CRITICO · El corpus y las cifras difieren del informe_FINAL

- **Ubicación:** Paso 3 (Tabla 3.1), Capítulo 8 y 4.4
- **Evidencia:** La Tabla 3.1 contiene 25 artículos, 14 patentes y 3 informes y el informe contiene 26, 15 y 1. Falta Hale et al. (2025) y de Moura et al. (2025) y se añaden Duvall y el Equipo Formulador. La correlación entre humedad y partículas es 0,73 en el informe y 0,48 en 3.15, 4.6 y ND-11. El valor de 35 minutos es el desfase temporal entre sensor y estación en Seúl y se usa como latencia de V08. Ali et al. (2022) es una patente sin datos de desempeño y se cita como evidencia de costos. El informe no contiene los términos TinyML ni Edge. Ningún documento de alertas del informe reporta detección, falsas alarmas ni anticipación. Las líneas base de V12 (20 %) y V13 (menos de 1 hora) carecen de respaldo. La cifra de 90,8 % corresponde a estaciones sin plan de calibración, no a falta de corrección por humedad. El valor 4.608 es el número de sensores de la red nacional propuesta, no una densidad del gemelo.
- **Corrección:** Reconciliar el corpus con el informe y ajustar cada línea base a su fuente.
- **Prueba de cierre:** La tabla de corpus coincide con las 42 entradas del informe y cada cifra cita su sección.
- **Estado en esta corrida:** Parcialmente corregido en 4.3 y 4.4 (fichas con localizador)

### HR-17 · CRITICO · Estatutos causales sin estimando

- **Ubicación:** Registros RDG ND-05, ND-10, ND-11, ND-13, ND-14, ND-15 y ND-16
- **Evidencia:** Se declaran IDC en ND-05, ND-10, ND-11, ND-13 y ND-16, y EST en ND-14 y ND-15, sin estimando ni datos. Un efecto estimado exige datos y diseño.
- **Corrección:** Declarar el estimando y rebajar a HIE lo que no tenga identificación.
- **Prueba de cierre:** 4.3.5 audita nueve nodos y deja ninguna afirmación en EST.
- **Estado en esta corrida:** Corregido en 4.3

### HR-18 · CRITICO · Registro de nodos incompleto y con contradicciones

- **Ubicación:** Registro de decisiones (RDG) de todo el documento
- **Evidencia:** El documento contiene solo ND-05, ND-06 y ND-10 a ND-16. Faltan ND-01 a ND-04, ND-07, ND-08 y ND-09. ND-10 declara «PR-05 ausente: Sí» y adopta PR-05 como patrón dominante. El código PR-06 se usa con nombres distintos en ND-12 a ND-15.
- **Corrección:** Emitir los nodos faltantes y corregir los antipatrones.
- **Prueba de cierre:** Los 18 nodos obligatorios existen en la cadena completa.
- **Estado en esta corrida:** Corregido para ND-01 a ND-09 en esta corrida

### HR-19 · CRITICO · Residuos de interfaz de conversación

- **Ubicación:** Todo el documento
- **Evidencia:** El texto conserva 53 marcadores «code Xml», 5 «hub Diagram», 1 «code Python» y 5 rótulos «BORRADOR INTERNO: REGENERAR COMO SVG» con espacios de no separación.
- **Corrección:** Eliminar los residuos y regenerar las figuras finales.
- **Prueba de cierre:** Búsqueda de los cuatro patrones sin resultados.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-20 · MAYOR · Solapamiento sin evaluar

- **Ubicación:** E3-P02
- **Evidencia:** Solo 5 de 105 pares tienen justificación. Los 100 restantes reciben ÚNICA en bloque. V01 (PM2,5) y V02 (PM10) se declaran únicas aunque PM2,5 está contenida en PM10 y el método define solapamiento como inclusión por definición.
- **Corrección:** Evaluar los 105 pares y redefinir V02 como fracción gruesa si procede.
- **Prueba de cierre:** REVISION_SOLAPAMIENTO.csv contiene 105 veredictos.
- **Estado en esta corrida:** Corregido en 4.4

### HR-21 · MAYOR · Secciones finales ausentes

- **Ubicación:** E3-P02 a E3-P21
- **Evidencia:** E3-P02 termina en la sección 13. E3-P03 a E3-P13, E3-P15, E3-P16 y E3-P18 a E3-P21 terminan en la 14. E3-P17 termina en la 15. Solo E3-P00, E3-P01 y E3-P14 tienen las secciones 1 a 18. D03 existe en E3-P16 pero no en E3-P02.
- **Corrección:** Completar las secciones 14 a 18 o declarar la plantilla reducida.
- **Prueba de cierre:** Cada paso contiene sus dieciocho secciones.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-22 · MAYOR · Hipótesis previa refutada sin reporte y parámetro distinto

- **Ubicación:** E3-P03, E3-P05 y E3-P06
- **Evidencia:** La clasificación previa pone V08 como palanca y el cálculo la deja AUTÓNOMA_RELATIVA; V09 y V10 quedan en FRONTERA. Ni E3-P05 ni E3-P06 reportan la refutación. E3-P05 usa kmax = 30 y el canon fija 10. Cinco de quince variables caen en FRONTERA y con la media cambian de clase.
- **Corrección:** Reportar la refutación y usar el parámetro del canon.
- **Prueba de cierre:** El reporte incluye la comparación de H_pre y el parámetro kmax = 10.
- **Estado en esta corrida:** Corregido en 4.4

### HR-23 · MAYOR · Restricciones de solución tratadas como requisitos y cifras sin fuente

- **Ubicación:** E3-P08, E3-P09 y E3-P18
- **Evidencia:** La función Z incluye «sensores comerciales de bajo costo», una restricción de solución marcada DOCUMENTADO (TdR) sin localizador. D10 impone OP-01 a OP-03 antes de evaluar alternativas. Las cifras 3 dólares, microsegundos, 20 % y 90/10 no tienen fuente. E3-P18 fija sin fuente cinco criterios de aceptación: reposo de 90 %, 14 días sin sol, 200 ms, AES-256 y TRL 4 a 7 u 8.
- **Corrección:** Rotular SUPUESTO las cifras y retirar la decisión previa.
- **Prueba de cierre:** Cada cifra tiene fuente o rótulo SUPUESTO.
- **Estado en esta corrida:** Registrado en 4.4-MDR (criterios y sesgos)

### HR-24 · MAYOR · Índices de efectos inducidos y de riesgo residual con premisas débiles

- **Ubicación:** E3-P12 y E3-P13
- **Evidencia:** El universo de contradicciones inducidas se construyó después de elegir ALT-03 y todos los pesos valen 1. IC-01 mapea la reparabilidad a V15, que es adopción institucional. E3-P13 escribe «desde el año 2» y la tabla «desde el mes 25». El control R01 presupone compromiso de las alcaldías. Los riesgos solo cubren IC-01 e IC-04. La aritmética es correcta.
- **Corrección:** Construir el universo antes de elegir y mapear cada contradicción a su variable.
- **Prueba de cierre:** Cada contradicción inducida tiene variable, riesgo y control.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-25 · MAYOR · Riesgos con identificadores duplicados y vacíos

- **Ubicación:** Capítulo 10
- **Evidencia:** R-ORG-01 designa el rechazo del tablero en 10.2 (probabilidad 3 por impacto 5 = 15) y el retrabajo de la interfaz en 10.3 (90 millones). Ningún riesgo cubre propiedad intelectual ni libertad de operación, pese a las diez solicitudes PCT con Colombia y tres plazos abiertos (informe, D-01). El valor monetario esperado de 585 millones (4,18 %) es aritméticamente correcto.
- **Corrección:** Asignar identificadores únicos e incluir el riesgo de libertad de operación.
- **Prueba de cierre:** Identificadores únicos y un riesgo de propiedad industrial con control.
- **Estado en esta corrida:** Pendiente (capítulo posterior)

### HR-26 · MAYOR · Equilibrio social presentado como sostenibilidad financiera

- **Ubicación:** Capítulo 14 (Tabla 14.2)
- **Evidencia:** El beneficio monetizado no recae en quien paga el gasto operativo. Corresponde al lucro cesante de las constructoras y a la morbilidad evitada del sistema de salud. Pagan el gasto operativo las secretarías de tecnologías de la información. El ahorro del año 1 iguala exactamente el costo del año 1 (190 millones) sin base. El personal en especie de la institución y la UNGRD contradice E3-P17.
- **Corrección:** Separar el flujo social del flujo del pagador y fundamentar cada ahorro.
- **Prueba de cierre:** La tabla identifica pagador y beneficiario de cada flujo con fuente.
- **Estado en esta corrida:** Registrado en 4.4-MDR.10

### HR-27 · MAYOR · Estadísticas bibliométricas inconsistentes

- **Ubicación:** Paso 3 (texto, PRISMA y Tabla 3.1)
- **Evidencia:** El texto y el diagrama PRISMA dan 26 artículos, 15 patentes y 1 informe y la Tabla 3.1 da 25, 14 y 3. Los años son 5, 9 y 17 en el texto y 6, 7 y 18 en la tabla. Además, 25 de 42 es 59,5 % y no 61,9 %. El 88,1 % en 2022 a 2026 resulta 83,3 % con 35 de 42. El cociente de Bradford no se sostiene en la zona 3 y 3 de 19 es 15,8 %. Los cuartiles de la tabla no coinciden con el texto. La afirmación «las tres revistas son de acceso abierto» es dudosa. La «integración metodológica inédita» carece de búsqueda exhaustiva.
- **Corrección:** Recalcular todas las cifras desde la tabla maestra y moderar la afirmación de novedad.
- **Prueba de cierre:** Cada cifra del texto coincide con la tabla y el recuento.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-28 · MAYOR · Datos de contexto no verificables

- **Ubicación:** Paso 1
- **Evidencia:** La fecha límite del 11 de noviembre de 2026 y los decretos 1414 y 1261 de 2026 no se pueden verificar. El sismo del 10 de agosto y el epicentro son SUPUESTO por instrucción del usuario. La cifra de error de 45 % cita F_REV_SISTEMATICA sin localizador.
- **Corrección:** Rotular DECLARADO y aportar las fuentes.
- **Prueba de cierre:** Cada dato cita documento y localizador.
- **Estado en esta corrida:** Registrado como vacío

### HR-29 · MAYOR · Priorización y ecuación sin derivación de la matriz

- **Ubicación:** Paso 4 (4.5 a 4.8) y Paso 5
- **Evidencia:** La tabla de causas priorizadas mezcla rango de influencia (V07 = 1,0) con rango de dependencia (V06 = 1,0). El rango de V07 coincide con S0 y los valores TA 6 y TP 15 de V06 con S1. La causa raíz de los cinco porqués («solo nube») no corresponde a ninguna de las quince variables. En la ecuación Y = f(X1, X2, X3), X2 (latencia) y X3 (disponibilidad) no actúan sobre V06 en S0. La sección 4.5 invoca la extinción de S0 sobre S1.
- **Corrección:** Derivar la priorización de una sola matriz y rotular hipótesis lo que no se derive.
- **Prueba de cierre:** 4.5 contrasta cada afirmación con S0, S1 y S2.
- **Estado en esta corrida:** Corregido en 4.5

### HR-30 · MAYOR · Dos matrices vigentes sin conciliar

- **Ubicación:** E3-P04 frente al Paso 4
- **Evidencia:** E3-P04 conserva S0 (22 aristas) y GENESIS usa S1 (32 aristas) como base de 4.5 a 4.8. No existe registro de las diferencias.
- **Corrección:** Declarar una matriz de trabajo y registrar las diferencias con las demás.
- **Prueba de cierre:** 4.4.13 compara S0, S1, S2, S3 y S4 y registra 26 aristas nuevas y 7 modificadas.
- **Estado en esta corrida:** Corregido en 4.4

### HR-31 · MAYOR · Código sin optimización trazable

- **Ubicación:** Paso 6, módulo de metaheurística
- **Evidencia:** El código es una función de aptitud lineal sin optimizador, semilla ni límites. Un objetivo lineal tiene óptimo en los bordes, no en 0,88; 0,12 y 0,05. Las unidades se mezclan. El resultado «Alfa» se afirma, no se calcula. La función incorpora la preferencia por cómputo en el borde. «90 % pasivos» no es variable de decisión.
- **Corrección:** Enumerar de forma exacta o ejecutar con semilla y límites declarados.
- **Prueba de cierre:** El resultado se reproduce con semilla y los límites constan.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-32 · MAYOR · Numeración ambigua

- **Ubicación:** E3-P18
- **Evidencia:** Los identificadores P01 a P23 de los artefactos colisionan con los pasos E3-P00 a E3-P21 y con P1 a P5 de los cinco porqués. Se cita el «Anexo 13» sin verificar.
- **Corrección:** Renombrar los artefactos con un prefijo propio.
- **Prueba de cierre:** Ningún identificador se repite entre listas.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-33 · MAYOR · Comprobaciones triviales y salidas prejuzgadas

- **Ubicación:** E3-P21 (libro de 19 hojas)
- **Evidencia:** La comprobación H5 (suma de influencias menos suma de dependencias igual a cero) es una identidad de toda matriz cuadrada. Los umbrales de H9 y H10 (0,50) no tienen fuente. H3 fija «ÚNICA» como diagnóstico requerido. H18 declara verificación paramétrica sin script ni huella.
- **Corrección:** Reemplazar por controles que puedan fallar y declarar el estado de cada umbral.
- **Prueba de cierre:** Cada control tiene un caso de rechazo ejecutable.
- **Estado en esta corrida:** Pendiente en el documento original

### HR-34 · MAYOR · La plantilla no está vacía

- **Ubicación:** Insumo: Vester_MICMAC_Plantilla_15_vacia.xlsx
- **Evidencia:** La hoja M contiene los quince nombres y la matriz S1, con 32 aristas y suma de influencias 67. Es idéntica celda a celda a S1 del Paso 4. La hoja SVG produce #NAME? en LibreOffice por funciones propias de Excel; el aviso REVISAR de «Comprobaciones» es un artefacto del programa.
- **Corrección:** Registrar S1 como escenario recibido y no como plantilla vacía.
- **Prueba de cierre:** Las tres hojas recalculadas coinciden con el motor de A¹ a A⁶.
- **Estado en esta corrida:** Corregido en 4.4 (libros S0, S1 y S2)

### HR-35 · MENOR · Lenguaje narrativo y enfático

- **Ubicación:** Paso 4, 4.4.2 a 4.4.12
- **Evidencia:** Aparecen términos como «explosivo», «titiriteros», «violentamente», «bucle infinito» y «propagación térmica». Incumplen el registro sobrio y la preferencia del usuario.
- **Corrección:** Sustituir por términos técnicos precisos.
- **Prueba de cierre:** Búsqueda de la lista de términos sin resultados.
- **Estado en esta corrida:** Corregido en las secciones nuevas

### HR-36 · MENOR · Datos fijos y magnitudes inconsistentes

- **Ubicación:** E3-P19 y Paso 5
- **Evidencia:** La fecha 11 de octubre de 2026 está escrita en el texto. K01 usa 100 nodos, el Paso 4 cita 4.608 nodos y la escena menciona 50 sensores.
- **Corrección:** Parametrizar la fecha y unificar la cantidad de nodos.
- **Prueba de cierre:** Una sola cantidad de nodos en todo el documento.
- **Estado en esta corrida:** Pendiente en el documento original

## 6. Resultados que el expediente calcula bien

| Elemento | Resultado de la revisión |
| --- | --- |
| Aritmética del índice de cierre lógico (0,20; 0,60; 0,70; 1,00) | Recalculada; correcta |
| Índice de carga de contradicciones derivadas (0,40; 0,40; 0,60; 0,60) | Recalculado; correcto |
| Riesgo residual (0,32; 0,24; 0,24; 0,24; índice 0,26; máximo 8) | Recalculado; correcto |
| Suma ponderada (0,460; 0,325; 0,535; 0,795) y sensibilidad de un criterio a la vez con variación de 20 % | Recalculada; sin reversión de ranking |
| Valor monetario esperado de riesgos: 585 millones, 4,18 % | Recalculado; correcto |
| Tabla 14.2: aritmética de filas y totales | Correcta; el problema está en la base de los ahorros |
| Sumas del ledger S0: ΣI = ΣD = 53; medianas 3 y 3; A⁷ = 0 | Recalculadas; correctas para S0 |
| Camino más largo de S0: seis aristas (V07, V09, V10, V06, V11, V12 o V14, V15) | Verificado |

## 7. Reconciliación numérica del escenario S1

La tabla compara las potencias de S1 del Paso 4 con las de tres cálculos concordantes. Los cálculos son el motor oficial, uno independiente y la plantilla recalculada.

| Potencia | Suma de la matriz en el documento | Suma recalculada |
| --- | --- | --- |
| A¹ | 67 | 67 |
| A² | 129 | 280 |
| A³ | 258 | 1.205 |
| A⁴ | 561 | 4.855 |
| A⁵ | 1.257 | 19.154 |
| A⁶ | 2.894 | 80.500 |
| A⁷ | 6.574 | 349.230 |
| A⁸ | 15.195 | 1.484.060 |
| A⁹ | 35.539 | 6.071.508 |
| A¹⁰ | 82.529 | 24.573.040 |

Solo A¹ coincide. El recálculo se verificó con aritmética exacta. El documento narra rangos de influencia indirecta (V05 en 12, V15 en 2). El cálculo los contradice (V05 en 1, V15 en 6).

## 8. ¿Qué se me escapa?

| Vacío | Efecto | Ruta de solución |
| --- | --- | --- |
| Términos de referencia y anexos | No permite verificar elegibilidad, tope, madurez ni contrapartida | Aportar los documentos y repetir Gate 0 |
| Lectura de fuentes primarias | El respaldo de 41 de 48 direcciones no nulas es secundario | Leer Suresh 2025, Bang 2026, Ayala-Parra 2026 y Tavella 2026 con localizador |
| Panel humano | Ninguna ficha de 4.4 está ratificada | Sesión de adjudicación con acta, desde los 14 enlaces de mayor efecto |
| Variables omitidas del modelo | Distancia a la referencia, edad del sensor, episodios de humo y precipitación pueden alterar las influencias | Evaluar una matriz de 19 variables |
| Línea base de error | Impide declarar éxito del piloto | Medir con referencia gravimétrica |
| Verificación de normas vigentes | Las citas normativas del expediente no se comprobaron | Consultar la fuente controlante con fecha |

## 9. Valor estratégico

La revisión permite decidir qué partes del expediente pueden usarse y cuáles requieren reconstrucción antes de presentar la propuesta. Separa el cálculo aritmético correcto de la cadena causal no reproducible. Ordena la corrección por impacto en las compuertas. La utilidad es potencial. Ningún resultado observado respalda todavía la propuesta.

## 10. Orden de corrección propuesto

| Orden | Acción | Hallazgos que cierra |
| --- | --- | --- |
| 1 | Aportar términos de referencia, anexos y fuentes citadas; repetir Gate 0 | HR-15, HR-28 y Gate 0 |
| 2 | Adoptar S2 como matriz de trabajo y ratificar las fichas prioritarias | HR-01 a HR-06, HR-20, HR-22 y HR-30 |
| 3 | Fijar una definición de calibración, una meta de error y una línea base | HR-12, HR-13 y HR-14 |
| 4 | Reescribir la sostenibilidad con custodia por tramos y recalcular presupuesto y cronograma | HR-09, HR-10, HR-11 y HR-26 |
| 5 | Reconciliar corpus, cifras bibliométricas y citas con el informe | HR-16 y HR-27 |
| 6 | Eliminar residuos, completar secciones y renombrar identificadores | HR-19, HR-21, HR-32 y HR-35 |

## 11. Premortem de la corrección

Se supone que, tres meses después, la corrección falló.

| Causa | Señal temprana | Contención |
| --- | --- | --- |
| Se corrigió el texto y no la matriz | El texto nuevo conserva las cifras de S1 | Regenerar todas las tablas con el motor |
| Las fichas se ratificaron en bloque | Un acta sin discusión por enlace | Revisar primero los enlaces de mayor efecto |
| Se reemplazó el receptor supuesto por otro supuesto | Cartas sin partida ni competencia | Exigir capacidad de absorción por dimensión |
| Los términos de referencia contradicen el piloto o los tramos | Observaciones del convocante | Consultar antes de presupuestar |

## 12. Referencias

Informe de vigilancia tecnológica y bibliometría de 42 documentos [Documento de trabajo aportado por el usuario, autoría NO_IDENTIFICADA]. (2026). Archivo informe_FINAL.docx.

Embudo de problematización y análisis causal del sistema de vigilancia ambiental, E3-P00 a E3-P21, Pasos 1, 3, 4, 5 y 6 [Documento de trabajo aportado por el usuario, autoría NO_IDENTIFICADA]. (2026). Archivo Problematica_E3-P00.docx.

GENESIS-CTeI 36.10 RC2 (VM-PAR3-MDR3-CONT1) y Norma Transversal CTeI v1.1 [Metaprompt aportado por el usuario]. (2026).
