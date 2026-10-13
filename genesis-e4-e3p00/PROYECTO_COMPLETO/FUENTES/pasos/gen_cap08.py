# -*- coding: utf-8 -*-
import sys, os, re, collections, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

d = Doc("8")
M = D.M
R = D.resumen()
SGR, CON, TOT = R["sgr"], R["contra"], R["total"]
sgr = [r for r in D.BUDGET if r["fuente"] == "SGR"]
porrubro = collections.OrderedDict((k, v) for k, v in D.bud_rows(sgr).items())
def pct(x, base, dec=1): return num(100 * x / base, dec)
def limpia(t): return re.sub(r"\(Tabla 8\.\d\)|Tabla 8\.\d", "tabla del expediente E3", t)
def natsum(rows, nat): return sum(r["total"] for r in rows if r["nat"] == nat)
def tab_lineas(tid, titulo, rubro, nota_extra=""):
    rows = porrubro[rubro]
    fil = []
    for r in rows:
        fil.append((r["id"], r["concepto"], f"{num(r['cant'], 0 if float(r['cant']).is_integer() else 1)} {r['unidad']}", cop(r["vunit"]), cop(r["total"]),
                    r["nat"], r["wbs"], f"{r['m_ini']}–{r['m_fin']}", limpia(r["just"])))
    fil.append(("Total", f"Subtotal de {rubro.lower()}", "", "", cop(D.total(rows)), "CALCULADO", "", "", f"{pct(D.total(rows), SGR)} % del valor solicitado al SGR"))
    d.tabla(tid, titulo, ["Id", "Concepto", "Cantidad y unidad", "Costo unitario (COP)", "Total (COP)", "Naturaleza", "WP", "Meses", "Justificación"], fil,
            "*Nota.* Elaboración propia con datos del libro maestro (maestro.py, líneas del presupuesto SGR) y de la ficha maestra §5. DECLARADO: valor del expediente E3 sin verificación; PROPUESTO: decisión de esta formulación, sujeta a cotización y a ratificación; CALCULADO: producto de cantidad por costo unitario. Los costos unitarios no incluyen cotizaciones soportadas (VACIO). " + nota_extra + " Decimales con coma y miles con punto.")

d.h(1, "Capítulo 8. Presupuesto Detallado")
d.p("Este capítulo presenta el presupuesto del proyecto por fuente, por rubro y por mes. Todas las cifras provienen del libro maestro del proyecto y coinciden con la ficha maestra. El valor solicitado al Sistema General de Regalías (SGR) es de 9.267.260.000 COP. La contrapartida es de 2.110.000.000 COP y el total del proyecto es de 11.377.260.000 COP. Los términos de referencia no se aportaron, por lo que los rubros siguen la estructura del metaprompt (SUPUESTO). Los costos unitarios no están respaldados por cotizaciones, y el anexo C reserva el espacio para ellas [DATO_USUARIO: cotizaciones vigentes de equipos].")

