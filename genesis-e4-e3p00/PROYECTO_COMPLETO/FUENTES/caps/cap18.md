%% PREFIJO: 18
# Capítulo 18. Marco Lógico

Este capítulo resume el diseño del proyecto en una matriz de cuatro niveles y verifica su coherencia. La matriz parte de los 15 indicadores del sistema PERS y de la red de 17 actividades del cronograma. El capítulo agrega el análisis de supuestos y de riesgos y ocho pruebas de coherencia. Todas las cifras proceden de la ficha maestra del proyecto.

## 18.1 Matriz de Marco Lógico Completa

La matriz sigue la cadena de resultados que Gertler et al. (2016) describen como una secuencia de insumos, actividades, productos, resultados e impacto. Elmore (1979) propone el mapeo hacia atrás: se parte del resultado final deseado y se deduce lo que debe ocurrir en cada nivel inferior. El proyecto construyó su árbol de objetivos con esa lógica. La {T:t01} presenta los cuatro niveles con su resumen narrativo, sus indicadores y metas, sus medios de verificación y sus supuestos.

:::TABLA t01 | Matriz de marco lógico 4 × 4 del proyecto
| Nivel | Resumen narrativo | Indicadores y metas finales | Medios de verificación | Supuestos |
| --- | --- | --- | --- | --- |
| Fin | Reducción de la exposición evitable de operarios y población a material particulado por remoción de escombros, mediante alertas basadas en mediciones verificadas. | PERS-S01 activación del protocolo: ≥ 80 % a los 12 meses posteriores al cierre; PERS-S02 continuidad de la red: ≥ 70 % a los 12 meses posteriores al cierre | Evaluación externa posproyecto | Los custodios financian la operación y los comités mantienen el protocolo. |
| Propósito | Los comités de gestión del riesgo usan mediciones verificadas de PM2,5 y PM10 de una red de 100 nodos para decidir alertas. | PERS-E01 uso institucional: ≥ 75 % al mes 24; PERS-E02 falsas alarmas: ≥ 30 % de reducción relativa; PERS-E03 capacidad en custodios: ≥ 60 personas certificadas | Actas de comité; registro de alertas; evaluaciones prácticas | Las compuertas C1 y C2 se aprueban y el enlace alterno funciona. |
| Componentes | Componente 1: modelo de corrección validado. Componente 2: red operativa con energía y enlace redundantes. Componente 3: tablero, protocolo y convenios de custodia. | PERS-P01 red operativa (nodos y gateways): 100 / 10 al mes 24; PERS-P02 software registrado: 1 registro vigente; PERS-P03 artículos: 2 sometidos y al menos 1 aceptado al mes 24; PERS-P04 apropiación social: 29 actividades (20 talleres y 9 jornadas) | Inventario, certificados DNDA, cartas de aceptación y actas | Los equipos llegan en los plazos de importación previstos. |
| Actividades | WP0 gestión, compuertas y cierre (4 actividades); WP1 medición verificada (6 actividades); WP2 red, energía y plataforma (4 actividades); WP3 uso institucional, apropiación y custodia (3 actividades) | PERS-R01 despliegue: 100 nodos y 10 gateways (100 %); PERS-R02 ciclos de calibración: 6 ciclos (2 por tramo); PERS-R03 plataforma en la nube: ≥ 99,0 %; PERS-R04 ejecución presupuestal: desviación absoluta ≤ 5 % al cierre; PERS-R05 horas-nodo: ≥ 60.000 y 4 rotaciones por departamento; PERS-R06 informes: 100 % | Informes de seguimiento y soportes financieros | Acceso a los sitios en ventanas secas y contratación oportuna. |
:::NOTA *Nota.* Elaboración propia con MARCO_LOGICO e IND (indicadores.py) y la red de actividades ACT (maestro.py). Los componentes se numeran 1 a 3 para no confundirlos con las compuertas C1 y C2. Naturaleza: metas PROPUESTO; líneas base en la ficha de cada indicador.

La matriz asigna cada indicador PERS a un solo nivel. Los dos indicadores de sostenibilidad (S) miden el fin. Los tres de efecto (E) miden el propósito. Los cuatro de producto (P) miden los componentes y los seis de proceso (R) miden las actividades. Los componentes se numeran 1 a 3 para no confundirlos con las compuertas C1 y C2. Los cuatro apartados siguientes describen cada nivel con el dato propio del proyecto.

