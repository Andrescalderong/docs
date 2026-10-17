# FICHA MAESTRA v2 DEL ANEXO 2 (fuente única de cifras; prevalece sobre la ficha anterior)

Esta ficha incorpora los términos de referencia (TdR v1.6, convocatoria 56) que se aportaron después de la corrida anterior. Donde difiere de RAIZ/maestro/FICHA_MAESTRA.md o de los capítulos de RAIZ/caps/, prevalece esta ficha.

## 1. Identidad

- Título (183 caracteres con espacios): Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto en Caldas, Cundinamarca y Valle del Cauca
- Proceso: Implementación. Objeto: red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto. Localización: Caldas, Cundinamarca y Valle del Cauca.
- Convocatoria: 56, Convocatoria de emergencia para la recuperación y generación de capacidades transformadoras, en el marco del Decreto 1414 de 17 de septiembre de 2026. Cierre de presentación: 3 de noviembre de 2026, 4:00 p. m.
- Línea temática principal: 5.1. Ciencia, tecnología e innovación para la gestión anticipada del riesgo y la seguridad de las regiones; subnumerales 5.1.1 (monitoreo inteligente, observación territorial y alerta temprana) y 5.1.2 (modelación avanzada, gemelos digitales y analítica predictiva). Sin línea secundaria.
- Territorio: Caldas (región Eje Cafetero), Cundinamarca (Centro Oriente) y Valle del Cauca (Pacífico); verificar con el Anexo 8. 12 municipios (4 por departamento; nombres por diligenciar). Nodos: Caldas 33, Cundinamarca 34, Valle del Cauca 33.
- Evento: terremoto (Decreto 1261 de 2026, modificado por el Decreto 1348 de 2026). Territorio y alianza son supuestos de trabajo por instrucción del usuario; no hay reportes oficiales de afectación en los archivos.
- Duración: 24 meses (104 semanas). TRL de entrada 4; TRL comprometido al cierre 8; piso TRL 7 al mes 19. La evidencia del TRL 8 es el ensayo independiente y la evaluación externa del mes 23 (hito H7).
- Alianza (numeral 3 de los TdR): entidad proponente = IES con acreditación de alta calidad (supuesto); aliada 1 = empresa tecnológica (actor del sector productivo); aliada 2 = entidad territorial de un departamento afectado. Nombres por diligenciar. Cada integrante aporta contrapartida cuantificada. La entidad territorial aliada no puede figurar también como beneficiaria; si coincide con la jurisdicción de alguno de los 15 comités, ese comité se sustituye por otro de la misma jurisdicción.
- Beneficiarios: 15 comités de gestión del riesgo (12 municipales y 3 departamentales), 150 funcionarios (supuesto), operarios de remoción, población expuesta, autoridades ambientales.

## 2. Solución

Red de 100 nodos hoja de medición de PM2,5 y PM10 (sensor óptico de bajo costo con temperatura y humedad), 10 gateways y 3 monitores gravimétricos de referencia (uno por departamento) para colocalización. Los nodos transmiten por LoRa al gateway; el gateway aplica el modelo de corrección (humedad, temperatura, fracción gruesa) y reenvía por red celular con enlace satelital de respaldo y almacenamiento local de 7 días; nodos con autonomía mínima de 14 días sin sol; la nube aloja el gemelo digital, la base de datos y el tablero con el índice local y el protocolo de alerta. Custodia distribuida por componente y por tramo, con cláusula de apertura. Metas técnicas: R² ≥ 0,70 y NRMSE ≤ 30 % frente a la referencia (guía de la EPA de 2021 como ancla informativa); pendiente 0,65–1,35; sesgo entre −5,0 y 5,0 µg/m³; disponibilidad mensual ≥ 90 %; pérdida de paquetes ≤ 10 %. NMAE ≤ 15 % es aspiración. La línea base de error se mide en el tramo 1.

## 3. Objetivos

- Objetivo general: Reducir el error de medición de material particulado de una red de 100 nodos de bajo costo, y asegurar su uso institucional en la gestión del riesgo, mediante calibración dinámica en gateways, operación con energía y enlace redundantes y custodia distribuida por tramos, en Caldas, Cundinamarca y Valle del Cauca, durante 24 meses.
- OE1: Corregir la interferencia de humedad y de fracción gruesa en las mediciones de PM2,5 y PM10 mediante colocalización con equipos de referencia y un modelo de corrección aplicado en gateways, hasta cumplir los umbrales de desempeño fijados en el piloto del tramo 1 y verificados al mes 24. Meta: R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia en los tres tramos.
- OE2: Mantener la disponibilidad de 100 nodos y 10 gateways ante polvo, humedad y fallas de energía y de enlace, mediante autonomía mínima de 14 días sin sol y un enlace alterno con almacenamiento local de 7 días. Meta: Disponibilidad mensual de nodos ≥ 90 % y pérdida de paquetes ≤ 10 %.
- OE3: Lograr el uso del tablero y del protocolo de alerta por los comités de gestión del riesgo, con umbrales validados localmente y custodia por componente, mediante co-diseño, formación y convenios por tramo. Meta: ≥ 75 % de los comités focalizados usan el tablero en decisiones documentadas al mes 24.

