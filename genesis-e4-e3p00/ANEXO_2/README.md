# Anexo 2. Documento técnico — Convocatoria 56 del SGR (proyecto SGR_CONV56_AIRE)

Fecha de corte: 24 de octubre de 2026. Estado: borrador completo con datos pendientes de la alianza.

El documento sigue la plantilla oficial del Anexo 2 de los términos de referencia (TdR) v1.6, con los 50 títulos de nivel 1 y 2 del numeral 10.6 en su texto original, encabezado y pie oficiales, referencias en APA 7, 108 tablas y 28 figuras. Incorpora un laboratorio de modelación y un gemelo predictivo de demolición dentro de los tres objetivos específicos, sin un cuarto objetivo. El Anexo A reúne el análisis del problema público y de la estructura causal (Vester, MICMAC, inferencia causal, árbol de problemas y teoría del cambio) con 31 tablas y 7 figuras, para no recargar el cuerpo del documento.

## Archivos

| Archivo | Contenido |
| --- | --- |
| anexo_2._documento_tecnico_15.docx y .pdf | Versión de trabajo completa: soporte inicial para la alianza (secciones S.1 a S.7, que se retiran antes de radicar), Anexo 2 y Anexo A. 339 páginas |
| anexo_2._documento_tecnico_15_para_radicar.docx y .pdf | Anexo 2 sin el soporte inicial y sin el Anexo A. 275 páginas. El PDF pesa 2,9 MB, por debajo del límite de 3 MB por archivo del SIGP |
| anexo_a._analisis_problema_publico_y_estructura_causal.docx y .pdf | Anexo A como documento independiente, con su propia lista de referencias. 50 páginas. El PDF se carga como otro adjunto del SIGP (hasta 10 MB) |
| guia_explicar_el_proyecto.docx y .pdf | Guía de cuatro páginas para explicar el proyecto a los integrantes de la alianza en lenguaje sencillo: la frase de apertura, la figura del recorrido del terremoto del 10 de agosto a la decisión del comité, las etapas de los 24 meses, lo que hace y recibe cada integrante, un guion de cinco minutos con prueba de comprensión, un glosario de palabras que se deben evitar, preguntas frecuentes y lo que se necesita esta semana |
| anexo_a._respaldo_fichas_y_matrices.xlsx | Libro de respaldo del Anexo A: variables, 210 fichas de dirección, matrices de S0 a S4 con totales por fórmula, clases, potencias y ciclos de S2 |
| fuentes/ | Secciones en Markdown (`sec/`, con `sA.md` para el Anexo A), datos maestros y generadores de tablas (`v2/`, con `causal.py`), resultados del cálculo estructural (`data_causal/`), guiones de figuras (`figs/`), banco cerrado de referencias (`refs/`), herramientas de ensamblado y control (`build/`) y la fuente de la guía (`guia/`) |

## Alianza modelada

| Integrante | Naturaleza | Objetivo que lidera |
| --- | --- | --- |
| Entidad proponente | Universidad (IES); aloja y valida el laboratorio de modelación | OE1 |
| Aliada 1 | Municipio de Caldas, Cundinamarca o Valle del Cauca; usuario del laboratorio | OE3 |
| Aliada 2 | Actor del SNCTI con reconocimiento vigente de MinCiencias | Ninguno; participa en actividades de formación, datos y validación |
| Aliada 3 | Empresa tecnológica | OE2 |

## Laboratorio de modelación predictiva de demolición

El laboratorio estima, antes de demoler una edificación, la emisión de polvo de la obra, su dispersión y la concentración esperada de PM2,5 y PM10 en receptores cercanos, con escenarios de medidas de control. Cada evaluación sirve a la demolición en curso y deja un modelo reutilizable para las siguientes.

- Ubicación en el proyecto: no es un objetivo aparte. La validación con eventos reales pertenece al OE1 (actividad 1.7), el diseño, la dotación y la calibración al OE2 (actividades 2.5 a 2.7) y el protocolo de evaluación previa al OE3 (actividad 3.5).
- Método: inventario de la demolición, emisión con factores AP-42 13.2.3 de la EPA ajustados con polvo local, dispersión con AERMOD de tamizaje y simulación del flujo entre edificios, modelo sustituto supervisado y evaluación previa con escenarios de control.
- Dotación: servidor de cómputo, 4 estaciones meteorológicas, dron con LiDAR y GNSS, 2 monitores portátiles y licencias de software de pago único.
- Valor: 1.671.500.000 COP del SGR (16,7 %), en 19 líneas del presupuesto, y 144.000.000 COP de contrapartida en especie de la universidad. Son estimaciones de formulación que deben confirmarse con cotizaciones.
- Madurez y metas: el gemelo pasa de TRL 3 a TRL 6. La validación exige al menos seis eventos reales al mes 22, con FAC2 ≥ 0,5 y sesgo fraccional absoluto ≤ 0,3, y el proyecto entrega 12 evaluaciones previas al mes 24. La línea base es el tamizaje con factores genéricos.
- Límites: el resultado es una evaluación previa y no autoriza ni prohíbe una demolición. El proyecto no afirma efectos en la salud.

## Cifras maestras

