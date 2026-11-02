# -*- coding: utf-8 -*-
"""Paso 6: alternativas y evaluación multicriterio (suma ponderada, escala ordinal de desempeño 1 a 9).
Pesos por defecto del metaprompt (sin términos de referencia; VACIO). Puntajes PROPUESTOS por la instancia analítica."""
import itertools

ALTS = [
 ("ALT-00", "Statu quo: sensores aislados sin calibración dinámica"),
 ("ALT-01", "Estaciones fijas de referencia en los sitios de remoción"),
 ("ALT-02", "Red de sensores con calibración centralizada en la nube"),
 ("ALT-03", "Red híbrida con corrección en gateway, despliegue por tramos y custodia distribuida (contrainductiva)"),
]
# criterio, peso (%), puntajes ALT-00..ALT-03, justificación breve (≤ 20 palabras)
CRIT = [
 ("Viabilidad técnica", 12.0, [9, 7, 5, 6], "ALT-00 no exige desarrollo; ALT-01 es madura pero logística; ALT-02 depende del enlace; ALT-03 parte de TRL 4."),
 ("Viabilidad financiera", 12.0, [9, 3, 6, 6], "ALT-01 exige equipos de referencia por sitio; ALT-02 y ALT-03 usan sensores de bajo costo."),
 ("Impacto esperado", 15.0, [1, 5, 5, 7], "ALT-03 corrige el sesgo en el origen y permite verificar el uso institucional."),
 ("Articulación con PDD y demandas territoriales", 10.0, [1, 5, 5, 5], "Sin PDD ni anexo de demandas aportados, la articulación es genérica (NO_VERIFICADO)."),
 ("Respuesta a prioridades del territorio", 8.0, [1, 4, 5, 5], "Sin evidencia documental de priorización local; se asigna alineación parcial."),
 ("Sostenibilidad", 8.0, [1, 3, 4, 5], "Custodia por tramos mejora la continuidad; no hay compromisos firmados."),
 ("Tiempo de implementación", 8.0, [9, 3, 6, 5], "ALT-01 exige obra y compra masiva; ALT-03 requiere piloto antes de ampliar."),
 ("Nivel de riesgo (mayor puntaje, menor riesgo)", 8.0, [9, 6, 4, 4], "ALT-02 y ALT-03 concentran riesgo en humedad y enlace; el piloto lo acota."),
 ("Escalabilidad", 5.0, [1, 2, 7, 7], "Costo marginal bajo por nodo adicional en ALT-02 y ALT-03."),
 ("Nivel de innovación", 4.0, [1, 2, 4, 8], "ALT-03 combina corrección en el borde, tramos condicionados y custodia distribuida."),
 ("PAFU: práctica", 2.5, [5, 4, 6, 6], "Operación sencilla para los comités."),
 ("PAFU: accesible", 2.5, [5, 3, 6, 6], "Costo por nodo accesible para municipios."),
 ("PAFU: fiable", 2.5, [3, 8, 4, 6], "Las estaciones de referencia son más fiables que los sensores corregidos."),
 ("PAFU: ubicua", 2.5, [2, 2, 6, 7], "Mayor cobertura espacial con ALT-02 y ALT-03."),
]
assert abs(sum(c[1] for c in CRIT) - 100.0) < 1e-9

def totales(pesos=None):
    w = pesos or [c[1] for c in CRIT]
    s = sum(w)
    return [sum(w[k] / s * CRIT[k][2][a] for k in range(len(CRIT))) for a in range(4)]

BASE = totales()

def escenario(nombre, idxs, rel=0.10):
    w = [c[1] for c in CRIT]
    for i in idxs: w[i] = w[i] * (1 + rel)
    s = sum(w)
    wn = [x / s for x in w]
    return nombre, wn, totales(w)

ESCENARIOS = [
    escenario("Prioridad técnica (viabilidad técnica +10 %)", [0]),
    escenario("Prioridad financiera (viabilidad financiera +10 %)", [1]),
    escenario("Prioridad de impacto (impacto esperado +10 %)", [2]),
    escenario("Prioridad de innovación (nivel de innovación +10 %)", [9]),
    escenario("Prioridad territorial (criterios territoriales +10 %)", [3, 4]),
]

def ganadora(t): return max(range(4), key=lambda i: t[i])

if __name__ == "__main__":
    print("Base:", [round(x, 3) for x in BASE], "ganadora", ALTS[ganadora(BASE)][0])
    for n, wn, t in ESCENARIOS:
        print(n, [round(x, 3) for x in t], ALTS[ganadora(t)][0], "Σw=", round(sum(wn), 6))
    # criterio de activación de GWO: espacio de decisión
    print("Espacio enumerable:", len(ALTS), "alternativas")
