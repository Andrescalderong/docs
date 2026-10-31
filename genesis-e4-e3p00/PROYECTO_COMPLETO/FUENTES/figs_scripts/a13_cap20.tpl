%% PREFIJO: 20
# Capítulo 20. Anexos técnicos

Los anexos de este capítulo se agrupan en dos clases según su origen. Los anexos E, F, G, H e I se derivan del proyecto y se redactan por completo. Son los instrumentos, el modelo de consentimiento, el presupuesto, el cronograma y los estudios previos. Los anexos A, B, C, D y J son documentos que solo el usuario posee o que emiten terceros. Para cada uno, el capítulo entrega una lista de verificación. La lista indica el documento, quién lo emite, su contenido mínimo y la línea del proyecto que lo exige. No redacta cartas, hojas de vida ni certificados, porque ninguna persona ni entidad los firmó. La alianza es SUPUESTO por instrucción del usuario. Los términos de referencia (TdR) no se aportaron, y por eso los requisitos exactos de cada documento quedan como [DATO_USUARIO]. Los anexos K a M, que siguen a este bloque, documentan el respaldo del análisis causal.

## Anexo A. Cartas de compromiso y avales

Las cartas de compromiso convierten una alianza supuesta en obligaciones verificables. El proyecto depende de ellas por tres razones. La contrapartida de <<con_cop>> COP requiere certificación de quien la aporta. La custodia por tramo requiere partida y competencia de cada alcaldía. El uso del tablero requiere que quienes aplican el protocolo lo acepten. La {T:t01} lista los ocho documentos, quién los emite, su contenido mínimo y la línea del proyecto que los exige.

@@TABLA t01@@

La lista separa dos clases de carta. Las de contrapartida (A1 y A2) afectan la admisibilidad financiera y el riesgo R-FIN-02. Las de custodia y uso (A4 a A6) afectan el tercer objetivo específico y la compuerta C2. Ostrom (2005) distingue reglas de posición, de información y de pago en un arreglo institucional. La carta de la alcaldía fija una regla de posición, porque asigna la competencia de operar los nodos. La partida fija una regla de pago. Una carta de intención sin partida no basta. El riesgo R-ORG-02 se activa cuando un convenio llega al cierre del tramo 2 sin partida. Ninguna de las ocho cartas se aportó, y todas figuran en estado VACIO.

## Anexo B. Hojas de vida completas

Las hojas de vida respaldan los <<n_perfiles>> perfiles del equipo. El capítulo 17 describe cada perfil por su competencia verificable y no por una persona. Los perfiles suman <<n_personas_total>> personas: <<n_pers>> financiadas por el SGR y <<n_cpers>> aportadas por la IES como contrapartida. Un total de <<perf_nombrados>> perfiles, con <<n_nombradas>> personas, requiere hoja de vida desde la radicación. Los perfiles P01, P02 y P10 suman <<n_sel>> personas y se vinculan por selección posterior a la aprobación. La {T:t02} lista cada perfil con la competencia que su hoja de vida debe soportar.

@@TABLA t02@@

Cada hoja de vida debe contener cuatro grupos de datos. Son la identificación, la formación con soportes, la experiencia en el perfil con certificaciones y la dedicación al proyecto. La dedicación se expresa en equivalentes de tiempo completo (ETC): <<etc>> ETC promedio para el personal del SGR y <<etc_ies>> ETC para la IES. Los formatos y los años mínimos de experiencia dependen de los TdR [DATO_USUARIO: formato y requisitos de experiencia de los términos de referencia]. La tabla no afirma títulos, años ni nombres.

La consecuencia es una regla de verificación. Ninguna persona se cuenta como vinculada sin hoja de vida con soportes. Los perfiles de selección posterior se completan en la actividad A0.1, de contratación y convenios, que termina en la semana 8. Un perfil sin persona verificada al cierre de esa actividad queda como vacante y se reporta en el hito H0 (PROPUESTO).

## Anexo C. Cotizaciones de equipos

