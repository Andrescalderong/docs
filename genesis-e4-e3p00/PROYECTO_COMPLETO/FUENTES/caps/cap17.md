%% PREFIJO: 17
# Capítulo 17. Equipo de Trabajo

Este capítulo describe el equipo que el proyecto requiere y no un equipo nominado. Las líneas de personal P01 a P14 del presupuesto fijan los roles, las dedicaciones y los meses de vinculación. Cada perfil es un perfil requerido (PROPUESTO). Cada persona queda como [DATO_USUARIO: nombre y hoja de vida]. Las cifras de personas, de persona-mes y de equivalentes de tiempo completo se calculan desde esas líneas.

## 17.1 Estructura del Equipo

### 17.1.1 Organigrama del proyecto

La estructura del equipo separa la dirección científica de la gerencia del proyecto. El Project Management Institute (PMI, 2021) trata el equipo como un dominio de desempeño que combina responsabilidades definidas y liderazgo compartido. El organigrama de la {F:f01} aplica esa lectura en tres niveles. El comité directivo decide las compuertas C1, C2 y C3. La dirección científica y la gerencia responden ante ese comité. Los paquetes de trabajo WP1, WP2 y WP3 responden ante la dirección científica y la gerencia.

:::FIGURA f01 | Organigrama del equipo del proyecto | Nota. Elaboración propia con las líneas P01 a P14 y C01 a C03 de maestro.py; script c17_figs.py, sin semilla; corte de datos 13 de octubre de 2026. ETC: equivalente de tiempo completo. Naturaleza: roles DECLARADO o PROPUESTO según la línea; comité directivo y comité asesor PROPUESTO.

Dos posiciones contrastan en el diseño de la gobernanza de un proyecto de cambio técnico. Kotter (2012) sostiene que el cambio exige una coalición directiva con poder y pericia suficientes. Argyris y Schön (1978) sostienen que el aprendizaje organizacional exige que las personas cuestionen los supuestos que orientan su acción. El proyecto aplica cada posición en un nivel distinto. El comité directivo actúa como coalición con autoridad sobre las compuertas. Los paquetes técnicos revisan sus supuestos en las retrospectivas quincenales que describe el capítulo 6.

El presupuesto financia 29 personas del Sistema General de Regalías (SGR) en 14 perfiles. Suma 624 persona-mes, equivalentes a 26,0 equivalentes de tiempo completo (ETC) promedio durante 24 meses (CALCULADO). La contrapartida de la institución de educación superior (IES) ejecutora agrega cuatro personas con dedicación parcial. Entre los meses 1 y 12 trabajan 29 personas del SGR. Desde el mes 13 trabajan 23, porque los seis jóvenes investigadores concluyen su vinculación en el mes 12.

La consecuencia metodológica es que ninguna decisión de compuerta recae en un solo cargo. El comité directivo reúne a la entidad ejecutora, a la empresa tecnológica y a los comités territoriales (PROPUESTO). Su composición formal queda como [DATO_USUARIO: composición del comité directivo según el convenio]. La salida de los jóvenes investigadores coincide con la compuerta C1. Por eso el proyecto programa la entrega de bitácoras y de código documentado antes del mes 12 (PROPUESTO). Esa entrega conserva el conocimiento del piloto para los tramos siguientes.

### 17.1.2 Roles y responsabilidades

Los roles se definen por línea presupuestal y se asignan a un paquete de trabajo. La {T:t01} resume cada rol con su responsabilidad principal, su dedicación y sus meses de vinculación. La tabla agrupa 14 líneas del SGR y tres de la IES. Las responsabilidades son una propuesta de formulación y requieren ratificación del comité directivo.

