# -*- coding: utf-8 -*-
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

d = Doc("10")
RK = D.RISKS
M = D.M
# ---- distribución exacta de la pérdida total bajo independencia (2^12 combinaciones)
p = [r["prob"] / 100 for r in RK]; v = [r["impacto"] / M for r in RK]
dist = collections.defaultdict(float)
for mask in range(1 << len(RK)):
    pr = 1.0; loss = 0.0
    for i in range(len(RK)):
        if mask >> i & 1: pr *= p[i]; loss += v[i]
        else: pr *= 1 - p[i]
    dist[round(loss, 3)] += pr
ks = sorted(dist)
media = sum(k * dist[k] for k in ks)
sd = (sum((k - media) ** 2 * dist[k] for k in ks)) ** 0.5
def cuantil(q):
    c = 0
    for k in ks:
        c += dist[k]
        if c >= q: return k
p_gt = sum(dist[k] for k in ks if k > D.RESERVA / M)
p_cero = dist[0.0]
suma_imp = sum(v)
RES = D.RESERVA / M

d.h(1, "Capítulo 10. Gestión de Riesgos")
d.p("Este capítulo identifica, mide y trata los riesgos que pueden impedir los resultados del proyecto. El registro contiene 12 riesgos en seis categorías. Cada riesgo recibe una probabilidad, un impacto, un valor monetario esperado (EMV), una respuesta y un disparador observable. La suma de los valores esperados fija la reserva de contingencia de 636.000.000 COP del capítulo 8. La probabilidad y el impacto son estimaciones propuestas por esta formulación (PROPUESTO, NO_VERIFICADO). El producto, el nivel y el valor esperado son cálculos sobre esas estimaciones. El capítulo sigue el proceso de la norma ISO 31000: identificar, analizar, evaluar y tratar (Organización Internacional de Normalización [ISO], 2018).")

# ------------------------------------------------------------------ 10.1
d.h(2, "10.1 Identificación de Riesgos")
d.p("La identificación combina tres fuentes. La primera es el análisis estructural de las 15 variables del problema, que señala qué variables se vinculan con cada riesgo. La segunda es el ejercicio previo al hecho de la sección 4.4-MDR.12. Ese ejercicio supone el fracaso de la decisión de despliegue por tramos y busca sus causas (Klein, 2007). La tercera es la literatura sobre sensores de bajo costo, que documenta fallas por humedad, deriva y dependencia del sitio (Jayaratne et al., 2018; Giordano et al., 2021). Los riesgos resultantes se agrupan en categorías técnica, organizacional, externa, financiera, jurídica y de datos. La {T:t01} presenta el registro.")
fil = []
for r in RK:
    fil.append((r["id"], r["cat"], r["desc"], r["causa"], r["disp"]))
d.tabla("t01", "Registro de riesgos identificados con variable causal y disparador",
        ["Id", "Categoría", "Riesgo", "Variable causal", "Disparador observable"], fil,
        "*Nota.* Elaboración propia con datos de maestro.py (RIESGOS) y de la ficha maestra §7. Las variables V02, V03, V05, V06, V07, V08, V09 y V15 provienen del análisis estructural de la sección 4.4. El guion indica ausencia de variable asociada. La identificación es PROPUESTO. Decimales con coma.")