- Valor solicitado al SGR: 10.022.840.000 COP (71,6 % del tope de 14.000.000.000 COP).
- Contrapartida: 2.374.000.000 COP, de los cuales 210.000.000 COP en efectivo. El aporte del actor del SNCTI se suma cuando se certifique.
- Valor total: 12.396.840.000 COP.
- Duración: 24 meses (104 semanas); 22 actividades; 9 productos del programa 3906 de la MGA.
- Red: 100 nodos, 10 gateways y 3 monitores de referencia en 12 municipios y 15 comités de gestión del riesgo; TRL 4 al inicio y TRL 8 al cierre.
- Reparto del valor solicitado: Caldas 1.233.519.514 COP, Cundinamarca 1.292.920.970 COP, Valle del Cauca 1.233.519.516 COP y componentes transversales 6.262.880.000 COP.
- Riesgos: 19 en el registro, 8 probables y 15 con impacto mayor. Hitos: H0 a H11 y compuertas C1 a C3.

## Conexión con la emergencia

El documento toma como evento de origen el terremoto del 10 de agosto de 2026, fecha que aportó la alianza y que debe confirmarse con el acto de declaratoria (Decreto 1261 de 2026, modificado por el Decreto 1348 de 2026). La cadena es: terremoto, demolición y remoción de escombros en los centros urbanos, polvo que respiran operarios y vecinos, y un comité de gestión del riesgo que debe decidir sin un dato confiable ni una estimación previa. La figura 4.1 del Anexo 2 y la figura S.1 del soporte la muestran. El eslabón de la remoción de escombros sigue siendo un supuesto de trabajo hasta que el municipio aliado entregue tres soportes: el acto de calamidad pública, el reporte de afectación de las edificaciones y el cronograma de demoliciones y remoción por sitio.

## Datos pendientes

El texto contiene 153 datos distintos con la marca `[Diligenciar: …]` en color verde, como indica la plantilla. La tabla S.9 de la versión de trabajo los agrupa por sección y por responsable. Quedan doce decisiones por confirmar (tabla S.8): departamento del municipio aliado, valor del aporte del actor del SNCTI, titularidad de los bienes y resultados, nivel TRL comprometido, criterio de aceptación de las compuertas, demanda territorial, sede y validación del laboratorio, valor del laboratorio, título y número de objetivos, acceso a demoliciones reales para validar, ratificación de las fichas del Anexo A y diseño con asignación aleatoria de la calibración. La hoja de ruta de la tabla S.7 parte del sábado 24 de octubre y fija la radicación anticipada para el viernes 30 de octubre. El cierre oficial es el martes 3 de noviembre de 2026 a las 4:00 p. m.

## Controles ejecutados

- Los 50 títulos de nivel 1 y 2 de la plantilla coinciden con `fuentes/TITULOS.md`, con el mismo texto, nivel y orden (`fuentes/build/check_titulos.py`).
- Validación de los tres DOCX con el validador de esquemas de Office: sin errores.
- Frases de 25 palabras o menos, citas dentro del banco cerrado, numeración y mención de tablas y figuras, y ausencia de vocabulario interno: verificadas por sección con `fuentes/v2/check.sh`.
- Revisión visual de las páginas con figuras y tablas nuevas. Cada figura cabe con su rótulo y su nota en una sola página, y ninguna página queda sin contenido (`fuentes/build/paginas_vacias.py`).
- De las 113 referencias del Anexo 2, 58 están verificadas, 19 parcialmente y 36 no se verificaron contra la fuente original. El Anexo A agrega 8 referencias (22 en su lista independiente: 7 verificadas, 2 parcialmente y 13 no verificadas). Las cinco fuentes del laboratorio (Cimorelli et al., 2005; Chang y Hanna, 2004; EPA, 1995; Dorevitch et al., 2006; Lateb et al., 2016) están parcialmente verificadas. Deben revisarse antes de radicar.
- Anexo A: las matrices de influencia se recalculan desde las fichas; las clases por mediana, los totales y los 144 ciclos de S2 se comprueban contra los resultados del cálculo estructural antes de generar cada tabla. Los 210 juicios de influencia son de formulación y ningún panel externo los ha adjudicado.

## Reconstrucción

Los guiones usan rutas absolutas del entorno de trabajo y deben ajustarse (`fuentes/v2/check.sh`, `fuentes/v2/m2.py`, `fuentes/figs/scripts/_comun.py` y `fuentes/build/lo_export_a2.py`). `fuentes/v2/m2.py` importa el libro maestro del proyecto, que está en `PROYECTO_COMPLETO/FUENTES/maestro/maestro.py`. Se requieren pandoc 3.1, LibreOffice con UNO, Python 3 con python-docx, matplotlib, Pillow y pypdf, y la plantilla oficial en `in/anexo2_plantilla.docx`, que no se incluye. Con ella, `python3 build/build_a2.py out/anexo2` genera la versión para radicar; con `LO_DPI=96` el PDF queda por debajo de 3 MB. La bandera `--soporte` incluye el soporte inicial, `--anexo` agrega el Anexo A al final y `--solo-anexo` genera el Anexo A como documento independiente. `python3 build/gen_xlsx_anexoA.py SALIDA.xlsx` genera el libro de respaldo y `build/run_all.sh` ejecuta las cuatro compilaciones en serie.
