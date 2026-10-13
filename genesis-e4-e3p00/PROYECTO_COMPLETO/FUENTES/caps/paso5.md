%% PREFIJO: F5
# Paso 5. Formalización tripartita del problema

El Paso 5 reformula el problema en tres niveles de abstracción: el metaproblema, el problema sustantivo y el problema formal. Cada nivel responde una pregunta distinta. El metaproblema pregunta por la falla sistémica que trasciende el contexto. El problema sustantivo pregunta cómo se manifiesta esa falla en el territorio. El problema formal pregunta qué variables medibles la capturan. La formalización parte de la causa raíz del Paso 4 (F4.8) y de las prioridades de la sección F4.7.

## F5.0 Validación de la articulación territorial del problema

El metaprompt exige verificar, antes de formalizar, que el problema se ancla al territorio y a las prioridades departamentales y nacionales. Exige también una regla bloqueante. Si menos de 5 de los 8 elementos del checklist se verifican, el proceso regresa a la fase de admisión. El expediente E3-P00 declara los 8 elementos como verificados. Esta formulación no puede confirmarlos. No se aportaron el Plan de Desarrollo Departamental (PDD) ni el Anexo 4 de la convocatoria. Tampoco se aportaron la política de investigación e innovación orientada por misiones (PIIOM) ni los documentos CONPES citados.

La {T:t01} contrasta lo declarado con lo verificado. Los ocho elementos quedan sin verificar y, por la regla bloqueante, el proceso debería regresar a la admisión. La decisión DEC-F12 continúa por orden expresa del usuario del 13 de octubre de 2026 y registra la reserva R-ART. El cierre del documento convierte esa reserva en una lista de documentos por obtener.

:::TABLA t01 | Checklist de articulación territorial del problema
| Elemento de articulación | Fuente | Referencia declarada por E3-P00 | Naturaleza | Verificación |
| --- | --- | --- | --- | --- |
| Demanda territorial seleccionada | Anexo 4 de la convocatoria | DT-CAL-11 (inteligencia artificial y riesgo); DT-CUN-11 (gobernanza territorial y riesgos) | DECLARADO | NO_VERIFICADO |
| Eje estratégico del PDD vigente | PDD de Caldas 2024-2027 | Eje 2, artículo 22: desarrollo sostenible y mitigación del riesgo climático y geológico | DECLARADO | NO_VERIFICADO |
| Indicador del PDD asociado al problema | PDD de Caldas 2024-2027 | Estaciones de monitoreo y alerta instaladas; línea base 12; meta 40 | DECLARADO | NO_VERIFICADO |
| Diagnóstico departamental | PDD de Cundinamarca y DANE | Déficit de cobertura de alerta temprana en zonas de alta pendiente (68 % sin datos) | DECLARADO | NO_VERIFICADO |
| Misión PIIOM aplicable | PIIOM de MinCiencias | Misión 3: territorios sostenibles frente al cambio climático y los desastres | DECLARADO | NO_VERIFICADO |
| CONPES o política nacional articulada | CONPES 4069 (Departamento Nacional de Planeación [DNP], 2021) | Objetivo 2, línea estratégica 4, según E3-P00 | DECLARADO | NO_VERIFICADO |
| Recomendación de la Misión de Sabios | Misión Internacional de Sabios (2019) | Foco 4: tecnologías convergentes, según E3-P00 | DECLARADO | NO_VERIFICADO |
| Demandas territoriales adicionales | Anexo 4 de la convocatoria | DT-VAL-7: prevención de enfermedades respiratorias, subdimensión calidad del aire | DECLARADO | NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente E3-P00 (Tabla E3-5.0). Los documentos CONPES 4069 y de la Misión de Sabios figuran en la lista de referencias, pero el contenido que E3 les atribuye no se verificó contra el texto. Ver decisión DEC-F12.

## F5.1 Metaproblema (nivel abstracto)

La pregunta del árbol de lógica es qué falla sistémica trasciende este contexto. La falla es estructural: los sistemas de vigilancia ambiental de bajo costo se despliegan sin calibración colocalizada ni corrección local. Por eso entregan mediciones de calidad desconocida. Con datos sin error conocido, las instituciones deciden alertas sin saber si el valor medido se acerca al valor real. La {T:t02} resume los componentes del metaproblema.

