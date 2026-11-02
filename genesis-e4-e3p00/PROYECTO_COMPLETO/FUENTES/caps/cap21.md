%% PREFIJO: 21
# Capítulo 21. Project Charter

El acta de constitución del proyecto, o project charter, autoriza formalmente el proyecto y fija sus requisitos iniciales (PMI, 2021). Este capítulo resume en diez secciones lo que los capítulos 1 a 18 desarrollan con detalle. No introduce decisiones nuevas. Cada cifra procede de la ficha maestra y las tablas se generan desde el libro maestro de datos. Los datos que solo posee el usuario figuran como marcadores [DATO_USUARIO: descripción del dato requerido]. El acta queda sin aprobar hasta que se completen las firmas de la sección 21.10.

## 21.1 Información General

La información general identifica el proyecto para quien lo evalúa y para quien lo audita. Reúne el título, el código, la versión del acta y las fechas. La {T:t01} presenta esos campos junto con el valor solicitado, la contrapartida y el plazo. La columna de naturaleza indica si cada dato es DECLARADO, PROPUESTO, CALCULADO, SUPUESTO o VACIO.

:::TABLA t01 | Ficha de identificación del proyecto
| Campo | Valor | Naturaleza |
| --- | --- | --- |
| Título del proyecto | Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto | DECLARADO |
| Código del caso de formulación | SGR_CONV56_AIRE | PROPUESTO |
| Código de radicación | [DATO_USUARIO: código de radicación asignado por la convocatoria] | VACIO |
| Versión del acta | 1.0, versión de formulación para ratificación | PROPUESTO |
| Fecha de corte de los datos | 13 de octubre de 2026 | DECLARADO |
| Fecha límite de radicación | 11 de noviembre de 2026 | DECLARADO |
| Fecha de aprobación del acta | [DATO_USUARIO: fecha de aprobación por el comité directivo] | VACIO |
| Convocatoria | Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56) | DECLARADO |
| Financiador | Sistema General de Regalías (SGR) / Ministerio de Ciencia, Tecnología e Innovación (MinCiencias) | DECLARADO |
| Tipología | Investigación aplicada, desarrollo tecnológico e innovación | DECLARADO |
| Área OCDE | 1.2 Ingeniería eléctrica, electrónica e informática | DECLARADO |
| Territorio | Departamentos de Caldas, Cundinamarca y Valle del Cauca; 12 municipios focalizados, 4 por departamento [DATO_USUARIO: lista de municipios] | SUPUESTO |
| Duración de ejecución | 24 meses (104 semanas); seguimiento posproyecto de 12 meses | CALCULADO; seguimiento PROPUESTO |
| Nivel de preparación tecnológica (TRL) | Inicial 4; final 7 | PROPUESTO |
| Red de medición | 100 nodos y 10 gateways operativos; 120 nodos y 11 gateways comprados; 3 monitores de referencia | PROPUESTO |
| Valor solicitado al SGR | $ 9.267.260.000 (66,2 % del tope declarado de $ 14.000.000.000) | CALCULADO; tope DECLARADO y NO_VERIFICADO |
| Contrapartida | $ 2.110.000.000 | DECLARADO; desglose de la IES PROPUESTO |
| Total del proyecto | $ 11.377.260.000 | CALCULADO |
| Entidad ejecutora | [DATO_USUARIO: nombre de la IES ejecutora con acreditación de alta calidad] | SUPUESTO |
| Empresa tecnológica aliada | [DATO_USUARIO: razón social de la empresa] | SUPUESTO |
| Director del proyecto | [DATO_USUARIO: nombre del investigador principal] | VACIO |
| Metaprompt y norma | GENESIS-CTeI 36.10 RC2 (VM-PAR3-MDR3-CONT1); NTC 1.1 | DECLARADO |
| Huella SHA-256 declarada del maestro (extraída de la conversación; no se recalcula sobre este documento) | 685a73f45ba1d3011a3b1ba3a1722482c46d8b9a68ffe5cbc4dbe131e4603ba8 | DECLARADO |
:::NOTA *Nota.* Elaboración propia con maestro.py (IDENT, resumen) y la ficha maestra, secciones 1 y 5. Territorio y alianza son SUPUESTO por instrucción del usuario. Los términos de referencia no se aportaron y el tope normativo no está verificado. SGR: Sistema General de Regalías. IES: institución de educación superior.

La tabla separa tres grupos de datos. Los datos de identidad son DECLARADOS por el usuario y se congelaron en esta corrida. Los datos de plazo y de valor son CALCULADOS desde el libro maestro: la ruta crítica suma 104 semanas, equivalentes a 24 meses. El nivel de preparación tecnológica (TRL) final es una decisión PROPUESTA. El expediente E3 declaraba TRL 8 y también un rango de 4 a 7 u 8. El proyecto fija el nivel 7, que corresponde a la demostración de un prototipo en entorno operativo (Mankins, 1995). El nivel 8 exige calificar el sistema completo, y el plazo no cubre esa calificación.

