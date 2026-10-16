# -*- coding: utf-8 -*-
"""Documento técnico en formato Anexo 2, secciones 1 a 9."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from a2lib import *

ID = D.IDENT
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = Doc("D")

d.h(1, "Documento técnico de la propuesta (formato del Anexo 2)")
d.p("Esta parte presenta el proyecto en las 30 secciones del Anexo 2 de la convocatoria. Conserva los títulos, el orden y la numeración de la plantilla oficial. Respeta también la estructura de sus tablas. Las instrucciones de la plantilla se sustituyen por el contenido del proyecto. Los datos que solo posee el proponente figuran como [DATO_USUARIO]. El análisis extenso y la trazabilidad de cada cifra se encuentran en el expediente de formulación, que sigue a la sección 30. El documento es un borrador con vacíos y no un paquete de radicación.")

# ============================================================== 1
nombre_mga = ("Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material "
              "particulado posterremoto en municipios afectados de Caldas, Cundinamarca y Valle del Cauca")
assert len(nombre_mga) <= 256
d.raw("# 1. IDENTIFICACIÓN DEL PROYECTO")
d.p("La {T:t01} diligencia los campos de identificación del Anexo 2. Los nombres de las entidades, el código SIGP y la lista de municipios dependen de la decisión de la alianza y quedan abiertos.")
d.tabla("t01", "Identificación del proyecto",
        ["Campo del Anexo 2", "Diligenciamiento"],
        [("Nombre del proyecto", ID["titulo"]),
         ("Nombre sugerido para la MGA (estructura proceso + objeto + localización; " + str(len(nombre_mga)) + " caracteres)", nombre_mga),
         ("Entidad proponente", "[DATO_USUARIO: universidad con grupo de investigación reconocido por MinCiencias]. Categoría de puntuación: IES"),
         ("Número total de entidades aliadas", "2, además de un municipio beneficiario"),
         ("Entidad aliada No. 1", "[DATO_USUARIO: actor reconocido por MinCiencias]. Categoría de puntuación: [DATO_USUARIO: centro o instituto de CTeI, instituto del SINA u otra]"),
         ("Entidad aliada No. 2", "[DATO_USUARIO: empresa aliada]. Categoría de puntuación: las cinco categorías del Anexo 2 no incluyen empresas; los términos de referencia deben confirmar su tratamiento"),
         ("Beneficiario focal", "[DATO_USUARIO: municipio de Cundinamarca, Risaralda, Caldas o Valle del Cauca], como beneficiario sin aporte de recursos"),
         ("Código SIGP", "[DATO_USUARIO: código asignado en la plataforma SIGP]"),
         ("Tiempo de ejecución en meses", "24"),
         ("Fecha y hora de cierre de la radicación", "[DATO_USUARIO: confirmar 3 de noviembre de 2026 a las 4:00 p. m. (guía financiera) o 11 de noviembre de 2026 (ficha del proyecto)]"),
         ("Región (SGR)", "[DATO_USUARIO: dos regiones del SGR según el artículo 45 de la Ley 2056 de 2020]. Con tres departamentos, el alcance podría abarcar más de dos regiones (NO_VERIFICADO)"),
         ("Departamento(s)", "Caldas, Cundinamarca y Valle del Cauca (SUPUESTO por instrucción del usuario); Risaralda por verificar"),
         ("Municipio(s)", "12 municipios, cuatro por departamento [DATO_USUARIO: lista de municipios afectados por la emergencia]"),
         ("Centro poblado", "[DATO_USUARIO: urbano o rural, por municipio]"),
         ("Resguardo", "[DATO_USUARIO: nombre o No aplica]"),
         ("Demanda(s) territorial(es)", "Nueva demanda derivada de la emergencia: mediciones de PM2,5 y PM10 con error conocido en sitios de remoción de escombros. Reporte oficial de afectación: [DATO_USUARIO: reporte de la UNGRD o del departamento]"),
         ("Línea temática principal", "[DATO_USUARIO: línea temática del numeral 5 de los términos de referencia]"),
         ("Línea temática secundaria", "[DATO_USUARIO: si aplica]")],
        "*Nota.* Elaboración propia con el Anexo 2 y la ficha maestra del proyecto. Los términos de referencia, el Anexo 4 y la lista de municipios afectados no se aportaron (NO_VERIFICADO).")
d.p("La {T:t02} registra los grupos de investigación que se vincularán. Las cifras de investigadores y estudiantes son las que sustenta el presupuesto. Los nombres y las categorías vigentes en MinCiencias los aportan los grupos.")
d.tabla("t02", "Grupos de investigación vinculados al proyecto",
        ["Nombre del grupo", "Entidad", "Líneas de investigación", "Investigadores y formación", "Estudiantes que puede vincular", "Contribución a la demanda territorial"],
        [("[DATO_USUARIO: grupo de la Universidad]", "Universidad proponente", "[DATO_USUARIO: líneas]", "Investigador principal (50 %) y coinvestigador técnico (30 %); más coinvestigadores de ambiente y ciencias sociales (20 %)", "8: 6 jóvenes investigadores y 2 de maestría", "Calibración y validación del modelo de corrección; gerencia científica; apropiación social"),
         ("[DATO_USUARIO: grupo del actor reconocido]", "Actor reconocido por MinCiencias", "[DATO_USUARIO: líneas]", "[DATO_USUARIO: número y formación]", "[DATO_USUARIO]", "Verificación metrológica independiente y formación de custodios")],
        "*Nota.* Elaboración propia con el presupuesto (líneas P01, P02, P07, P13 y C01 a C03). Se tendrá en cuenta la categoría obtenida en la convocatoria 894 de 2021 [DATO_USUARIO: categoría vigente de cada grupo].")

# ============================================================== 2
d.raw("# 2. RESUMEN EJECUTIVO")
d.p("El proyecto atiende un problema de calidad del dato. En los sitios de remoción de escombros posterremoto, los comités de gestión del riesgo no cuentan con mediciones de PM2,5 y PM10 de error conocido. Los sensores ópticos de bajo costo cambian su respuesta con la humedad y con el tamaño de las partículas. Sin referencia local, ese error no se estima.")
d.p("La propuesta instala una red de 100 nodos y 10 gateways en municipios afectados de Caldas, Cundinamarca y Valle del Cauca. Tres monitores gravimétricos de referencia, uno por departamento, se colocalizan con los nodos. Un modelo de corrección en el gateway ajusta cada lectura por humedad, temperatura y fracción gruesa. Un gemelo digital y un tablero presentan el resultado con su error residual. Un protocolo de alerta, co-diseñado con los comités, define los umbrales de decisión.")
d.p("El despliegue avanza por tres tramos de 30, 40 y 30 nodos. Dos compuertas, en los meses 12 y 17, liberan la compra del tramo siguiente. Lo hacen solo si el modelo cumple R² ≥ 0,70 y NRMSE ≤ 30 % frente a la referencia. La custodia de cada componente se transfiere a instituciones con competencia y partida. La madurez tecnológica pasa de TRL 4 a TRL 7 en 24 meses.")
d.p("Los resultados esperados son una red operativa con disponibilidad mensual de nodos de 90 % o más y un modelo de corrección validado. Se esperan también dos artículos científicos y un software registrado. Se espera además que 75 % o más de 15 comités use el tablero en decisiones documentadas y que 60 personas queden certificadas. El proyecto no afirma efectos en la salud. Solicita " + cop(SGR_T) + " al SGR y suma una contrapartida de " + cop(CON_T) + ".")

# ============================================================== 3
d.raw("# 3. PALABRAS CLAVE")
d.p("Material particulado; sensores de bajo costo; gemelo digital; calibración colocalizada; gestión del riesgo de desastres; posterremoto.")

# ============================================================== 4
d.raw("# 4. ALINEACIÓN CON LA POLÍTICA PÚBLICA")
d.p("La {T:t03} diligencia los campos de alineación con el Plan Nacional de Desarrollo 2022-2026, adoptado con la Ley 2294 de 2023 (Congreso de la República, 2023). Los artículos y programas exactos no se verificaron porque los documentos de planeación no se aportaron.")
d.tabla("t03", "Alineación con los planes de desarrollo",
        ["Campo del Anexo 2", "Diligenciamiento", "Estado"],
        [("Plan Nacional de Desarrollo", "Colombia Potencia Mundial de la Vida (Ley 2294 de 2023)", "DOCUMENTADO"),
         ("Estrategia transversal", "[DATO_USUARIO: estrategia transversal aplicable]", "VACIO"),
         ("Transformación", "Propuesta: la que relaciona la gestión del riesgo con la acción climática [DATO_USUARIO: nombre exacto]", "PROPUESTO; NO_VERIFICADO"),
         ("Pilar", "[DATO_USUARIO: pilar]", "VACIO"),
         ("Catalizador", "[DATO_USUARIO: catalizador]", "VACIO"),
         ("Programa", "[DATO_USUARIO: programa]", "VACIO"),
         ("Plan Departamental de Desarrollo", "[DATO_USUARIO: planes vigentes de Caldas, Cundinamarca y Valle del Cauca]", "VACIO"),
         ("Estrategia del Plan Departamental", "[DATO_USUARIO: estrategia por departamento]", "VACIO"),
         ("Plan Municipal de Desarrollo", "[DATO_USUARIO: planes vigentes de los municipios focalizados]", "VACIO"),
         ("Estrategia del Plan Municipal", "[DATO_USUARIO: estrategia por municipio]", "VACIO"),
         ("Programa del Plan Departamental", "[DATO_USUARIO: programa por departamento]", "VACIO")],
        "*Nota.* Elaboración propia con la Ley 2294 de 2023. La alineación ascendente del proyecto se mide con PERS-E01: uso del tablero por los comités. El expediente detalla otros once instrumentos en la sección 5.3 del capítulo 5.")
d.h(2, "4.1 Afectación y relación con la emergencia")
d.p("El proyecto atiende una afectación producida por la emergencia. La remoción de escombros posterremoto resuspende polvo y expone a cuadrillas y a población a PM2,5 y PM10. Los comités deben decidir alertas con lecturas de sensores de bajo costo que no tienen error conocido en estos sitios.")
d.p("La relación con la brecha de conocimiento es directa. El proyecto no trata la contaminación del aire derivada del terremoto. Trata el déficit metrológico que impide gestionar el riesgo: la ausencia de calibración colocalizada y de corrección local. El expediente documenta que solo 28 de 1.122 municipios cuentan con estaciones utilizables para estimar la carga (Rodríguez-Villamizar et al., 2022, pp. 3 y 6).")
d.p("La afectación debe sustentarse en reportes oficiales. El reporte de la UNGRD, el diagnóstico técnico sectorial y la lista de municipios afectados no se aportaron [DATO_USUARIO: reportes oficiales de afectación]. Sin ellos, la afectación es un supuesto declarado en el expediente E3 (NO_VERIFICADO).")

# ============================================================== 5
d.raw("# 5. IDENTIFICACIÓN Y DESCRIPCIÓN DEL PROBLEMA")
d.h(2, "5.1 Problema central")
d.p("Los comités de gestión del riesgo de los municipios focalizados deciden alertas con mediciones de PM2,5 y PM10 de error desconocido. Las lecturas ópticas de bajo costo no se verifican frente a una referencia en los sitios de remoción de escombros.")
d.h(2, "5.2 Descripción del problema y la situación existente")
d.p("El territorio comprende Caldas, Cundinamarca y Valle del Cauca, con 12 municipios focalizados y 15 comités de gestión del riesgo, 12 municipales y 3 departamentales. La delimitación es un supuesto por instrucción del usuario. La remoción de escombros resuspende polvo grueso y concentra maquinaria en sitios acotados (Landrigan et al., 2004).")
d.p("El análogo más cercano proviene de una mina de carbón a cielo abierto. Allí el PM2,5 medio fue de 159,11 µg/m3 (Suresh et al., 2025, pp. 10 y 22). Ese dato no describe un sitio de escombros, y la fracción gruesa local es un dato VACIO que el proyecto mide en el tramo 1.")
d.p("La causa inmediata es la interferencia de la humedad y de la fracción gruesa sobre la respuesta óptica del sensor. La correlación entre partículas y humedad fue de 0,73 en la mina citada (Suresh et al., 2025, p. 30). En Seúl, la corrección con una estación cercana elevó el R² de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8). La causa de fondo es la ausencia de un protocolo de calibración colocalizada con corrección en el borde y con custodia institucional.")
d.p("La evolución reciente es de expansión de redes sin plan de calibración. Se estima que 90,8 % de las 5.076 estaciones de la red nacional propuesta serían sensores sin plan de calibración (Murad Pedraza et al., 2026, pp. 10-11 y 13; cálculo del analista). No se identificaron intervenciones distintas a la propuesta en estos municipios [DATO_USUARIO: intervenciones previas de las alcaldías y la autoridad ambiental].")
d.h(2, "5.3 Magnitud actual del problema e indicadores de referencia")
d.p("La {T:t04} reúne los indicadores de referencia. La magnitud local no está medida. El proyecto la mide en el tramo 1, y la línea base propia queda como VACIO hasta el hito H2.")
d.tabla("t04", "Indicadores de referencia de la magnitud del problema",
        ["Indicador", "Valor", "Alcance", "Fuente", "Naturaleza"],
        [("Error de medición de los nodos frente a la referencia (NRMSE)", "VACIO: se mide en el tramo 1", "Tres departamentos", "Proyecto, hito H2 (mes 10)", "VACIO"),
         ("Error normalizado de sensores sin calibración dinámica en alta humedad", "Superior a 45 %", "Expediente E3", "Expediente E3, Paso 1", "DECLARADO; NO_VERIFICADO"),
         ("Municipios con estaciones utilizables para estimar la carga", "28 de 1.122 (2,5 %)", "Colombia", "Rodríguez-Villamizar et al. (2022, pp. 3 y 6)", "DECLARADO"),
         ("Estaciones propuestas sin plan de calibración", "90,8 % de 5.076", "Red nacional propuesta", "Murad Pedraza et al. (2026, pp. 10-11 y 13)", "CALCULADO por el analista"),
         ("Uso institucional del tablero (línea base)", "VACIO: se mide en el tramo 1", "15 comités", "Proyecto, PERS-E01", "VACIO")],
        "*Nota.* Elaboración propia con los datos de la sección 1.2.4 del expediente. Las fuentes oficiales de la línea base local deben aportarse [DATO_USUARIO: fuente oficial actualizada].")
d.h(2, "5.4 Árbol de problemas")
d.p("La {T:t05} presenta el árbol de problemas con el esquema que recomienda el Anexo 2. Las relaciones provienen del análisis estructural de Vester-MICMAC con 15 variables, en el escenario de trabajo S2. Son hipótesis de influencia estructural.")
d.tabla("t05", "Árbol de problemas",
        ["Nivel", "Elemento 1", "Elemento 2", "Elemento 3"],
        [("Efectos indirectos", "1.1. Baja confianza en las mediciones y desuso del tablero (V15)", "2.1. Decisiones de alerta sin respaldo metrológico", "3.1. Exposición no gestionada de operarios y población"),
         ("Efectos directos", "1. Falsas alarmas y fatiga de alarmas (V12)", "2. Índice de calidad del aire y salud con error desconocido (V11)", "3. Personas alertadas con datos de calidad desconocida (V14)"),
         ("Problema central", "Error de medición IoT sin verificar frente a una referencia (V06)", "", ""),
         ("Causas directas", "1. Humedad relativa sin corrección (V03)", "2. Fracción gruesa del polvo sin corrección (V02)", "3. Calibración estática o inexistente (V07)"),
         ("Causas indirectas", "1.1. Remoción de escombros que resuspende polvo (V05)", "2.1. Energía y enlace interrumpidos que reducen la disponibilidad (V09)", "3.1. Ausencia de custodia institucional de la red")],
        "*Nota.* Elaboración propia con el análisis de Vester-MICMAC (V01 a V15) del Paso 4 del expediente. V06 es crítica en los cinco escenarios (influencia 8; dependencia 13).")

# ============================================================== 6
d.raw("# 6. ANTECEDENTES")
d.p("El antecedente internacional más cercano es el uso de estaciones de referencia para corregir redes de sensores. En Seúl, la corrección con una estación cercana y 35 minutos de desfase llevó el R² de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8). Las guías de desempeño para sensores de partículas de la Agencia de Protección Ambiental de los Estados Unidos fijan umbrales de uso informativo (U.S. Environmental Protection Agency [EPA], 2021).")
d.p("En el ámbito nacional, el corpus de vigilancia tecnológica registra 209 estaciones reportadas y 154 integradas a un sistema de vigilancia (Rodríguez-Villamizar et al., 2022). El documento CONPES 3943 formula la política de mejoramiento de la calidad del aire (Departamento Nacional de Planeación [DNP], 2018). Ninguno de los cinco documentos de alerta del corpus reporta detección, falsas alarmas ni anticipación.")
d.p("No se identificó una iniciativa departamental o municipal que combine calibración colocalizada, corrección en el borde y custodia institucional en sitios de remoción de escombros. La búsqueda de antecedentes regionales debe completarse con los proponentes [DATO_USUARIO: antecedentes de las alcaldías, las corporaciones autónomas regionales y la Universidad]. El expediente desarrolla el estado del arte y la vigilancia tecnológica en el capítulo 2.")

# ============================================================== 7
d.raw("# 7. JUSTIFICACIÓN")
d.p("La necesidad particular es una medición con error conocido en el lugar y el momento en que se decide. Sin ella, el comité alerta con datos de calidad desconocida o no alerta. Ambas opciones tienen costos para operarios y población.")
d.p("La viabilidad descansa en tres hechos. Primero, la corrección en el gateway reduce el tráfico y la latencia frente a la calibración centralizada (Shi et al., 2016). Segundo, el despliegue por tramos limita el riesgo financiero, porque cada compuerta libera la compra siguiente solo con evidencia. Tercero, la solución utiliza componentes disponibles en el mercado y una arquitectura de largo alcance y bajo consumo (Adelantado et al., 2017).")
d.p("La pertinencia a corto plazo es una red operativa y un protocolo en uso. A mediano plazo es un modelo validado por departamento. A largo plazo es una red bajo custodia institucional con partida. Esa custodia cubre al menos 70 % de los nodos 12 meses después del cierre (PERS-S02). El costo de sostenimiento y la capacidad de absorción de los custodios son NO_CALCULABLE hasta contar con datos.")

# ============================================================== 8
d.raw("# 8. ARTICULACIÓN DEL PROYECTO EN RESPUESTA A LOS RETOS ESTRATÉGICOS Y DEMANDAS TERRITORIALES, A PARTIR DE LOS ALCANCES TEMÁTICOS")
d.p("La alianza entiende el reto estratégico como la falta de información ambiental verificable para gestionar el riesgo posterremoto. Su atención es importante porque las decisiones de alerta y de protección de operarios dependen de esa información. El proyecto la atiende con una red calibrada, un tablero y un protocolo co-diseñado.")
d.p("La {T:t06} relaciona el reto con la demanda territorial y con el producto. Los códigos del Anexo 4 y del plan bienal de convocatorias 2023-2024 no se aportaron y quedan abiertos.")
d.tabla("t06", "Articulación con retos estratégicos y demandas territoriales",
        ["Elemento", "Descripción", "Estado"],
        [("Reto estratégico del plan bienal (Anexo 4)", "[DATO_USUARIO: reto y código]", "VACIO"),
         ("Demanda territorial", "Mediciones de PM2,5 y PM10 con error conocido para la gestión del riesgo posterremoto", "PROPUESTO"),
         ("Alcance temático de los términos de referencia", "[DATO_USUARIO: numeral 5 de los términos de referencia]", "VACIO"),
         ("Respuesta del proyecto", "Red de 100 nodos y 10 gateways, modelo de corrección, gemelo digital, tablero y protocolo de alerta", "PROPUESTO"),
         ("Medida de atención de la demanda", "Uso del tablero por 75 % o más de 15 comités al mes 24 (PERS-E01)", "PROPUESTO")],
        "*Nota.* Elaboración propia con la ficha maestra. El expediente trata la articulación territorial en la sección 5.3.3 del capítulo 5.")

# ============================================================== 9
d.raw("# 9. MARCO CONCEPTUAL")
d.p("El marco conceptual articula cuatro ideas. La primera es la calibración colocalizada, que compara un sensor de bajo costo con un equipo de referencia en el mismo sitio. La segunda es la computación en el borde, que ejecuta la corrección en el gateway y no en la nube (Shi et al., 2016). La tercera es el gemelo digital, una representación en software que se actualiza con datos del sistema físico (Grieves y Vickers, 2017). La cuarta es la madurez tecnológica, medida con niveles TRL (Mankins, 1995).")
d.p("Los umbrales de desempeño siguen los criterios informativos de la EPA (2021): R² ≥ 0,70, NRMSE ≤ 30 %, pendiente entre 0,65 y 1,35 y sesgo entre −5,0 y 5,0 µg/m3. Los datos de la red no sustituyen la medición regulatoria. El tablero muestra el error residual junto con cada valor.")
d.h(2, "9.1 Marco de política pública y marco normativo")
d.p("La Ley 1523 de 2012 organiza la gestión del riesgo en procesos de conocimiento, reducción y manejo (Congreso de la República, 2012a). La Ley 2056 de 2020 regula el Sistema General de Regalías (Congreso de la República, 2020). La Ley 1286 de 2009 fortalece el Sistema Nacional de Ciencia, Tecnología e Innovación (Congreso de la República, 2009). La Resolución 2254 de 2017 adopta la norma de calidad del aire ambiente (Ministerio de Ambiente y Desarrollo Sostenible, 2017).")
d.p("El marco internacional incluye el Marco de Sendái 2015-2030 (Oficina de las Naciones Unidas para la Reducción del Riesgo de Desastres [UNDRR], 2015) y la Agenda 2030 (Organización de las Naciones Unidas [ONU], 2015). El expediente desarrolla el marco teórico en el capítulo 4.")

d.guardar(os.path.join(RAIZ, "caps", "a2a.md"))
print("a2a ok")
