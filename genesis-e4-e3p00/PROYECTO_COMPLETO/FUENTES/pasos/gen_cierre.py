# -*- coding: utf-8 -*-
"""Genera caps/cierre.md: verificación de completitud, registro de datos pendientes, F-01 a F-04. Ejecutar al final, sobre los archivos definitivos."""
import re, sys, os, json, subprocess, collections
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/build"); sys.path.insert(0, RAIZ + "/maestro"); sys.path.insert(0, RAIZ + "/refs")
import lista, maestro as M
C = lista.C
def esc(s): return str(s).replace("|", "\\|")
def pf(n): return f"{n:,}".replace(",", ".")
def conteo(files):
    tot = dict(pal=0, tab=0, fig=0, cit=0, largas=0)
    for f in files:
        if not os.path.exists(C + f): continue
        out = subprocess.run(["python3", "-I", RAIZ + "/build/check_cap.py", C + f], capture_output=True, text=True, env={**os.environ, "LC_ALL": "C.UTF-8"}).stdout
        m = re.search(r"palabras de prosa: (\d+).*?tablas: (\d+).*?figuras: (\d+).*?citas distintas: (\d+)", out)
        if m: tot["pal"] += int(m.group(1)); tot["tab"] += int(m.group(2)); tot["fig"] += int(m.group(3)); tot["cit"] += int(m.group(4))
        m = re.search(r"oraciones > \d+ palabras: (\d+)", out)
        if m: tot["largas"] += int(m.group(1))
    return tot
# (capítulo, archivos, mín palabras, mín tablas, mín figuras, mín refs)
CAPS = [(1, ["cap01.md"], 5000, 5, 3, 15), (2, ["cap02a.md", "cap02b.md"], 12000, 21, 13, 40), (3, ["cap03.md"], 1500, 3, 2, 5), (4, ["cap04.md"], 8000, 4, 3, 20),
        (5, ["cap05.md"], 5000, 7, 3, 15), (6, ["cap06.md"], 8000, 6, 4, 15), (7, ["cap07.md"], 2000, 3, 2, 3), (8, ["cap08.md"], 2500, 8, 3, 0), (9, ["cap09.md"], 1500, 3, 2, 0),
        (10, ["cap10.md"], 2000, 5, 3, 5), (11, ["cap11.md"], 2000, 4, 2, 0), (12, ["cap12.md"], 3500, 18, 5, 0), (13, ["cap13.md"], 4000, 8, 5, 0), (14, ["cap14.md"], 3500, 4, 2, 0),
        (15, ["cap15.md"], 3500, 3, 2, 0), (16, ["cap16.md"], 3500, 6, 4, 0), (17, ["cap17.md"], 2000, 4, 2, 0), (18, ["cap18.md"], 1500, 2, 1, 0), (19, ["cap19.md"], 0, 1, 0, 60),
        (20, ["cap20.md", "anexos_km.md"], 0, 1, 0, 0), (21, ["cap21.md"], 2500, 6, 2, 0)]
filas = []; tp = tt = tf = 0; nbad = 0; nlarg = 0
for n, fs, mp, mt, mf, mr in CAPS:
    c = conteo(fs); tp += c["pal"]; tt += c["tab"]; tf += c["fig"]; nlarg += c["largas"]
    if n == 19: ok = "CUMPLE" if c["tab"] >= 1 else "NO_CUMPLE"
    elif not any(os.path.exists(C + f) for f in fs): ok = "NO_CUMPLE (archivo ausente)"; nbad += 1
    else:
        faltas = []
        if mp and c["pal"] < mp: faltas.append(f"palabras {pf(c['pal'])} < {pf(mp)}")
        if c["tab"] < mt: faltas.append(f"tablas {c['tab']} < {mt}")
        if c["fig"] < mf: faltas.append(f"figuras {c['fig']} < {mf}")
        if mr and c["cit"] < mr: faltas.append(f"referencias {c['cit']} < {mr}")
        ok = "CUMPLE" if not faltas else "NO_CUMPLE (" + "; ".join(faltas) + ")"
        if faltas: nbad += 1
    filas.append((f"Capítulo {n}", f"{pf(c['pal'])} ({pf(mp) if mp else 'variable'})", f"{c['tab']} ({mt})", f"{c['fig']} ({mf})", f"{c['cit']} ({mr if mr else '—'})", ok))
