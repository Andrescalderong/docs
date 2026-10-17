# -*- coding: utf-8 -*-
import sys, re
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/figs/scripts"); sys.path.insert(0, RAIZ + "/maestro")
import c12_tablas as T
import c12_datos as D
import maestro as M
B = {l["id"]: l for l in M.BUDGET}
def mm(x, d=1): return M.mm(x, d)
def suma(ids): return sum(B[i]["total"] for i in ids)
rub = D.RUB if hasattr(D, "RUB") else None
ind = D.IND
# líneas de PERS-P01 definidas en c12_datos
import importlib
src = open(RAIZ + "/figs/scripts/c12_datos.py", encoding="utf-8").read()
m = re.search(r'"PERS-P01": dict\(prod=\[[^\]]*\], act=\[[^\]]*\], hitos=\[[^\]]*\], rub=\[([^\]]*)\]\)', src)
rub_p01 = re.findall(r'"([A-Z]\d\d)"', m.group(1))
V = {
 "R03_H": f"{0.01 * 720:.1f}".replace(".", ","),
 "R04_TOL": mm(0.05 * M.total(M.BUDGET)),
 "SGR": mm(M.total(M.BUDGET)),
 "RES": mm(M.RESERVA),
 "R05_POS": f"{30 * 16 * 168:,}".replace(",", "."),
 "R05_FRAC": f"{60000 / (30 * 16 * 168) * 100:.1f}".replace(".", ","),
 "R05_75": f"{int(0.75 * 30 * 16 * 168):,}".replace(",", "."),
 "R05_MARG": f"{int(0.75 * 30 * 16 * 168) - 60000:,}".replace(",", "."),
 "P01_M": mm(suma(rub_p01)),
 "P02_M": mm(suma(["O03", "S02"])),
 "DEV_P": mm(suma(["P03", "P08", "P12"])),
 "P03_M": mm(suma(["O01"])),
 "P04_M": mm(suma(["M05", "V05", "O02"])),
 "S09": mm(suma(["S09"])),
 "E03_C": mm(suma(["S09"]) / 60, 2),
}
t = open(RAIZ + "/figs/scripts/c12_plantilla.txt", encoding="utf-8").read()
t = re.sub(r"<<T:(t\d\d)>>", lambda m: T.TABLAS[m.group(1)], t)
t = re.sub(r"<<V:([A-Z0-9_]+)>>", lambda m: V[m.group(1)], t)
assert "<<" not in t
open(RAIZ + "/caps/cap12.md", "w", encoding="utf-8").write(t)
print("ok", V)
