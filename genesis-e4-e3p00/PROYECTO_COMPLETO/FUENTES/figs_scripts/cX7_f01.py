# -*- coding: utf-8 -*-
"""Figura cX7_f01: roadmap tecnológico en cuatro carriles y tres horizontes, con la escala TRL. Fechas y cifras de la ficha maestra; el seguimiento
posproyecto (meses 25 a 36) y los años 4 a 5 o más son PROPUESTOS o condicionados. Determinista."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
import estilo as E
from matplotlib.patches import Rectangle, FancyBboxPatch, Patch

def celda(ax, x, y, w, h, texto, fc, ls="-", hatch=None, fs=8.2, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2,rounding_size=0.6", fc=fc, ec=E.TINTA, lw=1.1, ls=ls, hatch=hatch))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=fs, color=E.TINTA, linespacing=1.22, fontweight="bold" if bold else "normal")

def main():
    fig, ax = C.lienzo_libre2(h1="El TRL pasa de 4 a 7 en 24 meses y el TRL 8 queda condicionado a evaluación independiente",
                              h2="Roadmap tecnológico en cuatro carriles y tres horizontes; el seguimiento posproyecto y los años 4 a 5 son PROPUESTOS o condicionados",
                              figsize=(10, 6.6), xlim=(0, 100), ylim=(6, 66), top=0.88)
    # columnas: (x, ancho, tipo)
    cols = [(13.0, 21.5, "proy"), (36.0, 18.5, "proy"), (56.0, 18.5, "seg"), (76.0, 23.0, "cond")]
    estilo = {"proy": (E.CLARO, "-", None), "seg": (E.MEDIO, "-", None), "cond": (E.GRIS, "--", None)}
    # encabezados de horizonte
    ax.add_patch(Rectangle((13.0, 59.3), 21.5, 4.6, fc=E.CAJA, ec=E.TINTA, lw=1.1))
    ax.text(23.75, 61.6, "Horizonte 1: año 1\n(meses 1 a 12)", ha="center", va="center", fontsize=8.6, fontweight="bold", color=E.TINTA)
    ax.add_patch(Rectangle((36.0, 59.3), 38.5, 4.6, fc=E.CAJA, ec=E.TINTA, lw=1.1))
    ax.text(55.25, 61.6, "Horizonte 2: años 2 y 3 (meses 13 a 36)", ha="center", va="center", fontsize=8.6, fontweight="bold", color=E.TINTA)
    ax.add_patch(Rectangle((76.0, 59.3), 23.0, 4.6, fc=E.CAJA, ec=E.TINTA, lw=1.1))
    ax.text(87.5, 61.6, "Horizonte 3: años 4 y 5 o más\n(desde el mes 37)", ha="center", va="center", fontsize=8.6, fontweight="bold", color=E.TINTA)
    # fila TRL
    trl = ["TRL 4 a 5\nColocalización en el\npiloto (C1, mes 12)", "TRL 6 en C2 (mes 17)\nTRL 7 en el mes 24", "TRL 7 sostenido\ncon seguimiento\n(meses 25 a 36)", "TRL 8 condicionado a\nevaluación independiente"]
    ax.text(0.5, 54.5, "Escala TRL", ha="left", va="center", fontsize=9.2, fontweight="bold", color=E.TINTA)
    for (x, w, t), txt in zip(cols, trl):
        f, ls, h = estilo[t]
        celda(ax, x, 51.3, w, 6.6, txt, f, ls, h, fs=8.0, bold=True)
    lanes = [
        ("Mercado y\nnecesidades", ["Línea base de error\npor departamento\nUmbrales locales\nen co-diseño", "Uso del tablero por\n15 comités (≥ 75 %\nal mes 24) y\nconvenios con partida",
                                      "Protocolo activado\n(≥ 80 %) y red bajo\ncustodia, medidos\ntras el cierre", "Otras zonas de\nposdesastre y otras\nredes (condicionado\na TdR y custodios)"]),
        ("Productos y\nservicios", ["v1.0 piloto:\n30 nodos, 3 gateways,\nmodelo de corrección\ny tablero piloto", "v2.0: 70 nodos (mes 17)\nv3.0: 100 nodos y\n10 gateways (mes 19)\nRegistro DNDA",
                                      "v3.x operada por\ncustodios y\nevaluación externa\nposproyecto", "Opciones sin\npresupuestar: más\nnodos, un cuarto tramo\ny custodia adicional"]),
        ("Tecnologías", ["Actuales: sensor óptico,\nLoRa, celular y solar\nA desarrollar: corrección\nen gateway", "Reentrenamiento por\ndepartamento, enlace\nsatelital alterno y\nensayo independiente",
                         "Mantenimiento del\nmodelo con datos\nde la custodia", "A evaluar con evidencia:\ncorrección en el nodo\n(fuera de alcance,\nDEC-F02)"]),
        ("Recursos y\ncapacidades", ["Equipo contratado\n(mes 2), 3 referencias\ny banco de calibración", "60 personas certificadas\ny 29 actividades de\napropiación social",
                                     "Custodios con partida\ny competencia\n(≥ 70 % a 12 meses)", "Alianzas: comités,\nUNGRD, alcaldías,\ncustodios y laboratorios"]),
    ]
    y = 42.0; h = 8.4; paso = 10.4
    for nombre, textos in lanes:
        ax.text(0.5, y + h / 2, nombre, ha="left", va="center", fontsize=9.2, fontweight="bold", color=E.TINTA)
        for k, ((x, w, t), txt) in enumerate(zip(cols, textos)):
            f, ls, hh = estilo[t]
            celda(ax, x, y, w, h, txt, f, ls, hh, fs=7.6)
        for (x0, w0, _), (x1, w1, _) in zip(cols[:-1], cols[1:]):
            E.flecha(ax, (x0 + w0 + 0.35, y + h / 2), (x1 - 0.35, y + h / 2), lw=1.0)
        y -= paso
    ax.legend(handles=[Patch(fc=E.CLARO, ec=E.TINTA, label="Proyecto financiado (meses 1 a 24)"), Patch(fc=E.MEDIO, ec=E.TINTA, label="Seguimiento posproyecto (meses 25 a 36, PROPUESTO)"),
                       Patch(fc=E.GRIS, ec=E.TINTA, ls="--", label="Condicionado a TdR y a evaluación (años 4 a 5 o más)")],
              loc="lower center", ncol=3, fontsize=8.2, bbox_to_anchor=(0.5, -0.02), frameon=False)
    E.guardar(fig, "cX7_f01")

if __name__ == "__main__":
    main(); print("figura cX7_f01 generada")