### 18.1.1 Fin (Impacto)

El fin del proyecto es reducir la exposición evitable al material particulado de la remoción de escombros. El medio son las alertas basadas en mediciones verificadas. Dos posiciones disputan cómo se demuestra un fin de este tipo. Gertler et al. (2016) sostienen que la evaluación de impacto exige un contrafactual que estime qué habría ocurrido sin la intervención. Mayne (2012) propone el análisis de contribución, que examina si la cadena de resultados es plausible y si otras causas externas la explican.

El proyecto no dispone de grupo de comparación y no estima efectos en salud. Por eso adopta la segunda posición. Los indicadores PERS-S01 y PERS-S02 miden la activación del protocolo ante superación de umbral y la continuidad de la red bajo custodia. Sus metas son 80 % y 70 % a los 12 meses posteriores al cierre. Ambos presentan línea base VACIO y se miden después del cierre con evaluación externa. Ninguno mide exposición ni salud.

La consecuencia metodológica es una redacción prudente del fin. El proyecto afirma que contribuye a reducir la exposición evitable si el protocolo se activa y la red continúa. No afirma que la reducción ocurra ni la cuantifica. La relación entre alerta y exposición es una hipótesis de influencia estructural (INFERIDO). El supuesto del nivel es que los custodios financian la operación y los comités mantienen el protocolo, que corresponde al supuesto crítico SC-4.

### 18.1.2 Propósito (Efecto)

El propósito es que los comités de gestión del riesgo usen mediciones verificadas de PM2,5 y PM10 para decidir alertas. Las mediciones proceden de una red de 100 nodos. Davis (1989) explica la adopción de una tecnología por la utilidad percibida y la facilidad de uso. Venkatesh et al. (2003) agregan la influencia social y las condiciones facilitadoras. Rogers (2003) atribuye la difusión a los atributos de la innovación y a la estructura del sistema social. Las tres lecturas coinciden en que la adopción no sigue automáticamente de la disponibilidad técnica.

El proyecto traduce esas lecturas en tres indicadores de efecto. El indicador PERS-E01 mide el uso institucional. Su meta es 75 % de los comités focalizados al mes 24, con un umbral de 50 % en el piloto. El indicador PERS-E02 mide la reducción relativa de falsas alarmas. Su meta es 30 % frente a una línea base que se mide en el tramo 1. El indicador PERS-E03 mide la capacidad instalada, con meta de 60 personas certificadas.

La consecuencia es doble. La encuesta del anexo E recoge utilidad, facilidad de uso, influencia social y condiciones facilitadoras. La lista de cotejo del mismo anexo verifica las decisiones documentadas. El propósito incluye además la expresión mediciones verificadas. Ningún indicador de efecto la mide de forma directa, pues el desempeño de la corrección se verifica en las compuertas. La sección 18.3 trata esa brecha.

### 18.1.3 Componentes (Productos)

Los componentes son tres productos. El primero es el modelo de corrección validado. El segundo es la red operativa con energía y enlace redundantes. El tercero es el tablero con el protocolo y los convenios de custodia. Funnell y Rogers (2011) describen los modelos lógicos como representaciones de la teoría del programa que ligan productos con resultados. Pawson y Tilley (1997) objetan que un modelo lineal oculta el contexto en el que cada mecanismo funciona. La primera posición ordena el diseño. La segunda advierte que un producto entregado no basta para producir un resultado.

Los cuatro indicadores de producto cubren los tres componentes de forma desigual. El indicador PERS-P01 mide la red con 100 nodos y 10 gateways al mes 24. Los indicadores PERS-P02 y PERS-P03 miden el software registrado y los artículos, vinculados al modelo de corrección. El indicador PERS-P04 mide 29 actividades de apropiación social, que son 20 talleres y nueve jornadas. El componente 3 cuenta con un solo indicador de producto, y los convenios de custodia se miden en PERS-E03 y PERS-S02.

La consecuencia metodológica es clara. El contexto entra al diseño por los supuestos y por las compuertas. El supuesto del nivel es que los equipos llegan en los plazos de importación previstos. El riesgo de devaluación (R-FIN-01) y el de humedad (R-TEC-01) concentran los mayores valores monetarios esperados del nivel. La compra por tramo reduce la exposición a ambos, porque cada compuerta libera solo el tramo siguiente.

### 18.1.4 Actividades (Procesos)

