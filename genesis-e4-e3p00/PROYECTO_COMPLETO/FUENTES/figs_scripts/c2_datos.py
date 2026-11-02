# -*- coding: utf-8 -*-
"""Datos y cálculos del Paso 3 y del Capítulo 2 (secciones 2.1 a 2.3).
Fuente única: RAIZ/refs/corpus_informe.json (42 referencias de F-INF §13.2) y cifras de F-INF citadas por sección.
Todo cálculo es reproducible: semilla 42, año de corte 2026."""
import json, os, re, math, collections, itertools
import numpy as np

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
INFORME = os.path.join(os.path.dirname(RAIZ), "work", "informe.md")
SEED = 42
CORTE = 2026

CORPUS = json.load(open(os.path.join(RAIZ, "refs", "corpus_informe.json"), encoding="utf-8"))

# --- TRL, IRL, DRL por documento (F-INF §4.1, Tabla 13, p. 29). Orden = G-01..G-42 (orden cronológico del informe)
TABLA13 = [
 ("G-01","Reintjes1995",3,2,3),("G-02","Koppinen2019",3,2,3),("G-03","Abernathy2019",3,3,3),("G-04","Blythe2020",4,3,3),
 ("G-05","MolinaGmez2021",3,1,2),("G-06","Becerra2021",4,4,3),("G-07","Gumaste2021",4,3,3),("G-08","RodrguezVillamizar2022",5,4,4),
 ("G-09","Ali2022",3,3,3),("G-10","Chang2023",4,2,2),("G-11","Izod2023",3,3,3),("G-12","Essamlali2024",5,3,2),
 ("G-13","RendnMarn2024",3,2,2),("G-14","Hurst2024",3,3,3),("G-15","Wilson2024",3,3,3),("G-16","Rine2024",2,2,3),
 ("G-17","Huang2025",4,2,2),("G-18","VlezPereira2025",4,2,3),("G-19","Moura2025",3,2,2),("G-20","Suresh2025",6,4,3),
 ("G-21","Botezat2025",4,2,3),("G-22","Miraglia2025",3,2,3),("G-23","Hale2025",3,2,3),("G-24","Eckenrode2025",3,3,3),
 ("G-25","Machida2025",4,3,3),("G-26","Nelson2026",5,4,2),("G-27","Wei2026",4,3,2),("G-28","Pedraza2026",3,2,3),
 ("G-29","RuizCarrascal2026",9,8,8),("G-30","AyalaParra2026",4,2,3),("G-31","Bang2026",4,4,3),("G-32","Alvarez2026",4,3,3),
 ("G-33","Espinoza2026",7,5,5),("G-34","Haris2026",4,3,3),("G-35","Tavella2026",3,2,4),("G-36","Kumar2026",3,2,3),
 ("G-37","Liao2026",5,3,4),("G-38","GallegoCartagena2026",3,2,3),("G-39","Huang2026",4,4,2),("G-40","Acosta2026",3,3,3),
 ("G-41","Brkic2026",4,3,4),("G-42","Comercio2026",None,None,3)]
VALLE = {"G-01":"V1","G-02":"V1","G-03":"V1","G-04":"V2","G-05":"V4","G-06":"V2","G-07":"V2","G-08":"V4","G-09":"V1","G-10":"V4",
 "G-11":"V1","G-12":"V4","G-13":"V1","G-14":"V1","G-15":"V1","G-16":"V1","G-17":"V4","G-18":"V4","G-19":"V1","G-20":"V3","G-21":"V1",
 "G-22":"V1","G-23":"V1","G-24":"V1","G-25":"V2","G-26":"V4","G-27":"V4","G-28":"V1","G-29":"Ninguno","G-30":"V4","G-31":"V4","G-32":"V4",
 "G-33":"V3","G-34":"V4","G-35":"V5","G-36":"V1","G-37":"V4","G-38":"V1","G-39":"V2","G-40":"V1","G-41":"V2","G-42":"Ninguno"}
