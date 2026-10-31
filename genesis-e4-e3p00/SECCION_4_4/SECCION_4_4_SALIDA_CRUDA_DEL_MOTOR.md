## 4.4. Vester y MICMAC: análisis estructural paritario

CASE_ID: SGR_CONV56_AIRE
Motor: 36.10-RC2-VM-PAR3-MDR3-CONT1

**Estado:** CÁLCULOS EJECUTADOS POR ESCENARIO; RATIFICACIÓN DE JUICIOS PENDIENTE. Este archivo verifica operaciones, no causalidad.

### 4.4.1 Procedencia y estado de los objetos

Se preserva la matriz formal. Los valores numéricos heredados siguen siendo declarados. No se eleva la autorización del traspaso.

### 4.4.2 Diccionario y anclas de escala

| ID | Nombre | Definición aportada |
| --- | --- | --- |
| V01 | Concentración PM2.5 | Masa de partículas &lt;2,5 µm (µg/m³). |
| V02 | Concentración PM10 | Masa de partículas &lt;10 µm (µg/m³). |
| V03 | Humedad relativa | Saturación de vapor de agua (%). |
| V04 | Velocidad del viento | Fuerza de dispersión eólica superficial (m/s). |
| V05 | Volumen de escombros | Residuos removidos tras el sismo (t/día). |
| V06 | Error de medición IoT | Desfase metrológico del sensor láser (NMAE %). |
| V07 | Frecuencia de calibración | Tasa de ajuste algorítmico del gemelo (ajustes/semana). |
| V08 | Latencia de datos | Retraso en la transmisión a la nube central (minutos). |
| V09 | Disponibilidad de nodos IoT | Porcentaje de la red de sensores activa y con energía (%). |
| V10 | Densidad del gemelo | Resolución del mapa predictivo espacial (nodos/km²). |
| V11 | Índice AQHI | Nivel de peligro de salud pública emitido (escala 1-10). |
| V12 | Falsas alarmas | Tasa de alertas emitidas sin superación de umbral real (%). |
| V13 | Anticipación | Tiempo de aviso preventivo antes del impacto (horas). |
| V14 | Personas alertadas | Población y operarios bajo protección efectiva (conteo). |
| V15 | Adopción institucional | Uso efectivo del tablero por alcaldías y UNGRD (%). |

La escala 0–3 es ordinal. Las anclas del caso deben justificar magnitud y alcance; no se deducen de densidad ni del número de fuentes.

### 4.4.3 Plan paritario reproducible

El archivo PLAN_PARITARIO.csv conserva 105 pares y dos sentidos por par. Semilla: 20261011. Paritario no implica simétrico.

### 4.4.4 Fichas y cobertura

Conteos de fichas (sin certificación semántica): {"fichas_recibidas": 105, "fichas_bidireccionales_validas": 105, "fichas_con_justificacion_declarada": 105, "fichas_con_dos_valores_propuestos": 105, "fichas_con_adjudicacion_documentada": 0, "direcciones_recibidas_unicas": 210, "direcciones_con_justificacion_declarada": 210, "direcciones_con_valor_propuesto": 210, "direcciones_con_adjudicacion_documentada": 0, "fichas_semanticamente_verificadas": null}. Estado: ESQUEMA_COMPLETO_NO_VALIDACION_CIENTIFICA

Errores específicos: Ninguno de esquema

### 4.4.5 Matriz formal y matrices de trabajo

| Origen / Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | U | U | U | U | 2 | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V02 | U | 0 | U | U | U | 3 | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V03 | 1 | 1 | 0 | U | U | 3 | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V04 | 2 | 2 | U | 0 | U | U | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V05 | 3 | 3 | U | U | 0 | U | U | U | U | U | U | U | U | U | U | PENDIENTE |
| V06 | U | U | U | U | U | 0 | U | U | U | U | 3 | 3 | U | U | U | PENDIENTE |
| V07 | U | U | U | U | U | 3 | 0 | U | 1 | U | U | U | U | U | U | PENDIENTE |
| V08 | U | U | U | U | U | U | U | 0 | U | U | U | U | 2 | U | U | PENDIENTE |
| V09 | U | U | U | U | U | U | U | U | 0 | 3 | U | U | U | U | U | PENDIENTE |
| V10 | U | U | U | U | U | 2 | U | U | U | 0 | 3 | U | U | U | U | PENDIENTE |
| V11 | U | U | U | U | U | U | U | U | U | U | 0 | 2 | U | 3 | U | PENDIENTE |
| V12 | U | U | U | U | U | U | U | U | U | U | U | 0 | U | U | 3 | PENDIENTE |
| V13 | U | U | U | U | U | U | U | U | U | U | U | U | 0 | 3 | U | PENDIENTE |
| V14 | U | U | U | U | U | U | U | U | U | U | U | U | U | 0 | 2 | PENDIENTE |
| V15 | U | U | U | U | U | U | U | U | U | U | U | U | U | U | 0 | PENDIENTE |
| TP | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE | PENDIENTE |

