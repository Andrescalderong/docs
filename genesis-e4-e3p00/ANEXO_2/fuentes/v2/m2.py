# -*- coding: utf-8 -*-
"""LIBRO MAESTRO v2 del Anexo 2: ajusta el libro maestro del proyecto (maestro.py) a los términos de referencia (TdR v1.6)
que se aportaron después de la corrida anterior. Fuente única de cifras del Anexo 2.
Cada ajuste se registra en AJUSTES con su fundamento en los TdR. Valores monetarios en pesos colombianos (enteros)."""
import sys, os, copy, math, collections
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/maestro")
import maestro as M0
import indicadores as I0

M = M0.M
L = M0.L

# ------------------------------------------------------------------ IDENTIDAD
IDENT = dict(M0.IDENT)
IDENT["titulo"] = ("Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo "
                   "por material particulado posterremoto en Caldas, Cundinamarca y Valle del Cauca")
IDENT["proceso"] = "Implementación"
IDENT["objeto"] = "red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto"
IDENT["localizacion"] = "Caldas, Cundinamarca y Valle del Cauca"
IDENT["trl_final"] = 8
IDENT["trl_piso"] = 7
IDENT["fecha_corte"] = "15 de octubre de 2026"
IDENT["fecha_cierre_conv"] = "3 de noviembre de 2026"
IDENT["linea_principal"] = "5.1. Ciencia, tecnología e innovación para la gestión anticipada del riesgo y la seguridad de las regiones"
IDENT["tope_cop"] = 14_000_000_000
assert len(IDENT["titulo"]) <= 256, len(IDENT["titulo"])

# ------------------------------------------------------------------ RUBROS DEL TdR (numeral 12.2)
RUB = ["Talento Humano", "Equipos y software", "Capacitación y eventos", "Servicios tecnológicos y pruebas",
       "Materiales, insumos y documentación", "Protección del conocimiento y divulgación", "Gastos de viaje",
       "Infraestructura", "Administrativos", "Seguimiento", "Otros"]
RUBRO_DE = {  # línea del libro anterior -> rubro del TdR
    **{f"P{n:02d}": "Talento Humano" for n in range(1, 15)}, "P02a": "Talento Humano", "P02b": "Talento Humano",
    **{f"E{n:02d}": "Equipos y software" for n in range(1, 12)},
    "E12": "Servicios tecnológicos y pruebas", "S10": "Servicios tecnológicos y pruebas",
    "S01": "Servicios tecnológicos y pruebas", "S03": "Servicios tecnológicos y pruebas", "S06": "Servicios tecnológicos y pruebas",
    "S07": "Servicios tecnológicos y pruebas", "S08": "Servicios tecnológicos y pruebas",
    "S05": "Infraestructura",
    "S09": "Capacitación y eventos", "O02": "Capacitación y eventos", "V05": "Capacitación y eventos",
    "S02": "Protección del conocimiento y divulgación", "O03": "Protección del conocimiento y divulgación",
    "O01": "Protección del conocimiento y divulgación", "O06": "Protección del conocimiento y divulgación", "M04": "Protección del conocimiento y divulgación",
    **{f"M{n:02d}": "Materiales, insumos y documentación" for n in (1, 2, 3, 5, 6, 7)},
    "V01": "Gastos de viaje", "V02": "Gastos de viaje", "V03": "Gastos de viaje", "V04": "Gastos de viaje",
    "S11": "Administrativos", "O05a": "Administrativos", "O05b": "Seguimiento",
}

# ------------------------------------------------------------------ PRESUPUESTO SGR v2
AJUSTES = []
def ajuste(id_, tema, antes, despues, base):
    AJUSTES.append(dict(id=id_, tema=tema, antes=antes, despues=despues, base=base))

