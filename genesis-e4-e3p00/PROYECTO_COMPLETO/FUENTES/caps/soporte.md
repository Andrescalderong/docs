%% PREFIJO: S

## S.2 Qué pide el mensaje y dónde se responde

El mensaje de la sección S.1 contiene nueve solicitudes. Cada una tiene una respuesta en esta parte inicial. La {T:t01} las relaciona con la sección que las contesta. El equipo remitente no podrá participar en la formulación porque atiende otro proyecto. Por esa razón, el calendario de la sección S.9 asigna a la Universidad la entrega de datos y la validación. La redacción queda en este documento.

:::TABLA t01 | Solicitudes del mensaje y sección que las responde
| N.º | Solicitud del mensaje | Respuesta | Sección |
| --- | --- | --- | --- |
| 1 | Presentación clara de qué es el proyecto | Ficha de una página y justificación de la opción única | S.3 |
| 2 | Objetivo al que aporta cada aliado | Objetivo específico, producto e indicador por actor | S.5 |
| 3 | Actividades que ejecuta cada actor | Matriz de responsabilidades de las 17 actividades y lista por actor | S.6 |
| 4 | Presupuesto asociado a esas actividades y organizaciones | Presupuesto SGR y contrapartida por actor y por rubro | S.7 |
| 5 | Opción más alineada al departamento y al terremoto | Alternativa única recomendada y criterios de selección del departamento | S.3 y S.4 |
| 6 | Reunión con la Universidad | Agenda con decisiones y datos que se necesitan | S.10 |
| 7 | Fechas claras del documento técnico completo | Calendario del 16 de octubre al 11 de noviembre de 2026 | S.9 |
| 8 | Beneficio que recibe cada actor | Beneficios y obligaciones por actor | S.8 |
| 9 | Correo con la presentación | Borrador listo para enviar | S.11 |
:::NOTA *Nota.* Elaboración propia a partir del mensaje de la sección S.1. Los números de sección remiten a esta parte inicial.


## S.3 El proyecto en una página

El proyecto instala una red de 100 nodos de bajo costo y 10 gateways. La red mide material particulado (PM2,5 y PM10) en sitios de remoción de escombros posterremoto. Tres monitores gravimétricos de referencia, uno por departamento, permiten comparar cada nodo con una medición de referencia. El gateway corrige la lectura por humedad y por fracción gruesa. Un tablero y un protocolo de alerta ponen esa medición, con su error conocido, a disposición de los comités de gestión del riesgo. La {T:t02} resume los datos que cualquier aliado necesita para entender el proyecto.

:::TABLA t02 | Ficha del proyecto para los aliados
| Elemento | Valor | Naturaleza |
| --- | --- | --- |
| Título | Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto | DECLARADO |
| Convocatoria | Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56) | DECLARADO |
| Duración | 24 meses (104 semanas), con tres tramos y compuertas en los meses 12, 17 y 24 | PROPUESTO |
| Territorio | Caldas, Cundinamarca y Valle del Cauca; 12 municipios focalizados [DATO_USUARIO: lista] | SUPUESTO |
| Red | 100 nodos, 10 gateways y 3 monitores de referencia; se compran 120 nodos y 11 gateways | PROPUESTO |
| Resultado principal | Al menos 75 % de 15 comités de gestión del riesgo usan el tablero en decisiones documentadas al mes 24 (PERS-E01) | PROPUESTO |
| Madurez tecnológica | TRL 4 a TRL 7; el Anexo 2 prioriza TRL 9 y la decisión está pendiente | PROPUESTO |
| Valor solicitado al SGR | $ 9.267.260.000 | CALCULADO |
| Contrapartida | $ 2.110.000.000 (Universidad 1.100 M; empresa 1.010 M) | DECLARADO |
| Total del proyecto | $ 11.377.260.000 | CALCULADO |
| Estado | Borrador con vacíos; no es un paquete de radicación | — |
:::NOTA *Nota.* Elaboración propia con la ficha maestra del proyecto. La contrapartida de la Universidad es una reconstrucción PROPUESTA y la de la empresa es DECLARADA en el expediente E3. Certificaciones pendientes.

El mensaje pide una sola opción y no tres. El documento recomienda la alternativa ALT-03, una red híbrida con corrección en el gateway, despliegue por tramos y custodia distribuida. Obtuvo 5,805 puntos en la escala de 1 a 9. La calibración centralizada obtuvo 5,150, el statu quo 4,475 y las estaciones fijas 4,335. El puntaje no equivale a una probabilidad de éxito. La alternativa responde a la emergencia por una razón física. El terremoto interrumpe la red eléctrica y la celular, y por eso el gateway almacena siete días de datos y conserva un enlace satelital alterno.