**S1_PREVIO_DOC**. Matriz S1_TRABAJO_PROPUESTO del Paso 4 (4.4.5) del documento Problematica E3-P00; juicios previos no ratificados y sin fichas completas.

| Origen / Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 |
| V03 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V04 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V05 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 6 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V08 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 4 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| V10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 5 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 5 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 4 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| TP | 6 | 6 | 0 | 0 | 0 | 15 | 2 | 2 | 6 | 3 | 7 | 5 | 2 | 8 | 5 | 67 |

**S3_ENVOLVENTE_ADMISIBLE_BAJA**. Cada dirección toma el mínimo de sus valores admisibles declarados en las fichas. Envolvente de sensibilidad, no predictiva ni adjudicada.

| Origen / Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 |
| V02 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V03 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V04 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V05 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 3 |
| V07 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| V10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 2 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| V15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 2 |
| TP | 3 | 3 | 0 | 0 | 0 | 7 | 0 | 0 | 2 | 0 | 5 | 2 | 1 | 4 | 2 | 29 |

**S4_ENVOLVENTE_ADMISIBLE_ALTA**. Cada dirección toma el máximo de sus valores admisibles declarados en las fichas. Envolvente de sensibilidad, no predictiva ni adjudicada.

| Origen / Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 7 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 1 | 0 | 8 |
| V03 | 1 | 1 | 0 | 0 | 1 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| V04 | 3 | 3 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 13 |
| V05 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 10 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 3 | 3 | 0 | 0 | 1 | 10 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V08 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 1 | 0 | 3 | 0 | 1 | 8 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 5 |
| V10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 3 | 2 | 2 | 0 | 0 | 10 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 3 | 2 | 9 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 3 | 7 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 3 | 1 | 0 | 1 | 1 | 3 | 0 | 12 |
| TP | 7 | 7 | 1 | 0 | 3 | 17 | 4 | 3 | 14 | 4 | 15 | 9 | 9 | 14 | 11 | 118 |

**S0_HISTORICO_CONDICIONADO**. Matriz histórica aportada; sus ceros no se trasladan como adjudicaciones a la MID formal.

| Origen / Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| V03 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V04 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| V05 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 6 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| V08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| V10 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 5 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 5 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| TP | 6 | 6 | 0 | 0 | 0 | 13 | 0 | 0 | 1 | 3 | 6 | 5 | 2 | 6 | 5 | 53 |

**S_TRABAJO_PROPUESTO**. Juicios propuestos derivados de las fichas; no equivalen a ratificación independiente.

| Origen / Destino | V01 | V02 | V03 | V04 | V05 | V06 | V07 | V08 | V09 | V10 | V11 | V12 | V13 | V14 | V15 | TA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V01 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 6 |
| V02 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 7 |
| V03 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| V04 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 8 |
| V05 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| V06 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 3 | 2 | 0 | 0 | 1 | 8 |
| V07 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| V08 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 |
| V09 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 4 |
| V10 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 5 |
| V11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 1 | 5 |
| V12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 4 |
| V13 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| V14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| V15 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 0 | 0 | 2 | 0 | 7 |
| TP | 5 | 6 | 0 | 0 | 1 | 13 | 2 | 2 | 9 | 4 | 11 | 5 | 4 | 9 | 7 | 78 |

### 4.4.6 Controles de estructura

| Escenario | TA=TP | Enlaces | Ciclos | MICMAC |
| --- | --- | --- | --- | --- |
| S1_PREVIO_DOC | 67 | 32 | True | SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX |
| S3_ENVOLVENTE_ADMISIBLE_BAJA | 29 | 21 | True | PERIODICIDAD_OBSERVADA |
| S4_ENVOLVENTE_ADMISIBLE_ALTA | 118 | 60 | True | SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX |
| S0_HISTORICO_CONDICIONADO | 53 | 22 | False | EXTINCION_DE_CAMINOS |
| S_TRABAJO_PROPUESTO | 78 | 48 | True | SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX |

Densidad, triangularidad y reciprocidad son descriptivas. Ninguna exige elevar puntuaciones o introducir ciclos.

### 4.4.7 Planos Vester

Cada escenario tiene su SVG: VESTER_<ID>.svg, con dependencia en X e influencia en Y. Corte principal aplicado: mediana. Se conserva contraste media/mediana.

### 4.4.8 Clasificación directa

**S1_PREVIO_DOC**

| ID | I | D | Rango I | Rango D | Mediana | Media |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | 3 | 6 | 13.0 | 5.0 | REACTIVA | REACTIVA |
| V02 | 4 | 6 | 9.5 | 5.0 | FRONTERA | REACTIVA |
| V03 | 6 | 0 | 2.5 | 14.0 | ACTIVA | ACTIVA |
| V04 | 5 | 0 | 5.5 | 14.0 | ACTIVA | ACTIVA |
| V05 | 8 | 0 | 1.0 | 14.0 | ACTIVA | ACTIVA |
| V06 | 6 | 15 | 2.5 | 1.0 | CRITICA | CRITICA |
| V07 | 5 | 2 | 5.5 | 11.0 | ACTIVA | ACTIVA |
| V08 | 4 | 2 | 9.5 | 11.0 | FRONTERA | AUTONOMA_RELATIVA |
| V09 | 3 | 6 | 13.0 | 5.0 | REACTIVA | REACTIVA |
| V10 | 5 | 3 | 5.5 | 9.0 | ACTIVA | ACTIVA |
| V11 | 5 | 7 | 5.5 | 3.0 | CRITICA | CRITICA |
| V12 | 4 | 5 | 9.5 | 7.5 | FRONTERA | REACTIVA |
| V13 | 3 | 2 | 13.0 | 11.0 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V14 | 2 | 8 | 15.0 | 2.0 | REACTIVA | REACTIVA |
| V15 | 4 | 5 | 9.5 | 7.5 | FRONTERA | REACTIVA |

**S3_ENVOLVENTE_ADMISIBLE_BAJA**

| ID | I | D | Rango I | Rango D | Mediana | Media |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | 3 | 3 | 2.5 | 4.5 | CRITICA | CRITICA |
| V02 | 2 | 3 | 7.0 | 4.5 | FRONTERA | CRITICA |
| V03 | 2 | 0 | 7.0 | 12.5 | FRONTERA | ACTIVA |
| V04 | 2 | 0 | 7.0 | 12.5 | FRONTERA | ACTIVA |
| V05 | 5 | 0 | 1.0 | 12.5 | ACTIVA | ACTIVA |
| V06 | 3 | 7 | 2.5 | 1.0 | CRITICA | CRITICA |
| V07 | 2 | 0 | 7.0 | 12.5 | FRONTERA | ACTIVA |
| V08 | 1 | 0 | 12.5 | 12.5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V09 | 0 | 2 | 15.0 | 7.0 | FRONTERA | REACTIVA |
| V10 | 1 | 0 | 12.5 | 12.5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V11 | 2 | 5 | 7.0 | 2.0 | FRONTERA | CRITICA |
| V12 | 1 | 2 | 12.5 | 7.0 | FRONTERA | REACTIVA |
| V13 | 2 | 1 | 7.0 | 9.0 | FRONTERA | ACTIVA |
| V14 | 1 | 4 | 12.5 | 3.0 | REACTIVA | REACTIVA |
| V15 | 2 | 2 | 7.0 | 7.0 | FRONTERA | CRITICA |

**S4_ENVOLVENTE_ADMISIBLE_ALTA**

