# -*- coding: utf-8 -*-
import sys
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/figs/scripts"); sys.path.insert(0, RAIZ + "/maestro")
import c12_datos as D
import maestro as M
import indicadores as I
IND = D.IND; ORD = D.ORDEN
def esc(s): return str(s).replace("|", "\\|")
L = []; A = L.append
def tabla(tid, titulo, enc, filas, nota):
    A(f":::TABLA {tid} | {titulo}")
    A("| " + " | ".join(enc) + " |"); A("| " + " | ".join("---" for _ in enc) + " |")
    for r in filas: A("| " + " | ".join(esc(x) for x in r) + " |")
    A(":::NOTA " + nota); A("")
def rdg(tid, titulo, campos, nota):
    tabla(tid, f"Registro de decisión GENESIS: {titulo}", ["Campo", "Contenido"], campos, nota)
cod = lambda n: f"PERS-{n}"
A("%% PREFIJO: F7")
A("# Paso 7. Sistema de indicadores PERS")
A("")
A("El Paso 7 diseña el sistema de indicadores que verifica la alternativa seleccionada. El sistema PERS reúne 15 indicadores en cuatro niveles: proceso (R), producto (P), efecto (E) y sostenibilidad (S). Este paso define la taxonomía, la estructura jerárquica, la articulación con los criterios del SGR y la validación entre metas y recursos. Presenta también la ficha técnica de cada indicador en dos tablas compactas. El capítulo 12 desarrolla cada ficha con sus 12 campos, su línea base y su cronograma de medición. Las dos presentaciones usan los mismos datos y no pueden diferir.")
A("")
A("## F7.0 Taxonomía obligatoria: outputs, outcomes e impacts")
A("")
A("Los evaluadores penalizan la confusión entre tres niveles. Un output es un bien, un servicio o un hecho verificable que agota un objetivo específico. Un outcome es el efecto inmediato en quienes reciben el output. Un impact es la transformación estructural y sostenida que se deriva de los outcomes. El error más frecuente consiste en presentar un indicador de gestión como si fuera un impacto. La {T:t01} aplica la taxonomía al proyecto con un ejemplo correcto y otro incorrecto de cada nivel.")
A("")
tabla("t01", "Taxonomía Output-Outcome-Impact aplicada al proyecto", ["Nivel", "En MinCiencias", "Definición", "Mide", "Horizonte", "Ejemplo correcto del proyecto", "Ejemplo incorrecto"], [
 ("Output", "Productos y actividades", "Bienes, servicios o hechos concretos y verificables que agotan los objetivos específicos", "El esfuerzo o la producción, no el cambio", "Inmediato, durante la ejecución", "100 nodos y 10 gateways operativos al mes 24 (PERS-P01)", "Declarar la instalación de la red como impacto del proyecto"),
 ("Outcome", "Resultados o efectos inmediatos", "Efectos de corto plazo en los destinatarios tras recibir los outputs; reflejan adopción o uso", "Cómo los beneficiarios usan el producto", "De 0 a 12 meses posteriores al output", "Al menos 75 % de los comités usa el tablero en decisiones documentadas (PERS-E01)", "Declarar el número de personas capacitadas como resultado de uso"),
 ("Impact", "Impacto", "Transformación sostenida que se deriva de los outcomes", "Si el proyecto resolvió el problema", "De 1 a 5 años posteriores al proyecto", "Al menos 70 % de la red opera bajo custodia 12 meses después del cierre (PERS-S02)", "Declarar una reducción de morbilidad sin línea base ni diseño causal"),
], "*Nota.* Elaboración propia con la especificación del metaprompt y la ficha maestra (sección 8). El proyecto no promete efectos en salud: los impacts son de uso institucional y de continuidad.")
A("La {F:f01} ordena los 15 indicadores en la cadena lógica. Los diez indicadores R y P son outputs, los tres E son outcomes y los dos S son impacts. Los impacts se miden entre 6 y 12 meses después del cierre y por una evaluación externa (decisión DEC-F10). Esa medición posterior exige una fuente de financiación que la línea S07 solo cubre hasta el mes 24.")
A("")
A(":::FIGURA f01 | Diez outputs sostienen tres outcomes y dos impactos que se miden después del cierre | Nota. Elaboración propia con maestro/indicadores.py y maestro.py. Cadena lógica de los 15 indicadores PERS. Figura generada con matplotlib mediante cF7_figs.py; sin semilla ni corpus.")
A("")
A("### F7.0.1 Validación bloqueante")
A("")
A("El sistema verifica cuatro condiciones antes de avanzar. Cada output debe tener al menos un outcome asociado. Cada outcome debe conectarse con al menos un impacto. Ningún output puede clasificarse como impacto. Los impactos deben ser transformaciones medibles a mediano o largo plazo. La {T:t02} registra el resultado. Una condición obtiene PARCIAL: dos outputs de gestión, R04 y R06, no tienen un outcome propio.")
A("")
tabla("t02", "Validación bloqueante de la cadena Output-Outcome-Impact", ["Condición", "Resultado", "Evidencia"], [
 ("Cada output tiene al menos un outcome", "PARCIAL", "R01, R03 y P01 alimentan E01 porque el uso exige datos disponibles. R02, R05, P02 y P03 alimentan E02 porque la corrección reduce falsas alarmas. P04 alimenta E01 y E03. R04 y R06 son outputs de gestión sin outcome propio."),
 ("Cada outcome se conecta con al menos un impact", "CUMPLE", "E01 y E02 conducen a S01 (activación del protocolo). E03 conduce a S02 (continuidad de la red bajo custodia)."),
 ("Ningún output se clasifica como impact", "CUMPLE", "Los 10 indicadores R y P tienen taxonomía Output; los 5 indicadores E y S tienen Outcome e Impact."),
 ("Los impacts son transformaciones medibles", "CUMPLE", "S01 y S02 se miden a 12 meses del cierre con evaluación externa; ninguno es una actividad."),
], "*Nota.* Elaboración propia con maestro/indicadores.py. Las asociaciones outcome-output son PROPUESTO. El estado PARCIAL no bloquea el avance porque R04 y R06 son outputs de gestión por diseño.")
A("Las metas de los indicadores siguen una regla de proporcionalidad. Los indicadores R se fijan en 100 % porque dependen de la ejecución propia. Los indicadores P se fijan en cantidades que el presupuesto y el cronograma sostienen, como lo demuestra la {T:t05}. Los indicadores E se fijan por debajo del 100 %, porque dependen de la decisión de terceros. Son 75 % de uso de los comités y 30 % de reducción relativa de falsas alarmas. Los indicadores S se fijan en 80 % y 70 %, porque dependen además de la custodia posterior.")
A("")
A("Esa gradación evita una promesa común en los proyectos de ciencia, tecnología e innovación. Consiste en comprometer con la misma certeza lo que se controla y lo que no. Cuanto más lejos del control del ejecutor está el indicador, menor es la meta y mayor es la exigencia de evidencia independiente. Los indicadores E y S se verifican con evaluación externa y con el registro de decisiones de los comités. No se verifican con el reporte del propio equipo.")
A("")
A("## F7.1 Estructura jerárquica PERS articulada con el SGR")
A("")
A("Los cuatro niveles del sistema corresponden a niveles del marco lógico y a horizontes de medición distintos. La {T:t03} los presenta con su cantidad y su criterio de viabilidad ante el SGR. El nivel R verifica la ejecución presupuestal y de actividades. El nivel P exige productos verificables y tipificados según el modelo de medición de grupos (MMG 2021). El nivel E exige evidencia de adopción. El nivel S exige evidencia de continuidad y articulación territorial.")
A("")
tabla("t03", "Estructura jerárquica PERS", ["Nivel PERS", "Marco lógico", "Taxonomía MinCiencias", "Cadena de valor", "Horizonte", "Cantidad", "Viabilidad SGR"], [
 ("R, proceso", "Actividades", "Outputs", "Insumos a actividades", "Corto (mensual)", "6", "Verificación de ejecución presupuestal y de actividades programadas"),
 ("P, producto", "Componentes", "Outputs tipificados MMG 2021", "Actividades a productos", "Mediano (trimestral)", "4", "Productos verificables en CvLAC y GrupLAC, registros de propiedad intelectual y certificaciones"),
 ("E, efecto", "Propósito", "Outcomes", "Productos a efectos", "Mediano (semestral)", "3", "Evidencia de adopción, uso o cambio de comportamiento"),
 ("S, sostenibilidad", "Fin", "Impact", "Efectos a impactos", "Largo (anual o posterior)", "2", "Continuidad de la red y activación del protocolo, articuladas con el PDD [DATO_USUARIO: indicadores del PDD]"),
 ("Total", "", "", "", "", "15", ""),
], "*Nota.* Elaboración propia con la especificación del metaprompt y maestro/indicadores.py.")
A("### F7.1.1 Articulación con los criterios de viabilidad del SGR")
A("")
A("Los términos de referencia no se aportaron. Por eso los pesos de los criterios de evaluación son los rangos por defecto del metaprompt (SUPUESTO). La {T:t04} vincula cada criterio con los indicadores que lo sustentan y con la evidencia que exige. Si los términos de referencia fijan otros pesos, el vínculo se conserva y solo cambia el peso.")
A("")
tabla("t04", "Articulación de los indicadores PERS con los criterios de viabilidad del SGR", ["Criterio SGR", "Indicadores PERS vinculados", "Evidencia requerida", "Peso por defecto"], [
 ("Pertinencia y articulación territorial", "PERS-S01 y PERS-S02", "Artículo del PDD y código de demanda territorial [DATO_USUARIO: artículos y códigos]", "20 a 25 %"),
 ("Fortalecimiento de la CTeI regional", "PERS-P01 a PERS-P04", "Productos tipificados MMG 2021 y nivel alcanzado de la escalera de apropiación social", "25 a 27 %"),
 ("Calidad técnica", "PERS-R01 a PERS-R06", "Metodología validada e indicadores con línea base", "20 a 25 %"),
 ("Impacto esperado", "PERS-E01 a PERS-E03, PERS-S01 y PERS-S02", "Cadena causal Output-Outcome-Impact verificable", "15 a 20 %"),
 ("Viabilidad presupuestal", "PERS-R con cruce al presupuesto", "Cada meta P validada contra rubro y plazo", "10 a 15 %"),
], "*Nota.* Elaboración propia con la especificación del metaprompt. Los pesos son rangos por defecto, SUPUESTO por falta de términos de referencia.")
A("### F7.1.2 Validación entre meta, recurso y cronograma")
A("")
A("Cada indicador de producto debe validarse contra el rubro que lo financia y contra el plazo del cronograma. La {T:t05} cruza las cuatro metas P con los rubros asociados, el monto asignado, la actividad y el mes. Los montos se calculan con los datos maestros. La regla del metaprompt detiene la generación del presupuesto si alguna coherencia falla. Ninguna falla en esta formulación: tres cumplen y una cumple con observación.")
A("")
obs = {"PERS-P01": "CUMPLE: la compra por tramos y la instalación coinciden con los hitos H4 y H6",
       "PERS-P02": "CUMPLE con observación: el esfuerzo de desarrollo se financia en personal; el rubro propio cubre solo el registro",
       "PERS-P03": "CUMPLE: el primer artículo usa el piloto de C1; el segundo exige la verificación final y puede no aceptarse al mes 24",
       "PERS-P04": "CUMPLE: 20 kits, 20 eventos y 9 jornadas coinciden con las 29 actividades"}
