# -*- coding: utf-8 -*-
"""Tablas del capítulo 18 (Marco Lógico), generadas desde indicadores.py (MARCO_LOGICO, IND), maestro.py (ACT, RISKS) y a11_datos.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11_datos as D
from a11_datos import cel, num, mm
from a11_tablas17 import bloque

CORTO = {"PERS-S01": "activación del protocolo", "PERS-S02": "continuidad de la red", "PERS-E01": "uso institucional",
         "PERS-E02": "falsas alarmas", "PERS-E03": "capacidad en custodios", "PERS-P01": "red operativa (nodos y gateways)",
         "PERS-P02": "software registrado", "PERS-P03": "artículos", "PERS-P04": "apropiación social", "PERS-R01": "despliegue",
         "PERS-R02": "ciclos de calibración", "PERS-R03": "plataforma en la nube", "PERS-R04": "ejecución presupuestal",
         "PERS-R05": "horas-nodo", "PERS-R06": "informes"}

def _ind_txt(niv):
    return "; ".join(f"{c} {CORTO[c]}: {D.meta_ind(c)}" for c in D.NIVEL_IND[niv])

def t18_matriz():
    filas = []
    for niv in ("Fin", "Propósito", "Componentes", "Actividades"):
        ml = D.I.MARCO_LOGICO[niv]
        if niv == "Actividades":
            res = "; ".join(f"{wp} {D.WP_NOMBRE[wp]} ({len(D.ACT_WP[wp])} actividades)" for wp in D.ACT_WP)
        else:
            res = D.ml_res(niv)
        filas.append([niv, res, _ind_txt(niv), ml["med"], ml["sup"]])
    return bloque("t01", "Matriz de marco lógico 4 × 4 del proyecto",
                  ["Nivel", "Resumen narrativo", "Indicadores y metas finales", "Medios de verificación", "Supuestos"], filas,
                  "*Nota.* Elaboración propia con MARCO_LOGICO e IND (indicadores.py) y la red de actividades ACT (maestro.py). Los componentes se numeran 1 a 3 para no confundirlos con las compuertas C1 y C2. Naturaleza: metas PROPUESTO; líneas base en la ficha de cada indicador.")

SC_RIESGO = {"R-TEC-01": "SC-1", "R-TEC-04": "SC-1", "R-TEC-02": "SC-2", "R-TEC-03": "SC-2", "R-ORG-01": "SC-3", "R-DAT-01": "SC-3", "R-ORG-02": "SC-4"}

def t18_supuestos():
    filas = []
    for niv, ids in D.NIVEL_RIESGO.items():
        sup = D.I.MARCO_LOGICO[niv]["sup"]
        for k, rid in enumerate(ids):
            r = D.RK[rid]
            filas.append([niv if k == 0 else "Ídem", sup if k == 0 else "Ídem", f"{rid}: {r['desc']}", SC_RIESGO.get(rid, "—"),
                          f"{r['P']} × {r['I']} = {r['score']} ({r['nivel']})", num(r["emv"] / D.MM), f"{r['estrategia']}: {r['respuesta']}"])
        filas.append([f"Subtotal {niv}", "—", f"{len(ids)} {'riesgo' if len(ids) == 1 else 'riesgos'}", "—", "—", num(D.emv_nivel(niv)), "—"])
    tot = sum(r["emv"] for r in D.M.RISKS) / D.MM
    filas.append(["Total", "—", f"{len(D.M.RISKS)} riesgos", "—", "—", num(tot), f"La reserva de contingencia redondea a {mm(D.M.RESERVA)}"])
    return bloque("t02", "Análisis de supuestos y riesgos por nivel del marco lógico",
                  ["Nivel", "Supuesto del nivel", "Riesgo asociado", "SC", "P × I (nivel)", "EMV (M COP)", "Estrategia y respuesta"], filas,
                  "*Nota.* Elaboración propia con RISKS (maestro.py) e indicadores.py. La asignación de cada riesgo a un nivel y a un supuesto crítico (SC-1 a SC-4) es PROPUESTO. P: probabilidad; I: impacto; EMV: valor monetario esperado, en millones de pesos colombianos (M COP), sin redondeo. Decimales con coma.")

def t18_pruebas():
    filas = [[p["id"], p["tipo"], p["regla"], p["evidencia"], p["estado"], p["accion"]] for p in D.PRUEBAS]
    return bloque("t03", "Resultado de las ocho pruebas de coherencia del marco lógico",
                  ["Prueba", "Tipo", "Regla verificada", "Evidencia calculada", "Estado", "Acción"], filas,
                  "*Nota.* Elaboración propia; las pruebas se calculan con a11_datos.pruebas() sobre IND, MARCO_LOGICO, ACT y RISKS. Las ocho pruebas son PROPUESTO porque la especificación no las enumera. Estados: CUMPLE, PARCIAL, NO CUMPLE.")

def todas():
    return {"t01": t18_matriz(), "t02": t18_supuestos(), "t03": t18_pruebas()}

if __name__ == "__main__":
    for k, v in todas().items():
        print(v); print()
