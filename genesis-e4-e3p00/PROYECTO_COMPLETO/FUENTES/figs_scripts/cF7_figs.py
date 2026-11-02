# -*- coding: utf-8 -*-
"""Figura F7.1: cadena Output -> Outcome -> Impact del proyecto. Datos: maestro/indicadores.py (IND) y maestro.py."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, RAIZ + "/maestro")
import estilo as E
import indicadores as I
import maestro as M
IND = {i["cod"]: i for i in I.IND}
fig, ax = E.lienzo_libre(h1="Diez outputs sostienen tres outcomes y dos impactos que se miden después del cierre",
                         h2="Cadena lógica de los 15 indicadores PERS; los impactos se evalúan entre 6 y 12 meses posteriores al cierre (PROPUESTO)",
                         figsize=(10, 6.8), xlim=(0, 100), ylim=(0, 62))
cols = [(1, 21, "INSUMOS", E.CAJA), (25, 24, "OUTPUTS (R y P)", E.CLARO), (53, 22, "OUTCOMES (E)", E.MEDIO), (79, 20, "IMPACT (S)", E.AZUL)]
for x, w, t, c in cols:
    E.caja(ax, x, 55, w, 5, t, relleno=c, bold=True, fs=10)
def col(x, w, items, y0, paso, h, fs):
    for k, t in enumerate(items):
        E.caja(ax, x, y0 - k * paso, w, h, t, relleno=E.CAJA, fs=fs)
col(1, 21, ["SGR\n" + M.mm(M.total(M.BUDGET)) + " M COP", "Contrapartida\n" + M.mm(M.total(M.CONTRA)) + " M COP", "29 cargos\ndel equipo", "120 nodos, 11 gateways\ny 3 referencias"], 44, 12, 8.5, 8.6)
col(25, 24, ["P01 · 100 nodos y 10\ngateways operativos", "P02 · software de corrección\ny gemelo digital", "P03 · 2 artículos Q1 o Q2\nsometidos", "P04 · 29 actividades de\napropiación social", "R01 a R06 · despliegue,\ncalibración, horas-nodo\ne informes"], 46, 10.2, 8.2, 8.0)
col(53, 22, ["E01 · uso del tablero\n≥ 75 % de 15 comités", "E02 · falsas alarmas\n−30 % relativo", "E03 · ≥ 60 personas\ncertificadas"], 44, 15, 10, 8.4)
col(79, 20, ["S01 · protocolo activado\n≥ 80 % a 12 meses\ndel cierre", "S02 · red bajo custodia\n≥ 70 % a 12 meses\ndel cierre"], 40, 18, 12, 8.4)
for (x0, x1, y) in [(22.6, 24.6, 33), (49.6, 52.6, 33), (75.6, 78.6, 33)]:
    E.flecha(ax, (x0, y), (x1, y), lw=1.6)
ax.text(23.6, 30.6, "act.", fontsize=7.2, ha="center"); ax.text(51.1, 30.6, "uso", fontsize=7.2, ha="center"); ax.text(77.1, 30.6, "efecto", fontsize=7.2, ha="center")
ax.text(50, 0.5, "Los outputs R04 y R06 son de gestión y condicionan la ejecución; ningún indicador de nivel R o P se presenta como impacto.",
        ha="center", fontsize=8.4, color=E.TINTA)
E.guardar(fig, "cF7_f01")