No existen cotizaciones formales de los equipos. Los valores unitarios de las líneas E01 a E12 son valores de formulación. De esas 12 líneas, <<n_decl_e>> proceden del expediente E3 (DECLARADO) y <<n_prop_e>> son decisiones de esta formulación (PROPUESTO). El rubro de equipos y software suma <<eq_cop>> COP, que equivalen a <<eq_pct>> % del valor solicitado al SGR. La {T:t03} lista las 12 líneas con su valor de formulación y el soporte que falta.

@@TABLA t03@@

La tabla concentra el valor en pocas líneas. Los nodos (E01, <<e01>> COP), los gateways (E04, <<e04>> COP) y los monitores de referencia (E03, <<e03>> COP) suman <<top3_cop>> COP. Equivalen a <<top3_pct>> % del rubro. Los nodos y los gateways se compran por tramo y se importan en tres lotes (línea S11). Los monitores de referencia se compran una sola vez, entre los meses 4 y 6. Por eso la vigencia y la moneda de cada cotización deben constar. El riesgo R-FIN-01 se activa cuando la tasa de cambio supera en 10 % la de la cotización. Una cotización sin fecha impide medir ese disparador. Cada cotización debe indicar además el plazo de entrega, porque la actividad A1.2 de adquisición del lote 1 dura 10 semanas.

## Anexo D. Certificados de grupos de investigación

El capítulo 17 exige cinco capacidades y no designa grupos. Cada capacidad necesita un certificado de existencia y de categoría vigente del grupo que la aporta, junto con una carta de vinculación al proyecto. La {T:t04} lista los certificados por capacidad y añade la constancia del requisito de categoría mínima de los TdR.

@@TABLA t04@@

Sin certificado vigente, el grupo no figura como vinculado. Si un grupo no certifica su participación, el capítulo 17 exige reemplazarlo por otro con la misma capacidad. La categoría de un grupo informa su trayectoria ante el sistema nacional de ciencia, tecnología e innovación. No sustituye la evidencia de resultados en medición de material particulado, que es VACIO para este proyecto. La admisibilidad de la propuesta puede depender de una categoría mínima [DATO_USUARIO: requisito de categoría de los términos de referencia]. Mientras ese requisito no se conozca, la admisibilidad queda sin verificar.

## Anexo E. Instrumentos de recolección

Este anexo reúne los dos instrumentos que el capítulo 6 deja como productos del proyecto. El primero es la lista de cotejo de instalación y mantenimiento. El segundo es la encuesta de uso institucional del tablero. Cada uno contiene <<n_cotejo>> ítems. La lista responde a los indicadores PERS-R01 y PERS-P01, que miden el despliegue y la red operativa. La encuesta responde a los indicadores PERS-E01 y PERS-S02, que miden el uso institucional y la continuidad.

### E.1 Lista de cotejo de instalación y mantenimiento de nodos y gateways

La lista de cotejo registra si una condición se cumple, con las opciones sí, no y no aplica. El personal técnico la aplica en la instalación de cada nodo y en cada visita mensual. Cada ítem exige una evidencia verificable. La concordancia entre observadores se calcula con el coeficiente kappa de Cohen sobre 20 % de las inspecciones (PROPUESTO). La {T:t05} presenta los 10 ítems con su evidencia y el indicador o riesgo que cada uno vigila.

@@TABLA t05@@

Los ítems cubren cinco dimensiones. El ítem 1 verifica la identidad del equipo. Los ítems 2, 3 y 7 verifican la integridad física y la medición. Los ítems 4 y 5 verifican la energía. Los ítems 6, 8 y 9 verifican la comunicación y los datos. El ítem 10 verifica la custodia local. Una respuesta negativa abre una acción correctiva que se registra en la bitácora del proyecto. Los ítems 2 y 3 vigilan el riesgo R-TEC-01, de mayor nivel del registro, porque la humedad y el polvo sesgan los cabezales ópticos. El ítem 5 vigila la autonomía de 14 días, que sostiene el segundo objetivo específico.

