# FICHA MAESTRA DEL PROYECTO (fuente única de cifras; no contradecir)

Naturaleza de cada dato: DECLARADO = valor del expediente E3 aportado por el usuario; PROPUESTO = decisión de formulación de esta corrida (requiere ratificación); CALCULADO = derivado por código de este libro; SUPUESTO = por instrucción del usuario; VACIO = dato que solo el usuario o los términos de referencia pueden aportar (usar [DATO_USUARIO: …]).

## 1. Identidad congelada (H36-02)

- titulo: Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto
- convocatoria: Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)
- financiador: Sistema General de Regalías (SGR) / Ministerio de Ciencia, Tecnología e Innovación (MinCiencias)
- tipologia: Investigación aplicada, desarrollo tecnológico e innovación
- ocde: 1.2 Ingeniería eléctrica, electrónica e informática
- territorio: Departamentos de Caldas, Cundinamarca y Valle del Cauca
- fecha_corte: 13 de octubre de 2026
- fecha_limite: 11 de noviembre de 2026
- Tope normativo declarado: $ 14.000.000.000 (DECLARADO; términos de referencia NO aportados, NO_VERIFICADO)
- Duración de ejecución: 24 meses (104 semanas); horizonte posproyecto de seguimiento: 12 meses (PROPUESTO)
- TRL inicial 4; TRL final 7 (PROPUESTO; el expediente E3 declaraba TRL 8 y 'TRL 4 a 7 u 8': se fija 7 porque el sistema se demuestra en entorno operativo sin calificación formal; TRL 8 queda condicionado a evaluación de desempeño independiente)
- Caso: SGR_CONV56_AIRE. Metaprompt: GENESIS-CTeI 36.10 RC2 (VM-PAR3-MDR3-CONT1); NTC 1.1. Huella SHA-256 del maestro: 685a73f45ba1d3011a3b1ba3a1722482c46d8b9a68ffe5cbc4dbe131e4603ba8
- Territorio y alianza: SUPUESTO por instrucción del usuario. Entidad ejecutora (IES con acreditación de alta calidad), empresa tecnológica, alcaldías, UNGRD: nombres [DATO_USUARIO].

## 2. Solución (PROPUESTO)

Red de 100 nodos hoja de medición de PM2,5 y PM10 (sensor óptico de bajo costo con temperatura y humedad), 10 gateways (1 por cada 10 nodos) y 3 monitores de referencia gravimétricos (uno por departamento) para colocalización. Los nodos transmiten por LoRa al gateway; el gateway aplica el modelo de corrección (humedad, temperatura y fracción gruesa) y reenvía por red celular, con enlace satelital alterno y almacenamiento local de 7 días. Los nodos operan con panel solar y batería con autonomía mínima de 14 días sin sol. La nube aloja el entrenamiento del modelo, el gemelo digital (estimación espacial) y el tablero del índice de calidad del aire y salud (AQHI) con umbrales validados localmente. La corrección se define en UN solo lugar: el gateway (se retiran las versiones 'en el chip del sensor' y 'en el microcontrolador de cada nodo' del expediente E3).
Umbrales de desempeño (PROPUESTO; ancla EPA 2021 para uso informativo en sitio fijo): R² ≥ 0,70; NRMSE ≤ 30 %; pendiente entre 0,65 y 1,35; sesgo entre −5,0 y 5,0 µg/m³. Meta aspiracional NMAE ≤ 15 %, que no condiciona las compuertas. Línea base de error: se mide en el tramo 1 (el 'NMAE > 45 %' del expediente E3 es DECLARADO sin localizador y NO_VERIFICADO).

## 3. Objetivos

- Objetivo general: Reducir el error de medición de material particulado de una red de 100 nodos de bajo costo, y asegurar su uso institucional en la gestión del riesgo, mediante calibración dinámica en gateways, operación con energía y enlace redundantes y custodia distribuida por tramos, en Caldas, Cundinamarca y Valle del Cauca, durante 24 meses.
- OE1 (SC-1; causa priorizada en Vester: V06 (crítica), V02 (crítica), V03 (activa)): Corregir la interferencia de humedad y de fracción gruesa en las mediciones de PM2,5 y PM10 mediante colocalización con equipos de referencia y un modelo de corrección aplicado en gateways, hasta cumplir los umbrales de desempeño fijados en el piloto del tramo 1 y verificados al mes 24. Meta: R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia en los tres tramos.
- OE2 (SC-2; causa priorizada en Vester: V05 (activa) → V09 (reactiva)): Mantener la disponibilidad de 100 nodos y 10 gateways ante polvo, humedad y fallas de energía y de enlace, mediante autonomía mínima de 14 días sin sol y un enlace alterno con almacenamiento local de 7 días. Meta: Disponibilidad mensual de nodos ≥ 90 % y pérdida de paquetes ≤ 10 %.
- OE3 (SC-3 y SC-4; causa priorizada en Vester: V15 (crítica)): Lograr el uso del tablero y del protocolo de alerta por los comités de gestión del riesgo, con umbrales validados localmente y custodia por componente, mediante co-diseño, formación y convenios por tramo. Meta: ≥ 75 % de los comités focalizados usan el tablero en decisiones documentadas al mes 24.

## 4. Tramos de despliegue condicionado (estrategia R4 de 4.4-MDR)

