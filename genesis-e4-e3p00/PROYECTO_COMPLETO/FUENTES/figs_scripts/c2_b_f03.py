# -*- coding: utf-8 -*-
"""Figura c2_b_f03 (Capítulo 2, sección 2.6): red de conexiones entre las referencias clave.
Nodos: 8 referencias con ficha (Tablas b_t09 a b_t16) y 5 referencias de apoyo del banco (Kumar 2026, Tavella 2026, Giordano 2021, Stieb 2008,
Rodríguez-Villamizar 2022). Aristas: los 16 vínculos de la matriz b_t17. Tipo de vínculo: A acuerdo, C complemento, D desacuerdo.
Grosor grueso = vínculo DOCUMENTADO en F-INF (§7.7, §8.3, §12.3, §12.4); grosor fino = lectura del proyecto (INFERIDO).
No usa aleatoriedad (posiciones fijas). Salida: figs/out/c2_b_f03.png y .svg"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import estilo as E

W, H = 16.2, 8.2
NODOS = {   # clave: (x, y, etiqueta, origen, con_ficha)
    "Jay":  (11, 44, "Jayaratne et al.\n(2018)", "dominio", True),
    "Sur":  (29, 59, "Suresh et al.\n(2025)", "corpus", True),
    "Bark": (22, 25, "Barkjohn et al.\n(2021)", "dominio", True),
    "Gio":  (9, 9, "Giordano et al.\n(2021)", "dominio", False),
    "EPA":  (45, 9, "EPA\n(2021)", "dominio", True),
    "Bang": (42, 41, "Bang et al.\n(2026)", "corpus", True),
    "Kum":  (64, 60, "Kumar et al.\n(2026)", "corpus", False),
    "Tav":  (89, 60, "Tavella et al.\n(2026)", "corpus", False),
    "Mur":  (66, 40, "Murad Pedraza et al.\n(2026)", "corpus", True),
    "Rui":  (91, 40, "Ruiz-Carrascal et al.\n(2026)", "corpus", True),
    "RV":   (79, 24, "Rodríguez-Villamizar\net al. (2022)", "corpus", False),
    "Lia":  (90, 9, "Liao et al.\n(2026)", "corpus", True),
    "Sti":  (66, 9, "Stieb et al.\n(2008)", "dominio", False),
}
# (origen, destino, tipo, documentado)
ARISTAS = [
    ("Bang", "Bark", "C", False), ("Bang", "Sur", "A", True), ("Sur", "Jay", "A", False), ("Jay", "Bark", "A", False),
    ("Mur", "Bang", "C", True), ("Mur", "Rui", "D", True), ("Rui", "Bang", "A", False), ("EPA", "Bang", "C", False),
    ("EPA", "Bark", "C", False), ("Lia", "Sti", "A", False), ("Tav", "Mur", "A", True), ("Tav", "Kum", "D", True),
    ("Kum", "Bang", "A", True), ("Gio", "Bark", "C", False), ("Lia", "RV", "C", True), ("RV", "Mur", "C", False),
]
assert len(ARISTAS) == 16 and sum(1 for a in ARISTAS if a[2] == "D") == 2
ESTILO = {"A": "-", "C": (0, (1, 2.2)), "D": (0, (5, 3))}

fig, ax = E.lienzo_libre(h1="Solo dos de 16 vínculos entre las referencias clave son desacuerdos",
                         h2="Red de 13 referencias (8 con ficha, borde grueso); los otros 14 vínculos son acuerdos o complementos; trazo grueso = DOCUMENTADO en F-INF, fino = INFERIDO",
                         figsize=(10, 7), xlim=(0, 100), ylim=(-9, 68))

for o, d, t, doc in ARISTAS:
    x0, y0 = NODOS[o][0], NODOS[o][1]; x1, y1 = NODOS[d][0], NODOS[d][1]
    ax.plot([x0, x1], [y0, y1], color=E.TINTA, lw=2.4 if doc else 1.0, ls=ESTILO[t], zorder=1, solid_capstyle="butt")
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    ax.text(mx, my, t, fontsize=9, fontweight="bold", color=E.TINTA, ha="center", va="center", zorder=2,
            bbox=dict(boxstyle="round,pad=0.15", fc=E.MARFIL, ec=E.TINTA, lw=0.5))

for k, (x, y, et, origen, ficha) in NODOS.items():
    relleno = E.MEDIO if origen == "corpus" else E.CLARO
    p = E.caja(ax, x - W / 2, y - H / 2, W, H, et, relleno=relleno, fs=7.8, bold=ficha, grosor=2.4 if ficha else 0.9)
    p.set_zorder(3)
    for t in ax.texts[-1:]:
        t.set_zorder(4)

ley = [Patch(fc=E.MEDIO, ec=E.TINTA, label="Corpus F-INF"), Patch(fc=E.CLARO, ec=E.TINTA, label="Literatura de dominio"),
       Line2D([0], [0], color=E.TINTA, lw=1.0, ls=ESTILO["A"], label="A acuerdo"),
       Line2D([0], [0], color=E.TINTA, lw=1.0, ls=ESTILO["C"], label="C complemento"),
       Line2D([0], [0], color=E.TINTA, lw=1.0, ls=ESTILO["D"], label="D desacuerdo"),
       Line2D([0], [0], color=E.TINTA, lw=2.4, ls="-", label="Documentado (grueso)")]
ax.legend(handles=ley, loc="lower center", bbox_to_anchor=(0.5, 0.0), fontsize=8, frameon=False, ncol=3)
fig.text(0.01, -0.02, "Nota. Vínculos de la matriz de conexiones; fuentes en F-INF §7.7 (p. 95), §8.3 (p. 102), §12.3 y §12.4 (pp. 196-197). Posiciones fijas, sin semilla; n = 13 nodos y 16 aristas.",
         fontsize=7.5, color=E.TINTA, ha="left", va="bottom")
print(E.guardar(fig, "c2_b_f03"))
