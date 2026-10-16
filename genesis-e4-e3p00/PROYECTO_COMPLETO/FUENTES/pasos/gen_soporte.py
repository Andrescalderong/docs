# -*- coding: utf-8 -*-
"""Parte inicial «Soporte de la solicitud»: alianza, roles, presupuesto por actor, beneficios, calendario y correo."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

R = D.resumen(); ID = D.IDENT
SGR, CON, TOT = R["sgr"], R["contra"], R["total"]
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- asignación de líneas SGR por actor (PROPUESTO)
UNI, ACT, EMP, MUN = "Universidad", "Actor reconocido", "Empresa aliada", "Municipio"
ASIG = {}
for i in ["P01", "P02", "P03", "P05", "P06", "P11", "P14", "E03", "E07", "E08", "M01", "M02", "M04", "M05", "M06",
          "S02", "S07", "V04", "V05", "O01", "O02", "O03", "O05", "O06", "X01"]: ASIG[i] = UNI
for i in ["P07", "P13", "S01", "S08", "S09"]: ASIG[i] = ACT
for i in ["P04", "P08", "P09", "P10", "P12", "E01", "E02", "E04", "E05", "E06", "E09", "E10", "E11", "E12", "M03", "M07",
          "S03", "S05", "S06", "S10", "S11", "V01", "V02", "V03"]: ASIG[i] = EMP
ids = [r["id"] for r in D.BUDGET if r["fuente"] == "SGR"]
assert set(ids) == set(ASIG), (set(ids) ^ set(ASIG))
tot_act = collections.OrderedDict((a, 0) for a in (UNI, ACT, EMP, MUN))
mat = {a: collections.OrderedDict((k, 0) for k in R["por_rubro"]) for a in tot_act}
for r in D.BUDGET:
    if r["fuente"] != "SGR": continue
    a = ASIG[r["id"]]; tot_act[a] += r["total"]; mat[a][r["rubro"]] += r["total"]
assert sum(tot_act.values()) == SGR
con_act = {UNI: sum(r["total"] for r in D.CONTRA if r["fuente"] == "IES"),
           EMP: sum(r["total"] for r in D.CONTRA if r["fuente"] == "EMP"), ACT: 0, MUN: 0}
assert sum(con_act.values()) == CON
pc = lambda v: num(v / SGR * 100, 1)

d = Doc("S")

# ---------------------------------------------------------------- S.2
d.h(2, "S.2 Qué pide el mensaje y dónde se responde")
d.p("El mensaje de la sección S.1 contiene nueve solicitudes. Cada una tiene una respuesta en esta parte inicial. La {T:t01} las relaciona con la sección que las contesta. La sección S.13 responde a una solicitud posterior: verificar el presupuesto frente a la Convocatoria 56. El equipo remitente no podrá participar en la formulación porque atiende otro proyecto. Por esa razón, el calendario de la sección S.9 asigna a la Universidad la entrega de datos y la validación. La redacción queda en este documento.")
d.tabla("t01", "Solicitudes del mensaje y sección que las responde",
        ["N.º", "Solicitud del mensaje", "Respuesta", "Sección"],
        [("1", "Presentación clara de qué es el proyecto", "Ficha de una página y justificación de la opción única", "S.3"),
         ("2", "Objetivo al que aporta cada aliado", "Objetivo específico, producto e indicador por actor", "S.5"),
         ("3", "Actividades que ejecuta cada actor", "Matriz de responsabilidades de las 17 actividades y lista por actor", "S.6"),
         ("4", "Presupuesto asociado a esas actividades y organizaciones", "Presupuesto SGR y contrapartida por actor y por rubro", "S.7"),
         ("5", "Opción más alineada al departamento y al terremoto", "Alternativa única recomendada y criterios de selección del departamento", "S.3 y S.4"),
         ("6", "Reunión con la Universidad", "Agenda con decisiones y datos que se necesitan", "S.10"),
         ("7", "Fechas claras del documento técnico completo", "Calendario del 16 de octubre al 3 de noviembre de 2026", "S.9"),
         ("8", "Beneficio que recibe cada actor", "Beneficios y obligaciones por actor", "S.8"),
         ("9", "Correo con la presentación", "Borrador listo para enviar", "S.11")],
        "*Nota.* Elaboración propia a partir del mensaje de la sección S.1. Los números de sección remiten a esta parte inicial.")

# ---------------------------------------------------------------- S.3
d.h(2, "S.3 El proyecto en una página")
d.p("El proyecto instala una red de 100 nodos de bajo costo y 10 gateways. La red mide material particulado (PM2,5 y PM10) en sitios de remoción de escombros posterremoto. Tres monitores gravimétricos de referencia, uno por departamento, permiten comparar cada nodo con una medición de referencia. El gateway corrige la lectura por humedad y por fracción gruesa. Un tablero y un protocolo de alerta ponen esa medición, con su error conocido, a disposición de los comités de gestión del riesgo. La {T:t02} resume los datos que cualquier aliado necesita para entender el proyecto.")
d.tabla("t02", "Ficha del proyecto para los aliados",
        ["Elemento", "Valor", "Naturaleza"],
        [("Título", ID["titulo"], "DECLARADO"),
         ("Convocatoria", "Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)", "DECLARADO"),
         ("Duración", "24 meses (104 semanas), con tres tramos y compuertas en los meses 12, 17 y 24", "PROPUESTO"),
         ("Territorio", "Caldas, Cundinamarca y Valle del Cauca; 12 municipios focalizados [DATO_USUARIO: lista]", "SUPUESTO"),
         ("Red", "100 nodos, 10 gateways y 3 monitores de referencia; se compran 120 nodos y 11 gateways", "PROPUESTO"),
         ("Resultado principal", "Al menos 75 % de 15 comités de gestión del riesgo usan el tablero en decisiones documentadas al mes 24 (PERS-E01)", "PROPUESTO"),
         ("Madurez tecnológica", "TRL 4 a TRL 7; el Anexo 2 prioriza TRL 9 y la decisión está pendiente", "PROPUESTO"),
         ("Valor solicitado al SGR", cop(SGR), "CALCULADO"),
         ("Contrapartida", cop(CON) + " (Universidad 1.100 M; empresa 1.010 M)", "DECLARADO"),
         ("Total del proyecto", cop(TOT), "CALCULADO"),
         ("Estado", "Borrador con vacíos; no es un paquete de radicación", "—")],
        "*Nota.* Elaboración propia con la ficha maestra del proyecto. La contrapartida de la Universidad es una reconstrucción PROPUESTA y la de la empresa es DECLARADA en el expediente E3. Certificaciones pendientes.")
d.p("El mensaje pide una sola opción y no tres. El documento recomienda la alternativa ALT-03, una red híbrida con corrección en el gateway, despliegue por tramos y custodia distribuida. Obtuvo 5,805 puntos en la escala de 1 a 9. La calibración centralizada obtuvo 5,150, el statu quo 4,475 y las estaciones fijas 4,335. El puntaje no equivale a una probabilidad de éxito. La alternativa responde a la emergencia por una razón física. El terremoto interrumpe la red eléctrica y la celular, y por eso el gateway almacena siete días de datos y conserva un enlace satelital alterno.")

# ---------------------------------------------------------------- S.4
d.h(2, "S.4 Conformación de la alianza")
d.p("La alianza propuesta tiene cuatro actores. El proponente es una universidad con un grupo de investigación reconocido por MinCiencias. Lo acompañan un municipio de Cundinamarca, Risaralda, Caldas o Valle del Cauca, un actor reconocido por MinCiencias y una empresa aliada. Los nombres quedan por definir [DATO_USUARIO: nombres de los cuatro actores]. La {T:t03} fija el perfil de cada actor y su posición en el análisis de participantes del Anexo 2.")
d.tabla("t03", "Actores de la alianza, perfil exigido y posición en el Anexo 2",
        ["Actor", "Identidad", "Perfil exigido", "Posición en el Anexo 2", "Estado"],
        [("Proponente", "[DATO_USUARIO: universidad]", "Institución de educación superior con grupo de investigación reconocido por MinCiencias en calidad del aire, instrumentación o ciencia de datos", "Cooperante: formula y ejecuta", "VACIO"),
         ("Municipio acompañante", "[DATO_USUARIO: municipio y departamento]", "Municipio afectado por la emergencia, con comité de gestión del riesgo activo", "Beneficiario", "VACIO"),
         ("Actor reconocido por MinCiencias", "[DATO_USUARIO: centro, instituto o grupo]", "Centro o instituto de CTeI, o grupo reconocido, con laboratorio o experiencia en metrología de partículas", "Cooperante", "VACIO"),
         ("Empresa aliada", "[DATO_USUARIO: empresa]", "Empresa con capacidad en hardware IoT, plataforma en la nube e instalación en campo", "Cooperante", "VACIO")],
        "*Nota.* Elaboración propia con el Anexo 2 de la convocatoria (secciones de entidades aliadas y de análisis de participantes). Los perfiles son PROPUESTOS. Las cinco categorías de puntuación del Anexo 2 son IES, centro o instituto de CTeI, instituto del SINA, corporación autónoma regional y sociedad civil organizada.")
d.p("El Anexo 2 impone una regla que condiciona al municipio. Una misma entidad no puede ser a la vez proponente o aliada (cooperante) y beneficiaria. Por tanto, el municipio acompañante figura como beneficiario y no recibe recursos del SGR. Si aportara recursos, pasaría a cooperante y perdería su posición de beneficiario. La ficha maestra ya registra que las alcaldías no aportan contrapartida, y este documento mantiene esa decisión (DEC-F19).")
d.p("La empresa plantea una segunda verificación. Las cinco categorías de puntuación del Anexo 2 no incluyen a las empresas. Los términos de referencia deben confirmar si una empresa puede ser aliada, si puntúa y si puede ejecutar líneas del presupuesto SGR. Si no pudiera, la empresa pasaría a proveedora por contratación, y su contrapartida de 1.010 millones de COP requeriría otro vehículo.")
d.p("La selección del departamento sigue cinco criterios, que la {T:t04} aplica a los cuatro departamentos mencionados. El primero es obligatorio: el municipio debe figurar entre los afectados por la emergencia. Los otros cuatro desempatan. Son la sede de la Universidad, la presencia del actor y de la empresa, la capacidad del comité y el acceso logístico.")
d.tabla("t04", "Departamentos candidatos para el municipio acompañante",
        ["Departamento", "Estado en la ficha maestra", "Criterio 1: afectación declarada", "Criterios 2 a 5"],
        [("Caldas", "Incluido: 33 nodos y 4 municipios (PROPUESTO)", "VACIO: confirmar municipios en el listado de la convocatoria", "VACIO: sede, actores, comité y acceso"),
         ("Cundinamarca", "Incluido: 34 nodos y 4 municipios (PROPUESTO)", "VACIO: confirmar municipios en el listado de la convocatoria", "VACIO: sede, actores, comité y acceso"),
         ("Valle del Cauca", "Incluido: 33 nodos y 4 municipios (PROPUESTO)", "VACIO: confirmar municipios en el listado de la convocatoria", "VACIO: sede, actores, comité y acceso"),
         ("Risaralda", "No incluido; lo propone el mensaje", "VACIO: confirmar que figura en el ámbito territorial de la emergencia", "VACIO: sede, actores, comité y acceso")],
        "*Nota.* Elaboración propia con la ficha maestra y el Anexo 2. El listado de municipios afectados no se aportó, por lo que ningún departamento puede puntuarse todavía.")
d.p("La recomendación es conservar el diseño de tres departamentos como base del documento. El presupuesto, las metas y las compuertas se calcularon para ese alcance. Reducirlo a un departamento obliga a recalcular nodos, comités y compuertas. El municipio acompañante se ubica en el departamento sede de la Universidad. Si la sede está en Risaralda, se verifica la declaratoria. Después se sustituye uno de los tres departamentos o se agrega Risaralda como cuarto, con el ajuste presupuestal correspondiente.")

# ---------------------------------------------------------------- S.5
d.h(2, "S.5 Objetivo, producto e indicador por actor")
d.p("Cada actor responde por un objetivo específico y por productos verificables. La Universidad responde ante el SGR por el objetivo general. La {T:t05} asigna a cada actor su objetivo principal, su aporte y los indicadores del marco PERS que lo miden.")
d.tabla("t05", "Objetivo específico, aporte e indicadores por actor",
        ["Actor", "Objetivo principal", "Aporte al objetivo", "Indicadores PERS"],
        [("Universidad", "OE1 y objetivo general", "Dirige el proyecto, calibra con el banco de laboratorio, entrena y valida el modelo de corrección, publica y forma jóvenes investigadores", "PERS-R02, PERS-R04, PERS-R06, PERS-P02, PERS-P03, PERS-P04"),
         ("Actor reconocido por MinCiencias", "OE1 (verificación independiente) y OE3 (formación)", "Aporta referencias gravimétricas, análisis de laboratorio, ensayo de desempeño y formación de custodios", "PERS-R05, PERS-E03"),
         ("Empresa aliada", "OE2", "Fabrica y compra los nodos y gateways, desarrolla el firmware y la plataforma, instala la red y opera la nube", "PERS-R01, PERS-R03, PERS-P01"),
         ("Municipio acompañante", "OE3", "Propone sitios, gestiona permisos y acceso, co-diseña los umbrales, usa el tablero y recibe la custodia", "PERS-E01, PERS-E02, PERS-S01, PERS-S02")],
        "*Nota.* Elaboración propia con los objetivos específicos de la ficha maestra y los 15 indicadores PERS. La asignación de indicadores a actores es PROPUESTA.")

# ---------------------------------------------------------------- S.6
d.h(2, "S.6 Actividades por actor")
d.p("La {T:t06} asigna a cada actor un nivel de responsabilidad en las 17 actividades del cronograma. La letra A designa al actor que responde por el resultado, y la Universidad la lleva en todas las actividades por ser proponente. La letra R designa a quien ejecuta. La letra C designa a quien aporta antes de decidir, y la letra I designa a quien recibe el resultado. En las compuertas C1 y C2 decide el comité directivo y la Universidad convoca.")
RA = {"A0.1": ("A/R", "C", "R", "C"), "A1.1": ("A", "R", "C", "R"), "A2.1": ("A", "I", "R", "C"), "A1.2": ("A", "R", "R", "I"),
      "A2.2": ("A", "I", "R", "I"), "A1.3": ("A/R", "R", "R", "C"), "A3.1": ("A/R", "C", "C", "R"), "A1.4": ("A/R", "R", "C", "I"),
      "C1": ("R", "C", "C", "C"), "A2.3": ("A", "I", "R", "R"), "A1.5": ("A/R", "R", "C", "I"), "A3.2": ("A", "C", "C", "R"),
      "C2": ("R", "C", "C", "C"), "A2.4": ("A", "I", "R", "R"), "A3.3": ("A", "R", "C", "R"), "A1.6": ("A", "R", "C", "I"),
      "A3.4": ("A/R", "R", "R", "R")}
filas = []
for aid, nom, sem, pred, wp in D.ACT:
    u, a, e, m = RA[aid]; filas.append((f"{aid} {nom}", str(sem), u, a, e, m))
assert len(filas) == 17
d.tabla("t06", "Responsabilidad de cada actor en las 17 actividades",
        ["Actividad", "Sem.", "Univ.", "Actor MinC.", "Empresa", "Municipio"], filas,
        "*Nota.* Elaboración propia con el cronograma de la ficha maestra (duración en semanas). A: aprueba y responde; R: ejecuta; C: consultado; I: informado. La asignación es PROPUESTA y se ratifica en la reunión con la Universidad. Univ.: Universidad. Actor MinC.: actor reconocido por MinCiencias.")
d.p("La {T:t07} traduce la matriz en lo que hace cada actor y en lo que entrega. Esa descripción es la que MinCiencias evaluará con mayor detalle, según el mensaje. Cada entregable tiene un hito de verificación en el cronograma del proyecto.")
d.tabla("t07", "Qué ejecuta y qué entrega cada actor",
        ["Actor", "Actividades que ejecuta", "Entregables verificables"],
        [("Universidad", "Gerencia y convenios (A0.1); colocalización y calibración en el piloto (A1.3); entrenamiento y validación del modelo (A1.4 y A1.5); co-diseño de umbrales con los comités (A3.1); convocatoria de compuertas; cierre y evaluación (A3.4)", "Convenios firmados; línea base de error medida; modelo validado con R² ≥ 0,70 y NRMSE ≤ 30 %; actas de compuerta; 2 artículos Q1 o Q2; informe de cierre"),
         ("Actor reconocido por MinCiencias", "Diseño de la colocalización con referencias gravimétricas (A1.1); caracterización de referencias (A1.2); verificación en cada departamento (A1.3 y A1.5); ensayo independiente de desempeño (A1.6); formación de custodios (A3.3)", "Base de datos de colocalización; informe de laboratorio; informe del ensayo de desempeño; 60 personas certificadas"),
         ("Empresa aliada", "Arquitectura de enlace y energía (A2.1); firmware y plataforma (A2.2); adquisición de nodos (A1.2); instalación de los tramos 2 y 3 (A2.3 y A2.4); operación de la nube y del gemelo digital", "Diseño de enlace y energía; plataforma operativa; 100 nodos y 10 gateways instalados; disponibilidad de nodos ≥ 90 %; software registrado"),
         ("Municipio acompañante", "Propuesta de sitios y permisos (A1.1); acceso y seguridad de los sitios (A2.3 y A2.4); co-diseño de umbrales (A3.1); uso del tablero (A3.2); convenio de custodia (A3.3 y A3.4)", "Listado de sitios autorizados; actas de uso del tablero en decisiones; convenio de custodia firmado")],
        "*Nota.* Elaboración propia con la matriz de la {T:t06} y los indicadores PERS de la ficha maestra. La operación de la nube y del gemelo digital se ejecuta durante los 24 meses en las líneas del presupuesto de la empresa.")

# ---------------------------------------------------------------- S.7
d.h(2, "S.7 Presupuesto por actor")
d.p("El mensaje pide verificar el presupuesto sobre las actividades de cada organización. Para ello, cada una de las 54 líneas del presupuesto SGR se asignó al actor que la ejecuta técnicamente. La {T:t08} muestra el resultado por rubro y la {T:t09} resume el total y la contrapartida. La asignación por línea se encuentra en la {T:t10}.")
rub = list(R["por_rubro"].keys())
cab = ["Actor", "Personal", "Equipos y software", "Materiales", "Servicios técnicos", "Viajes", "Otros", "Reserva", "Total"]
fil = []
for a in tot_act:
    fil.append((a,) + tuple(mm(mat[a][k]) for k in rub) + (mm(tot_act[a]),))
fil.append(("Total SGR",) + tuple(mm(R["por_rubro"][k]) for k in rub) + (mm(SGR),))
d.tabla("t08", "Presupuesto SGR por actor y por rubro (millones de COP)", cab, fil,
        "*Nota.* Elaboración propia con las 54 líneas del presupuesto SGR de la ficha maestra (CALCULADO). La asignación de cada línea a un actor es PROPUESTA. El municipio no recibe recursos SGR por su posición de beneficiario.")
d.tabla("t09", "Total por actor: recursos SGR y contrapartida",
        ["Actor", "SGR (M COP)", "% del SGR", "Contrapartida (M COP)", "Naturaleza de la contrapartida"],
        [(a, mm(tot_act[a]), pc(tot_act[a]), mm(con_act[a]), n) for a, n in
         [(UNI, "En especie, 1.100 M (reconstruida)"), (ACT, "VACIO: no declarada"), (EMP, "210 M en efectivo y 800 M en especie (DECLARADO)"), (MUN, "VACIO: sin aporte por regla del Anexo 2")]]
        + [("Total", mm(SGR), "100,0", mm(CON), "Certificaciones pendientes")],
        "*Nota.* Elaboración propia con la ficha maestra (CALCULADO). La reserva de contingencia de 636 M se asigna a la Universidad como proponente y se libera por decisión del comité directivo.")
filas = []
for r in D.BUDGET:
    if r["fuente"] != "SGR": continue
    filas.append((r["id"], r["concepto"], r["rubro"], ASIG[r["id"]], mm(r["total"])))
d.tabla("t10", "Asignación de las 54 líneas del presupuesto SGR a cada actor",
        ["Id", "Concepto", "Rubro", "Actor", "Valor (M COP)"], filas,
        "*Nota.* Elaboración propia con las líneas del presupuesto SGR de la ficha maestra. La columna Actor es PROPUESTA: indica quién ejecuta técnicamente la línea. La contratación formal depende de las reglas del SGR y de los términos de referencia.")
d.p("Tres conclusiones se desprenden de la {T:t09}. La primera: la empresa recibe " + pc(tot_act[EMP]) + " % del SGR y aporta 1.010 millones de COP. La relación entre ambas cifras debe validarse con sus costos reales [DATO_USUARIO: costos de la empresa]. La segunda: la Universidad concentra " + pc(tot_act[UNI]) + " % por la gerencia, la administración y la reserva. La tercera: el actor reconocido recibe " + pc(tot_act[ACT]) + " %, una participación que su perfil y su capacidad real pueden aumentar o reducir.")

# ---------------------------------------------------------------- S.8
d.h(2, "S.8 Beneficio que recibe cada actor")
d.p("Los aliados preguntan qué ganan. La {T:t11} responde con datos del proyecto y declara lo que todavía no está definido. Ningún beneficio incluye afirmaciones sobre efectos en salud, porque el proyecto produce mediciones, uso institucional y continuidad.")
d.tabla("t11", "Beneficios y obligaciones por actor",
        ["Actor", "Qué recibe", "Qué asume", "Aún no definido"],
        [("Universidad", "Financiación de 24 meses de investigación aplicada por " + mm(tot_act[UNI], 0) + " M; 6 jóvenes investigadores, 2 maestrantes y 1 doctor posdoctoral; 2 artículos Q1 o Q2; un software registrado; banco de calibración y monitores de referencia", "Responde ante el SGR por el proyecto; aporta 1.100 M en especie; administra y rinde cuentas", "Titularidad de la propiedad intelectual; destino de los equipos al cierre"),
         ("Actor reconocido por MinCiencias", "Financiación de " + mm(tot_act[ACT], 0) + " M por verificación y formación; coautoría de los artículos; uso del banco de datos de colocalización; reconocimiento como laboratorio de referencia", "Entrega verificaciones independientes y certifica a 60 personas", "Contrapartida; modalidad de contratación"),
         ("Empresa aliada", "Ejecución de " + mm(tot_act[EMP], 0) + " M; producto probado de TRL 4 a TRL 7 en entorno operativo; 15 comités como referencia; unidad de expansión con costo marginal de 120,08 M por gateway con 10 nodos", "Aporta 210 M en efectivo y 800 M en especie; responde por la plataforma y la instalación", "Titularidad de la propiedad intelectual; margen neto; condiciones de explotación posterior"),
         ("Municipio acompañante", "Red de nodos en su territorio sin costo SGR para el municipio; tablero y protocolo de alerta; formación de 10 funcionarios por comité; 5.000 cartillas y 3.000 mascarillas N95 para el proyecto", "Autoriza sitios, facilita el acceso, usa el tablero y asume la custodia al cierre", "Costo de sostenimiento (NO_CALCULABLE); capacidad de absorción")],
        "*Nota.* Elaboración propia con la ficha maestra, la {T:t09} y la ruta de escala del capítulo 14. Las cifras monetarias son CALCULADAS y los beneficios cualitativos son PROPUESTOS. Valores en millones de COP (M).")
d.p("En una frase por actor, la respuesta a la pregunta «y yo qué gano» es la siguiente. La Universidad gana capacidad de investigación, formación y publicaciones. El actor reconocido gana un papel de referencia metrológica. La empresa gana un producto validado y una cartera de comités. El municipio gana una medición con error conocido y la capacidad de usarla, a cambio de custodiar la red.")

# ---------------------------------------------------------------- S.9
d.h(2, "S.9 Calendario hacia el documento técnico completo")
d.p("La radicación cierra el 3 de noviembre de 2026 a las 4:00 p. m. El usuario confirmó la fecha el 16 de octubre, y la guía financiera de la Convocatoria 56 coincide. Este calendario parte de ella. Los términos de referencia completos deben ratificarla [DATO_USUARIO: confirmación en los términos de referencia].")
d.p("Desde el 16 de octubre quedan 18 días calendario hasta el cierre. El 2 de noviembre es probablemente festivo por el traslado de Todos los Santos. La {T:t12} fija fechas de entrega para que el documento técnico exista cuatro días hábiles antes del cierre.")
d.tabla("t12", "Calendario propuesto del 16 de octubre al 3 de noviembre de 2026",
        ["Fecha", "Hito", "Responsable", "Entregable"],
        [("Vie 16 oct", "Envío del correo con la presentación y este borrador", "Persona usuaria", "Correo y documento"),
         ("Lun 19 oct", "Reunión con la Universidad", "Persona usuaria y Universidad", "Decisiones D1 a D9 de la sección S.10"),
         ("Mié 21 oct", "Datos de la Universidad y confirmación de los cuatro actores", "Universidad", "Nombre, grupos, investigadores, certificación de contrapartida"),
         ("Vie 23 oct", "Decisiones presupuestales de la sección S.13 y solicitud de cotizaciones", "Universidad y empresa", "Presupuesto ajustado y cotizaciones solicitadas"),
         ("Mar 27 oct", "Cartas de intención, lista de municipios y reportes de afectación", "Universidad y municipio", "Cartas en borrador; lista de municipios afectados"),
         ("Mié 28 oct", "Congelamiento de datos y recepción de cotizaciones", "Universidad y empresa", "Al menos dos cotizaciones por rubro; Anexo 3 diligenciado"),
         ("Jue 29 oct", "Documento técnico completo v1.0", "Persona usuaria", "Documento y Anexo 3 sin datos pendientes; verificadores ejecutados"),
         ("Vie 30 oct", "Revisión cruzada, firma del representante legal y carga de prueba en SIGP", "Los cuatro actores", "Comentarios cerrados; archivos dentro de los límites de tamaño"),
         ("Lun 2 nov", "Festivo probable: sin actividades", "—", "—"),
         ("Mar 3 nov", "Radicación antes de las 12:00 m.", "Universidad", "Proyecto radicado; cierre a las 4:00 p. m.")],
        "*Nota.* Elaboración propia. Fechas PROPUESTAS; los días de la semana se verificaron con el calendario de 2026. La fecha de cierre es DECLARADA por el usuario y coincide con la guía financiera de la Convocatoria 56. El festivo del 2 de noviembre queda NO_VERIFICADO.")
d.p("La regla de control es sencilla. Ningún dato posterior al 28 de octubre cambia la estructura del documento. Los datos tardíos se incorporan como anexos o como notas de corrección. El plazo no admite subsanar la ausencia de cotizaciones ni de memorias de cantidades después del cierre.")

# ---------------------------------------------------------------- S.10
d.h(2, "S.10 Agenda de la reunión con la Universidad")
d.p("La reunión del 19 de octubre busca nueve decisiones. La {T:t13} las enumera con el motivo por el cual cada una condiciona el documento. La reunión dura 90 minutos y termina con un acta que asigna responsable y fecha a cada dato pendiente.")
d.tabla("t13", "Decisiones y datos que se requieren de la Universidad",
        ["N.º", "Decisión o dato", "Por qué condiciona el documento"],
        [("D1", "Nombre de la universidad, grupo(s) de investigación y categoría vigente en MinCiencias", "El proponente debe contar con un grupo de investigación, según los términos de referencia"),
         ("D2", "Departamento sede y municipio acompañante", "Fija el territorio, los sitios y el comité beneficiario"),
         ("D3", "Actor reconocido por MinCiencias, su papel y su contrapartida", "Cada integrante de la alianza debe comprometer una contrapartida"),
         ("D4", "Empresa aliada, contrapartida y forma de contratación", "Determina si la empresa puede ejecutar líneas del SGR"),
         ("D5", "Certificación de la contrapartida de 1.100 millones de COP", "El expediente no la soporta y el riesgo R-FIN-02 la menciona"),
         ("D6", "Titularidad de la propiedad intelectual y destino de los equipos", "Condiciona el beneficio de cada actor y la cláusula de apertura"),
         ("D7", "Nivel de madurez tecnológica objetivo: TRL 7 o TRL 9", "El Anexo 2 prioriza TRL 9 y el proyecto compromete TRL 7"),
         ("D8", "Términos de referencia completos y anexos de la convocatoria", "Sin ellos, la estructura, los topes y el puntaje siguen parcialmente supuestos"),
         ("D9", "Cotizaciones y contrapartida del actor reconocido, y ratificación de los ajustes de la sección S.13", "Las cotizaciones sustentan los precios y la contrapartida es exigida a cada integrante")],
        "*Nota.* Elaboración propia. Los términos de referencia completos, el Plan de Desarrollo y los demás anexos no se aportaron al proyecto (NO_VERIFICADO).")

# ---------------------------------------------------------------- S.11
d.h(2, "S.11 Borrador del correo")
d.p("El texto siguiente responde a la solicitud de la sección S.1. Puede enviarse sin cambios una vez se completen los nombres entre corchetes.")
d.raw(f"""**Asunto:** Proyecto SGR_CONV56_AIRE: qué es, qué hace cada aliado, presupuesto y calendario.