d.p("Cuatro supuestos críticos organizan el registro. El supuesto SC-1 sostiene que la corrección local reduce el error de medición. El supuesto SC-2 sostiene que los nodos conservan energía y enlace. El supuesto SC-3 sostiene que los comités usan el tablero. El supuesto SC-4 sostiene que los custodios asumen la operación. Cada riesgo técnico amenaza SC-1 o SC-2. Los riesgos organizacionales amenazan SC-3 o SC-4. Esa correspondencia evita una lista dispersa y permite que cada compuerta evalúe un conjunto acotado de amenazas.")
d.p("Dos posiciones compiten sobre cómo identificar riesgos. La primera exige un inventario exhaustivo, que reduce la probabilidad de omitir una amenaza (ISO, 2018). La segunda advierte que los inventarios largos diluyen la atención y recomienda concentrarse en los supuestos que sostienen la decisión (Klein, 2007). El proyecto adopta una síntesis. Registra 12 riesgos con disparador observable, y mantiene la revisión por supuesto crítico en cada compuerta. Merton (1936) recuerda que las acciones con propósito producen consecuencias no anticipadas. Por ello el registro se revisa cada trimestre y admite riesgos nuevos.")
d.p("El registro presenta tres limitaciones. Primero, ningún riesgo se calibró con datos del territorio, porque el proyecto aún no mide. Segundo, el registro omite riesgos de seguridad personal del equipo de campo en zonas de remoción. Los términos de referencia o las políticas de la entidad ejecutora deben fijarlos [DATO_USUARIO: política de seguridad de campo]. Tercero, el registro no incluye riesgos del financiador, como cambios de política. Esas omisiones se declaran y no se rellenan con conjeturas.")

# ------------------------------------------------------------------ 10.2
d.h(2, "10.2 Análisis Cualitativo")
niv = collections.Counter(r["nivel"] for r in RK)
d.p(f"El análisis cualitativo clasifica cada riesgo por probabilidad (P) e impacto (I) en una escala ordinal de 1 a 5. El nivel resulta del producto P×I. El nivel es extremo desde 20, alto de 12 a 19, medio de 6 a 11 y bajo por debajo de 6. Los umbrales son PROPUESTO. El registro contiene {niv['EXTREMO']} riesgo extremo, {niv['ALTO']} riesgos altos, {niv['MEDIO']} medios y {niv['BAJO']} bajos. La {{T:t02}} ubica los riesgos en la matriz de 5 por 5 y la {{F:f01}} la presenta como mapa de calor.")
celdas = collections.defaultdict(list)
for r in RK: celdas[(r["P"], r["I"])].append(r["id"][2:])
mat = []
for P in range(5, 0, -1):
    mat.append((f"P = {P}",) + tuple(", ".join(celdas[(P, I)]) or "—" for I in range(1, 6)))
d.tabla("t02", "Matriz de probabilidad e impacto con los riesgos ubicados",
        ["Probabilidad", "I = 1 (muy bajo)", "I = 2 (bajo)", "I = 3 (medio)", "I = 4 (alto)", "I = 5 (muy alto)"], mat,
        "*Nota.* Elaboración propia con datos de maestro.py (RIESGOS). Cada celda lista los identificadores sin el prefijo R-; TEC: técnico; ORG: organizacional; EXT: externo; FIN: financiero; JUR: jurídico; DAT: datos. Nivel = P × I: extremo (20 a 25), alto (12 a 19), medio (6 a 11), bajo (1 a 5). La ubicación es PROPUESTO.")
d.fig("f01", "1 riesgo extremo y 7 altos concentran el registro; ninguno queda en nivel bajo",
      "Nota. Elaboración propia con datos de maestro.py (RIESGOS). Matriz de 5 por 5 con nivel = P × I (escala de 1 a 5, PROPUESTO); trama y etiqueta según nivel. Python 3 y matplotlib; script c10_figs.py; sin semilla; corte del 13 de octubre de 2026.")
d.p("El riesgo R-TEC-01 es el único extremo. Describe la saturación de los cabezales ópticos por humedad y polvo, con probabilidad de 60 % e impacto de 250 millones de COP. Afecta directamente la variable central del problema, el error de medición sin verificar (V06). Los siete riesgos altos incluyen tres técnicos, dos organizacionales, uno externo y uno financiero. Los riesgos organizacionales R-ORG-01 y R-ORG-02 tienen impacto alto o muy alto sobre el uso y la custodia. Ningún riesgo es bajo, lo que sugiere que la escala puede estar sesgada hacia el pesimismo o que el proyecto es genuinamente arriesgado.")
d.p("Las escalas ordinales tienen límites conocidos. Multiplicar rangos ordinales produce un índice que ordena, pero no mide. Tversky y Kahneman (1974) documentaron que la estimación subjetiva de probabilidades se ancla en valores salientes y subestima la incertidumbre. Por esa razón el proyecto no usa el nivel para calcular la reserva. La reserva descansa en el valor esperado. El nivel solo decide quién responde. Ese uso es compatible con la crítica y mantiene la utilidad de la matriz como lenguaje común del equipo.")