# Grupo documental (F-INF §10.1 Tabla 46 y §4.6/§6.2; conteos 9/8/9/8/8)
GRUPO = {"Molina":1}
GRUPOS = {1:["MolinaGmez2021","Becerra2021","Chang2023","Essamlali2024","Huang2025","VlezPereira2025","Moura2025","Nelson2026","Wei2026"],
          2:["Suresh2025","Espinoza2026","RuizCarrascal2026","Pedraza2026","AyalaParra2026","Bang2026","Alvarez2026","Haris2026"],
          3:["RodrguezVillamizar2022","RendnMarn2024","Botezat2025","Miraglia2025","Tavella2026","Kumar2026","Liao2026","GallegoCartagena2026","Huang2026"],
          4:["Reintjes1995","Koppinen2019","Abernathy2019","Blythe2020","Gumaste2021","Ali2022","Hurst2024","Hale2025"],
          5:["Izod2023","Wilson2024","Rine2024","Eckenrode2025","Machida2025","Acosta2026","Brkic2026","Comercio2026"]}
GRUPO_DE = {k: g for g, ks in GRUPOS.items() for k in ks}

# Robustez conocida por documento (F-INF §2.2 p. 14 y Tabla 65 §13.1 p. 208)
ROB_CONOCIDA = {"Nelson2026":6.1,"MolinaGmez2021":5.1,"AyalaParra2026":5.0,"Acosta2026":2.7,"Machida2025":2.7,"Eckenrode2025":2.8,
 "Pedraza2026":3.8,"Kumar2026":4.1,"Suresh2025":2.8,"Alvarez2026":4.3,"RuizCarrascal2026":4.4,"VlezPereira2025":4.4,"Rine2024":3.0,
 "RodrguezVillamizar2022":5.0,"Tavella2026":4.6,"Reintjes1995":3.8,"Blythe2020":3.0}   # 1995 y 2020 tienen un solo documento (Tabla 14)
ROB_GRUPO = {1:(4.54,9),2:(4.12,8),3:(4.32,9),4:(3.54,8),5:(2.97,8)}   # F-INF §3.2 Tabla 6 (p. 22) y §2.2

def apa_fuente(r):
    a = r["apa"]
    if r["tipo"] == "articulo":
        m = re.search(r"\*([^*]+?),\s*(\d+)(?:\((\d+)\))?\*", a)
        rev = m.group(1).strip() if m else None
        if rev is None:
            m = re.search(r"\*([^*]+)\*", a); rev = m.group(1).split(",")[0].strip()
        rev = re.sub(r"\s*,\s*$", "", rev)
        doi = re.search(r"https://doi\.org/(\S+)", a).group(1)
        return rev, doi
    if r["tipo"] == "patente":
        m = re.search(r"\(([^()]*?(?:Patent)[^()]*?No\.\s*([^)]+?))\)\.\s*(.+)$", a)
        num = m.group(2).strip(); oficina = m.group(3).strip(". ")
        return oficina, num
    return "Superintendencia de Industria y Comercio (CIGEPI)", "Sin DOI ni número de solicitud"

def apellidos_autores(r):
    """Devuelve lista de (apellido, iniciales) de la cadena de autores APA (antes del año)."""
    a = r["apa"]; cab = a.split(" (%d)" % r["year"])[0]
    if r["tipo"] == "informe": return []
    cab = re.sub(r",\s*y\s+", ", ", cab)
    partes = re.split(r"(?<=\.),\s+(?=[A-ZÁÉÍÓÚÑa-z])", cab)
    out = []
    for p in partes:
        m = re.match(r"^(.*?),\s*(.+)$", p.strip())
        if not m: continue
        ap, ini = m.group(1).strip(), m.group(2).strip()
        out.append((ap, ini))
    return out

def clave_autor(ap, ini):
    n = lambda s: re.sub(r"[^a-z]", "", __import__("unicodedata").normalize("NFKD", s.lower()).encode("ascii","ignore").decode())
    ini1 = n(ini)[:1]
    ap = re.sub(r"^(de|da|van|von)\s+", "", ap.strip(), flags=re.I)
    return n(ap) + "_" + ini1

