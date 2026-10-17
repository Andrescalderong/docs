# -*- coding: utf-8 -*-
"""Datos de la alianza (cuatro integrantes), roles por actividad, beneficios y presupuesto por departamento.
Se importa desde expand.py. Todas las cifras monetarias salen de m2."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m2
cop = pct = None  # los inyecta expand.py

# ---------------------------------------------------------------- integrantes
ACTORES = ["IES", "ENT", "SNCTI", "EMP"]
NOMBRE = {
    "IES": "Entidad proponente: universidad",
    "ENT": "Entidad aliada 1: municipio",
    "SNCTI": "Entidad aliada 2: actor del SNCTI",
    "EMP": "Entidad aliada 3: empresa tecnológica",
}
NATURALEZA = {
    "IES": "Institución de educación superior; entidad proponente y ejecutora",
    "ENT": "Entidad territorial: municipio de un departamento afectado, uno de los municipios de intervención",
    "SNCTI": "Actor del Sistema Nacional de Ciencia, Tecnología e Innovación con reconocimiento vigente de MinCiencias",
    "EMP": "Actor del sector productivo con domicilio en un departamento afectado",
}

# actividad: (IES, ENT, SNCTI, EMP, actores de cambio y proveedores)
R = {
 "1.1": ("Lidera el diseño y el plan de análisis", "Facilita el acceso a sitios y aporta datos de afectación", "Revisa el diseño metrológico de la colocalización", "Aporta datos de cobertura", "Comités de los municipios"),
 "1.2": ("Dirige la compra y recibe las referencias", "No participa", "Participa en la caracterización de los cabezales", "Entrega nodos y gateways", "Laboratorio acreditado"),
 "1.3": ("Opera la colocalización y mide la línea base", "Provee acceso y seguridad en los sitios", "No participa", "Instala nodos y gateways", "Técnicos de campo departamentales"),
 "1.4": ("Entrena y valida el modelo", "Participa en la decisión de la compuerta", "Valida el procedimiento metrológico", "Despliega el modelo en el gateway", "Evaluador externo independiente"),
 "1.5": ("Reentrena y verifica por departamento", "Participa en la compuerta y en los convenios", "No participa", "Mantiene la red", "Comités y custodios"),
 "1.6": ("Dirige la verificación final", "Aporta registros de uso", "Contrasta los resultados finales", "Entrega la versión congelada", "Laboratorio externo y evaluador independiente"),
 "1.7": ("Ejerce la gerencia y la supervisión", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Supervisión del SGR"),
 "2.1": ("Revisa el diseño", "Informa restricciones del sitio", "No participa", "Lidera el diseño del enlace y de la energía", "Estudio de cobertura"),
 "2.2": ("Define requisitos de calidad de datos", "No participa", "No participa", "Lidera el firmware, la nube y el tablero", "Auditor de ciberseguridad"),
 "2.3": ("Coordina la instalación", "Provee acceso y custodia local", "No participa", "Lidera la instalación y el mantenimiento", "Técnicos de campo departamentales"),
 "2.4": ("Coordina la instalación", "Provee acceso y custodia local", "No participa", "Lidera la instalación y el mantenimiento", "Técnicos de campo departamentales"),
 "2.5": ("Gestiona compras y conciliación", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Agente aduanero"),
 "3.1": ("Facilita el co-diseño", "Lidera la convocatoria de los comités", "No participa", "Adapta el tablero", "Comités de gestión del riesgo"),
 "3.2": ("Acompaña y evalúa el uso", "Lidera el registro de decisiones", "No participa", "Da soporte técnico", "Comités de gestión del riesgo"),
 "3.3": ("Diseña y certifica la formación", "Firma los convenios de custodia", "Participa en la formación de custodios", "Transfiere conocimiento técnico", "Custodios designados"),
 "3.4": ("Entrega y evalúa", "Recibe la custodia", "Asume la custodia científica del repositorio de datos", "Entrega la plataforma", "Custodios y evaluador independiente"),
 "3.5": ("Gestiona eventos y logística", "Reporta su contrapartida", "Reporta su contrapartida", "Reporta su contrapartida", "Proveedores de logística"),
}
# actividades en que cada integrante tiene una función real (no «No participa» ni solo reporte de contrapartida)
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
            ["Actividad", NOMBRE["IES"], NOMBRE["ENT"], NOMBRE["SNCTI"], NOMBRE["EMP"], "Actores de cambio y proveedores"], f,
            "*Nota.* Elaboración propia con la formulación del proyecto. Una misma entidad no figura como integrante de la alianza y como beneficiaria. Los proveedores y el evaluador externo no integran la alianza.")

def _por_oe(actor, oe):
    return [a for a in actividades_de(actor) if a.startswith(oe[2])]

LIDERA = {"IES": ["OE1"], "ENT": ["OE3"], "SNCTI": [], "EMP": ["OE2"]}
APORTE = {
    "IES": "Coordina el proyecto y lidera la medición verificada; forma al talento y produce los documentos de investigación",
    "ENT": "Facilita el acceso a los sitios, convoca a los comités y asume la custodia local de la red",
    "SNCTI": "Aporta la validación metrológica y la formación de custodios, y asume la custodia científica de los datos",
    "EMP": "Aporta nodos, gateways, firmware, nube y tablero, y mantiene la red",
}

def _contrapartida_actor(actor):
    rows = [r for r in m2.CONTRA if r["fuente"] == actor]
    if actor == "SNCTI":
        return "Especie: [Diligenciar: valor certificado del aporte]"
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
            "*Nota.* Elaboración propia con los numerales 3 y 18 de los términos de referencia y la formulación del proyecto. Cada integrante asume al menos una actividad, designa un responsable institucional y aporta una contrapartida cuantificada.")

BENEF = [
 ("Universidad proponente",
  "Formación de nueve personas (seis jóvenes investigadores, dos estudiantes de maestría y un posdoctor) y nueve documentos de investigación; datos colocalizados y un modelo de corrección para su línea de investigación; capacidad de medición durante el proyecto; titularidad de los resultados según la regla de propiedad intelectual",
  "Productos 2 a 6 de la sección 20",
  "La titularidad de los bienes adquiridos se fija en el convenio de la alianza"),
 ("Municipio aliado",
  "Tablero con índice local de calidad del aire y protocolo de alerta de su jurisdicción, con umbrales que el municipio co-diseña como integrante que lidera el uso institucional; personas funcionarias formadas y certificadas como custodias; mediciones de PM2,5 y PM10 con error conocido en los sitios de remoción de su territorio; custodia local de los componentes con partida por convenio",
  "Indicadores R3 y R5 de resultado e I1 e I2 de impacto",
  "Su comité municipal no se cuenta entre los 15 comités beneficiarios y se sustituye por otro de la misma jurisdicción; la custodia exige una partida del municipio"),
 ("Actor del SNCTI reconocido por MinCiencias",
  "Coautoría de los documentos de investigación; acceso a series colocalizadas y verificadas; fortalecimiento de su capacidad de metrología de aerosoles; custodia científica del repositorio de datos; registro de los productos de CTeI en que participa",
  "Productos 2 y 9; actividades 1.1, 1.2, 1.4, 1.6, 3.3 y 3.4",
  "El valor de su contrapartida está por certificar"),
 ("Empresa tecnológica",
  "Validación independiente de su tecnología hasta el TRL 8 con informe de laboratorio externo; datos de campo para mejorar su producto; derechos de explotación según el acuerdo de propiedad intelectual; oportunidad de ofrecer el servicio a otras entidades",
  "Informe del ensayo independiente (actividad 1.6) y acuerdo de propiedad intelectual",
  "La oferta a terceros es una oportunidad y no un compromiso del proyecto"),
 ("Comités de gestión del riesgo y operarios de remoción",
  "Alertas y decisiones con datos de error conocido; cartillas del índice y del protocolo de alerta; mascarillas de protección para el personal de campo; formación en el uso del tablero",
  "Indicador R3 y productos 8 y 9",
  "La protección de las personas depende de que el comité active el protocolo"),
]
def t_beneficios():
    return ("Qué recibe cada integrante y cada grupo de usuarios del proyecto",
            ["Integrante o grupo", "Qué recibe", "Cómo se verifica", "Condición"], [tuple(b) for b in BENEF],
            "*Nota.* Elaboración propia con la formulación del proyecto. Los beneficios son resultados técnicos, de capacidad y de uso. El proyecto no promete efectos en la salud ni retornos monetarios.")

# ---------------------------------------------------------------- presupuesto por departamento
DEPTOS = ("Caldas", "Cundinamarca", "Valle del Cauca")
K_NODOS = (33, 34, 33); K_GW = (3, 4, 3); K_SITIOS = (36, 38, 36); K_IGUAL = (1, 1, 1)
TERR = {
 "E01": K_NODOS, "E02": K_NODOS, "E05": K_NODOS, "M03": K_NODOS, "M06": K_NODOS, "M07": K_NODOS,
 "V01": K_NODOS, "V02": K_NODOS, "V03": K_NODOS,
 "S05": K_SITIOS, "E09": K_SITIOS,
 "E04": K_GW, "E06": K_GW, "E12": K_GW, "S10": K_GW,
 "E03": K_IGUAL, "M01": K_IGUAL, "S01": K_IGUAL, "S06": K_IGUAL, "P10": K_IGUAL,
 "V05": K_IGUAL, "O02": K_IGUAL, "M04": K_IGUAL, "M05": K_IGUAL, "S09": K_IGUAL,
}
def _repartir(total, clave):
    s = sum(clave); out = [int(round(total * k / s)) for k in clave]
    out[max(range(3), key=lambda i: clave[i])] += total - sum(out)
    return out

def por_departamento():
    """Devuelve {rubro: [caldas, cundinamarca, valle, transversal]} del SGR."""
    res = {k: [0, 0, 0, 0] for k in m2.RUB}
    for r in m2.BUD:
        rb = r["rubro_tdr"]
        if r["id"] in TERR:
            v = _repartir(r["total"], TERR[r["id"]])
            for i in range(3): res[rb][i] += v[i]
        else:
            res[rb][3] += r["total"]
    return res

def t_presupuesto_departamento():
    d = por_departamento()
    f = []; tot = [0, 0, 0, 0]
    for rb, v in d.items():
        if sum(v) == 0: continue
        f.append((rb,) + tuple(cop(x) for x in v) + (cop(sum(v)),))
        for i in range(4): tot[i] += v[i]
    assert sum(tot) == m2.SGR
    f.append(("**Total**",) + tuple("**" + cop(x) + "**" for x in tot) + ("**" + cop(sum(tot)) + "**",))
    f.append(("Participación en el SGR",) + tuple(pct(x / m2.SGR) for x in tot) + ("100,0 %",))
    return ("Valor solicitado al SGR por rubro y departamento",
            ["Rubro", "Caldas", "Cundinamarca", "Valle del Cauca", "Transversal", "Total"], f,
            "*Nota.* Elaboración propia, con valores calculados. Los gastos territoriales se reparten con claves explícitas: nodos operativos (33, 34 y 33) para nodos, cabezales, energía, mástiles, insumos y viajes; sitios (36, 38 y 36) para instalación y equipos de campo; gateways (3, 4 y 3) para gateways, enlaces y planes de datos; y partes iguales para monitores de referencia, gravimetría, estudios, técnicos de campo, formación y apropiación. Los gastos transversales sirven a los tres departamentos y no se reparten.")

def nodos_por_depto():
    return list(K_NODOS)

TABLAS_ALIANZA = {
    "roles_actividad": t_roles_actividad,
    "roles_alianza": t_roles_alianza,
    "beneficios": t_beneficios,
    "presupuesto_departamento": t_presupuesto_departamento,
}

# ---------------------------------------------------------------- registro de datos pendientes
import re, glob, collections
SEC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sec")
OWN = [
 (r"actor del SNCTI|reconocimiento", "Actor del SNCTI"),
 (r"empresa|RUES|razón social de la empresa", "Empresa tecnológica"),
 (r"municipio|alcald|gobernaci|plan municipal|plan departamental|departamental|declaratoria|calamidad|afectaci|DANE|población|poblaci|resguardo|consejo comunitario|centro poblado|reporte oficial|autoridad ambiental|comités|comité de gestión|demanda|Anexo 4|operarios|remoción", "Municipio aliado y entidades territoriales"),
 (r"cotizaci|presupuesto|valor", "Universidad, con la empresa y el actor del SNCTI"),
]
def _owner(txt):
    low = txt.lower()
    for pat, o in OWN:
        if re.search(pat, txt, re.I): return o
    return "Universidad"
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