| Tramo | Meses | Nodos | Gateways | Compra de nodos | Compra de gateways | Compuerta |
| --- | --- | --- | --- | --- | --- | --- |
| Tramo 1: piloto de contraste | 1–12 | 30 | 3 | 36 | 4 | C1 (mes 12) |
| Tramo 2: ampliación condicionada | 13–17 | 40 | 4 | 48 | 4 | C2 (mes 17) |
| Tramo 3: consolidación y transferencia | 18–24 | 30 | 3 | 36 | 3 | C3 (mes 24) |
Totales: 100 nodos operativos y 120 comprados (20 de reserva); 10 gateways operativos y 11 comprados. Distribución por departamento (PROPUESTO): Caldas 33, Cundinamarca 34, Valle del Cauca 33 nodos; 1 monitor de referencia por departamento. Municipios focalizados: 12 (4 por departamento) [DATO_USUARIO: lista]. Comités de gestión del riesgo focalizados: 15 (12 municipales y 3 departamentales) (SUPUESTO). Funcionarios beneficiarios directos: 150 (SUPUESTO, 10 por comité). Operarios de remoción en sitios monitoreados: [DATO_USUARIO].
Compuertas: C1 (mes 12) decide ampliar al tramo 2 si el modelo cumple los umbrales en el piloto (R² ≥ 0,70 y NRMSE ≤ 30 %) y si al menos 50 % de los comités del tramo 1 usa el tablero; C2 (mes 17) decide consolidar el tramo 3 con los mismos umbrales en los tres departamentos, disponibilidad mensual ≥ 90 % y convenios de custodia con partida; C3 (mes 24) cierra y transfiere. Cada compuerta libera la compra del tramo siguiente.

## 5. Presupuesto (CALCULADO desde maestro.py)

- Valor solicitado al SGR: $ 9.267.260.000 (66.2 % del tope; holgura no solicitada: $ 4.732.740.000).
- Contrapartida: $ 2.110.000.000 (IES 1.100 M en especie; empresa 210 M en efectivo y 800 M en especie; alcaldías: sin aporte, VACIO). Todas las cifras de contrapartida son DECLARADO (E3) salvo el desglose de la IES, PROPUESTO; certificaciones pendientes.
- Total del proyecto: $ 11.377.260.000.
| Rubro SGR | Millones de COP | % del SGR |
| --- | --- | --- |
| Personal | 4.552,8 | 49,1 |
| Equipos y software | 1.885,6 | 20,3 |
| Materiales e insumos | 242,9 | 2,6 |
| Servicios técnicos | 896,0 | 9,7 |
| Viajes y viáticos | 462,0 | 5,0 |
| Otros rubros | 592,0 | 6,4 |
| Reserva de contingencia | 636,0 | 6,9 |
- Flujo semestral SGR (millones): 2.689,3, 1.936,1, 2.634,1, 2.007,8. Flujo semestral de contrapartida: 527,5, 527,5, 527,5, 527,5.
- Reserva de contingencia: $ 636.000.000 = suma de valores monetarios esperados (EMV) de 12 riesgos (CALCULADO); su admisibilidad como rubro depende de los TdR (VACIO). Administración: 360 M (3,9 % del SGR solicitado; el tope porcentual del expediente E3, 5 %, no se verificó).
- Decisión DEC-F06: se solicita la suma justificada, no el tope. La holgura se describe como opciones de ampliación condicionadas a TdR (más nodos, un cuarto tramo, un año adicional de custodia) y no se presupuesta.

### Líneas de presupuesto SGR

