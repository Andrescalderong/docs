%% PREFIJO: 21

# Capítulo 21. Project Charter

El acta de constitución del proyecto resume en pocas páginas lo que autoriza su ejecución. Define qué se hará, con qué recursos, en cuánto tiempo, con qué criterios de éxito y bajo la autoridad de quién. El Project Management Institute [PMI] (2021) la describe como el documento que autoriza formalmente el proyecto y otorga a la dirección la facultad de aplicar recursos. Este capítulo condensa los capítulos 1 a 20 en un instrumento que el comité directivo y el financiador pueden firmar. Todas las cifras provienen de la ficha maestra. Los datos que solo posee el usuario aparecen como [DATO_USUARIO].


## 21.1 Información General

La ficha de identificación reúne los datos que no cambian durante la ejecución. Fija el título, el código del caso, la versión del acta, las fechas y las cifras totales. La versión 1.0 es una propuesta de formulación. El acta solo adquiere efecto cuando el comité directivo y el financiador la firman. La {T:t01} presenta la ficha.

:::TABLA t01 | Ficha de identificación del proyecto
| Campo | Contenido | Naturaleza |
| --- | --- | --- |
| Título | Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto | DECLARADO |
| Código del caso | SGR_CONV56_AIRE | DECLARADO |
| Versión del acta de constitución | 1.0 (borrador con vacíos) | PROPUESTO |
| Convocatoria | Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56) | DECLARADO |
| Financiador | Sistema General de Regalías (SGR) / Ministerio de Ciencia, Tecnología e Innovación (MinCiencias) | DECLARADO |
| Tipología | Investigación aplicada, desarrollo tecnológico e innovación | DECLARADO |
| Clasificación OCDE | 1.2 Ingeniería eléctrica, electrónica e informática | DECLARADO |
| Territorio | Departamentos de Caldas, Cundinamarca y Valle del Cauca (12 municipios, 4 por departamento) | SUPUESTO |
| Duración de ejecución | 24 meses (104 semanas); seguimiento posproyecto de 12 meses | PROPUESTO |
| Madurez tecnológica | TRL 4 al inicio y TRL 7 al cierre | PROPUESTO |
| Fecha de corte de la formulación | 13 de octubre de 2026 | DECLARADO |
| Fecha límite de la convocatoria | 3 de noviembre de 2026 | DECLARADO |
| Valor solicitado al SGR | $ 8.729.840.000 | CALCULADO |
| Contrapartida | $ 2.110.000.000 | DECLARADO |
| Total del proyecto | $ 10.839.840.000 | CALCULADO |
| Entidad ejecutora | [DATO_USUARIO: nombre de la institución de educación superior ejecutora] | VACIO |
| Director del proyecto | [DATO_USUARIO: nombre y cargo] | VACIO |
| Fecha de aprobación del acta | [DATO_USUARIO: fecha de firma] | VACIO |
:::NOTA *Nota.* Elaboración propia con datos de la ficha maestra §1 y §5. El tope declarado de la convocatoria, 14.000.000.000 COP, no se verificó porque los términos de referencia no se aportaron. SGR: Sistema General de Regalías. OCDE: Organización para la Cooperación y el Desarrollo Económicos. TRL: nivel de madurez tecnológica.

La ficha deja tres campos en blanco: la entidad ejecutora, el director y la fecha de aprobación. Esos datos solo los posee el usuario. Sin ellos, el acta no puede firmarse. La alianza entre la entidad ejecutora y la empresa tecnológica es un supuesto por instrucción del usuario, y por eso los nombres quedan por definir. El comité directivo debe confirmar esos tres campos antes de la radicación.


## 21.2 Caso de Negocio