filas = []
for c in ("PERS-P01", "PERS-P02", "PERS-P03", "PERS-P04"):
    i = IND[c]; t = D.TRAZA[c]
    filas.append((f"{c}: {i['nombre']}", i["mf"], D.lista_y(t["rub"]), D.mm(D.monto(t["rub"])) + " M", D.lista_y(t["act"]), "Mes " + str(D.HIT[t["hitos"][-1]]["mes"]), obs[c]))
tabla("t05", "Validación cruzada de meta, recurso y cronograma para los indicadores de producto", ["Indicador", "Meta final", "Rubros asociados", "Monto (millones de COP)", "Actividades", "Plazo", "Coherencia"], filas,
      "*Nota.* Elaboración propia con maestro.py (BUDGET, ACT) y c12_datos.py. Los montos suman las líneas de rubro asociadas; la asociación indicador-rubro es PROPUESTO. M: millones de COP.")
A("## F7.2 Fichas técnicas de los indicadores")
A("")
A("Las fichas de los 15 indicadores siguen los 12 campos del metaprompt. Para no duplicar el capítulo 12, este paso presenta los campos en dos tablas. La {T:t06} reúne identificación, fórmula, línea base, metas y periodicidad. La {T:t07} reúne fuente de datos, supuestos, riesgo de incumplimiento y verificación. Los campos de limitaciones, desagregación y metadata, junto con la justificación de las metas, figuran en las fichas completas del capítulo 12.")
A("")
f6 = []; f7 = []
for c in ORD:
    i = IND[c]
    f6.append((c, i["nombre"], i["oe"], i["formula"], i["unidad"], f"{i['lb']} ({i['lb_nat']})", f"{i['m1']}; final: {i['mf']}", i["frecuencia"], i["resp"]))
    f7.append((c, i["fuente"], i["supuesto"], i["riesgo"], i["verificacion"], i["mmg"]))