| Id | Rubro | Concepto | Unidad | Cantidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Personal | Jóvenes investigadores (6) | persona-mes | 72 | $ 2.000.000 | $ 144.000.000 | DECLARADO | WP1 | 1–12 |
| P02 | Personal | Estudiantes de maestría (2) | persona-mes | 48 | $ 6.350.000 | $ 304.800.000 | DECLARADO | WP1 | 1–24 |
| P03 | Personal | Científico de datos senior (1) | persona-mes | 24 | $ 20.000.000 | $ 480.000.000 | DECLARADO | WP1 | 1–24 |
| P04 | Personal | Ingenieros IoT y de campo (3) | persona-mes | 72 | $ 9.000.000 | $ 648.000.000 | DECLARADO | WP2 | 1–24 |
| P05 | Personal | Coordinación de apropiación social (1) | persona-mes | 24 | $ 8.000.000 | $ 192.000.000 | DECLARADO | WP3 | 1–24 |
| P06 | Personal | Gerencia de proyecto (1) | persona-mes | 24 | $ 10.000.000 | $ 240.000.000 | DECLARADO | WP0 | 1–24 |
| P07 | Personal | Especialista en metrología y calibración (1) | persona-mes | 24 | $ 12.000.000 | $ 288.000.000 | PROPUESTO | WP1 | 1–24 |
| P08 | Personal | Ingenieros de software y nube (2) | persona-mes | 48 | $ 9.500.000 | $ 456.000.000 | PROPUESTO | WP2 | 1–24 |
| P09 | Personal | Ingeniero de firmware y energía (1) | persona-mes | 24 | $ 9.000.000 | $ 216.000.000 | PROPUESTO | WP2 | 1–24 |
| P10 | Personal | Técnicos de campo departamentales (6) | persona-mes | 144 | $ 4.500.000 | $ 648.000.000 | PROPUESTO | WP2 | 1–24 |
| P11 | Personal | Profesionales de apropiación social (2) | persona-mes | 48 | $ 6.000.000 | $ 288.000.000 | PROPUESTO | WP3 | 1–24 |
| P12 | Personal | Analista de datos espaciales y gemelo digital (1) | persona-mes | 24 | $ 10.000.000 | $ 240.000.000 | PROPUESTO | WP2 | 1–24 |
| P13 | Personal | Profesional en calidad del aire y salud ambiental (1) | persona-mes | 24 | $ 10.000.000 | $ 240.000.000 | PROPUESTO | WP3 | 1–24 |
| P14 | Personal | Profesional de convenios y custodia (1) | persona-mes | 24 | $ 7.000.000 | $ 168.000.000 | PROPUESTO | WP3 | 1–24 |
| E01 | Equipos y software | Nodos IoT de medición (100 + 20 de reserva) | unidad | 120 | $ 4.500.000 | $ 540.000.000 | DECLARADO | WP2 | 1–24 |
| E02 | Equipos y software | Cabezales ópticos de partículas | unidad | 150 | $ 1.200.000 | $ 180.000.000 | DECLARADO | WP2 | 1–24 |
| E03 | Equipos y software | Monitores gravimétricos de referencia | unidad | 3 | $ 85.000.000 | $ 255.000.000 | DECLARADO | WP1 | 4–6 |
| E04 | Equipos y software | Gateways con energía solar y respaldo (10 + 1 de reserva) | unidad | 11 | $ 28.000.000 | $ 308.000.000 | PROPUESTO | WP2 | 1–24 |
| E05 | Equipos y software | Kits de energía solar y batería para nodos | unidad | 120 | $ 650.000 | $ 78.000.000 | PROPUESTO | WP2 | 1–24 |
| E06 | Equipos y software | Módulos de enlace satelital de respaldo | unidad | 10 | $ 3.500.000 | $ 35.000.000 | PROPUESTO | WP2 | 3–24 |
| E07 | Equipos y software | Banco de calibración de laboratorio (cámara de humedad y generador de aerosol) | unidad | 1 | $ 150.000.000 | $ 150.000.000 | PROPUESTO | WP1 | 3–5 |
| E08 | Equipos y software | Estaciones de trabajo para entrenamiento de modelos | unidad | 2 | $ 25.000.000 | $ 50.000.000 | PROPUESTO | WP1 | 1–3 |
| E09 | Equipos y software | Equipos de campo e instrumentación (lote) | lote | 1 | $ 30.000.000 | $ 30.000.000 | PROPUESTO | WP2 | 1–3 |
| E10 | Equipos y software | Instancias en la nube reservadas (24 meses) | clúster | 1 | $ 180.000.000 | $ 180.000.000 | DECLARADO | WP2 | 1–24 |
| E11 | Equipos y software | Software de analítica y repositorios | paquete | 1 | $ 45.000.000 | $ 45.000.000 | DECLARADO | WP2 | 1–24 |
| E12 | Equipos y software | Planes de datos celulares M2M para gateways (12 SIM. 24 meses) | SIM-mes | 288 | $ 120.000 | $ 34.560.000 | PROPUESTO | WP2 | 1–24 |
| M01 | Materiales e insumos | Filtros de membrana PTFE para gravimetría | unidad | 1.200 | $ 12.000 | $ 14.400.000 | DECLARADO | WP1 | 3–24 |
| M02 | Materiales e insumos | Polvo de ensayo normalizado y consumibles del banco de calibración | lote | 15 | $ 2.800.000 | $ 42.000.000 | PROPUESTO | WP1 | 1–24 |
| M03 | Materiales e insumos | Cerramientos NEMA 4X y mástiles para nodos | unidad | 120 | $ 350.000 | $ 42.000.000 | DECLARADO | WP2 | 1–24 |
| M04 | Materiales e insumos | Cartillas impresas del índice y del protocolo de alerta | unidad | 5.000 | $ 8.500 | $ 42.500.000 | DECLARADO | WP3 | 3–24 |
| M05 | Materiales e insumos | Kits de papelería para talleres de co-diseño | kit | 20 | $ 1.500.000 | $ 30.000.000 | DECLARADO | WP3 | 2–24 |
| M06 | Materiales e insumos | Elementos de protección personal (mascarillas N95) | unidad | 3.000 | $ 4.000 | $ 12.000.000 | DECLARADO | WP3 | 1–24 |
| M07 | Materiales e insumos | Repuestos y consumibles de mantenimiento (baterías. cables. conectores) | lote | 1 | $ 60.000.000 | $ 60.000.000 | PROPUESTO | WP2 | 3–24 |
| S01 | Servicios técnicos | Análisis gravimétrico en laboratorio acreditado | muestra | 240 | $ 350.000 | $ 84.000.000 | DECLARADO | WP1 | 3–24 |
| S02 | Servicios técnicos | Consultoría jurídica en propiedad intelectual y libertad de operación | hora | 150 | $ 300.000 | $ 45.000.000 | DECLARADO | WP3 | 1–24 |
| S03 | Servicios técnicos | Auditoría externa de ciberseguridad | servicio | 2 | $ 15.000.000 | $ 30.000.000 | DECLARADO | WP2 | 8–24 |
| S04 | Servicios técnicos | Póliza todo riesgo de equipos | prima anual | 2 | $ 25.000.000 | $ 50.000.000 | DECLARADO | WP0 | 1–24 |
| S05 | Servicios técnicos | Instalación en sitio. mástiles y obra menor (100 nodos y 10 gateways) | sitio | 110 | $ 1.200.000 | $ 132.000.000 | PROPUESTO | WP2 | 3–24 |
| S06 | Servicios técnicos | Estudio de cobertura y de enlace en tres departamentos | estudio | 3 | $ 20.000.000 | $ 60.000.000 | PROPUESTO | WP2 | 1–4 |
| S07 | Servicios técnicos | Evaluación externa independiente (meses 12 y 24) | evaluación | 2 | $ 60.000.000 | $ 120.000.000 | PROPUESTO | WP0 | 12–24 |
| S08 | Servicios técnicos | Ensayo de desempeño con laboratorio externo | campaña | 1 | $ 90.000.000 | $ 90.000.000 | PROPUESTO | WP1 | 20–24 |
| S09 | Servicios técnicos | Formación y soporte a custodios por tramo | tramo | 3 | $ 50.000.000 | $ 150.000.000 | PROPUESTO | WP3 | 6–24 |
| S10 | Servicios técnicos | Planes de enlace satelital de respaldo (10 módulos. 22 meses) | módulo-mes | 220 | $ 250.000 | $ 55.000.000 | PROPUESTO | WP2 | 3–24 |
| S11 | Servicios técnicos | Importación y nacionalización de equipos | servicio | 1 | $ 80.000.000 | $ 80.000.000 | PROPUESTO | WP0 | 1–18 |
| V01 | Viajes y viáticos | Tiquetes aéreos nacionales | trayecto | 150 | $ 600.000 | $ 90.000.000 | PROPUESTO | WP2 | 1–24 |
| V02 | Viajes y viáticos | Viáticos de alojamiento y manutención | día-persona | 600 | $ 350.000 | $ 210.000.000 | PROPUESTO | WP2 | 1–24 |
| V03 | Viajes y viáticos | Arrendamiento de vehículos 4x4 | día | 240 | $ 450.000 | $ 108.000.000 | PROPUESTO | WP2 | 1–24 |
| V04 | Viajes y viáticos | Viaje internacional para divulgación científica | viaje | 2 | $ 12.000.000 | $ 24.000.000 | DECLARADO | WP3 | 14–24 |
| V05 | Viajes y viáticos | Alimentación de laboratorios ciudadanos | evento | 20 | $ 1.500.000 | $ 30.000.000 | DECLARADO | WP3 | 2–24 |
| O01 | Otros rubros | Cargos de procesamiento de artículos de acceso abierto | artículo | 2 | $ 12.500.000 | $ 25.000.000 | DECLARADO | WP3 | 14–24 |
| O02 | Otros rubros | Logística de ferias y laboratorios de apropiación | evento | 9 | $ 8.000.000 | $ 72.000.000 | DECLARADO | WP3 | 4–24 |
| O03 | Otros rubros | Registro ante la DNDA y asesoría de propiedad intelectual | paquete | 1 | $ 15.000.000 | $ 15.000.000 | DECLARADO | WP3 | 12–24 |
| O04 | Otros rubros | Pólizas y garantías del SGR | prima anual | 2 | $ 30.000.000 | $ 60.000.000 | DECLARADO | WP0 | 1–24 |
| O05 | Otros rubros | Administración (revisoría y plataforma de seguimiento) | mes | 24 | $ 15.000.000 | $ 360.000.000 | DECLARADO | WP0 | 1–24 |
| O06 | Otros rubros | Publicaciones de divulgación y eventos de socialización | paquete | 1 | $ 60.000.000 | $ 60.000.000 | PROPUESTO | WP3 | 6–24 |
| X01 | Reserva de contingencia | Reserva de contingencia (suma de valores monetarios esperados) | global | 1 | $ 636.000.000 | $ 636.000.000 | CALCULADO | WP0 | 1–24 |

