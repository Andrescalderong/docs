%% PREFIJO: F6
# Paso 6. Generación y evaluación de alternativas

El Paso 6 convierte el problema formalizado en un conjunto de alternativas y elige una con un método multicriterio explícito. Sigue cuatro etapas. La primera es el árbol de objetivos (F6.1). La segunda identifica alternativas con una contrainductiva obligatoria (F6.2). La tercera es la evaluación multicriterio con análisis de sensibilidad (F6.3). La cuarta es la selección con validación territorial (F6.4). Los puntajes de desempeño son juicios PROPUESTOS por la instancia analítica y requieren ratificación del panel evaluador. Ningún puntaje se interpreta como probabilidad de éxito.

## F6.1 Árbol de objetivos

El árbol de objetivos invierte el árbol de problemas A-PROB (sección F4.5). El problema central, el error de medición sin verificar (V06), se convierte en el objetivo general. Las causas directas e indirectas se convierten en objetivos específicos y en medios. Los efectos se convierten en fines. La {T:t01} muestra la conversión nodo por nodo y la {F:f01} presenta el árbol resultante.

:::TABLA t01 | Conversión del árbol de problemas en árbol de objetivos
| Nodo | Estado problemático (F4.5) | Estado deseado | Rol en el árbol de objetivos | Objetivo del proyecto |
| --- | --- | --- | --- | --- |
| V06 | Error de medición sin verificar frente a una referencia | Error conocido y dentro de los umbrales frente a la referencia | Objetivo general | OG |
| V03 | Humedad relativa alta en los sitios | Sesgo por humedad corregido por el modelo | Medio del objetivo específico | OE1 |
| V02 | PM10 con fracción gruesa | Fracción gruesa modelada en la corrección | Medio del objetivo específico | OE1 |
| V01 | Concentración de PM2,5 sin serie propia | Serie de PM2,5 medida y verificada | Medio del objetivo específico | OE1 |
| V07 | Calibración baja o nula | Ciclos de calibración colocalizada programados | Medio del objetivo específico | OE1 |
| V05 | Remoción de escombros en curso | Energía y enlace redundantes que sostienen la disponibilidad pese a la remoción | Medio del objetivo específico | OE2 |
| V11 | AQHI sin fórmula local validada | AQHI con fórmula y umbrales validados localmente | Fin 1 | Fin |
| V12 | Falsas alarmas sin medir | Tasa de falsas alarmas medida y reducida | Fin 1 | Fin |
| V14 | Personas sin protección efectiva por alertas confiables | Alertas confiables disponibles para el protocolo de protección | Fin 2 | Fin |
| V15 | Baja adopción institucional | Uso documentado del tablero y custodia por componente | Fin 2 y objetivo específico | OE3 |
:::NOTA *Nota.* Elaboración propia con la sección F4.5 (árbol A-PROB) y la ficha maestra (sección 3). Naturaleza: PROPUESTO. V14 no tiene variable de resultado ni línea base; el proyecto no afirma protección efectiva de personas.

:::FIGURA f01 | Árbol de objetivos del proyecto | Nota. Elaboración propia con maestro.py (objetivo general y objetivos específicos) y la sección F4.5. Los códigos V corresponden al diccionario de 15 variables de la sección F4.4.2. Estatuto de las relaciones: HIE.

## F6.2 Identificación de alternativas

El conjunto de alternativas incluye cuatro opciones. ALT-00 mantiene la práctica actual y sirve de línea de comparación. ALT-01 sustituye el sensor de bajo costo por estaciones de referencia en cada sitio. ALT-02 corrige los datos de forma centralizada en la nube. ALT-03 es la alternativa contrainductiva que exige el metaprompt: corrige en el gateway, despliega por tramos condicionados y distribuye la custodia. El expediente E3-P00 presentaba tres alternativas con presupuestos no comparables. Esta formulación incorpora el statu quo y compara costos solo cuando proceden de la misma fuente.

Las cuatro fichas siguientes ({T:t02}, {T:t03}, {T:t04} y {T:t05}) usan los mismos diez aspectos. Los campos de articulación con el PDD, la demanda territorial y la misión PIIOM quedan como VACIO en las cuatro. Los documentos de origen no se aportaron.