El código y la versión cumplen una función de control. El código SGR_CONV56_AIRE identifica el caso de formulación y no sustituye el código de radicación. Ese código lo asigna la convocatoria [DATO_USUARIO: código de radicación]. La versión 1.0 corresponde a la formulación con corte al 13 de octubre de 2026 (PROPUESTO). La radicación vence el 11 de noviembre de 2026, a 29 días del corte (CALCULADO). Todo cambio de alcance, de plazo o de presupuesto posterior a la aprobación genera una versión nueva. Esa versión requiere el acta de la compuerta que la autoriza. La fecha de aprobación es [DATO_USUARIO: fecha de aprobación del acta por el comité directivo].

## 21.2 Caso de Negocio

El caso de negocio justifica el proyecto por un vacío de información y no por una rentabilidad monetaria. Los comités de gestión del riesgo deciden alertas con mediciones de material particulado cuyo error se desconoce. En Colombia, solo 28 de 1.122 municipios cuentan con estaciones utilizables para estimar la carga de enfermedad (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). Además, 90,8 % de las estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13). El 90,8 % es un cálculo del analista. El expediente E3 declara un error normalizado superior a 45 % en alta humedad. Ese valor carece de localizador y está NO_VERIFICADO. Por eso el proyecto mide su propia línea base en el tramo 1.

Dos lecturas contrastan sobre qué justifica invertir en sensores de bajo costo. La primera sostiene que una corrección local acerca su desempeño al de una referencia. En Seúl, una corrección con estación cercana y 35 minutos de desfase llevó el R² de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8). Barkjohn et al. (2021) desarrollaron una corrección con humedad para PM2,5. La segunda lectura advierte que el desempeño varía con el sensor y con el entorno (Karagulian et al., 2019; Castell et al., 2017). El proyecto no asume que una corrección se transfiera entre contextos. La compuerta C1 decide con los datos del piloto si el modelo cumple en el tramo 1. La compuerta C2 lo decide para los tres departamentos.

La alineación estratégica se apoya en cinco instrumentos. La Ley 1523 de 2012 organiza la gestión del riesgo en procesos de conocimiento, reducción y manejo (Congreso de la República, 2012a). La Ley 2056 de 2020 regula la organización y el funcionamiento del Sistema General de Regalías (Congreso de la República, 2020). El documento CONPES 3943 formula la política de mejoramiento de la calidad del aire (DNP, 2018). El documento CONPES 4069 formula la política nacional de ciencia, tecnología e innovación 2022-2031 (DNP, 2021). El Marco de Sendái orienta la comprensión del riesgo y la preparación (UNDRR, 2015). Cada vínculo con el proyecto es PROPUESTO y NO_VERIFICADO. Los términos de referencia (TdR), los planes de desarrollo y el Anexo 4 no se aportaron, y la reserva R-ART conserva esa limitación.

Los beneficios esperados son técnicos, operativos, institucionales y de continuidad. El beneficio técnico es una red de 100 nodos con error conocido: R² de al menos 0,70 y NRMSE de 30 % o menos frente a referencia. El beneficio operativo es una disponibilidad mensual de nodos de 90 % o más. El beneficio institucional es el uso del tablero por al menos 75 % de los comités focalizados. El beneficio de continuidad se mide 12 meses después del cierre. La meta es activar el protocolo en 80 % de los eventos de superación de umbral. La red debe continuar bajo custodia en 70 %. El proyecto no estima efectos en salud. Sus resultados son técnicos, de adopción y de continuidad.

El caso de negocio no calcula un beneficio monetario. El análisis costo-beneficio exige valorar los resultados en dinero (Boardman et al., 2018). El proyecto carece de línea base de error y de costo de sostenimiento. Ambos datos son VACIO o NO_CALCULABLE. El costo por nodo operativo sirve como referencia de seguimiento: 92,7 millones de COP del SGR y 113,8 millones del total (CALCULADO). Esas cifras no permiten comparar alternativas, porque las alternativas ALT-00 a ALT-02 carecen de costos comparables. La evaluación multicriterio ordena las alternativas con puntajes PROPUESTOS en una escala de 1 a 9. La alternativa ALT-03 obtiene 5,805 y la alternativa ALT-02 obtiene 5,150. El puntaje no equivale a una probabilidad de éxito y requiere la ratificación del panel evaluador.

## 21.3 Descripción del Proyecto

El proyecto implementa una red híbrida de internet de las cosas (IoT) para vigilar PM2,5 y PM10 en sitios de remoción de escombros. La red combina cómputo en el borde y en la nube. Reúne 100 nodos hoja, 10 gateways y tres monitores de referencia gravimétricos, uno por departamento. Los nodos transmiten por LoRa al gateway. El gateway aplica el modelo de corrección por humedad, temperatura y fracción gruesa y reenvía los datos por red celular. Un enlace satelital alterno y un almacenamiento local de 7 días cubren las fallas de enlace. La nube aloja el entrenamiento del modelo, el gemelo digital y el tablero del índice de calidad del aire y salud (AQHI). El proyecto compra 120 nodos y 11 gateways. Los 20 nodos y el gateway adicionales son reserva.