:::TABLA t01 | Matriz de roles y responsabilidades del equipo
| Línea | Rol | Personas | Paquete | Responsabilidad principal (PROPUESTO) | ETC por persona | Meses | Naturaleza |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Jóvenes investigadores | 6 | WP1 | Apoyan la colocalización, el análisis de datos y la documentación del piloto. | 1,0 | 1 a 12 | DECLARADO |
| P02 | Estudiantes de maestría | 2 | WP1 | Desarrollan tesis sobre el modelo de corrección y su validación frente a la referencia. | 1,0 | 1 a 24 | DECLARADO |
| P03 | Científico de datos senior | 1 | WP1 | Diseña, entrena y valida el modelo de corrección que se ejecuta en los gateways. | 1,0 | 1 a 24 | DECLARADO |
| P04 | Ingenieros IoT y de campo | 3 | WP2 | Instalan, configuran y operan nodos y gateways; uno de ellos coordina WP2. | 1,0 | 1 a 24 | DECLARADO |
| P05 | Coordinación de apropiación social | 1 | WP3 | Coordina la apropiación social y el co-diseño con los comités de gestión del riesgo. | 1,0 | 1 a 24 | DECLARADO |
| P06 | Gerencia de proyecto | 1 | WP0 | Gerencia el alcance, el cronograma, el presupuesto y la preparación de las compuertas. | 1,0 | 1 a 24 | DECLARADO |
| P07 | Especialista en metrología y calibración | 1 | WP1 | Responde por la trazabilidad frente a la referencia gravimétrica y firma la validación. | 1,0 | 1 a 24 | PROPUESTO |
| P08 | Ingenieros de software y nube | 2 | WP2 | Construyen la plataforma en la nube, el gemelo digital y el tablero. | 1,0 | 1 a 24 | PROPUESTO |
| P09 | Ingeniero de firmware y energía | 1 | WP2 | Diseña el firmware y la energía para 14 días de autonomía sin sol. | 1,0 | 1 a 24 | PROPUESTO |
| P10 | Técnicos de campo departamentales | 6 | WP2 | Instalan, mantienen y reponen equipos en campo; dos técnicos por departamento. | 1,0 | 1 a 24 | PROPUESTO |
| P11 | Profesionales de apropiación social | 2 | WP3 | Facilitan talleres de co-diseño y acompañan a los comités en el uso del tablero. | 1,0 | 1 a 24 | PROPUESTO |
| P12 | Analista de datos espaciales y gemelo digital | 1 | WP2 | Desarrolla la estimación espacial del gemelo digital y valida sus resultados. | 1,0 | 1 a 24 | PROPUESTO |
| P13 | Profesional en calidad del aire y salud ambiental | 1 | WP3 | Define con los comités los umbrales locales del índice y el protocolo de alerta. | 1,0 | 1 a 24 | PROPUESTO |
| P14 | Profesional de convenios y custodia | 1 | WP3 | Gestiona los convenios por tramo, la cláusula de apertura y la propiedad intelectual. | 1,0 | 1 a 24 | PROPUESTO |
| Total SGR | 14 perfiles | 29 | WP0 a WP3 | 624 persona-mes; 26,0 ETC promedio en 24 meses | — | 1 a 24 | CALCULADO |
| C01 | Investigador principal (IES) | 1 | WP0 | Dirige la ejecución científica, representa al proyecto y preside el comité técnico. | 0,5 | 1 a 24 | DECLARADO |
| C02 | Coinvestigador técnico (IES) | 1 | WP1 | Coordina WP1 y la validación de la corrección frente a la referencia. | 0,3 | 1 a 24 | DECLARADO |
| C03 | Coinvestigadores de ambiente y ciencias sociales (IES) | 2 | WP3 | Asesoran el análisis de ambiente y salud ambiental y el co-diseño con ciencias sociales. | 0,2 | 1 a 24 | PROPUESTO |
| Total IES | 3 perfiles | 4 | WP0, WP1, WP3 | 1,2 ETC en 24 meses | — | 1 a 24 | CALCULADO |
:::NOTA *Nota.* Elaboración propia con las líneas P01 a P14 del presupuesto y C01 a C03 de la contrapartida (maestro.py). ETC: equivalente de tiempo completo, calculado como persona-mes ÷ (personas × meses de vigencia). La naturaleza corresponde a la línea; las responsabilidades son PROPUESTO. Decimales con coma.

La tabla muestra que el paquete WP2 concentra 312 de los 624 persona-mes, es decir 50,0 %. El paquete WP1 suma 168 persona-mes (26,9 %), el WP3 suma 120 (19,2 %) y la gerencia del WP0 suma 24 (3,8 %). La carga de campo se distribuye con dos técnicos por departamento. Cada técnico atiende en promedio 16,7 nodos (CALCULADO). Las tres personas de apropiación social acompañan a 15 comités, a razón de cinco comités por persona (CALCULADO).

La separación entre quien construye y quien evalúa organiza los roles técnicos. Hevner et al. (2004) exigen que el artefacto se construya y se evalúe con rigor y con criterios explícitos. Ries (2011) integra la construcción y la medición en un solo ciclo de aprendizaje a cargo del mismo equipo. Las dos posiciones difieren en la independencia de quien evalúa. El proyecto combina ambas. El rol de metrología (P07) pertenece al WP1 y no al WP2, de modo que no depende de quienes construyen nodos y gateways. El ciclo de colocalización, corrección y verificación (A1.3 y A1.4) integra a los dos paquetes.

