%% PREFIJO: 21
# Capítulo 21. Project Charter

El acta de constitución del proyecto, o project charter, autoriza formalmente el proyecto y fija sus requisitos iniciales (PMI, 2021). Este capítulo resume en diez secciones lo que los capítulos 1 a 18 desarrollan con detalle. No introduce decisiones nuevas. Cada cifra procede de la ficha maestra y las tablas se generan desde el libro maestro de datos. Los datos que solo posee el usuario figuran como marcadores [DATO_USUARIO]. El acta queda sin aprobar hasta que se completen las firmas de la sección 21.10.

## 21.1 Información General

La información general identifica el proyecto para quien lo evalúa y para quien lo audita. Reúne el título, el código, la versión del acta y las fechas. La {T:t01} presenta esos campos junto con el valor solicitado, la contrapartida y el plazo. La columna de naturaleza indica si cada dato es DECLARADO, PROPUESTO, CALCULADO, SUPUESTO o VACIO.

@@TABLA t01@@

La tabla separa tres grupos de datos. Los datos de identidad son DECLARADOS por el usuario y se congelaron en esta corrida. Los datos de plazo y de valor son CALCULADOS desde el libro maestro: la ruta crítica suma <<semanas>> semanas, equivalentes a <<meses>> meses. El nivel de preparación tecnológica (TRL) final es una decisión PROPUESTA. El expediente E3 declaraba TRL 8 y también un rango de 4 a 7 u 8. El proyecto fija el nivel 7, que corresponde a la demostración de un prototipo en entorno operativo (Mankins, 1995). El nivel 8 exige calificar el sistema completo, y el plazo no cubre esa calificación.

El código y la versión cumplen una función de control. El código SGR_CONV56_AIRE identifica el caso de formulación y no sustituye el código de radicación. Ese código lo asigna la convocatoria [DATO_USUARIO: código de radicación]. La versión 1.0 corresponde a la formulación con corte al 13 de octubre de 2026 (PROPUESTO). La radicación vence el 11 de noviembre de 2026, a <<dias>> días del corte (CALCULADO). Todo cambio de alcance, de plazo o de presupuesto posterior a la aprobación genera una versión nueva. Esa versión requiere el acta de la compuerta que la autoriza. La fecha de aprobación es [DATO_USUARIO: fecha de aprobación del acta por el comité directivo].

## 21.2 Caso de Negocio

El caso de negocio justifica el proyecto por un vacío de información y no por una rentabilidad monetaria. Los comités de gestión del riesgo deciden alertas con mediciones de material particulado cuyo error se desconoce. En Colombia, solo 28 de 1.122 municipios cuentan con estaciones utilizables para estimar la carga de enfermedad (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). Además, 90,8 % de las estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13). El 90,8 % es un cálculo del analista. El expediente E3 declara un error normalizado superior a 45 % en alta humedad. Ese valor carece de localizador y está NO_VERIFICADO. Por eso el proyecto mide su propia línea base en el tramo 1.

Dos lecturas contrastan sobre qué justifica invertir en sensores de bajo costo. La primera sostiene que una corrección local acerca su desempeño al de una referencia. En Seúl, una corrección con estación cercana y 35 minutos de desfase llevó el R² de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8). Barkjohn et al. (2021) desarrollaron una corrección con humedad para PM2,5. La segunda lectura advierte que el desempeño varía con el sensor y con el entorno (Karagulian et al., 2019; Castell et al., 2017). El proyecto no asume que una corrección se transfiera entre contextos. La compuerta C1 decide con los datos del piloto si el modelo cumple en el tramo 1. La compuerta C2 lo decide para los tres departamentos.