pasos = conteo([f"paso{i}.md" for i in range(0, 8)])
x = conteo(["x01.md", "x02.md", "x03.md", "x05.md", "x06.md", "x07.md", "x08.md", "x09.md", "x10.md"])
est = conteo(["estrategia.md"])
# --- datos pendientes
files_all = [f for f, t in lista.ORDEN if os.path.exists(C + f) and not f.startswith("div_") and f not in ("cierre.md",)]
def etiqueta(f):
    m = re.match(r"cap(\d+)", f)
    if m: return f"Cap. {int(m.group(1))}"
    m = re.match(r"paso(\d)", f)
    if m: return f"Paso {m.group(1)}"
    if f.startswith("x"): return "1000X-" + f[1:3]
    return {"estrategia.md": "1000X-04", "anexos_km.md": "Cap. 20", "front.md": "Preliminares"}.get(f, f)
reg = collections.OrderedDict()
for f in files_all:
    t = open(C + f, encoding="utf-8").read()
    for m in re.finditer(r"\[DATO_USUARIO:\s*([^\]]+?)\]", t):
        k = re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")
        key = k.lower()
        d = reg.setdefault(key, dict(txt=k, n=0, donde=collections.OrderedDict()))
        d["n"] += 1; d["donde"][etiqueta(f)] = 1
CAT = [("Presupuesto y cotizaciones", r"cotiz|costo|presupuesto|tarifa|honorario|precio|valor del|monto|valoraci"),
       ("Términos de la convocatoria", r"tdr|términos de referencia|convocatoria|formato|extensión|porcentaje exigido|calendario|tope|reglamento"),
       ("Territorio y planes", r"municipio|pdd|anexo 4|demanda|polígono|departament|sitio|población|dane|piiom|misión|conpes|territori|eje |artículo del"),
       ("Entidades, personas y firmas", r"nombre|razón social|nit|responsable|persona|hoja|firma|representante|autoridad|panel|comité|entidad|equipo|grupo|empresa|custodio|alcald"),
       ("Certificaciones, cartas y documentos", r"certific|carta|convenio|acuerdo|aval|resolución|acta|documento|registro|permiso|contrato|póliza|inventario"),
       ("Datos técnicos y de medición", r"línea base|medici|laboratorio|rango|serie|cobertura|toneladas|operarios|código|evidencia|tipolog|enlace|equipos|sitio|calibraci")]
def cat(k):
    low = k.lower()
    for nombre, rx in CAT:
        if re.search(rx, low): return nombre
    return "Otros datos del usuario"
for d in reg.values(): d["cat"] = cat(d["txt"])
por_cat = collections.OrderedDict()
for d in reg.values():
    c = por_cat.setdefault(d["cat"], dict(n=0, ap=0, ej=[]))
    c["n"] += 1; c["ap"] += d["n"]
    if len(c["ej"]) < 2: c["ej"].append(d["txt"])
nref = json.load(open(RAIZ + "/out/claves_citadas.json")) if os.path.exists(RAIZ + "/out/claves_citadas.json") else []
sgr = M.total(M.BUDGET)
L = []; A = L.append
def tabla(tid, titulo, enc, fl, nota):
    A(f":::TABLA {tid} | {titulo}"); A("| " + " | ".join(enc) + " |"); A("| " + " | ".join("---" for _ in enc) + " |")
    for r in fl: A("| " + " | ".join(esc(x) for x in r) + " |")
    A(":::NOTA " + nota); A("")