La evaluación externa (S07) y el ensayo con laboratorio externo (S08) agregan una verificación ajena al equipo ejecutor. La consecuencia es una regla de independencia. El rol P07 firma el informe de validación de cada ciclo de calibración, como exige el indicador PERS-R02. Las cargas por técnico y por profesional de apropiación social se contrastan con la carga real durante el tramo 1. Si la carga supera la prevista, el comité directivo decide una reasignación dentro del mismo rubro de personal (PROPUESTO).

### 17.1.3 Dedicación horaria

La dedicación se expresa en equivalentes de tiempo completo y no en horas semanales. El Manual de Frascati expresa el personal de investigación y desarrollo en equivalentes de tiempo completo (OCDE, 2015). Así se suman en una misma unidad las dedicaciones parciales y completas. El proyecto calcula la dedicación como persona-mes dividido entre el producto de las personas por los meses de vigencia. Las 14 líneas de personal del SGR resultan en 1,0 ETC por persona durante su vigencia (CALCULADO).

La jornada semanal que equivale a 1,0 ETC queda como [DATO_USUARIO: jornada laboral de la entidad ejecutora en horas por semana]. Las líneas de la contrapartida de la IES resultan en 0,5 ETC para el investigador principal y 0,3 ETC para el coinvestigador técnico. Cada coinvestigador de ambiente y ciencias sociales aporta 0,2 ETC. Las dos primeras dedicaciones son DECLARADO. La tercera es PROPUESTO. El total de la IES es de 1,2 ETC. Su valor es de 800 millones de pesos colombianos (COP) en especie para las líneas C01 a C03.

Dos posiciones orientan la elección entre personal dedicado y personal permanente de la institución anfitriona. La primera privilegia el personal de tiempo completo, que concentra su atención en los entregables. La segunda privilegia la vinculación del personal permanente. La integración con la organización y la presencia de un promotor del programa favorecen la continuidad (Shediac-Rizkallah y Bone, 1998). El proyecto adopta una solución mixta. El SGR financia personal dedicado, con 26,0 ETC promedio. La IES aporta personal permanente con dedicación parcial.

La consecuencia metodológica es el registro mensual de horas por rol, que alimenta el indicador PERS-R04 de desviación de la ejecución presupuestal. La certificación de las dedicaciones de la IES sigue pendiente. Se asocia al riesgo R-FIN-02, cuyo valor monetario esperado es de 20,0 millones de COP. Hasta que exista esa certificación, el aporte en especie del personal de la IES no se considera verificado.

## 17.2 Perfiles del Equipo

La {T:t02} reúne los perfiles requeridos por cada rol. La hoja de vida de cada persona queda como dato del usuario. El área de formación y la competencia verificable son una propuesta de formulación. Los niveles de formación y los años de experiencia mínimos dependen de los términos de referencia (TdR), que no se aportaron. Por esa razón la tabla no afirma títulos, años de experiencia ni nombres.

