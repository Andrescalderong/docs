%% PREFIJO: 14
# Capítulo 14. Sostenibilidad

La sostenibilidad de la red se diseña con una premisa que condiciona todo el capítulo. La premisa de diseño PD-0 establece que ninguna entidad pública puede asumir el sostenimiento de la solución al cierre. PD-0 es un SUPUESTO de diseño. No afirma la incapacidad de una entidad concreta. Obliga a que la solución sobreviva sin depender de esa capacidad. La sostenibilidad de los programas comunitarios de salud se explica por condiciones del diseño, del entorno organizacional y del entorno comunitario (Shediac-Rizkallah y Bone, 1998). El capítulo adopta ese marco y lo aplica a cinco dimensiones: técnica, financiera, institucional, social y de salida.

La evidencia sobre la continuidad de las redes de monitoreo es parcial. En Brasil, 96 de 570 estaciones, es decir 16,8 %, están inactivas o sin estado (Tavella et al., 2026, p. 6). En la propuesta de red nacional colombiana, 90,8 % de las estaciones serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13). El expediente E3 declara que algunos equipos terminan en bodegas municipales, sin cifra ni fuente (DECLARADO; NO_VERIFICADO). El informe de vigilancia tecnológica modela la calibración como un juego de bien público. Su equilibrio es que ninguna autoridad calibre (sección 6.5, INFERIDO). Ninguna fuente aportada evalúa la continuidad de proyectos financiados con regalías. La afirmación del usuario sobre antecedentes de baja sostenibilidad pública permanece DECLARADA, sin respaldo propio.

## 14.1 Sostenibilidad técnica

La sostenibilidad técnica es la capacidad de la solución para seguir midiendo con error conocido después del cierre. Se compone de tres actividades: mantener, actualizar y documentar. El artefacto de ingeniería es un producto que debe describirse con detalle suficiente para que otros lo reproduzcan y lo evalúen (Hevner et al., 2004). Esa exigencia convierte la documentación en parte del producto y no en un anexo. La solución consta de nueve componentes según la sección 4.4-MDR.10. La {T:t01} los inventaría con su función, sus dependencias y el estado de su costo anual.

:::TABLA t01 | Inventario de componentes de la solución y estado de su costo anual
| Componente | Tipo | Función | Dependencias | Costo anual con fuente |
| --- | --- | --- | --- | --- |
| Nodos sensoriales (M1) | Activos físicos | Miden PM2,5, PM10, temperatura y humedad | Energía; enlace de radio de largo alcance | VACIO por componente; línea agregada de repuestos en E3 |
| Gateways con corrección local (M2) | Activos físicos y software | Corrigen el error en sitio y reenvían los datos | Energía estable; enlace celular o satelital | VACIO |
| Gemelo digital (M3) | Software y datos | Estimación espacial y reentrenamiento del modelo | Nube; datos de M2 | Línea agregada de operación en E3 |
| Tablero de alertas (M4) | Software y servicio | Índice local y alertas | M3; fórmula local validada | VACIO |
| Series de datos | Datos | Base maestra de mediciones | Licencia y propiedad | VACIO |
| Protocolo de calibración y sorteo | Conocimiento | Referencia y contraste | Monitores gravimétricos | VACIO |
| Operación y soporte | Servicio | Mantenimiento y soporte algorítmico | Personal certificado | Línea agregada de personal en E3 |
| Usuarios institucionales | Red de usuarios | Uso del tablero en protocolos | Acuerdos y capacitación | VACIO |
| Modelos y código | Propiedad intelectual | Corrección local y gemelo digital | Libertad de operación | VACIO |
:::NOTA *Nota.* Elaboración propia a partir de la sección 4.4-MDR.10 y de la ficha maestra. Naturaleza: PROPUESTO; verificación: NO_VERIFICADO. VACIO: dato que solo el usuario o los términos de referencia pueden aportar.

La {T:t01} muestra que solo tres líneas agregadas de costo existen, todas del expediente E3: repuestos, operación del gemelo y personal. Seis componentes carecen de costo anual con fuente. Por eso el plan técnico no puede fijar un presupuesto posterior por componente. Fija responsabilidades, productos de documentación y un orden de prioridad de los recursos que sí se conocen.

El mantenimiento enfrenta una disyuntiva entre reparar al fallar y recalibrar de forma periódica. La primera posición minimiza visitas y exige un inventario amplio de repuestos. La segunda posición exige comparar los nodos con una referencia a intervalos fijos. Los sensores ópticos de bajo costo cambian su respuesta con el tiempo y con el entorno (Karagulian et al., 2019). Giordano et al. (2021) y Malings et al. (2020) respaldan la segunda posición: la calibración con referencia y la evaluación de largo plazo reducen el sesgo de estos sensores. El proyecto adopta una combinación. Programa seis ciclos de calibración, dos por tramo (PERS-R02), y cuatro rotaciones de colocalización por departamento (PERS-R05). Reserva 60 millones de COP para repuestos (M07) y 20 nodos de reserva.

La limitación posproyecto es la cobertura de referencias. El presupuesto incluye tres monitores gravimétricos, uno por departamento (E03), y un banco de calibración de laboratorio (E07). Para 100 nodos, esa dotación solo sostiene rotaciones, no una comparación continua. Además, el análisis gravimétrico depende de 1.200 filtros de membrana (M01) y de 240 muestras en laboratorio acreditado (S01), cuyo costo posterior es NO_CALCULABLE. La consecuencia metodológica es que el protocolo de calibración se transfiere como componente propio, con un custodio que asuma las rotaciones y el laboratorio. Ese componente se entrega en el tramo 1 de transferencia, tras el contraste del piloto.

