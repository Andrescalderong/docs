%% PREFIJO: F3
# Paso 3. Procesamiento bibliométrico del corpus de vigilancia tecnológica

Este apartado reúne la salida del Paso 3 y del Paso 3.5 del metaprompt GENESIS-CTeI 36.10 RC2. El corpus procede del informe de vigilancia tecnológica y bibliometría consolidado el 30 de septiembre de 2026 (F-INF). El Paso 3 verifica la completitud del corpus, documenta la selección y fija los parámetros reproducibles. El Paso 3.5 aplica las reglas de corpus pequeño a las leyes de Lotka y de Bradford. Las figuras y las tablas analíticas se presentan en el Capítulo 2, sección 2.2. Este apartado remite a ellas en texto plano.

## 3.1 Verificación de completitud del corpus

### 3.1.1 Inventario de los 42 documentos

La regla absoluta del Paso 3 exige que cada documento del corpus figure en el inventario. La verificación compara cada referencia con la bibliografía de la sección 13.2 del informe de vigilancia (F-INF §13.2, p. 212). La comparación fue textual y automática. Se normalizaron cursivas, tildes y signos, y se contrastaron las 42 cadenas una por una. Las 42 referencias coinciden con la bibliografía del informe. La {T:tF01} lista los documentos con autores, año, tipo, fuente e identificador. El identificador es un identificador de objeto digital (DOI) o un número de solicitud. La tabla incluye el nivel de preparación tecnológica (TRL, por su sigla en inglés) cuando el informe lo reporta. El TRL usa una escala de nueve niveles (Mankins, 1995).

