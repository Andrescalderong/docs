# -*- coding: utf-8 -*-
"""Gráfico integrado del proyecto SIGP 143329: red problema-solución, árbol de decisión,
marco conceptual por actividades y compromisos y valor de cada actor.
Uso: python3 grafico_integrado.py salida_sin_extension"""
import sys, json, textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.lines import Line2D

D = json.load(open("/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/diag_data.json"))
ACT = {a["id"]: a for a in D["acts"]}
OUT = sys.argv[1]

TINTA, MUTE, LINEA = "#1d2a33", "#5a6772", "#b9c4cc"
POLVO, POLVO_S = "#a85a17", "#f6e5d3"
OBJ, OBJ_S = "#34489a", "#e1e6f7"
SOL, SOL_S = "#0f6e6a", "#d7efeb"
NO, BLANCO = "#a33a2c", "#ffffff"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "text.parse_math": False})

W, H = 240, 207             # unidades de dibujo (1 u = 0,1 pulgada)
fig = plt.figure(figsize=(W / 10, H / 10), dpi=150)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
fig.patch.set_facecolor(BLANCO)

def caja(x, y, w, h, txt="", fc=BLANCO, ec=LINEA, lw=1.2, fs=8.6, bold=False, ls="-", ha="center", wrap=None, color=TINTA, titulo=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.8", fc=fc, ec=ec, lw=lw, ls=ls, zorder=2))
    wrap = wrap or max(8, int(w * 1.22 * 8.6 / fs))
    lineas = []
    if titulo:
        lineas.append(("t", titulo))
    for p in txt.split("\n"):
        for l in textwrap.wrap(p, wrap) or [""]:
            lineas.append(("c", l))
    n = len(lineas); lh = fs * 0.165
    y0 = y + h / 2 + (n - 1) * lh / 2
    xt = x + w / 2 if ha == "center" else x + 1.2
    for i, (k, l) in enumerate(lineas):
        ax.text(xt, y0 - i * lh, l, ha=ha, va="center", fontsize=fs, color=color,
                fontweight="bold" if (bold or k == "t") else "normal", zorder=3)
    return (x, y, w, h)

def flecha(p, q, col=LINEA, lw=1.0, curva=0.0, z=1):
    ax.annotate("", xy=q, xytext=p, zorder=z,
                arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=8,
                                connectionstyle=f"arc3,rad={curva}"))

def der(b): x, y, w, h = b; return (x + w, y + h / 2)
def izq(b): x, y, w, h = b; return (x, y + h / 2)
def aba(b): x, y, w, h = b; return (x + w / 2, y)
def arr(b): x, y, w, h = b; return (x + w / 2, y + h)

def banda(y, h, num, titulo, sub):
    ax.text(3, y + h - 1.5, f"{num}  {titulo}", fontsize=13, fontweight="bold", color=TINTA, va="top")
    ax.text(3, y + h - 5.2, sub, fontsize=8.8, color=MUTE, va="top")
    ax.plot([3, W - 3], [y + h + 1.2, y + h + 1.2], color=LINEA, lw=0.8)

# ------------------------------------------------------------------ título
ax.text(3, H - 2.5, "Del polvo posterremoto a una alerta con error conocido", fontsize=19, fontweight="bold", color=TINTA, va="top")
ax.text(3, H - 8.0, "Red IoT híbrida Edge-Cloud y gemelo digital · Manizales (Caldas) y Calarcá (Quindío) · SIGP 143329 · "
        "SGR $ 13.999.405.215 · contrapartida $ 1.774.000.000 (efectivo $ 150.000.000) · 24 meses · 100 nodos y 10 gateways · TRL 4 → 8",
        fontsize=9.6, color=MUTE, va="top")

# ================================================================== 1. RED
Y1, H1 = 106, 86
banda(Y1, H1, "1", "Diagrama de red: del problema a la solución",
      "Las flechas siguen el árbol de problemas y el de objetivos; cada actividad lleva su resultado. Relaciones como hipótesis de influencia, no efectos estimados.")
