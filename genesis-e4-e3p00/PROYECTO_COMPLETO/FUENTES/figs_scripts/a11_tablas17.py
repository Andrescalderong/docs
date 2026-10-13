# -*- coding: utf-8 -*-
"""Tablas del capítulo 17 (Equipo de Trabajo), generadas desde maestro.py mediante a11_datos.py. Cada función devuelve el bloque :::TABLA completo."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11_datos as D
from a11_datos import cel, num, mm

def bloque(id_, titulo, enc, filas, nota):
    out = [f":::TABLA {id_} | {titulo}", "| " + " | ".join(enc) + " |", "| " + " | ".join("---" for _ in enc) + " |"]
    for f in filas:
        assert len(f) == len(enc), (id_, f)
        out.append("| " + " | ".join(cel(c) for c in f) + " |")
    out.append(":::NOTA " + nota)
    return "\n".join(out)

def etc(x):
    return num(x, 1)

RESP = {
    "P01": "Apoyan la colocalización, el análisis de datos y la documentación del piloto.",
    "P02": "Desarrollan tesis sobre el modelo de corrección y su validación frente a la referencia.",
    "P03": "Diseña, entrena y valida el modelo de corrección que se ejecuta en los gateways.",
    "P04": "Instalan, configuran y operan nodos y gateways; uno de ellos coordina WP2.",
    "P05": "Coordina la apropiación social y el co-diseño con los comités de gestión del riesgo.",
    "P06": "Gerencia el alcance, el cronograma, el presupuesto y la preparación de las compuertas.",
    "P07": "Responde por la trazabilidad frente a la referencia gravimétrica y firma la validación.",
    "P08": "Construyen la plataforma en la nube, el gemelo digital y el tablero.",
    "P09": "Diseña el firmware y la energía para 14 días de autonomía sin sol.",
    "P10": "Instalan, mantienen y reponen equipos en campo; dos técnicos por departamento.",
    "P11": "Facilitan talleres de co-diseño y acompañan a los comités en el uso del tablero.",
    "P12": "Desarrolla la estimación espacial del gemelo digital y valida sus resultados.",
    "P13": "Define con los comités los umbrales locales del índice y el protocolo de alerta.",
    "P14": "Gestiona los convenios por tramo, la cláusula de apertura y la propiedad intelectual.",
    "C01": "Dirige la ejecución científica, representa al proyecto y preside el comité técnico.",
    "C02": "Coordina WP1 y la validación de la corrección frente a la referencia.",
    "C03": "Asesoran el análisis de ambiente y salud ambiental y el co-diseño con ciencias sociales.",
}

def rol_nombre(p):
    import re
    return re.sub(r"\s*\(\d+\)\s*$", "", p["concepto"])

def t17_roles():
    filas = []
    for p in D.PERS:
        filas.append([p["id"], rol_nombre(p), str(p["n"]), p["wp"], RESP[p["id"]], etc(p["etc"]), f"{p['ini']} a {p['fin']}", p["nat"]])
    filas.append(["Total SGR", f"{len(D.PERS)} perfiles", str(D.N_PERS), "WP0 a WP3", f"{D.PM_TOT} persona-mes; {etc(D.ETC_PROM)} ETC promedio en 24 meses", "—", "1 a 24", "CALCULADO"])
    for p in D.CPERS:
        filas.append([p["id"], rol_nombre(p) + " (IES)", str(p["n"]), p["wp"], RESP[p["id"]], etc(p["etc"]), f"{p['ini']} a {p['fin']}", p["nat"]])
    filas.append(["Total IES", "3 perfiles", str(D.N_CPERS), "WP0, WP1, WP3", f"{etc(D.ETC_CPERS)} ETC en 24 meses", "—", "1 a 24", "CALCULADO"])
    return bloque("t01", "Matriz de roles y responsabilidades del equipo",
                  ["Línea", "Rol", "Personas", "Paquete", "Responsabilidad principal (PROPUESTO)", "ETC por persona", "Meses", "Naturaleza"], filas,
                  "*Nota.* Elaboración propia con las líneas P01 a P14 del presupuesto y C01 a C03 de la contrapartida (maestro.py). ETC: equivalente de tiempo completo, calculado como persona-mes ÷ (personas × meses de vigencia). La naturaleza corresponde a la línea; las responsabilidades son PROPUESTO. Decimales con coma.")

PERFIL = {
    "C01": ("Ingeniería electrónica, ambiental o afín", "Dirección de proyectos que llevaron un desarrollo de laboratorio a entorno operativo"),
    "C02": ("Ingeniería electrónica, de telecomunicaciones, estadística o afín", "Validación de sensores frente a referencia con R², NRMSE, pendiente y sesgo"),
    "C03": ("Ciencias ambientales, salud ambiental y ciencias sociales", "Diseño participativo con instituciones y análisis de gestión del riesgo"),
    "P01": ("Ingeniería, estadística, ciencias ambientales o afín", "Procesamiento de series de sensores y registro de bitácoras de campo"),
    "P02": ("Posgrado en ingeniería, estadística o ciencias ambientales", "Tesis sobre el modelo de corrección o la validación con datos del proyecto"),
    "P03": ("Estadística, ciencia de datos o ingeniería", "Modelos de corrección con validación cruzada por departamento y partición temporal"),
    "P04": ("Ingeniería electrónica o de telecomunicaciones", "Instalación de redes LoRa con gateways, energía solar y enlace celular o satelital"),
    "P05": ("Ciencias sociales, comunicación o gestión del riesgo", "Facilitación de talleres de co-diseño y actas con comunidades e instituciones"),
    "P06": ("Ingeniería, administración o afín, con formación en gerencia de proyectos", "Control de alcance, cronograma, presupuesto y compuertas con informes de seguimiento"),
    "P07": ("Metrología, química, física o ingeniería", "Trazabilidad frente a la referencia gravimétrica y manejo del banco de calibración"),
    "P08": ("Ingeniería de sistemas o de software", "Plataformas en la nube, bases de series temporales y tableros con pruebas de seguridad"),
    "P09": ("Ingeniería electrónica o mecatrónica", "Firmware de bajo consumo y dimensionamiento solar para 14 días sin sol"),
    "P10": ("Formación técnica o tecnológica en electrónica o telecomunicaciones", "Instalación, mantenimiento y reposición de nodos en sitios de remoción con trabajo seguro"),
    "P11": ("Ciencias sociales, comunicación o educación", "Talleres de co-diseño con comités y materiales para comunidades"),
    "P12": ("Geografía, estadística, ingeniería o afín", "Estimación espacial de PM2,5 y PM10 y validación del gemelo digital"),
    "P13": ("Ingeniería ambiental, salud ambiental o afín", "Índice de calidad del aire y salud con umbrales locales y protocolo de alerta"),
    "P14": ("Derecho, administración pública o afín", "Convenios por tramo, cláusula de apertura y titularidad de propiedad intelectual"),
}
POR_SELECCION = {"P01", "P02", "P10"}

def t17_perfiles():
    filas = []
    orden = ["C01", "C02", "C03"] + [p["id"] for p in D.PERS]
    nom = {p["id"]: rol_nombre(p) for p in D.PERS}
    nom.update({"C01": "Investigador principal (IES)", "C02": "Coinvestigador técnico (IES)", "C03": "Coinvestigadores de ambiente y ciencias sociales (IES)"})
    for k in orden:
        a, c = PERFIL[k]
        per = "[DATO_USUARIO: nombre y hoja de vida o proceso de selección]" if k in POR_SELECCION else "[DATO_USUARIO: nombre y hoja de vida]"
        filas.append([f"{k} {nom[k]}", a, c, per])
    return bloque("t02", "Perfiles requeridos y hojas de vida resumidas por aportar",
                  ["Rol", "Área de formación requerida (PROPUESTO)", "Competencia verificable (PROPUESTO)", "Persona y hoja de vida"], filas,
                  "*Nota.* Elaboración propia con los roles de maestro.py. Cada fila describe un perfil requerido y no una persona. Los niveles de formación y los años de experiencia mínimos dependen de los términos de referencia (VACIO) y de cada hoja de vida.")

def t17_grupos():
    filas = [
        ["Calibración y metrología de partículas", "Metrología de sensores ópticos de bajo costo", "[DATO_USUARIO: nombre y código del grupo]", "[DATO_USUARIO: categoría vigente]", "Banco de calibración, colocalización y trazabilidad (WP1)", "P07, C02, C04, E03, E07"],
        ["Modelado y ciencia de datos", "Aprendizaje automático y estadística espacial aplicados a calidad del aire", "[DATO_USUARIO: nombre y código del grupo]", "[DATO_USUARIO: categoría vigente]", "Modelo de corrección y gemelo digital (WP1 y WP2)", "P03, P12, E08"],
        ["Sistemas embebidos, energía y comunicaciones", "Redes de sensores LoRa, energía solar y cómputo en el borde", "[DATO_USUARIO: nombre y código del grupo]", "[DATO_USUARIO: categoría vigente]", "Nodos, gateways, energía y enlace (WP2)", "P04, P09, P10, E01 a E06"],
        ["Calidad del aire y salud ambiental", "Exposición a material particulado y umbrales de alerta", "[DATO_USUARIO: nombre y código del grupo]", "[DATO_USUARIO: categoría vigente]", "Umbrales locales del índice y protocolo de alerta (WP3)", "P13, C03"],
        ["Gestión del riesgo y apropiación social", "Gestión del riesgo de desastres, co-diseño y apropiación del conocimiento", "[DATO_USUARIO: nombre y código del grupo]", "[DATO_USUARIO: categoría vigente]", "Co-diseño, formación y convenios de custodia (WP3)", "P05, P11, P14, C03"],
    ]
    return bloque("t03", "Caracterización de las capacidades de investigación y de los grupos por vincular",
                  ["Capacidad requerida", "Línea de investigación requerida (PROPUESTO)", "Grupo vinculado", "Categoría MinCiencias", "Rol en el proyecto", "Líneas del presupuesto asociadas"], filas,
                  "*Nota.* Elaboración propia. Las capacidades y las líneas son PROPUESTO. Los grupos concretos y sus categorías son datos que solo el usuario posee y no se afirman en este documento.")

def t17_alianzas():
    ser = sum(D.B[i]["total"] for i in ("S01", "S07", "S08"))
    filas = [
        ["IES ejecutora [DATO_USUARIO: nombre de la entidad]", "Co-ejecutor (SUPUESTO)", "Ejecución legal, dirección científica y laboratorios (C01 a C04)", mm(D.CONTRA_IES), "Especie", "Total DECLARADO; desglose de C03 y C04 PROPUESTO", "Certificación de la IES"],
        ["Empresa tecnológica [DATO_USUARIO: razón social]", "Co-ejecutor (SUPUESTO)", "Nube, propiedad intelectual y código, logística de emergencia (C05 y C06)", mm(D.CONTRA_EMP), f"{mm(D.CONTRA_EMP_EF)} efectivo y {mm(D.CONTRA_EMP_ES)} especie", "DECLARADO", "Carta, certificación y acuerdo de titularidad"],
        ["Alcaldías de 12 municipios [DATO_USUARIO: lista de municipios]", "Aliado de uso y custodio potencial", "Sus comités usan el tablero y asumen la custodia por tramo", "0,0", "Sin aporte", "VACIO", "Cartas con partida y competencia"],
        ["Gobernaciones y unidades departamentales de gestión del riesgo", "Aliado de uso y custodio potencial", "Tres comités departamentales y custodia potencial", "0,0", "Sin aporte", "NO_VERIFICADO", "Cartas de compromiso"],
        ["UNGRD y puestos de mando unificado", "Aliado de uso", "Reciben información y aplican el protocolo de alerta", "0,0", "Sin aporte", "INFERIDO", "Carta de aceptación del protocolo"],
        ["IDEAM y autoridades ambientales", "Referencia metrológica", "Punto de referencia para la colocalización", "0,0", "Sin aporte", "INFERIDO", "Convenio de referencia"],
        ["Laboratorio acreditado, laboratorio externo y evaluación externa", "Proveedores de servicio, no aliados", "Gravimetría (S01), ensayo independiente (S08) y evaluación (S07)", "0,0", f"{mm(ser)} con cargo al SGR", "DECLARADO y PROPUESTO", "Cotización y alcance de acreditación"],
        ["Total de contrapartida", "—", "—", mm(D.CONTRA_TOT), f"{mm(D.CONTRA_EMP_EF)} efectivo y {mm(D.CONTRA_ESPECIE)} especie", "CALCULADO", "—"],
    ]
    return bloque("t04", "Matriz de alianzas y aportes",
                  ["Entidad", "Vínculo", "Rol en el proyecto", "Aporte (M COP)", "Forma", "Naturaleza", "Soporte pendiente"], filas,
                  "*Nota.* Elaboración propia con la contrapartida de maestro.py (C01 a C06) y los actores de 4.4-MDR.5. La alianza empresa-IES es SUPUESTO por instrucción del usuario. M COP: millones de pesos colombianos. Decimales con coma.")

def todas():
    return {"t01": t17_roles(), "t02": t17_perfiles(), "t03": t17_grupos(), "t04": t17_alianzas()}

if __name__ == "__main__":
    for k, v in todas().items():
        print(v[:600]); print("...")