:::TABLA tF01 | Inventario completo de los 42 documentos del corpus
| ID | Autores | Año | Tipo | Fuente | DOI o número de solicitud | TRL | En F-INF §13.2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G-01 | Reintjes et al. | 1995 | Patente | OMPI | WO 95/12118 A1 | 3 | Sí |
| G-02 | Koppinen et al. | 2019 | Patente | OMPI | WO 2019/215392 A1 | 3 | Sí |
| G-03 | Abernathy et al. | 2019 | Patente | OEP | EP 3 483 800 A1 | 3 | Sí |
| G-04 | Blythe y Hohman | 2020 | Patente | OEP | EP 3 623 453 A1 | 4 | Sí |
| G-05 | Molina-Gómez et al. | 2021 | Artículo | International Journal of Environmental Science and Technology | 10.1007/s13762-020-02896-6 | 3 | Sí |
| G-06 | Becerra et al. | 2021 | Artículo | Urban Climate | 10.1016/j.uclim.2021.100960 | 4 | Sí |
| G-07 | Gumaste et al. | 2021 | Patente | OMPI | WO 2021/061603 A1 | 4 | Sí |
| G-08 | Rodríguez-Villamizar et al. | 2022 | Artículo | Environmental Health | 10.1186/s12940-022-00947-8 | 5 | Sí |
| G-09 | Ali et al. | 2022 | Patente | OMPI | WO 2022/217342 A1 | 3 | Sí |
| G-10 | Chang et al. | 2023 | Artículo | Sustainability | 10.3390/su152216064 | 4 | Sí |
| G-11 | Izod y Burch | 2023 | Patente | OMPI | WO 2023/139267 A1 | 3 | Sí |
| G-12 | Essamlali et al. | 2024 | Artículo | Sustainability | 10.3390/su16030976 | 5 | Sí |
| G-13 | Rendón-Marín et al. | 2024 | Artículo | International Journal of Environmental Research and Public Health | 10.3390/ijerph21060789 | 3 | Sí |
| G-14 | Hurst et al. | 2024 | Patente | OEP | EP 3 483 686 B1 | 3 | Sí |
| G-15 | Wilson et al. | 2024 | Patente | OMPI | WO 2024/064927 A1 | 3 | Sí |
| G-16 | Røine | 2024 | Patente | OMPI | WO 2024/080881 A1 | 2 | Sí |
| G-17 | Huang et al. | 2025 | Artículo | Atmosphere | 10.3390/atmos16091095 | 4 | Sí |
| G-18 | Vélez-Pereira et al. | 2025 | Artículo | Atmosphere | 10.3390/atmos16121377 | 4 | Sí |
| G-19 | de Moura et al. | 2025 | Artículo | Environmental Geochemistry and Health | 10.1007/s10653-025-02524-7 | 3 | Sí |
| G-20 | Suresh et al. | 2025 | Artículo | Sustainability | 10.3390/su17031301 | 6 | Sí |
| G-21 | Botezat et al. | 2025 | Artículo | Science of the Total Environment | 10.1016/j.scitotenv.2025.179560 | 4 | Sí |
| G-22 | Miraglia et al. | 2025 | Artículo | Air Quality, Atmosphere y Health | 10.1007/s11869-025-01701-y | 3 | Sí |
| G-23 | Hale et al. | 2025 | Patente | OEP | EP 4 617 736 A1 | 3 | Sí |
| G-24 | Eckenrode y Stevenson | 2025 | Patente | OMPI | WO 2025/049390 A2 | 3 | Sí |
| G-25 | Machida y Ammendola | 2025 | Patente | OMPI | WO 2025/257740 A1 | 4 | Sí |
| G-26 | Nelson et al. | 2026 | Artículo | Science of the Total Environment | 10.1016/j.scitotenv.2026.181593 | 5 | Sí |
| G-27 | Wei et al. | 2026 | Artículo | Urban Climate | 10.1016/j.uclim.2026.102937 | 4 | Sí |
| G-28 | Murad Pedraza et al. | 2026 | Artículo | Luna Azul | 10.17151/luaz.2025.62.13 | 3 | Sí |
| G-29 | Ruiz-Carrascal et al. | 2026 | Artículo | Climate Services | 10.1016/j.cliser.2026.100653 | 9 | Sí |
| G-30 | Ayala-Parra et al. | 2026 | Artículo | Atmospheric Research | 10.1016/j.atmosres.2025.108512 | 4 | Sí |
| G-31 | Bang et al. | 2026 | Artículo | Sensors | 10.3390/s26134307 | 4 | Sí |
| G-32 | Alvarez et al. | 2026 | Artículo | Geocarto International | 10.1080/10106049.2026.2684384 | 4 | Sí |
| G-33 | Espinoza et al. | 2026 | Artículo | Journal of South American Earth Sciences | 10.1016/j.jsames.2026.106211 | 7 | Sí |
| G-34 | Haris et al. | 2026 | Artículo | Environment Systems and Decisions | 10.1007/s10669-026-10090-1 | 4 | Sí |
| G-35 | Tavella et al. | 2026 | Artículo | Atmosphere | 10.3390/atmos17080797 | 3 | Sí |
| G-36 | Kumar et al. | 2026 | Artículo | CLEAN -- Soil, Air, Water | 10.1002/clen.70262 | 3 | Sí |
| G-37 | Liao et al. | 2026 | Artículo | Hygiene and Environmental Health Advances | 10.1016/j.heha.2026.100184 | 5 | Sí |
| G-38 | Gallego-Cartagena et al. | 2026 | Artículo | Science of the Total Environment | 10.1016/j.scitotenv.2025.181313 | 3 | Sí |
| G-39 | Huang et al. | 2026 | Artículo | Sustainable Cities and Society | 10.1016/j.scs.2026.107281 | 4 | Sí |
| G-40 | Acosta y Horstmann | 2026 | Patente | OMPI | WO 2026/093802 A1 | 3 | Sí |
| G-41 | Spasojevic Brkic et al. | 2026 | Patente | OMPI | WO 2026/180852 A1 | 4 | Sí |
| G-42 | Superintendencia de Industria y Comercio [SIC] | 2026 | Informe institucional | SIC (CIGEPI) | Sin DOI ni número | No reportado | Sí |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §13.2 (p. 212) y §4.1, Tabla 13 (p. 29). OMPI = Organización Mundial de la Propiedad Intelectual; OEP = Oficina Europea de Patentes; SIC = Superintendencia de Industria y Comercio. TRL en escala de 1 a 9 asignado por el analista del informe. Naturaleza: DOCUMENTADO. Verificación: PARCIALMENTE_VERIFICADO, porque se comprobó la coincidencia textual con el informe y no la resolución en línea de los DOI.

El inventario contiene 26 artículos con DOI, 15 patentes con número de solicitud o de patente y un informe institucional sin identificador. El TRL se reporta para 41 de los 42 documentos. El informe de la Superintendencia de Industria y Comercio (SIC) no describe una tecnología y carece de TRL (F-INF §4.1, p. 29). Las 15 patentes se reparten entre dos oficinas. La Organización Mundial de la Propiedad Intelectual (OMPI) publica 11 y la Oficina Europea de Patentes (OEP) publica cuatro. Ninguna referencia falta ni sobra frente a la bibliografía del informe. El inventario cumple la regla absoluta del Paso 3.