Las 17 actividades se agrupan en cuatro paquetes. El de gestión reúne cuatro actividades y el de medición verificada reúne seis. El de red, energía y plataforma reúne cuatro y el de uso institucional, apropiación y custodia reúne tres. El Project Management Institute (PMI, 2021) reconoce la planificación, el trabajo del proyecto y la incertidumbre como dominios de desempeño. Patton (2011) propone una evaluación del desarrollo que apoya la adaptación continua cuando las condiciones cambian. La primera lectura favorece un plan con ruta crítica. La segunda favorece la revisión frecuente del plan.

El cronograma combina ambas lecturas. La ruta crítica abarca 13 actividades y suma 104 semanas (CALCULADO). Las otras cuatro actividades presentan holgura. Las dos compuertas C1 y C2 son puntos de decisión donde el plan puede cambiar. Los seis indicadores de proceso son PERS-R01 a PERS-R06. Miden el despliegue, los ciclos de calibración, la disponibilidad de la plataforma, la ejecución presupuestal, las horas-nodo y los informes.

La consecuencia es que el nivel de actividades se controla con seis indicadores mensuales. El supuesto del nivel es el acceso a los sitios en ventanas secas y la contratación oportuna. Los riesgos R-EXT-01, R-EXT-02 y R-FIN-02 lo amenazan. Su valor monetario esperado conjunto es de 104,0 millones de COP.

## 18.2 Análisis de Supuestos

### 18.2.1 Supuestos por nivel

Un supuesto es una condición externa que debe cumplirse para que un nivel produzca el siguiente. Toulmin (1958) describe el argumento con datos, una garantía que justifica el paso de los datos a la conclusión y una posible refutación. Los supuestos del marco lógico cumplen la función de la garantía. Los riesgos cumplen la función de la refutación. El proyecto declara un supuesto por nivel. Asigna los cuatro supuestos críticos SC-1 a SC-4 del análisis causal a los niveles del fin y del propósito.

La {T:t02} muestra la asignación. El supuesto SC-4, de custodia, corresponde al fin. Los supuestos SC-1, SC-2 y SC-3, de medición verificada, de energía y enlace y de uso institucional, corresponden al propósito. Los niveles de componentes y de actividades dependen de condiciones externas de importación, de acceso y de contratación, que no figuran entre los supuestos críticos.

