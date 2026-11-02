# -*- coding: utf-8 -*-
"""Figuras del Capítulo 2 (parte A): prisma, produccion, lotka, bradford, geografica, patentes.
Semilla 42; corpus de 42 documentos; año de corte 2026. Usa figs/estilo.py."""
import os, sys, collections, math, datetime as dt
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
sys.path.insert(0, AQUI)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D
import estilo as E
import c2_datos as D

PIE = "n = 42 documentos; año de corte 2026; semilla 42"

def pie(fig, txt=PIE):
    fig.text(0.01, 0.002, txt, fontsize=7.5, color=E.TINTA, ha="left", va="bottom")

# ---------------------------------------------------------------- PRISMA
from matplotlib.patches import FancyBboxPatch
def caja_trama(ax, x, y, w, h, texto, fs=8.8, bold=False):
    """Caja con trama clara (dato NO_VERIFICADO) y texto sobre fondo liso para legibilidad."""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=E.CLARO, ec=E.MEDIO, lw=0, hatch="///"))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc="none", ec=E.TINTA, lw=1.2))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, fontweight="bold" if bold else "normal",
            linespacing=1.3, bbox=dict(boxstyle="round,pad=0.35", fc=E.BLANCO, ec="none", alpha=0.92))

def prisma(nombre, h1):
    fig, ax = E.lienzo_libre(h1=h1, h2="Flujo de selección con números reales del corpus: documentos por etapa, 1995 a 2026", figsize=(10, 7), xlim=(0, 100), ylim=(-2, 72))
    W, H = 46, 11.5
    xs = 12
    etapas = [("IDENTIFICACIÓN", 56), ("CRIBADO", 40), ("ELEGIBILIDAD", 24), ("INCLUSIÓN", 6)]
    for t, y in etapas:
        ax.add_patch(Rectangle((1, y - 1.0), 8.5, H + 2, fc=E.CAJA, ec=E.TINTA, lw=1))
        ax.text(5.25, y + H / 2, t, rotation=90, ha="center", va="center", fontsize=7.6, fontweight="bold", color=E.TINTA)
    caja_trama(ax, xs, 56, W, H, "Registros identificados en bases\n(Scopus, WoS, Lens.org, Espacenet)\nNO_VERIFICADO: ecuaciones del Anexo D\nsin ejecutar en bases comerciales")
    caja_trama(ax, xs, 40, W, H, "Registros tras eliminar duplicados\nNO_VERIFICADO")
    E.caja(ax, xs, 24, W, H, "Documentos evaluados a texto completo\nn = 42 (lectura completa de cada documento)", relleno=E.MEDIO, fs=8.8)
    E.caja(ax, xs, 6, W, H, "Documentos incluidos en el corpus: n = 42\nArtículos: 26 (61,9 %)\nPatentes: 15 (35,7 %)\nInforme institucional: 1 (2,4 %)", relleno=E.AZUL, fs=8.8, bold=True)
    xr = 64
    E.caja(ax, xr, 56, 33, H, "Origen real del corpus: 42 archivos\naportados al informe de vigilancia;\ncriterio de selección sin registro", relleno=E.CAJA, fs=8.3)
    caja_trama(ax, xr, 40, 33, H, "Excluidos en cribado\nNO_VERIFICADO")
    caja_trama(ax, xr, 24, 33, H, "Excluidos a texto completo\nsin registro: NO_VERIFICADO")
    for y in (56, 40, 24):
        E.flecha(ax, (xs + W / 2, y), (xs + W / 2, y - 4.4))
        E.flecha(ax, (xs + W + 0.3, y + H / 2), (xr - 0.3, y + H / 2))
    ax.add_patch(Rectangle((1, -1.2), 2.5, 2.2, fc=E.CLARO, ec=E.TINTA, hatch="///", lw=0.8))
    ax.text(4.5, -0.1, "Trama: dato NO_VERIFICADO", fontsize=8, va="center", color=E.TINTA)
    ax.add_patch(Rectangle((34, -1.2), 2.5, 2.2, fc=E.AZUL, ec=E.TINTA, lw=0.8))
    ax.text(37.5, -0.1, "Relleno liso: dato documentado en el informe de vigilancia", fontsize=8, va="center", color=E.TINTA)
    pie(fig)
    return E.guardar(fig, nombre)