### Contrapartida

| Id | Aporte | Fuente | Total (COP) | Naturaleza |
| --- | --- | --- | --- | --- |
| C01 | Investigador principal, 50 % durante 24 meses | IES | $ 350.000.000 | DECLARADO |
| C02 | Coinvestigador técnico, 30 % durante 24 meses | IES | $ 250.000.000 | DECLARADO |
| C03 | Coinvestigadores de ambiente y ciencias sociales, 20 % | IES | $ 200.000.000 | PROPUESTO |
| C04 | Uso de laboratorios y equipos de la IES | IES | $ 300.000.000 | PROPUESTO |
| C05 | Aporte de la empresa tecnológica: logística y viáticos de emergencia | EMP | $ 210.000.000 | DECLARADO |
| C06 | Infraestructura en la nube de la empresa | EMP | $ 800.000.000 | DECLARADO |

## 6. Cronograma (CALCULADO por CPM; semanas)

Duración = 104 semanas = ruta crítica. Actividades críticas: A0.1, A2.1, A1.2, A2.2, A1.3, A1.4, C1, A2.3, A1.5, C2, A2.4, A1.6, A3.4.
| Id | Actividad | Duración (sem.) | Predecesoras | Inicio temprano | Fin temprano | Holgura | WP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A0.1 | Contratar equipo y firmar convenios de ejecución | 8 | — | 0 | 8 | 0 | WP0 |
| A1.1 | Seleccionar sitios y diseñar la colocalización | 4 | A0.1 | 8 | 12 | 2 | WP1 |
| A2.1 | Diseñar arquitectura de enlace y energía | 6 | A0.1 | 8 | 14 | 0 | WP2 |
| A1.2 | Adquirir y caracterizar lote 1 de nodos y referencias | 10 | A1.1, A2.1 | 14 | 24 | 0 | WP1 |
| A2.2 | Desarrollar firmware y plataforma base | 10 | A2.1 | 14 | 24 | 0 | WP2 |
| A1.3 | Colocalizar y calibrar en el piloto (tramo 1) | 16 | A1.2, A2.2 | 24 | 40 | 0 | WP1 |
| A3.1 | Co-diseñar umbrales y protocolo de alerta con comités | 24 | A1.1 | 12 | 36 | 12 | WP3 |
| A1.4 | Entrenar y validar el modelo de corrección | 8 | A1.3 | 40 | 48 | 0 | WP1 |
| C1 | Compuerta C1: decisión de ampliación al tramo 2 | 2 | A1.4, A3.1 | 48 | 50 | 0 | WP0 |
| A2.3 | Instalar tramo 2 (40 nodos, 4 gateways) | 12 | C1 | 50 | 62 | 0 | WP2 |
| A1.5 | Reentrenar y verificar por departamento (tramo 2) | 6 | A2.3 | 62 | 68 | 0 | WP1 |
| A3.2 | Poner en uso el tablero con los comités | 12 | C1 | 50 | 62 | 6 | WP3 |
| C2 | Compuerta C2: decisión de consolidación al tramo 3 | 2 | A1.5, A3.2 | 68 | 70 | 0 | WP0 |
| A2.4 | Instalar tramo 3 (30 nodos, 3 gateways) | 12 | C2 | 70 | 82 | 0 | WP2 |
| A3.3 | Formar custodios y firmar convenios por tramo | 16 | C2 | 70 | 86 | 12 | WP3 |
| A1.6 | Verificar desempeño final y ensayo independiente | 16 | A2.4 | 82 | 98 | 0 | WP1 |
| A3.4 | Transferir, cerrar y evaluar | 6 | A1.6, A3.3 | 98 | 104 | 0 | WP0 |