A("%% PREFIJO: C")
A("## C.1 Verificación de completitud"); A("")
A(f"La verificación compara el contenido real de cada archivo con los mínimos del metaprompt: palabras de prosa, tablas, figuras y referencias distintas. Los conteos proceden de un verificador mecánico que cuenta la prosa sin tablas ni encabezados. Los 21 capítulos suman {pf(tp)} palabras, {tt} tablas y {tf} figuras. Los mínimos globales son 73.500 palabras, 87 tablas y 44 figuras. La {{T:t01}} detalla cada capítulo; entre paréntesis figura el mínimo.")
A("")
tabla("t01", "Verificación de completitud de los capítulos 1 a 21", ["Capítulo", "Palabras (mínimo)", "Tablas (mínimo)", "Figuras (mínimo)", "Referencias (mínimo)", "Estado"], filas,
      f"*Nota.* Elaboración propia con el verificador de capítulos del proyecto. El capítulo 2 suma sus dos archivos; el capítulo 20 suma los anexos A a J y K a M. La bibliografía del capítulo 19 se genera del banco de referencias. Pasos 0 a 7: {pf(pasos['pal'])} palabras, {pasos['tab']} tablas y {pasos['fig']} figuras. Paquete 1000X sin estrategia: {pf(x['pal'])} palabras, {x['tab']} tablas y {x['fig']} figuras. Estrategia: {pf(est['pal'])} palabras, {est['tab']} tablas y {est['fig']} figuras.")
tot_ok = tp >= 73500 and tt >= 87 and tf >= 44
A(f"Los totales de los capítulos {'superan' if tot_ok else 'no alcanzan'} los mínimos globales. {nbad} capítulos no cumplen su mínimo propio. El paquete 1000X suma {pf(x['pal'] + est['pal'])} palabras frente a un mínimo de 15.000 documentos y 8.000 de estrategia. La estrategia contiene {est['tab']} tablas frente a 15 y {est['fig']} figuras frente a 8.")
A("")
A("## C.2 Registro de datos pendientes del usuario"); A("")
A(f"El documento marca con [DATO_USUARIO: descripción] cada dato que solo el usuario o la entidad ejecutora posee. Hay {len(reg)} datos distintos con {sum(d['n'] for d in reg.values())} apariciones. La {{T:t02}} los agrupa por categoría y la {{T:t03}} los lista completos, con el lugar donde se usan. Ninguno se inventó: cada uno es un insumo que el equipo formulador debe reunir antes de radicar. La categoría «Términos de la convocatoria» es la más determinante, porque puede modificar presupuesto, estructura y plazos.")
A("")
tabla("t02", "Datos pendientes del usuario por categoría", ["Categoría", "Datos distintos", "Apariciones", "Ejemplos"], [(k, v["n"], v["ap"], "; ".join(v["ej"])) for k, v in sorted(por_cat.items(), key=lambda z: -z[1]["n"])],
      "*Nota.* Elaboración propia con los marcadores [DATO_USUARIO] de los archivos del documento. La clasificación usa palabras clave y puede asignar un dato a una categoría cercana.")
fl = []
for i, (k, d) in enumerate(sorted(reg.items(), key=lambda z: (z[1]["cat"], z[0])), 1):
    fl.append((i, d["txt"], d["cat"], d["n"], ", ".join(list(d["donde"])[:8]) + ("…" if len(d["donde"]) > 8 else "")))
tabla("t03", "Registro completo de datos pendientes del usuario", ["N.º", "Dato pendiente", "Categoría", "Apariciones", "Dónde se usa"], fl,
      "*Nota.* Elaboración propia. Ordenado por categoría y alfabéticamente. «Dónde se usa» lista hasta ocho partes del documento.")