# ------------------------------------------------------------------ 10.3
d.p("El seguimiento de cada riesgo usa su disparador observable y no la percepción del responsable. El disparador de R-TEC-01 es un NRMSE superior a 30 % en dos verificaciones consecutivas. El de R-TEC-02 es una disponibilidad mensual inferior a 90 %. El de R-ORG-01 es un uso inferior a 50 % en el tramo 1. Esos valores coinciden con los umbrales de los indicadores PERS, de modo que el seguimiento del riesgo y el del desempeño usan la misma medición. La ISO (2018) recomienda integrar la gestión del riesgo en los procesos de gobierno y de seguimiento. El proyecto cumple esa recomendación al registrar el estado de cada disparador en el informe mensual.")

d.h(2, "10.3 Análisis Cuantitativo")
d.p("El análisis cuantitativo calcula el valor monetario esperado de cada riesgo. El EMV es el producto de la probabilidad por el impacto en millones de COP (Raiffa, 1968). La suma de los 12 valores es de 636,5 millones de COP, y la reserva de contingencia redondea esa suma a 636,0 millones. La {T:t03} presenta el cálculo con la participación de cada riesgo.")
fil3 = []
tot = sum(r["emv"] for r in RK)
for r in sorted(RK, key=lambda z: -z["emv"]):
    fil3.append((r["id"], r["nivel"], f"{r['prob']} %", mm(r["impacto"]), mm(r["emv"]), num(100 * r["emv"] / tot, 1) + " %"))
fil3.append(("Total", "", "", mm(sum(r["impacto"] for r in RK)), mm(tot), "100,0 %"))
d.tabla("t03", "Análisis cuantitativo de los riesgos por valor monetario esperado",
        ["Riesgo", "Nivel", "Probabilidad", "Impacto (millones de COP)", "EMV (millones de COP)", "Participación del EMV"], fil3,
        "*Nota.* Elaboración propia con datos de maestro.py (RIESGOS). Probabilidad e impacto: PROPUESTO, NO_VERIFICADO. EMV: CALCULADO como probabilidad por impacto. La reserva de contingencia del capítulo 8 es la suma redondeada a millones: 636,0 millones de COP. Decimales con coma.")
d.p(f"Dos riesgos concentran la mitad del valor esperado. R-FIN-01, la devaluación del peso, aporta 165,0 millones, y R-TEC-01, la saturación de cabezales, aporta 150,0 millones. Juntos suman 315,0 millones, es decir, 49,5 % de la reserva. Por categoría, los riesgos técnicos suman 233,5 millones, los financieros 185,0, los organizacionales 96,0, los externos 84,0, los jurídicos 20,0 y los de datos 18,0. La reserva debe vigilarse con prioridad sobre estos dos riesgos.")
d.p(f"La reserva equivale al valor esperado y no a una cota de la pérdida. Si los 12 riesgos fueran independientes (SUPUESTO), la pérdida total tendría media de {mm(media * M)} millones y desviación estándar de {mm(sd * M)} millones. La probabilidad de que la pérdida supere la reserva sería de {num(100 * p_gt, 1)} %. Un cálculo exacto sobre las 4.096 combinaciones posibles da los cuantiles de la {{T:t04}}. Esos valores no son pronósticos. Muestran qué tan amplia es la incertidumbre que la reserva no cubre.")
fil4 = [("Pérdida esperada", mm(media * M), "CALCULADO", "Igual a la suma de los EMV"),
        ("Desviación estándar", mm(sd * M), "CALCULADO", "Bajo independencia de los 12 riesgos (SUPUESTO)"),
        ("Probabilidad de ninguna materialización", num(100 * p_cero, 2) + " %", "CALCULADO", "Producto de los complementos de las 12 probabilidades"),
        ("Probabilidad de que la pérdida supere la reserva", num(100 * p_gt, 1) + " %", "CALCULADO", "Reserva de 636,0 millones de COP"),
        ("Percentil 50", mm(cuantil(0.5) * M), "CALCULADO", "Mediana de la pérdida total"),
        ("Percentil 80", mm(cuantil(0.8) * M), "CALCULADO", "Primer valor con probabilidad acumulada de 80 % o más"),
        ("Percentil 90", mm(cuantil(0.9) * M), "CALCULADO", "Primer valor con probabilidad acumulada de 90 % o más"),
        ("Percentil 95", mm(cuantil(0.95) * M), "CALCULADO", "Primer valor con probabilidad acumulada de 95 % o más"),
        ("Suma de los 12 impactos", mm(suma_imp * M), "CALCULADO", "Pérdida si todos los riesgos se materializaran")]