:::TABLA t02 | Alternativa ALT-00: statu quo
| Aspecto | Descripción |
| --- | --- |
| Descripción | La alternativa mantiene la práctica actual: sensores ópticos de bajo costo operados de forma aislada, sin colocalización con equipos de referencia y sin corrección local. Cada comité interpreta las lecturas con el valor del fabricante. No exige inversión adicional ni desarrollo tecnológico. Tampoco entrega un error conocido ni un criterio para decidir cuándo una lectura es confiable. Sirve de comparación porque representa el costo de no intervenir. Su ventaja es la rapidez; su límite es que conserva el ciclo de baja confianza y bajo uso institucional. |
| Enfoque | Tradicional; mantener lo existente |
| TRL objetivo | No aplica: sin desarrollo |
| Componentes | Técnico: sensores aislados. Organizacional: sin protocolo de verificación. Económico: sin inversión adicional. |
| Duración | Continua; sin plazo de ejecución |
| Presupuesto | Sin inversión adicional; el costo de oportunidad no se estimó |
| Beneficiarios | Ningún comité con medición de error conocido |
| Articulación PDD | [DATO_USUARIO: eje y artículo del PDD, indicador y meta] |
| Demanda territorial | [DATO_USUARIO: código y nombre de la demanda territorial] |
| Misión PIIOM | [DATO_USUARIO: misión PIIOM y objetivo aplicable] |
:::NOTA *Nota.* Elaboración propia. Naturaleza: PROPUESTO. El presupuesto y los beneficiarios son INFERIDOS por la definición de la alternativa.

:::TABLA t03 | Alternativa ALT-01: estaciones fijas de referencia en los sitios de remoción
| Aspecto | Descripción |
| --- | --- |
| Descripción | La alternativa instala una estación de referencia, como un monitor gravimétrico o un equivalente, en cada uno de los 12 sitios focalizados. Cada estación entrega datos con error conocido y respaldo metrológico. El enfoque es tradicional: sustituye el sensor de bajo costo por el instrumento de referencia. La cobertura queda limitada por el costo unitario, por la energía y por la logística de cada sitio. No requiere un modelo de corrección. Con el costo unitario de los monitores gravimétricos de esta formulación, el equipamiento de referencia de 12 sitios suma $ 1.020.000.000 COP, sin energía, personal ni operación. |
| Enfoque | Tradicional; sustitución por instrumentos de referencia |
| TRL objetivo | TRL 9 del equipo comercial (INFERIDO; no verificado) |
| Componentes | Técnico: 12 estaciones de referencia. Organizacional: operación por personal capacitado en cada sitio. Económico: costo unitario alto y costo de operación continuo. |
| Duración | [DATO_USUARIO: plazo de adquisición e instalación de 12 estaciones de referencia] |
| Presupuesto | $ 1.020.000.000 COP solo en equipos de referencia (12 × $ 85.000.000); ILUSTRATIVO; excluye energía, personal y operación |
| Beneficiarios | 12 comités municipales, uno por estación (INFERIDO) |
| Articulación PDD | [DATO_USUARIO: eje y artículo del PDD, indicador y meta] |
| Demanda territorial | [DATO_USUARIO: código y nombre de la demanda territorial] |
| Misión PIIOM | [DATO_USUARIO: misión PIIOM y objetivo aplicable] |
:::NOTA *Nota.* Elaboración propia con el costo unitario de los monitores gravimétricos (línea E03 de maestro.py). El número de sitios (12) es SUPUESTO. El cálculo es ILUSTRATIVO y no equivale a una cotización.

:::TABLA t04 | Alternativa ALT-02: red de sensores con calibración centralizada en la nube
| Aspecto | Descripción |
| --- | --- |
| Descripción | La alternativa despliega 100 nodos con transmisión continua del dato crudo a la nube. Un modelo de calibración, entrenado con referencias colocalizadas, corrige los datos en la plataforma central. Mejora la práctica actual porque aplica corrección y mantiene control central del modelo. Depende de un enlace estable entre cada nodo y la nube. En sitios con cobertura deficiente, los datos no llegan y la corrección no se aplica. La transmisión continua aumenta el consumo de energía y de datos celulares. El hardware es equivalente al de ALT-03. |
| Enfoque | Mejorado; corrección centralizada |
| TRL objetivo | TRL 6 (INFERIDO) |
| Componentes | Técnico: 100 nodos y plataforma central de calibración. Organizacional: operación centralizada por el ejecutor. Económico: hardware equivalente al de ALT-03 y mayor costo de datos. |
| Duración | 24 meses (PROPUESTO), sin compuertas de ampliación |
| Presupuesto | Hardware equivalente al de ALT-03 (líneas E01 a E06); [DATO_USUARIO: costo de la plataforma de calibración centralizada] |
| Beneficiarios | 15 comités y 150 funcionarios (SUPUESTO) |
| Articulación PDD | [DATO_USUARIO: eje y artículo del PDD, indicador y meta] |
| Demanda territorial | [DATO_USUARIO: código y nombre de la demanda territorial] |
| Misión PIIOM | [DATO_USUARIO: misión PIIOM y objetivo aplicable] |
:::NOTA *Nota.* Elaboración propia con maestro.py. Naturaleza: PROPUESTO. El enfoque es la versión centralizada de la corrección que el expediente E3 ubicaba en varios lugares.