# ---------------------------------------------------------------- PRODUCCIÓN
def produccion():
    tipos = collections.defaultdict(lambda: collections.Counter())
    for r in D.CORPUS: tipos[r["year"]][r["tipo"]] += 1
    anios = [1995] + list(range(2019, 2027))
    pos = [0.0] + [2.0 + i for i in range(8)]          # hueco entre 1995 y 2019 (1996 a 2018 sin documentos)
    art = np.array([tipos[a]["articulo"] for a in anios]); pat = np.array([tipos[a]["patente"] for a in anios]); inf = np.array([tipos[a]["informe"] for a in anios])
    tot = art + pat + inf; acum = np.cumsum(tot); x = np.array(pos)
    fig, ax = E.lienzo(h1="La producción pasa de 2 documentos en 2019 a 17 en 2026", h2="Documentos por año de publicación (barras) y acumulado (línea discontinua); n = 42; 1996 a 2018 sin documentos")
    ax.bar(x, art, color=E.AZUL, edgecolor=E.TINTA, lw=0.7, label="Artículos (26)", width=0.8)
    ax.bar(x, pat, bottom=art, color=E.MEDIO, edgecolor=E.TINTA, lw=0.7, hatch="///", label="Patentes (15)", width=0.8)
    ax.bar(x, inf, bottom=art + pat, color=E.CLARO, edgecolor=E.TINTA, lw=0.7, hatch="...", label="Informe institucional (1)", width=0.8)
    for xi, t in zip(x, tot): ax.text(xi, t + 0.3, str(t), ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=E.TINTA, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.8), zorder=7)
    ax.set_xticks(x); ax.set_xticklabels([str(a) for a in anios], fontsize=9.5)
    ax.set_xlim(-0.8, 9.7); ax.set_ylim(0, 22); ax.set_yticks(range(0, 21, 5)); ax.set_ylabel("Documentos por año")
    ax.text(1.0, 8.5, "1996 a 2018:\nningún documento", ha="center", va="center", fontsize=8.7, color=E.TINTA)
    ax.plot([0.55, 1.45], [0.0, 0.0], color=E.BLANCO, lw=4, zorder=6); 
    ax.text(1.0, -0.9, "//", ha="center", va="center", fontsize=11, color=E.TINTA, clip_on=False)
    ax2 = ax.twinx(); ax2.plot(x, acum, color=E.TINTA, ls="--", lw=1.5, marker="o", ms=4)
    ax2.set_ylim(0, 44); ax2.set_yticks(range(0, 43, 10)); ax2.set_ylabel("Acumulado de documentos"); ax2.spines["right"].set_visible(True)
    ax2.text(x[-1] - 0.25, acum[-1] + 0.8, "42", fontsize=9, fontweight="bold", ha="right", color=E.TINTA)
    ax.legend(loc="upper left", fontsize=8.7, bbox_to_anchor=(0.0, 1.0))
    # eras: llaves bajo el eje
    eras = [(-0.4, 6.4, "Fundacional 1995 a 2023\n11 documentos (26,2 %)"), (6.6, 8.4, "Crecimiento\n2024 a 2025\n14 (33,3 %)"), (8.6, 9.4, "Aceleración\n2026\n17 (40,5 %)")]
    for i, (a, b, t) in enumerate(eras):
        ax.annotate("", xy=(a, -0.17), xytext=(b, -0.17), xycoords=("data", "axes fraction"), textcoords=("data", "axes fraction"), arrowprops=dict(arrowstyle="-", color=E.TINTA, lw=1.4))
        ax.text((a + b) / 2, -0.19, t, transform=ax.get_xaxis_transform(), ha="center", va="top", fontsize=8.5, color=E.TINTA, fontweight="bold")
    fig.subplots_adjust(bottom=0.24)
    pie(fig, PIE + ". Eras por segmentación óptima en tres tramos contiguos (SSE = 26,8)")
    return E.guardar(fig, "c2_produccion")