## S.4 Conformación de la alianza

La alianza propuesta tiene cuatro actores. El proponente es una universidad con un grupo de investigación reconocido por MinCiencias. Lo acompañan un municipio de Cundinamarca, Risaralda, Caldas o Valle del Cauca, un actor reconocido por MinCiencias y una empresa aliada. Los nombres quedan por definir [DATO_USUARIO: nombres de los cuatro actores]. La {T:t03} fija el perfil de cada actor y su posición en el análisis de participantes del Anexo 2.

:::TABLA t03 | Actores de la alianza, perfil exigido y posición en el Anexo 2
| Actor | Identidad | Perfil exigido | Posición en el Anexo 2 | Estado |
| --- | --- | --- | --- | --- |
| Proponente | [DATO_USUARIO: universidad] | Institución de educación superior con grupo de investigación reconocido por MinCiencias en calidad del aire, instrumentación o ciencia de datos | Cooperante: formula y ejecuta | VACIO |
| Municipio acompañante | [DATO_USUARIO: municipio y departamento] | Municipio afectado por la emergencia, con comité de gestión del riesgo activo | Beneficiario | VACIO |
| Actor reconocido por MinCiencias | [DATO_USUARIO: centro, instituto o grupo] | Centro o instituto de CTeI, o grupo reconocido, con laboratorio o experiencia en metrología de partículas | Cooperante | VACIO |
| Empresa aliada | [DATO_USUARIO: empresa] | Empresa con capacidad en hardware IoT, plataforma en la nube e instalación en campo | Cooperante | VACIO |
:::NOTA *Nota.* Elaboración propia con el Anexo 2 de la convocatoria (secciones de entidades aliadas y de análisis de participantes). Los perfiles son PROPUESTOS. Las cinco categorías de puntuación del Anexo 2 son IES, centro o instituto de CTeI, instituto del SINA, corporación autónoma regional y sociedad civil organizada.

El Anexo 2 impone una regla que condiciona al municipio. Una misma entidad no puede ser a la vez proponente o aliada (cooperante) y beneficiaria. Por tanto, el municipio acompañante figura como beneficiario y no recibe recursos del SGR. Si aportara recursos, pasaría a cooperante y perdería su posición de beneficiario. La ficha maestra ya registra que las alcaldías no aportan contrapartida, y este documento mantiene esa decisión (DEC-F19).

La empresa plantea una segunda verificación. Las cinco categorías de puntuación del Anexo 2 no incluyen a las empresas. Los términos de referencia deben confirmar si una empresa puede ser aliada, si puntúa y si puede ejecutar líneas del presupuesto SGR. Si no pudiera, la empresa pasaría a proveedora por contratación, y su contrapartida de 1.010 millones de COP requeriría otro vehículo.

La selección del departamento sigue cinco criterios, que la {T:t04} aplica a los cuatro departamentos mencionados. El primero es obligatorio: el municipio debe figurar entre los afectados por la emergencia. Los otros cuatro desempatan. Son la sede de la Universidad, la presencia del actor y de la empresa, la capacidad del comité y el acceso logístico.

:::TABLA t04 | Departamentos candidatos para el municipio acompañante
| Departamento | Estado en la ficha maestra | Criterio 1: afectación declarada | Criterios 2 a 5 |
| --- | --- | --- | --- |
| Caldas | Incluido: 33 nodos y 4 municipios (PROPUESTO) | VACIO: confirmar municipios en el listado de la convocatoria | VACIO: sede, actores, comité y acceso |
| Cundinamarca | Incluido: 34 nodos y 4 municipios (PROPUESTO) | VACIO: confirmar municipios en el listado de la convocatoria | VACIO: sede, actores, comité y acceso |
| Valle del Cauca | Incluido: 33 nodos y 4 municipios (PROPUESTO) | VACIO: confirmar municipios en el listado de la convocatoria | VACIO: sede, actores, comité y acceso |
| Risaralda | No incluido; lo propone el mensaje | VACIO: confirmar que figura en el ámbito territorial de la emergencia | VACIO: sede, actores, comité y acceso |
:::NOTA *Nota.* Elaboración propia con la ficha maestra y el Anexo 2. El listado de municipios afectados no se aportó, por lo que ningún departamento puede puntuarse todavía.

La recomendación es conservar el diseño de tres departamentos como base del documento. El presupuesto, las metas y las compuertas se calcularon para ese alcance. Reducirlo a un departamento obliga a recalcular nodos, comités y compuertas. El municipio acompañante se ubica en el departamento sede de la Universidad. Si la sede está en Risaralda, se verifica la declaratoria. Después se sustituye uno de los tres departamentos o se agrega Risaralda como cuarto, con el ajuste presupuestal correspondiente.


