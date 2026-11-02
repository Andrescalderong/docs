# -*- coding: utf-8 -*-
"""Figura cX5_f01: lienzo del modelo de negocio (nueve bloques) de valor público. Cifras de la ficha maestra (maestro.py). Determinista."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
import estilo as E
from matplotlib.patches import Rectangle

def bloque(ax, x, y, w, h, titulo, lineas, relleno=E.CAJA, fs=8.8):
    ax.add_patch(Rectangle((x, y), w, h, fc=relleno, ec=E.TINTA, lw=1.1))
    ax.add_patch(Rectangle((x, y + h - 3.6), w, 3.6, fc=E.MEDIO, ec=E.TINTA, lw=1.1))
    ax.text(x + 0.8, y + h - 1.8, titulo, ha="left", va="center", fontsize=9.6, fontweight="bold", color=E.TINTA)
    ax.text(x + 0.8, y + h - 4.7, "\n".join(lineas), ha="left", va="top", fontsize=fs, color=E.TINTA, linespacing=1.28)

def main():
    I = C.M.IDENT
    fig, ax = C.lienzo_libre2(h1="Modelo de valor público: la financiación cubre la ejecución y la custodia sostiene la red",
                             h2="Lienzo de nueve bloques; sin ingresos por ventas; cifras de la ficha maestra y nombres pendientes [DATO_USUARIO]", figsize=(10, 7), xlim=(0, 100), ylim=(0, 70))
    y_top = 24.5; h_top = 42.5; xs = [0.5, 20.3, 40.1, 59.9, 79.7]; w = 19.4
    bloque(ax, xs[0], y_top, w, h_top, "8. Alianzas clave", [
        "Co-ejecutores", "IES ejecutora y empresa", "tecnológica [DATO_USUARIO]", "",
        "Proveedores", "Laboratorio acreditado", "Laboratorio externo", "Equipos y nube", "", "Aliados de transferencia",
        "Comités de gestión", "del riesgo, UNGRD,", "alcaldías y custodios", "[DATO_USUARIO]"])
    bloque(ax, xs[1], y_top + h_top / 2, w, h_top / 2, "7. Actividades clave", [
        "I+D+i: colocalización y", "modelo de corrección", "Desarrollo: firmware,", "plataforma y gemelo digital", "Transferencia: formación", "y convenios de custodia"])
    bloque(ax, xs[1], y_top, w, h_top / 2, "6. Recursos clave", [
        "Personal: 14 líneas", "100 nodos, 10 gateways", "y 3 referencias", "Modelo y datos de", "colocalización",
        "Financieros: SGR y", "contrapartida"])
    bloque(ax, xs[2], y_top, w, h_top, "2. Propuesta de valor", [
        "Problema: lecturas de", "PM2,5 y PM10 sin error", "conocido en los sitios", "de remoción", "",
        "Beneficio: mediciones", "verificadas frente a", "referencia (R² ≥ 0,70 y", "NRMSE ≤ 30 %) para", "decidir alertas", "",
        "Diferenciador: corrección", "en gateway, tramos con", "compuertas y custodia", "distribuida", "",
        "Sin promesa de efectos", "en salud"], relleno=E.CLARO)
    bloque(ax, xs[3], y_top + h_top / 2, w, h_top / 2, "4. Relaciones", [
        "Asistencia y co-diseño", "con los comités", "Comunidad: 20 talleres", "y 9 jornadas", "Formación de custodios:", "60 personas certificadas"])
    bloque(ax, xs[3], y_top, w, h_top / 2, "3. Canales", [
        "Comunicación: cartillas", "(5.000) y jornadas", "Acceso: tablero del", "índice y protocolo de", "alerta", "Entrega: actas y", "convenios por tramo"])
    bloque(ax, xs[4], y_top, w, h_top, "1. Segmentos", [
        "Primarios", "15 comités de gestión del", "riesgo (12 municipales y", "3 departamentales)", "150 funcionarios", "beneficiarios (SUPUESTO)", "",
        "Secundarios", "Operarios de remoción y", "población expuesta en", "12 municipios", "[DATO_USUARIO]", "",
        "Autoridades ambientales", "y UNGRD"])
    h_bot = 22.0
    bloque(ax, 0.5, 1.0, 49.2, h_bot, "9. Estructura de costos", [
        f"Total del proyecto: {C.mm(C.TOTAL, 1)} millones de COP",
        f"Fijos {C.pct(C.por_clase()[1]['Fijo'] / C.SGR)} % del SGR (personal y plataforma)",
        f"Variables {C.pct(C.por_clase()[1]['Variable'] / C.SGR)} % (nodos, gateways y sitios)",
        f"Nodo adicional: {C.mm(C.costos_unitarios()['marginal'], 1)} millones (PROPUESTO)",
        "Economías de escala: el costo por nodo baja",
        "si el personal absorbe una ampliación"], fs=9.4)
    bloque(ax, 50.5, 1.0, 49.0, h_bot, "5. Fuentes de ingresos y financiación", [
        f"Durante el proyecto: SGR {C.mm(C.SGR, 1)} y",
        f"contrapartida {C.mm(C.CONTRA, 1)} millones de COP",
        "Después: custodia y financiación de custodios",
        "por convenio; monto VACIO",
        "Comercialización: sin ingresos por ventas"], fs=9.4)
    E.guardar(fig, "cX5_f01")

if __name__ == "__main__":
    main(); print("figura cX5_f01 generada")
