%% PREFIJO: F0
# Paso 0. Configuración de la convocatoria y del documento

## F0.1 Identificación de la convocatoria

El Paso 0 del metaprompt solicita los términos de referencia (TdR) de la convocatoria. En su defecto, pide los datos de identificación, los requisitos técnicos y la estructura del documento. El usuario no aportó los TdR. La configuración se reconstruye con el expediente E3-P00, el informe de vigilancia tecnológica y la instrucción expresa del 13 de octubre de 2026. Cada valor lleva su naturaleza y su estado de verificación según la norma de trazabilidad NTC 1.1. Así, ningún dato del expediente aparece como confirmado por la fuente normativa.

La {T:t01} registra la identificación de la convocatoria. Los valores del expediente se conservan como declarados. Los valores que solo los TdR pueden fijar quedan como vacíos y se resuelven con la entidad financiadora antes de radicar.

:::TABLA t01 | Identificación de la convocatoria
| Campo | Valor adoptado | Fuente | Naturaleza | Verificación |
| --- | --- | --- | --- | --- |
| Nombre de la convocatoria | Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56) | Paso 1 del usuario (E3-P00) | DECLARADO | NO_VERIFICADO |
| Entidad financiadora | Sistema General de Regalías (SGR) / Ministerio de Ciencia, Tecnología e Innovación (MinCiencias) | Paso 1 del usuario (E3-P00) | DECLARADO | NO_VERIFICADO |
| Tipología del proyecto | Investigación aplicada, desarrollo tecnológico e innovación | Paso 1 del usuario (E3-P00) | DECLARADO | NO_APLICA |
| Fecha límite de presentación | 3 de noviembre de 2026, 4:00 p. m. | Paso 1 del usuario (E3-P00) | DECLARADO | NO_VERIFICADO |
| Presupuesto máximo por proyecto | $ 14.000.000.000 COP | Paso 1 del usuario (E3-P00) | DECLARADO | NO_VERIFICADO |
| Contrapartida requerida (%) | [DATO_USUARIO: porcentaje exigido por los TdR]. Contrapartida ofrecida: $ 2,110,000,000 COP, equivalente a 22,8 % del valor solicitado al SGR y a 19,5 % del total | Cálculo sobre maestro.py | CALCULADO | NO_VERIFICADO |
| Duración máxima (meses) | 24 meses de ejecución (104 semanas) y 12 meses de seguimiento posproyecto | Paso 1 del usuario y decisión DEC-F08 | DECLARADO y PROPUESTO | NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente E3-P00 y la ficha maestra (sección 1). Los TdR no se aportaron; la regla bloqueante de articulación territorial (Paso 5.0) queda registrada como reserva en el cierre del documento.

## F0.2 Requisitos técnicos

Los requisitos técnicos definen la madurez de partida y de llegada, el tipo de grupo ejecutor y la alianza. El expediente E3 declara la madurez final en TRL 8 y también en «TRL 4 a 7 u 8». Esta formulación fija TRL 7 porque la demostración en entorno operativo no incluye calificación independiente del sistema completo, requisito del nivel 8. La {T:t02} muestra el valor adoptado y su estado.

:::TABLA t02 | Requisitos técnicos de la convocatoria
| Campo | Valor adoptado | Fuente | Naturaleza | Verificación |
| --- | --- | --- | --- | --- |
| TRL inicial mínimo exigido | [DATO_USUARIO: nivel mínimo exigido por los TdR] | TdR no aportados | VACIO | NO_VERIFICADO |
| TRL inicial del proyecto | TRL 4: validación de componentes en laboratorio | Paso 1 del usuario | DECLARADO | NO_VERIFICADO |
| TRL final esperado | TRL 7: demostración del sistema en entorno operativo (el expediente declaraba TRL 8) | Decisión DEC-F05 | PROPUESTO | NO_APLICA |
| Grupos de investigación requeridos | Un grupo de telecomunicaciones y señales con categoría A1 o A; [DATO_USUARIO: nombre y código GrupLAC] | Paso 1 del usuario | DECLARADO | NO_VERIFICADO |
| Alianzas obligatorias | Empresa tecnológica, institución de educación superior y entidades territoriales | Paso 1 del usuario y supuesto del usuario | SUPUESTO | NO_VERIFICADO |
| Enfoque diferencial | [DATO_USUARIO: enfoque diferencial exigido por los TdR] | TdR no aportados | VACIO | NO_VERIFICADO |
:::NOTA *Nota.* Elaboración propia con el expediente E3-P00 y la ficha maestra. La categoría del grupo es una declaración del expediente y no se verificó en la plataforma de MinCiencias.