top = Y1 + H1 - 9
# Detonante
d1 = caja(3, top - 10, 20, 8, "Sismo del\n10 de agosto de 2026", POLVO_S, POLVO, fs=8.4, bold=True)
d2 = caja(3, top - 24, 20, 10, "Demolición y remoción de escombros en centros urbanos", POLVO_S, POLVO, fs=8.2)
flecha(aba(d1), arr(d2), POLVO)
ax.text(13, top + 0.8, "DETONANTE", fontsize=7.6, color=MUTE, ha="center", fontweight="bold")
# Causas
causas = [("Humedad altera la lectura óptica", "D"), ("Fracción gruesa de PM10 sin corregir", "D"),
          ("PM2,5 sin referencia colocalizada", "D"), ("Calibración baja o nula", "D"),
          ("Remoción degrada nodos, energía y enlace", "I"), ("Demolición sin estimar la exposición", "C")]
ax.text(37, top + 0.8, "CAUSAS", fontsize=7.6, color=MUTE, ha="center", fontweight="bold")
cb = []
for i, (t, k) in enumerate(causas):
    b = caja(27, top - 6 - i * 6.6, 20, 5.6, t, POLVO_S if k == "D" else BLANCO, POLVO, fs=7.6, ls="-" if k == "D" else "--")
    cb.append(b)
for i in (1, 4, 5):
    flecha(der(d2), izq(cb[i]), POLVO, 0.8)
# Problema central
ax.text(62, top + 0.8, "PROBLEMA CENTRAL", fontsize=7.6, color=MUTE, ha="center", fontweight="bold")
pc = caja(51, top - 24, 22, 17, "Los consejos deciden alertas con mediciones de PM2,5 y PM10 sin error conocido", POLVO_S, POLVO, lw=2.2, fs=8.2, bold=True, wrap=22)
ef = caja(51, top - 38, 22, 10, "Efectos: índice sin validar, falsas alarmas sin medir, baja adopción", BLANCO, POLVO, fs=7.8, ls="--")
for b in cb[:5]:
    flecha(der(b), izq(pc), POLVO, 0.8)
flecha(aba(pc), arr(ef), POLVO)
# Objetivos
ax.text(87, top + 0.8, "OBJETIVOS", fontsize=7.6, color=MUTE, ha="center", fontweight="bold")
oes = {"OE1": "OE1 · Corregir la medición y validar el gemelo predictivo",
       "OE2": "OE2 · Red disponible y laboratorio de modelación",
       "OE3": "OE3 · Uso institucional del tablero y custodia"}
ob = {}
for i, (k, t) in enumerate(oes.items()):
    ob[k] = caja(77, top - 9 - i * 12.5, 20, 10, t, OBJ_S, OBJ, fs=8.0, bold=False)
for i in range(4): flecha(der(cb[i]), izq(ob["OE1"]), OBJ, 0.6, 0.1)
flecha(der(cb[5]), izq(ob["OE1"]), OBJ, 0.6, 0.15)
flecha(der(cb[4]), izq(ob["OE2"]), OBJ, 0.6, 0.0)
flecha(der(ef), izq(ob["OE3"]), OBJ, 0.8)
# Actividades (bloques por objetivo)
ax.text(127, top + 0.8, "ACTIVIDADES (21) · SGR / contrapartida en millones de COP", fontsize=7.6, color=MUTE, ha="center", fontweight="bold")
ab = {}
grupos = {"OE1": [a for a in D["acts"] if a["oe"] == "OE1"], "OE2": [a for a in D["acts"] if a["oe"] == "OE2"], "OE3": [a for a in D["acts"] if a["oe"] == "OE3"]}
ycur = top - 1.5
for oe, acts in grupos.items():
    y0 = ycur
    for a in acts:
        y = ycur - 3.7
        lab = f"{a['id']}  {a['n']}"
        lab = lab if len(lab) <= 66 else lab[:64] + "…"
        val = f"{a['sgr']/1e6:,.0f}".replace(",", ".") + (f" / {a['con']/1e6:,.0f}".replace(",", ".") if a["con"] else "")
        ab[a["id"]] = caja(101, y, 52, 3.2, lab, BLANCO, LINEA, fs=6.9, ha="left", wrap=200)
        ax.text(152.3, y + 1.6, val, fontsize=6.6, color=MUTE, ha="right", va="center", zorder=4)
        ycur -= 3.7
    flecha(der(ob[oe]), (101, (y0 + ycur) / 2), OBJ, 0.9)
    ycur -= 0.8