## 4. Tramos

| Tramo | Meses | Nodos | Gateways | Compra nodos | Compra gateways | Compuerta |
| --- | --- | --- | --- | --- | --- | --- |
| Tramo 1: piloto de contraste | 1–12 | 30 | 3 | 36 | 4 | C1 (mes 12) |
| Tramo 2: ampliación condicionada | 13–17 | 40 | 4 | 48 | 4 | C2 (mes 17) |
| Tramo 3: consolidación y transferencia | 18–24 | 30 | 3 | 36 | 3 | C3 (mes 24) |

Compuertas: C1 (mes 12) libera el tramo 2 si R² ≥ 0,70 y NRMSE ≤ 30 % en el piloto y si al menos 50 % de los comités del tramo 1 usa el tablero. C2 (mes 17) libera el tramo 3 con los mismos umbrales en los tres departamentos, disponibilidad ≥ 90 % y convenios de custodia con partida. C3 (mes 24) cierra y transfiere. Las compuertas no reducen el alcance de 100 nodos y 10 gateways: condicionan la secuencia y activan un ciclo de corrección del modelo.

## 5. Presupuesto v2 (SGR)

- Valor solicitado al SGR: $ 8.351.340.000 (59,7 % del tope de $ 14.000.000.000; no se solicita la holgura de $ 5.648.660.000).
- Contrapartida: $ 2.230.000.000 (efectivo $ 210.000.000, 2,51 % del SGR; especie $ 2.020.000.000). Total del proyecto: $ 10.581.340.000.
- Transferencia: $ 210.000.000 = 1,98 % del valor total (mínimo 1 %). Movilidad: $ 24.000.000 = 0,29 % del SGR (máximo 2 %).
- Sin reserva de contingencia, sin pólizas ni seguros (excluidos por el numeral 14.3 de los TdR). El riesgo se atiende con 20 nodos y 1 gateway de reserva, compras por tramo, compuertas y cotizaciones vigentes.

| Rubro del TdR | Valor (COP) | % SGR |
| --- | --- | --- |
| Talento Humano | $ 4.382.880.000 | 52,5 % |
| Equipos y software | $ 1.851.000.000 | 22,2 % |
| Capacitación y eventos | $ 252.000.000 | 3,0 % |
| Servicios tecnológicos y pruebas | $ 473.560.000 | 5,7 % |
| Materiales, insumos y documentación | $ 200.400.000 | 2,4 % |
| Protección del conocimiento y divulgación | $ 187.500.000 | 2,2 % |
| Gastos de viaje | $ 432.000.000 | 5,2 % |
| Infraestructura | $ 132.000.000 | 1,6 % |
| Administrativos | $ 248.000.000 | 3,0 % |
| Seguimiento | $ 192.000.000 | 2,3 % |

### Líneas de presupuesto SGR

