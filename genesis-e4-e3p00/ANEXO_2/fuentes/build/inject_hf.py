# -*- coding: utf-8 -*-
"""Inyecta el encabezado y el pie oficiales de la plantilla del Anexo 2 en un documento de referencia de pandoc."""
import zipfile, re, shutil, sys
base, tpl, out = sys.argv[1:4]
zt = zipfile.ZipFile(tpl); zb = zipfile.ZipFile(base)
files = {n: zb.read(n) for n in zb.namelist()}
for n in ('word/header2.xml', 'word/footer2.xml', 'word/_rels/header2.xml.rels', 'word/_rels/footer2.xml.rels',
          'word/media/image1.png', 'word/media/image2.png', 'word/media/image3.png'):
    files[n] = zt.read(n)
# interlineado sencillo en encabezado y pie, para que no dependa del estilo Normal del documento de referencia
for n in ('word/header2.xml', 'word/footer2.xml'):
    x = files[n].decode('utf-8')
    x = x.replace('</w:tabs><w:ind', '</w:tabs><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:ind')
    if n == 'word/footer2.xml':
        # número de página en posición fija (no centrado en el texto) para que no choque con el logo en las páginas apaisadas
        x = x.replace('<w:ind w:hanging="2"/><w:jc w:val="center"/>', '<w:ind w:left="4000" w:firstLine="0"/><w:jc w:val="left"/>')
        # el primer párrafo ancla el cuadro con la dirección (alto 24,7 pt); altura exacta para que el resto del pie quede debajo en Word y en LibreOffice
        x = x.replace('w:line="240" w:lineRule="auto"/>', 'w:line="520" w:lineRule="exact"/>', 1)
    files[n] = x.encode('utf-8')
ct = files['[Content_Types].xml'].decode('utf-8')
add = ''
if 'Extension="png"' not in ct: add += '<Default Extension="png" ContentType="image/png"/>'
add += ('<Override PartName="/word/header2.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
        '<Override PartName="/word/footer2.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>')
ct = ct.replace('</Types>', add + '</Types>'); files['[Content_Types].xml'] = ct.encode('utf-8')
rels = files['word/_rels/document.xml.rels'].decode('utf-8')
rels = rels.replace('</Relationships>',
    '<Relationship Id="rIdHdrOf" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header2.xml"/>'
    '<Relationship Id="rIdFtrOf" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer2.xml"/></Relationships>')
files['word/_rels/document.xml.rels'] = rels.encode('utf-8')
doc = files['word/document.xml'].decode('utf-8')
m = re.search(r'<w:sectPr[^>]*>', doc)
assert m, 'sin sectPr'
if 'xmlns:r=' not in doc[:600]:
    doc = doc.replace('<w:document ', '<w:document xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" ', 1)
    m = re.search(r'<w:sectPr[^>]*>', doc)
doc = doc[:m.end()] + '<w:headerReference w:type="default" r:id="rIdHdrOf"/><w:footerReference w:type="default" r:id="rIdFtrOf"/>' + doc[m.end():]
files['word/document.xml'] = doc.encode('utf-8')
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    for n, b in files.items(): z.writestr(n, b)
print('ok', out)