:::TABLA t05 | Alternativa ALT-03: red híbrida con corrección en gateway, despliegue por tramos y custodia distribuida
| Aspecto | Descripción |
| --- | --- |
| Descripción | La alternativa despliega 100 nodos hoja que transmiten por LoRa a 10 gateways. Cada gateway aplica el modelo de corrección vigente, almacena siete días de datos y reenvía por red celular con enlace satelital alterno. El despliegue se hace en tres tramos condicionados por compuertas: cada tramo libera la compra del siguiente solo si el modelo cumple los umbrales y los comités usan el tablero. La custodia de cada componente se asigna por convenio. Decide de forma distinta a lo esperado: no instala referencias en todos los sitios y no centraliza la corrección. |
| Enfoque | CONTRAINDUCTIVO |
| Justificación contrainductiva | Contradice dos supuestos del sector: que la calibración exige retirar el sensor (V07) y que un sensor de bajo costo no alcanza calidad de referencia (V06). Ver la {T:t06}. |
| Inspiración cross-domain | Vigilancia centinela en salud pública, trazabilidad metrológica y compuertas de etapa en gestión de innovación (Cooper, 2008). Ver la {T:t07}. |
| TRL objetivo | TRL 4 a TRL 7 (PROPUESTO) |
| Componentes | Técnico: 100 nodos, 10 gateways, 3 monitores de referencia y modelo de corrección en gateway. Organizacional: compuertas C1 y C2, comités y custodios por componente. Económico: presupuesto por tramos con reserva de contingencia. |
| Duración | 24 meses (104 semanas) y 12 meses de seguimiento |
| Presupuesto | $ 8.729.840.000 COP solicitados al SGR y $ 2.110.000.000 COP de contrapartida |
| Beneficiarios | 15 comités y 150 funcionarios (SUPUESTO); operarios [DATO_USUARIO: número en los sitios monitoreados] |
| Articulación PDD | [DATO_USUARIO: eje y artículo del PDD, indicador y meta] |
| Demanda territorial | [DATO_USUARIO: código y nombre de la demanda territorial] |
| Misión PIIOM | [DATO_USUARIO: misión PIIOM y objetivo aplicable] |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (secciones 2 a 5). Naturaleza: PROPUESTO. El presupuesto de ALT-03 incluye desarrollo, apropiación social y custodia; el de ALT-01 solo cubre equipos de referencia, de modo que los montos no son comparables.

### F6.2.1 Test de autenticidad contrainductiva

Tres condiciones acumulativas separan la contrainducción genuina de la cosmética. El incumplimiento de cualquiera devuelve la alternativa a rediseño. La {T:t06} verifica cada condición para ALT-03. La primera condición cierra el circuito con el desmantelamiento de ortodoxias de la Tabla F4.3 de la sección F4.2. Cita las filas V07 y V06.

:::TABLA t06 | Test de autenticidad contrainductiva de ALT-03
| Condición | Verificación | Cumple |
| --- | --- | --- |
| (a) Violación declarada | ALT-03 contradice dos ortodoxias de la tabla F4.3: la fila V07 («La calibración exige retirar el sensor al laboratorio», decisión Eliminar) y la fila V06 («Un sensor de bajo costo nunca alcanza la calidad de una referencia», decisión Cuestionar). | Sí; filas V07 y V06 de F4.3 |
| (b) Cambio de expectativas verificable | Las autoridades ambientales y los proveedores de estaciones de referencia reaccionarían con resistencia, porque el estándar aceptado exige una referencia fija en cada sitio. Este juicio es INFERIDO; no hay consulta documentada. | Sí; actor: autoridades ambientales y proveedores; razón: sustituye la referencia fija por corrección |
| (c) Irreducibilidad | ALT-03 no se reformula como ALT-02 con otros parámetros. Difiere en tres decisiones estructurales: el lugar de la corrección (gateway), la condición de ampliación (compuertas) y el régimen de custodia (convenios por componente). Las tres son institucionales, no paramétricas. | Sí; argumento: tres decisiones estructurales distintas |
:::NOTA *Nota.* Elaboración propia con la sección F4.2 y la ficha maestra. Ejemplo de contrainducción cosmética rechazada: «la misma plataforma de ALT-02 con inteligencia artificial»; falla las tres condiciones.