| Id | Rubro TdR | Concepto | Unidad | Cant. | Costo unitario | Total | Naturaleza |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Talento Humano | Jóvenes investigadores (6) | persona-mes | 72 | $ 2.000.000 | $ 144.000.000 | DOCUMENTADO |
| P02a | Talento Humano | Sostenimiento de estudiantes de maestría (2) | persona-mes | 48 | $ 4.350.000 | $ 208.800.000 | DOCUMENTADO |
| P02b | Talento Humano | Matrícula de maestría en modalidad de investigación (2) | matrícula | 2 | $ 48.000.000 | $ 96.000.000 | DOCUMENTADO |
| P03 | Talento Humano | Doctor en estancia posdoctoral (1) | persona-mes | 24 | $ 12.920.000 | $ 310.080.000 | DOCUMENTADO |
| P04 | Talento Humano | Ingenieros IoT y de campo (3) | persona-mes | 72 | $ 9.000.000 | $ 648.000.000 | DECLARADO |
| P05 | Talento Humano | Coordinación de apropiación social (1) | persona-mes | 24 | $ 8.000.000 | $ 192.000.000 | DECLARADO |
| P06 | Talento Humano | Gerencia de proyecto (1) | persona-mes | 24 | $ 10.000.000 | $ 240.000.000 | DECLARADO |
| P07 | Talento Humano | Especialista en metrología y calibración (1) | persona-mes | 24 | $ 12.000.000 | $ 288.000.000 | PROPUESTO |
| P08 | Talento Humano | Ingenieros de software y nube (2) | persona-mes | 48 | $ 9.500.000 | $ 456.000.000 | PROPUESTO |
| P09 | Talento Humano | Ingeniero de firmware y energía (1) | persona-mes | 24 | $ 9.000.000 | $ 216.000.000 | PROPUESTO |
| P10 | Talento Humano | Técnicos de campo departamentales (6) | persona-mes | 144 | $ 4.500.000 | $ 648.000.000 | PROPUESTO |
| P11 | Talento Humano | Profesionales de apropiación social (2) | persona-mes | 48 | $ 6.000.000 | $ 288.000.000 | PROPUESTO |
| P12 | Talento Humano | Analista de datos espaciales y gemelo digital (1) | persona-mes | 24 | $ 10.000.000 | $ 240.000.000 | PROPUESTO |
| P13 | Talento Humano | Profesional en calidad del aire y salud ambiental (1) | persona-mes | 24 | $ 10.000.000 | $ 240.000.000 | PROPUESTO |
| P14 | Talento Humano | Profesional de convenios y custodia (1) | persona-mes | 24 | $ 7.000.000 | $ 168.000.000 | PROPUESTO |
| E01 | Equipos y software | Nodos IoT de medición (100 + 20 de reserva) | unidad | 120 | $ 4.500.000 | $ 540.000.000 | DECLARADO |
| E02 | Equipos y software | Cabezales ópticos de partículas | unidad | 150 | $ 1.200.000 | $ 180.000.000 | DECLARADO |
| E03 | Equipos y software | Monitores gravimétricos de referencia | unidad | 3 | $ 85.000.000 | $ 255.000.000 | DECLARADO |
| E04 | Equipos y software | Gateways con energía solar y respaldo (10 + 1 de reserva) | unidad | 11 | $ 28.000.000 | $ 308.000.000 | PROPUESTO |
| E05 | Equipos y software | Kits de energía solar y batería para nodos | unidad | 120 | $ 650.000 | $ 78.000.000 | PROPUESTO |
| E06 | Equipos y software | Módulos de enlace satelital de respaldo | unidad | 10 | $ 3.500.000 | $ 35.000.000 | PROPUESTO |
| E07 | Equipos y software | Banco de calibración de laboratorio (cámara de humedad y generador de aerosol) | unidad | 1 | $ 150.000.000 | $ 150.000.000 | PROPUESTO |
| E08 | Equipos y software | Estaciones de trabajo para entrenamiento de modelos | unidad | 2 | $ 25.000.000 | $ 50.000.000 | PROPUESTO |
| E09 | Equipos y software | Equipos de campo e instrumentación (lote) | lote | 1 | $ 30.000.000 | $ 30.000.000 | PROPUESTO |
| E10 | Equipos y software | Instancias en la nube reservadas (24 meses) | clúster | 1 | $ 180.000.000 | $ 180.000.000 | DECLARADO |
| E11 | Equipos y software | Software de analítica y repositorios | paquete | 1 | $ 45.000.000 | $ 45.000.000 | DECLARADO |
| E12 | Servicios tecnológicos y pruebas | Planes de datos celulares M2M para gateways (12 SIM. 24 meses) | SIM-mes | 288 | $ 120.000 | $ 34.560.000 | PROPUESTO |
| M01 | Materiales. insumos y documentación | Filtros de membrana PTFE para gravimetría | unidad | 1.200 | $ 12.000 | $ 14.400.000 | DECLARADO |
| M02 | Materiales. insumos y documentación | Polvo de ensayo normalizado y consumibles del banco de calibración | lote | 15 | $ 2.800.000 | $ 42.000.000 | PROPUESTO |
| M03 | Materiales. insumos y documentación | Cerramientos NEMA 4X y mástiles para nodos | unidad | 120 | $ 350.000 | $ 42.000.000 | DECLARADO |
| M04 | Protección del conocimiento y divulgación | Cartillas impresas del índice y del protocolo de alerta | unidad | 5.000 | $ 8.500 | $ 42.500.000 | DECLARADO |
| M05 | Materiales. insumos y documentación | Kits de papelería para talleres de co-diseño | kit | 20 | $ 1.500.000 | $ 30.000.000 | DECLARADO |
| M06 | Materiales. insumos y documentación | Elementos de protección personal (mascarillas N95) | unidad | 3.000 | $ 4.000 | $ 12.000.000 | DECLARADO |
| M07 | Materiales. insumos y documentación | Repuestos y consumibles de mantenimiento (baterías. cables. conectores) | lote | 1 | $ 60.000.000 | $ 60.000.000 | PROPUESTO |
| S01 | Servicios tecnológicos y pruebas | Análisis gravimétrico en laboratorio acreditado | muestra | 240 | $ 350.000 | $ 84.000.000 | DECLARADO |
| S02 | Protección del conocimiento y divulgación | Consultoría jurídica en propiedad intelectual y libertad de operación | hora | 150 | $ 300.000 | $ 45.000.000 | DECLARADO |
| S03 | Servicios tecnológicos y pruebas | Auditoría externa de ciberseguridad | servicio | 2 | $ 15.000.000 | $ 30.000.000 | DECLARADO |
| S05 | Infraestructura | Instalación en sitio. mástiles y obra menor (100 nodos y 10 gateways) | sitio | 110 | $ 1.200.000 | $ 132.000.000 | PROPUESTO |
| S06 | Servicios tecnológicos y pruebas | Estudio de cobertura y de enlace en tres departamentos | estudio | 3 | $ 20.000.000 | $ 60.000.000 | PROPUESTO |
| S07 | Servicios tecnológicos y pruebas | Evaluación externa independiente (meses 12 y 24) | evaluación | 2 | $ 60.000.000 | $ 120.000.000 | PROPUESTO |
| S08 | Servicios tecnológicos y pruebas | Ensayo de desempeño con laboratorio externo | campaña | 1 | $ 90.000.000 | $ 90.000.000 | PROPUESTO |
| S09 | Capacitación y eventos | Formación y soporte a custodios por tramo | tramo | 3 | $ 50.000.000 | $ 150.000.000 | PROPUESTO |
| S10 | Servicios tecnológicos y pruebas | Planes de enlace satelital de respaldo (10 módulos. 22 meses) | módulo-mes | 220 | $ 250.000 | $ 55.000.000 | PROPUESTO |
| S11 | Administrativos | Importación y nacionalización de equipos | servicio | 1 | $ 80.000.000 | $ 80.000.000 | PROPUESTO |
| V01 | Gastos de viaje | Tiquetes aéreos nacionales | trayecto | 150 | $ 600.000 | $ 90.000.000 | PROPUESTO |
| V02 | Gastos de viaje | Viáticos de alojamiento y manutención | día-persona | 600 | $ 350.000 | $ 210.000.000 | PROPUESTO |
| V03 | Gastos de viaje | Arrendamiento de vehículos 4x4 | día | 240 | $ 450.000 | $ 108.000.000 | PROPUESTO |
| V04 | Gastos de viaje | Viaje internacional para divulgación científica | viaje | 2 | $ 12.000.000 | $ 24.000.000 | DECLARADO |
| V05 | Capacitación y eventos | Alimentación de laboratorios ciudadanos | evento | 20 | $ 1.500.000 | $ 30.000.000 | DECLARADO |
| O01 | Protección del conocimiento y divulgación | Cargos de procesamiento de artículos de acceso abierto | artículo | 2 | $ 12.500.000 | $ 25.000.000 | DECLARADO |
| O02 | Capacitación y eventos | Logística de ferias y laboratorios de apropiación | evento | 9 | $ 8.000.000 | $ 72.000.000 | DECLARADO |
| O03 | Protección del conocimiento y divulgación | Registro ante la DNDA y asesoría de propiedad intelectual | paquete | 1 | $ 15.000.000 | $ 15.000.000 | DECLARADO |
| O05a | Administrativos | Administración del proyecto (gastos administrativos y revisoría) | mes | 24 | $ 7.000.000 | $ 168.000.000 | PROPUESTO |
| O05b | Seguimiento | Apoyo a la supervisión y plataforma de seguimiento | mes | 24 | $ 8.000.000 | $ 192.000.000 | PROPUESTO |
| O06 | Protección del conocimiento y divulgación | Publicaciones de divulgación y eventos de socialización | paquete | 1 | $ 60.000.000 | $ 60.000.000 | PROPUESTO |

