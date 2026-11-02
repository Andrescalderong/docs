# -*- coding: utf-8 -*-
"""Tablas y valores del documento 1000X-05 (modelo de negocio de valor público). Cifras de maestro.py vía cX_comun.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
from cX6_datos import tabla
mm, pct = C.mm, C.pct
V = {}; T = {}
c, f = C.por_clase(); cu = C.costos_unitarios()
V["total"] = mm(C.TOTAL); V["sgr"] = mm(C.SGR); V["contra"] = mm(C.CONTRA)
V["fijos"] = pct(f["Fijo"] / C.SGR); V["variables"] = pct(f["Variable"] / C.SGR)
V["marg"] = mm(cu["marginal"]); V["medio"] = mm(cu["tot_nodo"]); V["pct_marg"] = pct(cu["marginal"] / cu["tot_nodo"])
V["holgura"] = mm(C.TOPE - C.SGR)
filas = [
    ["1. Segmentos de clientes", "Primarios: 15 comités de gestión del riesgo (12 municipales y 3 departamentales) y 150 funcionarios beneficiarios. Secundarios: operarios de remoción, población expuesta, autoridades ambientales y la Unidad Nacional para la Gestión del Riesgo de Desastres (UNGRD)", "Ficha §4", "SUPUESTO; operarios [DATO_USUARIO]"],
    ["2. Propuesta de valor", "Mediciones de PM2,5 y PM10 con error conocido frente a una referencia (coeficiente de determinación R² ≥ 0,70 y error cuadrático medio normalizado NRMSE ≤ 30 %) para decidir alertas. Sin promesa de efectos en salud", "Ficha §2 y §3", "PROPUESTO"],
    ["3. Canales", "Tablero del índice de calidad del aire y salud (AQHI) y protocolo de alerta; 5.000 cartillas impresas; talleres y jornadas; convenios por tramo", "Presupuesto M04; PERS-P04", "DECLARADO (cartillas); PROPUESTO"],
    ["4. Relaciones con clientes", "Asistencia y co-diseño con los comités; participación comunitaria; formación de custodios con meta de 60 personas certificadas", "PERS-P04 y PERS-E03", "PROPUESTO"],
    ["5. Fuentes de ingresos", f"Durante el proyecto: SGR de {V['sgr']} y contrapartida de {V['contra']} millones. Después: custodia y financiación de custodios, con monto VACIO", "Ficha §5", "CALCULADO; VACIO"],
    ["6. Recursos clave", "14 líneas de personal; 100 nodos, 10 gateways y 3 referencias; modelo de corrección y datos de colocalización; recursos financieros", "Ficha §2 y §5", "PROPUESTO"],
    ["7. Actividades clave", "I+D+i: colocalización y modelo. Desarrollo: firmware, plataforma y gemelo digital. Transferencia: formación y convenios de custodia", "Cronograma WP1 a WP3", "PROPUESTO"],
    ["8. Alianzas clave", "Co-ejecutores: institución de educación superior (IES) y empresa tecnológica. Proveedores: laboratorios, equipos y nube. Aliados de transferencia: comités, UNGRD, alcaldías y custodios", "Ficha §1 y §4", "SUPUESTO; nombres [DATO_USUARIO]"],
    ["9. Estructura de costos", f"Total de {V['total']} millones; costos fijos de {V['fijos']} % y variables de {V['variables']} % del SGR; costo marginal de un nodo de {V['marg']} millones", "Documento 1000X-06", "CALCULADO"],
]
T["t01"] = tabla("t01", "Descripción de los nueve bloques del lienzo de modelo de negocio",
                 ["Bloque", "Contenido", "Fuente", "Naturaleza"], filas,
                 "*Nota.* Elaboración propia con datos de la ficha maestra y de maestro.py. Los nombres de entidades y el número de operarios corresponden al usuario [DATO_USUARIO]. Decimales con coma.")
filas = [
    ["Ejecución (meses 1 a 24)", "SGR", mm(C.SGR), "Las compuertas C1 y C2 liberan las compras de los tramos 2 y 3", "CALCULADO"],
    ["Ejecución (meses 1 a 24)", "IES (especie)", "1.100,0", "Certificación pendiente", "DECLARADO; desglose PROPUESTO"],
    ["Ejecución (meses 1 a 24)", "Empresa tecnológica (efectivo)", "210,0", "Certificación pendiente", "DECLARADO"],
    ["Ejecución (meses 1 a 24)", "Empresa tecnológica (especie)", "800,0", "Infraestructura en la nube de la empresa", "DECLARADO"],
    ["Ejecución (meses 1 a 24)", "Alcaldías", "0,0", "Sin aporte", "VACIO"],
    ["Posproyecto (meses 25 a 36)", "Custodios y entidades territoriales", "[DATO_USUARIO: monto anual de custodia]", "Convenios con partida y cláusula de apertura", "VACIO"],
    ["Ampliación (años 4 y 5)", "Opciones condicionadas a términos de referencia (TdR)", "No presupuestado", f"Holgura de {V['holgura']} millones no solicitada", "PROPUESTO"],
]
T["t02"] = tabla("t02", "Financiación del modelo por fase, en millones de COP",
                 ["Fase", "Fuente", "Monto", "Condición", "Naturaleza"], filas,
                 "*Nota.* Elaboración propia con datos de la ficha maestra (§5) y de maestro.py. No se presupuestan ingresos por ventas ni licencias. El costo de sostenimiento posproyecto es NO_CALCULABLE con los datos actuales.")