## F0.3 Estructura del documento

La estructura obedece a la secuencia del metaprompt GENESIS-CTeI 36.10 RC2 y se entrega en un solo documento. La {T:t03} lista las partes. La Parte I reúne los pasos previos a la redacción de los capítulos. La Parte II desarrolla los 21 capítulos del Paso 8. La Parte III contiene el paquete de documentos 1000X del Paso 9 y el capítulo de estrategia del Mensaje 10. El documento cierra con el registro de vacíos y los cuatro cierres F-01 a F-04.

:::TABLA t03 | Estructura del documento único
| Parte | Contenido | Pasos del metaprompt | Formato |
| --- | --- | --- | --- |
| Parte I | Configuración, información básica, ecuaciones de vigilancia, procesamiento bibliométrico, análisis causal, formalización, alternativas e indicadores | Pasos 0 a 7 | Prefijo F en tablas y figuras (por ejemplo, Tabla F5.1) |
| Parte II | Capítulos 1 a 21: del problema al Project Charter, con bibliografía y anexos | Paso 8 | Numeración «capítulo.n» (por ejemplo, Tabla 8.3) |
| Parte III | Paquete 1000X (diez documentos) y capítulo de estrategia | Paso 9 y Mensaje 10 | Prefijo X y número de documento (por ejemplo, Tabla X4.2) |
| Cierre | Registro de vacíos, reservas y cierres F-01 a F-04 | Módulos de cierre | Prefijo C |
:::NOTA *Nota.* Elaboración propia con la especificación del metaprompt. La extensión máxima y el formato exigidos por los TdR son [DATO_USUARIO: extensión y formato de radicación]; el documento se entrega en Word y PDF por instrucción del usuario.

## F0.4 Convenciones de presentación

El usuario fijó dos reglas de presentación el 13 de octubre de 2026. La primera adopta los cinco niveles de encabezado de la séptima edición de las normas APA (American Psychological Association, 2020). La segunda impone una sola plantilla visual para todas las figuras y tablas. Ambas reglas se aplican al documento completo mediante estilos de Word y una hoja de estilo gráfica común. Ningún capítulo usa un criterio propio.

### F0.4.1 Jerarquía de encabezados

La {T:t04} describe los cinco niveles. Los niveles 1 a 3 aparecen en la tabla de contenido. Los niveles 4 y 5 inician el párrafo, terminan en punto y no se numeran. El documento numera los títulos de niveles 1 y 2 con un código decimal que se declara aquí una sola vez.

:::TABLA t04 | Niveles de encabezado según APA 7 aplicados al documento
| Nivel | Formato | Ubicación del texto | Uso en el documento |
| --- | --- | --- | --- |
| 1 | Centrado, negrita, mayúscula inicial en cada palabra principal | Párrafo nuevo bajo el título | Pasos, capítulos, paquete 1000X y cierre |
| 2 | Alineado a la izquierda, negrita | Párrafo nuevo bajo el título | Secciones numeradas (por ejemplo, 8.2) |
| 3 | Alineado a la izquierda, negrita cursiva | Párrafo nuevo bajo el título | Subsecciones numeradas (por ejemplo, 8.2.1) |
| 4 | Sangría de 1,27 cm, negrita, con punto final | Misma línea que el título | Apartados dentro de una subsección |
| 5 | Sangría de 1,27 cm, negrita cursiva, con punto final | Misma línea que el título | Ítems dentro de un apartado |
:::NOTA *Nota.* Elaboración propia con American Psychological Association (2020). Los niveles 4 y 5 no figuran en la tabla de contenido.