BUD = []
for r in M0.BUDGET:
    i = r["id"]
    if i == "X01":
        ajuste("AJ-01", "Reserva de contingencia", "636.000.000 COP como rubro del SGR",
               "Se elimina como rubro; el riesgo se atiende con unidades de reserva, compuertas y programación",
               "El numeral 12.2 no contempla la reserva como rubro y el numeral 14.3 exige justificar cada rubro con cotizaciones")
        continue
    if i == "S04":
        ajuste("AJ-02", "Póliza todo riesgo de equipos", "50.000.000 COP en servicios técnicos", "Se elimina del SGR",
               "El numeral 14.3 excluye los seguros del apoyo del SGR")
        continue
    if i == "O04":
        ajuste("AJ-03", "Pólizas y garantías", "60.000.000 COP en otros rubros", "Se elimina del SGR",
               "El numeral 14.3 excluye los seguros del apoyo del SGR")
        continue
    if i == "P03":
        r = dict(r); r.update(concepto="Doctor en estancia posdoctoral (1)", cant=24, vunit=12_920_000, total=24 * 12_920_000, nat="DOCUMENTADO",
                 just="Estancia posdoctoral de 24 meses con el monto del numeral 14.4 de los TdR; asesora a jóvenes y maestrantes y lidera el modelo de corrección.")
        ajuste("AJ-04", "Científico de datos senior (480.000.000 COP)", "24 persona-mes a 20.000.000 COP",
               "Doctor en estancia posdoctoral: 24 meses a 12.920.000 COP (310.080.000 COP)",
               "El numeral 9 exige un doctor en estancia posdoctoral y el numeral 14.4 fija su valor mensual")
    if i == "P01":
        r = dict(r); r.update(nat="DOCUMENTADO", just="Seis jóvenes investigadores e innovadores, estudiantes de pregrado, 12 meses cada uno a 2.000.000 COP (numeral 14.4); dos cohortes de tres.")
    if i == "P02":
        a = dict(r); a.update(id="P02a", concepto="Sostenimiento de estudiantes de maestría (2)", cant=48, vunit=4_350_000, total=48 * 4_350_000, nat="DOCUMENTADO",
                              just="Sostenimiento de 24 meses a 4.350.000 COP por estudiante (numeral 14.4).")
        b = dict(r); b.update(id="P02b", concepto="Matrícula de maestría en modalidad de investigación (2)", unidad="matrícula", cant=2, vunit=48_000_000,
                              total=2 * 48_000_000, nat="DOCUMENTADO", just="Matrícula hasta 48.000.000 COP por estudiante (numeral 14.4).")
        assert a["total"] + b["total"] == r["total"]
        BUD += [a, b]; continue
    if i == "O05":
        a = dict(r); a.update(id="O05a", concepto="Administración del proyecto (gastos administrativos y revisoría)", cant=24, vunit=7_000_000, total=24 * 7_000_000, nat="PROPUESTO",
                              just="Gastos administrativos del proyecto; no incluye porcentajes automáticos.")
        b = dict(r); b.update(id="O05b", concepto="Apoyo a la supervisión y plataforma de seguimiento", cant=24, vunit=8_000_000, total=24 * 8_000_000, nat="PROPUESTO",
                              just="Profesional de seguimiento técnico y financiero y plataforma de seguimiento; estimación por perfil y dedicación (numeral 19.1).")
        assert a["total"] + b["total"] == r["total"]
        ajuste("AJ-05", "Administración (360.000.000 COP en otros rubros)", "Un solo rubro de administración",
               "Se separa en Administrativos (168.000.000 COP) y Seguimiento (192.000.000 COP), con el mismo total",
               "Los numerales 12.2 y 14.3 exigen el rubro Seguimiento para la vigilancia del proyecto")
        BUD += [a, b]; continue
    BUD.append(dict(r))
for r in BUD:
    r["rubro_tdr"] = RUBRO_DE[r["id"]]

# ------------------------------------------------------------------ CONTRAPARTIDA v2 (cada integrante aporta, numeral 3)
CONTRA = [dict(r) for r in M0.CONTRA]
CONTRA.append(L("C07", "Personal (especie)", "Municipio aliado: profesionales de gestión del riesgo y logística de acceso a sitios", "mes", 24, 5_000_000,
                "ENT", "PROPUESTO", "WP3", 1, 24,
                "Tres profesionales al 20 % durante 24 meses y apoyo logístico; valor sujeto a certificación del municipio aliado."))
ajuste("AJ-06", "Contrapartida de la entidad territorial", "Sin aporte (VACIO)", "120.000.000 COP en especie (PROPUESTO, pendiente de certificación)",
       "El numeral 3 exige que cada integrante de la alianza aporte una contrapartida cuantificada en términos monetarios")