Los DOI se concentran en siete prefijos. Los prefijos 10.1016 y 10.3390 cubren 18 de los 26 artículos (69,2 %). Los otros cinco prefijos cubren ocho artículos. Cada patente tiene una oficina y un número propios, sin repeticiones. Esta comprobación protege el inventario contra duplicados que un conteo simple no detectaría.

### 3.1.2 Composición por grupo documental

El informe de vigilancia organiza el corpus en cinco grupos documentales que definió por criterio temático (F-INF §3.2, p. 22). La composición por grupo permite comprobar la estructura original. La {T:tF02} cruza cada grupo con el tipo documental y con el total del informe.

:::TABLA tF02 | Composición del corpus por grupo documental y tipo
| Grupo | Contenido temático | Artículos | Patentes | Informes | Total | Total en F-INF (§13.3, Tabla 67) |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Pronóstico con aprendizaje automático | 9 | 0 | 0 | 9 | 9 |
| G2 | Monitoreo, redes de sensores y alerta temprana | 8 | 0 | 0 | 8 | 8 |
| G3 | Exposición, carga de enfermedad y salud | 9 | 0 | 0 | 9 | 9 |
| G4 | Patentes de sensores y activos industriales | 0 | 8 | 0 | 8 | 8 |
| G5 | Patentes de espacios interiores y reporte de la SIC | 0 | 7 | 1 | 8 | 8 |
| Total | Corpus completo | 26 | 15 | 1 | 42 | 42 |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §13.3, Tabla 67 (p. 219), §10.1, Tabla 46 (p. 124) y §3.2 (p. 22). La asignación de cada documento a su grupo se reconstruyó con la Tabla 46 y con los conteos por año. Naturaleza: DOCUMENTADO; verificación: PARCIALMENTE_VERIFICADO.

Los tres primeros grupos reúnen los 26 artículos y los dos últimos reúnen las 15 patentes y el informe institucional. La suma coincide con la Tabla 67 del informe en los cinco casos. Seis de las ocho patentes de G4 son de 1995 a 2022. Las siete solicitudes del grupo G5 son de 2023 a 2026 y tratan edificios y exposición ocupacional. Esa separación explica por qué la composición temática cambia entre eras, como muestra el Capítulo 2, sección 2.2.8.

### 3.1.3 Verificación documento por documento

La verificación no se limita al conteo total. Cada comprobación contrasta un valor reproducido desde la bibliografía con el valor que reporta el informe. La {T:tF03} registra 13 comprobaciones y su resultado. La última concilia el inventario con el Paso 3 del expediente E3 que aportó el equipo del proyecto.

:::TABLA tF03 | Tabla de verificación de completitud del corpus
| N.º | Comprobación | Valor reproducido | Valor del informe de vigilancia | Resultado |
| --- | --- | --- | --- | --- |
| 1 | Documentos en el inventario | 42 | 42 (F-INF §3.1, p. 19) | Coincide |
| 2 | Tipos documentales | 26 artículos, 15 patentes, 1 informe | 26, 15 y 1 (F-INF §3.1, p. 19) | Coincide |
| 3 | Referencias con coincidencia textual en la bibliografía | 42 de 42 | 42 referencias (F-INF §13.2, p. 212) | Coincide |
| 4 | Artículos con DOI único | 26 de 26 | El DOI consta en cada referencia (F-INF §13.2) | Coincide |
| 5 | Patentes con número único de solicitud o de patente | 15 de 15 | El número consta en cada referencia (F-INF §13.2) | Coincide |
| 6 | Identificadores G-01 a G-42 asociados a una referencia con autor y año iguales | 42 de 42 | 42 filas (F-INF §4.1, Tabla 13, p. 29) | Coincide |
| 7 | TRL, IRL y DRL medios reproducidos desde la Tabla 13 | 3,85 (n = 41); 2,88 (n = 41); 3,05 (n = 42) | 3,85; 2,88; 3,05 (F-INF §3.2, Tabla 4, p. 22) | Coincide |
| 8 | Documentos por valle V1, V2, V3, V4, V5 y sin valle | 18, 6, 2, 13, 1 y 2 | 18, 6, 2, 13, 1 y 2 (F-INF §4.6, Tabla 17, p. 38) | Coincide |
| 9 | Documentos por año de 1995 a 2026 | 1, 2, 1, 3, 2, 2, 5, 9 y 17 en los nueve años con documentos | Mismos valores (F-INF §4.3, p. 34) | Coincide |
| 10 | Documentos por grupo documental | 9, 8, 9, 8 y 8 | 9, 8, 9, 8 y 8 (F-INF §13.3, Tabla 67, p. 219) | Coincide |
| 11 | Autores únicos por apellido e inicial | 213 | 213 (F-INF §7.6, p. 93) | Coincide |
| 12 | Autores por documento | 5,29 | 5,29 (F-INF §7.6, p. 93) | Coincide |
| 13 | Conciliación con el Paso 3 del expediente E3 | 26 artículos, 15 patentes, 1 informe; 83,3 % en 2022 a 2026 | E3 contiene dos conteos incompatibles (26, 15 y 1 frente a 25, 14 y 3) y 88,1 % en 2022 a 2026 | CONTRADICTORIO en E3; se adopta el valor reproducible |
:::NOTA *Nota.* Elaboración propia con datos de F-INF y del expediente E3 (DECLARADO). IRL = nivel de integración; DRL = nivel de preparación de la demanda. El valor de la comprobación 9 corresponde a los años 1995, 2019, 2020, 2021, 2022, 2023, 2024, 2025 y 2026. Naturaleza: CALCULADO; verificación: PARCIALMENTE_VERIFICADO.