## S.5 Objetivo, producto e indicador por actor

Cada actor responde por un objetivo específico y por productos verificables. La Universidad responde ante el SGR por el objetivo general. La {T:t05} asigna a cada actor su objetivo principal, su aporte y los indicadores del marco PERS que lo miden.

:::TABLA t05 | Objetivo específico, aporte e indicadores por actor
| Actor | Objetivo principal | Aporte al objetivo | Indicadores PERS |
| --- | --- | --- | --- |
| Universidad | OE1 y objetivo general | Dirige el proyecto, calibra con el banco de laboratorio, entrena y valida el modelo de corrección, publica y forma jóvenes investigadores | PERS-R02, PERS-R04, PERS-R06, PERS-P02, PERS-P03, PERS-P04 |
| Actor reconocido por MinCiencias | OE1 (verificación independiente) y OE3 (formación) | Aporta referencias gravimétricas, análisis de laboratorio, ensayo de desempeño y formación de custodios | PERS-R05, PERS-E03 |
| Empresa aliada | OE2 | Fabrica y compra los nodos y gateways, desarrolla el firmware y la plataforma, instala la red y opera la nube | PERS-R01, PERS-R03, PERS-P01 |
| Municipio acompañante | OE3 | Propone sitios, gestiona permisos y acceso, co-diseña los umbrales, usa el tablero y recibe la custodia | PERS-E01, PERS-E02, PERS-S01, PERS-S02 |
:::NOTA *Nota.* Elaboración propia con los objetivos específicos de la ficha maestra y los 15 indicadores PERS. La asignación de indicadores a actores es PROPUESTA.


## S.6 Actividades por actor

La {T:t06} asigna a cada actor un nivel de responsabilidad en las 17 actividades del cronograma. La letra A designa al actor que responde por el resultado, y la Universidad la lleva en todas las actividades por ser proponente. La letra R designa a quien ejecuta. La letra C designa a quien aporta antes de decidir, y la letra I designa a quien recibe el resultado. En las compuertas C1 y C2 decide el comité directivo y la Universidad convoca.

:::TABLA t06 | Responsabilidad de cada actor en las 17 actividades
| Actividad | Sem. | Univ. | Actor MinC. | Empresa | Municipio |
| --- | --- | --- | --- | --- | --- |
| A0.1 Contratar equipo y firmar convenios de ejecución | 8 | A/R | C | R | C |
| A1.1 Seleccionar sitios y diseñar la colocalización | 4 | A | R | C | R |
| A2.1 Diseñar arquitectura de enlace y energía | 6 | A | I | R | C |
| A1.2 Adquirir y caracterizar lote 1 de nodos y referencias | 10 | A | R | R | I |
| A2.2 Desarrollar firmware y plataforma base | 10 | A | I | R | I |
| A1.3 Colocalizar y calibrar en el piloto (tramo 1) | 16 | A/R | R | R | C |
| A3.1 Co-diseñar umbrales y protocolo de alerta con comités | 24 | A/R | C | C | R |
| A1.4 Entrenar y validar el modelo de corrección | 8 | A/R | R | C | I |
| C1 Compuerta C1: decisión de ampliación al tramo 2 | 2 | R | C | C | C |
| A2.3 Instalar tramo 2 (40 nodos, 4 gateways) | 12 | A | I | R | R |
| A1.5 Reentrenar y verificar por departamento (tramo 2) | 6 | A/R | R | C | I |
| A3.2 Poner en uso el tablero con los comités | 12 | A | C | C | R |
| C2 Compuerta C2: decisión de consolidación al tramo 3 | 2 | R | C | C | C |
| A2.4 Instalar tramo 3 (30 nodos, 3 gateways) | 12 | A | I | R | R |
| A3.3 Formar custodios y firmar convenios por tramo | 16 | A | R | C | R |
| A1.6 Verificar desempeño final y ensayo independiente | 16 | A | R | C | I |
| A3.4 Transferir, cerrar y evaluar | 6 | A/R | R | R | R |
:::NOTA *Nota.* Elaboración propia con el cronograma de la ficha maestra (duración en semanas). A: aprueba y responde; R: ejecuta; C: consultado; I: informado. La asignación es PROPUESTA y se ratifica en la reunión con la Universidad. Univ.: Universidad. Actor MinC.: actor reconocido por MinCiencias.

