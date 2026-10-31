# -*- coding: utf-8 -*-
"""Anexo A (análisis del problema público y de la estructura causal): tablas generadas desde los resultados del cálculo estructural.
Se importa desde expand.py. Lee los JSON de data_causal/ (fichas, resultados, análisis complementario, rutas, sensibilidad)
y verifica por recálculo la matriz de cada escenario, las clases por mediana y los ciclos antes de emitir las tablas."""
import os, re, json, statistics
import numpy as np

A2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.environ.get("CAUSAL_DATA") or os.path.join(A2, "data_causal")
def _j(n): return json.load(open(os.path.join(DATA, n), encoding="utf-8"))
R = _j("RESULTADOS.json"); F = _j("FICHAS_PARITARIAS.json"); AC = _j("ANALISIS_COMPLEMENTARIO.json"); RC = _j("RUTAS_Y_CICLOS.json"); SO = _j("SENSIBILIDAD_ORDINAL.json")

IDS = [v["id"] for v in R["variables"]]
NOM = {
 "V01": "Concentración de PM2,5", "V02": "Concentración de PM10", "V03": "Humedad relativa", "V04": "Velocidad del viento",
 "V05": "Volumen de escombros removidos", "V06": "Error de medición de los nodos", "V07": "Frecuencia de calibración", "V08": "Latencia de datos",
 "V09": "Disponibilidad de nodos", "V10": "Densidad del gemelo digital", "V11": "Índice local de calidad del aire", "V12": "Falsas alarmas",
 "V13": "Anticipación del aviso", "V14": "Personas alertadas", "V15": "Adopción institucional",
}
BLOQUE = {"FIS": "Físico", "TEC": "Técnico", "DEC": "Decisión"}
ESC = [("S0", "S0_HISTORICO_CONDICIONADO"), ("S1", "S1_PREVIO_DOC"), ("S2", "S_TRABAJO_PROPUESTO"), ("S3", "S3_ENVOLVENTE_ADMISIBLE_BAJA"), ("S4", "S4_ENVOLVENTE_ADMISIBLE_ALTA")]
ORIGEN = {
 "S0": "Matriz inicial del equipo formulador; los ceros se heredan sin adjudicar",
 "S1": "Matriz intermedia del equipo formulador, sin fichas completas",
 "S2": "Matriz de trabajo derivada de las 105 fichas bidireccionales",
 "S3": "Envolvente baja: mínimo admisible de cada vínculo",
 "S4": "Envolvente alta: máximo admisible de cada vínculo",
}
CLASE = {"ACTIVA": "Activa", "CRITICA": "Crítica", "REACTIVA": "Reactiva", "AUTONOMA_RELATIVA": "Autónoma relativa", "FRONTERA": "Frontera"}
ESTADO_MM = {"EXTINCION_DE_CAMINOS": "Se extingue en A⁷", "SIN_ESTABILIDAD_OBSERVADA_HASTA_KMAX": "Sin estabilidad hasta k = 10", "PERIODICIDAD_OBSERVADA": "Periodicidad observada"}

def num(x):
    if isinstance(x, float) and abs(x - round(x)) < 1e-9: x = int(round(x))
    if isinstance(x, float): return f"{x:.1f}".replace(".", ",")
    return f"{x:,}".replace(",", ".") if isinstance(x, int) and abs(x) >= 10000 else str(x)
def pc(x, d=1): return f"{x:.{d}f}".replace(".", ",") + " %"
def clase(c): return CLASE[c]
def esc_name(k): return dict(ESC)[k]
def S(k): return R["escenarios"][esc_name(k)]
def mat(k): return np.array(S(k)["matriz"], dtype=np.int64)

# ---------------------------------------------------------------- autoverificación por recálculo
def _clases_mediana(A):
    I = A.sum(1); D = A.sum(0); mi = statistics.median(I); md = statistics.median(D); out = []
    for i in range(15):
        if I[i] == mi or D[i] == md: out.append("FRONTERA")
        elif I[i] > mi and D[i] > md: out.append("CRITICA")
        elif I[i] > mi: out.append("ACTIVA")
        elif D[i] > md: out.append("REACTIVA")
        else: out.append("AUTONOMA_RELATIVA")
    return out