### E.2 Encuesta de uso institucional del tablero y del protocolo de alerta

La encuesta mide seis constructos con 10 ítems. La utilidad percibida y la facilidad de uso proceden de Davis (1989). La influencia social y las condiciones facilitadoras proceden de Venkatesh et al. (2003). El uso en decisiones corresponde al indicador PERS-E01 y la continuidad bajo custodia al indicador PERS-S02. La escala va de 1, totalmente en desacuerdo, a 5, totalmente de acuerdo. La unidad de encuesta es la persona y la unidad de decisión es el comité. La población es de 150 personas en 15 comités (SUPUESTO), con una respuesta esperada de 80 %, equivalente a <<n_resp_esp>> personas.

El cuestionario pasa por cuatro controles antes de aplicarse. Un panel de cinco personas expertas valida el contenido (PROPUESTO). Una prueba cognitiva con personal de dos comités ajenos a la muestra revisa la comprensión [DATO_USUARIO: comités para la prueba piloto]. El alfa de Cronbach debe alcanzar 0,70 tras la primera aplicación (PROPUESTO). Los cambios posteriores de redacción se registran y no alteran la comparabilidad de la línea base. La {T:t06} presenta los 10 ítems. La encuesta se aplica en la línea base, en la compuerta C1, en la compuerta C2 y en el mes 24.

@@TABLA t06@@

Los ítems 1 a 8 aplican los constructos teóricos de aceptación de tecnología. Esos modelos se desarrollaron para personas usuarias individuales, mientras que el tablero se usa en comités que deciden en grupo. Por eso los ítems 9 y 10 se contrastan con fuentes distintas de la declaración personal. El ítem 9 se contrasta con la lista de decisiones documentadas. El ítem 10 se contrasta con los convenios de custodia. Una diferencia sistemática entre lo declarado y lo documentado se reporta como limitación. Los resultados se reportan por comité, porque los 150 cuestionarios se agrupan en 15 comités.

## Anexo F. Consentimientos informados

Este anexo entrega el modelo de consentimiento informado. Lo firman las personas que responden la encuesta, participan en entrevistas, asisten a talleres o autorizan el registro de audio y de fotografía. El modelo sigue la Ley 1581 de 2012, que exige autorización previa e informada del titular y le reconoce derechos sobre sus datos (Congreso de la República, 2012b). Los datos del responsable del tratamiento son [DATO_USUARIO]. El texto usa la segunda persona en la información y la primera persona singular en la declaración.

### F.1 Texto del consentimiento informado

**Título del documento.** Consentimiento informado y autorización para el tratamiento de datos personales. El documento se refiere al proyecto de red IoT híbrida y gemelo digital para material particulado posterremoto.

**Identificación del responsable del tratamiento.** El responsable del tratamiento es [DATO_USUARIO: razón social de la entidad responsable], con número de identificación tributaria (NIT) [DATO_USUARIO: NIT] y domicilio en [DATO_USUARIO: dirección]. Su correo para consultas y reclamos es [DATO_USUARIO: correo electrónico] y su teléfono es [DATO_USUARIO: teléfono]. La entidad ejecuta el proyecto formulado para la Convocatoria de Emergencia, Decreto 1414 de 2026, del Sistema General de Regalías.

**Propósito de la participación.** El proyecto instala una red de nodos de bajo costo. La red mide PM2,5 y PM10 en sitios de remoción de escombros de Caldas, Cundinamarca y Valle del Cauca. Se le invita a responder una encuesta sobre el uso del tablero. Se le invita también a participar en una entrevista o a asistir a talleres de co-diseño y jornadas públicas. El proyecto no recoge muestras biológicas ni datos de salud.

**Finalidad del tratamiento.** Sus datos se usan para cuatro finalidades. La primera es evaluar el uso institucional del tablero y del protocolo de alerta. La segunda es documentar la participación en talleres y jornadas con actas y listas de asistencia. La tercera es reportar resultados agregados por comité al financiador y en publicaciones científicas. La cuarta es contactar a la persona participante para convocarla a las actividades. Ningún otro uso se realiza sin una nueva autorización.