La {T:t07} traduce la matriz en lo que hace cada actor y en lo que entrega. Esa descripción es la que MinCiencias evaluará con mayor detalle, según el mensaje. Cada entregable tiene un hito de verificación en el cronograma del proyecto.

:::TABLA t07 | Qué ejecuta y qué entrega cada actor
| Actor | Actividades que ejecuta | Entregables verificables |
| --- | --- | --- |
| Universidad | Gerencia y convenios (A0.1); colocalización y calibración en el piloto (A1.3); entrenamiento y validación del modelo (A1.4 y A1.5); co-diseño de umbrales con los comités (A3.1); convocatoria de compuertas; cierre y evaluación (A3.4) | Convenios firmados; línea base de error medida; modelo validado con R² ≥ 0,70 y NRMSE ≤ 30 %; actas de compuerta; 2 artículos Q1 o Q2; informe de cierre |
| Actor reconocido por MinCiencias | Diseño de la colocalización con referencias gravimétricas (A1.1); caracterización de referencias (A1.2); verificación en cada departamento (A1.3 y A1.5); ensayo independiente de desempeño (A1.6); formación de custodios (A3.3) | Base de datos de colocalización; informe de laboratorio; informe del ensayo de desempeño; 60 personas certificadas |
| Empresa aliada | Arquitectura de enlace y energía (A2.1); firmware y plataforma (A2.2); adquisición de nodos (A1.2); instalación de los tramos 2 y 3 (A2.3 y A2.4); operación de la nube y del gemelo digital | Diseño de enlace y energía; plataforma operativa; 100 nodos y 10 gateways instalados; disponibilidad de nodos ≥ 90 %; software registrado |
| Municipio acompañante | Propuesta de sitios y permisos (A1.1); acceso y seguridad de los sitios (A2.3 y A2.4); co-diseño de umbrales (A3.1); uso del tablero (A3.2); convenio de custodia (A3.3 y A3.4) | Listado de sitios autorizados; actas de uso del tablero en decisiones; convenio de custodia firmado |
:::NOTA *Nota.* Elaboración propia con la matriz de la {T:t06} y los indicadores PERS de la ficha maestra. La operación de la nube y del gemelo digital se ejecuta durante los 24 meses en las líneas del presupuesto de la empresa.


## S.7 Presupuesto por actor

El mensaje pide verificar el presupuesto sobre las actividades de cada organización. Para ello, cada una de las 56 líneas del presupuesto SGR se asignó al actor que la ejecuta técnicamente. La {T:t08} muestra el resultado por rubro y la {T:t09} resume el total y la contrapartida. La asignación por línea se encuentra en la {T:t10}.

:::TABLA t08 | Presupuesto SGR por actor y por rubro (millones de COP)
| Actor | Personal | Equipos y software | Materiales | Servicios técnicos | Viajes | Otros | Reserva | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Universidad | 1.816,8 | 455,0 | 140,9 | 215,0 | 54,0 | 592,0 | 636,0 | 3.909,7 |
| Actor reconocido | 528,0 | 0,0 | 0,0 | 324,0 | 0,0 | 0,0 | 0,0 | 852,0 |
| Empresa aliada | 2.208,0 | 1.430,6 | 102,0 | 357,0 | 408,0 | 0,0 | 0,0 | 4.505,6 |
| Municipio | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 | 0,0 |
| Total SGR | 4.552,8 | 1.885,6 | 242,9 | 896,0 | 462,0 | 592,0 | 636,0 | 9.267,3 |
:::NOTA *Nota.* Elaboración propia con las 56 líneas del presupuesto SGR de la ficha maestra (CALCULADO). La asignación de cada línea a un actor es PROPUESTA. El municipio no recibe recursos SGR por su posición de beneficiario.

:::TABLA t09 | Total por actor: recursos SGR y contrapartida
| Actor | SGR (M COP) | % del SGR | Contrapartida (M COP) | Naturaleza de la contrapartida |
| --- | --- | --- | --- | --- |
| Universidad | 3.909,7 | 42,2 | 1.100,0 | En especie, 1.100 M (reconstruida) |
| Actor reconocido | 852,0 | 9,2 | 0,0 | VACIO: no declarada |
| Empresa aliada | 4.505,6 | 48,6 | 1.010,0 | 210 M en efectivo y 800 M en especie (DECLARADO) |
| Municipio | 0,0 | 0,0 | 0,0 | VACIO: sin aporte por regla del Anexo 2 |
| Total | 9.267,3 | 100,0 | 2.110,0 | Certificaciones pendientes |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (CALCULADO). La reserva de contingencia de 636 M se asigna a la Universidad como proponente y se libera por decisión del comité directivo.