:::TABLA t02 | Perfiles requeridos y hojas de vida resumidas por aportar
| Rol | Área de formación requerida (PROPUESTO) | Competencia verificable (PROPUESTO) | Persona y hoja de vida |
| --- | --- | --- | --- |
| C01 Investigador principal (IES) | Ingeniería electrónica, ambiental o afín | Dirección de proyectos que llevaron un desarrollo de laboratorio a entorno operativo | [DATO_USUARIO: nombre y hoja de vida] |
| C02 Coinvestigador técnico (IES) | Ingeniería electrónica, de telecomunicaciones, estadística o afín | Validación de sensores frente a referencia con R², NRMSE, pendiente y sesgo | [DATO_USUARIO: nombre y hoja de vida] |
| C03 Coinvestigadores de ambiente y ciencias sociales (IES) | Ciencias ambientales, salud ambiental y ciencias sociales | Diseño participativo con instituciones y análisis de gestión del riesgo | [DATO_USUARIO: nombre y hoja de vida] |
| P01 Jóvenes investigadores | Ingeniería, estadística, ciencias ambientales o afín | Procesamiento de series de sensores y registro de bitácoras de campo | [DATO_USUARIO: nombre y hoja de vida o proceso de selección] |
| P02 Estudiantes de maestría | Posgrado en ingeniería, estadística o ciencias ambientales | Tesis sobre el modelo de corrección o la validación con datos del proyecto | [DATO_USUARIO: nombre y hoja de vida o proceso de selección] |
| P03 Científico de datos senior | Estadística, ciencia de datos o ingeniería | Modelos de corrección con validación cruzada por departamento y partición temporal | [DATO_USUARIO: nombre y hoja de vida] |
| P04 Ingenieros IoT y de campo | Ingeniería electrónica o de telecomunicaciones | Instalación de redes LoRa con gateways, energía solar y enlace celular o satelital | [DATO_USUARIO: nombre y hoja de vida] |
| P05 Coordinación de apropiación social | Ciencias sociales, comunicación o gestión del riesgo | Facilitación de talleres de co-diseño y actas con comunidades e instituciones | [DATO_USUARIO: nombre y hoja de vida] |
| P06 Gerencia de proyecto | Ingeniería, administración o afín, con formación en gerencia de proyectos | Control de alcance, cronograma, presupuesto y compuertas con informes de seguimiento | [DATO_USUARIO: nombre y hoja de vida] |
| P07 Especialista en metrología y calibración | Metrología, química, física o ingeniería | Trazabilidad frente a la referencia gravimétrica y manejo del banco de calibración | [DATO_USUARIO: nombre y hoja de vida] |
| P08 Ingenieros de software y nube | Ingeniería de sistemas o de software | Plataformas en la nube, bases de series temporales y tableros con pruebas de seguridad | [DATO_USUARIO: nombre y hoja de vida] |
| P09 Ingeniero de firmware y energía | Ingeniería electrónica o mecatrónica | Firmware de bajo consumo y dimensionamiento solar para 14 días sin sol | [DATO_USUARIO: nombre y hoja de vida] |
| P10 Técnicos de campo departamentales | Formación técnica o tecnológica en electrónica o telecomunicaciones | Instalación, mantenimiento y reposición de nodos en sitios de remoción con trabajo seguro | [DATO_USUARIO: nombre y hoja de vida o proceso de selección] |
| P11 Profesionales de apropiación social | Ciencias sociales, comunicación o educación | Talleres de co-diseño con comités y materiales para comunidades | [DATO_USUARIO: nombre y hoja de vida] |
| P12 Analista de datos espaciales y gemelo digital | Geografía, estadística, ingeniería o afín | Estimación espacial de PM2,5 y PM10 y validación del gemelo digital | [DATO_USUARIO: nombre y hoja de vida] |
| P13 Profesional en calidad del aire y salud ambiental | Ingeniería ambiental, salud ambiental o afín | Índice de calidad del aire y salud con umbrales locales y protocolo de alerta | [DATO_USUARIO: nombre y hoja de vida] |
| P14 Profesional de convenios y custodia | Derecho, administración pública o afín | Convenios por tramo, cláusula de apertura y titularidad de propiedad intelectual | [DATO_USUARIO: nombre y hoja de vida] |
:::NOTA *Nota.* Elaboración propia con los roles de maestro.py. Cada fila describe un perfil requerido y no una persona. Los niveles de formación y los años de experiencia mínimos dependen de los términos de referencia (VACIO) y de cada hoja de vida.

La tabla muestra 17 perfiles con una competencia verificable por cada uno. Tres perfiles (P01, P02 y P10) se pueden vincular por proceso de selección posterior a la aprobación, por lo cual su persona queda abierta. Los otros 14 perfiles requieren hoja de vida desde la radicación. Los siguientes apartados describen los perfiles por grupo de funciones.

### 17.2.1 Director e investigador principal

El investigador principal registra la dedicación parcial más alta del proyecto, con 0,5 ETC durante 24 meses. La línea C01 le asigna 350 millones de COP (DECLARADO). El perfil requerido combina formación en ingeniería o ciencias ambientales con experiencia verificable en proyectos que llevaron un desarrollo de laboratorio a entorno operativo. La persona queda como [DATO_USUARIO: nombre, hoja de vida y experiencia exigida por los TdR]. Sus funciones son dirigir la ejecución científica, representar al proyecto ante el financiador y presidir el comité técnico.

La escala de niveles de madurez tecnológica (TRL) ofrece un criterio para decidir cuándo un desarrollo pasa de un nivel al siguiente (Mankins, 1995). Cooper (2008) sitúa la decisión de avance en compuertas con criterios de negocio y de riesgo. La primera posición favorece a un director con criterio técnico. La segunda favorece a un director con criterio de gestión. El proyecto reparte los dos criterios entre cargos. El investigador principal responde por el criterio técnico de cada compuerta. La gerencia (P06) responde por el criterio de costo, plazo y riesgo.

