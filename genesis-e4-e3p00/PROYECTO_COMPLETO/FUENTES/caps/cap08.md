%% PREFIJO: 8
# Capítulo 8. Presupuesto detallado

El presupuesto del proyecto se construye línea por línea a partir de los datos maestros. Cada línea tiene concepto, cantidad, costo unitario, naturaleza, paquete de trabajo y meses de ejecución. Ninguna cifra se redondea antes de sumar. El resultado es un valor solicitado al Sistema General de Regalías (SGR) de 9.267.260.000 pesos colombianos (COP). La contrapartida es de 2.110.000.000 COP y el total es de 11.377.260.000 COP. El valor solicitado equivale a 66,2 % del tope declarado de 14.000.000.000 COP. Los términos de referencia no se aportaron, de modo que el tope y la admisibilidad de cada rubro quedan como NO_VERIFICADO.

Las cifras tienen dos naturalezas. Las declaradas proceden del expediente E3-P00 y suman 4.144,7 millones de COP. Las propuestas son decisiones de esta formulación y suman 4.486,6 millones. La reserva de contingencia, calculada, aporta 636,0 millones. No existen cotizaciones formales. Las cotizaciones por proveedor son [DATO_USUARIO: cotizaciones vigentes de equipos, servicios y software]. Por eso el presupuesto es una estimación de formulación con trazabilidad completa, no una oferta de proveedores.

## 8.1 Resumen presupuestal

### 8.1.1 Fuentes de financiación

El análisis costo-beneficio distingue entre el costo para quien financia y el costo total de la intervención (Boardman et al., 2018). Esa distinción orienta el resumen. La {T:t01} separa cuatro fuentes. Son el valor solicitado al SGR, la contrapartida de la institución de educación superior, la contrapartida de la empresa y el aporte de las alcaldías. El SGR financia 81,5 % del proyecto y la contrapartida financia 18,5 %. Las alcaldías no declaran aporte, y ese vacío se mantiene visible en la tabla.

:::TABLA t01 | Resumen presupuestal por fuente de financiación
| Fuente | Componente | Valor (COP) | % de la fuente | % del total | Naturaleza |
| --- | --- | --- | --- | --- | --- |
| SGR | Personal | 4.552.800.000 | 49,1 | 40,0 | DECLARADO y PROPUESTO |
| SGR | Equipos y software | 1.885.560.000 | 20,3 | 16,6 | DECLARADO y PROPUESTO |
| SGR | Materiales e insumos | 242.900.000 | 2,6 | 2,1 | DECLARADO y PROPUESTO |
| SGR | Servicios técnicos | 896.000.000 | 9,7 | 7,9 | DECLARADO y PROPUESTO |
| SGR | Viajes y viáticos | 462.000.000 | 5,0 | 4,1 | DECLARADO y PROPUESTO |
| SGR | Otros rubros | 592.000.000 | 6,4 | 5,2 | DECLARADO y PROPUESTO |
| SGR | Reserva de contingencia | 636.000.000 | 6,9 | 5,6 | CALCULADO |
| SGR | Subtotal solicitado al SGR | 9.267.260.000 | 100,0 | 81,5 | CALCULADO |
| Contrapartida IES | C01 Investigador principal, 50 % durante 24 meses (en especie) | 350.000.000 | 16,6 | 3,1 | DECLARADO |
| Contrapartida IES | C02 Coinvestigador técnico, 30 % durante 24 meses (en especie) | 250.000.000 | 11,8 | 2,2 | DECLARADO |
| Contrapartida IES | C03 Coinvestigadores de ambiente y ciencias sociales, 20 % (en especie) | 200.000.000 | 9,5 | 1,8 | PROPUESTO |
| Contrapartida IES | C04 Uso de laboratorios y equipos de la IES (en especie) | 300.000.000 | 14,2 | 2,6 | PROPUESTO |
| Contrapartida empresa | C05 Aporte de la empresa tecnológica: logística y viáticos de emergencia (en efectivo) | 210.000.000 | 10,0 | 1,8 | DECLARADO |
| Contrapartida empresa | C06 Infraestructura en la nube de la empresa (en especie) | 800.000.000 | 37,9 | 7,0 | DECLARADO |
| Alcaldías | Sin aporte declarado | 0 | 0,0 | 0,0 | VACIO |
| Contrapartida | Subtotal de contrapartida | 2.110.000.000 | 100,0 | 18,5 | DECLARADO y PROPUESTO |
| Proyecto | Total del proyecto | 11.377.260.000 | — | 100,0 | CALCULADO |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (resumen, BUDGET y CONTRA) y de la ficha maestra §5. Los aportes de contrapartida están pendientes de certificación. Los porcentajes se redondean a un decimal y pueden no sumar 100,0. Valores en COP, miles con punto.