### F6.2.2 Analogías entre dominios

Las analogías no sustituyen evidencia. Orientan el diseño y se mantienen como ILUSTRATIVAS hasta que el piloto las someta a prueba. La {T:t07} lista tres dominios fuente con la adaptación propuesta.

:::TABLA t07 | Analogías entre dominios para la alternativa contrainductiva
| Dominio fuente | Solución observada | Analogía | Adaptación propuesta |
| --- | --- | --- | --- |
| Salud pública | Vigilancia centinela: pocos sitios con medición de alta calidad que respaldan una cobertura amplia de menor costo | Los 3 monitores de referencia respaldan los 100 nodos | Colocalizar nodos con la referencia de cada departamento y rotarlos entre sitios |
| Metrología | Trazabilidad por transferencia de calibración desde un patrón hasta los instrumentos de campo | El modelo de corrección transfiere la exactitud de la referencia al nodo | Registrar la versión del modelo por gateway y por periodo |
| Gestión de la innovación | Compuertas de etapa que condicionan la inversión siguiente a criterios medibles (Cooper, 2008) | Las compuertas C1 y C2 liberan la compra de cada tramo | Fijar umbrales de desempeño y de uso institucional como criterios de decisión |
:::NOTA *Nota.* Elaboración propia. Naturaleza: ILUSTRATIVO. Verificación: NO_VERIFICADO salvo la cita de Cooper (2008), que no fue consultada en esta corrida.

La {T:t08} registra la decisión sobre la autenticidad de la alternativa contrainductiva (nodo ND-12).

:::TABLA t08 | Registro de decisión GENESIS: ND-12 Autenticidad contrainductiva
| Campo | Contenido |
| --- | --- |
| NODO | ND-12 Autenticidad contrainductiva |
| CLASE | MAYOR. Determina si ALT-03 sigue siendo contrainductiva o vuelve a rediseño. |
| DECISION | Declarar ALT-03 contrainductiva genuina por cumplir las tres condiciones del test. |
| DECIDE | Equipo formulador [DATO_USUARIO: responsable de la decisión]. La propuesta proviene de la instancia analítica. |
| EXCLUYE | Considerar contrainductiva una mejora tecnológica de ALT-02. Aceptar la condición (b) sin consulta documentada. |
| NODOS_BLANCOS | 2: filas V07 y V06 de la tabla F4.3; tres decisiones estructurales distintas entre ALT-02 y ALT-03. |
| NODOS_GRISES | 2: reacción de las autoridades ambientales (sin consulta); factibilidad de custodia por convenio. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | PR-06 (patrón emergente): diferenciar por decisiones institucionales y no por tecnología. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. La custodia depende de entidades cuya capacidad no se verificó. |
| ESCENA_SIMULABLE | Un representante de una autoridad ambiental revisa en el mes 12 si acepta datos corregidos en gateway como complemento de su referencia. |
| EVIDENCIA_JH_A | Filas V07 y V06 de la tabla F4.3. |
| EVIDENCIA_JH_B | Comparación de decisiones estructurales entre ALT-02 y ALT-03 en las tablas F6.4 y F6.5. |
| CERCA_CONCEPTUAL | Una alternativa contrainductiva no es mejor por serlo; debe ganar en la evaluación multicriterio. |
| ESTATUTO_CAUSAL | HIE. |
| VEREDICTO | ALT-03 pasa el test con la condición (b) sustentada solo en inferencia. |
| RAZON_DEL_DESCARTE | Se descarta presentar la condición (b) como verificada. |
| RESULTADO | CIERRA con un vacío declarado (consulta a actores). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS.

## F6.3 Evaluación multicriterio

La evaluación usa una suma ponderada con una escala ordinal de desempeño de 1 a 9. Esa escala no es la escala de Saaty (1980) ni un proceso analítico jerárquico. El nombre AHP se reserva para la elicitación de pesos mediante comparaciones pareadas con control de consistencia. Los términos de referencia no se aportaron y, por tanto, no fijan pesos. La matriz usa los pesos por defecto del metaprompt, que suman 100 %. Los dos criterios territoriales conservan su piso protegido de 10 % y 8 %, aunque la convocatoria no los pondere.

