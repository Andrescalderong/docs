# Admisión TV-1, Gate 0 y declaración de alcance

Caso: SGR_CONV56_AIRE. Corrida: RUN_2026-10-13_MDR. Este documento registra la admisión de los insumos, la validación de los prerrequisitos estratégicos y el alcance realmente ejecutado.

## 1. Admisión TV-1

TRANSPORTE_VERIFICADO no equivale a validación científica. Una dependencia faltante bloquea solo su uso.

| Control | Resultado | Evidencia | Límite |
| --- | --- | --- | --- |
| 1. Identidad y versión | CUMPLE | Caso SGR_CONV56_AIRE; corrida RUN_2026-10-13_MDR; GENESIS 36.10 RC2 VM-PAR3-MDR3-CONT1; NTC 1.1; huella SHA-256 del maestro extraído de la conversación: 685a73f45ba1d3011a3b1ba3a1722482c46d8b9a68ffe5cbc4dbe131e4603ba8. No se cambia la aprobación de E3 ni la del usuario | La huella corresponde al texto extraído de la conversación, no a un archivo original |
| 2. Integridad física | CUMPLE para los tres archivos aportados; NO_APLICA para ZIP previo | Problematica_E3-P00.docx ad06c90bd70a4d9217567f8eb4aff4771f3c92b5d961b7e60e8d90a126bd6801; informe_FINAL.docx 29f443a909e831b751fb39f0f43d5aec838a55177b32a5a89eb34cbbd7b4fc0b; Vester_MICMAC_Plantilla_15_vacia.xlsx 9155d355c7cc29b02eeb2c64b826768deb605a3bac6e59a84c87b2927ede1497 | Los archivos se abrieron y convirtieron sin error; no existe respaldo anterior |
| 3. Estado | NO_APLICA como paquete; CUMPLE para los nulos | No existe ESTADO previo. La plantilla contiene S1 con sus valores; no se rellenó ausencia con cero | La plantilla no estaba vacía |
| 4. Entregados | NO_APLICA | No existen IDs entregados previos. El documento Problematica_E3-P00 se leyó completo | No hay versiones anteriores que comparar |
| 5. Dependencias | CUMPLE con reserva | Doce programas con huella declarada coinciden (CONTROL_MDR). Faltan términos de referencia, Anexo 4, planes de desarrollo, artifact_tool y el código de verificador_ntc.py, que el metaprompt no incluye | Cada ausencia bloquea solo su uso |
| 6. Continuidad | CUMPLE | Cursor inicial: 4.3. Orden: 4.3, 4.4, 4.4-MDR y 4.5. Alcance autorizado: esas cuatro secciones. Cursor final: 4.5.7. Siguiente acción: formalización del problema solo con autorización | El respaldo ZIP se genera en el paquete |

## 2. Gate 0: prerrequisitos estratégicos

La regla bloqueante exige que ningún elemento tenga estado no cumplido para generar el Paso 1. La tabla evalúa los siete elementos con la evidencia del expediente.

| Elemento | Prueba | Evidencia | Naturaleza y verificación |
| --- | --- | --- | --- |
| EB-01 Demandas territoriales | NO_EJECUTADO | El expediente declara DT-CAL-11, DT-CUN-11 y DT-VAL-7 con artículos de los planes de desarrollo. El Anexo 4 no se aportó | DECLARADO; NO_VERIFICADO |
| EB-02 Perfil de alianza | NO_CUMPLE | La alianza es SUPUESTO por instrucción del usuario. Faltan NIT, verificación ScienTI y cartas con el sub-checklist jurídico | SUPUESTO |
| EB-03 TRL demostrable | NO_CUMPLE | TRL inicial 4 y final 8: salto de 4 niveles frente al máximo de 3. El TRL inicial no cita evidencia. E3-P20 declara TRL 4 a 7 u 8 | DECLARADO; NO_VERIFICADO |
| EB-04 Productos MMG tipificados | CUMPLE | PROT-FUNC, SW-REG, ART-A1/A2 y ASC-PART (Capítulo 12.3), con producto de nuevo conocimiento y de apropiación social | DOCUMENTADO; NO_VERIFICADO (tipología sin fuente controlante) |
| EB-05 Contrapartida documentada | NO_CUMPLE | Sin cartas de compromiso. El porcentaje exigido por los TdR es VACIO. La contrapartida de la institución es 1.100 millones en la Tabla 8.1 y 600 en la 8.2 | DECLARADO; CONTRADICTORIO |
| EB-06 Articulación con planes y políticas | NO_EJECUTADO | La Tabla 5.0 declara artículo, indicador y dos instrumentos nacionales. Ninguna fuente se aportó para verificar su vigencia | DECLARADO; NO_VERIFICADO |
| EB-07 Vigencia de fuentes | NO_CUMPLE | No existe registro de fuentes perecederas con fecha de verificación | VACIO |