La alineación estratégica se apoya en cinco instrumentos. La Ley 1523 de 2012 organiza la gestión del riesgo en procesos de conocimiento, reducción y manejo (Congreso de la República, 2012a). La Ley 2056 de 2020 regula la organización y el funcionamiento del Sistema General de Regalías (Congreso de la República, 2020). El documento CONPES 3943 formula la política de mejoramiento de la calidad del aire (DNP, 2018). El documento CONPES 4069 formula la política nacional de ciencia, tecnología e innovación 2022-2031 (DNP, 2021). El Marco de Sendái orienta la comprensión del riesgo y la preparación (UNDRR, 2015). Cada vínculo con el proyecto es PROPUESTO y NO_VERIFICADO. Los términos de referencia (TdR), los planes de desarrollo y el Anexo 4 no se aportaron, y la reserva R-ART conserva esa limitación.

Los beneficios esperados son técnicos, operativos, institucionales y de continuidad. El beneficio técnico es una red de <<nodos>> nodos con error conocido: R² de al menos 0,70 y NRMSE de 30 % o menos frente a referencia. El beneficio operativo es una disponibilidad mensual de nodos de 90 % o más. El beneficio institucional es el uso del tablero por al menos 75 % de los comités focalizados. El beneficio de continuidad se mide 12 meses después del cierre. La meta es activar el protocolo en 80 % de los eventos de superación de umbral. La red debe continuar bajo custodia en 70 %. El proyecto no estima efectos en salud. Sus resultados son técnicos, de adopción y de continuidad.

El caso de negocio no calcula un beneficio monetario. El análisis costo-beneficio exige valorar los resultados en dinero (Boardman et al., 2018). El proyecto carece de línea base de error y de costo de sostenimiento. Ambos datos son VACIO o NO_CALCULABLE. El costo por nodo operativo sirve como referencia de seguimiento: <<sgr_nodo>> millones de COP del SGR y <<tot_nodo>> millones del total (CALCULADO). Esas cifras no permiten comparar alternativas, porque las alternativas ALT-00 a ALT-02 carecen de costos comparables. La evaluación multicriterio ordena las alternativas con puntajes PROPUESTOS en una escala de 1 a 9. La alternativa ALT-03 obtiene <<alt03>> y la alternativa ALT-02 obtiene <<alt02>>. El puntaje no equivale a una probabilidad de éxito y requiere la ratificación del panel evaluador.

## 21.3 Descripción del Proyecto

El proyecto implementa una red híbrida de internet de las cosas (IoT) para vigilar PM2,5 y PM10 en sitios de remoción de escombros. La red combina cómputo en el borde y en la nube. Reúne <<nodos>> nodos hoja, <<gw>> gateways y <<refs>> monitores de referencia gravimétricos, uno por departamento. Los nodos transmiten por LoRa al gateway. El gateway aplica el modelo de corrección por humedad, temperatura y fracción gruesa y reenvía los datos por red celular. Un enlace satelital alterno y un almacenamiento local de 7 días cubren las fallas de enlace. La nube aloja el entrenamiento del modelo, el gemelo digital y el tablero del índice de calidad del aire y salud (AQHI). El proyecto compra <<nodos_c>> nodos y <<gw_c>> gateways. Los <<nodos_res>> nodos y el gateway adicionales son reserva.

La corrección se define en un solo lugar: el gateway. Dos arquitecturas compiten. La primera centraliza la corrección en la nube. La segunda la ubica en el borde y reduce la dependencia del enlace (Shi et al., 2016). La evaluación multicriterio favoreció la red híbrida, con <<alt03>> frente a <<alt02>> para la calibración centralizada. Ese resultado es PROPUESTO y depende de puntajes sin ratificar. La consecuencia es una regla de diseño: ningún nodo ni la nube aplican una segunda corrección.

