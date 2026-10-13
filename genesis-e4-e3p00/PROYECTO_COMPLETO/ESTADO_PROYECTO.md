# Estado del proyecto completo (corte 13-oct-2026, 19:50 UTC)

Documento en construcción: proyecto completo SGR_CONV56_AIRE según GENESIS-CTeI 36.10 RC2 en un solo documento (Word y PDF).
Este directorio guarda las fuentes de trabajo (Markdown con directivas, scripts de figuras y de ensamblado). El metaprompt y los tres archivos de entrada del usuario no se versionan.

## Archivos terminados (verificador `build/check_cap.py`: sin problemas salvo nota)
Pasos 0, 1, 2, 3 (paso3.md), 4 (paso4.md), 5, 6; capítulos 1, 2 (02a y 02b), 3, 4, 5, 6, 11, 13, 14, 15, 17, 18; capítulo de estrategia (estrategia.md); documentos 1000X x01, x02, x05, x06, x07, x08, x09; anexos K a M (anexos_km.md).
Con observaciones menores de estilo: cap16 (2 oraciones largas), cap18 (1 oración larga).

## Pendiente
Paso 7 (indicadores PERS), capítulos 7, 8, 9, 10, 12, 19 (bibliografía desde el banco), 20 (anexos A a J), 21 (Project Charter), documentos 1000X x03 y x10, cierre F-01 a F-04, portada e índices.
Las figuras de los capítulos 7 a 10, 12 y 21 ya existen (figs_png/c7_* a c21_*); falta el texto.
Los agentes redactores se interrumpieron por el límite semanal de uso (reinicio: 14-oct-2026, 21:00 UTC).

## Cómo reconstruir
`python3 build/build.py LISTA.json SALIDA` (ver build/build.py y build/post_apa.py). Las figuras se regeneran con los scripts de figs_scripts/.
