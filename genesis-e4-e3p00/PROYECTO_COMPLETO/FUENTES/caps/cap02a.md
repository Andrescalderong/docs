%% PREFIJO: 2
# Capítulo 2. Estado del arte y vigilancia tecnológica

## 2.1 Metodología de vigilancia tecnológica

La vigilancia tecnológica es la observación sistemática y repetible de la literatura científica y de las solicitudes de patente para decidir con evidencia vigente. El proyecto la usa con dos fines. El primero es establecer qué se sabe sobre la calibración y la corrección de sensores ópticos de material particulado fino (PM2,5) y grueso (PM10). El segundo es detectar restricciones de libertad de operación antes de comprar equipos. El esquema Elementos de Informe Preferidos para Revisiones Sistemáticas y Metaanálisis (PRISMA) ordena la transparencia de la selección (Page et al., 2021). El mapeo científico ordena el análisis posterior de la producción y de las redes temáticas (Aria y Cuccurullo, 2017).

### 2.1.1 Origen del corpus y ecuaciones de búsqueda

Este capítulo no parte de una búsqueda propia. Parte del informe de vigilancia tecnológica y bibliometría consolidado el 30 de septiembre de 2026 (F-INF). El informe analizó 42 documentos: 26 artículos, 15 patentes y un informe institucional (F-INF §3.1, p. 19). Los documentos llegaron como archivos aportados al análisis. El informe no registra el criterio de selección (F-INF §10.1, p. 124). Además, califica el corpus de muestra intencional y no aleatoria (F-INF §3.3, p. 24). Todo resultado de este capítulo describe el corpus y no la literatura completa del campo.

Dos posiciones orientan la selección de documentos. La primera exige búsquedas reproducibles con registro de cada exclusión (Page et al., 2021). La segunda acepta un corpus curado cuando el propósito es orientar una decisión y no estimar la producción de un campo. El informe adopta la segunda posición. Este capítulo la mantiene, declara su límite y propone cerrar la distancia con la primera mediante las ecuaciones de la {T:t01}.

La {T:t01} presenta tres ecuaciones con operadores booleanos explícitos. Las ecuaciones E1 y E2 provienen del Anexo D del informe. Allí el analista las propone como supuesto y advierte que deben probarse y ajustarse en el buscador (F-INF Anexo D, p. 222). Ninguna se ejecutó en bases comerciales en esta corrida. Por eso el conteo por base figura como NO_VERIFICADO. La ecuación E3 es una propuesta de este proyecto. Cubre el contexto de remoción de escombros posterremoto en Caldas, Cundinamarca y Valle del Cauca (SUPUESTO).

:::TABLA t01 | Ecuaciones de búsqueda por base de datos con resultados
| Ecuación | Expresión booleana | Campo de búsqueda | Bases previstas | Resultado por base | Naturaleza |
| --- | --- | --- | --- | --- | --- |
| E1 | («calidad del aire» O «material particulado» O «PM2,5» O «air quality») Y (sensor O monitor* O calibraci* O calibrat*) | Título y resumen | Scopus; Web of Science; PubMed; IEEE Xplore; Google Scholar | NO_VERIFICADO | SUPUESTO del analista del informe (Anexo D) |
| E2 | (F24F O G01N33 O B01D46 O B01D53 O G08B21/12) Y (CO2 O PM2,5 O «calidad del aire» O «air quality») | Clasificación de patentes | Lens.org; Espacenet; USPTO; buscador de la SIC | NO_VERIFICADO | SUPUESTO del analista del informe (Anexo D) |
| E3 | («escombros» O «demolición» O debris O rubble) Y (sismo O terremoto O earthquake) Y (PM2,5 O PM10 O «material particulado» O «particulate matter») | Título y resumen | Scopus; Web of Science; Google Scholar; Lens.org | NO_VERIFICADO | PROPUESTO por esta corrida |
:::NOTA *Nota.* Elaboración propia con datos de F-INF Anexo D (p. 222). O = unión; Y = intersección; el asterisco indica truncamiento. SIC = Superintendencia de Industria y Comercio; USPTO = Oficina de Patentes y Marcas de Estados Unidos. Las bases proceden de la especificación del capítulo. Ninguna ecuación se ejecutó en esta corrida; el conteo por base es NO_VERIFICADO.

La primera ecuación busca tecnologías por su descripción y la segunda por su clase. La unión de ambas reduce el riesgo de omitir solicitudes con títulos distintos (F-INF Anexo D, p. 222). La tercera agrega el contexto de escombros, ausente de las dos primeras. El procedimiento de la Superintendencia de Industria y Comercio (SIC) usa también dos ecuaciones, una de palabras clave y otra de clases (SIC, 2026, pp. 4-9). Un revisor ejecutará las tres ecuaciones y registrará el conteo por base. Se requiere acceso a bases comerciales [DATO_USUARIO: acceso institucional a Scopus, Web of Science y Lens.org].

### 2.1.2 Bases, período y criterios

Las bases previstas son Scopus, Web of Science, PubMed, IEEE Xplore y Google Scholar para la literatura. Para las patentes se prevén Lens.org, Espacenet, la Oficina de Patentes y Marcas de Estados Unidos (USPTO) y el buscador de la SIC. Esa lista procede de la especificación del capítulo y es PROPUESTO. No se consultó ninguna base en esta corrida.

El corpus abarca publicaciones de 1995 a 2026. La especificación recomienda una ventana de cinco a diez años según el campo. En el corpus, 35 de 42 documentos (83,3 %) son de los últimos cinco años. Otros seis son de los cinco años previos, y uno es de 1995. El proyecto adopta la ventana de 2017 a 2026 para la vigilancia futura (PROPUESTO). Conserva la patente de 1995 porque su vigencia ya venció, lo que la vuelve relevante para la libertad de operación (Reintjes et al., 1995; F-INF §5.7, p. 55).

La {T:t02} separa los criterios que describen el corpus actual de los que se proponen para la vigilancia futura. El informe documenta el ámbito temático y la lectura completa de cada documento. No documenta criterios de exclusión ni documentos excluidos (F-INF §1.2, p. 9).

:::TABLA t02 | Criterios de inclusión y exclusión del corpus
| Criterio | Tipo | Definición | Naturaleza | Aplicación al corpus de 42 documentos |
| --- | --- | --- | --- | --- |
| I1 | Inclusión | Ámbito: calidad del aire, sensores, pronóstico, exposición, salud y tecnología patentada | DOCUMENTADO (F-INF, información del documento) | Cumplido por los 42 documentos según el informe |
| I2 | Inclusión | Texto completo leído por el analista | DOCUMENTADO (F-INF §1.2, p. 9) | 42 de 42 |
| I3 | Inclusión | Tipo documental: artículo, patente o solicitud, informe institucional | DOCUMENTADO (F-INF §3.1, p. 19) | 26 artículos, 15 patentes y 1 informe |
| I4 | Inclusión | Publicación anterior al corte del informe (30 de septiembre de 2026) | DOCUMENTADO (F-INF, información del documento) | 42 de 42 |
| I5 | Inclusión | Idioma: inglés o español | DOCUMENTADO (F-INF §7.1, p. 74) | 2 documentos en español; el resto en inglés (INFERIDO) |
| E1 | Exclusión | Documento sin texto completo disponible | PROPUESTO | Sin exclusiones registradas |
| E2 | Exclusión | Documento duplicado por DOI, número o título | PROPUESTO | Sin duplicados en 42 identificadores |
| E3 | Exclusión | Documento ajeno a la calidad del aire y a la medición de partículas | PROPUESTO | Sin registro de exclusiones |
| E4 | Exclusión | Publicación en revista de práctica predatoria | PROPUESTO | NO_VERIFICADO: no se evaluó |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §1.2 (p. 9), §3.1 (p. 19) y §7.1 (p. 74). DOI = identificador de objeto digital. Naturaleza: DOCUMENTADO para los criterios de inclusión que el informe describe y PROPUESTO para los demás.

Cinco criterios de inclusión se documentan y cuatro de exclusión se proponen. La asimetría confirma que el corpus se armó por inclusión y no por exclusión. La vigilancia futura aplicará los nueve criterios y registrará cada exclusión. Así el diagrama de la sección 2.2.1 podrá completarse con números reales.

## 2.2 Análisis cienciométrico

El análisis cienciométrico cuantifica la producción, la autoría, las fuentes y la estructura temática del corpus. Sigue el protocolo de 13 figuras. Cada figura declara el tamaño del corpus, el año de corte (2026) y la semilla (42). Los cálculos se hacen sobre la bibliografía del informe cuando es posible. Los resultados de texto completo se toman del informe con su sección y página. Las reglas de corpus pequeño se aplican en cada subsección.

### 2.2.1 Diagrama PRISMA y selección sistemática

La selección sistemática exige que cada exclusión tenga un registro. El enunciado PRISMA 2020 organiza ese registro en cuatro etapas y pide el número de documentos en cada una (Page et al., 2021). La tasa de selección divide los documentos incluidos entre los identificados y mide la severidad del filtro.

Dos lecturas de PRISMA conviven. La lectura estricta lo reserva para revisiones sistemáticas con búsquedas reproducibles. La lectura flexible lo usa como lista de verificación de transparencia, también en estudios de vigilancia. Este capítulo adopta la lectura flexible. Su propósito es orientar una decisión de proyecto y no estimar efectos.

La {T:t03} y la {F:prisma} presentan el flujo con los números reales del corpus. Solo la etapa de inclusión está documentada, con 42 documentos. Hay 26 artículos (61,9 %), 15 patentes (35,7 %) y un informe institucional (2,4 %). Las etapas de identificación y cribado carecen de registro. La tasa de selección no es calculable. Los criterios aplicados figuran en la {T:t02}.

:::TABLA t03 | Flujo PRISMA simplificado con números reales del corpus
| Etapa | Descripción | Documentos | Artículos | Patentes | Informes | Naturaleza y verificación |
| --- | --- | --- | --- | --- | --- | --- |
| Identificación | Registros identificados en bases de datos | Sin dato | Sin dato | Sin dato | Sin dato | VACIO; NO_VERIFICADO |
| Cribado | Registros tras eliminar duplicados | Sin dato | Sin dato | Sin dato | Sin dato | VACIO; NO_VERIFICADO |
| Elegibilidad | Documentos evaluados a texto completo | 42 | 26 | 15 | 1 | DOCUMENTADO (F-INF §1.2, p. 9) |
| Exclusión a texto completo | Documentos excluidos tras la lectura | Sin registro | Sin registro | Sin registro | Sin registro | VACIO; NO_VERIFICADO |
| Inclusión | Documentos incluidos en el corpus | 42 | 26 | 15 | 1 | DOCUMENTADO (F-INF §3.1, p. 19) |
| Tasa de selección | Incluidos sobre identificados | No calculable | No calculable | No calculable | No calculable | NO_CALCULABLE |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §1.2 (p. 9), §3.1 (p. 19) y §10.1 (p. 124). Porcentajes sobre 42 documentos. Naturaleza: DOCUMENTADO para las etapas con dato y VACIO para las demás.