La corrección se define en un solo lugar: el gateway. Dos arquitecturas compiten. La primera centraliza la corrección en la nube. La segunda la ubica en el borde y reduce la dependencia del enlace (Shi et al., 2016). La evaluación multicriterio favoreció la red híbrida, con 5,805 frente a 5,150 para la calibración centralizada. Ese resultado es PROPUESTO y depende de puntajes sin ratificar. La consecuencia es una regla de diseño: ningún nodo ni la nube aplican una segunda corrección.

El despliegue procede por tramos con compuertas de decisión. El tramo 1 instala 30 nodos y 3 gateways en los meses 1 a 12. El tramo 2 agrega 40 nodos y 4 gateways en los meses 13 a 17. El tramo 3 agrega 30 nodos y 3 gateways en los meses 18 a 24. La compuerta C1, en el mes 12, libera la compra del tramo 2. Exige que el modelo cumpla R² de 0,70 o más y NRMSE de 30 % o menos. Exige también que al menos 50 % de los comités del tramo 1 use el tablero. La compuerta C2, en el mes 17, libera el tramo 3. Exige los mismos umbrales en los tres departamentos, disponibilidad mensual de 90 % o más y convenios de custodia con partida. Cooper (2008) describe este tipo de proceso como compuertas que condicionan la inversión siguiente a criterios explícitos.

Los entregables principales son nueve. La {T:t02} los lista con su indicador, su meta final, su paquete de trabajo y su hito de verificación. Cada entregable remite a un indicador del sistema PERS y a un paquete de la estructura de desglose del trabajo.

:::TABLA t02 | Lista de entregables principales y su verificación
| N.º | Entregable | Indicador y meta final | Paquete | Hito de verificación | Naturaleza |
| --- | --- | --- | --- | --- | --- |
| 1 | Red operativa de nodos y gateways con energía solar y enlace alterno | PERS-P01: 100 / 10 al mes 24 | WP2 | H6 y H8 | PROPUESTO |
| 2 | Modelo de corrección validado y aplicado en los gateways | R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia en los tres tramos; PERS-R02: 6 ciclos (2 por tramo) | WP1 | H3, H4 y H7 | PROPUESTO |
| 3 | Base de datos de colocalización y línea base de error medida | PERS-R05: ≥ 60.000 y 4 rotaciones por departamento | WP1 | H2 | PROPUESTO |
| 4 | Gemelo digital y software de corrección registrado | PERS-P02: 1 registro vigente | WP2 | Mes 24 (capítulo 9) | PROPUESTO |
| 5 | Tablero del AQHI y protocolo de alerta con umbrales validados localmente | PERS-E01: ≥ 75 % al mes 24; PERS-E02: ≥ 30 % de reducción relativa | WP3 | H3, H5 y mes 24 | PROPUESTO |
| 6 | Convenios de custodia y personal custodio certificado | PERS-E03: ≥ 60 personas certificadas; PERS-S02: ≥ 70 % a los 12 meses posteriores al cierre | WP3 | H5 y H8 | PROPUESTO |
| 7 | Actividades de apropiación social documentadas | PERS-P04: 29 actividades (20 talleres y 9 jornadas) | WP3 | Seguimiento trimestral; cierre en H8 | PROPUESTO |
| 8 | Artículos científicos en revistas Q1 o Q2 | PERS-P03: 2 sometidos y al menos 1 aceptado al mes 24 | WP1 | Mes 24 (capítulo 9) | PROPUESTO |
| 9 | Evaluación externa independiente y ensayo con laboratorio externo | 2 evaluaciones (meses 12 y 24) y 1 campaña de ensayo (meses 20 a 24) | WP0 y WP1 | H7 | PROPUESTO |
:::NOTA *Nota.* Elaboración propia con indicadores.py (IND), maestro.py (OE, HITOS y líneas S07 y S08) y la ficha maestra, secciones 3, 6 y 8. WP0: gestión, compuertas y cierre; WP1: medición verificada; WP2: red, energía y plataforma; WP3: uso institucional, apropiación y custodia. AQHI: índice de calidad del aire y salud.

La tabla muestra que los entregables se reparten entre los cuatro paquetes de trabajo. El reparto no es uniforme. El paquete WP1 participa en cuatro entregables, el WP3 en tres, el WP2 en dos y el WP0 en uno. Los entregables 5 y 6 dependen del uso institucional, que es el objeto del tercer objetivo específico y de los riesgos R-ORG-01 y R-ORG-02. Por eso las compuertas C1 y C2 verifican el uso del tablero y los convenios de custodia antes de liberar la compra del tramo siguiente.

Los requisitos de alto nivel son seis y cada uno remite a una meta. El primero es el desempeño de la medición: R² de 0,70 o más y NRMSE de 30 % o menos. El segundo es la disponibilidad: 90 % o más de nodos operativos cada mes y pérdida de paquetes de 10 % o menos. El tercero es la autonomía: 14 días sin sol y 7 días de almacenamiento local. El cuarto es el uso institucional: 75 % de los comités al mes 24. El quinto es la custodia, con convenios por tramo y cláusula de apertura. El sexto es la protección de datos personales según la Ley 1581 de 2012 (Congreso de la República, 2012b).