La contrapartida se concentra en dos fuentes. La institución de educación superior aporta 1.100,0 millones de COP, equivalentes a 52,1 % de la contrapartida. Casi todo es en especie: tiempo de investigadores y uso de laboratorios. La empresa aporta 1.010,0 millones, entre 210,0 millones en efectivo para logística y 800,0 millones en especie para infraestructura de nube. Los aportes en especie exigen certificación de valoración, un requisito que el riesgo R-FIN-02 vigila. Sin esa certificación, la contrapartida efectiva baja y el proyecto pierde la proporción que la convocatoria pueda exigir.

### 8.1.2 Distribución por rubro y holgura

La {F:f01} muestra cómo se reparte el valor solicitado. Personal reúne 49,1 % del SGR, con 4.552,8 millones de COP. Equipos y software reúne 20,3 %, con 1.885,6 millones. La reserva de contingencia reúne 6,9 %, con 636,0 millones. Los servicios técnicos, otros rubros, viajes y materiales completan 9,7 %, 6,4 %, 5,0 % y 2,6 %. El proyecto es intensivo en talento, no en hardware: el costo de las personas supera en más del doble al de los equipos.

:::FIGURA f01 | Personal y equipos concentran dos tercios del valor solicitado al SGR | Nota. Elaboración propia con maestro.py (BUDGET y resumen). Porcentajes sobre el valor solicitado de 9.267.260.000 COP. La reserva de contingencia es la suma de los valores monetarios esperados de 12 riesgos (CALCULADO). Figura generada con matplotlib mediante c8_figs.py; sin semilla ni corpus.

La diferencia entre el tope y el valor solicitado es de 4.732.740.000 COP. Esa holgura no se solicita ni se presupuesta. Equivale a 33,8 % del tope y a 51,1 % adicional sobre el valor solicitado. La decisión DEC-F06 la describe como opciones condicionadas a los términos de referencia: más nodos, un cuarto tramo o un año adicional de custodia. Solicitar el tope sin una actividad que lo justifique contradice una regla. Cada peso debe vincularse a una línea con paquete, meses y criterio de aceptación.

### 8.1.3 Supuestos del presupuesto

El presupuesto descansa en cinco supuestos que el equipo formulador debe revisar antes de radicar. Primero, los costos unitarios son valores de formulación sin cotización. Segundo, los precios se expresan en pesos corrientes del momento de la formulación y no incorporan indexación por inflación. Tercero, los equipos importados dependen de la tasa de cambio. El riesgo R-FIN-01 le asigna un valor monetario esperado de 165,0 millones de COP, el mayor del registro. Cuarto, la contrapartida en especie se valora con los costos de la institución y la empresa, aún sin certificar. Quinto, el tratamiento tributario de cada línea depende de los términos de referencia.

Estos supuestos no son iguales en peso. Los dos primeros afectan a todas las líneas y se corrigen con cotizaciones. El tercero afecta a los equipos importados y se mitiga con la compra por tramo, que reduce la exposición cambiaria acumulada. Los dos últimos afectan a la elegibilidad y se resuelven con documentos. La sensibilidad de la sección 8.9 cuantifica el efecto conjunto de los dos primeros. La reserva de contingencia no sustituye la revisión: cubre desviaciones aisladas y no una alteración sistemática de los precios.

## 8.2 Personal

El personal es el rubro mayor. La {T:t02} detalla 29 cargos con su cantidad, costo unitario mensual, naturaleza, paquete y meses. Suman 624 persona-mes, equivalentes a 26 personas de dedicación completa durante 24 meses. Los cargos con valor declarado en el expediente suman 2.008,8 millones de COP, y los cargos propuestos por esta formulación suman 2.544,0 millones. Los salarios son referencias de formulación y no corresponden a contratos.