def tabla_autores():
    """Cuenta documentos por autor (clave apellido + primera inicial). Devuelve Counter y mapa autor->documentos."""
    docs = collections.defaultdict(list); nombres = {}
    total = 0
    for r in CORPUS:
        vistos = set()
        for ap, ini in apellidos_autores(r):
            k = clave_autor(ap, ini); total += 1
            nombres.setdefault(k, f"{ap}, {ini}")
            if k in vistos: continue
            vistos.add(k); docs[k].append(r["key"])
    return docs, nombres, total

def lotka(docs):
    """Ajuste de Lotka con la distribución de autores por número de documentos. Devuelve dict con LS, MLE y bootstrap (semilla 42, 1.000 réplicas)."""
    cont = np.array([len(v) for v in docs.values()])
    xs = np.array(sorted(set(cont)))
    ys = np.array([(cont == x).sum() for x in xs])
    res = {"n_autores": int(len(cont)), "niveles": [(int(x), int(y)) for x, y in zip(xs, ys)]}
    def mle(c):
        c = np.asarray(c, float); xmin = 1.0
        return 1.0 + len(c) / np.sum(np.log(c / (xmin - 0.5)))
    def ls(c):
        c = np.asarray(c); xs_ = np.array(sorted(set(c)))
        if len(xs_) < 2: return float("nan")
        ys_ = np.array([(c == x).sum() for x in xs_])
        b = np.polyfit(np.log(xs_), np.log(ys_), 1)[0]
        return -b
    res["alpha_mle"] = mle(cont); res["alpha_ls"] = ls(cont)
    rng = np.random.default_rng(SEED); bm = []; bl = []
    for _ in range(1000):
        s = rng.choice(cont, size=len(cont), replace=True)
        bm.append(mle(s)); a = ls(s)
        if not math.isnan(a): bl.append(a)
    res["ic_mle"] = (float(np.percentile(bm, 2.5)), float(np.percentile(bm, 97.5)))
    res["ic_ls"] = (float(np.percentile(bl, 2.5)), float(np.percentile(bl, 97.5))) if bl else (float("nan"),)*2
    res["ls_validos"] = len(bl)
    res["frac_un_doc"] = float((cont == 1).mean())
    return res

def tabla_fuentes():
    c = collections.Counter(); porfuente = collections.defaultdict(list)
    for r in CORPUS:
        if r["tipo"] == "articulo":
            rev, _ = apa_fuente(r); c[rev] += 1; porfuente[rev].append(r["key"])
    return c, porfuente

def bradford(c):
    """Zonas de Bradford por tercios de artículos (orden descendente por documentos)."""
    N = sum(c.values()); orden = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))
    zonas = [[], [], []]; acum = 0; z = 0; lim = [N/3, 2*N/3, N]
    for rev, n in orden:
        # asigna a la zona cuyo límite acumulado aún no se ha superado antes de añadir
        while z < 2 and acum >= lim[z] - 1e-9: z += 1
        zonas[z].append((rev, n)); acum += n
    return zonas, N

def serie_anual():
    c = collections.Counter(r["year"] for r in CORPUS)
    return c

def segmentar(serie_anios, serie_vals, k=3):
    """Segmentación óptima en k tramos contiguos por mínima suma de cuadrados (programación dinámica)."""
    n = len(serie_vals); v = np.array(serie_vals, float)
    def sse(i, j):  # [i, j)
        s = v[i:j]; return float(((s - s.mean())**2).sum())
    INF = 1e18; dp = [[INF]*(n+1) for _ in range(k+1)]; bk = [[0]*(n+1) for _ in range(k+1)]
    dp[0][0] = 0
    for t in range(1, k+1):
        for j in range(t, n+1):
            for i in range(t-1, j):
                c = dp[t-1][i] + sse(i, j)
                if c < dp[t][j]: dp[t][j] = c; bk[t][j] = i
    cortes = []; j = n
    for t in range(k, 0, -1):
        i = bk[t][j]; cortes.append((i, j)); j = i
    cortes.reverse()
    return [(serie_anios[i], serie_anios[j-1]) for i, j in cortes], dp[k][n]

def cagr(v0, v1, anios):
    return (v1/v0)**(1.0/anios) - 1