| ID | I | D | Rango I | Rango D | Mediana | Media |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | 7 | 7 | 10.5 | 8.5 | FRONTERA | AUTONOMA_RELATIVA |
| V02 | 8 | 7 | 8.0 | 8.5 | FRONTERA | ACTIVA |
| V03 | 8 | 1 | 8.0 | 14.0 | FRONTERA | ACTIVA |
| V04 | 13 | 0 | 1.0 | 15.0 | ACTIVA | ACTIVA |
| V05 | 10 | 3 | 4.0 | 12.5 | ACTIVA | ACTIVA |
| V06 | 10 | 17 | 4.0 | 1.0 | CRITICA | CRITICA |
| V07 | 6 | 4 | 12.0 | 10.5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V08 | 8 | 3 | 8.0 | 12.5 | FRONTERA | ACTIVA |
| V09 | 5 | 14 | 13.0 | 3.5 | REACTIVA | REACTIVA |
| V10 | 10 | 4 | 4.0 | 10.5 | ACTIVA | ACTIVA |
| V11 | 9 | 15 | 6.0 | 2.0 | CRITICA | CRITICA |
| V12 | 7 | 9 | 10.5 | 6.5 | REACTIVA | REACTIVA |
| V13 | 3 | 9 | 14.0 | 6.5 | REACTIVA | REACTIVA |
| V14 | 2 | 14 | 15.0 | 3.5 | REACTIVA | REACTIVA |
| V15 | 12 | 11 | 2.0 | 5.0 | CRITICA | CRITICA |

**S0_HISTORICO_CONDICIONADO**

| ID | I | D | Rango I | Rango D | Mediana | Media |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | 2 | 6 | 13.0 | 3.5 | REACTIVA | REACTIVA |
| V02 | 3 | 6 | 9.5 | 3.5 | FRONTERA | REACTIVA |
| V03 | 5 | 0 | 4.0 | 13.0 | ACTIVA | ACTIVA |
| V04 | 4 | 0 | 6.5 | 13.0 | ACTIVA | ACTIVA |
| V05 | 6 | 0 | 1.5 | 13.0 | ACTIVA | ACTIVA |
| V06 | 6 | 13 | 1.5 | 1.0 | CRITICA | CRITICA |
| V07 | 4 | 0 | 6.5 | 13.0 | ACTIVA | ACTIVA |
| V08 | 2 | 0 | 13.0 | 13.0 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V09 | 3 | 1 | 9.5 | 10.0 | FRONTERA | AUTONOMA_RELATIVA |
| V10 | 5 | 3 | 4.0 | 8.0 | FRONTERA | ACTIVA |
| V11 | 5 | 6 | 4.0 | 3.5 | CRITICA | CRITICA |
| V12 | 3 | 5 | 9.5 | 6.5 | FRONTERA | REACTIVA |
| V13 | 3 | 2 | 9.5 | 9.0 | FRONTERA | AUTONOMA_RELATIVA |
| V14 | 2 | 6 | 13.0 | 3.5 | REACTIVA | REACTIVA |
| V15 | 0 | 5 | 15.0 | 6.5 | REACTIVA | REACTIVA |

**S_TRABAJO_PROPUESTO**

| ID | I | D | Rango I | Rango D | Mediana | Media |
| --- | --- | --- | --- | --- | --- | --- |
| V01 | 6 | 5 | 6.5 | 7.5 | FRONTERA | ACTIVA |
| V02 | 7 | 6 | 4.0 | 6.0 | CRITICA | CRITICA |
| V03 | 6 | 0 | 6.5 | 14.5 | ACTIVA | ACTIVA |
| V04 | 8 | 0 | 1.5 | 14.5 | ACTIVA | ACTIVA |
| V05 | 7 | 1 | 4.0 | 13.0 | ACTIVA | ACTIVA |
| V06 | 8 | 13 | 1.5 | 1.0 | CRITICA | CRITICA |
| V07 | 5 | 2 | 9.0 | 11.5 | FRONTERA | AUTONOMA_RELATIVA |
| V08 | 2 | 2 | 14.0 | 11.5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V09 | 4 | 9 | 11.5 | 3.5 | REACTIVA | REACTIVA |
| V10 | 5 | 4 | 9.0 | 9.5 | FRONTERA | AUTONOMA_RELATIVA |
| V11 | 5 | 11 | 9.0 | 2.0 | FRONTERA | REACTIVA |
| V12 | 4 | 5 | 11.5 | 7.5 | FRONTERA | AUTONOMA_RELATIVA |
| V13 | 2 | 4 | 14.0 | 9.5 | AUTONOMA_RELATIVA | AUTONOMA_RELATIVA |
| V14 | 2 | 9 | 14.0 | 3.5 | REACTIVA | REACTIVA |
| V15 | 7 | 7 | 4.0 | 5.0 | CRITICA | CRITICA |

### 4.4.9 MID compartida con MICMAC