### Contrapartida

| Id | Aportante | Aporte | Modalidad | Total |
| --- | --- | --- | --- | --- |
| C01 | IES | Investigador principal, 50 % durante 24 meses | Especie | $ 350.000.000 |
| C02 | IES | Coinvestigador técnico, 30 % durante 24 meses | Especie | $ 250.000.000 |
| C03 | IES | Coinvestigadores de ambiente y ciencias sociales, 20 % | Especie | $ 200.000.000 |
| C04 | IES | Uso de laboratorios y equipos de la IES | Especie | $ 300.000.000 |
| C05 | EMP | Aporte de la empresa tecnológica: logística y viáticos de emergencia | Efectivo | $ 210.000.000 |
| C06 | EMP | Infraestructura en la nube de la empresa | Especie | $ 800.000.000 |
| C07 | ENT | Entidad territorial aliada: profesionales de gestión del riesgo y logística de acceso a sitios | Especie | $ 120.000.000 |

### Ajustes por los TdR (respecto de la ficha anterior)

| Id | Tema | Antes | Después | Fundamento |
| --- | --- | --- | --- | --- |
| AJ-04 | Científico de datos senior (480.000.000 COP) | 24 persona-mes a 20.000.000 COP | Doctor en estancia posdoctoral: 24 meses a 12.920.000 COP (310.080.000 COP) | El numeral 9 exige un doctor en estancia posdoctoral y el numeral 14.4 fija su valor mensual |
| AJ-02 | Póliza todo riesgo de equipos | 50.000.000 COP en servicios técnicos | Se elimina del SGR | El numeral 14.3 excluye los seguros del apoyo del SGR |
| AJ-03 | Pólizas y garantías | 60.000.000 COP en otros rubros | Se elimina del SGR | El numeral 14.3 excluye los seguros del apoyo del SGR |
| AJ-05 | Administración (360.000.000 COP en otros rubros) | Un solo rubro de administración | Se separa en Administrativos (168.000.000 COP) y Seguimiento (192.000.000 COP), con el mismo total | Los numerales 12.2 y 14.3 exigen el rubro Seguimiento para la vigilancia del proyecto |
| AJ-01 | Reserva de contingencia | 636.000.000 COP como rubro del SGR | Se elimina como rubro; el riesgo se atiende con unidades de reserva, compuertas y programación | El numeral 12.2 no contempla la reserva como rubro y el numeral 14.3 exige justificar cada rubro con cotizaciones |
| AJ-06 | Contrapartida de la entidad territorial | Sin aporte (VACIO) | 120.000.000 COP en especie (PROPUESTO, pendiente de certificación) | El numeral 3 exige que cada integrante de la alianza aporte una contrapartida cuantificada en términos monetarios |