Doce de las 13 comprobaciones coinciden con el informe de vigilancia. La restante señala una contradicción interna del expediente E3. El texto y el diagrama de flujo de E3 reportan 26 artículos, 15 patentes y un informe. La tabla de inventario de E3 reporta 25, 14 y tres. Su porcentaje de 88,1 % para 2022 a 2026 no coincide con 35 de 42 documentos (83,3 %). El proyecto adopta los valores reproducibles. Esa decisión elimina la inconsistencia en los capítulos posteriores.

## 3.2 Diagrama PRISMA y parámetros de selección

El esquema Elementos de Informe Preferidos para Revisiones Sistemáticas y Metaanálisis (PRISMA) ordena la selección en cuatro etapas: identificación, cribado, elegibilidad e inclusión (Page et al., 2021). El Paso 3 exige reportar el número de documentos en cada etapa. Solo la etapa de inclusión tiene un número documentado en este proyecto. Los 42 documentos llegaron como archivos aportados al informe de vigilancia. El informe no registra el criterio de selección (F-INF §10.1, p. 124). La {F:prisma} presenta el flujo y distingue los datos documentados de los no verificados.

:::FIGURA prisma | Diagrama PRISMA del corpus de 42 documentos | Nota. Elaboración propia con matplotlib a partir de F-INF §1.2 (p. 9), §3.1 (p. 19) y §10.1 (p. 124). Las etapas de identificación y cribado carecen de registro y se marcan NO_VERIFICADO. Corpus de 42 documentos; año de corte 2026; semilla 42.

El diagrama muestra una asimetría. La etapa de inclusión se documenta con precisión y las etapas previas carecen de registro. El proyecto no puede presentar este corpus como resultado de una búsqueda sistemática. Lo presenta como una muestra intencional y no aleatoria (F-INF §3.3, p. 24). La {T:tF04} reúne los parámetros de selección que pide el Paso 3. Declara cuáles se documentan, cuáles se calculan y cuáles faltan.

:::TABLA tF04 | Parámetros de selección del Paso 3
| Parámetro | Definición | Valor | Naturaleza y verificación |
| --- | --- | --- | --- |
| Documentos identificados (N) | Registros recuperados en bases de datos | Sin dato | VACIO; NO_VERIFICADO |
| Documentos tras eliminar duplicados (N2) | Registros únicos | Sin dato | VACIO; NO_VERIFICADO |
| Documentos evaluados a texto completo (N3) | Documentos leídos por completo | 42 | DOCUMENTADO (F-INF §1.2, p. 9) |
| Documentos incluidos (N4) | Corpus final | 42 | DOCUMENTADO (F-INF §3.1, p. 19) |
| Tasa de selección | N4 sobre N, en porcentaje | No calculable | NO_CALCULABLE por falta de N |
| Distribución por tipo | Artículos, patentes e informes sobre 42 | 61,9 %; 35,7 %; 2,4 % | CALCULADO |
| Distribución por cuartil | Q1, Q2, Q3, Q4 y sin cuartil | Sin dato | VACIO; no se consultaron bases de indicadores |
| Documentos de 2025 y 2026 | Corpus de los dos últimos años | 26 de 42 (61,9 %) | DOCUMENTADO (F-INF §3.1, p. 19) |
| Documentos de 2022 a 2026 | Últimos cinco años | 35 de 42 (83,3 %) | CALCULADO |
| Documentos de 2017 a 2026 | Últimos diez años | 41 de 42 (97,6 %) | CALCULADO |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §1.2 (p. 9), §3.1 (p. 19) y §13.2 (p. 212). Porcentajes sobre 42 documentos, con decimales con coma. Corpus de 42 documentos; año de corte 2026.

