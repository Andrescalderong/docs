# -*- coding: utf-8 -*-
"""Documento corto para el CIF: actividades técnicas, estado de cotización y componente del actor del SNCTI.
Uso: python3 build/doc_cif.py salida.docx"""
import json, sys, collections
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
P = json.load(open("data_v7/partidas.json"))
EST = json.load(open("../estado_sop.json"))
C = json.load(open("data_v7/cronofin.json"))
ACTS = [("1.1","Seleccionar los sitios y diseñar la colocalización"),("1.2","Adquirir y caracterizar el lote 1 de nodos y las referencias"),
 ("1.3","Instalar el tramo 1, colocalizar y calibrar en el piloto"),("1.4","Entrenar y validar el modelo de corrección (compuerta C1)"),
 ("1.5","Reentrenar y verificar por municipio el tramo 2 (compuerta C2)"),("1.6","Verificar el desempeño final y ejecutar el ensayo independiente"),
 ("1.7","Validar el gemelo predictivo con demoliciones reales"),("1.8","Administración y apoyo a la supervisión (OE1)"),
 ("2.1","Diseñar la arquitectura de enlace y energía"),("2.2","Desarrollar el firmware y la plataforma base"),("2.3","Instalar el tramo 2"),
 ("2.4","Instalar el tramo 3"),("2.5","Diseñar el laboratorio de modelación y el inventario de emisión"),("2.6","Dotar el laboratorio y montar la cadena de modelación"),
 ("2.7","Construir y calibrar el gemelo predictivo de demolición"),("2.8","Administración y apoyo a la supervisión (OE2)"),
 ("3.1","Co-diseñar los umbrales y el protocolo de alerta con los consejos"),("3.2","Poner en uso el tablero con los consejos"),
 ("3.3","Formar custodios y firmar los convenios por tramo"),("3.4","Transferir, cerrar y evaluar"),
 ("3.5","Adoptar el protocolo de evaluación previa de demolición"),("3.6","Administración y apoyo a la supervisión (OE3)")]
OFERTA = {"EQ-01": "SIOT, oferta preliminar del 26-oct-2026", "EQ-04": "SIOT, oferta preliminar del 26-oct-2026",
          "EQ-03": "Inteccon V1316-2, oferta formal", "EQ-07": "Gesoltec 0151-2026, oferta del subpaquete (sin cámara climática)",
          "PD-04": "Oferta preliminar recibida; conciliación pendiente"}
QUIEN = {"E1": "Universidad", "E2": "Manizales", "E3": "Calarcá", "E4": "Avanciencia", "E5": "Gestión y Medio Ambiente"}
def m(x): return f"{x:,.0f}".replace(",", ".")
def cls(x):
    if x["id"] in OFERTA: return "oferta"
    e = EST.get(x["id"], "")
    if e.startswith("Escala") or e.startswith("Base normativa"): return "personal"
    if x["sgr"] == 0: return "especie"
    return "porcot"
d = docx.Document(); st = d.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(9)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
for s in d.sections: s.left_margin = s.right_margin = Cm(1.8); s.top_margin = s.bottom_margin = Cm(1.6)
def p(t, b=False, s=9, al=None, sp=4):
    q = d.add_paragraph(); r = q.add_run(t); r.bold = b; r.font.size = Pt(s); q.paragraph_format.space_after = Pt(sp)
    if al is not None: q.alignment = al
    return q
def sombra(c, hexc):
    tc = c._tc.get_or_add_tcPr(); sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hexc); tc.append(sh)
