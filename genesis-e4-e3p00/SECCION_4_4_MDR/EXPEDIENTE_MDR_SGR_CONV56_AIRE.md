# Expediente técnico de 4.4-MDR — SGR_CONV56_AIRE

Estado de entrega: BORRADOR_CON_VACIOS. Fecha: 2026-10-13. Este archivo acompaña a SECCION_4_4_MDR_SGR_CONV56_AIRE.md y no forma parte del entregable.

## 1. Identificación de corrida

- **mdr:** 3.0
- **ntc:** 1.1
- **modo:** /estandar
- **perfil:** PROYECTO_CTeI
- **anfitrion:** GENESIS 36.10 RC2 VM-PAR3-MDR3-CONT1
- **fecha:** 2026-10-13
- **capacidades_utilizadas:** Python local; Chromium para inspección de SVG
- **capacidades_no_disponibles:** Verificación de normas y referencias externas; artifact_tool; verificador_ntc.py
- **autorrevision:** AUTORREVISION_SECUENCIAL
- **huellas:** Ver CONTROL_MDR: 12 de 12 programas coinciden con la huella declarada

## 2. Contrato de requisitos e invariantes

| Invariante | Objetos | Estado | Pieza |
| --- | --- | --- | --- |
| P1 | ME-05, AR-07 | ENTREGADO_CON_VACIOS | 4.4-MDR.1 y 4.4-MDR.7 |
| P2 | ARBOL_1, ARBOL_4 | ENTREGADO; A-PROB (tipo 5) en 4.5 | 4.4-MDR.2 |
| P3 | SP-08 | ENTREGADO_CON_VACIOS; cálculos NO_CALCULABLE | 4.4-MDR.10 |
| P4 | TC-06 | ENTREGADO | 4.4-MDR.8 |

## 3. Registro de fuentes y afirmaciones

| ID | Afirmación | Naturaleza | Verificación | Fuente |
| --- | --- | --- | --- | --- |
| A-01 | La convocatoria fija un tope de 14.000 millones de COP | DECLARADO | NO_VERIFICADO | F-E3 (cita TdR pp. 7-8 y 25; TdR no aportados) |
| A-02 | El territorio es Caldas, Cundinamarca y Valle del Cauca; la alianza es IES, empresa y alcaldías | SUPUESTO | NO_APLICA: instrucción del usuario | Encargo |
| A-03 | El error normalizado supera 45 % sin corrección | DECLARADO | NO_VERIFICADO | F-E3, Paso 1 (F_REV_SISTEMATICA sin localizador) |
| A-04 | Las metas del error de V06 son menos de 30 %, 15 % o menos y menos de 15 % | DOCUMENTADO | CONTRADICTORIO | F-E3, K02, Paso 5 y Tabla 5.1 |
| A-05 | La correlación entre humedad y partículas es 0,73 (F-INF) o 0,48 (F-E3) | DOCUMENTADO | CONTRADICTORIO | F-INF §8.3; F-E3 3.15, 4.6 y ND-11 |
| A-06 | La corrección con estación cercana elevó R² de menos de 0,2 a 0,81 | DOCUMENTADO | NO_VERIFICADO | F-INF §3.1 y §8.3 (cita secundaria) |
| A-07 | El 90,8 % de las estaciones propuestas carecería de plan de calibración | DOCUMENTADO | NO_VERIFICADO | F-INF §8.3 (cita secundaria) |
| A-08 | El 16,8 % de las estaciones brasileñas está inactivo o sin estado | DOCUMENTADO | NO_VERIFICADO | F-INF §6.5 (cita secundaria) |
| A-09 | V06 es crítica en los cinco escenarios de 4.4 | CALCULADO | PARCIALMENTE_VERIFICADO: motor oficial y plantilla recalculada coinciden en A1 a A6; las fichas no están ratificadas | RESULTADOS_4_4 |
| A-10 | V15 participa en 140 de 144 ciclos simples de S2 | CALCULADO | PARCIALMENTE_VERIFICADO: una sola implementación | 4.4.13 |
| A-11 | Participación máxima 63,2 % e índice HHI 0,472 en el año 1 del portafolio declarado | CALCULADO | VERIFICADO: aritmética exacta recalculable; cifras de entrada NO_VERIFICADO | F-E3, Tabla 14.2; mdr_calc.py |
| A-12 | Costo parcial declarado de 190; 208,25 y 226,91 millones de COP por año | DECLARADO | NO_VERIFICADO | F-E3, Tabla 14.2 |
| A-13 | El equilibrio del juego de custodia es (N, N) | INFERIDO | NO_VERIFICADO | F-INF §6.5 (Juego 1) |
| A-14 | Una fase 0 de 12 meses debe preceder la compra masiva | DOCUMENTADO | NO_VERIFICADO | F-INF §8.3 (D-03) |
| A-15 | Diseño alternado de 52 semanas; 5.200 nodo-semanas; diferencia mínima detectable 0,034 | CALCULADO | PARCIALMENTE_VERIFICADO: cálculo recalculado sobre premisas NO_VERIFICADAS | 4.3.6; F-INF §11.7 y §11.8 |
| A-16 | Las alcaldías responden legalmente por actuar sobre la alerta | DECLARADO | NO_VERIFICADO | F-E3, E3-P17 |
| A-17 | La institución ejecutora carece de recursos permanentes; aporta personal en especie | DECLARADO | CONTRADICTORIO | F-E3, E3-P17 §13 y Tabla 14.2 |
| A-18 | El desglose del Capítulo 8 documenta 4.448,7 de 14.000 millones | CALCULADO | PARCIALMENTE_VERIFICADO: suma de rubros del expediente | F-E3, Cap. 8 |
| A-19 | El problema declara colapso celular y eléctrico y la alternativa transmite por enlace 4G con 100 tarjetas SIM | DOCUMENTADO | CONTRADICTORIO | F-E3, 4.6 y Tabla 8.3 |
| A-20 | Las elecciones territoriales siguientes son en octubre de 2027, con posesión en enero de 2028 | INFERIDO | NO_VERIFICADO: CANDIDATO_A_VERIFICAR | Conocimiento externo |
| A-21 | Derechos a la salud y a un ambiente sano; competencia territorial en gestión del riesgo | INFERIDO | NO_VERIFICADO: CANDIDATO_A_VERIFICAR | Conocimiento externo |
| A-22 | Diez solicitudes PCT designan a Colombia y tres plazos siguen abiertos | DOCUMENTADO | NO_VERIFICADO | F-INF §8.3 (D-01) |
| A-23 | Existen cuatro versiones del lugar de calibración | DOCUMENTADO | CONTRADICTORIO | F-E3, E3-P09, E3-P15, Paso 1 y Paso 6 |
| A-24 | La suma ponderada de E3-P14 arroja 0,795; 0,535; 0,460 y 0,325 | DOCUMENTADO | VERIFICADO: aritmética recalculada; pesos SUPUESTO y utilidades sin evidencia | F-E3, E3-P14 |
| A-25 | Instrumentos de financiación y reglas fiscales aplicables | INFERIDO | NO_VERIFICADO: CANDIDATO_A_VERIFICAR | Conocimiento externo |