- AJ-07 TRL: de TRL 4 a 7 (ficha anterior) a TRL 4 a 8 con piso 7 al mes 19; los TdR valoran el TRL 8 con 8 puntos y el TRL 7 con 3; la evidencia es el ensayo independiente (S08) y la evaluación externa (S07) del mes 23.
- AJ-08 Productos: seis artículos de jóvenes, dos productos de maestría y uno de posdoctorado (9 documentos de investigación) en lugar de 2 artículos; cada persona entrega además un producto de divulgación (numeral 9).
- AJ-09 Alcance integral: se elimina el lenguaje de «opciones de ampliación» posteriores; el proyecto no depende de fases posteriores (numerales 1, 3 y 6).

## 6. Actividades, periodo y valor (17 actividades)

| N.º | Actividad | OE | Meses | Semanas (inicio–fin) | Holgura | SGR | Contrapartida |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Seleccionar los sitios y diseñar la colocalización | OE1 | M2–M3 | 8–12 | 2 | $ 65.430.000 | $ 34.375.000 |
| 1.2 | Adquirir y caracterizar el lote 1 de nodos y las referencias | OE1 | M4–M6 | 14–24 | 0 | $ 986.241.666 | $ 85.937.500 |
| 1.3 | Instalar el tramo 1, colocalizar y calibrar en el piloto | OE1 | M6–M10 | 24–40 | 0 | $ 566.328.000 | $ 137.500.000 |
| 1.4 | Entrenar y validar el modelo de corrección y decidir en la compuerta C1 | OE1 | M10–M12 | 40–50 | 0 | $ 273.575.000 | $ 85.937.500 |
| 1.5 | Reentrenar y verificar por departamento el tramo 2 y decidir en la compuerta C2 | OE1 | M15–M17 | 62–70 | 0 | $ 147.660.000 | $ 68.750.000 |
| 1.6 | Verificar el desempeño final y ejecutar el ensayo independiente | OE1 | M19–M23 | 82–98 | 0 | $ 407.680.000 | $ 137.500.000 |
| 1.7 | Administración y apoyo a la supervisión (objetivo específico 1) | OE1 | M1–M24 | 0–104 | 0 | $ 200.000.000 | $ 116.666.666 |
| 2.1 | Diseñar la arquitectura de enlace y energía | OE2 | M2–M4 | 8–14 | 0 | $ 391.200.000 | $ 0 |
| 2.2 | Desarrollar el firmware y la plataforma base (gemelo digital y tablero) | OE2 | M4–M6 | 14–24 | 0 | $ 792.000.000 | $ 800.000.000 |
| 2.3 | Instalar el tramo 2 | OE2 | M12–M15 | 50–62 | 0 | $ 1.364.490.667 | $ 105.000.000 |
| 2.4 | Instalar el tramo 3 | OE2 | M17–M19 | 70–82 | 0 | $ 1.238.234.667 | $ 105.000.000 |
| 2.5 | Administración y apoyo a la supervisión (objetivo específico 2) | OE2 | M1–M24 | 0–104 | 0 | $ 200.000.000 | $ 116.666.667 |
| 3.1 | Co-diseñar los umbrales y el protocolo de alerta con los comités | OE3 | M3–M9 | 12–36 | 12 | $ 468.248.276 | $ 132.413.794 |
| 3.2 | Poner en uso el tablero con los comités | OE3 | M12–M15 | 50–62 | 6 | $ 295.824.138 | $ 66.206.896 |
| 3.3 | Formar custodios y firmar los convenios por tramo | OE3 | M17–M20 | 70–86 | 12 | $ 466.565.518 | $ 88.275.862 |
| 3.4 | Transferir, cerrar y evaluar | OE3 | M23–M24 | 98–104 | 0 | $ 287.862.068 | $ 33.103.448 |
| 3.5 | Administración y apoyo a la supervisión (objetivo específico 3) | OE3 | M1–M24 | 0–104 | 0 | $ 200.000.000 | $ 116.666.667 |

