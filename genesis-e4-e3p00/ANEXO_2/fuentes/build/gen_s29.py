# -*- coding: utf-8 -*-
"""Genera sec/s29.md (bibliografía APA 7) con las obras citadas (autor y año) y las normas nombradas en el texto de las demás secciones.
Uso: python3 build/gen_s29.py   -> escribe A2/sec/s29.md y A2/out/refs_usadas.json; imprime citas sin resolver."""
import re, sys, json, os, collections, unicodedata, glob
A2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(A2, "build"))
import check_cap as cc
BANCO = json.load(open(os.path.join(A2, "refs", "banco.json"), encoding="utf-8"))
byk = {r["key"]: r for r in BANCO}
SUF = {"Ley1523": "2012a", "Ley1581": "2012b"}
SUF_ACT = set()   # sufijos activos: solo si las dos leyes de 2012 se citan en la lista
def apa_de(r):
    a = r["apa"]
    if r["key"] in SUF_ACT: a = a.replace("(2012,", f"({SUF[r['key']]},")
    return a
norm = cc.norm
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
# normas nombradas en el texto (sin paréntesis de autor y año)
NORMAS = [
 (r"Ley 1523 de 2012", "Ley1523"), (r"Ley 2056 de 2020", "Ley2056"), (r"Ley 2294 de 2023", "Ley2294"), (r"Ley 1286 de 2009", "Ley1286"),
 (r"Ley 1581 de 2012", "Ley1581"), (r"Ley 1955 de 2019", "Ley1955"), (r"Decreto 1261 de 2026", "Dec1261"), (r"Decreto 1171 de 2026", "Dec1171"), (r"Decreto Legislativo 1414|Decreto 1414", "Dec1414"),
 (r"Decreto 1821 de 2020", "Dec1821"), (r"Decreto 591 de 1991", "Dec591"), (r"Resolución 2254 de 2017", "Res2254"),
 (r"CONPES 3943|documento CONPES 3943", "Conpes3943"), (r"CONPES 4069|documento CONPES 4069", "Conpes4069"),
 (r"Acuerdo 12 de 2024", "Acuerdo12"), (r"Decisión 486", "Decision486"), (r"Marco de Sendái", "UNISDR2015"),
 (r"Caldas 2024-2027", "PDDCaldas"), (r"Gobernando: Más que un Plan", "PDDCundinamarca"), (r"Liderazgo que Transforma", "PDDValle"),
]
def usadas_en(archivos):
    usadas = collections.Counter(); no = set(); amb = set()
    for f in archivos:
        t = open(f, encoding="utf-8").read(); t = re.sub(r"```.*?```", "", t, flags=re.S)
        t = re.sub(r"\[Diligenciar:[^\]]*\]", "", t)
        for au, y in cc.citas_texto(t):
            ks = resolver(au, y)
            if not ks: no.add(f"{au} ({y}) [{os.path.basename(f)}]")
            else:
                usadas.update(ks)
                if len(ks) > 1: amb.add(f"{au} ({y}): {sorted(ks)}")
        for pat, k in NORMAS:
            if re.search(pat, t): usadas[k] += 1
    return usadas, no, amb
def main(solo_anexo=False, sin_anexo=False):
    archivos = sorted(f for f in glob.glob(os.path.join(A2, "sec", "s*.md")) if not re.search(r"s(00|29)\.md$", f))
    if sin_anexo: archivos = [f for f in archivos if not f.endswith("sA.md")]
    if solo_anexo: archivos = [os.path.join(A2, "sec", "sA.md")]
    usadas, no, amb = usadas_en(archivos)
    if no: print("NO RESUELTAS:", sorted(no))
    if amb: print("AMBIGUAS:", sorted(amb))
    refs = [byk[k] for k in sorted(usadas)]
    SUF_ACT.clear()
    if all(k in usadas for k in SUF): SUF_ACT.update(SUF)
    def orden(r):
        s = re.sub(r"[*_]", "", apa_de(r)); s = unicodedata.normalize("NFKD", s.lower())
        return "".join(c for c in s if not unicodedata.combining(c))
    refs.sort(key=orden)
    L = ["%% PREFIJO: 29", "# 29. BIBLIOGRAFÍA", ""] if not solo_anexo else ["%% PREFIJO: R", "# REFERENCIAS DEL ANEXO A", ""]
    L.append(f"La lista reúne las {len(refs)} fuentes que {'el anexo' if solo_anexo else 'el documento'} cita, ordenadas alfabéticamente según las normas APA 7. Cada cita del texto tiene su referencia en la lista, y cada referencia tiene al menos una cita en el texto. Las leyes, los decretos y los documentos de política se nombran en el texto por su denominación y se listan con la entidad que los expide.")
    L.append("")
    if SUF_ACT:
        L.append("Las dos leyes del Congreso de la República de 2012 se distinguen con los sufijos «a» y «b», porque comparten autor y año. La Ley 1523 es 2012a y la Ley 1581 es 2012b.")
        L.append("")
    for r in refs:
        L += ['::: {custom-style="Referencia"}', apa_de(r), ":::", ""]
    out = os.path.join(A2, "sec", "s29.md") if not solo_anexo else os.path.join(A2, "out_md", "sA_refs.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(L))
    os.makedirs(os.path.join(A2, "out"), exist_ok=True)
    json.dump([r["key"] for r in refs], open(os.path.join(A2, "out", "refs_usadas.json" if not solo_anexo else "refs_anexoA.json"), "w"))
    ver = collections.Counter(r["ver"] for r in refs)
    print("ok", len(refs), "referencias", dict(ver))
if __name__ == "__main__":
    main("--solo-anexo" in sys.argv, "--sin-anexo" in sys.argv)