La {T:t09} presenta la matriz de desempeño. Los puntajes de los criterios territoriales reflejan la ausencia de documentos de origen. El puntaje 5 equivale a una articulación genérica. El puntaje 1 equivale a la ausencia de articulación demostrable. El puntaje 9 exigiría un artículo del PDD, un código de demanda y un indicador.

:::TABLA t09 | Matriz de desempeño multicriterio en escala ordinal de 1 a 9
| Criterio | Peso | ALT-00 | ALT-01 | ALT-02 | ALT-03 |
| --- | --- | --- | --- | --- | --- |
| Viabilidad técnica | 12,0 % | 9 | 7 | 5 | 6 |
| Viabilidad financiera | 12,0 % | 9 | 3 | 6 | 6 |
| Impacto esperado | 15,0 % | 1 | 5 | 5 | 7 |
| Articulación con PDD y demandas territoriales | 10,0 % | 1 | 5 | 5 | 5 |
| Respuesta a prioridades del territorio | 8,0 % | 1 | 4 | 5 | 5 |
| Sostenibilidad | 8,0 % | 1 | 3 | 4 | 5 |
| Tiempo de implementación | 8,0 % | 9 | 3 | 6 | 5 |
| Nivel de riesgo (mayor puntaje, menor riesgo) | 8,0 % | 9 | 6 | 4 | 4 |
| Escalabilidad | 5,0 % | 1 | 2 | 7 | 7 |
| Nivel de innovación | 4,0 % | 1 | 2 | 4 | 8 |
| PAFU: práctica | 2,5 % | 5 | 4 | 6 | 6 |
| PAFU: accesible | 2,5 % | 5 | 3 | 6 | 6 |
| PAFU: fiable | 2,5 % | 3 | 8 | 4 | 6 |
| PAFU: ubicua | 2,5 % | 2 | 2 | 6 | 7 |
| TOTAL PONDERADO | 100,0 % | 4,475 | 4,335 | 5,150 | 5,805 |
:::NOTA *Nota.* Elaboración propia con maestro/alternativas.py. Los totales se muestran con tres decimales. Naturaleza: PROPUESTO para puntajes y pesos; CALCULADO para los totales. Verificación: NO_VERIFICADO; los puntajes requieren ratificación del panel evaluador.

La {T:t10} registra la justificación de cada puntaje. Cada una cabe en una línea y enlaza la valoración con una característica de la alternativa. Ninguna cita una fuente de desempeño, porque las alternativas no se han ejecutado.

:::TABLA t10 | Justificación de los puntajes por criterio
| Criterio | Justificación |
| --- | --- |
| Viabilidad técnica | ALT-00 no exige desarrollo; ALT-01 es madura pero logística; ALT-02 depende del enlace; ALT-03 parte de TRL 4. |
| Viabilidad financiera | ALT-01 exige equipos de referencia por sitio; ALT-02 y ALT-03 usan sensores de bajo costo. |
| Impacto esperado | ALT-03 corrige el sesgo en el origen y permite verificar el uso institucional. |
| Articulación con PDD y demandas territoriales | Sin PDD ni anexo de demandas aportados, la articulación es genérica (NO_VERIFICADO). |
| Respuesta a prioridades del territorio | Sin evidencia documental de priorización local; se asigna alineación parcial. |
| Sostenibilidad | Custodia por tramos mejora la continuidad; no hay compromisos firmados. |
| Tiempo de implementación | ALT-01 exige obra y compra masiva; ALT-03 requiere piloto antes de ampliar. |
| Nivel de riesgo (mayor puntaje, menor riesgo) | ALT-02 y ALT-03 concentran riesgo en humedad y enlace; el piloto lo acota. |
| Escalabilidad | Costo marginal bajo por nodo adicional en ALT-02 y ALT-03. |
| Nivel de innovación | ALT-03 combina corrección en el borde, tramos condicionados y custodia distribuida. |
| PAFU: práctica | Operación sencilla para los comités. |
| PAFU: accesible | Costo por nodo accesible para municipios. |
| PAFU: fiable | Las estaciones de referencia son más fiables que los sensores corregidos. |
| PAFU: ubicua | Mayor cobertura espacial con ALT-02 y ALT-03. |
:::NOTA *Nota.* Elaboración propia con maestro/alternativas.py. Naturaleza: PROPUESTO.

### F6.3.1 Análisis de sensibilidad

La perturbación de «+10 %» es relativa. El peso del criterio perturbado se multiplica por 1,10 y todos los pesos se renormalizan para que sumen 1. La {T:t11} publica el vector completo de cada escenario y verifica que la suma sea 1. La {T:t12} compara los totales con el caso base.

