%% PREFIJO: 8

# Capítulo 8. Presupuesto Detallado

Este capítulo presenta el presupuesto del proyecto por fuente, por rubro y por mes. Todas las cifras provienen del libro maestro del proyecto y coinciden con la ficha maestra. El valor solicitado al Sistema General de Regalías (SGR) es de 9.267.260.000 COP. La contrapartida es de 2.110.000.000 COP y el total del proyecto es de 11.377.260.000 COP. Los términos de referencia no se aportaron, por lo que los rubros siguen la estructura del metaprompt (SUPUESTO). Los costos unitarios no están respaldados por cotizaciones, y el anexo C reserva el espacio para ellas [DATO_USUARIO: cotizaciones vigentes de equipos].


## 8.1 Resumen Presupuestal

El presupuesto se construyó de abajo hacia arriba, actividad por actividad, y no desde el tope normativo. El expediente revisado declaraba un tope de 14.000.000.000 COP (DECLARADO, NO_VERIFICADO). La decisión DEC-F06 solicita la suma justificada, que equivale a 66,2 % del tope, y no el tope. La holgura de 4.732.740.000 COP no se presupuesta. Se describe como opciones de ampliación condicionadas a los términos de referencia: más nodos, un cuarto tramo o un año adicional de custodia. La {T:t01} desglosa el total por fuente de financiación y la {F:f01} lo ilustra.

:::TABLA t01 | Resumen por fuente de financiación
| Fuente | Modalidad | Valor (COP) | Porcentaje del total | Naturaleza |
| --- | --- | --- | --- | --- |
| SGR (MinCiencias) | Efectivo solicitado | $ 9.267.260.000 | 81,5 % | CALCULADO |
| Institución de educación superior ejecutora | Especie: personal e infraestructura | $ 1.100.000.000 | 9,7 % | DECLARADO |
| Empresa tecnológica aliada | Efectivo: logística y viáticos de emergencia | $ 210.000.000 | 1,8 % | DECLARADO |
| Empresa tecnológica aliada | Especie: infraestructura en la nube | $ 800.000.000 | 7,0 % | DECLARADO |
| Alcaldías de los municipios focalizados | Sin aporte | $ 0 | 0,0 % | VACIO |
| Total del proyecto |  | $ 11.377.260.000 | 100,0 % | CALCULADO |
:::NOTA *Nota.* Elaboración propia con datos de la ficha maestra §5. La contrapartida suma 2.110.000.000 COP (18,5 % del total). El desglose de la entidad ejecutora es PROPUESTO; las certificaciones de contrapartida están pendientes [DATO_USUARIO: certificaciones de la entidad ejecutora y de la empresa]. Decimales con coma.

:::FIGURA f01 | El SGR financia 81,5 % del proyecto y el personal absorbe 49,1 % de lo solicitado | Nota. Elaboración propia con datos de maestro.py (BUDGET y CONTRA). Izquierda: fuentes del total del proyecto; derecha: rubros del valor solicitado al SGR. Cada sector lleva trama y etiqueta directa. Python 3 y matplotlib; script c8_figs.py; sin semilla; corte del 13 de octubre de 2026.

La contrapartida cubre 18,5 % del total y no incluye aportes de las alcaldías. La exigencia de cofinanciación depende de los términos de referencia y del régimen del SGR (Congreso de la República, 2020), y ninguno de los dos se verificó. El aporte en especie de la empresa, 800 millones de pesos colombianos (COP), corresponde a infraestructura en la nube. Su valoración depende de una certificación contable que aún no existe. El riesgo R-FIN-02 describe esa dependencia, con probabilidad de 25 % y valor monetario esperado de 20,0 millones de COP.

Dos posiciones compiten sobre el nivel de la solicitud. La primera sostiene que un proyecto debe pedir el máximo permitido para absorber imprevistos. La segunda exige que cada peso solicitado tenga un beneficio marginal esperado mayor que su costo (Boardman et al., 2018). El proyecto adopta la segunda. Incluye una reserva de contingencia de 636.000.000 COP. Esa reserva equivale a la suma de los valores monetarios esperados de los 12 riesgos identificados, y no a un porcentaje arbitrario. El Project Management Institute [PMI] (2021) distingue la reserva para riesgos identificados de la reserva de gestión para riesgos desconocidos. Esta formulación solo constituye la primera, y la admisibilidad del rubro depende de los términos de referencia (VACIO).

La {T:t02} distribuye el valor solicitado por rubro y separa lo declarado en el expediente revisado de lo propuesto en esta formulación. Los valores declarados suman 4.144,7 millones de COP (44,7 %). Los valores propuestos y calculados suman 5.122,6 millones (55,3 %). Esa proporción muestra que la mayor parte del presupuesto requiere ratificación por cotización.

:::TABLA t02 | Distribución del valor solicitado al SGR por rubro y naturaleza del dato
| Rubro | Líneas | Valor (millones de COP) | Porcentaje del SGR | Declarado (millones de COP) | Propuesto o calculado (millones de COP) |
| --- | --- | --- | --- | --- | --- |
| Personal | 14 | 4.552,8 | 49,1 % | 2.008,8 | 2.544,0 |
| Equipos y software | 12 | 1.885,6 | 20,3 % | 1.200,0 | 685,6 |
| Materiales e insumos | 7 | 242,9 | 2,6 % | 140,9 | 102,0 |
| Servicios técnicos | 11 | 896,0 | 9,7 % | 209,0 | 687,0 |
| Viajes y viáticos | 5 | 462,0 | 5,0 % | 54,0 | 408,0 |
| Otros rubros | 6 | 592,0 | 6,4 % | 532,0 | 60,0 |
| Reserva de contingencia | 1 | 636,0 | 6,9 % | 0,0 | 636,0 |
| Total SGR | 56 | 9.267,3 | 100,0 % | 4.144,7 | 5.122,6 |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py. Declarado: valores del expediente E3. Propuesto o calculado: valores de esta formulación y la reserva de contingencia. Los porcentajes suman 100,0 % con redondeo. Decimales con coma.