# ------------------------------------------------------------------ ACTIVIDADES v2 (17) con semanas del CPM
# id Anexo 2, id CPM, nombre, OE
ACT = [
 ("1.1", "A1.1", "Seleccionar los sitios y diseñar la colocalización", "OE1"),
 ("1.2", "A1.2", "Adquirir y caracterizar el lote 1 de nodos y las referencias", "OE1"),
 ("1.3", "A1.3", "Instalar el tramo 1, colocalizar y calibrar en el piloto", "OE1"),
 ("1.4", "A1.4", "Entrenar y validar el modelo de corrección y decidir en la compuerta C1", "OE1"),
 ("1.5", "A1.5", "Reentrenar y verificar por departamento el tramo 2 y decidir en la compuerta C2", "OE1"),
 ("1.6", "A1.6", "Verificar el desempeño final y ejecutar el ensayo independiente", "OE1"),
 ("1.7", None,   "Administración y apoyo a la supervisión (objetivo específico 1)", "OE1"),
 ("2.1", "A2.1", "Diseñar la arquitectura de enlace y energía", "OE2"),
 ("2.2", "A2.2", "Desarrollar el firmware y la plataforma base (gemelo digital y tablero)", "OE2"),
 ("2.3", "A2.3", "Instalar el tramo 2", "OE2"),
 ("2.4", "A2.4", "Instalar el tramo 3", "OE2"),
 ("2.5", None,   "Administración y apoyo a la supervisión (objetivo específico 2)", "OE2"),
 ("3.1", "A3.1", "Co-diseñar los umbrales y el protocolo de alerta con los comités", "OE3"),
 ("3.2", "A3.2", "Poner en uso el tablero con los comités", "OE3"),
 ("3.3", "A3.3", "Formar custodios y firmar los convenios por tramo", "OE3"),
 ("3.4", "A3.4", "Transferir, cerrar y evaluar", "OE3"),
 ("3.5", None,   "Administración y apoyo a la supervisión (objetivo específico 3)", "OE3"),
]
ACTD = collections.OrderedDict((a[0], dict(id=a[0], cpm=a[1], nombre=a[2], oe=a[3])) for a in ACT)
SEM_MES = 52 / 12
def mes_ini(sem): return int(math.floor(sem / SEM_MES + 1e-9)) + 1
def mes_fin(sem): return int(math.ceil(sem / SEM_MES - 1e-9))
# ventana de semanas por actividad (incluye las compuertas C1 y C2 cuando se adjuntan)
for k, a in ACTD.items():
    if a["cpm"]:
        c = M0.ACTS[a["cpm"]]; es, ef = c["ES"], c["EF"]
        if k == "1.4": ef = M0.ACTS["C1"]["EF"]
        if k == "1.5": ef = M0.ACTS["C2"]["EF"]
        a.update(es=es, ef=ef, holgura=c["holgura"], critica=(c["holgura"] == 0))
    else:
        a.update(es=0, ef=M0.DURACION_SEMANAS, holgura=0, critica=False)
    a["m_ini"] = mes_ini(a["es"]) if a["es"] > 0 else 1
    a["m_fin"] = min(24, mes_fin(a["ef"]))

# ------------------------------------------------------------------ ASIGNACIÓN DEL PRESUPUESTO A ACTIVIDADES
def dur(k): return max(1, ACTD[k]["ef"] - ACTD[k]["es"])
def por_duracion(keys):
    t = sum(dur(k) for k in keys); return {k: dur(k) / t for k in keys}
OE1 = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"]; OE2 = ["2.1", "2.2", "2.3", "2.4"]; OE3 = ["3.1", "3.2", "3.3", "3.4"]
ADM = ["1.7", "2.5", "3.5"]
TERCIOS = {k: 1 / 3 for k in ADM}
TR = {"1.2": 36 / 120, "2.3": 48 / 120, "2.4": 36 / 120}   # por tramo de compra de nodos (36, 48, 36)
TRG = {"1.2": 4 / 11, "2.3": 4 / 11, "2.4": 3 / 11}        # gateways comprados (4, 4, 3)
SIT = {"1.3": 33 / 110, "2.3": 44 / 110, "2.4": 33 / 110}  # sitios por tramo
VIAJE = {"1.3": .30, "2.3": .25, "2.4": .20, "3.1": .10, "3.2": .075, "3.3": .075}
ALLOC = {
 "P01": por_duracion(OE1), "P02a": por_duracion(OE1), "P02b": por_duracion(OE1), "P03": por_duracion(OE1), "P07": por_duracion(OE1),
 "P04": por_duracion(OE2), "P08": por_duracion(OE2), "P09": por_duracion(OE2), "P10": por_duracion(OE2), "P12": por_duracion(OE2),
 "P05": por_duracion(OE3), "P11": por_duracion(OE3), "P13": por_duracion(OE3), "P14": por_duracion(OE3),
 "P06": TERCIOS,
 "E01": TR, "E02": {"1.2": 50 / 150, "2.3": 50 / 150, "2.4": 50 / 150}, "E03": {"1.2": 1.0}, "E04": TRG, "E05": TR,
 "E06": {"1.3": .3, "2.3": .4, "2.4": .3}, "E07": {"1.2": 1.0}, "E08": {"1.4": 1.0}, "E09": {"1.3": 1.0},
 "E10": {"2.2": 1.0}, "E11": {"2.2": 1.0}, "E12": {"1.3": .3, "2.3": .4, "2.4": .3}, "S10": {"1.3": .3, "2.3": .4, "2.4": .3},
 "M01": {"1.3": .6, "1.6": .4}, "M02": {"1.2": .5, "1.3": .5}, "M03": TR, "M04": {"3.2": .6, "3.3": .4}, "M05": {"3.1": 1.0},
 "M06": SIT, "M07": {"2.3": .5, "2.4": .5},
 "S01": {"1.3": .5, "1.5": .2, "1.6": .3}, "S02": {"3.4": 1.0}, "S03": {"2.2": .5, "2.4": .5}, "S05": SIT, "S06": {"2.1": 1.0},
 "S07": {"1.4": .5, "3.4": .5}, "S08": {"1.6": 1.0}, "S09": {"3.3": 1.0}, "S11": {"1.2": 1 / 3, "2.3": 1 / 3, "2.4": 1 / 3},
 "V01": VIAJE, "V02": VIAJE, "V03": VIAJE, "V04": {"3.4": 1.0}, "V05": {"3.1": 1.0},
 "O01": {"1.6": 1.0}, "O02": {"3.2": 4 / 9, "3.3": 3 / 9, "3.4": 2 / 9}, "O03": {"3.4": 1.0}, "O05a": TERCIOS, "O05b": TERCIOS,
 "O06": {"3.2": .4, "3.4": .6},
}
CALLOC = {  # contrapartida
 "C01": TERCIOS, "C02": por_duracion(OE1), "C03": por_duracion(OE3), "C04": por_duracion(OE1),
 "C05": {"2.3": .5, "2.4": .5}, "C06": {"2.2": 1.0}, "C07": por_duracion(OE3),
}
def repartir(total, shares):
    """Reparte un total entero según proporciones; el residuo va a la mayor participación (suma exacta)."""
    ks = list(shares); out = {k: int(round(total * shares[k])) for k in ks}
    dif = total - sum(out.values())
    kmax = max(ks, key=lambda k: shares[k]); out[kmax] += dif
    return out
