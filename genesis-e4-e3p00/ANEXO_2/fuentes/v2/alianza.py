# -*- coding: utf-8 -*-
"""Datos de la alianza (cinco integrantes, Anexo 3 v6), roles por actividad, beneficios y localización del presupuesto por municipio.
Se importa desde expand.py. Todas las cifras monetarias salen de m2."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m2
cop = pct = None  # los inyecta expand.py

# ---------------------------------------------------------------- integrantes (cinco integrantes; Gestión y Medio Ambiente es aliado del sector productivo)
ACTORES = ["IES", "MAN", "CAL", "AVA", "GMA"]
NOMBRE = {
    "IES": "Universidad Santo Tomás, sede Villavicencio",
    "MAN": "Municipio de Manizales",
    "CAL": "Municipio de Calarcá",
    "AVA": "Avanciencia",
    "GMA": "Gestión y Medio Ambiente",
}
NATURALEZA = {
    "IES": "Institución de educación superior; entidad proponente y ejecutora",
    "MAN": "Entidad territorial de Caldas; municipio afectado y lugar de ejecución",
    "CAL": "Entidad territorial de Quindío; municipio afectado y lugar de ejecución",
    "AVA": "Oficina de transferencia de resultados de investigación (OTRI); actor del SNCTI con reconocimiento de MinCiencias",
    "GMA": "Empresa de servicios de calidad del aire con domicilio en Manizales; aliado tecnológico del sector productivo",
}
# actividad: (USTA, Manizales, Calarcá, Avanciencia, Gestión y Medio Ambiente, actores de cambio, actores técnicos y proveedores)
R = {
 "1.1": ("Lidera el diseño de la colocalización, el mapeo diagnóstico y el plan de análisis", "Facilita el acceso a los sitios de Manizales y aporta los datos de afectación", "Facilita el acceso a los sitios de Calarcá y aporta los datos de afectación", "Ejecuta la vigilancia tecnológica y la asesoría jurídica de libertad de operación antes de la primera compra", "Aporta equipos de monitoreo y apoyo técnico al diagnóstico de los sitios de Manizales", "Consejos de gestión del riesgo de los dos municipios"),
 "1.2": ("Dirige la compra y caracteriza los nodos en el banco de calibración", "No participa", "No participa", "Revisa la libertad de operación de los nodos y de los cabezales", "No participa", "Proveedores de nodos, monitores de referencia y banco de calibración"),
 "1.3": ("Instala el tramo 1, opera la colocalización y mide la línea base", "Provee acceso y seguridad en los sitios de Manizales", "Provee acceso y seguridad en los sitios de Calarcá", "No participa", "Apoya la colocalización en Manizales con equipos y personal técnico", "Técnicos de campo y laboratorio acreditado"),
 "1.4": ("Entrena y valida el modelo de corrección", "Participa en la decisión de la compuerta C1", "Participa en la decisión de la compuerta C1", "Documenta el modelo de corrección como resultado protegible", "No participa", "Evaluador externo independiente"),
 "1.5": ("Reentrena y verifica el modelo por municipio", "Participa en la compuerta C2", "Participa en la compuerta C2", "No participa", "No participa", "Consejos de gestión del riesgo y custodios"),
 "1.6": ("Dirige la verificación final y el ensayo independiente", "Aporta registros de uso", "Aporta registros de uso", "Valora los resultados finales para su transferencia", "Apoya la verificación final en Manizales", "Laboratorio externo y evaluador independiente"),
 "1.7": ("Lidera la validación del gemelo predictivo con demoliciones reales", "Gestiona el acceso a las demoliciones de Manizales", "Gestiona el acceso a las demoliciones de Calarcá", "No participa", "No participa", "Responsables de obra, verificador independiente y servicio contratado de analítica geoespacial"),
 "1.8": ("Ejerce la gerencia, la dirección científica y la supervisión", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Supervisión del SGR"),
 "2.1": ("Lidera el diseño del enlace, de la energía y de la arquitectura de la plataforma", "Informa restricciones de los sitios", "Informa restricciones de los sitios", "No participa", "No participa", "Estudio de cobertura por municipio y servicio contratado de arquitectura geoespacial"),
 "2.2": ("Desarrolla el firmware, la ingesta y la corrección en el gateway, y dirige el servicio contratado de la plataforma geoespacial", "No participa", "No participa", "No participa", "No participa", "Proveedor de la plataforma geoespacial y auditor de ciberseguridad"),
 "2.3": ("Instala y mantiene el tramo 2", "Provee acceso y custodia local", "Provee acceso y custodia local", "No participa", "Aporta en efectivo la logística y los viáticos de la instalación del tramo 2", "Técnicos de campo"),
 "2.4": ("Instala y mantiene el tramo 3", "Provee acceso y custodia local", "Provee acceso y custodia local", "No participa", "Aporta en efectivo la logística y los viáticos de la instalación del tramo 3", "Técnicos de campo"),
 "2.5": ("Lidera el diseño del laboratorio y del inventario de emisión de demolición", "Informa las demoliciones previstas y aporta cartografía local", "Informa las demoliciones previstas y aporta cartografía local", "No participa", "No participa", "Laboratorio acreditado de caracterización del polvo"),
 "2.6": ("Dota el laboratorio y monta la cadena de modelación", "No participa", "No participa", "No participa", "No participa", "Proveedores de equipos con entrega en Colombia"),
 "2.7": ("Lidera la construcción y la calibración del gemelo predictivo", "No participa", "No participa", "No participa", "No participa", "Servicio de cartografía y proveedor de la plataforma geoespacial"),
 "2.8": ("Gestiona compras y conciliación", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Proveedores y revisoría fiscal"),
 "3.1": ("Aporta los coinvestigadores de ambiente y ciencias sociales y el profesional en calidad del aire, y diseña el tablero", "Convoca a su consejo de gestión del riesgo y a la comunidad", "Convoca a su consejo de gestión del riesgo y a la comunidad", "Coordina el co-diseño y la apropiación social con su equipo", "No participa", "Consejos de gestión del riesgo, comunidades vecinas y servicio contratado de diseño del tablero"),
 "3.2": ("Acompaña el uso del tablero y coordina su soporte técnico", "Lidera el registro de decisiones en Manizales", "Lidera el registro de decisiones en Calarcá", "Organiza las jornadas públicas, las cartillas y las publicaciones de divulgación", "No participa", "Consejos de gestión del riesgo"),
 "3.3": ("Diseña el contenido técnico de la formación y certifica a los custodios", "Firma el convenio de custodia", "Firma el convenio de custodia", "Forma a los custodios y estructura los convenios de custodia", "No participa", "Custodios designados"),
 "3.4": ("Entrega los bienes y evalúa el cierre", "Recibe la custodia local", "Recibe la custodia local", "Lidera la valoración, el registro de propiedad intelectual y la divulgación internacional", "No participa", "Custodios, evaluador independiente y proveedor de la plataforma geoespacial"),
 "3.5": ("Lidera el protocolo de evaluación previa y transfiere el laboratorio", "Adopta el protocolo en Manizales", "Adopta el protocolo en Calarcá", "Registra el software y los datos del modelo predictivo", "No participa", "Consejos, responsables de obra y verificador independiente"),
 "3.6": ("Gestiona eventos y logística", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Proveedores de logística"),
}
def actividades_de(actor):
    k = ACTORES.index(actor)
    out = []
    for a, v in R.items():
        t = v[k]
        if t.startswith("No participa") or t.startswith("Reporta su contrapartida"):
            continue
        out.append(a)
    return out

def _compacta(lista):
    return ", ".join(lista)

# ---------------------------------------------------------------- tablas
def t_roles_actividad():
    f = []
    for a in m2.ACTD.values():
        v = R[a["id"]]
        f.append((f"{a['id']} {a['nombre']}",) + v)
    return ("Roles de los integrantes de la alianza y de los actores de cambio por actividad",
            ["Actividad", NOMBRE["IES"], NOMBRE["MAN"], NOMBRE["CAL"], NOMBRE["AVA"], NOMBRE["GMA"], "Actores de cambio, actores técnicos y proveedores"], f,
            "*Nota.* Elaboración propia con la formulación del proyecto y el Anexo 3 v6. Una misma entidad no figura como integrante de la alianza y como beneficiaria. Los proveedores, los laboratorios y el evaluador externo no integran la alianza.")

def _por_oe(actor, oe):
    return [a for a in actividades_de(actor) if a.startswith(oe[2])]

LIDERA = {"IES": ["OE1", "OE2"], "MAN": ["OE3"], "CAL": ["OE3"], "AVA": [], "GMA": []}
APORTE = {
    "IES": "Coordina y ejecuta el proyecto; lidera la medición verificada, la red, la plataforma geoespacial con un servicio contratado y el laboratorio de modelación; forma al talento, produce los documentos de investigación y contrata a Avanciencia para la apropiación social y la transferencia",
    "MAN": "Asume la responsabilidad territorial en Manizales: acceso a sitios y demoliciones, convocatoria del consejo de gestión del riesgo, adopción de los protocolos y custodia local",
    "CAL": "Asume la responsabilidad territorial en Calarcá: acceso a sitios y demoliciones, convocatoria del consejo de gestión del riesgo, adopción de los protocolos y custodia local",
    "AVA": "Ejecuta la apropiación social del conocimiento y el componente de transferencia: co-diseño, jornadas, cartillas, formación de custodios, vigilancia tecnológica, valoración, propiedad intelectual y convenios de transferencia y custodia",
    "GMA": "Aporta equipos de monitoreo y apoyo técnico en Manizales para el diagnóstico, la colocalización y la verificación final, y la logística en efectivo de los tramos 2 y 3"
}

def _contrapartida_actor(actor):
    rows = [r for r in m2.CONTRA if r["fuente"] == actor]
    tot = sum(r["total"] for r in rows)
    efe = sum(r["total"] for r in rows if r["rubro"] == "Efectivo")
    esp = tot - efe
    if efe and esp:
        return f"{cop(efe)} en efectivo y {cop(esp)} en especie"
    return f"{cop(tot)} en {'efectivo' if efe else 'especie'}"

def t_roles_alianza():
    f = []
    for ac in ACTORES:
        lid = ", ".join(LIDERA[ac]) or "Ninguno"
        part = ", ".join(o for o in ("OE1", "OE2", "OE3") if _por_oe(ac, o) and o not in LIDERA[ac]) or "Ninguno"
        f.append((NOMBRE[ac], NATURALEZA[ac], lid, part, _compacta(actividades_de(ac)), APORTE[ac], _contrapartida_actor(ac)))
    return ("Integrantes de la alianza: naturaleza, objetivos, actividades, aporte y contrapartida",
            ["Integrante", "Naturaleza", "Objetivo que lidera", "Objetivos en que participa", "Actividades con función", "Qué aporta", "Contrapartida"], f,
            "*Nota.* Elaboración propia con los numerales 3 y 18 de los términos de referencia y el Anexo 3. Cada integrante asume al menos una actividad, designa un responsable institucional y aporta una contrapartida cuantificada, sujeta a la certificación de su representante legal.")

BENEF = [
 ("Universidad Santo Tomás",
  "Formación de nueve personas (seis jóvenes investigadores, dos estudiantes de maestría y un posdoctor) y nueve documentos de investigación; datos colocalizados y un modelo de corrección para su línea de investigación; experiencia en la operación de un laboratorio de modelación predictiva",
  "Productos 1 a 6 de la sección 20 e indicador R6",
  "La titularidad de los bienes adquiridos se fija en el certificado del numeral 10.19 y en el convenio de la alianza"),
 ("Municipios de Manizales y de Calarcá",
  "Tablero con índice local de calidad del aire y protocolo de alerta de su jurisdicción, con umbrales co-diseñados; personas funcionarias formadas como custodias; mediciones de PM2,5 y PM10 con error conocido en los sitios de remoción; evaluaciones previas de demolición para sus decisiones",
  "Indicadores R3, R5 y R7 de resultado e I1 e I2 de impacto",
  "Como integrantes de la alianza no figuran como beneficiarios; la custodia exige una partida de cada municipio"),
 ("Avanciencia",
  "Cartera de resultados para valorar y transferir; acuerdos de propiedad intelectual y de licencia; experiencia en transferencia de tecnologías de monitoreo ambiental; coautoría de los productos en que participa",
  "Productos 7, 8 y 9; actividades 1.1 y 3.1 a 3.5",
  "El valor de su contrapartida requiere la certificación de su representante legal"),
 ("Gestión y Medio Ambiente",
  "Datos colocalizados de su red en Manizales, protocolo de calibración verificado y experiencia en una red con error conocido; posibilidad de prestar servicios de mantenimiento o verificación a los custodios por contrato posterior",
  "Actividades 1.1, 1.3, 1.6, 2.3 y 2.4",
  "Sus aportes (110.000.000 COP en especie y 150.000.000 COP en efectivo) requieren la certificación de su representante legal"),
 ("Consejos de gestión del riesgo, operarios y comunidad vecina",
  "Alertas y decisiones con datos de error conocido; estimación previa de la exposición por polvo antes de una demolición y medidas de control sugeridas; cartillas del índice y del protocolo de alerta; mascarillas para el personal de campo; formación en el uso del tablero",
  "Indicadores R3 y R7 y productos 8 y 9",
  "La protección de las personas depende de que el consejo active el protocolo"),
]
def t_beneficios():
    return ("Qué recibe cada integrante y cada grupo de usuarios del proyecto",
            ["Integrante o grupo", "Qué recibe", "Cómo se verifica", "Condición"], [tuple(b) for b in BENEF],
            "*Nota.* Elaboración propia con la formulación del proyecto. Los beneficios son resultados técnicos, de capacidad y de uso. El proyecto no promete efectos en la salud ni retornos monetarios.")

# ---------------------------------------------------------------- localización del valor por municipio (solo la que declara el Anexo 3)
# Fracciones (Manizales, Calarcá) que el Anexo 3 v5 declara de forma expresa; el resto de cada partida es común a los dos municipios.
LOCAL = {
 "TH-12": (0.5, 0.5, "tres técnicos por municipio"),
 "EQ-18": (0.25, 0.25, "una estación por municipio; la de laboratorio y la móvil son comunes"),
 "ST-04": (0.5, 0.5, "un estudio por municipio"),
 "CA-04": (0.5, 0.5, "tres talleres por municipio"),
}
def localizar(r):
    if r["id"] in LOCAL:
        a, b, _ = LOCAL[r["id"]]
        man = int(round(r["total"] * a)); cal = int(round(r["total"] * b))
        return man, cal, r["total"] - man - cal
    return 0, 0, r["total"]

def por_municipio():
    """{rubro: [Manizales, Calarcá, común]} del SGR."""
    res = {k: [0, 0, 0] for k in m2.RUB}
    for r in m2.BUD:
        v = localizar(r)
        for i in range(3): res[r["rubro_tdr"]][i] += v[i]
    return res

def t_presupuesto_municipio():
    d = por_municipio()
    f = []; tot = [0, 0, 0]
    for rb, v in d.items():
        if sum(v) == 0: continue
        f.append((rb,) + tuple(cop(x) for x in v) + (cop(sum(v)),))
        for i in range(3): tot[i] += v[i]
    assert sum(tot) == m2.SGR
    f.append(("**Total**",) + tuple("**" + cop(x) + "**" for x in tot) + ("**" + cop(sum(tot)) + "**",))
    f.append(("Participación en el SGR",) + tuple(pct(x / m2.SGR) for x in tot) + ("100,0 %",))
    return ("Valor solicitado al SGR por rubro y municipio, según la localización que declara el Anexo 3",
            ["Rubro", "Manizales (Caldas)", "Calarcá (Quindío)", "Común a los dos municipios", "Total"], f,
            "*Nota.* Elaboración propia con el Anexo 3. Solo se asignan a un municipio las partidas cuya cantidad por municipio declara el Anexo 3: técnicos de campo (tres por municipio), estaciones meteorológicas (una por municipio), estudio de cobertura (uno por municipio) y talleres de evaluación previa (tres por municipio). Las demás partidas sirven a los dos municipios y no se reparten.")

def por_departamento():
    """Compatibilidad: {rubro: [Manizales, Calarcá, común, 0]}."""
    return {k: v + [0] for k, v in por_municipio().items()}

def nodos_por_municipio():
    return [50, 50]

TABLAS_ALIANZA = {
    "roles_actividad": t_roles_actividad,
    "roles_alianza": t_roles_alianza,
    "beneficios": t_beneficios,
    "presupuesto_departamento": t_presupuesto_municipio,
    "presupuesto_municipio": t_presupuesto_municipio,
}

# ---------------------------------------------------------------- registro de datos pendientes
import re, glob, collections
SEC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sec")
OWN = [
 (r"Avanciencia|actor del SNCTI|reconocimiento|transferencia", "Avanciencia"),
 (r"Manizales|Calarcá|municipio|alcald|gobernaci|plan municipal|plan departamental|departamental|declaratoria|calamidad|afectaci|DANE|población|poblaci|resguardo|consejo comunitario|centro poblado|reporte oficial|autoridad ambiental|comités|consejo|demanda|Anexo 4|operarios|remoción", "Municipios de Manizales y de Calarcá"),
 (r"cotizaci|presupuesto|valor", "Universidad Santo Tomás, con Avanciencia"),
]
def _owner(txt):
    low = txt.lower()
    for pat, o in OWN:
        if re.search(pat, txt, re.I): return o
    return "Universidad Santo Tomás"
def t_pendientes():
    d = collections.OrderedDict()
    for f in sorted(glob.glob(os.path.join(SEC, "s[0-9][0-9].md"))):
        n = int(re.search(r"s(\d\d)\.md", f).group(1))
        if n in (0, 29): continue
        tx = open(f, encoding="utf-8").read()
        for m in re.finditer(r"\[Diligenciar: ([^\]]+)\]", tx):
            if m.group(1).strip().lower() == "descripción del dato": continue
            d.setdefault(m.group(1).strip(), [])
            if n not in d[m.group(1).strip()]: d[m.group(1).strip()].append(n)
    f = []
    for txt, secs in sorted(d.items(), key=lambda kv: (kv[1][0], kv[0])):
        f.append((txt[0].upper() + txt[1:], ", ".join(str(s) for s in secs), _owner(txt)))
    return ("Datos pendientes del documento, secciones donde aparecen y responsable sugerido",
            ["Dato pendiente", "Secciones", "Responsable sugerido"], f,
            "*Nota.* Elaboración propia a partir de los marcadores verdes del documento. El total es de %d datos distintos. Cada dato se completa en el texto y se elimina el marcador antes de radicar." % len(f))
TABLAS_ALIANZA["pendientes"] = t_pendientes