Hitos (mes de calendario):

| Hito | Descripción | Mes | Verificación |
| --- | --- | --- | --- |
| H0 | Acta de inicio y contratación completa | 2 | Contratos, convenios y plan de trabajo aprobados |
| H1 | Sitios del tramo 1 y diseño de enlace y energía listos | 4 | Informe de sitios, de cobertura y de energía |
| H2 | Colocalización del tramo 1 finalizada | 10 | Base de datos de colocalización y línea base de error medida |
| H3 | Compuerta C1: modelo validado en el piloto | 12 | Acta de compuerta con NRMSE y R² frente a referencia |
| H4 | Tramo 2 instalado y verificado | 16 | Informe de disponibilidad y desempeño del tramo 2 |
| H5 | Compuerta C2: uso institucional y desempeño | 17 | Acta de compuerta con uso del tablero y convenios |
| H6 | Tramo 3 instalado | 19 | Inventario de 100 nodos y 10 gateways operativos |
| H7 | Ensayo independiente y evaluación final | 23 | Informe de laboratorio externo y evaluación externa |
| H8 | Transferencia y cierre del tramo 3 | 24 | Actas de entrega a custodios y cláusula de apertura firmada |

Paquetes de trabajo: WP0 gestión, compuertas y cierre; WP1 medición verificada (OE1); WP2 red, energía y plataforma (OE2); WP3 uso institucional, apropiación y custodia (OE3).

## 7. Riesgos (CALCULADO)

| Id | Categoría | Riesgo | P | I | P×I | Nivel | Prob. % | Impacto (M COP) | EMV (M COP) | Estrategia |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-TEC-01 | Técnico | La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10. | 4 | 5 | 20 | EXTREMO | 60 | 250,0 | 150,0 | Mitigar |
| R-TEC-02 | Técnico | Las baterías se agotan antes de 14 días sin sol y los nodos dejan de transmitir. | 3 | 4 | 12 | ALTO | 30 | 80,0 | 24,0 | Mitigar |
| R-TEC-03 | Técnico | La red celular falla en el sitio y los gateways pierden el enlace con la nube. | 3 | 4 | 12 | ALTO | 40 | 70,0 | 28,0 | Mitigar |
| R-TEC-04 | Técnico | El modelo de corrección no generaliza entre departamentos. | 3 | 4 | 12 | ALTO | 35 | 90,0 | 31,5 | Mitigar |
| R-ORG-01 | Organizacional | Los comités de gestión del riesgo no adoptan el tablero ni el protocolo. | 3 | 5 | 15 | ALTO | 40 | 90,0 | 36,0 | Mitigar |
| R-ORG-02 | Organizacional | Los custodios no asumen la operación en el posproyecto. | 4 | 4 | 16 | ALTO | 50 | 120,0 | 60,0 | Mitigar |
| R-EXT-01 | Externo | Deslizamientos o réplicas bloquean vías y retrasan la instalación. | 4 | 3 | 12 | ALTO | 50 | 120,0 | 60,0 | Aceptar y mitigar |
| R-EXT-02 | Externo | Robo o vandalismo de nodos en sitios de remoción. | 3 | 3 | 9 | MEDIO | 40 | 60,0 | 24,0 | Transferir y mitigar |
| R-FIN-01 | Financiero | La devaluación del peso encarece los equipos importados. | 4 | 4 | 16 | ALTO | 55 | 300,0 | 165,0 | Mitigar |
| R-FIN-02 | Financiero | La contrapartida en especie no se certifica a tiempo. | 2 | 4 | 8 | MEDIO | 25 | 80,0 | 20,0 | Evitar |
| R-JUR-01 | Jurídico | Una solicitud de patente de terceros afecta la libertad de operación. | 2 | 4 | 8 | MEDIO | 20 | 100,0 | 20,0 | Mitigar |
| R-DAT-01 | Datos | Un incidente de ciberseguridad compromete la plataforma. | 2 | 4 | 8 | MEDIO | 20 | 90,0 | 18,0 | Mitigar |