:::FIGURA prisma | Diagrama PRISMA de flujo del corpus de 42 documentos | Nota. Elaboración propia con matplotlib a partir de F-INF §1.2 (p. 9), §3.1 (p. 19) y §10.1 (p. 124). Las etapas de identificación y cribado carecen de registro y se marcan NO_VERIFICADO. Corpus de 42 documentos; año de corte 2026; semilla 42.

La asimetría tiene una consecuencia metodológica. El proyecto no afirma exhaustividad. Cada capítulo que use este corpus lo describe como una muestra intencional de 42 documentos. La vigilancia futura completará el diagrama con las ecuaciones de la sección 2.1, y el plan de cierre figura en el Paso 3, sección 3.2.

### 2.2.2 Producción científica temporal

La producción temporal mide cuántos documentos entran al corpus por año de publicación. El corpus pasa de dos documentos en 2019 a nueve en 2025 y 17 en 2026 (F-INF §4.3, p. 34). El pico ocurre en 2026, con 17 documentos y 40,5 % del corpus. Los últimos cinco años concentran 35 de 42 documentos (83,3 %).

La tasa de crecimiento anual compuesta (CAGR) resume el cambio entre dos años. Se calcula como el valor final dividido por el inicial, elevado a uno sobre el número de años, menos uno. Su valor depende de la ventana elegida. La {T:t04} presenta la producción anual con la era de cada año. La {F:produccion} la representa con el acumulado.

:::TABLA t04 | Producción anual de documentos y era histórica
| Año | Artículos | Patentes | Informes | Total | Acumulado | Porcentaje del corpus | Era |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1995 | 0 | 1 | 0 | 1 | 1 | 2,4 % | Fundacional |
| 2019 | 0 | 2 | 0 | 2 | 3 | 4,8 % | Fundacional |
| 2020 | 0 | 1 | 0 | 1 | 4 | 2,4 % | Fundacional |
| 2021 | 2 | 1 | 0 | 3 | 7 | 7,1 % | Fundacional |
| 2022 | 1 | 1 | 0 | 2 | 9 | 4,8 % | Fundacional |
| 2023 | 1 | 1 | 0 | 2 | 11 | 4,8 % | Fundacional |
| 2024 | 2 | 3 | 0 | 5 | 16 | 11,9 % | Crecimiento |
| 2025 | 6 | 3 | 0 | 9 | 25 | 21,4 % | Crecimiento |
| 2026 | 14 | 2 | 1 | 17 | 42 | 40,5 % | Aceleración |
| Total | 26 | 15 | 1 | 42 | 42 | 100,0 % | Tres eras |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §4.3 (p. 34) y §13.2 (p. 212). Años sin documentos entre 1996 y 2018 omitidos. Eras por segmentación óptima en tres tramos contiguos de la serie 1995 a 2026 (mínima suma de cuadrados). Naturaleza: CALCULADO.

La ventana principal es 2019 a 2026, la única serie continua sin años vacíos, y da un CAGR de 35,8 %. Las ventanas de 2021 a 2026 y de 2024 a 2026 dan 41,5 % y 84,4 %. La dispersión de los tres valores muestra que el CAGR describe la ventana elegida y no un ritmo estable. La segmentación óptima identifica tres eras. La era fundacional va de 1995 a 2023 y tiene 11 documentos. La de crecimiento va de 2024 a 2025 y tiene 14. La de aceleración es 2026 y tiene 17. El nombre madurez no se usa para la última era, porque el informe muestra madurez baja y sin tendencia sostenida (F-INF §4.3, p. 34).

:::FIGURA produccion | Producción temporal de documentos con acumulado y eras históricas | Nota. Elaboración propia con matplotlib a partir de F-INF §4.3 (p. 34) y §13.2. Barras apiladas por tipo documental; línea discontinua con el acumulado; eras por segmentación óptima en tres tramos (SSE de 26,8). Corpus de 42 documentos; año de corte 2026; semilla 42.

Dos posiciones explican el aumento. La primera sostiene que un campo joven madurará con el tiempo. La segunda sostiene que la norma de cada género documental no exige verificación externa. El informe contrasta ambas con tres hipótesis. El año no se asocia con la robustez (ρ de 0,26; p de 0,11). Su coeficiente es de menos 0,03 puntos por año (p de 0,49). La evidencia favorece la segunda posición (F-INF §10.2, p. 129).

Los puntos de inflexión coinciden con hechos de contexto que el informe documenta. Las guías de la Organización Mundial de la Salud (OMS) de 2021 redefinieron los umbrales de referencia (de Moura et al., 2025; OMS, 2021). El Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) integra la red de calidad del aire de Medellín. En 2023 el Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM) acreditó esa red. Ese año el informe nacional registró 23 sistemas y 209 estaciones. Ambos hechos marcan el paso de redes por contrato a un sistema acreditado (Ruiz-Carrascal et al., 2026; Murad Pedraza et al., 2026). El aumento de 2026 combina revisiones, agendas y propuestas nacionales. Esa concentración en el último año obliga a tratar el corpus como un retrato reciente. El proyecto no extrapola la producción. Actualizará la vigilancia cada seis meses y recalculará la ventana (PROPUESTO).

### 2.2.3 Autores y productividad: ley de Lotka

La productividad de autores cuenta cuántos documentos firma cada persona. El corpus tiene 213 autores únicos y 5,29 autores por documento (F-INF §7.6, p. 93). Solo nueve autores figuran en más de un documento. Ninguno figura en más de dos.

La ley de Lotka (1926) postula que el número de autores con x documentos decrece como x elevado a menos α, con α cercano a 2. Un α menor que 2 indica un campo concentrado en pocos autores prolíficos. Un α mayor que 2 indica dispersión. El ajuste se hace sobre la distribución de autores por número de documentos. La {T:t05} lista los nueve autores con más de un documento. Los autores más citados no se identifican, porque el índice h y las citas no se consultaron (VACIO).

:::TABLA t05 | Autores con más de un documento: productividad, era y vínculo
| Autor | Documentos en el corpus | Documentos | Eras | Vínculo declarado en el informe | h-index y citas |
| --- | --- | --- | --- | --- | --- |
| Chiaramonte, G. J. | 2 | Abernathy et al. (2019); Hurst et al. (2024) | Fundacional y Crecimiento | General Electric | VACIO |
| Horn, D. | 2 | Abernathy et al. (2019); Hurst et al. (2024) | Fundacional y Crecimiento | General Electric | VACIO |
| Levin, S. R. | 2 | Abernathy et al. (2019); Hurst et al. (2024) | Fundacional y Crecimiento | General Electric | VACIO |
| Buffarini, R. | 2 | De Moura et al. (2025); Tavella et al. (2026) | Crecimiento y Aceleración | Grupo brasileño | VACIO |
| Carvalho, H. | 2 | De Moura et al. (2025); Tavella et al. (2026) | Crecimiento y Aceleración | Grupo brasileño | VACIO |
| Tavella, R. A. | 2 | Miraglia et al. (2025); Tavella et al. (2026) | Crecimiento y Aceleración | Grupo brasileño | VACIO |
| da Silva Júnior, F. M. R. | 2 | De Moura et al. (2025); Tavella et al. (2026) | Crecimiento y Aceleración | Grupo brasileño | VACIO |
| de Moura, F. R. | 2 | De Moura et al. (2025); Tavella et al. (2026) | Crecimiento y Aceleración | Grupo brasileño | VACIO |
| Zuluaga, M. D. | 2 | Ayala-Parra et al. (2026); Ruiz-Carrascal et al. (2026) | Aceleración | SIATA | VACIO |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §7.6 (p. 93) y §13.2 (p. 212). Autor definido por apellido y primera inicial. El índice h y las citas no se consultaron (VACIO; NO_VERIFICADO). Naturaleza: CALCULADO. Corpus de 42 documentos; año de corte 2026.

Tres grupos explican los nueve casos. Tres corresponden a inventores de General Electric, cinco al grupo brasileño y uno a SIATA (F-INF §7.6, p. 93). Ningún grupo domina dos eras completas. Los inventores de General Electric aparecen en las eras fundacional y de crecimiento. Los otros dos grupos aparecen en crecimiento y aceleración, o solo en aceleración. El corpus no muestra una escuela con liderazgo sostenido.

La {T:t06} y la {F:lotka} presentan el ajuste. Con la regla de corpus pequeño, la estadística descriptiva es la lectura vigente y el ajuste es exploratorio.

:::TABLA t06 | Parámetros de la ley de Lotka en el corpus
| Parámetro | Valor observado | Valor de referencia | Interpretación |
| --- | --- | --- | --- |
| α por máxima verosimilitud | 2,38 (IC de 95 %: 2,35 a 2,42) | 2,00 (Lotka estándar) | α mayor que 2: dispersión; estimación exploratoria |
| α por mínimos cuadrados | 4,50 (IC de 95 %: 3,72 a 6,13) | 2,00 | Dos niveles de productividad y cero grados de libertad |
| Corpus y autores | 42 documentos; 213 autores | 100 o más documentos para caracterización definitiva | N menor que 45: la regla R3 sustituye la ley por estadística descriptiva |
| Autores con un documento | 204 (95,8 %) | Más de 85 %: campo emergente | Supera el umbral que el protocolo asocia con campo emergente |
| Autores con dos documentos | 9 (4,2 %) | No aplica | Máximo observado |
| Autores más productivos | Nueve autores empatados con dos documentos | No aplica | Sin líderes por productividad |
:::NOTA *Nota.* Elaboración propia. Método: máxima verosimilitud con aproximación continua y x mínimo de 1; mínimos cuadrados sobre la recta log-log; intervalos por bootstrap de 1.000 réplicas con semilla 42. Estimación exploratoria. Naturaleza: CALCULADO. Corpus de 42 documentos; año de corte 2026.

:::FIGURA lotka | Distribución de Lotka de los 213 autores con ajustes exploratorios | Nota. Elaboración propia con matplotlib. Escala logarítmica en ambos ejes; n de 213 autores de 41 documentos con autoría individual. Máxima verosimilitud con x mínimo de 1 y mínimos cuadrados log-log; bootstrap de 1.000 réplicas con semilla 42. Estimación exploratoria (N menor que 45); año de corte 2026.

Dos lecturas compiten. La primera interpreta α mayor que 2 como un campo disperso, sin núcleo de autores. La segunda advierte que, con N menor que 45 y dos niveles de productividad, el exponente no se identifica. Los dos métodos confirman la segunda lectura, porque dan 2,38 y 4,50. El proyecto adopta una conclusión limitada. La autoría es dispersa, con 95,8 % de autores con un documento, y el corpus no permite inferir una ley de productividad.

La decisión metodológica es doble. La vigilancia no se apoyará en seguir autores líderes, porque no existen en este corpus. El proyecto documentará su protocolo de colocalización en forma replicable, para que otros grupos lo evalúen.

### 2.2.4 Fuentes y dispersión: ley de Bradford

La distribución de fuentes cuenta cuántos artículos publica cada revista. Los 26 artículos del corpus aparecen en 19 revistas. Atmosphere, Science of the Total Environment y Sustainability publican tres artículos cada una. Urban Climate publica dos, y las 15 revistas restantes publican uno.