Ruta crítica: 1.2, 1.3, 1.4, 1.5, 1.6, 2.1, 2.2, 2.3, 2.4 y 3.4 (más las compuertas C1 y C2 incluidas en 1.4 y 1.5) = 104 semanas. Con holgura: 1.1 (2 semanas), 3.1 (12), 3.2 (6), 3.3 (12). 1 mes = 52/12 semanas.

Hitos: H0 mes 2: Acta de inicio y contratación completa; H1 mes 4: Sitios del tramo 1 y diseño de enlace y energía listos; H2 mes 10: Colocalización del tramo 1 finalizada; H3 mes 12: Compuerta C1: modelo validado en el piloto; H4 mes 16: Tramo 2 instalado y verificado; H5 mes 17: Compuerta C2: uso institucional y desempeño; H6 mes 19: Tramo 3 instalado; H7 mes 23: Ensayo independiente y evaluación final; H8 mes 24: Transferencia y cierre del tramo 3; C3 mes 24: Compuerta C3: cierre y transferencia con evidencia del TRL 8

## 7. Talento humano de formación (numeral 9 y 14.4 de los TdR)

| Categoría | N | Duración | Mensual | Total | Vinculación | Productos |
| --- | --- | --- | --- | --- | --- | --- |
| Joven investigador e innovador (pregrado) | 6 | 12 meses | $ 2.000.000 | $ 144.000.000 | Cohorte A: meses 1 a 12 (3 personas). Cohorte B: meses 13 a 24 (3 personas). | Un artículo en formato publicable en revista A1, A2, B o C de Publindex y un producto de divulgación pública de la ciencia por persona. |
| Estudiante de maestría en modalidad de investigación | 2 | 24 meses | $ 4.350.000 | $ 304.800.000 | Dos personas, meses 1 a 24; matrícula hasta 48.000.000 COP por persona. | Un producto tipo TOP o tipo A sometido o publicado y un producto de divulgación pública de la ciencia por persona. |
| Doctor en estancia posdoctoral | 1 | 24 meses | $ 12.920.000 | $ 310.080.000 | Una persona, meses 1 a 24, sin vínculo laboral con las entidades de la alianza. | Un producto tipo TOP o tipo A, un producto de divulgación pública de la ciencia y un informe técnico final. |

Otro personal del equipo (SGR): ingenieros IoT y de campo (3), técnicos de campo departamentales (6), ingenieros de software y nube (2), ingeniero de firmware y energía (1), analista de datos espaciales y gemelo digital (1), especialista en metrología y calibración (1), profesional en calidad del aire y salud ambiental (1), coordinación de apropiación social (1), profesionales de apropiación social (2), profesional de convenios y custodia (1), gerencia de proyecto (1).

## 8. Productos MGA (sector 39, programa 3906)