Hola [DATO_USUARIO: nombre del destinatario],

Gracias por tu mensaje. Aquí está la presentación que pediste, con una sola opción: la más alineada con la emergencia del terremoto.

**1. Qué es el proyecto.** Una red de 100 nodos de bajo costo y 10 gateways mide PM2,5 y PM10 en sitios de remoción de escombros. Corrige el error de cada medición. Entrega un tablero y un protocolo de alerta a 15 comités de gestión del riesgo. Dura 24 meses. Solicita {num(SGR)} COP al SGR y suma {num(CON)} COP de contrapartida. El presupuesto ya está ajustado a las reglas de la convocatoria (sección S.13).

**2. Alianza propuesta.** La Universidad, con su grupo de investigación reconocido por MinCiencias, es la proponente. La acompañan un municipio beneficiario, un actor reconocido por MinCiencias y una empresa aliada.

**3. Objetivo de cada aliado.** La Universidad responde por la calibración y la validación del modelo. El actor reconocido verifica de forma independiente y forma a los custodios. La empresa instala y opera la red y la plataforma. El municipio usa el tablero y recibe la custodia.

**4. Actividades y presupuesto.** El documento adjunto asigna a cada actor las 17 actividades y las {len(ids)} líneas del presupuesto (secciones S.6 y S.7).