La ley de Bradford (1934) ordena las revistas por productividad y las reparte en zonas con igual número de artículos. La zona núcleo concentra pocas revistas. Las zonas siguientes necesitan multiplicar ese número por un factor φ para reunir los mismos artículos. Un φ cercano a 3 describe un campo bien estructurado, según el protocolo del proyecto. La {T:t07} lista las 19 revistas con su zona. Las columnas de cuartil, factor de impacto y CiteScore quedan vacías. No se consultaron bases de indicadores [DATO_USUARIO: cuartiles SJR, factor de impacto y CiteScore de las revistas del núcleo].

:::TABLA t07 | Revistas del corpus por número de artículos y zona de Bradford
| Posición | Revista | Artículos | Zona de Bradford | Cuartil SJR, JIF y CiteScore |
| --- | --- | --- | --- | --- |
| 1 | Atmosphere | 3 | Zona 1 | VACIO |
| 2 | Science of the Total Environment | 3 | Zona 1 | VACIO |
| 3 | Sustainability | 3 | Zona 1 | VACIO |
| 4 | Urban Climate | 2 | Zona 2 | VACIO |
| 5 | Air Quality, Atmosphere y Health | 1 | Zona 2 | VACIO |
| 6 | Atmospheric Research | 1 | Zona 2 | VACIO |
| 7 | CLEAN -- Soil, Air, Water | 1 | Zona 2 | VACIO |
| 8 | Climate Services | 1 | Zona 2 | VACIO |
| 9 | Environment Systems and Decisions | 1 | Zona 2 | VACIO |
| 10 | Environmental Geochemistry and Health | 1 | Zona 2 | VACIO |
| 11 | Environmental Health | 1 | Zona 2 | VACIO |
| 12 | Geocarto International | 1 | Zona 3 | VACIO |
| 13 | Hygiene and Environmental Health Advances | 1 | Zona 3 | VACIO |
| 14 | International Journal of Environmental Research and Public Health | 1 | Zona 3 | VACIO |
| 15 | International Journal of Environmental Science and Technology | 1 | Zona 3 | VACIO |
| 16 | Journal of South American Earth Sciences | 1 | Zona 3 | VACIO |
| 17 | Luna Azul | 1 | Zona 3 | VACIO |
| 18 | Sensors | 1 | Zona 3 | VACIO |
| 19 | Sustainable Cities and Society | 1 | Zona 3 | VACIO |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §13.2 (p. 212). Desempate alfabético entre revistas con un artículo. Los indicadores de revista son VACIO y NO_VERIFICADO. Naturaleza: CALCULADO. Corpus de 26 artículos; año de corte 2026.

Las zonas por tercios de artículos reúnen tres, ocho y ocho revistas. La {T:t08} y la {F:bradford} presentan las zonas y el multiplicador entre ellas.

:::TABLA t08 | Zonas de Bradford, porcentajes y multiplicador φ
| Zona | Revistas | Artículos | Porcentaje de artículos | Multiplicador entre zonas |
| --- | --- | --- | --- | --- |
| Zona 1 (núcleo) | 3 | 9 | 34,6 % | No aplica |
| Zona 2 (general) | 8 | 9 | 34,6 % | 2,67 (8 sobre 3) |
| Zona 3 (periférica) | 8 | 8 | 30,8 % | 1,00 (8 sobre 8) |
| Total | 19 | 26 | 100,0 % | Intervalo de 95 % del primer multiplicador: 1,00 a 2,50 |
:::NOTA *Nota.* Elaboración propia. Zonas por tercios de 26 artículos (8,67 por zona). Intervalo de 95 % por bootstrap de 1.000 réplicas con semilla 42 sobre los artículos; el valor observado queda fuera del intervalo por los empates. Estimación exploratoria. Naturaleza: CALCULADO.

:::FIGURA bradford | Revistas del corpus por zona de Bradford y número de artículos | Nota. Elaboración propia con matplotlib. Barras horizontales por revista; zonas por tercios de artículos; multiplicador φ con intervalo de 95 % por bootstrap (1.000 réplicas, semilla 42). Estimación exploratoria (N menor que 45); corpus de 26 artículos de 42 documentos; año de corte 2026.

El multiplicador entre las zonas 1 y 2 es 2,67, cercano al valor de 3 que el protocolo asocia con estructura. El multiplicador entre las zonas 2 y 3 es 1,00, porque ocho revistas aportan un artículo cada una en ambas zonas. Bradford exige un multiplicador estable, y aquí no lo es. El intervalo de 95 % del primero va de 1,00 a 2,50 y no contiene el valor observado. Una lectura sostiene que la literatura se dispersa entre revistas generalistas de ambiente y sostenibilidad. La otra sostiene que un corpus armado por tema no permite estimar dispersión. El proyecto adopta la segunda.

La implicación práctica es una lista de monitoreo continuo. Las tres revistas del núcleo y Urban Climate forman la lista mínima (PROPUESTO). Climate Services y Luna Azul se añaden por su vínculo con Colombia. Publican a Ruiz-Carrascal et al. (2026) y a Murad Pedraza et al. (2026), en ese orden. Para patentes, dos oficinas concentran los 15 documentos del corpus. La Organización Mundial de la Propiedad Intelectual (OMPI) publica 11 y la Oficina Europea de Patentes (OEP) publica cuatro. El buscador de la SIC completa la lista para Colombia.


### 2.2.5 Red de co-ocurrencia de palabras clave

La red de co-ocurrencia une términos que aparecen juntos y revela los temas que organizan un campo. El informe construyó una red con los 600 términos más frecuentes del texto completo. Usó una ventana de ocho términos y un peso mínimo de 30 co-ocurrencias. El resultado es una red de 584 nodos y 5.300 aristas (F-INF §7.5, p. 88). El análisis de co-palabras identifica temas por la asociación entre términos (Callon et al., 1991). Los programas de mapeo agrupan los términos en clusters según su co-ocurrencia (van Eck y Waltman, 2010).

El informe detectó comunidades con tres algoritmos. Louvain produjo ocho comunidades con modularidad de 0,311. La propagación de etiquetas produjo dos comunidades con modularidad de 0,002, y el informe la descarta por inadecuada en una red densa. Girvan-Newman sobre los 70 términos de mayor grado produjo 22 grupos con modularidad de 0,013 y quedó degenerado (F-INF §7.5, p. 88). La {T:t09} reproduce los 12 términos de mayor grado ponderado y su comunidad de Louvain.

:::TABLA t09 | Términos principales de la red de co-palabras de texto completo
| Término | Grado | Grado ponderado | Intermediación | Comunidad de Louvain | Lectura |
| --- | --- | --- | --- | --- | --- |
| data | 393 | 39.987 | 0,5869 | 2 | Centro de la red y puente entre comunidades |
| air | 371 | 34.274 | 0,4463 | 1 | Núcleo de la comunidad de aire y contaminantes |
| model | 287 | 26.811 | 0,2304 | 3 | Núcleo de la comunidad de modelo y predicción |
| sensor | 226 | 22.377 | 0,1568 | 2 | Une datos, dispositivos y control |
| health | 163 | 15.795 | 0,0931 | 4 | Polisémico: estado de activos y salud humana |
| asset | 104 | 14.943 | 0,1517 | 4 | Vocabulario de patentes de turbinas |
| quality | 167 | 13.571 | 0,0000 | 1 | Acompaña a air sin actuar como puente |
| time | 150 | 11.222 | 0,0215 | 3 | Series temporales y pronóstico |
| engine | 113 | 10.539 | 0,0420 | 4 | Vocabulario de patentes de motores |
| value | 130 | 10.084 | 0,0294 | 3 | Valores de modelos y de índices |
| environment | 94 | 9.338 | 0,0412 | 2 | Contexto de datos y sensores |
| pollutant | 123 | 9.056 | 0,0300 | 1 | Contaminantes del aire |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §7.5, Tabla 36 (p. 88). Red de 584 nodos y 5.300 aristas; Louvain con 8 comunidades y modularidad de 0,311. Naturaleza: DOCUMENTADO; la columna de lectura es INFERIDO. Corpus de 42 documentos; año de corte 2026.

Los términos data, air, model y sensor concentran el grado ponderado. La intermediación de data, de 0,5869, y la de air, de 0,4463, indican que ambos términos conectan comunidades. El término health ocupa el quinto lugar, pero pertenece a la comunidad de activos y motores. Dos patentes de General Electric usan salud para describir el estado de una turbina (F-INF §10.3, p. 132). Por eso la centralidad de health no prueba que el corpus mida salud humana.

El proyecto calcula además una red propia con palabras de título. La rotula así porque el informe no reporta palabras clave por documento. La {T:t10} y la {F:coocurrencia} presentan la red de 49 palabras con frecuencia de dos o más, 260 aristas y cinco comunidades. Su modularidad es de 0,27.

:::TABLA t10 | Palabras de título principales: frecuencia, comunidad y centralidad
| Palabra de título | Frecuencia en títulos | Comunidad | Grado | Intermediación | Lectura |
| --- | --- | --- | --- | --- | --- |
| air | 22 | C1 | 39 | 0,249 | Centro de la red: se enlaza con 39 de las otras 48 palabras |
| quality | 13 | C1 | 32 | 0,126 | Acompaña a air; núcleo de la comunidad de pronóstico |
| pollution | 9 | C3 | 22 | 0,058 | Núcleo de la comunidad de contaminación, clima y patrimonio |
| health | 8 | C2 | 16 | 0,095 | Polisémica: designa salud humana y estado de activos industriales |
| monitoring | 8 | C2 | 17 | 0,080 | Une salud, gestión y edificios |
| management | 5 | C2 | 11 | 0,021 | Aparece solo en la era de aceleración |
| learning | 4 | C1 | 15 | 0,009 | Pronóstico con aprendizaje automático |
| urban | 4 | C1 | 18 | 0,023 | Estudios urbanos de pronóstico y de patrimonio |
| machine | 4 | C1 | 15 | 0,016 | Pronóstico con aprendizaje automático |
| forecasting | 4 | C5 | 18 | 0,032 | Puente hacia meteorología y gemelo digital |
| sustainable | 3 | C1 | 13 | 0,008 | Revisiones y estudios de desarrollo sostenible |
| review | 3 | C1 | 11 | 0,004 | Revisiones sistemáticas y comprensivas |
| application | 3 | C4 | 15 | 0,049 | Enlaza sensores, partículas y teledetección |
| climate | 3 | C3 | 11 | 0,009 | Clima, patrimonio y Brasil |
:::NOTA *Nota.* Elaboración propia con los títulos de los 42 documentos. Palabras vacías eliminadas; cuatro términos del español equiparados al inglés (aire, calidad, salud y gestión). Grado: palabras enlazadas por co-ocurrencia en el mismo título; intermediación sin pesos. Louvain con semilla 42. Naturaleza: CALCULADO; la columna de lectura es INFERIDO.

:::FIGURA coocurrencia | Red de co-ocurrencia de palabras de título con cinco comunidades | Nota. Elaboración propia con networkx y matplotlib. 49 nodos con frecuencia mínima de 2 en los títulos de 42 documentos; 260 aristas; comunidades de Louvain con modularidad de 0,27. Disposición por comunidades con semilla 42; año de corte 2026. Son palabras de título y no palabras clave.