El despliegue procede por tramos con compuertas de decisión. El tramo 1 instala 30 nodos y 3 gateways en los meses 1 a 12. El tramo 2 agrega 40 nodos y 4 gateways en los meses 13 a 17. El tramo 3 agrega 30 nodos y 3 gateways en los meses 18 a 24. La compuerta C1, en el mes <<mes_c1>>, libera la compra del tramo 2. Exige que el modelo cumpla R² de 0,70 o más y NRMSE de 30 % o menos. Exige también que al menos 50 % de los comités del tramo 1 use el tablero. La compuerta C2, en el mes <<mes_c2>>, libera el tramo 3. Exige los mismos umbrales en los tres departamentos, disponibilidad mensual de 90 % o más y convenios de custodia con partida. Cooper (2008) describe este tipo de proceso como compuertas que condicionan la inversión siguiente a criterios explícitos.

Los entregables principales son <<n_entreg>>. La {T:t02} los lista con su indicador, su meta final, su paquete de trabajo y su hito de verificación. Cada entregable remite a un indicador del sistema PERS y a un paquete de la estructura de desglose del trabajo.

@@TABLA t02@@

La tabla muestra que los entregables se reparten entre los cuatro paquetes de trabajo. El reparto no es uniforme. El paquete WP1 participa en <<n_wp1>> entregables, el WP3 en <<n_wp3>>, el WP2 en <<n_wp2>> y el WP0 en <<n_wp0>>. Los entregables 5 y 6 dependen del uso institucional, que es el objeto del tercer objetivo específico y de los riesgos R-ORG-01 y R-ORG-02. Por eso las compuertas C1 y C2 verifican el uso del tablero y los convenios de custodia antes de liberar la compra del tramo siguiente.

Los requisitos de alto nivel son seis y cada uno remite a una meta. El primero es el desempeño de la medición: R² de 0,70 o más y NRMSE de 30 % o menos. El segundo es la disponibilidad: 90 % o más de nodos operativos cada mes y pérdida de paquetes de 10 % o menos. El tercero es la autonomía: 14 días sin sol y 7 días de almacenamiento local. El cuarto es el uso institucional: 75 % de los comités al mes 24. El quinto es la custodia, con convenios por tramo y cláusula de apertura. El sexto es la protección de datos personales según la Ley 1581 de 2012 (Congreso de la República, 2012b).

## 21.4 Objetivos Medibles

Los objetivos medibles derivan del objetivo general y de tres objetivos específicos. El objetivo general es reducir el error de medición de material particulado de una red de <<nodos>> nodos de bajo costo. Busca también asegurar su uso institucional en Caldas, Cundinamarca y Valle del Cauca durante <<meses>> meses. El primer objetivo específico exige R² de al menos 0,70 y NRMSE de 30 % o menos frente a referencia en los tres tramos. El segundo exige disponibilidad mensual de nodos de 90 % o más y pérdida de paquetes de 10 % o menos. El tercero exige que al menos 75 % de los comités focalizados use el tablero en decisiones documentadas al mes 24.

Los umbrales del primer objetivo siguen los protocolos de la Agencia de Protección Ambiental de Estados Unidos (EPA). Esos protocolos evalúan sensores de PM2,5 en sitio fijo (EPA, 2021). Admiten un uso informativo y no regulatorio. Dos posiciones contrastan sobre el valor de estos datos. La primera trata el dato de sensores como sustituto de la medición regulatoria que fija la Resolución 2254 de 2017 (Ministerio de Ambiente y Desarrollo Sostenible, 2017). La segunda lo trata como información suplementaria con desempeño declarado. El proyecto adopta la segunda y por eso el tablero muestra el error residual junto con cada valor. La meta de NMAE de 15 % o menos es aspiracional y no condiciona las compuertas.

La {T:t03} reúne <<n_criterios>> criterios de éxito con su indicador, su línea base y sus metas. Los criterios de desempeño y de disponibilidad provienen de los objetivos específicos. Los demás son indicadores del sistema PERS.

@@TABLA t03@@

