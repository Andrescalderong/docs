%% PREFIJO: 9
# Capítulo 9. Cronograma

El cronograma traduce la estructura de desglose del trabajo en una red de 17 actividades con duración, precedencias y holgura. La red se calculó con el método de la ruta crítica (CPM, por sus siglas en inglés). Este método determina el plazo mínimo del proyecto y las actividades que no admiten retraso. El resultado coincide con el plazo de ejecución: 104 semanas, equivalentes a 24 meses de calendario si un mes equivale a 52/12 semanas. Las duraciones son propuestas de formulación, y la red no cambia por decisión editorial: cualquier ajuste se calcula de nuevo desde las precedencias.

El capítulo sigue cuatro pasos. Primero presenta el diagrama de Gantt (sección 9.1). Segundo lista los hitos y los entregables (sección 9.2). Tercero analiza la ruta crítica y las holguras (sección 9.3). Cuarto define las sesiones de revisión y aprendizaje que cortan el proyecto en fases (sección 9.4). La lógica común es que la red, y no la intención del equipo, determina qué actividad controla el plazo.

## 9.1 Cronograma general (Gantt)

### 9.1.1 Lectura del diagrama de Gantt

El diagrama de Gantt de la {F:f01} ordena las 17 actividades por paquete de trabajo. Marca el inicio temprano, el fin temprano y la holgura de cada una. Las barras de la ruta crítica se distinguen de las demás con el color de acento. Las compuertas C1 y C2 aparecen como actividades de dos semanas y no como hitos instantáneos. La decisión exige tiempo de revisión del comité directivo. La compuerta C1 ocupa las semanas 48 a 50, y la compuerta C2 ocupa las semanas 68 a 70.

:::FIGURA f01 | Una ruta crítica de 13 actividades ocupa las 104 semanas; cuatro actividades tienen holgura | Nota. Elaboración propia con maestro.py (ACT y cpm). El mes de calendario equivale a 52/12 semanas. Las barras con holgura muestran su ventana de flexibilidad. Naturaleza: CALCULADO. Figura generada con matplotlib mediante c9_figs.py; sin semilla ni corpus.

El diagrama permite comprobar tres propiedades de la red. La ruta crítica atraviesa los cuatro paquetes y suma las 104 semanas del proyecto. Las actividades A1.1, A3.1, A3.2 y A3.3 tienen holgura. La compuerta C1 depende de las actividades A1.4 y A3.1, y la compuerta C2 depende de A1.5 y A3.2. La primera propiedad es la que el expediente E3-P00 no cumplía. Su ruta crítica sumaba 38 semanas en un proyecto de 104, señal de una red incompleta. En esta formulación, la ruta crítica y el plazo coinciden por construcción y por verificación.

### 9.1.2 Fases del cronograma

Las compuertas dividen el cronograma en tres fases. La primera, de 50 semanas, comprende la contratación, el diseño, la compra del primer lote, la colocalización y la validación del modelo. La segunda, de 20 semanas, comprende la instalación del tramo 2, el reentrenamiento por departamento y la puesta en uso del tablero. La tercera, de 34 semanas, comprende la instalación del tramo 3, la verificación final y la transferencia. La fase 1 es la más larga, con 50 semanas. La fase 3 sigue con 34 semanas, aunque instala el tramo más pequeño, porque incluye el ensayo independiente y la formación de custodios.

La distribución de la duración responde a la incertidumbre. La fase 1 concentra el mayor riesgo técnico, y por eso incluye 16 semanas de colocalización antes de decidir. Reducir esa duración ahorraría tiempo, pero acortaría la muestra de pares nodo-referencia con la que se estima el modelo. El plazo de 16 semanas se justifica en el capítulo 6 con el cálculo de horas-nodo válidas. No se negocia sin recalcular ese tamaño de muestra.

## 9.2 Hitos y entregables

### 9.2.1 Matriz de hitos