def palabras_titulo():
    """Palabras de título (sin palabras vacías) por documento."""
    vac = set("a an and the of in on for to with by from at as or its their into using use via toward towards how what is are be between under during across case study based approach approaches system systems method methods apparatus new through among regarding due highly recent real key de del la las los el en y para con por un una al se que como sobre entre hacia".split())
    out = {}
    for r in CORPUS:
        t = re.search(r"\*([^*]+)\*|\)\.\s*([^.*]+?)[.?]\s", r["apa"])
        titulo = None
        if r["tipo"] == "articulo":
            m = re.search(r"\(\d{4}\)\.\s*(.+?)\s*\*", r["apa"]); titulo = m.group(1)
        else:
            m = re.search(r"\*([^*]+)\*", r["apa"]); titulo = m.group(1)
        toks = re.findall(r"[a-záéíóúñü][a-záéíóúñü\-]+|pm2[.,]5", titulo.lower())
        toks = [x for x in toks if x not in vac and len(x) > 2]
        out[r["key"]] = (titulo, sorted(set(toks)))
    return out

if __name__ == "__main__":
    print(len(CORPUS), collections.Counter(r["tipo"] for r in CORPUS))
    docs, nombres, total = tabla_autores()
    print("autores únicos", len(docs), "ocurrencias", total)
    rep = {k: v for k, v in docs.items() if len(v) > 1}
    for k, v in rep.items(): print("  repetido", nombres[k], v)
    print(lotka(docs))
    c, pf = tabla_fuentes(); print(sum(c.values()), len(c)); print(c.most_common())
    z, N = bradford(c); 
    for i, zz in enumerate(z, 1): print("Z", i, len(zz), sum(n for _, n in zz), zz)
    s = serie_anual(); anios = list(range(1995, 2027)); vals = [s.get(a, 0) for a in anios]
    print(segmentar(anios, vals, 3)); print(sorted(s.items()))
    for w in ((2019, 2026), (2021, 2026), (2024, 2026), (1995, 2026)):
        print(w, cagr(s[w[0]], s[w[1]], w[1]-w[0]))
    for r in CORPUS: print(r["key"], apa_fuente(r))


EQ_TITULO = {"aire": "air", "calidad": "quality", "salud": "health", "gestión": "management"}

def red_titulos(umbral=2):
    """Red de co-ocurrencia de palabras de título (frecuencia >= umbral). Louvain con semilla 42."""
    import networkx as nx
    pt = palabras_titulo()
    docs = {k: sorted(set(EQ_TITULO.get(w, w) for w in toks)) for k, (t, toks) in pt.items()}
    cnt = collections.Counter(w for ws in docs.values() for w in ws)
    nodos = [w for w, c in cnt.items() if c >= umbral]
    G = nx.Graph()
    for w in nodos: G.add_node(w, f=cnt[w])
    for ws in docs.values():
        for a, b in itertools.combinations([w for w in ws if w in nodos], 2):
            if G.has_edge(a, b): G[a][b]["weight"] += 1
            else: G.add_edge(a, b, weight=1)
    com = nx.community.louvain_communities(G, weight="weight", seed=SEED)
    com = sorted(com, key=lambda c: (-len(c), sorted(c)[0]))
    mod = nx.community.modularity(G, com, weight="weight")
    return G, cnt, com, mod


def bootstrap_phi(reps=1000):
    """Bootstrap de φ (revistas de la zona 2 sobre revistas de la zona 1) remuestreando los 26 artículos; semilla 42."""
    arts = []
    for r in CORPUS:
        if r["tipo"] == "articulo": arts.append(apa_fuente(r)[0])
    rng = np.random.default_rng(SEED); out = []; invalid = 0
    for _ in range(reps):
        m = rng.choice(len(arts), size=len(arts), replace=True)
        c = collections.Counter(arts[i] for i in m)
        z, N = bradford(c)
        if len(z[0]) == 0 or len(z[1]) == 0: invalid += 1; continue
        out.append(len(z[1]) / len(z[0]))
    return (float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5)), float(np.mean(out)), invalid, len(out))