for r in BUD:
    assert abs(sum(ALLOC[r["id"]].values()) - 1) < 1e-9, r["id"]
    r["por_act"] = repartir(r["total"], ALLOC[r["id"]])
for r in CONTRA:
    assert abs(sum(CALLOC[r["id"]].values()) - 1) < 1e-9, r["id"]
    r["por_act"] = repartir(r["total"], CALLOC[r["id"]])
for a in ACTD.values():
    a["sgr"] = sum(r["por_act"].get(a["id"], 0) for r in BUD)
    a["contra"] = sum(r["por_act"].get(a["id"], 0) for r in CONTRA)
    a["total"] = a["sgr"] + a["contra"]

# ------------------------------------------------------------------ TOTALES Y CONTROLES
def total(rows): return sum(r["total"] for r in rows)
SGR = total(BUD); CON = total(CONTRA); TOTAL = SGR + CON
CON_EFECTIVO = sum(r["total"] for r in CONTRA if r["rubro"] == "Efectivo")
POR_RUBRO = collections.OrderedDict((k, sum(r["total"] for r in BUD if r["rubro_tdr"] == k)) for k in RUB)
assert sum(POR_RUBRO.values()) == SGR
assert sum(a["sgr"] for a in ACTD.values()) == SGR and sum(a["contra"] for a in ACTD.values()) == CON
POR_OE = {oe: dict(sgr=sum(a["sgr"] for a in ACTD.values() if a["oe"] == oe), contra=sum(a["contra"] for a in ACTD.values() if a["oe"] == oe)) for oe in ("OE1", "OE2", "OE3")}
TRANSFER = sum(r["total"] for r in BUD if r["id"] in ("S09", "S02", "O03"))
MOVILIDAD = sum(r["total"] for r in BUD if r["id"] == "V04")
assert TRANSFER >= 0.01 * TOTAL, (TRANSFER, TOTAL)
assert MOVILIDAD <= 0.02 * SGR
assert CON_EFECTIVO >= 0.01 * SGR
assert SGR <= IDENT["tope_cop"]

def cop(n): return "$ " + f"{int(round(n)):,}".replace(",", ".")
def pct(x, d=1): return f"{x * 100:.{d}f}".replace(".", ",") + " %"
def mm(n, d=1):
    s = f"{n / M:,.{d}f}"; return s.replace(",", "X").replace(".", ",").replace("X", ".")

# flujo semestral SGR
def flujo(rows, months=24):
    f = [0.0] * months
    for r in rows:
        if r["id"] in ("E01", "E02", "E04", "E05", "M03", "S11"):
            # compras por tramo en el mes de compra
            continue
        n = r["m_fin"] - r["m_ini"] + 1
        for m in range(r["m_ini"], r["m_fin"] + 1): f[m - 1] += r["total"] / n
    for r in rows:
        if r["id"] in ("E01", "E02", "E04", "E05", "M03", "S11"):
            sh = {"E01": ("compra_nodos", r["vunit"]), "E02": ("compra_cabezales", r["vunit"]), "E04": ("compra_gw", r["vunit"]),
                  "E05": ("compra_nodos", r["vunit"]), "M03": ("compra_nodos", r["vunit"])}
            for t in M0.TRAMOS:
                mes = t["mes_compra"]
                if r["id"] in sh: f[mes - 1] += t[sh[r["id"]][0]] * sh[r["id"]][1]
                else: f[mes - 1] += r["total"] / 3  # S11 importación: un tercio por lote
    return f
