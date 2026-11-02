%% PREFIJO: 7
# Capítulo 7. Estructura de desglose del trabajo (EDT/WBS)

La estructura de desglose del trabajo (EDT, o WBS por sus siglas en inglés) descompone el alcance del proyecto en paquetes. Cada paquete se puede presupuestar, programar y asignar. El Project Management Institute (PMI) define la EDT como una descomposición jerárquica del alcance total del trabajo (Project Management Institute [PMI], 2021). Este capítulo aplica esa definición al proyecto de la red híbrida de vigilancia de material particulado. La estructura sale de los datos maestros del proyecto: 17 actividades, cuatro paquetes de trabajo, nueve hitos y 11 roles. Ninguna cifra se calcula fuera de esa fuente.

Una EDT útil cumple tres condiciones. Cada actividad pertenece a un solo paquete. La suma de los paquetes reproduce el alcance y el presupuesto. Cada paquete tiene un criterio de aceptación verificable. El capítulo muestra que la estructura propuesta satisface las tres. Los cuatro paquetes suman 9.267.260.000 COP del Sistema General de Regalías (SGR) y 2.110.000.000 COP de contrapartida. Cada uno tiene su criterio en la ficha de la {T:t01}.

## 7.1 Estructura jerárquica

### 7.1.1 Niveles de la estructura

La EDT tiene cuatro niveles. El nivel 0 es el proyecto completo. El nivel 1 reúne las tres fases que corresponden a los tramos de despliegue: piloto de contraste, ampliación condicionada y consolidación con transferencia. El nivel 2 agrupa los entregables que verifican los hitos H0 a H8. El nivel 3 contiene los paquetes de trabajo WP0 a WP3, divididos en segmentos por fase, y las actividades de la red de precedencias. Los segmentos suman 16; cada uno resulta de cruzar un paquete con una fase.

La razón de organizar el nivel 1 por tramos y no por disciplinas es de control. Los tramos fijan las compuertas C1 y C2, que liberan la compra del tramo siguiente. Si la EDT se organizara por disciplina, la decisión de ampliar no tendría un entregable único que la sustente. La literatura de desarrollo por etapas con compuertas sostiene una regla. Cada etapa cierra con un entregable que alimenta una decisión explícita de continuar, detener o rehacer (Cooper, 2008). La {F:f01} presenta la estructura completa.

:::FIGURA f01 | La EDT descompone el proyecto en tres fases, nueve entregables, 16 segmentos de paquete y 17 actividades | Nota. Elaboración propia con maestro.py (ACT, HITOS y TRAMOS) y la ficha maestra §4 y §6. Las fases corresponden a los tramos 1 a 3; los entregables, a los hitos H0 a H8. Figura generada con matplotlib mediante c7_figs.py; sin semilla ni corpus.

La figura permite dos lecturas. La primera es de cobertura: ninguna de las 17 actividades queda fuera de un paquete. La segunda es de dependencia. Los entregables de los hitos H3 y H5 son las compuertas C1 y C2. Cada una depende de actividades de tres paquetes distintos. Esa dependencia cruzada obliga a que la gerencia coordine los paquetes WP1, WP2 y WP3 antes de cada compuerta. Por eso el paquete WP0 conserva la autoridad sobre las compuertas.

### 7.1.2 Asignación de actividades a paquetes

La asignación de actividades a paquetes sigue el objetivo específico que cada paquete sirve. El paquete WP1 responde al objetivo OE1 (medición verificada) y reúne las actividades A1.1 a A1.6. El paquete WP2 responde a OE2 (red, energía y plataforma) y reúne A2.1 a A2.4. El paquete WP3 responde a OE3 (uso institucional, apropiación y custodia) y reúne A3.1 a A3.3. El paquete WP0 reúne la contratación, las dos compuertas y el cierre, además de la reserva de contingencia de 636,0 millones de COP.