:::TABLA t02 | Análisis de supuestos y riesgos por nivel del marco lógico
| Nivel | Supuesto del nivel | Riesgo asociado | SC | P × I (nivel) | EMV (M COP) | Estrategia y respuesta |
| --- | --- | --- | --- | --- | --- | --- |
| Fin | Los custodios financian la operación y los comités mantienen el protocolo. | R-ORG-02: Los custodios no asumen la operación en el posproyecto. | SC-4 | 4 × 4 = 16 (ALTO) | 60,0 | Mitigar: Convenios por tramo, formación de custodios y cláusula de apertura. |
| Subtotal Fin | — | 1 riesgo | — | — | 60,0 | — |
| Propósito | Las compuertas C1 y C2 se aprueban y el enlace alterno funciona. | R-ORG-01: Los comités de gestión del riesgo no adoptan el tablero ni el protocolo. | SC-3 | 3 × 5 = 15 (ALTO) | 36,0 | Mitigar: Co-diseño de umbrales, formación por comité y uso piloto con registro de decisiones. |
| Ídem | Ídem | R-TEC-04: El modelo de corrección no generaliza entre departamentos. | SC-1 | 3 × 4 = 12 (ALTO) | 31,5 | Mitigar: Validación cruzada por departamento y reentrenamiento por tramo. |
| Ídem | Ídem | R-DAT-01: Un incidente de ciberseguridad compromete la plataforma. | SC-3 | 2 × 4 = 8 (MEDIO) | 18,0 | Mitigar: Pruebas de penetración, segmentación y copias de respaldo. |
| Subtotal Propósito | — | 3 riesgos | — | — | 85,5 | — |
| Componentes | Los equipos llegan en los plazos de importación previstos. | R-TEC-01: La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10. | SC-1 | 4 × 5 = 20 (EXTREMO) | 150,0 | Mitigar: Modelo de corrección por humedad, banco de calibración y reposición de cabezales. |
| Ídem | Ídem | R-TEC-02: Las baterías se agotan antes de 14 días sin sol y los nodos dejan de transmitir. | SC-2 | 3 × 4 = 12 (ALTO) | 24,0 | Mitigar: Kits solares dimensionados, modo de bajo consumo y repuestos de batería. |
| Ídem | Ídem | R-TEC-03: La red celular falla en el sitio y los gateways pierden el enlace con la nube. | SC-2 | 3 × 4 = 12 (ALTO) | 28,0 | Mitigar: Enlace satelital de respaldo y almacenamiento local de 7 días. |
| Ídem | Ídem | R-FIN-01: La devaluación del peso encarece los equipos importados. | — | 4 × 4 = 16 (ALTO) | 165,0 | Mitigar: Compra por tramo con cobertura cambiaria y cotizaciones vigentes. |
| Ídem | Ídem | R-JUR-01: Una solicitud de patente de terceros afecta la libertad de operación. | — | 2 × 4 = 8 (MEDIO) | 20,0 | Mitigar: Análisis de libertad de operación y diseño alternativo del módulo afectado. |
| Subtotal Componentes | — | 5 riesgos | — | — | 387,0 | — |
| Actividades | Acceso a los sitios en ventanas secas y contratación oportuna. | R-EXT-01: Deslizamientos o réplicas bloquean vías y retrasan la instalación. | — | 4 × 3 = 12 (ALTO) | 60,0 | Aceptar y mitigar: Instalación en ventanas secas, técnicos locales y holgura en el cronograma. |
| Ídem | Ídem | R-EXT-02: Robo o vandalismo de nodos en sitios de remoción. | — | 3 × 3 = 9 (MEDIO) | 24,0 | Transferir y mitigar: Póliza todo riesgo, cerramientos y custodia local por sitio. |
| Ídem | Ídem | R-FIN-02: La contrapartida en especie no se certifica a tiempo. | — | 2 × 4 = 8 (MEDIO) | 20,0 | Evitar: Certificación de la IES y de la empresa antes del acta de inicio. |
| Subtotal Actividades | — | 3 riesgos | — | — | 104,0 | — |
| Total | — | 12 riesgos | — | — | 636,5 | La reserva de contingencia redondea a 636,0 |
:::NOTA *Nota.* Elaboración propia con RISKS (maestro.py) e indicadores.py. La asignación de cada riesgo a un nivel y a un supuesto crítico (SC-1 a SC-4) es PROPUESTO. P: probabilidad; I: impacto; EMV: valor monetario esperado, en millones de pesos colombianos (M COP), sin redondeo. Decimales con coma.

### 18.2.2 Riesgos asociados

La tabla vincula los 12 riesgos del registro con un nivel del marco lógico. El valor monetario esperado suma 636,5 millones de COP sin redondeo. El nivel de componentes concentra 387,0 millones, es decir 60,8 % de la suma. El nivel de actividades suma 104,0 millones, el del propósito 85,5 millones y el del fin 60,0 millones. La concentración indica que el mayor riesgo económico está en la entrega de los productos y no en la gestión de las actividades.

### 18.2.3 Estrategias de mitigación

El estándar ISO 31000 describe opciones de tratamiento del riesgo (ISO, 2018). Entre ellas figuran evitar la fuente, modificar la probabilidad o la consecuencia, compartir el riesgo y retenerlo con una decisión informada. El registro del proyecto clasifica el tratamiento en cuatro estrategias. Aplica mitigar a nueve riesgos, aceptar y mitigar a un riesgo, transferir y mitigar a un riesgo y evitar a un riesgo. El premortem de 4.4-MDR.12 anticipa fallas del diseño con la técnica de Klein (2007). El capítulo 10 convierte esas fallas en eventos con probabilidad, impacto y valor monetario esperado.

La consecuencia metodológica es que la reserva de contingencia respalda a los cuatro niveles. Su admisibilidad como rubro depende de los términos de referencia (VACIO). Si la reserva no se admite, los riesgos del nivel de componentes quedan sin cobertura monetaria. En ese caso la compuerta C1 reevalúa el alcance del tramo 2.

## 18.3 Coherencia Vertical y Horizontal

### 18.3.1 Verificación de coherencia lógica

La especificación del capítulo exige verificar la coherencia vertical y la horizontal, pero no enumera las pruebas. El proyecto adopta ocho pruebas (PROPUESTO). Las cuatro verticales, V1 a V4, comprueban que cada nivel conduce al siguiente y que los supuestos están asignados. Las cuatro horizontales, H1 a H4, comprueban que cada nivel cuenta con indicadores completos y trazables. La {T:t03} muestra el resultado y la {F:f01} lo sitúa sobre la matriz.