La tasa de selección no se calcula porque falta el número de registros identificados. La distribución por tipo sí se calcula: 61,9 % de artículos, 35,7 % de patentes y 2,4 % de informes. La distribución por cuartil queda vacía porque no se consultaron bases de indicadores de revistas. La concentración temporal es alta. Treinta y cinco de los 42 documentos son de 2022 a 2026, y solo uno es anterior a 2017. Esa concentración obliga a leer el corpus como un retrato reciente del campo y no como su historia completa.

El informe describe el ámbito del corpus: calidad del aire, sensores, pronóstico, exposición, salud y tecnología patentada. Cada documento se leyó por completo (F-INF §1.2, p. 9). El informe no registra criterios de exclusión ni documentos excluidos. Por esa razón, los criterios del Capítulo 2, sección 2.1, describen el corpus actual y orientan la vigilancia futura. No se presentan como criterios aplicados. Esta distinción evita atribuir al corpus un rigor de selección que el informe no documenta.

El proyecto propone completar las etapas ausentes durante el primer mes de ejecución (PROPUESTO). El plan tiene cuatro pasos. Primero, se ejecutan las ecuaciones E1 a E3 del Capítulo 2, sección 2.1, en las bases previstas. Se registra el número de registros por base. Segundo, se eliminan los duplicados por DOI y por título normalizado. Tercero, dos revisores aplican los criterios de inclusión y exclusión a título, resumen y texto completo. Cuarto, se actualiza el diagrama con los números reales y se calcula la tasa de selección. Hasta entonces, el diagrama de este apartado es la única versión vigente.

## 3.3 Parámetros reproducibles del análisis

### 3.3.1 Entorno, semillas y definiciones

El Paso 3 exige que cada cálculo sea reproducible. Esta sección fija el entorno, las semillas y las definiciones operativas. La {T:tF05} lista los parámetros. Distingue los que se calcularon en esta corrida de los que se heredan del informe de vigilancia sin recalcular.

:::TABLA tF05 | Parámetros reproducibles del análisis bibliométrico
| Parámetro | Valor o definición | Origen |
| --- | --- | --- |
| Corpus de entrada | 42 referencias estructuradas derivadas de la bibliografía del informe (§13.2) | DOCUMENTADO |
| Año de corte | 2026; fecha de corte del proyecto: 13 de octubre de 2026 | Ficha maestra |
| Entorno de cálculo | Python 3.13.16; numpy 2.5.3; scipy 1.18.1; networkx 3.7; matplotlib 3.11.2 | CALCULADO |
| Semilla | 42 para el remuestreo, la disposición de redes y la detección de comunidades | PROPUESTO por el metaprompt |
| Clave de autor | Apellido y primera inicial; los duplicados dentro de un documento se cuentan una vez | CALCULADO |
| Ley de Lotka | Máxima verosimilitud con aproximación continua y x mínimo de 1; mínimos cuadrados log-log; 1.000 réplicas bootstrap | CALCULADO |
| Ley de Bradford | 26 artículos en 19 revistas; zonas por tercios de artículos (8,67 por zona); desempate alfabético | CALCULADO |
| Eras históricas | Segmentación óptima de la serie anual 1995 a 2026 en tres tramos contiguos por mínima suma de cuadrados | CALCULADO |
| Tasa de crecimiento anual compuesta (CAGR) | (valor final dividido por valor inicial) elevado a 1 sobre n, menos 1; ventanas 2019 a 2026, 2021 a 2026 y 2024 a 2026 | CALCULADO |
| Red de palabras de título | 42 títulos; lista de palabras vacías; frecuencia mínima de 2; co-ocurrencia en el mismo título; Louvain con resolución de 1,0 | CALCULADO |
| Redes y tópicos de texto completo | TF-IDF, k-means (K de 15), LDA (K de 25), co-palabras (584 nodos) y acoplamiento (102 pares) | DOCUMENTADO (F-INF §7) |
| Madurez y robustez | Rúbricas del analista con escalas ordinales de 1 a 9 y de 0 a 10 | DOCUMENTADO (F-INF §2.2 y §3.2) |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §2.2 (p. 14), §3.2 (p. 22) y §7 (pp. 72-95). Las versiones corresponden al entorno de esta corrida. Corpus de 42 documentos; año de corte 2026; semilla 42.