La modularidad de 0,27 es baja, de modo que las comunidades son tendencias y no fronteras. Air y quality se enlazan con 39 y 32 de las otras 48 palabras. La comunidad C1 agrupa el pronóstico con aprendizaje automático. La C2 agrupa salud, monitoreo y gestión, e incluye engine y turbine por las patentes de activos. La C3 agrupa contaminación, clima y patrimonio. La C4 agrupa partículas, sensores y exposición. La C5 agrupa meteorología, ciudad y gemelo digital.

Dos posiciones evalúan estas redes. Una confía en la red de texto completo, porque usa más información por documento. La otra confía en la red de títulos, porque los títulos resumen el tema que declaran los autores. Ambas coinciden en que aire, calidad y monitoreo organizan el campo. Divergen en la salud, que la red de títulos asocia a la gestión y la de texto completo a los activos.

La consecuencia para el proyecto es doble. Primero, la humedad pertenece a la comunidad 5 del texto completo, de 48 términos, clasificada como emergente o en declive (F-INF §7.5, p. 88). El análisis causal del proyecto la sitúa en el centro del problema. Segundo, los términos calibración y colocalización no figuran entre los 12 de mayor grado. Esa ausencia respalda la formulación del problema. La calibración colocalizada ocupa la periferia del corpus.

### 2.2.6 Red de co-citación y acoplamiento bibliográfico

La base intelectual de un campo se estudia con dos medidas complementarias. El acoplamiento bibliográfico une dos documentos que comparten referencias (Kessler, 1963). La co-citación une dos documentos que otros citan juntos (Small, 1973). El corpus permite calcular solo la primera medida.

El informe comparó las listas de referencias de los 26 artículos con fragmentos de título de siete palabras. Excluyó los fragmentos presentes en cinco o más documentos. Detectó 102 pares con referencias compartidas, casi todos con una o dos (F-INF §7.7, p. 95). La {T:t11} lista los 12 pares de mayor acoplamiento. La {F:cocitacion} los representa por era de publicación.

:::TABLA t11 | Pares de artículos con mayor acoplamiento bibliográfico
| Documento A | Documento B | Referencias compartidas | Eras de A y B | Lectura |
| --- | --- | --- | --- | --- |
| De Moura 2025 | Tavella 2026 | 12 | crecimiento y aceleración | Grupo de autores común |
| Nelson 2026 | Essamlali 2024 | 6 | crecimiento y aceleración | Revisiones de aprendizaje automático |
| De Moura 2025 | Rodríguez-Villamizar 2022 | 6 | fundacional y crecimiento | Carga de enfermedad y exposición |
| De Moura 2025 | Kumar 2026 | 5 | crecimiento y aceleración | Exposición y materia particulada |
| Botezat 2025 | Tavella 2026 | 4 | crecimiento y aceleración | Humo de biomasa y salud |
| Huang 2025 | Wei 2026 | 4 | crecimiento y aceleración | Pronóstico con aprendizaje profundo y gemelo digital |
| Rodríguez-Villamizar 2022 | Liao 2026 | 4 | fundacional y aceleración | Carga e índices de salud |
| Kumar 2026 | Liao 2026 | 3 | aceleración | Materia particulada e índices |
| Becerra 2021 | Vélez-Pereira 2025 | 3 | fundacional y crecimiento | Pronóstico de calidad del aire |
| Essamlali 2024 | Haris 2026 | 3 | crecimiento y aceleración | Revisiones de métodos |
| Bang 2026 | Tavella 2026 | 3 | aceleración | Redes de sensores y agenda de Brasil |
| Murad Pedraza 2026 | Tavella 2026 | 3 | aceleración | Sistemas de vigilancia y agenda de Brasil |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §7.7, Tabla 39 (p. 95). Referencias compartidas aproximadas por fragmentos de título de siete palabras. Eras según la segmentación de la sección 2.2.2. Naturaleza: DOCUMENTADO; la columna de lectura es INFERIDO. Corpus de 26 artículos de 42 documentos; año de corte 2026.

:::FIGURA cocitacion | Acoplamiento bibliográfico entre artículos y referencias más compartidas | Nota. Elaboración propia con networkx y matplotlib a partir de F-INF §7.7, Tabla 39 (p. 95). Los 12 pares de mayor acoplamiento de 102; nodos por era de publicación. El corpus no permite calcular co-citación de autores. Corpus de 26 artículos de 42 documentos; año de corte 2026; semilla 42.

El par de Moura et al. (2025) y Tavella et al. (2026) comparte 12 referencias, y el informe lo atribuye al grupo de autores común. Los otros 11 pares comparten entre tres y seis. La referencia más compartida es la guía de la OMS de 2021, que citan nueve artículos (OMS, 2021). Una revisión sobre efectos ambientales y de salud de la contaminación aparece en cinco artículos. La red forma cuatro componentes, y el mayor reúne ocho artículos.

Una posición valora el acoplamiento porque capta el frente de investigación actual. La otra valora la co-citación porque capta la base consolidada. Aquí la base compartida es delgada. Las listas casi no se solapan, y la guía de la OMS es la única referencia que citan nueve artículos. La co-citación de autores no es calculable sin una base de citas, y el proyecto la declara VACIO.

La literatura de calibración colocalizada que el proyecto usa no figura en el corpus. Las evaluaciones de sensores ópticos frente a referencia pertenecen al banco de referencias del proyecto (Barkjohn et al., 2021; Malings et al., 2020; Giordano et al., 2021). También pertenece al banco el protocolo de pruebas de la Agencia de Protección Ambiental de Estados Unidos (EPA, 2021). La consecuencia es que el proyecto debe construir su base intelectual de calibración fuera del corpus. No puede apoyarse en la red documental de la vigilancia.

### 2.2.7 Mapa estratégico de cuatro cuadrantes

El mapa estratégico ubica cada comunidad temática según su centralidad y su densidad. La centralidad mide la fuerza de los enlaces con otras comunidades. La densidad mide la fuerza de los enlaces internos (Callon et al., 1991). Las comunidades con ambas medidas altas son temas motores. Las de ambas medidas bajas son emergentes o están en declive. Cobo et al. (2011) usan el mismo diagrama estratégico para describir la evolución de un campo.

La especificación pide un mapa de acoplamiento bibliográfico con impacto por cluster. El informe no reporta impacto por cluster, porque no incluye citas. Por eso el mapa usa las ocho comunidades de la red de co-palabras. Sus valores de centralidad y densidad provienen del informe (F-INF §7.5, Tabla 37, p. 88). La {T:t12} y la {F:cuadrantes} presentan las comunidades. El corte entre cuadrantes usa las medianas de centralidad (379.935) y de densidad (27.825), calculadas con los valores del informe.

:::TABLA t12 | Comunidades de co-palabras por cuadrante estratégico
| Comunidad | Términos | Términos principales | Densidad | Centralidad | Cuadrante en el informe | Cuadrante por medianas |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | 195 | aire, calidad, contaminantes | 31.461,54 | 875.310 | Motor | Motor |
| C2 | 136 | datos, sensores, dispositivos | 33.518,38 | 881.650 | Motor | Motor |
| C3 | 94 | modelo, tiempo, valor | 30.410,64 | 700.890 | Motor | Motor |
| C4 | 59 | salud, activos, motores | 54.844,07 | 479.950 | Motor | Motor |
| C5 | 48 | temperatura, viento, partículas | 20.495,83 | 279.920 | Emergente o en declive | Emergente o en declive |
| C6 | 29 | edificios, espacio, urbano | 21.855,17 | 218.480 | Emergente o en declive | Emergente o en declive |
| C7 | 13 | conjuntos, índices, métricas | 25.238,46 | 73.660 | Emergente o en declive | Emergente o en declive |
| C8 | 10 | fechas de publicación | 8.330,00 | 10.640 | Emergente o en declive | Emergente o en declive |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §7.5, Tabla 37 (p. 88). Medianas calculadas sobre las ocho comunidades: centralidad de 379.935 y densidad de 27.825. Naturaleza: DOCUMENTADO para los valores y CALCULADO para el cuadrante por medianas. Corpus de 42 documentos; año de corte 2026.

:::FIGURA cuadrantes | Mapa estratégico de cuatro cuadrantes de las comunidades de co-palabras | Nota. Elaboración propia con matplotlib a partir de F-INF §7.5, Tabla 37 (p. 88). Tamaño proporcional al número de términos; cortes en las medianas. Louvain con ocho comunidades sobre 584 nodos. Corpus de 42 documentos; año de corte 2026; semilla 42.

Cuatro comunidades son motoras. Son aire, calidad y contaminantes (195 términos); datos, sensores y dispositivos (136); modelo, tiempo y valor (94); y salud, activos y motores (59). Las otras cuatro son emergentes o marginales. Ninguna comunidad cae en los cuadrantes de nicho ni de tema básico. La comunidad de salud, activos y motores tiene la mayor densidad (54.844) y la menor centralidad entre las motoras. El informe la describe como nicho denso, porque proviene de dos patentes largas de General Electric (F-INF §7.5, p. 88).

Dos lecturas del cuadrante emergente conviven. Una lo interpreta como frontera de investigación que crece. Otra lo interpreta como periferia que decae. Con 42 documentos y sin serie temporal por comunidad, el corpus no discrimina entre ambas. El informe agrega que dos comunidades reflejan el género y el idioma más que un tema. Son la de conjuntos, índices y métricas, con 13 términos, y la de fechas de publicación, con 10 (F-INF §7.5, p. 88).

La comunidad 5 reúne temperatura, humedad, viento y partículas. Son las variables del modelo de corrección del proyecto. Su posición emergente respalda la oportunidad de posicionamiento: la corrección por humedad y temperatura está menos consolidada que el pronóstico o el monitoreo. La consecuencia metodológica es que el proyecto debe aportar evidencia propia en el tramo 1. El corpus no la ofrece.

### 2.2.8 Evolución temática por períodos

La evolución temática compara la composición del corpus en períodos sucesivos. Cobo et al. (2011) la describen como la persistencia, la fusión o la desaparición de temas entre períodos. Este análisis usa las tres eras de la sección 2.2.2 y los cinco grupos documentales del informe. La {T:t13} y la {F:evolucion} muestran la composición por grupo. Cada documento pertenece a un solo período. Por eso los listones de la figura unen el mismo grupo y no representan migración de documentos.

:::TABLA t13 | Composición del corpus por era y grupo documental
| Era | Años | Documentos | G1 | G2 | G3 | G4 | G5 | Grupo mayoritario |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fundacional | 1995 a 2023 | 11 | 3 | 0 | 1 | 6 | 1 | G4 (6) |
| Crecimiento | 2024 a 2025 | 14 | 4 | 1 | 3 | 2 | 4 | G1 (4) |
| Aceleración | 2026 | 17 | 2 | 7 | 5 | 0 | 3 | G2 (7) |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §10.1, Tabla 46 (p. 124) y §13.2 (p. 212). G1: pronóstico con aprendizaje automático; G2: monitoreo y alerta; G3: exposición y salud; G4: patentes de sensores y activos; G5: patentes de espacios interiores y reporte de la SIC. Naturaleza: CALCULADO. Corpus de 42 documentos; año de corte 2026.

:::FIGURA evolucion | Composición temática del corpus en tres eras mediante listones entre grupos | Nota. Elaboración propia con matplotlib a partir de F-INF §4.3 (p. 34) y §10.1, Tabla 46 (p. 124). Segmentos con el número de documentos por grupo; los listones unen el mismo grupo entre eras y no representan flujos de documentos. Corpus de 42 documentos; año de corte 2026; semilla 42.

