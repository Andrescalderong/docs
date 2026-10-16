# -*- coding: utf-8 -*-
"""Figuras del capítulo 5 (prefijo 5): F5.1 diagrama CARS, F5.2 cadena de valor, F5.3 mapa de alianzas con roles.
Datos: FICHA_MAESTRA (§3 objetivos, §4 tramos, §5 presupuesto y contrapartida, §8 indicadores PERS) y cifras de F-INF con página
(DECLARADO, NO_VERIFICADO). Alianza y territorio: SUPUESTO; nombres de entidades: [DATO_USUARIO]. No se inventa ningún valor.
Ejecución: python3 c5_figs.py   (genera figs/out/c5_f01, c5_f02 y c5_f03 en .png y .svg)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import estilo as E

TINTA, AZUL, MEDIO, CLARO, GRIS = E.TINTA, E.AZUL, E.MEDIO, E.CLARO, E.GRIS


def caja_texto(ax, cx, cy, w, h, lineas, relleno, bold=False, grosor=1.2, fs=9, dashed=False):
    p = E.caja(ax, cx - w / 2, cy - h / 2, w, h, "\n".join(lineas), relleno=relleno, fs=fs, bold=bold, grosor=grosor)
    if dashed:
        p.set_linestyle((0, (4, 2)))
    return p


def lienzo(h1, h2, figsize=(10, 7), ylim=(0, 72)):
    fig, ax = E.lienzo_libre(h1=h1, h2=h2, figsize=figsize, xlim=(0, 100), ylim=ylim)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.86, bottom=0.01)
    return fig, ax


def f01():
    fig, ax = lienzo(
        "El proyecto ocupa el nicho de la medición con error conocido y del uso verificado",
        "Modelo CARS de Swales (1990, 2004) aplicado al proyecto. Cifras de F-INF con página:\nDECLARADO y NO_VERIFICADO; cifras del proyecto: PROPUESTO")
    cols = [
        ("Movida 1: establecer el territorio", CLARO, False,
         ["La vigilancia de PM2,5 y PM10", "sostiene decisiones de riesgo", "", "209 estaciones reportadas en el país;", "154 integran un sistema de vigilancia", "", "28 de 1.122 municipios cuentan", "con estaciones utilizables", "para estimar la carga"]),
        ("Movida 2: crear el nicho", MEDIO, False,
         ["Vacíos que la literatura no cierra", "", "90,8 % de las estaciones propuestas", "serían sensores sin plan de calibración", "", "Cero de cinco documentos de alerta", "reporta falsas alarmas", "", "9,4 % de los estudios de AQHI valida", "con partición de datos"]),
        ("Movida 3: ocupar el nicho", AZUL, True,
         ["Respuesta del proyecto", "", "Colocalización con tres referencias", "y corrección en el gateway", "", "100 nodos y 10 gateways por tramos", "con compuertas C1 y C2", "", "Umbrales R² ≥ 0,70 y NRMSE ≤ 30 %;", "uso institucional ≥ 75 % al mes 24"]),
    ]
    xs = [16, 50, 84]
    for (titulo, col, grueso, lineas), x in zip(cols, xs):
        E.caja(ax, x - 13, 14, 26, 44, "", relleno=col, grosor=2.2 if grueso else 1.3)
        ax.text(x, 55, titulo, ha="center", va="center", fontsize=9.6, fontweight="bold", color=TINTA)
        for i, t in enumerate(lineas):
            ax.text(x, 50.2 - i * 3.4, t, ha="center", va="center", fontsize=8.1, color=TINTA,
                    fontweight="bold" if i == 0 else "normal")
    E.flecha(ax, (29.8, 36), (36.2, 36), lw=2.0)
    E.flecha(ax, (63.8, 36), (70.2, 36), lw=2.0)
    ax.text(33, 39.3, "Brecha", fontsize=8.4, color=TINTA, ha="center")
    ax.text(67, 39.3, "Aporte", fontsize=8.4, color=TINTA, ha="center")
    ax.text(50, 8.5, "Estructura argumentativa: el territorio valida la importancia del campo, el nicho declara lo que falta\ny la ocupación presenta el proyecto como respuesta con condiciones de verificación.",
            ha="center", va="center", fontsize=8.8, color=TINTA, linespacing=1.3)
    ax.text(50, 2.0, "Territorio y alianza: SUPUESTO por instrucción del usuario. Fuentes: F-INF (secciones 1.3, 3.1 y 5.4) y ficha maestra.",
            ha="center", va="center", fontsize=8.2, color=TINTA)
    E.guardar(fig, "c5_f01")


def f02():
    fig, ax = lienzo(
        "Salidas durante la ejecución, efectos al mes 24 e impactos tras el cierre",
        "Cadena de valor del proyecto con los 15 indicadores PERS (ficha maestra, sección 8).\nValores monetarios en millones de pesos colombianos (COP)")
    cols = [
        ("Insumos", GRIS, False, ["SGR: COP 8.729,8 millones", "Contrapartida: COP 2.110", "millones (DECLARADO;", "desglose IES PROPUESTO)", "Duración: 24 meses", "(104 semanas)"]),
        ("Actividades", CLARO, False, ["WP1: medición verificada", "(OE1)", "WP2: red, energía y", "plataforma (OE2)", "WP3: uso institucional", "y custodia (OE3)", "WP0: gestión y", "compuertas"]),
        ("Outputs", MEDIO, False, ["PERS-P01: 100 nodos y", "10 gateways operativos", "PERS-P02: software y", "gemelo digital registrado", "PERS-P03: 2 artículos", "sometidos", "PERS-P04: 29 actividades", "de apropiación social"]),
        ("Outcomes", AZUL, False, ["PERS-E01: uso del tablero", "en al menos 75 % de los", "comités al mes 24", "PERS-E02: reducción", "relativa de falsas alarmas", "de al menos 30 %", "PERS-E03: 60 personas", "certificadas"]),
        ("Impact", AZUL, True, ["PERS-S01: activación del", "protocolo en al menos", "80 % de las superaciones", "PERS-S02: continuidad de", "la red en al menos 70 %", "", "Medidos a los 12 meses", "posteriores al cierre"]),
    ]
    w = 16.4
    xs = [9.2, 29.6, 50, 70.4, 90.8]
    for (titulo, col, dash, lineas), x in zip(cols, xs):
        p = E.caja(ax, x - w / 2, 22, w, 40, "", relleno=col, grosor=1.3)
        if dash:
            p.set_linestyle((0, (4, 2)))
        ax.text(x, 58.5, titulo, ha="center", va="center", fontsize=10.2, fontweight="bold", color=TINTA)
        for i, t in enumerate(lineas):
            ax.text(x, 53.2 - i * 3.9, t, ha="center", va="center", fontsize=7.6, color=TINTA)
    for a, b in zip(xs[:-1], xs[1:]):
        E.flecha(ax, (a + w / 2 + 0.3, 42), (b - w / 2 - 0.3, 42), lw=1.6)
    # Bandas de horizonte
    ax.text(40, 16.5, "Producción durante la ejecución (meses 1 a 24)", ha="center", fontsize=8.8, fontweight="bold", color=TINTA)
    ax.plot([1, 59], [19.5, 19.5], color=TINTA, lw=1.2)
    ax.text(70.4, 16.5, "Uso al mes 24", ha="center", fontsize=8.8, fontweight="bold", color=TINTA)
    ax.plot([61.2, 80.4], [19.5, 19.5], color=TINTA, lw=1.2)
    ax.text(90.8, 16.5, "Tras el cierre", ha="center", fontsize=8.8, fontweight="bold", color=TINTA)
    ax.plot([82.6, 99], [19.5, 19.5], color=TINTA, lw=1.2, ls="--")
    ax.text(50, 8.5, "Los outputs no son impactos. El impacto es el cambio sostenido y se mide entre seis y 12 meses después del cierre con evaluación externa.",
            ha="center", va="center", fontsize=8.4, color=TINTA)
    ax.text(50, 3.6, "Líneas base de PERS-E01, PERS-E02, PERS-S01 y PERS-S02: VACIO; se miden en el tramo 1. El proyecto no promete efectos en salud.",
            ha="center", va="center", fontsize=8.4, color=TINTA)
    E.guardar(fig, "c5_f02")


def f03():
    fig, ax = lienzo(
        "La alianza supuesta asigna roles verificables y deja sin nombre a las entidades",
        "Mapa de alianzas con roles y aportes. Alianza y territorio: SUPUESTO por instrucción del usuario;\nnombres de entidades: [DATO_USUARIO]. Valores en millones de pesos colombianos (COP)")
    caja_texto(ax, 50, 62, 36, 8.5, ["Financiador: SGR y MinCiencias", "Valor solicitado: COP 8.729,8 millones"], GRIS, fs=8.6)
    caja_texto(ax, 86, 62, 27, 8.5, ["UNGRD (SUPUESTO)", "Articulación nacional del protocolo"], GRIS, fs=8.2, dashed=True)
    caja_texto(ax, 50, 39, 30, 15, ["Entidad ejecutora", "IES con acreditación de alta calidad", "[DATO_USUARIO: nombre]", "Coordina, mide y custodia los datos"], AZUL, bold=True, grosor=2.2, fs=8.6)
    caja_texto(ax, 13, 39, 25, 15, ["Empresa tecnológica", "[DATO_USUARIO: nombre]", "Plataforma, nube y desarrollo IoT", "Contrapartida: 210 en efectivo", "y 800 en especie (DECLARADO)"], MEDIO, fs=8.0)
    caja_texto(ax, 87, 39, 25, 15, ["Alcaldías focalizadas", "[DATO_USUARIO: nombres]", "Custodia por tramo y uso", "Aporte: sin aporte (VACIO)"], MEDIO, fs=8.2, dashed=True)
    caja_texto(ax, 24, 11.5, 42, 14, ["Verificación independiente", "Laboratorio acreditado de gravimetría,", "laboratorio externo de ensayo, evaluador", "externo y auditoría de ciberseguridad", "[DATO_USUARIO: nombres]"], CLARO, fs=8.0)
    caja_texto(ax, 74, 11.5, 42, 14, ["Comités de gestión del riesgo", "12 municipales y tres departamentales", "Usuarios del tablero y del protocolo", "(SUPUESTO)"], CLARO, fs=8.2, dashed=True)
    E.flecha(ax, (50, 57.6), (50, 46.7), lw=1.5)
    ax.text(51.2, 52, "financia", fontsize=8.2, color=TINTA, va="center")
    E.flecha(ax, (76, 57.6), (60, 46.7), lw=1.3, ls="--")
    ax.text(77, 50.5, "articula", fontsize=8.2, color=TINTA, ha="center")
    E.flecha(ax, (26, 40.5), (34.4, 40.5), lw=1.5)
    E.flecha(ax, (34.4, 37.5), (26, 37.5), lw=1.5)
    ax.text(30.2, 43.2, "convenio", fontsize=8.0, color=TINTA, ha="center")
    E.flecha(ax, (65.6, 40.5), (74, 40.5), lw=1.3, ls="--")
    E.flecha(ax, (74, 37.5), (65.6, 37.5), lw=1.3, ls="--")
    ax.text(69.8, 43.2, "custodia", fontsize=8.0, color=TINTA, ha="center")
    E.flecha(ax, (40, 31.4), (30, 18.7), lw=1.4)
    ax.text(31.5, 26, "contrata", fontsize=8.2, color=TINTA, ha="center")
    E.flecha(ax, (58, 31.4), (68, 18.7), lw=1.4)
    ax.text(68.6, 26, "co-diseña y forma", fontsize=8.2, color=TINTA, ha="center")
    E.flecha(ax, (87, 31.4), (82, 18.7), lw=1.2, ls="--")
    ax.text(87.5, 25.5, "integran", fontsize=8.2, color=TINTA, ha="left")
    ax.text(50, 2.0, "Línea continua: relación con soporte en la ficha maestra. Línea discontinua: relación SUPUESTO o aporte VACIO.",
            ha="center", va="center", fontsize=8.2, color=TINTA)
    E.guardar(fig, "c5_f03")


if __name__ == "__main__":
    f01(); f02(); f03()
    print("c5_f01, c5_f02, c5_f03 generadas")