FLUJO_SGR = flujo(BUD)
assert abs(sum(FLUJO_SGR) - SGR) < 1, (sum(FLUJO_SGR), SGR)
def por_periodo(f, size): return [sum(f[i:i + size]) for i in range(0, len(f), size)]
FLUJO_SEM = por_periodo(FLUJO_SGR, 6)
FLUJO_CON_SEM = por_periodo(M0.flujo(CONTRA), 6)

# ------------------------------------------------------------------ RIESGOS v2 (tipos del formato del Anexo 2)
def nivel_prob(p): return "Probable" if p >= 40 else ("Improbable" if p >= 20 else "Raro")
def nivel_imp(i): return "Mayor" if i >= 4 else ("Moderado" if i == 3 else "Menor")
TIPO = {"Técnico": "Operacionales", "Organizacional": "Operacionales", "Externo": "Operacionales", "Financiero": "Financieros",
        "Jurídico": "Legales", "Datos": "Operacionales"}
RIESGOS = []
for (id_, cat, desc, causa, P, I, prob, imp, est, resp, own, trig) in M0.RIESGOS:
    tipo = TIPO[cat]
    if id_ == "R-FIN-01": tipo = "De costos"
    RIESGOS.append(dict(id=id_, cat=cat, tipo=tipo, desc=desc, P=P, I=I, prob=prob, imp=imp, estrategia=est, respuesta=resp, resp=own, disparador=trig,
                        n_prob=nivel_prob(prob), n_imp=nivel_imp(I)))
RIESGOS_NUEVOS = [
 dict(id="R-ADM-01", cat="Administrativo", tipo="Administrativos", desc="La contratación del equipo y la firma de los convenios de ejecución se demoran más de ocho semanas.",
      P=3, I=4, prob=30, imp=0, estrategia="Mitigar", respuesta="Convenio marco previo con la IES y la empresa, plan de contratación con lista de elegibles y seguimiento semanal de la gerencia.",
      resp="Gerencia de proyecto", disparador="Equipo sin contratar al finalizar la semana 8", n_prob="Improbable", n_imp="Mayor"),
 dict(id="R-CAL-01", cat="Calendario", tipo="De calendario", desc="La importación y la nacionalización de un lote de equipos exceden doce semanas.",
      P=3, I=4, prob=35, imp=0, estrategia="Mitigar", respuesta="Importación por lote con anticipación de la orden, agente aduanero contratado y lote de reserva de cabezales en el país.",
      resp="Gerencia de proyecto", disparador="Lote sin nacionalizar a la semana 10 de su orden", n_prob="Improbable", n_imp="Mayor"),
 dict(id="R-SAN-01", cat="Sanitario", tipo="Sanitarios", desc="El personal de campo se expone al polvo y a los escombros durante la instalación y el mantenimiento.",
      P=3, I=3, prob=30, imp=0, estrategia="Mitigar", respuesta="Protocolo de seguridad y salud con respiradores N95, inducción previa y ventanas de trabajo fuera de la remoción activa.",
      resp="Ingenieros IoT y de campo", disparador="Incidente de salud reportado o sitio sin protocolo firmado", n_prob="Improbable", n_imp="Moderado"),
]
RIESGOS += RIESGOS_NUEVOS
# riesgos que cambian por los ajustes de los TdR
for r in RIESGOS:
    if r["id"] == "R-TEC-04": r["resp"] = "Analista de datos espaciales y gemelo digital"
    if r["id"] == "R-FIN-01":
        r["respuesta"] = "Compra por tramo con cotizaciones vigentes, orden de compra anticipada y cobertura cambiaria del proveedor; la contrapartida en efectivo cubre variaciones menores."
    if r["id"] == "R-EXT-02":
        r["estrategia"] = "Mitigar"
        r["respuesta"] = "Cerramientos y mástiles protegidos, custodia local por sitio, 20 nodos y 1 gateway de reserva y convenio de custodia con el municipio aliado."
    if r["id"] == "R-EXT-01":
        r["respuesta"] = "Instalación en ventanas secas, técnicos locales y holgura en las actividades 1.1, 3.1, 3.2 y 3.3; las instalaciones de los tramos 2 y 3 se programan con acceso previamente verificado."