Los hitos H0 a H8 marcan la verificación de resultados. La {T:t01} presenta la matriz. Cada hito tiene su descripción, su mes, su semana de fin, las actividades que lo definen y el entregable que lo verifica. Los meses 2, 4, 10, 12, 16, 17, 19, 23 y 24 distribuyen los hitos de forma desigual. Cuatro caen en la fase 1, dos en la fase 2 y tres en la fase 3. La primera fase requiere más puntos de control antes de comprometer recursos.

:::TABLA t01 | Matriz de hitos y entregables
| Hito | Descripción | Mes | Semana de fin | Actividades que lo definen | Entregable y verificación |
| --- | --- | --- | --- | --- | --- |
| H0 | Acta de inicio y contratación completa | 2 | 8 | A0.1 | Contratos, convenios y plan de trabajo aprobados |
| H1 | Sitios del tramo 1 y diseño de enlace y energía listos | 4 | 14 | A1.1, A2.1 | Informe de sitios, de cobertura y de energía |
| H2 | Colocalización del tramo 1 finalizada | 10 | 40 | A1.3 | Base de datos de colocalización y línea base de error medida |
| H3 | Compuerta C1: modelo validado en el piloto | 12 | 50 | C1 | Acta de compuerta con NRMSE y R² frente a referencia |
| H4 | Tramo 2 instalado y verificado | 16 | 68 | A1.5 | Informe de disponibilidad y desempeño del tramo 2 |
| H5 | Compuerta C2: uso institucional y desempeño | 17 | 70 | C2 | Acta de compuerta con uso del tablero y convenios |
| H6 | Tramo 3 instalado | 19 | 82 | A2.4 | Inventario de 100 nodos y 10 gateways operativos |
| H7 | Ensayo independiente y evaluación final | 23 | 98 | A1.6 | Informe de laboratorio externo y evaluación externa |
| H8 | Transferencia y cierre del tramo 3 | 24 | 104 | A3.4 | Actas de entrega a custodios y cláusula de apertura firmada |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (HITOS y ACT) y de la ficha maestra §6. El mes es el de calendario (un mes equivale a 52/12 semanas). Naturaleza: CALCULADO.

Dos hitos son compuertas de decisión. El hito H3 (compuerta C1, mes 12) decide si se amplía al tramo 2. El hito H5 (compuerta C2, mes 17) decide si se consolida el tramo 3. Los demás hitos son de verificación y no condicionan la compra. Esta separación evita que el equipo trate todos los hitos con la misma gravedad. Un retraso del hito H1 mueve el cronograma, pero no detiene la inversión; un incumplimiento en el hito H3 sí la detiene.

### 9.2.2 Calendario de entregas

El calendario de entregas convierte los hitos en una agenda mensual. La {T:t02} lista las entregas a lo largo de los 24 meses, con su origen y su verificación. Incluye los informes de seguimiento al financiador, según el calendario de los términos de referencia [DATO_USUARIO: calendario de informes]. Incluye también las entregas propias del proyecto. La tabla permite detectar meses sin entrega verificable. Esos meses concentran el riesgo de que un atraso pase inadvertido.

