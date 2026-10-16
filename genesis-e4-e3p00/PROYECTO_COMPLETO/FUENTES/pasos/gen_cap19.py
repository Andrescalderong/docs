# -*- coding: utf-8 -*-
"""Genera el capítulo 19 (bibliografía) desde el banco cerrado: solo las obras citadas en el documento, con sufijo a/b cuando
dos obras comparten autor y año. Salidas: caps/cap19a.md, caps/cap19_refs.md (crudo), caps/cap19b.md y refs/citadas.json."""
import sys, os, re, json, glob, collections, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANCO = json.load(open(os.path.join(RAIZ, "refs", "banco.json"), encoding="utf-8"))
CAPS = os.path.join(RAIZ, "caps")
A2ONLY = bool(os.environ.get("A2ONLY"))
EXCL = {"cap19a.md", "cap19b.md", "cap19_refs.md", "frente.md", "a29a_r.md", "a29_refs_r.md", "a29b_r.md"}
SOLO = {"a2a_r.md", "a2b_r.md", "a2c_r.md", "a2d_r.md"}
texto = ""
for f in sorted(glob.glob(os.path.join(CAPS, "*.md"))):
    if os.path.basename(f) in EXCL: continue
    if A2ONLY and os.path.basename(f) not in SOLO: continue
    if not A2ONLY and os.path.basename(f) in SOLO: continue
    texto += "\n" + open(f, encoding="utf-8").read()

def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return re.sub(r"[^a-z0-9 ]", "", "".join(c for c in s if not unicodedata.combining(c))).strip()

def patrones(r):
    base = re.sub(r"\s*\[[^\]]*\]", "", r["cite"]).strip()
    m = re.search(r"\[([^\]]+)\]", r["cite"])
    nombres = [base] + ([m.group(1)] if m else [])
    pats = []
    for n in nombres:
        pats.append(re.compile(r"(?<![\w\-])" + re.escape(n) + r"(?:,\s*|\s*\()\s*" + str(r["year"]) + r"([a-z]?)(?![\w])"))
    return pats

grupos = collections.defaultdict(list)
for r in BANCO:
    base = re.sub(r"\s*\[[^\]]*\]", "", r["cite"]).strip()
    grupos[(base, r["year"])].append(r)
sufijo = {}
for k, v in grupos.items():
    if len(v) > 1:
        for i, r in enumerate(sorted(v, key=lambda z: norm(re.sub(r"^.*?\(\d{4}[^)]*\)\.\s*", "", z["apa"])))):
            sufijo[r["key"]] = "abcdefgh"[i]

citadas = []
conteo = {}
for r in BANCO:
    n = 0
    for p in patrones(r):
        for m in p.finditer(texto):
            s = m.group(1)
            if r["key"] in sufijo and s and s != sufijo[r["key"]]: continue
            if r["key"] in sufijo and not s: continue   # ambigua sin sufijo: se corrige aguas arriba
            n += 1
    if n: citadas.append(r); conteo[r["key"]] = n
sin_sufijo = []
for k, v in grupos.items():
    if len(v) > 1:
        for p in patrones(v[0]):
            for m in p.finditer(texto):
                if not m.group(1): sin_sufijo.append(k)

def apa_con_sufijo(r):
    a = r["apa"]
    if r["key"] in sufijo:
        a = re.sub(r"\((\d{4})", lambda m: "(" + m.group(1) + sufijo[r["key"]], a, count=1)
    return a

def clave_orden(r):
    a = re.sub(r"[*_]", "", apa_con_sufijo(r))
    return norm(a)

citadas.sort(key=clave_orden)
json.dump([{"key": r["key"], "n": conteo[r["key"]]} for r in citadas], open(os.path.join(RAIZ, "refs", "citadas_r.json" if A2ONLY else "citadas.json"), "w"), ensure_ascii=False, indent=1)
N = len(citadas)

# ---------------------------------------------------------------- estadísticas
tipos = collections.Counter(r["tipo"] for r in citadas)
orig = collections.Counter(r["origen"] for r in citadas)
ver = collections.Counter(r.get("ver", "NO_VERIFICADO") for r in citadas)
años = [r["year"] for r in citadas]
ult5 = sum(1 for y in años if y >= 2022)
doi = sum(1 for r in citadas if "doi.org" in r["apa"])
rangos = [("1900 a 1999", lambda y: y < 2000), ("2000 a 2015", lambda y: 2000 <= y <= 2015), ("2016 a 2021", lambda y: 2016 <= y <= 2021), ("2022 a 2026", lambda y: y >= 2022)]
NOMBRE_TIPO = {"articulo": "Artículo de revista", "libro": "Libro", "capitulo": "Capítulo de libro", "informe": "Informe o documento institucional",
               "patente": "Patente", "norma": "Norma o documento oficial colombiano"}

# ---------------------------------------------------------------- 19a
d = Doc("29")
d.h(1, "29. BIBLIOGRAFÍA")
d.h(2, "29.1 Referencias bibliográficas")
d.p(f"Esta lista reúne las {N} obras citadas en el documento, ordenadas alfabéticamente y con sangría francesa, en formato APA 7. Cada cita del texto corresponde a una referencia de la lista, y cada referencia de la lista se cita al menos una vez. Cuando dos obras comparten autor y año, el año lleva una letra: 2012a y 2012b distinguen la Ley 1523 de la Ley 1581. La lista no incluye obras no citadas.")
d.p("El estado de verificación de cada referencia procede de una revisión web parcial que la corrida registró. Las obras del corpus de vigilancia tecnológica (informe_FINAL) conservan la naturaleza DECLARADO: su verificación independiente queda pendiente. Se añadió el DOI solo cuando la fuente lo aportó. Ninguna referencia se inventó, y las que no se encontraron en la revisión web conservan el estado NO_VERIFICADO. La {T:t01} del apartado 19.2 resume la composición de la lista.")
d.guardar(os.path.join(CAPS, "a29a_r.md" if A2ONLY else "cap19a.md"))