El grupo de patentes de sensores y activos domina la era fundacional con seis de 11 documentos. Los grupos de pronóstico y de patentes de espacios interiores lideran el crecimiento con cuatro documentos cada uno. El grupo de monitoreo y alerta lidera la aceleración con siete de 17, y el de exposición y salud aporta cinco. Las patentes de sensores y activos no tienen documentos en 2026.

El modelado de tópicos del informe añade dos señales. El tópico de alerta temprana y desastres crece de 0,002 antes de 2019 a 0,138 en 2026 y es el más emergente. El tópico de salud, exposición y mortalidad está presente en todos los períodos y es el más consolidado (F-INF §7.4, p. 82). Los tópicos de retiro de activos y de cuantificador de salud solo pesan en 2019 y 2024, años de las patentes de General Electric. Su descenso refleja ausencia de documentos y no declive tecnológico.

El análisis de ráfagas se aproxima con la proporción de documentos cuyo título contiene un término, por era. La {T:t14} lista ocho términos. Esta medida no es el algoritmo de Kleinberg. Con 11, 14 y 17 documentos por era, solo indica tendencias.

:::TABLA t14 | Términos de título en aceleración por era
| Palabra de título | Era fundacional (11) | Era de crecimiento (14) | Era de aceleración (17) | Proporción de documentos por era | Lectura |
| --- | --- | --- | --- | --- | --- |
| management | 0 | 0 | 5 | 0,0 %; 0,0 %; 29,4 % | Aparece solo en 2026; incluye la gestión del riesgo |
| pollution | 0 | 4 | 5 | 0,0 %; 28,6 %; 29,4 % | Aparece desde 2024 |
| monitoring | 1 | 3 | 4 | 9,1 %; 21,4 %; 23,5 % | Crece en cada era |
| climate | 0 | 1 | 2 | 0,0 %; 7,1 %; 11,8 % | Crece desde 2024 |
| heritage | 0 | 0 | 2 | 0,0 %; 0,0 %; 11,8 % | Aparece solo en 2026 |
| review | 0 | 1 | 2 | 0,0 %; 7,1 %; 11,8 % | Crece desde 2024 |
| particulate | 0 | 1 | 2 | 0,0 %; 7,1 %; 11,8 % | Crece desde 2024 |
| health | 2 | 4 | 2 | 18,2 %; 28,6 %; 11,8 % | No crece: sube y baja |
:::NOTA *Nota.* Elaboración propia con los títulos de los 42 documentos. Conteo de documentos cuyo título contiene el término; un término cuenta una vez por documento. Aproximación a ráfagas por razón de proporciones, no por el algoritmo de Kleinberg. Naturaleza: CALCULADO; la columna de lectura es INFERIDO. Año de corte 2026.

El término management pasa de cero a 29,4 % de los títulos en la era de aceleración. El término pollution pasa de cero a 28,6 % y luego a 29,4 %. El término monitoring crece de 9,1 % a 23,5 %. Los términos heritage, climate, review y particulate aparecen o crecen entre 2024 y 2026. El término health no crece: sube a 28,6 % y cae a 11,8 %.

Dos lecturas de estas tendencias compiten. La primera ve una aceleración temática hacia la gestión del riesgo y las alertas. La segunda ve un efecto de composición, porque la era de aceleración incluye siete documentos de monitoreo y alerta. El informe respalda la segunda lectura. Afirma que la evolución de tópicos describe la composición del corpus más que la dinámica del campo (F-INF §7.4, p. 82).

La decisión metodológica es tratar la gestión y la alerta como direcciones plausibles y no como tendencias probadas. El proyecto alinea su tercer objetivo específico con esa dirección. Lo respalda con indicadores propios de uso institucional (PERS-E01) y no con la tendencia bibliométrica.

### 2.2.9 Complejidad frente a adopción

La relación entre complejidad y adopción pregunta si los métodos más sofisticados se adoptan menos. El protocolo propone un gráfico de burbujas con una zona de valle de la muerte para complejidad mayor que 7 y adopción menor que 5. El corpus no mide la complejidad de los métodos. Por eso se usan dos proxies que el informe sí mide. El nivel de preparación tecnológica (TRL) representa la sofisticación, y el nivel de integración (IRL) representa la adopción.

El TRL describe la madurez de una tecnología en nueve niveles (Mankins, 1995). La adopción depende además de la utilidad y de la facilidad de uso percibidas (Davis, 1989; Venkatesh et al., 2003). Depende también de las propiedades de la innovación que describe la teoría de difusión (Rogers, 2003). El IRL del informe mide la integración con interfaces y con sistemas. Es una condición de adopción y no su medida completa.

La {T:t15} presenta las brechas entre el TRL y las demás dimensiones. La {F:complejidad} ubica los 41 documentos con TRL e IRL.

:::TABLA t15 | Brechas entre el TRL y las demás dimensiones de madurez
| Brecha | Documentos con dato | Media | Mínimo | Máximo | Documentos con esta brecha como crítica |
| --- | --- | --- | --- | --- | --- |
| TRL menos IRL | 41 | 0,98 | 0 | 2 | 22 |
| TRL menos DRL | 41 | 0,80 | -1 | 3 | 11 |
| TRL menos BRL | 9 | 2,33 | 1 | 5 | 6 |
| BRL menos DRL | 9 | -1,44 | -3 | -1 | 1 |
| TRL menos MRL | 4 | 1,75 | 1 | 3 | Sin dato; otra brecha: 2 |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §4.5, Tablas 15 y 16 (p. 37). BRL = nivel de preparación del negocio; MRL = nivel de preparación de la manufactura. La brecha crítica de cada documento es la de mayor magnitud o riesgo. Naturaleza: DOCUMENTADO. Año de corte 2026.

El TRL supera al IRL en 0,98 niveles en promedio. Esa brecha es la crítica en 22 de 42 documentos (F-INF §4.5, p. 37). Treinta y cuatro de 41 documentos tienen TRL de 4 o menos, y 33 de 41 tienen IRL de 3 o menos. El valle de componentes sin integración reúne 13 documentos. Nueve de ellos están en la región de TRL 4 a 5 con IRL de 3 o menos. Solo dos documentos alcanzan TRL 7 o más. Son el sistema de SIATA, con TRL 9 e IRL 8, y el sistema de lahares del Instituto Geofísico del Perú. Este tiene TRL 7 e IRL 5 (Ruiz-Carrascal et al., 2026; Espinoza et al., 2026).

:::FIGURA complejidad | Sofisticación frente a integración de los documentos y valle de componentes sin integración | Nota. Elaboración propia con matplotlib a partir de F-INF §4.1, Tabla 13 (p. 29) y §4.6, Tabla 17 (p. 38). El TRL representa la sofisticación y el IRL la adopción porque el corpus no mide la complejidad. Tamaño proporcional al número de documentos; n de 41 con TRL e IRL. Año de corte 2026; semilla 42.

Dos posiciones explican el valle. La primera sostiene una secuencia lineal. La madurez tecnológica precede a la adopción, y el valle se cierra con más desarrollo. La segunda sostiene que la adopción depende del uso y del contexto institucional, de modo que más madurez tecnológica no basta (Rogers, 2003; Davis, 1989). El grupo de pronóstico apoya la segunda posición. Tiene TRL de 4,0 y el DRL medio más bajo entre los grupos (2,22). Eso indica modelos probados con datos históricos y sin intención de uso verificada (F-INF §4.4, p. 36). Quienes deciden con alertas enfrentan además sesgos de decisión bajo riesgo, como la aversión a la pérdida (Kahneman y Tversky, 1979).

El proyecto parte de TRL 4 y apunta a TRL 7 (PROPUESTO). Parte, por tanto, de la región donde el corpus acumula el valle. El proyecto no confía en que más ingeniería cierre esa distancia. Mide la adopción desde el tramo 1. La compuerta C1 exige que al menos 50 % de los comités del tramo 1 use el tablero. El indicador PERS-E01 fija 75 % de uso al mes 24 (PROPUESTO).


### 2.2.10 Radar de cobertura por criterios de evaluación

El radar compara perfiles de cobertura entre grupos de documentos. El protocolo propone seis criterios: financiero, estratégico, de recursos, de riesgo, de partes interesadas y de sostenibilidad. El corpus no mide esos seis criterios. Mide cinco indicadores comparables con un criterio de referencia (F-INF §3.2, p. 22). Son TRL, IRL, nivel de preparación de la demanda (DRL), robustez y valor estratégico. Sus criterios son 7, 6, 5, 7 y 7. El radar usa esos cinco ejes y expresa cada media como porcentaje del criterio.

El DRL mide, en una escala de 1 a 9, si usuarios concretos validaron la necesidad de una tecnología. El informe extiende así la lógica de los niveles de madurez de Mankins (1995) a la demanda, la integración y el sistema. La {T:t16} y la {F:radar} presentan los perfiles de los cinco grupos y del corpus.

:::TABLA t16 | Perfil de los grupos documentales como porcentaje del criterio de referencia
| Grupo | Documentos | TRL (% de 7) | IRL (% de 6) | DRL (% de 5) | Robustez (% de 7) | Valor (% de 7) | Promedio de los cinco ejes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1 Pronóstico con aprendizaje automático | 9 | 57 % | 43 % | 44 % | 65 % | 90 % | 60 % |
| G2 Monitoreo y alerta | 8 | 73 % | 65 % | 78 % | 59 % | 95 % | 74 % |
| G3 Exposición y salud | 9 | 52 % | 43 % | 62 % | 62 % | 92 % | 62 % |
| G4 Patentes de sensores y activos | 8 | 46 % | 44 % | 60 % | 51 % | 61 % | 52 % |
| G5 Patentes interiores y reporte de la SIC | 8 | 45 % | 48 % | 62 % | 42 % | 70 % | 53 % |
| Corpus completo | 42 | 55 % | 48 % | 61 % | 56 % | 82 % | 60 % |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §3.2, Tablas 5 y 6 (p. 22). Criterios de referencia: TRL 7, IRL 6, DRL 5, robustez 7 y valor estratégico 7. El SRL se excluye porque solo tres grupos tienen datos. Naturaleza: CALCULADO sobre medias DOCUMENTADAS. Corpus de 42 documentos; año de corte 2026.

:::FIGURA radar | Perfil de cada grupo documental frente al criterio de referencia en cinco indicadores | Nota. Elaboración propia con matplotlib a partir de F-INF §3.2, Tablas 5 y 6 (p. 22). Cada eje es la media del grupo como porcentaje del criterio; la línea discontinua es el corpus de 42 documentos. Los seis criterios de la especificación no se midieron en el corpus. Año de corte 2026; semilla 42.

El grupo de monitoreo y alerta tiene el perfil más alto. Su TRL llega a 73 %, su IRL a 65 % y su DRL a 78 %. Su robustez llega a 59 % y su valor a 95 %. Los grupos de patentes tienen el perfil más bajo, con promedios de 52 % y 53 %. El grupo de pronóstico combina un TRL de 57 % con un DRL de 44 %, el más bajo entre los tres grupos de artículos. Ningún grupo llega a 100 % en ningún eje.

