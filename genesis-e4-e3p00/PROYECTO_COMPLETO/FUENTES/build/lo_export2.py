# -*- coding: utf-8 -*-
"""Exporta DOCX a PDF con marcadores y devuelve (JSON) la página de cada marcador rot_* mediante el cursor de vista de LibreOffice."""
import subprocess, time, sys, os, json, uno
from com.sun.star.beans import PropertyValue
src, outpdf, outjson = map(os.path.abspath, sys.argv[1:4])
port = 2004
prof = '/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy/build/lo_profile'
p = subprocess.Popen(['soffice', '--headless', '--norestore', '--nologo', f'-env:UserInstallation=file://{prof}',
                      f'--accept=socket,host=localhost,port={port};urp;'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
ctx = None
for i in range(120):
    try:
        local = uno.getComponentContext()
        res = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
        ctx = res.resolve(f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext'); break
    except Exception:
        time.sleep(1)
assert ctx, 'sin conexion'
desk = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
def pv(n, v):
    x = PropertyValue(); x.Name = n; x.Value = v; return x
doc = desk.loadComponentFromURL('file://' + src, '_blank', 0, (pv('Hidden', True),))
pages = {}
try:
    vc = doc.getCurrentController().getViewCursor()
    bms = doc.getBookmarks()
    for nm in bms.getElementNames():
        if nm.startswith('rot_'):
            a = bms.getByName(nm).getAnchor()
            vc.gotoRange(a, False)
            pages[nm] = vc.getPage()
except Exception as e:
    print('aviso: no se obtuvieron páginas de marcadores:', e)
fd = uno.Any('[]com.sun.star.beans.PropertyValue', (pv('UseLosslessCompression', False), pv('Quality', 70), pv('ReduceImageResolution', True),
                                                      pv('MaxImageResolution', 150), pv('ExportBookmarks', True), pv('UseTaggedPDF', True),
                                                      pv('ExportBookmarksToPDFDestination', True)))
uno.invoke(doc, 'storeToURL', ('file://' + outpdf, (pv('FilterName', 'writer_pdf_Export'), pv('FilterData', fd))))
doc.close(True)
try: desk.terminate()
except Exception: pass
p.wait(timeout=120)
json.dump(pages, open(outjson, 'w'))
print('marcadores con página:', len(pages))
