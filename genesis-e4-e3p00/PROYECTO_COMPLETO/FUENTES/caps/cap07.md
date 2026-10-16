%% PREFIJO: 7

# Capítulo 7. Estructura de Desglose del Trabajo (EDT/WBS)

Este capítulo descompone el proyecto en unidades de trabajo que pueden presupuestarse, programarse, asignarse y verificarse. La descomposición sigue cinco niveles: proyecto, fase, entregable, paquete de trabajo y actividad. Cada nivel hereda del anterior su alcance y no lo supera. El capítulo cierra con la matriz de responsabilidades (RACI) y el organigrama funcional. Los nombres de personas y entidades quedan por definir [DATO_USUARIO: nombres de entidad ejecutora, empresa tecnológica y equipo]. La alianza es un supuesto por instrucción del usuario.


## 7.1 Estructura Jerárquica

La estructura jerárquica organiza el alcance completo del proyecto en niveles de detalle creciente. El Project Management Institute [PMI] (2021) define la EDT como una descomposición jerárquica del trabajo total. Ese trabajo lo ejecuta el equipo para lograr los objetivos y crear los entregables. La regla de cobertura total exige que la suma de los componentes de un nivel agote el alcance del nivel superior. Esa regla impide trabajo oculto y obliga a que cada línea del presupuesto tenga un destino. La {T:t01} resume los cinco niveles, su cantidad y su regla de formación, y la {F:f01} los muestra completos.

:::TABLA t01 | Niveles de la EDT, cantidad de componentes y regla de formación
| Nivel | Componente | Cantidad | Regla de formación | Naturaleza |
| --- | --- | --- | --- | --- |
| 1 | Proyecto | 1 | Red IoT híbrida y gemelo digital de 24 meses y 104 semanas | DECLARADO |
| 2 | Fase (tramo de despliegue) | 3 | Un tramo por compuerta de decisión: C1, C2 y C3 | PROPUESTO |
| 3 | Entregable (hito) | 9 | Un hito verificable por evidencia, H0 a H8, asignado a una fase | PROPUESTO |
| 4 | Paquete de trabajo (WP) | 4 (16 segmentos por entregable) | Un paquete por objetivo específico y uno de gestión: WP0 a WP3 | PROPUESTO |
| 5 | Actividad | 17 | Una actividad por nodo de la red CPM, con duración en semanas | CALCULADO |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (maestro.py) y de las secciones 4.4-MDR y 4.5. Un segmento de paquete es la intersección de un entregable con un paquete de trabajo; hay 16 intersecciones no vacías. Decimales con coma.

:::FIGURA f01 | La EDT descompone el proyecto en 3 fases, 9 entregables, 16 segmentos de paquete y 17 actividades | Nota. Elaboración propia con datos de maestro.py (ACT, HITOS, TRAMOS). Cada actividad se asigna al primer hito alcanzable aguas abajo en la red. Borde grueso: ruta crítica. Python 3 y matplotlib; script c7_figs.py; sin semilla; corte del 13 de octubre de 2026.

La descomposición responde a la estructura del problema que el proyecto atiende. Simon (1973) sostiene que los problemas mal estructurados se resuelven al dividirlos en subproblemas bien estructurados, cada uno con criterios propios de solución. El problema central de este proyecto, el error de medición sin verificar (V06), pertenece a esa clase. Sus causas son físicas, energéticas e institucionales a la vez. Por eso la EDT separa la medición verificada, la red y el uso institucional en paquetes distintos. Cada paquete tiene un criterio de éxito propio y una responsabilidad única. La contrapartida es que la separación oculta interacciones, como el efecto de la disponibilidad de nodos sobre la calibración. La matriz de la sección 7.3 asigna esas interacciones al rol consultado.

**Nivel 1: proyecto.** El nivel 1 contiene un solo componente y fija el alcance contractual. El proyecto entrega una red de 100 nodos y 10 gateways que mide material particulado con error conocido. Entrega también un uso institucional documentado de sus lecturas. No promete efectos en salud. Esa delimitación sigue la regla de coherencia de la ficha maestra y evita que un paquete de trabajo absorba compromisos que el diseño no sustenta. La duración total es de 24 meses, equivalentes a 104 semanas, y coincide con la ruta crítica de la red de actividades (Project Management Institute [PMI], 2021).

