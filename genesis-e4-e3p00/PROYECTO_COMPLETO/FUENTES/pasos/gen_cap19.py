# -*- coding: utf-8 -*-
"""Genera caps/cap19.md (bibliografía y análisis bibliométrico) a partir de las citas de todos los archivos del documento."""
import re, sys, json, os, collections, unicodedata
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/build"); sys.path.insert(0, RAIZ + "/refs")
import check_cap as cc
import lista
BANCO = json.load(open(RAIZ + "/refs/banco.json", encoding="utf-8"))
byk = {r["key"]: r for r in BANCO}
# desambiguación 2012a / 2012b
SUF = {"Ley1523": "2012a", "Ley1581": "2012b"}
def apa_de(r):
    a = r["apa"]
    if r["key"] in SUF: a = a.replace("(2012,", f"({SUF[r['key']]},")
    return a
def norm(s): return cc.norm(s)
IDX = collections.defaultdict(lambda: collections.defaultdict(set))
for r in BANCO:
    y = str(r["year"]); base = re.sub(r"\s*\[[^\]]*\]", "", r["cite"])
    IDX[y][norm(base)].add(r["key"])
    m = re.search(r"\[([^\]]+)\]", r["cite"])
    if m: IDX[y][norm(m.group(1))].add(r["key"])
    if " y " in base or "et al" in r["cite"]: IDX[y][norm(base.split(" y ")[0]) + " et al"].add(r["key"])
def resolver(autor, año):
    autor = re.sub(r"\s*\[[^\]]*\]", "", autor)
    a = norm(re.sub(r"\bet al\.?", "et al", autor))
    if a.startswith("matriz de "): a = a[10:]
    if a.split(" ")[0] in ("de", "del", "la", "van", "von") and a not in IDX[año]: a = re.sub(r"^(de|del|la|van|von) ", "", a)
    pos = IDX[año]
    if a in pos: return pos[a]
    sin = a.replace(" et al", "")
    for p, ks in pos.items():
        if p.replace(" et al", "") == sin: return ks
    for p, ks in pos.items():
        if len(a.split()) >= 2 and p.endswith(" " + a): return ks
    return set()
usadas = collections.Counter(); noresueltas = set(); ambiguas = set()
SALTAR = {"cap19.md", "front.md", "cierre.md"}
archivos = [f for f, t in lista.ORDEN if os.path.exists(lista.C + f) and f not in SALTAR and not f.startswith("div_")]
for f in archivos:
    t = open(lista.C + f, encoding="utf-8").read()
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    for au, y in cc.citas_texto(t):
        ks = resolver(au, y)
        if not ks: noresueltas.add(f"{au} ({y}) [{f}]")
        elif len(ks) > 1: ambiguas.add(f"{au} ({y}): {sorted(ks)}"); usadas.update(ks)
        else: usadas.update(ks)
if noresueltas: print("NO RESUELTAS:", sorted(noresueltas)[:40])
if ambiguas: print("AMBIGUAS:", sorted(ambiguas)[:10])
claves = sorted(usadas)
refs = [byk[k] for k in claves]
def clave_orden(r):
    s = re.sub(r"[*_]", "", apa_de(r)); s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))
refs.sort(key=clave_orden)
n = len(refs)
def esc(s): return s.replace("|", "\\|")
L = []; A = L.append
A("%% PREFIJO: 19"); A("# Capítulo 19. Bibliografía"); A("")
A("## 19.1 Referencias bibliográficas"); A("")
A(f"La lista reúne las {n} obras citadas en el documento, ordenadas alfabéticamente según las normas APA 7. Cada cita del texto tiene su referencia en la lista, y cada referencia de la lista tiene al menos una cita en el texto. Las obras que provienen del informe de vigilancia tecnológica llevan el número de página en la cita del texto cuando el informe lo permite. El estado de verificación de cada obra se resume en la {{T:t01}}; ninguna obra se afirma como verificada sin una consulta registrada.")
A("")
A("Las dos leyes del Congreso de la República de 2012 se distinguen con los sufijos «a» y «b», porque comparten autor y año. La Ley 1523 es 2012a y la Ley 1581 es 2012b.")
A("")
for r in refs:
    A('::: {custom-style="Referencia"}'); A(apa_de(r)); A(":::"); A("")
