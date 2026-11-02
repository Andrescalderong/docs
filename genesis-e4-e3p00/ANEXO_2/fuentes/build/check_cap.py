# -*- coding: utf-8 -*-
"""Comprobación mecánica de un archivo de capítulo (md). Uso: python3 check_cap.py caps/cap05.md [--minpal N --mintab N --minfig N --minref N]
Verifica: palabras de prosa, tablas y figuras, orden de mención, citas frente al banco, oraciones > 25 palabras, palabras prohibidas,
marcadores de omisión, párrafos sin punto final, placeholders no permitidos, 'Pero' inicial, rayas de énfasis, barras inclusivas."""
import re, sys, json, os, argparse, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCO = json.load(open(os.path.join(ROOT, "refs", "banco.json"), encoding="utf-8"))

ENF = ["abrumador", "dominante", "sin precedentes", "extraordinari", "revolucionari", "disruptiv", "masivo", "monumental", "explosiv",
       "titiritero", "violentamente", "drástic", "enorme", "crucial", "inédit", "holístic", "garantiza", "garantizando", "demuestra matemáticamente",
       "ampliamente reconocid", "crecimiento exponencial", "cabe destacar", "es importante mencionar", "juega un papel", "en el mundo actual",
       "hoy en día", "sin lugar a dudas", "paradigma", "sinergia", "robusto ", "robusta ", "óptimo ", "impecable", "indiscutible", "incuestionable"]
OMIT = [r"\betc\.", r"entre otros", r"y así sucesivamente", r"\[continuar", r"se omite", r"\.\.\.", r"…", r"\bTBD\b", r"\bXXX\b"]
SIGLAS_CITA = {"OMS": "WHO2021", "EPA": "EPA2021", "SIC": "SIC2026", "UNDRR": "UNISDR2015", "ONU": "ONU2015", "OCDE": "OCDE2018", "DNP": None, "PMI": "PMI2021", "ISO": "ISO31000"}

def norm(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s.lower())
    return re.sub(r"[^a-z0-9 ]", "", "".join(c for c in s if not unicodedata.combining(c))).strip()

CITAS = collections.defaultdict(set)   # año -> {cite normalizada}
for r in BANCO:
    base = re.sub(r"\s*\[[^\]]*\]", "", r["cite"])
    CITAS[str(r["year"])].add(norm(base))
    m = re.search(r"\[([^\]]+)\]", r["cite"])
    if m: CITAS[str(r["year"])].add(norm(m.group(1)))
    CITAS[str(r["year"])].add(norm(base.split(" y ")[0]) + " et al")  # tolerancia

def split_directives(text):
    """Devuelve (prosa, tablas, figuras, notas, ids_tabla, ids_fig, orden) separando directivas y bloques."""
    lines = text.split("\n"); prose = []; tabs = []; figs = []; order = []
    i = 0
    while i < len(lines):
        l = lines[i]
        m = re.match(r"^:::TABLA\s+(\S+)\s*\|\s*(.+)$", l)
        if m:
            tabs.append((m.group(1), m.group(2).strip())); order.append(("T", m.group(1), len(prose)))
            i += 1
            while i < len(lines) and lines[i].startswith("|"): i += 1
            continue
        m = re.match(r"^:::FIGURA\s+(\S+)\s*\|\s*([^|]+)\|?(.*)$", l)
        if m:
            figs.append((m.group(1), m.group(2).strip(), m.group(3).strip())); order.append(("F", m.group(1), len(prose))); i += 1; continue
        if l.startswith(":::NOTA"): i += 1; continue
        prose.append(l); i += 1
    return prose, tabs, figs, order

def citas_texto(t):
    out = []
    for g in re.findall(r"\(([^()]*?\d{4}[a-z]?[^()]*?)\)", t):
        for part in g.split(";"):
            m = re.match(r"\s*(?:véase |ver |p\. ej\., |como se citó en )?(.+?),\s*(\d{4})[a-z]?", part.strip())
            if m: out.append((m.group(1).strip(), m.group(2)))
    for m in re.finditer(r"([A-ZÁÉÍÓÚÑ][\w\-ÁÉÍÓÚáéíóúñü]+(?: (?:y|de|del|la|van|von) [A-ZÁÉÍÓÚÑa-z][\w\-ÁÉÍÓÚáéíóúñü]+)*(?: et al\.)?) \((\d{4})[a-z]?[,)]", t):
        out.append((m.group(1).strip(), m.group(2)))
    return out