d.tabla("t04", "Distribución de la pérdida total por riesgos bajo independencia, en millones de COP",
        ["Estadístico", "Valor", "Naturaleza", "Observación"], fil4,
        "*Nota.* Elaboración propia con datos de maestro.py (RIESGOS); enumeración exacta de las 4.096 combinaciones de ocurrencia con probabilidades PROPUESTO. La independencia entre riesgos es un SUPUESTO que no se verificó. Decimales con coma.")
d.p(f"El percentil 80 de la pérdida es de {mm(cuantil(0.8) * M)} millones de COP y el percentil 95 es de {mm(cuantil(0.95) * M)} millones. La reserva cubre entonces {num(100 * RES / suma_imp, 1)} % de la suma de los impactos y {num(100 * RES / cuantil(0.8), 0)} % del percentil 80. El supuesto de independencia probablemente subestima la cola. R-TEC-01 y R-TEC-04 comparten la variable V06, y una falla de humedad puede propagarse a ambos. La correlación positiva amplía la dispersión. La conclusión es que la reserva sirve para el escenario esperado, y no para un escenario adverso.")
d.p("Tres opciones permiten tratar esa brecha. La primera acepta que, en la mitad de los casos, las pérdidas superarán la reserva. Las absorben el cronograma y la holgura no solicitada, de 4.732.740.000 COP bajo el tope declarado. La segunda solicita una reserva mayor, si los términos de referencia la admiten, y la decisión DEC-F06 no la adopta. La tercera reduce la exposición con compra por tramos y cobertura cambiaria, que atacan los dos riesgos de mayor valor esperado. El proyecto adopta la tercera y deja la segunda como opción condicionada, a decidir con el financiador.")

# ------------------------------------------------------------------ 10.4
d.h(2, "10.4 Plan de Respuesta")
est = collections.Counter(r["estrategia"] for r in RK)
d.p(f"El plan de respuesta asigna a cada riesgo una estrategia, una acción específica, un responsable y un disparador. La norma ISO 31000 distingue cuatro opciones de tratamiento: evitar, transferir, mitigar y aceptar (ISO, 2018). El plan usa {est['Mitigar']} riesgos con estrategia de mitigación, uno con aceptación y mitigación, uno con transferencia y mitigación, y uno con evitación. Ningún riesgo se trata solo con aceptación pasiva. La {{T:t05}} presenta el plan y la {{F:f02}} muestra el flujo de escalamiento.")
fil5 = []
for r in RK:
    fil5.append((r["id"], r["estrategia"], r["respuesta"], r["resp"], r["disp"], mm(r["emv"])))
d.tabla("t05", "Plan de respuesta a riesgos con responsable, disparador y reserva asignada",
        ["Riesgo", "Estrategia", "Acción específica", "Responsable", "Disparador de activación", "Reserva (millones de COP)"], fil5,
        "*Nota.* Elaboración propia con datos de maestro.py (RIESGOS). La reserva asignada es el EMV de cada riesgo. Las estrategias, acciones y responsables son PROPUESTO. Los cargos corresponden a las líneas de personal del capítulo 8. Decimales con coma.")
