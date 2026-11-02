# -*- coding: utf-8 -*-
"""Documentos complementarios v6: plan de sostenibilidad revisado y certificados de precios unitarios de Manizales y Calarcá.
Uso: python3 build/docs_v6.py carpeta_salida"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "v2"))
import v5, m2
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
TIT = m2.IDENT["titulo"]
VERDE = RGBColor(0x00, 0x80, 0x00)

def cop(n): return "$ " + f"{int(round(n)):,}".replace(",", ".")
def mm(n): return f"{n / 1e6:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def base():
    d = docx.Document()
    st = d.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(10)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    for s in d.sections:
        s.top_margin = s.bottom_margin = Cm(2.5); s.left_margin = s.right_margin = Cm(2.2)
    return d

def par(d, txt, b=False, i=False, al=None, size=None, after=6):
    p = d.add_paragraph()
    for k, frag in enumerate(re.split(r"(\[Diligenciar:[^\]]*\])", txt)):
        if not frag: continue
        r = p.add_run(frag); r.bold = b; r.italic = i
        if size: r.font.size = Pt(size)
        if frag.startswith("[Diligenciar"): r.font.color.rgb = VERDE
    if al: p.alignment = al
    p.paragraph_format.space_after = Pt(after)
    return p

def titulo(d, txt, size=11):
    p = par(d, txt, b=True, size=size, after=4); p.paragraph_format.space_before = Pt(8); return p

def tabla(d, enc, filas, anchos=None, size=8.5):
    t = d.add_table(rows=1, cols=len(enc)); t.style = "Table Grid"
    for j, h in enumerate(enc):
        c = t.rows[0].cells[j]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size)
        sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:fill"), "D9E2F3"); c._tc.get_or_add_tcPr().append(sh)
    for f in filas:
        cells = t.add_row().cells
        for j, v in enumerate(f):
            cells[j].text = ""
            for frag in re.split(r"(\[Diligenciar:[^\]]*\])", str(v)):
                if not frag: continue
                r = cells[j].paragraphs[0].add_run(frag); r.font.size = Pt(size)
                if frag.startswith("[Diligenciar"): r.font.color.rgb = VERDE
    if anchos:
        for row in t.rows:
            for j, w in enumerate(anchos): row.cells[j].width = Cm(w)
    d.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

# ------------------------------------------------------------------ plan de sostenibilidad
def plan():
    P = {p["id"]: p for p in v5.partidas()}
    sig4 = 4 * 12 * P["EQ-14"]["vunit"]; sigp = 12 * P["EQ-15"]["vunit"]; geo = P["EQ-16"]["vunit"]
    nube = P["EQ-10"]["total"] / 2; sim = 12 * 12 * P["ST-01"]["vunit"]; sat = 10 * 12 * P["ST-07"]["vunit"]
    rep = P["MA-06"]["total"] / 2; lic = P["EQ-21"]["total"] / 2
    sig = sig4 + sigp + geo; con = sim + sat
    total = sig + nube + con + rep + lic
    assert round(total) == 265716408, total
    d = base()
    par(d, "PLAN DE SOSTENIBILIDAD Y MODELO DE NEGOCIO MÍNIMO", b=True, al=WD_ALIGN_PARAGRAPH.CENTER, size=12)
    par(d, "Adaptación editable del Anexo 7 del Acuerdo 12 de 2024 (numeral 10.16 de los TdR de la Convocatoria 56). Versión revisada.", i=True, al=WD_ALIGN_PARAGRAPH.CENTER, size=9)
    tabla(d, ["Campo", "Contenido"], [
        ["Código SIGP", "143329 (identificación distinta del BPIN)"],
        ["Nombre del proyecto", TIT],
        ["Entidad operadora principal", "Universidad Santo Tomás, sede Villavicencio: nodos, gateways, plataforma, gemelo digital, datos, banco de calibración y laboratorio de modelación"],
        ["Entidades operadoras por componente", "Municipio de Manizales y Municipio de Calarcá: tablero, protocolo de alerta y custodia local de los nodos de su jurisdicción"],
        ["Apoyo a la transferencia", "Avanciencia: formación de custodios, licencias de uso, acuerdo de titularidad y convenios de custodia; no opera componentes"],
        ["Apoyo técnico", "Gestión y Medio Ambiente: puede prestar mantenimiento o verificación a los custodios por contrato posterior; no opera componentes al radicar"],
        ["Territorios", "Manizales (Caldas) y Calarcá (Quindío)"],
        ["BPIN", "[Diligenciar: BPIN, si se asigna]"],
        ["Período de costeo", "Un año de operación posterior a la entrega del mes 24; no equivale a la vida útil total"],
    ], [5, 11.5])
    titulo(d, "1. Alcance y organización de la operación")
    par(d, "La operación conserva la red de 100 nodos y 10 gateways, la plataforma y el laboratorio de modelación. Cada componente se transfiere a un custodio con partida, personal designado y competencia jurídica. La universidad opera la red, los datos y el laboratorio. Cada municipio opera el tablero y la custodia local de los nodos de su jurisdicción.")
    par(d, "Horizonte: escenario inicial de 12 meses después de la entrega, coherente con la medición de los impactos I1 e I2 en el mes 36. La vida útil total y sus fechas se validan con las fichas técnicas de los equipos [Diligenciar: vida útil declarada por el fabricante].")
    titulo(d, "2. Actividades y recursos del año 1 de operación")
    par(d, "Valores en millones de COP. ND: no determinado; PV: por validar. ND y PV no equivalen a cero.", i=True, size=9)
    filas = [
        ["Licencias del sistema de geociencias (SIG y geoestadística)", mm(sig), "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Nube reservada (reserva de formulación)", mm(nube), "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Conectividad: planes celulares de 12 gateways y enlace satelital de 10 terminales", mm(con), "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Repuestos y consumibles de mantenimiento", mm(rep), "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Licencias de modelación urbana, de dispersión y SIG", mm(lic), "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Calibración periódica (gravimetría y rotación con referencia)", "ND", "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Tablero, alertas y custodia local de nodos", "ND", "PV", "Presupuesto municipal", "Municipios de Manizales y de Calarcá"],
        ["Personal de operación, calidad de datos y soporte", "ND", "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Subtotal calculable con precios del Anexo 3", mm(total), "PV", "F1 / F2", "Universidad Santo Tomás"],
        ["Costo integral de operación", "ND", "PV", "F1 / F2 / municipal", "Todas las operadoras"],
    ]
    tabla(d, ["Actividad", "Año 1", "Años 2 a n", "Fuente propuesta", "Responsable"], filas, [6.8, 1.8, 1.8, 2.6, 3.6])
    par(d, "F1: recursos institucionales sujetos a aprobación. F2: convenios o cofinanciación por gestionar. Son fuentes propuestas sin certificación. Los ingresos del modelo de negocio son escenarios y no se suman como recursos asegurados.", size=9)
    titulo(d, "3. Memoria de costos anuales")
    tabla(d, ["Componente", "Base de cálculo anual", "COP por año", "Soporte"], [
        ["Sistema de geociencias, nivel profesional", f"4 usuarios × 12 meses × {cop(P['EQ-14']['vunit'])}", cop(sig4), "Anexo 3, EQ-14 (referencia de compra pública)"],
        ["Sistema de geociencias, nivel superior", f"1 usuario × 12 meses × {cop(P['EQ-15']['vunit'])}", cop(sigp), "Anexo 3, EQ-15"],
        ["Complemento de geoestadística", f"1 usuario-año × {cop(geo)}", cop(geo), "Anexo 3, EQ-16 (condicional)"],
        ["Nube reservada", f"{cop(P['EQ-10']['total'])} ÷ 24 × 12", cop(nube), "Anexo 3, EQ-10 (reserva de formulación)"],
        ["Planes celulares", f"12 SIM × 12 meses × {cop(P['ST-01']['vunit'])}", cop(sim), "Anexo 3, ST-01"],
        ["Enlace satelital", f"10 módulos × 12 meses × {cop(P['ST-07']['vunit'])}", cop(sat), "Anexo 3, ST-07"],
        ["Repuestos y consumibles", f"{cop(P['MA-06']['total'])} ÷ 2 años", cop(rep), "Anexo 3, MA-06"],
        ["Licencias de modelación", f"{cop(P['EQ-21']['total'])} ÷ 2 años, con renovación anual", cop(lic), "Anexo 3, EQ-21"],
        ["Subtotal calculable", "Suma de las filas anteriores", cop(total), "Igual a la tabla 16.6 del Anexo 2"],
    ], [4.2, 5.4, 2.8, 4.2])
    par(d, f"Si la geoestadística ya está incluida en la licencia de nivel superior, el subtotal baja a {cop(total - geo)}. No debe contratarse dos veces la misma funcionalidad. La reserva de nube divide el valor de formulación entre 24 meses; no acredita capacidad ni oferta de renovación. El IVA de las referencias de licencias debe confirmarse.")
    par(d, "Costos por completar: personal de operación y calidad de datos; calibración del banco y del conjunto de referencia; gravimetría a 350.000 COP por muestra con frecuencia por definir; energía y visitas en ambos municipios; baterías al fin de su vida útil; seguros y logística.")
    titulo(d, "4. Cronograma y seguimiento")
    par(d, "La calibración y el mantenimiento siguen las especificaciones de los equipos. Las licencias y la nube se renuevan según sus ciclos. El seguimiento registra cumplimiento técnico, disponibilidad mensual de nodos, uso del tablero por los consejos, disponibilidad de recursos y renovaciones. La meta de continuidad es de 70 % o más de los nodos bajo custodia a los 12 meses del cierre.")
    titulo(d, "5. Modelo de negocio mínimo propuesto")
    tabla(d, ["Elemento", "Propuesta (hipótesis por validar)"], [
        ["Usuarios y posibles clientes", "Entidades territoriales, autoridades ambientales, contratistas de demolición y empresas que requieran información local de calidad del aire. Ser usuario no supone capacidad de pago."],
        ["Propuesta de valor", "Monitoreo con error conocido, evaluación previa de demoliciones, analítica espacial y mantenimiento o calibración. No implica acreditación ni equivalencia con mediciones regulatorias."],
        ["Ingresos posibles", "Contratos de monitoreo y analítica, evaluaciones previas de demolición, soporte y mantenimiento, y convenios de cofinanciación. No son recursos comprometidos."],
        ["Canales y validación", "Demostraciones a posibles clientes, pilotos y propuestas por los canales institucionales autorizados."],
        ["Propiedad intelectual y datos", "Titularidad y licencias definidas en el acuerdo marco del mes 6, con Avanciencia. Los datos públicos se separan de los servicios técnicos contratables."],
        ["Gobernanza y reinversión", "La universidad y los aliados aprueban el esquema de prestación y el destino de los ingresos a los gastos recurrentes."],
        ["Indicadores", "Contratos o convenios vigentes, cobertura de gastos recurrentes, continuidad de la red, calidad de los datos y uso efectivo de la información."],
    ], [4.2, 12.4])
    titulo(d, "6. Validación y firma de cada entidad operadora")
    par(d, "El formato definitivo contiene la garantía de operación y funcionamiento respaldada en ingresos de naturaleza permanente. Este borrador no contiene firmas ni acredita esa garantía.", i=True)
    for ent, bienes in (("Universidad Santo Tomás, sede Villavicencio", "Nodos, gateways, plataforma, gemelo digital, datos, banco de calibración, conjunto de referencia y laboratorio de modelación"),
                        ("Municipio de Manizales", "Tablero y protocolo de alerta de su jurisdicción; custodia local de los nodos instalados en Manizales"),
                        ("Municipio de Calarcá", "Tablero y protocolo de alerta de su jurisdicción; custodia local de los nodos instalados en Calarcá")):
        tabla(d, ["Campo", "Contenido"], [["Entidad", ent], ["Bienes, servicios y actividades a su cargo", bienes],
                                         ["Fuente permanente de financiación", "[Diligenciar: rubro presupuestal permanente]"],
                                         ["Nombre del representante legal", "[Diligenciar: nombre]"], ["Cargo", "[Diligenciar: cargo]"],
                                         ["Firma", ""], ["Lugar y fecha", "[Diligenciar: lugar y fecha]"]], [5, 11.6])
    titulo(d, "Fuentes")
    for s in ("Anexo 3 del proyecto, versión 5: líneas EQ-10, EQ-14, EQ-15, EQ-16, EQ-21, ST-01, ST-07 y MA-06, y estudio de mercado.",
              "Colombia Compra Eficiente, órdenes 150119 del 12 de agosto de 2025 y 149044 del 16 de julio de 2025 (referencias del sistema de geociencias citadas en el Anexo 3).",
              "Acuerdo 12 de 2024 de la Comisión Rectora del SGR, Anexo 7: formato del plan de sostenibilidad.",
              "MinCiencias (2026). Términos de referencia de la Convocatoria 56, numeral 10.16."):
        par(d, s, size=9, after=2)
    f = os.path.join(OUT, "Plan_sostenibilidad_Aire_SIGP_143329_v3.docx"); d.save(f); print("ok", f, cop(total))

# ------------------------------------------------------------------ certificados de precios unitarios
def base_precio(p):
    t = p["texto"]
    m = re.search(r"cotizaci[oó]n seleccionada de ([^(;]+)", t)
    if p["id"].startswith("ST-") and 12 <= int(p["id"][3:]) <= 20: return "Cotización por renovar (proveedor retirado)"
    if m: return "Cotización de " + m.group(1).strip()
    if "TdR §14.4" in t and p["rubro_tdr"] == "Talento Humano": return "Valor fijado por los TdR (numeral 14.4)"
    if "Escala de honorarios" in t: return "Escala de honorarios de referencia (SMLV 2026)"
    if "Colombia Compra" in t or "Orden " in t: return "Referencia de compra pública"
    if re.search(r"mediana de \d+ referencias", t): return "Mediana de referencias de mercado"
    if re.search(r"dimensionamiento|sin oferta|sin referencia", t): return "Valor de dimensionamiento; cotización por reunir"
    return "Estudio de mercado del Anexo 3"

def certificado(mun, dep):
    d = base()
    par(d, f"[Diligenciar: membrete oficial de la Alcaldía de {mun}]", al=WD_ALIGN_PARAGRAPH.CENTER, size=9)
    par(d, f"EL SUSCRITO REPRESENTANTE LEGAL DEL MUNICIPIO DE {mun.upper()} — {dep.upper()},", b=True, al=WD_ALIGN_PARAGRAPH.CENTER, size=11)
    par(d, "En uso de sus atribuciones legales, en particular las conferidas por la Constitución Política, la Ley 2056 de 2020, el Decreto 1821 de 2020 y el Acuerdo 12 de 2024 de la Comisión Rectora del Sistema General de Regalías,", al=WD_ALIGN_PARAGRAPH.JUSTIFY)
    par(d, "CERTIFICA:", b=True, al=WD_ALIGN_PARAGRAPH.CENTER, size=11)
    par(d, f"Que los precios unitarios incorporados en el proyecto de inversión presentado a la Convocatoria 56 del SGR de 2026, identificado con el código SIGP 143329 (código BPIN pendiente de asignación) y denominado «{TIT}», corresponden a precios de mercado de la región Eje Cafetero del Sistema General de Regalías. Esos precios son los que se usan de manera ordinaria para actividades de ciencia, tecnología e innovación de este tipo.", al=WD_ALIGN_PARAGRAPH.JUSTIFY)
    par(d, "Que la determinación de los precios unitarios se sustentó en el estudio de mercado del Anexo 3. Para el talento humano de formación se aplicaron los valores del numeral 14.4 de los términos de referencia. Para los perfiles profesionales se aplicó una escala de honorarios de referencia con el salario mínimo de 2026. Para los equipos especializados se usaron cotizaciones de proveedores y medianas de referencias de mercado. El anexo de este certificado relaciona cada precio unitario y su base.", al=WD_ALIGN_PARAGRAPH.JUSTIFY)
    par(d, "Que los precios unitarios certificados guardan coherencia con el Anexo 3 (presupuesto del proyecto), con la Metodología General Ajustada (MGA) y con el documento técnico (Anexo 2) presentado al Ministerio de Ciencia, Tecnología e Innovación.", al=WD_ALIGN_PARAGRAPH.JUSTIFY)
    par(d, f"Que la presente certificación se expide en el marco del rol del Municipio de {mun} como integrante de la alianza y lugar de ejecución del proyecto. No compromete recursos propios distintos de la contrapartida en especie certificada por separado.", al=WD_ALIGN_PARAGRAPH.JUSTIFY)
    par(d, "La presente certificación se expide bajo la gravedad del juramento y sirve para los fines pertinentes ante MinCiencias y el Órgano Colegiado de Administración y Decisión de Ciencia, Tecnología e Innovación del SGR.", al=WD_ALIGN_PARAGRAPH.JUSTIFY)
    par(d, f"Dada en {mun}, {dep}, a los [Diligenciar: día] días del mes de [Diligenciar: mes] de 2026.", al=WD_ALIGN_PARAGRAPH.JUSTIFY)
    par(d, "Atentamente,", after=30)
    par(d, "[Diligenciar: nombre del alcalde]", b=True, al=WD_ALIGN_PARAGRAPH.CENTER, after=0)
    par(d, "[Diligenciar: C.C.]", al=WD_ALIGN_PARAGRAPH.CENTER, after=0)
    par(d, f"Alcalde Municipal de {mun}", al=WD_ALIGN_PARAGRAPH.CENTER)
    d.add_page_break()
    par(d, "ANEXO — PRECIOS UNITARIOS DEL PROYECTO (FUENTE: SGR)", b=True, al=WD_ALIGN_PARAGRAPH.CENTER, size=11)
    par(d, "Valores en pesos colombianos, tomados del Anexo 3, versión 5. La columna «Base» indica el soporte del precio. Las líneas con cotización por reunir se completan antes del cierre.", i=True, size=9)
    filas = []
    for p in v5.partidas():
        if p["contra"]: continue
        filas.append([p["id"], p["concepto"][:95], p["unidad"], f"{p['cant']:g}".replace(".", ","), cop(p["vunit"]), cop(p["total"]), base_precio(p)])
    tot = sum(p["total"] for p in v5.partidas() if not p["contra"]); assert tot == m2.SGR
    filas.append(["", "Total solicitado al SGR", "", "", "", cop(tot), ""])
    tabla(d, ["Código", "Concepto", "Unidad", "Cantidad", "Valor unitario", "Valor total", "Base"], filas, [1.4, 5.6, 1.6, 1.3, 2.2, 2.4, 3.0], size=7.5)
    f = os.path.join(OUT, f"Certificado_precios_unitarios_{mun.replace('á', 'a')}.docx"); d.save(f); print("ok", f)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    plan(); certificado("Manizales", "Caldas"); certificado("Calarcá", "Quindío")
