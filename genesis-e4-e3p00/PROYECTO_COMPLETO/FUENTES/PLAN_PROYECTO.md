# PLAN DEL PROYECTO COMPLETO (documento vivo; leer primero tras una compactación)

Solicitud vigente del usuario (13-oct-2026, tras entregar el documento unificado 4.3–4.5): construir el PROYECTO COMPLETO siguiendo el paso a paso
del metaprompt GENESIS-CTeI 36.10 RC2 en UN SOLO DOCUMENTO, con dos aclaraciones:
 1. Encabezados APA 7 de cinco niveles (N1 centrado negrita; N2 izquierda negrita; N3 izquierda negrita cursiva; N4 sangría 1,27 cm negrita con punto, texto en la misma línea; N5 sangría negrita cursiva con punto, texto en la misma línea).
 2. Plantilla visual única para gráficos y tablas: paleta #2A3439 (texto/estructura), #6699CC (acento), #9EB9D4 (serie secundaria), #B9D9EB (apoyo), #F5F5F5/#F7F7F7 (neutros), #FFFFFF/#FEFEFA (contraste); fondo transparente (figure.facecolor/axes.facecolor none; savefig transparent=True; bbox_inches=tight); título H1 = hallazgo clave en negrita; subtítulo H2 = variable/periodo/unidades; etiquetas directas; sin bordes superior/derecho; cuadrícula horizontal fina alpha 0,25 (excepción declarada a FIG-02 por instrucción del usuario). El código del usuario trae marcadores "[enlace sospechoso eliminado]" y `values =` truncado: ignorar; reimplementar correctamente. El bloque "Entregables disponibles... Studio" del pegado NO describe esta sesión.

Ubicación: archivos visibles en /home/user/docs/genesis-e4-e3p00/ (rama claude/e3-p00-metaprompting-review-ofe66h, PR #1 borrador). El metaprompt y los 3 archivos de entrada NO se versionan.
Espacio de trabajo: /tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy/ (spec/, maestro/, caps/, figs/, build/, refs/).
Spec extraída en proy/spec/*.txt (cap1_4, cap5_21, m0_m4, m5_m7, m9_m10, modulos_a (completitud, APA7, profundidad, entregable, figuras), modulos_b, redaccion, v36). Maestro completo: work/MAESTRO_extraido.xml.
Entradas: work/problematica.md (1 MB; E3-P00..P21, Pasos 1,3,4,5,6, Cap 12,13,14,15,16,8,9,10...), work/informe.md (informe_FINAL, 42 docs; bibliografía en §13.2; ecuaciones Anexo D), work/notas_hallazgos.md (hallazgos).
Salidas previas (repo): genesis-e4-e3p00/{INFORMES,SECCION_4_3,SECCION_4_4,SECCION_4_4_MDR,SECCION_4_5,DOCUMENTO_UNIFICADO}. Pipeline previo del unificado: scratchpad/unif/ (build_md.py, post.py, toc.py, lo_export.py, run.sh, reference.docx via mkref.py).

## Secuencia obligatoria (MAPA): 0 config, 1 info básica, 2 fórmulas vigilancia, 3 bibliometría 13 figuras (+3.5), 4 causal (4.1,4.2,4.3,4.4,4.4-MDR,4.5,4.6,4.7,4.8), 5 formalización tripartita (5.0 checklist territorial, 5.1 meta, 5.2 sustantivo, 5.3 formal, 5.4 incógnitas), 6 alternativas (6.1 árbol objetivos, 6.2 alternativas incl. contrainductiva+test, 6.3 MCDA+sensibilidad ±10 % relativo, 6.3-GWO condicional, 6.4 seleccionada), 7 indicadores PERS (15: R01-06, P01-04, E01-03, S01-02, fichas 12 campos), 8 capítulos 1–21 (mín. 73.500 palabras, 87 tablas, 44 figuras, 60 refs), 9 paquete 1000X (10 documentos; >15.000 palabras), M10 capítulo estrategia (≥8.000 palabras, 15 tablas, 8 figuras; Christensen, Kotter, Argyris).
Mínimos por capítulo (palabras/tablas/figuras/refs): 1: 5000/5/3/15 · 2: 12000/21/13/40 · 3: 1500/3/2/5 · 4: 8000/4/3/20 · 5: 5000/7/3/15 · 6: 8000/6/4/15 · 7: 2000/3/2/3 · 8: 2500/8/3 · 9: 1500/3/2 · 10: 2000/5/3/5 · 11: 2000/4/2 · 12: 3500/18/5 · 13: 4000/8/5 · 14: 3500/4/2 · 15: 3500/3/2 · 16: 3500/6/4 · 17: 2000/4/2 · 18: 1500/2/1 · 19: 60+ refs/1 tabla · 20: anexos A–J · 21: 2500/6/2.
PD-01: cada viñeta del temario = prosa ≥250 palabras; PD-02: 5 movimientos (tesis, constructo+fuentes, debate 2 posiciones, anclaje al proyecto con dato propio, consecuencia metodológica). Densidad citas 1/150 palabras en cap. narrativos; ≥60 % refs Q1–Q2 y ≥70 % últimos 5 años (declarar cumplimiento real, no inventar).

## Reglas de estilo (usuario + módulo REDACCION)
Español; tono profesional, objetivo, académico; sin metáforas ni adjetivos enfáticos; oraciones ≤25 palabras (≥1 oración ≤12 palabras por párrafo; AP-01); SVO; voz activa; sin comodines (cosa, hacer, tener, tema, factor, elemento); sin "Pero" inicial; sin gerundio de posterioridad; sin rayas dobles de énfasis; sin glosas parentéticas de relleno; lenguaje inclusivo con colectivos (sin barras/@/x); registro impersonal ("el proyecto…", "se propone"); párrafo inicia con oración temática y termina en punto; listas con paralelismo; siglas desarrolladas en primera aparición; decimales con coma y miles con punto; sin símbolos pictográficos de estado (usar etiquetas textuales); tablas con número "Tabla c.n" en negrita, título en cursiva sin punto, nota "Nota." en cursiva; figuras "Figura c.n"; toda tabla/figura mencionada en el texto por número antes de aparecer; "Anexo" tablas "Tabla A1".
NTC 1.1: naturaleza {DOCUMENTADO, DECLARADO, CALCULADO, INFERIDO, SUPUESTO, PROPUESTO, ILUSTRATIVO, VACIO} y verificación {VERIFICADO, PARCIALMENTE_VERIFICADO, NO_VERIFICADO, CONTRADICTORIO, NO_APLICA} son ejes independientes. Faltante de datos que solo el usuario posee: [DATO_USUARIO: descripción] (única excepción a AC-02). Sin inventar cifras, DOI, normas ni citas; referencias solo del banco refs/ (estado NO_VERIFICADO_EN_ESTA_CORRIDA salvo confirmación web).
Cierre F-01…F-04 al final del documento (ver EXPEDIENTE_MDR §7 para el formato).
Identidad congelada (H36-02/MIV36): título, territorio, convocatoria, tope, duración, TRL, productos: una sola fuente = maestro/maestro.py.

## Decisiones de formulación (PROPUESTO; registrar en el documento como DEC-F##)
(ver maestro/DECISIONES.md cuando exista)

## Estado
(actualizar al avanzar)