:::TABLA t11 | Vectores de pesos de los escenarios de sensibilidad
| Criterio | Base | E1 | E2 | E3 | E4 | E5 |
| --- | --- | --- | --- | --- | --- | --- |
| Viabilidad técnica | 0,120 | 0,130 | 0,119 | 0,118 | 0,120 | 0,118 |
| Viabilidad financiera | 0,120 | 0,119 | 0,130 | 0,118 | 0,120 | 0,118 |
| Impacto esperado | 0,150 | 0,148 | 0,148 | 0,163 | 0,149 | 0,147 |
| Articulación con PDD y demandas territoriales | 0,100 | 0,099 | 0,099 | 0,099 | 0,100 | 0,108 |
| Respuesta a prioridades del territorio | 0,080 | 0,079 | 0,079 | 0,079 | 0,080 | 0,086 |
| Sostenibilidad | 0,080 | 0,079 | 0,079 | 0,079 | 0,080 | 0,079 |
| Tiempo de implementación | 0,080 | 0,079 | 0,079 | 0,079 | 0,080 | 0,079 |
| Nivel de riesgo (mayor puntaje, menor riesgo) | 0,080 | 0,079 | 0,079 | 0,079 | 0,080 | 0,079 |
| Escalabilidad | 0,050 | 0,049 | 0,049 | 0,049 | 0,050 | 0,049 |
| Nivel de innovación | 0,040 | 0,040 | 0,040 | 0,039 | 0,044 | 0,039 |
| PAFU: práctica | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 |
| PAFU: accesible | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 |
| PAFU: fiable | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 |
| PAFU: ubicua | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 | 0,025 |
| Suma de pesos | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |
:::NOTA *Nota.* Elaboración propia con maestro/alternativas.py. E1: Prioridad técnica (viabilidad técnica +10 %). E2: Prioridad financiera (viabilidad financiera +10 %). E3: Prioridad de impacto (impacto esperado +10 %). E4: Prioridad de innovación (nivel de innovación +10 %). E5: Prioridad territorial (criterios territoriales +10 %).

:::TABLA t12 | Resultados del análisis de sensibilidad
| Escenario | Cambio en pesos | Ganadora | ALT-00 | ALT-01 | ALT-02 | ALT-03 | Robustez |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base | Pesos por defecto | ALT-03 | 4,475 | 4,335 | 5,150 | 5,805 | Referencia |
| Prioridad técnica | viabilidad técnica +10 % | ALT-03 | 4,529 | 4,367 | 5,148 | 5,807 | No cambia |
| Prioridad financiera | viabilidad financiera +10 % | ALT-03 | 4,529 | 4,319 | 5,160 | 5,807 | No cambia |
| Prioridad de impacto | impacto esperado +10 % | ALT-03 | 4,424 | 4,345 | 5,148 | 5,823 | No cambia |
| Prioridad de innovación | nivel de innovación +10 % | ALT-03 | 4,461 | 4,326 | 5,145 | 5,814 | No cambia |
| Prioridad territorial | criterios territoriales +10 % | ALT-03 | 4,414 | 4,339 | 5,147 | 5,791 | No cambia |
:::NOTA *Nota.* Elaboración propia con maestro/alternativas.py. Los escenarios perturban un peso o un grupo de pesos en +10 % relativo y renormalizan.

La alternativa ganadora no cambia en ningún escenario. Además, ninguna perturbación de un solo peso entre −99 % y +500 % invierte el primer lugar entre ALT-03 y ALT-02. El margen entre ambas es de 0,655 puntos en el caso base. Este resultado no valida el ranking. ALT-03 supera a ALT-02 en seis criterios: viabilidad técnica, impacto esperado, sostenibilidad, nivel de innovación y los criterios PAFU de fiabilidad y ubicuidad. ALT-02 supera a ALT-03 solo en tiempo de implementación, con 6 frente a 5. Los otros siete criterios empatan.


### F6.3.2 Optimización metaheurística (GWO)

El módulo de optimización con el algoritmo del lobo gris (Mirjalili et al., 2014) se activa solo si la enumeración exacta no es viable. El espacio de decisión de esta formulación contiene cuatro alternativas discretas, y la suma ponderada se evalúa por enumeración completa. Por esa razón, GWO no se activa (aserción AS-32 y decisión DEC-F15). No se ejecutó ningún algoritmo, de modo que no existe tabla de contraste GWO-MCDA ni estabilidad multisemilla.

La {T:t13} registra la decisión sobre la activación de la metaheurística (nodo ND-14).

