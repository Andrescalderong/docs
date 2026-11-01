# Qué sigue faltando para radicar · SIGP 143329 · Anexo 3 v7

Corte: 1 de noviembre de 2026. Cierre: martes 3 de noviembre de 2026, 4:00 p. m. Firmas y soportes: domingo 1 de noviembre, 6:00 p. m.

## A. Cambios del Anexo 3 v7 y de Avanciencia ya incorporados

| Cambio | Dónde quedó |
| --- | --- |
| Las cifras no cambian: SGR 13.999.405.215 COP; contrapartida 1.774.000.000 COP (150.000.000 en efectivo); total 15.773.405.215 COP | Anexo 2 y matriz v7 (la conciliación cuadra) |
| El aporte de cada municipio deja de ser «profesionales» (TH-20 y TH-21) y pasa a «uso de software y hardware existentes» (EQ-24 y EQ-25, 60.000.000 COP cada uno): licencias SIG 20.000.000; alojamiento en el centro de datos 15.000.000; equipos de la sala de gestión del riesgo 15.000.000; conectividad 10.000.000. No incluye horas de funcionarios | Secciones 10, 19 y 26 del Anexo 2; Anexo 1; certificados 10.18 y de contrapartida de los municipios; resúmenes para los alcaldes; gráfico integrado |
| Estado de soporte de cada partida (hoja «C. Soportes y pendientes» del Anexo 3 v7) | Columna «Observación» y hoja «Alertas» de la matriz v7 |
| Actualización de Avanciencia al componente de apropiación social: liderazgo, trayectoria (Expociencia, Maloka, revista Innovación y Ciencia, podcast y convenciones de interfaz política-ciencia), cinco razones de idoneidad, co-creación y sostenibilidad | Sección 19 del Anexo 2 y documento de estrategia ASC; razón social en la sección 1 |
| Resumen ejecutivo para el despacho de cada alcalde | Carpetas B y C de 02_FIRMAR |

## B. Lo que sigue faltando, por gravedad

### No subsanables

| N.º | Pendiente | Estado según el Anexo 3 v7 | Responsable |
| --- | --- | --- | --- |
| 1 | Dos cotizaciones y análisis de costos por bien o servicio (TdR 12.2, nota 4) | 70 partidas «por cotizar»; EQ-01 (nodos) y EQ-04 (gateways) con una sola oferta preliminar; EQ-03 (referencias) con oferta de configuración y moneda pendientes; EQ-07 (banco) con oferta parcial; EQ-23 (cámara climática) sin oferta; ST-12 a ST-20 (plataforma geoespacial) sin oferta; PD-04 con oferta preliminar por conciliar | Universidad y formulador |
| 2 | Atribución de las escalas de honorarios | 16 partidas de personal y viáticos con escala sin fuente atribuible | Universidad |
| 3 | Acto de declaratoria que comprenda Manizales y Calarcá (10.20) | Sin copia | Universidad con los municipios |
| 4 | Certificado de concordancia con el plan de acción específico (10.21), uno por lugar de ejecución | Modelos listos; sin firmar | Alcaldías o gobernaciones |
| 5 | Aval del comité de ética y acto de conformación (10.10) | Solicitud lista; sin aval | Universidad |
| 6 | Firma del Anexo 3 por representante legal con facultad | «Pendiente de datos y firma verificable» | Universidad |

### Estado de los puntos observados en la revisión del 1 de noviembre

| Punto | Texto corregido | Protocolo o formato preparado | Evidencia efectivamente producida | Falta |
| --- | --- | --- | --- | --- |
| TRL 4: documentación técnica del nodo y del gateway | Sí (tabla 13.4: equipos comerciales ya probados) | Sí (carta de solicitud al proveedor, carpeta 04) | No | Recibirla de SIOT, firmada |
| TRL 4: informe de prueba de fábrica del nodo enlazado con el gateway | Sí | Sí (misma carta) | No | Recibirlo de SIOT, firmado |
| TRL 4: declaración de conformidad y referencias de instalación | Sí | Sí (misma carta) | No | Recibirla de SIOT, con PIRE y ganancia de antena |
| Pruebas de sensor, enlace y autonomía | Sí: pasan a pruebas de aceptación de los lotes en los meses 4 a 6 (actividad 1.2) | Sí (protocolo de aceptación, carpeta 04) | No aplica antes del inicio | Nada antes de radicar |
| TRL 4: informe 4 (modelo de corrección) | Sí | No aplica | Sí, analítica: simulación con datos sintéticos, reproducible (código, salidas y huellas SHA-256 en la carpeta A). No acredita desempeño físico | Firma del responsable técnico |
| Cifra de transferencia entre municipios | Sí: 95,55 % (1.911 de 2.000 pruebas) en Anexo 2 e Informe 4 | No aplica | Sí: salida sim_coloc.json reproducida con semilla fija | Nada |
| Grupo de investigación | Sí: GAUV, COL0159731, categoría B (verificado en GrupLAC) | Certificado 10.18 de la universidad con el grupo | No | Aval escrito del líder del grupo y registro en el SIGP |
| Gestión y Medio Ambiente | Sí (filas en secciones 1 y 26) | Sí (ficha de identidad y capacidades) | No | Certificado de existencia, NIT, inventario de equipos con calibración, personal y experiencia |
| Radio (ANE) | Sí: Anexo 1 de la Resolución 105 de 2020 compilada (469/2020, 648/2023, 91/2023, 28/2026); plan de canales 915-928 MHz sin 902-915 MHz | Sí (declaración de conformidad pedida al proveedor) | No | PIRE máxima y modulación verificadas en la compilación vigente; declaración de conformidad del fabricante |
| Dron (Aerocivil) | Sí: RAC 100 (Res. 01983 de 2023), operación de trabajo, registro, idoneidad del piloto, seguro, línea de vista | No | No | Límites de altura y distancias del texto oficial; categoría y autorización por sitio; reglas para zonas del sismo, si existen |
| Localización (DIVIPOLA) | Sí: 17001 y 63130 | No aplica | Sí (verificado por el revisor) | Coordenadas MAGNA-SIRGAS de las cabeceras para la MGA |