La consecuencia metodológica es doble. Primero, la reserva y el personal propuesto concentran la incertidumbre de costo. Segundo, la ratificación del panel evaluador debe priorizar los rubros de personal y de equipos, que reúnen 69,4 % del valor solicitado. Las secciones siguientes detallan cada rubro con su justificación.


## 8.2 Personal

El rubro de personal suma 4.552,8 millones de COP, que equivalen a 49,1 % del valor solicitado. Incluye 14 líneas, 29 cargos y 624 persona-mes. Las líneas P01 a P06 son valores heredados del expediente revisado (2.008,8 millones). Las líneas P07 a P14 son propuestas de esta formulación (2.544,0 millones, 55,9 % del rubro). Esa composición exige ratificar las escalas de pago. Ninguna se verificó contra una tabla institucional [DATO_USUARIO: escala salarial y carga prestacional de la entidad ejecutora].

La estructura de cargos sigue los cuatro paquetes de trabajo. WP1 reúne 10 cargos para la medición verificada: seis jóvenes investigadores, dos estudiantes de maestría, un científico de datos senior y un especialista en metrología. WP2 reúne 13 cargos para la red, el software y el campo, incluidos seis técnicos departamentales. WP3 reúne cinco cargos para la apropiación, la calidad del aire y los convenios. WP0 tiene un cargo de gerencia. La investigación principal y los coinvestigadores no cargan al SGR, porque la entidad ejecutora los aporta como contrapartida en especie.

La {T:t03} detalla las 14 líneas de personal. Cada línea indica cantidad, costo unitario, paquete de trabajo y meses de dedicación.

:::TABLA t03 | Presupuesto de personal detallado
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses | Justificación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Jóvenes investigadores (6) | 72 persona-mes | $ 2.000.000 | $ 144.000.000 | DECLARADO | WP1 | 1–12 | Requisito de formación de talento; valor del expediente E3 tabla del expediente E3. |
| P02 | Estudiantes de maestría (2) | 48 persona-mes | $ 6.350.000 | $ 304.800.000 | DECLARADO | WP1 | 1–24 | Sostenimiento y matrícula; valor del expediente E3. |
| P03 | Científico de datos senior (1) | 24 persona-mes | $ 20.000.000 | $ 480.000.000 | DECLARADO | WP1 | 1–24 | Modelo de corrección y validación; valor E3. |
| P04 | Ingenieros IoT y de campo (3) | 72 persona-mes | $ 9.000.000 | $ 648.000.000 | DECLARADO | WP2 | 1–24 | Instalación y operación de la red; valor E3. |
| P05 | Coordinación de apropiación social (1) | 24 persona-mes | $ 8.000.000 | $ 192.000.000 | DECLARADO | WP3 | 1–24 | Escalera ASC niveles 1 a 4; valor E3. |
| P06 | Gerencia de proyecto (1) | 24 persona-mes | $ 10.000.000 | $ 240.000.000 | DECLARADO | WP0 | 1–24 | Seguimiento físico y financiero; valor E3. |
| P07 | Especialista en metrología y calibración (1) | 24 persona-mes | $ 12.000.000 | $ 288.000.000 | PROPUESTO | WP1 | 1–24 | Responsable de la trazabilidad frente a la referencia gravimétrica. |
| P08 | Ingenieros de software y nube (2) | 48 persona-mes | $ 9.500.000 | $ 456.000.000 | PROPUESTO | WP2 | 1–24 | Plataforma, gemelo digital y tablero. |
| P09 | Ingeniero de firmware y energía (1) | 24 persona-mes | $ 9.000.000 | $ 216.000.000 | PROPUESTO | WP2 | 1–24 | Autonomía de 14 días y modo de bajo consumo. |
| P10 | Técnicos de campo departamentales (6) | 144 persona-mes | $ 4.500.000 | $ 648.000.000 | PROPUESTO | WP2 | 1–24 | Dos por departamento; mantenimiento y reposición. |
| P11 | Profesionales de apropiación social (2) | 48 persona-mes | $ 6.000.000 | $ 288.000.000 | PROPUESTO | WP3 | 1–24 | Co-diseño con comités y comunidades. |
| P12 | Analista de datos espaciales y gemelo digital (1) | 24 persona-mes | $ 10.000.000 | $ 240.000.000 | PROPUESTO | WP2 | 1–24 | Modelo de estimación espacial y validación. |
| P13 | Profesional en calidad del aire y salud ambiental (1) | 24 persona-mes | $ 10.000.000 | $ 240.000.000 | PROPUESTO | WP3 | 1–24 | Umbrales locales del índice y protocolo de alerta. |
| P14 | Profesional de convenios y custodia (1) | 24 persona-mes | $ 7.000.000 | $ 168.000.000 | PROPUESTO | WP3 | 1–24 | Convenios por tramo, cláusula de apertura y propiedad intelectual. |
| Total | Subtotal de personal |  |  | $ 4.552.800.000 | CALCULADO |  |  | 49,1 % del valor solicitado al SGR |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (maestro.py, líneas del presupuesto SGR) y de la ficha maestra §5. DECLARADO: valor del expediente E3 sin verificación; PROPUESTO: decisión de esta formulación, sujeta a cotización y a ratificación; CALCULADO: producto de cantidad por costo unitario. Los costos unitarios no incluyen cotizaciones soportadas (VACIO).  Decimales con coma y miles con punto.

