# Estado del proyecto completo (corte 15-oct-2026)

Documento: proyecto completo SGR_CONV56_AIRE según GENESIS-CTeI 36.10 RC2, en un solo archivo (Word y PDF).

| Archivo | Contenido |
| --- | --- |
| PROYECTO_COMPLETO_SGR_CONV56_AIRE.docx | 979 páginas en el PDF; encabezados APA 7 de cinco niveles; tablas con bordes APA; figuras con fondo transparente y paleta única |
| PROYECTO_COMPLETO_SGR_CONV56_AIRE.pdf | Misma maquetación, con marcadores, índice, lista de tablas y lista de figuras |
| FUENTES/ | Fuentes de trabajo: Markdown con directivas, libro maestro de datos, generadores, scripts de figuras y de ensamblado |

## Estructura
Parte I (pasos 0 a 7), Parte II (capítulos 1 a 21), Parte III (paquete 1000X, diez documentos, y capítulo de estrategia) y cierre F-01 a F-04.

## Verificación ejecutada
- Verificador mecánico `build/check_cap.py` por archivo: palabras de prosa, tablas, figuras, orden de mención, citas frente al banco, oraciones de más de 25 palabras, términos enfáticos, marcadores de omisión.
- Los 21 capítulos cumplen los mínimos del metaprompt (palabras, tablas, figuras, referencias); la Tabla C.1 del cierre lo detalla.
- El archivo DOCX valida contra el esquema (validate.py: PASSED).
- Citas y referencias: 161 obras en el capítulo 19; 44 (27,3 %) son de 2021 a 2026.

## Limitaciones que el documento declara
- Los términos de referencia de la convocatoria no se aportaron. El territorio, el evento y la alianza son supuestos por instrucción del usuario.
- 270 descripciones distintas de datos pendientes del usuario (463 apariciones) quedan como [DATO_USUARIO: …] y se registran en la Tabla C.3.
- Cartas, hojas de vida, certificados, cotizaciones y términos de referencia no existen: el capítulo 20 entrega listas de verificación para esos documentos.
- No se ejecutaron corrector ortográfico ni lectura de un tercero independiente.
- Criterio de 70 % de referencias de los últimos cinco años: NO CUMPLE (27,3 %). Criterio de cuartiles: no determinable con los archivos disponibles.
- Los puntajes multicriterio, las probabilidades de riesgo y las metas de indicadores son PROPUESTOS y requieren ratificación del panel evaluador.
- La huella SHA-256 del maestro es una constante declarada en la conversación; no es el SHA-256 de `maestro/maestro.py`.
- La reserva de contingencia (636,0 millones de COP) redondea la suma exacta de 636,5 millones con la regla del par entero; el redondeo convencional daría 637,0 millones.

## Cómo reconstruir
Los scripts usan una ruta absoluta de trabajo (constante `RAIZ`); ajústela antes de ejecutar.
1. `python3 -I pasos/gen_paso0.py` y los demás `pasos/gen_*.py` regeneran los pasos 0 a 7, el frente, el capítulo 19 (`gen_cap19.py`) y el cierre (`gen_cierre.py`).
2. `figs_scripts/` regenera las figuras; `figs_png/` conserva las versiones finales.
3. `python3 -I build/lista.py build/opts.json` crea la lista de archivos y `LC_ALL=C.UTF-8 python3 -I build/build.py LISTA.json SALIDA` produce DOCX y PDF (LibreOffice con UNO).
4. `pasos/x10/gen_x10.py` regenera el checklist 1000X-10 (ejecutar dos veces).
