# -*- coding: utf-8 -*-
"""Recolecta los conteos reales del paquete (ejecuta check_cap.py) y los escaneos de coherencia. Salida: dict D (JSON en a14/datos.json)."""
import subprocess, re, json, glob, os, sys, ast, collections, importlib.util

RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
CAPS = RAIZ + "/caps/"
CC = RAIZ + "/build/check_cap.py"
TMP = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/a14/"

spec = importlib.util.spec_from_file_location("cc", CC)
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

PROB_NAMES = ["oraciones > 25 palabras", "párrafos sin punto final", "'Pero' inicial", "rayas de énfasis", "palabras prohibidas o enfáticas",
              "marcadores de omisión", "barras o arrobas inclusivas", "símbolos pictográficos", "marcadores [..] no permitidos",
              "tablas/figuras sin mención", "menciones sin objeto", "objeto mencionado tras su aparición", "citas fuera del banco", "figuras sin archivo"]


def exists(f):
    return os.path.exists(CAPS + f)


def correr(path, minpal=0, mintab=0, minfig=0, minref=0):
    cmd = ["python3", "-I", CC, path, "-v", "--minpal", str(minpal), "--mintab", str(mintab), "--minfig", str(minfig), "--minref", str(minref)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout
    d = {}
    m = re.search(r"palabras de prosa: (\d+).*?tablas: (\d+).*?figuras: (\d+).*?citas distintas: (\d+)", out)
    d["pal"], d["tab"], d["fig"], d["cit"] = [int(x) for x in m.groups()]
    d["dens"] = float(re.search(r"densidad de citación: ([\d.]+)", out).group(1))
    probs = {}
    for line in out.split("\n"):
        for name in PROB_NAMES:
            if line.startswith(name + ":"):
                val = line[len(name) + 1:].strip()
                if val != "0":
                    probs[name] = val
    d["probs"] = probs
    d["resultado"] = re.search(r"RESULTADO: (.*)", out).group(1).strip()
    d["salida"] = out
    return d


def cuenta(val):
    """Número de elementos de un valor de problema (entero, lista o dict en texto)."""
    try:
        v = ast.literal_eval(val)
    except Exception:
        return 1
    if isinstance(v, (list, dict, tuple)):
        return len(v)
    return int(v)


def citas_totales(files):
    n = 0
    for f in files:
        raw = open(CAPS + f, encoding="utf-8").read()
        prose, tabs, figs, order = cc.split_directives(raw)
        body = []; fence = False
        for l in prose:
            s = l.strip()
            if s.startswith("```"): fence = not fence; continue
            if fence or not s or s.startswith("#") or s.startswith("|") or s.startswith("<!--") or s.startswith("%%"): continue
            body.append(s)
        n += len(cc.citas_texto("\n".join(body)))
    return n


def titulo(f):
    for l in open(CAPS + f, encoding="utf-8"):
        if l.startswith("# "):
            return l[2:].strip()
    return ""


# ------------------------------------------------------------------ definición del plan
CAP_DEF = [
    (1, ["cap01.md"], 5000, 5, 3, 15), (2, ["cap02a.md", "cap02b.md"], 12000, 21, 13, 40), (3, ["cap03.md"], 1500, 3, 2, 5),
    (4, ["cap04.md"], 8000, 4, 3, 20), (5, ["cap05.md"], 5000, 7, 3, 15), (6, ["cap06.md"], 8000, 6, 4, 15),
    (7, ["cap07.md"], 2000, 3, 2, 3), (8, ["cap08.md"], 2500, 8, 3, 0), (9, ["cap09.md"], 1500, 3, 2, 0),
    (10, ["cap10.md"], 2000, 5, 3, 5), (11, ["cap11.md"], 2000, 4, 2, 0), (12, ["cap12.md"], 3500, 18, 5, 0),
    (13, ["cap13.md"], 4000, 8, 5, 0), (14, ["cap14.md"], 3500, 4, 2, 0), (15, ["cap15.md"], 3500, 3, 2, 0),
    (16, ["cap16.md"], 3500, 6, 4, 0), (17, ["cap17.md"], 2000, 4, 2, 3), (18, ["cap18.md"], 1500, 2, 1, 3),
    (19, ["cap19.md"], 0, 1, 0, 0), (20, ["cap20.md"], 1800, 6, 0, 0), (21, ["cap21.md"], 2500, 6, 2, 0),
]
NARRATIVOS = {1: 30, 2: 60, 4: 50, 5: 30, 6: 40, 13: 20, 14: 18, 15: 18, 16: 18}   # PD-03: citas mínimas
X_DEF = [
    ("1000X-01", "Resumen ejecutivo", "x01.md", 800, 1, 0, "800 a 1.000 palabras"),
    ("1000X-02", "One-pager", "x02.md", 400, 1, 1, "400 a 500 palabras"),
    ("1000X-03", "Pitch deck", "x03.md", 1500, 2, 1, "15 diapositivas; 1.500 palabras"),
    ("1000X-04", "Capítulo de estrategia", "estrategia.md", 8000, 15, 8, "8.000 palabras; 12 citas distintas"),
    ("1000X-05", "Modelo de negocio", "x05.md", 500, 2, 1, "500 palabras"),
    ("1000X-06", "Análisis financiero", "x06.md", 1500, 6, 3, "1.500 palabras"),
    ("1000X-07", "Roadmap tecnológico", "x07.md", 500, 2, 1, "500 palabras"),
    ("1000X-08", "Mapa de interesados", "x08.md", 800, 3, 1, "800 palabras"),
    ("1000X-09", "Tablero de riesgos", "x09.md", 0, 3, 3, "tablas de soporte"),
    ("1000X-10", "Checklist de cumplimiento", "x10.md", 800, 4, 0, "800 palabras"),
]
PASOS = ["paso0.md", "paso1.md", "paso2.md", "paso3.md", "paso4.md", "paso5.md", "paso6.md", "paso7.md"]


def recolectar():
    D = {"capitulos": {}, "x": {}, "pasos": {}, "otros": {}}
    # capítulos
    for n, files, mp, mt, mf, mr in CAP_DEF:
        ex = [f for f in files if exists(f)]
        e = {"n": n, "files": files, "existentes": ex, "mins": [mp, mt, mf, mr]}
        if not ex:
            e["falta"] = True
            D["capitulos"][n] = e
            continue
        if len(files) == 1:
            r = correr(CAPS + files[0], mp, mt, mf, mr)
            e.update({k: r[k] for k in ("pal", "tab", "fig", "cit", "dens", "probs", "resultado")})
            e["probs_por_archivo"] = {files[0]: r["probs"]}
            e["titulo"] = titulo(files[0])
        else:
            rs = {f: correr(CAPS + f) for f in ex}
            pal = sum(r["pal"] for r in rs.values()); tab = sum(r["tab"] for r in rs.values()); fig = sum(r["fig"] for r in rs.values())
            tmp = TMP + "tmp_cap02.md"
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write("%% PREFIJO: 2\n")
                for f in ex:
                    fh.write(open(CAPS + f, encoding="utf-8").read().replace("%% PREFIJO: 2", "") + "\n\n")
            rc = correr(tmp)
            e.update({"pal": pal, "tab": tab, "fig": fig, "cit": rc["cit"], "dens": rc["dens"], "titulo": titulo(files[0])})
            probs = collections.Counter()
            for f, r in rs.items():
                for k, v in r["probs"].items():
                    probs[k] += cuenta(v)
            e["probs"] = {k: str(v) for k, v in probs.items()}
            e["probs_por_archivo"] = {f: r["probs"] for f, r in rs.items()}
            e["resultado"] = "SIN PROBLEMAS" if not probs else f"{len(probs)} problema(s)"
        e["cit_total"] = citas_totales(ex)
        D["capitulos"][n] = e
    # cap19: obras en la lista
    if exists("cap19.md"):
        t = open(CAPS + "cap19.md", encoding="utf-8").read()
        D["otros"]["refs_cap19"] = len(re.findall(r'custom-style="Referencia"', t))
        m = re.search(r"De las (\d+) obras, (\d+) \(([\d,]+) %\) se publicaron entre 2021 y 2026", t)
        if m:
            D["otros"]["refs_recientes"] = int(m.group(2)); D["otros"]["pct_recientes"] = m.group(3)
        m = re.search(r"\| Verificación \| NO_VERIFICADO \| (\d+) \| ([\d,]+) \|", t)
        if m: D["otros"]["refs_noverif"] = int(m.group(1))
        m = re.search(r"\| Verificación \| VERIFICADO \| (\d+) \| ([\d,]+) \|", t)
        if m: D["otros"]["refs_verif"] = int(m.group(1))
        m = re.search(r"\| Verificación \| PARCIALMENTE_VERIFICADO \| (\d+) \| ([\d,]+) \|", t)
        if m: D["otros"]["refs_parc"] = int(m.group(1))
    # anexos K a M
    if exists("anexos_km.md"):
        r = correr(CAPS + "anexos_km.md"); D["otros"]["anexos_km"] = {k: r[k] for k in ("pal", "tab", "fig", "cit", "probs", "resultado")}
    # paquete X
    for cod, nombre, f, mp, mt, mf, ext in X_DEF:
        if not exists(f):
            D["x"][cod] = {"falta": True, "file": f, "mins": [mp, mt, mf]}
            continue
        mr = 12 if f == "estrategia.md" else 0
        r = correr(CAPS + f, mp, mt, mf, mr)
        D["x"][cod] = {"file": f, "mins": [mp, mt, mf], "pal": r["pal"], "tab": r["tab"], "fig": r["fig"], "cit": r["cit"], "dens": r["dens"], "probs": r["probs"], "resultado": r["resultado"]}
    # pasos
    for f in PASOS:
        if not exists(f):
            D["pasos"][f] = {"falta": True}
            continue
        r = correr(CAPS + f)
        D["pasos"][f] = {"pal": r["pal"], "tab": r["tab"], "fig": r["fig"], "probs": r["probs"], "resultado": r["resultado"]}
    # otros archivos de ensamblado
    for f in ["front.md", "div_parte1.md", "div_parte2.md", "div_parte3.md", "div_cierre.md", "cierre.md"]:
        D["otros"][f] = exists(f)
    return D


# ------------------------------------------------------------------ escaneos de contenido
def leer_todo():
    txt = {}
    for f in sorted(glob.glob(CAPS + "*.md")):
        b = os.path.basename(f)
        if b in ("ejemplo.md",):
            continue
        txt[b] = open(f, encoding="utf-8").read()
    return txt


def marcadores(txt):
    desc = collections.defaultdict(set); orig = {}; ocur = 0; vacios = collections.Counter(); porarch = collections.Counter(); distarch = collections.defaultdict(set)
    for f, t in txt.items():
        if f in ("front.md",):
            continue
        for m in re.finditer(r"\[DATO_USUARIO(?::\s*([^\]]*))?\]", t):
            d = (m.group(1) or "").strip()
            ocur += 1; porarch[f] += 1
            if not d:
                vacios[f] += 1
            else:
                desc[d.lower()].add(f); distarch[f].add(d.lower()); orig.setdefault(d.lower(), d)
    return {"ocurrencias": ocur, "distintos": len(desc), "sin_descripcion": sum(vacios.values()), "sin_desc_archivos": dict(vacios),
            "desc": {k: sorted(v) for k, v in desc.items()}, "orig": orig, "porarch": dict(porarch), "distarch": {k: len(v) for k, v in distarch.items()}}


CATS = [
    ("Términos de referencia y requisitos de la convocatoria", r"términos de referencia|\btdr\b|convocatoria|rubros admisibles|requisitos? de|porcentaje exigido|nivel mínimo|extensión y formato|clasificación de revistas|periodicidad|calendario|tasa social|enfoque diferencial|código de radicación|código de tipología|reasignación|elegibilidad|reglas de titularidad|código id"),
    ("Articulación con planes y políticas (PDD, PIIOM, ODS, PND, MGA)", r"\bpdd\b|piiom|\bods\b|plan nacional|planes (?:de desarrollo|vigentes)|demanda|\bmga\b|sigp|misión|vocación|transformación|objetivo y|línea de acción|\beje\b|artículos? (?:aplicables|y códigos|o eje)|indicadores? (?:y meta|del plan|, línea base)|indicador y meta|foco y recomendación|líneas de política|acciones del documento|tipología mmg|^código$|^indicador"),
    ("Datos económicos y de financiación", r"cotizacion|costos? de|monto|financiación|plazo de adquisición|^proporción$|porcentaje máximo"),
    ("Datos técnicos, bibliométricos y de medición", r"gateway|distancia máxima|aqhi|viento|validación de laboratorio|inventario de equipos|evidencia|pilotos|resultados por base|scopus|cuartiles?|especificación del monitor|capacidad de procesamiento"),
    ("Documentos y compromisos jurídicos", r"carta|\bacta\b|acto o|acuerdo|convenio|reglamento|comité de ética|\baval\b|certificad|tratamiento de datos|gestor autorizado|ordenanza|instrumento"),
    ("Territorio, población y sitios de remoción", r"municipio|polígono|operarios|habitantes|población|organizaciones comunitarias|caracterización|\bsitios?\b|toneladas|rango|censo|dane|volumen removido|asistentes|horas por comité|comités (?:del tramo|para la prueba)|fecha del evento|número en"),
    ("Nombres de entidades, aliados y razón social", r"razón social|\bnit\b|nombre de la (?:ies|empresa|entidad)|nombres? de (?:los )?aliados|nombres de las (?:entidades|alcaldías)|nombres de los (?:comités|interesados)|nombres de la entidad|entidades|proveedores|laboratorios|evaluador|nombre y organización|nombre de la persona o|logotipo|titular de la marca|dependencia y contacto|nombre del equipo formulador|custodio|nombres y roles de la entidad|panel|número y organizaciones|nombre del comité"),
    ("Personas, perfiles y grupos de investigación", r"hojas? de vida|\bnombres?\b|nombres? del|nombres por rol|nombre del investigador|nombre de la persona|nombre y cargo|nombre y hoja|grupo|grupl|categoría|líneas de investigación|programas? de|modalidad de joven|jornada laboral|credenciales|proyecto similar|proyectos propios|certificaciones de proyectos|personas designadas|composición del comité"),
    ("Fechas, firmas, contacto y presentación", r"fecha|firma|autorización|contacto|\bqr\b|fotograf|colores|responsable|decisión|reglas"),
]


def categorizar(desc):
    out = collections.OrderedDict()
    for d in sorted(desc):
        for nombre, pat in CATS:
            if re.search(pat, d):
                out.setdefault(nombre, []).append(d); break
        else:
            out.setdefault("Otros datos del usuario", []).append(d)
    return out


def refs_check(txt):
    banco = json.load(open(RAIZ + "/refs/banco.json", encoding="utf-8"))
    cap19 = txt.get("cap19.md", "").replace("*", "")
    body = " ".join(t for f, t in txt.items() if f not in ("cap19.md", "front.md"))
    def names(cite):
        base = re.sub(r"\s*\[[^\]]*\]", "", cite).strip()
        m = re.search(r"\[([^\]]+)\]", cite)
        return [base] + ([m.group(1)] if m else [])
    def cited(r):
        ns = "|".join(re.escape(n) for n in names(r["cite"]))
        return re.search(rf"(?:{ns})(?: et al\.)?,? \(?{r['year']}[a-z]?", body) is not None
    def listed(r):
        a = r["apa"].replace("*", ""); i = a.find(").")
        tail = a[i + 2:i + 42].strip() if i > 0 else a[:45]
        return tail in cap19 and a[:25] in cap19
    c = {r["key"] for r in banco if cited(r)}; l = {r["key"] for r in banco if listed(r)}
    return {"banco": len(banco), "citadas": len(c), "listadas": len(l), "citadas_no_listadas": sorted(c - l), "listadas_no_citadas": sorted(l - c)}


def escanear(txt):
    S = {}
    def contar(pat, flags=0):
        c = collections.Counter()
        for f, t in txt.items():
            for m in re.finditer(pat, t, flags): c[f] += 1
        return c
    SGR = contar(r"9\.267\.260\.000"); CON = contar(r"2\.110\.000\.000"); TOT = contar(r"11\.377\.260\.000")
    S["sgr_exacto"] = sum(SGR.values()); S["contra_exacto"] = sum(CON.values()); S["total_exacto"] = sum(TOT.values())
    S["sgr_otros"] = [f"{m.group(0)}" for t in txt.values() for m in re.finditer(r"\$ ?9\.\d{3}\.\d{3}\.\d{3}", t) if m.group(0).replace("$ ", "").replace("$", "") != "9.267.260.000"]
    S["trl8_condicionado"] = True
    # TRL 8 sin condicionamiento cercano
    malos = []
    for f, t in txt.items():
        for m in re.finditer(r"TRL 8", t):
            ctx = t[max(0, m.start() - 140): m.end() + 160].lower()
            if not re.search(r"condicion|declar|exige|requiere|no cubre|sin calificaci|calificad|queda|fija el trl 7|fija trl 7|por la decisi|se fija|expediente|e3|dec-f05|punto de partida|rival|conserva", ctx):
                malos.append(f)
    S["trl8_sin_condicion"] = malos
    S["decimal_punto"] = []
    for f, t in txt.items():
        if f in ("cap19.md", "anexos_km.md", "front.md"):
            continue
        for m in re.finditer(r"(?<![\w.,/#-])(\d{1,3})\.(\d{1,2}|\d{4,}) ?%|(?<![\w.,/#-])0\.\d{3,}", t):
            S["decimal_punto"].append((f, m.group(0)))
    # rubros SGR en cap08, x06, x03
    rub = ["4.552,8", "1.885,6", "242,9", "896,0", "462,0", "592,0", "636,0"]
    S["rubros_cap08"] = [r for r in rub if r in txt.get("cap08.md", "")]
    S["rubros_x06"] = [r for r in rub if r in txt.get("x06.md", "")]
    S["rubros_x03"] = [r for r in rub if r in txt.get("x03.md", "")]
    # R² y NRMSE
    S["r2_umbrales"] = collections.Counter(m.group(1) for t in txt.values() for m in re.finditer(r"R² (?:≥|de al menos|de) (0,\d+)", t))
    S["nrmse_umbrales"] = collections.Counter(m.group(1) for t in txt.values() for m in re.finditer(r"NRMSE (?:≤|de|máximo de) (\d+) ?%", t))
    S["ev_salud"] = sum(len(re.findall(r"reducirá (?:la )?mortalidad|reduce (?:la )?mortalidad|evitar[áa]n muertes|salvar[áa]n vidas|disminuirá las enfermedades", t)) for t in txt.values())
    S["etc"] = sum(len(re.findall(r"\betc\.|entre otros|y así sucesivamente", t)) for t in txt.values())
    S["verificado_solo"] = sum(len(re.findall(r"(?<![A-Z_])VERIFICADO\b", t)) for f, t in txt.items() if f != "cap19.md")
    S["e65"] = "≥ 65 %" in txt.get("cap12.md", "")
    S["paso6_escalabilidad"] = "supera a ALT-02 en impacto, escalabilidad, innovación y fiabilidad ubicua" in txt.get("paso6.md", "")
    S["cap02b_desactualizado"] = "archivo de las secciones 2.1 a 2.3 estaba incompleto" in txt.get("cap02b.md", "")
    S["feynman"] = sum(len(re.findall(r"Feynman|Brecha No Resuelta|COMPROMISO D[ÉE]BIL", t)) for t in txt.values())
    # encabezados
    h1 = {}
    saltos = []
    for f, t in txt.items():
        if f in ("front.md",) or f.startswith("div_"):
            continue
        niveles = [len(m.group(1)) for m in re.finditer(r"^(#{1,6}) ", t, re.M)]
        h1[f] = sum(1 for n in niveles if n == 1)
        prev = 0
        for n in niveles:
            if prev and n > prev + 1:
                saltos.append(f); break
            prev = n
    S["h1"] = h1; S["saltos"] = saltos
    pref = collections.defaultdict(list)
    for f, tx in txt.items():
        m = re.match(r"%% PREFIJO:\s*(\S+)", tx)
        if m: pref[m.group(1)].append(f)
    S["prefijos"] = dict(pref)
    S["sin_prefijo"] = [f for f, tx in txt.items() if not f.startswith(("front", "div_")) and not tx.startswith("%% PREFIJO")]
    S["refs"] = refs_check(txt)
    return S


if __name__ == "__main__":
    D = recolectar()
    txt = leer_todo()
    D["marcadores"] = marcadores(txt)
    D["escaneo"] = escanear(txt)
    for k in ("salida",):
        pass
    json.dump(D, open(TMP + "datos.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    print("ok", len(D["capitulos"]), len(D["x"]))
