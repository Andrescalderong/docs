# -*- coding: utf-8 -*-
"""Deriva la versión radicable (sin la parte inicial de soporte) de las secciones 1 a 30 del Anexo 2."""
import os, re
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REEMP = [
 ("según la Tabla S.8 de la sección S.7", "según el presupuesto por actor del expediente"),
 ("La verificación de las Tablas S.15 a S.17 identifica", "La verificación presupuestal identifica"),
 ("Los ajustes pendientes de las Tablas S.15 a S.17 modificarían", "Los ajustes pendientes de la verificación presupuestal modificarían"),
 ("la ficha maestra y la sección S.8", "la ficha maestra y el expediente"),
 ("la matriz de responsabilidades de la sección S.6", "la matriz de responsabilidades del expediente"),
 ("en el expediente de formulación, que sigue a la sección 30", "en el expediente de formulación, que se entrega como soporte"),
 ("El expediente de formulación que sigue a esta sección contiene", "El expediente de formulación, entregado como soporte, contiene"),
 ("Incluido a continuación", "Soporte comprimido de hasta 10 MB"),
 ("Elaboración propia con el cronograma y la matriz de responsabilidades de la sección S.6.", "Elaboración propia con el cronograma y la matriz de responsabilidades del expediente."),
]
for n in ("a2a", "a2b", "a2c", "a2d"):
    t = open(os.path.join(RAIZ, "caps", n + ".md"), encoding="utf-8").read()
    for a, b in REEMP: t = t.replace(a, b)
    rest = re.findall(r".{30}\bS\.\d+.{20}", t)
    assert not rest, (n, rest[:3])
    open(os.path.join(RAIZ, "caps", n + "_r.md"), "w", encoding="utf-8").write(t)
print("ok")
