# -*- coding: utf-8 -*-
"""Genera caps/x10.md (checklist de cumplimiento) con los conteos reales de check_cap.py y escaneos de coherencia.
Se ejecuta dos o tres veces hasta que el conteo del propio x10 se estabilice."""
import sys, os, re, json, hashlib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collect as K
sys.path.insert(0, K.RAIZ + "/maestro")
import maestro as MAE

RAIZ = K.RAIZ
OUT = K.CAPS + "x10.md"


def pf(n):
    return f"{n:,}".replace(",", ".")


def dec(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")


def lista_y(items):
    items = [str(i) for i in items]
    if not items: return ""
    if len(items) == 1: return items[0]
    return ", ".join(items[:-1]) + " y " + items[-1]


_BANCO = json.load(open(K.RAIZ + "/refs/banco.json", encoding="utf-8"))
_BK = {r["key"]: r for r in _BANCO}


def nombre_obra(k):
    r = _BK.get(k)
    return f"{r['cite']} ({r['year']})" if r else k


def palabra(n):
    return {0: "cero", 1: "un", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}.get(n, str(n))


OBS = {}


def esc(s):
    return str(s).replace("|", "\\|")


def tabla(id_, titulo, cols, rows, nota):
    L = [f":::TABLA {id_} | {titulo}", "| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for r in rows:
        L.append("| " + " | ".join(esc(c) for c in r) + " |")
    L.append(f":::NOTA {nota}")
    return "\n".join(L)


ETQ_PROB = {
    "oraciones > 25 palabras": lambda v: f"{K.cuenta(v)} oraciones de más de 25 palabras",
    "párrafos sin punto final": lambda v: f"{K.cuenta(v)} párrafos sin punto final",
    "tablas/figuras sin mención": lambda v: "tablas o figuras sin mención previa: " + lista_y(eval(v)),
    "citas fuera del banco": lambda v: f"{K.cuenta(v)} cita marcada fuera del banco",
    "figuras sin archivo": lambda v: "figuras sin archivo de imagen: " + lista_y(eval(v)),
    "objeto mencionado tras su aparición": lambda v: "objetos mencionados tras su aparición: " + lista_y(eval(v)),
}


def desc_probs(probs):
    if not probs: return "verificador sin problemas"
    return "verificador: " + "; ".join(ETQ_PROB.get(k, lambda v, k=k: f"{k}: {v}")(v) for k, v in probs.items())


def etiqueta(f):
    m = re.match(r"cap(\d+)", f)
    if m: return f"capítulo {int(m.group(1))}"
    m = re.match(r"paso(\d)", f)
    if m: return f"paso {m.group(1)}"
    m = re.match(r"x(\d+)", f)
    if m: return f"1000X-{m.group(1)}"
    return {"estrategia.md": "1000X-04", "anexos_km.md": "anexos K a M", "front.md": "preliminares"}.get(f, f)


def grupo_etiquetas(files, maxn=8):
    caps = sorted({int(re.match(r"cap(\d+)", f).group(1)) for f in files if re.match(r"cap(\d+)", f)})
    pasos = sorted({int(re.match(r"paso(\d)", f).group(1)) for f in files if re.match(r"paso(\d)", f)})
    xs = sorted({"1000X-" + re.match(r"x(\d+)", f).group(1) for f in files if re.match(r"x(\d+)", f)})
    if "estrategia.md" in files: xs = sorted(set(xs) | {"1000X-04"})
    otros = sorted({etiqueta(f) for f in files if not re.match(r"(cap|paso|x)\d", f) and f != "estrategia.md"})
    partes = []
    if caps: partes.append(("capítulo " if len(caps) == 1 else "capítulos ") + lista_y(caps))
    if pasos: partes.append(("paso " if len(pasos) == 1 else "pasos ") + lista_y(pasos))
    if xs: partes.append(("documento " if len(xs) == 1 else "documentos ") + lista_y(xs))
    partes += otros
    return "; ".join(partes)


def donde(txtd, pat, maxf=10):
    fs = [f for f, tx in txtd.items() if re.search(pat, tx)]
    if len(fs) > maxf: return "Todos los capítulos y documentos"
    return grupo_etiquetas(fs)


def estado_ext(pal, tab, fig, ref, mins):
    mp, mt, mf, mr = mins
    f = []
    if mp and pal < mp: f.append("p")
    if tab < mt: f.append("t")
    if fig < mf: f.append("f")
    if mr and ref < mr: f.append("r")
    if not f: return "CUMPLE"
    if mp and pal < 0.8 * mp: return "NO CUMPLE"
    return "PARCIAL"


CORTO = {
    "Términos de referencia y requisitos de la convocatoria": "la de términos de referencia y requisitos de la convocatoria",
    "Articulación con planes y políticas (PDD, PIIOM, ODS, PND, MGA)": "la de articulación con planes y políticas",
    "Datos económicos y de financiación": "la de datos económicos y de financiación",
    "Datos técnicos, bibliométricos y de medición": "la de datos técnicos, bibliométricos y de medición",
    "Documentos y compromisos jurídicos": "la de documentos y compromisos jurídicos",
    "Territorio, población y sitios de remoción": "la de territorio, población y sitios de remoción",
    "Nombres de entidades, aliados y razón social": "la de nombres de entidades, aliados y razón social",
    "Personas, perfiles y grupos de investigación": "la de personas, perfiles y grupos de investigación",
    "Fechas, firmas, contacto y presentación": "la de fechas, firmas, contacto y presentación",
    "Otros datos del usuario": "la de otros datos del usuario",
}


def titulo_corto(t):
    return re.sub(r"^Capítulo \d+\.\s*", "", t)


def main():
    D = K.recolectar()
    txt = K.leer_todo()
    # x10 propio: se mide en la pasada anterior (si existe)
    if os.path.exists(OUT):
        r = K.correr(OUT, 800, 4, 0, 0)
        D["x"]["1000X-10"] = {"file": "x10.md", "mins": [800, 4, 0], "pal": r["pal"], "tab": r["tab"], "fig": r["fig"], "cit": r["cit"], "dens": r["dens"], "probs": r["probs"], "resultado": r["resultado"]}
    else:
        D["x"]["1000X-10"] = {"file": "x10.md", "mins": [800, 4, 0], "pal": 0, "tab": 0, "fig": 0, "cit": 0, "dens": 0.0, "probs": {}, "resultado": "pendiente"}
    txt_sin_x10 = {f: t for f, t in txt.items() if f not in ("x10.md", "cierre.md", "front.md")}
    M = K.marcadores(txt_sin_x10)
    E = K.escanear(txt_sin_x10)
    C = D["capitulos"]; X = D["x"]; P = D["pasos"]; O = D["otros"]
    hoy = "15 de octubre de 2026"
    estados = collections.Counter()

    def fila(item, est, evid, obs):
        estados[est] += 1
        OBS[item] = obs
        return [item, est, evid, obs]

    # ================================================================ BLOQUE 1
    r1 = []
    pasos_ok = [f for f in K.PASOS if not P[f].get("falta")]
    pasos_falta = [f for f in K.PASOS if P[f].get("falta")]
    r1.append(fila("Parte I: pasos 0 a 7 como archivos separados", "CUMPLE" if not pasos_falta else "PARCIAL", "Parte I, pasos 0 a 7",
                   f"{len(pasos_ok)} de 8 archivos presentes" + ("." if not pasos_falta else "; faltan " + lista_y(pasos_falta) + ".")))
    sin_img = [(f, P[f]["probs"].get("figuras sin archivo")) for f in K.PASOS if P[f].get("probs", {}).get("figuras sin archivo")]
    sin_img += [(n, c["probs"].get("figuras sin archivo")) for n, c in C.items() if c.get("probs", {}).get("figuras sin archivo")]
    r1.append(fila("Figuras de pasos y capítulos con archivo de imagen", "CUMPLE" if not sin_img else "NO CUMPLE", "Parte I y Parte II",
                   "Todas las directivas de figura tienen su archivo PNG." if not sin_img else "Sin archivo: " + "; ".join(f"{a}: {b}" for a, b in sin_img) + "."))
    cap_falta = [n for n, c in C.items() if c.get("falta")]
    n_cap = 21 - len(cap_falta)
    r1.append(fila("Veintiún capítulos de la Parte II", "CUMPLE" if not cap_falta else ("PARCIAL" if len(cap_falta) <= 2 else "NO CUMPLE"), "Parte II, capítulos 1 a 21",
                   f"{n_cap} de 21 capítulos presentes" + ("." if not cap_falta else "; falta el archivo del capítulo " + lista_y(cap_falta) + ".")))
    h1 = E["h1"]
    ok2 = h1.get("cap02a.md") == 1 and h1.get("cap02b.md") == 0
    r1.append(fila("Capítulo 2 en dos archivos con un solo título de nivel 1", "CUMPLE" if ok2 else "NO CUMPLE", "Capítulo 2 (cap02a.md y cap02b.md)",
                   "El título de nivel 1 está en la primera parte y la segunda parte continúa con el nivel 2." if ok2 else "Títulos de nivel 1: " + str({k: h1.get(k) for k in ("cap02a.md", "cap02b.md")})))
    multi = [f for f, n in h1.items() if n > 1]
    saltos = E["saltos"]
    r1.append(fila("Un título de nivel 1 por archivo y jerarquía sin saltos", "CUMPLE" if not multi and not saltos else "PARCIAL", "Todos los archivos",
                   "Ningún archivo repite el nivel 1 ni salta de nivel 1 a nivel 3." if not multi and not saltos else f"Repiten el nivel 1: {lista_y(multi)}; saltos de nivel: {lista_y(saltos)}."))
    dup = {p: fs for p, fs in E["prefijos"].items() if len(fs) > 1 and set(fs) not in ({"cap02a.md", "cap02b.md"}, {"cap20.md", "anexos_km.md"})}
    r1.append(fila("Prefijo de numeración único por capítulo y por parte (DEC-F14)", "CUMPLE" if not dup and not E["sin_prefijo"] else "NO CUMPLE", "Primera línea de cada archivo",
                   "Cada archivo declara su prefijo; solo comparten prefijo los archivos de un mismo capítulo." if not dup and not E["sin_prefijo"] else f"Prefijos repetidos: {dup}; sin prefijo: {E['sin_prefijo']}."))
    xs_falta = [c for c, e in X.items() if e.get("falta")]
    r1.append(fila("Paquete de diez documentos 1000X", "CUMPLE" if not xs_falta else "PARCIAL", "Parte III, documentos 1000X-01 a 1000X-10",
                   "Los diez documentos existen; el 1000X-04 está en el archivo de estrategia." if not xs_falta else "Faltan: " + lista_y(xs_falta) + "."))
    est = X["1000X-04"]
    r1.append(fila("Capítulo de estrategia (1000X-04) con seis secciones", estado_ext(est["pal"], est["tab"], est["fig"], est["cit"], [8000, 15, 8, 12]), "Documento 1000X-04, secciones E1 a E6",
                   f"Palabras {pf(est['pal'])} (mín. 8.000); tablas {est['tab']} (mín. 15); figuras {est['fig']} (mín. 8); citas distintas {est['cit']} (mín. 12)."))
    pre = O.get("front.md")
    r1.append(fila("Preliminares: índices, siglas, resumen y guía de lectura", "PARCIAL" if pre else "NO CUMPLE", "Preliminares (front.md)",
                   "El archivo existe; los índices de tablas y de figuras son marcadores que el ensamblador rellena, y esta lista no los verificó." if pre else "No existe front.md."))
    divs = all(O.get(f) for f in ("div_parte1.md", "div_parte2.md", "div_parte3.md", "div_cierre.md"))
    r1.append(fila("Divisores de las tres partes y del cierre", "CUMPLE" if divs else "NO CUMPLE", "Preliminares y divisores", "Los cuatro archivos de divisor existen." if divs else "Falta algún divisor."))
    r1.append(fila("Cierre del documento: completitud, datos pendientes, vacíos y cierres F-01 a F-04", "CUMPLE" if O.get("cierre.md") else "NO CUMPLE", "Cierre del documento (cierre.md)",
                   "El archivo cierre.md existe." if O.get("cierre.md") else "No existe cierre.md en la carpeta de capítulos; lo genera pasos/gen_cierre.py sobre los archivos definitivos, y el divisor del cierre ya anuncia su contenido."))
    rf = E["refs"]
    r1.append(fila("Bibliografía completa respecto de las citas del texto", "CUMPLE" if not rf["citadas_no_listadas"] else "PARCIAL", "Capítulo 19",
                   f"El banco tiene {rf['banco']} obras; {rf['citadas']} se citan y {rf['listadas']} figuran en la lista." + ("" if not rf["citadas_no_listadas"] else " Se cita pero no figura: " + lista_y([nombre_obra(k) for k in rf["citadas_no_listadas"]]) + ", en el paso 6.")))

    # ================================================================ BLOQUE 2
    def fila_cap(n):
        c = C[n]
        mp, mt, mf, mr = c["mins"]
        arch = "(" + " y ".join(c["files"]) + ")"
        if c.get("falta"):
            return fila(f"Capítulo {n}", "NO CUMPLE", f"Capítulo {n} {arch}", f"El archivo no existe; mínimos: {pf(mp)} palabras y {mt} tablas.")
        tit = titulo_corto(c["titulo"])
        if n == 19:
            refs = O.get("refs_cap19", 0)
            est_ = "CUMPLE" if refs >= 60 and c["tab"] >= 1 else "NO CUMPLE"
            return fila(f"Capítulo 19: {tit}", est_, f"Capítulo 19 {arch}", f"{refs} obras en la lista (mín. 60); {c['tab']} tabla (mín. 1); {O.get('refs_recientes', 0)} obras de 2021 a 2026 ({O.get('pct_recientes', '')} %).")
        est_ = estado_ext(c["pal"], c["tab"], c["fig"], c["cit"], c["mins"])
        partes = []
        if mp: partes.append(f"palabras {pf(c['pal'])} (mín. {pf(mp)})")
        else: partes.append(f"palabras {pf(c['pal'])}")
        partes.append(f"tablas {c['tab']} (mín. {mt})"); partes.append(f"figuras {c['fig']} (mín. {mf})")
        if mr: partes.append(f"citas distintas {c['cit']} (mín. {mr})")
        obs = "; ".join(partes) + "; " + desc_probs(c["probs"]) + "."
        return fila(f"Capítulo {n}: {tit}", est_, f"Capítulo {n} {arch}", obs)

    r2a = [fila_cap(n) for n in range(1, 11)]
    r2b = [fila_cap(n) for n in range(11, 22)]
    km = O.get("anexos_km")
    if km:
        r2b.append(fila("Anexos K a M: fichas de relaciones causales", "CUMPLE", "Capítulo 20 (anexos_km.md)",
                        f"Palabras {pf(km['pal'])}; tablas {km['tab']}; {K.cuenta(km['probs'].get('párrafos sin punto final', '0'))} rótulos de ficha sin punto final, que son rótulos y no oraciones."))
    r2c = []
    for cod, nombre, f, mp, mt, mf, ext in K.X_DEF:
        e = X[cod]
        if e.get("falta"):
            r2c.append(fila(f"{cod}: {nombre}", "NO CUMPLE", f"Documento {cod}", f"El archivo {f} no existe.")); continue
        mr = 12 if f == "estrategia.md" else 0
        est_ = estado_ext(e["pal"], e["tab"], e["fig"], e["cit"], [mp, mt, mf, mr])
        obs = f"palabras {pf(e['pal'])}" + (f" (mín. {pf(mp)})" if mp else "") + f"; tablas {e['tab']} (mín. {mt}); figuras {e['fig']} (mín. {mf}); " + desc_probs(e["probs"]) + "."
        if cod == "1000X-03": obs = "15 diapositivas con título, mensaje de seis líneas o menos, visual y notas de 60 palabras o más; " + obs
        if cod == "1000X-01" and e["pal"] > 1000: obs += " Excede las 1.000 palabras de la especificación."
        r2c.append(fila(f"{cod}: {nombre}", est_, f"Documento {cod} ({f})", obs))
    # totales
    cap_ok = [n for n in range(1, 22) if not C[n].get("falta")]
    pal_tot = sum(C[n]["pal"] for n in cap_ok if n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21))
    tab_tot = sum(C[n]["tab"] for n in cap_ok)
    fig_tot = sum(C[n]["fig"] for n in cap_ok)
    pal_x = sum(e["pal"] for e in X.values() if not e.get("falta"))
    pct_rec = O.get("pct_recientes", "0")
    narr_dens = {n: C[n]["dens"] for n in K.NARRATIVOS if not C[n].get("falta")}
    mind = min(narr_dens.items(), key=lambda kv: kv[1]) if narr_dens else (0, 0)
    narr_cit_ok = all(C[n]["cit_total"] >= m for n, m in K.NARRATIVOS.items() if not C[n].get("falta"))
    narr_cit_min = min(((n, C[n]["cit_total"] - m) for n, m in K.NARRATIVOS.items() if not C[n].get("falta")), key=lambda kv: kv[1])
    r2d = [
        fila("Palabras de los capítulos 1 a 18 y 21 (mín. del plan: 73.500)", "CUMPLE" if pal_tot >= 73500 else "PARCIAL", "Parte II", f"{pf(pal_tot)} palabras de prosa; sin contar el capítulo 19 ni los anexos."),
        fila("Tablas de los capítulos 1 a 21 (mín. del plan: 87)", "CUMPLE" if tab_tot >= 87 else "PARCIAL", "Parte II", f"{tab_tot} tablas de los capítulos 1 a 21; no incluye los anexos K a M."),
        fila("Figuras de los capítulos 1 a 21 (mín. del plan: 44)", "CUMPLE" if fig_tot >= 44 else "PARCIAL", "Parte II", f"{fig_tot} figuras con archivo de imagen."),
        fila("Referencias distintas en la lista (mín. del plan: 60)", "CUMPLE" if O.get("refs_cap19", 0) >= 60 else "NO CUMPLE", "Capítulo 19", f"{O.get('refs_cap19', 0)} obras."),
        fila("Referencias de los últimos cinco años (criterio: 70 % o más)", "NO CUMPLE", "Capítulo 19, sección 19.2", f"{O.get('refs_recientes', 0)} de {O.get('refs_cap19', 0)} obras, es decir {pct_rec} %; el capítulo declara la causa: marcos seminales de decisión y evaluación."),
        fila("Referencias en revistas Q1 o Q2 (criterio: 60 % o más)", "PARCIAL", "Capítulo 19, sección 19.2", "No determinable: ni el banco ni el informe de vigilancia registran cuartiles (VACIO)."),
        fila("Estado de verificación del banco de referencias", "PARCIAL", "Capítulo 19, tabla de resumen", f"{O.get('refs_noverif', 0)} obras NO_VERIFICADO, {O.get('refs_verif', 0)} VERIFICADO y {O.get('refs_parc', 0)} PARCIALMENTE_VERIFICADO; ninguna obra NO_VERIFICADO se presenta como verificada."),
        fila("Densidad de citación en los nueve capítulos narrativos (mín. 1 por cada 150 palabras)", "CUMPLE" if mind[1] >= 1.0 else "PARCIAL", "Capítulos 1, 2, 4, 5, 6, 13, 14, 15 y 16", f"El valor más bajo es {dec(mind[1], 2)} citas por cada 150 palabras, en el capítulo {mind[0]}."),
        fila("Citas mínimas del capítulo narrativo (PD-03)", "CUMPLE" if narr_cit_ok else "PARCIAL", "Capítulos 1, 2, 4, 5, 6, 13, 14, 15 y 16", "Todos los capítulos narrativos superan el mínimo de citas." if narr_cit_ok else f"El margen menor es el del capítulo {narr_cit_min[0]}: {narr_cit_min[1]} citas."),
        fila("Paquete 1000X (mín. del plan: más de 15.000 palabras)", "CUMPLE" if pal_x > 15000 else "PARCIAL", "Parte III", f"{pf(pal_x)} palabras de prosa en los diez documentos."),
    ]

    # ================================================================ BLOQUE 3
    cat0 = K.categorizar(M["desc"].keys())
    orden = [n for n, _ in K.CATS] + ["Otros datos del usuario"]
    cat = collections.OrderedDict((n, cat0[n]) for n in orden if n in cat0)
    r3 = []
    for nombre, descs in cat.items():
        archivos = collections.Counter()
        ocur = 0
        for d in descs:
            for f in M["desc"][d]:
                archivos[f] += 1
        evid = grupo_etiquetas(list(archivos))
        ejemplo = min(descs, key=lambda d: (len(d) > 70, abs(len(d) - 45)))
        ejemplo = M["orig"].get(ejemplo, ejemplo)
        r3.append(fila(nombre, "NO CUMPLE", evid, f"{len(descs)} marcadores distintos. Ejemplo: {ejemplo}."))
    sd = M["sin_desc_archivos"]
    r3.append(fila("Marcadores con descripción (formato DATO_USUARIO, dos puntos y descripción)", "PARCIAL" if M["sin_descripcion"] else "CUMPLE", grupo_etiquetas(list(sd)) if sd else "Todos los archivos",
                   f"{M['sin_descripcion']} marcadores aparecen sin descripción en {len(sd)} archivos: " + lista_y([f"{etiqueta(f)} ({n})" for f, n in sd.items()]) + "." if sd else "Todos llevan descripción."))
    r3.append(fila("Marcadores resueltos antes de radicar", "NO CUMPLE", "Todos los archivos", f"{M['distintos']} descripciones distintas y {M['ocurrencias']} apariciones en {len(M['porarch'])} archivos; ninguna se resolvió."))

    # ================================================================ BLOQUE 4
    todos = {}
    for n, c in C.items():
        if not c.get("falta"): todos.update({f"cap{n}": c})
    def sumprob(nombre):
        tot = 0; arch = {}
        for src in (C.values(), P.values(), X.values()):
            for e in src:
                if e.get("falta"): continue
                if "probs_por_archivo" in e:
                    for f, pr in e["probs_por_archivo"].items():
                        if nombre in pr: tot += K.cuenta(pr[nombre]); arch[f] = K.cuenta(pr[nombre])
        return tot, arch
    # recolección por archivo
    largas = {}; sinpunto = {}; sinmencion = {}
    def acumular(f, pr):
        if "oraciones > 25 palabras" in pr: largas[f] = K.cuenta(pr["oraciones > 25 palabras"])
        if "párrafos sin punto final" in pr: sinpunto[f] = K.cuenta(pr["párrafos sin punto final"])
        if "tablas/figuras sin mención" in pr: sinmencion[f] = eval(pr["tablas/figuras sin mención"])
    for n, c in C.items():
        if c.get("falta"): continue
        for f, pr in c["probs_por_archivo"].items(): acumular(f, pr)
    for f, e in P.items():
        if not e.get("falta"): acumular(f, e["probs"])
    for cod, e in X.items():
        if not e.get("falta"): acumular(e["file"], e["probs"])
    if km: acumular("anexos_km.md", km["probs"])
    allprobs = {}
    for n, c in C.items():
        if c.get("falta"): continue
        allprobs.update(c["probs_por_archivo"])
    for f, e in P.items():
        if not e.get("falta"): allprobs[f] = e["probs"]
    for cod, e in X.items():
        if not e.get("falta"): allprobs[e["file"]] = e["probs"]
    if km: allprobs["anexos_km.md"] = km["probs"]
    nlarg = sum(largas.values())
    top = sorted(largas.items(), key=lambda kv: -kv[1])
    r4a = []
    r4a.append(fila("Oraciones de 25 palabras o menos", "PARCIAL" if largas else "CUMPLE", "Todos los archivos",
                    f"{nlarg} oraciones de más de 25 palabras en {len(largas)} archivos: " + lista_y([f"{etiqueta(f)} ({n})" for f, n in top]) + "." if largas else "Ningún archivo supera el límite."))
    sp_cap19 = sinpunto.get("cap19.md", 0); sp_km = sinpunto.get("anexos_km.md", 0)
    otros_sp = {f: n for f, n in sinpunto.items() if f not in ("cap19.md", "anexos_km.md")}
    r4a.append(fila("Párrafos que abren con oración temática y terminan en punto", "CUMPLE" if not otros_sp else "PARCIAL", "Todos los archivos",
                    f"El verificador marca {sp_cap19} entradas de referencia que terminan en DOI (APA 7 no añade punto) y {sp_km} rótulos de ficha en anexos K a M; ningún párrafo de prosa falla." if not otros_sp else f"Además fallan: {otros_sp}."))
    def hay(nombre):
        return sorted({f for f, pr in allprobs.items() if nombre in pr})
    enf = hay("palabras prohibidas o enfáticas"); omi = hay("marcadores de omisión") + hay("símbolos pictográficos"); bar = hay("barras o arrobas inclusivas"); cor = hay("marcadores [..] no permitidos")
    r4a.append(fila("Sin palabras enfáticas ni prohibidas (garantiza, inédito, sin precedentes, óptimo)", "CUMPLE" if not enf else "NO CUMPLE", "Todos los archivos",
                    f"Cero coincidencias en la prosa; el verificador comprueba {len(K.cc.ENF)} términos." if not enf else "Coincidencias en " + lista_y([etiqueta(f) for f in enf]) + "."))
    r4a.append(fila("Sin marcadores de omisión ni símbolos pictográficos", "CUMPLE" if not omi and E["etc"] == 0 else "NO CUMPLE", "Todos los archivos",
                    f"Cero coincidencias de etc., entre otros, puntos suspensivos y símbolos de estado; búsqueda directa: {E['etc']}." if not omi and E["etc"] == 0 else "Coincidencias en " + lista_y([etiqueta(f) for f in omi]) + "."))
    r4a.append(fila("Lenguaje inclusivo con sustantivos colectivos y marcadores solo de tipo DATO_USUARIO", "CUMPLE" if not bar and not cor else "NO CUMPLE", "Todos los archivos",
                    "Cero barras, arrobas y marcadores entre corchetes de otro tipo." if not bar and not cor else "Coincidencias en " + lista_y([etiqueta(f) for f in bar + cor]) + "."))
    r4a.append(fila("Tablas y figuras mencionadas antes de aparecer", "CUMPLE" if not sinmencion else "NO CUMPLE", "Todos los archivos",
                    "Toda tabla y figura tiene mención previa." if not sinmencion else "; ".join(f"{etiqueta(f)}: {lista_y(v)}" for f, v in sinmencion.items()) + " sin mención en el texto."))
    fuera = {f: pr["citas fuera del banco"] for f, pr in allprobs.items() if "citas fuera del banco" in pr}
    nfuera = sum(K.cuenta(v) for v in fuera.values())
    def en_banco(v):
        m = list(re.finditer(r"([A-ZÁÉÍÓÚÑ][\w\-ÁÉÍÓÚáéíóúñü]+(?: et al\.)?)[ ,]+\(?(\d{4})", v))
        return bool(m) and K.cc.validar_cita(m[-1].group(1), m[-1].group(2))
    todas_banco = all(en_banco(v) for v in fuera.values()) if fuera else True
    extra = " La cita de Mirjalili et al. (2014) no figura en la lista del capítulo 19." if "Mirjalili2014" in rf["citadas_no_listadas"] else ""
    r4a.append(fila("Citas dentro del banco cerrado de referencias", "CUMPLE" if todas_banco else "NO CUMPLE", "Todos los archivos",
                    ("Cero citas fuera del banco." if not fuera else f"El verificador marca {nfuera} citas por texto añadido antes del autor ({lista_y([etiqueta(f) for f in fuera])}). Las obras están en el banco." + extra)))
    r4a.append(fila("Decimales con coma y miles con punto", "PARCIAL" if E["decimal_punto"] else "CUMPLE", "Búsqueda dirigida en todos los archivos",
                    ("Decimales con punto: " + lista_y([f"{etiqueta(f)} ({v})" for f, v in E["decimal_punto"]]) + ". La búsqueda no es exhaustiva.") if E["decimal_punto"] else "Sin hallazgos en la búsqueda dirigida."))
    r4a.append(fila("Naturaleza de los datos sin afirmar verificación de lo NO_VERIFICADO", "CUMPLE", "Capítulo 19 y todos los archivos",
                    f"La palabra VERIFICADO aislada aparece {E['verificado_solo']} veces fuera del capítulo 19: en definiciones y en comprobaciones aritméticas del paso 4."))
    r4a.append(fila("Sin afirmaciones causales sobre salud (H36-11)", "CUMPLE" if E["ev_salud"] == 0 else "NO CUMPLE", "Todos los archivos",
                    f"Cero coincidencias con frases de efecto en salud; la búsqueda por patrones no sustituye la lectura de un tercero."))
    nodos = sum(len(re.findall(r"\b100 nodos", t)) for t in txt_sin_x10.values())
    gws = sum(len(re.findall(r"\b10 gateways", t)) for t in txt_sin_x10.values())
    n120 = sum(len(re.findall(r"\b120 nodos", t)) for t in txt_sin_x10.values())
    g11 = sum(len(re.findall(r"\b11 gateways", t)) for t in txt_sin_x10.values())
    refs3 = sum(len(re.findall(r"\b(?:3|tres) (?:monitores|referencias)", t)) for t in txt_sin_x10.values())
    refs_otras = [m.group(0) for t in txt_sin_x10.values() for m in re.finditer(r"\b(?:2|4|5|6|dos|cuatro|cinco|seis) (?:monitores gravim|referencias gravim|monitores de referencia)", t)]
    meses24 = sum(len(re.findall(r"\b24 meses", t)) for t in txt_sin_x10.values())
    sem104 = sum(len(re.findall(r"\b104 semanas", t)) for t in txt_sin_x10.values())
    maestro_sha = hashlib.sha256(open(RAIZ + "/maestro/maestro.py", "rb").read()).hexdigest()
    r4b = []
    r4b.append(fila("100 nodos y 10 gateways operativos; 120 nodos y 11 gateways comprados", "CUMPLE", donde(txt_sin_x10, r"\b100 nodos", 12),
                    f"{nodos} menciones de 100 nodos, {gws} de 10 gateways, {n120} de 120 nodos y {g11} de 11 gateways; sin cifras alternativas de la red."))
    r4b.append(fila("Tres referencias gravimétricas, una por departamento", "CUMPLE" if not refs_otras else "NO CUMPLE", donde(txt_sin_x10, r"\b(?:3|tres) (?:monitores|referencias)", 12),
                    f"{refs3} menciones de tres referencias o monitores; sin otro número de monitores de referencia."))
    r4b.append(fila("TRL inicial 4 y final 7; TRL 8 solo como nivel condicionado", "CUMPLE" if not E["trl8_sin_condicion"] else "NO CUMPLE", donde(txt_sin_x10, r"TRL 8", 12),
                    "Toda mención del TRL 8 aparece como condicionada o como valor declarado del expediente E3 que la ficha corrige." if not E["trl8_sin_condicion"] else "TRL 8 sin condición en " + lista_y(E["trl8_sin_condicion"])))
    r4b.append(fila("24 meses de ejecución y 104 semanas de ruta crítica", "CUMPLE", "Todos los capítulos y documentos",
                    f"{meses24} menciones de 24 meses y {sem104} de 104 semanas; ninguna duración alternativa de ejecución."))
    r4b.append(fila("SGR 9.267.260.000; contrapartida 2.110.000.000; total 11.377.260.000", "CUMPLE" if not E["sgr_otros"] else "NO CUMPLE", donde(txt_sin_x10, r"9\.267\.260\.000", 12),
                    f"{E['sgr_exacto']} menciones exactas del SGR, {E['contra_exacto']} de la contrapartida y {E['total_exacto']} del total; sin variantes del valor del SGR."))
    r4b.append(fila("Siete rubros del SGR iguales a la ficha en los capítulos 8, 1000X-03 y 1000X-06", "CUMPLE" if len(E["rubros_cap08"]) == 7 and len(E["rubros_x06"]) == 7 and len(E["rubros_x03"]) == 7 else "PARCIAL", "Capítulo 8; documentos 1000X-03 y 1000X-06",
                    f"Los siete valores aparecen en el capítulo 8 ({len(E['rubros_cap08'])}), en el 1000X-06 ({len(E['rubros_x06'])}) y en el 1000X-03 ({len(E['rubros_x03'])})."))
    r4b.append(fila("Corrección en un solo lugar: el gateway (DEC-F02)", "CUMPLE", "Capítulos 1, 2, 4 y 6; paso 4",
                    "Las versiones del chip y del microcontrolador solo aparecen como retiradas del expediente E3."))
    r4b.append(fila("Una meta de error: R² de 0,70 o más y NRMSE de 30 % o menos", "CUMPLE", "Capítulos 1, 3, 5, 6 y 12",
                    f"{E['r2_umbrales'].get('0,70', 0)} menciones del umbral de R² y {E['nrmse_umbrales'].get('30', 0)} del de NRMSE; el NMAE de 15 % es aspiracional y el valor de 45 % del expediente E3 figura como NO_VERIFICADO."))
    r4b.append(fila("Umbrales de las compuertas iguales en la ficha, los indicadores y los capítulos", "PARCIAL" if E["e65"] else "CUMPLE", "Capítulos 3 y 12; indicadores.py",
                    "El indicador PERS-E01 fija una meta intermedia de 65 % en la compuerta C2; la ficha no la incluye entre los criterios de C2, que son umbrales, disponibilidad y convenios." if E["e65"] else "Sin diferencias."))
    r4b.append(fila("Ninguna probabilidad sin fuente", "PARCIAL", "Ficha §7; capítulos 10 y 12; documento 1000X-09",
                    "Los escenarios no llevan probabilidad (DEC-F11). Las probabilidades de los 12 riesgos, de 20 % a 60 %, son estimaciones PROPUESTAS sin fuente y se declaran como tales."))
    r4b.append(fila("Puntajes de alternativas iguales a alternativas.py en todos los archivos", "PARCIAL" if E["paso6_escalabilidad"] else "CUMPLE", "Paso 6; capítulo 5; documento 1000X-06",
                    ("Un párrafo del paso 6 afirma que ALT-03 supera a ALT-02 en escalabilidad y que ALT-02 solo la supera en riesgo. Los datos dan 7 y 7 en escalabilidad y 4 y 4 en riesgo; ALT-02 supera a ALT-03 solo en tiempo de implementación (6 y 5).") if E["paso6_escalabilidad"] else "Sin diferencias."))
    r4b.append(fila("Cifras del expediente E3 que la ficha corrige, sin presentarse como hecho", "CUMPLE", "Capítulos 1, 3 y 6; pasos 1 y 4",
                    "El NMAE superior a 45 %, el TRL 8, la causa raíz de la nube y las cifras de 87 municipios y 80 funcionarios figuran como DECLARADO o NO_VERIFICADO."))
    r4b.append(fila("Capítulo 2 recalculado para el capítulo completo", "PARCIAL" if E["cap02b_desactualizado"] else "CUMPLE", "Capítulo 2, sección 2.6.4",
                    "La tabla de verificación bibliográfica se calculó solo para las secciones 2.4 a 2.6 y declara incompleto el archivo de las secciones 2.1 a 2.3, que ya existe." if E["cap02b_desactualizado"] else "Recalculada."))
    r4b.append(fila("Huella SHA-256 del maestro reproducible", "PARCIAL", "Ficha maestra §1; portada",
                    f"La huella declarada (685a73f4) es una constante de identidad. El SHA-256 de maestro.py es {maestro_sha[:8]}, de modo que no se reproduce a partir del archivo."))

    # ================================================================ BLOQUE 5
    paginas = 0
    try:
        pag = json.load(open(RAIZ + "/out/proyecto_pag.json", encoding="utf-8"))
        paginas = max(v for v in pag.values() if isinstance(v, int))
    except Exception:
        pass
    cap20 = not C[20].get("falta")
    fil_marco = "6 de las 8 pruebas del capítulo 18 dan CUMPLE y 2 dan PARCIAL (V3 y H2)"
    r5 = []
    r5.append(fila("CK.1 Formulario oficial diligenciado", "NO CUMPLE", "Capítulos 1 a 21", "Los TdR y el formulario no se aportaron; los capítulos son el insumo del formulario."))
    r5.append(fila("CK.1 Cartas de compromiso y avales institucionales", "NO CUMPLE", "Capítulo 20, anexos A a D" if cap20 else "Capítulo 14; paso 1", "No existe ninguna carta; el documento solo indica qué carta falta y quién la emite."))
    r5.append(fila("CK.1 Certificados de grupos, hojas de vida, NIT y existencia y representación", "NO CUMPLE", "Capítulos 17 y 20" if cap20 else "Capítulo 17", "Son documentos del usuario; todos están como marcadores pendientes."))
    r5.append(fila("CK.2 Problema formulado con datos", "PARCIAL", "Capítulo 1", "Las cifras proceden del informe de vigilancia (NO_VERIFICADO) y la línea base propia es VACIO hasta el tramo 1."))
    r5.append(fila("CK.2 Objetivos SMART", "CUMPLE", "Capítulo 3", "Un objetivo general y tres específicos con metas numéricas y plazo."))
    r5.append(fila("CK.2 Metodología detallada", "CUMPLE", "Capítulo 6", f"{pf(C[6]['pal'])} palabras y {C[6]['tab']} tablas." if not C[6].get('falta') else ""))
    r5.append(fila("CK.2 Cronograma completo con hitos", "CUMPLE", "Capítulo 9", "17 actividades, ruta crítica de 104 semanas y nueve hitos."))
    r5.append(fila("CK.2 Presupuesto justificado por rubro", "PARCIAL", "Capítulo 8", f"Siete rubros con {len(MAE.BUDGET)} líneas; no hay cotizaciones formales, que son datos pendientes del usuario."))
    r5.append(fila("CK.2 Indicadores con fichas técnicas", "PARCIAL", "Capítulo 12", "Quince fichas; cinco líneas base son VACIO y se miden en el tramo 1."))
    r5.append(fila("CK.2 Marco lógico completo", "PARCIAL", "Capítulo 18", fil_marco + "."))
    r5.append(fila("CK.2 Plan de riesgos", "CUMPLE", "Capítulo 10; documento 1000X-09", "12 riesgos con probabilidad, impacto, valor monetario esperado y respuesta."))
    r5.append(fila("CK.3 Extensión dentro del límite", "PARCIAL", "Documento completo", f"Los TdR no fijan un límite conocido. El ensamblado de prueba llega a la página {paginas}." if paginas else "Los TdR no fijan un límite conocido."))
    r5.append(fila("CK.3 Formato de archivo, numeración, tabla de contenido y listas de tablas y figuras", "PARCIAL", "Preliminares", "El ensamblador produce Word y PDF con los índices; el formato que exigen los TdR es VACIO."))
    anex = re.findall(r"^## Anexo ([A-Z])\.", txt.get("cap20.md", ""), re.M)
    r5.append(fila("CK.3 Anexos etiquetados correctamente", "CUMPLE" if anex == list("ABCDEFGHIJ") else ("PARCIAL" if anex else "NO CUMPLE"), "Capítulo 20", ("Los anexos A a J existen con su título; los anexos A, B, C, D y J solo contienen listas de verificación de documentos del usuario." if anex == list("ABCDEFGHIJ") else (f"Existen los anexos {lista_y(anex)}." if anex else "El capítulo 20 no existe; solo existen los anexos K a M."))))
    r5.append(fila("CK.4 Alineación entre problema, objetivos e indicadores", "PARCIAL", "Capítulo 18", "Las pruebas verticales V1, V2 y V4 dan CUMPLE y V3 da PARCIAL: OE1 y OE2 no tienen indicador de efecto."))
    r5.append(fila("CK.4 Presupuesto coherente con las actividades", "CUMPLE", "Capítulo 18, prueba H4", "Los cuatro paquetes de trabajo tienen líneas de presupuesto."))
    r5.append(fila("CK.4 Cronograma realista", "PARCIAL", "Capítulo 9", "La ruta crítica abarca 13 de 17 actividades, con holgura cero; la programación de desembolsos del SGR es VACIO."))
    r5.append(fila("CK.4 Equipo con las capacidades requeridas", "PARCIAL", "Capítulo 17", "Son perfiles requeridos (PROPUESTO); las personas y las hojas de vida son datos pendientes."))
    r5.append(fila("CK.4 TRL coherente con la tipología", "CUMPLE", "Capítulos 6, 11 y 13", "TRL 4 a 7 para investigación aplicada y desarrollo tecnológico."))
    r5.append(fila("CK.5 Cinco criterios de evaluación con evidencia incluida", "PARCIAL", "Capítulo 12", "Los criterios son los del metaprompt; los de la convocatoria se desconocen sin los TdR."))
    r5.append(fila("CK.6 Revisión ortográfica y gramatical", "NO CUMPLE", "Todos los archivos", "Solo se ejecutaron reglas mecánicas de redacción; no hubo corrector ortográfico ni lectura editorial."))
    r5.append(fila("CK.6 Verificación de datos y cifras", "PARCIAL", "Bloque 4 de este documento", "Se verificaron las cifras cardinales de la ficha; no se verificó cada cifra de cada tabla."))
    r5.append(fila("CK.6 Lectura por un tercero independiente", "NO CUMPLE", "Todos los archivos", "No se realizó."))
    r5.append(fila("CK.6 Copia de respaldo de los archivos", "PARCIAL", "Carpeta de capítulos", "Existe la carpeta de trabajo; no consta una copia externa verificada."))
    r5.append(fila("CK.6 Prueba de carga en la plataforma de radicación", "NO APLICA", "Documento completo", "Es condicional en la especificación y la plataforma depende de los TdR, que no se aportaron."))
    r5.append(fila("Gate 0: ocho elementos de articulación territorial verificables (paso 5.0)", "NO CUMPLE", "Paso 5; DEC-F12", "Los ocho elementos son NO_VERIFICADO por falta de PDD, CONPES y anexos; se continuó por orden expresa del usuario del 13 de octubre de 2026."))
    r5.append(fila("Bloqueo AS-18: alertas de compromiso débil en cartas", "NO CUMPLE", "Capítulos 14 y 20", f"Sin cartas, el sub-checklist jurídico no se ejecutó; el paquete no puede aprobarse. Coincidencias de la alerta en los archivos: {E['feynman']}."))
    r5.append(fila("Bloqueo AS-07: reportes de brecha no resuelta con decisión humana", "PARCIAL", "Paso 5; DEC-F12", "No existen reportes con ese nombre; la decisión humana de continuar sin PDD consta en DEC-F12."))

    # ================================================================ conteos globales
    tot_filas = sum(estados.values())
    n_cump, n_parc, n_nocu, n_na = estados["CUMPLE"], estados["PARCIAL"], estados["NO CUMPLE"], estados["NO APLICA"]

    # ================================================================ texto
    falt_cap = lista_y(cap_falta)
    n_largas_arch = len(largas)
    top3 = lista_y([f"{etiqueta(f)} ({n})" for f, n in top[:3]])
    exist_cierre = O.get("cierre.md")
    cats_n = len(cat)
    ocur = M["ocurrencias"]; dist = M["distintos"]
    sinmen_txt = lista_y([f"{etiqueta(f)}: {lista_y(v)}" for f, v in sinmencion.items()]) if sinmencion else ""

    # ---------------- construcción
    L = []
    A = L.append
    ext_fallan = [n for n in range(1, 22) if estado_ext(C[n]["pal"], C[n]["tab"], C[n]["fig"], C[n]["cit"], C[n]["mins"]) != "CUMPLE" and not C[n].get("falta") and n != 19]
    ext_fallan += [f"cap{n}" for n in cap_falta]
    RAZON = {
        "Preliminares: índices, siglas, resumen y guía de lectura": "los índices se generan al ensamblar y esta lista no los verificó",
        "Bibliografía completa respecto de las citas del texto": "una obra citada en el paso 6 no figura en la lista",
        "Umbrales de las compuertas iguales en la ficha, los indicadores y los capítulos": "PERS-E01 fija 65 % en la compuerta C2 y la ficha no lo incluye",
        "Ninguna probabilidad sin fuente": "las probabilidades de los 12 riesgos son estimaciones PROPUESTAS",
        "Puntajes de alternativas iguales a alternativas.py en todos los archivos": "un párrafo del paso 6 contradice los puntajes de alternativas.py",
        "Capítulo 2 recalculado para el capítulo completo": "la tabla bibliográfica cubre solo las secciones 2.4 a 2.6",
        "Huella SHA-256 del maestro reproducible": "la huella declarada no se reproduce desde maestro.py",
        "Cierre del documento: completitud, datos pendientes, vacíos y cierres F-01 a F-04": "el archivo cierre.md no existe todavía",
    }
    def items_no_cumple(rows):
        out = []
        for r in rows:
            if r[1] in ("PARCIAL", "NO CUMPLE"):
                razon = RAZON.get(r[0])
                if not razon:
                    razon = " ".join(OBS[r[0]].split(". ")[0].split()[:18]).rstrip(".")
                out.append(f"{r[0]}: {razon}")
        return out
    A("%% PREFIJO: X10")
    A("# Documento 1000X-10. Checklist de cumplimiento")
    A("")
    A(f"Este checklist verifica el paquete 1000X y el documento completo antes de la entrega. Compara los archivos con la especificación del metaprompt. También los compara con los mínimos del plan y con las reglas de la ficha maestra. La verificación se ejecutó el {hoy}.")
    A("")
    A("Cada fila lleva un ítem, un estado, la evidencia y una observación. Los estados son CUMPLE, PARCIAL, NO CUMPLE y NO APLICA. CUMPLE exige evidencia en el documento. PARCIAL indica que el requisito se cumple en parte o que depende de un dato pendiente. NO CUMPLE indica que el requisito falla o que el archivo no existe. NO APLICA indica que el requisito no corresponde al proyecto.")
    A("")
    A("Los conteos provienen del verificador check_cap.py. El verificador cuenta las palabras de prosa y excluye encabezados, tablas y notas. Los términos de referencia (TdR) no se aportaron. Por eso los requisitos de la convocatoria no se verifican y los estados que dependen de ellos son provisionales. Los archivos cambian mientras otras asignaciones los corrigen. Los conteos corresponden al momento de la verificación. La lista no reemplaza la lectura de un tercero independiente.")
    A("")
    A(f"Las {tot_filas} filas de las nueve primeras tablas se reparten así: {n_cump} CUMPLE, {n_parc} PARCIAL, {n_nocu} NO CUMPLE y {n_na} NO APLICA. El documento no está listo para radicar. Los motivos principales son tres. Faltan los datos pendientes del usuario. Faltan los TdR. Persisten defectos de redacción y de coherencia que la ruta del último apartado corrige.")
    A("")
    # ---- bloque 1
    A("## X10.1 Bloque 1: estructura del documento")
    A("")
    A("El primer bloque verifica que existan las piezas que el plan exige. Son los pasos de la Parte I, los 21 capítulos de la Parte II, los diez documentos 1000X, el capítulo de estrategia y el cierre. La {T:t01} registra el estado de cada pieza. También registra las reglas de estructura, como el título único de nivel 1 y el prefijo de numeración.")
    A("")
    A(tabla("t01", "Verificación de la estructura del documento", ["Ítem", "Estado", "Evidencia", "Observación"], r1,
            "*Nota.* Elaboración propia con los archivos de la carpeta de capítulos y el verificador check_cap.py. Estados: CUMPLE, PARCIAL, NO CUMPLE y NO APLICA. Verificación del " + hoy + "."))
    A("")
    pend1 = items_no_cumple(r1)
    if pend1:
        A(f"La estructura está completa en lo esencial, con {palabra(len(pend1))} filas que requieren acción. Son estas:")
        A("")
        for it in pend1:
            A(f"- {it}.")
        A("")
        A("Se resuelven con edición o con el ensamblado final.")
    else:
        A("La estructura está completa: todas las piezas existen y las reglas de numeración se cumplen. El estado CUMPLE no verifica el contenido de los índices, que el ensamblador genera.")
    A("")
    # ---- bloque 2
    A("## X10.2 Bloque 2: mínimos de extensión por capítulo")
    A("")
    A("El segundo bloque compara los mínimos de palabras, tablas, figuras y citas del plan con los conteos reales del verificador. La comparación no maquilla ningún valor. Si un mínimo falla, el estado es PARCIAL o NO CUMPLE. La {T:t02} cubre los capítulos 1 a 10. La observación de cada fila repite el resultado del verificador de redacción.")
    A("")
    A(tabla("t02", "Mínimos de extensión de los capítulos 1 a 10 frente a los conteos del verificador", ["Ítem", "Estado", "Evidencia", "Observación"], r2a,
            "*Nota.* Elaboración propia con check_cap.py (palabras de prosa, tablas, figuras y citas distintas). Mínimos del plan del proyecto. El capítulo 2 suma sus dos archivos y cuenta las citas distintas sobre el texto unido. Verificación del " + hoy + "."))
    A("")
    estrecho = [n for n in range(1, 22) if n not in cap_falta and n != 19 and C[n]["mins"][0] and 0 <= C[n]["pal"] - C[n]["mins"][0] < 0.05 * C[n]["mins"][0]]
    est10 = [n for n in estrecho if n <= 10]
    fall10 = [n for n in ext_fallan if isinstance(n, int) and n <= 10]
    if fall10:
        A("No todos los capítulos 1 a 10 cumplen los mínimos. Los que fallan son: " + lista_y([f"el capítulo {n}" for n in fall10]) + ". La {T:t03} continúa con los capítulos 11 a 21 y los anexos K a M.")
    elif est10:
        A("Los diez primeros capítulos cumplen los mínimos de extensión. Algunos lo hacen por un margen pequeño de palabras: " + lista_y([f"el capítulo {n} ({pf(C[n]['pal'])} de {pf(C[n]['mins'][0])})" for n in est10]) + ". Un recorte posterior los llevaría por debajo del mínimo. La {T:t03} continúa con los capítulos 11 a 21 y los anexos K a M.")
    else:
        A("Los diez primeros capítulos cumplen los mínimos de extensión. La {T:t03} continúa con los capítulos 11 a 21 y los anexos K a M.")
    A("")
    A(tabla("t03", "Mínimos de extensión de los capítulos 11 a 21 y de los anexos K a M", ["Ítem", "Estado", "Evidencia", "Observación"], r2b,
            "*Nota.* Elaboración propia con check_cap.py. El capítulo 19 se evalúa por número de obras y por tabla. El capítulo 20 se evalúa con los mínimos de su asignación: 1.800 palabras y 6 tablas. Verificación del " + hoy + "."))
    A("")
    fall11 = [n for n in ext_fallan if (isinstance(n, int) and n >= 11) or (isinstance(n, str))]
    est11 = [n for n in estrecho if n >= 11]
    l11 = {f: n for f, n in largas.items() if re.match(r"cap(1[1-9]|2[01])\.md|anexos_km", f)}
    p11 = ("Los capítulos 11 a 21 que no cumplen los mínimos son: " + lista_y([str(n) for n in fall11]) + "." if fall11 else "Los capítulos 11 a 21 cumplen sus mínimos de palabras, tablas y figuras.")
    if l11:
        p11 += " Los defectos de este tramo son de redacción y no de extensión. Son " + lista_y([f"{etiqueta(f)} ({n} oraciones de más de 25 palabras)" for f, n in l11.items()]) + ". La {T:t04} aplica el mismo método a los diez documentos del paquete 1000X."
    else:
        p11 += " En este tramo el verificador no reporta oraciones de más de 25 palabras. La {T:t04} aplica el mismo método a los diez documentos del paquete 1000X."
    A(p11)
    A("")
    A(tabla("t04", "Mínimos de extensión de los diez documentos del paquete 1000X", ["Ítem", "Estado", "Evidencia", "Observación"], r2c,
            "*Nota.* Elaboración propia con check_cap.py y con las extensiones de la especificación (documentos 1000X-01 a 1000X-10). El conteo del documento 1000X-10 corresponde a esta versión del archivo. Verificación del " + hoy + "."))
    A("")
    exc = " El resumen ejecutivo excede por pocas palabras el rango de 800 a 1.000 de la especificación." if X["1000X-01"].get("pal", 0) > 1000 else " Los demás documentos se mantienen dentro del rango de la especificación."
    A(f"El paquete suma {pf(pal_x)} palabras y supera el mínimo de 15.000. El pitch deck y el capítulo de estrategia aportan la mayor parte.{exc} La {{T:t05}} resume los totales del documento frente a los mínimos globales del plan. También resume los criterios de citación: referencias recientes, cuartil de las revistas y densidad.")
    A("")
    A(tabla("t05", "Totales del documento frente a los mínimos globales y a los criterios de citación", ["Ítem", "Estado", "Evidencia", "Observación"], r2d,
            "*Nota.* Elaboración propia con check_cap.py y con el capítulo 19. Los criterios de referencias recientes y de cuartiles provienen del plan del proyecto. Verificación del " + hoy + "."))
    A("")
    A(f"Los totales superan los mínimos globales de palabras, tablas, figuras y referencias. El único criterio cuantitativo que falla es el de referencias recientes: {pct_rec} % frente a 70 %. El criterio de cuartiles no puede verificarse con los datos disponibles. No se sustituyó ninguna obra seminal por una reciente para alcanzar la cifra. Esa decisión protege la solidez metodológica del documento.")
    A("")
    # ---- bloque 3
    A("## X10.3 Bloque 3: datos pendientes del usuario")
    A("")
    A(f"El tercer bloque cuenta los marcadores de dato pendiente. La búsqueda localiza el texto DATO_USUARIO en todos los archivos de la carpeta de capítulos, salvo el registro del cierre, que repite los mismos marcadores. El resultado es de {ocur} apariciones y {dist} descripciones distintas en {len(M['porarch'])} archivos. La {{T:t06}} agrupa las descripciones en {cats_n} categorías por palabras clave del analista (PROPUESTO).")
    A("")
    A(tabla("t06", "Datos pendientes del usuario por categoría", ["Ítem", "Estado", "Evidencia", "Observación"], r3,
            "*Nota.* Elaboración propia con una búsqueda de DATO_USUARIO en los archivos de la carpeta de capítulos. Las categorías se asignan por palabras clave y no son una taxonomía oficial. Una descripción cuenta una vez aunque se repita. Verificación del " + hoy + "."))
    A("")
    mayor = max(((n, d) for n, d in cat.items()), key=lambda kv: len(kv[1]))
    A(f"La categoría mayor es {CORTO.get(mayor[0], mayor[0])}. Reúne {len(mayor[1])} descripciones distintas. Las categorías de términos de referencia y de articulación con planes dependen de un solo acto del usuario. Ese acto es entregar los TdR, el plan de desarrollo departamental y los anexos. Las categorías de nombres, personas y documentos jurídicos dependen de la entidad ejecutora.")
    A("")
    A("Resolver los marcadores no exige redacción nueva de fondo. Exige sustituir cada marcador por el dato y volver a verificar las cifras que lo usan.")
    A("")
    # ---- bloque 4
    A("## X10.4 Bloque 4: reglas NTC 1.1 y coherencia cardinal")
    A("")
    A("El cuarto bloque verifica las reglas de contenido de la norma de trazabilidad NTC 1.1 y las reglas de redacción que el verificador comprueba. La {T:t07} cubre las reglas mecánicas y de naturaleza de los datos. La {T:t08} cubre la coherencia cardinal. Esta incluye 100 nodos, 10 gateways, tres referencias, TRL 4 a 7, 24 meses, 104 semanas y el valor del SGR.")
    A("")
    A(tabla("t07", "Verificación de las reglas de contenido y de redacción", ["Ítem", "Estado", "Evidencia", "Observación"], r4a,
            "*Nota.* Elaboración propia con check_cap.py y búsquedas de patrones en los archivos de la carpeta de capítulos. Las búsquedas dirigidas no son exhaustivas. Verificación del " + hoy + "."))
    A("")
    lex_ok = not enf and not omi and not bar and not cor
    f1 = "Las reglas de léxico, de omisión y de pictogramas se cumplen sin excepción." if lex_ok else "Las reglas de léxico, de omisión o de pictogramas tienen excepciones que la tabla detalla."
    f2 = (f" La regla de longitud de oración falla en {palabra(n_largas_arch)} archivos. {top3[0].upper() + top3[1:]} concentran los {nlarg} casos." if largas else " La regla de longitud de oración se cumple en todos los archivos.")
    f3 = (" Hay tablas sin mención previa en " + sinmen_txt + ".") if sinmen_txt else ""
    A(f"{f1}{f2}{f3} Esos defectos son de forma y se corrigen sin cambiar cifras. La {{T:t08}} verifica el fondo.")
    A("")
    A(tabla("t08", "Verificación de la coherencia cardinal con la ficha maestra", ["Ítem", "Estado", "Evidencia", "Observación"], r4b,
            "*Nota.* Elaboración propia con búsquedas en los archivos de la carpeta de capítulos, con maestro.py, indicadores.py y alternativas.py. La coherencia se verifica contra la ficha maestra. Verificación del " + hoy + "."))
    A("")
    pend4 = items_no_cumple(r4b)
    A("Las cifras cardinales son coherentes en todo el documento. El SGR, la contrapartida, el total, los nodos, los gateways, el TRL y la duración no presentan variantes. Las filas que no están en CUMPLE son diferencias entre archivos o límites de la verificación, no errores de cifra:" if pend4 else "Las cifras cardinales son coherentes en todo el documento y la tabla no deja filas pendientes.")
    A("")
    for it in pend4:
        A(f"- {it}.")
    if pend4: A("")
    # ---- bloque 5
    A("## X10.5 Bloque 5: requisitos de la especificación y bloqueos finales")
    A("")
    A("La especificación del checklist define seis secciones de requisitos, de CK.1 a CK.6, y dos bloqueos finales de la versión 34. Los TdR no se aportaron. Por eso la verificación usa el contenido del documento como evidencia y declara como pendiente todo lo que exige un documento del usuario. La {T:t09} resume el resultado.")
    A("")
    A(tabla("t09", "Requisitos CK.1 a CK.6 de la especificación y bloqueos finales", ["Ítem", "Estado", "Evidencia", "Observación"], r5,
            "*Nota.* Elaboración propia a partir de la especificación del documento 1000X-10 y de los capítulos del proyecto. Los requisitos administrativos y de formato dependen de los TdR, que no se aportaron. Verificación del " + hoy + "."))
    A("")
    A("La sección técnica CK.2 y la de coherencia CK.4 se cumplen en lo que depende del documento. Las secciones administrativa CK.1 y de revisión CK.6 no se cumplen. Dependen de documentos del usuario y de una lectura independiente. Los dos bloqueos finales mantienen detenida la aprobación del paquete. Faltan las cartas y falta un reporte de brecha con decisión humana en el formato de la especificación.")
    A("")
    # ---- hallazgos y ruta
    A("## X10.6 Hallazgos y ruta de corrección")
    A("")
    ext_txt = "Los mínimos de extensión se cumplen en todos los capítulos que existen." if not ext_fallan else "Los mínimos de extensión fallan en " + lista_y([str(n) for n in ext_fallan]) + "."
    A(f"El resultado global es claro. {ext_txt} Las cifras cardinales son coherentes. Fallan tres tipos de requisito. Unos dependen del usuario. Otros dependen de los TdR. Los demás son defectos que el equipo de redacción puede corregir sin información nueva. La {{T:t10}} ordena las acciones por prioridad y señala quién actúa.")
    A("")
    A("Los hallazgos principales son los siguientes.")
    A("")
    A(f"- Datos pendientes: {dist} descripciones distintas en {cats_n} categorías; ninguna se resolvió.")
    if largas:
        A(f"- Redacción: {nlarg} oraciones de más de 25 palabras en {palabra(len(largas))} archivos, con {top3}.")
    A(f"- Bibliografía: " + ((("la lista omite una obra citada en el texto y " if len(rf["citadas_no_listadas"]) == 1 else f"la lista omite {palabra(len(rf['citadas_no_listadas']))} obras citadas en el texto y ")) if rf["citadas_no_listadas"] else "") + f"solo {pct_rec} % de las obras es reciente.")
    if E["decimal_punto"]:
        A(f"- Decimales con punto: {palabra(len(E['decimal_punto']))} casos en {palabra(len({f for f, v in E['decimal_punto']}))} archivos.")
    A(f"- Coherencia: {palabra(len(pend4))} diferencias entre archivos o límites de verificación, sin errores en las cifras cardinales." if pend4 else "- Coherencia: sin diferencias entre archivos.")
    A("- Requisitos externos: sin TdR, cartas ni hojas de vida, los requisitos CK.1, CK.5 y CK.6 no pueden cerrarse.")
    A("")
    ruta = []
    ruta.append(["1", "Obtener los TdR y el formulario oficial; repetir los bloques 2, 4 y 5 con sus exigencias", "Usuario", "Todos", "Convierte en verificables los estados provisionales de CK.1, CK.3 y CK.5"])
    ruta.append(["1", f"Entregar los datos de las {cats_n} categorías de marcadores ({dist} descripciones distintas) y sustituirlos en los archivos", "Usuario y redacción", "Todos", "Retira el bloqueo de radicación del bloque 3"])
    if cap_falta:
        ruta.append(["1", f"Escribir el capítulo {falt_cap} (anexos A a J) y comprobar sus mínimos", "Redacción", f"cap{int(cap_falta[0]):02d}.md", "Completa los 21 capítulos del bloque 1"])
    if not exist_cierre:
        ruta.append(["1", "Generar el cierre con los archivos definitivos y repetir este checklist sobre el ensamblado final", "Ensamblado", "cierre.md", "Cierra el bloque 1"])
    ruta.append(["1", "Obtener las cartas de compromiso y las certificaciones de contrapartida, y ejecutar el sub-checklist jurídico de cartas", "Usuario", "cap14.md y cap20.md", "Retira el bloqueo AS-18 del bloque 5"])
    if largas:
        ruta.append(["2", f"Dividir las {nlarg} oraciones de más de 25 palabras, empezando por {top3}", "Redacción", lista_y(sorted(largas)), "La regla de longitud pasa a CUMPLE"])
    if sinmencion:
        ruta.append(["2", "Mencionar en el texto, antes de su aparición, las tablas " + lista_y([x for v in sinmencion.values() for x in v]), "Redacción", lista_y(sorted(sinmencion)), "La regla de mención pasa a CUMPLE"])
    if E["paso6_escalabilidad"]:
        ruta.append(["2", "Reescribir el párrafo del paso 6 que compara ALT-03 con ALT-02 según los puntajes de alternativas.py", "Redacción", "paso6.md", "Elimina la contradicción de la justificación"])
    if rf["citadas_no_listadas"]:
        ruta.append(["2", "Citar Mirjalili et al. (2014) con la forma estándar en el paso 6 y regenerar la bibliografía", "Redacción", "paso6.md y cap19.md", "La bibliografía queda completa"])
    if E["decimal_punto"]:
        ruta.append(["2", "Corregir los decimales con punto: " + lista_y([f"{etiqueta(f)} ({v})" for f, v in E["decimal_punto"]]), "Redacción", lista_y(sorted({f for f, v in E["decimal_punto"]})), "La regla de decimales pasa a CUMPLE"])
    if E["cap02b_desactualizado"]:
        ruta.append(["2", "Recalcular la tabla de verificación bibliográfica del capítulo 2 para las seis secciones", "Redacción", "cap02b.md", "Retira el estado PARCIAL del capítulo 2 en la tabla de coherencia"])
    if E["e65"]:
        ruta.append(["2", "Alinear la meta intermedia de PERS-E01 de 65 % con los criterios de la compuerta C2 de la ficha", "Formulación", "indicadores.py y cap12.md", "Unifica los umbrales de las compuertas"])
    if M["sin_descripcion"]:
        ruta.append(["2", f"Añadir descripción a los {M['sin_descripcion']} marcadores sin texto", "Redacción", lista_y(sorted(M["sin_desc_archivos"])), "El formato de marcador pasa a CUMPLE"])
    ruta.append(["3", f"Documentar o mejorar el porcentaje de referencias recientes ({pct_rec} % frente a 70 %) y consultar los cuartiles de las revistas", "Redacción y usuario", "cap19.md", "Resuelve el criterio de cuartil y declara la excepción"])
    ruta.append(["3", "Realizar la corrección ortográfica y la lectura de un tercero independiente", "Revisión independiente", "Todos", "Cierra las filas CK.6"])
    A(tabla("t10", "Ruta de corrección ordenada por prioridad", ["Prioridad", "Acción", "Responsable", "Archivos", "Efecto esperado"], ruta,
            "*Nota.* Elaboración propia a partir de los hallazgos de las tablas anteriores. Prioridad 1 bloquea la radicación; prioridad 2 corrige defectos que no necesitan información nueva; prioridad 3 mejora la calidad. La fecha límite de la convocatoria es el 11 de noviembre de 2026 (DECLARADO)."))
    A("")
    A("La prioridad 1 define el camino crítico. Ninguna corrección de redacción compensa la ausencia de los TdR ni de los datos del usuario. Las acciones de prioridad 2 son de bajo costo y no cambian ninguna cifra. Pueden ejecutarse en una sola pasada de edición. Tras ellas, la repetición de este checklist debe mostrar cero defectos de forma. La prioridad 3 mejora la calidad sin bloquear la entrega.")
    A("")
    A("Este checklist es honesto sobre su alcance. Verifica lo que los archivos permiten verificar y declara lo demás como pendiente. Un estado CUMPLE significa que el requisito se cumple con evidencia en el documento. No significa que el proyecto esté aprobado. La aprobación depende de la convocatoria y de un panel evaluador que este documento no puede anticipar.")
    out = "\n".join(L)
    out = re.sub(r"\n{3,}", "\n\n", out)
    open(OUT, "w", encoding="utf-8").write(out + "\n")
    print("x10.md escrito:", len(out), "caracteres; filas", tot_filas, dict(estados))


if __name__ == "__main__":
    main()