La tabla contiene <<n_ind_vacio>> indicadores con línea base sin dato: PERS-R03, PERS-E01, PERS-E02, PERS-S01 y PERS-S02. Las líneas base VACIO se miden en el tramo 1, como fija la decisión DEC-F10. Los dos indicadores de impacto se miden entre 6 y 12 meses después del cierre y por una evaluación externa. Ningún criterio mide exposición ni salud. Gertler et al. (2016) exigen un contrafactual para estimar el impacto de una intervención, y el proyecto no dispone de grupo de comparación. El éxito del proyecto se juzga entonces por mediciones verificadas, uso institucional y continuidad.

## 21.5 Alcance y Exclusiones

El alcance fija qué entrega el proyecto y qué deja fuera. Dentro del alcance están la medición verificada, la red, el tablero con el protocolo de alerta y la custodia por tramos. Fuera del alcance están los efectos en salud, la medición regulatoria, la operación posterior al cierre y los territorios distintos de los tres departamentos. La {T:t04} ordena esa frontera en <<n_alcance>> componentes, con el supuesto o la restricción que sostiene cada decisión.

@@TABLA t04@@

La tabla deja ver que cada exclusión protege una meta. Excluir la estimación de exposición y de morbilidad evita afirmaciones causales sin contrafactual. Excluir las opciones de ampliación preserva el valor solicitado de <<pct_tope>> % del tope. Excluir la calificación independiente fija el TRL final en 7 y no en 8.

Los supuestos críticos del análisis causal son cuatro. SC-1 es la medición verificada, SC-2 la energía y el enlace, SC-3 el uso institucional y SC-4 la custodia. A ellos se suman dos supuestos de formulación. El territorio y la alianza son SUPUESTO por instrucción del usuario, y el acceso a los sitios ocurre en ventanas secas. Las restricciones son cuatro. El tope normativo declarado es de <<tope_cop>> COP y no está verificado, porque los términos de referencia no se aportaron. El plazo es de <<meses>> meses. La corrección se define solo en el gateway. La contrapartida exige certificación.

Dos posiciones disputan cuánto debe cerrarse el alcance. Una lo fija en la formulación para controlar el costo. La otra lo mantiene abierto porque el contexto cambia y el aprendizaje exige adaptar el plan (Patton, 2011). El proyecto cierra el alcance de cada tramo y deja abierto el del tramo siguiente. Cada compuerta decide si el plan se mantiene, se ajusta o se detiene.

## 21.6 Riesgos de Alto Nivel

El registro del proyecto contiene 12 riesgos con un valor monetario esperado (VME) total de <<vme_sum>> millones de COP (CALCULADO). La reserva de contingencia se redondea a <<res_mm>> millones. El proceso de la norma ISO 31000 comprende identificar, analizar, evaluar y tratar el riesgo (ISO, 2018). La {T:t05} presenta los cinco riesgos de mayor VME con su estrategia preliminar. Reúnen <<emv_top5>> millones de COP, que equivalen a <<emv_top5_pct>> % del VME total.

@@TABLA t05@@

Dos criterios de ordenación contrastan. El nivel, que resulta de multiplicar probabilidad e impacto, prioriza la atención. El VME dimensiona la reserva. El riesgo R-TEC-01 es el único de nivel EXTREMO, con un producto de 20. El riesgo R-FIN-01 presenta el mayor VME, con <<emv_fin>> millones frente a <<emv_tec>> millones de R-TEC-01. Juntos suman <<emv_21>> millones, que equivalen a <<emv_21_pct>> % del VME. Los otros siete riesgos suman <<emv_otros>> millones.

Las estrategias preliminares son de mitigación en casi todos los casos. La compra por tramo reduce la exposición cambiaria acumulada. El modelo de corrección por humedad, el banco de calibración y la reposición de cabezales tratan el sesgo por polvo y humedad. Los convenios por tramo y la cláusula de apertura tratan la falta de custodia. La instalación en ventanas secas y los técnicos locales tratan los bloqueos viales. La holgura del cronograma cubre el co-diseño y la formación, pero no las instalaciones, que pertenecen a la ruta crítica (Anexo H). El capítulo 10 desarrolla el plan de respuesta, los responsables y los disparadores de los 12 riesgos.