**Nivel 2: fases.** El nivel 2 adopta los tres tramos de despliegue como fases, y no las etapas clásicas de diseño, construcción y cierre. Dos posiciones compiten en este punto. Cooper (2008) propone un proceso por etapas y compuertas, en el que cada compuerta autoriza la inversión de la etapa siguiente. El PMI (2021) recomienda descomponer por entregables y deja las fases como agrupación posterior. El proyecto combina ambas: las fases siguen las compuertas C1, C2 y C3, y el nivel 3 conserva los entregables. La ventaja es que la compra de nodos y gateways de cada tramo queda atada a una decisión y no a una fecha.

La progresión de madurez tecnológica refuerza la elección de las fases. Mankins (1995) definió los niveles de madurez tecnológica (TRL) como una escala de nueve grados para comparar tecnologías entre sí. El proyecto parte del TRL 4 y alcanza el TRL 7 (PROPUESTO). La fase 1 valida el modelo de corrección en el piloto. La fase 2 lo reentrena por departamento. La fase 3 lo demuestra en entorno operativo con 100 nodos. Esa secuencia convierte cada compuerta en una evidencia de madurez. El TRL 8 queda condicionado a una evaluación independiente que el plazo no cubre.

**Nivel 3: entregables.** El nivel 3 reúne nueve entregables, H0 a H8, que coinciden con los hitos del cronograma. Cada uno se identifica por una evidencia, y no por una actividad terminada. H3, por ejemplo, exige un acta de compuerta con el error normalizado (NRMSE) y el coeficiente de determinación (R²) frente a la referencia. Esa exigencia separa el entregable del esfuerzo, como lo separan los modelos lógicos de programa (Funnell y Rogers, 2011). La fase 1 contiene cuatro entregables, la fase 2 contiene dos y la fase 3 contiene tres.

**Nivel 4: paquetes de trabajo.** El nivel 4 define cuatro paquetes: WP0 de gestión, WP1 de medición verificada, WP2 de red, energía y plataforma, y WP3 de uso institucional, apropiación y custodia. Los tres últimos corresponden a los objetivos específicos OE1, OE2 y OE3. Esa correspondencia uno a uno permite medir el avance de cada objetivo con el presupuesto y con los indicadores de su paquete. La contrapartida es que ninguna actividad puede atender dos objetivos a la vez. El diseño acepta esa restricción porque simplifica la asignación de responsabilidades.

**Nivel 5: actividades.** El nivel 5 contiene 17 actividades, incluidas las compuertas C1 y C2 como actividades de dos semanas. Trece actividades forman la ruta crítica y cuatro tienen holgura de 2, 6 o 12 semanas. Las actividades de co-diseño y de formación (A3.1, A3.2 y A3.3) tienen la mayor holgura. Dependen de las compuertas y no del suministro de equipos. El capítulo 9 desarrolla esa red. La consecuencia metodológica es doble. Una demora en A1.3, la colocalización del piloto, retrasa todo el proyecto. Una demora en A3.1 consume holgura antes de afectar la compuerta C1.


## 7.2 Diccionario de la EDT

El diccionario describe cada paquete de trabajo con su alcance, sus entregables y sus criterios de aceptación. El diccionario complementa la EDT y evita la ambigüedad de los títulos breves (PMI, 2021). En este proyecto el diccionario cumple una segunda función: vincula cada paquete con su presupuesto y con los indicadores del sistema PERS. La {T:t02} presenta los cuatro paquetes con el valor solicitado al Sistema General de Regalías (SGR), las persona-mes y los criterios de aceptación.