# Resultados
RES = {"R1": ("R1 · R² ≥ 0,70 y NRMSE ≤ 30 %", ["1.3", "1.4", "1.5", "1.6"]), "R2": ("R2 · Disponibilidad ≥ 90 %", ["2.1", "2.2", "2.3", "2.4"]),
       "R3": ("R3 · ≥ 75 % de consejos decide con el tablero", ["3.1", "3.2"]), "R4": ("R4 · Falsas alarmas −30 % o más", ["3.1", "3.2"]),
       "R5": ("R5 · 60 custodios certificados", ["3.3", "3.4"]), "R6": ("R6 · Gemelo FAC2 ≥ 0,5 en ≥ 6 eventos", ["1.7", "2.5", "2.6", "2.7"]),
       "R7": ("R7 · 12 evaluaciones previas de demolición", ["3.5"])}
ax.text(170, top + 0.8, "RESULTADOS (mes 24)", fontsize=7.6, color=MUTE, ha="center", fontweight="bold")
rb = {}
for i, (k, (t, acts)) in enumerate(RES.items()):
    rb[k] = caja(159, top - 6 - i * 6.2, 22, 5.2, t, SOL_S, SOL, fs=7.4)
    for a in acts:
        flecha(der(ab[a]), izq(rb[k]), SOL, 0.45, 0.0)
# Impactos
ax.text(195, top + 0.8, "IMPACTOS (mes 36)", fontsize=7.6, color=MUTE, ha="center", fontweight="bold")
i1 = caja(186, top - 14, 18, 10, "I1 · Protocolo activado ante ≥ 80 % de las superaciones", SOL_S, SOL, lw=2, fs=7.8, bold=True)
i2 = caja(186, top - 30, 18, 10, "I2 · ≥ 70 % de la red operando bajo custodia", SOL_S, SOL, lw=2, fs=7.8, bold=True)
for r in ("R3", "R4", "R5"): flecha(der(rb[r]), izq(i1), SOL, 0.8)
for r in ("R2", "R5"): flecha(der(rb[r]), izq(i2), SOL, 0.8)
# leyenda
lx = 208
for i, (fc, ec, t) in enumerate([(POLVO_S, POLVO, "Problema y causas"), (OBJ_S, OBJ, "Objetivos"), (BLANCO, LINEA, "Actividades"), (SOL_S, SOL, "Resultados e impactos")]):
    caja(lx, top - 4 - i * 5, 4, 3.2, "", fc, ec)
    ax.text(lx + 5.5, top - 2.4 - i * 5, t, fontsize=8, va="center", color=TINTA)
ax.text(lx, top - 25, "Línea discontinua:\ncausa indirecta o\ncomplementaria", fontsize=7.6, color=MUTE, va="top")

# ================================================================== 2. ÁRBOL DE DECISIÓN
Y2, H2 = 53, 42
banda(Y2, H2, "2", "Árbol de decisión: las compuertas liberan cada compra",
      "Criterios fijados antes de medir. Un «no» no reduce el alcance: abre un ciclo de corrección o activa la custodia alterna.")