| N.º | OE | Producto | Medido a través de | Indicador | Unidad | Meta |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | OE1 | Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos | Prototipos validados en condiciones reales | Prototipos funcionales validados (red de nodos y gateways con modelo de corrección) | Número | 1 sistema de 100 nodos y 10 gateways |
| 2 | OE1 | Documentos de investigación | Documentos de investigación elaborados | Documentos de investigación elaborados (6 de jóvenes, 2 de maestría y 1 de posdoctorado) | Número | 9 |
| 3 | OE1 | Servicio de apoyo financiero para la formación de maestría ya sea nacional o en el exterior, en la modalidad de investigación | Personas apoyadas con formación de maestría | Estudiantes de maestría en modalidad de investigación apoyados | Número | 2 |
| 4 | OE1 | Servicio de apoyo financiero de estancias de investigación | Estancias de investigación apoyadas | Doctores con estancia posdoctoral apoyados | Número | 1 |
| 5 | OE1 | Servicio de apoyo financiero para el fortalecimiento de las vocaciones científicas en CTI | Jóvenes investigadores e innovadores apoyados | Jóvenes investigadores e innovadores apoyados con beca-pasantía | Número | 6 |
| 6 | OE2 | Servicio de apoyo financiero para programas y proyectos de infraestructura científica y tecnológica | Infraestructura científica y tecnológica dotada | Equipos y plataforma de medición dotados y en operación (3 referencias, 100 nodos, 10 gateways y plataforma) | Número | 1 infraestructura integrada |
| 7 | OE3 | Documentos de política: Documentos de planeación | Documentos de planeación elaborados | Documentos de planeación elaborados (protocolo de alerta y plan de sostenibilidad con convenios de custodia) | Número | 2 |
| 8 | OE3 | Servicio de apropiación social del conocimiento | Actividades de apropiación social realizadas | Estrategias y actividades de apropiación social del conocimiento realizadas (20 talleres de co-diseño y 9 jornadas) | Número | 29 |
| 9 | OE3 | Servicio de Asistencia Técnica | Personas y entidades asistidas técnicamente | Personas de comités y custodios certificadas en el uso y la custodia de la red | Número | 60 personas y 15 comités |

## 9. Indicadores de resultado e impacto

| Cód. | Nivel | Indicador | Línea base | Meta |
| --- | --- | --- | --- | --- |
| R1 | Resultado | Error de medición frente a la referencia en los tres tramos | Se mide en el tramo 1 (mes 12) | R² ≥ 0,70 y NRMSE ≤ 30 % en 100 nodos al mes 24 |
| R2 | Resultado | Disponibilidad mensual de nodos | 0 % | ≥ 90 % y pérdida de paquetes ≤ 10 % al mes 24 |
| R3 | Resultado | Uso institucional del tablero y del protocolo | Sin uso documentado | ≥ 75 % al mes 24 |
| R4 | Resultado | Reducción relativa de falsas alarmas | Se mide en el tramo 1 | ≥ 30 % de reducción relativa |
| R5 | Resultado | Capacidad instalada en custodios | 0 | ≥ 60 personas certificadas |
| I1 | Impacto | Activación del protocolo ante superación de umbral | Sin protocolo | ≥ 80 % a los 12 meses posteriores al cierre |
| I2 | Impacto | Continuidad de la red bajo custodia | 0 | ≥ 70 % a los 12 meses posteriores al cierre |

Indicadores de gestión: 8 informes trimestrales de supervisión (meses 3, 6, 9, 12, 15, 18, 21, 24); ejecución presupuestal con desviación ≤ 5 % al cierre; cumplimiento de los hitos H0 a H8 y C3.

## 10. Riesgos (15)

