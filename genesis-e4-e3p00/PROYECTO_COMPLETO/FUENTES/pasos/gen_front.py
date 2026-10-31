# -*- coding: utf-8 -*-
import sys
RAIZ = "/tmp/claude-0/-home-user-docs/8ca5c040-2adb-56b3-8e64-05d4e7e569ed/scratchpad/proy"
sys.path.insert(0, RAIZ + "/maestro")
import maestro as M
sgr = M.total(M.BUDGET); con = M.total(M.CONTRA)
L = []; A = L.append
A("# Índice de tablas {.unnumbered}"); A(""); A("@@INDICE_TABLAS@@"); A("")
A("# Índice de figuras {.unnumbered}"); A(""); A("@@INDICE_FIGURAS@@"); A("")
A("# Lista de siglas {.unnumbered}"); A("")
SIG = [
 ("AQHI", "Índice de calidad del aire y salud"), ("ASC", "Apropiación social del conocimiento"), ("CPM", "Método de la ruta crítica"),
 ("CTeI", "Ciencia, tecnología e innovación"), ("DANE", "Departamento Administrativo Nacional de Estadística"), ("DNP", "Departamento Nacional de Planeación"),
 ("EDT", "Estructura de desglose del trabajo"), ("EPA", "Agencia de Protección Ambiental de Estados Unidos"), ("F-E3", "Expediente E3-P00 aportado por el usuario"),
 ("F-INF", "Informe de vigilancia tecnológica y bibliometría aportado por el usuario"), ("HIE", "Hipótesis de influencia estructural"), ("IDC", "Estimando causal identificado bajo supuestos"),
 ("IES", "Institución de educación superior"), ("IoT", "Internet de las cosas"), ("LoRa", "Tecnología de radio de largo alcance y bajo consumo"),
 ("MCDA", "Análisis de decisión multicriterio"), ("MGA", "Metodología General Ajustada"), ("MinCiencias", "Ministerio de Ciencia, Tecnología e Innovación"),
 ("MMG", "Modelo de medición de grupos de investigación"), ("NMAE", "Error absoluto medio normalizado"), ("NRMSE", "Error cuadrático medio normalizado"),
 ("NTC", "Norma de trazabilidad del documento (NTC 1.1)"), ("PDD", "Plan de Desarrollo Departamental"), ("PERS", "Sistema de indicadores del proyecto (procesos, productos, efectos y sostenibilidad)"),
 ("PIIOM", "Política de investigación e innovación orientada por misiones"), ("PM2,5 y PM10", "Material particulado de hasta 2,5 y 10 micrómetros"), ("R²", "Coeficiente de determinación"),
 ("RACI", "Matriz de responsables, aprobadores, consultados e informados"), ("SGR", "Sistema General de Regalías"), ("TdR", "Términos de referencia"),
 ("TRL", "Nivel de madurez tecnológica"), ("UNGRD", "Unidad Nacional para la Gestión del Riesgo de Desastres"), ("VME", "Valor monetario esperado"), ("WP", "Paquete de trabajo"),
]
for s, d in SIG: A(f"**{s}.** {d}.  "); 
A("")
A("# Resumen ejecutivo del documento {.unnumbered}"); A("")
A("El proyecto se titula «" + M.IDENT["titulo"] + "». La convocatoria es la de Emergencia, Decreto 1414 de 2026 (SGR_CONV56). El documento sigue el paso a paso del metaprompt GENESIS-CTeI 36.10 RC2 en un solo archivo. Incluye los pasos 0 a 7, los 21 capítulos, el paquete de diez documentos 1000X y el capítulo de estrategia. El territorio, el evento y la alianza son supuestos de trabajo por instrucción del usuario. Los términos de referencia de la convocatoria no se aportaron.")
A("")
A("El proyecto propone una red de 100 nodos de bajo costo para medir PM2,5 y PM10. Los sitios son de remoción de escombros en Caldas, Cundinamarca y Valle del Cauca. La red usa 10 gateways y 3 monitores gravimétricos de referencia. El modelo de corrección se aplica en el gateway y se entrena por colocalización con las referencias. El despliegue ocurre en tres tramos condicionados por las compuertas C1 (mes 12) y C2 (mes 17). La duración es de 24 meses, equivalentes a 104 semanas, y la madurez tecnológica avanza del nivel 4 al nivel 7.")
A("")
A("El valor solicitado al SGR es de " + M.cop(sgr) + " COP, equivalente a 66,2 % del tope declarado de 14.000.000.000 COP. La contrapartida es de " + M.cop(con) + " COP y el total del proyecto es de " + M.cop(sgr + con) + " COP. Las metas de desempeño frente a la referencia son dos. El coeficiente de determinación debe ser de 0,70 o más. El error cuadrático medio normalizado debe ser de 30 % o menos. Además, la disponibilidad mensual de nodos debe ser de 90 % o más. Por último, al menos 75 % de los 15 comités de gestión del riesgo debe usar el tablero en decisiones documentadas.")
A("")
A("El proyecto no promete efectos en la salud de la población. Promete mediciones con error conocido, uso institucional verificado y continuidad de la red bajo custodia. Toda cifra tiene una naturaleza (declarada, calculada, propuesta, supuesta o vacía) y un estado de verificación. Los datos que solo el usuario posee se marcan como [DATO_USUARIO: descripción] y se reúnen en el cierre del documento. Mientras esos datos y los términos de referencia no existan, el documento no está listo para radicar.")
A("")
A("# Guía de lectura {.unnumbered}"); A("")
A("La Parte I reúne los pasos previos: configuración, información básica, ecuaciones de vigilancia, bibliometría, análisis causal, formalización, alternativas e indicadores. La Parte II desarrolla los 21 capítulos del proyecto. La Parte III contiene el paquete 1000X de documentos ejecutivos y el capítulo de estrategia. El cierre verifica la completitud, lista los datos pendientes y expone los vacíos. Las tablas y las figuras se numeran por capítulo, por ejemplo Tabla 8.3. Las de la Parte I y las del paquete 1000X llevan prefijo, por ejemplo Tabla F5.1 y Tabla X6.2. El apartado F0.4 explica los encabezados y la plantilla visual.")
open(RAIZ + "/caps/front.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
for n, t, d in [(1, "Parte I. Pasos previos del metaprompt", "Los pasos 0 a 7 configuran la convocatoria y reúnen la información básica. Definen las ecuaciones de vigilancia y procesan el corpus. Analizan las causas, formalizan el problema, comparan alternativas y diseñan los indicadores. Sus tablas y figuras llevan el prefijo F."),
                (2, "Parte II. Capítulos del proyecto", "Los capítulos 1 a 21 desarrollan el problema, el estado del arte, el marco normativo, los objetivos y la metodología. Desarrollan también la estructura de trabajo, el presupuesto, el cronograma, los riesgos y los resultados. Siguen los indicadores, los impactos, la sostenibilidad, la transferencia y la apropiación social. Cierran el equipo, el marco lógico, la bibliografía, los anexos y el Project Charter."),
                (3, "Parte III. Paquete 1000X y estrategia", "El paquete reúne diez documentos ejecutivos. Son el resumen, el one-pager, el pitch deck, el capítulo de estrategia y el modelo de negocio. Son también el análisis financiero, el roadmap, el mapa de interesados, el tablero de riesgos y la lista de cumplimiento. Sus tablas y figuras llevan el prefijo X y el número del documento.")]:
    open(RAIZ + f"/caps/div_parte{n}.md", "w", encoding="utf-8").write(f"# {t}\n\n{d}\n")
open(RAIZ + "/caps/div_cierre.md", "w", encoding="utf-8").write("# Cierre del documento\n\nEl cierre verifica la completitud contra los mínimos del metaprompt. Registra los datos pendientes del usuario y expone los vacíos. Entrega el valor estratégico y el traspaso. Sus cifras se calcularon sobre los archivos del documento en el momento del ensamblado.\n")
print("ok")