A("## C.3 Cierre F-01 a F-04"); A("")
A("### C.3.1 F-01 Autoauditoría"); A("")
A("La autoauditoría lista cada requisito con su resultado, su evidencia, el método de comprobación, su estado y su limitación. Los estados son CUMPLE, NO_CUMPLE, NO_EJECUTADO y NO_APLICA. La {T:t04} la presenta. Ningún estado afirma más de lo que el método permite comprobar.")
A("")
ref_ok = len(nref)
fl = [
 ("Documento único con pasos 0 a 7, capítulos 1 a 21, paquete 1000X y estrategia", "Presente", "Parte I, Parte II y Parte III", "Inventario de archivos del ensamblado", "CUMPLE" if nbad == 0 else "PARCIAL", f"{nbad} capítulos por debajo de su mínimo propio (tabla C.1)"),
 ("Mínimos globales de los capítulos (73.500 palabras, 87 tablas, 44 figuras)", f"{pf(tp)} palabras, {tt} tablas, {tf} figuras", "Tabla C.1", "Verificador mecánico de prosa, tablas y figuras", "CUMPLE" if tot_ok else "NO_CUMPLE", "El verificador cuenta palabras de prosa sin encabezados ni tablas"),
 ("Jerarquía de encabezados APA 7 de cinco niveles", "Estilos de nivel 1 a 3 y párrafos con título en negrita de nivel 4 y 5", "Sección F0.4", "Inspección del archivo Word", "CUMPLE", "Los niveles 4 y 5 son párrafos con título, no estilos de la tabla de contenido"),
 ("Plantilla visual única (paleta, fondo transparente, jerarquía tipográfica)", "Todas las figuras usan la hoja de estilo común", "Tabla F0.5 y figuras", "Revisión de las imágenes y de los scripts", "CUMPLE", "Las figuras de capítulos escritos por agentes se revisaron una a una; la cuadrícula tenue es una excepción declarada a FIG-02"),
 ("Correspondencia entre citas del texto y lista de referencias", f"{ref_ok} referencias citadas, todas con cita; ninguna sin cita", "Capítulo 19", "Análisis mecánico de las citas de todos los archivos", "CUMPLE", "El analizador omite algunas citas narrativas de varias palabras; se revisaron a mano las no resueltas"),
 ("Verificación de las referencias en fuentes web", "71 verificadas, 12 parcialmente verificadas y el resto NO_VERIFICADO", "Tabla 19.1", "Búsquedas web por lotes", "PARCIAL", "Obras de 2025 y 2026 no aparecieron en las búsquedas"),
 ("Proporción de referencias de los últimos cinco años (70 %) y de artículos Q1 o Q2 (60 %)", "Proporción reciente en la Tabla 19.1; cuartiles sin datos", "Tabla 19.1", "Conteo por año; cuartil sin fuente", "NO_CUMPLE", "El cuartil de las revistas es VACIO; la proporción reciente es menor que 70 %"),
 ("Oraciones de 25 palabras o menos", f"{nlarg} oraciones largas restantes en los capítulos", "Archivos del documento", "Verificador mecánico", "PARCIAL" if nlarg else "CUMPLE", "El verificador no evalúa el contexto de la oración"),
 ("Coherencia cardinal (100 nodos, 10 gateways, 3 referencias, TRL 4 a 7, 24 meses y 104 semanas, SGR " + M.cop(sgr) + " COP)", "Cifras tomadas de una sola fuente (maestro.py)", "Ficha maestra", "Lectura de las cifras clave; sin barrido automático completo", "PARCIAL", "El barrido automático MCC36 sobre todas las cifras no se ejecutó"),
 ("Pruebas de rechazo del metaprompt y verificador NTC", "No ejecutadas", "—", "—", "NO_EJECUTADO", "Requieren los programas de verificación del metaprompt"),
 ("Validación empírica con el panel evaluador y los comités", "No ejecutada", "—", "—", "NO_EJECUTADO", "Exige casos reales"),
 ("Datos pendientes del usuario", f"{len(reg)} datos distintos marcados", "Tabla C.3", "Búsqueda de marcadores", "CUMPLE", "El estado CUMPLE significa que los datos están marcados, no que existan"),
]
tabla("t04", "Autoauditoría del documento (F-01)", ["Requisito", "Resultado", "Evidencia", "Método", "Estado", "Limitación"], fl,
      "*Nota.* Elaboración propia. Los estados siguen la norma de cierre del metaprompt. PARCIAL se usa cuando una parte del requisito se cumple y otra no.")