La justificación del proyecto parte de un problema de medición. Los sensores de bajo costo para partículas finas multiplican la cobertura de la vigilancia. Entregan lecturas de calidad desconocida cuando no se calibran en el sitio (Karagulian et al., 2019). En Colombia, 90,8 % de las 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13). La cifra es un cálculo del analista sobre el informe de vigilancia tecnológica. En el país hay 209 estaciones reportadas y 154 integradas a un sistema de vigilancia. Solo 28 de 1.122 municipios cuentan con estaciones utilizables para estimar la carga (Rodríguez-Villamizar et al., 2022, pp. 3 y 6).

Tras un terremoto, la remoción de escombros genera material particulado que expone a operarios y comunidades. Decidir alertas con mediciones de error desconocido produce falsas alarmas o ausencia de alerta. La baja confianza reduce el uso institucional de las mediciones, y esa menor confianza perpetúa la ausencia de datos verificados. El análisis estructural de la sección 4.4 identificó ese ciclo y señaló la variable de error de medición sin verificar (V06) como problema central. El caso de negocio consiste en romper el ciclo. La red de 100 nodos se corrige en el gateway y se verifica contra tres referencias gravimétricas. Los comités de gestión del riesgo la ponen en uso.

La viabilidad del caso de negocio depende de tres condiciones que el acta deja explícitas. La primera es técnica: que el modelo de corrección alcance los umbrales en el piloto. La segunda es institucional: que los comités usen el tablero y los custodios asuman la operación. La tercera es financiera: que el tipo de cambio y la contrapartida se mantengan dentro de lo previsto. Si falla la primera, el proyecto se detiene en C1 con una pérdida acotada al tramo 1. Si falla la segunda, el proyecto cierra con una red verificada y datos abiertos, y activa la cláusula de apertura. Si falla la tercera, ajusta el tamaño del tramo siguiente. Ninguna de las tres fallas obliga a comprometer el presupuesto restante (Boardman et al., 2018).

La alternativa seleccionada resultó de comparar cuatro opciones en el Paso 6. ALT-00 mantiene sensores aislados sin calibración dinámica y obtuvo 4,475. ALT-01 instala estaciones fijas de referencia en los sitios y obtuvo 4,335. ALT-02 calibra de forma centralizada en la nube y obtuvo 5,150. ALT-03 combina corrección en el gateway, despliegue por tramos y custodia distribuida, y obtuvo 5,805 en una escala de 1 a 9. La ganadora no cambió en los cinco escenarios de sensibilidad de más o menos 10 % relativo. Los puntajes son juicios PROPUESTOS y no probabilidades de éxito. Un monitor de referencia en cada sitio ofrece mayor exactitud, pero a 85 millones de COP por monitor, cien monitores sumarían 8.500 millones (CALCULADO). Esa suma supera el valor solicitado y por eso ALT-01 pierde frente a la red híbrida (U.S. Environmental Protection Agency, 2021).

La alineación estratégica se apoya en cuatro marcos. La Ley 1523 de 2012 crea el Sistema Nacional de Gestión del Riesgo de Desastres y asigna funciones a los consejos territoriales (Congreso de la República, 2012a). La Ley 2056 de 2020 regula el uso de los recursos del SGR (Congreso de la República, 2020). La política para el mejoramiento de la calidad del aire fija la vigilancia como línea de acción (Departamento Nacional de Planeación [DNP], 2018). El Marco de Sendái promueve los sistemas de alerta temprana (Oficina de las Naciones Unidas para la Reducción del Riesgo de Desastres [UNDRR], 2015). La articulación con el Plan de Desarrollo Departamental y con el Anexo 4 no se verificó, porque esos documentos no se aportaron.

Los beneficios esperados son técnicos, institucionales y de continuidad (Funnell y Rogers, 2011). El proyecto entrega mediciones con error conocido frente a una referencia. Entrega un tablero que los comités usan en decisiones documentadas. Entrega una red que los custodios mantienen tras el cierre. No promete reducir la morbilidad ni la mortalidad, porque no incluye un diseño causal que lo identifique. La evaluación económica completa, con la comparación de costos y beneficios, no se calcula, porque los beneficios monetarios no tienen fuente (Boardman et al., 2018). La decisión de invertir descansa en el valor de la información verificada y en la opción de detener la inversión en cada compuerta.


