# -*- coding: utf-8 -*-
"""Datos del documento 1000X-08 (mapa de interesados): registro con roles genéricos, posiciones PROPUESTAS de poder e interés,
tablas (T) y valores de prosa (V). Los nombres son [DATO_USUARIO]; las posiciones son PROPUESTAS (escala de 1 a 10)."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cX_comun as C
from cX6_datos import tabla
mm, pct, num = C.mm, C.pct, C.num

# id, grupo, rol genérico, nombre, aporte o expectativa principal, poder, interés, nombre corto (figura)
S = [
 ("S01", "Interno", "Entidad ejecutora (IES con acreditación de alta calidad)", "[DATO_USUARIO: nombre de la IES ejecutora]", "Ejecuta, aporta 1.100 millones en especie y responde por los resultados", 8, 9, "IES ejecutora"),
 ("S02", "Interno", "Gerencia de proyecto", "[DATO_USUARIO: nombre de la persona gerente]", "Cumple plazos, presupuesto y compuertas", 7, 10, "Gerencia de proyecto"),
 ("S03", "Interno", "Equipo técnico (datos, metrología, IoT, firmware, software y análisis espacial)", "[DATO_USUARIO: nombres del equipo técnico]", "Valida el modelo de corrección y opera la red", 4, 9, "Equipo técnico"),
 ("S04", "Interno", "Equipo de apropiación social, calidad del aire y convenios", "[DATO_USUARIO: nombres del equipo]", "Co-diseña con los comités y negocia los convenios", 3, 8, "Apropiación y convenios"),
 ("S05", "Externo primario", "Empresa tecnológica aliada", "[DATO_USUARIO: nombre de la empresa]", "Aporta 210 millones en efectivo y 800 millones en especie", 7, 8, "Empresa aliada"),
 ("S06", "Externo primario", "Financiador", "SGR y MinCiencias", "Recibe resultados verificables y ejecución presupuestal", 10, 7, "Financiador"),
 ("S07", "Externo primario", "Comités municipales de gestión del riesgo (12)", "[DATO_USUARIO: lista de municipios]", "Usan el tablero en decisiones documentadas", 6, 8, "Comités municipales"),
 ("S08", "Externo primario", "Comités departamentales de gestión del riesgo (3)", "[DATO_USUARIO: nombres de los comités]", "Coordinan la respuesta departamental", 7, 7, "Comités departamentales"),
 ("S09", "Externo primario", "Unidad Nacional para la Gestión del Riesgo de Desastres (UNGRD)", "[DATO_USUARIO: dependencia y contacto]", "Articula el protocolo con el sistema nacional", 8, 6, "UNGRD"),
 ("S10", "Externo primario", "Alcaldías de los municipios focalizados", "[DATO_USUARIO: nombres de las alcaldías]", "Deciden las partidas de custodia y no aportan contrapartida (VACIO)", 8, 4, "Alcaldías"),
 ("S11", "Externo primario", "Custodios designados por tramo", "[DATO_USUARIO: entidades custodias]", "Operan la red después del cierre", 6, 9, "Custodios"),
 ("S12", "Externo primario", "Operarios de remoción en sitios monitoreados", "[DATO_USUARIO: número y organizaciones]", "Reciben mediciones para proteger su trabajo", 2, 9, "Operarios de remoción"),
 ("S13", "Externo primario", "Población expuesta en los municipios focalizados", "No aplica (grupo)", "Recibe información comprensible del índice", 2, 6, "Población expuesta"),
 ("S14", "Externo secundario", "Autoridades ambientales y red nacional de calidad del aire", "[DATO_USUARIO: entidades]", "Verifican datos y normas aplicables", 7, 3, "Autoridades ambientales"),
 ("S15", "Externo secundario", "Laboratorio acreditado y laboratorio externo", "[DATO_USUARIO: laboratorios]", "Prestan análisis gravimétrico y ensayo de desempeño", 3, 3, "Laboratorios"),
 ("S16", "Externo secundario", "Proveedores de equipos y de nube", "[DATO_USUARIO: proveedores]", "Entregan en plazo según los lotes por tramo", 3, 2, "Proveedores"),
 ("S17", "Externo secundario", "Comunidad científica y medios de divulgación", "No aplica (grupo)", "Reciben artículos y piezas de divulgación", 2, 4, "Comunidad científica y medios"),
 ("S18", "Externo secundario", "Evaluación externa independiente", "[DATO_USUARIO: evaluador]", "Verifica los resultados en los meses 12 y 24", 6, 3, "Evaluación externa"),
]
UMBRAL = 6   # alto = 6 o más en la escala de 1 a 10

def cuadrante(p, i):
    if p >= UMBRAL and i >= UMBRAL: return "Gestionar de cerca"
    if p >= UMBRAL: return "Mantener satisfecho"
    if i >= UMBRAL: return "Mantener informado"
    return "Monitorear"

V = {}; T = {}
cu = collections.OrderedDict((k, []) for k in ("Gestionar de cerca", "Mantener satisfecho", "Mantener informado", "Monitorear"))
for s in S: cu[cuadrante(s[5], s[6])].append(s[0])
for k, key in zip(cu, ("n_cerca", "n_satisf", "n_inform", "n_monit")): V[key] = str(len(cu[k]))
V["n_total"] = str(len(S))
V["n_int"] = str(sum(1 for s in S if s[1] == "Interno")); V["n_prim"] = str(sum(1 for s in S if s[1] == "Externo primario")); V["n_sec"] = str(sum(1 for s in S if s[1] == "Externo secundario"))

# t01 registro
filas = [[s[0], s[1], s[2], s[3], s[4]] for s in S]
T["t01"] = tabla("t01", "Registro de interesados con roles genéricos y nombres pendientes",
                 ["Id", "Grupo", "Rol genérico", "Nombre", "Aporte o expectativa principal"], filas,
                 "*Nota.* Elaboración propia con datos de la ficha maestra. Los roles son genéricos y los nombres corresponden al usuario [DATO_USUARIO]. El territorio y la alianza son SUPUESTOS por instrucción del usuario. Cifras de contrapartida DECLARADAS en el expediente E3.")

# t02 cuadrantes
estrategia = {
    "Gestionar de cerca": "Decisiones conjuntas, reunión mensual y revisión en cada compuerta",
    "Mantener satisfecho": "Información breve y verificable; consulta antes de cada compuerta",
    "Mantener informado": "Participación en talleres, cartillas y jornadas; canales sencillos",
    "Monitorear": "Seguimiento por hito y comunicación por contrato o por publicación",
}
criterio = {"Gestionar de cerca": "Poder ≥ 6 e interés ≥ 6", "Mantener satisfecho": "Poder ≥ 6 e interés ≤ 5", "Mantener informado": "Poder ≤ 5 e interés ≥ 6", "Monitorear": "Poder ≤ 5 e interés ≤ 5"}
filas = []
for k, ids in cu.items():
    filas.append([k, criterio[k], str(len(ids)), ", ".join(ids), estrategia[k]])
T["t02"] = tabla("t02", "Clasificación de los interesados por cuadrante de poder e interés y estrategia asociada",
                 ["Cuadrante", "Criterio", "Número", "Interesados", "Estrategia"], filas,
                 "*Nota.* Elaboración propia. Las posiciones de poder e interés (escala de 1 a 10) son PROPUESTAS y requieren validación del equipo de proyecto y del financiador. Decimales con coma.")

# t03 plan de gestión
filas = [
    ["S06 Financiador", "Informes de seguimiento y actas de compuerta con evidencia", "Informe escrito y reunión de compuerta", "Mensual; en C1, C2 y C3", "Gerencia de proyecto"],
    ["S01 y S05 IES y empresa", "Decisiones de ejecución y verificación de la contrapartida", "Comité directivo", "Mensual", "Gerencia de proyecto"],
    ["S02, S03 y S04 Equipo", "Coordinación técnica, social y de convenios", "Reunión de equipo y tablero interno", "Semanal", "Gerencia de proyecto"],
    ["S07 y S08 Comités", "Co-diseño de umbrales, formación y registro de decisiones", "Talleres y sesiones del comité", "Trimestral; taller por tramo", "Coordinación de apropiación social"],
    ["S09 UNGRD", "Articulación del protocolo de alerta", "Reunión técnica y nota informativa", "Semestral; en C1 y C2", "Investigador principal"],
    ["S10 y S11 Alcaldías y custodios", "Convenios por tramo, partida y formación", "Mesas de convenio y capacitación", "Mensual en negociación; trimestral después", "Profesional de convenios y custodia"],
    ["S12 y S13 Operarios y población", "Cartillas, jornadas y explicación del índice", "Cartillas impresas y jornadas públicas", "Por jornada (9) y por tramo", "Profesionales de apropiación social"],
    ["S14 Autoridades ambientales", "Reporte técnico de desempeño y de referencias", "Informe técnico", "Semestral", "Profesional en calidad del aire y salud ambiental"],
    ["S15 y S16 Laboratorios y proveedores", "Cronograma de ensayos y de compras por lote", "Contrato y acta de entrega", "Compras en los meses 5, 13 y 18; ensayo en el mes 23", "Especialista en metrología y gerencia"],
    ["S17 Comunidad científica y medios", "Artículos y piezas de divulgación", "Revistas y boletines", "Semestral", "Investigador principal"],
    ["S18 Evaluación externa", "Acceso a datos y evidencias", "Sesión de evaluación", "Meses 12 y 24", "Gerencia de proyecto"],
]
T["t03"] = tabla("t03", "Plan de gestión de interesados con estrategia, canal, frecuencia y responsable",
                 ["Interesados", "Estrategia de comunicación", "Canal", "Frecuencia", "Responsable de la relación (rol)"], filas,
                 "*Nota.* Elaboración propia. Las frecuencias son PROPUESTAS. Los responsables son roles del presupuesto de la ficha maestra; los nombres son [DATO_USUARIO: nombres del personal responsable]. Meses de compra y ensayo según el cronograma de la ficha.")

if __name__ == "__main__":
    for k in sorted(V): print(k, V[k])
    print({k: v for k, v in cu.items()})
    for k in sorted(T): print(); print(T[k])
