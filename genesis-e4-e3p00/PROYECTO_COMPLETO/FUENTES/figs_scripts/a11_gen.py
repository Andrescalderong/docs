# -*- coding: utf-8 -*-
"""Generador de los capítulos 17, 18, 20 y 21 (asignación A11).
Lee una plantilla de prosa (con marcas @@TABLA id@@ y <<VALOR>>), inserta las tablas generadas desde maestro.py e indicadores.py
y escribe RAIZ/caps/capNN.md. Uso: python3 a11_gen.py 17 [18 20 21]   (las plantillas están en la carpeta a11 del espacio de trabajo)."""
import os, sys, re, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11_datos as D

TPL = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a11"
CAPS = os.path.join(D.RAIZ, "caps")

def valores(cap):
    mod = importlib.import_module(f"a11_valores")
    return mod.valores(cap)

def generar(cap):
    tpl = open(os.path.join(TPL, f"cap{cap}.tpl"), encoding="utf-8").read()
    tablas = importlib.import_module(f"a11_tablas{cap}").todas()
    vals = valores(cap)
    usados = set()
    def rt(m):
        k = m.group(1)
        usados.add(k)
        return tablas[k]
    out = re.sub(r"@@TABLA (\S+)@@", rt, tpl)
    def rv(m):
        k = m.group(1)
        if k not in vals: raise KeyError(f"valor sin definir: {k}")
        return str(vals[k])
    out = re.sub(r"<<([A-Za-z0-9_]+)>>", rv, out)
    sin = set(tablas) - usados
    if sin: print(f"AVISO cap{cap}: tablas sin usar {sorted(sin)}")
    ruta = os.path.join(CAPS, f"cap{cap}.md")
    open(ruta, "w", encoding="utf-8").write(out)
    print("escrito", ruta, len(out.split()), "palabras brutas")

if __name__ == "__main__":
    for c in sys.argv[1:]: generar(c)