:::TABLA t02 | Calendario de entregas
| Mes | Entrega | Origen | Verificación |
| --- | --- | --- | --- |
| 2 | H0: Acta de inicio y contratación completa | Hito H0 | Contratos, convenios y plan de trabajo aprobados |
| 4 | H1: Sitios del tramo 1 y diseño de enlace y energía listos | Hito H1 | Informe de sitios, de cobertura y de energía |
| 4 | Estudio de cobertura y de enlace en tres departamentos | Línea S06 | Informe de cobertura aprobado |
| 5 | Compra del lote del tramo 1: 36 nodos y 4 gateways | Compra por tramo (E01, E02, E04) | Orden de compra tras el acta de inicio y el diseño de enlace |
| 5 | Banco de calibración de laboratorio operativo | Línea E07 | Acta de recibo e instalación |
| 6 | Tres monitores gravimétricos de referencia instalados | Línea E03 | Acta de recibo y de colocalización |
| 10 | H2: Colocalización del tramo 1 finalizada | Hito H2 | Base de datos de colocalización y línea base de error medida |
| 12 | H3: Compuerta C1: modelo validado en el piloto | Hito H3 | Acta de compuerta con NRMSE y R² frente a referencia |
| 12 | Primera evaluación externa independiente | Línea S07 | Informe del evaluador |
| 12 | Formación y soporte a custodios del tramo 1 | Línea S09 | Registro de personas certificadas |
| 13 | Compra del lote del tramo 2: 48 nodos y 4 gateways | Compra por tramo (E01, E02, E04) | Orden de compra tras la compuerta C1 |
| 16 | H4: Tramo 2 instalado y verificado | Hito H4 | Informe de disponibilidad y desempeño del tramo 2 |
| 17 | H5: Compuerta C2: uso institucional y desempeño | Hito H5 | Acta de compuerta con uso del tablero y convenios |
| 17 | Formación y soporte a custodios del tramo 2 | Línea S09 | Registro de personas certificadas |
| 18 | Compra del lote del tramo 3: 36 nodos y 3 gateways | Compra por tramo (E01, E02, E04) | Orden de compra tras la compuerta C2 |
| 19 | H6: Tramo 3 instalado | Hito H6 | Inventario de 100 nodos y 10 gateways operativos |
| 23 | H7: Ensayo independiente y evaluación final | Hito H7 | Informe de laboratorio externo y evaluación externa |
| 24 | H8: Transferencia y cierre del tramo 3 | Hito H8 | Actas de entrega a custodios y cláusula de apertura firmada |
| 24 | Segunda evaluación externa independiente | Línea S07 | Informe del evaluador |
| 24 | Campaña de ensayo de desempeño con laboratorio externo (meses 20 a 24) | Línea S08 | Informe del laboratorio externo |
| 24 | Dos artículos sometidos y al menos uno aceptado | Línea O01; PERS-P03 | Cartas de recepción y aceptación |
| 24 | Formación y soporte a custodios del tramo 3 | Línea S09 | Registro de personas certificadas |
| 24 | Registro del software de corrección y gemelo digital | Línea O03; PERS-P02 | Certificado de registro |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (HITOS, TRAMOS y BUDGET). Los meses de los servicios con rango (S06, E03, E07, S07, S08, O01, O03, S09) son el mes de cierre de la línea o el de la compuerta correspondiente (PROPUESTO). La periodicidad de los informes al financiador es [DATO_USUARIO: periodicidad exigida por los términos de referencia].

El calendario cumple una función de gestión adicional. Permite a la gerencia anticipar los meses con varias entregas simultáneas. El mes 12 es un ejemplo: coinciden la compuerta C1 y el cierre de la primera fase. En esos meses conviene reforzar la capacidad de revisión. También permite coordinar con los comités: las entregas que requieren su participación se programan con anticipación y con convocatoria formal.

## 9.3 Ruta crítica

### 9.3.1 Análisis de las 17 actividades

La ruta crítica reúne las actividades cuya holgura es cero. La {T:t03} presenta, para cada actividad, la duración, el inicio y el fin tempranos, el inicio y el fin tardíos, la holgura y el paquete. Hay 13 actividades críticas y cuatro con holgura. La holgura máxima es de 12 semanas, en las actividades A3.1 y A3.3, y la mínima es de 2 semanas, en A1.1. La red conecta las actividades críticas en una sola cadena que va de la contratación al cierre.