Una posición usa el perfil conjunto como señal de preparación global. La otra advierte que un perfil promedio oculta la dispersión. El grupo de monitoreo y alerta depende de un solo sistema de nivel 9. Ese sistema sostiene su TRL, su IRL y su DRL (F-INF §4.4, p. 36). Sin SIATA, el TRL medio del corpus baja de 3,85 a 3,73 (F-INF §3.6, p. 28). El proyecto adopta la segunda advertencia y no promedia grupos con un solo caso destacado.

Los documentos del grupo de monitoreo y alerta sirven como anclas del proyecto. Son SIATA, el sistema de lahares, la red de Seúl y la red de una mina de carbón (Ruiz-Carrascal et al., 2026; Espinoza et al., 2026; Bang et al., 2026; Suresh et al., 2025). Las patentes sirven para la libertad de operación y no como evidencia de desempeño. El proyecto no usa el valor estratégico asignado como criterio de selección, porque es una escala del analista.

### 2.2.11 Mapa de calor de líneas tecnológicas y madurez

El mapa de calor cruza líneas tecnológicas con criterios de madurez. El protocolo pide una matriz de métodos por criterios con valores de compatibilidad de 0 a 10. El corpus no contiene esa puntuación. La versión que los datos soportan cruza las 12 líneas tecnológicas del informe con dos criterios medidos, el TRL y el IRL. Cada valor se expresa como porcentaje del criterio de referencia.

El informe agrega los documentos en 13 líneas tecnológicas y calcula su madurez media (F-INF §4.8, p. 41). Un documento puede pertenecer a más de una línea. Por eso las 13 líneas suman 45 asignaciones para 42 documentos. La {T:t17} y la {F:heatmap} presentan las 12 líneas con TRL e IRL.

:::TABLA t17 | Madurez media por línea tecnológica como porcentaje del criterio
| Línea tecnológica | Documentos | TRL actual | IRL actual | TRL (% de 7) | IRL (% de 6) | Brecha TRL menos IRL |
| --- | --- | --- | --- | --- | --- | --- |
| Sistemas de alerta temprana y gestión de desastres | 4 | 5,75 | 4,50 | 82 % | 75 % | 1,25 |
| Pronóstico con aprendizaje automático | 9 | 4,00 | 2,56 | 57 % | 43 % | 1,44 |
| Valorización de residuos por gasificación | 1 | 4,00 | 3,00 | 57 % | 50 % | 1,00 |
| Exposición ocupacional | 2 | 4,00 | 3,00 | 57 % | 50 % | 1,00 |
| Redes de sensores de bajo costo y calibración | 5 | 3,80 | 3,00 | 54 % | 50 % | 0,80 |
| Índices y calificaciones de salud y salubridad | 4 | 3,75 | 3,00 | 54 % | 50 % | 0,75 |
| Teledetección de incendios, humo y transporte regional | 3 | 3,67 | 2,33 | 52 % | 39 % | 1,34 |
| Carga de enfermedad y exposición | 5 | 3,60 | 2,40 | 51 % | 40 % | 1,20 |
| Patrimonio y materiales | 2 | 3,50 | 3,00 | 50 % | 50 % | 0,50 |
| Diagnóstico predictivo con gemelo digital | 3 | 3,33 | 3,00 | 48 % | 50 % | 0,33 |
| Medición de partículas y calibración (patentes) | 3 | 3,00 | 2,33 | 43 % | 39 % | 0,67 |
| Energía, carbono y control de interiores | 3 | 2,67 | 2,67 | 38 % | 44 % | 0,00 |
| Vigilancia de propiedad industrial | 1 | No aplica | No aplica | No aplica | No aplica | No aplica |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §4.8, Tabla 18 (p. 41). Criterios: TRL 7 e IRL 6. Un documento puede pertenecer a más de una línea. La brecha es TRL menos IRL. Naturaleza: DOCUMENTADO para TRL e IRL y CALCULADO para porcentajes y brechas. Corpus de 42 documentos; año de corte 2026.

:::FIGURA heatmap | Mapa de calor de madurez tecnológica y de integración por línea tecnológica | Nota. Elaboración propia con matplotlib a partir de F-INF §4.8, Tabla 18 (p. 41). Color proporcional al porcentaje del criterio (TRL 7; IRL 6); brecha TRL menos IRL en niveles. La línea de vigilancia de propiedad industrial carece de TRL e IRL. Corpus de 42 documentos; año de corte 2026.

Los sistemas de alerta temprana tienen los valores más altos, con TRL de 5,75 (82 %) e IRL de 4,50 (75 %). El pronóstico con aprendizaje automático tiene la mayor brecha entre TRL e IRL, de 1,44 niveles. Las redes de sensores de bajo costo y calibración tienen TRL de 3,80 e IRL de 3,00, con cinco documentos. La línea de energía, carbono y control de interiores tiene la menor madurez, con TRL de 2,67.

Dos lecturas identifican las líneas versátiles. La primera elige las líneas con brecha pequeña, porque integran lo que desarrollan. Con ese criterio, dos líneas son las más versátiles: energía y control de interiores (brecha de 0,00) y diagnóstico predictivo con gemelo digital (0,33). Ambas tienen TRL bajo. La segunda elige las líneas de madurez alta, porque ofrecen más usos. Con ese criterio, solo los sistemas de alerta lo son.

La línea que interesa al proyecto es la de redes de sensores de bajo costo y calibración. Alcanza 54 % del criterio en TRL y 50 % en IRL. Esa posición intermedia indica que existe base técnica y falta integración con un protocolo de referencia. El proyecto actúa sobre esa brecha con tres monitores gravimétricos de referencia, uno por departamento, y con la corrección en el gateway (DEC-F02).

### 2.2.12 Distribución geográfica

La distribución geográfica mide dónde se produce el conocimiento del corpus. El informe asigna cada documento a los países de sus instituciones. Estados Unidos aporta 12 documentos, Colombia nueve, China cuatro, y España, Brasil y el Reino Unido tres cada uno. El corpus incluye 21 nacionalidades (F-INF §6.2, p. 61). La {T:t18} y la {F:geografica} presentan los seis países que el informe desagrega.

:::TABLA t18 | Países con mayor número de documentos del corpus
| País | Documentos | Porcentaje de 42 | Posición |
| --- | --- | --- | --- |
| Estados Unidos | 12 | 28,6 % | Primero |
| Colombia | 9 | 21,4 % | Segundo |
| China | 4 | 9,5 % | Tercero |
| España | 3 | 7,1 % | Cuarto, empatado |
| Brasil | 3 | 7,1 % | Cuarto, empatado |
| Reino Unido | 3 | 7,1 % | Cuarto, empatado |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §6.2 (p. 61). Un documento puede contar en varios países, de modo que los porcentajes no suman 100 %. Los 15 países restantes no se desagregan en el informe. Naturaleza: DOCUMENTADO para los conteos y CALCULADO para los porcentajes. Corpus de 42 documentos; año de corte 2026.

:::FIGURA geografica | Documentos del corpus por país de las instituciones | Nota. Elaboración propia con matplotlib a partir de F-INF §6.2 (p. 61) y §7.6 (p. 93). Seis países desagregados de 21 nacionalidades; un documento puede contar en varios países. Corpus de 42 documentos; año de corte 2026.

Colombia ocupa el segundo lugar con 21,4 % de los documentos. Su aporte proviene de grupos con vínculos locales fuertes, como SIATA, EAFIT y la Universidad de Antioquia. Los vínculos internacionales son pocos (F-INF §7.6, p. 93). Solo ocho de los 26 artículos (30,8 %) tienen coautoría internacional. Ninguna de las 15 patentes tiene solicitante colombiano, y diez designan a Colombia (F-INF §6.2, p. 61). América Latina no se cuantifica como región, porque el informe solo desagrega a Colombia y Brasil entre los países latinoamericanos.

Los estudios de índices de calidad del aire y salud ilustran el vacío regional. Ninguno de los 53 estudios revisados proviene de América Latina, y 88,7 % proviene de China (Liao et al., 2026, p. 6). Dos posiciones interpretan este patrón. La primera ve una oportunidad de posicionamiento, porque la región aporta datos locales y poca validación de métodos. La segunda ve una dependencia, porque los métodos se importan de grupos de China, Corea y Estados Unidos y se aplican sin validación local. El informe describe la dinámica como un primer movimiento asimétrico en índices y minería (F-INF §6.5, p. 68).

La consecuencia es que el proyecto debe producir validación local en Caldas, Cundinamarca y Valle del Cauca (SUPUESTO) y publicarla. Los dos artículos en revistas Q1 o Q2 del indicador PERS-P03 apuntan en esa dirección. Las redes de colaboración internacional del corpus son escasas. El proyecto las trata como una tarea de alianza y no como un dato de partida.

### 2.2.13 Robustez metodológica

La robustez metodológica evalúa cuán sólido es el argumento de cada documento. El informe la calcula como 0,3 por consistencia lógica, 0,3 por calidad de la evidencia, 0,2 por validez causal y 0,2 por generalizabilidad. Cada componente va de 1 a 10 (F-INF §2.2, p. 14). La definición se parece a la lectura de argumentos por afirmación, datos y garantía (Toulmin, 1958).

La media del corpus es 3,93, la mediana 4,0 y la desviación estándar 0,75. El rango va de 2,7 a 6,1. Veintiún documentos tienen robustez de 4 o menos. Solo uno, Nelson et al. (2026), supera 6. Ningún documento alcanza 7, de modo que el porcentaje de documentos sólidos, con 8,5 o más, es 0 %. La {T:t19} y la {F:robustez} presentan la media por grupo y por clase documental. El informe no publica la robustez de cada documento. Por eso no se construye un gráfico de violín.

:::TABLA t19 | Robustez por grupo y clase documental
| Grupo o clase | Documentos | Media | Desviación estándar | Valores individuales publicados | Rango de los valores publicados |
| --- | --- | --- | --- | --- | --- |
| G1 Pronóstico con aprendizaje automático | 9 | 4,54 | No publicada | 3 | 4,4 a 6,1 |
| G2 Monitoreo y alerta | 8 | 4,12 | No publicada | 5 | 2,8 a 5,0 |
| G3 Exposición y salud | 9 | 4,32 | No publicada | 3 | 4,1 a 5,0 |
| G4 Patentes de sensores y activos | 8 | 3,54 | No publicada | 2 | 3,0 a 3,8 |
| G5 Patentes interiores y reporte de la SIC | 8 | 2,97 | No publicada | 4 | 2,7 a 3,0 |
| Artículos | 26 | 4,34 | No publicada | 11 | 2,8 a 6,1 |
| Patentes | 15 | 3,27 | No publicada | 5 | 2,7 a 3,8 |
| Corpus completo | 42 | 3,93 | 0,75 | 17 | 2,7 a 6,1 |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §2.2 (p. 14), §3.2, Tablas 6 y 7 (p. 22) y §13.1, Tabla 65 (p. 208). El informe reporta 2,97 para G5 en el texto de §2.2 y en la Tabla 6, y 2,98 en la Tabla 1. Los valores individuales son los publicados en el informe, 17 de 42. Naturaleza: DOCUMENTADO. Año de corte 2026.