:::TABLA t10 | Asignación de las 56 líneas del presupuesto SGR a cada actor
| Id | Concepto | Rubro | Actor | Valor (M COP) |
| --- | --- | --- | --- | --- |
| P01 | Jóvenes investigadores (6) | Personal | Universidad | 144,0 |
| P02 | Estudiantes de maestría (2) | Personal | Universidad | 304,8 |
| P03 | Científico de datos senior (1) | Personal | Universidad | 480,0 |
| P04 | Ingenieros IoT y de campo (3) | Personal | Empresa aliada | 648,0 |
| P05 | Coordinación de apropiación social (1) | Personal | Universidad | 192,0 |
| P06 | Gerencia de proyecto (1) | Personal | Universidad | 240,0 |
| P07 | Especialista en metrología y calibración (1) | Personal | Actor reconocido | 288,0 |
| P08 | Ingenieros de software y nube (2) | Personal | Empresa aliada | 456,0 |
| P09 | Ingeniero de firmware y energía (1) | Personal | Empresa aliada | 216,0 |
| P10 | Técnicos de campo departamentales (6) | Personal | Empresa aliada | 648,0 |
| P11 | Profesionales de apropiación social (2) | Personal | Universidad | 288,0 |
| P12 | Analista de datos espaciales y gemelo digital (1) | Personal | Empresa aliada | 240,0 |
| P13 | Profesional en calidad del aire y salud ambiental (1) | Personal | Actor reconocido | 240,0 |
| P14 | Profesional de convenios y custodia (1) | Personal | Universidad | 168,0 |
| E01 | Nodos IoT de medición (100 + 20 de reserva) | Equipos y software | Empresa aliada | 540,0 |
| E02 | Cabezales ópticos de partículas | Equipos y software | Empresa aliada | 180,0 |
| E03 | Monitores gravimétricos de referencia | Equipos y software | Universidad | 255,0 |
| E04 | Gateways con energía solar y respaldo (10 + 1 de reserva) | Equipos y software | Empresa aliada | 308,0 |
| E05 | Kits de energía solar y batería para nodos | Equipos y software | Empresa aliada | 78,0 |
| E06 | Módulos de enlace satelital de respaldo | Equipos y software | Empresa aliada | 35,0 |
| E07 | Banco de calibración de laboratorio (cámara de humedad y generador de aerosol) | Equipos y software | Universidad | 150,0 |
| E08 | Estaciones de trabajo para entrenamiento de modelos | Equipos y software | Universidad | 50,0 |
| E09 | Equipos de campo e instrumentación (lote) | Equipos y software | Empresa aliada | 30,0 |
| E10 | Instancias en la nube reservadas (24 meses) | Equipos y software | Empresa aliada | 180,0 |
| E11 | Software de analítica y repositorios | Equipos y software | Empresa aliada | 45,0 |
| E12 | Planes de datos celulares M2M para gateways (12 SIM, 24 meses) | Equipos y software | Empresa aliada | 34,6 |
| M01 | Filtros de membrana PTFE para gravimetría | Materiales e insumos | Universidad | 14,4 |
| M02 | Polvo de ensayo normalizado y consumibles del banco de calibración | Materiales e insumos | Universidad | 42,0 |
| M03 | Cerramientos NEMA 4X y mástiles para nodos | Materiales e insumos | Empresa aliada | 42,0 |
| M04 | Cartillas impresas del índice y del protocolo de alerta | Materiales e insumos | Universidad | 42,5 |
| M05 | Kits de papelería para talleres de co-diseño | Materiales e insumos | Universidad | 30,0 |
| M06 | Elementos de protección personal (mascarillas N95) | Materiales e insumos | Universidad | 12,0 |
| M07 | Repuestos y consumibles de mantenimiento (baterías, cables, conectores) | Materiales e insumos | Empresa aliada | 60,0 |
| S01 | Análisis gravimétrico en laboratorio acreditado | Servicios técnicos | Actor reconocido | 84,0 |
| S02 | Consultoría jurídica en propiedad intelectual y libertad de operación | Servicios técnicos | Universidad | 45,0 |
| S03 | Auditoría externa de ciberseguridad | Servicios técnicos | Empresa aliada | 30,0 |
| S04 | Póliza todo riesgo de equipos | Servicios técnicos | Universidad | 50,0 |
| S05 | Instalación en sitio, mástiles y obra menor (100 nodos y 10 gateways) | Servicios técnicos | Empresa aliada | 132,0 |
| S06 | Estudio de cobertura y de enlace en tres departamentos | Servicios técnicos | Empresa aliada | 60,0 |
| S07 | Evaluación externa independiente (meses 12 y 24) | Servicios técnicos | Universidad | 120,0 |
| S08 | Ensayo de desempeño con laboratorio externo | Servicios técnicos | Actor reconocido | 90,0 |
| S09 | Formación y soporte a custodios por tramo | Servicios técnicos | Actor reconocido | 150,0 |
| S10 | Planes de enlace satelital de respaldo (10 módulos, 22 meses) | Servicios técnicos | Empresa aliada | 55,0 |
| S11 | Importación y nacionalización de equipos | Servicios técnicos | Empresa aliada | 80,0 |
| V01 | Tiquetes aéreos nacionales | Viajes y viáticos | Empresa aliada | 90,0 |
| V02 | Viáticos de alojamiento y manutención | Viajes y viáticos | Empresa aliada | 210,0 |
| V03 | Arrendamiento de vehículos 4x4 | Viajes y viáticos | Empresa aliada | 108,0 |
| V04 | Viaje internacional para divulgación científica | Viajes y viáticos | Universidad | 24,0 |
| V05 | Alimentación de laboratorios ciudadanos | Viajes y viáticos | Universidad | 30,0 |
| O01 | Cargos de procesamiento de artículos de acceso abierto | Otros rubros | Universidad | 25,0 |
| O02 | Logística de ferias y laboratorios de apropiación | Otros rubros | Universidad | 72,0 |
| O03 | Registro ante la DNDA y asesoría de propiedad intelectual | Otros rubros | Universidad | 15,0 |
| O04 | Pólizas y garantías del SGR | Otros rubros | Universidad | 60,0 |
| O05 | Administración (revisoría y plataforma de seguimiento) | Otros rubros | Universidad | 360,0 |
| O06 | Publicaciones de divulgación y eventos de socialización | Otros rubros | Universidad | 60,0 |
| X01 | Reserva de contingencia (suma de valores monetarios esperados) | Reserva de contingencia | Universidad | 636,0 |
:::NOTA *Nota.* Elaboración propia con las líneas del presupuesto SGR de la ficha maestra. La columna Actor es PROPUESTA: indica quién ejecuta técnicamente la línea. La contratación formal depende de las reglas del SGR y de los términos de referencia.

