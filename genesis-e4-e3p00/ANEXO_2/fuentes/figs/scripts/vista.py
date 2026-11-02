# -*- coding: utf-8 -*-
"""Genera vistas JPG sobre fondo blanco (con A2/figs/ver.py) en el directorio de trabajo temporal para revisar las figuras."""
import sys, os
sys.path.insert(0, "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs")
import ver
OUT = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a2/figs/out/"
V = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/vistas/"
os.makedirs(V, exist_ok=True)
for n in sys.argv[1:]:
    print(ver.ver(OUT + n + ".png", out=V + n + ".jpg", ancho=1700))