La MID es idéntica a la matriz Vester de cada escenario. No se puntúa de nuevo ni se impone transitividad directa.

### 4.4.10 Influencias potenciales

Estado MIDP: NO_CONFIGURADA_NO_INFERIDA. Solo se calcula con horizonte, máscara y condiciones explícitas; nunca se inventa para llenar la sección.

### 4.4.11 Potencias exactas y criterios de parada

**S1_PREVIO_DOC**

| k | Total | Celdas no nulas |
| --- | --- | --- |
| 1 | 67 | 32 |
| 2 | 280 | 47 |
| 3 | 1205 | 68 |
| 4 | 4855 | 95 |
| 5 | 19154 | 122 |
| 6 | 80500 | 136 |
| 7 | 349230 | 143 |
| 8 | 1484060 | 148 |
| 9 | 6071508 | 150 |
| 10 | 24573040 | 150 |

Estado: SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX. Potencia de referencia: 10. Primera nula: None.

Cada potencia completa con TA y TP está en CSV y en el JSON. En extinción se interpreta la última NO nula, no la tabla de ceros.

**S3_ENVOLVENTE_ADMISIBLE_BAJA**

| k | Total | Celdas no nulas |
| --- | --- | --- |
| 1 | 29 | 21 |
| 2 | 58 | 26 |
| 3 | 100 | 31 |
| 4 | 133 | 32 |
| 5 | 167 | 31 |
| 6 | 169 | 32 |
| 7 | 167 | 31 |
| 8 | 169 | 32 |
| 9 | 167 | 31 |
| 10 | 169 | 32 |

Estado: PERIODICIDAD_OBSERVADA. Potencia de referencia: 10. Primera nula: None.

Cada potencia completa con TA y TP está en CSV y en el JSON. En extinción se interpreta la última NO nula, no la tabla de ceros.

**S4_ENVOLVENTE_ADMISIBLE_ALTA**

| k | Total | Celdas no nulas |
| --- | --- | --- |
| 1 | 118 | 60 |
| 2 | 856 | 125 |
| 3 | 6249 | 172 |
| 4 | 44281 | 189 |
| 5 | 312165 | 193 |
| 6 | 2210258 | 195 |
| 7 | 15707903 | 195 |
| 8 | 111521718 | 195 |
| 9 | 791024704 | 195 |
| 10 | 5608709083 | 195 |

Estado: SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX. Potencia de referencia: 10. Primera nula: None.

Cada potencia completa con TA y TP está en CSV y en el JSON. En extinción se interpreta la última NO nula, no la tabla de ceros.

**S0_HISTORICO_CONDICIONADO**

| k | Total | Celdas no nulas |
| --- | --- | --- |
| 1 | 53 | 22 |
| 2 | 189 | 23 |
| 3 | 672 | 27 |
| 4 | 1521 | 19 |
| 5 | 1548 | 7 |
| 6 | 216 | 1 |
| 7 | 0 | 0 |

Estado: EXTINCION_DE_CAMINOS. Potencia de referencia: 6. Primera nula: 7.

Cada potencia completa con TA y TP está en CSV y en el JSON. En extinción se interpreta la última NO nula, no la tabla de ceros.

**S_TRABAJO_PROPUESTO**

| k | Total | Celdas no nulas |
| --- | --- | --- |
| 1 | 78 | 48 |
| 2 | 403 | 99 |
| 3 | 1974 | 151 |
| 4 | 9427 | 179 |
| 5 | 45846 | 189 |
| 6 | 224551 | 192 |
| 7 | 1101608 | 195 |
| 8 | 5373011 | 195 |
| 9 | 26172826 | 195 |
| 10 | 127613540 | 195 |

Estado: SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX. Potencia de referencia: 10. Primera nula: None.

Cada potencia completa con TA y TP está en CSV y en el JSON. En extinción se interpreta la última NO nula, no la tabla de ceros.

### 4.4.12 Plano indirecto y cambios de rango

**S1_PREVIO_DOC**