Tres conclusiones se desprenden de la {T:t09}. La primera: la empresa recibe 48,6 % del SGR y aporta 1.010 millones de COP. La relación entre ambas cifras debe validarse con sus costos reales [DATO_USUARIO: costos de la empresa]. La segunda: la Universidad concentra 42,2 % por la gerencia, la administración y la reserva. La tercera: el actor reconocido recibe 9,2 %, una participación que su perfil y su capacidad real pueden aumentar o reducir.


## S.8 Beneficio que recibe cada actor

Los aliados preguntan qué ganan. La {T:t11} responde con datos del proyecto y declara lo que todavía no está definido. Ningún beneficio incluye afirmaciones sobre efectos en salud, porque el proyecto produce mediciones, uso institucional y continuidad.

:::TABLA t11 | Beneficios y obligaciones por actor
| Actor | Qué recibe | Qué asume | Aún no definido |
| --- | --- | --- | --- |
| Universidad | Financiación de 24 meses de investigación aplicada por 3.910 M; 6 jóvenes investigadores y 2 maestrantes; 2 artículos Q1 o Q2; un software registrado; banco de calibración y monitores de referencia | Responde ante el SGR por el proyecto; aporta 1.100 M en especie; administra y rinde cuentas | Titularidad de la propiedad intelectual; destino de los equipos al cierre |
| Actor reconocido por MinCiencias | Financiación de 852 M por verificación y formación; coautoría de los artículos; uso del banco de datos de colocalización; reconocimiento como laboratorio de referencia | Entrega verificaciones independientes y certifica a 60 personas | Contrapartida; modalidad de contratación |
| Empresa aliada | Ejecución de 4.506 M; producto probado de TRL 4 a TRL 7 en entorno operativo; 15 comités como referencia; unidad de expansión con costo marginal de 120,08 M por gateway con 10 nodos | Aporta 210 M en efectivo y 800 M en especie; responde por la plataforma y la instalación | Titularidad de la propiedad intelectual; margen neto; condiciones de explotación posterior |
| Municipio acompañante | Red de nodos en su territorio sin costo SGR para el municipio; tablero y protocolo de alerta; formación de 10 funcionarios por comité; 5.000 cartillas y 3.000 mascarillas N95 para el proyecto | Autoriza sitios, facilita el acceso, usa el tablero y asume la custodia al cierre | Costo de sostenimiento (NO_CALCULABLE); capacidad de absorción |
:::NOTA *Nota.* Elaboración propia con la ficha maestra, la {T:t09} y la ruta de escala del capítulo 14. Las cifras monetarias son CALCULADAS y los beneficios cualitativos son PROPUESTOS. Valores en millones de COP (M).