:::TABLA t02 | Componentes del metaproblema
| Componente | Contenido |
| --- | --- |
| Falla sistémica | Despliegue de sensores de bajo costo sin calibración colocalizada ni corrección local, con resultados de calidad desconocida. |
| Ámbito | Vigilancia ambiental de material particulado para la gestión del riesgo de desastres. |
| Dimensión temporal | Persistencia durante la respuesta a un desastre y durante la recuperación posterior. [DATO_USUARIO: fecha del evento y duración de la remoción en cada sitio] |
| Alcance geográfico | Nacional, con evidencia de nivel sistémico: 90,8 % de las 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13; cálculo del analista). |
| Población afectada | Operarios de remoción de escombros y población expuesta en los sitios de intervención; comités de gestión del riesgo que deciden con los datos. |
| Articulación PDD | VACIO: el PDD vigente no se aportó (ver Tabla F5.1). |
| Demanda territorial | VACIO: el Anexo 4 no se aportó (ver Tabla F5.1). |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (sección 10c) y el informe de vigilancia tecnológica. Naturaleza: INFERIDO salvo la cifra citada (CALCULADO sobre un dato del documento).

**Enunciado del metaproblema.**

> Los sistemas de vigilancia ambiental de bajo costo desplegados en contextos de desastre no entregan mediciones de material particulado con error conocido. La causa sistémica es la ausencia de calibración colocalizada y de corrección local. Esta disfunción lleva a decidir alertas con datos de calidad desconocida. Afecta a los operarios de remoción y a la población expuesta. Además, mantiene un ciclo: la baja confianza reduce el uso institucional de las mediciones.

El enunciado conserva la estructura que fija el metaprompt: sistema, incapacidad, causa sistémica, consecuencia, población afectada y ciclo de refuerzo. No afirma magnitud de daño en salud, porque el corpus no la mide en el contexto de escombros.

## F5.2 Problema sustantivo (nivel contextual)

La pregunta es cómo se manifiesta la falla en el territorio y en la población objetivo. La falla se manifiesta en los sitios de remoción de escombros. El territorio de trabajo es Caldas, Cundinamarca y Valle del Cauca (SUPUESTO). Allí los comités de gestión del riesgo no disponen de mediciones de PM2,5 y PM10 con error conocido frente a una referencia. El expediente E3 declara un error normalizado superior a 45 % en alta humedad. La cifra carece de localizador y no se verificó. La línea base propia se mide en el tramo 1.

El contexto nacional sí consta en el corpus. Hay 209 estaciones reportadas, 154 de ellas integradas a un sistema de vigilancia. Solo 28 de 1.122 municipios cuentan con estaciones utilizables para estimar la carga de enfermedad (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). Esa cifra describe la cobertura nacional y no el error de los sensores. La {T:t03} reúne los cinco indicadores de línea base. Tres de ellos son VACIO porque los medirá el proyecto.

:::TABLA t03 | Indicadores de línea base del problema sustantivo
| Indicador | Valor actual | Valor meta | Brecha | Fuente | Año |
| --- | --- | --- | --- | --- | --- |
| NRMSE de los nodos frente a la referencia colocalizada | VACIO: se mide en el tramo 1 | ≤ 30 % | VACIO | Medición propia del proyecto; umbral de EPA (2021) | 2027 |
| Coeficiente de determinación (R²) frente a la referencia | VACIO: se mide en el tramo 1 | ≥ 0,70 | VACIO | Medición propia del proyecto; umbral de EPA (2021) | 2027 |
| Disponibilidad mensual de nodos | VACIO: se mide desde el mes 4 | ≥ 90 % | VACIO | Medición propia del proyecto | 2027 |
| Comités que usan el tablero en decisiones documentadas | VACIO: sin medición de uso | ≥ 75 % de 15 comités al mes 24 | VACIO | Medición propia del proyecto | 2028 |
| Municipios con estaciones utilizables para estimar la carga de enfermedad | 28 de 1.122 (2,5 %) | Sin meta propia | No aplica | Rodríguez-Villamizar et al. (2022, pp. 3 y 6); porcentaje calculado por el analista | 2022 |
:::NOTA *Nota.* Elaboración propia con la ficha maestra y el informe de vigilancia tecnológica. Los años de las metas son los de la medición prevista dentro de la ejecución. Naturaleza: PROPUESTO para las metas; DOCUMENTADO para la última fila.

**Enunciado del problema sustantivo.**

> En los sitios de remoción de Caldas, Cundinamarca y Valle del Cauca (SUPUESTO), los comités de gestión del riesgo no conocen el error de sus mediciones de PM2,5 y PM10. El valor actual del error es VACIO y se mide en el tramo 1. El estándar de referencia es NRMSE de 30 % o menos y R² de 0,70 o más (U.S. Environmental Protection Agency [EPA], 2021). La situación persiste mientras no exista una referencia colocalizada en los sitios. Sin intervención, el escenario inferido es la continuidad de decisiones con datos de calidad desconocida. Esta inferencia no es una proyección con datos.