Las líneas de jóvenes investigadores y de estudiantes de maestría atienden un doble propósito. Proveen capacidad de trabajo y forman talento, que es un resultado del sistema nacional de ciencia, tecnología e innovación (Congreso de la República, 2009). Los jóvenes investigadores se concentran en los meses 1 a 12, porque su trabajo principal es la colocalización del piloto. Los estudiantes de maestría permanecen 24 meses y pueden producir una tesis asociada al segundo artículo. El costo mensual de la maestría, de 6.350.000 COP, incluye matrícula y sostenimiento según el expediente revisado.

La contrapartida de personal merece atención aparte, porque su certificación determina la viabilidad del aporte. La {T:t04} presenta las seis líneas de contrapartida. Las tres primeras corresponden a la dedicación del equipo investigador de la entidad ejecutora, que suma 800.000.000 COP. La cuarta valora el uso de laboratorios por 300.000.000 COP. Las dos últimas son aportes de la empresa tecnológica. Ningún valor está certificado todavía.

:::TABLA t04 | Contrapartida por línea, fuente y naturaleza del dato
| Id | Aporte | Fuente | Total (COP) | Naturaleza | Observación |
| --- | --- | --- | --- | --- | --- |
| C01 | Investigador principal, 50 % durante 24 meses | IES | $ 350.000.000 | DECLARADO | Valor E3, tabla del expediente E3; certificación de la IES pendiente. |
| C02 | Coinvestigador técnico, 30 % durante 24 meses | IES | $ 250.000.000 | DECLARADO | Valor E3, tabla del expediente E3. |
| C03 | Coinvestigadores de ambiente y ciencias sociales, 20 % | IES | $ 200.000.000 | PROPUESTO | Dos personas; valor sujeto a certificación de la IES. |
| C04 | Uso de laboratorios y equipos de la IES | IES | $ 300.000.000 | PROPUESTO | Laboratorio de calibración óptica; valor sujeto a certificación. |
| C05 | Aporte de la empresa tecnológica: logística y viáticos de emergencia | EMP | $ 210.000.000 | DECLARADO | Valor E3, tabla del expediente E3. |
| C06 | Infraestructura en la nube de la empresa | EMP | $ 800.000.000 | DECLARADO | Valor E3, tabla del expediente E3. |
| Total | Contrapartida del proyecto | IES y empresa | $ 2.110.000.000 | CALCULADO | 18,5 % del total del proyecto |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (CONTRA) y de la ficha maestra §5. IES: institución de educación superior ejecutora; EMP: empresa tecnológica aliada. Las certificaciones de las dos entidades están pendientes [DATO_USUARIO: certificados de aporte en especie]. Decimales con coma y miles con punto.

El valor de la dedicación de personal propio se estima como porcentaje de una remuneración mensual de referencia. Esa convención es habitual en proyectos con financiación pública, pero exige un certificado de la dirección financiera de cada entidad. Sin certificado, el aporte en especie se rechaza en la evaluación de viabilidad. Por esa razón la mitigación del riesgo R-FIN-02 exige certificar los aportes antes del acta de inicio.


## 8.3 Equipos y Software

El rubro de equipos y software suma 1.885,6 millones de COP, que equivalen a 20,3 % del valor solicitado. Incluye 12 líneas. Cinco de ellas son valores del expediente revisado y siete son propuestas de esta formulación. La {T:t05} presenta cada línea con su justificación técnica. La compra de nodos, cabezales y gateways se programa por tramo y no en bloque, y la {T:t06} muestra el valor liberado por cada compuerta.