La actualización tecnológica combina tres cambios: el firmware de los nodos, el modelo de corrección y la plataforma. El firmware se actualiza por lote y no por nodo aislado, para no multiplicar versiones. El modelo de corrección cambia con cada ciclo de calibración, y el registro de versiones conserva la historia de parámetros. La plataforma depende del servicio en la nube (E10, 180 millones de COP por 24 meses). También depende del software de analítica (E11, 45 millones). La capacidad de la red presenta además límites físicos. Adelantado et al. (2017) muestran que el protocolo LoRaWAN limita el número de dispositivos por gateway por la saturación del canal. El diseño de un gateway por cada 10 nodos limita la carga por gateway, y el piloto del tramo 1 debe verificarlo (SUPUESTO).

El gemelo digital exige una definición explícita, porque el término carece de acepción común. El informe de vigilancia tecnológica encuentra cinco acepciones en al menos 11 documentos (sección 1.3). Grieves y Vickers (2017) lo describen como la pareja de un sistema físico y su réplica virtual conectada. Tao et al. (2019) revisan sus aplicaciones industriales y muestran implementaciones muy distintas. Aquí el gemelo digital es una estimación espacial de la concentración alimentada por los datos corregidos. Esa definición se documenta en el diccionario de datos y en el manual de operación. Así un custodio nuevo no la confunde con una simulación física.

La documentación técnica final reúne ocho productos. Son la hoja de vida de cada nodo, el manual de reactivación, el diccionario de datos y el registro de versiones del modelo. Son también el protocolo de calibración, el manual del tablero, el protocolo de alerta y los instrumentos de licencia. La libertad de operación requiere una consulta jurídica. El informe de vigilancia tecnológica advierte que diez solicitudes de patente designan a Colombia. Ninguna informa su fase nacional (sección 1.3). El presupuesto prevé 150 horas de consultoría en propiedad intelectual (S02, 45 millones de COP). Prevé también el registro del software ante la Dirección Nacional de Derecho de Autor (DNDA) (O03, 15 millones). La {T:t02} resume el plan técnico por componente.

:::TABLA t02 | Plan de sostenibilidad técnica por componente
| Componente | Mantenimiento | Actualización | Documentación | Partidas del proyecto |
| --- | --- | --- | --- | --- |
| Nodos sensoriales | Limpieza y reemplazo de cabezales, baterías y paneles con repuestos | Firmware por lote; reposición de cabezales según su edad | Hoja de vida por nodo y manual de reactivación | E01, E02, E05, M03 y M07 |
| Gateways con corrección local | Revisión de energía, enlace celular y satelital y almacenamiento de 7 días | Versión del modelo tras cada ciclo de calibración (6 ciclos) | Registro de versiones del modelo | E04, E06, E12 y S10 |
| Gemelo digital y datos | Instancias en la nube, repositorios y copias de seguridad | Reentrenamiento con nuevos pares nodo-referencia | Diccionario de datos y definición del gemelo | E10, E11 y S03 |
| Tablero y alertas | Mantenimiento correctivo del tablero y del servicio de alertas | Revisión de la fórmula local y de los umbrales con la autoridad de salud | Manual del tablero y protocolo de alerta | M04 y WP3 |
| Protocolo de calibración y sorteo | Rotaciones de colocalización con la referencia (4 por departamento) | Ajuste del protocolo ante cambios de sensor | Protocolo escrito y bitácora de la referencia | E03, E07, S01 y M01 |
| Modelos y código | Gestión de versiones y de licencias | Consulta periódica de libertad de operación | Código, manual y licencia | O03 y S02 |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (líneas de presupuesto y indicadores PERS-R02 y PERS-R05). Naturaleza: PROPUESTO. Las frecuencias de mantenimiento posteriores al cierre son VACIO y se fijan en el manual de operación.

La {T:t02} asigna a cada componente una partida del presupuesto vigente y un producto de documentación verificable. Solo los ciclos de calibración y las rotaciones cuentan con cantidad en la ficha de indicadores. Las demás frecuencias quedan como VACIO hasta que el manual de operación las fije con base en la experiencia del piloto. Esa decisión evita comprometer una frecuencia sin evidencia de campo.

## 14.2 Sostenibilidad financiera

La sostenibilidad financiera se evalúa con el costo total de sostenimiento (CTS) anual. La fórmula suma operación, personal, licencias, mantenimiento, reposición y gobernanza. La reposición anual equivale al costo del activo dividido entre su vida útil. El expediente E3 declara tres de los seis rubros en su Tabla 14.2. Faltan licencias, reposición y gobernanza. Por tanto, el CTS anual es NO_CALCULABLE. Solo existe una cota inferior declarada. Vale 190,00, 208,25 y 226,91 millones de COP en los años 1, 2 y 3 posteriores al proyecto (CALCULADO sobre cifras PROPUESTAS; NO_VERIFICADO). Esa cota no incluye ahorro ni inversión inicial. El nivel mínimo de servicio comprende nodos de referencia verificados, un tablero con umbrales vigentes, conservación y publicación de datos y mantenimiento correctivo. Su costo anual también es NO_CALCULABLE, porque ningún rubro está desagregado por componente.

Dos posiciones se disputan el modelo financiero posterior al proyecto. La primera sostiene que la gestión del riesgo es una función pública y que su costo recurrente corresponde al presupuesto de las entidades territoriales. La Ley 1523 de 2012 atribuye competencias de gestión del riesgo a esas entidades (Congreso de la República, 2012), dato CANDIDATO_A_VERIFICAR. La segunda posición sostiene que el servicio necesita un portafolio de aportes de varios actores. La estabilidad de la financiación figura entre las condiciones que explican la continuidad de un programa (Shediac-Rizkallah y Bone, 1998). El proyecto adopta la segunda posición para el costo recurrente y conserva la primera para la competencia legal sobre la alerta. Esa combinación coincide con la síntesis de la sección 4.4-MDR.9.