def _ciclos(A, maxlen=7):
    n = 15; adj = [[j for j in range(n) if A[i][j] > 0] for i in range(n)]; cyc = set()
    def dfs(st, cur, path, vis):
        for nx in adj[cur]:
            if nx == st and len(path) >= 2:
                r = path.index(min(path)); cyc.add(tuple(path[r:] + path[:r]))
            elif nx > st and nx not in vis and len(path) < maxlen: dfs(st, nx, path + [nx], vis | {nx})
    for st in range(n): dfs(st, st, [st], {st})
    return cyc
def autoverificar():
    for k, _ in ESC:
        A = mat(k); s = S(k)
        assert [x["clase_mediana"] for x in s["directa"]] == _clases_mediana(A), f"clases {k}"
        assert int(A.sum()) == s["total"], f"total {k}"
        assert (A.sum(1) == [x["influencia"] for x in s["directa"]]).all() and (A.sum(0) == [x["dependencia"] for x in s["directa"]]).all(), f"I y D {k}"
    A = mat("S2"); cy = _ciclos(A)
    assert len(cy) == 144 and sum(1 for c in cy if 14 in c) == 140, "ciclos S2"
    return True
autoverificar()
CICLOS_S2 = _ciclos(mat("S2"))

# ---------------------------------------------------------------- tablas
def t_variables():
    f = [(v["id"], NOM[v["id"]], v["definicion"].replace("PM2.5", "PM2,5"), BLOQUE[v["bloque"]]) for v in R["variables"]]
    return ("Variables del modelo estructural: identificador, definición operacional y bloque",
            ["ID", "Variable", "Definición operacional (unidad)", "Bloque"], f,
            "*Nota.* Elaboración propia con el diccionario de variables del equipo formulador. Las 15 variables no se amplían ni se retiran durante el análisis.")

def t_escenarios():
    f = []
    for k, _ in ESC:
        s = S(k); A = mat(k); n = int((A > 0).sum()); sin_ent = [IDS[j] for j in range(15) if A[:, j].sum() == 0]
        f.append((k, ORIGEN[k], str(n), pc(100 * n / 210), str(s["total"]), "Sí" if s["topologia"]["ciclos"] else "No", ", ".join(sin_ent), ESTADO_MM[s["micmac"]["estado"]]))
    return ("Escenarios de la matriz de influencia directa y sus propiedades estructurales",
            ["Escenario", "Origen de los valores", "Vínculos", "Densidad", "Suma de pesos", "Ciclos", "Variables sin entradas", "MICMAC"], f,
            "*Nota.* Elaboración propia. La densidad es la proporción de vínculos no nulos sobre 210 pares ordenados. La suma de pesos es igual para las filas y las columnas. S2 es el escenario de trabajo; S3 y S4 son envolventes de sensibilidad y no predicen.")

def t_matriz_s2():
    A = mat("S2"); f = []
    for i in range(15):
        f.append(tuple([IDS[i]] + [str(int(x)) for x in A[i]] + [f"**{int(A[i].sum())}**"]))
    f.append(tuple(["**TP**"] + [f"**{int(x)}**" for x in A.sum(0)] + [f"**{int(A.sum())}**"]))
    return ("Matriz de influencia directa del escenario de trabajo S2, con pesos de 0 a 3",
            ["Origen"] + IDS + ["TA"], f,
            "*Nota.* Elaboración propia con las 105 fichas bidireccionales. Cada celda es la influencia directa del origen (fila) sobre el destino (columna). TA es la suma de la fila (influencia total) y TP la suma de la columna (dependencia total). La escala es ordinal y no expresa proporciones ni probabilidades.")

def _r(x):
    x = float(x); t = num(x) if not x.is_integer() else str(int(x))
    return t.replace("-", "−")
def t_clases_s2():
    s = S("S2"); f = []
    for d in s["directa"]:
        f.append((d["id"], NOM[d["id"]], str(d["influencia"]), str(d["dependencia"]), _r(d["rango_influencia"]), _r(d["rango_dependencia"]), clase(d["clase_mediana"]), clase(d["clase_media"])))
    return ("Influencia, dependencia y clase de cada variable en el escenario de trabajo S2",
            ["ID", "Variable", "Influencia", "Dependencia", "Rango de influencia", "Rango de dependencia", "Clase por mediana", "Clase por media"], f,
            f"*Nota.* Elaboración propia. Los cortes por mediana son {s['mediana_I']} para la influencia y {s['mediana_D']} para la dependencia; la media de ambos ejes es {num(float(s['media']))}. Una variable que iguala un corte queda en la frontera. El rango 1 es el mayor valor y los empates promedian posiciones.")