El peso de cada paquete en el presupuesto del SGR confirma la prioridad técnica del proyecto. WP2 concentra 47,8 % del SGR, con 4.425,6 millones de COP, porque contiene la compra de nodos, gateways y energía. WP1 aporta 20,5 %, con 1.902,2 millones. WP0 reúne 16,7 %, con 1.546,0 millones, de los cuales 636,0 millones son reserva. WP3 reúne 15,0 %, con 1.393,5 millones. Sin la reserva, WP0 baja a 910,0 millones de COP. La distribución no es un juicio de importancia: WP3 recibe la menor parte del SGR y, sin embargo, aloja el supuesto crítico de adopción institucional.

## 7.2 Diccionario de la EDT

### 7.2.1 Diccionario de paquetes de trabajo

El diccionario de la EDT describe cada paquete con su alcance, sus actividades, su responsable, su costo y su criterio de aceptación. La {T:t01} reúne esos campos. El responsable se expresa como rol y no como persona, porque los nombres son datos que solo el ejecutor posee. Los criterios de aceptación proceden de la ficha maestra y coinciden con las metas de los indicadores del capítulo 12.

:::TABLA t01 | Diccionario de paquetes de trabajo
| Paquete | Descripción | Actividades | Responsable (rol) | SGR (COP) | Contrapartida (COP) | Criterio de aceptación |
| --- | --- | --- | --- | --- | --- | --- |
| WP0 Gestión, compuertas y cierre | Contratación, convenios, compuertas C1 y C2, evaluación externa, pólizas, administración y cierre | A0.1, C1, C2, A3.4 | Gerencia de proyecto (P06) | 1.546.000.000 | 350.000.000 | Desviación presupuestal ≤ 5 % al cierre; informes de seguimiento 100 %; actas de C1 y C2 |
| WP1 Medición verificada (OE1) | Colocalización con referencias, modelo de corrección en el gateway y verificación del desempeño | A1.1, A1.2, A1.3, A1.4, A1.5, A1.6 | Especialista en metrología y calibración (P07) | 1.902.200.000 | 550.000.000 | R² ≥ 0,70; NRMSE ≤ 30 %; pendiente 0,65 a 1,35; sesgo ±5,0 µg/m³; ≥ 60.000 horas-nodo válidas |
| WP2 Red, energía y plataforma (OE2) | Diseño de enlace y energía, firmware, plataforma, instalación por tramos y mantenimiento | A2.1, A2.2, A2.3, A2.4 | Ingenieros IoT y de campo (P04) | 4.425.560.000 | 1.010.000.000 | Disponibilidad mensual ≥ 90 %; pérdida de paquetes ≤ 10 %; 100 nodos y 10 gateways operativos |
| WP3 Uso institucional, apropiación y custodia (OE3) | Co-diseño de umbrales y protocolo, uso del tablero, formación de custodios y convenios | A3.1, A3.2, A3.3 | Coordinación de apropiación social (P05) | 1.393.500.000 | 200.000.000 | ≥ 75 % de los comités usa el tablero; ≥ 60 personas certificadas; 29 actividades de apropiación |
| Total |  | 17 actividades |  | 9.267.260.000 | 2.110.000.000 |  |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (ACT, BUDGET y CONTRA) y de la ficha maestra §2, §5, §6 y §8. Los roles son PROPUESTO; las personas son [DATO_USUARIO: nombres por rol]. WP0 incluye la reserva de contingencia de 636,0 millones de COP. Valores en COP con miles separados por punto.

La tabla revela dos rasgos del diseño. El primero es que cada criterio se mide con un instrumento del proyecto. Los umbrales de WP1 salen de la colocalización. La disponibilidad de WP2 sale de la plataforma. El uso de WP3 sale del registro de decisiones de los comités. El segundo es que la contrapartida se concentra en WP2 y WP1, con 1.010,0 y 550,0 millones de COP en especie y en efectivo. La contrapartida de la institución de educación superior sostiene a las personas que operan la medición. La de la empresa sostiene la nube y la logística.