La referencia de escala de una red sostenida existe en Colombia. El Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) opera 65 equipos acreditados y 450 sensores de bajo costo. Su inversión es de 1,63 dólares por habitante y año (Ruiz-Carrascal et al., 2026, pp. 3 y 8). Su trayectoria supera los 20 años según el título de la fuente. Esa red muestra que la continuidad es posible con una institución estable y un presupuesto recurrente. No es un modelo transferible sin más. La red de este proyecto opera en sitios de remoción temporales y sin una institución con presupuesto permanente comprometido. El proyecto toma la cifra solo como orden de magnitud del esfuerzo recurrente que una red sostenida requiere.

La {T:t03} presenta la proyección financiera posterior al proyecto con las cifras que E3 declara en su Tabla 14.2. Las cifras se reutilizan sin cambio y se rotulan CALCULADO sobre cifras NO_VERIFICADO. La tabla no incluye ingresos, porque ninguno cuenta con fuente.

:::TABLA t03 | Proyección financiera posproyecto: costo parcial declarado, concentración y ausencia de ingresos
| Fuente declarada | Año 1 | Participación año 1 | Año 2 | Participación año 2 | Año 3 | Participación año 3 |
| --- | --- | --- | --- | --- | --- | --- |
| Secretarías TIC municipales (operación de nube e IoT) | 45,00 | 23,7 % | 47,25 | 22,7 % | 49,61 | 21,9 % |
| Convenio de ARL y corporación autónoma (mantenimiento y repuestos) | 25,00 | 13,2 % | 35,00 | 16,8 % | 45,00 | 19,8 % |
| IES regional y UNGRD en especie (personal técnico y soporte) | 120,00 | 63,2 % | 126,00 | 60,5 % | 132,30 | 58,3 % |
| Total declarado (costo parcial, cota inferior) | 190,00 | 100,0 % | 208,25 | 100,0 % | 226,91 | 100,0 % |
| Participación máxima | — | 63,2 % | — | 60,5 % | — | 58,3 % |
| Índice HHI | — | 0,472 | — | 0,446 | — | 0,427 |
| Costo total de sostenimiento | NO_CALCULABLE | — | NO_CALCULABLE | — | NO_CALCULABLE | — |
| Ingresos propios del servicio | VACIO | — | VACIO | — | VACIO | — |
| Punto de equilibrio | NO_CALCULABLE | — | NO_CALCULABLE | — | NO_CALCULABLE | — |
:::NOTA *Nota.* Elaboración propia con la sección 4.4-MDR.10 y la Tabla 14.2 del expediente E3 (millones de COP). Naturaleza: CALCULADO sobre cifras PROPUESTAS; verificación: NO_VERIFICADO. Los umbrales de concentración de 50 % y 0,40 son convenciones locales PROPUESTAS. IES: institución de educación superior. ARL: administradora de riesgos laborales. HHI: índice de Herfindahl-Hirschman. UNGRD: Unidad Nacional para la Gestión del Riesgo de Desastres. TIC: tecnologías de la información y las comunicaciones.

La {T:t03} permite leer tres resultados. El costo parcial crece de 190,00 a 226,91 millones de COP en tres años. La participación máxima supera 50 % en los tres años. El índice de Herfindahl-Hirschman (HHI), que suma los cuadrados de las participaciones, supera 0,40. Ambos valores incumplen las convenciones locales PROPUESTAS. La fuente concentrada es el personal técnico en especie. E3 lo asigna a la institución de educación superior (IES) y a la Unidad Nacional para la Gestión del Riesgo de Desastres (UNGRD). Ese aporte contradice la falta de recursos permanentes de la institución ejecutora que el mismo expediente declara (E3-P17).

La prueba de orfandad mide cuánto soporta el portafolio si una fuente desaparece. Para cada fuente se compara la suma de las demás con el costo mínimo anual del servicio. Si la suma es menor, la fuente es CRITICA. El costo mínimo es NO_CALCULABLE, y por eso se calcula el umbral que vuelve crítica a cada fuente con las cifras del año 1. La {T:t04} presenta esos umbrales.

:::TABLA t04 | Prueba de orfandad del portafolio declarado en el año 1
| Fuente | Suma de las demás fuentes, año 1 (millones de COP) | Condición para que la fuente sea CRITICA |
| --- | --- | --- |
| IES regional y UNGRD en especie | 70 | Costo mínimo anual mayor que 70 |
| Secretarías TIC municipales | 145 | Costo mínimo anual mayor que 145 |
| Convenio de ARL y corporación autónoma | 165 | Costo mínimo anual mayor que 165 |
:::NOTA *Nota.* Elaboración propia con la sección 4.4-MDR.10 (millones de COP). Naturaleza: CALCULADO sobre cifras NO_VERIFICADO. El costo mínimo anual del servicio es NO_CALCULABLE.

La {T:t04} arroja una consecuencia directa. La fuente en especie resulta CRITICA con cualquier nivel mínimo de servicio que cueste más de 70 millones de COP al año. El soporte técnico declarado cuesta 120 millones. Si el nivel mínimo incluye ese soporte, la prueba invalida el portafolio declarado y reabre la asignación de custodia. Además, esa fuente incluye a una entidad pública, la UNGRD, lo que contradice la premisa PD-0. La conclusión es condicional al costo mínimo, que falta. La acción que la resuelve es cotizar cada componente y fijar la vida útil de cada activo.