:::TABLA t05 | Presupuesto de equipos y software
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses | Justificación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E01 | Nodos IoT de medición (100 + 20 de reserva) | 120 unidad | $ 4.500.000 | $ 540.000.000 | DECLARADO | WP2 | 1–24 | Compra por tramo: 36, 48 y 36 unidades; valor E3. |
| E02 | Cabezales ópticos de partículas | 150 unidad | $ 1.200.000 | $ 180.000.000 | DECLARADO | WP2 | 1–24 | Reposición por desgaste higroscópico; valor E3. |
| E03 | Monitores gravimétricos de referencia | 3 unidad | $ 85.000.000 | $ 255.000.000 | DECLARADO | WP1 | 4–6 | Uno por departamento para colocalización; valor E3. |
| E04 | Gateways con energía solar y respaldo (10 + 1 de reserva) | 11 unidad | $ 28.000.000 | $ 308.000.000 | PROPUESTO | WP2 | 1–24 | Aplican el modelo de corrección; compra por tramo: 4, 4 y 3. |
| E05 | Kits de energía solar y batería para nodos | 120 unidad | $ 650.000 | $ 78.000.000 | PROPUESTO | WP2 | 1–24 | Autonomía de 14 días sin sol. |
| E06 | Módulos de enlace satelital de respaldo | 10 unidad | $ 3.500.000 | $ 35.000.000 | PROPUESTO | WP2 | 3–24 | Enlace alterno ante falla celular. |
| E07 | Banco de calibración de laboratorio (cámara de humedad y generador de aerosol) | 1 unidad | $ 150.000.000 | $ 150.000.000 | PROPUESTO | WP1 | 3–5 | Caracterización previa de cada lote de cabezales. |
| E08 | Estaciones de trabajo para entrenamiento de modelos | 2 unidad | $ 25.000.000 | $ 50.000.000 | PROPUESTO | WP1 | 1–3 | Entrenamiento y validación del modelo de corrección. |
| E09 | Equipos de campo e instrumentación (lote) | 1 lote | $ 30.000.000 | $ 30.000.000 | PROPUESTO | WP2 | 1–3 | Herramientas, medidores y repuestos de uso general. |
| E10 | Instancias en la nube reservadas (24 meses) | 1 clúster | $ 180.000.000 | $ 180.000.000 | DECLARADO | WP2 | 1–24 | Gemelo digital, base de datos y tablero; valor E3. |
| E11 | Software de analítica y repositorios | 1 paquete | $ 45.000.000 | $ 45.000.000 | DECLARADO | WP2 | 1–24 | Entorno seguro de desarrollo y control de versiones; valor E3. |
| E12 | Planes de datos celulares M2M para gateways (12 SIM, 24 meses) | 288 SIM-mes | $ 120.000 | $ 34.560.000 | PROPUESTO | WP2 | 1–24 | Solo los gateways transmiten por red celular. |
| Total | Subtotal de equipos y software |  |  | $ 1.885.560.000 | CALCULADO |  |  | 20,3 % del valor solicitado al SGR |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (maestro.py, líneas del presupuesto SGR) y de la ficha maestra §5. DECLARADO: valor del expediente E3 sin verificación; PROPUESTO: decisión de esta formulación, sujeta a cotización y a ratificación; CALCULADO: producto de cantidad por costo unitario. Los costos unitarios no incluyen cotizaciones soportadas (VACIO).  Decimales con coma y miles con punto.

La justificación técnica descansa en tres decisiones de diseño. La primera es el uso de sensores ópticos de bajo costo para PM2,5 y PM10. Esos sensores responden a la humedad relativa y a la fracción gruesa (Jayaratne et al., 2018; Malings et al., 2020), y su desempeño depende del sitio (Giordano et al., 2021). La segunda decisión es la colocalización con tres monitores gravimétricos de referencia, uno por departamento. Ese diseño sigue los protocolos de desempeño para sensores de partículas finas (U.S. Environmental Protection Agency [EPA], 2021). La tercera es la corrección en el gateway, que desplaza el cómputo hacia el borde de la red (Shi et al., 2016).

La arquitectura de comunicación explica las líneas de gateways, satélite y datos celulares. Los nodos hoja transmiten por LoRa, una tecnología de largo alcance y bajo consumo (Adelantado et al., 2017). Cada gateway reenvía por red celular y cuenta con un enlace satelital alterno y almacenamiento local de siete días. El costo de esa redundancia, 35.000.000 COP en módulos y 55.000.000 COP en planes satelitales, equivale a 1,0 % del valor solicitado. La redundancia responde al riesgo R-TEC-03, la falla de la red celular en el sitio, que tiene probabilidad de 40 %.

La línea E10 financia las instancias en la nube que alojan el gemelo digital. Un gemelo digital es una representación computacional que se actualiza con datos del sistema físico y permite simular su estado (Grieves y Vickers, 2017; Tao et al., 2019). En este proyecto estima la distribución espacial de PM2,5 y PM10 entre los nodos. El aporte en especie de la empresa, 800.000.000 COP en infraestructura en la nube, complementa la línea E10 y no la sustituye. La separación entre ambas debe constar en el convenio para evitar que el mismo servicio se cuente dos veces.

:::TABLA t06 | Compras de nodos, gateways y cabezales por tramo y compuerta que las libera
| Tramo | Mes de compra | Nodos | Gateways | Cabezales | Valor (millones de COP) | Decisión que libera la compra |
| --- | --- | --- | --- | --- | --- | --- |
| Tramo 1 | 5 | 36 | 4 | 50 | 334,0 | Acta de inicio y contratación (H0) |
| Tramo 2 | 13 | 48 | 4 | 50 | 388,0 | Compuerta C1 (mes 12) |
| Tramo 3 | 18 | 36 | 3 | 50 | 306,0 | Compuerta C2 (mes 17) |
| Total |  | 120 | 11 | 150 | 1.028,0 |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (TRAMOS y líneas E01, E02 y E04). Costos unitarios: nodo 4,5 millones; cabezal 1,2 millones; gateway 28,0 millones de COP. Se compran 120 nodos para operar 100, y 11 gateways para operar 10. Decimales con coma.

La {T:t06} muestra que el proyecto compromete 334,0 millones de COP en equipos del tramo 1 antes de cualquier evidencia de desempeño. Libera 388,0 y 306,0 millones solo tras las compuertas C1 y C2. Esa estructura limita la exposición ante un fallo del modelo de corrección. Si C1 no se aprueba, el proyecto detiene 694,0 millones de COP en compras. Esa suma equivale a 67,5 % de las compras de nodos, cabezales y gateways. Collingridge (1980) describe el dilema: la tecnología es fácil de cambiar al inicio, cuando se sabe poco de ella. La compra por tramos conserva esa facilidad el mayor tiempo posible.