## 21.3 Descripción del Proyecto

El proyecto implementa una red híbrida de borde y nube que mide PM2,5 y PM10 en sitios de remoción de escombros. Cien nodos hoja con sensor óptico, temperatura y humedad transmiten por LoRa a 10 gateways. Cada gateway aplica el modelo de corrección, almacena siete días de datos y reenvía por red celular, con enlace satelital alterno. Tres monitores gravimétricos, uno por departamento, sirven de referencia en la colocalización. La nube aloja el entrenamiento del modelo, el gemelo digital y el tablero del índice de calidad del aire y salud. El despliegue se hace en tres tramos de 30, 40 y 30 nodos. Las compuertas C1 y C2 liberan la compra del tramo siguiente.

La decisión de invertir sigue un esquema por etapas y compuertas (Cooper, 2008). La madurez tecnológica avanza del nivel 4 al nivel 7 (Mankins, 1995). El nivel 4 corresponde a la validación de componentes en laboratorio. El nivel 7 corresponde a la demostración de un prototipo en entorno operativo. Entre ambos, el piloto del tramo 1 valida el modelo en un entorno relevante. El tramo 2 lo reentrena por departamento. El tramo 3 lo demuestra con 100 nodos. El proyecto no afirma el nivel 8, porque exige una calificación independiente que el plazo no cubre.

Los entregables principales son siete. Cada uno tiene un indicador PERS, un hito y un responsable. La {T:t02} los lista con su criterio de aceptación. Los requisitos de alto nivel provienen de los umbrales de desempeño. El modelo debe cumplir R² de 0,70 o más y NRMSE de 30 % o menos frente a la referencia. La pendiente debe estar entre 0,65 y 1,35 y el sesgo entre −5,0 y 5,0 µg/m³. Los nodos deben operar con autonomía de 14 días sin sol y una pérdida de paquetes de 10 % o menos. El tablero debe usarse en decisiones documentadas por 75 % o más de los comités.

:::TABLA t02 | Lista de entregables principales con indicador, hito y criterio de aceptación
| Id | Entregable | Indicador PERS | Hito | Criterio de aceptación |
| --- | --- | --- | --- | --- |
| E1 | Red de 100 nodos y 10 gateways operativa | PERS-P01 | H6 (mes 19) y H8 | 100 nodos y 10 gateways con disponibilidad mensual de 90 % o más |
| E2 | Modelo de corrección validado y software registrado | PERS-P02, PERS-R02 | H3 (mes 12) | R² de 0,70 o más, NRMSE de 30 % o menos y 1 registro vigente |
| E3 | Base de datos de colocalización y protocolo de calibración | PERS-R05 | H2 (mes 10) | 60.000 horas-nodo válidas y 4 rotaciones por departamento |
| E4 | Tablero, protocolo de alerta y umbrales validados localmente | PERS-E01, PERS-E02 | H5 (mes 17) | Uso en 75 % o más de los comités y línea base de falsas alarmas medida |
| E5 | Artículos científicos en revistas Q1 o Q2 | PERS-P03 | H7 (mes 23) | 2 sometidos y al menos 1 aceptado al mes 24 |
| E6 | Actividades de apropiación social y custodios formados | PERS-P04, PERS-E03 | H8 (mes 24) | 29 actividades documentadas y 60 personas certificadas o más |
| E7 | Convenios de custodia con partida y cláusula de apertura | PERS-S01, PERS-S02 | H5 y H8 | Convenios firmados por tramo; 70 % de continuidad a los 12 meses del cierre |
:::NOTA *Nota.* Elaboración propia con datos de la ficha maestra §4, §6 y §8 e indicadores.py. Los criterios de aceptación son PROPUESTO. Los indicadores S01 y S02 se miden después del cierre. Decimales con coma y miles con punto.