**Resultado de Gate 0.** No aprobado: cuatro elementos NO_CUMPLE (EB-02, EB-03, EB-05 y EB-07) y dos NO_EJECUTADO (EB-01 y EB-06). El metaprompt no genera el Paso 1 en ese estado. Esta corrida no genera el Paso 1. Continúa con el análisis de 4.3 a 4.5 porque el usuario lo instruyó. Esos resultados son borrador con vacíos y no habilitan por sí mismos los pasos siguientes.

## 3. Registros de decisión de Gate 0

**ND-01 Aprobación de Gate 0.**

**Tabla RDG. Registro de decisión GENESIS**

| Campo | Contenido |
| --- | --- |
| NODO | ND-01 Aprobación de Gate 0 |
| CLASE | MAYOR. Determina el avance al Paso 1. |
| DECISION | No aprobar el avance al Paso 1 con la evidencia del expediente. Continuar con 4.3 a 4.5 como borrador con vacíos por instrucción del usuario. |
| DECIDE | Usuario, mediante la instrucción de continuar. Ningún programa aprueba el Gate 0. |
| EXCLUYE | Declarar aprobado el Gate 0 por la existencia del Paso 1 en el documento. Usar 4.3 a 4.5 como habilitación de pasos posteriores. |
| NODOS_BLANCOS | 5: EB-04 con cuatro tipos MMG (Capítulo 12.3); TRL inicial 4 y final 8 (Paso 1); contrapartida de 2.110 millones en la Tabla 8.1; códigos DT-CAL-11, DT-CUN-11 y DT-VAL-7 (Tabla 5.0); alianza declarada como SUPUESTO por el usuario. |
| NODOS_GRISES | 2: términos de referencia y Anexo 4 no aportados; cartas de la alianza inexistentes. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0 |
| PATRON_DOMINANTE | PR-06: sin patrón emergente identificado; es una decisión de control del expediente. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: Sí. |
| ESCENA_SIMULABLE | El equipo formulador recibe esta tabla, consigue los términos de referencia y las cartas y repite la validación antes de formular. La entidad ejecutora decide si presenta la propuesta con las reservas. |
| EVIDENCIA_JH_A | Cartas de compromiso con el sub-checklist jurídico de cinco puntos (inexistentes). |
| EVIDENCIA_JH_B | Cálculo del salto de TRL (8 − 4 = 4 niveles frente al máximo de 3) y la tabla de siete elementos. |
| CERCA_CONCEPTUAL | No es un juicio sobre la calidad científica de la propuesta: evalúa prerrequisitos documentales. |
| ESTATUTO_CAUSAL | NO_APLICA. |
| VEREDICTO | Gate 0 no aprobado: cuatro elementos NO_CUMPLE y dos NO_EJECUTADO. |
| RAZON_DEL_DESCARTE | Se descarta aprobar con condiciones, porque la regla es bloqueante. |
| RESULTADO | NO_CIERRA para el avance al Paso 1. CIERRA con vacíos la corrida de 4.3 a 4.5. |

**ND-02 Selección de demanda territorial.**

**Tabla RDG. Registro de decisión GENESIS**

| Campo | Contenido |
| --- | --- |
| NODO | ND-02 Selección de demanda territorial |
| CLASE | MAYOR. |
| DECISION | Registrar DT-CAL-11, DT-CUN-11 y DT-VAL-7 como demandas declaradas. No verificarlas sin el Anexo 4. |
| DECIDE | Equipo formulador (POR_IDENTIFICAR). |
| EXCLUYE | Elegir la demanda por afinidad con la alternativa preferida. |
| NODOS_BLANCOS | 3: códigos y nombres de las tres demandas (Tabla 5.0 y Capítulo 13); departamentos asociados; artículos citados de los planes de desarrollo. |
| NODOS_GRISES | 2: existencia de los códigos en el Anexo 4; vigencia de los artículos y metas citados. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 1 (la verificación no puede cerrarse sin el Anexo 4) |
| PATRON_DOMINANTE | PR-06: sin patrón emergente identificado. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: Sí. |
| ESCENA_SIMULABLE | Un analista del equipo abre el Anexo 4 y copia el código y el nombre de cada demanda con su página. El equipo compara cada código con el expediente antes de formular. |
| EVIDENCIA_JH_A | Anexo 4 con página y código (inexistente en esta sesión). |
| EVIDENCIA_JH_B | Tabla 5.0 con artículo e indicador por departamento. |
| CERCA_CONCEPTUAL | La selección no se justifica por afinidad con la solución. |
| ESTATUTO_CAUSAL | NO_APLICA. |
| VEREDICTO | Demandas declaradas; verificación pendiente. |
| RAZON_DEL_DESCARTE | Se descarta marcarlas verificadas, porque el Anexo 4 no se aportó. |
| RESULTADO | CIERRA con vacíos declarados. |

**ND-03 Declaración de TRL.**

**Tabla RDG. Registro de decisión GENESIS**