La consecuencia metodológica es que el acta de cada compuerta lleva dos firmas de responsabilidad distinta. La del investigador principal certifica los umbrales de desempeño (R² y NRMSE). La de la gerencia certifica el estado de presupuesto, cronograma y riesgos. El comité directivo decide con ambos soportes. Esta regla evita que una sola persona apruebe el avance de un tramo sobre su propia evaluación.

### 17.2.2 Co-investigadores

Los co-investigadores aportan dos competencias que el personal financiado por el SGR no cubre completamente. El coinvestigador técnico (C02) dedica 0,3 ETC y coordina el WP1. Su línea suma 250 millones de COP (DECLARADO). Los dos coinvestigadores de ambiente y ciencias sociales (C03) dedican 0,2 ETC cada uno. Su línea suma 200 millones de COP (PROPUESTO). Los perfiles requeridos figuran en la {T:t02} y las personas quedan como [DATO_USUARIO: nombre y hoja de vida de cada coinvestigador].

Dos posiciones disputan la autoridad sobre una alerta. Los protocolos técnicos de la Agencia de Protección Ambiental de Estados Unidos (EPA) fijan el desempeño mediante métricas estadísticas frente a una referencia (EPA, 2021). Callon (1999) y Funtowicz y Ravetz (1993) sostienen que, con evidencia incierta y decisiones urgentes, las personas afectadas participan en la producción del conocimiento. El proyecto toma el ancla de la EPA para el desempeño de la medición (PROPUESTO). Toma la segunda posición para los umbrales locales del índice, que se co-diseñan con los comités.

La consecuencia es una división de la validación. El coinvestigador técnico valida el desempeño de la corrección con los umbrales de la ficha: R² mayor o igual a 0,70 y NRMSE menor o igual a 30 %. Los coinvestigadores de ambiente y ciencias sociales validan el sentido local de los umbrales de alerta con los comités. Ninguno de los dos validadores sustituye al otro.

### 17.2.3 Personal técnico

El personal técnico y profesional suma 21 personas y 504 persona-mes, es decir 80,8 % del esfuerzo del SGR (CALCULADO). Incluye a las líneas P03 a P14. Sus perfiles cubren ciencia de datos, redes de sensores, firmware, plataforma en la nube, estimación espacial, metrología, calidad del aire, apropiación social y convenios. La {T:t02} detalla el área de formación y la competencia verificable de cada línea.

El perfil de la ingeniería de red y de firmware depende de una decisión de arquitectura. La computación en el borde procesa los datos cerca de la fuente y reduce la dependencia del enlace (Shi et al., 2016). La red de área amplia de baja potencia presenta límites de capacidad que condicionan la tasa de envío de cada nodo (Adelantado et al., 2017). Una posición centraliza la corrección en la nube. La otra la ubica en el borde. La decisión DEC-F02 del proyecto fija la corrección en el gateway. Por ello los perfiles P04 y P09 requieren competencia en diseño de redes LoRa y en firmware de bajo consumo.

La consecuencia metodológica es que el científico de datos senior (P03) debe entregar un modelo que quepa en el gateway. El criterio de parsimonia del capítulo 6 se convierte en requisito de perfil. La plataforma en la nube (P08) y el análisis espacial (P12) usan el resultado del gateway y no lo reemplazan. Los seis técnicos de campo (P10) reciben formación en trabajo seguro (PROPUESTO). En los sitios de remoción usan las mascarillas de la línea M06.

### 17.2.4 Estudiantes vinculados

Los estudiantes vinculados forman el talento del proyecto y cubren 19,2 % del esfuerzo del SGR. Son seis jóvenes investigadores (P01) y dos estudiantes de maestría (P02). Los jóvenes se vinculan de los meses 1 a 12 con 144,0 millones de COP. Los estudiantes de maestría se vinculan de los meses 1 a 24 con 304,8 millones de COP. Juntos suman 120 persona-mes. Su selección depende de las condiciones de la modalidad en los TdR. Esas condiciones quedan como [DATO_USUARIO: modalidad de joven investigador y de beca de maestría].

Freire (2005) distingue la educación que deposita contenidos de la educación que se construye con problemas reales y con diálogo. La primera posición trata al estudiante como apoyo operativo. La segunda lo trata como productor de conocimiento. El proyecto adopta la segunda para los dos estudiantes de maestría, cuyas tesis usan los datos de colocalización y de validación (PROPUESTO). Los jóvenes investigadores apoyan el piloto del tramo 1 con tareas definidas en la {T:t01}.

