# -*- coding: utf-8 -*-
"""Figura F7.0 del Paso 7: cadena lógica Output -> Outcome -> Impact del proyecto.
Datos: maestro.py (presupuesto, equipo) e indicadores.py (15 indicadores PERS). Sin componente aleatorio."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); RAIZ = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, RAIZ + "/maestro")
import estilo as E
import maestro as M
import indicadores as I

def f00():
    r = M.resumen()
    fig, ax = E.lienzo_libre(
        h1="La cadena del proyecto separa 10 outputs, 3 outcomes y 2 impactos institucionales",
        h2="Cadena lógica Output → Outcome → Impact con el horizonte de cada nivel; indicadores PERS entre paréntesis",
        figsize=(10, 6.6), xlim=(0, 100), ylim=(-3, 68))
    cols = [(1, 16, "INSUMOS\nEjecución", E.CAJA), (20, 33, "OUTPUTS (R y P)\nMeses 1 a 24", E.CLARO),
            (58, 19, "OUTCOMES (E)\nCorto plazo", E.MEDIO), (80, 19, "IMPACT (S)\nMeses 30 a 36", E.BLANCO)]
    for x, w, t, rel in cols:
        E.caja(ax, x, 56, w, 7, t, relleno=rel, fs=8.6, bold=True)
    ins = ["Presupuesto SGR\n" + M.mm(r["sgr"]) + "\nmillones de COP", "Contrapartida\n" + M.mm(r["contra"]) + "\nmillones de COP",
           "Equipo\n29 cargos\n624 persona-mes", "Plazo\n24 meses\n104 semanas"]
    for k, t in enumerate(ins):
        E.caja(ax, 1, 43.5 - k * 13, 16, 10.5, t, relleno=E.CAJA, fs=8.0)
    outs = ["Red de 100 nodos y\n10 gateways (R01, R03, P01)", "Modelo de corrección y software\nregistrado (R02, R05, P02)",
            "2 artículos Q1 o Q2 (P03)", "29 actividades de\napropiación social (P04)", "Control de la ejecución\n(R04, R06)"]
    for k, t in enumerate(outs):
        E.caja(ax, 20, 46.5 - k * 10.8, 33, 8.4, t, relleno=E.CLARO, fs=8.0)
    oc = ["Uso institucional\ndel tablero y del\nprotocolo (E01)", "Reducción relativa de\nfalsas alarmas (E02)", "Capacidad instalada\nen custodios (E03)"]
    for k, t in enumerate(oc):
        E.caja(ax, 58, 44 - k * 14, 19, 11, t, relleno=E.MEDIO, fs=8.0)
    im = ["Activación del protocolo\nante superación de\numbral (S01)", "Continuidad de la red\nbajo custodia (S02)"]
    for k, t in enumerate(im):
        E.caja(ax, 80, 44 - k * 14, 19, 11, t, relleno=E.BLANCO, fs=8.0)
    E.flecha(ax, (17.8, 36), (19.3, 36), lw=1.6)
    E.flecha(ax, (54.0, 36), (57.3, 36), lw=1.6)
    E.flecha(ax, (77.8, 36), (79.3, 36), lw=1.6)
    ax.plot([55.5, 55.5], [6, 64.5], color=E.TINTA, lw=1.6, ls=(0, (6, 4)))
    ax.text(55.5, 66.2, "Techo de rendición de cuentas", ha="center", fontsize=8.6, fontweight="bold", color=E.TINTA)
    ax.text(30, -1.2, "Bajo el techo: metas comprometidas", ha="center", fontsize=8.4, color=E.TINTA)
    ax.text(79, -1.2, "Sobre el techo: metas de contribución", ha="center", fontsize=8.4, color=E.TINTA)
    ax.text(89.5, 17.0, "Cambio en salud:\nsin medición (VACIO)", ha="center", fontsize=8.0, color=E.TINTA, style="italic")
    E.guardar(fig, "cF7_f00")

if __name__ == "__main__":
    f00()
    print("ok")