| Campo | Contenido |
| --- | --- |
| NODO | ND-03 Declaración de TRL |
| CLASE | MAYOR. |
| DECISION | No aprobar el TRL inicial 4 ni el final 8 con la evidencia disponible. Exigir evidencia del TRL inicial y reducir el salto a 3 niveles o justificarlo. |
| DECIDE | Equipo formulador (POR_IDENTIFICAR) con la entidad ejecutora. |
| EXCLUYE | Declarar TRL 8 por la meta del proyecto sin pruebas en condiciones reales planificadas. |
| NODOS_BLANCOS | 3: TRL inicial 4 (Paso 1); TRL final 8 (Paso 1); TRL 4 a 7 u 8 (E3-P20). |
| NODOS_GRISES | 2: evidencia de laboratorio de los algoritmos de corrección; criterio de entorno relevante del Hito 1, que usa una prueba de conectividad. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 1 (el TRL final se declara antes de definir la prueba que lo demuestra) |
| PATRON_DOMINANTE | PR-06: sin patrón emergente identificado. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No: el TRL 8 exige entornos reales con infraestructura no verificada. |
| ESCENA_SIMULABLE | El ingeniero de la institución ejecutora corre el algoritmo con datos de laboratorio y registra el error frente a la referencia. El equipo decide con ese registro si el TRL inicial es 4. |
| EVIDENCIA_JH_A | Informe de laboratorio con fecha y configuración (inexistente). |
| EVIDENCIA_JH_B | Salto de 4 niveles calculado frente al máximo de 3. |
| CERCA_CONCEPTUAL | El TRL no mide el valor científico de la propuesta. |
| ESTATUTO_CAUSAL | NO_APLICA. |
| VEREDICTO | TRL no aprobado. |
| RAZON_DEL_DESCARTE | Se descarta aprobar TRL 4 a 8, porque el salto excede 3 niveles. |
| RESULTADO | CIERRA con vacíos declarados. |

**ND-04 Vigencia de fuentes (clase MENOR: se ejecutan G-1, G-3 y G-7).**

**Tabla RDG. Registro de decisión GENESIS**

| Campo | Contenido |
| --- | --- |
| NODO | ND-04 Vigencia de fuentes |
| CLASE | MENOR. No es bloqueante por sí sola: afecta la verificabilidad. |
| DECISION | Exigir un registro de fuentes perecederas con fecha de verificación antes de formular. Marcar NO_VERIFICADO toda norma y plan citados. |
| DECIDE | Equipo formulador (POR_IDENTIFICAR). |
| EXCLUYE | Presentar normas o planes como vigentes sin consulta. |
| NODOS_BLANCOS | NO_APLICA (clase MENOR). |
| NODOS_GRISES | NO_APLICA (clase MENOR). |
| RUPTURAS | R-01: 0 \| R-02: NO_APLICA \| R-03: 0 \| R-04: NO_APLICA \| R-05: NO_APLICA |
| PATRON_DOMINANTE | NO_APLICA (clase MENOR). |
| ANTIPATRONES_PR | NO_APLICA (clase MENOR). |
| ESCENA_SIMULABLE | NO_APLICA (clase MENOR). |
| EVIDENCIA_JH_A | NO_APLICA (clase MENOR). |
| EVIDENCIA_JH_B | NO_APLICA (clase MENOR). |
| CERCA_CONCEPTUAL | NO_APLICA (clase MENOR). |
| ESTATUTO_CAUSAL | NO_APLICA. |
| VEREDICTO | Registro de fuentes perecederas exigido. |
| RAZON_DEL_DESCARTE | Se descarta aceptar la vigencia por mención. |
| RESULTADO | CIERRA con vacíos declarados. |

## 4. Declaración de alcance

| Parte | Estado | Motivo |
| --- | --- | --- |
| 4.3 Clasificación de variables para inferencia causal | EJECUTADA | El expediente la omite |
| 4.4 Vester y MICMAC paritario | EJECUTADA | Catorce piezas, 105 fichas, cinco escenarios y registros ND-08 y ND-09 |
| 4.4-MDR | EJECUTADA | Nueve fases, árboles A-DEC y A-TDC, expediente y registro de contraste |
| 4.5 Árbol de problemas | EJECUTADA | Árbol A-PROB con los identificadores de las variables |
| Pasos 5 y 6 (formalización del problema y alternativas) | NO_EJECUTADO | Dependen de la ratificación de las fichas y de los términos de referencia; requieren autorización |
| Capítulos 1 a 21, paquete 1000X y estrategia | NO_EJECUTADO | El metaprompt los entrega uno por uno con la orden CONTINUAR y exigen insumos ausentes |

El usuario pidió ejecutar el metaprompt completo. La corrida cubre la totalidad del tramo en el que el expediente revisado omite o calcula de forma no reproducible las secciones. Los pasos y capítulos posteriores quedan pendientes por las dependencias indicadas y se ejecutan con la orden CONTINUAR.