**Datos que se recogen.** El proyecto recoge su nombre, su cargo, su comité, sus datos de contacto y sus respuestas a cuestionarios. Con su autorización expresa, recoge también grabaciones de audio de entrevistas y de sesiones, y registros fotográficos de las actividades. No recoge documentos de identidad. Ninguna pregunta del proyecto se refiere a datos sensibles.

**Carácter voluntario.** Su participación es voluntaria. Usted puede negarse a responder cualquier pregunta. Puede retirar su consentimiento en cualquier momento, sin consecuencia alguna para su cargo ni para su comité. Si lo retira, sus datos individuales salen del análisis y se eliminan, salvo los resultados agregados que ya se publicaron.

**Riesgos y beneficios.** El riesgo de participar es mínimo (PROPUESTO). Consiste en la exposición de sus opiniones sobre el funcionamiento de su comité. El proyecto reduce ese riesgo con seudónimos y con reporte agregado por comité. La participación no ofrece pago ni beneficio personal. El beneficio es colectivo: un tablero y un protocolo de alerta ajustados a las necesidades de los comités.

**Derechos del titular.** Como titular de los datos, le asisten los derechos que reconoce la Ley 1581 de 2012 (Congreso de la República, 2012b). Usted puede conocer, actualizar y rectificar sus datos. Puede solicitar prueba de esta autorización y recibir información sobre el uso de sus datos. Puede acceder de forma gratuita a ellos. Puede revocar la autorización y solicitar la supresión de sus datos cuando el tratamiento no respete los principios y las garantías legales. Puede presentar quejas ante la Superintendencia de Industria y Comercio. Para ejercer estos derechos, escriba al correo del responsable indicado en este documento.

**Seguridad y destinatarios.** El responsable protege los datos con seudónimos por comité y por persona. Aplica cifrado en almacenamiento y en tránsito y control de acceso por rol. La llave de los seudónimos se guarda aparte. Solo accede a los datos el personal autorizado por escrito. El responsable puede apoyarse en encargados del tratamiento, como el proveedor de la infraestructura en la nube. Esos encargados operan bajo contrato y bajo las mismas reglas. Los datos personales no se transmiten a terceros con fines comerciales.

**Vigencia y conservación.** Esta autorización rige durante la ejecución del proyecto, de <<meses>> meses, y durante el seguimiento posproyecto de 12 meses. Al terminar ese periodo, el responsable elimina los datos personales identificables (PROPUESTO). Los datos ambientales de los nodos no son datos personales. Se abren según la cláusula de apertura del hito H8, con coordenadas al nivel del sitio y no del predio.

**Declaración y firma.** Declaro que leí este documento o que me lo leyeron en voz alta, que recibí respuesta a mis preguntas y que participo de forma voluntaria. Autorizo el tratamiento de mis datos para las finalidades descritas. Indico abajo si autorizo la grabación de audio y el registro fotográfico.

El documento termina con el bloque de firma de la {T:t07}. Cada persona participante lo diligencia en dos ejemplares, uno para ella y otro para el responsable. El proyecto asigna el seudónimo después de la firma.

@@TABLA t07@@

El bloque separa tres autorizaciones. La firma autoriza el tratamiento descrito en el texto. Las dos casillas autorizan por separado la grabación de audio y el registro fotográfico. Negar una casilla no impide participar en la encuesta, en la entrevista ni en el taller (PROPUESTO).

### F.2 Registro de datos personales tratados

El consentimiento se acompaña de un registro de datos. La {T:t08} lista cada dato que el proyecto trata con su finalidad, su medida de protección y su plazo de conservación. Las medidas siguen la sección 6.5.3 del capítulo 6: minimización, seudonimización, control de acceso por rol, cifrado y conservación limitada.

@@TABLA t08@@