La tabla muestra que seis de los siete entregables se verifican durante la ejecución y uno depende del posproyecto. Los entregables E1 a E4 son las condiciones de las compuertas. El entregable E5 depende de tiempos editoriales ajenos. El entregable E7 es el más expuesto, porque requiere partidas que las alcaldías aún no han comprometido. Esa exposición explica por qué la compuerta C2 exige convenios con partida antes de liberar el tramo 3.


## 21.4 Objetivos Medibles

Los criterios de éxito traducen los tres objetivos específicos en metas numéricas con plazo. Cada criterio tiene un umbral, un medio de verificación y un momento de evaluación. El éxito no se declara por completar actividades, sino por cumplir umbrales verificados por una fuente independiente. La {T:t03} presenta los criterios y los indicadores clave del proyecto. Los umbrales de desempeño toman como ancla los protocolos de la U.S. Environmental Protection Agency [EPA] (2021) para uso informativo en sitio fijo.

:::TABLA t03 | Criterios de éxito medibles e indicadores clave del proyecto
| Objetivo | Criterio de éxito | Umbral | Verificación | Momento |
| --- | --- | --- | --- | --- |
| OE1: medición verificada | Error de los nodos frente a la referencia | R² de 0,70 o más y NRMSE de 30 % o menos en los tres tramos | Informe de validación y ensayo con laboratorio externo | Meses 12, 17 y 24 |
| OE2: disponibilidad de la red | Disponibilidad mensual de nodos y pérdida de paquetes | Disponibilidad de 90 % o más y pérdida de 10 % o menos | Registro de la plataforma e inventario | Cada mes; compuerta C2 |
| OE3: uso institucional | Comités que usan el tablero en decisiones documentadas | 75 % o más de los 15 comités al mes 24 | Actas de comité con referencia al tablero | Meses 12, 17 y 24 |
| Gestión | Ejecución presupuestal | Desviación absoluta de 5 % o menos al cierre | Informe financiero conciliado | Cada mes |
| Capacidad | Personas certificadas en operación y mantenimiento | 60 personas o más | Evaluaciones prácticas aprobadas | Semestral |
| Continuidad | Nodos operados por custodios con partida | 70 % o más a los 12 meses del cierre | Evaluación externa posproyecto | Meses 30 y 36 |
:::NOTA *Nota.* Elaboración propia con datos de la ficha maestra §3, §6 y §8. Los umbrales de desempeño son PROPUESTO con ancla en EPA (2021). La línea base de error se mide en el tramo 1 y no existe todavía (VACIO). Decimales con coma.

Dos criterios dependen de líneas base que aún no existen. El error de partida de los nodos se mide en el tramo 1. La reducción relativa de falsas alarmas se calcula con la tasa inicial de ese tramo. Por esa razón las metas de esos criterios son aspiraciones hasta la compuerta C1. El acta de constitución acepta esa condición porque cada compuerta convierte una aspiración en compromiso cuando la línea base existe.


## 21.5 Alcance y Exclusiones

La delimitación del alcance protege al proyecto de compromisos que no puede sostener. Lo que está dentro del alcance coincide con los siete entregables. Lo que queda fuera se declara de forma expresa. Entre las exclusiones, la más importante es la ausencia de afirmaciones sobre efectos en salud. La {T:t04} presenta la matriz de alcance con supuestos y restricciones.