## 21.4 Objetivos Medibles

Los objetivos medibles derivan del objetivo general y de tres objetivos específicos. El objetivo general es reducir el error de medición de material particulado de una red de 100 nodos de bajo costo. Busca también asegurar su uso institucional en Caldas, Cundinamarca y Valle del Cauca durante 24 meses. El primer objetivo específico exige R² de al menos 0,70 y NRMSE de 30 % o menos frente a referencia en los tres tramos. El segundo exige disponibilidad mensual de nodos de 90 % o más y pérdida de paquetes de 10 % o menos. El tercero exige que al menos 75 % de los comités focalizados use el tablero en decisiones documentadas al mes 24.

Los umbrales del primer objetivo siguen los protocolos de la Agencia de Protección Ambiental de Estados Unidos (EPA). Esos protocolos evalúan sensores de PM2,5 en sitio fijo (EPA, 2021). Admiten un uso informativo y no regulatorio. Dos posiciones contrastan sobre el valor de estos datos. La primera trata el dato de sensores como sustituto de la medición regulatoria que fija la Resolución 2254 de 2017 (Ministerio de Ambiente y Desarrollo Sostenible, 2017). La segunda lo trata como información suplementaria con desempeño declarado. El proyecto adopta la segunda y por eso el tablero muestra el error residual junto con cada valor. La meta de NMAE de 15 % o menos es aspiracional y no condiciona las compuertas.

La {T:t03} reúne 12 criterios de éxito con su indicador, su línea base y sus metas. Los criterios de desempeño y de disponibilidad provienen de los objetivos específicos. Los demás son indicadores del sistema PERS.

:::TABLA t03 | Criterios de éxito medibles y metas del proyecto
| Objetivo | Indicador | Línea base | Meta intermedia | Meta final | Frecuencia |
| --- | --- | --- | --- | --- | --- |
| OE1 | Desempeño de la corrección frente a referencia: R² y NRMSE | Se mide en el tramo 1 (VACIO) | Compuerta C1: umbrales en el piloto; compuerta C2: umbrales en los tres departamentos | R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia en los tres tramos | Compuertas C1, C2 y ensayo final |
| OE1 | PERS-R05 Horas-nodo de colocalización válidas | 0 (CALCULADO) | ≥ 60.000 horas-nodo en el tramo 1; ≥ 60.000 + rotaciones trimestrales | ≥ 60.000 y 4 rotaciones por departamento | Mensual |
| OE1 | PERS-R02 Ciclos de calibración ejecutados | 0 (CALCULADO) | 2 ciclos (tramo 1); 4 ciclos acumulados | 6 ciclos (2 por tramo) | Mensual |
| OE2 | Disponibilidad mensual de nodos y pérdida de paquetes | Se mide en el tramo 1 (VACIO) | Compuerta C2: disponibilidad mensual de 90 % o más | Disponibilidad mensual de nodos ≥ 90 % y pérdida de paquetes ≤ 10 % | Mensual |
| OE2 | PERS-P01 Red de 100 nodos y 10 gateways operativa | 0 / 0 (CALCULADO) | 30 / 3 al mes 12; 70 / 7 al mes 17 y 100 / 10 al mes 19 | 100 / 10 al mes 24 | Trimestral |
| OE2 | PERS-R03 Disponibilidad de la plataforma en la nube | VACIO (VACIO) | ≥ 99,0 % | ≥ 99,0 % | Mensual |
| OE3 | PERS-E01 Uso institucional del tablero y del protocolo | VACIO (VACIO) | ≥ 50 % (piloto); ≥ 65 % | ≥ 75 % al mes 24 | Trimestral |
| OE3 | PERS-E02 Reducción relativa de falsas alarmas | Se mide en el tramo 1 (VACIO) | Línea base medida; ≥ 15 % | ≥ 30 % de reducción relativa | Trimestral |
| OE3 | PERS-E03 Capacidad instalada en custodios | 0 (CALCULADO) | 20 personas; 40 personas | ≥ 60 personas certificadas | Semestral |
| OE3 | PERS-S01 Activación del protocolo ante superación de umbral | VACIO (VACIO) | No aplica: medición posproyecto | ≥ 80 % a los 12 meses posteriores al cierre | Anual, 6 a 12 meses tras el cierre |
| OE3 | PERS-S02 Continuidad de la red bajo custodia | VACIO (VACIO) | No aplica: medición posproyecto | ≥ 70 % a los 12 meses posteriores al cierre | Anual, 12 meses tras el cierre |
| Gestión | PERS-R04 Desviación de la ejecución presupuestal | 0 (CALCULADO) | Desviación absoluta ≤ 10 % | Desviación absoluta ≤ 5 % al cierre | Mensual |
:::NOTA *Nota.* Elaboración propia con indicadores.py (IND), maestro.py (OE) y la ficha maestra, secciones 2, 3 y 8. Las metas son PROPUESTO. Las líneas base VACIO se miden en el tramo 1 (DEC-F10). Los indicadores de impacto (PERS-S) se miden entre 6 y 12 meses después del cierre.

