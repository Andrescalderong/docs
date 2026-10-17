# -*- coding: utf-8 -*-
"""Capítulo 6 (Metodología): cálculos del diseño de medición (A4).
1) Horas-nodo teóricas y válidas de la colocalización del tramo 1 (CALCULADO).
2) Pares nodo-referencia a 1 hora y a 24 horas, tamaño efectivo e intervalos esperables de R² y pendiente por simulación
   (ILUSTRATIVO; semilla 20261013; parámetros declarados en PARAM).
3) Cálculos auxiliares de muestra (comités, personal funcionario) y rotaciones.
Uso: python3 c6_diseno_medicion.py   (escribe c6_diseno_medicion_resultados.json junto a este archivo)."""
import json, os, math
import numpy as np
from scipy.signal import lfilter
from scipy import stats

SEED = 20261013
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- 1. Cálculo determinista (ficha: 3 sitios, 10 nodos, 16 semanas)
SITIOS, NODOS, SEMANAS, H_SEM = 3, 10, 16, 168
H_SITIO = SEMANAS * H_SEM
HN_TEO = SITIOS * NODOS * H_SITIO
META_R05 = 60000
det = {
    "horas_por_nodo": H_SITIO, "dias_por_nodo": SEMANAS * 7,
    "horas_nodo_teoricas": HN_TEO,
    "horas_nodo_por_sitio": NODOS * H_SITIO,
    "completitud_minima_para_meta": META_R05 / HN_TEO,
    "escenarios": {},
}
for c in (1.0, 0.90, 0.81, 0.765, 0.75, 0.744):
    det["escenarios"][str(c)] = {"horas_nodo": HN_TEO * c, "margen_vs_meta": HN_TEO * c - META_R05}
det["completitud_nodo_requerida_con_ref_90"] = META_R05 / HN_TEO / 0.90
det["pares_con_disp_90_90"] = HN_TEO * 0.81
det["aceptacion_qc_minima_con_81"] = META_R05 / (HN_TEO * 0.81)
det["pares_75"] = {"por_nodo": H_SITIO * 0.75, "por_sitio": NODOS * H_SITIO * 0.75, "total": HN_TEO * 0.75}
det["dias_ref_por_sitio"] = SEMANAS * 7
det["horas_ref_por_sitio"] = H_SITIO

# n requerido (observaciones independientes) para semiancho de IC de R² y pendiente
def n_para_r2(r2, semi, z=1.96):
    r = math.sqrt(r2)
    for n in range(10, 100000):
        zr = math.atanh(r); se = 1 / math.sqrt(n - 3)
        lo, hi = math.tanh(zr - z * se) ** 2, math.tanh(zr + z * se) ** 2
        if (hi - lo) / 2 <= semi: return n
def n_para_pend(r2, semi, b=1.0, z=1.96):
    # SE(b) = b*sqrt((1-r2)/r2)/sqrt(n-2) en regresión de y sobre x con pendiente b
    k = b * math.sqrt((1 - r2) / r2)
    return math.ceil((z * k / semi) ** 2 + 2)
det["n_iid"] = {"R2_0.80_semi_0.05": n_para_r2(0.80, 0.05), "R2_0.80_semi_0.10": n_para_r2(0.80, 0.10),
                "pend_R2_0.80_semi_0.10": n_para_pend(0.80, 0.10), "pend_R2_0.80_semi_0.05": n_para_pend(0.80, 0.05)}
# IC de R² con n días de referencia independientes
def ic_r2(r2, n, z=1.96):
    r = math.sqrt(r2); zr = math.atanh(r); se = 1 / math.sqrt(n - 3)
    return math.tanh(zr - z * se) ** 2, math.tanh(zr + z * se) ** 2
det["ic_r2_84dias"] = ic_r2(0.80, 84)
det["ic_r2_112dias"] = ic_r2(0.80, 112)
det["ic_r2_2016h"] = ic_r2(0.80, 2016)

# Comités y personal
from scipy.stats import beta
def clopper(k, n, a=0.05):
    lo = 0.0 if k == 0 else beta.ppf(a / 2, k, n - k + 1)
    hi = 1.0 if k == n else beta.ppf(1 - a / 2, k + 1, n - k)
    return lo, hi
det["comites"] = {"11_de_15": 11 / 15, "12_de_15": 12 / 15, "minimo_comites_75": math.ceil(0.75 * 15),
                  "IC_12_de_15": clopper(12, 15), "IC_11_de_15": clopper(11, 15), "IC_8_de_15": clopper(8, 15)}