:::TABLA t03 | Análisis de ruta crítica de las 17 actividades
| Id | Actividad | Duración (sem.) | ES | EF | LS | LF | Holgura (sem.) | Crítica | WP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0.1 | Contratar equipo y firmar convenios de ejecución | 8 | 0 | 8 | 0 | 8 | 0 | Sí | WP0 |
| A1.1 | Seleccionar sitios y diseñar la colocalización | 4 | 8 | 12 | 10 | 14 | 2 | No | WP1 |
| A2.1 | Diseñar arquitectura de enlace y energía | 6 | 8 | 14 | 8 | 14 | 0 | Sí | WP2 |
| A3.1 | Co-diseñar umbrales y protocolo de alerta con comités | 24 | 12 | 36 | 24 | 48 | 12 | No | WP3 |
| A1.2 | Adquirir y caracterizar lote 1 de nodos y referencias | 10 | 14 | 24 | 14 | 24 | 0 | Sí | WP1 |
| A2.2 | Desarrollar firmware y plataforma base | 10 | 14 | 24 | 14 | 24 | 0 | Sí | WP2 |
| A1.3 | Colocalizar y calibrar en el piloto (tramo 1) | 16 | 24 | 40 | 24 | 40 | 0 | Sí | WP1 |
| A1.4 | Entrenar y validar el modelo de corrección | 8 | 40 | 48 | 40 | 48 | 0 | Sí | WP1 |
| C1 | Compuerta C1: decisión de ampliación al tramo 2 | 2 | 48 | 50 | 48 | 50 | 0 | Sí | WP0 |
| A2.3 | Instalar tramo 2 (40 nodos, 4 gateways) | 12 | 50 | 62 | 50 | 62 | 0 | Sí | WP2 |
| A3.2 | Poner en uso el tablero con los comités | 12 | 50 | 62 | 56 | 68 | 6 | No | WP3 |
| A1.5 | Reentrenar y verificar por departamento (tramo 2) | 6 | 62 | 68 | 62 | 68 | 0 | Sí | WP1 |
| C2 | Compuerta C2: decisión de consolidación al tramo 3 | 2 | 68 | 70 | 68 | 70 | 0 | Sí | WP0 |
| A2.4 | Instalar tramo 3 (30 nodos, 3 gateways) | 12 | 70 | 82 | 70 | 82 | 0 | Sí | WP2 |
| A3.3 | Formar custodios y firmar convenios por tramo | 16 | 70 | 86 | 82 | 98 | 12 | No | WP3 |
| A1.6 | Verificar desempeño final y ensayo independiente | 16 | 82 | 98 | 82 | 98 | 0 | Sí | WP1 |
| A3.4 | Transferir, cerrar y evaluar | 6 | 98 | 104 | 98 | 104 | 0 | Sí | WP0 |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (cpm). ES y EF = inicio y fin tempranos; LS y LF = inicio y fin tardíos; holgura = LS menos ES. Naturaleza: CALCULADO; las duraciones son las de la ficha maestra §6.

Dos conclusiones se desprenden de la tabla. Primera, la mayor parte del plazo depende de WP1 y WP2. Las actividades críticas del paquete WP1 suman 56 semanas. Las del paquete WP2 suman 30 semanas de la serie principal. El paquete WP3 tiene holgura. El co-diseño y la puesta en uso pueden absorber retrasos de hasta 12 semanas sin mover el cierre. Segunda, un retraso de una semana en una actividad crítica equivale a 0,96 % del plazo, y uno de tres semanas equivale a 2,9 %.

### 9.3.2 Diagrama de red

El diagrama de red de la {F:f02} dibuja las precedencias. Cada nodo muestra la actividad, su duración y su holgura. La cadena crítica atraviesa trece nodos. Las cuatro actividades con holgura forman ramas laterales que se reincorporan a la cadena en las compuertas. Esa forma de la red significa que las compuertas son puntos de sincronización: allí confluyen los paquetes y allí se decide.

:::FIGURA f02 | 13 de 17 actividades forman la ruta crítica; las demás tienen holguras de 2 a 12 semanas | Nota. Elaboración propia con maestro.py (ACT y cpm). Cada nodo indica identificador, duración y holgura en semanas. Naturaleza: CALCULADO. Figura generada con matplotlib mediante c9_figs.py; sin semilla ni corpus.

La sensibilidad del plazo a las duraciones es directa. Como la ruta crítica es única, cada semana adicional en una actividad crítica se suma al plazo. Esto da un criterio de priorización de riesgos. Los riesgos que afectan actividades críticas merecen respuesta antes que los demás. Son ejemplos la saturación de cabezales en la colocalización (R-TEC-01) y el retraso por deslizamientos en la instalación (R-EXT-01). Las cuatro actividades con holgura absorben retrasos de 2 a 12 semanas sin consecuencia para el cierre. No los absorben si el retraso las convierte en críticas.