Los artículos promedian 4,34 y las patentes 3,27. La diferencia es significativa (Mann-Whitney, p menor que 0,001). Un modelo lineal asigna a la patente un coeficiente de menos 1,10 puntos una vez controlados TRL, IRL y año (F-INF §3.3, p. 24). El informe interpreta que las patentes describen sin demostrar. La consistencia lógica es el componente más alto (4,93) y la validez causal el más bajo (3,17). Las patentes casi igualan a los artículos en consistencia, con 4,87 y 5,00. Se separan en evidencia, con 2,00 y 4,54 (F-INF §2.2, p. 14).

:::FIGURA robustez | Robustez media por grupo documental y valores individuales publicados | Nota. Elaboración propia con matplotlib a partir de F-INF §2.2 (p. 14), §3.2 (p. 22) y §13.1, Tabla 65 (p. 208). Barras con la media del grupo y puntos con los 17 valores individuales publicados; la distribución completa no se publica. Corpus de 42 documentos; año de corte 2026; semilla 42.

Una posición toma la robustez como medida de la calidad de los documentos. La otra la toma como una escala ordinal del analista, útil para ordenar la atención y no para medir calidad (F-INF §3.3, p. 24). Este capítulo adopta la segunda lectura. La rúbrica no sustituye la verificación empírica. Ningún documento aporta la verificación que exige el proyecto: la comparación con una referencia colocalizada en sitios de remoción de escombros.

La consecuencia metodológica es que los umbrales de desempeño del proyecto no provienen del corpus. Provienen del protocolo de pruebas de sensores de la EPA (EPA, 2021). Fijan un coeficiente de determinación (R²) de 0,70 o más. Fijan también un error cuadrático medio normalizado (NRMSE) de 30 % o menos. Ambos se miden frente a una referencia colocalizada (PROPUESTO). El proyecto trata las afirmaciones de los documentos como hipótesis de diseño.

### 2.2.14 Síntesis cienciométrica, brechas cuantitativas y marco de análisis de brechas

La síntesis cienciométrica reúne los indicadores y los traduce en brechas cuantitativas. El corpus crece de dos documentos en 2019 a 17 en 2026. Tiene autoría dispersa, con 95,8 % de autores con un documento, y 19 revistas para 26 artículos. Su red temática forma cinco comunidades con modularidad de 0,27. La madurez es baja: TRL de 3,85, IRL de 2,88 y DRL de 3,05 frente a criterios de 7, 6 y 5 (F-INF §3.2, p. 22). La robustez media es 3,93 y ningún documento llega a 7.

El marco de análisis de brechas agrupa cuatro categorías heredadas y una quinta ranura para el patrón propio del campo. Cada categoría se instancia solo si el corpus cumple su criterio de aplicabilidad. La {T:t20} consolida cada brecha con su evidencia, sus fuentes y la oportunidad que abre para el proyecto.

:::TABLA t20 | Consolidación de brechas cuantitativas: evidencia, fuentes y oportunidad
| Brecha | Instanciación en este corpus | Evidencia cuantitativa | Fuentes | Oportunidad para el proyecto | Naturaleza |
| --- | --- | --- | --- | --- | --- |
| Paradoja de usabilidad | Sofisticación medida por el TRL; adopción medida por el IRL y el DRL; aplica con proxies | Brecha TRL menos IRL de 0,98 niveles, crítica en 22 de 42 documentos; el grupo de pronóstico tiene DRL de 2,22 | F-INF §4.4 y §4.5 (pp. 36-37) | Medir la adopción desde el tramo 1 con la compuerta C1 y el indicador PERS-E01 | CALCULADO; INFERIDO |
| Espejismo del óptimo | Unidad: sensor o modelo; conjunto: red con calibración, mantenimiento y uso; aplica | 90,8 % de 5.076 estaciones sin plan de calibración; 96 de 570 estaciones brasileñas inactivas o sin estado (16,8 %) | Murad Pedraza et al. (2026, pp. 10-11 y 13); Tavella et al. (2026, p. 6) | Condicionar la compra de cada tramo a la calibración con las compuertas C1 y C2 | DOCUMENTADO; INFERIDO |
| Brecha TRL-BRL | Madurez de la solución frente a madurez del negocio; aplica a 9 documentos con BRL | Brecha media de 2,33 niveles, de 1 a 5; BRL menos DRL de -1,44 | F-INF §4.5, Tabla 15 (p. 37) | Custodia distribuida y convenios por tramo para cerrar la brecha de negocio | DOCUMENTADO; INFERIDO |
| Variables conductuales ausentes | Decisión humana: respuesta de comités ante alertas; aplica de forma limitada | Ninguno de los 5 documentos de alerta reporta detección, falsas alarmas ni anticipación; 1 de 42 documentos (2,4 %) trata conocimientos, actitudes y prácticas | F-INF §1.3 (p. 10); Rendón-Marín et al. (2024) | Co-diseño con comités y medición del uso del tablero y de las falsas alarmas | DOCUMENTADO; INFERIDO |
| Brecha emergente: producción sin verificación | Patrón propio del campo; exploratoria porque N es menor que 45 | Robustez media de 3,93; 0 de 15 patentes con validación frente a verdad de referencia; 9,4 % de 53 estudios de índices con partición de datos | F-INF §1.3 (p. 10); Liao et al. (2026, pp. 6 y 8) | Verificar con colocalización y evaluación independiente (líneas S07 y S08) | DOCUMENTADO; INFERIDO |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §1.3 (p. 10), §4.4 y §4.5 (pp. 36-37) y de las fuentes citadas. BRL = nivel de preparación del negocio. Las instanciaciones son INFERIDO y los datos de cada fuente son DOCUMENTADO. Corpus de 42 documentos; año de corte 2026.

La paradoja de usabilidad se instancia como la distancia entre desarrollo e integración. El grupo de pronóstico alcanza un TRL de 4,0 con el DRL más bajo. Cinco de sus nueve documentos carecen de línea base de persistencia (F-INF §1.3, p. 10). El segundo patrón, la optimización de unidades aisladas, aparece cuando se optimiza el sensor o el modelo sin considerar el sistema. La compra de sensores sin plan de calibración sigue esa lógica. El 90,8 % de las 5.076 estaciones propuestas no tendría plan (Murad Pedraza et al., 2026, pp. 10-11 y 13). En Brasil, 96 de 570 estaciones están inactivas o sin estado (Tavella et al., 2026, p. 6).

La brecha TRL-BRL mide cuánto supera la madurez tecnológica a la del negocio. En los nueve documentos con BRL, el promedio es 2,33 niveles. SIATA es el único caso con BRL de 6 (F-INF §4.1, p. 29). Las variables conductuales faltan en los procesos de decisión. Los cinco documentos de alerta no reportan detección, falsas alarmas ni anticipación. SIATA no evalúa sus alertas con un contrafactual (Ruiz-Carrascal et al., 2026, pp. 2, 5 y 7). Los sesgos cognitivos y la racionalidad limitada afectan la lectura de las alertas (Tversky y Kahneman, 1974; Simon, 1955). El corpus no los modela.

La brecha emergente es la producción sin verificación. Ninguna de las 15 patentes valida con verdad de referencia (F-INF §1.3, p. 10). Solo 9,4 % de los 53 estudios de índices de calidad del aire y salud validó con partición de datos (Liao et al., 2026, pp. 6 y 8). Con 42 documentos, esta brecha es una hipótesis exploratoria y no una ley del campo. Dos posiciones evalúan el marco. Una lo usa para priorizar la inversión. La otra advierte que las categorías heredadas pueden forzar patrones ajenos al corpus. El proyecto aplica el criterio de aplicabilidad y declara en cada brecha si la instanciación es completa o limitada.

Las oportunidades de posicionamiento son tres. La primera es la colocalización con referencia gravimétrica en sitios de remoción de escombros, que el corpus no cubre. La segunda es la medición de la adopción institucional desde el tramo 1. La tercera es la verificación independiente del desempeño, con una evaluación externa y un ensayo con laboratorio externo (líneas S07 y S08). La ventana temporal combina dos señales. Primero, 17 de 42 documentos son de 2026, de modo que el interés por alertas y gestión crece. Segundo, tres solicitudes del Tratado de Cooperación en materia de Patentes (PCT) vencen en tres fechas. Esas fechas van del 10 de diciembre de 2026 al 28 de agosto de 2027. Caen entre dos y 11 meses después de la fecha de corte. Si la ejecución inicia pronto, las tres caen dentro del tramo 1, que dura 12 meses. La fecha de inicio es un dato por definir [DATO_USUARIO: fecha del acta de inicio].


## 2.3 Análisis de patentes y vigilancia tecnológica

El análisis de patentes responde a dos preguntas. La primera es quién protege qué en el campo. La segunda es qué restricciones de libertad de operación enfrenta el proyecto. El corpus incluye 15 patentes. La Organización Mundial de la Propiedad Intelectual publica 11 y la Oficina Europea de Patentes publica cuatro. Diez designan a Colombia y ninguna tiene solicitante colombiano (F-INF §6.2, p. 61). Los titulares se toman de los nombres que el informe de vigilancia asigna a cada solicitud.

### 2.3.1 Titulares y clasificaciones

La libertad de operación es la posibilidad de fabricar y operar una tecnología sin infringir derechos vigentes de terceros. El régimen común andino de propiedad industrial rige la materia en Colombia (Comunidad Andina, 2000). Una solicitud del Tratado de Cooperación en materia de Patentes (PCT) puede designar muchos países. Designar a Colombia no obliga al titular a entrar a la fase nacional (F-INF §6.6, p. 71). La {T:t21} lista las 15 patentes con su titular, su año, su oficina, su número y su TRL.

:::TABLA t21 | Principales titulares de patentes del corpus con oficina, número y TRL
| Documento | Titular según el informe | Año | Oficina | Número | TRL | Grupo | Colombia designada |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reintjes et al. (1995) | No identificado en el informe | 1995 | OMPI | WO 95/12118 A1 | 3 | G4 | No figura en el Anexo C |
| Abernathy et al. (2019) | General Electric | 2019 | OEP | EP 3 483 800 A1 | 3 | G4 | No figura en el Anexo C |
| Koppinen et al. (2019) | VTT | 2019 | OMPI | WO 2019/215392 A1 | 3 | G4 | Sí (Anexo C) |
| Blythe y Hohman (2020) | Monte Cristo | 2020 | OEP | EP 3 623 453 A1 | 4 | G4 | No figura en el Anexo C |
| Gumaste et al. (2021) | Cummins | 2021 | OMPI | WO 2021/061603 A1 | 4 | G4 | Sí (Anexo C) |
| Ali et al. (2022) | No identificado en el informe | 2022 | OMPI | WO 2022/217342 A1 | 3 | G4 | Sí (Anexo C) |
| Izod y Burch (2023) | Healthy Space | 2023 | OMPI | WO 2023/139267 A1 | 3 | G5 | Sí (Anexo C) |
| Hurst et al. (2024) | General Electric | 2024 | OEP | EP 3 483 686 B1 | 3 | G4 | No figura en el Anexo C |
| Røine (2024) | Airthings | 2024 | OMPI | WO 2024/080881 A1 | 2 | G5 | Sí (Anexo C) |
| Wilson et al. (2024) | View | 2024 | OMPI | WO 2024/064927 A1 | 3 | G5 | Sí (Anexo C) |
| Eckenrode y Stevenson (2025) | Auros | 2025 | OMPI | WO 2025/049390 A2 | 3 | G5 | Sí (Anexo C) |
| Hale et al. (2025) | Disney | 2025 | OEP | EP 4 617 736 A1 | 3 | G4 | No figura en el Anexo C |
| Machida y Ammendola (2025) | Ambient X | 2025 | OMPI | WO 2025/257740 A1 | 4 | G5 | Sí (Anexo C) |
| Acosta y Horstmann (2026) | CosySense | 2026 | OMPI | WO 2026/093802 A1 | 3 | G5 | Sí (Anexo C) |
| Spasojevic Brkic et al. (2026) | SmartMiner | 2026 | OMPI | WO 2026/180852 A1 | 4 | G5 | Sí (Anexo C) |
:::NOTA *Nota.* Elaboración propia con datos de F-INF §13.2 (p. 212), §4.1, Tabla 13 (p. 29), §5.7 (p. 55), §6.1 (p. 56) y Anexo C (p. 221). Titulares tomados del texto del informe; dos patentes no tienen titular identificado. OMPI: Organización Mundial de la Propiedad Intelectual; OEP: Oficina Europea de Patentes. Naturaleza: DOCUMENTADO; verificación: PARCIALMENTE_VERIFICADO. Año de corte 2026.