## 21.7 Hitos Principales

El cronograma contiene nueve hitos, H0 a H8, entre el mes 2 y el mes 24. La ruta crítica suma <<semanas>> semanas y abarca <<n_rc>> de las <<n_act>> actividades (CALCULADO). La {F:f01} ubica los hitos sobre los tres tramos. Los hitos H3 y H5 son compuertas de decisión: C1 en el mes <<mes_c1>> y C2 en el mes <<mes_c2>>. El hito H8 cierra el proyecto en el mes 24 con la compuerta C3.

:::FIGURA f01 | Nueve hitos entre el mes 2 y el mes 24; C1 y C2 liberan los tramos 2 y 3 | Nota. Elaboración propia con maestro.HITOS, TRAMOS y ACT (CPM) mediante c21_figs.py; sin componente aleatorio ni semilla; corte de datos 13 de octubre de 2026. El mes de calendario equivale a 52/12 semanas. Naturaleza: CALCULADO; compuertas PROPUESTO.

La figura muestra que el tramo 1 reúne <<h_t1>> hitos, el tramo 2 reúne <<h_t2>> y el tramo 3 reúne <<h_t3>>. La concentración inicial responde al riesgo técnico. El piloto debe producir la línea base de error y el modelo validado antes de comprometer la compra siguiente. Los lotes de equipos se compran en los meses 5, 13 y 18, cada uno después de la decisión que lo autoriza.

Dos posiciones contrastan sobre cómo controlar un proyecto de desarrollo. Cooper (2008) propone compuertas formales que decidan avanzar, ajustar o detener. Ries (2011) integra construcción y medición en ciclos cortos de aprendizaje. El proyecto combina ambas. Los ciclos de calibración, dos por tramo, ocurren dentro de cada tramo. Las compuertas ocurren entre tramos. Las fechas clave son el 13 de octubre de 2026, corte de los datos, y el 11 de noviembre de 2026, límite de radicación. Las fechas de calendario de los hitos dependen del acta de inicio [DATO_USUARIO: fecha del acta de inicio].

## 21.8 Presupuesto Resumido

El presupuesto total del proyecto es de <<tot_cop>> COP. El SGR financia <<sgr_cop>> COP, que equivalen a <<pct_sgr_tot>> % del total. La contrapartida suma <<con_cop>> COP, que equivalen a <<pct_con_tot>> %. El valor solicitado representa <<pct_tope>> % del tope declarado de <<tope_cop>> COP. El proyecto no solicita la holgura de <<holgura_cop>> COP, conforme a la decisión DEC-F06. La {T:t06} resume la distribución por fuente y por rubro.

@@TABLA t06@@

La distribución muestra un proyecto intensivo en talento. Personal reúne <<pct_pers>> % del valor solicitado y equipos y software reúne <<pct_eq>> %. La contrapartida equivale a <<pct_con_sgr>> % del valor solicitado. La especie representa <<pct_especie>> % de ese aporte, y las alcaldías no declaran aporte (VACIO). Por esa razón la certificación de la contrapartida es una condición que vigila el riesgo R-FIN-02. El flujo semestral del SGR es de <<f1>>, <<f2>>, <<f3>> y <<f4>> millones de COP. El flujo semestral de la contrapartida es de <<c1>> millones.

Dos prácticas contrastan en la solicitud de recursos: pedir el tope disponible o pedir la suma que cada actividad justifica. La primera maximiza el recurso. La segunda permite rastrear cada peso hasta una línea con paquete y meses. El proyecto adopta la segunda. La holgura se describe como opciones de ampliación condicionadas a los TdR: más nodos, un cuarto tramo y un año adicional de custodia. Esas opciones no se presupuestan.