# ---------------------------------------------------------------- 8.1
d.h(2, "8.1 Resumen Presupuestal")
d.p("El presupuesto se construyó de abajo hacia arriba, actividad por actividad, y no desde el tope normativo. El expediente revisado declaraba un tope de 14.000.000.000 COP (DECLARADO, NO_VERIFICADO). La decisión DEC-F06 solicita la suma justificada, que equivale a 66,2 % del tope, y no el tope. La holgura de 4.732.740.000 COP no se presupuesta. Se describe como opciones de ampliación condicionadas a los términos de referencia: más nodos, un cuarto tramo o un año adicional de custodia. La {T:t01} desglosa el total por fuente de financiación y la {F:f01} lo ilustra.")
d.tabla("t01", "Resumen por fuente de financiación",
        ["Fuente", "Modalidad", "Valor (COP)", "Porcentaje del total", "Naturaleza"],
        [("SGR (MinCiencias)", "Efectivo solicitado", cop(SGR), pct(SGR, TOT) + " %", "CALCULADO"),
         ("Institución de educación superior ejecutora", "Especie: personal e infraestructura", cop(1_100 * M), pct(1_100 * M, TOT) + " %", "DECLARADO"),
         ("Empresa tecnológica aliada", "Efectivo: logística y viáticos de emergencia", cop(210 * M), pct(210 * M, TOT) + " %", "DECLARADO"),
         ("Empresa tecnológica aliada", "Especie: infraestructura en la nube", cop(800 * M), pct(800 * M, TOT) + " %", "DECLARADO"),
         ("Alcaldías de los municipios focalizados", "Sin aporte", cop(0), "0,0 %", "VACIO"),
         ("Total del proyecto", "", cop(TOT), "100,0 %", "CALCULADO")],
        "*Nota.* Elaboración propia con datos de la ficha maestra §5. La contrapartida suma 2.110.000.000 COP (18,5 % del total). El desglose de la entidad ejecutora es PROPUESTO; las certificaciones de contrapartida están pendientes [DATO_USUARIO: certificaciones de la entidad ejecutora y de la empresa]. Decimales con coma.")
d.fig("f01", "El SGR financia 81,5 % del proyecto y el personal absorbe 49,1 % de lo solicitado",
      "Nota. Elaboración propia con datos de maestro.py (BUDGET y CONTRA). Izquierda: fuentes del total del proyecto; derecha: rubros del valor solicitado al SGR. Cada sector lleva trama y etiqueta directa. Python 3 y matplotlib; script c8_figs.py; sin semilla; corte del 13 de octubre de 2026.")
decl, prop = natsum(sgr, "DECLARADO"), natsum(sgr, "PROPUESTO")
d.p(f"La contrapartida cubre 18,5 % del total y no incluye aportes de las alcaldías. La exigencia de cofinanciación depende de los términos de referencia y del régimen del SGR (Congreso de la República, 2020), y ninguno de los dos se verificó. El aporte en especie de la empresa, 800 millones de pesos colombianos (COP), corresponde a infraestructura en la nube. Su valoración depende de una certificación contable que aún no existe. El riesgo R-FIN-02 describe esa dependencia, con probabilidad de 25 % y valor monetario esperado de 20,0 millones de COP.")
d.p("Dos posiciones compiten sobre el nivel de la solicitud. La primera sostiene que un proyecto debe pedir el máximo permitido para absorber imprevistos. La segunda exige que cada peso solicitado tenga un beneficio marginal esperado mayor que su costo (Boardman et al., 2018). El proyecto adopta la segunda. Incluye una reserva de contingencia de 636.000.000 COP. Esa reserva equivale a la suma de los valores monetarios esperados de los 12 riesgos identificados, y no a un porcentaje arbitrario. El Project Management Institute [PMI] (2021) distingue la reserva para riesgos identificados de la reserva de gestión para riesgos desconocidos. Esta formulación solo constituye la primera, y la admisibilidad del rubro depende de los términos de referencia (VACIO).")
filr = []
for k, rows in porrubro.items():
    filr.append((k, str(len(rows)), mm(D.total(rows)), pct(D.total(rows), SGR) + " %", mm(natsum(rows, "DECLARADO")), mm(natsum(rows, "PROPUESTO") + natsum(rows, "CALCULADO"))))
filr.append(("Total SGR", str(len(sgr)), mm(SGR), "100,0 %", mm(decl), mm(prop + natsum(sgr, "CALCULADO"))))
d.p(f"La {{T:t02}} distribuye el valor solicitado por rubro y separa lo declarado en el expediente revisado de lo propuesto en esta formulación. Los valores declarados suman {mm(decl)} millones de COP ({pct(decl, SGR)} %). Los valores propuestos y calculados suman {mm(SGR - decl)} millones ({pct(SGR - decl, SGR)} %). Esa proporción muestra que la mayor parte del presupuesto requiere ratificación por cotización.")
d.tabla("t02", "Distribución del valor solicitado al SGR por rubro y naturaleza del dato",
        ["Rubro", "Líneas", "Valor (millones de COP)", "Porcentaje del SGR", "Declarado (millones de COP)", "Propuesto o calculado (millones de COP)"], filr,
        "*Nota.* Elaboración propia con datos de maestro.py. Declarado: valores del expediente E3. Propuesto o calculado: valores de esta formulación y la reserva de contingencia. Los porcentajes suman 100,0 % con redondeo. Decimales con coma.")