El titular se identifica en 13 de las 15 patentes. General Electric aparece dos veces, con Abernathy et al. (2019) y Hurst et al. (2024). Esas dos patentes comparten 50,1 % de los fragmentos de ocho palabras (F-INF §3.1, p. 19). Los demás titulares aparecen una sola vez. Las patentes se agrupan por función: medición de partículas, gestión de activos industriales, calificación de edificios y exposición ocupacional (F-INF §4.8, p. 41).

Las clases de la clasificación internacional de patentes de cada documento no se tabularon en el informe (VACIO). El informe propone cinco clases para vigilar la calidad del aire (F-INF Anexo D, p. 222). Son F24F, G01N 33, B01D 46, B01D 53 y G08B 21/12. Esa lista es PROPUESTO y no describe el corpus actual. El proyecto adopta una consecuencia práctica. Tabulará las clases de los 15 documentos en la primera ejecución de la ecuación E2 y las comparará con la lista propuesta. Hasta entonces, la lectura por clase queda pendiente.

### 2.3.2 Tendencia de patentamiento

La tendencia de patentamiento se lee por año de publicación. Hay una patente de 1995 y dos de 2019. Hay una por año de 2020 a 2023, tres en 2024, tres en 2025 y dos en 2026. Catorce de las 15 son de 2016 a 2026, y 10 de las 15 son de 2022 a 2026. El número crece de forma modesta, con dos o tres publicaciones por año desde 2024. Con 15 patentes, la serie no permite estimar una tasa de crecimiento.

El aumento de solicitudes no se acompaña de más evidencia. La robustez media de las patentes es 3,20 en 2024, 2,93 en 2025 y 3,00 en 2026. Fue 3,55 en 2019 y 3,80 en 1995 (F-INF §4.3, p. 34). Dos posiciones interpretan el patrón. La primera sostiene que el patentamiento anuncia tecnología madura. La segunda sostiene que las patentes describen sin demostrar. Los datos favorecen la segunda. El TRL medio de las patentes es 3,20. Además, 10 de las 15 tienen documentos de categoría X, Y o PX en su informe de búsqueda (F-INF §3.1, Tabla 3, p. 19). Esos documentos debilitan la novedad de los conceptos generales (F-INF §5.7, p. 55).

### 2.3.3 Libertad de operación

El análisis de libertad de operación parte de las diez solicitudes PCT que designan a Colombia (F-INF Anexo C, p. 221). La {T:t22} y la {F:patentes} presentan cada solicitud con su prioridad, su plazo de 30 meses y su estado al 13 de octubre de 2026. Los plazos son un cálculo del analista del informe con conocimiento externo y siguen NO_VERIFICADO. El estado real de cada expediente lo establece la consulta a la SIC. La última columna de la tabla es una inferencia de esta corrida y no un análisis jurídico.

:::TABLA t22 | Solicitudes PCT con Colombia designada, plazo de fase nacional y relación con el diseño
| Solicitud | Documento | Titular según el informe | Prioridad o presentación | Plazo de 30 meses | Estado al 13/10/2026 | Días restantes | Relación con el diseño del proyecto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WO 2019/215392 A1 | Koppinen et al. (2019) | VTT | 11/05/2018 | 11/11/2020 | Vencido | No aplica | Baja: sensor termoforético de partículas; el proyecto usa un sensor óptico |
| WO 2021/061603 A1 | Gumaste et al. (2021) | Cummins | 23/09/2019 | 23/03/2022 | Vencido | No aplica | Baja: gemelo digital de unidades reemplazables en motores |
| WO 2022/217342 A1 | Ali et al. (2022) | titular sin identificar | 14/04/2021 | 14/10/2023 | Vencido | No aplica | Media a alta: modelo entrenado para un parámetro del aire, análogo a la corrección en el gateway |
| WO 2023/139267 A1 | Izod y Burch (2023) | Healthy Space | 21/01/2022 | 21/07/2024 | Vencido | No aplica | Baja: riesgos de salud en espacios cerrados |
| WO 2024/064927 A1 | Wilson et al. (2024) | View | 23/09/2022 | 23/03/2025 | Vencido | No aplica | Baja: calificación de salud de edificios |
| WO 2024/080881 A1 | Røine (2024) | Airthings | 12/10/2022 | 12/04/2025 | Vencido | No aplica | Baja: retiro de CO2 del aire interior |
| WO 2025/049390 A2 | Eckenrode y Stevenson (2025) | Auros | 28/08/2023 | 28/02/2026 | Vencido | No aplica | Baja: descarbonización de edificios |
| WO 2025/257740 A1 | Machida y Ammendola (2025) | Ambient X | 10/06/2024 | 10/12/2026 | Abierto | 58 | Media: monitoreo multimodal que estima sílice respirable a partir del PM2,5 |
| WO 2026/093802 A1 | Acosta y Horstmann (2026) | CosySense | 28/10/2024 | 28/04/2027 | Abierto | 197 | Baja: gestión del ambiente construido |
| WO 2026/180852 A1 | Spasojevic Brkic et al. (2026) | SmartMiner | 28/02/2025 (presentación) | 28/08/2027 | Abierto | 319 | Media a alta: monitoreo de condiciones de trabajo en maquinaria de movimiento de tierras |
:::NOTA *Nota.* Elaboración propia con datos de F-INF Anexo C, Tabla 68 (p. 221), §1.3 (p. 10), §5.7 (p. 55) y §13.2. Días restantes calculados al 13 de octubre de 2026; el informe los calculó al 30 de septiembre de 2026 (71, 210 y 332 días). Plazos con conocimiento externo: NO_VERIFICADO. La relación con el diseño es INFERIDO y requiere análisis jurídico. Año de corte 2026.

:::FIGURA patentes | Línea de tiempo de las patentes del corpus y de los plazos de fase nacional en Colombia | Nota. Elaboración propia con matplotlib a partir de F-INF Anexo C (p. 221), §5.7 (p. 55) y §13.2 (p. 212). Marcador: año de publicación; barra: ventana de 30 meses desde la prioridad; corte al 13 de octubre de 2026. Plazos con conocimiento externo: NO_VERIFICADO. 15 patentes; año de corte 2026.

Siete solicitudes tienen vencido el plazo de 30 meses. Tres siguen abiertas. Machida y Ammendola (2025) cierra el 10 de diciembre de 2026, Acosta y Horstmann (2026) el 28 de abril de 2027 y Spasojevic Brkic et al. (2026) el 28 de agosto de 2027. Ninguna solicitud informa la fase nacional (F-INF §5.7, p. 55). Si el titular no entró a la fase nacional dentro del plazo, la tecnología sería de uso libre en Colombia (INFERIDO). La patente más antigua, Reintjes et al. (1995), tiene prioridad de 1993 y superó la vigencia de 20 años (F-INF §5.7, p. 55).

Cuatro patentes ofrecen métodos de calibración, autocalibración o medición de partículas sin datos de desempeño. Son Koppinen et al. (2019), Ali et al. (2022), Wilson et al. (2024) y Spasojevic Brkic et al. (2026) (F-INF §1.3, p. 10). Las tres primeras tienen el plazo vencido. La cuarta sigue abierta. Su título menciona maquinaria de movimiento de tierras, un contexto cercano a la remoción de escombros. Es la única de las abiertas con esa mención (INFERIDO). Su análisis tiene prioridad.

Dos posiciones orientan el manejo del riesgo. La primera propone evitar toda tecnología con solicitudes abiertas. La segunda propone consultar primero el estado nacional y decidir después. La segunda es la que sigue el informe de vigilancia, porque designar a Colombia no implica entrar a la fase nacional. Teece (1986) analiza cómo los mecanismos de apropiación determinan quién captura el valor de una innovación. En esa lógica, una designación que el titular no ejerce no excluye a terceros (INFERIDO). El informe de la SIC describe un procedimiento con dos ecuaciones para identificar tecnologías en dominio público (SIC, 2026, pp. 4-9). El informe de vigilancia propone replicarlo para la calidad del aire. Plantea que al menos 30 % de las solicitudes nacionales de esa materia están en dominio público (F-INF §5.7, p. 55). Esa cifra es una hipótesis y no un dato.

El proyecto presupuesta 150 horas de consultoría jurídica en propiedad intelectual y libertad de operación, por 45 millones de pesos colombianos (COP). Es la línea S02 y su naturaleza es DECLARADO. También registra el riesgo R-JUR-01. Una solicitud de terceros afecta la libertad de operación con probabilidad de 20 % y un impacto de COP 100 millones. El valor monetario esperado es de COP 20 millones (CALCULADO). Tres acciones se proponen (PROPUESTO). Primera, consultar el estado nacional de las diez solicitudes durante el primer mes de ejecución con el procedimiento que publica la SIC (SIC, 2026, pp. 2, 7 y 9). Segunda, vigilar los tres vencimientos abiertos con alertas anteriores a cada fecha. Tercera, someter el diseño final del nodo y del gateway a un análisis jurídico de reivindicaciones con las horas de la línea S02.

### 2.3.4 Evidencia de validación en las patentes

Ninguna patente del corpus reporta validación con verdad de referencia (F-INF §1.3, p. 10). El resultado abarca las 15 patentes. Las patentes afirman ventajas frente a las prácticas convencionales, como exactitud, costo o energía. Ningún documento las demuestra (F-INF §6.1, p. 56). Esa ausencia define el papel de las patentes en el proyecto. Sirven como señal de libertad de operación y como inventario de ideas. No sirven como evidencia de desempeño.

La consecuencia es que el proyecto genera su propia evidencia en el tramo 1. Coloca tres monitores gravimétricos de referencia, uno por departamento, junto a los nodos del piloto de 30 nodos y tres gateways. Compara las lecturas corregidas con los umbrales de la EPA (EPA, 2021). Esos umbrales son R² de 0,70 o más y NRMSE de 30 % o menos (PROPUESTO). El resultado alimenta la compuerta C1 al mes 12. Así el proyecto convierte la ausencia de validación en las patentes en su propia hipótesis verificable.