La consecuencia metodológica es doble. Cada estudiante recibe un producto verificable, como un capítulo de tesis o una sección de artículo, vinculado al indicador PERS-P03. Además, la salida de los seis jóvenes en el mes 12 exige el protocolo de transferencia descrito en la sección 17.1.1. La IES debe certificar el vínculo de cada estudiante con un programa académico [DATO_USUARIO: programa de posgrado y convenio de vinculación].

## 17.3 Grupos de Investigación

### 17.3.1 Grupos vinculados

El proyecto exige cinco capacidades de investigación y no designa grupos concretos. La {T:t03} relaciona cada capacidad con una línea de investigación, con un rol y con las líneas del presupuesto que la financian. Los grupos que aportan cada capacidad son datos que solo el usuario posee. Cada grupo queda como [DATO_USUARIO: nombre y código del grupo]. El capítulo no afirma la existencia de ningún grupo.

:::TABLA t03 | Caracterización de las capacidades de investigación y de los grupos por vincular
| Capacidad requerida | Línea de investigación requerida (PROPUESTO) | Grupo vinculado | Categoría MinCiencias | Rol en el proyecto | Líneas del presupuesto asociadas |
| --- | --- | --- | --- | --- | --- |
| Calibración y metrología de partículas | Metrología de sensores ópticos de bajo costo | [DATO_USUARIO: nombre y código del grupo] | [DATO_USUARIO: categoría vigente] | Banco de calibración, colocalización y trazabilidad (WP1) | P07, C02, C04, E03, E07 |
| Modelado y ciencia de datos | Aprendizaje automático y estadística espacial aplicados a calidad del aire | [DATO_USUARIO: nombre y código del grupo] | [DATO_USUARIO: categoría vigente] | Modelo de corrección y gemelo digital (WP1 y WP2) | P03, P12, E08 |
| Sistemas embebidos, energía y comunicaciones | Redes de sensores LoRa, energía solar y cómputo en el borde | [DATO_USUARIO: nombre y código del grupo] | [DATO_USUARIO: categoría vigente] | Nodos, gateways, energía y enlace (WP2) | P04, P09, P10, E01 a E06 |
| Calidad del aire y salud ambiental | Exposición a material particulado y umbrales de alerta | [DATO_USUARIO: nombre y código del grupo] | [DATO_USUARIO: categoría vigente] | Umbrales locales del índice y protocolo de alerta (WP3) | P13, C03 |
| Gestión del riesgo y apropiación social | Gestión del riesgo de desastres, co-diseño y apropiación del conocimiento | [DATO_USUARIO: nombre y código del grupo] | [DATO_USUARIO: categoría vigente] | Co-diseño, formación y convenios de custodia (WP3) | P05, P11, P14, C03 |
:::NOTA *Nota.* Elaboración propia. Las capacidades y las líneas son PROPUESTO. Los grupos concretos y sus categorías son datos que solo el usuario posee y no se afirman en este documento.

La tabla permite verificar que cada capacidad cuenta con al menos una línea de personal asociada. Tres capacidades combinan líneas del SGR con la contrapartida de la IES. Dos capacidades se apoyan solo en líneas del SGR. La capacidad de metrología se apoya además en el laboratorio de calibración de la IES (C04), valorado en 300 millones de COP (PROPUESTO). La capacidad de sistemas embebidos se apoya en los equipos de las líneas E01 a E06. Si un grupo no certifica su participación, el capítulo 20 exige reemplazarlo por otro con la misma capacidad.

### 17.3.2 Categoría MinCiencias

La categoría de un grupo resume su capacidad acumulada ante el sistema nacional de ciencia, tecnología e innovación. El proyecto no asume ninguna categoría. Cada una queda como [DATO_USUARIO: categoría vigente del grupo en la última medición de MinCiencias]. Esa categoría informa la trayectoria del grupo, pero no sustituye la evidencia de resultados en medición de material particulado, que es VACIO para este proyecto.

La consecuencia es una regla de verificación. El anexo D del capítulo 20 lista los certificados que deben acompañar cada grupo. Sin certificado vigente, el grupo no figura como vinculado. Los términos de referencia pueden exigir una categoría mínima [DATO_USUARIO: requisito de categoría de los TdR]. Su ausencia en esta corrida deja la admisibilidad sin verificar.

### 17.3.3 Líneas de investigación

El proyecto requiere cinco líneas de investigación, descritas en la {T:t03}. La primera es la metrología de sensores ópticos de bajo costo, que enfrenta la sensibilidad de la lectura a la humedad (Jayaratne et al., 2018). La segunda es el aprendizaje automático y la estadística espacial para corregir y estimar. La tercera cubre redes de sensores, energía solar y cómputo en el borde. La cuarta trata la exposición a material particulado y los umbrales de alerta. La quinta trata la gestión del riesgo y la apropiación social.

