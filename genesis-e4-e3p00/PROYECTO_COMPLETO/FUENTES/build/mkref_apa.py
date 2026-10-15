import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
d=docx.Document('ref_default.docx')
class _S(dict): pass
S=_S({s.name:s for s in d.styles})
FONT='Times New Roman'
def font(st,name=FONT,size=None,bold=None,italic=None,color=None):
    f=st.font; f.name=name
    rpr=st.element.get_or_add_rPr()
    rf=rpr.find(qn('w:rFonts'))
    if rf is None: rf=OxmlElement('w:rFonts'); rpr.insert(0,rf)
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),name)
    for a in ('w:asciiTheme','w:hAnsiTheme','w:cstheme','w:eastAsiaTheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if size: f.size=Pt(size)
    if bold is not None: f.bold=bold
    if italic is not None: f.italic=italic
    f.color.rgb=RGBColor.from_string(color or '000000')
def para(st,before=0,after=0,line=None,keep=False,align=None,indent=None,left=None):
    p=st.paragraph_format; p.space_before=Pt(before); p.space_after=Pt(after)
    if line=='double': p.line_spacing_rule=WD_LINE_SPACING.DOUBLE
    elif line: p.line_spacing=line
    if keep: p.keep_with_next=True
    if align is not None: p.alignment=align
    if indent is not None: p.first_line_indent=Cm(indent)
    if left is not None: p.left_indent=Cm(left)
# cuerpo: doble espacio; sangría de 1,27 cm salvo primer párrafo de sección
font(S['Normal'],size=12); para(S['Normal'],0,0,'double')
font(S['Body Text'],size=12); para(S['Body Text'],0,0,'double',indent=1.27,align=WD_ALIGN_PARAGRAPH.LEFT)
font(S['First Paragraph'],size=12); para(S['First Paragraph'],0,0,'double',indent=1.27,align=WD_ALIGN_PARAGRAPH.LEFT)
font(S['Compact'],size=11); para(S['Compact'],0,2,1.0)
# encabezados APA 7
H={'Heading 1':(True,False,WD_ALIGN_PARAGRAPH.CENTER),'Heading 2':(True,False,WD_ALIGN_PARAGRAPH.LEFT),
   'Heading 3':(True,True,WD_ALIGN_PARAGRAPH.LEFT),'Heading 4':(True,False,WD_ALIGN_PARAGRAPH.LEFT),'Heading 5':(True,True,WD_ALIGN_PARAGRAPH.LEFT)}
for n,(b,i,al) in H.items():
    font(S[n],size=12,bold=b,italic=i); para(S[n],12 if n!='Heading 1' else 0,0 ,'double' if False else 1.15,keep=True,align=al,indent=0)
S['Heading 1'].paragraph_format.page_break_before=True
S['Heading 1'].paragraph_format.space_after=Pt(12)
for n in ('Heading 2','Heading 3'): S[n].paragraph_format.space_after=Pt(6)
font(S['Title'],size=20,bold=True); para(S['Title'],72,12,1.1,align=WD_ALIGN_PARAGRAPH.CENTER)
font(S['Subtitle'],size=14); para(S['Subtitle'],0,12,1.1,align=WD_ALIGN_PARAGRAPH.CENTER)
for n in ('Author','Date'): font(S[n],size=12); para(S[n],0,6,1.1,align=WD_ALIGN_PARAGRAPH.CENTER)
font(S['TOC Heading'],size=12,bold=True); para(S['TOC Heading'],0,12,1.0,keep=True,align=WD_ALIGN_PARAGRAPH.CENTER)
S['TOC Heading'].paragraph_format.page_break_before=True
font(S['Block Text'],size=12); para(S['Block Text'],0,0,'double',left=1.27)
font(S['Image Caption'],size=10,italic=True); para(S['Image Caption'],2,8,1.0,align=WD_ALIGN_PARAGRAPH.CENTER)
font(S['Table Caption'],size=10,italic=True); para(S['Table Caption'],2,3,1.0)
font(S['Captioned Figure'],size=10); para(S['Captioned Figure'],4,0,1.0,align=WD_ALIGN_PARAGRAPH.CENTER,keep=True)
font(S['Figure'],size=10); para(S['Figure'],4,0,1.0,align=WD_ALIGN_PARAGRAPH.CENTER)
font(S['Footnote Text'],size=9)
# estilos propios (tablas y figuras APA)
def nuevo(nombre,base='Normal'):
    if nombre in S: return S[nombre]
    st=d.styles.add_style(nombre,1); st.base_style=S[base]; S[nombre]=st; return st
for nm,(b,i,sz,before,after,keep,al) in {
  'TablaRotulo':(True,False,11,14,0,True,WD_ALIGN_PARAGRAPH.LEFT),
  'TablaTitulo':(False,True,11,0,4,True,WD_ALIGN_PARAGRAPH.LEFT),
  'TablaNota':(False,False,9.5,3,10,False,WD_ALIGN_PARAGRAPH.LEFT),
  'FiguraRotulo':(True,False,11,14,0,True,WD_ALIGN_PARAGRAPH.LEFT),
  'FiguraTitulo':(False,True,11,0,4,True,WD_ALIGN_PARAGRAPH.LEFT),
  'FiguraNota':(False,False,9.5,2,12,False,WD_ALIGN_PARAGRAPH.LEFT)}.items():
    st=nuevo(nm); font(st,size=sz,bold=b,italic=i); para(st,before,after,1.0,keep=keep,align=al,indent=0)
for nm,sz in (('Tabla9',9),('Tabla8',8),('Tabla7',7),('Tabla65',6.3)):
    st=nuevo(nm,'Compact'); font(st,size=sz); para(st,0,0,1.0,indent=0,left=0,align=WD_ALIGN_PARAGRAPH.LEFT)
st=nuevo('Codigo','Normal'); font(st,'Courier New',6.5); para(st,0,0,1.0,indent=0)
if 'Source Code' not in S:
    st=nuevo('Source Code','Normal')
font(S['Source Code'],'Courier New',6.5); para(S['Source Code'],0,0,1.0)
for i,(sz,left,bf) in {1:(11,0,6),2:(11,0.6,0),3:(10,1.2,0)}.items():
    nm=f'TOC {i}'; st=nuevo(nm)
    font(st,size=sz,bold=(i==1)); para(st,bf,0,1.0,left=left,indent=0)
for nm in ('Indice','Indice2'):
    st=nuevo(nm); font(st,size=11); para(st,0,0,1.0,left=0,indent=0)
st=nuevo('CuerpoCompacto','Body Text'); font(st,size=11.5); para(st,0,4,1.12,indent=1.27,align=WD_ALIGN_PARAGRAPH.LEFT)
st=nuevo('Referencia','Normal'); font(st,size=12); para(st,0,0,'double',left=1.27,indent=-1.27,align=WD_ALIGN_PARAGRAPH.LEFT)
if 'Block Text' in S:
    font(S['Block Text'],size=11); para(S['Block Text'],6,6,1.15,left=1.27,indent=0,align=WD_ALIGN_PARAGRAPH.LEFT)
font(S['Source Code'],'Courier New',7.5); para(S['Source Code'],0,0,1.0,indent=0,left=0)
if 'Compact' in S: para(S['Compact'],0,0,1.0,indent=0,left=0)
for s in d.sections:
    s.page_width=Cm(21.59); s.page_height=Cm(27.94)
    s.left_margin=s.right_margin=Cm(2.54); s.top_margin=Cm(2.54); s.bottom_margin=Cm(2.54)
    s.header_distance=Cm(1.2); s.footer_distance=Cm(1.2)
d.save('reference_apa.docx'); print('ok')