d.p("La consecuencia metodológica es doble. Primero, la reserva y el personal propuesto concentran la incertidumbre de costo. Segundo, la ratificación del panel evaluador debe priorizar los rubros de personal y de equipos, que reúnen 69,4 % del valor solicitado. Las secciones siguientes detallan cada rubro con su justificación.")

# ---------------------------------------------------------------- 8.2
d.h(2, "8.2 Personal")
pers = porrubro["Personal"]
d.p(f"El rubro de personal suma {mm(D.total(pers))} millones de COP, que equivalen a {pct(D.total(pers), SGR)} % del valor solicitado. Incluye 14 líneas, 29 cargos y 624 persona-mes. Las líneas P01 a P06 son valores heredados del expediente revisado ({mm(natsum(pers, 'DECLARADO'))} millones). Las líneas P07 a P14 son propuestas de esta formulación ({mm(natsum(pers, 'PROPUESTO'))} millones, {pct(natsum(pers, 'PROPUESTO'), D.total(pers))} % del rubro). Esa composición exige ratificar las escalas de pago. Ninguna se verificó contra una tabla institucional [DATO_USUARIO: escala salarial y carga prestacional de la entidad ejecutora].")
d.p("La estructura de cargos sigue los cuatro paquetes de trabajo. WP1 reúne 10 cargos para la medición verificada: seis jóvenes investigadores, dos estudiantes de maestría, un científico de datos senior y un especialista en metrología. WP2 reúne 13 cargos para la red, el software y el campo, incluidos seis técnicos departamentales. WP3 reúne cinco cargos para la apropiación, la calidad del aire y los convenios. WP0 tiene un cargo de gerencia. La investigación principal y los coinvestigadores no cargan al SGR, porque la entidad ejecutora los aporta como contrapartida en especie.")
d.p("La {T:t03} detalla las 14 líneas de personal. Cada línea indica cantidad, costo unitario, paquete de trabajo y meses de dedicación.")
tab_lineas("t03", "Presupuesto de personal detallado", "Personal")
d.p("Las líneas de jóvenes investigadores y de estudiantes de maestría atienden un doble propósito. Proveen capacidad de trabajo y forman talento, que es un resultado del sistema nacional de ciencia, tecnología e innovación (Congreso de la República, 2009). Los jóvenes investigadores se concentran en los meses 1 a 12, porque su trabajo principal es la colocalización del piloto. Los estudiantes de maestría permanecen 24 meses y pueden producir una tesis asociada al segundo artículo. El costo mensual de la maestría, de 6.350.000 COP, incluye matrícula y sostenimiento según el expediente revisado.")
d.p("La contrapartida de personal merece atención aparte, porque su certificación determina la viabilidad del aporte. La {T:t04} presenta las seis líneas de contrapartida. Las tres primeras corresponden a la dedicación del equipo investigador de la entidad ejecutora, que suma 800.000.000 COP. La cuarta valora el uso de laboratorios por 300.000.000 COP. Las dos últimas son aportes de la empresa tecnológica. Ningún valor está certificado todavía.")
fc = []
for r in D.CONTRA:
    fc.append((r["id"], r["concepto"], r["fuente"], cop(r["total"]), r["nat"], limpia(r["just"])))