:::TABLA t04 | Matriz de alcance con inclusiones, exclusiones, supuestos y restricciones
| Categoría | Contenido |
| --- | --- |
| Dentro del alcance | Red de 100 nodos y 10 gateways en Caldas, Cundinamarca y Valle del Cauca; modelo de corrección en el gateway; gemelo digital y tablero; protocolo de alerta con umbrales locales; 29 actividades de apropiación social; 60 personas formadas; convenios de custodia por tramo; evaluación externa en los meses 12 y 24 |
| Fuera del alcance | Efectos en salud o reducción de morbilidad; cobertura de otros departamentos; más de 100 nodos operativos; un cuarto tramo; un año adicional de custodia; calificación formal TRL 8; vigilancia de otros contaminantes; financiación de la medición posproyecto |
| Supuestos | Territorio y alianza ejecutora definidos por instrucción del usuario; compuertas C1 y C2 aprobadas en los meses 12 y 17; acceso vial en ventanas secas; comités constituidos con sesiones periódicas; custodios con competencia jurídica y partida |
| Restricciones | Duración de 24 meses y 104 semanas; tope declarado de 14.000.000.000 COP sin verificar; sin cotizaciones soportadas; términos de referencia no aportados; contrapartida sin certificar; ningún dato de salud en el diseño |
:::NOTA *Nota.* Elaboración propia con la ficha maestra §1, §3, §4 y §12. Las opciones fuera del alcance son opciones de ampliación condicionadas a los términos de referencia y no se presupuestan (DEC-F06).

Las exclusiones tienen una consecuencia práctica. Si el financiador pide ampliar la cobertura o añadir un cuarto tramo, el cambio exige una modificación formal del acta. Exige también un nuevo presupuesto y una revisión de riesgos. El acta no impide esa ampliación. La condiciona a la evidencia de las compuertas, porque ampliar antes de validar el modelo repetiría el error que el proyecto pretende corregir.

La gestión del cambio sigue una regla simple. Todo cambio que altere el alcance, el plazo o el valor total pasa por el comité directivo. Queda registrado con su efecto sobre los criterios de éxito. Collingridge (1980) advierte que el costo de corregir una tecnología crece con el tiempo y que el control es más fácil al inicio. Por eso el acta concentra las decisiones difíciles de revertir, como la compra de equipos, en las compuertas. Deja las decisiones reversibles, como el calendario de talleres, en manos de la gerencia.


## 21.6 Riesgos de Alto Nivel

El registro del capítulo 10 contiene 12 riesgos. El acta resume los cinco de mayor valor monetario esperado. Esos cinco suman 471,0 millones de COP, que equivalen a 74,0 % de la reserva de contingencia. Se ordenan por valor esperado y no por nivel, porque el valor esperado combina probabilidad e impacto en una misma escala monetaria (ISO, 2018). La {T:t05} presenta los cinco con su estrategia preliminar.

:::TABLA t05 | Riesgos de alto nivel con valor esperado y estrategia preliminar
| Riesgo | Descripción | Nivel | EMV (millones de COP) | Estrategia preliminar |
| --- | --- | --- | --- | --- |
| R-FIN-01 | La devaluación del peso encarece los equipos importados. | ALTO | 165,0 | Mitigar: Compra por tramo con cobertura cambiaria y cotizaciones vigentes. |
| R-TEC-01 | La humedad y el polvo saturan los cabezales ópticos y sesgan PM2,5 y PM10. | EXTREMO | 150,0 | Mitigar: Modelo de corrección por humedad, banco de calibración y reposición de cabezales. |
| R-EXT-01 | Deslizamientos o réplicas bloquean vías y retrasan la instalación. | ALTO | 60,0 | Aceptar y mitigar: Instalación en ventanas secas, técnicos locales y holgura en el cronograma. |
| R-ORG-02 | Los custodios no asumen la operación en el posproyecto. | ALTO | 60,0 | Mitigar: Convenios por tramo, formación de custodios y cláusula de apertura. |
| R-ORG-01 | Los comités de gestión del riesgo no adoptan el tablero ni el protocolo. | ALTO | 36,0 | Mitigar: Co-diseño de umbrales, formación por comité y uso piloto con registro de decisiones. |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py (RIESGOS). Probabilidad e impacto son PROPUESTO y NO_VERIFICADO; el EMV es CALCULADO. Los cinco riesgos suman 471,0 millones de COP; la reserva total es de 636,0 millones. Decimales con coma.