Barkjohn et al. (2021) desarrollan una corrección única para Estados Unidos que incorpora la humedad relativa. Giordano et al. (2021) sistematizan los desafíos y las buenas prácticas de calibración, entre ellas la colocalización con instrumentos de referencia. La primera posición busca una corrección que se transfiera entre sitios. La segunda exige verificar cada contexto. El proyecto no resuelve la disputa con una cita. La resuelve con el diseño: el tramo 1 mide la línea base por departamento y la compuerta C1 decide si el modelo generaliza.

### 17.3.4 Capacidades complementarias

Las capacidades complementarias determinan si el desarrollo llega al entorno operativo. El proyecto parte de TRL 4 y llega a TRL 7 (PROPUESTO). Mankins (1995) ubica el TRL 4 en la validación de componentes en laboratorio y el TRL 7 en la demostración de un prototipo en entorno operativo. El laboratorio de la IES sostiene el primer tramo de esa escala. La infraestructura en la nube de la empresa, valorada en 800 millones de COP, y los técnicos de campo sostienen el segundo tramo.

Teece (1986) sostiene que el valor de una innovación depende de activos complementarios como la manufactura, los servicios y la distribución. Esa lectura explica por qué la alianza reúne a una IES con laboratorio y a una empresa con infraestructura. La consecuencia metodológica es la trazabilidad de cada capacidad hasta una línea de presupuesto o de contrapartida, como muestra la {T:t03}. Una capacidad sin línea asociada no se considera comprometida.

## 17.4 Alianzas y Co-ejecutores

### 17.4.1 Entidades aliadas

La alianza entre una IES y una empresa tecnológica es SUPUESTO por instrucción del usuario. Los nombres de ambas entidades quedan como [DATO_USUARIO: nombre de la IES y razón social de la empresa]. La {T:t04} clasifica a los actores en co-ejecutores, aliados de uso, referencias y proveedores. Solo los dos co-ejecutores aportan contrapartida. Los demás actores participan sin aporte y sin compromiso escrito.

:::TABLA t04 | Matriz de alianzas y aportes
| Entidad | Vínculo | Rol en el proyecto | Aporte (M COP) | Forma | Naturaleza | Soporte pendiente |
| --- | --- | --- | --- | --- | --- | --- |
| IES ejecutora [DATO_USUARIO: nombre de la entidad] | Co-ejecutor (SUPUESTO) | Ejecución legal, dirección científica y laboratorios (C01 a C04) | 1.100,0 | Especie | Total DECLARADO; desglose de C03 y C04 PROPUESTO | Certificación de la IES |
| Empresa tecnológica [DATO_USUARIO: razón social] | Co-ejecutor (SUPUESTO) | Nube, propiedad intelectual y código, logística de emergencia (C05 y C06) | 1.010,0 | 210,0 efectivo y 800,0 especie | DECLARADO | Carta, certificación y acuerdo de titularidad |
| Alcaldías de 12 municipios [DATO_USUARIO: lista de municipios] | Aliado de uso y custodio potencial | Sus comités usan el tablero y asumen la custodia por tramo | 0,0 | Sin aporte | VACIO | Cartas con partida y competencia |
| Gobernaciones y unidades departamentales de gestión del riesgo | Aliado de uso y custodio potencial | Tres comités departamentales y custodia potencial | 0,0 | Sin aporte | NO_VERIFICADO | Cartas de compromiso |
| UNGRD y puestos de mando unificado | Aliado de uso | Reciben información y aplican el protocolo de alerta | 0,0 | Sin aporte | INFERIDO | Carta de aceptación del protocolo |
| IDEAM y autoridades ambientales | Referencia metrológica | Punto de referencia para la colocalización | 0,0 | Sin aporte | INFERIDO | Convenio de referencia |
| Laboratorio acreditado, laboratorio externo y evaluación externa | Proveedores de servicio, no aliados | Gravimetría (S01), ensayo independiente (S08) y evaluación (S07) | 0,0 | 294,0 con cargo al SGR | DECLARADO y PROPUESTO | Cotización y alcance de acreditación |
| Total de contrapartida | — | — | 2.110,0 | 210,0 efectivo y 1.900,0 especie | CALCULADO | — |
:::NOTA *Nota.* Elaboración propia con la contrapartida de maestro.py (C01 a C06) y los actores de 4.4-MDR.5. La alianza empresa-IES es SUPUESTO por instrucción del usuario. M COP: millones de pesos colombianos. Decimales con coma.