El fondo patrimonial es una vía descartada por falta de datos. El capital requerido sería K, igual al costo total cubierto dividido entre la rentabilidad real anual, como en toda renta perpetua (Boardman et al., 2018). K es NO_CALCULABLE, porque ni el CTS completo ni la rentabilidad real cuentan con fuente. El proyecto no propone constituir un fondo. Propone, en cambio, financiar con el SGR la preparación de la transferencia. Esa preparación usa partidas del presupuesto vigente. La partida S09 asigna 150 millones de COP a la formación y el soporte de custodios, en tres tramos de 50 millones. La partida P14 asigna 168 millones al profesional de convenios y custodia. El lote de repuestos M07 suma 60 millones y las instancias en la nube E10 suman 180 millones por 24 meses.

El modelo de negocio posproyecto no se formula con ingresos, porque ninguno cuenta con fuente. Teece (1986) sostiene que capturar el valor de una innovación depende del régimen de apropiación y de los activos complementarios. Chesbrough (2003) sostiene que abrir la innovación a socios puede ampliar el valor capturado. Ambas posiciones requieren un mercado identificable, y el expediente no aporta ninguno (VACIO). El proyecto describe fuentes posibles y sus condiciones. Los instrumentos de la {T:t05} son CANDIDATO_A_VERIFICAR: no se consultó su fuente controlante y no se afirma su vigencia.

:::TABLA t05 | Fuentes posibles de financiación posproyecto y condiciones de uso
| Instrumento | Uso posible | Condición previa | Estado |
| --- | --- | --- | --- |
| Vigencias futuras | Comprometer el gasto recurrente después del cierre | Competencia y autorización de cada entidad | CANDIDATO_A_VERIFICAR |
| Asociaciones público-privadas | Operación con una empresa por contrato | Modelo de negocio y valoración del servicio | CANDIDATO_A_VERIFICAR |
| Convenios de cofinanciación | Aportes de ARL y autoridades ambientales | Carta de compromiso y partida | CANDIDATO_A_VERIFICAR |
| Pago por resultados | Pago ligado a disponibilidad y verificación | Indicador verificable y línea base | CANDIDATO_A_VERIFICAR |
| Corporaciones mixtas de ciencia, tecnología e innovación | Vehículo operador de la red | Acto de constitución y gobierno | CANDIDATO_A_VERIFICAR |
| Obras por impuestos y beneficios tributarios | Financiación por el sector privado | Elegibilidad de la red como proyecto | CANDIDATO_A_VERIFICAR |
| Reglas de operación y mantenimiento de proyectos con regalías | Límites o habilitación del gasto recurrente | Texto de los términos de referencia (VACIO) | CANDIDATO_A_VERIFICAR |
:::NOTA *Nota.* Elaboración propia con la sección 4.4-MDR.10. Ninguna fuente se presupuesta. Las reglas del Sistema General de Regalías se regulan en la Ley 2056 de 2020 (Congreso de la República, 2020), cuyo texto no se consultó.

La {T:t05} deja claro que ninguna fuente está lista para comprometerse. Cada fila exige un documento que hoy no existe: una carta, una partida, un acto o un indicador. La cobertura del costo mínimo debe superar 100 % de forma sostenida. Si cae por debajo de ese valor durante dos trimestres consecutivos, se activa la cláusula de apertura descrita en el plan de salida. El punto de equilibrio es NO_CALCULABLE, porque requiere ingresos y un costo mínimo que no existen.

La ruta de escala requiere un propietario. La regla H36-07 exige que toda ruta de escala identifique cinco datos. Son el actor que adopta, el recurso requerido, la unidad de expansión, el costo marginal y la decisión que habilita la expansión. El motor MESS36 marca ASPIRACIONAL toda afirmación de escalabilidad que carezca de actor adoptante, recurso y mecanismo de expansión. La unidad de expansión del proyecto es un gateway con 10 nodos. Su costo marginal es de 120,08 millones de COP (CALCULADO). Incluye adquisición, instalación y 24 meses de conectividad, con precios unitarios de la ficha. Excluye importación, personal, nube y calibración. La {T:t06} aplica las 11 variables de MESS36.

:::TABLA t06 | Ruta de escala con propietario: variables del motor MESS36
| Variable | Contenido para el proyecto | Estado |
| --- | --- | --- |
| Propietario de la escala | Actor adoptante no identificado [DATO_USUARIO: custodio o gobernación que adopta] | VACIO |
| Mecanismo de adopción | Opciones de ampliación: más nodos, un cuarto tramo o un año adicional de custodia | PROPUESTO; sin presupuesto |
| Recurso financiero | Sin partida; depende de términos de referencia y de custodios | VACIO |
| Costo marginal | 120,08 millones de COP por unidad de 10 nodos y un gateway | CALCULADO |
| Capacidad operativa | ICAR de los candidatos | NO_CALCULABLE |
| Marco regulatorio | Términos de referencia no aportados | VACIO |
| Demanda | 15 comités focalizados; línea base de uso institucional | VACIO |
| Mantenimiento | Plan técnico por componente (14.1) | PROPUESTO |
| Gobernanza | Órgano de gobierno con veto por componente | PROPUESTO |
| Distribución de beneficios | Sin análisis de quién recibe los beneficios | VACIO |
| Aprendizaje pendiente | Supuestos SC-1 a SC-4 y línea base en el tramo 1 | PROPUESTO |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (partidas E01, E02, E04, E05, E06, E12, M03, S05 y S10) y la especificación MESS36. Costo marginal: 10 × (4,5 + 1,2 + 0,65 + 0,35) + 28 + 3,5 + 11 × 1,2 + 24 × 0,12 + 22 × 0,25 = 120,08 millones de COP. Resultado de la prueba: ASPIRACIONAL. ICAR: índice de capacidad de absorción de los custodios.