La tabla permite verificar el principio de finalidad: ningún dato se recoge sin una finalidad listada. Los datos de audio y de fotografía son los de mayor riesgo. Por eso exigen autorización expresa y eliminación posterior a su uso. La apertura de datos y su protección se tensionan. La ciencia posnormal favorece una comunidad ampliada de pares que revise la evidencia (Funtowicz y Ravetz, 1993). La ley exige limitar el tratamiento a la finalidad autorizada (Congreso de la República, 2012b). El proyecto resuelve la tensión por tipo de dato. Abre los datos ambientales de los nodos y restringe los datos de las personas.

### F.3 Variantes institucional y de predios

El consentimiento institucional autoriza el uso de documentos del comité, como las actas. Lo firma la presidencia o la secretaría técnica y reproduce el texto de F.1 con tres cambios. El titular es el comité, el objeto son las actas y los registros de sesiones, y quien firma declara su competencia para autorizar. La autorización de predios usa la misma estructura para el acta de instalación. Identifica el predio y autoriza la instalación del nodo o del gateway. Autoriza también el acceso de los técnicos y fija el periodo y las condiciones de custodia local. Ambos documentos requieren firmantes que solo el usuario conoce [DATO_USUARIO: representantes que firman por cada comité y por cada predio].

## Anexo G. Presupuesto detallado (formato entidad)

El Anexo G reproduce el presupuesto en formato de entidad. Cada fila es una línea, con unidad, cantidad, costo unitario y total. La {T:t09} contiene las <<n_lineas>> líneas del valor solicitado al SGR en 12 columnas y suma <<sgr_cop>> COP. Incluye la naturaleza de cada cifra, el paquete de trabajo y los meses de ejecución, para que cada peso se pueda rastrear hasta una actividad.

@@TABLA t09@@

Cada línea resulta de multiplicar una cantidad por un costo unitario, sin redondeos previos. Las líneas DECLARADAS proceden del expediente E3 y las PROPUESTAS son decisiones de esta formulación. La reserva X01 es la suma de los valores monetarios esperados de los 12 riesgos. Su admisibilidad como rubro depende de los TdR (VACIO). La administración (O05) suma <<adm_cop>> COP, equivalentes a <<adm_pct>> % del valor solicitado. La {T:t10} cruza los rubros con los cuatro paquetes de trabajo.

@@TABLA t10@@

La distribución es desigual. El paquete WP0 reúne <<wp0>> % del valor solicitado, el WP1 reúne <<wp1>> %, el WP2 reúne <<wp2>> % y el WP3 reúne <<wp3>> %. La reserva de contingencia, la administración, las pólizas, la evaluación externa y la importación se asignan al paquete de gestión. La {T:t11} detalla la contrapartida, que el formato de entidad exige por separado del valor solicitado.

@@TABLA t11@@

La contrapartida suma <<con_cop>> COP. La especie representa <<pct_especie>> % de ese aporte, y toda la contrapartida está pendiente de certificación. Las alcaldías no declaran aporte (VACIO). El total del proyecto es de <<tot_cop>> COP. Cada certificación debe coincidir con el valor de su línea. Una diferencia obliga a ajustar el presupuesto y la contrapartida declarada.

## Anexo H. Cronograma detallado (MS Project/Excel)

El Anexo H presenta la red de <<n_act>> actividades con su duración, sus predecesoras, su inicio, su fin y su holgura. Los valores salen del método de la ruta crítica (CPM) calculado en maestro.cpm(). La {T:t12} sirve de fuente para generar el archivo de MS Project o de Excel. Cada fila es una tarea. La duración se expresa en semanas y los vínculos son de fin a inicio. La semana 0 corresponde al acta de inicio [DATO_USUARIO: fecha del acta de inicio].

@@TABLA t12@@

La ruta crítica abarca <<n_rc>> actividades y suma <<semanas>> semanas. Presentan holgura las actividades <<h2>> (2 semanas), <<h6>> (6 semanas) y <<h12>> (12 semanas). Esas holguras absorben retrasos sin mover el cierre. Cubren el diseño de sitios (A1.1), el co-diseño (A3.1), la puesta en uso del tablero (A3.2) y la formación de custodios (A3.3). No absorben retrasos del piloto, de las instalaciones ni de las verificaciones. Cualquier retraso en una actividad crítica mueve el cierre en la misma magnitud.