:::TABLA t02 | Presupuesto de personal detallado
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Jóvenes investigadores (6) | 72 persona-mes | 2.000.000 | 144.000.000 | DECLARADO | WP1 | 1–12 |
| P02 | Estudiantes de maestría (2) | 48 persona-mes | 6.350.000 | 304.800.000 | DECLARADO | WP1 | 1–24 |
| P03 | Científico de datos senior (1) | 24 persona-mes | 20.000.000 | 480.000.000 | DECLARADO | WP1 | 1–24 |
| P04 | Ingenieros IoT y de campo (3) | 72 persona-mes | 9.000.000 | 648.000.000 | DECLARADO | WP2 | 1–24 |
| P05 | Coordinación de apropiación social (1) | 24 persona-mes | 8.000.000 | 192.000.000 | DECLARADO | WP3 | 1–24 |
| P06 | Gerencia de proyecto (1) | 24 persona-mes | 10.000.000 | 240.000.000 | DECLARADO | WP0 | 1–24 |
| P07 | Especialista en metrología y calibración (1) | 24 persona-mes | 12.000.000 | 288.000.000 | PROPUESTO | WP1 | 1–24 |
| P08 | Ingenieros de software y nube (2) | 48 persona-mes | 9.500.000 | 456.000.000 | PROPUESTO | WP2 | 1–24 |
| P09 | Ingeniero de firmware y energía (1) | 24 persona-mes | 9.000.000 | 216.000.000 | PROPUESTO | WP2 | 1–24 |
| P10 | Técnicos de campo departamentales (6) | 144 persona-mes | 4.500.000 | 648.000.000 | PROPUESTO | WP2 | 1–24 |
| P11 | Profesionales de apropiación social (2) | 48 persona-mes | 6.000.000 | 288.000.000 | PROPUESTO | WP3 | 1–24 |
| P12 | Analista de datos espaciales y gemelo digital (1) | 24 persona-mes | 10.000.000 | 240.000.000 | PROPUESTO | WP2 | 1–24 |
| P13 | Profesional en calidad del aire y salud ambiental (1) | 24 persona-mes | 10.000.000 | 240.000.000 | PROPUESTO | WP3 | 1–24 |
| P14 | Profesional de convenios y custodia (1) | 24 persona-mes | 7.000.000 | 168.000.000 | PROPUESTO | WP3 | 1–24 |
| Total | Personal |  |  | 4.552.800.000 |  |  |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (BUDGET). Naturaleza: DECLARADO = valor del expediente E3; PROPUESTO = decisión de formulación sujeta a ratificación. No hay cotizaciones: [DATO_USUARIO: cotizaciones formales por proveedor]. Valores en COP, miles con punto.

El costo unitario mensual varía de 2.000.000 a 20.000.000 COP según el cargo. Esa dispersión refleja la combinación de perfiles técnicos con asistentes de campo. La línea técnica concentra 65,4 % del gasto de personal y la de gestión 24,8 %. Cuando los términos de referencia fijen topes de honorarios, el equipo formulador debe compararlos con estas cifras y ajustar el costo unitario. El ajuste altera el total del rubro, pero no la estructura del paquete.

## 8.3 Equipos y software

Los equipos y el software suman 1.885,6 millones de COP. La {T:t03} los detalla en 12 líneas. Tres grupos organizan el gasto. La red de medición, con nodos, cabezales, gateways, energía y enlace satelital, suma 1.175,56 millones, equivalentes a 62,3 % del rubro. Los equipos de referencia y calibración suman 405,0 millones, equivalentes a 21,5 %. La plataforma de cómputo suma 275,0 millones, equivalentes a 14,6 %.

:::TABLA t03 | Presupuesto de equipos y software
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E01 | Nodos IoT de medición (100 + 20 de reserva) | 120 unidad | 4.500.000 | 540.000.000 | DECLARADO | WP2 | 1–24 |
| E02 | Cabezales ópticos de partículas | 150 unidad | 1.200.000 | 180.000.000 | DECLARADO | WP2 | 1–24 |
| E03 | Monitores gravimétricos de referencia | 3 unidad | 85.000.000 | 255.000.000 | DECLARADO | WP1 | 4–6 |
| E04 | Gateways con energía solar y respaldo (10 + 1 de reserva) | 11 unidad | 28.000.000 | 308.000.000 | PROPUESTO | WP2 | 1–24 |
| E05 | Kits de energía solar y batería para nodos | 120 unidad | 650.000 | 78.000.000 | PROPUESTO | WP2 | 1–24 |
| E06 | Módulos de enlace satelital de respaldo | 10 unidad | 3.500.000 | 35.000.000 | PROPUESTO | WP2 | 3–24 |
| E07 | Banco de calibración de laboratorio (cámara de humedad y generador de aerosol) | 1 unidad | 150.000.000 | 150.000.000 | PROPUESTO | WP1 | 3–5 |
| E08 | Estaciones de trabajo para entrenamiento de modelos | 2 unidad | 25.000.000 | 50.000.000 | PROPUESTO | WP1 | 1–3 |
| E09 | Equipos de campo e instrumentación (lote) | 1 lote | 30.000.000 | 30.000.000 | PROPUESTO | WP2 | 1–3 |
| E10 | Instancias en la nube reservadas (24 meses) | 1 clúster | 180.000.000 | 180.000.000 | DECLARADO | WP2 | 1–24 |
| E11 | Software de analítica y repositorios | 1 paquete | 45.000.000 | 45.000.000 | DECLARADO | WP2 | 1–24 |
| E12 | Planes de datos celulares M2M para gateways (12 SIM, 24 meses) | 288 SIM-mes | 120.000 | 34.560.000 | PROPUESTO | WP2 | 1–24 |
| Total | Equipos y software |  |  | 1.885.560.000 |  |  |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (BUDGET). Naturaleza: DECLARADO = valor del expediente E3; PROPUESTO = decisión de formulación sujeta a ratificación. No hay cotizaciones: [DATO_USUARIO: cotizaciones formales por proveedor]. Valores en COP, miles con punto.

