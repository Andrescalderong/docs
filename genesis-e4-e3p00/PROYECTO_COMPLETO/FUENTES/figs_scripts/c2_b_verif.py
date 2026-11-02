# -*- coding: utf-8 -*-
"""Tabla de verificación bibliográfica del Capítulo 2 (cap02a.md y cap02b.md), calculada desde el banco de referencias.
Uso: python3 c2_b_verif.py [archivo.md ...]   (por defecto, caps/cap02a.md y caps/cap02b.md si existen)
Cuenta las citas de la prosa con las mismas expresiones que build/check_cap.py (las tablas y las notas no cuentan) y las asigna a
refs/banco.json por autor y año. Origen = F-INF (corpus), CANON, DOMINIO o NORMA. Últimos cinco años = 2022 a 2026 (corte 13-oct-2026).
Cuartiles: no determinables (NO_VERIFICADO en el banco). Sin aleatoriedad."""
import os, re, sys, json, collections
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "build"))
import check_cap as C   # reutiliza norm, citas_texto y split_directives

BANCO = json.load(open(os.path.join(RAIZ, "refs", "banco.json"), encoding="utf-8"))
ORIGEN = {"F-INF": "Corpus (F-INF)", "CANON": "Canon", "DOMINIO": "Dominio", "NORMA": "Norma"}
ORDEN_ORIGEN = ["F-INF", "CANON", "DOMINIO", "NORMA"]

def claves(r):
    base = re.sub(r"\s*\[[^\]]*\]", "", r["cite"])
    ks = {C.norm(base)}
    m = re.search(r"\[([^\]]+)\]", r["cite"])
    if m: ks.add(C.norm(m.group(1)))
    tol = C.norm(base.split(" y ")[0]) + " et al"
    return ks, {tol}

INDICE = []
for r in BANCO:
    exactas, tolerantes = claves(r)
    INDICE.append((r, exactas, tolerantes))

def buscar(autor, año):
    a = C.norm(re.sub(r"\bet al\.?", "et al", autor))
    if a.split(" ")[0] in ("de", "del", "la", "van", "von"):
        a2 = re.sub(r"^(de|del|la|van|von) ", "", a)
    else:
        a2 = a
    cand = [x for x in INDICE if str(x[0]["year"]) == año]
    for r, ex, tol in cand:
        if a in ex or a2 in ex: return r
    for r, ex, tol in cand:
        if a in tol or a2 in tol: return r
    for r, ex, tol in cand:
        if a.replace(" et al", "") in {k.replace(" et al", "") for k in ex | tol}: return r
    return None

def cargar(archivos, tablas=False):
    """Citas de la prosa (como check_cap) o, con tablas=True, de toda la prosa más las celdas y notas de tablas (sin las filas de referencia APA)."""
    cits = []
    for f in archivos:
        raw = open(f, encoding="utf-8").read()
        if tablas:
            lineas = [l for l in raw.split("\n") if l.strip() and not l.startswith(("%%", "#", "| Referencia APA 7", "| ---", ":::FIGURA"))]
            texto = "\n".join(re.sub(r"^:::NOTA|^:::TABLA\s+\S+\s*\|", "", l) for l in lineas)
        else:
            prose, tabs, figs, order = C.split_directives(raw)
            body = [s.strip() for s in prose if s.strip() and not s.strip().startswith(("#", "|", "%%", "<!--"))]
            texto = "\n".join(body)
        for au, y in C.citas_texto(texto):
            r = buscar(au, y)
            if r is not None: cits.append(r["key"])
    return cits

def por_clave_global(k):
    return {r['key']: r for r in BANCO}[k]

def num(n, dec=1):
    return f"{n:.{dec}f}".replace(".", ",")

def main():
    caps = os.path.join(RAIZ, "caps")
    archivos = sys.argv[1:] or [os.path.join(caps, n) for n in ("cap02a.md", "cap02b.md") if os.path.exists(os.path.join(caps, n))]
    cits = cargar(archivos)
    por_clave = {r["key"]: r for r in BANCO}
    occ = collections.Counter(cits)
    distintas = sorted(occ)
    N, D = len(cits), len(distintas)
    print("ARCHIVOS:", [os.path.basename(a) for a in archivos])
    ct = cargar(archivos, tablas=True)
    print(f"CON TABLAS Y NOTAS: citas {len(ct)}; referencias distintas {len(set(ct))}")
    ut = [k for k in set(ct) if por_clave_global(k)["year"] >= 2022]
    print(f"   de ellas, 2022-2026: {len(ut)} ({num(100*len(ut)/len(set(ct)))} %)")
    print(f"citas (ocurrencias): {N}; referencias distintas: {D}")
    print("\nPOR ORIGEN (distintas, % ; ocurrencias, %)")
    for o in ORDEN_ORIGEN:
        d = [k for k in distintas if por_clave[k]["origen"] == o]; n = sum(occ[k] for k in d)
        print(f"  {ORIGEN[o]:16s} {len(d):3d} ({num(100*len(d)/D)} %)   {n:4d} ({num(100*n/N)} %)")
    print("\nPOR TIPO DE FUENTE (distintas, %)")
    tipos = collections.Counter(por_clave[k]["tipo"] for k in distintas)
    for t, n in tipos.most_common():
        print(f"  {t:10s} {n:3d} ({num(100*n/D)} %)")
    print("\nPOR AÑO (distintas, % ; ocurrencias, %)")
    def banda(y):
        if y <= 2009: return "2009 o antes"
        if y <= 2015: return "2010 a 2015"
        if y <= 2021: return "2016 a 2021"
        return str(y)
    bandas = collections.OrderedDict((b, [0, 0]) for b in ["2009 o antes", "2010 a 2015", "2016 a 2021", "2022", "2023", "2024", "2025", "2026"])
    for k in distintas:
        b = banda(por_clave[k]["year"]); bandas[b][0] += 1; bandas[b][1] += occ[k]
    for b, (d, n) in bandas.items():
        print(f"  {b:14s} {d:3d} ({num(100*d/D)} %)   {n:4d} ({num(100*n/N)} %)")
    u5d = [k for k in distintas if por_clave[k]["year"] >= 2022]; u5n = sum(occ[k] for k in u5d)
    print(f"\nULTIMOS 5 ANOS (2022-2026): distintas {len(u5d)} de {D} = {num(100*len(u5d)/D)} %; ocurrencias {u5n} de {N} = {num(100*u5n/N)} %")
    print("Q1-Q2: no determinable (cuartiles NO_VERIFICADO en el banco)")
    # por origen dentro de los últimos cinco años
    print("\nULTIMOS 5 ANOS POR ORIGEN (distintas)")
    for o in ORDEN_ORIGEN:
        d = [k for k in u5d if por_clave[k]["origen"] == o]
        print(f"  {ORIGEN[o]:16s} {len(d):3d}")
    print("\nDISTINTAS:", ", ".join(distintas))

if __name__ == "__main__":
    main()
