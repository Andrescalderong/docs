# Estado del proyecto completo (corte 13-oct-2026)

Documento único del proyecto SGR_CONV56_AIRE según GENESIS-CTeI 36.10 RC2. Estado: borrador con vacíos. No es un paquete de radicación.

## Entregables (carpeta DOCUMENTO/)

- `PROYECTO_COMPLETO_SGR_CONV56_AIRE.docx` y `.pdf`: pasos 0 a 7, capítulos 1 a 21 (con bibliografía y anexos A a N), paquete 1000X (documentos 1 a 10) y cierre F-01 a F-04.
- `PITCH_DECK_SGR_CONV56_AIRE.pptx`: 15 diapositivas del documento 1000X-03.

## Qué se completó en esta corrida

Paso 7 y capítulo 12 (indicadores PERS, 15 fichas), capítulos 7 a 10, 19, 20 (anexos A a J y N) y 21; documentos 1000X-03 y 1000X-10; cierre; guía de lectura e índices. Se recibieron el metaprompt completo y el Anexo 2 de la convocatoria. El anexo N cruza el documento con el Anexo 2 y registra ocho hallazgos; los de fondo son la madurez tecnológica (TRL 7 frente a la prioridad de TRL 9) y el mínimo de 1 % de recursos para transferencia.

## Bloqueos y pendientes (ver checklist 1000X-10 y cierre)

Dos bloqueos finales activos (cartas con partida y reportes de brecha sin decisión). Pendientes del usuario: términos de referencia completos y anexos 4, 10 y 12, reportes oficiales de afectación, cartas, cotizaciones, hojas de vida, certificaciones de contrapartida y la decisión sobre el TRL objetivo.

## Cómo reconstruir

Requisitos: python3 con python-docx, pypdf, matplotlib y python-pptx; pandoc; LibreOffice con python-uno.

1. Copiar `FUENTES/` a un directorio de trabajo con subcarpetas `maestro`, `refs`, `caps`, `build`, `figs/{scripts,out}` (las figuras PNG de `figs_png/` van en `figs/out`; los scripts de `figs_scripts/` en `figs/scripts`).
2. `cd build && pandoc -o ref_default.docx --print-default-data-file reference.docx && python3 mkref_apa.py`.
3. Regenerar capítulos con `python3 pasos/gen_capNN.py` (7 a 10, 12, 20, 21), `gen_paso7.py`, `gen_anexoN.py`, `gen_x03.py`, `gen_x10.py`; después `gen_cap19.py` y `gen_cierre.py`.
4. `python3 build/make_lista.py out/lista.json && python3 build/build.py out/lista.json out/PROYECTO_COMPLETO_SGR_CONV56_AIRE`.

El verificador mecánico es `build/check_cap.py`. Los archivos de entrada del usuario y el metaprompt no se versionan; sus huellas SHA-256 están en el anexo I.