Tres decisiones de compra explican la estructura. Primera, se compran 120 nodos para operar 100, con una reserva de 20 que absorbe pérdidas por robo, falla o desgaste. Segunda, se compran 150 cabezales ópticos, con una relación de 1,25 cabezales por nodo, para reponer 30 cabezales saturados por polvo. Tercera, se compran 11 gateways para operar 10. Los tres lotes se compran por tramo y no de una vez, de acuerdo con la compuerta que libera cada tramo.

El costo del equipo de referencia ilustra la razón de los tramos. Un monitor gravimétrico cuesta 18,9 veces lo que cuesta un nodo, de modo que solo se compran tres, uno por departamento. La proporción es la que hace viable la colocalización: el modelo aprende de pocos instrumentos costosos y se aplica a muchos nodos baratos. La nube y el software, en cambio, son costos declarados del expediente y se mantienen como están.

## 8.4 Materiales e insumos

Los materiales e insumos suman 242,9 millones de COP, equivalentes a 2,6 % del SGR. La {T:t04} los lista. El mayor componente es el mantenimiento de la red: repuestos y consumibles, cerramientos con mástiles y polvo de ensayo para el banco de calibración. Los filtros de membrana para gravimetría suman 14,4 millones de COP. La verificación gravimétrica usa filtros de politetrafluoroetileno, con 5 filtros por análisis incluidos los de control.

:::TABLA t04 | Presupuesto de materiales e insumos
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M01 | Filtros de membrana PTFE para gravimetría | 1.200 unidad | 12.000 | 14.400.000 | DECLARADO | WP1 | 3–24 |
| M02 | Polvo de ensayo normalizado y consumibles del banco de calibración | 15 lote | 2.800.000 | 42.000.000 | PROPUESTO | WP1 | 1–24 |
| M03 | Cerramientos NEMA 4X y mástiles para nodos | 120 unidad | 350.000 | 42.000.000 | DECLARADO | WP2 | 1–24 |
| M04 | Cartillas impresas del índice y del protocolo de alerta | 5.000 unidad | 8.500 | 42.500.000 | DECLARADO | WP3 | 3–24 |
| M05 | Kits de papelería para talleres de co-diseño | 20 kit | 1.500.000 | 30.000.000 | DECLARADO | WP3 | 2–24 |
| M06 | Elementos de protección personal (mascarillas N95) | 3.000 unidad | 4.000 | 12.000.000 | DECLARADO | WP3 | 1–24 |
| M07 | Repuestos y consumibles de mantenimiento (baterías, cables, conectores) | 1 lote | 60.000.000 | 60.000.000 | PROPUESTO | WP2 | 3–24 |
| Total | Materiales e insumos |  |  | 242.900.000 |  |  |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (BUDGET). Naturaleza: DECLARADO = valor del expediente E3; PROPUESTO = decisión de formulación sujeta a ratificación. No hay cotizaciones: [DATO_USUARIO: cotizaciones formales por proveedor]. Valores en COP, miles con punto.

Un aspecto del rubro conviene señalar. Las cartillas impresas del índice y del protocolo, junto con los kits de talleres y las mascarillas, apoyan el uso institucional (objetivo OE3). Representan un gasto pequeño frente al total. Su inclusión responde al supuesto crítico de adopción: un tablero que los comités no entienden no se usa. El costo del material impreso es una inversión en el supuesto SC-3.

## 8.5 Servicios técnicos

Los servicios técnicos suman 896,0 millones de COP. La {T:t05} los agrupa en cuatro áreas. Los servicios de laboratorio y metrología suman 294,0 millones, equivalentes a 32,8 % del rubro. Los servicios de campo suman 327,0 millones, equivalentes a 36,5 %. Los servicios de protección y seguridad suman 125,0 millones, equivalentes a 14,0 %. Los servicios de formación suman 150,0 millones, equivalentes a 16,7 %.