La {T:t06} concluye que la ruta de escala es ASPIRACIONAL. Existe el costo marginal, pero faltan el actor adoptante, el recurso y el marco regulatorio. El proyecto no afirma escalabilidad. Declara qué dato permitiría afirmarla: un custodio con partida y competencia que adopte una unidad de expansión. La {F:f01} resume el modelo de sostenibilidad financiera. El panel izquierdo muestra el costo parcial declarado por fuente. El panel derecho muestra los umbrales de la prueba de orfandad.

:::FIGURA f01 | Modelo de sostenibilidad financiera: costo parcial declarado y prueba de orfandad | Nota. Elaboración propia con la sección 4.4-MDR.10 (millones de COP; cifras del expediente E3, CALCULADO sobre cifras PROPUESTAS; NO_VERIFICADO). El costo total de sostenimiento y el punto de equilibrio son NO_CALCULABLE. Generada con matplotlib sin parámetros aleatorios.

La {F:f01} muestra que el portafolio declarado depende de una sola fuente en especie. Su participación baja de 63,2 % a 58,3 % en tres años, pero sigue por encima de 50 %. Los umbrales de orfandad indican que el portafolio no resiste la salida de la fuente en especie. Esto ocurre si el servicio mínimo cuesta más de 70 millones de COP al año. Este resultado orienta la decisión. Antes de comprometer el portafolio, hay que cotizar el servicio mínimo.

## 14.3 Sostenibilidad institucional

La apropiación institucional es el grado en que una entidad incorpora el tablero y el protocolo en sus decisiones, con presupuesto, personal y competencia. Las instituciones son reglas que restringen la conducta (North, 1990). Las reglas formales difieren de las reglas en uso (Ostrom, 2005). Esa distinción importa aquí: un acto administrativo que asigna la alerta a una alcaldía no implica que el comité la use. El uso de una tecnología se explica por su utilidad percibida, por la influencia social y por las condiciones de apoyo (Rogers, 2003; Venkatesh et al., 2003). El proyecto mide la apropiación con PERS-E01: al menos 75 % de los 15 comités focalizados usa el tablero en decisiones documentadas al mes 24. La línea base es VACIO y se mide en el tramo 1.

Dos posiciones se oponen sobre quién debe recibir la operación. La tesis sostiene que las alcaldías deben recibirla. Responden legalmente por actuar sobre la alerta (E3-P17) y poseen competencias en gestión del riesgo (Congreso de la República, 2012), dato CANDIDATO_A_VERIFICAR. La antítesis sostiene que ninguna entidad pública puede sostener la solución sola. Tres hechos la respaldan. No existe compromiso firmado, la institución ejecutora carece de recursos permanentes y el equilibrio del juego de calibración es que nadie calibre. La síntesis de la sección 4.4-MDR.9 distribuye la operación técnica y el financiamiento entre custodios con capacidad demostrada. Las alcaldías conservan la competencia legal sobre la alerta. La tesis explica quién responde ante la ley. La antítesis explica por qué esa responsabilidad no basta para sostener la operación.

La capacidad instalada se mide con PERS-E03: al menos 60 personas certificadas en mantenimiento, lectura y operación. La línea base es cero (CALCULADO). La partida S09 financia la formación y el soporte con 150 millones de COP en tres tramos de 50 millones. La partida cubre solo la formación. Por eso el costo de 2,50 millones de COP por persona certificada no es el costo total de la capacidad. El personal de primera línea adapta las normas a su carga de trabajo (Lipsky, 1980). La rotación del personal, que registra la sección 4.4-MDR.4, borra la capacidad adquirida. La consecuencia es que la certificación exige evaluación práctica y que el convenio de cada custodio designa personal con permanencia. Esa condición alimenta el supuesto SC-4.

El índice de capacidad de absorción de los custodios (ICAR) puntúa seis dimensiones por candidato, de 0 a 3. Las dimensiones son financiera, talento, jurídica, técnica, continuidad y demanda. El resultado es el mínimo de las seis, sin compensación entre dimensiones. Ningún candidato cuenta con evidencia en las seis. Un custodio sin evidencia queda NO_EVALUADO y no en cero, porque asignar cero afirmaría una incapacidad que nadie ha demostrado. La {T:t07} registra la evidencia disponible por candidato y el resultado del índice.

:::TABLA t07 | Evidencia disponible por custodio candidato y resultado del ICAR
| Custodio candidato | Evidencia disponible | ICAR |
| --- | --- | --- |
| Alcaldías | Responden legalmente por actuar sobre la alerta (E3-P17); sin partida ni compromiso; DECLARADO | NO_CALCULABLE |
| Gobernaciones y unidades de gestión del riesgo | E3 propone ordenanzas; no existen | NO_CALCULABLE |
| UNGRD | Aporte en especie de personal declarado en E3, sin aval | NO_CALCULABLE |
| IDEAM y autoridades ambientales | Referencia metrológica descrita en el informe de vigilancia tecnológica; sin convenio | NO_CALCULABLE |
| Institución ejecutora | CONTRADICTORIO: sin recursos permanentes (E3-P17) frente a personal en especie declarado en E3 | NO_CALCULABLE |
| Empresa aliada | Responsable de código y propiedad intelectual (E3-P17); sin modelo de negocio | NO_CALCULABLE |
| ARL y corporación autónoma | Convenio de cofinanciación declarado en E3, sin evidencia | NO_CALCULABLE |
:::NOTA *Nota.* Elaboración propia con la sección 4.4-MDR.10. Naturaleza: DECLARADO en E3; verificación: NO_VERIFICADO. IDEAM: Instituto de Hidrología, Meteorología y Estudios Ambientales.