| ID | Rango I inicial | Rango I indirecto | Ascenso I | Ascenso D | Clase indirecta |
| --- | --- | --- | --- | --- | --- |
| V01 | 13.0 | 13.0 | 0.0 | -8.0 | AUTONOMA_RELATIVA |
| V02 | 9.5 | 9.0 | 0.5 | -8.0 | AUTONOMA_RELATIVA |
| V03 | 2.5 | 2.0 | 0.5 | 1.0 | ACTIVA |
| V04 | 5.5 | 7.0 | -1.5 | 1.0 | ACTIVA |
| V05 | 1.0 | 1.0 | 0.0 | 1.0 | ACTIVA |
| V06 | 2.5 | 4.0 | -1.5 | -6.0 | CRITICA |
| V07 | 5.5 | 3.0 | 2.5 | 5.0 | CRITICA |
| V08 | 9.5 | 12.0 | -2.5 | 2.0 | AUTONOMA_RELATIVA |
| V09 | 13.0 | 10.0 | 3.0 | 1.0 | REACTIVA |
| V10 | 5.5 | 5.0 | 0.5 | 1.0 | FRONTERA |
| V11 | 5.5 | 11.0 | -5.5 | 1.0 | REACTIVA |
| V12 | 9.5 | 8.0 | 1.5 | 4.5 | FRONTERA |
| V13 | 13.0 | 15.0 | -2.0 | 1.0 | AUTONOMA_RELATIVA |
| V14 | 15.0 | 14.0 | 1.0 | -3.0 | REACTIVA |
| V15 | 9.5 | 6.0 | 3.5 | 6.5 | CRITICA |

**S3_ENVOLVENTE_ADMISIBLE_BAJA**

| ID | Rango I inicial | Rango I indirecto | Ascenso I | Ascenso D | Clase indirecta |
| --- | --- | --- | --- | --- | --- |
| V01 | 2.5 | 3.0 | -0.5 | -5.0 | FRONTERA |
| V02 | 7.0 | 5.0 | 2.0 | -5.0 | FRONTERA |
| V03 | 7.0 | 5.0 | 2.0 | 3.0 | FRONTERA |
| V04 | 7.0 | 2.0 | 5.0 | 3.0 | FRONTERA |
| V05 | 1.0 | 1.0 | 0.0 | 3.0 | FRONTERA |
| V06 | 2.5 | 7.0 | -4.5 | -8.5 | FRONTERA |
| V07 | 7.0 | 5.0 | 2.0 | 3.0 | FRONTERA |
| V08 | 12.5 | 8.5 | 4.0 | 3.0 | FRONTERA |
| V09 | 15.0 | 15.0 | 0.0 | 5.5 | REACTIVA |
| V10 | 12.5 | 8.5 | 4.0 | 3.0 | FRONTERA |
| V11 | 7.0 | 11.5 | -4.5 | -7.5 | FRONTERA |
| V12 | 12.5 | 11.5 | 1.0 | -2.5 | FRONTERA |
| V13 | 7.0 | 11.5 | -4.5 | -0.5 | FRONTERA |
| V14 | 12.5 | 11.5 | 1.0 | 1.5 | REACTIVA |
| V15 | 7.0 | 14.0 | -7.0 | 4.0 | REACTIVA |

**S4_ENVOLVENTE_ADMISIBLE_ALTA**

| ID | Rango I inicial | Rango I indirecto | Ascenso I | Ascenso D | Clase indirecta |
| --- | --- | --- | --- | --- | --- |
| V01 | 10.5 | 8.0 | 2.5 | -4.0 | FRONTERA |
| V02 | 8.0 | 7.0 | 1.0 | -4.0 | ACTIVA |
| V03 | 8.0 | 4.0 | 4.0 | -0.5 | ACTIVA |
| V04 | 1.0 | 1.0 | 0.0 | 0.5 | ACTIVA |
| V05 | 4.0 | 3.0 | 1.0 | 2.5 | ACTIVA |
| V06 | 4.0 | 2.0 | 2.0 | -8.0 | ACTIVA |
| V07 | 12.0 | 9.0 | 3.0 | 2.5 | FRONTERA |
| V08 | 8.0 | 12.0 | -4.0 | 1.5 | AUTONOMA_RELATIVA |
| V09 | 13.0 | 13.0 | 0.0 | 0.5 | REACTIVA |
| V10 | 4.0 | 6.0 | -2.0 | 4.5 | CRITICA |
| V11 | 6.0 | 10.0 | -4.0 | -3.0 | REACTIVA |
| V12 | 10.5 | 11.0 | -0.5 | 2.5 | REACTIVA |
| V13 | 14.0 | 15.0 | -1.0 | -0.5 | REACTIVA |
| V14 | 15.0 | 14.0 | 1.0 | 2.5 | REACTIVA |
| V15 | 2.0 | 5.0 | -3.0 | 3.0 | CRITICA |

