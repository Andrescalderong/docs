# -*- coding: utf-8 -*-
"""Genera FICHA_MAESTRA.md: resumen legible de toda cifra cardinal y decisión de formulación (fuente: maestro.py, indicadores.py,
alternativas.py). Los capítulos citan SOLO estas cifras (H36-03: una cifra, una fuente)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import maestro as M, indicadores as I, alternativas as A

def build():
    r = M.resumen(); ID = M.IDENT
    L = []
    w = L.append
    w("# FICHA MAESTRA DEL PROYECTO (fuente única de cifras; no contradecir)\n")
    w("Naturaleza de cada dato: DECLARADO = valor del expediente E3 aportado por el usuario; PROPUESTO = decisión de formulación de esta corrida (requiere ratificación); CALCULADO = derivado por código de este libro; SUPUESTO = por instrucción del usuario; VACIO = dato que solo el usuario o los términos de referencia pueden aportar (usar [DATO_USUARIO: …]).\n")
    w("## 1. Identidad congelada (H36-02)\n")
    for k in ("titulo", "convocatoria", "financiador", "tipologia", "ocde", "territorio", "fecha_corte", "fecha_limite"):
        w(f"- {k}: {ID[k]}")
    w(f"- Tope normativo declarado: {M.cop(ID['tope_cop'])} (según la guía financiera de la Convocatoria 56; términos de referencia completos NO aportados, NO_VERIFICADO)")
    w(f"- Cierre de radicación: {ID['fecha_limite']}, {ID['hora_limite']} (confirmado por el usuario el 16-oct-2026; la guía financiera coincide)")
    w(f"- Duración de ejecución: {ID['duracion_meses']} meses ({M.DURACION_SEMANAS} semanas); horizonte posproyecto de seguimiento: {ID['horizonte_posproyecto_meses']} meses (PROPUESTO)")
    w(f"- TRL inicial {ID['trl_inicial']}; TRL final {ID['trl_final']} (PROPUESTO; el expediente E3 declaraba TRL 8 y 'TRL 4 a 7 u 8': se fija 7 porque el sistema se demuestra en entorno operativo sin calificación formal; TRL 8 queda condicionado a evaluación de desempeño independiente)")
    w(f"- Caso: {ID['caso']}. Metaprompt: {ID['metaprompt']}; {ID['ntc']}. Huella SHA-256 del maestro: {ID['hash_maestro']}")
    w("- Territorio y alianza: SUPUESTO por instrucción del usuario. Entidad ejecutora (IES con acreditación de alta calidad), empresa tecnológica, alcaldías, UNGRD: nombres [DATO_USUARIO].\n")
    w("## 2. Solución (PROPUESTO)\n")
    w("Red de 100 nodos hoja de medición de PM2,5 y PM10 (sensor óptico de bajo costo con temperatura y humedad), 10 gateways (1 por cada 10 nodos) y 3 monitores de referencia gravimétricos (uno por departamento) para colocalización. Los nodos transmiten por LoRa al gateway; el gateway aplica el modelo de corrección (humedad, temperatura y fracción gruesa) y reenvía por red celular, con enlace satelital alterno y almacenamiento local de 7 días. Los nodos operan con panel solar y batería con autonomía mínima de 14 días sin sol. La nube aloja el entrenamiento del modelo, el gemelo digital (estimación espacial) y el tablero del índice de calidad del aire y salud (AQHI) con umbrales validados localmente. La corrección se define en UN solo lugar: el gateway (se retiran las versiones 'en el chip del sensor' y 'en el microcontrolador de cada nodo' del expediente E3).")
    w(f"Umbrales de desempeño (PROPUESTO; ancla EPA 2021 para uso informativo en sitio fijo): R² ≥ 0,70; NRMSE ≤ 30 %; pendiente entre 0,65 y 1,35; sesgo entre −5,0 y 5,0 µg/m³. Meta aspiracional NMAE ≤ 15 %, que no condiciona las compuertas. Línea base de error: se mide en el tramo 1 (el 'NMAE > 45 %' del expediente E3 es DECLARADO sin localizador y NO_VERIFICADO).\n")
    w("## 3. Objetivos\n")
    w(f"- Objetivo general: {M.OG}")
    for o in M.OE: w(f"- {o['id']} ({o['sc']}; causa priorizada en Vester: {o['causa']}): {o['texto']} Meta: {o['meta']}.")
    w("\n## 4. Tramos de despliegue condicionado (estrategia R4 de 4.4-MDR)\n")
    w("| Tramo | Meses | Nodos | Gateways | Compra de nodos | Compra de gateways | Compuerta |\n| --- | --- | --- | --- | --- | --- | --- |")
    for t in M.TRAMOS: w(f"| {t['nombre']} | {t['m_ini']}–{t['m_fin']} | {t['nodos']} | {t['gateways']} | {t['compra_nodos']} | {t['compra_gw']} | {t['compuerta']} (mes {t['mes_compuerta']}) |")
    w("Totales: 100 nodos operativos y 120 comprados (20 de reserva); 10 gateways operativos y 11 comprados. Distribución por departamento (PROPUESTO): Caldas 33, Cundinamarca 34, Valle del Cauca 33 nodos; 1 monitor de referencia por departamento. Municipios focalizados: 12 (4 por departamento) [DATO_USUARIO: lista]. Comités de gestión del riesgo focalizados: 15 (12 municipales y 3 departamentales) (SUPUESTO). Funcionarios beneficiarios directos: 150 (SUPUESTO, 10 por comité). Operarios de remoción en sitios monitoreados: [DATO_USUARIO].")
    w("Compuertas: C1 (mes 12) decide ampliar al tramo 2 si el modelo cumple los umbrales en el piloto (R² ≥ 0,70 y NRMSE ≤ 30 %) y si al menos 50 % de los comités del tramo 1 usa el tablero; C2 (mes 17) decide consolidar el tramo 3 con los mismos umbrales en los tres departamentos, disponibilidad mensual ≥ 90 % y convenios de custodia con partida; C3 (mes 24) cierra y transfiere. Cada compuerta libera la compra del tramo siguiente.\n")
    w("## 5. Presupuesto (CALCULADO desde maestro.py)\n")
    w(f"- Valor solicitado al SGR: {M.cop(r['sgr'])} ({r['pct_tope']*100:.1f} % del tope; holgura no solicitada: {M.cop(r['holgura'])}).")
    w(f"- Contrapartida: {M.cop(r['contra'])} (IES 1.100 M en especie; empresa 210 M en efectivo y 800 M en especie; alcaldías: sin aporte, VACIO). Todas las cifras de contrapartida son DECLARADO (E3) salvo el desglose de la IES, PROPUESTO; certificaciones pendientes.")
    w(f"- Total del proyecto: {M.cop(r['total'])}.")
    w("| Rubro SGR | Millones de COP | % del SGR |\n| --- | --- | --- |")
    for k, v in r["por_rubro"].items(): w(f"| {k} | {M.mm(v)} | {v / r['sgr'] * 100:.1f} |".replace(".", ",", 1) if False else f"| {k} | {M.mm(v)} | {str(round(v / r['sgr'] * 100, 1)).replace('.', ',')} |")
    w(f"- Flujo semestral SGR (millones): {', '.join(M.mm(x) for x in r['flujo_sgr_sem'])}. Flujo semestral de contrapartida: {', '.join(M.mm(x) for x in r['flujo_con_sem'])}.")
    w(f"- Reserva de contingencia: {M.cop(M.RESERVA)} = suma de valores monetarios esperados (EMV) de 12 riesgos (CALCULADO); según el Anexo 3 oficial, los imprevistos son admisibles si se asocian al análisis de riesgos y se soportan en el análisis de costos; se ubican en el rubro 11 (Otros) y su asociación por rubro figura en la sección 5 de esta ficha. Administración: 360 M (" + str(round(360e6 / r['sgr'] * 100, 1)).replace('.', ',') + " % del SGR solicitado; el tope porcentual del expediente E3, 5 %, no se verificó).")
    w("\n### Equivalencia con los 11 rubros del Anexo 3 oficial (CALCULADO)\n")
    w("| N.º | Rubro del Anexo 3 | Líneas | Millones de COP | % del SGR |\n| --- | --- | --- | --- | --- |")
    for i, nom in enumerate(M.RUBROS11, 1):
        ls = [x for x in M.BUDGET if x["rubro11"] == nom and x["fuente"] == "SGR"]
        v = sum(x["total"] for x in ls)
        w(f"| {i} | {nom} | {', '.join(x['id'] for x in ls) or '—'} | {M.mm(v)} | {str(round(v / r['sgr'] * 100, 1)).replace('.', ',')} |")
    w("- Imprevistos por rubro (EMV de los 12 riesgos, CALCULADO): Equipos y software 363,0 M (R-TEC-01, R-TEC-02, R-EXT-02, R-FIN-01); Servicios tecnológicos y pruebas 77,5 M (R-TEC-03, R-TEC-04, R-DAT-01); Capacitación y eventos 96,0 M (R-ORG-01, R-ORG-02); Protección del conocimiento 20,0 M (R-JUR-01); Otros 80,0 M (R-EXT-01, R-FIN-02). Suma 636,5 M; la reserva se redondea a 636,0 M.")
    w("- Movilidad financiada por el SGR (líneas V01 a V04): " + M.mm(sum(x["total"] for x in M.BUDGET if x["id"] in ("V01", "V02", "V03", "V04"))) + " M, equivalente a " + str(round(sum(x["total"] for x in M.BUDGET if x["id"] in ("V01", "V02", "V03", "V04")) / r["sgr"] * 100, 2)).replace(".", ",") + " % del SGR (tope de la guía financiera: 2 %; NO_VERIFICADO frente a los TdR).")
    w("- Decisión DEC-F06: se solicita la suma justificada, no el tope. La holgura se describe como opciones de ampliación condicionadas a TdR (más nodos, un cuarto tramo, un año adicional de custodia) y no se presupuesta.\n")
    w("### Líneas de presupuesto SGR\n")
    w("| Id | Rubro | Concepto | Unidad | Cantidad | Costo unitario (COP) | Total (COP) | Naturaleza | WP | Meses |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for l in M.BUDGET: w(f"| {l['id']} | {l['rubro']} | {l['concepto']} | {l['unidad']} | {l['cant']:,} | {M.cop(l['vunit'])} | {M.cop(l['total'])} | {l['nat']} | {l['wp'] if 'wp' in l else l['wbs']} | {l['m_ini']}–{l['m_fin']} |".replace(",", "."))
    w("\n### Contrapartida\n")
    w("| Id | Aporte | Fuente | Total (COP) | Naturaleza |\n| --- | --- | --- | --- | --- |")
    for l in M.CONTRA: w(f"| {l['id']} | {l['concepto']} | {l['fuente']} | {M.cop(l['total'])} | {l['nat']} |")
    w("\n## 6. Cronograma (CALCULADO por CPM; semanas)\n")
    w(f"Duración = {M.DURACION_SEMANAS} semanas = ruta crítica. Actividades críticas: {', '.join(M.RUTA_CRITICA)}.")
    w("| Id | Actividad | Duración (sem.) | Predecesoras | Inicio temprano | Fin temprano | Holgura | WP |\n| --- | --- | --- | --- | --- | --- | --- | --- |")
    for k, a in M.ACTS.items(): w(f"| {k} | {a['nombre']} | {a['dur']} | {', '.join(a['pred']) or '—'} | {a['ES']} | {a['EF']} | {a['holgura']} | {a['wp']} |")
    w("\nHitos (mes de calendario):\n")
    w("| Hito | Descripción | Mes | Verificación |\n| --- | --- | --- | --- |")
    for h in M.HITOS: w(f"| {h[0]} | {h[1]} | {h[2]} | {h[3]} |")
    w("\nPaquetes de trabajo: WP0 gestión, compuertas y cierre; WP1 medición verificada (OE1); WP2 red, energía y plataforma (OE2); WP3 uso institucional, apropiación y custodia (OE3).\n")
    w("## 7. Riesgos (CALCULADO)\n")
    w("| Id | Categoría | Riesgo | P | I | P×I | Nivel | Prob. % | Impacto (M COP) | EMV (M COP) | Estrategia |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for k in M.RISKS: w(f"| {k['id']} | {k['cat']} | {k['desc']} | {k['P']} | {k['I']} | {k['score']} | {k['nivel']} | {k['prob']} | {M.mm(k['impacto'])} | {M.mm(k['emv'])} | {k['estrategia']} |")
    w(f"\nSuma de EMV sin redondeo: {M.mm(sum(k['emv'] for k in M.RISKS))} M COP; reserva redondeada: {M.mm(M.RESERVA)} M COP.\n")
    w("## 8. Indicadores PERS (15)\n")
    w("| Código | Nivel | Taxonomía | Nombre | OE | Línea base | Meta final | MMG |\n| --- | --- | --- | --- | --- | --- | --- | --- |")
    for i in I.IND: w(f"| {i['cod']} | {i['nivel']} | {i['tax']} | {i['nombre']} | {i['oe']} | {i['lb']} ({i['lb_nat']}) | {i['mf']} | {i['mmg']} |")
    w("\n## 9. Alternativas y evaluación multicriterio (CALCULADO; puntajes PROPUESTO)\n")
    for a, n in A.ALTS: w(f"- {a}: {n}")
    w(f"Puntajes totales ponderados (escala 1 a 9): " + "; ".join(f"{A.ALTS[i][0]} = {str(round(A.BASE[i], 3)).replace('.', ',')}" for i in range(4)) + f". Alternativa ganadora: {A.ALTS[A.ganadora(A.BASE)][0]}. Sensibilidad ±10 % relativo: la ganadora no cambia en los 5 escenarios. GWO no se activa: 4 alternativas son enumerables (AS-32). Puntajes sujetos a ratificación del panel evaluador.\n")
    w("## 10. Resultados del análisis causal (secciones 4.3 a 4.5 y 4.4-MDR)\n")
    w("- Escenario de trabajo S2: 48 aristas, ΣI = ΣD = 78; ciclos: V15 en 140 de 144 ciclos simples; sin estabilidad de potencias hasta k = 10.")
    w("- Problema central: error de medición IoT sin verificar (V06), crítica en los cinco escenarios (I = 8; D = 13). Causas directas: V03 humedad (I 6, D 0), V02 PM10 (I 7, D 6), V01 PM2,5 (I 6, D 5), V07 frecuencia de calibración (I 5, D 2); indirecta: V05 escombros (I 7, D 1). Efectos: V11 AQHI (D 11), V12 falsas alarmas, V14 personas alertadas (D 9), V15 adopción institucional (crítica, I 7, D 7).")
    w("- Clasificación S2 por mediana: críticas V02, V06, V15; activas V03, V04, V05; frontera V01, V07, V10, V11, V12; reactivas V09, V14; autónomas relativas V08, V13.")
    w("- Decisión de 4.4-MDR: R4 = desplegar por tramos con piloto de contraste y custodia distribuida; R3 (transferencia a las alcaldías al mes 25 como receptor único) no se recomienda como diseño base; R0 (sin intervención) tampoco. Supuestos críticos SC-1 (medición verificada), SC-2 (energía y enlace), SC-3 (uso institucional), SC-4 (custodia). Probabilidades de los árboles de decisión: no declaradas (sin fuente).")
    w("- Sostenibilidad: costo total de sostenimiento, ICAR y fondo patrimonial NO_CALCULABLE; portafolio del expediente E3: máxima participación 63,2 %, HHI 0,472 en el año 1; cláusula de apertura y salida ordenada; transferencia por tramos condicionados.")
    w("- Premortem y escenarios: ver 4.4-MDR.12 (tres futuros con tres objetivos y tres opciones cada uno).\n")
    w("## 10b. Cadena de 5 porqués, causas priorizadas y causa raíz (Paso 4.6 a 4.8; INFERIDO, estatuto HIE, sin efecto estimado)\n")
    w("- P1. ¿Por qué existe el problema central? Porque las lecturas ópticas de PM2,5 y PM10 no se verifican frente a una referencia en los sitios de remoción (V06).")
    w("- P2. ¿Por qué el error de lectura es alto? Porque la humedad relativa (V03) y la fracción gruesa (V02) alteran la respuesta óptica sin corrección local (S2: V03→V06 = 3 y V02→V06 = 3). Respaldo del corpus: correlación de 0,73 de las partículas con la humedad en una mina a cielo abierto (Suresh et al., 2025, p. 30); corrección con estación cercana y 35 minutos de desfase que llevó el R² de menos de 0,2 a 0,81 en Seúl (Bang et al., 2026, pp. 6-8).")
    w("- P3. ¿Por qué no hay corrección local? Porque la calibración es estática o inexistente (V07→V06 = 3) y no hay referencias colocalizadas: 90,8 % de las 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13; el 90,8 % es cálculo del analista).")
    w("- P4. ¿Por qué no se calibra en el sitio? Porque la calibración depende de referencias costosas, de energía y de enlace estables, y la remoción de escombros (V05) degrada la disponibilidad de nodos (S2: V05→V09 = 2) y expone los cabezales al polvo.")
    w("- P5. Causa raíz (hipótesis de diseño, INFERIDO): la red de bajo costo opera sin un protocolo de calibración colocalizada y de corrección en el borde con custodia institucional, adaptado a sitios de remoción de escombros. El expediente E3 declaraba como causa raíz la 'arquitectura dependiente de la nube'; ninguna de las 15 variables la representa, por lo que se trata como hipótesis rival.")
    w("- Causas priorizadas (S2, corte por mediana: I = 5 y D = 5): V06 (crítica; I 8, D 13) es el problema central; V02 (crítica; I 7, D 6); V15 (crítica; I 7, D 7); V03 (activa; I 6, D 0); V05 (activa; I 7, D 1); V07 (frontera; I 5, D 2). Intervención: calibración colocalizada y corrección en gateway (V06, V02, V03, V07), disponibilidad con energía y enlace redundantes (V05→V09) y co-diseño del uso institucional (V15). Todas las relaciones son hipótesis de influencia estructural.\n")
    w("## 10c. Formalización tripartita del problema (Paso 5; texto base reutilizable)\n")
    w("- Metaproblema: los sistemas de vigilancia ambiental de bajo costo desplegados en contextos de desastre carecen de calibración colocalizada y de corrección local, por lo que entregan mediciones de material particulado de calidad desconocida. Esa condición lleva a decidir alertas con datos sin error conocido, afecta a operarios de remoción y a población expuesta, y mantiene un ciclo en el que la baja confianza reduce el uso institucional de las mediciones. Evidencia de nivel sistémico: 90,8 % de las estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13).")
    w("- Problema sustantivo: en los sitios de remoción de escombros de Caldas, Cundinamarca y Valle del Cauca (SUPUESTO), los comités de gestión del riesgo no disponen de mediciones de PM2,5 y PM10 con error conocido frente a una referencia. El expediente E3 declara un error normalizado superior a 45 % en sensores ópticos sin calibración dinámica en alta humedad (DECLARADO, sin localizador; NO_VERIFICADO); la línea base propia se mide en el tramo 1. Contexto nacional (F-INF): 209 estaciones reportadas, 154 integradas a un sistema de vigilancia; solo 28 de 1.122 municipios con estaciones utilizables para estimar la carga (Rodríguez-Villamizar et al., 2022, pp. 3 y 6). El PDD, el Anexo 4 y los CONPES citados por E3 no se aportaron (NO_VERIFICADO).")
    w("- Problema formal: Y = NRMSE de los nodos frente a la referencia colocalizada (V06), en porcentaje. Variables independientes: X1 = humedad relativa (V03; moderadora de la respuesta óptica); X2 = fracción gruesa (V02 menos V01); X3 = frecuencia y calidad de calibración (V07). Moderadora M = disponibilidad de nodos (V09). Controles C = temperatura, edad del cabezal y distancia a la referencia (variables omitidas del modelo de 15, a evaluar en una matriz de 19). Valor actual de Y: [VACIO: se mide en el tramo 1]. Meta: NRMSE ≤ 30 % y R² ≥ 0,70 (EPA, 2021) al mes 24; NMAE ≤ 15 % aspiracional. Horizonte: 24 meses.")
    w("- Incógnitas principales: línea base de error por departamento; completitud real de datos en sitios de remoción; capacidad de absorción de los custodios (ICAR, NO_CALCULABLE); fórmula local del índice y umbrales; disponibilidad real del enlace celular y satelital en los sitios.\n")
    w("## 11. Decisiones de formulación (registro DEC-F)\n")
    for d in DECISIONES: w(f"- {d}")
    w("\n## 12. Reglas de coherencia obligatorias\n")
    w("1. Una cifra, una fuente: cualquier cifra cardinal sale de este archivo. 2. Una definición del lugar de corrección (gateway). 3. Una meta de error (R² y NRMSE; NMAE ≤ 15 % aspiracional) y una línea base medida en el tramo 1. 4. TRL 4 → 7. 5. 24 meses y 104 semanas. 6. 100 nodos y 10 gateways operativos; 120 y 11 comprados. 7. SGR solicitado y contrapartida según §5. 8. Ninguna afirmación causal sobre salud: los resultados son técnicos, de adopción y de continuidad (H36-11). 9. Ninguna probabilidad sin fuente. 10. Lenguaje: sin metáforas ni adjetivos enfáticos; sin 'garantiza', 'demuestra matemáticamente' ni 'inédito'.\n")
    return "\n".join(L)

DECISIONES = [
 "DEC-F01 Fuente de financiación y estructura: el expediente mezcla 'Convocatoria 56 MinCiencias' y 'SGR/OCAD/MGA'. Se adopta la denominación 'Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)' del Paso 1 del usuario. Los términos de referencia no se aportaron: la estructura de 21 capítulos es la del metaprompt (SUPUESTO) y los datos que solo el usuario posee se marcan [DATO_USUARIO].",
 "DEC-F02 Arquitectura: la corrección ocurre en el gateway; los nodos hoja usan LoRa y bajo consumo; los gateways usan red celular con enlace satelital alterno y almacenamiento local de 7 días (corrige HR-12 y HR-13).",
 "DEC-F03 Estrategia de despliegue: R4 de 4.4-MDR (tramos con piloto de contraste y custodia distribuida), con compuertas C1 y C2 que liberan las compras del tramo siguiente.",
 "DEC-F04 Meta de desempeño: R² ≥ 0,70 y NRMSE ≤ 30 % frente a referencia (ancla EPA, 2021); NMAE ≤ 15 % aspiracional; línea base medida en el tramo 1 (corrige HR-14: tres metas contradictorias).",
 "DEC-F05 TRL final 7 (no 8): demostración en entorno operativo; TRL 8 exige calificación independiente que el plazo no cubre.",
 "DEC-F06 Presupuesto: se solicita la suma justificada por actividad (" + str(round(M.resumen()["pct_tope"] * 100, 1)).replace(".", ",") + " % del tope), no el tope; la holgura se describe como opciones sin presupuestar (corrige HR-10).",
 "DEC-F07 Contrapartida: 2.110 M (IES 1.100 en especie; empresa 210 en efectivo y 800 en especie), valores del expediente E3 con desglose de la IES reconstruido; certificaciones pendientes; las alcaldías no aportan (VACIO).",
 "DEC-F08 Cronograma: red de 17 actividades con ruta crítica igual a la duración (104 semanas); importación de 12 semanas máximo por lote; compras por tramo y no 100 % en la semana 2 (corrige HR-11).",
 "DEC-F09 Alternativa seleccionada: ALT-03 híbrida por tramos, condicionada a la ratificación del panel; el puntaje no se interpreta como probabilidad de éxito.",
 "DEC-F10 Indicadores: los de impacto (S) se miden 6 a 12 meses tras el cierre y por una evaluación externa; las líneas base VACIO se miden en el tramo 1.",
 "DEC-F11 Escenarios estratégicos: el metaprompt sugiere probabilidades 25/50/20/5; se omiten porque ninguna tiene fuente (NTC 1.1). Los escenarios se presentan sin probabilidad y con condiciones de activación.",
 "DEC-F12 Articulación territorial (Paso 5.0): los ocho elementos del checklist quedan NO_VERIFICADO por falta de PDD, CONPES y anexos. La regla bloqueante del metaprompt exige regresar a Gate 0; se continúa por orden expresa del usuario (13-oct-2026) con la reserva R-ART registrada en el cierre.",
 "DEC-F13 Estética: se aplica la paleta y la jerarquía tipográfica del usuario; excepción a FIG-02: opacidad 0,25 solo en la cuadrícula; el relleno de encabezados de tabla usa #B9D9EB con texto #2A3439 (contraste superior a 4,5:1; el texto sobre #6699CC no lo alcanza) y #6699CC como filete inferior del encabezado; filas alternas #F7F7F7.",
 "DEC-F14 Numeración: tablas y figuras 'c.n' por capítulo; Parte I con prefijo F (F5.1), paquete 1000X con prefijo X (X6.1) y anexos con letra (A1).",
 "DEC-F15 GWO no se activa porque el espacio de decisión (4 alternativas) es enumerable (AS-32).",
 "DEC-F19 Alianza y presupuesto por actor (Parte inicial S): proponente universidad con grupo de investigación; municipio beneficiario sin aporte (regla del Anexo 2: una entidad no es cooperante y beneficiaria a la vez); actor reconocido por MinCiencias; empresa aliada. Las líneas SGR se asignan a actores de forma PROPUESTA; requiere ratificación de la Universidad y verificación de la categoría de la empresa en los TdR.",
 "DEC-F20 Cierre de radicación: 3 de noviembre de 2026, 4:00 p. m. (decisión del usuario del 16-oct-2026). Sustituye al 11 de noviembre de la ficha anterior.",
 "DEC-F21 Ajuste del presupuesto a la guía financiera de la Convocatoria 56 (decisión del usuario del 16-oct-2026): se retiran los seguros (S04 y O04, 110 M); P03 pasa a doctor en estancia posdoctoral (24 meses × 12,92 M, numeral 14.4); la movilidad (V01 a V04) se reduce a 174,5 M, 2 % del SGR; las líneas se presentan en los 11 rubros del Anexo 3; la reserva se conserva en el rubro 11 asociada al análisis de riesgos. El exceso de viajes lo cubre la logística de emergencia de la empresa (C05). Si los TdR aclaran que el tope de 2 % no aplica a viajes de campo, se restituyen 257,5 M.",
 "DEC-F22 Formato de radicación: el documento técnico se entrega en las 30 secciones del Anexo 2 (PDF de 3 MB como máximo); el expediente completo se entrega aparte, comprimido (10 MB como máximo).",
 "DEC-F23 Formato del documento: el expediente completo se presenta en el formato oficial del Anexo 2 (plantilla, Arial, tablas con encabezado verde); las figuras conservan la plantilla visual.",
]

if __name__ == "__main__":
    t = build()
    open(os.path.join(HERE, "FICHA_MAESTRA.md"), "w", encoding="utf-8").write(t)
    print(len(t.split()), "palabras")
