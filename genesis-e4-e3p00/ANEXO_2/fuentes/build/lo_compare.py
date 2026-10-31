# -*- coding: utf-8 -*-
"""Compara una versión nueva (abierta) con la anterior y guarda un DOCX con control de cambios.
Uso: python3 lo_compare.py nuevo.docx anterior.docx salida.docx"""
import subprocess, time, sys, os, uno
from com.sun.star.beans import PropertyValue
nuevo, anterior, salida = map(os.path.abspath, sys.argv[1:4])
port = int(os.environ.get('LO_PORT', '2016'))
prof = '/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/build/lo_profile2'
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
smgr = ctx.ServiceManager
desk = smgr.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
def pv(n, v):
    x = PropertyValue(); x.Name = n; x.Value = v; return x
doc = desk.loadComponentFromURL('file://' + nuevo, '_blank', 0, (pv('Hidden', True),))
disp = smgr.createInstanceWithContext('com.sun.star.frame.DispatchHelper', ctx)
frame = doc.getCurrentController().getFrame()
t0 = time.time()
disp.executeDispatch(frame, '.uno:CompareDocuments', '', 0, (pv('URL', 'file://' + anterior), pv('NoAcceptDialog', True)))
print('comparación en', round(time.time() - t0), 's; cambios:', doc.getRedlines().createEnumeration().hasMoreElements())
doc.storeToURL('file://' + salida, (pv('FilterName', 'MS Word 2007 XML'),))
doc.close(True)
try: desk.terminate()
except Exception: pass
p.wait(timeout=120)