:::TABLA t13 | Registro de decisión GENESIS: ND-14 Activación de la metaheurística
| Campo | Contenido |
| --- | --- |
| NODO | ND-14 Activación de la metaheurística |
| CLASE | MENOR. Define si se ejecuta una optimización adicional. |
| DECISION | No activar GWO: el espacio de decisión es enumerable. |
| DECIDE | Equipo formulador [DATO_USUARIO: responsable de la decisión]. |
| EXCLUYE | Optimizar variables continuas sin datos. Presentar un resultado metaheurístico no calculado. |
| NODOS_BLANCOS | 1: cuatro alternativas discretas evaluadas con 14 criterios por enumeración. |
| NODOS_GRISES | 0. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | Ninguno. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: Sí. |
| ESCENA_SIMULABLE | No aplica: no se ejecuta la metaheurística. |
| EVIDENCIA_JH_A | Espacio de decisión de 4 alternativas. |
| EVIDENCIA_JH_B | Criterio (1) a (3) de activación no se cumplen. |
| CERCA_CONCEPTUAL | Una metaheurística no valida causalidad ni sustituye la evidencia. |
| ESTATUTO_CAUSAL | NO_APLICA. |
| VEREDICTO | GWO no activado. |
| RAZON_DEL_DESCARTE | Se descarta activarlo porque la búsqueda exacta es viable. |
| RESULTADO | CIERRA sin vacíos. |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS y el módulo GWO del metaprompt.

La {T:t14} registra la decisión sobre los pesos y los puntajes de la evaluación multicriterio (nodo ND-13).

:::TABLA t14 | Registro de decisión GENESIS: ND-13 Pesos y puntajes MCDA
| Campo | Contenido |
| --- | --- |
| NODO | ND-13 Pesos y puntajes MCDA |
| CLASE | MAYOR. Determina el ranking de alternativas. |
| DECISION | Adoptar los pesos por defecto del metaprompt y los puntajes de la tabla F6.9, con ratificación pendiente del panel evaluador. |
| DECIDE | Panel evaluador [DATO_USUARIO: composición del panel]. La propuesta proviene de la instancia analítica. |
| EXCLUYE | Pesos elicitados con comparaciones pareadas (no hay comité). Puntajes derivados de una ejecución de las alternativas. |
| NODOS_BLANCOS | 2: suma de pesos igual a 100 %; mínimos protegidos de los criterios territoriales respetados. |
| NODOS_GRISES | 3: los 14 puntajes son juicios sin evidencia de desempeño; la articulación territorial carece de documentos de origen; el panel no existe aún. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | PR-06 (patrón emergente): decisión con juicios ordinales y sensibilidad publicada. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: Sí. |
| ESCENA_SIMULABLE | Un panel de tres evaluadores puntúa cada criterio de forma independiente y se compara con la tabla F6.9. |
| EVIDENCIA_JH_A | Cinco escenarios de sensibilidad sin cambio de ganadora (tabla F6.12). |
| EVIDENCIA_JH_B | Justificación por criterio (tabla F6.10). |
| CERCA_CONCEPTUAL | El puntaje total no es una probabilidad de éxito. |
| ESTATUTO_CAUSAL | NO_APLICA: es una evaluación multicriterio. |
| VEREDICTO | Ranking adoptado como propuesta condicionada a la ratificación. |
| RAZON_DEL_DESCARTE | Se descarta elicitar pesos por AHP sin un comité que compare criterios. |
| RESULTADO | CIERRA con vacíos declarados (panel y evidencia de desempeño). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS.

## F6.4 Alternativa seleccionada

**Alternativa ganadora.** ALT-03: red híbrida con corrección en gateway, despliegue por tramos y custodia distribuida.

**Puntaje.** 5,805 de 9,000 (5,81 con dos decimales). El puntaje ordena las alternativas y no estima probabilidad de éxito.

**Justificación.** ALT-03 obtiene el mayor puntaje en impacto esperado (7), escalabilidad (7) y nivel de innovación (8). Empata con ALT-02 en viabilidad financiera (6). Su desventaja frente a ALT-00 está en tres criterios. Son viabilidad técnica (6 frente a 9), tiempo de implementación (5 frente a 9) y nivel de riesgo (4 frente a 9). La causa es que ALT-03 exige desarrollo y piloto. Los tramos condicionados acotan esos riesgos sin eliminarlos.

La {T:t15} valida la articulación territorial de la alternativa seleccionada. El criterio «Articulación con PDD y demandas territoriales» recibió 5 de 9, que es el umbral de la regla del metaprompt. Por tanto, no se activa la alerta, pero el 5 equivale a articulación genérica y no está verificado. La alerta se activaría si el equipo no obtiene los documentos territoriales.