fc.append(("Total", "Contrapartida del proyecto", "IES y empresa", cop(CON), "CALCULADO", "18,5 % del total del proyecto"))
d.tabla("t04", "Contrapartida por línea, fuente y naturaleza del dato",
        ["Id", "Aporte", "Fuente", "Total (COP)", "Naturaleza", "Observación"], fc,
        "*Nota.* Elaboración propia con datos de maestro.py (CONTRA) y de la ficha maestra §5. IES: institución de educación superior ejecutora; EMP: empresa tecnológica aliada. Las certificaciones de las dos entidades están pendientes [DATO_USUARIO: certificados de aporte en especie]. Decimales con coma y miles con punto.")
d.p("El valor de la dedicación de personal propio se estima como porcentaje de una remuneración mensual de referencia. Esa convención es habitual en proyectos con financiación pública, pero exige un certificado de la dirección financiera de cada entidad. Sin certificado, el aporte en especie se rechaza en la evaluación de viabilidad. Por esa razón la mitigación del riesgo R-FIN-02 exige certificar los aportes antes del acta de inicio.")

# ---------------------------------------------------------------- 8.3
d.h(2, "8.3 Equipos y Software")
eq = porrubro["Equipos y software"]
d.p(f"El rubro de equipos y software suma {mm(D.total(eq))} millones de COP, que equivalen a {pct(D.total(eq), SGR)} % del valor solicitado. Incluye 12 líneas. Cinco de ellas son valores del expediente revisado y siete son propuestas de esta formulación. La {{T:t05}} presenta cada línea con su justificación técnica. La compra de nodos, cabezales y gateways se programa por tramo y no en bloque, y la {{T:t06}} muestra el valor liberado por cada compuerta.")
tab_lineas("t05", "Presupuesto de equipos y software", "Equipos y software")
d.p("La justificación técnica descansa en tres decisiones de diseño. La primera es el uso de sensores ópticos de bajo costo para PM2,5 y PM10. Esos sensores responden a la humedad relativa y a la fracción gruesa (Jayaratne et al., 2018; Malings et al., 2020), y su desempeño depende del sitio (Giordano et al., 2021). La segunda decisión es la colocalización con tres monitores gravimétricos de referencia, uno por departamento. Ese diseño sigue los protocolos de desempeño para sensores de partículas finas (U.S. Environmental Protection Agency [EPA], 2021). La tercera es la corrección en el gateway, que desplaza el cómputo hacia el borde de la red (Shi et al., 2016).")
d.p("La arquitectura de comunicación explica las líneas de gateways, satélite y datos celulares. Los nodos hoja transmiten por LoRa, una tecnología de largo alcance y bajo consumo (Adelantado et al., 2017). Cada gateway reenvía por red celular y cuenta con un enlace satelital alterno y almacenamiento local de siete días. El costo de esa redundancia, 35.000.000 COP en módulos y 55.000.000 COP en planes satelitales, equivale a 1,0 % del valor solicitado. La redundancia responde al riesgo R-TEC-03, la falla de la red celular en el sitio, que tiene probabilidad de 40 %.")
d.p("La línea E10 financia las instancias en la nube que alojan el gemelo digital. Un gemelo digital es una representación computacional que se actualiza con datos del sistema físico y permite simular su estado (Grieves y Vickers, 2017; Tao et al., 2019). En este proyecto estima la distribución espacial de PM2,5 y PM10 entre los nodos. El aporte en especie de la empresa, 800.000.000 COP en infraestructura en la nube, complementa la línea E10 y no la sustituye. La separación entre ambas debe constar en el convenio para evitar que el mismo servicio se cuente dos veces.")
ft = []
for t in D.TRAMOS:
    val = t["compra_nodos"] * 4.5 * M + t["compra_cabezales"] * 1.2 * M + t["compra_gw"] * 28.0 * M
    libera = "Acta de inicio y contratación (H0)" if t["id"] == 1 else ("Compuerta C1 (mes 12)" if t["id"] == 2 else "Compuerta C2 (mes 17)")
    ft.append((f"Tramo {t['id']}", str(t["mes_compra"]), str(t["compra_nodos"]), str(t["compra_gw"]), str(t["compra_cabezales"]), mm(val), libera))
