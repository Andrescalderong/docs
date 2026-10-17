# -*- coding: utf-8 -*-
"""Genera las 22 tablas del capítulo 12 (bloques ':::TABLA ... :::NOTA') desde IND, TRAMOS, HITOS y BUDGET (c12_datos.py).
TABLAS: dict id -> bloque markdown. Orden de aparición lo fija la plantilla."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c12_datos as D

IND = D.IND; M = D.M

def esc(s):
    return str(s).replace("|", "\\|")

def bloque(id_, titulo, heads, rows, nota):
    L = [f":::TABLA {id_} | {titulo}", "| " + " | ".join(heads) + " |", "| " + " | ".join("---" for _ in heads) + " |"]
    for r in rows:
        assert len(r) == len(heads), (id_, r)
        L.append("| " + " | ".join(esc(c) for c in r) + " |")
    L.append(f":::NOTA {nota}")
    return "\n".join(L)

# ------------------------------------------------------------------ ficha técnica (12 campos del paso 7 + trazabilidad)
TAXO_TXT = {"R": "Output de gestión: mide esfuerzo y ejecución, no resultados ni impactos",
            "P": "Output tipificado: mide el producto entregado, no su uso",
            "E": "Outcome: mide adopción o cambio de capacidad en destinatarios, sin efectos en salud",
            "S": "Impact institucional: mide continuidad y activación sostenidas, sin estimar exposición ni salud"}

def ficha(c):
    i = IND[c]; x = D.EXTRA[c]; t = D.TRAZA[c]; n = i["nivel"]
    rub = D.rubros_texto(c)
    if n == "S":
        rub += ". La línea S07 cubre las evaluaciones de los meses 12 y 24; la medición del mes 36 no tiene línea (VACIO)"
    if c == "PERS-P03":
        rub += ". El tiempo de autoría es contrapartida de la IES (C01 y C02)"
    prod = "; ".join(D.COMPONENTES[k] for k in t["prod"])
    R = []
    g = "1. Identificación"
    R += [(g, "Código", c), ("", "Nombre", i["nombre"]), ("", "Nivel PERS", D.NIVEL_PERS[n]),
          ("", "Taxonomía MinCiencias", f"{i['tax']}. {TAXO_TXT[n]}"), ("", "Nivel del marco lógico", D.MARCO[n]),
          ("", "Objetivo asociado", D.OE_NOMBRE[i["oe"]])]
    if i["mmg"] != "—":
        if c == "PERS-E03":
            R.append(("", "Tipo MMG 2021", f"{i['mmg']}. [DATO_USUARIO: código de tipología según la convocatoria vigente]"))
        else:
            R.append(("", "Tipo MMG 2021", f"{i['mmg']} (PROPUESTO; NO_VERIFICADO)"))
    R += [("", "Producto asociado", prod), ("", "Actividad (ACT)", D.act_texto(c)), ("", "Hito", D.hitos_texto(c)),
          ("", "Rubro presupuestal", rub)]
    g = "2. Definición"
    R += [(g, "Descripción", x["desc"]), ("", "Justificación", x["just"])]
    g = "3. Fórmula"
    R += [(g, "Expresión", i["formula"]), ("", "Variables", x["vars"]), ("", "Unidad", i["unidad"])]
    g = "4. Línea base"
    R += [(g, "Valor actual", f"{i['lb']} ({i['lb_nat']})"), ("", "Fecha de medición", x["lbf"]), ("", "Fuente", x["lbfu"]), ("", "Metodología", x["lbm"])]
    g = "5. Metas"
    R += [(g, "Meta al mes 12 (año 1; compuerta C1)", i["m1"]), ("", "Meta al mes 17 (año 2; compuerta C2)", i["m2"]),
          ("", "Meta final", i["mf"]), ("", "Justificación", x["jm"])]
    g = "6. Periodicidad"
    R += [(g, "Frecuencia de medición", i["frecuencia"]), ("", "Frecuencia de reporte", x["rep"]),
          ("", "Responsable de medición", i["resp"]), ("", "Responsable de reporte", x["rrep"])]
    g = "7. Fuente de datos"
    R += [(g, "Fuente primaria", i["fuente"]), ("", "Fuente secundaria", x["fsec"]), ("", "Instrumento", x["ins"]), ("", "Ubicación de los datos", x["ubi"])]
    g = "8. Desagregación"
    R += [(g, "Territorial", x["dterr"]), ("", "Temporal", x["dtemp"]), ("", "Poblacional", x["dpob"]), ("", "Otras", x["dotr"])]
    g = "9. Limitaciones"
    R += [(g, "Metodológica", x["lmet"]), ("", "Cobertura", x["lcob"]), ("", "Mitigación", x["lmit"])]
    g = "10. Supuestos"
    R += [(g, "Condición externa", x["cext"]), ("", "Condición institucional", x["cins"]), ("", "Supuesto de la ficha maestra", i["supuesto"]),
          ("", "Riesgo de incumplimiento", i["riesgo"])]
    g = "11. Verificación"
    R += [(g, "Medio de verificación", i["verificacion"]), ("", "Formato de evidencia", x["fmt"]), ("", "Responsable", x["rver"]), ("", "Periodicidad", x["pver"])]
    g = "12. Metadata"
    R += [(g, "Fecha de creación", D.FECHA), ("", "Versión", "1.0"), ("", "Autor", D.AUTOR), ("", "Última actualización", D.FECHA)]
    return R

NOMBRE_TABLA = {"R": "Ficha técnica {c} con clasificación Output de gestión: {n}",
                "P": "Ficha técnica {c} con tipo MMG 2021 y clasificación Output: {n}",
                "E": "Ficha técnica {c} con clasificación Outcome: {n}",
                "S": "Ficha técnica {c} con clasificación Impact y vinculación con el PDD: {n}"}

def tabla_ficha(id_, c):
    i = IND[c]
    nota = ("*Nota.* Elaboración propia con datos de la ficha maestra del proyecto (indicadores PERS, presupuesto y cronograma). "
            "Las líneas base y las metas conservan la naturaleza indicada en cada celda (CALCULADO o VACIO). Los campos de definición, "
            "desagregación, limitaciones, supuestos y verificación son PROPUESTO. TdR: términos de referencia, no aportados (NO_VERIFICADO). "
            "Decimales con coma.")
    return bloque(id_, NOMBRE_TABLA[i["nivel"]].format(c=c, n=i["nombre"]), ["Grupo", "Campo", "Contenido"], ficha(c), nota)

TABLAS = {}
IDS_FICHA = {"PERS-R01": "t02", "PERS-R02": "t03", "PERS-R03": "t04", "PERS-R04": "t05", "PERS-R05": "t06", "PERS-R06": "t07",
             "PERS-P01": "t08", "PERS-P02": "t09", "PERS-P03": "t10", "PERS-P04": "t11",
             "PERS-E01": "t14", "PERS-E02": "t15", "PERS-E03": "t16", "PERS-S01": "t17", "PERS-S02": "t18"}
for c, id_ in IDS_FICHA.items():
    TABLAS[id_] = tabla_ficha(id_, c)

# ------------------------------------------------------------------ t01 mapeo PERS -> taxonomía -> marco lógico -> criterio SGR
rows = []
for c in D.ORDEN:
    i = IND[c]
    rows.append((c, D.NIVEL_PERS[i["nivel"]], i["tax"], D.MARCO[i["nivel"]], i["oe"], D.CRITERIO[i["nivel"]]))
TABLAS["t01"] = bloque("t01", "Mapeo de los 15 indicadores PERS con la taxonomía MinCiencias, el marco lógico y el criterio SGR",
    ["Código", "Nivel PERS", "Taxonomía", "Marco lógico", "OE", "Criterio SGR del metaprompt (peso)"], rows,
    "*Nota.* Elaboración propia con datos de la ficha maestra del proyecto (indicadores PERS y marco lógico). Los criterios y los rangos de peso provienen del metaprompt "
    "GENESIS-CTeI y son SUPUESTO: los términos de referencia (TdR) no se aportaron (NO_VERIFICADO). SGR: Sistema General de Regalías. "
    "CTeI: ciencia, tecnología e innovación. OE: objetivo específico.")

# ------------------------------------------------------------------ t12 tipificación MMG
VERIF_CVLAC = " Reporte en CvLAC o GrupLAC (PROPUESTO)."
mmg_rows = [
    ("PERS-P01", "PROT-FUNC", "Prototipo funcional", IND["PERS-P01"]["verificacion"] + "." + VERIF_CVLAC, "PROPUESTO; NO_VERIFICADO"),
    ("PERS-P02", "SW-REG", "Software registrado", IND["PERS-P02"]["verificacion"] + "." + VERIF_CVLAC, "PROPUESTO; NO_VERIFICADO"),
    ("PERS-P03", "ART-A1", "Artículo en revista A1 (Q1-Q2)", IND["PERS-P03"]["verificacion"] + "." + VERIF_CVLAC, "PROPUESTO; NO_VERIFICADO"),
    ("PERS-P03", "ART-A2", "Artículo en revista A2 (Q2-Q3)", IND["PERS-P03"]["verificacion"] + "." + VERIF_CVLAC, "PROPUESTO; NO_VERIFICADO"),
    ("PERS-P04", "ASC-PART", "Participación ciudadana en CTeI", IND["PERS-P04"]["verificacion"] + "." + VERIF_CVLAC, "PROPUESTO; NO_VERIFICADO"),
    ("PERS-P04", "ASC-COM", "Comunicación social del conocimiento", IND["PERS-P04"]["verificacion"] + "." + VERIF_CVLAC, "PROPUESTO; NO_VERIFICADO"),
    ("PERS-P04", "ASC-CIRC", "Circulación de conocimiento especializado", IND["PERS-P04"]["verificacion"] + "." + VERIF_CVLAC, "PROPUESTO; NO_VERIFICADO"),
    ("PERS-E03", "[DATO_USUARIO: código de tipología según la convocatoria vigente]", "FORM (capacitación), denominación de la ficha maestra",
     IND["PERS-E03"]["verificacion"] + ".", "VACIO"),
]
TABLAS["t12"] = bloque("t12", "Tipificación MMG 2021 de los productos PERS-P con código, denominación y criterio de verificación",
    ["Indicador", "Código MMG 2021", "Denominación en la tabla de referencia", "Criterio de verificación", "Estado del dato"], mmg_rows,
    "*Nota.* Elaboración propia con los códigos de la ficha maestra y la tabla de referencia del metaprompt GENESIS-CTeI. MMG: Modelo de Medición de Grupos. "
    "La equivalencia de ART-A1 y ART-A2 con los cuartiles Q1 y Q2 depende de la clasificación de revistas vigente [DATO_USUARIO: clasificación de revistas de la convocatoria]. "
    "Los TdR y el texto del MMG 2021 no se aportaron (NO_VERIFICADO). El indicador PERS-E03 no es un producto P; se incluye porque la ficha le asigna FORM.")

# ------------------------------------------------------------------ t13 validación cruzada meta-recurso-cronograma
def plazo_txt(c):
    a, b = D.plazo_lineas(D.TRAZA[c]["rub"])
    return f"Meses {a} a {b}"
vc = []
obs = {
 "PERS-P01": "COHERENTE. 120 nodos, 11 gateways, 10 módulos y 110 sitios cubren la meta.",
 "PERS-P02": "COHERENTE. O03 inicia en el mes 12, tras la validación de C1.",
 "PERS-P03": "COHERENTE CON OBSERVACIÓN. La autoría no tiene línea SGR; usa contrapartida.",
 "PERS-P04": "COHERENTE CON OBSERVACIÓN. La meta del mes 17 iguala la final.",
}
meta_txt = {"PERS-P01": "100 nodos y 10 gateways", "PERS-P02": "1 registro vigente", "PERS-P03": "2 sometidos y al menos 1 aceptado", "PERS-P04": "29 actividades"}
assert "100 / 10" in IND["PERS-P01"]["mf"] and "29 actividades" in IND["PERS-P04"]["mf"]
for c in ("PERS-P01", "PERS-P02", "PERS-P03", "PERS-P04"):
    t = D.TRAZA[c]
    vc.append((c, meta_txt[c], ", ".join(t["rub"]), D.cop(D.monto(t["rub"])), ", ".join(t["act"]), plazo_txt(c), obs[c]))
TABLAS["t13"] = bloque("t13", "Validación cruzada meta-recurso-cronograma para los indicadores PERS-P",
    ["Indicador", "Meta", "Rubros asociados", "Monto asignado (COP)", "Actividad en cronograma", "Plazo de las líneas", "Coherencia"], vc,
    "*Nota.* Elaboración propia con datos de la ficha maestra del proyecto (presupuesto SGR y cronograma). Montos CALCULADOS como suma de las líneas indicadas; las líneas pueden servir a más de un indicador, "
    "de modo que los montos no son aditivos. La asignación de líneas a indicadores es PROPUESTO. Ninguna fila activa la alerta bloqueante de incoherencia. Naturaleza de las metas: CALCULADO y PROPUESTO.")

# ------------------------------------------------------------------ t19 articulación S con PDD
rows = []
for c in ("PERS-S01", "PERS-S02"):
    for d, nn in D.DEPTO:
        if c == "PERS-S01":
            contrib = f"Activación registrada del protocolo en los comités de {d} (80 % o más de los eventos confirmados al mes 36)"
        else:
            contrib = f"{nn} nodos entregados en {d}; 70 % o más equivale a {D.S02_DEPTO[d]} nodos con custodia al mes 36"
        rows.append((c, d, f"[DATO_USUARIO: indicador del PDD de {d}]", f"[DATO_USUARIO: meta del PDD de {d}]", contrib,
                     f"[DATO_USUARIO: código de la demanda territorial de {d}]"))
TABLAS["t19"] = bloque("t19", "Articulación de los indicadores PERS-S con el PDD: indicador del PDD, meta del PDD y contribución del proyecto",
    ["Indicador PERS", "Departamento", "Indicador del PDD", "Meta del PDD", "Contribución del proyecto", "Código de demanda (Anexo 4)"], rows,
    "*Nota.* Elaboración propia con datos de la ficha maestra del proyecto. PDD: Plan de Desarrollo Departamental. El PDD, el Anexo 4 y los documentos CONPES que cita el expediente no se aportaron (NO_VERIFICADO); "
    "los campos entre corchetes son VACIO. La distribución de 33, 34 y 33 nodos es PROPUESTO y el cálculo del 70 % por departamento es CALCULADO con redondeo hacia arriba.")

# ------------------------------------------------------------------ t20 dashboard
sem = {"Alto": "ROJO: riesgo alto", "Medio": "AMARILLO: riesgo medio", "Bajo": "VERDE: riesgo bajo"}
rows = []
for c in D.ORDEN:
    i = IND[c]
    lb = f"{i['lb']} ({i['lb_nat']})"
    est = sem[i["riesgo"]] + ("; línea base VACIO" if i["lb_nat"] == "VACIO" else "")
    rows.append((c, i["nombre"], i["nivel"], i["tax"], lb, i["mf"], i["frecuencia"], i["resp"], est))
TABLAS["t20"] = bloque("t20", "Dashboard de indicadores PERS: código, nombre, nivel, taxonomía, línea base, meta, frecuencia, responsable y estado",
    ["Código", "Nombre", "Nivel", "Taxonomía", "Línea base", "Meta final", "Frecuencia", "Responsable", "Estado (semáforo ex ante)"], rows,
    "*Nota.* Elaboración propia con datos de la ficha maestra del proyecto. El estado es un semáforo ex ante al 13 de octubre de 2026: refleja el riesgo de incumplimiento de la ficha "
    f"(alto {D.RIESGO['Alto']}, medio {D.RIESGO['Medio']}, bajo {D.RIESGO['Bajo']}) y no un avance medido. Naturaleza: PROPUESTO.")

# ------------------------------------------------------------------ t21 MGA preliminar
def fila_ind(campo, c):
    i = IND[c]
    return (campo, f"{c}: {i['nombre']}; meta final: {i['mf']}", c, f"{i['lb_nat']} (línea base); PROPUESTO (clasificación)")
mga = [
 ("Identificación del proyecto", f"{M.IDENT['titulo']} (caso {M.IDENT['caso']})", "—", "PROPUESTO"),
 ("Sector y subsector (OCDE)", M.IDENT["ocde"], "—", "PROPUESTO"),
 ("Localización geográfica", "Caldas, Cundinamarca y Valle del Cauca; 12 municipios, 4 por departamento [DATO_USUARIO: lista de municipios]", "PERS-R01, PERS-P01", "SUPUESTO"),
 ("Demanda territorial (código ID)", "[DATO_USUARIO: código ID de la demanda territorial del Anexo 4]", "PERS-S01, PERS-S02", "VACIO"),
 ("Entidades participantes y roles", "[DATO_USUARIO: nombres y roles de la entidad ejecutora, la empresa tecnológica, las alcaldías y la Unidad Nacional para la Gestión del Riesgo de Desastres]", "—", "VACIO"),
 ("Presupuesto estimado por fuente", f"SGR {D.cop(D.SGR)}; contrapartida {D.cop(D.CONTRA)}; total {D.cop(D.TOTAL)}", "PERS-R04", "CALCULADO"),
]
for c in ("PERS-P01", "PERS-P02", "PERS-P03", "PERS-P04"):
    mga.append(fila_ind("Productos esperados (tipificados MMG)", c)[:1] + (f"{c}: {IND[c]['nombre']}; {IND[c]['mmg']}; meta final: {IND[c]['mf']}", c, "PROPUESTO; MMG NO_VERIFICADO"))
for c in ("PERS-E01", "PERS-E02", "PERS-E03"):
    mga.append(fila_ind("Indicadores de resultado", c))
for c in ("PERS-S01", "PERS-S02"):
    mga.append(fila_ind("Indicadores de impacto", c))
for c in ("PERS-R01", "PERS-R02", "PERS-R03", "PERS-R04", "PERS-R05", "PERS-R06"):
    mga.append(fila_ind("Indicadores de gestión (campo no listado por el metaprompt)", c))
TABLAS["t21"] = bloque("t21", "Tabla MGA preliminar para transferencia al SIGP",
    ["Campo MGA preliminar", "Contenido propuesto", "Indicador PERS enlazado", "Naturaleza"], mga,
    "*Nota.* Elaboración propia con datos de la ficha maestra y con los campos de la tabla MGA preliminar del metaprompt GENESIS-CTeI. MGA: Metodología General Ajustada. "
    "La estructura del formulario web del SIGP y los códigos del catálogo de indicadores no se aportaron [DATO_USUARIO: códigos del catálogo vigente de la MGA y del SIGP]; "
    "la transferencia exige verificar cada campo (NO_VERIFICADO).")

# ------------------------------------------------------------------ t22 cronograma de medición
def hitos_en(a, b):
    out = []
    for h, d in D.HIT.items():
        if a < d["mes"] <= b:
            comp = {"H3": ", compuerta C1", "H5": ", compuerta C2", "H8": ", compuerta C3"}.get(h, "")
            out.append(f"{h} (mes {d['mes']}{comp})")
    return "; ".join(out) if out else "Sin hito"
assert [M.TRAMOS[k]["mes_compuerta"] for k in range(3)] == [12, 17, 24] and D.HIT["H3"]["mes"] == 12 and D.HIT["H5"]["mes"] == 17 and D.HIT["H8"]["mes"] == 24
rows = []
for q in range(8):
    a, b = 3 * q, 3 * q + 3
    anio = "Año 1" if b <= 12 else "Año 2"
    cort = f"R01 a R06 mensual; P01 a P04, E01 y E02 en el mes {b}"
    if b % 6 == 0: cort += "; E03"
    rep = "Tablero trimestral"
    if b % 6 == 0: rep = "Informe semestral y tablero trimestral"
    if b in (12, 17): pass
    if b == 12: rep += "; acta de compuerta C1; evaluación externa (S07)"
    if b == 18: rep += "; acta de compuerta C2 (mes 17)"
    if b == 24: rep += "; acta de cierre; evaluación externa final (S07)"
    rows.append((f"{anio}, trimestre {q + 1 if q < 4 else q - 3}", f"{a + 1} a {b}", cort, hitos_en(a, b), rep))
rows.append(("Posproyecto, semestre 1", "25 a 30", "S01 en el mes 30", "Sin hito", "Informe de evaluación externa posproyecto"))
rows.append(("Posproyecto, semestre 2", "31 a 36", "S01 y S02 en el mes 36", "Sin hito", "Informe final de evaluación externa posproyecto"))
TABLAS["t22"] = bloque("t22", "Cronograma de medición anual con hitos de reporte",
    ["Periodo", "Meses", "Cortes de medición", "Hitos y compuertas", "Reportes y verificación"], rows,
    "*Nota.* Elaboración propia con las frecuencias de la ficha maestra y los hitos H0 a H8. Los reportes al financiador siguen el calendario de los TdR [DATO_USUARIO: calendario de informes]. "
    "La medición posproyecto (meses 25 a 36) es PROPUESTO y su financiación es VACIO: la línea S07 cubre solo los meses 12 a 24.")

ORDEN_TABLAS = [f"t{k:02d}" for k in range(1, 23)]
assert sorted(TABLAS) == ORDEN_TABLAS

if __name__ == "__main__":
    for k in ORDEN_TABLAS:
        print(TABLAS[k][:160].replace("\n", " ¦ "))
    print(len(TABLAS))