## 8.4 Materiales e Insumos

El rubro de materiales e insumos suma 242,9 millones de COP, que equivalen a 2,6 % del valor solicitado. Incluye siete líneas. Cinco son valores del expediente revisado y dos son propuestas. La línea M02 sustituye los gases patrón que el expediente incluía, porque los gases patrón calibran analizadores de gases y no sensores de material particulado. El polvo de ensayo normalizado y los consumibles del banco de calibración cumplen la función correcta. La {T:t07} presenta las líneas.

:::TABLA t07 | Presupuesto de materiales e insumos
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses | Justificación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M01 | Filtros de membrana PTFE para gravimetría | 1.200 unidad | $ 12.000 | $ 14.400.000 | DECLARADO | WP1 | 3–24 | Validación gravimétrica; valor E3. |
| M02 | Polvo de ensayo normalizado y consumibles del banco de calibración | 15 lote | $ 2.800.000 | $ 42.000.000 | PROPUESTO | WP1 | 1–24 | Sustituye los gases patrón del expediente E3, que no aplican a partículas. |
| M03 | Cerramientos NEMA 4X y mástiles para nodos | 120 unidad | $ 350.000 | $ 42.000.000 | DECLARADO | WP2 | 1–24 | Protección contra intemperie; valor E3. |
| M04 | Cartillas impresas del índice y del protocolo de alerta | 5.000 unidad | $ 8.500 | $ 42.500.000 | DECLARADO | WP3 | 3–24 | Población sin acceso a internet; valor E3. |
| M05 | Kits de papelería para talleres de co-diseño | 20 kit | $ 1.500.000 | $ 30.000.000 | DECLARADO | WP3 | 2–24 | Mesas de co-creación; valor E3. |
| M06 | Elementos de protección personal (mascarillas N95) | 3.000 unidad | $ 4.000 | $ 12.000.000 | DECLARADO | WP3 | 1–24 | Bioseguridad en campo; valor E3. |
| M07 | Repuestos y consumibles de mantenimiento (baterías, cables, conectores) | 1 lote | $ 60.000.000 | $ 60.000.000 | PROPUESTO | WP2 | 3–24 | Existencias de reposición en cada departamento. |
| Total | Subtotal de materiales e insumos |  |  | $ 242.900.000 | CALCULADO |  |  | 2,6 % del valor solicitado al SGR |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (maestro.py, líneas del presupuesto SGR) y de la ficha maestra §5. DECLARADO: valor del expediente E3 sin verificación; PROPUESTO: decisión de esta formulación, sujeta a cotización y a ratificación; CALCULADO: producto de cantidad por costo unitario. Los costos unitarios no incluyen cotizaciones soportadas (VACIO).  Decimales con coma y miles con punto.

Los filtros de membrana de politetrafluoroetileno (PTFE) permiten la medición gravimétrica de referencia. Se programan 1.200 unidades para 240 análisis de laboratorio acreditado (línea S01 del rubro de servicios). Resultan cinco filtros por muestra analizada, entre pesajes, blancos y repeticiones. Esa proporción es PROPUESTO. Las cartillas impresas, 5.000 unidades, atienden a población sin acceso a internet en los municipios focalizados. Cada cartilla cuesta 8.500 COP y presenta el índice y el protocolo de alerta.

Las mascarillas N95 protegen al personal de campo y a los asistentes a talleres, y cumplen una función de bioseguridad. La Organización Mundial de la Salud (OMS, 2021) fija guías de calidad del aire para PM2,5 y PM10. Esas guías justifican proteger a quien trabaja en sitios de remoción. El proyecto no afirma, sin embargo, que las mascarillas reduzcan un efecto en salud medido. Son una medida de precaución para el equipo. La consecuencia es que el indicador de impacto del proyecto no depende de ellas.


## 8.5 Servicios Técnicos

El rubro de servicios técnicos suma 896,0 millones de COP, que equivalen a 9,7 % del valor solicitado. Incluye 11 líneas. Cuatro de ellas verifican el desempeño o auditan el sistema. Son el análisis gravimétrico, la evaluación externa independiente, el ensayo con laboratorio externo y la auditoría de ciberseguridad. La {T:t08} presenta el detalle.