# ------------------------------------------------------------------ TALENTO HUMANO (numeral 9)
TALENTO = [
 dict(cat="Joven investigador e innovador (pregrado)", n=6, dur=12, mensual=2_000_000, total=6 * 12 * 2_000_000, linea="P01",
      cohortes="Cohorte A: meses 1 a 12 (3 personas). Cohorte B: meses 13 a 24 (3 personas).",
      productos="Un artículo en formato publicable en revista A1, A2, B o C de Publindex y un producto de divulgación pública de la ciencia por persona."),
 dict(cat="Estudiante de maestría en modalidad de investigación", n=2, dur=24, mensual=4_350_000, total=2 * (24 * 4_350_000 + 48_000_000), linea="P02a y P02b",
      cohortes="Dos personas, meses 1 a 24; matrícula hasta 48.000.000 COP por persona.",
      productos="Un producto tipo TOP o tipo A sometido o publicado y un producto de divulgación pública de la ciencia por persona."),
 dict(cat="Doctor en estancia posdoctoral", n=1, dur=24, mensual=12_920_000, total=24 * 12_920_000, linea="P03",
      cohortes="Una persona, meses 1 a 24, sin vínculo laboral con las entidades de la alianza.",
      productos="Un producto tipo TOP o tipo A, un producto de divulgación pública de la ciencia y un informe técnico final."),
]
assert sum(t["total"] for t in TALENTO) == sum(r["total"] for r in BUD if r["id"] in ("P01", "P02a", "P02b", "P03"))

# ------------------------------------------------------------------ PRODUCTOS (MGA, sector 39, programa 3906)
PRODUCTOS = [
 dict(n=1, oe="OE1", programa="3906", producto="Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos",
      medido="Prototipos validados en condiciones reales", indicador="Prototipos funcionales validados (red de nodos y gateways con modelo de corrección)", unidad="Número", meta="1 sistema de 100 nodos y 10 gateways",
      act=["1.2", "1.3", "1.4", "1.5", "1.6", "2.3", "2.4"], resp="IES ejecutora y empresa tecnológica"),
 dict(n=2, oe="OE1", programa="3906", producto="Documentos de investigación",
      medido="Documentos de investigación elaborados", indicador="Documentos de investigación elaborados (6 de jóvenes, 2 de maestría y 1 de posdoctorado)", unidad="Número", meta="9",
      act=["1.6", "3.4"], resp="IES ejecutora"),
 dict(n=3, oe="OE1", programa="3906", producto="Servicio de apoyo financiero para la formación de maestría ya sea nacional o en el exterior, en la modalidad de investigación",
      medido="Personas apoyadas con formación de maestría", indicador="Estudiantes de maestría en modalidad de investigación apoyados", unidad="Número", meta="2",
      act=["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"], resp="IES ejecutora"),
 dict(n=4, oe="OE1", programa="3906", producto="Servicio de apoyo financiero de estancias de investigación",
      medido="Estancias de investigación apoyadas", indicador="Doctores con estancia posdoctoral apoyados", unidad="Número", meta="1",
      act=["1.3", "1.4", "1.6"], resp="IES ejecutora"),
 dict(n=5, oe="OE1", programa="3906", producto="Servicio de apoyo financiero para el fortalecimiento de las vocaciones científicas en CTI",
      medido="Jóvenes investigadores e innovadores apoyados", indicador="Jóvenes investigadores e innovadores apoyados con beca-pasantía", unidad="Número", meta="6",
      act=["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"], resp="IES ejecutora"),
 dict(n=6, oe="OE2", programa="3906", producto="Servicio de apoyo financiero para programas y proyectos de infraestructura científica y tecnológica",
      medido="Infraestructura científica y tecnológica dotada", indicador="Equipos y plataforma de medición dotados y en operación (3 referencias, 100 nodos, 10 gateways y plataforma)", unidad="Número", meta="1 infraestructura integrada",
      act=["2.1", "2.2", "2.3", "2.4"], resp="IES ejecutora y empresa tecnológica"),
 dict(n=7, oe="OE3", programa="3906", producto="Documentos de política: Documentos de planeación",
      medido="Documentos de planeación elaborados", indicador="Documentos de planeación elaborados (protocolo de alerta y plan de sostenibilidad con convenios de custodia)", unidad="Número", meta="2",
      act=["3.1", "3.3", "3.4"], resp="IES ejecutora y municipio aliado"),
 dict(n=8, oe="OE3", programa="3906", producto="Servicio de apropiación social del conocimiento",
      medido="Actividades de apropiación social realizadas", indicador="Estrategias y actividades de apropiación social del conocimiento realizadas (20 talleres de co-diseño y 9 jornadas)", unidad="Número", meta="29",
      act=["3.1", "3.2", "3.3", "3.4"], resp="IES ejecutora y municipio aliado"),
 dict(n=9, oe="OE3", programa="3906", producto="Servicio de Asistencia Técnica",
      medido="Personas y entidades asistidas técnicamente", indicador="Personas de comités y custodios certificadas en el uso y la custodia de la red", unidad="Número", meta="60 personas y 15 comités",
      act=["3.2", "3.3", "3.4"], resp="IES ejecutora y empresa tecnológica"),
]
for p in PRODUCTOS:
    p["sgr"] = sum(ACTD[k]["sgr"] for k in p["act"]); p["contra"] = sum(ACTD[k]["contra"] for k in p["act"])