Objetos de entrada con huella SHA-256:

| Objeto | Versión | SHA-256 |
| --- | --- | --- |
| F-INF | 1 | 29f443a909e831b751fb39f0f43d5aec838a55177b32a5a89eb34cbbd7b4fc0b |
| F-E3 | 1 | ad06c90bd70a4d9217567f8eb4aff4771f3c92b5d961b7e60e8d90a126bd6801 |
| PLANTILLA_VM | 1 | 9155d355c7cc29b02eeb2c64b826768deb605a3bac6e59a84c87b2927ede1497 |
| SECCION_4_3 | 1 | 819ac18380f5957060adabdc7b04ffbcc44b835f1d6d00114035792307417ab4 |
| SECCION_4_4 | 1 | 623ae50cf0472b7bf6b4a38283ad733713d1b85dd0acbad39fd477e6eac516ea |
| RESULTADOS_4_4 | 1 | 452990c1f3ef37bec031172afb9a88bc991e21ef15f23b39734e0d1caad9ec19 |
| FICHAS_PARITARIAS | 1 | 68aff6b7443a52caf0847ac1fe45df66d0c30e5e5ef65e01c22b11d41d9fcd83 |

## 4. Productos de las nueve fases

Cada producto lleva case_id, object_id, versión, fase, fuentes, estado, vacíos, puerta y reentradas. Las puertas posibles son AVANZA, AVANZA_CON_RESERVA y REINGRESA.