tot_val = sum(float(x[5].replace(".", "").replace(",", ".")) for x in ft)
ft.append(("Total", "", "120", "11", "150", mm(tot_val * M), ""))
d.tabla("t06", "Compras de nodos, gateways y cabezales por tramo y compuerta que las libera",
        ["Tramo", "Mes de compra", "Nodos", "Gateways", "Cabezales", "Valor (millones de COP)", "Decisión que libera la compra"], ft,
        "*Nota.* Elaboración propia con datos de maestro.py (TRAMOS y líneas E01, E02 y E04). Costos unitarios: nodo 4,5 millones; cabezal 1,2 millones; gateway 28,0 millones de COP. Se compran 120 nodos para operar 100, y 11 gateways para operar 10. Decimales con coma.")
d.p("La {T:t06} muestra que el proyecto compromete 334,0 millones de COP en equipos del tramo 1 antes de cualquier evidencia de desempeño. Libera 388,0 y 306,0 millones solo tras las compuertas C1 y C2. Esa estructura limita la exposición ante un fallo del modelo de corrección. Si C1 no se aprueba, el proyecto detiene 694,0 millones de COP en compras. Esa suma equivale a 67,5 % de las compras de nodos, cabezales y gateways. Collingridge (1980) describe el dilema: la tecnología es fácil de cambiar al inicio, cuando se sabe poco de ella. La compra por tramos conserva esa facilidad el mayor tiempo posible.")

# ---------------------------------------------------------------- 8.4
d.h(2, "8.4 Materiales e Insumos")
mat = porrubro["Materiales e insumos"]
d.p(f"El rubro de materiales e insumos suma {mm(D.total(mat))} millones de COP, que equivalen a {pct(D.total(mat), SGR)} % del valor solicitado. Incluye siete líneas. Cinco son valores del expediente revisado y dos son propuestas. La línea M02 sustituye los gases patrón que el expediente incluía, porque los gases patrón calibran analizadores de gases y no sensores de material particulado. El polvo de ensayo normalizado y los consumibles del banco de calibración cumplen la función correcta. La {{T:t07}} presenta las líneas.")
tab_lineas("t07", "Presupuesto de materiales e insumos", "Materiales e insumos")
d.p("Los filtros de membrana de politetrafluoroetileno (PTFE) permiten la medición gravimétrica de referencia. Se programan 1.200 unidades para 240 análisis de laboratorio acreditado (línea S01 del rubro de servicios). Resultan cinco filtros por muestra analizada, entre pesajes, blancos y repeticiones. Esa proporción es PROPUESTO. Las cartillas impresas, 5.000 unidades, atienden a población sin acceso a internet en los municipios focalizados. Cada cartilla cuesta 8.500 COP y presenta el índice y el protocolo de alerta.")
d.p("Las mascarillas N95 protegen al personal de campo y a los asistentes a talleres, y cumplen una función de bioseguridad. La Organización Mundial de la Salud (OMS, 2021) fija guías de calidad del aire para PM2,5 y PM10. Esas guías justifican proteger a quien trabaja en sitios de remoción. El proyecto no afirma, sin embargo, que las mascarillas reduzcan un efecto en salud medido. Son una medida de precaución para el equipo. La consecuencia es que el indicador de impacto del proyecto no depende de ellas.")