Suma de EMV sin redondeo: 636,5 M COP; reserva redondeada: 636,0 M COP.

## 8. Indicadores PERS (15)

| Código | Nivel | Taxonomía | Nombre | OE | Línea base | Meta final | MMG |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PERS-R01 | R | Output | Cumplimiento del despliegue por tramo | OE2 | 0 (CALCULADO) | 100 nodos y 10 gateways (100 %) | — |
| PERS-R02 | R | Output | Ciclos de calibración ejecutados | OE1 | 0 (CALCULADO) | 6 ciclos (2 por tramo) | — |
| PERS-R03 | R | Output | Disponibilidad de la plataforma en la nube | OE2 | VACIO (VACIO) | ≥ 99,0 % | — |
| PERS-R04 | R | Output | Desviación de la ejecución presupuestal | OE3 | 0 (CALCULADO) | |desviación| ≤ 5 % al cierre | — |
| PERS-R05 | R | Output | Horas-nodo de colocalización válidas | OE1 | 0 (CALCULADO) | ≥ 60.000 y 4 rotaciones por departamento | — |
| PERS-R06 | R | Output | Cumplimiento de informes de seguimiento | OE3 | 0 (CALCULADO) | 100 % | — |
| PERS-P01 | P | Output | Red de 100 nodos y 10 gateways operativa | OE2 | 0 / 0 (CALCULADO) | 100 / 10 al mes 24 | PROT-FUNC |
| PERS-P02 | P | Output | Software de corrección y gemelo digital registrado | OE1 | 0 (CALCULADO) | 1 registro vigente | SW-REG |
| PERS-P03 | P | Output | Artículos científicos en revistas Q1 o Q2 | OE1 | 0 (CALCULADO) | 2 sometidos y al menos 1 aceptado al mes 24 | ART-A1 / ART-A2 |
| PERS-P04 | P | Output | Actividades de apropiación social documentadas | OE3 | 0 (CALCULADO) | 29 actividades (20 talleres y 9 jornadas) | ASC-PART / ASC-COM / ASC-CIRC |
| PERS-E01 | E | Outcome | Uso institucional del tablero y del protocolo | OE3 | VACIO (VACIO) | ≥ 75 % al mes 24 | — |
| PERS-E02 | E | Outcome | Reducción relativa de falsas alarmas | OE3 | Se mide en el tramo 1 (VACIO) | ≥ 30 % de reducción relativa | — |
| PERS-E03 | E | Outcome | Capacidad instalada en custodios | OE3 | 0 (CALCULADO) | ≥ 60 personas certificadas | FORM (capacitación) |
| PERS-S01 | S | Impact | Activación del protocolo ante superación de umbral | OE3 | VACIO (VACIO) | ≥ 80 % a los 12 meses posteriores al cierre | — |
| PERS-S02 | S | Impact | Continuidad de la red bajo custodia | OE3 | VACIO (VACIO) | ≥ 70 % a los 12 meses posteriores al cierre | — |

## 9. Alternativas y evaluación multicriterio (CALCULADO; puntajes PROPUESTO)

- ALT-00: Statu quo: sensores aislados sin calibración dinámica
- ALT-01: Estaciones fijas de referencia en los sitios de remoción
- ALT-02: Red de sensores con calibración centralizada en la nube
- ALT-03: Red híbrida con corrección en gateway, despliegue por tramos y custodia distribuida (contrainductiva)
Puntajes totales ponderados (escala 1 a 9): ALT-00 = 4,475; ALT-01 = 4,335; ALT-02 = 5,15; ALT-03 = 5,805. Alternativa ganadora: ALT-03. Sensibilidad ±10 % relativo: la ganadora no cambia en los 5 escenarios. GWO no se activa: 4 alternativas son enumerables (AS-32). Puntajes sujetos a ratificación del panel evaluador.

## 10. Resultados del análisis causal (secciones 4.3 a 4.5 y 4.4-MDR)