def t_clases_5esc():
    f = []
    for i, v in enumerate(IDS):
        cl = [S(k)["directa"][i]["clase_mediana"] for k, _ in ESC]
        f.append((v, NOM[v]) + tuple(clase(c) for c in cl) + ("Sí" if len(set(cl)) == 1 else "No",))
    return ("Clase directa por mediana de cada variable en los cinco escenarios",
            ["ID", "Variable", "S0", "S1", "S2", "S3", "S4", "Estable"], f,
            "*Nota.* Elaboración propia. Una variable es estable si conserva la clase en los cinco escenarios. Solo lo son V05, V06 y V14. Las demás cambian al variar los juicios, de modo que su clase no es un rol firme.")

def t_micmac_s2():
    c = S("S2")["micmac"]["contraste"] if isinstance(S("S2")["micmac"].get("contraste"), list) else None
    f = []
    for d in c:
        f.append((d["id"], _r(d["rango_I_directo"]), _r(d["rango_I_indirecto"]), _r(d["ascenso_I"]), _r(d["rango_D_directo"]), _r(d["rango_D_indirecto"]), _r(d["ascenso_D"]), clase(d["clase_indirecta"])))
    return ("Rangos directos e indirectos (A¹⁰) de influencia y dependencia en el escenario S2",
            ["ID", "Rango I directo", "Rango I indirecto", "Ascenso I", "Rango D directo", "Rango D indirecto", "Ascenso D", "Clase indirecta"], f,
            "*Nota.* Elaboración propia. El ascenso es el rango directo menos el indirecto; un valor positivo indica que la variable gana posición al considerar recorridos largos. Los recorridos miden longitud de caminos y no tiempo ni efecto causal.")

def t_rangos_5esc():
    f = []
    for i, v in enumerate(IDS):
        row = [v, NOM[v]]
        for k, _ in ESC:
            row.append(_r(S(k)["micmac"]["contraste"][i]["rango_I_indirecto"]))
        f.append(tuple(row))
    return ("Rango de influencia indirecta de cada variable en los cinco escenarios",
            ["ID", "Variable", "S0 (A⁶)", "S1 (A¹⁰)", "S2 (A¹⁰)", "S3 (A¹⁰)", "S4 (A¹⁰)"], f,
            "*Nota.* Elaboración propia. En S0 solo V07 tiene influencia positiva en A⁶ y las demás empatan en 8,5, de modo que no hay ranking. El rango 1 es la mayor influencia indirecta.")

def t_oat():
    sel = [o for o in AC["oat"] if o["cambia_top3_influencia_indirecta"] or o["cambia_clase_indirecta"]]
    sel.sort(key=lambda o: (not o["cambia_top3_influencia_indirecta"], -o["max_desplazamiento_rango_directo"], o["origen"], o["destino"]))
    f = []
    for o in sel:
        cd = ", ".join(o["cambia_clase_directa"]) or "—"; ci = ", ".join(o["cambia_clase_indirecta"]) or "—"
        f.append((f"{o['origen']}→{o['destino']}", f"{o['valor_base']} → {o['valor_alterno']}", cd, ci, f"{_r(o['max_desplazamiento_rango_directo'])} / {_r(o['max_desplazamiento_rango_indirecto'])}", "Sí" if o["cambia_top3_influencia_indirecta"] else "No"))
    r = AC["oat_resumen"]
    return ("Vínculos cuyo cambio de un valor altera las tres primeras posiciones o la clase indirecta",
            ["Vínculo", "Valor base → alterno", "Cambia la clase directa de", "Cambia la clase indirecta de", "Desplazamiento máximo (directo / indirecto)", "Altera el top 3 indirecto"], f,
            f"*Nota.* Elaboración propia. Se evaluaron {r['perturbaciones']} cambios de un solo valor dentro del dominio admisible de cada vínculo incierto. De ellos, {r['con_cambio_de_clase_directa']} cambian la clase directa de alguna variable, {r['con_cambio_de_clase_indirecta']} cambian la clase indirecta y {r['con_cambio_top3']} alteran las tres primeras posiciones. No se asignan probabilidades a los cambios.")