def margen_prop(N, n, p=0.5, z=1.96):
    return z * math.sqrt(p * (1 - p) / n * (N - n) / (N - 1))
det["encuesta"] = {f"n{n}": margen_prop(150, n) for n in (150, 135, 120, 105, 90)}
det["rotaciones"] = {"no_colocalizados_por_depto": {"Caldas": 33 - 10, "Cundinamarca": 34 - 10, "Valle": 33 - 10},
                     "cupos_4x6": 24, "cupos_4x7": 28}
det["sesiones"] = {"bitacoras_semanales": 104, "retrospectivas": 104 // 2, "serendipia_mensual": 24}

# ---------------------------------------------------------------- 2. Simulación (ILUSTRATIVO)
PARAM = dict(
    mu_ref=25.0, sigma_ln_ref=0.55, phi_ref=0.96, amp_diurna_ln=0.15,
    rh_base=0.70, rh_amp=0.15, rh_sd_dia=0.10, rh_phi_dia=0.8, rh_min=0.25, rh_max=0.95,
    kappa_media=0.15, kappa_sd=0.03, ganancia_sd=0.08, offset_media=1.0, offset_sd=1.0,
    rho_ruido=0.5, escenarios_sigma_eta={"ruido_bajo": 0.10, "ruido_medio": 0.20, "ruido_alto": 0.30},
    comp_nodo=0.85, gap_nodo_h=12, comp_ref=0.90, gap_ref_h=24, dia_valido_min_horas=18,
    n_rep=1000, boot_rep=100, boot_B=300)
T = H_SITIO
hora = np.arange(T) % 24
dia = np.arange(T) // 24
ND = T // 24

def ar1(rng, shape, phi, sd):
    e = rng.standard_normal(shape) * sd * math.sqrt(1 - phi ** 2)
    e[..., 0] = rng.standard_normal(shape[:-1]) * sd
    return lfilter([1.0], [1.0, -phi], e, axis=-1)

def markov_valid(rng, shape, comp, gap):
    """Disponibilidad como cadena de Markov de dos estados (bloques contiguos de datos faltantes)."""
    p_on = 1.0 / gap; p_off = p_on * (1 - comp) / comp
    u = rng.random(shape); s = np.empty(shape, dtype=bool)
    s[..., 0] = rng.random(shape[:-1]) < comp
    for t in range(1, shape[-1]):
        prev = s[..., t - 1]
        s[..., t] = np.where(prev, u[..., t] >= p_off, u[..., t] < p_on)
    return s

def simular_campana(rng, sig_eta):
    P = PARAM
    # humedad relativa por sitio
    rh_d = ar1(rng, (SITIOS, ND), P["rh_phi_dia"], P["rh_sd_dia"])
    rh = P["rh_base"] - P["rh_amp"] * np.cos(2 * np.pi * (hora - 15) / 24)[None, :] + np.repeat(rh_d, 24, axis=1)
    rh = np.clip(rh, P["rh_min"], P["rh_max"])
    # referencia (PM2,5, µg/m³)
    z = ar1(rng, (SITIOS, T), P["phi_ref"], P["sigma_ln_ref"])
    lnc = math.log(P["mu_ref"]) - P["sigma_ln_ref"] ** 2 / 2 + z + P["amp_diurna_ln"] * np.cos(2 * np.pi * (hora - 8) / 24)[None, :]
    ref = np.exp(lnc)
    # nodos
    kap = np.clip(rng.normal(P["kappa_media"], P["kappa_sd"], (SITIOS, NODOS, 1)), 0.02, None)
    gan = rng.normal(1.0, P["ganancia_sd"], (SITIOS, NODOS, 1))
    off = rng.normal(P["offset_media"], P["offset_sd"], (SITIOS, NODOS, 1))
    g = 1 + kap * (rh[:, None, :] ** 2) / (1 - rh[:, None, :])
    eta = ar1(rng, (SITIOS, NODOS, T), P["rho_ruido"], sig_eta)
    x = np.maximum((off + gan * ref[:, None, :] * g) * np.exp(eta), 0.0)
    # disponibilidad
    vn = markov_valid(rng, (SITIOS, NODOS, T), P["comp_nodo"], P["gap_nodo_h"])
    vr = markov_valid(rng, (SITIOS, T), P["comp_ref"], P["gap_ref_h"])
    valid = vn & vr[:, None, :]
    return ref, rh, x, valid

def ajustar_m1(x, rh, ref, m):
    """Modelo lineal con humedad: ref ~ 1 + x + rh + x·rh (MCO con los pares válidos de los sitios de entrenamiento)."""
    X = np.column_stack([np.ones(m.sum()), x[m], rh[m], x[m] * rh[m]])
    beta_, *_ = np.linalg.lstsq(X, ref[m], rcond=None)
    return beta_

def metricas(y, r):
    """y: lectura corregida; r: referencia. Convención EPA: regresión de y sobre r."""
    n = r.size
    if n < 5: return None
    sx, sy = r.sum(), y.sum(); sxx, syy, sxy = (r * r).sum(), (y * y).sum(), (r * y).sum()
    cov = sxy - sx * sy / n; vx = sxx - sx * sx / n; vy = syy - sy * sy / n
    slope = cov / vx; r2 = cov * cov / (vx * vy)
    rmse = math.sqrt(((y - r) ** 2).mean()); nrmse = rmse / r.mean()
    nmae = np.abs(y - r).mean() / r.mean(); bias = (y - r).mean()
    return dict(R2=r2, pend=slope, NRMSE=nrmse, NMAE=nmae, sesgo=bias, n=n)

def promedios_dia(y, r, v):
    """Promedios de 24 h con regla de validez: al menos 18 horas válidas del día (y y r comparten máscara)."""
    nn = v.shape[:-1]
    vv = v.reshape(*nn, ND, 24); yy = np.where(v, y, 0).reshape(*nn, ND, 24); rr = np.where(v, r, 0).reshape(*nn, ND, 24)
    cnt = vv.sum(-1); ok = cnt >= PARAM["dia_valido_min_horas"]
    ym = yy.sum(-1) / np.maximum(cnt, 1); rm = rr.sum(-1) / np.maximum(cnt, 1)
    return ym, rm, ok

def stats_semana(y, r, ok_mask, semana_idx, n_sem):
    """Estadísticos suficientes por semana para el bootstrap por bloques."""
    out = np.zeros((n_sem, 7))
    for w in range(n_sem):
        s = semana_idx == w
        m = ok_mask & s
        yy, rr = y[m], r[m]
        out[w] = [yy.size, rr.sum(), yy.sum(), (rr * rr).sum(), (yy * yy).sum(), (rr * yy).sum(), ((yy - rr) ** 2).sum()]
    return out

def metr_desde_stats(S):
    n, sx, sy, sxx, syy, sxy, sd2 = [S[..., i] for i in range(7)]
    cov = sxy - sx * sy / n; vx = sxx - sx * sx / n; vy = syy - sy * sy / n
    return cov * cov / (vx * vy), cov / vx, np.sqrt(sd2 / n) / (sx / n)

def correr_escenario(nombre, sig_eta, rng):
    P = PARAM
    reg = {k: [] for k in ("h_R2", "h_pend", "h_NRMSE", "h_NMAE", "h_sesgo", "d_R2", "d_pend", "d_NRMSE", "d_NMAE", "d_sesgo",
                           "hD_R2", "hD_pend", "hD_NRMSE", "dD_R2", "dD_pend", "dD_NRMSE",
                           "pares", "dias_nodo", "z_h", "z_d")}
    bootres = {k: [] for k in ("h_R2", "h_pend", "d_R2", "d_pend", "h_NRMSE", "d_NRMSE")}
    semana_h = np.arange(T) // H_SEM
    semana_d = np.arange(ND) // 7
    for rep in range(P["n_rep"]):
        ref, rh, x, valid = simular_campana(rng, sig_eta)
        reg["pares"].append(valid.sum())
        yc = np.zeros_like(x)
        # LODO: entrenar con 2 sitios, probar en el tercero
        for s in range(SITIOS):
            tr = [k for k in range(SITIOS) if k != s]
            xr = np.concatenate([x[k].ravel() for k in tr]); rhr = np.concatenate([np.broadcast_to(rh[k], (NODOS, T)).ravel() for k in tr])
            rr = np.concatenate([np.broadcast_to(ref[k], (NODOS, T)).ravel() for k in tr]); mr = np.concatenate([valid[k].ravel() for k in tr])
            b = ajustar_m1(xr, rhr, rr, mr)
            yc[s] = b[0] + b[1] * x[s] + b[2] * rh[s][None, :] + b[3] * x[s] * rh[s][None, :]
        refb = np.broadcast_to(ref[:, None, :], x.shape)
        # por departamento (sitio) a 1 h y 24 h
        ymd, rmd, okd = promedios_dia(yc, refb, valid)
        zs_h, zs_d = [], []
        for s in range(SITIOS):
            m = valid[s]
            mh = metricas(yc[s][m], refb[s][m])
            md = metricas(ymd[s][okd[s]], rmd[s][okd[s]])
            for k in ("R2", "pend", "NRMSE", "NMAE", "sesgo"):
                reg["h_" + k].append(mh[k]); reg["d_" + k].append(md[k])
            zs_h.append(math.atanh(math.sqrt(mh["R2"]))); zs_d.append(math.atanh(math.sqrt(md["R2"])))
            reg["dias_nodo"].append(okd[s].sum())
        reg["z_h"] += zs_h; reg["z_d"] += zs_d
        # conjunto de los tres sitios (30 nodos)
        mh = metricas(yc[valid], refb[valid]); md = metricas(ymd[okd], rmd[okd])
        for k in ("R2", "pend", "NRMSE"):
            reg["hD_" + k].append(mh[k]); reg["dD_" + k].append(md[k])
        # bootstrap por semanas sobre los 30 nodos (primeras réplicas)
        if rep < P["boot_rep"]:
            sh = np.zeros((16, 7)); sd_ = np.zeros((16, 7))
            idx_h = np.broadcast_to(semana_h[None, None, :], valid.shape)
            sh = stats_semana(yc[valid], refb[valid], np.ones(valid.sum(), bool), idx_h[valid], 16)
            idx_d = np.broadcast_to(semana_d[None, None, :], okd.shape)
            sd_ = stats_semana(ymd[okd], rmd[okd], np.ones(okd.sum(), bool), idx_d[okd], 16)
            for tag, S in (("h", sh), ("d", sd_)):
                ib = rng.integers(0, 16, (P["boot_B"], 16))
                r2, pe, nr = metr_desde_stats(S[ib].sum(1))
                for k, v in (("R2", r2), ("pend", pe), ("NRMSE", nr)):
                    lo, hi = np.percentile(v, [2.5, 97.5]); bootres[f"{tag}_{k}"].append((hi - lo) / 2)
    res = {"sigma_eta": sig_eta}
    for k, v in reg.items():
        if k in ("z_h", "z_d"): continue
        a = np.asarray(v, float)
        if k == "pares":
            res[k] = dict(mediana=float(np.median(a)), p025=float(np.percentile(a, 2.5)), p975=float(np.percentile(a, 97.5)),
                          frac_meta=float((a >= META_R05).mean()))
        else:
            res[k] = dict(mediana=float(np.median(a)), p025=float(np.percentile(a, 2.5)), p975=float(np.percentile(a, 97.5)))
    for tag in ("h", "d"):
        z = np.asarray(reg["z_" + tag]); res["n_efectivo_" + tag] = float(3 + 1 / z.var(ddof=1))
    res["boot_semiancho"] = {k: float(np.median(v)) for k, v in bootres.items()}
    # fracción de réplicas que cumplen R² y NRMSE (conjunto de 30 nodos) y cada criterio por sitio
    for tag in ("h", "d"):
        r2 = np.asarray(reg[f"{tag}D_R2"]); nr = np.asarray(reg[f"{tag}D_NRMSE"]); pe = np.asarray(reg[f"{tag}D_pend"])
        res[f"frac_cumple_{tag}"] = dict(R2=float((r2 >= 0.70).mean()), NRMSE=float((nr <= 0.30).mean()),
                                         ambos=float(((r2 >= 0.70) & (nr <= 0.30)).mean()),
                                         pend=float(((pe >= 0.65) & (pe <= 1.35)).mean()))
        r2s = np.asarray(reg[f"{tag}_R2"]); nrs = np.asarray(reg[f"{tag}_NRMSE"])
        res[f"frac_cumple_sitio_{tag}"] = float(((r2s >= 0.70) & (nrs <= 0.30)).mean())
    return res

if __name__ == "__main__":
    rng = np.random.default_rng(SEED)
    out = {"semilla": SEED, "parametros": PARAM, "determinista": det, "simulacion": {}}
    for nombre, sig in PARAM["escenarios_sigma_eta"].items():
        out["simulacion"][nombre] = correr_escenario(nombre, sig, rng)
        print(nombre, "listo", flush=True)
    with open(os.path.join(HERE, "c6_diseno_medicion_resultados.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, default=float)
    print(json.dumps(out["determinista"], ensure_ascii=False, indent=1, default=float))