Los parámetros heredados provienen de procedimientos que usan texto completo, como las redes de co-palabras y el acoplamiento bibliográfico (F-INF §7, pp. 72-95). El proyecto no los recalcula porque no dispone de los textos completos. Los parámetros calculados dependen solo de la bibliografía. Cualquier revisor puede repetirlos con el archivo de 42 referencias y la semilla 42. Los resultados de ambos tipos se rotulan con su naturaleza en cada tabla. El protocolo sigue la lógica del mapeo científico que implementa bibliometrix (Aria y Cuccurullo, 2017), con las adaptaciones que exige un corpus pequeño.

### 3.3.2 Definiciones operativas

El análisis define autor por apellido y primera inicial. Esa clave coincide con la del informe de vigilancia, que reporta 213 autores únicos. Dos autores de Bang et al. (2026) comparten apellido e inicial (Kim, K. H. y Kim, K.-R.) y se cuentan como uno. El máximo posible de autores únicos es por tanto 214. La diferencia no altera ninguna conclusión.

La productividad es el número de documentos por autor. La fuente de un artículo es su revista. Las patentes se agrupan por oficina de publicación y el informe institucional por entidad emisora. Esta definición evita mezclar revistas con oficinas en una misma distribución de Bradford, que se calcula solo sobre los 26 artículos.

Las eras históricas resultan de una segmentación de la serie anual. El algoritmo prueba todas las particiones en tres tramos contiguos y elige la de menor suma de cuadrados intra-tramo. Con 32 años calendario, el resultado es 1995 a 2023, 2024 a 2025 y 2026. La tasa de crecimiento anual compuesta se calcula en tres ventanas porque depende de los años de inicio y de fin. La ventana principal es 2019 a 2026, la única serie continua sin años vacíos.

La red de palabras de título usa los títulos de los 42 documentos. Se eliminaron las palabras vacías y se equipararon cuatro términos del español a su equivalente en inglés: aire, calidad, salud y gestión. Se conservaron las 49 palabras con frecuencia de dos o más. Dos palabras quedan enlazadas cuando aparecen en el mismo título. La red resultante tiene 260 aristas, cinco comunidades de Louvain y modularidad de 0,27. Esta red es una herramienta complementaria. Aplica la lógica de la co-ocurrencia para el mapeo bibliométrico (van Eck y Waltman, 2010). Se rotula palabras de título porque el informe no reporta las palabras clave de cada documento.

## 3.4 Reglas de corpus pequeño aplicadas a Lotka y a Bradford

El Paso 3.5 impone tres reglas condicionales a las leyes de Lotka (1926) y de Bradford (1934). La primera exige la etiqueta estimación exploratoria cuando el corpus tiene menos de 100 documentos. La segunda exige un intervalo de confianza de 95 % por remuestreo con 1.000 réplicas. La tercera ordena sustituir las leyes por estadística descriptiva cuando el corpus tiene menos de 45 documentos. El corpus tiene 42 documentos, de modo que las tres reglas aplican. La {T:tF06} resume cada regla, su condición y la forma en que se aplicó.

:::TABLA tF06 | Reglas condicionales de corpus pequeño y su aplicación
| Regla | Condición | Estado del corpus | Aplicación en este proyecto |
| --- | --- | --- | --- |
| R1 Advertencia | Menos de 100 documentos | 42 documentos | α y φ se rotulan estimación exploratoria |
| R2 Remuestreo | Bootstrap de 1.000 réplicas con intervalo de 95 % | Semilla 42; intervalos calculados | IC de α por máxima verosimilitud: 2,35 a 2,42; por mínimos cuadrados: 3,72 a 6,13; IC de φ: 1,00 a 2,50 |
| R2 Indeterminación | Si el IC de α cruza 2, la lectura es INDETERMINADA | Ningún IC de α cruza 2 | No se declara indeterminación por esta regla |
| R3 Sustitución | Menos de 45 documentos: sustituir por estadística descriptiva | 42 documentos | La estadística descriptiva es la lectura vigente; el ajuste se conserva como ilustración |
:::NOTA *Nota.* Elaboración propia con las reglas R1 a R3 del Paso 3.5 del metaprompt y cálculos propios (CALCULADO). Corpus de 42 documentos; año de corte 2026; semilla 42.