# ---------------------------------------------------------------- 8.5
d.h(2, "8.5 Servicios Técnicos")
srv = porrubro["Servicios técnicos"]
d.p(f"El rubro de servicios técnicos suma {mm(D.total(srv))} millones de COP, que equivalen a {pct(D.total(srv), SGR)} % del valor solicitado. Incluye 11 líneas. Cuatro de ellas verifican el desempeño o auditan el sistema. Son el análisis gravimétrico, la evaluación externa independiente, el ensayo con laboratorio externo y la auditoría de ciberseguridad. La {{T:t08}} presenta el detalle.")
tab_lineas("t08", "Presupuesto de servicios técnicos", "Servicios técnicos")
d.p("Las líneas de verificación externa cumplen una función de control que la ejecución interna no puede cumplir. La evaluación externa de los meses 12 y 24 y el ensayo con laboratorio externo suman 210.000.000 COP. Estos servicios producen la evidencia independiente que respalda las compuertas y la afirmación de desempeño. Patton (2011) propone la evaluación orientada al desarrollo para proyectos de innovación con incertidumbre. Esa lógica sustenta la evaluación del mes 12, antes de la compuerta C1.")
d.p("La consultoría jurídica en propiedad intelectual, con 150 horas por 45.000.000 COP, atiende el riesgo R-JUR-01. El análisis de libertad de operación examina si solicitudes de patente de terceros afectan el diseño. La Decisión 486 regula el régimen común de propiedad industrial y sustenta ese análisis en Colombia (Comunidad Andina, 2000). La auditoría de ciberseguridad cubre dos pruebas de penetración. Debe también verificar el cumplimiento de la Ley 1581 de 2012 sobre protección de datos personales (Congreso de la República, 2012b). Las lecturas pueden asociarse con ubicaciones de viviendas y trabajadores.")
d.p("La línea S11, importación y nacionalización, suma 80.000.000 COP y atiende tres lotes. El riesgo financiero R-FIN-01, la devaluación del peso, tiene el mayor valor monetario esperado del registro, 165,0 millones de COP. La mitigación combina compra por tramos, cobertura cambiaria y cotizaciones vigentes. Las líneas E01 a E04 suman 1.283,0 millones de COP. Si se importaran en su totalidad (SUPUESTO), una devaluación de 10 % las encarecería en 128,3 millones. La reserva cubre esa cifra solo en parte.")

# ---------------------------------------------------------------- 8.6
d.h(2, "8.6 Viajes y Viáticos")
via = porrubro["Viajes y viáticos"]
d.p(f"El rubro de viajes y viáticos suma {mm(D.total(via))} millones de COP, que equivalen a {pct(D.total(via), SGR)} % del valor solicitado. Incluye cinco líneas. Tres de ellas, propuestas por esta formulación, cubren el trabajo de campo en tres departamentos: tiquetes, viáticos y vehículos 4x4. Su valor suma 408,0 millones de COP. El expediente revisado asignaba menos recursos a este rubro. La ampliación obedece a que la red cubre Caldas, Cundinamarca y Valle del Cauca. La {{T:t09}} detalla las líneas.")
tab_lineas("t09", "Presupuesto de viajes y viáticos", "Viajes y viáticos")
d.p("El trabajo de campo comprende instalación, mantenimiento, colocalización y talleres en 12 municipios, cuatro por departamento [DATO_USUARIO: lista de municipios]. Los 600 días-persona de viáticos equivalen a 25 días-persona por mes durante 24 meses. Esa cifra es una estimación gruesa, porque la carga real depende del calendario de instalación. La programación de viajes debe revisarse con el cronograma de cada tramo.")
d.p("Las dos líneas del expediente revisado, el viaje internacional de divulgación y la alimentación de laboratorios ciudadanos, suman 54,0 millones de COP. El viaje internacional de divulgación sustenta el producto de nuevo conocimiento. La alimentación de laboratorios ciudadanos apoya la participación de las comunidades. Su vínculo con la escalera de participación de Arnstein (1969) se desarrolla en el capítulo 16. El proyecto no presupuesta viajes fuera de esas dos líneas.")