- Escenario de trabajo S2: 48 aristas, ΣI = ΣD = 78; ciclos: V15 en 140 de 144 ciclos simples; sin estabilidad de potencias hasta k = 10.
- Problema central: error de medición IoT sin verificar (V06), crítica en los cinco escenarios (I = 8; D = 13). Causas directas: V03 humedad (I 6, D 0), V02 PM10 (I 7, D 6), V01 PM2,5 (I 6, D 5), V07 frecuencia de calibración (I 5, D 2); indirecta: V05 escombros (I 7, D 1). Efectos: V11 AQHI (D 11), V12 falsas alarmas, V14 personas alertadas (D 9), V15 adopción institucional (crítica, I 7, D 7).
- Clasificación S2 por mediana: críticas V02, V06, V15; activas V03, V04, V05; frontera V01, V07, V10, V11, V12; reactivas V09, V14; autónomas relativas V08, V13.
- Decisión de 4.4-MDR: R4 = desplegar por tramos con piloto de contraste y custodia distribuida; R3 (transferencia a las alcaldías al mes 25 como receptor único) no se recomienda como diseño base; R0 (sin intervención) tampoco. Supuestos críticos SC-1 (medición verificada), SC-2 (energía y enlace), SC-3 (uso institucional), SC-4 (custodia). Probabilidades de los árboles de decisión: no declaradas (sin fuente).
- Sostenibilidad: costo total de sostenimiento, ICAR y fondo patrimonial NO_CALCULABLE; portafolio del expediente E3: máxima participación 63,2 %, HHI 0,472 en el año 1; cláusula de apertura y salida ordenada; transferencia por tramos condicionados.
- Premortem y escenarios: ver 4.4-MDR.12 (tres futuros con tres objetivos y tres opciones cada uno).

## 10b. Cadena de 5 porqués, causas priorizadas y causa raíz (Paso 4.6 a 4.8; INFERIDO, estatuto HIE, sin efecto estimado)

- P1. ¿Por qué existe el problema central? Porque las lecturas ópticas de PM2,5 y PM10 no se verifican frente a una referencia en los sitios de remoción (V06).
- P2. ¿Por qué el error de lectura es alto? Porque la humedad relativa (V03) y la fracción gruesa (V02) alteran la respuesta óptica sin corrección local (S2: V03→V06 = 3 y V02→V06 = 3). Respaldo del corpus: correlación de 0,73 de las partículas con la humedad en una mina a cielo abierto (Suresh et al., 2025, p. 30); corrección con estación cercana y 35 minutos de desfase que llevó el R² de menos de 0,2 a 0,81 en Seúl (Bang et al., 2026, pp. 6-8).
- P3. ¿Por qué no hay corrección local? Porque la calibración es estática o inexistente (V07→V06 = 3) y no hay referencias colocalizadas: 90,8 % de las 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13; el 90,8 % es cálculo del analista).
- P4. ¿Por qué no se calibra en el sitio? Porque la calibración depende de referencias costosas, de energía y de enlace estables, y la remoción de escombros (V05) degrada la disponibilidad de nodos (S2: V05→V09 = 2) y expone los cabezales al polvo.
- P5. Causa raíz (hipótesis de diseño, INFERIDO): la red de bajo costo opera sin un protocolo de calibración colocalizada y de corrección en el borde con custodia institucional, adaptado a sitios de remoción de escombros. El expediente E3 declaraba como causa raíz la 'arquitectura dependiente de la nube'; ninguna de las 15 variables la representa, por lo que se trata como hipótesis rival.
- Causas priorizadas (S2, corte por mediana: I = 5 y D = 5): V06 (crítica; I 8, D 13) es el problema central; V02 (crítica; I 7, D 6); V15 (crítica; I 7, D 7); V03 (activa; I 6, D 0); V05 (activa; I 7, D 1); V07 (frontera; I 5, D 2). Intervención: calibración colocalizada y corrección en gateway (V06, V02, V03, V07), disponibilidad con energía y enlace redundantes (V05→V09) y co-diseño del uso institucional (V15). Todas las relaciones son hipótesis de influencia estructural.

## 10c. Formalización tripartita del problema (Paso 5; texto base reutilizable)

- Metaproblema: los sistemas de vigilancia ambiental de bajo costo desplegados en contextos de desastre carecen de calibración colocalizada y de corrección local, por lo que entregan mediciones de material particulado de calidad desconocida. Esa condición lleva a decidir alertas con datos sin error conocido, afecta a operarios de remoción y a población expuesta, y mantiene un ciclo en el que la baja confianza reduce el uso institucional de las mediciones. Evidencia de nivel sistémico: 90,8 % de las estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13).
- Problema sustantivo: en los sitios de remoción de escombros de Caldas, Cundinamarca y Valle del Cauca (SUPUESTO), los comités de gestión del riesgo no disponen de mediciones de PM2,5 y PM10 con error conocido frente a una referencia. El expediente E3 declara un error normalizado superior a 45 % en sensores ópticos sin calibración dinámica en alta humedad (DECLARADO, sin localizador; NO_VERIFICADO); la línea base propia se mide en el tramo 1. Contexto nacional (F-INF): 209 estaciones reportadas, 154 integradas a un sistema de vigilancia; solo 28 de 1.122 municipios con estaciones utilizables para estimar la carga (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). El PDD, el Anexo 4 y los CONPES citados por E3 no se aportaron (NO_VERIFICADO).
- Problema formal: Y = NRMSE de los nodos frente a la referencia colocalizada (V06), en porcentaje. Variables independientes: X1 = humedad relativa (V03; moderadora de la respuesta óptica); X2 = fracción gruesa (V02 menos V01); X3 = frecuencia y calidad de calibración (V07). Moderadora M = disponibilidad de nodos (V09). Controles C = temperatura, edad del cabezal y distancia a la referencia (variables omitidas del modelo de 15, a evaluar en una matriz de 19). Valor actual de Y: [VACIO: se mide en el tramo 1]. Meta: NRMSE ≤ 30 % y R² ≥ 0,70 (EPA, 2021) al mes 24; NMAE ≤ 15 % aspiracional. Horizonte: 24 meses.
- Incógnitas principales: línea base de error por departamento; completitud real de datos en sitios de remoción; capacidad de absorción de los custodios (ICAR, NO_CALCULABLE); fórmula local del índice y umbrales; disponibilidad real del enlace celular y satelital en los sitios.