**S0_HISTORICO_CONDICIONADO**

| ID | Rango I inicial | Rango I indirecto | Ascenso I | Ascenso D | Clase indirecta |
| --- | --- | --- | --- | --- | --- |
| V01 | 13.0 | 8.5 | 4.5 | -5.0 | FRONTERA |
| V02 | 9.5 | 8.5 | 1.0 | -5.0 | FRONTERA |
| V03 | 4.0 | 8.5 | -4.5 | 4.5 | FRONTERA |
| V04 | 6.5 | 8.5 | -2.0 | 4.5 | FRONTERA |
| V05 | 1.5 | 8.5 | -7.0 | 4.5 | FRONTERA |
| V06 | 1.5 | 8.5 | -7.0 | -7.5 | FRONTERA |
| V07 | 6.5 | 1.0 | 5.5 | 4.5 | FRONTERA |
| V08 | 13.0 | 8.5 | 4.5 | 4.5 | FRONTERA |
| V09 | 9.5 | 8.5 | 1.0 | 1.5 | FRONTERA |
| V10 | 4.0 | 8.5 | -4.5 | -0.5 | FRONTERA |
| V11 | 4.0 | 8.5 | -4.5 | -5.0 | FRONTERA |
| V12 | 9.5 | 8.5 | 1.0 | -2.0 | FRONTERA |
| V13 | 9.5 | 8.5 | 1.0 | 0.5 | FRONTERA |
| V14 | 13.0 | 8.5 | 4.5 | -5.0 | FRONTERA |
| V15 | 15.0 | 8.5 | 6.5 | 5.5 | FRONTERA |

**S_TRABAJO_PROPUESTO**

| ID | Rango I inicial | Rango I indirecto | Ascenso I | Ascenso D | Clase indirecta |
| --- | --- | --- | --- | --- | --- |
| V01 | 6.5 | 7.0 | -0.5 | -4.5 | ACTIVA |
| V02 | 4.0 | 4.0 | 0.0 | -5.0 | ACTIVA |
| V03 | 6.5 | 3.0 | 3.5 | 0.0 | ACTIVA |
| V04 | 1.5 | 2.0 | -0.5 | 0.0 | ACTIVA |
| V05 | 4.0 | 1.0 | 3.0 | 4.0 | ACTIVA |
| V06 | 1.5 | 5.0 | -3.5 | -6.0 | CRITICA |
| V07 | 9.0 | 8.0 | 1.0 | 3.5 | FRONTERA |
| V08 | 14.0 | 15.0 | -1.0 | -1.5 | AUTONOMA_RELATIVA |
| V09 | 11.5 | 12.0 | -0.5 | -0.5 | REACTIVA |
| V10 | 9.0 | 9.0 | 0.0 | 4.5 | REACTIVA |
| V11 | 9.0 | 10.0 | -1.0 | -1.0 | REACTIVA |
| V12 | 11.5 | 11.0 | 0.5 | 1.5 | REACTIVA |
| V13 | 14.0 | 14.0 | 0.0 | -0.5 | AUTONOMA_RELATIVA |
| V14 | 14.0 | 13.0 | 1.0 | 1.5 | REACTIVA |
| V15 | 4.0 | 6.0 | -2.0 | 4.0 | CRITICA |

### 4.4.13 Sensibilidad y reconciliación

SENSIBILIDAD_ORDINAL.json compara las codificaciones [0,1,2,3], [0,1,3,5] y [0,1,2,4]. Son pruebas de robustez de una escala ordinal, no otra evidencia del territorio.

Una ruta A→B→C contribuye a A²; no obliga a añadir A→C en la MID. Los ciclos se conservan cuando corresponden al escenario.

### 4.4.14 Interpretación, límites y cierre

Las posiciones directas e indirectas dependen de los juicios suministrados. La estabilidad observada de rangos no demuestra validez de las relaciones ni estabilidad dinámica del sistema.

No se declara alternativa ganadora, causa raíz probada ni aceptación formal E3. La revisión de fichas, anclas y evidencia permanece identificada por separado.

**ALCANCE TERMINADO:** 4.4. **No se autoriza** otra sección. El control de alcance se aplica al archivo real; no es una garantía sobre otro modelo.
