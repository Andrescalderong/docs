# -*- coding: utf-8 -*-
"""Tabla de pie del one-pager (documento 1000X-02). Cifras de la ficha maestra y de maestro.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
from cX6_datos import tabla
V = {}; T = {}
cop = lambda v: "COP " + f"{v:,.0f}".replace(",", ".")
filas = [[f"{cop(C.TOTAL)}; SGR {cop(C.SGR)[4:]}", "24 meses", "4 a 7", "150 funcionarios directos"]]
T["t01"] = tabla("t01", "Cifras de pie del proyecto",
                 ["Presupuesto", "Duración", "TRL", "Beneficiarios"], filas,
                 "*Nota.* Elaboración propia con datos de la ficha maestra y de maestro.py. Presupuesto CALCULADO; duración CALCULADA por el método de la ruta crítica; TRL PROPUESTO; beneficiarios SUPUESTOS. COP = pesos colombianos.")