d.fig("f02", "El nivel P × I fija quién decide: responsable, gerencia o comité directivo",
      "Nota. Elaboración propia. Flujo de escalamiento PROPUESTO con los niveles de la Figura 10.1; reserva de contingencia de 636,0 millones de COP. Python 3 y matplotlib; script c10_figs.py; sin semilla; corte del 13 de octubre de 2026.")
d.p("El escalamiento sigue el nivel del riesgo. Los cuatro riesgos de nivel medio los gestiona el responsable asignado, que informa en la retrospectiva quincenal. Los siete de nivel alto requieren aprobación de la gerencia de proyecto para usar la reserva. El único extremo, R-TEC-01, se decide en el comité directivo, que evalúa el pivote y comunica al financiador. Una pregunta de control complementa el flujo. Si el riesgo compromete una compuerta o supera la reserva, se activa la revisión de compuerta con el árbol de decisión.")
d.p("Las acciones más relevantes atacan las causas del análisis estructural. Para R-TEC-01, el modelo de corrección por humedad, el banco de calibración y la reposición de cabezales atacan la causa V03. Para R-TEC-02 y R-TEC-03, los kits solares y el enlace satelital protegen la disponibilidad. Para R-ORG-01 y R-ORG-02, el co-diseño y los convenios por tramo atacan V15, la adopción institucional. Casi todas las acciones tienen un costo presupuestado en alguna línea del capítulo 8, de modo que la mitigación no depende de la reserva. La cobertura cambiaria de R-FIN-01 es la excepción, porque ninguna línea la incluye.")
d.p("Una limitación del plan es que los responsables son cargos y no personas. La asignación nominal depende de la contratación, que ocurre en las primeras ocho semanas [DATO_USUARIO: nombres de los responsables de riesgo]. Hasta entonces, el plan es una propuesta. Otra limitación es el procedimiento para modificar el plan con el financiador. Depende de los términos de referencia [DATO_USUARIO: procedimiento de modificación del plan]. Sin ese procedimiento, el pivote de una compuerta puede exigir una adenda.")

# ------------------------------------------------------------------ 10.5
d.h(2, "10.5 Verificación de Alineación Estratégica")
d.p("La verificación de alineación pregunta, en cada hito, si el proyecto sigue sirviendo al propósito que lo justifica. Un proyecto puede cumplir cada actividad y, aun así, desviarse de su objetivo. Argyris y Schön (1978) llaman aprendizaje de lazo doble a la revisión de los supuestos que sostienen las metas. La {T:t06} lista las preguntas por hito, el criterio de decisión y la evidencia requerida. Las preguntas se responden por escrito y quedan en el acta de cada compuerta.")
fil6 = [
 ("H1", "¿Los sitios y el diseño de enlace y energía permiten cumplir la autonomía de 14 días y el almacenamiento de 7 días?", "Informe de sitios, de cobertura y de energía sin brechas críticas", "Rediseñar enlace o energía antes de comprar el lote 1"),
 ("H2", "¿La línea base de error se midió frente a la referencia en los tres departamentos?", "Base de colocalización con 60.000 horas-nodo válidas o más", "Ampliar la colocalización o reducir la meta de forma justificada"),
 ("H3 (C1)", "¿El modelo cumple R² de 0,70 o más y NRMSE de 30 % o menos, y 50 % o más de los comités usa el tablero?", "Acta de compuerta con métricas de validación y actas de comité", "Pivotar la medición o el uso; no liberar el tramo 2"),
 ("H4", "¿El modelo entrenado en un departamento generaliza a los otros dos?", "Informe de desempeño por departamento del tramo 2", "Reentrenar por departamento; reforzar energía y enlace"),
 ("H5 (C2)", "¿Se cumplen los umbrales en tres departamentos, con disponibilidad de 90 % o más y convenios de custodia con partida?", "Acta de compuerta con convenios y partidas verificadas", "Pivotar la custodia; cláusula de apertura por función; no liberar el tramo 3"),
 ("H6", "¿Las 100 unidades y los 10 gateways operan con disponibilidad mensual de 90 % o más?", "Inventario de la red con huella de configuración", "Reponer con reserva de 20 nodos y un gateway"),
 ("H7", "¿Un laboratorio externo confirma el desempeño frente a los umbrales?", "Informe del ensayo independiente y evaluación externa final", "Declarar el nivel de madurez alcanzado sin afirmar TRL 8"),
 ("H8 (C3)", "¿Los custodios tienen capacidad, partida y convenio para operar tras el cierre?", "Actas de entrega y cláusula de apertura firmada", "Activar la cláusula de apertura y liberar datos y código"),
]
d.tabla("t06", "Lista de verificación de alineación estratégica por hito",
        ["Hito", "Pregunta de alineación", "Evidencia requerida", "Respuesta si el criterio no se cumple"], fil6,
        "*Nota.* Elaboración propia con datos de la ficha maestra §4, §6 y §8 y de la sección 4.4-MDR.12. Las preguntas, evidencias y respuestas son PROPUESTO. Los umbrales de desempeño tienen ancla externa en U.S. Environmental Protection Agency (2021) para uso informativo en sitio fijo y requieren ratificación. Decimales con coma.")
