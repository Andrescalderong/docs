# -*- coding: utf-8 -*-
"""Matriz de correspondencia del presupuesto (Anexo 3 v7) con el Anexo 2, la MGA y el SIGP.
Uso: python3 build/matriz_v7.py salida.xlsx"""
import sys, os, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "v2"))
import v5, m2, alianza
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

P = v5.partidas()
import openpyxl as _ox
_wb = _ox.load_workbook('/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/in33/anexo3_v7.xlsx', data_only=True)
SOP = {r[0]: (r[2], r[5]) for r in _wb['C. Soportes y pendientes'].iter_rows(min_row=2, values_only=True) if r[0]}
ACT = m2.ACTD
PROD = {p["n"]: p for p in m2.PRODUCTOS}
ENT = {"IES": "Universidad Santo Tomás, sede Villavicencio", "MAN": "Municipio de Manizales", "CAL": "Municipio de Calarcá",
       "AVA": "Avanciencia", "GMA": "Gestión y Medio Ambiente"}
RESP_ACT = {"1.1": "Investigador principal", "1.2": "Especialista en metrología y calibración", "1.3": "Técnicos de campo y especialista en metrología",
            "1.4": "Analista de datos espaciales e ingenieros de software", "1.5": "Especialista en metrología", "1.6": "Especialista en metrología y evaluador externo",
            "1.7": "Investigador líder en modelación", "1.8": "Gerencia del proyecto", "2.1": "Ingeniero de firmware y energía",
            "2.2": "Ingenieros de software y nube", "2.3": "Técnicos de campo", "2.4": "Técnicos de campo", "2.5": "Investigador líder en modelación",
            "2.6": "Investigador líder en modelación", "2.7": "Investigador líder en modelación", "2.8": "Gerencia del proyecto",
            "3.1": "Coordinación de apropiación social (Avanciencia)", "3.2": "Coordinación de apropiación social (Avanciencia)", "3.3": "Profesional de convenios y custodia (Avanciencia)",
            "3.4": "Avanciencia, con la gerencia del proyecto", "3.5": "Investigador líder en modelación", "3.6": "Gerencia del proyecto"}
INSUMO_MGA = {"Talento Humano": "Mano de obra calificada", "Equipos y software": "Maquinaria y equipo; software",
              "Capacitación y eventos": "Servicios de capacitación y eventos", "Servicios tecnológicos y pruebas": "Servicios técnicos",
              "Materiales, insumos y documentación": "Materiales e insumos", "Protección del conocimiento y divulgación": "Servicios de propiedad intelectual y divulgación",
              "Gastos de viaje": "Transporte y viáticos", "Infraestructura": "Obra menor (instalación)", "Administrativos": "Gastos administrativos",
              "Seguimiento": "Servicios de seguimiento"}
SIN_FIN = [a for a in ACT if ACT[a]["sgr"] == 0 and ACT[a]["contra"] == 0]

def productos(p):
    t = p["texto"]
    n = sorted({int(x) for x in re.findall(r"\bP(\d)\b", t)} | {int(x) for x in re.findall(r"producto (\d)", t)})
    n = [x for x in n if x in PROD]
    if n:
        return "; ".join(f"P{x}. {PROD[x]['producto']}" for x in n), "Anexo 3"
    n = [k for k, v in PROD.items() if p["act"] in v["act"]]
    return "; ".join(f"P{x}. {PROD[x]['producto']}" for x in n), "Por actividad (Tabla 15.1)"

def municipio(p):
    if p["id"] in alianza.LOCAL:
        a, b, nota = alianza.LOCAL[p["id"]]
        man, cal = round(p["total"] * a), round(p["total"] * b)
        com = p["total"] - man - cal
        return f"Manizales {m2.cop(man)}; Calarcá {m2.cop(cal)}" + (f"; común {m2.cop(com)}" if com else "") + f" ({nota})"
    if p["id"] in ("EQ-01", "EQ-02", "EQ-04", "EQ-05", "MA-03", "IN-01"):
        return "Común; despliegue propuesto de 50 nodos y 5 gateways por municipio (sin localización en el Anexo 3)"
    return "Común a Manizales y Calarcá (sin localización en el Anexo 3)"