Dos partidas protegen el valor solicitado. La reserva de contingencia es de <<res_cop>> COP, equivalente a <<res_pct>> % del valor solicitado. Es la suma de los VME de los 12 riesgos, redondeada a millones, y su admisibilidad como rubro depende de los TdR (VACIO). La administración suma <<adm_cop>> COP, equivalente a <<adm_pct>> % del valor solicitado. El tope porcentual de administración del expediente E3, de 5 %, no se verificó.

## 21.9 Stakeholders Clave

Los interesados clave se agrupan por rol y no por nombre. El patrocinador es el convocante y los órganos de decisión del SGR, que aprueban la asignación y fijan los términos (DECLARADO). La entidad ejecutora es una institución de educación superior con acreditación de alta calidad [DATO_USUARIO: nombre de la IES] (SUPUESTO). La empresa tecnológica aliada responde por la propiedad intelectual y por el código de la plataforma [DATO_USUARIO: razón social] (SUPUESTO). El director del proyecto es el investigador principal, con dedicación de <<etc_ip>> equivalentes de tiempo completo. Lo acompaña la gerencia del proyecto [DATO_USUARIO: nombre del investigador principal y de la gerencia].

La {F:f02} ordena 12 actores en cinco grupos: decide y financia, ejecuta, custodia y usa, afectados y posibles financiadores, y referencia y control. En el grupo de custodia y uso están las alcaldías de los 12 municipios focalizados y las gobernaciones. También está la UNGRD, con los puestos de mando unificado. El IDEAM y las autoridades ambientales aportan la referencia metrológica. Las constructoras y los contratistas de remoción generan la emisión y se ven afectados por los paros. Los operarios y las comunidades colindantes se exponen al material particulado. Mitchell et al. (1997) definen la relevancia de un actor por su poder, su legitimidad y su urgencia. El expediente documenta solo el poder del convocante. Los atributos de los otros 11 actores son NO_EVALUADO. Dos actores ejercen veto: el convocante y las alcaldías de los municipios con remoción.

:::FIGURA f02 | Doce actores sin relevancia evaluada; solo el convocante tiene poder documentado | Nota. Elaboración propia con el análisis de actores de 4.4-MDR.5; script c21_figs.py, sin componente aleatorio ni semilla; corte de datos 13 de octubre de 2026. El borde grueso marca actores con veto. Poder, legitimidad y urgencia: NO_EVALUADO salvo el poder del convocante. Alianza SUPUESTO; ningún actor firmó compromiso.

La figura implica una decisión de gestión. Ningún actor firmó compromiso, y la alianza es SUPUESTO por instrucción del usuario. El análisis de actores modela la custodia como un juego de bien público cuyo equilibrio es que ninguna entidad asuma la operación (Scharpf, 1997). Los tramos condicionados cambian esos pagos, porque cada transferencia exige capacidad demostrada. Mientras no existan las cartas del Anexo A, el proyecto trata a las alcaldías como custodios potenciales sujetos a las compuertas C1 y C2.

## 21.10 Autorización

La autorización formaliza el acta y activa la ejecución. La {T:t07} lista los cinco roles que firman: el patrocinador, las dos entidades co-ejecutoras, el director y la gerencia. Los nombres y las fechas son datos que solo posee el usuario. La fecha de autorización es [DATO_USUARIO: fecha de autorización]. El acta entra en vigor con la última firma.

@@TABLA t07@@

La gerencia del proyecto administra el alcance, el cronograma, el presupuesto y la preparación de las compuertas. Responde ante el comité directivo (PROPUESTO). No decide las compuertas C1, C2 y C3. Las decide el comité con dos certificaciones: la técnica del investigador principal y la de gerencia sobre costo, plazo y riesgos. Todo cambio del valor solicitado, del plazo o de los umbrales de desempeño exige una versión nueva del acta. El límite de reasignación entre rubros depende de los TdR [DATO_USUARIO: porcentaje máximo de reasignación entre rubros].