d.p("La alineación con el marco lógico completa la verificación. Cada pregunta de la lista se vincula con un nivel del marco lógico. Las de H1 y H2 corresponden a las actividades. Las de H4 y H6 corresponden a los componentes. Las de H3 y H5 corresponden al propósito. La de H8 corresponde al fin. Esa correspondencia permite detectar saltos lógicos entre niveles (Funnell y Rogers, 2011). Si el producto se entrega pero el efecto no ocurre, el equipo debe revisar el mecanismo de cambio y no solo la ejecución. El capítulo 12 desarrolla los indicadores que miden esos efectos y el capítulo 18 presenta el marco lógico.")
d.p("El mecanismo de revisión continua combina tres capas. La revisión trimestral del registro actualiza probabilidades e impactos con datos reales. La revisión de fase, antes de cada compuerta, cuestiona los supuestos críticos. La evaluación externa de los meses 12 y 24 aporta una mirada independiente. Ries (2011) define el pivote como una corrección de rumbo estructurada para probar una nueva hipótesis fundamental. El proyecto adopta esa definición. Pivotar la medición, el uso o la custodia es una respuesta legítima y no un fracaso.")
d.p("La {F:f03} formaliza los criterios de pivote o perseverancia de las compuertas C1 y C2. En C1, dos preguntas en secuencia determinan la decisión: el desempeño del modelo y el uso del tablero. Si ambas se cumplen, se libera la compra del tramo 2, por 388,0 millones de COP. En C2, dos preguntas determinan la liberación del tramo 3, por 306,0 millones. La primera exige desempeño en los tres departamentos con disponibilidad de 90 % o más. La segunda exige convenios de custodia con partida.")
d.fig("f03", "C1 y C2 liberan la compra del tramo siguiente solo si se cumplen todos los criterios",
      "Nota. Elaboración propia con los umbrales de la ficha maestra (C1 y C2); respuestas de pivote PROPUESTO de la sección 4.4-MDR.12. Python 3 y matplotlib; script c10_figs.py; sin semilla; corte del 13 de octubre de 2026.")
d.p("El árbol obliga a elegir antes de conocer los datos. Esa elección previa protege contra la reinterpretación de los criterios después de ver los resultados. Cooper (2008) señala que las compuertas pierden valor cuando los criterios se relajan para no detener un proyecto. Collingridge (1980) recomienda mantener reversibles las decisiones tempranas. La compra por tramos cumple ambos consejos. Los criterios se fijan ahora, y las compras que no se liberan quedan sin ejecutar. El capítulo 21 resume los cinco riesgos de mayor valor esperado en el acta de constitución.")
d.guardar(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps", "cap10.md"))
print("ok", round(media, 1), round(sd, 1), round(p_gt, 4), cuantil(0.5), cuantil(0.8), cuantil(0.9), cuantil(0.95), round(p_cero, 4))