## 9.4 Sesiones de revisión y aprendizaje

### 9.4.1 Calendario de sesiones

Un proyecto de desarrollo tecnológico aprende mientras ejecuta, y el cronograma debe reservar tiempo para ello. Las sesiones se organizan en tres niveles. Cada semana se registra una bitácora. Cada dos semanas se realiza una retrospectiva. Al cerrar cada fase se hace una revisión formal que alimenta la decisión de la compuerta o del cierre. La {T:t04} presenta el calendario. Hay 104 bitácoras semanales y 52 retrospectivas quincenales. Las retrospectivas se reparten así: 25 en la fase 1, 10 en la fase 2 y 17 en la fase 3.

:::TABLA t04 | Calendario de sesiones de revisión y aprendizaje
| Fase | Semanas | Bitácoras semanales | Retrospectivas quincenales | Revisión de fase | Punto de decisión |
| --- | --- | --- | --- | --- | --- |
| Tramo 1 | 0 a 50 | 50 | 25 | Antes de C1: revisión de H2 y H3 | Compuerta C1 (semanas 48 a 50) |
| Tramo 2 | 50 a 70 | 20 | 10 | Antes de C2: revisión de H4 y H5 | Compuerta C2 (semanas 68 a 70) |
| Tramo 3 | 70 a 104 | 34 | 17 | Antes del cierre: revisión de H6 a H8 | Cierre y transferencia, C3 (mes 24) |
| Total | 0 a 104 | 104 | 52 | Tres revisiones de fase | Tres puntos de decisión |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (cpm). Una bitácora por semana y una retrospectiva cada dos semanas; las fases se cortan en el fin de las compuertas C1 y C2. La plantilla de la bitácora se define en el Capítulo 6. Naturaleza: CALCULADO y PROPUESTO.

La plantilla de la bitácora y el protocolo de las retrospectivas se definen en el capítulo 6, y no se repiten aquí. El capítulo 9 asigna el tiempo. Las revisiones de fase coinciden con las compuertas. Así, cada decisión de continuar, detener o reorientar se toma con un registro de aprendizajes de la fase. La literatura sobre aprendizaje organizacional distingue entre corregir un error dentro de las reglas vigentes y cuestionar las reglas mismas (Argyris, 1999). Las bitácoras sostienen la primera forma de aprendizaje y las revisiones de fase la segunda.

### 9.4.2 Consecuencias para la gestión del tiempo

Las sesiones tienen un costo en horas del equipo que ya está incluido en las dedicaciones del capítulo 8, y no agregan líneas presupuestales. Su beneficio es doble. Reducen el riesgo de que un aprendizaje se pierda por rotación del personal. Y alimentan los criterios de pivote del capítulo 10 con evidencia documentada. Un equipo que decide en la compuerta C1 sin bitácora decide con memoria, y un equipo con bitácora decide con registros.

El cronograma resultante es una hipótesis de formulación con tres condiciones de revisión. La primera es la recepción de los términos de referencia, que pueden fijar plazos de informes o hitos obligatorios. La segunda es el contrato con el proveedor de equipos, que debe confirmar el plazo de importación de 12 semanas como máximo por lote. La tercera es la contratación del equipo, cuyo plazo de ocho semanas define el hito H0. Si alguna de las tres cambia, la red se recalcula completa y se publica de nuevo con su ruta crítica.

## 9.5 Valor y límites del capítulo

El cronograma crea valor porque identifica qué actividades controlan el plazo y cuáles no. Esa información orienta la vigilancia de la gerencia y la asignación de la reserva. Sus límites son tres. Las duraciones son propuestas sin contrato. La red no incluye variabilidad probabilística de las duraciones, y por eso el plazo de 104 semanas es una cifra determinista. Y las holguras dependen de que las precedencias declaradas sean las únicas, un supuesto que el equipo debe confirmar con los responsables de cada actividad.