La tabla contiene cinco indicadores con línea base sin dato: PERS-R03, PERS-E01, PERS-E02, PERS-S01 y PERS-S02. Las líneas base VACIO se miden en el tramo 1, como fija la decisión DEC-F10. Los dos indicadores de impacto se miden entre 6 y 12 meses después del cierre y por una evaluación externa. Ningún criterio mide exposición ni salud. Gertler et al. (2016) exigen un contrafactual para estimar el impacto de una intervención, y el proyecto no dispone de grupo de comparación. El éxito del proyecto se juzga entonces por mediciones verificadas, uso institucional y continuidad.

## 21.5 Alcance y Exclusiones

El alcance fija qué entrega el proyecto y qué deja fuera. Dentro del alcance están la medición verificada, la red, el tablero con el protocolo de alerta y la custodia por tramos. Fuera del alcance están los efectos en salud, la medición regulatoria, la operación posterior al cierre y los territorios distintos de los tres departamentos. La {T:t04} ordena esa frontera en nueve componentes, con el supuesto o la restricción que sostiene cada decisión.

:::TABLA t04 | Matriz de alcance: dentro, fuera y supuestos o restricciones asociadas
| Componente | Dentro del alcance | Fuera del alcance | Supuesto o restricción |
| --- | --- | --- | --- |
| Medición | PM2,5 y PM10 con 3 monitores gravimétricos de referencia (uno por departamento) y corrección aplicada en el gateway | Otros contaminantes; sustitución de la medición regulatoria de la Resolución 2254 de 2017 | La línea base de error se mide en el tramo 1 |
| Red | 100 nodos y 10 gateways operativos en 12 municipios (120 nodos y 11 gateways comprados) | Más nodos, un cuarto tramo y un año adicional de custodia: opciones sin presupuestar (DEC-F06) | Acceso a los sitios en ventanas secas |
| Energía y enlace | Autonomía mínima de 14 días sin sol, enlace celular con enlace satelital alterno y almacenamiento local de 7 días | Infraestructura eléctrica o de telecomunicaciones de terceros | Cobertura verificada en el estudio de cobertura (S06) |
| Plataforma | Gemelo digital, tablero del AQHI y umbrales validados localmente con los comités | Operación de la plataforma después del mes 24, salvo la custodia entregada | Cláusula de apertura y salida ordenada firmada en H8 |
| Uso institucional | Co-diseño y formación con 15 comités (12 municipales y 3 departamentales) y 150 funcionarios beneficiarios directos | Las decisiones de los comités: el protocolo apoya la decisión y no la sustituye | Comités y funcionarios son SUPUESTO |
| Salud | Reporte de mediciones, de uso institucional y de continuidad | Estimación de exposición individual, de morbilidad o de mortalidad | Sin grupo de comparación ni contrafactual |
| Custodia y transferencia | Convenios por tramo, formación de al menos 60 personas y entrega a custodios en el mes 24 | Financiación de la operación posterior al cierre, a cargo de los custodios | Costo de sostenimiento NO_CALCULABLE |
| Gestión y verificación | Compuertas C1, C2 y C3; evaluación externa (S07); ensayo con laboratorio externo (S08); registro del software | Calificación independiente que sustente el TRL 8 | TRL final 7 (DEC-F05) |
| Apropiación social | 29 actividades documentadas: 20 talleres y 9 jornadas | Actividades adicionales a las 29 y comunicación fuera de los municipios focalizados | Participación con consentimiento informado |
:::NOTA *Nota.* Elaboración propia con la ficha maestra, secciones 2 a 6 y 11 (DEC-F05 y DEC-F06). Naturaleza: la frontera de alcance es PROPUESTO. TRL: nivel de preparación tecnológica. AQHI: índice de calidad del aire y salud.

La tabla deja ver que cada exclusión protege una meta. Excluir la estimación de exposición y de morbilidad evita afirmaciones causales sin contrafactual. Excluir las opciones de ampliación preserva el valor solicitado de 66,2 % del tope. Excluir la calificación independiente fija el TRL final en 7 y no en 8.

Los supuestos críticos del análisis causal son cuatro. SC-1 es la medición verificada, SC-2 la energía y el enlace, SC-3 el uso institucional y SC-4 la custodia. A ellos se suman dos supuestos de formulación. El territorio y la alianza son SUPUESTO por instrucción del usuario, y el acceso a los sitios ocurre en ventanas secas. Las restricciones son cuatro. El tope normativo declarado es de 14.000.000.000 COP y no está verificado, porque los términos de referencia no se aportaron. El plazo es de 24 meses. La corrección se define solo en el gateway. La contrapartida exige certificación.

Dos posiciones disputan cuánto debe cerrarse el alcance. Una lo fija en la formulación para controlar el costo. La otra lo mantiene abierto porque el contexto cambia y el aprendizaje exige adaptar el plan (Patton, 2011). El proyecto cierra el alcance de cada tramo y deja abierto el del tramo siguiente. Cada compuerta decide si el plan se mantiene, se ajusta o se detiene.