def t_recodificacion():
    f = []
    cod = list(SO["S_TRABAJO_PROPUESTO"].keys())
    for i, v in enumerate(IDS):
        row = [v]
        for c in cod: row.append(clase(SO["S_TRABAJO_PROPUESTO"][c]["directa"][i]["clase_mediana"]))
        for c in cod:
            row.append(_r(SO["S_TRABAJO_PROPUESTO"][c]["contraste"][i]["rango_I_indirecto"]))
        f.append(tuple(row))
    enc = ["ID"] + [f"Clase {c}" for c in cod] + [f"Rango I {c}" for c in cod]
    return ("Clase directa y rango de influencia indirecta de S2 bajo tres codificaciones de la escala ordinal", enc, f,
            "*Nota.* Elaboración propia. La recodificación prueba la robustez de una escala ordinal y no aporta evidencia del territorio.")

def t_ciclos():
    n = len(CICLOS_S2); f = []
    for v in ("V15", "V10", "V06", "V09"):
        c = sum(1 for cy in CICLOS_S2 if IDS.index(v) in cy)
        f.append((v, NOM[v], str(c), pc(100 * c / n)))
    return (f"Participación de las variables más frecuentes en los {n} ciclos simples de S2",
            ["ID", "Variable", "Ciclos que la contienen", "Proporción de ciclos"], f,
            "*Nota.* Elaboración propia. Se cuentan los ciclos simples de hasta siete vínculos del escenario S2. Los ciclos de dos vínculos son V06↔V07, V09↔V15, V11↔V12 y V14↔V15.")

def t_rutas():
    f = []
    for par, rs in RC["rutas"].items():
        o, d = par.split("->"); best = rs[0] if isinstance(rs, list) else rs
        ruta = best["ruta"] if isinstance(best, dict) and "ruta" in best else best
        prod = best.get("producto_pesos") if isinstance(best, dict) else ""
        f.append((f"{o}→{d}", " → ".join(ruta) if isinstance(ruta, list) else str(ruta), str(prod)))
    return ("Ruta simple más intensa entre pares seleccionados de variables en S2",
            ["Origen→Destino", "Ruta de mayor producto de pesos", "Producto de pesos"], f,
            "*Nota.* Elaboración propia. El producto de pesos es un índice ordinal de intensidad y no un efecto estimado. Se consideran rutas de hasta cinco vínculos intermedios.")

_CITA_OK = {"Liao et al., 2026": "Liao et al., 2026", "Tavella et al., 2026": "Tavella et al., 2026", "Suresh et al., 2025": "Suresh et al., 2025",
            "Bang et al., 2026": "Bang et al., 2026", "Ruiz-Carrascal et al., 2026": "Ruiz-Carrascal et al., 2026", "Ayala-Parra et al., 2026": "Ayala-Parra et al., 2026"}
def _respaldo(d):
    ids = {x["id"] for x in d["fuentes"]}; txt = " ".join(x["localizador"] + " " + x.get("alcance", "") for x in d["fuentes"]); cit = []
    if "F-INF" in ids: cit.append("Equipo formulador, 2026")
    for m in re.finditer(r"([A-ZÁÉÍÓÚ][\w\-áéíóúñ]+(?: et al\.)?),? \(?(\d{4})", txt):
        c = f"{m.group(1)}, {m.group(2)}"
        if c in _CITA_OK and _CITA_OK[c] not in cit: cit.append(_CITA_OK[c])
    return ("(" + "; ".join(cit) + ")") if cit else "Razonamiento del equipo formulador"
def aristas():
    out = []
    for fi in F:
        for d in fi["direcciones"]:
            if d["valor_propuesto"] > 0: out.append(d)
    out.sort(key=lambda d: (d["origen"], d["destino"]))
    return out
SIGNO = {"+": "+", "-": "−", "MIXTO": "Mixto", "NO_IDENTIFICADO": "Sin definir"}
def _limpiar(t):
    """Quita referencias internas de las fichas (códigos de artefactos y de pasos) y normaliza las flechas."""
    t = re.sub(r"\s*\(P\d{2}\)", "", t)
    t = re.sub(r"\s*\(E3-P\d+[^)]*\)", "", t)
    t = t.replace("->", "→")
    t = re.sub(r"\s*\(VACIO V-DIC-0\d\)", " (definición por aclarar)", t)
    t = re.sub(r"\s*\(VACIO V-LLUVIA-01\)", " (variable no incluida en el modelo)", t)
    t = re.sub(r"\s*\(VACIO V-VIENTO-01\)", " (umbral operativo por definir)", t)
    t = re.sub(r"\s*\(Tabla \d+\.\d+\)", "", t)
    t = t.replace("El diccionario E3-P01", "El diccionario")
    t = t.replace("del expediente", "de la formulación").replace("en el expediente", "en la formulación").replace("El expediente", "La formulación")
    return t