# ---------------------------------------------------------------- LOTKA
def lotka():
    docs, nombres, total = D.tabla_autores(); L = D.lotka(docs)
    obs = dict(L["niveles"]); y1 = obs[1]
    fig, ax = E.lienzo(h1="El 95,8 % de los 213 autores firma un solo documento", h2="Autores por número de documentos, escala logarítmica en ambos ejes; n = 213 autores de 41 documentos con autoría individual")
    xx = np.linspace(1, 4, 50)
    ax.plot(xx, y1 * xx ** (-2.0), color=E.TINTA, ls=":", lw=1.8)
    ax.plot(xx, y1 * xx ** (-L["alpha_mle"]), color=E.MEDIO, ls="--", lw=2.2)
    xl = np.linspace(1, 2.9, 30)
    ax.plot(xl, y1 * xl ** (-L["alpha_ls"]), color=E.AZUL, ls="-", lw=1.8)
    ax.scatter([1, 2], [obs[1], obs[2]], s=150, color=E.AZUL, edgecolor=E.TINTA, zorder=5, lw=1.2)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xticks([1, 2, 3, 4]); ax.set_xticklabels(["1", "2", "3", "4"]); ax.set_yticks([1, 3, 10, 30, 100, 300]); ax.set_yticklabels(["1", "3", "10", "30", "100", "300"])
    ax.set_xlim(0.85, 9.5); ax.set_ylim(2, 450)
    ax.minorticks_off()
    ax.set_xlabel("Documentos por autor (x)"); ax.set_ylabel("Número de autores con x documentos (y)")
    ax.annotate("Observado: 204 autores con 1 documento", xy=(1, 204), xytext=(1.12, 290), fontsize=9, color=E.TINTA, fontweight="bold")
    ax.annotate("Observado: 9 autores con 2 documentos", xy=(2, 9), xytext=(2.25, 9), fontsize=9, color=E.TINTA, fontweight="bold", va="center")
    ax.text(4.15, y1 * 4 ** (-2.0), "Lotka teórico: α = 2,00", fontsize=8.7, ha="left", va="center", color=E.TINTA)
    ax.text(4.15, y1 * 4 ** (-L["alpha_mle"]) * 0.85, f"Máxima verosimilitud: α = {E.num(L['alpha_mle'],2)}\nIC 95 % bootstrap: {E.num(L['ic_mle'][0],2)} a {E.num(L['ic_mle'][1],2)}", fontsize=8.7, ha="left", va="top", color=E.TINTA)
    ax.text(1.12, 9.0, f"Mínimos cuadrados:\nα = {E.num(L['alpha_ls'],2)}\ndos niveles, 0 grados\nde libertad\nIC 95 %: {E.num(L['ic_ls'][0],2)} a {E.num(L['ic_ls'][1],2)}", fontsize=8.7, ha="left", va="center", color=E.TINTA)
    ax.grid(axis="both")
    pie(fig, "Estimación exploratoria (N < 45): bootstrap de 1.000 réplicas, semilla 42; 42 documentos; año de corte 2026")
    return E.guardar(fig, "c2_lotka")

