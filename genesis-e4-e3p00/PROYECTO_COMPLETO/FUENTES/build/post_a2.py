# -*- coding: utf-8 -*-
"""Posprocesado Word en el formato oficial del Anexo 2 (Convocatoria 56 del SGR): encabezado y pie de la plantilla,
Arial, tablas con encabezado verde 00B050 y bordes negros, portada con banner verde."""
import docx, re
from docx.oxml.ns import qn, nsdecls
from docx.oxml import OxmlElement, parse_xml
from xml.sax.saxutils import escape
import post_apa as PA

VERDE = '00B050'; BANNER = '2F633A'
MARG = 1133   # márgenes laterales de la plantilla (twips)

def tabla_a2(tbl, styles_id):
    n = PA.ncols(tbl)
    tblPr = tbl.find(qn('w:tblPr'))
    for tag in ('w:tblBorders', 'w:tblCellMar', 'w:tblLayout'):
        for old in tblPr.findall(qn(tag)): tblPr.remove(old)
    b = ''.join(f'<w:{e} w:val="single" w:sz="6" w:space="0" w:color="000000"/>' for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
    tblPr.append(parse_xml(f'<w:tblBorders {nsdecls("w")}>{b}</w:tblBorders>'))
    tblPr.append(parse_xml(f'<w:tblCellMar {nsdecls("w")}><w:top w:w="30" w:type="dxa"/><w:left w:w="70" w:type="dxa"/><w:bottom w:w="30" w:type="dxa"/><w:right w:w="70" w:type="dxa"/></w:tblCellMar>'))
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    st = 'Tabla9' if n <= 6 else ('Tabla8' if n <= 10 else ('Tabla7' if n <= 14 else 'Tabla65'))
    if re.search(r'[0-9a-f]{64}', ''.join(x.text or '' for x in tbl.iter(qn('w:t')))) and n < 9: st = 'Tabla8'
    rows = tbl.findall(qn('w:tr'))
    for ri, tr in enumerate(rows):
        trPr = tr.find(qn('w:trPr'))
        if trPr is None: trPr = OxmlElement('w:trPr'); tr.insert(0, trPr)
        if trPr.find(qn('w:cantSplit')) is None: trPr.append(OxmlElement('w:cantSplit'))
        if ri == 0 and trPr.find(qn('w:tblHeader')) is None: trPr.append(OxmlElement('w:tblHeader'))
        for tc in tr.findall(qn('w:tc')):
            if ri == 0: PA.shade(tc, VERDE)
            for p in tc.findall(qn('w:p')):
                pPr = p.find(qn('w:pPr'))
                if pPr is None: pPr = OxmlElement('w:pPr'); p.insert(0, pPr)
                ps = pPr.find(qn('w:pStyle'))
                if ps is None: ps = OxmlElement('w:pStyle'); pPr.insert(0, ps)
                ps.set(qn('w:val'), styles_id[st])
                if ri == 0:
                    for old in pPr.findall(qn('w:jc')): pPr.remove(old)
                    jc = OxmlElement('w:jc'); jc.set(qn('w:val'), 'center'); pPr.append(jc)
                    for r in p.findall(qn('w:r')):
                        rPr = r.find(qn('w:rPr'))
                        if rPr is None: rPr = OxmlElement('w:rPr'); r.insert(0, rPr)
                        if rPr.find(qn('w:b')) is None: rPr.append(OxmlElement('w:b'))
                        for old in rPr.findall(qn('w:color')): rPr.remove(old)
                        c = OxmlElement('w:color'); c.set(qn('w:val'), 'FFFFFF'); rPr.append(c)

def sect_xml(land, refs):
    if land:
        sz = '<w:pgSz w:w="15840" w:h="12240" w:orient="landscape"/>'
    else:
        sz = '<w:pgSz w:w="12240" w:h="15840"/>'
    return (f'<w:sectPr>{refs}{sz}<w:pgMar w:top="1417" w:right="{MARG}" w:bottom="1417" w:left="{MARG}" '
            f'w:header="709" w:footer="709" w:gutter="0"/></w:sectPr>')

def mk_sect_par(land, refs):
    return parse_xml(f'<w:p {nsdecls("w", "r")}><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/>{sect_xml(land, refs)}</w:pPr></w:p>')

def _p(texto, bold=False, size=22, color=None, jc='both', shd=None, before=0, after=120, left=None, hang=None, italic=False):
    rpr = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>' + ('<w:b/><w:bCs/>' if bold else '') + ('<w:i/>' if italic else '') + \
          (f'<w:color w:val="{color}"/>' if color else '') + f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    ppr = f'<w:keepNext/>' if bold else ''
    if shd: ppr += f'<w:shd w:val="clear" w:color="auto" w:fill="{shd}"/>'
    ppr += f'<w:spacing w:before="{before}" w:after="{after}"/>'
    if left is not None: ppr += f'<w:ind w:left="{left}" w:hanging="{hang or 0}"/>'
    ppr += f'<w:jc w:val="{jc}"/>'
    return parse_xml(f'<w:p {nsdecls("w")}><w:pPr>{ppr}</w:pPr><w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(texto)}</w:t></w:r></w:p>')

def portada_a2(d, body, opts):
    sdt = body.find(qn('w:sdt')); anchor = sdt if sdt is not None else body[0]
    def add(el): anchor.addprevious(el)
    add(_p('', after=120))
    add(_p('CONVOCATORIA DE EMERGENCIA PARA LA RECUPERACIÓN Y GENERACIÓN DE CAPACIDADES TRANSFORMADORAS, EN EL MARCO DEL DECRETO 1414 DE 17 DE SEPTIEMBRE DE 2026.',
           bold=True, color='FAFAFA', jc='center', shd=BANNER, after=240, before=120))
    add(_p('ANEXO 2. DOCUMENTO TÉCNICO', bold=True, jc='center', after=360))
    add(_p(opts.get('titulo', ''), bold=True, size=26, jc='center', after=120))
    if opts.get('subtitulo'): add(_p(opts['subtitulo'], bold=True, size=22, jc='center', after=360))
    for kind, txt, kw in opts.get('portada', []):
        if kind == 'p': add(_p(txt, bold=kw.get('bold', False), size=2 * kw.get('size', 11), jc='center', after=120))
    add(_p('Notas:', bold=True, jc='left', before=240))
    for n in opts.get('notas', []):
        color = n[0]; t = n[1]
        add(_p('●  ' + t, color=color, jc='both', left=426, hang=426, after=100))
    add(parse_xml(f'<w:p {nsdecls("w")}><w:r><w:br w:type="page"/></w:r></w:p>'))

def postprocesar(src, dst, opts, wide_cols=12):
    d = docx.Document(src); body = d.element.body
    styles_id = {s.name: s.style_id for s in d.styles}
    for lvl in d.part.numbering_part.element.iter(qn('w:lvl')):
        ppr = lvl.find(qn('w:pPr'))
        if ppr is None: continue
        ind = ppr.find(qn('w:ind'))
        if ind is None: continue
        il = int(lvl.get(qn('w:ilvl')))
        ind.set(qn('w:left'), str(567 + 340 * il)); ind.set(qn('w:hanging'), '283')
        if ind.get(qn('w:firstLine')) is not None: del ind.attrib[qn('w:firstLine')]
    for t in body.findall(qn('w:tbl')): tabla_a2(t, styles_id)
    fin = body.find(qn('w:sectPr'))
    from lxml import etree
    refs = ''.join(etree.tostring(r, encoding='unicode') for r in fin if r.tag in (qn('w:headerReference'), qn('w:footerReference')))
    refs = re.sub(r'\sxmlns:\w+="[^"]*"', '', refs)
    children = list(body)
    wide = [i for i, el in enumerate(children) if el.tag == qn('w:tbl') and PA.ncols(el) >= wide_cols]
    for i in sorted(wide, reverse=True):
        el = children[i]; first = el; j = i - 1
        while j >= 0 and children[j].tag == qn('w:p') and children[j].find(qn('w:pPr')) is not None and \
                children[j].find(qn('w:pPr')).find(qn('w:pStyle')) is not None and \
                children[j].find(qn('w:pPr')).find(qn('w:pStyle')).get(qn('w:val')) in (styles_id['TablaRotulo'], styles_id['TablaTitulo']):
            first = children[j]; j -= 1
        last = el; nx = el.getnext()
        if nx is not None and nx.tag == qn('w:p') and nx.find(qn('w:pPr')) is not None and nx.find(qn('w:pPr')).find(qn('w:pStyle')) is not None \
                and nx.find(qn('w:pPr')).find(qn('w:pStyle')).get(qn('w:val')) == styles_id['TablaNota']:
            last = nx
        first.addprevious(mk_sect_par(False, refs)); last.addnext(mk_sect_par(True, refs))
    portada_a2(d, body, opts)
    for fc in body.iter(qn('w:fldChar')):
        if fc.get(qn('w:dirty')) is not None: del fc.attrib[qn('w:dirty')]
    for jc in body.iter(qn('w:jc')):
        v = jc.get(qn('w:val'))
        if v in ('start', 'end'): jc.set(qn('w:val'), 'left' if v == 'start' else 'right')
    PA.reorder(d.element); PA.reorder(d.settings.element); PA.reorder(d.styles.element)
    for rp in d.styles.element.iter(qn('w:rPr')):
        for k in rp:
            if k.tail and k.tail.strip(): k.tail = None
    for ns_ in d.part.numbering_part.element.iter(qn('w:nsid'), qn('w:tmpl')):
        v = ns_.get(qn('w:val'))
        if len(v) != 8: ns_.set(qn('w:val'), v.upper().zfill(8))
    cp = d.core_properties
    cp.title = opts.get('titulo', 'Anexo 2. Documento técnico'); cp.subject = 'Convocatoria 56 del SGR · GENESIS-CTeI 36.10 RC2'; cp.author = ''; cp.language = 'es-CO'
    d.save(dst)
    return dst