El PDD, el Anexo 4 y los CONPES citados por E3 no se aportaron. Por esa razón, el enunciado no puede citar un eje, un artículo ni un código de demanda como lo prevé la plantilla del metaprompt. El campo queda como [DATO_USUARIO: eje y artículo del PDD, código de demanda territorial].

## F5.3 Problema formal (nivel operacional)

La pregunta es qué variables específicas y medibles capturan el problema. La variable dependiente Y es el error de medición de los nodos frente a la referencia, expresado como error cuadrático medio normalizado (NRMSE, V06). Hay tres variables independientes. X1 es la humedad relativa (V03). X2 es la fracción gruesa (V02 menos V01). X3 es la frecuencia y calidad de calibración (V07). La disponibilidad de nodos (M, V09) modera el acceso a las mediciones. Tres controles omitidos del modelo de 15 variables completan el marco: temperatura, edad del cabezal y distancia a la referencia.

Este modelo corrige dos defectos del expediente E3-P00. En E3, X2 era la latencia de datos y X3 la disponibilidad de nodos. Ninguna de las dos actúa sobre el sesgo de calibración en la matriz de influencia directa de E3. Además, E3 fijaba tres metas distintas para el error. Esta formulación adopta una sola meta: NRMSE de 30 % o menos y R² de 0,70 o más (decisión DEC-F04).

**Modelo relacional.** Y = f(X1, X2, X3 | M, C).

La {T:t04} define cada variable con su unidad y su rango. Las relaciones del modelo son hipótesis de influencia estructural (HIE). La ecuación no está identificada como efecto causal, salvo el efecto de X3 sobre Y bajo el sorteo semanal de la sección F4.3.

:::TABLA t04 | Variables del modelo relacional del problema formal
| Variable | Tipo | Nombre | Definición operacional | Unidad | Rango | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Y | Dependiente | Error normalizado de los nodos (V06) | RMSE de las lecturas horarias del nodo frente a la referencia, dividido por la media de la referencia | Porcentaje | 0 a 100 % (meta ≤ 30 %) | Medición propia; EPA (2021) |
| X1 | Independiente | Humedad relativa (V03) | Humedad relativa del aire en el sitio, promedio horario | Porcentaje | 0 a 100 % | Sensor del nodo; Suresh et al. (2025, p. 30) |
| X2 | Independiente | Fracción gruesa (V02 menos V01) | Diferencia entre PM10 y PM2,5, promedio horario | µg/m³ | ≥ 0 | Sensor del nodo y referencia |
| X3 | Independiente | Calibración (V07) | Ciclos de calibración colocalizada ejecutados por tramo | Ciclos por tramo | Meta de diseño: 2 por tramo (6 en total) | Plan de trabajo; Bang et al. (2026, pp. 6-8) |
| M | Moderadora | Disponibilidad de nodos (V09) | Proporción mensual de nodos activos con energía y enlace | Porcentaje | 0 a 100 % (meta ≥ 90 %) | Plataforma; Tavella et al. (2026, p. 6) |
| C1 | Control | Temperatura | Temperatura del aire en el sitio, promedio horario | °C | [DATO_USUARIO: rango climático por sitio] | Sensor del nodo |
| C2 | Control | Edad del cabezal | Meses desde la instalación del cabezal óptico | Meses | 0 a 24 | Registro de mantenimiento |
| C3 | Control | Distancia a la referencia | Distancia entre el nodo y el monitor de referencia más cercano | Metros | [DATO_USUARIO: rango por sitio] | Georreferenciación del proyecto |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (sección 10c). Los controles C1 a C3 son variables omitidas del modelo de 15 variables; se evaluarán en una matriz ampliada a 19 variables. Naturaleza: PROPUESTO.

**Enunciado del problema formal.**

> El nivel de Y en los sitios de remoción de Caldas, Cundinamarca y Valle del Cauca es [VACIO: se mide en el tramo 1]. La meta es NRMSE de 30 % o menos y R² de 0,70 o más al mes 24 (EPA, 2021). El NMAE de 15 % o menos es aspiracional y no condiciona las compuertas. La brecha exige una intervención sobre las tres variables independientes en 24 meses. La intervención corrige por humedad (X1), modela la fracción gruesa (X2) y calibra con ciclos programados (X3). La disponibilidad de nodos (M) se mantiene en 90 % o más para que existan mediciones.

## F5.4 Incógnitas declaradas

Una incógnita declarada es un dato que el proyecto necesita y no posee. Declararla evita presentar el problema como más conocido de lo que es. La {T:t05} lista cinco incógnitas con su importancia, la estrategia para reducirla y el riesgo si no se resuelve. Cada una se relaciona con un riesgo del capítulo 10 o con un supuesto crítico del Paso 4.