## 21.6 Riesgos de Alto Nivel

El registro del proyecto contiene 12 riesgos con un valor monetario esperado (VME) total de 636,5 millones de COP (CALCULADO). La reserva de contingencia se redondea a 636,0 millones. El proceso de la norma ISO 31000 comprende identificar, analizar, evaluar y tratar el riesgo (ISO, 2018). La {T:t05} presenta los cinco riesgos de mayor VME con su estrategia preliminar. Reúnen 471,0 millones de COP, que equivalen a 74,0 % del VME total.

:::TABLA t05 | Riesgos de alto nivel: los cinco de mayor valor monetario esperado
| Id | Riesgo | P × I | Nivel | Prob. (%) | Impacto (M COP) | VME (M COP) | Estrategia preliminar | Disparador |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-FIN-01 | La devaluación del peso encarece los equipos importados. | 4 × 4 = 16 | ALTO | 55 | 300,0 | 165,0 | Mitigar: compra por tramo con cobertura cambiaria y cotizaciones vigentes. | TRM supera en 10 % la de la cotización |
| R-TEC-01 | La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10. | 4 × 5 = 20 | EXTREMO | 60 | 250,0 | 150,0 | Mitigar: modelo de corrección por humedad, banco de calibración y reposición de cabezales. | NRMSE > 30 % en dos verificaciones consecutivas |
| R-ORG-02 | Los custodios no asumen la operación en el posproyecto. | 4 × 4 = 16 | ALTO | 50 | 120,0 | 60,0 | Mitigar: convenios por tramo, formación de custodios y cláusula de apertura. | Convenio sin partida al cierre del tramo 2 |
| R-EXT-01 | Deslizamientos o réplicas bloquean vías y retrasan la instalación. | 4 × 3 = 12 | ALTO | 50 | 120,0 | 60,0 | Aceptar y mitigar: instalación en ventanas secas, técnicos locales y holgura en el cronograma. | Retraso de instalación > 3 semanas |
| R-ORG-01 | Los comités de gestión del riesgo no adoptan el tablero ni el protocolo. | 3 × 5 = 15 | ALTO | 40 | 90,0 | 36,0 | Mitigar: co-diseño de umbrales, formación por comité y uso piloto con registro de decisiones. | Menos de 50 % de uso en el tramo 1 |
| Otros siete | Los siete riesgos restantes: R-DAT-01, R-EXT-02, R-FIN-02, R-JUR-01, R-TEC-02, R-TEC-03, R-TEC-04. | — | MEDIO a ALTO | — | — | 165,5 | Mitigar, evitar o transferir según el capítulo 10 | Según cada riesgo |
:::NOTA *Nota.* Elaboración propia con maestro.RISKS (CALCULADO). P: probabilidad de 1 a 5; I: impacto de 1 a 5; VME: valor monetario esperado, igual a probabilidad por impacto monetario. M COP: millones de pesos colombianos. Los 12 riesgos suman 636,5 millones de COP; la reserva se redondea a 636,0 millones. Orden por VME y, en empate, por P × I. Decimales con coma.

Dos criterios de ordenación contrastan. El nivel, que resulta de multiplicar probabilidad e impacto, prioriza la atención. El VME dimensiona la reserva. El riesgo R-TEC-01 es el único de nivel EXTREMO, con un producto de 20. El riesgo R-FIN-01 presenta el mayor VME, con 165,0 millones frente a 150,0 millones de R-TEC-01. Juntos suman 315,0 millones, que equivalen a 49,5 % del VME. Los otros siete riesgos suman 165,5 millones.

Las estrategias preliminares son de mitigación en casi todos los casos. La compra por tramo reduce la exposición cambiaria acumulada. El modelo de corrección por humedad, el banco de calibración y la reposición de cabezales tratan el sesgo por polvo y humedad. Los convenios por tramo y la cláusula de apertura tratan la falta de custodia. La instalación en ventanas secas y los técnicos locales tratan los bloqueos viales. La holgura del cronograma cubre el co-diseño y la formación, pero no las instalaciones, que pertenecen a la ruta crítica (Anexo H). El capítulo 10 desarrolla el plan de respuesta, los responsables y los disparadores de los 12 riesgos.

## 21.7 Hitos Principales

El cronograma contiene nueve hitos, H0 a H8, entre el mes 2 y el mes 24. La ruta crítica suma 104 semanas y abarca 13 de las 17 actividades (CALCULADO). La {F:f01} ubica los hitos sobre los tres tramos. Los hitos H3 y H5 son compuertas de decisión: C1 en el mes 12 y C2 en el mes 17. El hito H8 cierra el proyecto en el mes 24 con la compuerta C3.

:::FIGURA f01 | Nueve hitos entre el mes 2 y el mes 24; C1 y C2 liberan los tramos 2 y 3 | Nota. Elaboración propia con maestro.HITOS, TRAMOS y ACT (CPM) mediante c21_figs.py; sin componente aleatorio ni semilla; corte de datos 13 de octubre de 2026. El mes de calendario equivale a 52/12 semanas. Naturaleza: CALCULADO; compuertas PROPUESTO.