### FD-01 — Ficha de construcción y diagnóstico (fase F1, pieza 4.4-MDR.3)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **pregunta_rectora:** ¿Qué fenómeno existe, cómo se representa y en qué dominio causal se ubica?
- **delimitacion:** {"territorio": "SUPUESTO", "horizonte_meses": 36, "unidad_decisora": "Equipo formulador (POR_IDENTIFICAR)"}
- **representacion_dominante:** Limitación técnica de medición y comunicaciones (F-E3, E3-P07)
- **marcos_rivales:** ["Control en la fuente y salud ocupacional", "Gestión del riesgo de desastres como servicio", "Metrología y acreditación"]
- **restricciones_normativas:** {"tope_14000_millones": "DECLARADO; NO_VERIFICADO", "derecho_salud_ambiente": "CANDIDATO_A_VERIFICAR", "competencia_gestion_riesgo": "CANDIDATO_A_VERIFICAR"}
- **C1:** NO_CUMPLE
- **C2:** CUMPLE_CON_RESERVA
- **C3:** CUMPLE
- **C4:** NO_CUMPLE
- **clasificacion_estructura:** PARCIALMENTE_ESTRUCTURADO
- **rasgos_perversos:** NO_ACTIVADO
- **escala:** PROBLEMA_PUBLICO (INFERIDO)
- **dominio:** {"medicion_con_correccion_local": "COMPLICADO", "adopcion_y_custodia": "COMPLEJO", "naturaleza": "INFERIDO"}
- **vacios:** ["Línea base de error", "TdR", "Fórmula local del índice (V-AQHI-01)", "Población expuesta"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** Vacíos no impiden clasificar; condicionan el uso
- **reentradas:** []

### AE-02 — Ficha de entorno (fase F2, pieza 4.4-MDR.4)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **condicionantes:** ["Humedad y polvo higroscópico", "Maquinaria de remoción", "Infraestructura colapsada", "Estaciones de referencia (cobertura VACIO)", "Tope de 14.000 millones", "Capacidad local"]
- **reglas_formales:** ["TdR (VACIO)", "Normas de gestión del riesgo (CANDIDATO_A_VERIFICAR)", "Anualidad presupuestal (CANDIDATO_A_VERIFICAR)", "Propiedad industrial (F-INF §8.3)"]
- **reglas_informales:** ["Compra de sensores sin plan de calibración (F-INF §6.5)", "Equipos en bodegas municipales (F-E3; NO_VERIFICADO)"]
- **estrategias_favorecidas:** ["Novedad tecnológica visible", "Entrega de activos antes que servicios", "Asignación de operación en la matriz de responsabilidades"]
- **estrategias_penalizadas:** ["Piloto previo y compra por tramos", "Control de polvo en la fuente"]
- **restricciones_de_continuidad:** ["Anualidad presupuestal", "Calendario electoral (oct. 2027; posesión ene. 2028)", "Rotación de personal", "Plazos de liquidación", "Vencimientos de propiedad industrial"]
- **vacios:** ["Cobertura de referencias", "Reglas del instrumento sobre gasto recurrente", "Calendario real de inicio"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** TdR ausentes
- **reentradas:** []

### MA-03 — Mapa de actores (fase F3, pieza 4.4-MDR.5)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **actores:** 12
- **relevancia:** NO_EVALUADO salvo el convocante (poder ALTO, DECLARADO)
- **capacidad_de_custodia_preliminar:** VACIO
- **juego:** {"jugadores": "Dos entidades territoriales", "pagos_ordinales": "(3,3),(1,4),(4,1),(2,2)", "equilibrio": "(N, N)", "naturaleza": "INFERIDO", "fuente": "F-INF §6.5"}
- **red_de_actores:** NO_APLICA: sin datos relacionales
- **vacios:** ["Compromisos escritos", "Poder, legitimidad y urgencia con evidencia", "Participación de afectados"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** Relevancia sin evidencia
- **reentradas:** []

### EN-04 — Ficha de encuadre (fase F4, pieza 4.4-MDR.6)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **E1:** MEDIO en medición; BAJO en adopción y custodia
- **E2:** INCREMENTAL en medición; ESTRUCTURAL en custodia
- **E3:** MEDIO
- **E4:** PARCIALMENTE_REVERSIBLE
- **cuadrante_MBL:** {"medicion": "Frontera Q1-Q3", "custodia": "Q4"}
- **cuadrante_MTT:** Frontera T3-T4
- **contraste_dominio:** Coherente en ambas partes
- **modelos_compatibles:** ["Exploración mixta", "Racionalidad limitada (con reserva)", "Estructuración participativa (solo custodia)"]
- **modelo_seleccionado:** Exploración mixta
- **modelo_rival:** Racionalidad limitada y satisfacción
- **tensiones:** ["Modelo adecuado técnicamente y penalizado por la selectividad estratégica y el calendario electoral"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** Ejes INFERIDOS; tensión abierta
- **reentradas:** []

### ME-05 — Ficha de alternativas y método (fase F5, pieza 4.4-MDR.7)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **criterios_registrados:** {"version": "1.0", "criterios": ["CR-1", "CR-2", "CR-3", "CR-4", "CR-5", "CR-6"]}
- **alternativas:** ["R0", "R1", "R2", "R3", "R4", "R5"]
- **metodo_id:** MDR-MT04 (matriz de compensaciones)
- **insumos:** {"desempeños": "INFERIDO; NO_VERIFICADO", "probabilidades": "VACIO", "utilidades": "VACIO", "pesos": "VACIO"}
- **procedimiento:** Matriz sin agregación y revisión de dominancia
- **resultado:** Sin dominancia confirmada; sin ganador
- **sensibilidad:** Condiciones de elección cualitativas
- **umbral_de_cambio:** NO_CALCULABLE
- **heuristicas:** Ninguna aplicada
- **auditoria_de_sesgos:** {"detectados_decisor": ["B1", "B2", "B4", "B5", "B6", "B8"], "no_detectado": ["B3"], "no_evaluado": ["B7"]}
- **limites:** ["Suma ponderada de E3 conservada como dato; no es ganador", "CR-5 NO_EVALUADO"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** Sin dominancia ni probabilidades
- **reentradas:** []

### TC-06 — Teoría del cambio (fase F6, pieza 4.4-MDR.8)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **impacto:** Operarios y comunidades protegidos por alertas basadas en mediciones verificadas
- **horizonte_meses:** 36
- **niveles:** ["Productos", "Resultados inmediatos", "Resultados intermedios", "Impacto"]
- **nodos:** 11
- **relaciones:** 12
- **supuestos:** {"SC-1": "SUPUESTO", "SC-2": "SUPUESTO", "SC-3": "SUPUESTO", "SC-4": "SUPUESTO"}
- **techo:** Después de los resultados inmediatos
- **dominio:** COMPLICADO y COMPLEJO
- **arquitectura:** Anidada
- **arquitectura_rival:** Sistémica (rechazada para la medición; reexaminar con el piloto)
- **celda_de_desajuste:** ["MDR-MX-CO-A: ADECUADA", "MDR-MX-CX-A: ADMISIBLE_CON_AJUSTE"]
- **efectos_por_dimension:** 6
- **marcos_de_cambio:** {"incentivos": "Economía política y arquitectura de decisiones", "habilidad y refuerzo": "ADKAR", "estándar de calibración": "PDCA"}
- **traduccion_a_formatos:** CANDIDATO_A_VERIFICAR
- **vacios:** ["Evidencia primaria de SC-2 y SC-3", "Cobertura de referencias"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** Supuestos SUPUESTO sin verificación
- **reentradas:** []

### AR-07 — Ficha de argumento (fase F7, pieza 4.4-MDR.9)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **Q:** CONDICIONALMENTE
- **PA:** {"PA-1": "CUMPLE para I(1), I(2), I(5); NO_CUMPLE para I(3), I(4)", "PA-2": "CUMPLE", "PA-3": "NO_EJECUTADO", "PA-4": "CUMPLE", "PA-5": "CUMPLE", "PA-6": "CUMPLE"}
- **supuestos_validados:** {"SC-1": "CONDICIONALMENTE", "SC-2": "PLAUSIBLEMENTE", "SC-3": "PLAUSIBLEMENTE", "SC-4": "CONDICIONALMENTE"}
- **evaluador:** Ninguno independiente
- **autorrevision:** true
- **argumento_sostenibilidad:** {"continuidad_tras_mes_24": "NO_SOSTENIDO", "alcaldias_asumen_opex": "NO_SOSTENIDO", "preservacion_con_clausula_de_apertura": "CONDICIONALMENTE"}
- **reentradas:** []
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** PA-3 no ejecutada; objeciones abiertas

### SP-08 — Arquitectura de sostenibilidad posproyecto (fase F8, pieza 4.4-MDR.10)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **evidencia_de_antecedentes:** DECLARADO por el usuario; evidencia parcial en redes de monitoreo (F-INF)
- **componentes:** 9
- **CTS_anual:** NO_CALCULABLE
- **cota_inferior_declarada_millones_COP:** [190.0, 208.25, 226.9125]
- **NMSV:** PROPUESTO; costo NO_CALCULABLE
- **CTS_min:** NO_CALCULABLE
- **ICAR:** NO_CALCULABLE para siete candidatos
- **asignacion_de_custodia:** POR_DEFINIR con ICAR
- **portafolio_declarado_F_E3:** {"participaciones_anio1": {"OpEx nube e IoT": 0.23684210526315788, "Mantenimiento FRU": 0.13157894736842105, "Personal técnico y soporte de algoritmos": 0.631578947368421}, "max_participacion": [0.631578947368421, 0.6050420168067226, 0.5830441249380268], "HHI": [0.47229916897506924, 0.44580185015182544, 0.4270731504079479]}
- **fondo_patrimonial:** NO_CALCULABLE
- **prueba_de_orfandad:** {"umbral_costo_minimo_anio1_millones": {"OpEx nube e IoT": 145.0, "Mantenimiento FRU": 165.0, "Personal técnico y soporte de algoritmos": 70.0}, "estado": "CONDICIONAL"}
- **tramos:** 4
- **clausula_de_apertura:** PROPUESTA; licencia VACIO
- **gobernanza:** PROPUESTA
- **instrumentos_verificados:** NINGUNO: CANDIDATO_A_VERIFICAR
- **vacios:** ["CTS completo", "ICAR", "r_real", "Costos por componente", "Evidencia de continuidad de proyectos con regalías"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** ICAR y costo mínimo ausentes; reabrir F8 y F5 cuando existan
- **reentradas:** []

### AA-09 — Plan de ejecución, evaluación y aprendizaje (fase F9, pieza 4.4-MDR.11)

- **version:** 1.0
- **estado:** BORRADOR_CON_VACIOS
- **fuentes:** ["F-INF", "F-E3", "PLANTILLA_VM", "SECCION_4_3", "SECCION_4_4", "RESULTADOS_4_4", "FICHAS_PARITARIAS"]
- **hipotesis_de_intervencion:** Si se ejecuta R4 durante 24 meses, en 36 meses se espera una diferencia detectable del logaritmo del error normalizado y al menos un tramo de custodia recibido
- **estrategia:** Piloto como producto de conocimiento; tramos como evidencia de alianza
- **indicadores:** ["Logaritmo del error normalizado por nodo-semana"]
- **linea_base:** VACIO
- **umbrales:** {"detencion_R4": "PROPUESTO", "disponibilidad_menor_80_por_ciento_tres_meses": "PROPUESTO; sin fuente", "falsas_alarmas": "PROPUESTO"}
- **ruta_evaluativa:** {"efecto_del_metodo": "RE-1", "adopcion": "RE-2", "contribucion": "RE-4", "QCA": "NO_APLICA", "cosecha": "NO_APLICA"}
- **supuestos_priorizados:** ["SC-2", "SC-3", "SC-1"]
- **frecuencia_de_revision:** Trimestral en adopción y custodia; anual en medición
- **responsable:** RESPONSABLE_POR_DESIGNAR
- **consecuencias_no_deseadas:** 5
- **punto_de_reversion:** Hito 2 (mes 12)
- **prueba_piloto:** Sorteo semanal; 52 semanas; 100 nodos y 20 % de repuestos
- **vacios:** ["Línea base", "Actualización remota de nodos", "Responsable"]
- **puerta:** AVANZA_CON_RESERVA
- **motivo_puerta:** Línea base y responsable ausentes
- **reentradas:** []

## 5. Cálculos

- **VE_arbol_decision:** {"estado": "NO_CALCULABLE", "motivo": "Sin probabilidades ni utilidades con fuente", "estructura": "VE = p1·[p2·(p3·(p4·v5 + (1 − p4)·v4) + (1 − p3)·v3) + (1 − p2)·v2] + (1 − p1)·v1"}
- **umbrales_SC:** {"estado": "NO_CALCULABLE", "criticidad_para_la_decision": "NO_CALCULABLE"}
- **ICAR:** {"estado": "NO_CALCULABLE", "motivo": "Mínimo de seis dimensiones sin evidencia", "regla": "Eslabón débil sin compensación"}
- **CTS:** {"formula": "CTS anual = operación + personal + licencias + mantenimiento + reposición + gobernanza", "estado": "NO_CALCULABLE", "cota_inferior_declarada_millones_COP": {"anio1": 190.0, "anio2": 208.25, "anio3": 226.9125}, "naturaleza": "DECLARADO (F-E3, Tabla 14.2)", "verificacion": "NO_VERIFICADO"}
- **portafolio_HHI:** {"formula": "HHI = suma de los cuadrados de las participaciones", "rotulo": "CALCULADO sobre cifras NO_VERIFICADAS", "anios": [{"anio": 1, "cts_parcial": 190.0, "participaciones": {"OpEx nube e IoT": 0.23684210526315788, "Mantenimiento FRU": 0.13157894736842105, "Personal técnico y soporte de algoritmos": 0.631578947368421}, "max_participacion": 0.631578947368421, "hhi": 0.47229916897506924, "suma_de_las_demas": {"OpEx nube e IoT": 145.0, "Mantenimiento FRU": 165.0, "Personal técnico y soporte de algoritmos": 70.0}, "umbral_cts_min_para_critica": {"OpEx nube e IoT": 145.0, "Mantenimiento FRU": 165.0, "Personal técnico y soporte de algoritmos": 70.0}}, {"anio": 2, "cts_parcial": 208.25, "participaciones": {"OpEx nube e IoT": 0.226890756302521, "Mantenimiento FRU": 0.16806722689075632, "Personal técnico y soporte de algoritmos": 0.6050420168067226}, "max_participacion": 0.6050420168067226, "hhi": 0.44580185015182544, "suma_de_las_demas": {"OpEx nube e IoT": 161.0, "Mantenimiento FRU": 173.25, "Personal técnico y soporte de algoritmos": 82.25}, "umbral_cts_min_para_critica": {"OpEx nube e IoT": 161.0, "Mantenimiento FRU": 173.25, "Personal técnico y soporte de algoritmos": 82.25}}, {"anio": 3, "cts_parcial": 226.9125, "participaciones": {"OpEx nube e IoT": 0.21864154685176004, "Mantenimiento FRU": 0.1983143282102132, "Personal técnico y soporte de algoritmos": 0.5830441249380268}, "max_participacion": 0.5830441249380268, "hhi": 0.4270731504079479, "suma_de_las_demas": {"OpEx nube e IoT": 177.3, "Mantenimiento FRU": 181.9125, "Personal técnico y soporte de algoritmos": 94.6125}, "umbral_cts_min_para_critica": {"OpEx nube e IoT": 177.3, "Mantenimiento FRU": 181.9125, "Personal técnico y soporte de algoritmos": 94.6125}}]}
- **prueba_de_orfandad:** {"regla": "Fuente CRITICA si la suma de las demás es menor que el costo mínimo", "costo_minimo": "NO_CALCULABLE", "umbrales_anio1_millones_COP": {"OpEx nube e IoT": 145.0, "Mantenimiento FRU": 165.0, "Personal técnico y soporte de algoritmos": 70.0}}
- **fondo_patrimonial:** {"formula": "K = CTS cubierto / r_real", "estado": "NO_CALCULABLE", "motivo": "Sin CTS completo ni r_real con fuente"}
- **sensibilidad:** "Condiciones de elección cualitativas (4.4-MDR.7)"

## 6. Comprobaciones

### Matriz K01 a K32

| ID | Nombre | Estado | Objeto | Método | Evidencia | Limitación |
| --- | --- | --- | --- | --- | --- | --- |
| K01 | Delimitación | CUMPLE | 4.4-MDR.3 | Lectura contra D1 | Tabla de delimitación; problema como estado observable separado de la solución preferida | La línea base del estado descrito es VACIO |
| K02 | Construcción discursiva | CUMPLE | 4.4-MDR.3 | Lectura contra D2 | Cuatro preguntas respondidas; tres marcos rivales con portador | Los marcos rivales no tienen evidencia verificada |
| K03 | Núcleo normativo | CUMPLE | 4.4-MDR.3 | Lectura contra D3 | Cada restricción cita fuente o portador; las no citables se rotulan preferencia o CANDIDATO_A_VERIFICAR | Los TdR no se aportaron: ninguna norma se verificó |
| K04 | Estructura y escala | CUMPLE | 4.4-MDR.3 | C1–C4 evaluadas con evidencia | Tabla de C1–C4; escala PROBLEMA_PUBLICO | La escala se infiere sin alcance poblacional (VACIO) |
| K05 | Entorno | CUMPLE | 4.4-MDR.4 | Lectura contra N1–N4 | Reglas formales con fuente, informales con evidencia y selectividad estratégica | Las reglas formales aplicables son VACIO o CANDIDATO_A_VERIFICAR |
| K06 | Actores | NO_CUMPLE | 4.4-MDR.5 | Lectura contra A1–A3 | Tipología y lógicas de acción registradas | La relevancia (poder, legitimidad, urgencia) quedó NO_EVALUADO para cuatro de cinco actores evaluados |
| K07 | Interdependencia | CUMPLE | 4.4-MDR.5 | Forma de juego con supuestos declarados | Juego de bien público con pagos ordinales de F-INF §6.5 | Pagos ordinales adoptados por analogía; no verificados |
| K08 | Ejes de encuadre | CUMPLE | 4.4-MDR.6 | E1–E4 puntuados antes de seleccionar el modelo | Tabla de ejes con evidencia | Los valores son INFERIDO |
| K09 | Selección del modelo | CUMPLE | 4.4-MDR.6 | Condiciones de cada modelo contrastadas | Modelo seleccionado, rival y tensión registrados | Las condiciones dependen de ejes INFERIDOS |
| K10 | Alternativas | CUMPLE | 4.4-MDR.7 | Recuento y origen | Seis alternativas; R4 y R5 diseñadas bajo PD-0 | R5 sin evidencia aportada |
| K11 | Criterios previos | CUMPLE | 4.4-MDR.7 | Registro con versión 1.0 antes de la matriz | Seis criterios con aspiraciones | Varias aspiraciones son VACIO |
| K12 | Ejecución del método | CUMPLE | 4.4-MDR.7 | Matriz de compensaciones ejecutada; demás métodos con estado | Matriz sin agregación; métodos no ejecutados con motivo | El resultado no designa ganador |
| K13 | Reproducibilidad aritmética | CUMPLE | 4.4-MDR.10 | Recálculo con fracciones exactas | Participaciones, HHI y umbrales de orfandad recalculables | Las cifras de entrada son NO_VERIFICADO |
| K14 | Sensibilidad | CUMPLE | 4.4-MDR.7 | Declaración de NO_CALCULABLE conforme a la regla de integración | Condiciones de elección cualitativas; umbral NO_CALCULABLE | Sin umbral numérico |
| K15 | Auditoría de sesgos | CUMPLE | 4.4-MDR.7 | B1–B8 por decisor y por analista y modelo | Tabla de sesgos con estado | B7 NO_EVALUADO |
| K16 | Paquete de árboles | CUMPLE | ARBOL_1 y ARBOL_4 | Auditor mecánico y render con navegador | Dos SVG completos con comprobaciones superadas | El auditor no verifica evidencia ni todo el solapamiento visual |
| K17 | Argumento completo | NO_CUMPLE | 4.4-MDR.9 | Siete elementos y pruebas PA-1 a PA-6 | Siete elementos con estado; cinco pruebas con resultado | La prueba de respaldo es NO_EJECUTADO |
| K18 | Control grupal | CUMPLE | 4.4-MDR.9 | Declaración | AUTORREVISION declarada; objeciones abiertas conservadas | No hubo evaluador independiente |
| K19 | Sostenibilidad: costos | CUMPLE | 4.4-MDR.10 | Fórmula y vacíos declarados | CTS, NMSV y costo mínimo declarados NO_CALCULABLE con cota inferior parcial | Tres de seis rubros |
| K20 | Sostenibilidad: receptores | NO_CUMPLE | 4.4-MDR.10 | Regla del eslabón débil sin compensación | Siete candidatos con evidencia disponible | Sin evidencia por dimensión: ICAR NO_CALCULABLE |
| K21 | Sostenibilidad: financiación | NO_CUMPLE | 4.4-MDR.10 | Cálculo sobre cifras de F-E3 | Participación máxima y HHI de tres años | Fondo patrimonial NO_CALCULABLE; portafolio no es diseño propio |
| K22 | Prueba de orfandad | NO_CUMPLE | 4.4-MDR.10 | Umbral por fuente | Umbrales de costo mínimo por fuente | El costo mínimo falta: la prueba es condicional |
| K23 | Tramos y salida | CUMPLE | 4.4-MDR.10 | Lectura contra SP8–SP10 | Cuatro tramos, cláusula de apertura y gobernanza | Hitos PROPUESTOS |
| K24 | Plan adaptativo | CUMPLE | 4.4-MDR.11 | Lectura contra las reglas de ejecución | Hipótesis, consecuencias, umbrales con naturaleza y punto de reversión | Umbrales PROPUESTOS |
| K25 | Redacción y separación | CUMPLE | 4.4-MDR y expediente | Revisión mecánica parcial de longitud de oración, palabras de énfasis y citas, y lectura | Oraciones de más de 25 palabras solo en supuestos SI-ENTONCES-PORQUE y referencias; ninguna palabra de énfasis; entregable sin códigos de puerta; expediente separado | Verificador oficial verificador_ntc.py NO_EJECUTADO; concordancia, tildes y gerundios revisados por lectura |
| K26 | Correcciones a la fuente | CUMPLE | 4.4-MDR.3, .6, .8 y .9 | Lectura contra CF-01 a CF-34 | Cinco dominios; Smalley sin uso clasificatorio; término «techo» como convención; Dunn como adaptación de Toulmin | Referencias NO_VERIFICADO_EN_ESTA_CORRIDA |
| K27 | Dominio causal | CUMPLE | 4.4-MDR.3 | D8 con evidencia y naturaleza | Dos partes clasificadas; observación que cambiaría la clasificación | INFERIDO |
| K28 | Arquitectura y efectos | CUMPLE | 4.4-MDR.8 | Matriz de desajuste y de efectos | Celdas, arquitectura rival rechazada y efectos por dimensión | Celdas PROPUESTAS |
| K29 | Supuestos y techo | CUMPLE | 4.4-MDR.8 | Supuestos SI-ENTONCES-PORQUE completos | Cuatro supuestos con mecanismo; techo trazado | Naturaleza SUPUESTO |
| K30 | Acoplamiento árbol-TdC | NO_CUMPLE | ARBOL_1 y ARBOL_4 | Auditor mecánico | SC-1 a SC-4 compartidos; niveles en resultados | Criticidad de los supuestos NO_CALCULABLE |
| K31 | Emisión de árboles | CUMPLE | 4.4-MDR.2 | Auditor de orden de emisión y recuento de raíces SVG | Árboles tras la síntesis; dos raíces SVG; desc no vacío; rol declarado | Verifica orden editorial, no calidad |
| K32 | Evaluación y bucle doble | CUMPLE | 4.4-MDR.11 | Recorrido de la ruta evaluativa con la pregunta real | Tres rutas elegidas y dos descartadas con motivo; revisión de supuestos programada | Frecuencias PROPUESTAS |

Resumen: {'CUMPLE': 26, 'NO_CUMPLE': 6}. Las métricas no se promedian.

### Señales S01 a S40 (revisadas según aplicabilidad)

| ID | Señal | En F-E3 | En esta corrida | Tratamiento |
| --- | --- | --- | --- | --- |
| S01 | Solución disfrazada de problema | ACTIVADA | NO_ACTIVADA | La causa raíz del expediente E3 es una arquitectura; 4.4-MDR.3 reformula el problema como estado observable |
| S02 | Representación única | ACTIVADA | NO_ACTIVADA | Tres marcos rivales registrados |
| S03 | Norma sin fuente | ACTIVADA | NO_ACTIVADA | Restricciones rotuladas como preferencia o CANDIDATO_A_VERIFICAR |
| S04 | Valor tratado como hecho | ACTIVADA | NO_ACTIVADA | Juicios de valor divergentes conservados con portador |
| S05 | Estructura sin criterio | NO_EVALUADA | NO_ACTIVADA | C1–C4 con evidencia |
| S06 | Entorno ignorado | NO_EVALUADA | NO_ACTIVADA | N1–N4 ejecutados antes del encuadre |
| S07 | Teoría de juegos sin pagos | NO_ACTIVADA | NO_ACTIVADA | Pagos ordinales declarados y reacciones como anticipación cualitativa |
| S08 | Modelo elegido antes de los ejes | NO_EVALUADA | NO_ACTIVADA | Ejes puntuados antes de seleccionar el modelo |
| S09 | Sinóptico sin requisitos | ACTIVADA | NO_ACTIVADA | La racionalidad sinóptica se descartó por incumplir condiciones |
| S10 | Método nombrado, no ejecutado | ACTIVADA | NO_ACTIVADA | Métodos no ejecutados con motivo y estado |
| S11 | Probabilidades inventadas | ACTIVADA | NO_ACTIVADA | Ninguna probabilidad asignada; árbol cualitativo |
| S12 | Criterio posterior | ACTIVADA | NO_ACTIVADA | Criterios versión 1.0 registrados antes |
| S13 | Sesgos solo del otro | NO_EVALUADA | NO_ACTIVADA | Auditoría extendida al analista y al modelo |
| S14 | Árbol ausente | NO_APLICA | NO_ACTIVADA | Árboles emitidos tras la síntesis |
| S15 | Árbol con cifras inventadas | NO_APLICA | NO_ACTIVADA | Modalidad cualitativa |
| S16 | Árbol no editable | NO_APLICA | NO_ACTIVADA | Texto editable, grupos con id |
| S17 | Calificador desproporcionado | ACTIVADA | NO_ACTIVADA | Calificadores CONDICIONALMENTE y PLAUSIBLEMENTE |
| S18 | Refutación vacía | NO_EVALUADA | NO_ACTIVADA | Cuatro condiciones observables de refutación |
| S19 | Panel simulado | NO_ACTIVADA | NO_ACTIVADA | AUTORREVISION declarada |
| S20 | Sostenibilidad omitida | NO_ACTIVADA | NO_ACTIVADA | 4.4-MDR.10 ejecutada |
| S21 | Receptor público supuesto | ACTIVADA | NO_ACTIVADA | Premisa de diseño sin receptor único; ICAR sin valor por defecto |
| S22 | Compensación en ICAR | NO_APLICA | NO_ACTIVADA | Regla del eslabón débil |
| S23 | Fuente financiera crítica | NO_EVALUADA | ACTIVADA_CONDICIONAL | El portafolio declarado en F-E3 resulta crítico si el costo mínimo supera 70 millones; reabre custodia y motor financiero cuando exista el costo mínimo |
| S24 | Instrumento no verificado | ACTIVADA | ACTIVADA | Instrumentos rotulados CANDIDATO_A_VERIFICAR |
| S25 | Antecedentes inventados | NO_EVALUADA | NO_ACTIVADA | Antecedentes con fuente o DECLARADO |
| S26 | Salida ordenada ausente | NO_EVALUADA | NO_ACTIVADA | Cláusula de apertura y manual de reactivación |
| S27 | Umbral inventado | ACTIVADA | NO_ACTIVADA | Umbrales marcados PROPUESTO |
| S28 | Atribución corregida restituida | NO_APLICA | NO_ACTIVADA | Correcciones a la fuente aplicadas |
| S29 | Andamiaje en el entregable | NO_APLICA | NO_ACTIVADA | Códigos de puerta, métricas y señales en el expediente |
| S30 | Promesa de seguimiento | NO_EVALUADA | NO_ACTIVADA | Protocolo ejecutable por el responsable |
| S31 | Árbol descrito y no dibujado | NO_APLICA | NO_ACTIVADA | SVG completos |
| S32 | Árbol al final | NO_APLICA | NO_ACTIVADA | Auditor de orden de emisión |
| S33 | Descripción vacía | NO_APLICA | NO_ACTIVADA | desc no vacío |
| S34 | Arquitectura desajustada | NO_EVALUADA | NO_ACTIVADA | Matriz de desajuste aplicada |
| S35 | Supuesto sin mecanismo | NO_EVALUADA | NO_ACTIVADA | Cuatro supuestos con PORQUE |
| S36 | Azar sin código | NO_APLICA | NO_ACTIVADA | Cada nodo de azar lleva SC-n |
| S37 | Techo ausente | ACTIVADA | NO_ACTIVADA | Metas sobre el techo reformuladas como contribución |
| S38 | Marco de cambio sin cuello | NO_EVALUADA | NO_ACTIVADA | Eslabón identificado antes de elegir el marco |
| S39 | Método evaluativo por prestigio | NO_EVALUADA | NO_ACTIVADA | Recorrido con la pregunta evaluativa |
| S40 | Cita sin fuente convertida | NO_ACTIVADA | NO_ACTIVADA | Citas secundarias rotuladas como tales |

### Otras comprobaciones

- **arboles:** {"cierres_svg_por_archivo": {"ARBOL_1": 1, "ARBOL_4": 1, "ARBOL_5": 1}, "auditor": "Ver CONTROL_MDR", "revision_visual": "EJECUTADA con navegador; etiqueta SC-3 de R3 a I1 cruza el techo con fondo blanco"}
- **AP_11_V:** {"RESULTADO": "NO_EJECUTADO", "motivo": "No se realizó el conteo por unidad exigido. Se aplicó una revisión de marcadores auxiliar que no equivale a AP-11-V", "revision_de_marcadores": "Ver CONTROL_MDR"}
- **RS_99:** {"estado": "EJECUTADA_PARCIAL", "mecanico": ["Oraciones de más de 25 palabras", "Palabras de énfasis", "Citas y referencias"], "lectura": ["Concordancia", "Tildes diacríticas", "Gerundios"], "excepciones_aplicadas": ["Supuestos SI-ENTONCES-PORQUE", "Referencias", "Fórmulas", "Títulos nominales"], "verificador_ntc.py": "NO_EJECUTADO"}
- **pruebas_de_rechazo:** NO_EJECUTADO: no se ejecutaron las pruebas de rechazo del metaprompt contra esta salida
- **validacion_empirica:** NO_EJECUTADA: comprensión, eficacia decisional y continuidad requieren casos reales

## 7. Cierre

**F-01.** Autoauditoría: contrato e invariantes P1 a P4 con estado; K01–K32 con 26 CUMPLE y 6 NO_CUMPLE; árboles con comprobaciones mecánicas superadas y dos raíces SVG en archivos; señales revisadas; AP-11-V NO_EJECUTADO; RS-99 ejecutada de forma parcial; verificador_ntc.py NO_EJECUTADO; MDR 3.0, NTC 1.1; huellas comprobadas.

**F-02.** Vacíos y contradicciones con efecto: ver 4.4-MDR.13 y open_items. Rutas: aportar TdR, adjudicar fichas, reunir evidencia de custodios, cotizar CTS completo, medir línea base, validar fórmula local, diseñar enlace alterno, fijar una definición de lugar de calibración, reconciliar presupuesto, consultar a operarios y comunidades, consultar propiedad industrial.

**F-03.** Valor estratégico: habilita decidir entre despliegue por tramos con evidencia y compromiso en bloque con receptor supuesto, y ordena la revisión humana de cuatro supuestos. La utilidad es potencial; no se afirman ahorros ni impactos medidos.

**F-04.** {
 "productos": [
  "FD-01",
  "AE-02",
  "MA-03",
  "EN-04",
  "ME-05",
  "TC-06",
  "AR-07",
  "SP-08",
  "AA-09",
  "A-DEC",
  "A-TDC",
  "A-PROB"
 ],
 "restricciones": [
  "Todas las relaciones son HIE",
  "Probabilidades y utilidades ausentes",
  "Estado de entrega BORRADOR_CON_VACIOS"
 ],
 "pendientes": [
  "V-TDR",
  "V-FICHAS",
  "V-ICAR",
  "V-CTS",
  "V-LB",
  "V-AQHI",
  "V-ENLACE",
  "V-CAL",
  "V-PPTO",
  "V-COM",
  "V-PCT"
 ],
 "siguiente_accion": "Sesión de revisión humana de SC-1 a SC-4 y de los 14 enlaces de mayor efecto; aportar TdR",
 "condicion_de_aceptacion": "Revisión independiente de las fichas, de los supuestos y de la objeción principal, con acta",
 "checkpoint": {
  "estado": "BORRADOR_CON_VACIOS",
  "seccion": "4.4-MDR y 4.5",
  "siguiente": "Formalización del problema solo con autorización",
  "autorizacion_E3_mutada": false
 }
}