G = [("Mes 12 · C1", "¿El piloto cumple?", "30 nodos: R² ≥ 0,70 y NRMSE ≤ 30 %;\n≥ 50 % de consejos usa el tablero",
      "Libera tramo 2 (40 nodos)\nentrega protocolo y series", "Ciclo de corrección y\nmesa de gestión con consejos"),
     ("Mes 17 · C2", "¿La red escala?", "Umbrales en los 2 municipios;\ndisponibilidad ≥ 90 %;\nconvenios de custodia con partida",
      "Libera tramo 3 (30 nodos);\n100 nodos al mes 19 (TRL 7)", "Reentrenar por municipio;\ncustodia alterna"),
     ("Mes 22 · H11", "¿El gemelo acierta?", "FAC2 ≥ 0,5 y |sesgo| ≤ 0,3 en\n≥ 6 demoliciones reales; mejor\nque el cribado genérico",
      "Protocolo de evaluación\nprevia y 12 informes", "Uso restringido al\ndominio validado"),
     ("Mes 24 · C3", "¿Se transfiere?", "Ensayo independiente del mes 23\n(TRL 8); 60 custodios;\nactas por componente",
      "Custodia distribuida con\npartida y personal", "Cláusula de apertura:\ndatos y código abiertos")]
gx, gw, gap = 3, 40, 3.5
yq = Y2 + H2 - 21
inicio = caja(gx, yq + 1, 14, 9, "Mes 2 · H0\nInicio y\ncontratación", OBJ_S, OBJ, fs=7.6)
prev = inicio
for i, (mes, q, crit, si, no) in enumerate(G):
    x = gx + 17 + i * (gw + gap)
    qb = caja(x, yq - 2, gw, 14, crit, OBJ_S, OBJ, fs=7.3, titulo=f"{mes} · {q}")
    flecha(der(prev), izq(qb), OBJ, 1.2)
    sb = caja(x, yq - 20, gw / 2 - 0.8, 13, si, SOL_S, SOL, fs=7.0, titulo="Sí")
    nb = caja(x + gw / 2 + 0.8, yq - 20, gw / 2 - 0.8, 13, no, BLANCO, NO, fs=7.0, ls="--", titulo="No", color=TINTA)
    flecha((x + gw * 0.25, yq - 2), arr(sb), SOL, 1.0)
    flecha((x + gw * 0.75, yq - 2), arr(nb), NO, 1.0)
    prev = qb

# ================================================================== 3. MARCO CONCEPTUAL (a la derecha del árbol)
mx = 196
ax.text(mx, Y2 + H2 - 1.5, "3  Marco conceptual por actividades", fontsize=13, fontweight="bold", color=TINTA, va="top")
ax.text(mx, Y2 + H2 - 5.2, "Cada teoría explica un eslabón y\norigina actividades verificables.", fontsize=8.6, color=MUTE, va="top")
F = [("Metrología y calibración", "1.1–1.6"), ("Computación en el borde", "2.1–2.4"), ("Gemelo digital y dispersión", "1.7, 2.5–2.7, 3.5"),
     ("Gestión del riesgo y alerta", "3.1, 3.2"), ("Adopción de tecnología", "3.1–3.3"), ("Gobernanza de recursos comunes", "3.3, 3.4"),
     ("Aprendizaje de doble bucle", "1.4–1.6 y compuertas")]
fy = Y2 + H2 - 14
prevb = None
for i, (t, acts) in enumerate(F):
    b = caja(mx, fy - i * 4.6, 41, 3.9, f"{t}  →  {acts}", BLANCO, OBJ, fs=7.4, ha="left", wrap=200)
    if prevb: flecha(aba(prevb), arr(b), OBJ, 0.7)
    prevb = b
ax.text(mx, fy - 7 * 4.6 + 3.2, "Dato con error conocido → corregido en el borde → estimado → alerta →\nadoptado → custodiado → revisado en cada compuerta", fontsize=7.2, color=MUTE, va="top")

# ================================================================== 4. ACTORES: compromisos y valor
Y4, H4 = 3, 44
banda(Y4, H4, "4", "Compromisos y valor de cada actor",
      "● lidera o ejecuta   ○ participa o apoya. El valor es capacidad, resultados y uso documentado; ningún actor recibe ingresos prometidos.")