tabla("t06", "Fichas de los indicadores PERS: identificación, fórmula, línea base, metas y periodicidad", ["Código", "Nombre", "OE", "Fórmula", "Unidad", "Línea base", "Metas", "Frecuencia", "Responsable"], f6,
      "*Nota.* Elaboración propia con maestro/indicadores.py. Línea base VACIO se mide en el tramo 1. Naturaleza de las metas: PROPUESTO; de las líneas base: CALCULADO o VACIO según la celda.")
tabla("t07", "Fichas de los indicadores PERS: fuente, supuestos, riesgo y verificación", ["Código", "Fuente de datos", "Supuesto", "Riesgo de incumplimiento", "Medio de verificación", "Tipo MMG"], f7,
      "*Nota.* Elaboración propia con maestro/indicadores.py. El riesgo de incumplimiento es un juicio PROPUESTO. El tipo MMG 2021 se confirma con la convocatoria vigente [DATO_USUARIO: tipología MMG].")
A("La {T:t08} registra la decisión sobre la asignación de niveles (nodo ND-16).")
A("")
rdg("t08", "ND-16 Asignación output, outcome e impact", [
 ("NODO", "ND-16 Asignación output, outcome e impact"),
 ("CLASE", "MAYOR. Determina qué se promete como resultado y qué como impacto."),
 ("DECISION", "Clasificar los 10 indicadores R y P como outputs, los 3 E como outcomes y los 2 S como impacts, sin promesa de efecto en salud."),
 ("DECIDE", "Equipo formulador [DATO_USUARIO: responsable de la decisión]."),
 ("EXCLUYE", "Presentar outputs como impactos. Prometer reducción de morbilidad sin línea base ni diseño causal."),
 ("NODOS_BLANCOS", "3: el diseño de cada indicador usa fórmula, unidad y fuente; las metas de desempeño usan umbrales de EPA (2021); el presupuesto respalda cada meta P."),
 ("NODOS_GRISES", "3: líneas base VACIO de E y S; capacidad de los custodios; articulación con el PDD."),
 ("RUPTURAS", "R-01: 0 | R-02: 0 | R-03: 0 | R-04: 0 | R-05: 0."),
 ("PATRON_DOMINANTE", "PR-06 (patrón emergente): medir uso y continuidad, no efectos que el diseño no identifica."),
 ("ANTIPATRONES_PR", "PR-04 ausente: Sí. PR-05 ausente: No. Los impacts dependen de la custodia por entidades externas."),
 ("ESCENA_SIMULABLE", "Un evaluador pide el impacto del proyecto. El documento responde con S01 y S02 medidos a 12 meses del cierre."),
 ("EVIDENCIA_JH_A", "Tabla F7.2: validación bloqueante."),
 ("EVIDENCIA_JH_B", "Tabla F7.5: cruce de metas P con presupuesto y cronograma."),
 ("CERCA_CONCEPTUAL", "Un indicador de uso no prueba un cambio en la salud de la población."),
 ("ESTATUTO_CAUSAL", "HIE."),
 ("VEREDICTO", "Asignación adoptada; R04 y R06 se conservan como outputs de gestión."),
 ("RAZON_DEL_DESCARTE", "Se descarta un indicador de morbilidad por falta de línea base y de diseño causal."),
 ("RESULTADO", "CIERRA con vacíos declarados (líneas base de E y S)."),
], "*Nota.* Elaboración propia con el protocolo de decisión GENESIS.")
A("El Paso 7 crea valor al convertir cada promesa del proyecto en un indicador con fórmula, fuente, responsable y plazo. También separa lo que el proyecto entrega de lo que otros deben sostener. El Paso 8 desarrolla los 21 capítulos del documento con estas definiciones.")
open(RAIZ + "/caps/paso7.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("ok")