La {T:t07} muestra siete candidatos y ningún ICAR calculable. Cada fila indica qué documento falta: una partida, un acto, un convenio o un modelo de negocio. La asignación de custodios no puede decidirse hoy, y por eso el proyecto no asigna ninguna entidad por defecto. La condición para asignar es la evidencia en las seis dimensiones antes de cada tramo de transferencia. La {T:t08} fija las exigencias por componente y los candidatos, con el custodio asignado por definir.

:::TABLA t08 | Custodia distribuida por componente: exigencias, candidatos y custodio asignado
| Componente | Dimensiones del ICAR que exige | Candidatos | Custodio asignado |
| --- | --- | --- | --- |
| Nodos y repuestos | Técnica; talento | Empresa aliada; institución ejecutora | POR_DEFINIR con ICAR |
| Gemelo digital y datos | Financiera; técnica | Institución ejecutora; empresa aliada | POR_DEFINIR con ICAR |
| Tablero y alertas | Jurídica; demanda | Unidades de gestión del riesgo; alcaldías | POR_DEFINIR con ICAR |
| Protocolo de calibración | Técnica; continuidad | Autoridad ambiental; institución ejecutora | POR_DEFINIR con ICAR |
| Gobernanza y acuerdos | Jurídica; continuidad | Órgano de gobierno de la alianza | POR_DEFINIR |
:::NOTA *Nota.* Elaboración propia con la sección 4.4-MDR.10. Naturaleza: PROPUESTO. Ningún componente queda sin custodio o sin cláusula de apertura.

La {T:t08} cumple una regla de diseño: ningún componente queda sin custodio o sin cláusula de apertura. Cada componente exige dos dimensiones del índice como mínimo. El tablero y las alertas exigen capacidad jurídica y demanda, y por eso sus candidatos son las unidades de gestión del riesgo y las alcaldías. El protocolo de calibración exige capacidad técnica y continuidad, y por eso su candidato natural es una autoridad ambiental. Un componente sin custodio que cumpla la condición permanece bajo la alianza o pasa a la cláusula de apertura.

La gobernanza integra a los custodios en un órgano de la alianza. Lo componen la institución ejecutora, con ejecución técnica y custodia del conocimiento, y la empresa aliada, con desarrollo y mantenimiento tecnológico. También participan las alcaldías y gobernaciones, con uso de la alerta y competencia legal. Participa la autoridad ambiental o el IDEAM, con la referencia metrológica. Cierran el órgano las ARL o las constructoras, con cofinanciación y uso del dato. La regla de decisión PROPUESTA es la mayoría calificada con veto de cada custodio sobre su propio componente. Las reglas que combinan decisiones individuales en una decisión colectiva se llaman reglas de agregación (Ostrom, 2005). Los resultados de política surgen de la interacción de actores con capacidades y preferencias propias (Scharpf, 1997). Por eso el proyecto condiciona la conducta de los custodios con reglas y no la supone. La rendición es un informe anual público con tres indicadores. Son la capacidad de absorción de cada custodio, la cobertura del costo mínimo y la disponibilidad de nodos.

Los compromisos de continuidad se formalizan con instrumentos firmados. El expediente no contiene ninguno, y por eso el estado de todos es pendiente de firma. La {T:t09} lista el compromiso esperado de cada entidad, el instrumento que lo formaliza y la condición de recepción. La columna de estado marca el dato que el usuario debe aportar. Ningún compromiso se supone firmado.

:::TABLA t09 | Compromisos institucionales de continuidad y estado de formalización
| Entidad | Compromiso de continuidad esperado | Instrumento | Condición de recepción | Estado |
| --- | --- | --- | --- | --- |
| Alcaldías | Competencia legal sobre la alerta y uso del tablero en sus protocolos | Acto administrativo o carta de compromiso | Partida en el plan operativo anual y personal designado | Pendiente de firma [DATO_USUARIO: acto o carta de las alcaldías] |
| Gobernaciones y unidades de gestión del riesgo | Custodia del tablero y de las alertas por departamento | Convenio u ordenanza | Competencia jurídica documentada | Pendiente de firma [DATO_USUARIO: convenio u ordenanza departamental] |
| UNGRD | Aporte de personal y articulación con los puestos de mando | Convenio de cooperación | Aval y partida del aporte en especie | Pendiente de firma [DATO_USUARIO: convenio con la UNGRD] |
| IDEAM y autoridades ambientales | Referencia metrológica y custodia del protocolo de calibración | Convenio | Capacidad técnica y continuidad | Pendiente de firma [DATO_USUARIO: convenio con la autoridad ambiental] |
| Institución ejecutora | Custodia del conocimiento, del gemelo digital y de los datos | Convenio de ejecución y acta de cierre | Recursos permanentes que E3 declara ausentes | Pendiente de firma [DATO_USUARIO: nombre de la entidad ejecutora y convenio] |
| Empresa aliada | Mantenimiento tecnológico, código y propiedad intelectual | Acuerdo de titularidad y licencia | Modelo de negocio con fuente | Pendiente de firma [DATO_USUARIO: nombre de la empresa tecnológica y acuerdo] |
| ARL y corporación autónoma | Cofinanciación de mantenimiento y repuestos | Convenio de cofinanciación | Evidencia de la partida | Pendiente de firma [DATO_USUARIO: convenio de cofinanciación] |
| Órgano de gobierno de la alianza | Cláusula de apertura y salida ordenada | Acta de constitución del órgano | Firma antes del primer tramo de transferencia | Pendiente de firma [DATO_USUARIO: acta de constitución] |
:::NOTA *Nota.* Elaboración propia con la sección 4.4-MDR.10 y la ficha maestra (hito H8). Naturaleza: PROPUESTO. Los nombres de entidades y los instrumentos firmados son [DATO_USUARIO].