CONF = {"ALTA": "Alta", "MEDIA": "Media", "BAJA": "Baja"}
def t_aristas():
    f = []
    for d in aristas():
        va = d["valores_admisibles"]; dom = str(va[0]) if len(va) == 1 else f"{min(va)} a {max(va)}"
        f.append((f"{d['origen']}→{d['destino']}", str(d["valor_propuesto"]), dom, SIGNO.get(d["signo"], d["signo"]), CONF[d["confianza"]["nivel"]], _limpiar(d["mecanismo_o_razon_cero"]), _respaldo(d)))
    return ("Los 48 vínculos no nulos de S2, con peso, dominio admisible, signo, confianza, mecanismo y respaldo",
            ["Vínculo", "Peso", "Dominio", "Signo", "Confianza", "Mecanismo propuesto", "Respaldo"], f,
            "*Nota.* Elaboración propia con las fichas bidireccionales. El dominio es el conjunto de valores que el equipo formulador considera admisibles. Los 162 pares restantes tienen peso 0, con la razón de ausencia o de mediación declarada en la ficha. Todos los valores son hipótesis de influencia estructural.")

def t_arbol_relaciones():
    dib = [("V05", "V02"), ("V05", "V01"), ("V03", "V06"), ("V02", "V06"), ("V01", "V06"), ("V07", "V06"), ("V06", "V11"), ("V06", "V12"), ("V11", "V14"), ("V12", "V15")]
    idx = {(d["origen"], d["destino"]): d for d in aristas()}; f = []
    for o, d in dib:
        a = idx[(o, d)]
        f.append((f"{o}→{d}", str(a["valor_propuesto"]), SIGNO.get(a["signo"], a["signo"]), CONF[a["confianza"]["nivel"]], _limpiar(a["explicacion_rival"])))
    return ("Relaciones dibujadas en el árbol de problemas, con su explicación rival principal",
            ["Relación", "Peso", "Signo", "Confianza", "Explicación rival principal"], f,
            "*Nota.* Elaboración propia con las fichas bidireccionales. Se dibujan las relaciones de peso 2 o 3 que unen niveles contiguos sin trazos ambiguos. Las demás permanecen en la tabla de vínculos del escenario S2.")

def resumen():
    """Cifras que el texto del Anexo A cita; el texto las toma con macros {{CAUSAL_*}}."""
    A = mat("S2"); n = int((A > 0).sum()); w = {1: int((A == 1).sum()), 2: int((A == 2).sum()), 3: int((A == 3).sum())}
    return {"CAUSAL_ARISTAS": str(n), "CAUSAL_SUMA": str(int(A.sum())), "CAUSAL_W1": str(w[1]), "CAUSAL_W2": str(w[2]), "CAUSAL_W3": str(w[3]),
            "CAUSAL_CICLOS": str(len(CICLOS_S2)), "CAUSAL_CICLOS_V15": str(sum(1 for c in CICLOS_S2 if 14 in c)),
            "CAUSAL_DENSIDAD": pc(100 * n / 210), "CAUSAL_OAT": str(AC["oat_resumen"]["perturbaciones"])}

TABLAS_CAUSAL = {"variables": t_variables, "escenarios": t_escenarios, "matriz_s2": t_matriz_s2, "clases_s2": t_clases_s2, "clases_5esc": t_clases_5esc,
                 "micmac_s2": t_micmac_s2, "rangos_5esc": t_rangos_5esc, "oat": t_oat, "recodificacion": t_recodificacion, "ciclos": t_ciclos,
                 "rutas": t_rutas, "aristas": t_aristas, "arbol_relaciones": t_arbol_relaciones}

if __name__ == "__main__":
    print(resumen())
    for k, fn in TABLAS_CAUSAL.items():
        t, enc, filas, nota = fn(); print(k, len(filas), "filas;", len(enc), "cols;", t[:70])