# ---------------------------------------------------------------- 8.7
d.h(2, "8.7 Otros Rubros")
otr = porrubro["Otros rubros"]
d.p(f"El rubro de otros rubros suma {mm(D.total(otr))} millones de COP, que equivalen a {pct(D.total(otr), SGR)} % del valor solicitado. Incluye seis líneas que no encajan en los rubros anteriores: publicaciones, eventos, propiedad intelectual, pólizas y administración. La {{T:t10}} las presenta.")
tab_lineas("t10", "Presupuesto de otros rubros", "Otros rubros")
d.p("La administración suma 360.000.000 COP, que equivalen a 3,9 % del valor solicitado. El expediente revisado declaraba un tope porcentual de 5 %, que no se verificó. Si el tope existe y se mantiene, el proyecto queda por debajo. Si los términos de referencia fijan un tope menor, la línea O05 debe recalcularse. La línea O04, pólizas y garantías del SGR, suma 60.000.000 COP y cubre cumplimiento, anticipo y responsabilidad civil. La Ley 2056 de 2020 regula la organización y el funcionamiento del SGR y es el marco de referencia de esas garantías (Congreso de la República, 2020).")
d.p("Las líneas O01, O03 y O06 apoyan la propiedad intelectual y la divulgación. Teece (1986) argumenta que el valor de una innovación depende de los activos complementarios y de los regímenes de apropiación. El registro del software ante la Dirección Nacional de Derecho de Autor (15.000.000 COP) protege el modelo de corrección y el gemelo digital. El acceso abierto de los artículos (25.000.000 COP) difunde el protocolo de calibración. Esa combinación es deliberada. Protege el software que la entidad ejecutora debe sostener y abre el conocimiento que otras redes pueden reutilizar.")

# ---------------------------------------------------------------- 8.8
d.h(2, "8.8 Flujo de Caja")
f = D.flujo_sgr(); fcn = D.flujo_contra()
cum = list(itertools.accumulate(f))
tri = D.por_periodo(f, 3); trc = D.por_periodo(fcn, 3)
d.p("El flujo de caja distribuye el presupuesto en el tiempo según el calendario de cada línea. Las líneas de personal y de servicios se reparten de forma uniforme entre su mes inicial y su mes final. Las compras de nodos, cabezales y gateways se concentran en los meses 5, 13 y 18, que corresponden a los tres tramos. La {T:t11} presenta el flujo por trimestre y la {F:f02} muestra la ejecución acumulada.")
cacu = 0; fil11 = []
for i in range(8):
    cacu += tri[i]
    fil11.append((f"T{i+1} (meses {3*i+1} a {3*i+3})", mm(tri[i]), mm(trc[i]), mm(tri[i] + trc[i]), pct(cacu, SGR) + " %"))
fil11.append(("Total", mm(sum(tri)), mm(sum(trc)), mm(sum(tri) + sum(trc)), "100,0 %"))
d.tabla("t11", "Flujo de caja trimestral del SGR y de la contrapartida",
        ["Trimestre", "SGR (millones de COP)", "Contrapartida (millones de COP)", "Total (millones de COP)", "SGR acumulado"], fil11,
        "*Nota.* Elaboración propia con datos de maestro.py (flujo_sgr y flujo_contra). La contrapartida se distribuye de forma uniforme en 24 meses. El flujo semestral del SGR es 2.689,3; 1.936,1; 2.634,1 y 2.007,8 millones de COP. Naturaleza: CALCULADO. Decimales con coma.")
d.fig("f02", "El SGR se ejecuta 49,9 % hasta la compuerta C1 y 71,5 % hasta C2",
      "Nota. Elaboración propia con datos de maestro.py (flujo_sgr y flujo_contra). Ejecución acumulada mensual en porcentaje del valor de cada fuente; líneas verticales: compuertas C1 (mes 12) y C2 (mes 17). Python 3 y matplotlib; script c8_figs.py; sin semilla; corte del 13 de octubre de 2026.")