:::TABLA t05 | Presupuesto de servicios técnicos
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Análisis gravimétrico en laboratorio acreditado | 240 muestra | 350.000 | 84.000.000 | DECLARADO | WP1 | 3–24 |
| S02 | Consultoría jurídica en propiedad intelectual y libertad de operación | 150 hora | 300.000 | 45.000.000 | DECLARADO | WP3 | 1–24 |
| S03 | Auditoría externa de ciberseguridad | 2 servicio | 15.000.000 | 30.000.000 | DECLARADO | WP2 | 8–24 |
| S04 | Póliza todo riesgo de equipos | 2 prima anual | 25.000.000 | 50.000.000 | DECLARADO | WP0 | 1–24 |
| S05 | Instalación en sitio, mástiles y obra menor (100 nodos y 10 gateways) | 110 sitio | 1.200.000 | 132.000.000 | PROPUESTO | WP2 | 3–24 |
| S06 | Estudio de cobertura y de enlace en tres departamentos | 3 estudio | 20.000.000 | 60.000.000 | PROPUESTO | WP2 | 1–4 |
| S07 | Evaluación externa independiente (meses 12 y 24) | 2 evaluación | 60.000.000 | 120.000.000 | PROPUESTO | WP0 | 12–24 |
| S08 | Ensayo de desempeño con laboratorio externo | 1 campaña | 90.000.000 | 90.000.000 | PROPUESTO | WP1 | 20–24 |
| S09 | Formación y soporte a custodios por tramo | 3 tramo | 50.000.000 | 150.000.000 | PROPUESTO | WP3 | 6–24 |
| S10 | Planes de enlace satelital de respaldo (10 módulos, 22 meses) | 220 módulo-mes | 250.000 | 55.000.000 | PROPUESTO | WP2 | 3–24 |
| S11 | Importación y nacionalización de equipos | 1 servicio | 80.000.000 | 80.000.000 | PROPUESTO | WP0 | 1–18 |
| Total | Servicios técnicos |  |  | 896.000.000 |  |  |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (BUDGET). Naturaleza: DECLARADO = valor del expediente E3; PROPUESTO = decisión de formulación sujeta a ratificación. No hay cotizaciones: [DATO_USUARIO: cotizaciones formales por proveedor]. Valores en COP, miles con punto.

Dos líneas tienen un papel de control. La evaluación externa independiente suma 210,0 millones de COP, equivalentes a 23,4 % del rubro. Esa línea produce el informe de laboratorio externo del hito H7, que sostiene el nivel de madurez tecnológica final. La formación de custodios suma 150,0 millones y responde a la meta de 60 personas certificadas. Ambas líneas existen para reducir dos incertidumbres declaradas: el desempeño real del modelo y la capacidad de los custodios.

## 8.6 Viajes y viáticos

Los viajes y viáticos suman 462,0 millones de COP. La {T:t06} los desagrega en siete líneas. Los desplazamientos de campo concentran 408,0 millones, equivalentes a 88,3 % del rubro. Los viajes de integración suman 24,0 millones y los de laboratorio suman 30,0 millones. El gasto de campo se explica por la geografía: la red cubre tres departamentos y 12 municipios, con visitas de instalación, mantenimiento y colocalización.

:::TABLA t06 | Presupuesto de viajes y viáticos
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | Tiquetes aéreos nacionales | 150 trayecto | 600.000 | 90.000.000 | PROPUESTO | WP2 | 1–24 |
| V02 | Viáticos de alojamiento y manutención | 600 día-persona | 350.000 | 210.000.000 | PROPUESTO | WP2 | 1–24 |
| V03 | Arrendamiento de vehículos 4x4 | 240 día | 450.000 | 108.000.000 | PROPUESTO | WP2 | 1–24 |
| V04 | Viaje internacional para divulgación científica | 2 viaje | 12.000.000 | 24.000.000 | DECLARADO | WP3 | 14–24 |
| V05 | Alimentación de laboratorios ciudadanos | 20 evento | 1.500.000 | 30.000.000 | DECLARADO | WP3 | 2–24 |
| Total | Viajes y viáticos |  |  | 462.000.000 |  |  |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (BUDGET). Naturaleza: DECLARADO = valor del expediente E3; PROPUESTO = decisión de formulación sujeta a ratificación. No hay cotizaciones: [DATO_USUARIO: cotizaciones formales por proveedor]. Valores en COP, miles con punto.

La estimación usa costos unitarios de formulación: viáticos de 5,5 millones de COP y transporte de 2,2 millones por visita a un sitio. Esos valores son propuestos y deben sustituirse por las tarifas oficiales de comisión cuando existan. El riesgo R-EXT-01 (deslizamientos o réplicas) puede alterar los costos de desplazamiento, y la reserva de contingencia lo cubre en parte. La estimación no incluye tiquetes aéreos internacionales, que no se prevén.

## 8.7 Otros rubros

Otros rubros suman 592,0 millones de COP. La {T:t07} los lista. La administración del proyecto suma 360,0 millones, equivalentes a 3,9 % del SGR solicitado y a 60,8 % del rubro. El expediente E3 declara un tope porcentual de administración de 5 %, que equivaldría a 463,4 millones. Ese tope no se verificó, y la administración propuesta queda por debajo de él por 103,4 millones. Los seguros suman 110,0 millones, la publicación y difusión suman 85,0 millones y la evaluación suma 72,0 millones.