**Decisión sobre el TRL (opción A, aprobada el 1 de noviembre).** Los TdR puntúan el TRL que la solución alcanza al cierre (criterio 3.1) y no exigen ensayos propios para el nivel de entrada. La red usa equipos comerciales ya probados, cuyo funcionamiento en conjunto acredita el fabricante; el proyecto desarrolla la corrección, la integración y la operación. Si SIOT no entrega sus documentos antes del cierre, la tabla 13.4 los deja como «solicitados» y no se presentan como evidencia.

### Habilitantes de las entidades

| N.º | Pendiente | Observación |
| --- | --- | --- |
| 7 | Numeral por el que se habilita Avanciencia | Ahora se presenta como Asociación Colombiana para el Avance de la Ciencia, entidad privada sin ánimo de lucro. Confirmar si se habilita por 10.12 (sector productivo), 10.13 (sociedad civil: exige domicilio en un departamento afectado) o 10.14 (actor reconocido del SNCTI con resolución vigente). Si es por 10.13 y su domicilio es Bogotá, no cumple |
| 8 | Denominación de Avanciencia | El Anexo 2 la llama «oficina de transferencia de resultados de investigación (OTRI)». Confirmar si tiene ese reconocimiento; si no, se cambia por «actor del SNCTI» en todo el documento |
| 8b | Identidad y capacidades de Gestión y Medio Ambiente | No aparece en fuentes públicas con esa razón social; la ficha de la carpeta E recoge razón social, NIT, constitución, equipos, personal y experiencia |
| 8c | Grupo de investigación de la universidad | Gestión Ambiental USTA Villavicencio (GAUV), COL0159731, categoría B (verificado en GrupLAC); falta el aval escrito del líder a su participación |
| 9 | Certificados de existencia (menos de 90 días) de Avanciencia y de Gestión y Medio Ambiente (con un año de constitución) y resolución de reconocimiento de Avanciencia | Sin copia |

### Firmas en curso

| N.º | Pendiente | Estado |
| --- | --- | --- |
| 10 | Cartas de contrapartida de Manizales y Calarcá (EQ-24 y EQ-25) con inventario, periodo de uso, método de valoración y facultad del firmante | «En proceso de firma»; copia no recibida. Modelos en las carpetas B y C |
| 11 | Anexo 1 con las cinco firmas en un solo PDF | Versión v7 lista |
| 12 | Certificados 10.18, 10.19, compromisos 10.6 y plan de sostenibilidad 10.16 | Modelos listos |
| 13 | Certificaciones de contrapartida de Avanciencia y de Gestión y Medio Ambiente (sin la del efectivo, el criterio 7 queda en cero) | Modelos listos |

### Datos del documento técnico

| N.º | Pendiente | Responsable |
| --- | --- | --- |
| 14 | Soportes de la experiencia de Avanciencia y fuente de la afirmación atribuida a Eduardo Posada | Avanciencia |
| 15 | NIT, representantes legales y responsables institucionales de las cinco entidades | Cada entidad |
| 16 | Grupo de investigación con categoría vigente, dos proyectos para el Anexo 5 y acreditación | Universidad |
| 17 | Sede del laboratorio de modelación en Manizales o en Calarcá | Universidad con los municipios |
| 18 | Demanda territorial (Anexo 4) y reportes oficiales de afectación | Municipios |
| 19 | Registro en la MGA-Web (tipología D) en la PIIP | Universidad |
| 20 | Responsable del tratamiento de datos y programas de maestría con registro calificado | Universidad |