# ---------------------------------------------------------------- BRADFORD
ABREV = {"International Journal of Environmental Research and Public Health": "Int. J. Environ. Res. Public Health", "International Journal of Environmental Science and Technology": "Int. J. Environ. Sci. Technol."}
def bradford():
    c, pf = D.tabla_fuentes(); zonas, N = D.bradford(c)
    orden = [(z + 1, rev, n) for z, zz in enumerate(zonas) for rev, n in zz]
    fig, ax = E.lienzo(h1="Tres revistas concentran 9 de los 26 artículos", h2="Artículos por revista, ordenadas de mayor a menor, y zonas de Bradford por tercios de artículos; n = 26 artículos, 19 revistas", figsize=(10, 7))
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    cols = {1: E.AZUL, 2: E.MEDIO, 3: E.CLARO}; hat = {1: "", 2: "///", 3: "..."}
    ys = np.arange(len(orden))[::-1]
    for y, (z, rev, n) in zip(ys, orden):
        b = ax.barh(y, n, color=cols[z], edgecolor=E.TINTA, lw=0.7, hatch=hat[z], height=0.72)
        ax.text(n + 0.05, y, str(n), va="center", ha="left", fontsize=9, fontweight="bold", color=E.TINTA)
        ax.text(-0.08, y, __import__("textwrap").fill(ABREV.get(rev, rev), 44), va="center", ha="right", fontsize=8.3, color=E.TINTA, linespacing=1.0)
    ax.set_yticks([]); ax.set_xlim(0, 4.2); ax.set_xlabel("Artículos del corpus por revista")
    ax.spines["left"].set_visible(False)
    zc = [(zonas[z], z + 1) for z in range(3)]
    ini = 0
    for zz, z in zc:
        k = len(zz); top = ys[ini]; bot = ys[ini + k - 1]
        ax.plot([3.55, 3.55], [bot - 0.35, top + 0.35], color=E.TINTA, lw=1.2)
        arts = sum(n for _, n in zz)
        ax.text(3.65, (top + bot) / 2, f"Zona {z}: {k} revistas\n{arts} artículos ({E.num(100*arts/N,1)} %)", va="center", fontsize=8.7, color=E.TINTA, fontweight="bold")
        ini += k
    lo, hi, mu, inv, nb = D.bootstrap_phi()
    ax.text(2.6, ys[len(ys) // 2 + 3], f"φ zona 2 sobre zona 1 = {E.num(8/3,2)}\nIC 95 % bootstrap: {E.num(lo,2)} a {E.num(hi,2)}\nφ zona 3 sobre zona 2 = {E.num(1.0,2)}", fontsize=8.5, color=E.TINTA, ha="center", va="center", bbox=dict(boxstyle="round,pad=0.4", fc=E.CAJA, ec=E.TINTA, lw=0.8))
    pie(fig, "Estimación exploratoria (N < 45); desempate alfabético entre revistas con un artículo; 42 documentos; año de corte 2026; semilla 42")
    fig.subplots_adjust(left=0.36)
    return E.guardar(fig, "c2_bradford")

# ---------------------------------------------------------------- GEOGRÁFICA
def geografica():
    datos = [("Estados Unidos", 12), ("Colombia", 9), ("China", 4), ("España", 3), ("Brasil", 3), ("Reino Unido", 3)]
    fig, ax = E.lienzo(h1="Colombia aporta 9 de los 42 documentos, el segundo lugar tras Estados Unidos", h2="Documentos con al menos una institución del país, F-INF §6.2; un documento puede contar en varios países; 21 nacionalidades", figsize=(10, 4.8))
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    ys = np.arange(len(datos))[::-1]
    for y, (p, n) in zip(ys, datos):
        col = E.AZUL if p == "Colombia" else E.MEDIO
        ax.barh(y, n, color=col, edgecolor=E.TINTA, lw=0.8, hatch="" if p == "Colombia" else "///", height=0.66)
        ax.text(n + 0.15, y, f"{n}  ({E.num(100*n/42,1)} %)", va="center", fontsize=9.5, fontweight="bold", color=E.TINTA)
    ax.set_yticks(ys); ax.set_yticklabels([d[0] for d in datos], fontsize=10)
    ax.set_xlim(0, 16.5); ax.set_xlabel("Documentos del corpus con institución del país (de 42)")
    ax.text(16.4, 0.4, "Quince países restantes: sin desagregar\nen el informe de vigilancia\n8 de 26 artículos (30,8 %) con coautoría internacional", ha="right", va="center", fontsize=8.7, color=E.TINTA)
    fig.subplots_adjust(bottom=0.2)
    pie(fig, "Fuente: F-INF §6.2 (p. 61) y §7.6 (p. 93). Porcentajes sobre 42 documentos; año de corte 2026")
    return E.guardar(fig, "c2_geografica")

# ---------------------------------------------------------------- LÍNEA DE TIEMPO DE PATENTES
PCT = {  # clave -> (prioridad o presentación, plazo 30 meses) F-INF Anexo C, Tabla 68 (p. 221)
 "Koppinen2019": (dt.date(2018, 5, 11), dt.date(2020, 11, 11)), "Gumaste2021": (dt.date(2019, 9, 23), dt.date(2022, 3, 23)),
 "Ali2022": (dt.date(2021, 4, 14), dt.date(2023, 10, 14)), "Izod2023": (dt.date(2022, 1, 21), dt.date(2024, 7, 21)),
 "Wilson2024": (dt.date(2022, 9, 23), dt.date(2025, 3, 23)), "Rine2024": (dt.date(2022, 10, 12), dt.date(2025, 4, 12)),
 "Eckenrode2025": (dt.date(2023, 8, 28), dt.date(2026, 2, 28)), "Machida2025": (dt.date(2024, 6, 10), dt.date(2026, 12, 10)),
 "Acosta2026": (dt.date(2024, 10, 28), dt.date(2027, 4, 28)), "Brkic2026": (dt.date(2025, 2, 28), dt.date(2027, 8, 28))}
TITULAR = {"Reintjes1995": "titular sin identificar", "Koppinen2019": "VTT", "Abernathy2019": "General Electric", "Blythe2020": "Monte Cristo",
 "Gumaste2021": "Cummins", "Ali2022": "titular sin identificar", "Izod2023": "Healthy Space", "Hurst2024": "General Electric", "Wilson2024": "View",
 "Rine2024": "Airthings", "Hale2025": "Disney", "Eckenrode2025": "Auros", "Machida2025": "Ambient X", "Acosta2026": "CosySense", "Brkic2026": "SmartMiner"}
CORTE_FECHA = dt.date(2026, 10, 13)
def anio_frac(d): return d.year + (d.timetuple().tm_yday - 1) / 365.25

def patentes():
    pats = [r for r in D.CORPUS if r["tipo"] == "patente"]
    pats.sort(key=lambda r: (r["year"], r["key"]))
    fig, ax = E.lienzo(h1="Siete de diez solicitudes PCT con Colombia designada tienen el plazo vencido", h2="Patentes del corpus por año de publicación (marcador) y ventana de 30 meses desde la prioridad hasta la fase nacional (barra); 15 patentes", figsize=(10, 7))
    ax.grid(axis="x"); ax.grid(axis="y", visible=False)
    ys = np.arange(len(pats))[::-1]
    X0 = 2016.6
    for y, r in zip(ys, pats):
        k = r["key"]; nom = f"{r['cite']} ({TITULAR.get(k, '')})"
        ax.text(X0 - 0.3, y, nom, ha="right", va="center", fontsize=8.5, color=E.TINTA, clip_on=False)
        if k in PCT:
            a, b = PCT[k]; abierto = b > CORTE_FECHA
            ax.barh(y, anio_frac(b) - anio_frac(a), left=anio_frac(a), height=0.5, color=E.AZUL if abierto else E.CLARO, edgecolor=E.TINTA, lw=0.8, hatch="" if abierto else "///")
            ax.scatter([r["year"] + 0.5], [y], marker="D", s=46, color=E.TINTA, zorder=5)
            if abierto: ax.text(anio_frac(b) + 0.15, y, "hasta " + b.strftime("%d/%m/%Y"), va="center", fontsize=8, color=E.TINTA, fontweight="bold")
            elif anio_frac(b) < 2024.0: ax.text(anio_frac(b) + 0.15, y, "vencido " + b.strftime("%d/%m/%Y"), va="center", ha="left", fontsize=8, color=E.TINTA)
            else: ax.text(anio_frac(a) - 0.15, y, "vencido " + b.strftime("%d/%m/%Y"), va="center", ha="right", fontsize=8, color=E.TINTA)
        elif k == "Reintjes1995":
            ax.scatter([X0 + 0.1], [y], marker="<", s=70, color=E.TINTA, zorder=5)
            ax.text(X0 + 0.5, y, "publicada en 1995, prioridad de 1993; vigencia de 20 años superada", va="center", fontsize=8, color=E.TINTA)
        else:
            ax.scatter([r["year"] + 0.5], [y], marker="s", s=46, color=E.MEDIO, edgecolor=E.TINTA, zorder=5)
            ax.text(r["year"] + 0.5 - 0.35, y, "solicitud europea", va="center", ha="right", fontsize=8, color=E.TINTA)
    ax.axvline(anio_frac(CORTE_FECHA), color=E.TINTA, ls="--", lw=1.3)
    ax.text(anio_frac(CORTE_FECHA) + 0.12, len(pats) - 0.55, "Corte 13/10/2026", ha="left", va="top", fontsize=8.5, color=E.TINTA, fontweight="bold")
    ax.set_xlim(X0, 2029.4); ax.set_ylim(-0.8, len(pats) - 0.2); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.set_xticks(range(2017, 2030)); ax.set_xlabel("Año calendario")
    ax.legend(handles=[Line2D([], [], marker="D", ls="", color=E.TINTA, label="Publicación (solicitud PCT)"), Line2D([], [], marker="s", ls="", color=E.MEDIO, markeredgecolor=E.TINTA, label="Publicación (solicitud europea)"),
                       Patch(fc=E.CLARO, ec=E.TINTA, hatch="///", label="Plazo de 30 meses vencido"), Patch(fc=E.AZUL, ec=E.TINTA, label="Plazo de 30 meses abierto")], loc="lower left", fontsize=8, bbox_to_anchor=(0.0, 0.0))
    fig.subplots_adjust(left=0.30)
    pie(fig, "Fuente: F-INF Anexo C (p. 221), §5.7 (p. 55) y §13.2; plazos con conocimiento externo, NO_VERIFICADO; 15 patentes; año de corte 2026")
    return E.guardar(fig, "c2_patentes")

if __name__ == "__main__":
    print(prisma("c2_prisma", "Solo la etapa de inclusión tiene números documentados: 42 documentos"))
    print(prisma("cF3_prisma", "Solo la etapa de inclusión tiene números documentados: 42 documentos"))
    print(produccion()); print(lotka()); print(bradford()); print(geografica()); print(patentes())