:::TABLA t08 | Presupuesto de servicios técnicos
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses | Justificación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Análisis gravimétrico en laboratorio acreditado | 240 muestra | $ 350.000 | $ 84.000.000 | DECLARADO | WP1 | 3–24 | Lectura certificada de filtros; valor E3. |
| S02 | Consultoría jurídica en propiedad intelectual y libertad de operación | 150 hora | $ 300.000 | $ 45.000.000 | DECLARADO | WP3 | 1–24 | Solicitudes PCT con Colombia designada; valor E3. |
| S03 | Auditoría externa de ciberseguridad | 2 servicio | $ 15.000.000 | $ 30.000.000 | DECLARADO | WP2 | 8–24 | Dos pruebas de penetración; valor E3. |
| S04 | Póliza todo riesgo de equipos | 2 prima anual | $ 25.000.000 | $ 50.000.000 | DECLARADO | WP0 | 1–24 | Robo y daño climático; valor E3. |
| S05 | Instalación en sitio, mástiles y obra menor (100 nodos y 10 gateways) | 110 sitio | $ 1.200.000 | $ 132.000.000 | PROPUESTO | WP2 | 3–24 | Ejecución por tramo. |
| S06 | Estudio de cobertura y de enlace en tres departamentos | 3 estudio | $ 20.000.000 | $ 60.000.000 | PROPUESTO | WP2 | 1–4 | Presupuesto de enlace de los gateways. |
| S07 | Evaluación externa independiente (meses 12 y 24) | 2 evaluación | $ 60.000.000 | $ 120.000.000 | PROPUESTO | WP0 | 12–24 | Verificación de resultados frente a la línea base. |
| S08 | Ensayo de desempeño con laboratorio externo | 1 campaña | $ 90.000.000 | $ 90.000.000 | PROPUESTO | WP1 | 20–24 | Verificación independiente del cumplimiento de los umbrales. |
| S09 | Formación y soporte a custodios por tramo | 3 tramo | $ 50.000.000 | $ 150.000.000 | PROPUESTO | WP3 | 6–24 | Capacidad de absorción de los custodios. |
| S10 | Planes de enlace satelital de respaldo (10 módulos, 22 meses) | 220 módulo-mes | $ 250.000 | $ 55.000.000 | PROPUESTO | WP2 | 3–24 | Datos de respaldo. |
| S11 | Importación y nacionalización de equipos | 1 servicio | $ 80.000.000 | $ 80.000.000 | PROPUESTO | WP0 | 1–18 | Tres lotes de importación. |
| Total | Subtotal de servicios técnicos |  |  | $ 896.000.000 | CALCULADO |  |  | 9,7 % del valor solicitado al SGR |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (maestro.py, líneas del presupuesto SGR) y de la ficha maestra §5. DECLARADO: valor del expediente E3 sin verificación; PROPUESTO: decisión de esta formulación, sujeta a cotización y a ratificación; CALCULADO: producto de cantidad por costo unitario. Los costos unitarios no incluyen cotizaciones soportadas (VACIO).  Decimales con coma y miles con punto.

Las líneas de verificación externa cumplen una función de control que la ejecución interna no puede cumplir. La evaluación externa de los meses 12 y 24 y el ensayo con laboratorio externo suman 210.000.000 COP. Estos servicios producen la evidencia independiente que respalda las compuertas y la afirmación de desempeño. Patton (2011) propone la evaluación orientada al desarrollo para proyectos de innovación con incertidumbre. Esa lógica sustenta la evaluación del mes 12, antes de la compuerta C1.

La consultoría jurídica en propiedad intelectual, con 150 horas por 45.000.000 COP, atiende el riesgo R-JUR-01. El análisis de libertad de operación examina si solicitudes de patente de terceros afectan el diseño. La Decisión 486 regula el régimen común de propiedad industrial y sustenta ese análisis en Colombia (Comunidad Andina, 2000). La auditoría de ciberseguridad cubre dos pruebas de penetración. Debe también verificar el cumplimiento de la Ley 1581 de 2012 sobre protección de datos personales (Congreso de la República, 2012b). Las lecturas pueden asociarse con ubicaciones de viviendas y trabajadores.

La línea S11, importación y nacionalización, suma 80.000.000 COP y atiende tres lotes. El riesgo financiero R-FIN-01, la devaluación del peso, tiene el mayor valor monetario esperado del registro, 165,0 millones de COP. La mitigación combina compra por tramos, cobertura cambiaria y cotizaciones vigentes. Las líneas E01 a E04 suman 1.283,0 millones de COP. Si se importaran en su totalidad (SUPUESTO), una devaluación de 10 % las encarecería en 128,3 millones. La reserva cubre esa cifra solo en parte.


## 8.6 Viajes y Viáticos

El rubro de viajes y viáticos suma 462,0 millones de COP, que equivalen a 5,0 % del valor solicitado. Incluye cinco líneas. Tres de ellas, propuestas por esta formulación, cubren el trabajo de campo en tres departamentos: tiquetes, viáticos y vehículos 4x4. Su valor suma 408,0 millones de COP. El expediente revisado asignaba menos recursos a este rubro. La ampliación obedece a que la red cubre Caldas, Cundinamarca y Valle del Cauca. La {T:t09} detalla las líneas.

:::TABLA t09 | Presupuesto de viajes y viáticos
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses | Justificación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Tiquetes aéreos nacionales | 150 trayecto | $ 600.000 | $ 90.000.000 | PROPUESTO | WP2 | 1–24 | Ampliado respecto del expediente E3 por cubrir tres departamentos. |
| V02 | Viáticos de alojamiento y manutención | 600 día-persona | $ 350.000 | $ 210.000.000 | PROPUESTO | WP2 | 1–24 | Instalación, mantenimiento y talleres. |
| V03 | Arrendamiento de vehículos 4x4 | 240 día | $ 450.000 | $ 108.000.000 | PROPUESTO | WP2 | 1–24 | Acceso a sitios sin vía pavimentada. |
| V04 | Viaje internacional para divulgación científica | 2 viaje | $ 12.000.000 | $ 24.000.000 | DECLARADO | WP3 | 14–24 | Presentación de resultados; valor E3. |
| V05 | Alimentación de laboratorios ciudadanos | 20 evento | $ 1.500.000 | $ 30.000.000 | DECLARADO | WP3 | 2–24 | Participación comunitaria; valor E3. |
| Total | Subtotal de viajes y viáticos |  |  | $ 462.000.000 | CALCULADO |  |  | 5,0 % del valor solicitado al SGR |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (maestro.py, líneas del presupuesto SGR) y de la ficha maestra §5. DECLARADO: valor del expediente E3 sin verificación; PROPUESTO: decisión de esta formulación, sujeta a cotización y a ratificación; CALCULADO: producto de cantidad por costo unitario. Los costos unitarios no incluyen cotizaciones soportadas (VACIO).  Decimales con coma y miles con punto.