:::TABLA t03 | Resultado de las ocho pruebas de coherencia del marco lógico
| Prueba | Tipo | Regla verificada | Evidencia calculada | Estado | Acción |
| --- | --- | --- | --- | --- | --- |
| V1 | Vertical | Cada componente tiene actividades que lo producen y cada actividad tiene paquete | 17 de 17 actividades con paquete; WP1 6, WP2 4, WP3 3, WP0 4 | CUMPLE | Sin acción. |
| V2 | Vertical | Cada objetivo específico tiene al menos un indicador de producto | OE1: P02, P03; OE2: P01; OE3: P04 | CUMPLE | Sin acción. |
| V3 | Vertical | Cada objetivo tiene indicador de efecto y de impacto | Efecto e impacto solo en OE3; sin cobertura: OE1, OE2 | PARCIAL | Verificar R², NRMSE, pendiente y sesgo en las compuertas y en el ensayo independiente |
| V4 | Vertical | Cada nivel declara supuestos y cada supuesto crítico tiene nivel | 4 de 4 niveles con supuesto; SC-1 a SC-4 asignados | CUMPLE | Sin acción. |
| H1 | Horizontal | Cada indicador tiene fórmula, unidad y meta final | 15 de 15 indicadores completos | CUMPLE | Sin acción. |
| H2 | Horizontal | Cada indicador tiene línea base | 10 de 15 con línea base; VACIO: R03, E01, E02, S01, S02 | PARCIAL | Medir las líneas base en el tramo 1 (DEC-F10) |
| H3 | Horizontal | Cada indicador tiene medio, fuente, frecuencia y responsable | 15 de 15 indicadores completos | CUMPLE | Sin acción. |
| H4 | Horizontal | Cada nivel enlaza riesgos y cada paquete tiene presupuesto | 12 de 12 riesgos asignados a un nivel; 4 de 4 paquetes con líneas de presupuesto | CUMPLE | Sin acción. |
:::NOTA *Nota.* Elaboración propia; las pruebas se calculan con a11_datos.pruebas() sobre IND, MARCO_LOGICO, ACT y RISKS. Las ocho pruebas son PROPUESTO porque la especificación no las enumera. Estados: CUMPLE, PARCIAL, NO CUMPLE.

:::FIGURA f01 | Diagrama de coherencia vertical y horizontal del marco lógico | Nota. Elaboración propia con indicadores.py y maestro.py mediante a11_datos.pruebas(); script c18_figs.py, sin semilla; corte de datos 13 de octubre de 2026. Estados CALCULADOS; la trama señala una prueba que cumple parcialmente.

Seis de las ocho pruebas cumplen y dos cumplen parcialmente. Ninguna falla. La prueba V3 queda parcial porque solo el objetivo OE3 cuenta con indicadores de efecto y de impacto. El umbral de desempeño de la corrección es la meta del objetivo OE1 y el criterio de las compuertas. Consiste en R² mayor o igual a 0,70 y NRMSE menor o igual a 30 %. Los 15 indicadores PERS no lo miden como indicador propio. El proyecto lo verifica en el acta de cada compuerta y en el ensayo independiente del mes 23.

### 18.3.2 Trazabilidad de indicadores

La prueba H2 queda parcial porque cinco indicadores carecen de línea base: PERS-R03, PERS-E01, PERS-E02, PERS-S01 y PERS-S02. La decisión DEC-F10 fija que esas líneas se midan en el tramo 1. La trazabilidad completa une cada indicador con un objetivo, un paquete de trabajo, un riesgo y una línea de presupuesto. Mayne (2012) y Befani y Mayne (2014) proponen combinar el análisis de contribución con el rastreo de procesos para sostener afirmaciones causales con evidencia. El proyecto adopta esa combinación para evaluar los indicadores de efecto y de impacto.

La consecuencia es una regla de cierre del marco lógico. Las dos pruebas parciales no bloquean la presentación del proyecto. Sí condicionan la compuerta C1. El acta de esa compuerta debe incluir dos elementos. El primero es la línea base medida de los indicadores PERS-E02 y PERS-R03. El segundo es la verificación de los umbrales de desempeño en el piloto. Si alguna falta, el comité directivo decide si aplaza el tramo 2.