El proyecto presenta primero la estadística descriptiva y conserva el ajuste de α y de φ como ilustración del procedimiento. Los 213 autores se distribuyen en dos niveles de productividad. Un total de 204 autores firma un documento (95,8 %) y nueve firman dos. Ningún autor firma tres. Los 26 artículos se distribuyen en 19 revistas, y 15 revistas aportan un solo artículo (78,9 %). Tres revistas reúnen nueve artículos (34,6 %).

Las dos leyes cumplen funciones distintas. La ley de Lotka (1926) describe cuántos autores producen cada número de documentos. La ley de Bradford (1934) describe cómo se dispersan los documentos de un tema entre las revistas. Ambas se formularon para literaturas amplias y acumuladas durante años. Un corpus de 42 documentos seleccionado por tema no cumple esa condición. Aun así, el cálculo tiene valor descriptivo, porque cuantifica la dispersión que el proyecto necesita conocer para diseñar su vigilancia. El proyecto adopta la posición prudente: informa el valor, informa su intervalo y no lo interpreta como ley del campo.

El ajuste exploratorio de α da 2,38 por máxima verosimilitud y 4,50 por mínimos cuadrados. Los intervalos de 95 % van de 2,35 a 2,42 y de 3,72 a 6,13. La distancia entre ambos métodos muestra que la magnitud de α no es estable con dos niveles de productividad. Con dos puntos no hay grados de libertad. El parámetro φ de Bradford vale 2,67 entre las zonas 1 y 2 y 1,00 entre las zonas 2 y 3. Su intervalo de 95 % para la primera transición va de 1,00 a 2,50.

## 3.5 Resultados del Paso 3 y remisión al Capítulo 2

Las figuras y las tablas analíticas del Paso 3 ocupan el Capítulo 2, sección 2.2. Allí se desarrollan 14 subsecciones, desde el diagrama PRISMA hasta la síntesis de brechas. La {T:tF07} resume los indicadores principales y señala dónde se interpreta cada uno. Los indicadores se leen con las limitaciones de la sección 3.7. Para el detalle de cada análisis, véase el Capítulo 2, sección 2.2.

Las subsecciones 2.2.1 y 2.2.2 describen la selección y la producción temporal. Las subsecciones 2.2.3 y 2.2.4 tratan autores y fuentes con las leyes de Lotka y de Bradford. Las subsecciones 2.2.5 a 2.2.8 analizan la estructura temática con la red de co-ocurrencia, el acoplamiento bibliográfico, el mapa estratégico y la evolución por eras. Las subsecciones 2.2.9 a 2.2.11 usan los niveles de madurez para construir el gráfico de burbujas, el radar y el mapa de calor. Las subsecciones 2.2.12 y 2.2.13 cubren la geografía y la robustez. La subsección 2.2.14 consolida las brechas, y la sección 2.3 analiza las patentes y la libertad de operación.

:::TABLA tF07 | Indicadores principales del Paso 3 y ubicación de su análisis
| Indicador | Valor | Naturaleza | Ubicación |
| --- | --- | --- | --- |
| Corpus por tipo | 42 documentos: 26 artículos, 15 patentes, 1 informe | DOCUMENTADO | Capítulo 2, sección 2.2.1 |
| Producción anual | Pico de 17 documentos en 2026 (40,5 %); CAGR 2019 a 2026 de 35,8 % | CALCULADO | Capítulo 2, sección 2.2.2 |
| Concentración temporal | 35 de 42 (83,3 %) en 2022 a 2026 | CALCULADO | Capítulo 2, sección 2.2.2 |
| Autores | 213 autores; 95,8 % con un documento; α exploratorio de 2,38 | CALCULADO | Capítulo 2, sección 2.2.3 |
| Fuentes | 19 revistas; zonas de 3, 8 y 8 revistas; φ de 2,67 | CALCULADO | Capítulo 2, sección 2.2.4 |
| Red de co-palabras de texto completo | 584 nodos; 8 comunidades; modularidad de 0,311 | DOCUMENTADO | Capítulo 2, sección 2.2.5 |
| Red de palabras de título | 49 nodos; 5 comunidades; modularidad de 0,27 | CALCULADO | Capítulo 2, sección 2.2.5 |
| Acoplamiento bibliográfico | 102 pares; máximo de 12 referencias compartidas | DOCUMENTADO | Capítulo 2, sección 2.2.6 |
| Mapa estratégico | 4 comunidades motoras y 4 emergentes o marginales | DOCUMENTADO | Capítulo 2, sección 2.2.7 |
| Madurez | TRL 3,85; IRL 2,88; DRL 3,05 | DOCUMENTADO | Capítulo 2, sección 2.2.9 |
| Geografía | Colombia con 9 documentos, segundo lugar | DOCUMENTADO | Capítulo 2, sección 2.2.12 |
| Robustez | Media 3,93; desviación estándar 0,75; ningún documento sobre 6,1 | DOCUMENTADO | Capítulo 2, sección 2.2.13 |
| Patentes | 15 patentes; 10 solicitudes con Colombia designada: 7 con plazo vencido y 3 abiertas | DOCUMENTADO | Capítulo 2, sección 2.3 |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §3.1, §3.2, §6.2, §7.5 a §7.7, Anexo C y cálculos propios. Corpus de 42 documentos; año de corte 2026; semilla 42.