:::TABLA t07 | Presupuesto de otros rubros
| Id | Concepto | Cantidad y unidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |
| --- | --- | --- | --- | --- | --- | --- | --- |
| O01 | Cargos de procesamiento de artículos de acceso abierto | 2 artículo | 12.500.000 | 25.000.000 | DECLARADO | WP3 | 14–24 |
| O02 | Logística de ferias y laboratorios de apropiación | 9 evento | 8.000.000 | 72.000.000 | DECLARADO | WP3 | 4–24 |
| O03 | Registro ante la DNDA y asesoría de propiedad intelectual | 1 paquete | 15.000.000 | 15.000.000 | DECLARADO | WP3 | 12–24 |
| O04 | Pólizas y garantías del SGR | 2 prima anual | 30.000.000 | 60.000.000 | DECLARADO | WP0 | 1–24 |
| O05 | Administración (revisoría y plataforma de seguimiento) | 24 mes | 15.000.000 | 360.000.000 | DECLARADO | WP0 | 1–24 |
| O06 | Publicaciones de divulgación y eventos de socialización | 1 paquete | 60.000.000 | 60.000.000 | PROPUESTO | WP3 | 6–24 |
| Total | Otros rubros |  |  | 592.000.000 |  |  |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (BUDGET). Naturaleza: DECLARADO = valor del expediente E3; PROPUESTO = decisión de formulación sujeta a ratificación. No hay cotizaciones: [DATO_USUARIO: cotizaciones formales por proveedor]. Valores en COP, miles con punto.

La reserva de contingencia aparece en el resumen y no en esta tabla, porque su origen es analítico y no una compra. Su valor de 636,0 millones de COP resulta de sumar los valores monetarios esperados de 12 riesgos. La suma sin redondear es 636,5 millones, y la diferencia de 0,5 millones obedece al redondeo a millones. El capítulo 10 documenta cada valor. La admisibilidad de la reserva como rubro depende de los términos de referencia. Si no es admisible, el valor solicitado baja a 8.631.260.000 COP, equivalente a 61,7 % del tope.

## 8.8 Flujo de caja

El flujo de caja distribuye cada línea de forma uniforme entre su mes inicial y su mes final. Hay dos excepciones. Las compras de equipos se concentran en los meses 5, 13 y 18. La reserva se reparte en 24 cuotas. La {T:t08} presenta el flujo trimestral del SGR y de la contrapartida. El desembolso semestral del SGR es de 2.689,3, 1.936,1, 2.634,1 y 2.007,8 millones de COP; la contrapartida es de 527,5 millones por semestre.

:::TABLA t08 | Flujo de caja trimestral del proyecto
| Trimestre | Meses | SGR (COP) | Contrapartida (COP) | Total (COP) | SGR acumulado (%) |
| --- | --- | --- | --- | --- | --- |
| T1 | 1–3 | 1.048.943.452 | 263.750.000 | 1.312.693.452 | 11,3 |
| T2 | 4–6 | 1.640.335.948 | 263.750.000 | 1.904.085.948 | 29,0 |
| T3 | 7–9 | 961.970.623 | 263.750.000 | 1.225.720.623 | 39,4 |
| T4 | 10–12 | 974.119.944 | 263.750.000 | 1.237.869.944 | 49,9 |
| T5 | 13–15 | 1.355.798.266 | 263.750.000 | 1.619.548.266 | 64,5 |
| T6 | 16–18 | 1.278.252.811 | 263.750.000 | 1.542.002.811 | 78,3 |
| T7 | 19–21 | 994.919.478 | 263.750.000 | 1.258.669.478 | 89,1 |
| T8 | 22–24 | 1.012.919.478 | 263.750.000 | 1.276.669.478 | 100,0 |
| Total | 1–24 | 9.267.260.000 | 2.110.000.000 | 11.377.260.000 | 100,0 |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (flujo_sgr, flujo_contra y por_periodo). Cada línea se distribuye de forma uniforme entre su mes inicial y final; los nodos, los cabezales y los gateways se compran en los meses 5, 13 y 18; la reserva se reparte en 24 cuotas. Naturaleza: CALCULADO con redondeo por mayor resto. Valores en COP.

La curva de ejecución acumulada tiene un rasgo útil para la gestión. Hasta el mes 6 se ejecuta 29,0 % del SGR. Hasta la compuerta C1, en el mes 12, se ejecuta 49,9 %, equivalente a 4.625,4 millones de COP. Hasta la compuerta C2, en el mes 17, se ejecuta 71,5 %, equivalente a 6.629,3 millones. Esto significa que un poco más de la mitad del valor solicitado se compromete después de la compuerta C1. Si el piloto no cumple los umbrales, el proyecto puede detenerse o reorientarse con la mitad del presupuesto sin ejecutar. La {F:f02} presenta la curva.

