# -*- coding: utf-8 -*-
"""Presupuesto aprobado del Anexo 3 v5 (libro Anexo3_Conv56_POLVO-L51-PM_v5.xlsx): partidas con código, rubro, cantidad, unidad,
valor unitario, fuentes, actividad principal y meses de ejecución. Es la fuente única del presupuesto del Anexo 2 desde la versión v5."""
import json, os, re
D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data_v6")
PART = json.load(open(os.path.join(D, "partidas.json"), encoding="utf-8"))
CRONO = json.load(open(os.path.join(D, "cronofin.json"), encoding="utf-8"))
RUBRO = {"R01": "Talento Humano", "R02": "Equipos y software", "R03": "Capacitación y eventos", "R04": "Servicios tecnológicos y pruebas",
         "R05": "Materiales, insumos y documentación", "R06": "Protección del conocimiento y divulgación", "R07": "Infraestructura",
         "R08": "Gastos de viaje", "R09": "Administrativos", "R10": "Seguimiento", "R11": "Otros"}
ENT = {"USTA": "IES", "Manizales": "MAN", "Calarcá": "CAL", "Avanciencia": "AVA", "GyMA": "GMA", "DreamGIS": "DGI"}
RESP = {"E1": "IES", "E2": "MAN", "E3": "CAL", "E4": "AVA", "E5": "GMA"}   # DGI: aportes sin aportante (SIN_APORTANTE)
# Decisiones de la alianza del 29 de octubre de 2026: Avanciencia reemplaza a Cientech y Asociados. DreamGIS S.A.S. sale de la alianza;
# Gestión y Medio Ambiente (Manizales) participa solo como actor técnico externo. Las partidas de servicios de la plataforma geoespacial
# se conservan como servicios por contratar; los dos aportes de DreamGIS (EQ-13 en especie y VI-05 en efectivo) quedan sin aportante.
SIN_APORTANTE = set()   # Anexo 3 v6: Gestión y Medio Ambiente es la Entidad 5 y aporta EQ-13 (especie) y VI-05 (efectivo)
import re as _re
def ren(s):
    if not isinstance(s, str): return s
    s = s.replace("Cientech y Asociados", "Avanciencia").replace("Cientech", "Avanciencia")
    s = s.replace("de DreamGIS S.A.S.", "del proveedor cotizado").replace("de DreamGIS", "del proveedor cotizado")
    s = s.replace("(DreamGIS)", "(servicio contratado)").replace("DreamGIS S.A.S.", "el proveedor cotizado").replace("DreamGIS", "el proveedor cotizado")
    return s

def _txt(p):
    return " ".join(str(v) for v in p["campos"].values() if isinstance(v, str))

def _unidad_cant(p):
    c = p["campos"]; t = _txt(p); rub = p["rubro"]
    if rub == "R01":
        n = c.get("CANT") or 1; sem = c.get("SEMANAS") or 0
        if "Matrícula" in p["item"]: return "matrícula", n
        if p["sgr"] == 0: return "aporte", 1
        meses = round(sem * 12 / 52)
        return "persona-mes", n * meses
    if rub == "R08":
        u = {"VI-01": "trayecto", "VI-02": "día-persona", "VI-03": "día", "VI-04": "viaje", "VI-06": "trayecto", "VI-07": "día-persona", "VI-08": "día", "VI-05": "aporte"}[p["id"]]
        q = (c.get("No. De Viajes") or 1) * (c.get("No de personas") or 1) * (c.get("No de días") or 1)
        return u, (1 if u == "aporte" else q)
    if p["id"] == "AD-01" or p["id"] == "SE-01": return "mes", 24
    if p["id"] == "IN-01": return "sitio", 110
    if p["id"] == "CA-05": return "misión", 15
    if c.get("UNIDAD DE MEDIDA"): return c["UNIDAD DE MEDIDA"], c.get("CANTIDAD") or 1
    m = re.search(r"([\d.,]+) ([\wáéíóúñ-]+(?:-[\wáéíóúñ]+)?) × (?:valor unitario )?\$", t)
    q = c.get("CANTIDAD") or c.get("CANTIDAD REQUERIDA") or c.get("Cantidad") or 1
    u = m.group(2) if m else "unidad"
    if p["sgr"] == 0 and p["rubro"] == "R02": u = "aporte"
    return u, q

def partidas():
    out = []
    for p in PART:
        u, q = _unidad_cant(p)
        tot = p["total"]
        out.append(dict(id=p["id"], rubro_tdr=RUBRO[p["rubro"]], concepto=ren(p["item"]), unidad=u, cant=q,
                        vunit=(tot / q if q else tot), total=tot, sgr=p["sgr"], m_ini=p["ini"], m_fin=p["fin"],
                        act=p["act"][1:], perfil=p["tipo"], texto=ren(_txt(p)), resp=RESP.get(p.get("resp"), "IES"),
                        contra={ENT[k.split()[0]] + ("_EF" if "efectivo" in k else "_ES"): v for k, v in p["fuentes_contra"].items()}))
    return out

def mensual_por_item():
    """Valor mensual por partida (meses 1 a 24), tomado del cronograma financiero del Anexo 3."""
    out = {}
    for r in CRONO:
        k = ren(r["item"]); out.setdefault(k, [0.0] * 24)
        for i, v in enumerate(r["mensual"]): out[k][i] += v
    return out