En una frase por actor, la respuesta a la pregunta «y yo qué gano» es la siguiente. La Universidad gana capacidad de investigación, formación y publicaciones. El actor reconocido gana un papel de referencia metrológica. La empresa gana un producto validado y una cartera de comités. El municipio gana una medición con error conocido y la capacidad de usarla, a cambio de custodiar la red.


## S.9 Calendario hacia el documento técnico completo

La fecha límite de la convocatoria es el 11 de noviembre de 2026. Desde el 16 de octubre quedan 26 días calendario. El calendario de la {T:t12} fija fechas de entrega para que el documento técnico completo exista seis días hábiles antes del cierre. El 2 de noviembre es probablemente festivo por el traslado de Todos los Santos. El calendario oficial debe confirmarlo [DATO_USUARIO: hora de cierre en la plataforma].

:::TABLA t12 | Calendario propuesto del 16 de octubre al 11 de noviembre de 2026
| Fecha | Hito | Responsable | Entregable |
| --- | --- | --- | --- |
| Vie 16 oct | Envío del correo con la presentación y este borrador | Persona usuaria | Correo y documento |
| Mar 20 oct | Reunión con la Universidad | Persona usuaria y Universidad | Decisiones D1 a D8 de la sección S.10 |
| Jue 22 oct | Datos de la Universidad | Universidad | Nombre, grupos, investigadores, certificación de contrapartida |
| Lun 26 oct | Confirmación de municipio, actor reconocido y empresa | Universidad | Cartas de intención en borrador; lista de municipios |
| Mié 28 oct | Congelamiento de datos de entrada | Universidad y empresa | Cotizaciones y presupuesto verificado |
| Vie 30 oct | Documento técnico completo v1.0 | Persona usuaria | Documento sin datos pendientes y con verificadores ejecutados |
| Mar 3 y mié 4 nov | Revisión cruzada por los cuatro actores | Los cuatro actores | Comentarios consolidados |
| Jue 5 nov | Documento técnico v1.1 aprobado | Universidad | Versión final y carga de prueba en la plataforma |
| Vie 6 nov | Cartas y certificaciones firmadas | Los cuatro actores | Cartas de compromiso y certificación de contrapartida |
| Lun 9 nov | Verificación final de requisitos | Persona usuaria | Lista de chequeo sin alertas activas |
| Mar 10 nov | Margen de seguridad | Universidad | Radicación anticipada sin cambios de contenido |
| Mié 11 nov | Fecha límite de la convocatoria | Universidad | Proyecto radicado |
:::NOTA *Nota.* Elaboración propia. Las fechas son PROPUESTAS y los días de la semana se verificaron con el calendario de 2026. La fecha límite es DECLARADA por el usuario. El festivo del 2 de noviembre queda NO_VERIFICADO.

La regla de control es sencilla. Ningún dato que llegue después del 28 de octubre cambia la estructura del documento. Los datos tardíos se incorporan como anexos o como notas de corrección. Esa regla evita que la formulación se concentre en los últimos días.


## S.10 Agenda de la reunión con la Universidad

La reunión del 20 de octubre busca ocho decisiones. La {T:t13} las enumera con el motivo por el cual cada una condiciona el documento. La reunión dura 90 minutos y termina con un acta que asigna responsable y fecha a cada dato pendiente.

:::TABLA t13 | Decisiones y datos que se requieren de la Universidad
| N.º | Decisión o dato | Por qué condiciona el documento |
| --- | --- | --- |
| D1 | Nombre de la universidad, grupo(s) de investigación y categoría vigente en MinCiencias | El proponente debe contar con un grupo de investigación, según los términos de referencia |
| D2 | Departamento sede y municipio acompañante | Fija el territorio, los sitios y el comité beneficiario |
| D3 | Actor reconocido por MinCiencias y su papel | Define el verificador independiente y la línea de formación |
| D4 | Empresa aliada, contrapartida y forma de contratación | Determina si la empresa puede ejecutar líneas del SGR |
| D5 | Certificación de la contrapartida de 1.100 millones de COP | El expediente no la soporta y el riesgo R-FIN-02 la menciona |
| D6 | Titularidad de la propiedad intelectual y destino de los equipos | Condiciona el beneficio de cada actor y la cláusula de apertura |
| D7 | Nivel de madurez tecnológica objetivo: TRL 7 o TRL 9 | El Anexo 2 prioriza TRL 9 y el proyecto compromete TRL 7 |
| D8 | Términos de referencia y anexos de la convocatoria | Sin ellos, la estructura y el puntaje siguen siendo supuestos |
:::NOTA *Nota.* Elaboración propia. Los términos de referencia, el Plan de Desarrollo y los anexos de la convocatoria no se aportaron al proyecto (NO_VERIFICADO).