def tabla(enc, filas, anchos, total=None):
    t = d.add_table(rows=1, cols=len(enc)); t.style = "Table Grid"
    for i, x in enumerate(enc):
        c = t.rows[0].cells[i]; c.text = x; sombra(c, "D9E2EC")
        for r in c.paragraphs[0].runs: r.bold = True; r.font.size = Pt(8)
    for f in filas + ([total] if total else []):
        cs = t.add_row().cells
        for i, x in enumerate(f):
            cs[i].text = x
            for r in cs[i].paragraphs[0].runs:
                r.font.size = Pt(8); r.bold = (f is total)
            if i > 0 and enc[i].startswith("Valor"): cs[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    t.autofit = False
    for i, w in enumerate(anchos): t.columns[i].width = Cm(w)
    for row in t.rows:
        for i, w in enumerate(anchos): row.cells[i].width = Cm(w)
    d.add_paragraph().paragraph_format.space_after = Pt(2)
SGR = sum(x["sgr"] for x in P); TOT = sum(x["total"] for x in P)
p("Proyecto SIGP 143329 · Actividades técnicas, estado de cotización y componente del actor del SNCTI", b=True, s=12, al=WD_ALIGN_PARAGRAPH.CENTER)
p("«Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto». Convocatoria 56 del SGR (MinCiencias). Corte: 2 de noviembre de 2026.", s=8.5, al=WD_ALIGN_PARAGRAPH.CENTER, sp=8)
p(f"El proyecto instala una red de 100 nodos y 10 gateways en sitios de remoción de escombros de Manizales (Caldas) y Calarcá (Quindío), corrige sus lecturas contra un conjunto de referencia, entrega a los consejos de gestión del riesgo un tablero con protocolo de alerta y monta un laboratorio de modelación que anticipa el polvo de cada demolición. "
  f"Dura 24 meses. Solicita {m(SGR)} COP al SGR, con contrapartida de {m(TOT-SGR)} COP (total {m(TOT)} COP). La Universidad Santo Tomás es la entidad proponente y ejecutora. Fuente de cifras y estados: Anexo 3 v7, hoja «C. Soportes y pendientes».")
p("1. Actividades y estado de cotización", b=True, s=10)
G = collections.defaultdict(list)
for x in P: G[x["act"].replace("A", "")].append(x)
filas = []
for a, n in ACTS:
    L = G.get(a, [])
    if not L:
        filas.append((a, n, "—", "Universidad", "Sin partida propia: la ejecuta el personal de otras actividades")); continue
    sg = sum(x["sgr"] for x in L)
    ej = ", ".join(sorted({QUIEN[x["resp"]] for x in L}, key=lambda q: list(QUIEN.values()).index(q)))
    k = collections.Counter(cls(x) for x in L); partes = []
    if k["oferta"]: partes.append(f"{k['oferta']} con oferta")
    if k["porcot"]: partes.append(f"{k['porcot']} por cotizar")
    if k["personal"]: partes.append(f"{k['personal']} de personal (escala o valor fijado)")
    if k["especie"]: partes.append(f"{k['especie']} en especie")
    filas.append((a, n, m(sg), ej, "; ".join(partes)))
tabla(["Act.", "Actividad", "Valor SGR (COP)", "Ejecuta", "Partidas y estado"], filas, [1.0, 6.2, 2.6, 3.0, 5.2],
      total=("", "Total", m(SGR), "", f"{len(P)} partidas"))
p("2. Partidas con oferta de proveedor", b=True, s=10)
fo = [(x["id"], x["item"].split(" (")[0], m(x["sgr"]), OFERTA[x["id"]]) for x in P if x["id"] in OFERTA]
tabla(["Código", "Bien o servicio", "Valor SGR (COP)", "Soporte y estado"], fo, [1.5, 7.0, 2.8, 6.7],
      total=("", "Total con oferta", m(sum(x["sgr"] for x in P if x["id"] in OFERTA)), "Todas requieren una segunda cotización (TdR, numeral 12.2)"))
npc = sum(1 for x in P if cls(x) == "porcot"); vpc = sum(x["sgr"] for x in P if cls(x) == "porcot")
npe = sum(1 for x in P if cls(x) == "personal"); vpe = sum(x["sgr"] for x in P if cls(x) == "personal")
p(f"Las demás partidas de bienes y servicios ({npc}, por {m(vpc)} COP) están dimensionadas y por cotizar. Las {npe} partidas de personal ({m(vpe)} COP) se valoran con escalas de honorarios o con valores fijados por los términos de referencia y no requieren cotización.")
p("3. Componente a cargo de Avanciencia (actor del SNCTI)", b=True, s=10)
A4 = [x for x in P if x["resp"] == "E4"]
fa = [(x["act"].replace("A", ""), x["id"], x["item"].split(" (")[0].split(" — ")[0], m(x["sgr"]) if x["sgr"] else f"{m(x['total'])} (especie)") for x in sorted(A4, key=lambda x: (x["act"], x["id"]))]
tabla(["Act.", "Código", "Partida", "Valor (COP)"], fa, [1.0, 1.5, 11.0, 4.5],
      total=("", "", "Total SGR que ejecuta por contrato con la universidad", m(sum(x["sgr"] for x in A4))))
p(f"Avanciencia ejecuta por contrato con la universidad la apropiación social del conocimiento (co-diseño con los consejos, laboratorios ciudadanos, cartillas, ferias y divulgación), la formación de custodios y la transferencia (propiedad intelectual, registros ante la DNDA y convenios de custodia). Aporta además {m(sum(x['total']-x['sgr'] for x in A4))} COP en especie (horas de su equipo de transferencia, TH-22).")
p("4. Lo que asumiría la entidad que ocupe este rol", b=True, s=10)
for t in ["Ejecutar por contrato con la universidad las partidas de la sección 3, con su personal y sus soportes.",
          "Aportar la contrapartida en especie que pueda certificar y firmar la certificación de contrapartida.",
          "Firmar el certificado de participación (numeral 10.18) y el Anexo 1 de la alianza.",
          "Adjuntar la resolución de reconocimiento como actor del SNCTI vigente a la fecha de cierre (numeral 10.14) y el certificado de existencia y representación legal de menos de 90 días.",
          "Designar un responsable institucional ante el proyecto."]:
    q = d.add_paragraph(t, style="List Bullet"); q.paragraph_format.space_after = Pt(1)
    for r in q.runs: r.font.size = Pt(9)
p("Cierre de la convocatoria: martes 3 de noviembre de 2026, 4:00 p. m.", s=8.5, sp=0)
d.save(sys.argv[1]); print("ok", sys.argv[1])