# ------------------------------------------------------------------ HITOS
HITOS = [dict(id=h[0], desc=h[1], mes=h[2], verif=h[3]) for h in M0.HITOS]
HITOS.append(dict(id="C3", desc="Compuerta C3: cierre y transferencia con evidencia del TRL 8", mes=24,
                  verif="Informe de evaluación final con el desempeño de los 100 nodos y acta de entrega a custodios"))

# ------------------------------------------------------------------ INDICADORES DE GESTIÓN
INFORMES = [3, 6, 9, 12, 15, 18, 21, 24]

# ------------------------------------------------------------------ RESUMEN
def resumen():
    return dict(sgr=SGR, contra=CON, total=TOTAL, contra_efectivo=CON_EFECTIVO, pct_tope=SGR / IDENT["tope_cop"], holgura=IDENT["tope_cop"] - SGR,
                transfer=TRANSFER, pct_transfer=TRANSFER / TOTAL, movilidad=MOVILIDAD, pct_mov=MOVILIDAD / SGR, pct_efectivo=CON_EFECTIVO / SGR,
                por_rubro=POR_RUBRO, por_oe=POR_OE)

if __name__ == "__main__":
    r = resumen()
    print("SGR", cop(SGR), "| contrapartida", cop(CON), "(efectivo", cop(CON_EFECTIVO) + ") | total", cop(TOTAL))
    print("tope %", pct(r["pct_tope"], 2), "| holgura", cop(r["holgura"]), "| transferencia", cop(TRANSFER), pct(r["pct_transfer"], 2), "| movilidad", pct(r["pct_mov"], 2), "| efectivo/SGR", pct(r["pct_efectivo"], 2))
    for k, v in POR_RUBRO.items(): print(f"  {k:48s} {cop(v):>20s} {pct(v / SGR):>8s}")
    print("por OE", {k: (cop(v['sgr']), cop(v['contra'])) for k, v in POR_OE.items()})
    for a in ACTD.values(): print(a["id"], f"M{a['m_ini']}-M{a['m_fin']}", cop(a["sgr"]), cop(a["contra"]), "crit" if a["critica"] else "", a["nombre"][:60])
    print("flujo sem", [mm(x) for x in FLUJO_SEM], "contra", [mm(x) for x in FLUJO_CON_SEM])
    print("productos", [(p["n"], cop(p["sgr"])) for p in PRODUCTOS])
    print("riesgos", len(RIESGOS), [(x["id"], x["tipo"], x["n_prob"], x["n_imp"]) for x in RIESGOS])