### 7.2.2 Matriz de entregables

Los entregables conectan la EDT con el cronograma. Cada hito H0 a H8 se verifica con un documento o con un acta. Cada entregable se origina en actividades de uno o varios paquetes. La {T:t02} asigna las actividades al primer hito que alcanzan aguas abajo en la red. Esa regla evita contar una actividad en dos hitos y permite auditar la trazabilidad entre paquete, actividad y entrega.

:::TABLA t02 | Matriz de entregables por paquete de trabajo
| Hito | Mes | Fase | Entregable verificado | WP0 | WP1 | WP2 | WP3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H0 | 2 | Tramo 1 | Contratos, convenios y plan de trabajo aprobados | A0.1 | — | — | — |
| H1 | 4 | Tramo 1 | Informe de sitios, de cobertura y de energía | — | A1.1 | A2.1 | — |
| H2 | 10 | Tramo 1 | Base de datos de colocalización y línea base de error medida | — | A1.2, A1.3 | A2.2 | — |
| H3 | 12 | Tramo 1 | Acta de compuerta con NRMSE y R² frente a referencia | C1 | A1.4 | — | A3.1 |
| H4 | 16 | Tramo 2 | Informe de disponibilidad y desempeño del tramo 2 | — | A1.5 | A2.3 | — |
| H5 | 17 | Tramo 2 | Acta de compuerta con uso del tablero y convenios | C2 | — | — | A3.2 |
| H6 | 19 | Tramo 3 | Inventario de 100 nodos y 10 gateways operativos | — | — | A2.4 | — |
| H7 | 23 | Tramo 3 | Informe de laboratorio externo y evaluación externa | — | A1.6 | — | — |
| H8 | 24 | Tramo 3 | Actas de entrega a custodios y cláusula de apertura firmada | A3.4 | — | — | A3.3 |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (HITOS, ACT). Cada actividad se asigna al primer hito alcanzable aguas abajo en la red; un guion indica que el paquete no aporta al hito. Naturaleza: CALCULADO (hitos y actividades) y PROPUESTO (asignación a hitos).

Tres hitos dependen de un solo paquete: H0, H6 y H7. El hito H3 depende de tres paquetes, lo que confirma la lectura de la {F:f01}: la compuerta C1 integra medición, plataforma y uso institucional. Una consecuencia metodológica sigue de ese hecho. Los informes de seguimiento no pueden presentarse por paquete aislado antes de C1. Deben presentarse por hito, con las tres contribuciones juntas.

## 7.3 Matriz de responsabilidades (RACI)

### 7.3.1 Roles y asignación

La matriz RACI asigna, para cada paquete y cada decisión de compuerta, cuatro funciones. R indica quién es responsable y A quién aprueba. C indica quién es consultado e I quién es informado. El equipo del SGR suma 29 cargos y 624 persona-mes, agrupados en 11 roles. La {T:t03} usa esos roles. El comité directivo aprueba los paquetes y las tres decisiones de compuerta. La gerencia de proyecto es responsable de todos los paquetes y de las compuertas.

