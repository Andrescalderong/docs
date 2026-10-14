# -*- coding: utf-8 -*-
"""Endurece el DOCX para Word: marcadores ASCII sin guiones ni puntos, estilo TableNormal, sin partes vacías."""
import sys, re, zipfile

TN = ('<w:style w:type="table" w:styleId="TableNormal"><w:name w:val="Normal Table"/><w:uiPriority w:val="99"/>'
      '<w:semiHidden/><w:unhideWhenUsed/><w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar>'
      '<w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/>'
      '<w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>')

def fix(src, dst):
    zi = zipfile.ZipFile(src); zo = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
    for it in zi.infolist():
        b = zi.read(it.filename)
        if it.filename == 'word/document.xml':
            s = b.decode('utf8'); mp = {}
            def rn(m):
                n = m.group(2)
                if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', n): return m.group(0)
                mp.setdefault(n, '_Toc%08d' % (900000 + len(mp) + 1))
                return m.group(1) + mp[n] + '"'
            s = re.sub(r'(<w:bookmarkStart w:id="\d+" w:name=")([^"]*)"', rn, s)
            s = re.sub(r'(w:anchor=")([^"]*)"', lambda m: m.group(1) + mp.get(m.group(2), m.group(2)) + '"', s)
            b = s.encode('utf8'); print('marcadores renombrados:', len(mp))
        elif it.filename == 'word/styles.xml':
            s = b.decode('utf8')
            if 'w:styleId="TableNormal"' not in s:
                i = s.find('<w:style w:default="1" w:styleId="Table"')
                if i < 0: i = s.find('<w:style ', s.find('</w:latentStyles>') if '</w:latentStyles>' in s else 0)
                s = s[:i] + TN + s[i:]
            b = s.encode('utf8')
        zo.writestr(it, b) if False else zo.writestr(it.filename, b)
    zo.close()

if __name__ == '__main__': fix(sys.argv[1], sys.argv[2])
