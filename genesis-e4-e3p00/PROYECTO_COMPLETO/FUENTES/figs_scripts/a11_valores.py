# -*- coding: utf-8 -*-
"""Valores calculados que las plantillas de prosa insertan con <<NOMBRE>> (asignación A11). Todo sale de maestro.py e indicadores.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a11_datos as D
from a11_datos import num, mm, pct

PAL = {0: "cero", 1: "un", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}

def pal(n):
    """Palabras del cero al nueve y cifras desde 10 (regla de números del brief)."""
    return PAL[n] if n in PAL else str(n)

def valores(cap):
    M = D.M; R = D.RES; B = D.B
    v = {}
    # personal
    v["N_PERS"] = D.N_PERS; v["PM_TOT"] = D.PM_TOT; v["ETC_PROM"] = num(D.ETC_PROM, 1)
    v["N_CPERS"] = D.N_CPERS; v["ETC_CPERS"] = num(D.ETC_CPERS, 1)
    tec = [p for p in D.PERS if p["id"] not in ("P01", "P02")]
    v["N_TEC"] = sum(p["n"] for p in tec); v["PM_TEC"] = sum(p["pm"] for p in tec)
    v["PM_EST"] = D.PM_TOT - v["PM_TEC"]
    v["PCT_PM_TEC"] = pct(v["PM_TEC"] / D.PM_TOT); v["PCT_PM_EST"] = pct(v["PM_EST"] / D.PM_TOT)
    for wp in ("WP0", "WP1", "WP2", "WP3"):
        v[f"PM_{wp}"] = D.WP_PM[wp]; v[f"N_{wp}"] = D.WP_N[wp]; v[f"PCT_PM_{wp}"] = pct(D.WP_PM[wp] / D.PM_TOT)
        v[f"COP_{wp}"] = mm(D.WP_COP[wp])
    v["COP_PERS"] = mm(R["por_rubro"]["Personal"]); v["PCT_PERS"] = pct(R["por_rubro"]["Personal"] / R["sgr"])
    v["NODOS_POR_TEC"] = num(M.IDENT["nodos"] / 6, 1)
    v["COMITES_POR_PERS"] = int(15 / 3)
    v["P01_COP"] = mm(B["P01"]["total"]); v["P02_COP"] = mm(B["P02"]["total"])
    # contrapartida
    v["CON_IES"] = mm(D.CONTRA_IES, 0); v["CON_EMP_EF"] = mm(D.CONTRA_EMP_EF, 0); v["CON_EMP_ES"] = mm(D.CONTRA_EMP_ES, 0)
    v["CON_TOT"] = mm(D.CONTRA_TOT, 0); v["CON_ESPECIE"] = mm(D.CONTRA_ESPECIE, 0)
    v["PCT_ESPECIE"] = pct(D.CONTRA_ESPECIE / D.CONTRA_TOT); v["PCT_EF"] = pct(D.CONTRA_EMP_EF / D.CONTRA_TOT)
    v["PCT_CON_SGR"] = pct(D.CONTRA_TOT / R["sgr"]); v["PCT_CON_TOT"] = pct(D.CONTRA_TOT / R["total"])
    v["PCT_EF_TOT"] = pct(D.CONTRA_EMP_EF / R["total"])
    v["IES_PERS"] = mm(D.C["C01"]["total"] + D.C["C02"]["total"] + D.C["C03"]["total"], 0)
    for k in ("C01", "C02", "C03", "C04", "C05", "C06"): v[k] = mm(D.C[k]["total"], 0)
    v["SERV_EXT"] = mm(sum(B[i]["total"] for i in ("S01", "S07", "S08")))
    # presupuesto
    v["SGR"] = M.cop(R["sgr"]); v["SGR_M"] = mm(R["sgr"]); v["TOT"] = M.cop(R["total"]); v["TOT_M"] = mm(R["total"]); v["CONTRA"] = M.cop(R["contra"])
    v["PCT_TOPE"] = pct(R["pct_tope"]); v["HOLGURA"] = M.cop(R["holgura"]); v["TOPE"] = M.cop(M.IDENT["tope_cop"])
    v["RESERVA_M"] = mm(M.RESERVA, 0); v["ADMIN_PCT"] = pct(B["O05"]["total"] / R["sgr"])
    v["PCT_SGR_TOT"] = pct(R["sgr"] / R["total"])
    for k, x in R["por_rubro"].items():
        key = {"Personal": "PERS_M", "Equipos y software": "EQ_M", "Materiales e insumos": "MAT_M", "Servicios técnicos": "SERV_M",
               "Viajes y viáticos": "VIAJ_M", "Otros rubros": "OTR_M", "Reserva de contingencia": "RES_M"}[k]
        v[key] = mm(x); v[key.replace("_M", "_PCT")] = pct(x / R["sgr"])
    v["FLUJO"] = ", ".join(mm(x) for x in R["flujo_sgr_sem"]); v["FLUJO_CON"] = mm(R["flujo_con_sem"][0])
    # marco lógico y riesgos
    v["EMV_FIN"] = num(D.emv_nivel("Fin")); v["EMV_PROP"] = num(D.emv_nivel("Propósito")); v["EMV_COMP"] = num(D.emv_nivel("Componentes")); v["EMV_ACT"] = num(D.emv_nivel("Actividades"))
    v["EMV_SUMA"] = num(sum(r["emv"] for r in M.RISKS) / D.MM)
    v["N_CUMPLE"] = D.N_CUMPLE; v["N_PARCIAL"] = D.N_PARCIAL
    tr = sum(r["emv"] for r in D.TOP5)
    v["EMV_TOP5"] = num(tr / D.MM); v["PCT_TOP5"] = pct(tr / sum(r["emv"] for r in M.RISKS))
    tot_emv = sum(r["emv"] for r in M.RISKS)
    v["PCT_EMV_COMP"] = pct(sum(D.RK[i]["emv"] for i in D.NIVEL_RIESGO["Componentes"]) / tot_emv)
    est = [r["estrategia"] for r in M.RISKS]
    v["N_EST_MIT"] = est.count("Mitigar"); v["N_EST_ACE"] = est.count("Aceptar y mitigar"); v["N_EST_TRA"] = est.count("Transferir y mitigar"); v["N_EST_EVI"] = est.count("Evitar")
    for wp in ("WP0", "WP1", "WP2", "WP3"): v[f"N_ACT_{wp}"] = len(D.ACT_WP[wp])
    # cronograma
    v["SEM"] = M.DURACION_SEMANAS; v["N_ACT"] = len(M.ACT)
    v["N_CRIT"] = len(M.RUTA_CRITICA)
    v["N_HOLG"] = len(M.ACT) - len(M.RUTA_CRITICA)
    # versiones en palabras (cero a nueve)
    for k in list(v):
        if isinstance(v[k], int) and not isinstance(v[k], bool):
            v[k + "_W"] = pal(v[k]); v[k + "_WC"] = pal(v[k]).capitalize()
    return v