Los cinco riesgos afectan las compuertas y el cronograma. R-TEC-01 amenaza la compuerta C1, porque la saturación de los cabezales sesgaría la validación. R-ORG-01 y R-ORG-02 amenazan la compuerta C2, porque el uso y los convenios dependen de actores externos. R-FIN-01 y R-EXT-01 amenazan el cronograma y el costo de cada tramo. El comité directivo recibe un informe de estos cinco riesgos en cada compuerta.


## 21.7 Hitos Principales

El cronograma de hitos reúne los nueve puntos de control del capítulo 9. Dos de ellos son compuertas de decisión, H3 en el mes 12 y H5 en el mes 17. El cierre H8 en el mes 24 es la tercera compuerta. Las compuertas liberan compras por 388,0 y 306,0 millones de COP. Las fechas exactas dependen de la fecha del acta de inicio [DATO_USUARIO: fecha del acta de inicio]. La {F:f01} presenta la línea de tiempo.

:::FIGURA f01 | Nueve hitos entre el mes 2 y el mes 24; C1 y C2 liberan los tramos 2 y 3 | Nota. Elaboración propia con datos de maestro.py (HITOS y TRAMOS). Línea de tiempo en meses de calendario (1 mes = 52/12 semanas); hitos H0 a H8 del cronograma CPM de 104 semanas. Python 3 y matplotlib; script c21_figs.py; sin semilla; corte del 13 de octubre de 2026.

La línea de tiempo muestra que 10 de los 24 meses transcurren antes de que exista una colocalización terminada (H2, mes 10). La evidencia que sostiene toda la decisión llega, por tanto, tarde en el plan. Esa característica es inherente a un piloto con colocalización de 16 semanas. El acta la acepta y la compensa con las compras por tramo, que limitan la exposición financiera antes de C1.


## 21.8 Presupuesto Resumido

El presupuesto resumido presenta el total, la distribución por fuente y las reservas. El valor solicitado al SGR es de 8.729.840.000 COP, que equivale a 62,4 % del tope declarado. La contrapartida es de 2.110.000.000 COP. La reserva de contingencia, de 636.000.000 COP, está incluida en el valor solicitado y suma los valores esperados de los 12 riesgos. La {T:t06} presenta el resumen por rubro y por fuente.

:::TABLA t06 | Resumen presupuestal por rubro y por fuente
| Concepto | Valor (millones de COP) | Porcentaje del SGR |
| --- | --- | --- |
| Personal | 4.382,9 | 50,2 % |
| Equipos y software | 1.885,6 | 21,6 % |
| Materiales e insumos | 242,9 | 2,8 % |
| Servicios técnicos | 846,0 | 9,7 % |
| Viajes y viáticos | 204,5 | 2,3 % |
| Otros rubros | 532,0 | 6,1 % |
| Reserva de contingencia | 636,0 | 7,3 % |
| Total solicitado al SGR | 8.729,8 | 100,0 % |
| Contrapartida de la entidad ejecutora (especie) | 1.100,0 | — |
| Contrapartida de la empresa tecnológica (efectivo y especie) | 1.010,0 | — |
| Total del proyecto | 10.839,8 | — |
:::NOTA *Nota.* Elaboración propia con datos de maestro.py y de la ficha maestra §5. La reserva de contingencia depende de su admisibilidad como rubro según los términos de referencia (VACIO). La contrapartida no está certificada. Decimales con coma.

La holgura entre lo solicitado y el tope declarado es de 5.270.160.000 COP. El acta no la presupuesta. Se describe como opciones de ampliación que dependen de los términos de referencia. Esa decisión busca que cada peso solicitado tenga una actividad que lo justifique. Si la reserva de contingencia no se admite como rubro, el valor solicitado baja a 8.631.260.000 COP y la reserva debe absorberse de otra manera. El capítulo 8 desarrolla cada línea.


## 21.9 Stakeholders Clave