**5. Beneficio de cada actor.** Está en la sección S.8, con lo que cada uno recibe y lo que asume.

**6. Fechas.** La radicación cierra el 3 de noviembre a las 4:00 p. m. Por eso el documento técnico completo estará listo el 29 de octubre. Los cuatro actores lo revisan y firman el 30 de octubre. La radicación se prevé el 3 de noviembre antes del mediodía.

**7. Lo que necesitamos.** Una reunión con la Universidad el 19 de octubre. Necesitamos también los datos de la sección S.10 antes del 21 de octubre. Y, de cada aliado, al menos dos cotizaciones por rubro antes del 28 de octubre.

Quedo atento.

[DATO_USUARIO: firma]""")

# ---------------------------------------------------------------- S.12
d.h(2, "S.12 ¿Qué se me escapa?")
d.p("Cinco vacíos pueden afectar la propuesta. La {T:t14} los relaciona con su riesgo y con una ruta de solución. El riesgo mayor es de calendario. Si la Universidad entrega los datos después del 28 de octubre, el documento llegaría al cierre sin certificaciones, cotizaciones ni cartas.")
d.tabla("t14", "Vacíos de la alianza, riesgo y ruta de solución",
        ["Vacío", "Riesgo si no se resuelve", "Ruta de solución"],
        [("Términos de referencia completos no aportados", "La estructura, los topes y el puntaje siguen parcialmente supuestos", "Obtenerlos en la reunión del 19 de octubre; hoy solo se consultó la guía financiera y el Anexo 3"),
         ("La empresa no figura entre las categorías de puntuación", "La empresa podría no ser aliada ni ejecutar líneas del SGR", "Confirmar con los términos; si no procede, contratarla como proveedora"),
         ("El municipio como beneficiario no puede aportar recursos", "Un aporte municipal lo convierte en cooperante", "Mantener cartas de apoyo sin aporte económico"),
         ("Risaralda no está en la ficha maestra", "El territorio podría quedar fuera del ámbito de la emergencia", "Verificar la declaratoria antes de definir la sede"),
         ("El actor reconocido sin contrapartida ni papel pactado", "La verificación independiente quedaría sin responsable", "Acordar el papel y su valor en la reunión con la Universidad")],
        "*Nota.* Elaboración propia con el Anexo 2, la guía financiera de la Convocatoria 56, la ficha maestra y los registros DEC-F del proyecto.")
d.p("El premortem identifica una causa probable de fracaso: la Universidad no puede certificar la contrapartida o el grupo no tiene categoría vigente. La contingencia es preparar desde ya una segunda universidad candidata y reservar el 28 de octubre como fecha límite para decidir el cambio.")
d.p("El valor estratégico de esta parte es doble. Responde las nueve solicitudes del mensaje en un solo lugar y convierte los roles de los actores en tablas verificables. Con ello reduce el riesgo de que MinCiencias detecte ambigüedad en las funciones y el presupuesto de cada organización.")
d.p("La decisión DEC-F19 registra tres hechos. La alianza propuesta tiene cuatro actores. El municipio es beneficiario sin aporte. El presupuesto se asigna por actor de forma PROPUESTA. Esa decisión queda sujeta a la ratificación de la Universidad.")

# ---------------------------------------------------------------- S.13
import importlib.util
_spec = importlib.util.spec_from_file_location("maestro_old", os.path.join(RAIZ, "maestro", "maestro_old.py"))
OLD = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(OLD)
O_SGR = OLD.resumen()["sgr"]
RUB = {i + 1: n for i, n in enumerate(D.RUBROS11)}
t11 = collections.OrderedDict((k, 0) for k in RUB)
lineas11 = collections.defaultdict(list)
for r in D.BUDGET:
    if r["fuente"] != "SGR": continue
    k = D.RUBROS11.index(r["rubro11"]) + 1; t11[k] += r["total"]; lineas11[k].append(r["id"])
assert sum(t11.values()) == SGR
mov = sum(r["total"] for r in D.BUDGET if r["id"] in ("V01", "V02", "V03", "V04"))
mov_old = sum(r["total"] for r in OLD.BUDGET if r["id"] in ("V01", "V02", "V03", "V04"))
seg_old = sum(r["total"] for r in OLD.BUDGET if r["id"] in ("S04", "O04"))
p03_old = [x for x in OLD.BUDGET if x["id"] == "P03"][0]["total"]; p03 = [x for x in D.BUDGET if x["id"] == "P03"][0]["total"]
resv = [x for x in D.BUDGET if x["id"] == "X01"][0]["total"]
assert mov <= 0.02 * SGR, (mov, 0.02 * SGR)
EMV = {"R-TEC-01": 2, "R-TEC-02": 2, "R-EXT-02": 2, "R-FIN-01": 2, "R-TEC-03": 4, "R-TEC-04": 4, "R-DAT-01": 4, "R-ORG-01": 3, "R-ORG-02": 3,
       "R-JUR-01": 6, "R-EXT-01": 11, "R-FIN-02": 11}
emv_rub = collections.defaultdict(float)
for rk in D.RISKS: emv_rub[EMV[rk["id"]]] += rk["emv"]
assert abs(sum(emv_rub.values()) - sum(rk["emv"] for rk in D.RISKS)) < 1

d.h(2, "S.13 Verificación del presupuesto frente a la Convocatoria 56")
d.p("La guía financiera de la Convocatoria 56 y el Anexo 3 oficial permiten verificar el presupuesto. El Anexo 3 se descargó del portal de MinCiencias y se leyó su hoja de resumen. Los términos de referencia completos no se consultaron. Algunas cifras de la guía son ejemplos ilustrativos. El presupuesto original incumplía cinco exigencias. El usuario decidió ajustarlo el 16 de octubre. La {T:t15} resume las 20 verificaciones con su estado inicial, el ajuste aplicado y el resultado actual.")
V = [
 ("1", "Monto SGR hasta 14.000 millones de COP", cop(O_SGR) + " (66,2 %)", "Ninguno", "CUMPLE: " + cop(SGR) + " (" + num(SGR / 14e9 * 100, 1) + " %)"),
 ("2", "Duración hasta 24 meses", "24 meses", "Ninguno", "CUMPLE"),
 ("3", "Contrapartida en efectivo de al menos 1 % del SGR para obtener puntos", "Efectivo de 210 millones de COP", "Ninguno", "CUMPLE: " + num(210_000_000 / SGR * 100, 2) + " % del SGR"),
 ("4", "6 jóvenes investigadores con apoyo de 2.000.000 COP por 12 meses", "P01: 144 millones de COP", "Ninguno", "CUMPLE; la edad máxima de 28 años se verifica (diferencia entre TdR y Anexo 12)"),
 ("5", "2 estudiantes de maestría con apoyo de 4.350.000 COP y matrícula hasta 48 millones de COP", "P02: apoyo de 208,8 y matrícula de 96 millones de COP", "Ninguno", "CUMPLE"),
 ("6", "1 doctor en estancia posdoctoral con apoyo de 12.920.000 COP", "No había línea; P03 era un científico de datos senior de 480 millones de COP", "P03 pasa a posdoctorado: 24 meses × 12,92 millones de COP = " + num(p03 / 1_000_000, 2) + " millones de COP", "CUMPLE; el perfil exige uno o dos productos TOP según el documento (diferencia entre TdR y Anexo 12)"),
 ("7", "Movilidad financiada por el SGR hasta 2 % del monto solicitado", "V01 a V04: " + cop(mov_old) + " (" + num(mov_old / O_SGR * 100, 2) + " %)", "Viajes reducidos a " + cop(mov) + "; el complemento lo cubre la logística de emergencia de la empresa (C05)", "CUMPLE: " + num(mov / SGR * 100, 2) + " % del SGR"),
 ("8", "Seguros excluidos de la financiación", "S04 y O04 sumaban " + cop(seg_old), "Líneas retiradas del SGR; la entidad ejecutora asume los seguros", "CUMPLE"),
 ("9", "Imprevistos asociados al análisis de riesgos y soportados en el análisis de costos", "Reserva de " + cop(resv) + ", igual a la suma de los valores esperados de 12 riesgos", "Se ubica en el rubro 11 y se asocia por rubro (Tabla S.18)", "CUMPLE; falta la memoria de cálculo firmada"),
 ("10", "Cada integrante de la alianza debe comprometer contrapartida", "Universidad y empresa sí; el actor reconocido no", "Se deja en blanco por decisión del usuario", "PENDIENTE"),
 ("11", "Rubros del Anexo 3: 11 categorías oficiales", "El presupuesto usaba 7 categorías propias", "Cada línea tiene un rubro oficial (Tabla S.16)", "CUMPLE"),
 ("12", "Seguimiento con cálculo objetivo y sin porcentaje arbitrario", "O05 asigna 15 millones de COP al mes sin memoria de cálculo", "Ninguno", "PARCIAL: faltan actividades, perfiles y dedicaciones"),
 ("13", "Software, nube y conectividad recurrentes: precisar financiabilidad y sostenibilidad", "E10, E11, E12 y S10 suman " + cop(sum(x["total"] for x in D.BUDGET if x["id"] in ("E10", "E11", "E12", "S10"))), "Ninguno", "PARCIAL: justificar el uso durante el proyecto y asignar la operación posterior"),
 ("14", "Sin doble financiación de una misma actividad", "C05 de la empresa cubre logística y viáticos; V01 a V03 también", "Los viajes del SGR se limitan al 2 %; C05 cubre el resto", "PENDIENTE: separar por escrito los viajes de cada fuente"),
 ("15", "Presupuesto completo, sin depender de financiación futura indispensable", "La custodia posterior depende de partidas de los custodios (R-ORG-02)", "Ninguno", "PENDIENTE: documentar partidas y convenios de custodia"),
 ("16", "Análisis de costos con dos cotizaciones por rubro", "Los precios son DECLARADOS o PROPUESTOS; no hay cotizaciones", "Se dejan en blanco por decisión del usuario", "PENDIENTE: el Anexo 3 las pide después de la lista de elegibles y el Anexo 14 no admite subsanar su ausencia"),
 ("17", "Anexo 3 oficial en Excel, con fecha y firma del representante legal", "El presupuesto está en el formato del proyecto", "Diligenciar el Excel queda para después, por decisión del usuario", "PENDIENTE"),
 ("18", "Coherencia de valores entre SIGP, Anexos 1, 2 y 3 y la MGA", "Los valores salen de una sola ficha maestra", "Todos los capítulos se actualizaron con el presupuesto ajustado", "CUMPLE; reconciliar con SIGP y la MGA al cargar"),
 ("19", "Honorarios de formulación no financiables", "El presupuesto no incluye honorarios de formulación", "Ninguno", "CUMPLE"),
 ("20", "Archivos en PDF de 3 MB como máximo; adjuntos comprimidos hasta 10 MB", "El expediente completo pesa 30 MB en Word y 53 MB en PDF", "El documento técnico de 30 secciones se entrega aparte: PDF de 0,9 MB", "CUMPLE con el documento técnico; el expediente va comprimido"),
]
est = [v[4].split(":")[0].split(";")[0].strip() for v in V]
n_ok = sum(1 for e in est if e.startswith("CUMPLE")); n_par = sum(1 for e in est if e.startswith("PARCIAL")); n_pen = sum(1 for e in est if e.startswith("PENDIENTE"))
assert (n_ok, n_par, n_pen) == (13, 2, 5), (n_ok, n_par, n_pen)
d.tabla("t15", "Verificación del proyecto frente a la Convocatoria 56",
        ["N.º", "Exigencia", "Estado inicial", "Ajuste aplicado", "Resultado actual"], V,
        "*Nota.* Elaboración propia con la guía financiera de la Convocatoria 56 (corte 16 de octubre de 2026) y el Anexo 3 oficial. Las exigencias son NO_VERIFICADAS frente a los términos de referencia completos. Resultado actual: 13 cumplen, 2 cumplen parcialmente y 5 están pendientes de datos que solo la alianza aporta.")
d.p("La {T:t16} presenta el presupuesto en los 11 rubros del Anexo 3. El rubro de infraestructura queda en cero, porque el proyecto no adecúa infraestructura. El rubro de administrativos queda en cero, porque la administración se registra en seguimiento. Cada línea del presupuesto maestro conserva su rubro oficial.")
d.tabla("t16", "Presupuesto SGR en los 11 rubros del Anexo 3",
        ["N.º", "Rubro del Anexo 3", "Líneas del proyecto", "Valor SGR (M COP)", "% del SGR"],
        [(str(k), RUB[k], ", ".join(lineas11[k]) or "—", mm(t11[k]), pc(t11[k])) for k in RUB]
        + [("", "Total", str(len(ids)) + " líneas", mm(SGR), "100,0")],
        "*Nota.* Elaboración propia con la ficha maestra y la hoja RESUMEN del Anexo 3. La asignación de cada línea a un rubro es PROPUESTA. El expediente conserva sus siete categorías internas de formulación (capítulo 8).")
d.p("La {T:t17} muestra los cuatro ajustes aplicados. El presupuesto SGR baja a " + cop(SGR) + ". La reserva se conserva y se asocia a los rubros mediante la {T:t18}.")
d.tabla("t17", "Ajustes aplicados al presupuesto SGR",
        ["Concepto", "Antes (M COP)", "Después (M COP)", "Diferencia (M COP)", "Motivo"],
        [("Seguros (S04 y O04)", mm(seg_old), "0,0", "−" + mm(seg_old), "La convocatoria excluye los seguros"),
         ("Posdoctorado en lugar de científico de datos senior (P03)", mm(p03_old), mm(p03), "−" + mm(p03_old - p03), "Perfil y valor fijados por los numerales 9 y 14.4"),
         ("Movilidad financiada por el SGR (V01 a V04)", mm(mov_old), mm(mov), "−" + mm(mov_old - mov), "Tope de 2 % del valor solicitado"),
         ("Reserva de contingencia (X01)", mm(resv), mm(resv), "0,0", "Se conserva en el rubro 11, asociada al análisis de riesgos"),
         ("Presupuesto SGR", mm(O_SGR), mm(SGR), "−" + mm(O_SGR - SGR), "Tope de 14.000 millones de COP: se cumple"),
         ("Contrapartida", mm(CON), mm(CON), "0,0", "Sin cambios; el actor reconocido queda en blanco")],
        "*Nota.* Elaboración propia (CALCULADO). Si los términos de referencia aclaran que el tope de 2 % no se aplica a los viajes de campo, el proyecto restituye " + mm(mov_old - mov) + " millones de COP en viajes.")
d.tabla("t18", "Reserva de contingencia asociada a los rubros del Anexo 3",
        ["Rubro asociado", "Riesgos que la justifican", "Valor esperado (M COP)"],
        [("Equipos y software", "R-TEC-01, R-TEC-02, R-EXT-02 y R-FIN-01", mm(emv_rub[2])),
         ("Servicios tecnológicos y pruebas", "R-TEC-03, R-TEC-04 y R-DAT-01", mm(emv_rub[4])),
         ("Capacitación y eventos", "R-ORG-01 y R-ORG-02", mm(emv_rub[3])),
         ("Protección del conocimiento y divulgación", "R-JUR-01", mm(emv_rub[6])),
         ("Otros", "R-EXT-01 y R-FIN-02", mm(emv_rub[11])),
         ("Total (la reserva se redondea a " + mm(resv) + ")", "12 riesgos", mm(sum(emv_rub.values())))],
        "*Nota.* Elaboración propia con el análisis de riesgos del capítulo 10. El valor esperado es probabilidad por impacto (CALCULADO). La reserva se registra en una sola línea del rubro 11 (Otros).")
d.p("Quedan cinco pendientes que solo la alianza resuelve. Primero, la contrapartida del actor reconocido. Segundo, el soporte de que los viajes del SGR y la logística de la empresa no se duplican. Tercero, las partidas de custodia. Cuarto, las cotizaciones. Quinto, el Anexo 3 en Excel firmado. El proyecto no puede radicarse mientras esos cinco puntos sigan abiertos.")

d.guardar(os.path.join(RAIZ, "caps", "soporte.md"))
print("md ok", {k: mm(v) for k, v in tot_act.items()})