:::TABLA t02 | Diccionario de paquetes de trabajo con presupuesto SGR y criterios de aceptación
| WP | Alcance | Entregables | Valor SGR | Cargos y persona-mes | Criterios de aceptación |
| --- | --- | --- | --- | --- | --- |
| WP0 | Gestión, compuertas y cierre: contratación, seguimiento físico y financiero, actas de compuerta, evaluación externa y transferencia. | H0, H3 (C1), H5 (C2) y H8 (cierre) | 1.436,0 M COP | 1 cargos; 24 persona-mes | Informes mensuales entregados a tiempo (PERS-R06); desviación presupuestal de 10 % o menos y de 5 % o menos al cierre (PERS-R04); tres actas de compuerta firmadas. |
| WP1 | Medición verificada (OE1): selección de sitios, colocalización con tres referencias gravimétricas, calibración, entrenamiento y validación del modelo de corrección. | H1, H2, H3, H4 y H7 | 1.732,3 M COP | 10 cargos; 168 persona-mes | Línea base de error medida en el tramo 1; R² de 0,70 o más y NRMSE de 30 % o menos frente a la referencia; 60.000 horas-nodo válidas o más; seis ciclos de calibración. |
| WP2 | Red, energía y plataforma (OE2): diseño de enlace y energía, firmware, instalación de 100 nodos y 10 gateways, nube y gemelo digital. | H1, H2, H4 y H6 | 4.180,1 M COP | 13 cargos; 312 persona-mes | 100 nodos y 10 gateways operativos; disponibilidad mensual de nodos de 90 % o más; pérdida de paquetes de 10 % o menos; autonomía de 14 días sin sol; almacenamiento local de 7 días. |
| WP3 | Uso institucional, apropiación y custodia (OE3): co-diseño de umbrales, tablero, protocolo de alerta, formación de custodios y convenios por tramo. | H3, H5 y H8 | 1.381,5 M COP | 5 cargos; 120 persona-mes | Uso del tablero por 75 % o más de los comités al mes 24; 29 actividades de apropiación documentadas; 60 personas certificadas o más; convenios de custodia con partida. |
:::NOTA *Nota.* Elaboración propia con datos del libro maestro (líneas del presupuesto SGR por paquete) y de la ficha maestra §6 y §8. Los criterios de aceptación y la asignación de cargos son PROPUESTO; los valores monetarios son CALCULADOS. La suma de los cuatro paquetes es 8.729,8 M COP. Decimales con coma.

El paquete WP2 concentra 4.425,6 millones de pesos colombianos (COP), es decir, 47,8 % del valor solicitado. Allí residen la compra de nodos, gateways y cabezales, la instalación y las instancias en la nube. El paquete WP1 suma 1.902,2 millones, el WP3 suma 1.393,5 millones y el WP0 suma 1.546,0 millones. Esta distribución sigue el orden de riesgo del registro. El riesgo extremo R-TEC-01 y los tres riesgos técnicos de nivel alto recaen sobre WP1 y WP2. La consecuencia es que los criterios de aceptación de WP1 y WP2 son los más exigentes y los únicos que condicionan las compuertas por desempeño.

Los criterios de aceptación se redactan con umbrales medibles y con la fuente de verificación. Un criterio sin umbral no puede aprobarse ni rechazarse. Por esa razón el diccionario repite las metas del sistema PERS en lugar de parafrasearlas. Los umbrales de desempeño son R² de 0,70 o más y NRMSE de 30 % o menos. Toman como ancla los protocolos de la Agencia de Protección Ambiental de los Estados Unidos (U.S. Environmental Protection Agency [EPA], 2021) para uso informativo en sitio fijo. El umbral es una propuesta del equipo y requiere ratificación del panel evaluador (PROPUESTO, NO_VERIFICADO).

Cada indicador de proceso y de producto del sistema PERS se asigna a un paquete de trabajo. WP1 responde por PERS-R02, PERS-R05, PERS-P02 y PERS-P03. WP2 responde por PERS-R01, PERS-R03 y PERS-P01. WP3 responde por PERS-P04 y por los indicadores de efecto y de sostenibilidad (PERS-E01 a PERS-E03, PERS-S01 y PERS-S02). WP0 responde por PERS-R04 y PERS-R06, aunque la ficha los vincule con OE3, porque miden gestión y no uso institucional. Esa asignación es PROPUESTO. Permite que la persona responsable de cada paquete reporte sus indicadores sin depender de otra y sin duplicar la medición (Funnell y Rogers, 2011).

Dos posiciones sobre el nivel de detalle del diccionario merecen contraste. La primera, de orientación predictiva, defiende fijar criterios cerrados desde el inicio para evitar disputas en la entrega (PMI, 2021). La segunda, de orientación adaptativa, advierte que en tecnologías con incertidumbre los criterios deben revisarse con los datos del piloto (Collingridge, 1980). El proyecto adopta una solución mixta. Los criterios de WP1 y WP2 se fijan ahora. Los de WP3 sobre uso institucional se confirman en C1, cuando exista una línea base medida. Esa decisión reduce el riesgo de aprobar una meta que no se puede medir.

La {T:t03} cruza los nueve entregables con los paquetes que los producen. Cada fila indica el mes del hito, las actividades por paquete, la fase y la evidencia de verificación.