El trabajo de campo comprende instalación, mantenimiento, colocalización y talleres en 12 municipios, cuatro por departamento [DATO_USUARIO: lista de municipios]. Los 600 días-persona de viáticos equivalen a 25 días-persona por mes durante 24 meses. Esa cifra es una estimación gruesa, porque la carga real depende del calendario de instalación. La programación de viajes debe revisarse con el cronograma de cada tramo.

Las dos líneas del expediente revisado, el viaje internacional de divulgación y la alimentación de laboratorios ciudadanos, suman 54,0 millones de COP. El viaje internacional de divulgación sustenta el producto de nuevo conocimiento. La alimentación de laboratorios ciudadanos apoya la participación de las comunidades. Su vínculo con la escalera de participación de Arnstein (1969) se desarrolla en el capítulo 16. El proyecto no presupuesta viajes fuera de esas dos líneas.


## 8.7 Otros Rubros

El rubro de otros rubros suma 592,0 millones de COP, que equivalen a 6,4 % del valor solicitado. Incluye seis líneas que no encajan en los rubros anteriores: publicaciones, eventos, propiedad intelectual, pólizas y administración. La {T:t10} las presenta.

:::TABLA t10 | Presupuesto de otros rubros
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses | Justificación |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| O01 | Cargos de procesamiento de artículos de acceso abierto | 2 artículo | $ 12.500.000 | $ 25.000.000 | DECLARADO | WP3 | 14–24 | Dos artículos Q1 o Q2; valor E3 (sin duplicar en servicios). |
| O02 | Logística de ferias y laboratorios de apropiación | 9 evento | $ 8.000.000 | $ 72.000.000 | DECLARADO | WP3 | 4–24 | Espacios, pantallas y moderación; valor E3. |
| O03 | Registro ante la DNDA y asesoría de propiedad intelectual | 1 paquete | $ 15.000.000 | $ 15.000.000 | DECLARADO | WP3 | 12–24 | Registro del software; valor E3. |
| O04 | Pólizas y garantías del SGR | 2 prima anual | $ 30.000.000 | $ 60.000.000 | DECLARADO | WP0 | 1–24 | Cumplimiento, anticipo y responsabilidad civil; valor E3. |
| O05 | Administración (revisoría y plataforma de seguimiento) | 24 mes | $ 15.000.000 | $ 360.000.000 | DECLARADO | WP0 | 1–24 | Valor E3; el tope porcentual de administración no se verificó. |
| O06 | Publicaciones de divulgación y eventos de socialización | 1 paquete | $ 60.000.000 | $ 60.000.000 | PROPUESTO | WP3 | 6–24 | Piezas audiovisuales y jornadas de cierre. |
| Total | Subtotal de otros rubros |  |  | $ 592.000.000 | CALCULADO |  |  | 6,4 % del valor solicitado al SGR |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (maestro.py, líneas del presupuesto SGR) y de la ficha maestra §5. DECLARADO: valor del expediente E3 sin verificación; PROPUESTO: decisión de esta formulación, sujeta a cotización y a ratificación; CALCULADO: producto de cantidad por costo unitario. Los costos unitarios no incluyen cotizaciones soportadas (VACIO).  Decimales con coma y miles con punto.

La administración suma 360.000.000 COP, que equivalen a 3,9 % del valor solicitado. El expediente revisado declaraba un tope porcentual de 5 %, que no se verificó. Si el tope existe y se mantiene, el proyecto queda por debajo. Si los términos de referencia fijan un tope menor, la línea O05 debe recalcularse. La línea O04, pólizas y garantías del SGR, suma 60.000.000 COP y cubre cumplimiento, anticipo y responsabilidad civil. La Ley 2056 de 2020 regula la organización y el funcionamiento del SGR y es el marco de referencia de esas garantías (Congreso de la República, 2020).

Las líneas O01, O03 y O06 apoyan la propiedad intelectual y la divulgación. Teece (1986) argumenta que el valor de una innovación depende de los activos complementarios y de los regímenes de apropiación. El registro del software ante la Dirección Nacional de Derecho de Autor (15.000.000 COP) protege el modelo de corrección y el gemelo digital. El acceso abierto de los artículos (25.000.000 COP) difunde el protocolo de calibración. Esa combinación es deliberada. Protege el software que la entidad ejecutora debe sostener y abre el conocimiento que otras redes pueden reutilizar.


## 8.8 Flujo de Caja

El flujo de caja distribuye el presupuesto en el tiempo según el calendario de cada línea. Las líneas de personal y de servicios se reparten de forma uniforme entre su mes inicial y su mes final. Las compras de nodos, cabezales y gateways se concentran en los meses 5, 13 y 18, que corresponden a los tres tramos. La {T:t11} presenta el flujo por trimestre y la {F:f02} muestra la ejecución acumulada.