def fuente(p):
    if p["contra"]:
        k, v = next(iter(p["contra"].items()))
        ent, mod = k.split("_")
        modal = "efectivo" if mod == "EF" else "especie"
        if p["id"] in v5.SIN_APORTANTE:
            return f"Contrapartida en {modal} sin aportante vigente (excluida del total)", ENT[ent]
        return f"Contrapartida en {modal}", ENT[ent]
    if p.get("resp") == "AVA":
        return "SGR, Asignación para la CTeI", "Avanciencia (ejecuta por contrato con la universidad)"
    return "SGR, Asignación para la CTeI", "Universidad Santo Tomás (ejecutora)"

def ubic_a2(p):
    u = []
    if p["contra"]:
        u.append("Tablas 26.2 y 28.7 (contrapartida)")
    else:
        u.append("Tabla 30.3 (líneas del SGR)")
    if p["rubro_tdr"] == "Equipos y software" and not p["contra"]:
        u.append("Tabla 7.4 (equipos)")
    u.append(f"Tabla 15.2 (actividad {p['act']}); Tabla 28.3 (rubro)")
    if p["id"] in alianza.LOCAL:
        u.append("Tablas 15.3 y 28.5 (municipio)")
    if p["id"] in m2.TRANSFER_IDS if hasattr(m2, "TRANSFER_IDS") else p["id"] in ("CA-01", "PD-02", "PD-04", "CA-04", "PD-06"):
        u.append("Tabla 18.5 (Plan de transferencia)")
    if p["act"] in ("3.1", "3.2", "3.3", "3.4"):
        u.append("Tabla 19.4 (apropiación social)")
    return "; ".join(u)

def obs(p):
    o = []
    t = p["texto"]
    if p["id"] in v5.SIN_APORTANTE:
        o.append("El aportante del Anexo 3 v5 salió de la alianza; la partida no cuenta en la contrapartida y debe retirarse o reasignarse")
    if re.search(r"pendiente|por reunir", t):
        o.append("El Anexo 3 declara cotizaciones pendientes (TdR 12.2: al menos dos por rubro, no subsanable)")
    if p["id"].startswith("ST-") and 12 <= int(p["id"][3:]) <= 20:
        o.append("Cotización original del proveedor retirado; reunir dos cotizaciones nuevas")
    if "SNCTI" in t and p["id"] in ("EQ-03", "EQ-20", "EQ-13"):
        o.append("El texto del Anexo 3 asigna custodia al actor del SNCTI; en el Anexo 2 la custodia es de la universidad")
    if "15 comités" in t or "comités" in p["concepto"]:
        o.append("El Anexo 3 escribe «comités» o «15 comités»; el Anexo 2 usa cuatro consejos (Ley 1523 de 2012)")
    if p["id"] == "PD-02":
        o.append("Las 150 horas se ejecutan en M2–M4 (actividad 1.1); la aplicación posterior la ejecutan TH-16 y TH-22 de Avanciencia sin costo adicional de esta línea (tabla 18.5)")
    if p["id"] == "VI-05":
        o.append("Partida completa en su actividad principal (2.3), según la regla del cronograma financiero; también financia la instalación del tramo 3 (2.4)")
    if p["id"] == "CA-05":
        o.append("Partida nueva del Anexo 3 v7: 15 misiones de 3 personas por 3 días, trasladadas de VI-01 a VI-03")
    if p["id"] == "TH-12":
        o.append("El Anexo 3 los llama «departamentales»; son tres técnicos por municipio")
    if p["id"] == "TH-05":
        o.append("El Anexo 12 pide dos productos TOP o A al doctor; el numeral 9 de los TdR pide uno")
    if p["id"] in ("EQ-22", "EQ-12"):
        o.append("Aporte en especie de la universidad: debe ubicarse en Manizales o Calarcá (municipios afectados)")
    if "Cientech" in t or "DreamGIS" in t:
        o.append("Texto del Anexo 3 con el nombre anterior del aliado")
    if p["id"] in SOP:
        o.insert(0, f"Soporte (Anexo 3 v7): {SOP[p['id']][0]}")
    return " | ".join(o)

def acts_declaradas(p):
    a = sorted(set(re.findall(r"A(\d\.\d)", p["texto"])))
    return ", ".join(a)