:::TABLA t03 | Matriz de entregables por paquete de trabajo, fase y evidencia de verificación
| Hito | Entregable | Mes | Fase | Actividades por paquete | Evidencia de verificación |
| --- | --- | --- | --- | --- | --- |
| H0 | Acta de inicio y contratación completa | 2 | Fase 1 | WP0: A0.1 | Contratos, convenios y plan de trabajo aprobados |
| H1 | Sitios del tramo 1 y diseño de enlace y energía listos | 4 | Fase 1 | WP1: A1.1; WP2: A2.1 | Informe de sitios, de cobertura y de energía |
| H2 | Colocalización del tramo 1 finalizada | 10 | Fase 1 | WP1: A1.2, A1.3; WP2: A2.2 | Base de datos de colocalización y línea base de error medida |
| H3 | Compuerta C1: modelo validado en el piloto | 12 | Fase 1 | WP0: C1; WP1: A1.4; WP3: A3.1 | Acta de compuerta con NRMSE y R² frente a referencia |
| H4 | Tramo 2 instalado y verificado | 16 | Fase 2 | WP1: A1.5; WP2: A2.3 | Informe de disponibilidad y desempeño del tramo 2 |
| H5 | Compuerta C2: uso institucional y desempeño | 17 | Fase 2 | WP0: C2; WP3: A3.2 | Acta de compuerta con uso del tablero y convenios |
| H6 | Tramo 3 instalado | 19 | Fase 3 | WP2: A2.4 | Inventario de 100 nodos y 10 gateways operativos |
| H7 | Ensayo independiente y evaluación final | 23 | Fase 3 | WP1: A1.6 | Informe de laboratorio externo y evaluación externa |
| H8 | Transferencia y cierre del tramo 3 | 24 | Fase 3 | WP0: A3.4; WP3: A3.3 | Actas de entrega a custodios y cláusula de apertura firmada |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (HITOS y ACT). El mes de calendario resulta de dividir las semanas entre 52/12 y redondear hacia arriba. La asignación de actividades a entregables sigue la regla del primer hito alcanzable aguas abajo. Naturaleza: CALCULADO para meses y PROPUESTO para evidencias.

La matriz muestra que seis entregables dependen de más de un paquete. H1, H2, H3, H4, H5 y H8 requieren coordinación entre dos o tres paquetes, y por tanto exigen una responsabilidad única de integración. La asignan la gerencia de proyecto y el comité directivo, como se detalla en la sección siguiente. La ruta crítica atraviesa WP0, WP1 y WP2, mientras WP3 aporta holgura. En consecuencia, el seguimiento semanal prioriza las actividades críticas y el mensual cubre las de holgura.

El diccionario también resuelve un problema de trazabilidad presupuestal. Cada una de las 54 líneas del presupuesto SGR pertenece a un solo paquete, y cada paquete agrupa entre 7 y 23 líneas. La regla evita doble contabilización y permite reconstruir el valor de un entregable. El valor del piloto del tramo 1, por ejemplo, surge de sumar las líneas de WP1 y WP2 ejecutadas entre los meses 1 y 12. El capítulo 8 aplica esa regla en el flujo de caja y en la curva S.


## 7.3 Matriz de Responsabilidades (RACI)

La matriz RACI asigna a cada actividad un nivel de responsabilidad por rol. Las cuatro letras tienen un significado fijo. R designa al responsable, quien ejecuta. A designa al aprobador, quien responde por el resultado y firma. C designa al consultado, quien aporta antes de decidir. I designa al informado, quien recibe el resultado. La práctica habitual de la matriz exige un solo aprobador por actividad. El diseño respeta esa regla. Cuando el aprobador también ejecuta, la celda indica A/R. La {T:t04} presenta la matriz para las 17 actividades de la EDT.