### F0.4.2 Plantilla visual

La plantilla visual asigna una función a cada color y define una jerarquía tipográfica. El color #2A3439 se reserva para texto, estructura y máximo contraste. El color #6699CC marca la categoría principal, el punto más alto y el filete bajo el encabezado de tabla. El color #9EB9D4 identifica la serie secundaria, y #B9D9EB, el apoyo y la baja prioridad. Los neutros #F5F5F5 y #F7F7F7 rellenan cajas y filas alternas. La {F:f01} resume esas funciones.

:::FIGURA f01 | Funciones de color de la plantilla visual | Nota. Elaboración propia con matplotlib 3 y la hoja de estilo figs/estilo.py; paleta definida por el usuario el 13 de octubre de 2026. El texto sobre #6699CC alcanza una relación de contraste de 4,24:1, inferior a 4,5:1; por eso los encabezados de tabla usan #B9D9EB (8,61:1) y reservan #6699CC para el filete.

Las figuras siguen cuatro reglas adicionales. El título de la figura enuncia el hallazgo en negrita y el subtítulo indica variable, periodo y unidades en peso normal. Las etiquetas de datos se escriben junto a la marca y no en una leyenda separada. Los ejes superior y derecho no se dibujan, y la cuadrícula horizontal es una línea discontinua fina con opacidad de 0,25. El fondo es transparente, con exportación recortada al contenido. Este último criterio exceptúa la regla FIG-02 del metaprompt, que prohíbe la cuadrícula, por instrucción expresa del usuario (decisión DEC-F13).

Las tablas siguen el estilo APA. El rótulo («Tabla c.n») va en negrita y el título en cursiva, sin punto final. La tabla lleva un filete superior, otro inferior y otro bajo el encabezado. La nota comienza con la palabra «Nota» en cursiva. Ninguna tabla lleva líneas verticales. El encabezado usa relleno #B9D9EB y texto #2A3439; las filas pares usan #F7F7F7. Las tablas con doce o más columnas se imprimen en hoja apaisada.

### F0.4.3 Convenciones de redacción y de trazabilidad

El texto usa registro impersonal, oraciones de 25 palabras o menos y siglas desarrolladas en su primera aparición. Los decimales se escriben con coma y los miles con punto. Cada cifra cardinal procede de la ficha maestra del proyecto o del informe de vigilancia tecnológica con su página. La naturaleza del dato puede ser DOCUMENTADO, DECLARADO, CALCULADO, INFERIDO, SUPUESTO, PROPUESTO, ILUSTRATIVO o VACIO. Su verificación puede ser VERIFICADO, PARCIALMENTE_VERIFICADO, NO_VERIFICADO, CONTRADICTORIO o NO_APLICA. Ambos son ejes independientes. El marcador [DATO_USUARIO: descripción] señala la información que solo el usuario posee y que no se inventa.

## F0.5 Decisiones de formulación

La formulación exigió quince decisiones que resuelven contradicciones del expediente E3-P00 o que fijan una opción cuando el metaprompt ofrece varias. La {T:t05} las registra con el código DEC-F que se cita en el resto del documento. Cada decisión es PROPUESTA y requiere ratificación del equipo formulador antes de radicar.