:::FIGURA f02 | El SGR se ejecuta 49,9 % hasta la compuerta C1 y 71,5 % hasta C2 | Nota. Elaboración propia con maestro.py (flujo_sgr). La curva acumula el desembolso mensual del SGR; las líneas verticales marcan las compuertas C1 (mes 12) y C2 (mes 17). Naturaleza: CALCULADO. Figura generada con matplotlib mediante c8_figs.py; sin semilla ni corpus.

El desembolso mensual no es uniforme. La {F:f03} muestra tres picos que coinciden con las compras de los tramos: 777,4, 707,6 y 630,1 millones de COP. Las compras de los tramos 2 y 3 suman 694,0 millones, equivalentes a 7,5 % del SGR. La compra del tramo 1 suma 334,0 millones, equivalentes a 3,6 %. La secuencia protege el capital: lo que se compra después de una compuerta depende de que la compuerta se supere.

:::FIGURA f03 | Tres picos de desembolso coinciden con las compras de los tramos 1, 2 y 3 | Nota. Elaboración propia con maestro.py (flujo_sgr y compras por tramo). Los picos corresponden a los meses 5, 13 y 18. Naturaleza: CALCULADO. Figura generada con matplotlib mediante c8_figs.py; sin semilla ni corpus.

## 8.9 Sensibilidad del presupuesto

La sensibilidad evalúa cuánto cambia el valor solicitado ante variaciones de 10 % en las líneas. La {T:t09} presenta diez escenarios. Si todas las líneas, sin la reserva, aumentan 10 %, el valor solicitado sube 863,1 millones de COP. Llega a 10.130,4 millones, equivalentes a 72,4 % del tope. La reserva de 636,0 millones no cubre ese aumento y deja un déficit de 227,1 millones. Si todas las líneas bajan 10 %, el valor baja a 8.404,1 millones, equivalentes a 60,0 % del tope.

:::TABLA t09 | Sensibilidad del valor solicitado ante variaciones de ±10 % en las líneas
| Escenario | SGR (millones de COP) | Variación (millones de COP) | % del tope | ¿La reserva cubre el aumento? |
| --- | --- | --- | --- | --- |
| Base: valor solicitado | 9.267,3 | 0,0 | 66,2 | No aplica |
| Todas las líneas, sin reserva, −10 % | 8.404,1 | -863,1 | 60,0 | No aplica |
| Todas las líneas, sin reserva, +10 % | 10.130,4 | +863,1 | 72,4 | No; déficit de 227,1 M |
| Personal +10 % | 9.722,5 | +455,3 | 69,4 | Sí |
| Equipos y software +10 % | 9.455,8 | +188,6 | 67,5 | Sí |
| Materiales e insumos +10 % | 9.291,5 | +24,3 | 66,4 | Sí |
| Servicios técnicos +10 % | 9.356,9 | +89,6 | 66,8 | Sí |
| Viajes y viáticos +10 % | 9.313,5 | +46,2 | 66,5 | Sí |
| Otros rubros +10 % | 9.326,5 | +59,2 | 66,6 | Sí |
| Líneas PROPUESTO +10 % | 9.715,9 | +448,7 | 69,4 | Sí |
:::NOTA *Nota.* Elaboración propia con python a partir de maestro.py (BUDGET). La reserva de 636,0 millones de COP permanece fija; el tope declarado es 14.000 millones de COP (NO_VERIFICADO). Naturaleza: CALCULADO.

El rubro más sensible es el personal. Un aumento de 10 % en personal suma 455,3 millones, que representan 71,6 % del aumento total. Un aumento de 10 % en las líneas propuestas, que no tienen soporte en el expediente, suma 448,7 millones. La reserva cubre cada aumento por rubro de forma individual, pero no el aumento simultáneo de todos. La lectura es prudente: el presupuesto resiste desviaciones aisladas y no resiste un alza general. La vigilancia mensual de la ejecución, con el indicador PERS-R04, es la defensa.

## 8.10 Costo-efectividad

El análisis de costo-efectividad compara el costo con una unidad de resultado, sin monetizar el resultado. Es la forma adecuada cuando los beneficios no se expresan en dinero (Gertler et al., 2016). Esta sección calcula diez razones con cifras de la ficha maestra y de la red de actividades. La {T:t10} las lista. El SGR por nodo operativo es de 92,7 millones de COP. El total del proyecto por nodo es de 113,8 millones. El SGR sin reserva por nodo es de 86,3 millones.