## S.11 Borrador del correo

El texto siguiente responde a la solicitud de la sección S.1. Puede enviarse sin cambios una vez se completen los nombres entre corchetes.

**Asunto:** Proyecto SGR_CONV56_AIRE: qué es, qué hace cada aliado, presupuesto y calendario.

Hola [DATO_USUARIO: nombre del destinatario],

Gracias por tu mensaje. Aquí está la presentación que pediste, con una sola opción: la más alineada con la emergencia del terremoto.

**1. Qué es el proyecto.** Una red de 100 nodos de bajo costo y 10 gateways mide PM2,5 y PM10 en sitios de remoción de escombros. Corrige el error de cada medición. Entrega un tablero y un protocolo de alerta a 15 comités de gestión del riesgo. Dura 24 meses. Solicita 9.267.260.000 COP al SGR y suma 2.110.000.000 COP de contrapartida.

**2. Alianza propuesta.** La Universidad, con su grupo de investigación reconocido por MinCiencias, es la proponente. La acompañan un municipio beneficiario, un actor reconocido por MinCiencias y una empresa aliada.

**3. Objetivo de cada aliado.** La Universidad responde por la calibración y la validación del modelo. El actor reconocido verifica de forma independiente y forma a los custodios. La empresa instala y opera la red y la plataforma. El municipio usa el tablero y recibe la custodia.

**4. Actividades y presupuesto.** El documento adjunto asigna a cada actor las 17 actividades y las 56 líneas del presupuesto (secciones S.6 y S.7).

**5. Beneficio de cada actor.** Está en la sección S.8, con lo que cada uno recibe y lo que asume.

**6. Fechas.** El documento técnico completo estará listo el 30 de octubre. Los cuatro actores lo revisan el 3 y el 4 de noviembre. La radicación se prevé el 10 de noviembre, un día antes del cierre.

**7. Lo que necesitamos.** Una reunión con la Universidad el 20 de octubre y los datos de la sección S.10 antes del 22 de octubre.

Quedo atento.

[DATO_USUARIO: firma]


## S.12 ¿Qué se me escapa?

Cinco vacíos pueden afectar la propuesta. La {T:t14} los relaciona con su riesgo y con una ruta de solución. El riesgo mayor es de calendario. Si la Universidad entrega los datos después del 28 de octubre, el documento llegaría al cierre sin certificaciones ni cartas.

:::TABLA t14 | Vacíos de la alianza, riesgo y ruta de solución
| Vacío | Riesgo si no se resuelve | Ruta de solución |
| --- | --- | --- |
| Términos de referencia no aportados | La estructura, los topes y el puntaje siguen siendo supuestos | Solicitar los términos y el listado de municipios en la reunión del 20 de octubre |
| La empresa no figura entre las categorías de puntuación | La empresa podría no ser aliada ni ejecutar líneas del SGR | Confirmar con los términos; si no procede, contratarla como proveedora |
| El municipio como beneficiario no puede aportar recursos | Un aporte municipal lo convierte en cooperante | Mantener cartas de apoyo sin aporte económico |
| Risaralda no está en la ficha maestra | El territorio podría quedar fuera del ámbito de la emergencia | Verificar la declaratoria antes de definir la sede |
| El actor reconocido sin contrapartida ni papel pactado | La verificación independiente quedaría sin responsable | Acordar el papel y su valor en la reunión con la Universidad |
:::NOTA *Nota.* Elaboración propia con el Anexo 2, la ficha maestra y los registros DEC-F del proyecto.

El premortem identifica una causa probable de fracaso: la Universidad no puede certificar la contrapartida o el grupo no tiene categoría vigente. La contingencia es preparar desde ya una segunda universidad candidata y reservar el 30 de octubre como fecha límite para decidir el cambio.

El valor estratégico de esta parte es doble. Responde las nueve solicitudes del mensaje en un solo lugar y convierte los roles de los actores en tablas verificables. Con ello reduce el riesgo de que MinCiencias detecte ambigüedad en las funciones y el presupuesto de cada organización.

La decisión DEC-F19 registra tres hechos. La alianza propuesta tiene cuatro actores. El municipio es beneficiario sin aporte. El presupuesto se asigna por actor de forma PROPUESTA. Esa decisión queda sujeta a la ratificación de la Universidad.