La figura muestra que el tramo 1 reúne cuatro hitos, el tramo 2 reúne dos y el tramo 3 reúne tres. La concentración inicial responde al riesgo técnico. El piloto debe producir la línea base de error y el modelo validado antes de comprometer la compra siguiente. Los lotes de equipos se compran en los meses 5, 13 y 18, cada uno después de la decisión que lo autoriza.

Dos posiciones contrastan sobre cómo controlar un proyecto de desarrollo. Cooper (2008) propone compuertas formales que decidan avanzar, ajustar o detener. Ries (2011) integra construcción y medición en ciclos cortos de aprendizaje. El proyecto combina ambas. Los ciclos de calibración, dos por tramo, ocurren dentro de cada tramo. Las compuertas ocurren entre tramos. Las fechas clave son el 13 de octubre de 2026, corte de los datos, y el 11 de noviembre de 2026, límite de radicación. Las fechas de calendario de los hitos dependen del acta de inicio [DATO_USUARIO: fecha del acta de inicio].

## 21.8 Presupuesto Resumido

El presupuesto total del proyecto es de 11.377.260.000 COP. El SGR financia 9.267.260.000 COP, que equivalen a 81,5 % del total. La contrapartida suma 2.110.000.000 COP, que equivalen a 18,5 %. El valor solicitado representa 66,2 % del tope declarado de 14.000.000.000 COP. El proyecto no solicita la holgura de 4.732.740.000 COP, conforme a la decisión DEC-F06. La {T:t06} resume la distribución por fuente y por rubro.

:::TABLA t06 | Resumen presupuestal por fuente y por rubro
| Fuente | Rubro o aporte | Valor (M COP) | % de la fuente | % del total | Naturaleza |
| --- | --- | --- | --- | --- | --- |
| SGR | Personal | 4.552,8 | 49,1 | 40,0 | DECLARADO y PROPUESTO |
| SGR | Equipos y software | 1.885,6 | 20,3 | 16,6 | DECLARADO y PROPUESTO |
| SGR | Materiales e insumos | 242,9 | 2,6 | 2,1 | DECLARADO y PROPUESTO |
| SGR | Servicios técnicos | 896,0 | 9,7 | 7,9 | DECLARADO y PROPUESTO |
| SGR | Viajes y viáticos | 462,0 | 5,0 | 4,1 | DECLARADO y PROPUESTO |
| SGR | Otros rubros | 592,0 | 6,4 | 5,2 | DECLARADO y PROPUESTO |
| SGR | Reserva de contingencia | 636,0 | 6,9 | 5,6 | CALCULADO |
| SGR | Subtotal solicitado al SGR | 9.267,3 | 100,0 | 81,5 | CALCULADO |
| Contrapartida IES | Aportes C01 a C04, en especie | 1.100,0 | 52,1 | 9,7 | DECLARADO y PROPUESTO |
| Contrapartida empresa | Aporte C05, en efectivo | 210,0 | 10,0 | 1,8 | DECLARADO |
| Contrapartida empresa | Aporte C06, infraestructura en la nube, en especie | 800,0 | 37,9 | 7,0 | DECLARADO |
| Alcaldías | Sin aporte declarado | 0,0 | 0,0 | 0,0 | VACIO |
| Contrapartida | Subtotal de contrapartida | 2.110,0 | 100,0 | 18,5 | DECLARADO y PROPUESTO |
| Proyecto | Total del proyecto | 11.377,3 | — | 100,0 | CALCULADO |
:::NOTA *Nota.* Elaboración propia con maestro.resumen(), BUDGET y CONTRA. M COP: millones de pesos colombianos. Valores exactos: SGR $ 9.267.260.000; contrapartida $ 2.110.000.000; total $ 11.377.260.000. La contrapartida está pendiente de certificación. Los porcentajes se redondean a un decimal. Decimales con coma.

La distribución muestra un proyecto intensivo en talento. Personal reúne 49,1 % del valor solicitado y equipos y software reúne 20,3 %. La contrapartida equivale a 22,8 % del valor solicitado. La especie representa 90,0 % de ese aporte, y las alcaldías no declaran aporte (VACIO). Por esa razón la certificación de la contrapartida es una condición que vigila el riesgo R-FIN-02. El flujo semestral del SGR es de 2.689,3, 1.936,1, 2.634,1 y 2.007,8 millones de COP. El flujo semestral de la contrapartida es de 527,5 millones.

Dos prácticas contrastan en la solicitud de recursos: pedir el tope disponible o pedir la suma que cada actividad justifica. La primera maximiza el recurso. La segunda permite rastrear cada peso hasta una línea con paquete y meses. El proyecto adopta la segunda. La holgura se describe como opciones de ampliación condicionadas a los TdR: más nodos, un cuarto tramo y un año adicional de custodia. Esas opciones no se presupuestan.

Dos partidas protegen el valor solicitado. La reserva de contingencia es de 636.000.000 COP, equivalente a 6,9 % del valor solicitado. Es la suma de los VME de los 12 riesgos, redondeada a millones, y su admisibilidad como rubro depende de los TdR (VACIO). La administración suma 360.000.000 COP, equivalente a 3,9 % del valor solicitado. El tope porcentual de administración del expediente E3, de 5 %, no se verificó.