La tabla confirma que cada resultado del Paso 3 tiene una ubicación y una naturaleza declaradas. Los indicadores calculados dependen de la bibliografía y los heredados dependen del informe. Ningún indicador usa las cifras del Paso 3 del expediente E3. Las 13 figuras del protocolo y la línea de tiempo de patentes están en el Capítulo 2.

## 3.6 Síntesis ejecutiva del análisis bibliométrico

El corpus reúne 42 documentos de 1995 a 2026: 26 artículos, 15 patentes y un informe institucional. La producción pasa de dos documentos en 2019 a 17 en 2026, con una tasa de crecimiento anual compuesta de 35,8 %. El 83,3 % es de 2022 a 2026. El crecimiento describe la composición del corpus y no la producción del campo.

La estructura autoral es dispersa. Hay 213 autores y 204 firman un solo documento. Nueve autores aparecen en dos documentos y ninguno en más. El ajuste de Lotka es exploratorio, con α de 2,38 por máxima verosimilitud. La magnitud depende del método, y el corpus no permite identificar escuelas.

Los 26 artículos se publican en 19 revistas. Atmosphere, Science of the Total Environment y Sustainability reúnen nueve artículos. Las zonas de Bradford tienen tres, ocho y ocho revistas, con φ de 2,67 y 1,00. Las patentes se concentran en la OMPI con 11 documentos y en la OEP con cuatro.

La estructura temática tiene cinco grupos documentales y ocho comunidades de co-palabras. Los términos centrales son data, air, model y sensor. El término salud aparece en la comunidad de activos y motores por el vocabulario de dos patentes. La humedad queda en una comunidad emergente de 48 términos.

Colombia ocupa el segundo lugar con nueve documentos, después de Estados Unidos con 12. Solo ocho de los 26 artículos tienen coautoría internacional. Ninguna de las 15 patentes tiene solicitante colombiano y diez designan a Colombia. Ninguno de los 53 estudios de índices de calidad del aire y salud proviene de América Latina (Liao et al., 2026, p. 6).

La robustez media es 3,93 sobre 10, con desviación estándar de 0,75 y rango de 2,7 a 6,1. Ningún documento llega a 7. Los artículos promedian 4,34 y las patentes 3,27.

Las brechas se instancian en cuatro categorías y una emergente. El TRL medio de 3,85 supera al nivel de integración (IRL) de 2,88 en 0,98 niveles. La brecha entre TRL y nivel de preparación del negocio llega a 2,33 niveles en nueve documentos. La brecha emergente es la producción sin verificación, porque ninguna patente valida con verdad de referencia.

Las implicaciones para el proyecto son tres. La calibración colocalizada ocupa un vacío documentado: el 90,8 % de las estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13). El Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) es el único sistema de TRL 9 (Ruiz-Carrascal et al., 2026). La adopción institucional requiere una medición propia desde el tramo 1. La libertad de operación exige consultar a la SIC por diez solicitudes del Tratado de Cooperación en materia de Patentes (PCT). Esas solicitudes designan a Colombia y tres siguen abiertas hasta 2027.

## 3.7 Limitaciones del Paso 3

El Paso 3 se apoya en un corpus intencional de 42 documentos. Las escalas de madurez y de robustez son ordinales y las asignó el analista del informe (F-INF §3.3, p. 24). Los intervalos de confianza describen la variación del remuestreo y no una población de documentos. Esa lectura restringe cualquier generalización al campo.

El proyecto no consultó bases bibliométricas. El índice h, el factor de impacto, el cuartil y el número de citas quedan vacíos (VACIO; NO_VERIFICADO). La co-citación de autores no es calculable sin una base de citas. La geografía se mide por documento y no por autor. Cerrar esas lagunas requiere acceso a bases comerciales [DATO_USUARIO: acceso institucional a Scopus, Web of Science y Lens.org]. Cada limitación se repite en la sección del Capítulo 2 donde afecta la lectura.