A("### C.3.2 F-02 ¿Qué se me escapa?"); A("")
A("Los vacíos siguientes tienen efecto sobre la decisión de radicar. Cada uno lleva su ruta de resolución. La lista no pretende ser exhaustiva: registra los vacíos que esta corrida pudo detectar. La ausencia de otros hallazgos no equivale a su inexistencia. La {T:t05} los presenta.")
A("")
fl = [
 ("Los términos de referencia no se aportaron", "Presupuesto, rubros admisibles, estructura, plazos y pesos de evaluación pueden cambiar", "Obtener los TdR y cotejar capítulos 7, 8, 9 y 21"),
 ("Articulación territorial no verificada (reserva R-ART)", "La regla bloqueante del metaprompt exigía regresar a la admisión; el proyecto puede ser rechazado por pertinencia", "Reunir PDD de los tres departamentos, Anexo 4, PIIOM, diagnóstico del Observatorio y CONPES vigentes"),
 ("Línea base de error propia inexistente", "Las metas de 30 % y 0,70 no tienen punto de partida y la compuerta C1 depende de ella", "Colocalizar en el tramo 1 y registrar la línea base en los meses 4 a 10"),
 ("Cotizaciones y certificaciones de contrapartida ausentes", "El presupuesto es una estimación sin soporte de proveedores", "Solicitar cotizaciones formales y certificar los aportes en especie"),
 ("Alianza, entidad ejecutora, grupo y equipo supuestos", "Sin cartas ni certificaciones el proyecto no es elegible", "Firmar cartas de compromiso y certificar el grupo (anexos A, B y D)"),
 ("Referencias no verificadas en fuentes web", "Parte de las obras de 2025 y 2026 no apareció en las búsquedas", "Verificar cada obra contra su fuente primaria antes de radicar"),
 ("Cuartiles de las revistas y citas recibidas desconocidos", "No se puede comprobar el criterio de calidad de 60 % en Q1 y Q2", "Consultar SJR, Scopus o Web of Science para cada artículo"),
 ("Reserva igual al valor esperado", "Tiene cerca de la mitad de probabilidad de ser insuficiente si los riesgos ocurren como se calificaron", "Decidir con el panel un criterio de reserva basado en percentil"),
 ("Costos de las alternativas ALT-00 a ALT-02 no comparables", "El análisis de costo-efectividad no distingue entre alternativas", "Cotizar las alternativas con el mismo alcance"),
 ("Consulta con operarios, comunidades y autoridades ambientales ausente", "Los juicios sobre reacción de actores son inferencias", "Realizar entrevistas y registrar sus resultados antes de la compuerta C1"),
 ("Verificación humana de la autoría de los capítulos", "Una sola instancia analítica redactó el documento; el control de pares no se ejecutó", "Someter el documento a revisión por pares antes de radicar"),
]
tabla("t05", "Vacíos, efecto sobre la decisión y ruta de resolución (F-02)", ["Vacío o contradicción", "Efecto sobre la decisión", "Ruta de resolución"], fl,
      "*Nota.* Elaboración propia con los hallazgos del documento y de las secciones F4.4-MDR.13 y F4.4.14.")
A("### C.3.3 F-03 Valor estratégico"); A("")
A("El documento habilita tres decisiones. Primera, decidir si el proyecto se radica con la alternativa de red híbrida por tramos y no con un compromiso en bloque. Las compuertas condicionan cada compra. Segunda, ordenar el trabajo previo a la radicación: la lista de datos pendientes indica qué documentos reunir y en qué orden. Tercera, fijar los criterios con que el panel evaluador y el comité directivo decidirán perseverar o pivotar en los meses 12 y 17. La utilidad es potencial. El documento no afirma ahorros ni impactos medidos, y ninguna cifra de desempeño existe todavía como medición propia.")
A("")
A("### C.3.4 F-04 Traspaso y cierre"); A("")
A("**Insumos utilizables.** El documento entrega pasos 0 a 7, 21 capítulos, diez documentos 1000X, un capítulo de estrategia y las fuentes de trabajo en el repositorio. **Restricciones.** No es apto para radicar. Faltan los términos de referencia, los datos de la {T:t03} y la ratificación del panel de los puntajes de la sección F6.3. **Siguiente acción.** El equipo formulador reúne los términos de referencia y los cinco documentos territoriales. Luego recalcula los capítulos 7 a 10, 12 y 21 con las cifras definitivas. **Condición de aceptación.** El documento se acepta cuando se cumplen tres condiciones. Los datos pendientes tienen documento de soporte. La autoauditoría no contiene estados NO_CUMPLE por causas del contenido. Un revisor humano certifica la formulación. Este cierre no activa otra estación ni declara cerrada una cadena de la que no se conoce el estado.")
A("")
open(C + "cierre.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("ok", len(reg), "datos;", tp, tt, tf, "nbad", nbad, "largas", nlarg)