| Id | Tipo | Riesgo | Probabilidad | Impacto | Respuesta |
| --- | --- | --- | --- | --- | --- |
| R-TEC-01 | Operacionales | La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10. | Probable (60 %) | Mayor | Modelo de corrección por humedad, banco de calibración y reposición de cabezales. |
| R-TEC-02 | Operacionales | Las baterías se agotan antes de 14 días sin sol y los nodos dejan de transmitir. | Improbable (30 %) | Mayor | Kits solares dimensionados, modo de bajo consumo y repuestos de batería. |
| R-TEC-03 | Operacionales | La red celular falla en el sitio y los gateways pierden el enlace con la nube. | Probable (40 %) | Mayor | Enlace satelital de respaldo y almacenamiento local de 7 días. |
| R-TEC-04 | Operacionales | El modelo de corrección no generaliza entre departamentos. | Improbable (35 %) | Mayor | Validación cruzada por departamento y reentrenamiento por tramo. |
| R-ORG-01 | Operacionales | Los comités de gestión del riesgo no adoptan el tablero ni el protocolo. | Probable (40 %) | Mayor | Co-diseño de umbrales, formación por comité y uso piloto con registro de decisiones. |
| R-ORG-02 | Operacionales | Los custodios no asumen la operación en el posproyecto. | Probable (50 %) | Mayor | Convenios por tramo, formación de custodios y cláusula de apertura. |
| R-EXT-01 | Operacionales | Deslizamientos o réplicas bloquean vías y retrasan la instalación. | Probable (50 %) | Moderado | Instalación en ventanas secas, técnicos locales y holgura en las actividades 1.1, 3.1, 3.2 y 3.3; las instalaciones de los tramos 2 y 3 se programan con acceso previamente verificado. |
| R-EXT-02 | Operacionales | Robo o vandalismo de nodos en sitios de remoción. | Probable (40 %) | Moderado | Cerramientos y mástiles protegidos, custodia local por sitio, 20 nodos y 1 gateway de reserva y convenio de custodia con la entidad territorial. |
| R-FIN-01 | De costos | La devaluación del peso encarece los equipos importados. | Probable (55 %) | Mayor | Compra por tramo con cotizaciones vigentes, orden de compra anticipada y cobertura cambiaria del proveedor; la contrapartida en efectivo cubre variaciones menores. |
| R-FIN-02 | Financieros | La contrapartida en especie no se certifica a tiempo. | Improbable (25 %) | Mayor | Certificación de la IES y de la empresa antes del acta de inicio. |
| R-JUR-01 | Legales | Una solicitud de patente de terceros afecta la libertad de operación. | Improbable (20 %) | Mayor | Análisis de libertad de operación y diseño alternativo del módulo afectado. |
| R-DAT-01 | Operacionales | Un incidente de ciberseguridad compromete la plataforma. | Improbable (20 %) | Mayor | Pruebas de penetración, segmentación y copias de respaldo. |
| R-ADM-01 | Administrativos | La contratación del equipo y la firma de los convenios de ejecución se demoran más de ocho semanas. | Improbable (30 %) | Mayor | Convenio marco previo con la IES y la empresa, plan de contratación con lista de elegibles y seguimiento semanal de la gerencia. |
| R-CAL-01 | De calendario | La importación y la nacionalización de un lote de equipos exceden doce semanas. | Improbable (35 %) | Mayor | Importación por lote con anticipación de la orden, agente aduanero contratado y lote de reserva de cabezales en el país. |
| R-SAN-01 | Sanitarios | El personal de campo se expone al polvo y a los escombros durante la instalación y el mantenimiento. | Improbable (30 %) | Moderado | Protocolo de seguridad y salud con respiradores N95, inducción previa y ventanas de trabajo fuera de la remoción activa. |

## 11. Alternativas (puntaje ponderado, escala 1 a 9; puntajes PROPUESTO)

Statu quo 4,475; estaciones fijas de referencia en los sitios 4,335; red con calibración centralizada en la nube 5,150; red híbrida con corrección en gateway por tramos y custodia distribuida 5,805. La ganadora no cambia con perturbaciones de ±10 % relativo en los pesos ni con perturbaciones de un solo peso entre −99 % y +500 %. Costo por punto de medición (millones de COP): statu quo 6,70; estaciones fijas 114,20 (7,2 veces ALT-03); nube 13,15; híbrida 15,90.

## 12. Datos que solo el usuario o los TdR pueden aportar (marcar con [Diligenciar: …])

Nombres de la IES, la empresa y la entidad territorial; categoría de cada entidad; código SIGP; nombres de los 12 municipios y centros poblados; resguardos; código de la demanda territorial (Anexo 4) o reportes oficiales de afectación; grupos de investigación (nombre, categoría A1/A/B/C, líneas, investigadores, estudiantes); artículos y programas de los planes de desarrollo; población afectada y objetivo con fuente DANE; experiencia de los integrantes (Anexo 5); cotizaciones; certificaciones de contrapartida; aval de ética si aplica; permisos.

## 13. Reglas de coherencia

1. Una cifra, una fuente: esta ficha. 2. Corrección en el gateway. 3. R² ≥ 0,70 y NRMSE ≤ 30 %; línea base medida en el tramo 1. 4. TRL 4 a 8 (piso 7 al mes 19). 5. 24 meses y 104 semanas. 6. 100 nodos y 10 gateways operativos; 120 y 11 comprados. 7. Valores según la sección 5. 8. Ninguna afirmación causal sobre salud: los resultados son técnicos, de adopción y de continuidad. 9. Ninguna probabilidad sin fuente en los árboles de decisión; las probabilidades de riesgo son estimaciones de formulación. 10. Sin reserva de contingencia ni seguros en el presupuesto.