:::TABLA t10 | Indicadores de costo-efectividad por nodo y por hora-nodo
| Indicador | Numerador (COP) | Denominador | Valor (COP) | Naturaleza |
| --- | --- | --- | --- | --- |
| SGR por nodo operativo | 9.267.260.000 | 100 nodos | 92.672.600 | CALCULADO |
| SGR sin reserva por nodo operativo | 8.631.260.000 | 100 nodos | 86.312.600 | CALCULADO |
| Total del proyecto por nodo operativo | 11.377.260.000 | 100 nodos | 113.772.600 | CALCULADO |
| Equipos de medición por nodo comprado (E01, E02, E05, M03) | 840.000.000 | 120 nodos | 7.000.000 | CALCULADO |
| Compra de nodos, cabezales y gateways por nodo operativo, tramo 1 | 334.000.000 | 30 nodos | 11.133.333 | CALCULADO |
| Compra de nodos, cabezales y gateways por nodo operativo, tramo 2 | 388.000.000 | 40 nodos | 9.700.000 | CALCULADO |
| Compra de nodos, cabezales y gateways por nodo operativo, tramo 3 | 306.000.000 | 30 nodos | 10.200.000 | CALCULADO |
| SGR por hora-nodo teórica de operación | 9.267.260.000 | 796.320 horas-nodo | 11.638 | CALCULADO; SUPUESTO de operación |
| SGR por hora-nodo con disponibilidad de 90 % | 9.267.260.000 | 716.688 horas-nodo | 12.931 | CALCULADO; SUPUESTO de operación |
| SGR de WP1 por hora-nodo válida de colocalización (cota superior) | 1.902.200.000 | 60.000 horas-nodo | 31.703 | CALCULADO |
| Formación de custodios por persona certificada (S09) | 150.000.000 | 60 personas | 2.500.000 | CALCULADO |
| Costos directos de talleres y jornadas por actividad (V05, M05, O02) | 132.000.000 | 29 actividades | 4.551.724 | CALCULADO |
| SGR de WP3 por comité focalizado | 1.393.500.000 | 15 comités | 92.900.000 | CALCULADO; denominador SUPUESTO |
| SGR de WP3 por funcionario beneficiario | 1.393.500.000 | 150 funcionarios | 9.290.000 | CALCULADO; denominador SUPUESTO |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py y de la ficha maestra (§4, §5, §6 y §8). Las horas-nodo teóricas suman, por tramo, nodos por semanas desde el fin de la instalación hasta la semana 104 por 168 horas semanales (SUPUESTO). Sin costos de las alternativas ALT-00 a ALT-02 no hay comparación entre alternativas: [DATO_USUARIO: costos de ALT-00 a ALT-02].

La razón por hora-nodo teórica de operación es de 11.638 COP, con un supuesto de operación continua desde el fin de cada instalación. Con una disponibilidad de 90 %, la razón sube a 12.931 COP. La razón por hora-nodo válida de colocalización usa solo el gasto del paquete WP1. Es de 31.703 COP y es una cota superior, porque incluye la verificación final. Estas cifras no permiten concluir que el proyecto sea más o menos costo-efectivo que otra alternativa. No existen costos comparables de las alternativas ALT-00 a ALT-02. Permiten fijar una línea de referencia para el seguimiento.

Dos razones se refieren al uso institucional. La formación cuesta 2,5 millones de COP por persona certificada, y los talleres y jornadas cuestan 4,55 millones por actividad en costos directos. El paquete WP3 cuesta 92,9 millones por comité focalizado y 9,29 millones por funcionario beneficiario, con denominadores supuestos. Esas razones no miden efecto. Miden el costo de ofrecer la capacidad de uso. El efecto se mide con el indicador PERS-E01 y su línea base se levanta en el tramo 1.

Las razones sirven para el seguimiento más que para la comparación. Si la ejecución real se aparta de ellas, la desviación señala dónde buscar la causa. Una razón por nodo más alta que la prevista indica sobrecostos de compra. Una razón por hora-nodo más alta indica pérdida de disponibilidad. Una razón por actividad de apropiación más alta indica talleres con menos asistentes de los previstos. Cada lectura remite a un indicador PERS y a un riesgo del capítulo 10. Así el análisis de costo-efectividad se integra con el sistema de control.

## 8.11 Valor y límites del capítulo

El capítulo entrega un presupuesto que se puede auditar fila por fila y recomponer por rubro, por paquete, por fuente y por periodo. Ese valor reside en la trazabilidad: cualquier cifra del resumen se rastrea hasta una línea con su naturaleza. Los límites son cuatro. Los costos unitarios no son cotizaciones. El tope y la admisibilidad de la reserva no se verificaron. La contrapartida está pendiente de certificación. Y los análisis de sensibilidad y de costo-efectividad no incluyen incertidumbre en los precios ni costos comparables de otras alternativas.