def main(out):
    wb = Workbook()
    th = Font(bold=True, color="FFFFFF"); fill = PatternFill("solid", fgColor="1F4E79")
    alerta = PatternFill("solid", fgColor="FCE4D6")
    borde = Border(*(Side(style="thin", color="BFBFBF"),) * 4)
    wrap = Alignment(wrap_text=True, vertical="top")

    def hoja(ws, enc, filas, anchos, money=()):
        ws.append(enc)
        for c in ws[1]:
            c.font = th; c.fill = fill; c.alignment = Alignment(wrap_text=True, vertical="center"); c.border = borde
        for f in filas:
            ws.append(f)
        for row in ws.iter_rows(min_row=2):
            for c in row:
                c.alignment = wrap; c.border = borde
                if c.column in money: c.number_format = '#,##0'
        for i, w in enumerate(anchos, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = "B2"; ws.auto_filter.ref = ws.dimensions

    # ---- hoja 1: matriz por partida
    enc = ["Código Anexo 3", "Rubro (TdR 12.2)", "Concepto", "Objetivo específico", "Producto MGA (programa 3906)", "Origen del vínculo con el producto",
           "Actividad principal (cronograma financiero)", "Actividades declaradas en el texto del Anexo 3", "Cantidad", "Unidad", "Valor unitario (COP)",
           "Costo total (COP)", "Fuente de financiación", "Entidad aportante o ejecutora", "Responsable (perfil)", "Municipio", "Período (mes inicial–final)",
           "Ubicación en el Anexo 2", "Ubicación en la MGA-Web", "Ubicación en el SIGP", "Observación"]
    filas = []
    for p in P:
        a = ACT[p["act"]]
        prod, origen = productos(p)
        fte, ent = fuente(p)
        filas.append([p["id"], p["rubro_tdr"], p["concepto"], f"{a['oe']}. {m2.OE_NOMBRE[a['oe']] if hasattr(m2, 'OE_NOMBRE') else ''}".strip(),
                      prod, origen, f"{a['id']} {a['nombre']}", acts_declaradas(p), p["cant"], p["unidad"], p["vunit"], p["total"], fte, ent,
                      (p["concepto"].split(" — ")[0] if p["rubro_tdr"] == "Talento Humano" else RESP_ACT[p["act"]]), municipio(p), f"M{p['m_ini']}–M{p['m_fin']}", ubic_a2(p),
                      f"Cadena de valor › {a['oe']} › {prod.split(';')[0]} › Actividad {a['id']} › insumo: {INSUMO_MGA.get(p['rubro_tdr'], p['rubro_tdr'])} (clasificación propuesta)",
                      f"Presupuesto › rubro «{p['rubro_tdr']}» › fuente «{'SGR' if not p['contra'] else 'Contrapartida ' + ent}»; Cronograma › actividad {a['id']}",
                      obs(p)])
    ws = wb.active; ws.title = "Matriz por partida"
    hoja(ws, enc, filas, [11, 18, 40, 30, 45, 16, 34, 18, 9, 12, 15, 17, 26, 28, 26, 34, 12, 34, 50, 46, 60], money=(11, 12))
    n = len(filas) + 1
    ws.append([]); ws.append(["Total SGR", None, None, None, None, None, None, None, None, None, None, f'=SUMIFS(L2:L{n},M2:M{n},"SGR*")'])
    ws.append(["Total contrapartida vigente", None, None, None, None, None, None, None, None, None, None, f'=SUMIFS(L2:L{n},M2:M{n},"Contrapartida en especie")+SUMIFS(L2:L{n},M2:M{n},"Contrapartida en efectivo")'])
    ws.append(["Contrapartida sin aportante (excluida)", None, None, None, None, None, None, None, None, None, None, f'=SUMIFS(L2:L{n},M2:M{n},"*sin aportante*")'])
    for r in range(n + 2, n + 5):
        ws.cell(r, 1).font = Font(bold=True); ws.cell(r, 12).number_format = '#,##0'; ws.cell(r, 12).font = Font(bold=True)
    for r in range(2, n + 1):
        if ws.cell(r, 21).value:
            ws.cell(r, 21).fill = alerta

    # ---- hoja 2: actividades
    ws2 = wb.create_sheet("Actividades")
    fil = []
    for a in ACT.values():
        ids = [p["id"] for p in P if p["act"] == a["id"]]
        prods = "; ".join(f"P{k}" for k, v in PROD.items() if a["id"] in v["act"])
        estado = "Con financiación directa" if (a["sgr"] or a["contra"]) else "Sin financiación directa en el Anexo 3"
        nota = "" if (a["sgr"] or a["contra"]) else "Se ejecuta con talento humano y servicios asignados a otras actividades del mismo objetivo; el cronograma financiero del Anexo 3 asigna cada partida completa a su actividad principal"
        fil.append([a["id"], a["oe"], a["nombre"], f"M{a['m_ini']}–M{a['m_fin']}", a["sgr"], a["contra"], len(ids), ", ".join(ids), prods, RESP_ACT[a["id"]], estado, nota])
    hoja(ws2, ["Actividad", "Objetivo", "Nombre", "Período", "SGR (COP)", "Contrapartida (COP)", "N.º de partidas", "Partidas", "Productos", "Responsable", "Estado", "Explicación"],
         fil, [9, 9, 50, 12, 17, 17, 9, 40, 18, 30, 26, 60], money=(5, 6))
    k = len(fil) + 1
    ws2.append(["Total", None, None, None, f"=SUM(E2:E{k})", f"=SUM(F2:F{k})"])
    for c in (5, 6): ws2.cell(k + 1, c).number_format = '#,##0'
    for r in range(2, k + 1):
        if ws2.cell(r, 11).value.startswith("Sin"):
            for c in range(1, 13): ws2.cell(r, c).fill = alerta

    # ---- hoja 3: alertas
    ws3 = wb.create_sheet("Alertas")
    al = []
    sin_act = [p["id"] for p in P if not p["act"] or p["act"] not in ACT]
    al.append(["Partidas sin actividad", "Ninguna" if not sin_act else ", ".join(sin_act), "Todas las partidas del Anexo 3 v7 tienen actividad principal en el cronograma financiero", "Sin acción"])
    al.append(["Actividades sin financiación directa", ", ".join(SIN_FIN), "El cronograma financiero asigna cada partida completa a una sola actividad", "Mantener y explicar (nota de las tablas 15.2 y 28.3) o repartir partidas en el Anexo 3 v7"])
    al.append(["Partidas sin aportante", "Ninguna", "EQ-13 y VI-05 pasan a Gestión y Medio Ambiente, integrante de la alianza en el Anexo 3 v7", "Certificar los aportes"])
    al.append(["Contrapartida en efectivo", m2.cop(m2.CON_EFECTIVO), "El criterio 7 otorga dos puntos con efectivo ≥ 1 % del SGR (139.994.053 COP); VI-05 lo cumple con 1,07 %", "Certificación del representante legal de Gestión y Medio Ambiente"])
    import collections as _c
    _cnt = _c.Counter(v[0] for k, v in SOP.items() if k in {p["id"] for p in P})
    al.append(["Soportes de precios (hoja C. Soportes y pendientes)", "; ".join(f"{k}: {v}" for k, v in _cnt.most_common()), "TdR 12.2 nota 4: análisis de costos y dos cotizaciones por bien o servicio; su falta no se subsana", "Reunir antes del cierre; prioridad EQ-01, EQ-03, EQ-04, EQ-07, EQ-23, ST-12 a ST-20 y cartas EQ-24 y EQ-25"])
    al.append(["Período de PD-02", "Actividad 1.1, M2–M4", "Resuelto: las 150 horas producen en M2–M4 el informe de libertad de operación, el borrador del acuerdo marco, las minutas de convenio y la matriz de vencimientos; la aplicación posterior la ejecutan TH-16 y TH-22 de Avanciencia (tabla 18.5)", "Sin ajuste al Anexo 3"])
    al.append(["Importación", "Sin partida", "El Anexo 2 supone entrega en Colombia incluida en el precio cotizado", "Confirmar en cada cotización"])
    al.append(["Sede del laboratorio", "EQ-22, EQ-12", "Los equipos solo se financian en municipios afectados; la universidad no tiene sede en Manizales ni en Calarcá", "Definir el espacio en Manizales o Calarcá"])
    al.append(["Plan de sostenibilidad", "SIG a 1.005.925 COP/usuario-mes", "El Anexo 3 usa 995.103 COP/usuario-mes en EQ-14", "Unificar el precio unitario en el plan"])
    hoja(ws3, ["Alerta", "Partidas o valor", "Causa", "Acción"], al, [28, 34, 60, 60])

    # ---- hoja 4: conciliación
    ws4 = wb.create_sheet("Conciliación")
    sgr = sum(p["total"] for p in P if not p["contra"])
    con = sum(p["total"] for p in P if p["contra"] and p["id"] not in v5.SIN_APORTANTE)
    rows = [["SGR (suma de partidas)", sgr, m2.SGR, "Cuadra" if sgr == m2.SGR else "Revisar"],
            ["Contrapartida vigente", con, m2.CON, "Cuadra" if con == m2.CON else "Revisar"],
            ["Total del proyecto", sgr + con, m2.TOTAL, "Cuadra" if sgr + con == m2.TOTAL else "Revisar"]]
    for oe, v in m2.POR_OE.items():
        rows.append([f"{oe}: SGR", v["sgr"], sum(ACT[a]["sgr"] for a in ACT if ACT[a]["oe"] == oe), "Cuadra"])
    for i, v in enumerate(m2.FLUJO_SEM):
        rows.append([f"Semestre {i + 1}: SGR", round(v), None, "Cronograma financiero del Anexo 3"])
    for rb, v in m2.POR_RUBRO.items():
        if v: rows.append([f"Rubro {rb}", v, None, f"{v / m2.SGR * 100:.1f} % del SGR"])
    hoja(ws4, ["Concepto", "Matriz (COP)", "Anexo 2 (COP)", "Resultado"], rows, [36, 20, 20, 30], money=(2, 3))

    # ---- hoja 5: cambios en el Anexo 2
    ws5 = wb.create_sheet("Cambios en el Anexo 2")
    cambios = [
        ("1, 8, 11", "Localización y población", "Manizales (Caldas) y Calarcá (Quindío); cuatro consejos; población objetivo de cerca de 40 personas de consejos", "Cambio de territorio aprobado"),
        ("2", "Resumen", "Puntos clave, resumen gráfico (Figura 2.1) y resumen", "Solicitud de la alianza"),
        ("5 y 12", "Árboles", "Árbol de problemas y de objetivos en tabla con el esquema de la plantilla y una columna por objetivo; se conserva la figura", "Plantilla del Anexo 2"),
        ("7, 13 y 14", "Alcance y metodología", "Conjunto de referencia rotativo (beta, óptico y gravimétrico) con intercambio en la semana 8; partición por municipio; nueva simulación de 1.000 campañas", "Anexo 3 v7 (EQ-03) y justificación técnica"),
        ("7, 14 y 28", "Ampliaciones", "Plataforma geoespacial contratada (ST-12 a ST-20), sistema de geociencias (EQ-14 a EQ-16), cámara climática (EQ-23), estudio de cobertura por municipio (ST-04)", "Anexo 3 v7"),
        ("10, 14, 18, 19, 26", "Alianza y responsabilidades", "Cinco integrantes: Universidad Santo Tomás, municipios de Manizales y de Calarcá (aporte en uso de software y hardware, EQ-24 y EQ-25), Avanciencia (lidera la ASC y la transferencia) y Gestión y Medio Ambiente (aliado del sector productivo)", "Anexo 3 v7"),
        ("15 y 28", "Presupuesto", "Valores por actividad, objetivo, rubro, municipio y semestre del Anexo 3 v7; contrapartida de 1.774.000.000 COP con 150.000.000 COP en efectivo", "Anexo 3 v7"),
        ("16", "Sostenibilidad", "Custodios de la nueva alianza; costo recurrente con licencias (265.716.408 COP por año) conciliado con el plan de sostenibilidad", "Anexo 3 v7 y plan 10.16"),
        ("17, 20, 24", "Metas e indicadores", "R3 con cuatro consejos; R7 con tres evaluaciones por municipio; productos con territorio y responsables nuevos", "Cambio de territorio"),
        ("21 y 22", "Cronograma y riesgos", "Cronograma financiero del Anexo 3; riesgos de importación y de entrega ajustados", "Anexo 3 v7"),
        ("27", "Permisos", "Importación a cargo del proveedor; responsables territoriales por municipio", "Anexo 3 v7 sin partida de importación"),
        ("30", "Anexos", "Requisitos de Avanciencia (10.12 o 10.13 y 10.14) y soportes por municipio", "Cambio de alianza"),
    ]
    hoja(ws5, ["Secciones", "Tema", "Cambio", "Origen"], [list(c) for c in cambios], [16, 24, 80, 34])
    wb.save(out); print("ok", out, len(P), "partidas")

if __name__ == "__main__":
    main(sys.argv[1])