# ------------------------------------------------------------------ INDICADORES DE PRODUCTO Y DE RESULTADO
IND_PROD = [
 dict(n=1, prod="Servicio de apoyo para la generación de prototipos de materiales, productos o dispositivos", ind="Prototipos funcionales validados", unidad="Número",
      meta="1 sistema de 100 nodos y 10 gateways: 30 y 3 al mes 12; 70 y 7 al mes 17; 100 y 10 al mes 19", resp="IES ejecutora y empresa tecnológica", periodo="Meses 4 a 24",
      evidencia="Inventario con coordenadas y número de serie; informes de validación frente a la referencia (R² ≥ 0,70 y NRMSE ≤ 30 %); informe del ensayo independiente", territorio="12 municipios de Caldas, Cundinamarca y Valle del Cauca"),
 dict(n=2, prod="Documentos de investigación", ind="Documentos de investigación elaborados", unidad="Número",
      meta="9: seis de jóvenes investigadores, dos de maestría y uno de posdoctorado; al menos 2 sometidos a revistas Q1 o Q2", resp="IES ejecutora", periodo="Meses 6 a 24",
      evidencia="Manuscritos con constancia de sometimiento o publicación", territorio="Tres departamentos"),
 dict(n=3, prod="Servicio de apoyo financiero para la formación de maestría ya sea nacional o en el exterior, en la modalidad de investigación", ind="Estudiantes de maestría apoyados", unidad="Número",
      meta="2", resp="IES ejecutora", periodo="Meses 1 a 24", evidencia="Certificados de admisión o matrícula, avance del trabajo de grado y producto TOP o tipo A sometido", territorio="Tres departamentos"),
 dict(n=4, prod="Servicio de apoyo financiero de estancias de investigación", ind="Doctores con estancia posdoctoral apoyados", unidad="Número",
      meta="1", resp="IES ejecutora", periodo="Meses 1 a 24", evidencia="Contrato o beca, producto TOP o tipo A, producto de divulgación e informe técnico final", territorio="Tres departamentos"),
 dict(n=5, prod="Servicio de apoyo financiero para el fortalecimiento de las vocaciones científicas en CTI", ind="Jóvenes investigadores e innovadores apoyados", unidad="Número",
      meta="6: tres en los meses 1 a 12 y tres en los meses 13 a 24", resp="IES ejecutora", periodo="Meses 1 a 24", evidencia="Contratos de beca-pasantía, CvLAC actualizado, artículo en formato publicable y producto de divulgación por persona", territorio="Tres departamentos"),
 dict(n=6, prod="Servicio de apoyo financiero para programas y proyectos de infraestructura científica y tecnológica", ind="Infraestructura de medición dotada y en operación", unidad="Número",
      meta="1 infraestructura integrada: 3 monitores de referencia, banco de calibración, 100 nodos, 10 gateways y plataforma", resp="IES ejecutora y empresa tecnológica", periodo="Meses 2 a 19",
      evidencia="Actas de recibo, inventario con huella de configuración y registro fotográfico", territorio="12 municipios"),
 dict(n=7, prod="Documentos de política: Documentos de planeación", ind="Documentos de planeación elaborados", unidad="Número",
      meta="2: protocolo de alerta co-diseñado con los comités y plan de sostenibilidad con convenios de custodia", resp="IES ejecutora y municipio aliado", periodo="Meses 3 a 24",
      evidencia="Documentos adoptados por acta de cada comité y convenios de custodia firmados", territorio="15 comités de gestión del riesgo"),
 dict(n=8, prod="Servicio de apropiación social del conocimiento", ind="Actividades de apropiación social del conocimiento realizadas", unidad="Número",
      meta="29: 20 talleres de co-diseño y 9 jornadas públicas", resp="IES ejecutora y municipio aliado", periodo="Meses 3 a 24", evidencia="Actas, listas de asistencia y piezas producidas con las comunidades", territorio="12 municipios"),
 dict(n=9, prod="Servicio de Asistencia Técnica", ind="Personas certificadas y comités asistidos", unidad="Número",
      meta="60 personas certificadas y 15 comités asistidos", resp="IES ejecutora y empresa tecnológica", periodo="Meses 6 a 24", evidencia="Certificados de formación y actas de asistencia técnica", territorio="15 comités de gestión del riesgo"),
]
IND_RES = [
 dict(cod="R1", nombre="Error de medición frente a la referencia en los tres tramos", formula="NRMSE y R² de cada nodo corregido frente al monitor de referencia colocalizado", lb="Se mide en el tramo 1 (mes 12)", meta="R² ≥ 0,70 y NRMSE ≤ 30 % en 100 nodos al mes 24", nivel="Resultado"),
 dict(cod="R2", nombre="Disponibilidad mensual de nodos", formula="Horas con dato válido ÷ horas del mes", lb="0 %", meta="≥ 90 % y pérdida de paquetes ≤ 10 % al mes 24", nivel="Resultado"),
 dict(cod="R3", nombre="Uso institucional del tablero y del protocolo", formula="Comités con al menos una decisión documentada por trimestre ÷ comités focalizados × 100", lb="Sin uso documentado", meta="≥ 75 % al mes 24", nivel="Resultado"),
 dict(cod="R4", nombre="Reducción relativa de falsas alarmas", formula="1 − (tasa del periodo ÷ tasa medida en el tramo 1)", lb="Se mide en el tramo 1", meta="≥ 30 % de reducción relativa", nivel="Resultado"),
 dict(cod="R5", nombre="Capacidad instalada en custodios", formula="Personas certificadas en el uso y la custodia de la red", lb="0", meta="≥ 60 personas certificadas", nivel="Resultado"),
 dict(cod="I1", nombre="Activación del protocolo ante superación de umbral", formula="Activaciones documentadas ÷ superaciones de umbral × 100", lb="Sin protocolo", meta="≥ 80 % a los 12 meses posteriores al cierre", nivel="Impacto"),
 dict(cod="I2", nombre="Continuidad de la red bajo custodia", formula="Nodos operativos bajo custodia ÷ nodos entregados × 100", lb="0", meta="≥ 70 % a los 12 meses posteriores al cierre", nivel="Impacto"),
]