El mapa de la {F:f02} muestra la misma estructura. Mitchell et al. (1997) definen la relevancia de un actor por su poder, su legitimidad y su urgencia. La evaluación de esos atributos exige evidencia que el expediente no aporta. Por ello el análisis de actores de 4.4-MDR.5 registra la relevancia como NO_EVALUADO para casi todos los actores. Esta tabla y el mapa no corrigen ese vacío. Solo ordenan a los actores por su vínculo con el proyecto.

:::FIGURA f02 | Mapa de alianzas estratégicas del proyecto | Nota. Elaboración propia con la contrapartida de maestro.py (C01 a C06) y los actores de 4.4-MDR.5; script c17_figs.py, sin semilla; corte de datos 13 de octubre de 2026. Montos en millones de COP. Naturaleza: aportes DECLARADO, con desglose de la IES PROPUESTO; alianza SUPUESTO.

El Sistema Nacional de Gestión del Riesgo de Desastres organiza instancias nacionales y territoriales de decisión (Congreso de la República, 2012). Los 15 comités del proyecto, 12 municipales y tres departamentales, pertenecen a ese sistema y son los usuarios del tablero (SUPUESTO). Ningún actor del sistema firmó un compromiso con el proyecto. Por consiguiente, el proyecto no cuenta con las alcaldías como aportantes. Las trata como custodios potenciales sujetos a las compuertas C1 y C2.

### 17.4.2 Rol de cada co-ejecutor

La IES ejecutora responde ante el control fiscal. Dirige científicamente el proyecto. Aporta el investigador principal, el coinvestigador técnico, los dos coinvestigadores de ambiente y ciencias sociales y los laboratorios (líneas C01 a C04). La empresa tecnológica responde por la propiedad intelectual y por el código de la plataforma. Aporta la infraestructura en la nube (C06) y la logística y los viáticos de emergencia (C05). Estos roles proceden del análisis de actores de 4.4-MDR.5, que se basó en el expediente E3 (DECLARADO).

Chesbrough (2003) sostiene que las organizaciones obtienen valor al combinar ideas y rutas de mercado internas y externas. Teece (1986) advierte que quien controla los activos complementarios captura buena parte del valor de la innovación. Las dos posiciones se aplican a la nube de la empresa. La alianza amplía la capacidad, pero también crea dependencia de un solo proveedor. El proyecto responde con tres instrumentos. El primero es la cláusula de apertura y salida ordenada. El segundo es el acuerdo de titularidad que exige el indicador PERS-P02. El tercero es el análisis de libertad de operación (riesgo R-JUR-01).

La consecuencia metodológica es que el convenio de ejecución debe fijar quién titula el modelo de corrección, el firmware y el gemelo digital. Debe fijar también qué ocurre con los datos y con la infraestructura al cierre. El profesional de convenios y custodia (P14) elabora ese convenio antes del acta de inicio (PROPUESTO). Sin convenio firmado, la actividad A0.1 no se considera concluida.

### 17.4.3 Aportes específicos

La contrapartida suma 2.110 millones de COP (DECLARADO, con certificaciones pendientes). La IES aporta 1.100 millones en especie. Corresponden 350 millones al investigador principal y 250 al coinvestigador técnico. Otros 200 millones corresponden a los coinvestigadores de ambiente y ciencias sociales y 300 al uso de laboratorios y equipos. La empresa aporta 210 millones en efectivo y 800 millones en especie. Las alcaldías no aportan (VACIO).

La contrapartida equivale a 22,8 % del valor solicitado al SGR y a 18,5 % del total del proyecto. La especie representa 90,0 % del aporte. El efectivo representa 10,0 % del aporte y 1,8 % del total del proyecto. Estas proporciones muestran que el proyecto depende de valoraciones en especie, que requieren certificación para ser admisibles. El riesgo R-FIN-02 recoge esa dependencia y el plan lo trata con la estrategia de evitar: certificar antes del acta de inicio.

Ostrom (2005) distingue reglas de posición, de información y de pago que gobiernan quién actúa, qué sabe y qué recibe en un arreglo institucional. La contrapartida es una regla de pago. La custodia por tramo es una regla de posición. El tablero compartido es una regla de información. El proyecto diseña los convenios con las tres reglas explícitas. El anexo A del capítulo 20 lista las cartas y las certificaciones que respaldan cada aporte. La compuerta C2 exige convenios de custodia con partida, de modo que ningún tramo se libera sin compromiso presupuestal verificable.
