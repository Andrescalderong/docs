# BRIEF COMÚN PARA REDACTORES (leer completo antes de escribir)

Eres redactor técnico de un proyecto de ciencia, tecnología e innovación (CTeI) que se formula con el metaprompt GENESIS-CTeI 36.10 RC2.
El producto final es UN documento en español (Word y PDF). Tu parte es uno o varios capítulos. Trabajas sobre archivos; no recibes más contexto que este brief.

## 1. Rutas (todas absolutas)
RAIZ = /tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy
- Ficha maestra de cifras y decisiones: RAIZ/maestro/FICHA_MAESTRA.md (LEER PRIMERO; es la única fuente de cifras cardinales).
- Datos programables: RAIZ/maestro/maestro.py, indicadores.py, alternativas.py (python3; `sys.path.insert(0, RAIZ+'/maestro')`).
- Banco cerrado de referencias: RAIZ/refs/BANCO_REFERENCIAS.md (y banco.json). SOLO se citan obras de ese banco.
- Especificación del metaprompt por capítulo: RAIZ/spec/spec_cap1_4.txt (capítulos 1 a 4), RAIZ/spec/spec_cap5_21.txt (5 a 21), RAIZ/spec/spec_m9_m10.txt (paquete 1000X y estrategia), RAIZ/spec/spec_m5_m7.txt (pasos 5 a 7), RAIZ/spec/spec_modulos_a.txt (completitud, APA 7, profundidad doctoral, documento y figuras), RAIZ/spec/spec_redaccion.txt (reglas de redacción). Tu asignación indica qué capítulo leer.
- Entradas del usuario (solo lectura): /tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/work/informe.md (informe_FINAL: vigilancia tecnológica y bibliometría de 42 documentos; las cifras con página están en §1.3, §3.1, §4, §5, §6, §7 y la bibliografía en §13.2; lo llamamos F-INF) y work/problematica.md (expediente E3-P00 a E3-P21 y pasos 1 a 6 del usuario; F-E3). Resumen de sus defectos: work/notas_hallazgos.md. NO copies de F-E3 cifras que la ficha maestra corrige.
- Resultados previos de análisis causal (solo lectura): /home/user/docs/genesis-e4-e3p00/SECCION_4_3/, SECCION_4_4/ (Vester y MICMAC), SECCION_4_4_MDR/ (decisión, teoría del cambio, sostenibilidad, premortem y escenarios) y SECCION_4_5/ (árbol de problemas).
- Estilo de figuras: RAIZ/figs/estilo.py (plantilla única). Verificador: RAIZ/build/check_cap.py.
- Salida: RAIZ/caps/ (un archivo .md por capítulo o parte; el nombre lo fija tu asignación).

## 2. Qué es el proyecto (resumen; el detalle está en la ficha maestra)
Red IoT híbrida Edge-Cloud con gemelo digital para vigilar PM2,5 y PM10 en sitios de remoción de escombros posterremoto en Caldas, Cundinamarca y Valle del Cauca. 100 nodos, 10 gateways, 3 referencias, tramos 1 a 3 con compuertas C1 y C2, 24 meses, TRL 4 a 7. Territorio y alianza son SUPUESTO por instrucción del usuario. Los términos de referencia (TdR) no se aportaron. El proyecto no promete efectos en salud: promete mediciones verificadas, uso institucional y continuidad.