:::TABLA t03 | Matriz RACI por paquete de trabajo y decisión de compuerta
| Paquete o decisión | CD | GER | CDS | MET | IOT | SWN | CAM | APR | CON | AIR | EVA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WP0 Gestión, compuertas y cierre | A | R | C | C | C | I | I | C | C | I | C |
| WP1 Medición verificada (OE1) | I | A | R | R | C | C | R | I | I | C | C |
| WP2 Red, energía y plataforma (OE2) | I | A | C | C | R | R | R | I | I | I | I |
| WP3 Uso institucional y custodia (OE3) | I | A | C | I | I | C | C | R | R | R | C |
| Decisión de la compuerta C1 (mes 12) | A | R | C | C | I | I | I | C | I | C | C |
| Decisión de la compuerta C2 (mes 17) | A | R | C | C | C | I | I | C | C | C | I |
| Cierre y transferencia, C3 (mes 24) | A | R | C | C | C | C | I | R | R | C | C |
:::NOTA *Nota.* Elaboración propia. R = responsable; A = aprobador; C = consultado; I = informado. Roles PROPUESTO: CD = Comité directivo; GER = Gerencia de proyecto (P06); CDS = Ciencia de datos (P03, P12); MET = Metrología y calibración (P07); IOT = Ingeniería IoT, firmware y energía (P04, P09); SWN = Ingeniería de software y nube (P08); CAM = Técnicos de campo (P10); APR = Apropiación social (P05, P11); CON = Convenios y custodia (P14); AIR = Calidad del aire y salud ambiental (P13); EVA = Evaluación externa independiente (S07). Las personas y las entidades son [DATO_USUARIO: nombres por rol]. Una sola A por fila.

La matriz cumple dos reglas de control. Cada fila tiene exactamente un aprobador y al menos un responsable. Además, la gerencia figura como responsable en las siete filas. Esa concentración fija la coordinación en un solo rol y expone un riesgo de dependencia. Si la gerencia falta, no hay suplente definido. Esta limitación se registra en el capítulo 10 y exige designar una suplencia al firmar los contratos del hito H0.

### 7.3.2 Organigrama del proyecto

El organigrama del proyecto organiza los cargos por línea técnica. La {F:f02} muestra el tamaño de cada línea en cargos y en persona-mes. La línea técnica concentra 65,4 % del gasto de personal del SGR, con 2.976,0 millones de COP. La línea de gestión concentra 24,8 %, con 1.128,0 millones. La asistencia concentra 9,9 %, con 448,8 millones.

:::FIGURA f02 | El equipo del SGR suma 29 cargos y 624 persona-mes en tres líneas técnicas | Nota. Elaboración propia con maestro.py (líneas P01 a P14 de BUDGET). Los cargos son roles PROPUESTO; las personas son [DATO_USUARIO: nombres y hojas de vida]. Figura generada con matplotlib mediante c7_figs.py; sin semilla ni corpus.

El tamaño del equipo en persona-mes equivale a 26 personas de dedicación completa durante 24 meses, con un promedio de 7,3 meses por cargo. Esa cifra supone dedicaciones parciales que el contrato de cada cargo debe fijar. La estructura propuesta es una hipótesis de formulación. Su valor reside en una comparación previa a la contratación. Permite contrastar la carga de cada línea con la de las actividades que sirve. Así detecta cuellos de botella, como la concentración de responsabilidades en la gerencia.

## 7.4 Criterios de descomposición y control de la estructura

### 7.4.1 Reglas de descomposición

Una EDT bien formada respeta la regla del cien por ciento. La suma del trabajo de los niveles inferiores reproduce el trabajo del nivel superior, sin omisiones ni superposiciones (PMI, 2021). Esta estructura verifica la regla con dos pruebas aritméticas. La primera compara el presupuesto: los cuatro paquetes suman 9.267.260.000 COP, igual al valor solicitado al SGR. La segunda compara las actividades: los paquetes contienen 17 actividades distintas, igual a las de la red de precedencias. Ninguna actividad aparece en dos paquetes.

La regla tiene una interpretación discutida. Una posición sostiene que la EDT describe productos y entregables, no actividades, y que mezclar ambos niveles confunde el alcance con el plan. La posición contraria sostiene otra cosa. En proyectos de desarrollo tecnológico, el alcance cambia con los resultados del piloto. Por eso conviene conservar las actividades en la estructura para renegociarlas. Este proyecto adopta una solución intermedia. Los entregables forman el nivel 2 y las actividades forman el nivel 3. La estructura conserva ambos niveles y los separa.