El patrocinador del proyecto es el financiador, el Sistema General de Regalías con el Ministerio de Ciencia, Tecnología e Innovación. La entidad ejecutora designa al director del proyecto y responde por los resultados. Los demás interesados se agrupan según el modelo de saliencia, que combina poder, legitimidad y urgencia (Mitchell et al., 1997). El análisis de la sección 4.4-MDR.5 identificó 12 actores. El documento 1000X-08 los desagrega en 18 interesados. La {F:f02} presenta el mapa por tipo de relación.

:::FIGURA f02 | Doce actores sin relevancia evaluada; solo el convocante tiene poder documentado | Nota. Elaboración propia con datos de la sección 4.4-MDR.5; sin nombres de personas. Poder, legitimidad y urgencia NO_EVALUADO salvo el poder del convocante. Borde grueso: actor con veto. Python 3 y matplotlib; script c21_figs.py; sin semilla; corte del 13 de octubre de 2026.

Kotter (2012) recomienda formar una coalición con poder, experticia y credibilidad para liderar un cambio. El comité directivo cumple esa función en el proyecto, con representantes de la entidad ejecutora, la empresa tecnológica y el financiador. La coalición incorpora además a un representante de los comités de gestión del riesgo. Ese representante no vota en las compuertas, pero presenta el estado del uso del tablero (PROPUESTO). Esa participación aumenta la legitimidad de las decisiones y reduce el riesgo R-ORG-01. Los nombres y las funciones se definen en el acta de inicio [DATO_USUARIO: integrantes del comité directivo].

El mapa muestra una asimetría que el acta reconoce. Solo el convocante tiene poder documentado. Las alcaldías tienen veto sobre la custodia, pero ninguna firmó un compromiso. Los comités de gestión del riesgo deciden el uso del tablero, y su participación no está asegurada. La mitigación consiste en negociar los convenios por tramo antes de cada compuerta. Incluye también a los comités en el co-diseño desde el mes 3. Ningún actor firmó compromiso alguno porque la alianza es un supuesto.


## 21.10 Autorización

La autorización requiere las firmas del patrocinador, del representante legal de la entidad ejecutora y del director del proyecto. El acta confiere al director la facultad de aplicar los recursos aprobados. Le permite reasignar dentro de los rubros del presupuesto, hasta un límite que fija el comité directivo [DATO_USUARIO: límite de reasignación sin autorización]. Cualquier cambio de alcance, plazo o valor total exige una modificación firmada. Las compuertas C1, C2 y C3 las decide el comité directivo, y no el director. La {T:t07} deja los espacios de firma.

El PMI (2021) separa dos autoridades. El director de proyecto gestiona el trabajo dentro de límites. El patrocinador aprueba los cambios que los superan. El acta adopta esa separación. El director gestiona el cronograma de las actividades con holgura, reasigna recursos dentro de un rubro y aprueba respuestas a riesgos de nivel medio. El patrocinador y el comité aprueban las compuertas, los cambios de alcance y el uso de la reserva por encima de la delegación.

:::TABLA t07 | Firmas de autorización del acta de constitución
| Rol | Nombre | Cargo | Firma | Fecha |
| --- | --- | --- | --- | --- |
| Patrocinador (financiador) | [DATO_USUARIO: nombre] | [DATO_USUARIO: cargo] | [DATO_USUARIO: firma] | [DATO_USUARIO: fecha] |
| Representante legal de la entidad ejecutora | [DATO_USUARIO: nombre] | [DATO_USUARIO: cargo] | [DATO_USUARIO: firma] | [DATO_USUARIO: fecha] |
| Representante de la empresa tecnológica aliada | [DATO_USUARIO: nombre] | [DATO_USUARIO: cargo] | [DATO_USUARIO: firma] | [DATO_USUARIO: fecha] |
| Director del proyecto | [DATO_USUARIO: nombre] | [DATO_USUARIO: cargo] | [DATO_USUARIO: firma] | [DATO_USUARIO: fecha] |
:::NOTA *Nota.* Elaboración propia. Ningún dato de esta tabla se aportó; todos los campos son VACIO. El acta no produce efectos hasta que las cuatro partes la firmen.