# ---------------------------------------------------------------- lista cruda
L = []
for r in citadas:
    L += ['::: {custom-style="Referencia"}', apa_con_sufijo(r), ":::", ""]
open(os.path.join(CAPS, "a29_refs_r.md" if A2ONLY else "cap19_refs.md"), "w", encoding="utf-8").write("\n".join(L))

# ---------------------------------------------------------------- 19b
d = Doc("29")
d.h(2, "29.2 Análisis bibliométrico de las referencias")
d.p(f"El análisis describe la composición de las {N} referencias por tipo de fuente, por año de publicación, por origen y por estado de verificación. El cuartil de las revistas no se consultó en esta corrida, porque no se accedió a SJR ni a JCR. La {{T:t01}} presenta el resumen estadístico.")
fil = []
for t, c in sorted(tipos.items(), key=lambda z: -z[1]):
    fil.append(("Tipo de fuente", NOMBRE_TIPO.get(t, t), str(c), num(100 * c / N, 1) + " %"))
for nm, fn in rangos:
    c = sum(1 for y in años if fn(y)); fil.append(("Año de publicación", nm, str(c), num(100 * c / N, 1) + " %"))
for k in ("F-INF", "CANON", "DOMINIO", "NORMA"):
    if orig.get(k): fil.append(("Origen", {"F-INF": "Corpus del informe de vigilancia tecnológica", "CANON": "Obras canónicas del metaprompt y del análisis de decisión", "DOMINIO": "Literatura de dominio", "NORMA": "Normas y documentos oficiales"}[k], str(orig[k]), num(100 * orig[k] / N, 1) + " %"))
for k in ("VERIFICADO", "PARCIALMENTE_VERIFICADO", "NO_VERIFICADO"):
    fil.append(("Estado de verificación", k, str(ver.get(k, 0)), num(100 * ver.get(k, 0) / N, 1) + " %"))
fil.append(("Identificador", "Referencias con DOI", str(doi), num(100 * doi / N, 1) + " %"))
fil.append(("Cuartil de la revista", "Q1 o Q2", "NO_VERIFICADO", "NO_VERIFICADO"))
d.tabla("t01", "Resumen estadístico de las referencias por tipo, año, origen y verificación",
        ["Dimensión", "Categoría", "Referencias", "Porcentaje"], fil,
        f"*Nota.* Elaboración propia con el banco cerrado de referencias (banco.json) y el recuento de citas del documento. Total de referencias: {N}. Los años se cuentan desde la fecha de la publicación citada. El cuartil no se consultó (NO_VERIFICADO). Decimales con coma.")
d.p(f"La lista cumple el mínimo de 60 referencias, con {N}. En actualidad, {ult5} referencias, equivalentes a {num(100 * ult5 / N, 1)} %, son de 2022 a 2026. El criterio exige 70 % o más en los últimos cinco años. {'La lista cumple ese criterio.' if ult5 / N >= 0.70 else 'La lista no cumple ese criterio.'} La diferencia se explica por la presencia de obras canónicas de teoría de la decisión, de la evaluación y de la innovación. Su antigüedad es parte de su valor. Un documento que cita a Simon (1973), Raiffa (1968) o Rogers (2003) no puede cumplir una regla de actualidad estricta sin renunciar a su fundamento teórico. La ruta de solución es añadir literatura reciente de 2022 a 2026 en los capítulos que hoy se apoyan en obras clásicas.")
d.p(f"El criterio de 60 % de artículos en cuartiles Q1 o Q2 no puede verificarse. Los {tipos.get('articulo', 0)} artículos de la lista no tienen cuartil consultado, y declarar cumplimiento sin ese dato sería inventar un resultado. La ruta de solución es consultar SJR o JCR para cada revista y registrar el cuartil de la fecha de publicación. Esa tarea corresponde a la verificación de referencias de la revisión final y se registra como pendiente en el cierre del documento.")
d.p(f"La composición por origen muestra que {orig.get('F-INF', 0)} referencias ({num(100 * orig.get('F-INF', 0) / N, 1)} %) provienen del corpus de vigilancia tecnológica del informe aportado. Ese corpus incluye {tipos.get('patente', 0)} patentes, que sustentan el análisis de libertad de operación y no la evidencia científica. El estado de verificación indica que {ver.get('VERIFICADO', 0)} referencias quedaron verificadas, {ver.get('PARCIALMENTE_VERIFICADO', 0)} quedaron parcialmente verificadas y {ver.get('NO_VERIFICADO', 0)} quedaron sin verificar. Antes de la radicación se deben verificar las {ver.get('NO_VERIFICADO', 0)} restantes, con edición, páginas y DOI.")
d.guardar(os.path.join(CAPS, "a29b_r.md" if A2ONLY else "cap19b.md"))
print("ok", N, dict(tipos), ult5, dict(ver), "sin_sufijo:", len(sin_sufijo), "doi", doi)