La {T:t09} muestra ocho compromisos y ocho estados pendientes. La compuerta C2 del mes 17 exige convenios de custodia con partida. Por eso los convenios de los custodios del tramo 2 deben firmarse antes de esa fecha. Los convenios del tramo 3 se firman en la actividad A3.3, después de C2. La condición de recepción protege el servicio. Sin partida, personal y competencia jurídica, la transferencia no ocurre y rige la cláusula de apertura.

## 14.4 Sostenibilidad social

La apropiación comunitaria es el proceso por el cual la población usa y exige el servicio sin depender del equipo del proyecto. La participación simbólica se distingue del poder real de decisión (Arnstein, 1969). Callon (1999) sostiene que las personas no expertas producen conocimiento útil cuando participan desde el diseño. La educación se construye en diálogo (Freire, 2005). Una posición sostiene que informar y consultar basta para que la comunidad use una alerta. La posición contraria sostiene que la comunidad solo sostiene lo que ayudó a definir. El proyecto adopta la segunda para los umbrales y la primera para los materiales. Compromete 29 actividades de apropiación, 20 talleres y 9 jornadas (PERS-P04), y al menos tres actividades de nivel 3 con acta firmada.

Las redes de soporte son los actores que mantienen el uso cuando el equipo se retira. Mitchell et al. (1997) proponen identificarlos por su poder, su legitimidad y su urgencia. En el proyecto, los comités de gestión del riesgo son 15, 12 municipales y 3 departamentales (SUPUESTO), con 150 funcionarios beneficiarios (SUPUESTO). E3 identifica además a los líderes de las juntas de acción comunal como canal para transmitir alertas simplificadas (DECLARADO; NO_VERIFICADO). La influencia social y las condiciones de apoyo figuran entre las causas del uso sostenido (Venkatesh et al., 2003). La difusión de una innovación depende de los canales de comunicación y del sistema social que la rodea (Rogers, 2003). La consecuencia es que el proyecto diseña el soporte como una red de comités, líderes y custodios con funciones definidas. No lo diseña como una dependencia de la entidad ejecutora.

Los mecanismos de continuidad social son cuatro. El primero es la formación de formadores locales, que cubre el nivel 4 de la escalera. Se mide con PERS-E03: al menos 60 personas certificadas. El segundo es el observatorio comunitario, que se declara aspiracional con una actividad que posea plan de sostenibilidad. El tercero son los materiales. El presupuesto financia 5.000 cartillas del índice y del protocolo de alerta (M04) y 20 laboratorios ciudadanos con alimentación (V05). El cuarto es la designación de personal permanente en cada convenio. El riesgo asociado es que los custodios no asuman la operación (R-ORG-02), con un valor monetario esperado de 60,0 millones de COP (CALCULADO). La {T:t10} presenta el plan de sostenibilidad social.

:::TABLA t10 | Plan de sostenibilidad social: mecanismos, actores, indicadores y metas
| Mecanismo | Actores | Indicador | Línea base | Meta | Naturaleza |
| --- | --- | --- | --- | --- | --- |
| Actividades de apropiación | Comunidad, operarios y comités | PERS-P04: actividades documentadas | 0 | 29 actividades (20 talleres y 9 jornadas) al mes 24 | DECLARADO; CALCULADO |
| Co-diseño de umbrales (nivel 3) | Comités, autoridad de salud y comunidad | Actividades de nivel 3 con acta firmada | 0 | Mínimo 3 | DECLARADO |
| Uso institucional del tablero | 15 comités y 150 funcionarios | PERS-E01: comités con decisión documentada | VACIO | ≥ 75 % al mes 24 | DECLARADO; SUPUESTO |
| Formación de formadores locales | Custodios y líderes locales | PERS-E03: personas certificadas | 0 | ≥ 60 personas | DECLARADO; CALCULADO |
| Observatorio comunitario (nivel 4) | Comunidad y custodios | Actividad con plan de sostenibilidad | 0 | 1 (aspiracional) | PROPUESTO |
| Continuidad bajo custodia | Custodios con partida | PERS-S02: nodos operados a los 12 meses del cierre | VACIO | ≥ 70 % | DECLARADO |
| Materiales de apropiación | Población y funcionarios | Cartillas del índice y del protocolo (M04) | 0 | 5.000 unidades presupuestadas | DECLARADO |
:::NOTA *Nota.* Elaboración propia con la ficha de indicadores PERS y la ficha maestra (líneas M04 y V05). Los comités y funcionarios son SUPUESTO. Los indicadores PERS-S01 y PERS-S02 se miden 6 a 12 meses después del cierre.

La {T:t10} indica que cinco de los siete mecanismos cuentan con un indicador PERS. El observatorio comunitario se mide con la meta aspiracional de la escalera ASC y los materiales con la cantidad presupuestada. Las metas de uso, formación y continuidad dependen de los custodios y quedan sujetas a SC-4. El plan social no promete un resultado de salud. Promete uso documentado, personal certificado y continuidad bajo custodia. La {F:f02} integra los actores y los componentes en un ecosistema de sostenibilidad.

:::FIGURA f02 | Ecosistema de sostenibilidad: componentes, custodios candidatos y comunidad | Nota. Elaboración propia con la sección 4.4-MDR.10 (custodia distribuida y gobernanza). Los custodios asignados están por definir con el ICAR (POR_DEFINIR). Naturaleza: PROPUESTO. Generada con matplotlib sin parámetros aleatorios.

La {F:f02} muestra que el servicio central depende de cinco componentes y que cada uno posee candidatos a custodio, no un custodio asignado. La comunidad y los operarios rodean el ecosistema como usuarios y como red de soporte. El órgano de gobierno articula los componentes. Activa la cláusula de apertura cuando la cobertura del costo mínimo cae bajo 100 % durante dos trimestres consecutivos.

