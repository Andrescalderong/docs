# Anexo 2. Documento técnico — Convocatoria 56 del SGR (proyecto SGR_CONV56_AIRE)

Fecha de corte: 17 de octubre de 2026. Estado: borrador completo con datos pendientes de la alianza.

El documento sigue la plantilla oficial del Anexo 2 de los términos de referencia (TdR) v1.6, con los 30 títulos textuales del numeral 10.6, encabezado y pie oficiales, referencias en APA 7, 115 tablas y 28 figuras.

## Archivos

| Archivo | Contenido |
| --- | --- |
| anexo_2._documento_tecnico_15.docx y .pdf | Versión de trabajo: incluye al inicio el soporte para la alianza (secciones S.1 a S.7, que se retiran antes de radicar) y el Anexo 2 completo. 262 páginas |
| anexo_2._documento_tecnico_15_para_radicar.docx y .pdf | Anexo 2 sin el soporte inicial. 248 páginas. El PDF pesa menos de 3 MB, límite por archivo del SIGP |
| fuentes/ | Secciones en Markdown (`sec/`), datos maestros y generadores de tablas (`v2/`), guiones de figuras (`figs/`), banco cerrado de referencias (`refs/`) y herramientas de ensamblado (`build/`) |

## Alianza modelada

| Integrante | Naturaleza | Objetivo que lidera |
| --- | --- | --- |
| Entidad proponente | Universidad (IES) | OE1 |
| Aliada 1 | Municipio de Caldas, Cundinamarca o Valle del Cauca | OE3 |
| Aliada 2 | Actor del SNCTI con reconocimiento vigente de MinCiencias | Ninguno; participa en actividades de formación, datos y validación |
| Aliada 3 | Empresa tecnológica | OE2 |

## Cifras maestras

- Valor solicitado al SGR: 8.351.340.000 COP (59,7 % del tope de 14.000.000.000 COP).
- Contrapartida: 2.230.000.000 COP, de los cuales 210.000.000 COP en efectivo. El aporte del actor del SNCTI se suma cuando se certifique.
- Valor total: 10.581.340.000 COP.
- Duración: 24 meses (104 semanas); 17 actividades; 9 productos del programa 3906 de la MGA.
- Red: 100 nodos, 10 gateways y 3 monitores de referencia en 12 municipios y 15 comités de gestión del riesgo; TRL 4 al inicio y TRL 8 al cierre.
- Reparto del valor solicitado: Caldas 1.080.352.848 COP, Cundinamarca 1.139.754.303 COP, Valle del Cauca 1.080.352.849 COP y componentes transversales 5.050.880.000 COP.

## Datos pendientes

El texto contiene 145 datos distintos con la marca `[Diligenciar: …]` en color verde, como indica la plantilla. La tabla S.9 de la versión de trabajo los agrupa por sección y por responsable. Quedan seis decisiones por confirmar (tabla S.8): departamento del municipio aliado, valor del aporte del actor del SNCTI, titularidad de los bienes, nivel TRL comprometido, criterio de aceptación de las compuertas y código de la demanda territorial.

## Controles ejecutados

- Los 50 títulos de nivel 1 y 2 de la plantilla coinciden con `fuentes/TITULOS.md`, en el mismo orden.
- Validación del DOCX con el validador de esquemas de Office: sin errores.
- Frases de 25 palabras o menos, citas dentro del banco cerrado, numeración y mención de tablas y figuras, y ausencia de vocabulario interno: verificadas por sección con `fuentes/v2/check.sh`.
- De las 108 referencias citadas, 58 están verificadas, 14 parcialmente y 36 no se verificaron contra la fuente original. Deben revisarse antes de radicar.

## Reconstrucción

Los guiones usan rutas absolutas del entorno de trabajo y deben ajustarse (`fuentes/v2/check.sh` y `fuentes/build/lo_export_a2.py`). Se requieren pandoc 3.1, LibreOffice con UNO, Python 3 con python-docx, matplotlib y Pillow, y la plantilla oficial en `in/anexo2_plantilla.docx`, que no se incluye. Con ella, `python3 build/build_a2.py out/anexo2` genera la versión para radicar y agregar `--soporte` incluye el soporte inicial.
