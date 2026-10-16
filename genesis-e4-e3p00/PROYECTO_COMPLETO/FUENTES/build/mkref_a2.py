# -*- coding: utf-8 -*-
"""Construye reference_a2.docx: estilos de lectura tipo Anexo 2 sobre el paquete de la plantilla oficial (encabezado, pie, página, márgenes)."""
import docx, zipfile, re, sys, os, shutil
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
HERE = os.path.dirname(os.path.abspath(__file__))
ORIG = sys.argv[1]; OUT = os.path.join(HERE, 'reference_a2.docx')
d = docx.Document(os.path.join(HERE, 'ref_default.docx'))
S = {s.name: s for s in d.styles}
FONT = 'Arial'
def font(st, name=FONT, size=None, bold=None, italic=None, color=None):
    f = st.font; f.name = name
    rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
    if rf is None: rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'): rf.set(qn(a), name)
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:cstheme', 'w:eastAsiaTheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    f.color.rgb = RGBColor.from_string(color or '000000')
def para(st, before=0, after=0, line=1.0, keep=False, align=None, indent=None, left=None):
    p = st.paragraph_format; p.space_before = Pt(before); p.space_after = Pt(after)
    p.line_spacing = line
    p.keep_with_next = True if keep else None
    if align is not None: p.alignment = align
    if indent is not None: p.first_line_indent = Cm(indent)
    if left is not None: p.left_indent = Cm(left)
J = WD_ALIGN_PARAGRAPH.JUSTIFY; L = WD_ALIGN_PARAGRAPH.LEFT; C = WD_ALIGN_PARAGRAPH.CENTER
font(S['Normal'], size=10.5); para(S['Normal'], 0, 4, 1.05, align=J, indent=0)
font(S['Body Text'], size=10.5); para(S['Body Text'], 0, 6, 1.08, align=J, indent=0)
font(S['First Paragraph'], size=10.5); para(S['First Paragraph'], 0, 6, 1.08, align=J, indent=0)
font(S['Compact'], size=10); para(S['Compact'], 0, 2, 1.0, align=L, indent=0)
H = {'Heading 1': (True, False, 12, 16, 6), 'Heading 2': (True, False, 11, 12, 4), 'Heading 3': (True, True, 10.5, 10, 3),
     'Heading 4': (True, False, 10.5, 8, 2), 'Heading 5': (False, True, 10.5, 6, 2), 'Heading 6': (False, True, 10, 6, 2)}
for n, (b, i, sz, bef, aft) in H.items():
    font(S[n], size=sz, bold=b, italic=i); para(S[n], bef, aft, 1.05, keep=True, align=L, indent=0)
S['Heading 1'].font.all_caps = True
font(S['Title'], size=15, bold=True); para(S['Title'], 18, 6, 1.1, align=C)
font(S['Subtitle'], size=12, bold=True); para(S['Subtitle'], 0, 12, 1.1, align=C)
for n in ('Author', 'Date'): font(S[n], size=11); para(S[n], 0, 4, 1.1, align=C)
font(S['TOC Heading'], size=12, bold=True); para(S['TOC Heading'], 6, 8, 1.0, keep=True, align=L)
font(S['Block Text'], size=10, italic=False); para(S['Block Text'], 2, 8, 1.1, align=J, left=1.0)
font(S['Image Caption'], size=9, italic=True); para(S['Image Caption'], 2, 8, 1.0, align=C)
font(S['Table Caption'], size=9, italic=True); para(S['Table Caption'], 2, 3, 1.0)
font(S['Captioned Figure'], size=10); para(S['Captioned Figure'], 4, 0, 1.0, align=C, keep=True)
font(S['Figure'], size=10); para(S['Figure'], 4, 0, 1.0, align=C)
font(S['Footnote Text'], size=8.5)
def nuevo(nombre, base='Normal'):
    if nombre in S: return S[nombre]
    st = d.styles.add_style(nombre, 1); st.base_style = S[base]; S[nombre] = st; return st
for nm, (b, i, sz, bef, aft, keep, al) in {
  'TablaRotulo': (True, False, 10, 10, 0, True, L), 'TablaTitulo': (False, True, 10, 0, 3, True, L), 'TablaNota': (False, False, 8.5, 3, 8, False, J),
  'FiguraRotulo': (True, False, 10, 10, 0, True, L), 'FiguraTitulo': (False, True, 10, 0, 3, True, L), 'FiguraNota': (False, False, 8.5, 2, 10, False, J)}.items():
    st = nuevo(nm); font(st, size=sz, bold=b, italic=i); para(st, bef, aft, 1.0, keep=keep, align=al, indent=0)
for nm, sz in (('Tabla9', 9), ('Tabla8', 8), ('Tabla7', 7), ('Tabla65', 6.3)):
    st = nuevo(nm, 'Compact'); font(st, size=sz); para(st, 0, 0, 1.0, align=L, indent=0)
st = nuevo('Referencia'); font(st, size=10); para(st, 0, 5, 1.0, indent=-1.0, left=1.0, align=L)
st = nuevo('Codigo'); font(st, 'Courier New', 6.5); para(st, 0, 0, 1.0, align=L)
if 'Source Code' not in S: nuevo('Source Code')
font(S['Source Code'], 'Courier New', 6.5); para(S['Source Code'], 0, 0, 1.0, align=L)
for i, (sz, left, bf) in {1: (10.5, 0, 4), 2: (10, 0.5, 0), 3: (9.5, 1.0, 0)}.items():
    st = nuevo(f'TOC {i}'); font(st, size=sz, bold=(i == 1)); para(st, bf, 0, 1.0, left=left, align=L)
for nm in ('Indice', 'Indice2'):
    st = nuevo(nm); font(st, size=10); para(st, 0, 0, 1.0, left=0, align=L)
tmp = os.path.join(HERE, '_tmp_styles.docx'); d.save(tmp)
styles_xml = zipfile.ZipFile(tmp).read('word/styles.xml')
zo = zipfile.ZipFile(ORIG); zn = zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED)
for it in zo.infolist():
    b = zo.read(it.filename)
    if it.filename.startswith('word/fonts/') or it.filename == 'word/_rels/fontTable.xml.rels': continue
    if it.filename == 'word/fontTable.xml':
        b = re.sub(rb'<w:embed\w+ [^>]*/>', b'', b)
    if it.filename == 'word/styles.xml': b = styles_xml
    elif it.filename == 'word/document.xml':
        s = b.decode('utf8')
        head = s[:s.index('<w:body>') + len('<w:body>')]
        sect = re.search(r'<w:sectPr>.*?</w:sectPr>', s, re.S).group(0)
        sect = re.sub(r'<w:pgNumType[^>]*/>', '', sect)
        b = (head + sect + '</w:body></w:document>').encode('utf8')
    zn.writestr(it.filename, b)
zn.close(); os.remove(tmp); print('ok', OUT)