## 11. Decisiones de formulación (registro DEC-F)

- DEC-F01 Fuente de financiación y estructura: el expediente mezcla 'Convocatoria 56 MinCiencias' y 'SGR/OCAD/MGA'. Se adopta la denominación 'Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)' del Paso 1 del usuario. Los términos de referencia no se aportaron: la estructura de 21 capítulos es la del metaprompt (SUPUESTO) y los datos que solo el usuario posee se marcan [DATO_USUARIO].
- DEC-F02 Arquitectura: la corrección ocurre en el gateway; los nodos hoja usan LoRa y bajo consumo; los gateways usan red celular con enlace satelital alterno y almacenamiento local de 7 días (corrige HR-12 y HR-13).
- DEC-F03 Estrategia de despliegue: R4 de 4.4-MDR (tramos con piloto de contraste y custodia distribuida), con compuertas C1 y C2 que liberan las compras del tramo siguiente.
- DEC-F04 Meta de desempeño: R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia (ancla EPA, 2021); NMAE ≤ 15 % aspiracional; línea base medida en el tramo 1 (corrige HR-14: tres metas contradictorias).
- DEC-F05 TRL final 7 (no 8): demostración en entorno operativo; TRL 8 exige calificación independiente que el plazo no cubre.
- DEC-F06 Presupuesto: se solicita la suma justificada por actividad (66,2 % del tope), no el tope; la holgura se describe como opciones sin presupuestar (corrige HR-10).
- DEC-F07 Contrapartida: 2.110 M (IES 1.100 en especie; empresa 210 en efectivo y 800 en especie), valores del expediente E3 con desglose de la IES reconstruido; certificaciones pendientes; las alcaldías no aportan (VACIO).
- DEC-F08 Cronograma: red de 17 actividades con ruta crítica igual a la duración (104 semanas); importación de 12 semanas máximo por lote; compras por tramo y no 100 % en la semana 2 (corrige HR-11).
- DEC-F09 Alternativa seleccionada: ALT-03 híbrida por tramos, condicionada a la ratificación del panel; el puntaje no se interpreta como probabilidad de éxito.
- DEC-F10 Indicadores: los de impacto (S) se miden 6 a 12 meses tras el cierre y por una evaluación externa; las líneas base VACIO se miden en el tramo 1.
- DEC-F11 Escenarios estratégicos: el metaprompt sugiere probabilidades 25/50/20/5; se omiten porque ninguna tiene fuente (NTC 1.1). Los escenarios se presentan sin probabilidad y con condiciones de activación.
- DEC-F12 Articulación territorial (Paso 5.0): los ocho elementos del checklist quedan NO_VERIFICADO por falta de PDD, CONPES y anexos. La regla bloqueante del metaprompt exige regresar a Gate 0; se continúa por orden expresa del usuario (13-oct-2026) con la reserva R-ART registrada en el cierre.
- DEC-F13 Estética: se aplica la paleta y la jerarquía tipográfica del usuario; excepción a FIG-02: opacidad 0,25 solo en la cuadrícula; el relleno de encabezados de tabla usa #B9D9EB con texto #2A3439 (contraste superior a 4,5:1; el texto sobre #6699CC no lo alcanza) y #6699CC como filete inferior del encabezado; filas alternas #F7F7F7.
- DEC-F14 Numeración: tablas y figuras 'c.n' por capítulo; Parte I con prefijo F (F5.1), paquete 1000X con prefijo X (X6.1) y anexos con letra (A1).
- DEC-F15 GWO no se activa porque el espacio de decisión (4 alternativas) es enumerable (AS-32).

## 12. Reglas de coherencia obligatorias

1. Una cifra, una fuente: cualquier cifra cardinal sale de este archivo. 2. Una definición del lugar de corrección (gateway). 3. Una meta de error (R² y NRMSE; NMAE ≤ 15 % aspiracional) y una línea base medida en el tramo 1. 4. TRL 4 → 7. 5. 24 meses y 104 semanas. 6. 100 nodos y 10 gateways operativos; 120 y 11 comprados. 7. SGR solicitado y contrapartida según §5. 8. Ninguna afirmación causal sobre salud: los resultados son técnicos, de adopción y de continuidad (H36-11). 9. Ninguna probabilidad sin fuente. 10. Lenguaje: sin metáforas ni adjetivos enfáticos; sin 'garantiza', 'demuestra matemáticamente' ni 'inédito'.