Las instalaciones A2.3 y A2.4 pertenecen a la ruta crítica. La mitigación del riesgo R-EXT-01, de bloqueos viales, depende entonces de las ventanas secas y de los técnicos locales. No depende de holgura en la red. Las compuertas se registran como tareas de dos semanas: C1 entre las semanas <<c1_ini>> y <<c1_fin>>, y C2 entre las semanas <<c2_ini>> y <<c2_fin>>. Si una compuerta decide ajustar o detener, el archivo se recalcula con las duraciones nuevas y se emite una versión del cronograma.

## Anexo I. Estudios previos (si aplica)

El proyecto cuenta con dos clases de estudio previo. La primera es el informe de vigilancia tecnológica y bibliometría (F-INF), que analiza 42 documentos. La segunda es el conjunto de análisis causales de las secciones F4.3 a F4.5. Los documentos aportados no incluyen un estudio de factibilidad, de cobertura ni de línea base de error. Este anexo sintetiza lo que existe, con su naturaleza y su verificación, y lista lo que el proyecto produce durante la ejecución.

### I.1 Estudios que existen

La {T:t13} reúne seis estudios disponibles. Cada fila indica el alcance, el localizador en la fuente y el aporte al proyecto. Las cifras del informe se toman con su página y no se recalculan.

@@TABLA t13@@

Dos lecturas contrastan sobre el valor de un estudio previo. Una lo trata como evidencia que sustenta la decisión. La otra lo trata como hipótesis que debe contrastarse. El informe F-INF es un insumo DECLARADO y no se verificó de forma independiente. Sus cifras se citan con página y no se promueven a datos verificados. Los análisis F4.3 a F4.5 expresan hipótesis de influencia estructural. Pearl y Mackenzie (2018) separan la asociación, la intervención y el contrafactual como niveles distintos de razonamiento causal. Por eso el proyecto usa esos análisis para ordenar el diseño y no para afirmar efectos.

### I.2 Estudios que el proyecto produce

El diseño necesita seis insumos que no figuran en los documentos aportados. La {T:t14} los lista con el motivo de la ausencia, el lugar donde se producen y la decisión que alimentan.

@@TABLA t14@@

Tres de los estudios cuentan con costo propio en el presupuesto. Son el estudio de cobertura (S06, <<s06>> COP), la evaluación externa (S07, <<s07>> COP) y el ensayo con laboratorio externo (S08, <<s08>> COP). Suman <<est_cop>> COP, equivalentes a <<est_pct>> % del valor solicitado. La línea base de error alimenta la compuerta C1. Sin ella, el proyecto no puede decidir si el modelo reduce el error, pues carece de un punto de comparación propio. El estudio de cobertura alimenta la compra del tramo 1, en el mes 5.

## Anexo J. Otros documentos según convocatoria

Los TdR no se aportaron. Por eso el proyecto no conoce la lista completa de documentos que la convocatoria exige. El Anexo J deja abierta esa lista y registra los documentos que el propio proyecto necesita. La {T:t15} los ordena con quién los emite, su contenido mínimo y la línea del proyecto que los exige.

@@TABLA t15@@

La lista contiene ocho documentos, y todos son datos que solo el usuario posee. Algunos presentan un momento límite en el cronograma. El aval ético debe existir antes de la semana 12, cuando comienza la actividad A3.1. El acta de constitución firmada autoriza la ejecución. Las pólizas respaldan las líneas O04 y S04. Las cotizaciones de laboratorio respaldan las líneas S01 y S08. Antes de radicar, el equipo formulador cruza esta lista con los TdR y reclasifica cada fila. Lo que los TdR exijan y no figure aquí se agrega. Lo que figure y los TdR no exijan queda como soporte interno.