:::TABLA t05 | Registro de decisiones de formulación
| Código | Decisión y fundamento |
| --- | --- |
| DEC-F01 | Fuente de financiación y estructura: el expediente mezcla 'Convocatoria 56 MinCiencias' y 'SGR/OCAD/MGA'. Se adopta la denominación 'Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)' del Paso 1 del usuario. Los términos de referencia no se aportaron: la estructura de 21 capítulos es la del metaprompt (SUPUESTO) y los datos que solo el usuario posee se marcan [DATO_USUARIO]. |
| DEC-F02 | Arquitectura: la corrección ocurre en el gateway; los nodos hoja usan LoRa y bajo consumo; los gateways usan red celular con enlace satelital alterno y almacenamiento local de 7 días (corrige HR-12 y HR-13). |
| DEC-F03 | Estrategia de despliegue: R4 de 4.4-MDR (tramos con piloto de contraste y custodia distribuida), con compuertas C1 y C2 que liberan las compras del tramo siguiente. |
| DEC-F04 | Meta de desempeño: R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia (ancla EPA, 2021); NMAE ≤ 15 % aspiracional; línea base medida en el tramo 1 (corrige HR-14: tres metas contradictorias). |
| DEC-F05 | TRL final 7 (no 8): demostración en entorno operativo; TRL 8 exige calificación independiente que el plazo no cubre. |
| DEC-F06 | Presupuesto: se solicita la suma justificada por actividad (62,4 % del tope), no el tope; la holgura se describe como opciones sin presupuestar (corrige HR-10). |
| DEC-F07 | Contrapartida: 2.110 M (IES 1.100 en especie; empresa 210 en efectivo y 800 en especie), valores del expediente E3 con desglose de la IES reconstruido; certificaciones pendientes; las alcaldías no aportan (VACIO). |
| DEC-F08 | Cronograma: red de 17 actividades con ruta crítica igual a la duración (104 semanas); importación de 12 semanas máximo por lote; compras por tramo y no 100 % en la semana 2 (corrige HR-11). |
| DEC-F09 | Alternativa seleccionada: ALT-03 híbrida por tramos, condicionada a la ratificación del panel; el puntaje no se interpreta como probabilidad de éxito. |
| DEC-F10 | Indicadores: los de impacto (S) se miden 6 a 12 meses tras el cierre y por una evaluación externa; las líneas base VACIO se miden en el tramo 1. |
| DEC-F11 | Escenarios estratégicos: el metaprompt sugiere probabilidades 25/50/20/5; se omiten porque ninguna tiene fuente (NTC 1.1). Los escenarios se presentan sin probabilidad y con condiciones de activación. |
| DEC-F12 | Articulación territorial (Paso 5.0): los ocho elementos del checklist quedan NO_VERIFICADO por falta de PDD, CONPES y anexos. La regla bloqueante del metaprompt exige regresar a Gate 0; se continúa por orden expresa del usuario (13-oct-2026) con la reserva R-ART registrada en el cierre. |
| DEC-F13 | Estética: se aplica la paleta y la jerarquía tipográfica del usuario; excepción a FIG-02: opacidad 0,25 solo en la cuadrícula; el relleno de encabezados de tabla usa #B9D9EB con texto #2A3439 (contraste superior a 4,5:1; el texto sobre #6699CC no lo alcanza) y #6699CC como filete inferior del encabezado; filas alternas #F7F7F7. |
| DEC-F14 | Numeración: tablas y figuras 'c.n' por capítulo; Parte I con prefijo F (F5.1), paquete 1000X con prefijo X (X6.1) y anexos con letra (A1). |
| DEC-F15 | GWO no se activa porque el espacio de decisión (4 alternativas) es enumerable (AS-32). |
:::NOTA *Nota.* Elaboración propia con la ficha maestra (sección 11). Naturaleza: PROPUESTO. Las decisiones DEC-F05 y DEC-F09 dependen de la ratificación del panel evaluador.

## F0.6 Valor que crea el paso

El Paso 0 convierte la ausencia de los TdR en una lista cerrada de datos pendientes. Esa lista evita que el documento se presente como conforme con una convocatoria que no se leyó. También fija el criterio con que se resuelve cualquier discrepancia posterior: gobierna la ficha maestra, y los TdR, cuando existan, gobiernan sobre la ficha.
