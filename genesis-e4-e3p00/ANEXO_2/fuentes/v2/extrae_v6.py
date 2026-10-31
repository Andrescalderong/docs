# -*- coding: utf-8 -*-
"""Extrae del Anexo 3 v6 el perfil de pagos (FC1) y el cronograma financiero a JSON.
Uso: python3 -I v2/extrae_v6.py anexo3.xlsx carpeta_salida"""
import sys, json, re, openpyxl
wb = openpyxl.load_workbook(sys.argv[1], data_only=True); out = sys.argv[2]
ws = wb["FC1. Perfil de pagos"]
hdr = {c.value: c.column for c in ws[6] if c.value is not None}
col = lambda n: hdr[n]
fc1 = []
for r in range(7, ws.max_row + 1):
    i = ws.cell(r, col("ID")).value
    if not (isinstance(i, str) and re.fullmatch(r"[A-Z]{2}-\d{2}", i)): continue
    if any(x["id"] == i for x in fc1): break          # solo el bloque A
    g = lambda n: ws.cell(r, col(n)).value
    d = dict(id=i, rubro=g("Rubro"), item=g("Ítem"), perfil=g("Perfil de pago"), total=g("Costo total (COP)"), sgr=g("SGR (COP)"),
             act=g("ENTRADA · Actividad principal"), ini=g("ENTRADA · Mes inicio"), fin=g("ENTRADA · Mes fin"), tipo=g("ENTRADA · Perfil (L/I/F/S/A/M)"),
             resp=g("ENTRADA · Entidad responsable (E1, E2…)"))
    for k in range(1, 6):
        d[f"ef{k}"] = g(f"Efectivo E{k}") or 0; d[f"es{k}"] = g(f"Especie E{k}") or 0
    fc1.append(d)
json.dump(fc1, open(f"{out}/fc1.json", "w"), ensure_ascii=False, indent=1, default=str)
ws = wb["Cronograma financiero"]
h = [c.value for c in ws[2]]
mcols = [j for j, v in enumerate(h) if isinstance(v, str) and re.fullmatch(r"Mes \d+", v)]
cr = []
for r in range(4, ws.max_row + 1):
    v = [c.value for c in ws[r]]
    if not (isinstance(v[1], str) and re.fullmatch(r"A\d\.\d", v[1]) and v[5]): continue
    mens = [float(v[j] or 0) for j in mcols]
    cr.append(dict(fila=r, oe=v[0], act=v[1], act_nombre=v[2], rubro=v[4], item=v[5], ini=v[7], fin=v[8], mensual=mens, valor=sum(mens)))
json.dump(cr, open(f"{out}/cronofin.json", "w"), ensure_ascii=False, indent=1, default=str)
print(len(fc1), "partidas;", len(cr), "filas de cronograma; suma", round(sum(x["valor"] for x in cr)), "; meses", len(mcols))