:::TABLA t15 | Validación de articulación territorial de la alternativa seleccionada
| Elemento | Contenido verificable | Fuente | Estado |
| --- | --- | --- | --- |
| PDD vigente | [DATO_USUARIO: nombre del PDD, eje y artículo] | PDD de cada departamento | VACIO |
| Indicador PDD | [DATO_USUARIO: indicador, línea base y meta] | Capítulo de metas del PDD | VACIO |
| Demanda territorial | [DATO_USUARIO: código y nombre de la demanda] | Anexo 4 de la convocatoria | VACIO |
| Contribución a la meta PDD | ALT-03 contribuye a un indicador de estaciones de monitoreo y alerta mediante 100 nodos y 10 gateways con error verificado; el indicador exacto es [DATO_USUARIO] | Análisis propio | INFERIDO |
| Misión PIIOM | [DATO_USUARIO: misión aplicable] | PIIOM de MinCiencias | VACIO |
| CONPES articulado | CONPES 4069 de política de ciencia, tecnología e innovación (DNP, 2021); objetivo [DATO_USUARIO: objetivo y línea] | Departamento Nacional de Planeación | NO_VERIFICADO |
| Actores territoriales involucrados | Alcaldías de 12 municipios, comités de gestión del riesgo y empresa tecnológica [DATO_USUARIO: nombres y cartas de intención] | Cartas de intención | SUPUESTO |
| Beneficiarios territoriales | 150 funcionarios en 15 comités; indirectos [DATO_USUARIO: población de los municipios] | Cálculo propio | SUPUESTO |
:::NOTA *Nota.* Elaboración propia. Los elementos VACIO son documentos que solo la entidad ejecutora posee. Ver la reserva R-ART de la decisión DEC-F12.

La {T:t16} registra la decisión sobre la alternativa seleccionada (nodo ND-15).

:::TABLA t16 | Registro de decisión GENESIS: ND-15 Alternativa seleccionada
| Campo | Contenido |
| --- | --- |
| NODO | ND-15 Alternativa seleccionada |
| CLASE | MAYOR. Fija la alternativa que desarrollan los capítulos del documento. |
| DECISION | Seleccionar ALT-03 como alternativa del proyecto, condicionada a la ratificación del panel. |
| DECIDE | Panel evaluador y equipo formulador [DATO_USUARIO: responsables]. |
| EXCLUYE | Descartar de forma definitiva ALT-00 a ALT-02: la convocatoria exige comparar y el panel puede reordenar. |
| NODOS_BLANCOS | 2: ALT-03 gana en el caso base y en los cinco escenarios; el test contrainductivo se cumple. |
| NODOS_GRISES | 3: articulación territorial; desempeño real del modelo en escombros; capacidad de custodia. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | PR-06 (patrón emergente): selección condicionada con compuertas de reversa. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. La selección depende de capacidad de custodia no verificada. |
| ESCENA_SIMULABLE | En la compuerta C1, el panel decide perseverar o pivotar con los datos del tramo 1. |
| EVIDENCIA_JH_A | Puntaje 5,805 frente a 5,150 de ALT-02. |
| EVIDENCIA_JH_B | Presupuesto y cronograma de ALT-03 en la ficha maestra. |
| CERCA_CONCEPTUAL | La selección no prueba que ALT-03 funcione; el piloto del tramo 1 lo establece. |
| ESTATUTO_CAUSAL | HIE. |
| VEREDICTO | ALT-03 seleccionada con reservas. |
| RAZON_DEL_DESCARTE | Se descarta el statu quo por conservar el ciclo de baja confianza. |
| RESULTADO | CIERRA con vacíos declarados (territorio y custodia). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS.

La {F:f02} resume el ranking y el rango del puntaje en los cinco escenarios.

:::FIGURA f02 | Puntaje ponderado por alternativa y rango en los escenarios de sensibilidad | Nota. Elaboración propia con maestro/alternativas.py. Escala ordinal de desempeño de 1 a 9; caso base con pesos por defecto y cinco perturbaciones de +10 % relativo con renormalización. Los puntajes son juicios PROPUESTOS.

El Paso 6 crea valor al ofrecer una decisión auditable. Cualquier lector reproduce los totales con los pesos y los puntajes publicados. Puede identificar los juicios más débiles y comprobar que la conclusión resiste cambios de peso. El Paso 7 diseña el sistema de indicadores que verifica la alternativa seleccionada.
