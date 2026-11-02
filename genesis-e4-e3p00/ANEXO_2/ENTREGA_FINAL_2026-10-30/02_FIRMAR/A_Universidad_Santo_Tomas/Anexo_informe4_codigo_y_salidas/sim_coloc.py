# -*- coding: utf-8 -*-
"""Simulación de formulación de la colocalización del tramo 1 con el conjunto de referencia rotativo (Anexo 3 v5).

Diseño: dos municipios, 15 nodos por municipio, 16 semanas (2.688 horas por nodo). El monitor beta y el monitor
óptico de referencia se intercambian entre los municipios en la semana 8. Partición temporal: semanas 1 a 11 para
entrenar y 12 a 16 para probar. Corrección: regresión lineal con humedad e interacción, común a los 30 nodos.
Las cifras orientan el tamaño de los intervalos; no predicen el desempeño real.
"""
import json, os, sys
import numpy as np

H = 2688; SEM = 168; N_MUN = 2; N_NOD = 15; N_CAMP = 1000
ESC = {"bajo": (0.15, 1.0), "medio": (0.30, 2.0), "alto": (0.50, 4.0)}  # (ruido multiplicativo, ruido aditivo µg/m³)
MEDIA = (22.0, 18.0)       # PM2,5 medio supuesto por municipio (µg/m³)
HR_MEDIA = (80.0, 74.0)    # humedad relativa media supuesta por municipio (%)
SESGO_INST = {"beta": 0.03, "optico": -0.03}


def serie_pm(rng, media):
    t = np.arange(H)
    e = rng.normal(0, 0.18, H); z = np.empty(H); z[0] = 0
    for i in range(1, H):
        z[i] = 0.95 * z[i - 1] + e[i]
    diurno = 0.30 * np.sin(2 * np.pi * (t % 24) / 24 - 1.2)
    x = np.exp(np.log(media) - 0.18 + z + diurno)
    for _ in range(rng.poisson(16)):  # episodios de remoción: uno por semana en promedio
        i0 = rng.integers(0, H - 12); d = rng.integers(4, 13)
        x[i0:i0 + d] *= rng.uniform(3, 8)
    return x


def serie_hr(rng, media):
    t = np.arange(H)
    e = rng.normal(0, 2.5, H); z = np.empty(H); z[0] = 0
    for i in range(1, H):
        z[i] = 0.9 * z[i - 1] + e[i]
    return np.clip(media + 12 * np.cos(2 * np.pi * (t % 24) / 24) + z, 30, 97)


def metricas(c, y):
    r = np.corrcoef(c, y)[0, 1]
    pend = np.polyfit(y, c, 1)[0]
    return r * r, np.sqrt(np.mean((c - y) ** 2)) / np.mean(y), pend, np.mean(c - y)


def campaña(rng, sm, sa):
    filas = []
    for m in range(N_MUN):
        x = serie_pm(rng, MEDIA[m]); hr = serie_hr(rng, HR_MEDIA[m])
        inst = np.where(np.arange(H) < 8 * SEM, 0 if m == 0 else 1, 1 if m == 0 else 0)  # 0 beta, 1 óptico
        sesgo = np.where(inst == 0, SESGO_INST["beta"], SESGO_INST["optico"])
        y = x * (1 + sesgo) * (1 + rng.normal(0, 0.05, H))
        f = 1 + 0.10 * (hr / 100) ** 2 / (1 - hr / 100)
        for _ in range(N_NOD):
            g = rng.normal(1, 0.10); o = rng.normal(0, 2.0)
            s = g * x * f + o + rng.normal(0, 1, H) * sm * x + rng.normal(0, sa, H)
            filas.append((s, hr, y))
    S = np.stack([f[0] for f in filas]); HRm = np.stack([f[1] for f in filas]); Y = np.stack([f[2] for f in filas])
    ent = np.arange(H) < 11 * SEM
    X = lambda s, h: np.column_stack([np.ones(s.size), s, h, s * h])
    b, *_ = np.linalg.lstsq(X(S[:, ent].ravel(), HRm[:, ent].ravel()), Y[:, ent].ravel(), rcond=None)
    St, Ht, Yt = S[:, ~ent], HRm[:, ~ent], Y[:, ~ent]
    C = (X(St.ravel(), Ht.ravel()) @ b).reshape(St.shape)
    h1 = metricas(C.ravel(), Yt.ravel())
    nd = C.shape[1] // 24
    C24 = C[:, :nd * 24].reshape(C.shape[0], nd, 24).mean(2).ravel()
    Y24 = Yt[:, :nd * 24].reshape(Yt.shape[0], nd, 24).mean(2).ravel()
    h24 = metricas(C24, Y24)
    # transferencia espacial: entrena con un municipio y prueba en el otro (promedio de los dos sentidos, 24 horas)
    xs = []
    for a_, b_ in ((slice(0, N_NOD), slice(N_NOD, 2 * N_NOD)), (slice(N_NOD, 2 * N_NOD), slice(0, N_NOD))):
        bb, *_ = np.linalg.lstsq(X(S[a_][:, ent].ravel(), HRm[a_][:, ent].ravel()), Y[a_][:, ent].ravel(), rcond=None)
        Cx = (X(S[b_][:, ~ent].ravel(), HRm[b_][:, ~ent].ravel()) @ bb).reshape(S[b_][:, ~ent].shape)
        Yx = Y[b_][:, ~ent]
        xs.append(metricas(Cx[:, :nd * 24].reshape(Cx.shape[0], nd, 24).mean(2).ravel(), Yx[:, :nd * 24].reshape(Yx.shape[0], nd, 24).mean(2).ravel()))
    return h1, h24, xs


def cumple(r2, nrmse, pend, sesgo):
    return r2 >= 0.70 and nrmse <= 0.30 and 0.65 <= pend <= 1.35 and -5 <= sesgo <= 5


def main(out):
    rng = np.random.default_rng(20261029)
    res = {"diseno": {"municipios": N_MUN, "nodos_por_municipio": N_NOD, "horas_por_nodo": H,
                      "horas_nodo_teoricas": N_MUN * N_NOD * H, "campanas_por_escenario": N_CAMP}, "escenarios": {}}
    for k, (sm, sa) in ESC.items():
        r1, r24, rx = [], [], []
        for _ in range(N_CAMP):
            a, b, c = campaña(rng, sm, sa); r1.append(a); r24.append(b); rx.extend(c)
        r1 = np.array(r1); r24 = np.array(r24); rx = np.array(rx)
        res["escenarios"][k] = {
            "R2_1h_mediana": float(np.median(r1[:, 0])), "NRMSE_1h_mediana": float(np.median(r1[:, 1])),
            "R2_24h_mediana": float(np.median(r24[:, 0])), "NRMSE_24h_mediana": float(np.median(r24[:, 1])),
            "cumple_1h": float(np.mean([cumple(*v) for v in r1])), "cumple_24h": float(np.mean([cumple(*v) for v in r24])),
            "pend_24h_bajo_065": float(np.mean(r24[:, 2] < 0.65)), "pend_24h_mediana": float(np.median(r24[:, 2])),
            "sesgo_24h_mediana": float(np.median(r24[:, 3])),
            "transfer_R2_24h_mediana": float(np.median(rx[:, 0])), "transfer_NRMSE_24h_mediana": float(np.median(rx[:, 1])),
            "transfer_cumple_24h": float(np.mean([cumple(*v) for v in rx]))}
        print(k, json.dumps(res["escenarios"][k], ensure_ascii=False))
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "data_v5", "sim_coloc.json"))
