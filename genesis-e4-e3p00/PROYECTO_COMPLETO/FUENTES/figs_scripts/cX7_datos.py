# -*- coding: utf-8 -*-
"""Tablas del documento 1000X-07 (roadmap tecnológico). Datos de la ficha maestra; carriles y horizontes PROPUESTOS."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cX6_datos import tabla
V = {}; T = {}
filas = [
    ["Mercado y necesidades", "Línea base de error por departamento y umbrales locales en co-diseño", "Uso del tablero por 15 comités (≥ 75 % al mes 24) y convenios con partida",
     "Activación del protocolo (≥ 80 %) y continuidad de la red (≥ 70 %), medidas tras el cierre", "Otras zonas de posdesastre y otras redes, condicionado a TdR y custodios"],
    ["Productos y servicios", "Versión 1.0: 30 nodos, 3 gateways, modelo de corrección y tablero piloto", "Versión 2.0 (70 nodos, mes 17) y versión 3.0 (100 nodos y 10 gateways, mes 19); registro DNDA",
     "Versión 3.x operada por custodios y evaluación externa posproyecto", "Opciones sin presupuestar: más nodos, un cuarto tramo y un año adicional de custodia"],
    ["Tecnologías", "Actuales: sensor óptico, LoRa, celular y solar. A desarrollar: corrección en el gateway", "Reentrenamiento por departamento, enlace satelital alterno y ensayo independiente",
     "Mantenimiento del modelo con datos de la custodia", "A evaluar con evidencia: corrección en el nodo (fuera de alcance, DEC-F02)"],
    ["Recursos y capacidades", "Equipo contratado (mes 2), 3 referencias gravimétricas y banco de calibración", "60 personas certificadas y 29 actividades de apropiación social",
     "Custodios con partida y competencia (≥ 70 % a 12 meses)", "Alianzas: comités, UNGRD, alcaldías, custodios y laboratorios"],
]
T["t01"] = tabla("t01", "Matriz de carriles y horizontes del roadmap tecnológico",
                 ["Carril", "Año 1 (meses 1 a 12)", "Años 2 y 3: meses 13 a 24", "Años 2 y 3: meses 25 a 36", "Años 4 y 5 o más"], filas,
                 "*Nota.* Elaboración propia con datos de la ficha maestra e indicadores PERS. Naturaleza: PROPUESTO. El seguimiento de los meses 25 a 36 y los años 4 y 5 son PROPUESTOS o condicionados a los términos de referencia.")
filas = [
    ["4", "Validación de componentes en laboratorio", "Caracterización de nodos y referencias en el banco de calibración", "Inicio y H1", "0 a 4", "DECLARADO (TRL inicial)"],
    ["5", "Validación de componentes en entorno relevante", "Línea base de error medida; NRMSE y R² frente a referencia en el piloto", "H2 y C1", "10 y 12", "PROPUESTO"],
    ["6", "Demostración de prototipo en entorno relevante", "Tramo 2 verificado; uso del tablero y convenios de custodia", "H4 y C2", "16 y 17", "PROPUESTO"],
    ["7", "Demostración de prototipo en entorno operativo", "Inventario de 100 nodos y 10 gateways; ensayo independiente", "H6, H7 y H8", "19, 23 y 24", "PROPUESTO (TRL final)"],
    ["8", "Sistema completo calificado", "Evaluación de desempeño independiente con calificación", "Posterior al cierre", "Después del mes 24", "PROPUESTO (condicionado)"],
]
T["t02"] = tabla("t02", "Escala TRL del proyecto con evidencia de salida, hito y mes",
                 ["TRL", "Definición", "Evidencia de salida", "Hito o compuerta", "Mes", "Naturaleza"], filas,
                 "*Nota.* Elaboración propia con definiciones de Mankins (1995) y con hitos de la ficha maestra. El TRL 8 está condicionado a una evaluación independiente que el plazo no cubre (DEC-F05).")
