# -*- coding: utf-8 -*-
"""Tabla de datos clave del documento 1000X-01 (resumen ejecutivo). Cifras de la ficha maestra y de maestro.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
from cX6_datos import tabla
V = {}; T = {}
I = C.M.IDENT
filas = [
    ["Título", I["titulo"], "Ficha maestra §1"],
    ["Convocatoria", I["convocatoria"], "Ficha maestra §1"],
    ["Financiador", "Sistema General de Regalías (SGR) y Ministerio de Ciencia, Tecnología e Innovación (MinCiencias)", "Ficha maestra §1"],
    ["Entidad ejecutora", "[DATO_USUARIO: nombre de la IES ejecutora]", "SUPUESTO"],
    ["Territorio", "Caldas, Cundinamarca y Valle del Cauca", "SUPUESTO"],
    ["Presupuesto total", f"COP {C.TOTAL:,.0f}".replace(",", "."), "CALCULADO"],
    ["Valor solicitado al SGR", f"COP {C.SGR:,.0f} ({C.pct(C.SGR / C.TOPE)} % del tope declarado)".replace(",", "."), "CALCULADO; tope NO_VERIFICADO"],
    ["Contrapartida", f"COP {C.CONTRA:,.0f}".replace(",", "."), "DECLARADO; desglose de la IES PROPUESTO"],
    ["Duración", "24 meses (104 semanas)", "CALCULADO por el método de la ruta crítica"],
    ["TRL inicial y final", "4 y 7; TRL 8 condicionado", "PROPUESTO"],
    ["Beneficiarios directos", "150 funcionarios en 15 comités de gestión del riesgo", "SUPUESTO"],
    ["ODS principal", "ODS 11: ciudades y comunidades sostenibles", "PROPUESTO"],
]
T["t01"] = tabla("t01", "Datos clave del proyecto",
                 ["Campo", "Valor", "Naturaleza o fuente"], filas,
                 "*Nota.* Elaboración propia con datos de la ficha maestra y de maestro.py. COP = pesos colombianos. La clasificación en el ODS 11 es PROPUESTA con base en la Agenda 2030. Decimales con coma.")