def validar_cita(autor, año):
    autor = re.sub(r"\s*\[[^\]]*\]", "", autor)
    a = norm(re.sub(r"\bet al\.?", "et al", autor))
    a = re.sub(r"^(de|del|la|van|von) ", "", a) if a.split(" ")[0] in ("de", "del", "la", "van", "von") and a not in CITAS.get(año, set()) else a
    pos = CITAS.get(año, set())
    if a.startswith("matriz de "): a = a[10:]
    if a in pos: return True
    if len(a.split()) >= 2 and any(p.endswith(" " + a) or p.endswith(a) for p in pos if len(p) > len(a)): return True
    if a.replace(" et al", "") in {p.replace(" et al", "") for p in pos}: return True
    # sigla
    return any(a == p for p in pos)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivo"); ap.add_argument("--minpal", type=int, default=0); ap.add_argument("--mintab", type=int, default=0)
    ap.add_argument("--minfig", type=int, default=0); ap.add_argument("--minref", type=int, default=0)
    ap.add_argument("--maxw", type=int, default=25); ap.add_argument("-v", action="store_true")
    a = ap.parse_args()
    raw = open(a.archivo, encoding="utf-8").read()
    prose, tabs, figs, order = split_directives(raw)
    problems = []
    # ---- prosa
    body = []; fence = False
    for ln, l in enumerate(prose, 1):
        s = l.strip()
        if s.startswith("```"): fence = not fence; continue
        if fence or not s or s.startswith("#") or s.startswith("|") or s.startswith("<!--") or s.startswith("%%") or "**Nombre del proyecto:**" in s or s.startswith("El objetivo general es el siguiente:") or s.startswith("- **Objetivo específico") or s.startswith("- **Valor total"): continue
        body.append((ln, s))
    texto = "\n".join(s for _, s in body)
    plain = re.sub(r"\{[TF]:[^}]+\}", "Tabla 0.0", texto)
    plain = re.sub(r"\*+", "", plain)
    palabras = len(re.findall(r"[\wÁÉÍÓÚÜÑáéíóúüñ%]+(?:[.,\-/][\wÁÉÍÓÚÜÑáéíóúüñ]+)*", plain))
    # ---- oraciones largas
    largas = []; sin_punto = []; sin_corta = 0; parrs = 0
    for ln, s in body:
        if re.match(r"^([-*]|\d+\.)\s", s): item = True
        else: item = False
        t = re.sub(r"^([-*]|\d+\.)\s+", "", s)
        t = re.sub(r"\*+|\{[TF]:[^}]+\}", "", t)
        if not item and not re.search(r"[.?!:)\]»]$", t) and len(t.split()) > 6: sin_punto.append((ln, t[-60:]))
        sents = re.split(r"(?<=[.!?;:])\s+(?=[A-ZÁÉÍÓÚÑ¿¡(«\[])", t)
        if item: sents = [x for s2 in sents for x in re.split(r";\s+", s2)]
        parrs += 0 if item else 1
        for sent in sents:
            n = len(re.findall(r"[\wÁÉÍÓÚÜÑáéíóúüñ%/.,:\-→]+", re.sub(r"\([^()]*\d{4}[^()]*\)", "", sent)))
            if n > a.maxw: largas.append((ln, n, sent[:500]))
    # ---- prohibidas
    low = texto.lower(); enf = {w: low.count(w) for w in ENF if w in low}
    omit = {p: len(re.findall(p, texto)) for p in OMIT if re.search(p, texto)}
    pero = [(ln, s[:60]) for ln, s in body if re.match(r"^(Pero)\b", s)]
    rayas = [(ln, s[:70]) for ln, s in body if re.search(r"\s—[^—]+—\s|\s-\s[^-]{3,}\s-\s", s)]
    barras = re.findall(r"\b\w+/\w?a\b|\b(?:los|las|todos|todas)/(?:las|los|as|os)\b|@", texto)
    pict = re.findall(r"[✓✗✔✘✅❌⚠️🔴🟡🟢]", raw)
    ph = [m for m in re.findall(r"\[([^\]]{3,80})\]", texto) if not m.startswith(("DATO_USUARIO", "Diligenciar")) and not re.match(r"[A-Z]{2,}", m) and not re.fullmatch(r"\w{2,20}", m) and "http" not in m and not re.match(r"[\d,.\s]+$", m)]
    # ---- numeración y menciones
    ids_t = [t[0] for t in tabs]; ids_f = [f[0] for f in figs]
    men_t = [(m.start(), m.group(1)) for m in re.finditer(r"\{T:([^}]+)\}", texto)]
    men_f = [(m.start(), m.group(1)) for m in re.finditer(r"\{F:([^}]+)\}", texto)]
    sin_mencion = [i for i in ids_t if i not in {x[1] for x in men_t}] + [i for i in ids_f if i not in {x[1] for x in men_f}]
    inexist = [x[1] for x in men_t if x[1] not in ids_t] + [x[1] for x in men_f if x[1] not in ids_f]
    # menciones previas a la aparición: ubicación del primer {T:id} frente a la directiva (por línea de prosa acumulada)
    tarde = []
    pos_prose = {}
    acc = 0
    for kind, id_, nprose in order: pos_prose[(kind, id_)] = nprose
    # línea de la primera mención
    primera = {}
    for ln, s in body:
        for m in re.finditer(r"\{([TF]):([^}]+)\}", s): primera.setdefault((m.group(1), m.group(2)), ln)
    for key, idx in pos_prose.items():
        pm = primera.get(key)
        if pm is None: continue
        if pm > idx + 1: tarde.append(key)
    # ---- citas
    cit = citas_texto(texto)
    desconocidas = sorted({f"{au} ({y})" for au, y in cit if not validar_cita(au, y)})
    usadas = {f"{norm(au)}|{y}" for au, y in cit}
    # ---- figuras: existen archivos?
    pref = None
    mpref = re.search(r"^%% PREFIJO:\s*(\S+)", raw, re.M)
    pref = mpref.group(1) if mpref else "X"
    faltan_fig = []
    for i in ids_f:
        pth = os.path.join(ROOT, "figs", "out", f"c{pref}_{i}.png")
        if not os.path.exists(pth): faltan_fig.append(f"c{pref}_{i}.png")
    # ---- salida
    print(f"ARCHIVO {a.archivo}  PREFIJO {pref}")
    print(f"palabras de prosa: {palabras} (mín {a.minpal})  tablas: {len(tabs)} (mín {a.mintab})  figuras: {len(figs)} (mín {a.minfig})  citas distintas: {len(usadas)} (mín {a.minref})")
    if a.minpal and palabras < a.minpal: problems.append(f"PALABRAS {palabras} < {a.minpal}")
    if a.mintab and len(tabs) < a.mintab: problems.append(f"TABLAS {len(tabs)} < {a.mintab}")
    if a.minfig and len(figs) < a.minfig: problems.append(f"FIGURAS {len(figs)} < {a.minfig}")
    if a.minref and len(usadas) < a.minref: problems.append(f"CITAS DISTINTAS {len(usadas)} < {a.minref}")
    dens = (len(cit) / (palabras / 150)) if palabras else 0
    print(f"densidad de citación: {dens:.2f} citas por cada 150 palabras (meta ≥ 1,0 en capítulos narrativos)")
    for name, val in (("oraciones > %d palabras" % a.maxw, largas), ("párrafos sin punto final", sin_punto), ("'Pero' inicial", pero), ("rayas de énfasis", rayas)):
        print(f"{name}: {len(val)}")
        if val: problems.append(f"{name}: {len(val)}")
        if a.v:
            for v in val[:8]: print("   ", v)
    for name, val in (("palabras prohibidas o enfáticas", enf), ("marcadores de omisión", omit), ("barras o arrobas inclusivas", barras),
                      ("símbolos pictográficos", pict), ("marcadores [..] no permitidos", ph), ("tablas/figuras sin mención", sin_mencion),
                      ("menciones sin objeto", inexist), ("objeto mencionado tras su aparición", tarde), ("citas fuera del banco", desconocidas),
                      ("figuras sin archivo", faltan_fig)):
        print(f"{name}: {val if val else 0}")
        if val: problems.append(f"{name}: {val}")
    print("RESULTADO:", "SIN PROBLEMAS" if not problems else f"{len(problems)} problema(s)")
    if a.v and largas:
        print("oraciones largas (primeras 12):")
        for l in largas[:60]: print("   ", l)
    return 0 if not problems else 1

if __name__ == "__main__":
    sys.exit(main())