## 21.9 Stakeholders Clave

Los interesados clave se agrupan por rol y no por nombre. El patrocinador es el convocante y los órganos de decisión del SGR, que aprueban la asignación y fijan los términos (DECLARADO). La entidad ejecutora es una institución de educación superior con acreditación de alta calidad [DATO_USUARIO: nombre de la IES] (SUPUESTO). La empresa tecnológica aliada responde por la propiedad intelectual y por el código de la plataforma [DATO_USUARIO: razón social] (SUPUESTO). El director del proyecto es el investigador principal, con dedicación de 0,5 equivalentes de tiempo completo. Lo acompaña la gerencia del proyecto [DATO_USUARIO: nombre del investigador principal y de la gerencia].

La {F:f02} ordena 12 actores en cinco grupos: decide y financia, ejecuta, custodia y usa, afectados y posibles financiadores, y referencia y control. En el grupo de custodia y uso están las alcaldías de los 12 municipios focalizados y las gobernaciones. También está la UNGRD, con los puestos de mando unificado. El IDEAM y las autoridades ambientales aportan la referencia metrológica. Las constructoras y los contratistas de remoción generan la emisión y se ven afectados por los paros. Los operarios y las comunidades colindantes se exponen al material particulado. Mitchell et al. (1997) definen la relevancia de un actor por su poder, su legitimidad y su urgencia. El expediente documenta solo el poder del convocante. Los atributos de los otros 11 actores son NO_EVALUADO. Dos actores ejercen veto: el convocante y las alcaldías de los municipios con remoción.

:::FIGURA f02 | Doce actores sin relevancia evaluada; solo el convocante tiene poder documentado | Nota. Elaboración propia con el análisis de actores de 4.4-MDR.5; script c21_figs.py, sin componente aleatorio ni semilla; corte de datos 13 de octubre de 2026. El borde grueso marca actores con veto. Poder, legitimidad y urgencia: NO_EVALUADO salvo el poder del convocante. Alianza SUPUESTO; ningún actor firmó compromiso.

La figura implica una decisión de gestión. Ningún actor firmó compromiso, y la alianza es SUPUESTO por instrucción del usuario. El análisis de actores modela la custodia como un juego de bien público cuyo equilibrio es que ninguna entidad asuma la operación (Scharpf, 1997). Los tramos condicionados cambian esos pagos, porque cada transferencia exige capacidad demostrada. Mientras no existan las cartas del Anexo A, el proyecto trata a las alcaldías como custodios potenciales sujetos a las compuertas C1 y C2.

## 21.10 Autorización

La autorización formaliza el acta y activa la ejecución. La {T:t07} lista los cinco roles que firman: el patrocinador, las dos entidades co-ejecutoras, el director y la gerencia. Los nombres y las fechas son datos que solo posee el usuario. La fecha de autorización es [DATO_USUARIO: fecha de autorización]. El acta entra en vigor con la última firma.

:::TABLA t07 | Firmas de autorización del acta de constitución
| Rol | Responsabilidad en la autorización | Nombre y cargo | Firma | Fecha |
| --- | --- | --- | --- | --- |
| Patrocinador | Aprueba la asignación y fija los términos de la convocatoria | [DATO_USUARIO: nombre y cargo de quien representa al convocante] |  | [DATO_USUARIO: fecha de firma] |
| Representante legal de la entidad ejecutora | Compromete la ejecución legal y la contrapartida de la IES | [DATO_USUARIO: nombre y cargo] |  | [DATO_USUARIO: fecha de firma] |
| Representante legal de la empresa tecnológica | Compromete la contrapartida de la empresa y el acuerdo de titularidad | [DATO_USUARIO: nombre y cargo] |  | [DATO_USUARIO: fecha de firma] |
| Director del proyecto | Certifica el criterio técnico de cada compuerta | [DATO_USUARIO: nombre del investigador principal] |  | [DATO_USUARIO: fecha de firma] |
| Gerente del proyecto | Certifica presupuesto, cronograma y riesgos de cada compuerta | [DATO_USUARIO: nombre de la persona a cargo de la gerencia] |  | [DATO_USUARIO: fecha de firma] |
:::NOTA *Nota.* Elaboración propia. Ninguna persona firmó el acta: los nombres y las fechas son datos que solo el usuario posee. Los roles son PROPUESTO y se ratifican en el comité directivo.

La gerencia del proyecto administra el alcance, el cronograma, el presupuesto y la preparación de las compuertas. Responde ante el comité directivo (PROPUESTO). No decide las compuertas C1, C2 y C3. Las decide el comité con dos certificaciones: la técnica del investigador principal y la de gerencia sobre costo, plazo y riesgos. Todo cambio del valor solicitado, del plazo o de los umbrales de desempeño exige una versión nueva del acta. El límite de reasignación entre rubros depende de los TdR [DATO_USUARIO: porcentaje máximo de reasignación entre rubros].