d.p("La curva de ejecución del SGR alcanza 49,9 % en el mes 12 y 71,5 % en el mes 17. La compra del tramo 2 en el mes 13 produce un salto de 7,6 puntos porcentuales. La del tramo 3 en el mes 18 produce un salto de 6,8 puntos. La contrapartida avanza de forma lineal. El desembolso concentra por tanto casi la mitad de los recursos antes de la primera compuerta de decisión. Esa concentración proviene de personal y servicios iniciales, que no dependen de las compuertas, y de la compra del tramo 1.")
d.p("La {F:f03} presenta el desembolso mensual del SGR por grupo de rubros. Los tres picos de los meses 5, 13 y 18 alcanzan 777,4; 707,6 y 630,1 millones de COP. Corresponden a las compras de cada tramo. El resto de los meses oscila entre 320 y 460 millones, con un núcleo estable de personal. La tabla de desembolsos condicionados fija qué sucede con cada pico si una compuerta no se aprueba.")
d.fig("f03", "Tres picos de desembolso coinciden con las compras de los tramos 1, 2 y 3 (meses 5, 13 y 18)",
      "Nota. Elaboración propia con datos de maestro.py (flujo_sgr). Desembolso mensual del SGR por grupo de rubros, en millones de COP; trama y etiqueta directa en los picos. Python 3 y matplotlib; script c8_figs.py; sin semilla; corte del 13 de octubre de 2026.")
d.p("La {T:t12} traduce el flujo en hitos de desembolso. Cada hito indica el mes, el valor acumulado liberado y la condición de liberación. El financiador define el esquema real de desembolsos, que los términos de referencia no precisan [DATO_USUARIO: esquema de desembolsos del financiador].")
hit = [("Anticipo y acta de inicio (H0)", "2", mm(cum[1]), pct(cum[1], SGR) + " %", "Contratos, convenios y plan de trabajo aprobados"),
       ("Compra del tramo 1", "5", mm(cum[4]), pct(cum[4], SGR) + " %", "Diseño de enlace y energía listo (H1); pólizas vigentes"),
       ("Compuerta C1 (H3)", "12", mm(cum[11]), pct(cum[11], SGR) + " %", "Modelo validado: R² de 0,70 o más y NRMSE de 30 % o menos; 50 % o más de los comités usa el tablero"),
       ("Compra del tramo 2", "13", mm(cum[12]), pct(cum[12], SGR) + " %", "C1 aprobada: 388,0 millones de COP en nodos, gateways y cabezales"),
       ("Compuerta C2 (H5)", "17", mm(cum[16]), pct(cum[16], SGR) + " %", "Umbrales en tres departamentos, disponibilidad de 90 % o más y convenios de custodia con partida"),
       ("Compra del tramo 3", "18", mm(cum[17]), pct(cum[17], SGR) + " %", "C2 aprobada: 306,0 millones de COP en nodos, gateways y cabezales"),
       ("Cierre y transferencia (H8)", "24", mm(cum[23]), "100,0 %", "Actas de entrega a custodios y cláusula de apertura firmada")]
d.tabla("t12", "Hitos de desembolso del SGR y condición de liberación",
        ["Hito de desembolso", "Mes", "SGR acumulado (millones de COP)", "Porcentaje del SGR", "Condición de liberación"], hit,
        "*Nota.* Elaboración propia con datos de maestro.py y de la ficha maestra §4 y §6. Los valores acumulados son CALCULADOS al cierre de cada mes. Las condiciones de liberación son PROPUESTO y se ajustan al esquema que fije el financiador. Decimales con coma.")
d.p("El esquema propuesto vincula los desembolsos con evidencias y no con fechas. Cooper (2008) describe este diseño como compuertas con criterios explícitos que autorizan la inversión de la etapa siguiente. El proyecto adopta tres compuertas y cada una libera una compra. La contrapartida es administrativa: el financiador debe aceptar un desembolso condicionado, y el cronograma debe absorber dos semanas de decisión por compuerta. La ruta crítica incluye esas dos semanas. El capítulo 21 resume el presupuesto para el acta de constitución.")
d.guardar(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps", "cap08.md"))
print("ok", mm(tot_val * M))