:::TABLA t11 | Flujo de caja trimestral del SGR y de la contrapartida
| Trimestre | SGR (millones de COP) | Contrapartida (millones de COP) | Total (millones de COP) | SGR acumulado |
| --- | --- | --- | --- | --- |
| T1 (meses 1 a 3) | 1.048,9 | 263,7 | 1.312,7 | 11,3 % |
| T2 (meses 4 a 6) | 1.640,3 | 263,7 | 1.904,1 | 29,0 % |
| T3 (meses 7 a 9) | 962,0 | 263,7 | 1.225,7 | 39,4 % |
| T4 (meses 10 a 12) | 974,1 | 263,7 | 1.237,9 | 49,9 % |
| T5 (meses 13 a 15) | 1.355,8 | 263,7 | 1.619,5 | 64,5 % |
| T6 (meses 16 a 18) | 1.278,3 | 263,7 | 1.542,0 | 78,3 % |
| T7 (meses 19 a 21) | 994,9 | 263,7 | 1.258,7 | 89,1 % |
| T8 (meses 22 a 24) | 1.012,9 | 263,7 | 1.276,7 | 100,0 % |
| Total | 9.267,3 | 2.110,0 | 11.377,3 | 100,0 % |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (flujo_sgr y flujo_contra). La contrapartida se distribuye de forma uniforme en 24 meses. El flujo semestral del SGR es 2.689,3; 1.936,1; 2.634,1 y 2.007,8 millones de COP. Naturaleza: CALCULADO. Decimales con coma.

:::FIGURA f02 | El SGR se ejecuta 49,9 % hasta la compuerta C1 y 71,5 % hasta C2 | Nota. Elaboración propia con datos de maestro.py (flujo_sgr y flujo_contra). Ejecución acumulada mensual en porcentaje del valor de cada fuente; líneas verticales: compuertas C1 (mes 12) y C2 (mes 17). Python 3 y matplotlib; script c8_figs.py; sin semilla; corte del 13 de octubre de 2026.

La curva de ejecución del SGR alcanza 49,9 % en el mes 12 y 71,5 % en el mes 17. La compra del tramo 2 en el mes 13 produce un salto de 7,6 puntos porcentuales. La del tramo 3 en el mes 18 produce un salto de 6,8 puntos. La contrapartida avanza de forma lineal. El desembolso concentra por tanto casi la mitad de los recursos antes de la primera compuerta de decisión. Esa concentración proviene de personal y servicios iniciales, que no dependen de las compuertas, y de la compra del tramo 1.

La {F:f03} presenta el desembolso mensual del SGR por grupo de rubros. Los tres picos de los meses 5, 13 y 18 alcanzan 777,4; 707,6 y 630,1 millones de COP. Corresponden a las compras de cada tramo. El resto de los meses oscila entre 320 y 460 millones, con un núcleo estable de personal. La tabla de desembolsos condicionados fija qué sucede con cada pico si una compuerta no se aprueba.

:::FIGURA f03 | Tres picos de desembolso coinciden con las compras de los tramos 1, 2 y 3 (meses 5, 13 y 18) | Nota. Elaboración propia con datos de maestro.py (flujo_sgr). Desembolso mensual del SGR por grupo de rubros, en millones de COP; trama y etiqueta directa en los picos. Python 3 y matplotlib; script c8_figs.py; sin semilla; corte del 13 de octubre de 2026.

La {T:t12} traduce el flujo en hitos de desembolso. Cada hito indica el mes, el valor acumulado liberado y la condición de liberación. El financiador define el esquema real de desembolsos, que los términos de referencia no precisan [DATO_USUARIO: esquema de desembolsos del financiador].

:::TABLA t12 | Hitos de desembolso del SGR y condición de liberación
| Hito de desembolso | Mes | SGR acumulado (millones de COP) | Porcentaje del SGR | Condición de liberación |
| --- | --- | --- | --- | --- |
| Anticipo y acta de inicio (H0) | 2 | 652,3 | 7,0 % | Contratos, convenios y plan de trabajo aprobados |
| Compra del tramo 1 | 5 | 2.284,8 | 24,7 % | Diseño de enlace y energía listo (H1); pólizas vigentes |
| Compuerta C1 (H3) | 12 | 4.625,4 | 49,9 % | Modelo validado: R² de 0,70 o más y NRMSE de 30 % o menos; 50 % o más de los comités usa el tablero |
| Compra del tramo 2 | 13 | 5.333,0 | 57,5 % | C1 aprobada: 388,0 millones de COP en nodos, gateways y cabezales |
| Compuerta C2 (H5) | 17 | 6.629,3 | 71,5 % | Umbrales en tres departamentos, disponibilidad de 90 % o más y convenios de custodia con partida |
| Compra del tramo 3 | 18 | 7.259,4 | 78,3 % | C2 aprobada: 306,0 millones de COP en nodos, gateways y cabezales |
| Cierre y transferencia (H8) | 24 | 9.267,3 | 100,0 % | Actas de entrega a custodios y cláusula de apertura firmada |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py y de la ficha maestra §4 y §6. Los valores acumulados son CALCULADOS al cierre de cada mes. Las condiciones de liberación son PROPUESTO y se ajustan al esquema que fije el financiador. Decimales con coma.

El esquema propuesto vincula los desembolsos con evidencias y no con fechas. Cooper (2008) describe este diseño como compuertas con criterios explícitos que autorizan la inversión de la etapa siguiente. El proyecto adopta tres compuertas y cada una libera una compra. La contrapartida es administrativa: el financiador debe aceptar un desembolso condicionado, y el cronograma debe absorber dos semanas de decisión por compuerta. La ruta crítica incluye esas dos semanas. El capítulo 21 resume el presupuesto para el acta de constitución.