La consecuencia metodológica es que cualquier cambio de alcance debe registrarse en el nivel donde ocurre. Un cambio en el entregable de un hito exige la aprobación del comité directivo, porque altera una compuerta. Un cambio en una actividad que conserva el entregable lo decide la gerencia y se informa al comité.

### 7.4.2 Control de la estructura durante la ejecución

El control de la estructura se apoya en tres instrumentos. El primero es la comparación mensual entre el presupuesto ejecutado y el programado por paquete, que alimenta el indicador PERS-R04. El segundo es la verificación de cada entregable contra su criterio de aceptación antes de cerrar el hito. El tercero es el registro de cambios, que documenta cada modificación de una actividad, de un entregable o de un criterio.

Un dato de la estructura orienta el control. De las 17 actividades, 13 pertenecen a la ruta crítica y cuatro tienen holgura. En el paquete WP1, 56 de las semanas de duración total de sus actividades están sobre la ruta crítica; en WP0, 18. Cualquier retraso en esas actividades retrasa el proyecto completo, de modo que la gerencia vigila primero los paquetes WP1 y WP2. El capítulo 9 desarrolla el análisis de la ruta crítica.

La estructura admite una ampliación sin romper su lógica. El valor no solicitado de 4.732,7 millones de COP se describe en el capítulo 8 como opciones condicionadas a los términos de referencia. Las opciones son más nodos, un cuarto tramo o un año adicional de custodia. Cada opción se incorporaría como un segmento nuevo dentro de un paquete existente. No crearía un paquete nuevo. Así se conservan la regla del cien por ciento y la trazabilidad con los indicadores.

### 7.4.3 Correspondencia entre fases y madurez tecnológica

Las tres fases del nivel 1 también marcan el avance de la madurez tecnológica. La escala de niveles de madurez tecnológica (TRL, por sus siglas en inglés) describe nueve estados. Van desde el principio básico observado hasta el sistema probado en operación (Mankins, 1995). El proyecto parte del nivel 4, con componentes validados en laboratorio. Fija como meta el nivel 7, con demostración del sistema en entorno operativo (decisión DEC-F05). La correspondencia entre fases y niveles es una propuesta de formulación y no una evaluación independiente.

En la fase del tramo 1, los segmentos de WP1 y WP2 llevan los componentes del laboratorio al sitio. La colocalización con referencias convierte el nivel 4 en una validación en entorno relevante, equivalente al nivel 5 o 6. En la fase del tramo 2, la ampliación a 70 nodos y siete gateways demuestra el sistema en entornos distintos de tres departamentos. En la fase del tramo 3, la red completa de 100 nodos y 10 gateways opera durante el ensayo independiente del hito H7. Solo esa verificación externa sostiene la afirmación del nivel 7.

La relación tiene una consecuencia para el control de la EDT. Un entregable no se da por aceptado porque exista el documento, sino porque la evidencia respalda el nivel de madurez declarado. Si el ensayo independiente no confirma los umbrales, el proyecto declara el nivel alcanzado. También limita el alcance de la transferencia. El criterio de pivote del hito H7, en el capítulo 10, lo prevé.

## 7.5 Valor y límites del capítulo

La EDT convierte el alcance en unidades controlables y ata cada unidad a un criterio de aceptación. Ese vínculo reduce la discusión posterior sobre qué significa cumplir. Tiene tres límites. Los responsables son roles hipotéticos hasta que existan los contratos. Los criterios de aceptación de WP3 dependen de datos de uso que no existen todavía. Y la estructura no incorpora actividades de los TdR, que no se aportaron. Cuando los términos de referencia estén disponibles, el equipo formulador debe cotejar la EDT con las actividades obligatorias de la convocatoria. El cotejo cubre cuatro puntos: actividades exigidas, entregables obligatorios, topes por rubro y requisitos del equipo. Cada discrepancia se resuelve ajustando un segmento o un criterio de aceptación, nunca alterando la lógica de los tres tramos.
