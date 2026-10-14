# -*- coding: utf-8 -*-
"""Reescribe un DOCX con LibreOffice (filtro MS Word 2007 XML)."""
import subprocess, time, sys, os, uno
from com.sun.star.beans import PropertyValue
src, dst = map(os.path.abspath, sys.argv[1:3])
port = 2005
prof = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lo_profile')
p = subprocess.Popen(['soffice', '--headless', '--norestore', '--nologo', f'-env:UserInstallation=file://{prof}',
                      f'--accept=socket,host=localhost,port={port};urp;'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
ctx = None
for i in range(120):
    try:
        local = uno.getComponentContext()
        res = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
        ctx = res.resolve(f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext'); break
    except Exception: time.sleep(1)
assert ctx
desk = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
def pv(n, v):
    x = PropertyValue(); x.Name = n; x.Value = v; return x
doc = desk.loadComponentFromURL('file://' + src, '_blank', 0, (pv('Hidden', True),))
doc.storeToURL('file://' + dst, (pv('FilterName', 'MS Word 2007 XML'),))
doc.close(True)
try: desk.terminate()
except Exception: pass
p.wait(timeout=120); print('ok')