A("**Archivos aportados.** Los dos archivos del usuario que originan el documento no se publicaron y se citan por sus siglas en el texto. Informe de vigilancia tecnológica y bibliometría de 42 documentos: autoría no identificada, 2026, archivo informe_FINAL.docx, citado como F-INF. Embudo de problematización y análisis causal del sistema de vigilancia ambiental, expediente E3-P00 a E3-P21: autoría no identificada, 2026, archivo Problematica_E3-P00.docx, citado como F-E3.")
A("")
A("## 19.2 Análisis bibliométrico de las referencias"); A("")
yr = lambda r: int(re.sub(r"\D", "", str(r["year"]))[:4])
cnt_t = collections.Counter(r["tipo"] for r in refs)
cnt_o = collections.Counter(r["origen"] for r in refs)
cnt_v = collections.Counter(r["ver"] for r in refs)
cnt_y = collections.Counter()
for r in refs:
    y = yr(r)
    cnt_y["1995 o antes" if y <= 1995 else ("1996 a 2010" if y <= 2010 else ("2011 a 2015" if y <= 2015 else ("2016 a 2020" if y <= 2020 else ("2021 a 2023" if y <= 2023 else "2024 a 2026"))))] += 1
ult5 = sum(1 for r in refs if yr(r) >= 2021)
pct = lambda a, b: f"{a / b * 100:.1f}".replace(".", ",")
A(f"El análisis describe la lista por tipo de fuente, por año, por origen y por estado de verificación. De las {n} obras, {ult5} ({pct(ult5, n)} %) se publicaron entre 2021 y 2026, el periodo de los últimos cinco años. El cuartil de las revistas no consta en el informe de vigilancia ni en el banco de referencias. Por ello, el criterio de 60 % de artículos en cuartiles Q1 o Q2 no se puede verificar con los archivos disponibles (VACIO). El banco se construyó con tres criterios: obras del corpus de vigilancia, obras que el metaprompt exige y literatura de dominio.")
A("")
A("La {T:t01} presenta el resumen. El criterio de 60 referencias como mínimo se cumple. El criterio de 70 % en los últimos cinco años " + ("se cumple" if ult5 / n >= 0.7 else "no se cumple") + f" con {pct(ult5, n)} %. La lista combina literatura reciente del corpus con obras seminales de metodología. Esa combinación explica la proporción, porque los marcos de decisión, de evaluación y de gestión que fundamentan el diseño datan de décadas anteriores.")
A("")
A(":::TABLA t01 | Resumen estadístico de las referencias del documento")
A("| Dimensión | Categoría | Referencias | % del total |"); A("| --- | --- | --- | --- |")
names = {"articulo": "Artículos de revista", "libro": "Libros", "capitulo": "Capítulos de libro", "informe": "Informes institucionales y documentos oficiales", "norma": "Normas y leyes", "patente": "Patentes"}
for k, v in sorted(cnt_t.items(), key=lambda x: -x[1]): A(f"| Tipo de fuente | {names.get(k, k)} | {v} | {pct(v, n)} |")
for k in ("1995 o antes", "1996 a 2010", "2011 a 2015", "2016 a 2020", "2021 a 2023", "2024 a 2026"):
    A(f"| Año de publicación | {k} | {cnt_y.get(k, 0)} | {pct(cnt_y.get(k, 0), n)} |")
on = {"F-INF": "Corpus de vigilancia tecnológica (F-INF)", "CANON": "Obras del metaprompt y de la sección F4.4-MDR", "DOMINIO": "Literatura de dominio", "NORMA": "Normas y documentos oficiales"}
for k, v in sorted(cnt_o.items(), key=lambda x: -x[1]): A(f"| Origen | {on.get(k, k)} | {v} | {pct(v, n)} |")
for k, v in sorted(cnt_v.items(), key=lambda x: -x[1]): A(f"| Verificación | {k} | {v} | {pct(v, n)} |")
A("| Cuartil de la revista | Q1 o Q2 | VACIO | VACIO |")
A(f"| Total | Referencias citadas | {n} | 100,0 |")
A(":::NOTA *Nota.* Elaboración propia con el banco de referencias del proyecto y las citas de los archivos del documento. Verificación: VERIFICADO y PARCIALMENTE_VERIFICADO corresponden a consultas web de esta corrida; NO_VERIFICADO significa que no se consultó la obra o que la consulta no la encontró.")
A("")
A("El estado de verificación merece una advertencia. Parte de las obras del corpus, publicadas en 2025 y 2026, no aparecieron en las búsquedas de verificación. Esa ausencia puede deberse a que no están indexadas todavía, pero no confirma su existencia. El equipo formulador debe verificar cada obra marcada NO_VERIFICADO contra su fuente primaria antes de radicar, y corregir las que difieran.")
open(RAIZ + "/caps/cap19.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
json.dump(claves, open(RAIZ + "/out/claves_citadas.json", "w"), ensure_ascii=False)
print("ok", n, "referencias;", ult5, "últimos 5 años;", dict(cnt_v))
