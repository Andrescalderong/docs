# -*- coding: utf-8 -*-
"""Orden de ensamblado del documento único. Genera out/lista_proyecto.json con los archivos que existen."""
import os, json, sys
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
C = RAIZ + "/caps/"
ORDEN = [
 ("front.md", "raw"), ("div_parte1.md", "raw"),
 ("paso0.md", "cap"), ("paso1.md", "cap"), ("paso2.md", "cap"), ("paso3.md", "cap"), ("paso4.md", "cap"), ("paso5.md", "cap"), ("paso6.md", "cap"), ("paso7.md", "cap"),
 ("div_parte2.md", "raw"),
 ("cap01.md", "cap"), ("cap02a.md", "cap"), ("cap02b.md", "cap"), ("cap03.md", "cap"), ("cap04.md", "cap"), ("cap05.md", "cap"), ("cap06.md", "cap"),
 ("cap07.md", "cap"), ("cap08.md", "cap"), ("cap09.md", "cap"), ("cap10.md", "cap"), ("cap11.md", "cap"), ("cap12.md", "cap"), ("cap13.md", "cap"),
 ("cap14.md", "cap"), ("cap15.md", "cap"), ("cap16.md", "cap"), ("cap17.md", "cap"), ("cap18.md", "cap"), ("cap19.md", "cap"),
 ("cap20.md", "cap"), ("anexos_km.md", "cap"), ("cap21.md", "cap"),
 ("div_parte3.md", "raw"),
 ("x01.md", "cap"), ("x02.md", "cap"), ("x03.md", "cap"), ("estrategia.md", "cap"), ("x05.md", "cap"), ("x06.md", "cap"), ("x07.md", "cap"), ("x08.md", "cap"), ("x09.md", "cap"), ("x10.md", "cap"),
 ("div_cierre.md", "raw"), ("cierre.md", "cap"),
]
def lista(solo_existentes=True):
    return [[C + f, t] for f, t in ORDEN if (os.path.exists(C + f) or not solo_existentes)]
if __name__ == "__main__":
    opts = json.load(open(sys.argv[1], encoding="utf-8")) if len(sys.argv) > 1 else {}
    out = {"entradas": lista(), "opts": opts}
    json.dump(out, open(RAIZ + "/out/lista_proyecto.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(out["entradas"]), "archivos")