ACTS = [a["id"] for a in D["acts"]]
LIDER = ("Lidera", "Dirige", "Coordina", "Ejecuta", "Organiza", "Forma", "Entrena", "Instala", "Reentrena", "Registra", "Diseña", "Desarrolla", "Construye", "Valida", "Compra", "Administra")
def nivel(r):
    if not r or r.startswith("No participa") or r.startswith("Reporta"): return 0
    return 2 if r.startswith(LIDER) else 1
AC = [("IES", "Universidad Santo Tomás", "$ 1.244 M especie · ejecuta el SGR", "9 documentos, 9 personas formadas,\nlaboratorio de modelación, TRL 8 validado"),
      ("MAN", "Municipio de Manizales", "$ 60 M especie", "Tablero y protocolo en uso, custodios\nformados, evaluaciones de demoliciones"),
      ("CAL", "Municipio de Calarcá", "$ 60 M especie", "Tablero y protocolo en uso, custodios\nformados, evaluaciones de demoliciones"),
      ("AVA", "Avanciencia (OTRI)", "$ 150 M especie · ejecuta $ 1.347 M SGR\n(ASC $ 892,6 M; transferencia $ 454,5 M)", "Cartera valorada y protegida, acuerdos\nde PI, experiencia en apropiación"),
      ("GMA", "Gestión y Medio Ambiente", "$ 110 M especie + $ 150 M efectivo\n(1,07 % del SGR: criterio 7)", "Desempeño de sus equipos frente a\nla referencia, gobernanza")]
x0, cw = 50, 4.25
yh = Y4 + H4 - 14
# encabezados de actividades
for j, a in enumerate(ACTS):
    oe = ACT[a]["oe"]; col = {"OE1": OBJ, "OE2": SOL, "OE3": POLVO}[oe]
    ax.text(x0 + j * cw + cw / 2, yh, a, fontsize=7.2, ha="center", va="center", color=col, fontweight="bold")
for oe, col in (("OE1", OBJ), ("OE2", SOL), ("OE3", POLVO)):
    js = [j for j, a in enumerate(ACTS) if ACT[a]["oe"] == oe]
    ax.plot([x0 + js[0] * cw + 0.4, x0 + (js[-1] + 1) * cw - 0.4], [yh + 2.2, yh + 2.2], color=col, lw=2)
    ax.text(x0 + (js[0] + js[-1] + 1) * cw / 2, yh + 3.6, oe, fontsize=8, ha="center", color=col, fontweight="bold")
ax.text(3, yh, "Actor", fontsize=8, fontweight="bold", color=MUTE, va="center")
ax.text(25, yh, "Aporta", fontsize=8, fontweight="bold", color=MUTE, va="center")
vx = x0 + len(ACTS) * cw + 2
ax.text(vx, yh, "Qué recibe (valor)", fontsize=8, fontweight="bold", color=MUTE, va="center")
rh = 5.6
for i, (k, n, ap, val) in enumerate(AC):
    y = yh - 3.5 - (i + 1) * rh + rh / 2
    if i % 2 == 0:
        ax.add_patch(FancyBboxPatch((2.5, y - rh / 2), W - 5, rh, boxstyle="round,pad=0,rounding_size=0.5", fc="#f2f5f7", ec="none", zorder=0))
    ax.text(3, y, n, fontsize=8.4, fontweight="bold", color=TINTA, va="center")
    ax.text(25, y, ap, fontsize=7.0, color=TINTA, va="center", linespacing=1.15)
    for j, a in enumerate(ACTS):
        lv = nivel(ACT[a]["roles"].get(k, ""))
        cx = x0 + j * cw + cw / 2
        if lv == 2: ax.add_patch(Circle((cx, y), 1.05, fc=TINTA, ec=TINTA, zorder=3))
        elif lv == 1: ax.add_patch(Circle((cx, y), 1.0, fc=BLANCO, ec=TINTA, lw=1.1, zorder=3))
    ax.text(vx, y, val, fontsize=7.0, color=TINTA, va="center", linespacing=1.15)

fig.savefig(OUT + ".png", dpi=150, facecolor=BLANCO)
fig.savefig(OUT + ".pdf", facecolor=BLANCO)
print("ok", OUT)