:::TABLA t05 | Incógnitas identificadas del problema
| Incógnita | Importancia | Estrategia para reducirla | Riesgo si no se resuelve |
| --- | --- | --- | --- |
| Línea base de error por departamento | Alta | Colocalizar 10 nodos por sitio durante 16 semanas en el tramo 1 y medir NRMSE, R² y pendiente | La meta de 30 % carece de punto de partida y la compuerta C1 no puede decidir (R-TEC-04) |
| Completitud real de datos en sitios de remoción | Alta | Medir la completitud desde el mes 4 y rotar nodos entre sitios | La meta de 60.000 horas-nodo válidas no se alcanza (R-TEC-02, R-TEC-03) |
| Capacidad de absorción de los custodios | Alta | Calcular el índice ICAR con datos de cada custodio antes de firmar los convenios | La custodia posproyecto no se sostiene (R-ORG-02) |
| Fórmula local del índice AQHI y sus umbrales | Media | Validar la fórmula con los comités y los datos del tramo 1 | Las alertas usan umbrales sin validación local (R-ORG-01) |
| Disponibilidad real del enlace celular y satelital en los sitios | Media | Medir cobertura en la selección de sitios (actividad A1.1) y dimensionar el almacenamiento local de 7 días | Los gateways pierden enlace y la plataforma no recibe datos (R-TEC-03) |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (secciones 7 y 10c). Las actividades y los riesgos corresponden a los capítulos 9 y 10. Naturaleza: PROPUESTO.

La {T:t06} registra la decisión sobre el enunciado tripartito (nodo ND-11).

:::TABLA t06 | Registro de decisión GENESIS: ND-11 Enunciado tripartito del problema
| Campo | Contenido |
| --- | --- |
| NODO | ND-11 Enunciado tripartito del problema |
| CLASE | MAYOR. Fija las variables que los pasos siguientes optimizan y miden. |
| DECISION | Estructurar el problema en metaproblema, problema sustantivo y problema formal, con V06 como variable dependiente y V03, V02 menos V01 y V07 como independientes. |
| DECIDE | Equipo formulador [DATO_USUARIO: responsable de la decisión]. La propuesta proviene de la instancia analítica. |
| EXCLUYE | Latencia y disponibilidad como palancas del sesgo de calibración. Metas de error contradictorias entre secciones. Un efecto en salud como variable de resultado. |
| NODOS_BLANCOS | 3: umbrales de EPA (2021); corrección con estación cercana (Bang et al., 2026, pp. 6-8); redes sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13). |
| NODOS_GRISES | 3: línea base de error propia; articulación con el PDD y la demanda territorial; capacidad de los custodios. |
| RUPTURAS | R-01: 0 \| R-02: 0 \| R-03: 0 \| R-04: 0 \| R-05: 0. |
| PATRON_DOMINANTE | PR-01 (ciclo de atrapamiento): agregar nodos sin calibración local multiplica el ruido y no mejora la decisión. |
| ANTIPATRONES_PR | PR-04 ausente: Sí. PR-05 ausente: No. La formalización supone capacidad de custodia que no se verificó. |
| ESCENA_SIMULABLE | Un técnico del comité compara en el tablero la lectura de un nodo con la del monitor de referencia del mismo sitio y registra la diferencia de la semana. |
| EVIDENCIA_JH_A | El umbral de 30 % y R² de 0,70 procede de un protocolo de la EPA; el nivel actual es VACIO. |
| EVIDENCIA_JH_B | La tabla F5.4 define cada variable con unidad, rango y fuente. |
| CERCA_CONCEPTUAL | El problema formal no es la falta de sensores en el mercado: es la ausencia de error conocido en los sitios. |
| ESTATUTO_CAUSAL | HIE. El efecto de la calibración sobre Y es IDC prospectivo solo bajo el sorteo de F4.3. |
| VEREDICTO | Formulación tripartita adoptada con reserva R-ART (articulación territorial no verificada). |
| RAZON_DEL_DESCARTE | Se descartan la latencia y la disponibilidad como independientes porque no actúan sobre V06 en el ledger de E3. |
| RESULTADO | CIERRA con vacíos declarados (línea base, articulación territorial y custodia). |
:::NOTA *Nota.* Elaboración propia con el protocolo de decisión GENESIS y la ficha maestra (sección 10c).

El Paso 5 crea valor al reemplazar tres metas de error contradictorias por una sola, ligada a un estándar externo. También reconoce que la línea base propia no existe todavía. El Paso 6 usa estas definiciones para generar y comparar alternativas.