## 3. Reglas de contenido (NTC 1.1 y metaprompt)
1. Una cifra, una fuente: toda cifra cardinal sale de la ficha maestra o de F-INF con página. Prohibido inventar cifras, normas, DOI, cuartiles, páginas, nombres de personas o entidades. Si falta un dato que solo el usuario posee, escribe `[DATO_USUARIO: descripción]` (es la única forma permitida de marcador entre corchetes).
2. Naturaleza de los datos (ejes independientes): DOCUMENTADO, DECLARADO, CALCULADO, INFERIDO, SUPUESTO, PROPUESTO, ILUSTRATIVO, VACIO; verificación: VERIFICADO, PARCIALMENTE_VERIFICADO, NO_VERIFICADO, CONTRADICTORIO, NO_APLICA. En tablas usa una columna «Naturaleza» cuando haya cifras no sustentadas en una cita; en el texto marca entre paréntesis (PROPUESTO), (SUPUESTO), etc. Todo lo que el banco marca NO_VERIFICADO sigue así: no afirmes «verificado».
3. Afirmaciones: sin causalidad no identificada; correlación, asociación y causalidad por separado; «sin evidencia, vacío» antes que relleno. Prohibido «garantiza», «demuestra matemáticamente», «inédito», «sin precedentes», «óptimo» como juicio absoluto.
4. Profundidad: cada viñeta del temario de tu capítulo (spec) se desarrolla en prosa continua (≥ 250 palabras por viñeta cuando la spec lo exige) con los cinco movimientos sin rotularlos: (1) oración temática; (2) constructo con definición y fuentes seminales; (3) debate con al menos dos posiciones contrastadas y autores; (4) anclaje al proyecto con dato propio; (5) consecuencia metodológica (qué decisión del proyecto se deriva). Las tablas acompañan la prosa: cada tabla va precedida de un párrafo que la introduce y seguida de otro que extrae su consecuencia.
5. Extensión: los mínimos de palabras, tablas, figuras y referencias de tu asignación son bloqueantes. No rellenes con generalidades: añade evidencia, análisis, casos del corpus, comparaciones y consecuencias. Si de verdad no puedes alcanzar un mínimo sin inventar, declara la insuficiencia en una línea final `%% INSUFICIENCIA: …` y entrega lo real.
6. Densidad de citas en capítulos narrativos: ≥ 1 cita por cada 150 palabras; ≥ 60 % de citas parentéticas, 25–35 % narrativas, ≤ 5 citas textuales literales por capítulo (con página). No cites una fuente para una afirmación que la fuente no contiene: si usas F-INF, toma la cifra y la página del informe.
7. Lenguaje inclusivo con sustantivos colectivos («el personal», «la población», «la comunidad»); sin barras, arrobas ni dobletes.

## 4. Reglas de redacción (mecánicas; el verificador las comprueba)
- Español académico, objetivo, sobrio. Sin metáforas. Sin adjetivos enfáticos (abrumador, dominante, crucial, drástico, enorme, extraordinario, revolucionario, etc.).
- Oraciones de 25 palabras o menos (excepto celdas de tabla y listas de referencias). Cada párrafo incluye al menos una oración de 12 palabras o menos. Orden sujeto-verbo-complemento; voz activa; registro impersonal («el proyecto propone», «se mide»); sin primera persona del plural.
- Cada párrafo abre con una oración temática y termina en punto. No empieces oraciones con «Pero». No uses rayas dobles (—…—) ni glosas parentéticas de relleno. Un solo «falta de» por oración. No uses «etc.», «entre otros», «y así sucesivamente», puntos suspensivos.
- Evita comodines: cosa, hacer, tener, tema, factor, elemento, aspecto (sustituye por el término exacto). Sin gerundio de posterioridad. «Sino» solo tras negación explícita. Tildes diacríticas correctas.
- Enumeraciones con paralelismo sintáctico. Siglas desarrolladas en la primera aparición del documento (no del capítulo): usa la sigla desarrollada cuando el capítulo la introduce por primera vez.
- Números: palabras del cero al nueve y cifras desde 10, salvo unidades, porcentajes, fechas y cifras exactas. Decimales con coma y miles con punto (1.234,5). Moneda: «COP» o «millones de pesos colombianos (COP)».
- Marca de estado con etiquetas textuales, nunca símbolos pictográficos.