## 14.5 Plan de salida

El plan de salida organiza el paso de la responsabilidad del proyecto a los custodios. La transferencia se ejecuta por tramos condicionados. Cada tramo exige presupuesto aprobado, personal designado y competencia jurídica documentada. El costo de corregir una tecnología crece con el tiempo, y conviene decidir mientras el cambio es barato (Collingridge, 1980). Argyris y Schön (1978) sostienen que una organización aprende si revisa sus reglas y no solo sus acciones. El plan aplica ambos criterios: transfiere por etapas, con puntos de decisión tempranos, y deja una revisión de reglas en cada compuerta. Los hitos de transferencia son PROPUESTOS y se alinean con las compuertas de la ficha maestra.

La alineación con la ficha maestra ajusta un mes de la secuencia original. La sección 4.4-MDR.10 situaba el tramo 2 de transferencia en el mes 18. La compuerta C2 de la ficha cae en el mes 17 y exige convenios de custodia con partida. Por eso el tramo 2 se ubica en ese mes. Los otros tramos coinciden con la secuencia original. El tramo 0 ocurre en el mes 6 y el tramo 1 en la compuerta C1 del mes 12. El tramo 3 ocurre en la compuerta C3 del mes 24. La {T:t11} presenta los cuatro tramos con su contenido, su condición y las partidas que los financian.

:::TABLA t11 | Transferencia por tramos condicionados: contenido, condición y partidas del proyecto
| Tramo | Mes | Qué se transfiere | Condición de recepción | Partidas y evidencia |
| --- | --- | --- | --- | --- |
| 0 | 6 | Nada; se firman los acuerdos de custodia y la cláusula de apertura | Acuerdos firmados antes de comprar el segundo lote de nodos | P14 y S02; actas firmadas |
| 1 | 12 (C1) | Protocolo de calibración y series de datos | Evidencia del contraste (SC-1) y custodio con ICAR de 2 o más | S09 (50 millones de COP); acta de la compuerta C1 |
| 2 | 17 (C2) | Nodos adicionales y tablero a los custodios con capacidad demostrada | Partida en el plan operativo anual y personal designado | S09 (50 millones de COP); acta de la compuerta C2 |
| 3 | 24 (C3) | Operación continua de los componentes con custodio | Competencia jurídica documentada y primer pago del servicio | S09 (50 millones de COP); actas de entrega (H8) |
:::NOTA *Nota.* Elaboración propia con la sección 4.4-MDR.10 y la ficha maestra (compuertas, hitos y líneas S09, P14 y S02). Naturaleza: PROPUESTO. El mes 17 del tramo 2 adapta el mes 18 de la sección 4.4-MDR.10.

La {T:t11} asigna una evidencia fechable a cada tramo. El tramo 0 no transfiere activos. Obliga a firmar los acuerdos antes de la compra del segundo lote. Así evita el supuesto de que un receptor aparecerá al final. Los tramos 1 a 3 financian su formación con la partida S09, de 50 millones de COP cada uno. La suma de S09 es de 150 millones. Un componente cuyo custodio no cumple la condición no se transfiere: permanece bajo la alianza o pasa a la cláusula de apertura.

La documentación final se entrega con cada tramo, no al cierre. Incluye el inventario de activos con su estado, el manual de reactivación y el diccionario de datos. Incluye también el registro de versiones del modelo, el protocolo de calibración, el manual del tablero y los instrumentos de licencia. El hito H7 del mes 23 reúne el informe del laboratorio externo y la evaluación final. El hito H8 del mes 24 exige las actas de entrega a los custodios y la cláusula de apertura firmada. La cláusula se firma con los acuerdos del tramo 0, y el acta de cierre registra su vigencia. Esa lectura concilia el momento de la firma con el hito de verificación.

El cierre ordenado sigue una secuencia de cuatro pasos. El primero concilia el inventario físico con el registro de la plataforma y con la ejecución presupuestal. La desviación presupuestal no debe superar 5 % en valor absoluto al cierre (PERS-R04). El segundo cierra los contratos y las pólizas del proyecto, que incluyen las pólizas del SGR (O04) y la póliza de equipos (S04). El tercero entrega los datos, el código y el conocimiento a los custodios o, si no hay custodio, los libera con una licencia definida. El cuarto entrega a la evaluación externa los registros que sustentan las mediciones de los meses 6 y 12 posteriores al cierre. Esa evaluación se plantea como análisis de contribución y no como atribución (Mayne, 2012).

La cláusula de apertura protege el servicio mínimo ante una falla financiera. Su disparador es PROPUESTO: la cobertura del costo mínimo es menor que 100 % durante dos trimestres consecutivos. Si se activa, los datos, el código y el conocimiento se liberan con una licencia definida. Los activos físicos pasan a un custodio académico o comunitario con el manual de reactivación. La elección de la licencia es un VACIO que deciden el equipo formulador y la empresa aliada. La libertad de operación sobre propiedad industrial requiere la consulta jurídica ya presupuestada (S02). El manual de reactivación contiene el inventario de activos, los procedimientos de calibración, la estructura de datos y las credenciales de custodia.

La salida ordenada presenta un límite que el capítulo declara. La cláusula preserva datos, código y conocimiento, pero no asegura que la red continúe operando. Esa continuidad es el objetivo de PERS-S02, y su cumplimiento depende de los custodios después del cierre. Por eso el argumento de sostenibilidad de la sección 4.4-MDR.9 califica como NO_SOSTENIDO el enunciado de que la red opera después del mes 24. Califica como CONDICIONALMENTE el de que el diseño preserva datos, código y conocimiento. Esa condición exige firmar la cláusula antes del primer tramo de transferencia.