:::TABLA t04 | Matriz RACI por actividad y paquete de trabajo
| Actividad | WP | CD | GP | DC | MET | IOT | ASC | EV | US | FIN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0.1 (crítica) | WP0 | C | A/R | C | I | I | R |  |  | I |
| A1.1 | WP1 | I | C | A | R | C | C |  | C |  |
| A2.1 (crítica) | WP2 | I | A | C | C | R |  |  |  |  |
| A3.1 | WP3 | I | A | C | C | C | R |  | R |  |
| A1.2 (crítica) | WP1 | I | C | A | R | R |  |  |  |  |
| A2.2 (crítica) | WP2 | I | A | C | C | R |  |  |  |  |
| A1.3 (crítica) | WP1 | I | C | A | R | R | C | I | C |  |
| A1.4 (crítica) | WP1 | I | C | A | R | C |  | I |  |  |
| C1 (crítica) | WP0 | A | R | C | C | C | C | C | I | I |
| A2.3 (crítica) | WP2 | I | A | C | C | R | C |  | I |  |
| A3.2 | WP3 | I | A | C | C | C | R |  | R |  |
| A1.5 (crítica) | WP1 | I | C | A | R | C |  |  |  |  |
| C2 (crítica) | WP0 | A | R | C | C | C | C | C | I | I |
| A2.4 (crítica) | WP2 | I | A | C | C | R | C |  | I |  |
| A3.3 | WP3 | I | A | C | C | C | R |  | R | I |
| A1.6 (crítica) | WP1 | I | C | A | R | R |  | C | I |  |
| A3.4 (crítica) | WP0 | A | R | R | C | C | R | C | C | I |
:::NOTA *Nota.* Elaboración propia. Roles (PROPUESTO): CD, comité directivo de la entidad ejecutora y la empresa tecnológica; GP, gerencia de proyecto (P06); DC, dirección científica; MET, medición y datos (P01, P02, P03, P07); IOT, red, software y campo (P04, P08, P09, P10, P12); ASC, apropiación, calidad del aire y custodia (P05, P11, P13, P14); EV, evaluación externa (S07); US, comités de gestión del riesgo; FIN, financiador. R: responsable; A: aprobador; C: consultado; I: informado; celda vacía: sin participación. Cada fila tiene un solo aprobador.

La matriz concentra la aprobación en tres roles. La dirección científica aprueba las actividades de medición. La gerencia de proyecto aprueba las de red, uso y gestión. El comité directivo aprueba las compuertas y el cierre. Esa separación sigue la idea de que quien decide una compuerta no debe ser quien ejecuta la actividad evaluada. Los comités de gestión del riesgo figuran como responsables del co-diseño y del uso del tablero (A3.1, A3.2 y A3.3). El indicador de uso institucional depende de su participación efectiva. Mitchell et al. (1997) clasifican a los interesados según su poder, su legitimidad y su urgencia. Los comités combinan legitimidad y urgencia, porque usan las lecturas para decidir alertas.

La asignación de responsabilidades admite dos lecturas. La lectura jerárquica concentra la decisión en pocos roles para acelerar las compuertas (PMI, 2021). La lectura policéntrica reparte la decisión entre quienes poseen la información local y mantiene reglas visibles para todos los participantes (Ostrom, 2005). El proyecto combina ambas lecturas. Las compuertas se deciden en un comité reducido, y el co-diseño del uso se decide con los comités de gestión del riesgo. La combinación responde a la naturaleza del riesgo organizacional R-ORG-01, la no adopción del tablero, que ninguna decisión jerárquica puede resolver por sí sola.

El organigrama de la {F:f02} traduce la matriz en una estructura funcional. Un comité directivo preside la gerencia de proyecto y la dirección científica. Tres paquetes técnicos dependen de la gerencia. La evaluación externa independiente se ubica al margen de la línea jerárquica, de modo que su juicio no dependa de quien ejecuta. En total, el equipo suma 29 cargos y 624 persona-mes en cuatro paquetes. Los roles son PROPUESTO y los nombres de las personas y de las entidades permanecen sin definir.

:::FIGURA f02 | El equipo del SGR suma 29 cargos y 624 persona-mes en tres líneas técnicas | Nota. Elaboración propia con datos de maestro.py (líneas P01 a P14). Organigrama funcional; roles PROPUESTO; entidades SUPUESTO. Python 3 y matplotlib; script c7_figs.py; sin semilla; corte del 13 de octubre de 2026.

La matriz presenta dos riesgos de diseño que el proyecto registra. El primero es la concentración de aprobación en el comité directivo para las compuertas y el cierre. Si el comité no se reúne en la semana prevista, la compuerta retrasa la compra del tramo siguiente. La mitigación es fijar en el acta de inicio el calendario de reuniones y un suplente por cada miembro. El segundo es la dependencia de los comités de gestión del riesgo, que son actores externos sin vínculo contractual. El capítulo 10 trata ambos y el capítulo 17 describe el equipo de trabajo. Las firmas de aprobación del organigrama se completan en el acta de inicio [DATO_USUARIO: nombres y cargos del comité directivo].