## 5. Formato de salida (Markdown con directivas; el ensamblador las convierte a Word)
Primera línea del archivo: `%% PREFIJO: N` donde N es el número de capítulo (o el prefijo que indique tu asignación).
Encabezados (jerarquía APA 7 de cinco niveles con numeración decimal declarada una vez en el documento):
- `# Capítulo N. Título` = nivel 1 (centrado, negrita). Un solo `#` por capítulo (el archivo de la segunda parte de un capítulo NO repite `#`).
- `## N.1 Título` = nivel 2; `### N.1.1 Título` = nivel 3.
- Nivel 4 = párrafo que empieza con `**Título del apartado.** Texto…` (negrita, punto final, texto en la misma línea).
- Nivel 5 = párrafo que empieza con `***Título del ítem.*** Texto…` (negrita cursiva, punto final, texto en la misma línea).
- No saltes niveles. No uses viñetas como títulos. No numeres títulos de nivel 4 o 5.
Tablas: 
```
:::TABLA id | Título en cursiva sin punto final
| Encabezado A | Encabezado B |
| --- | --- |
| dato | dato |
:::NOTA *Nota.* Elaboración propia con datos de F-INF (p. 12). Naturaleza: PROPUESTO. Decimales con coma.
```
`id` es único dentro de tu archivo (t01, t02…). Las filas no se truncan ni llevan «…». Celdas de ≤ 15 palabras en tablas de presupuesto y cronograma.
Menciones: en el texto escribe `{T:id}` y `{F:id}`; el ensamblador las convierte en «Tabla 5.3» o «Figura 5.1». Cada tabla y figura se menciona ANTES de que aparezca (APA-T05/F05). Prohibido «la tabla siguiente» o «la figura anterior».
Figuras: una línea `:::FIGURA id | Título en cursiva sin punto final | Nota. Fuente, método, software y parámetros reproducibles (semilla, tamaño del corpus, año de corte).`
El archivo de imagen lo generas tú con un script python propio: RAIZ/figs/scripts/c{PREFIJO}_{id}.py (o un único script por capítulo que genere varias) que usa `estilo.py` y guarda `E.guardar(fig, 'c{PREFIJO}_{id}')` → RAIZ/figs/out/c{PREFIJO}_{id}.png y .svg. Reglas de figuras: fondo transparente; texto siempre #2A3439; máximo 4 colores de datos de la paleta (#6699CC, #9EB9D4, #B9D9EB, #F5F5F5) con segundo canal (trama, marcador o etiqueta directa); título H1 = hallazgo clave, H2 = variable, periodo y unidades; etiquetas directas; sin borde superior ni derecho; sin sombras ni degradados; tamaño 10 × 7 pulgadas (o 10 × 4,5 si es ancha). Todo dato de una figura viene de las fuentes: nunca inventes valores. Revisa visualmente cada figura: `python3 RAIZ/figs/ver.py RUTA.png` crea una vista JPG sobre fondo blanco (ábrela con la herramienta de lectura de imágenes).
Referencias: NO escribas lista de referencias en tu capítulo (se genera del banco). Cita con el formato del banco (columna «Cita en el texto»): `(Bang et al., 2026)`, `Bang et al. (2026)`, `(Jayaratne et al., 2018; Barkjohn et al., 2021)`, dos autores con «y» (`Braybrooke y Lindblom, 1963`). Si no encuentras una obra en el banco, NO la cites: reformula con las que existen. Para páginas de F-INF usa la forma `(Bang et al., 2026, pp. 6-8)` tomada del informe.
Placeholders de datos del usuario: `[DATO_USUARIO: nombre de la entidad ejecutora]`.

## 6. Verificación obligatoria antes de entregar
Ejecuta `python3 RAIZ/build/check_cap.py RAIZ/caps/TU_ARCHIVO.md -v --minpal N --mintab N --minfig N --minref N` (valores de tu asignación) y corrige hasta que diga SIN PROBLEMAS, salvo `densidad de citación` (informativa) y los problemas que solo se resuelven con insuficiencia declarada. Revisa tú mismo que cada cifra coincide con la ficha maestra. Lee tu texto completo una vez antes de cerrar.

## 6b. Límites de escritura
Solo creas o modificas archivos en RAIZ/caps/ (tus archivos), RAIZ/figs/scripts/ y RAIZ/figs/out/ (tus figuras). NO modifiques maestro/, refs/, spec/, build/, estilo.py, ni archivos del repositorio. Si necesitas una referencia que no está en el banco o una cifra que no está en la ficha, repórtalo en tu respuesta final en lugar de inventarla.

## 7. Tu respuesta final (breve)
Informa: archivos escritos, conteos reales (palabras, tablas, figuras, citas distintas), resultado del verificador, cualquier insuficiencia declarada y cualquier dato de la ficha maestra que consideres contradictorio. No pegues el texto del capítulo en tu respuesta.
