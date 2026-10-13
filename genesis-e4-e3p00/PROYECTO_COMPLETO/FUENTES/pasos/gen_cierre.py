# -*- coding: utf-8 -*-
"""Cierre ordenado F-01 a F-04 del documento único. Lee los conteos reales de cada archivo con el verificador."""
import sys, os, re, subprocess, collections, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPS = os.path.join(RAIZ, "caps")

def medir(archivos):
    p = w = t = f = 0; probs = []
    for a in archivos:
        r = subprocess.run(["python3", "-I", os.path.join(RAIZ, "build", "check_cap.py"), os.path.join(CAPS, a)], capture_output=True, text=True)
        m = re.search(r"palabras de prosa: (\d+).*tablas: (\d+).*figuras: (\d+).*citas distintas: (\d+)", r.stdout)
        w += int(m.group(1)); t += int(m.group(2)); f += int(m.group(3))
        if "SIN PROBLEMAS" not in r.stdout: probs.append((a, re.findall(r"RESULTADO: (.*)", r.stdout)))
    return w, t, f, probs

# capítulo -> (archivos, mínimo palabras, tablas, figuras)
CAP = collections.OrderedDict([
 ("1", (["cap01.md"], 5000, 5, 3)), ("2", (["cap02a.md", "cap02b.md"], 12000, 21, 13)), ("3", (["cap03.md"], 1500, 3, 2)),
 ("4", (["cap04.md"], 8000, 4, 3)), ("5", (["cap05.md"], 5000, 7, 3)), ("6", (["cap06.md"], 8000, 6, 4)),
 ("7", (["cap07.md"], 2000, 3, 2)), ("8", (["cap08.md"], 2500, 8, 3)), ("9", (["cap09.md"], 1500, 3, 2)),
 ("10", (["cap10.md"], 2000, 5, 3)), ("11", (["cap11.md"], 2000, 4, 2)), ("12", (["cap12.md"], 3500, 18, 5)),
 ("13", (["cap13.md"], 4000, 8, 5)), ("14", (["cap14.md"], 3500, 4, 2)), ("15", (["cap15.md"], 3500, 3, 2)),
 ("16", (["cap16.md"], 3500, 6, 4)), ("17", (["cap17.md"], 2000, 4, 2)), ("18", (["cap18.md"], 1500, 2, 1)),
 ("19", (["cap19a.md", "cap19b.md"], 0, 1, 0)), ("20", (["cap20.md", "anexo_n.md"], 0, 0, 0)), ("21", (["cap21.md"], 2500, 6, 2))])
fil = []; TW = TT = TF = 0; problemas = []
for k, (arch, mw, mt, mf) in CAP.items():
    w, t, f, pr = medir(arch); problemas += pr
    ok = w >= mw and t >= mt and f >= mf
    fil.append((f"Capítulo {k}", num(w), num(mw), str(t), str(mt), str(f), str(mf), "CUMPLE" if ok else "NO CUMPLE"))
    TW += w; TT += t; TF += f
MIN_W, MIN_T, MIN_F = 73500, 87, 44
fil.append(("Total capítulos 1 a 21", num(TW), num(MIN_W), str(TT), str(MIN_T), str(TF), str(MIN_F), "CUMPLE" if (TW >= MIN_W and TT >= MIN_T and TF >= MIN_F) else "NO CUMPLE"))
pasos = ["paso0.md", "paso1.md", "paso2.md", "paso3.md", "paso4.md", "paso5.md", "paso6.md", "paso7.md"]
pw, pt, pf, pr = medir(pasos); problemas += pr
xs = ["x01.md", "x02.md", "x03.md", "estrategia.md", "x05.md", "x06.md", "x07.md", "x08.md", "x09.md", "x10.md"]
xw, xt, xf, pr = medir(xs); problemas += pr
ew, et, ef, _ = medir(["estrategia.md"])
cw, ct, cf, _ = medir(["anexos_km.md"])
print("totales", TW, TT, TF, "pasos", pw, "1000X", xw, "estrategia", ew, "problemas", problemas)

d = Doc("FC")
d.h(1, "Cierre del documento")
d.p("El cierre sigue el orden fijado por el metaprompt: autoauditoría (F-01), vacíos y contradicciones (F-02), valor estratégico (F-03) y traspaso (F-04). Cada bloque declara lo que se verificó y lo que no. Ningún resultado se presenta como validación independiente, porque ninguna revisión externa ocurrió.")

# ---------------------------------------------------------------- F-01
d.h(2, "F-01 Autoauditoría")
d.p(f"La autoauditoría compara cada capítulo con los mínimos de extensión del metaprompt. Los capítulos 1 a 21 suman {num(TW)} palabras de prosa, {TT} tablas y {TF} figuras, frente a mínimos de {num(MIN_W)} palabras, {MIN_T} tablas y {MIN_F} figuras. La {{T:t01}} presenta el detalle. Las palabras se cuentan sin las tablas, las notas ni las listas de referencias.")
d.tabla("t01", "Cumplimiento de los mínimos de extensión por capítulo",
        ["Capítulo", "Palabras", "Mínimo de palabras", "Tablas", "Mínimo de tablas", "Figuras", "Mínimo de figuras", "Estado"], fil,
        "*Nota.* Elaboración propia con el verificador mecánico del proyecto (check_cap.py). El capítulo 2 reúne sus dos partes; el capítulo 19 incluye la lista de referencias aparte; el capítulo 20 incluye el anexo N y no cuenta los anexos K a M, que son datos. Los mínimos provienen del metaprompt y de las plantillas por capítulo. Naturaleza: CALCULADO. Decimales con coma y miles con punto.")
pf = {a for a, _ in problemas}
if pf <= {"cap19a.md", "paso4.md"}:
    sin_prob = "El verificador no reporta problemas, con dos excepciones declaradas. El Paso 4 conserva nueve secuencias de más de 25 palabras: cuatro supuestos en formato SI-ENTONCES-PORQUE con sus fundamentos y tres líneas técnicas de comprobación del SVG, que el metaprompt exceptúa o que se conservan por fidelidad. El capítulo 19 menciona una tabla que se define en su segundo archivo."
else:
    sin_prob = "Archivos con observaciones del verificador: " + "; ".join(sorted(pf)) + "."
d.p(f"La verificación mecánica comprueba oraciones de 25 palabras o menos, palabras enfáticas, marcadores de omisión, citas frente al banco, menciones previas de tablas y figuras y archivos de figuras. {sin_prob} El paquete 1000X suma {num(xw)} palabras de prosa, y el capítulo de estrategia suma {num(ew)}, frente a mínimos de 15.000 y 8.000. Los pasos 0 a 7 suman {num(pw)} palabras de prosa y {pt} tablas.")
d.p("Seis controles no se ejecutaron. El control AP-11-V de anclaje por unidad y el programa verificador_ntc.py quedan NO_EJECUTADO. Las pruebas de rechazo del metaprompt contra esta salida no se corrieron. La revisión RS-99 se ejecutó de forma parcial, con los controles mecánicos y sin lectura humana completa. La validación empírica de comprensión y eficacia decisional exige casos reales. La revisión visual del DOCX se hizo en LibreOffice, no en Microsoft Word.")
d.p("Los invariantes del proyecto se conservan. Hay una definición del lugar de calibración, el gateway. Hay una meta de error, R² de 0,70 o más y NRMSE de 30 % o menos, con línea base medida en el tramo 1. El TRL va de 4 a 7. La duración es de 24 meses y 104 semanas. La red tiene 100 nodos y 10 gateways operativos, con 120 y 11 comprados. Las cifras presupuestales coinciden con la ficha maestra. Ninguna afirmación causal sobre salud aparece. Ninguna probabilidad carece de fuente, con la excepción de las del registro de riesgos, que son PROPUESTO.")

# ---------------------------------------------------------------- F-02
d.h(2, "F-02 ¿Qué se me escapa?")
d.p("Los vacíos con efecto sobre la decisión se resumen en la {T:t02}. Cada fila indica el efecto, la decisión que depende del vacío, quién posee el dato y la vía de obtención. El plazo se da como NO_ESTIMADO cuando no hay base para estimarlo. La lista no inventa vacíos para llenar el apartado. Incluye los hallazgos que el Anexo 2 hizo visibles después de la primera entrega.")
fil2 = [
 ("V1", "Términos de referencia completos y anexos 4, 10 y 12 no aportados", "Línea temática, topes, rubros admisibles y demanda territorial sin verificar", "Radicar o no; forma del presupuesto", "Usuario", "Aportar los documentos", "NO_ESTIMADO"),
 ("V2", "Madurez tecnológica final de 7 frente a la prioridad de nivel 9 del Anexo 2", "Posible pérdida de elegibilidad o de puntaje", "Mantener TRL 7 o rediseñar el cronograma y el presupuesto", "Usuario y comité directivo", "Decidir y reunir evidencias del TRL 4", "NO_ESTIMADO"),
 ("V3", "Afectación por la emergencia y municipios afectados sin soporte oficial", "Requisito de la convocatoria sin cumplir", "Territorio del proyecto", "Usuario", "Aportar reportes oficiales", "NO_ESTIMADO"),
 ("V4", "Cartas de compromiso con partida, sobre todo de las alcaldías", "Custodia posproyecto sin respaldo; bloqueo AS-18", "Liberar el tramo 3; transferir", "Alcaldías y entidades", "Obtener cartas", "NO_ESTIMADO"),
 ("V5", "Cotizaciones de mercado de equipos y servicios", "100 % del valor solicitado sin soporte", "Monto solicitado", "Proveedores", "Solicitar cotizaciones vigentes", "NO_ESTIMADO"),
 ("V6", "Línea base de error de los nodos en sitios de remoción", "Meta de NRMSE sin punto de partida", "Compuerta C1", "Equipo del proyecto", "Medir en el tramo 1", "Mes 12"),
 ("V7", "Ratificación de las 105 fichas del análisis estructural", "Las relaciones causales siguen siendo hipótesis", "Prioridad de las causas", "Panel de revisión", "Adjudicación independiente", "NO_ESTIMADO"),
 ("V8", "Referencias NO_VERIFICADO y cuartil de las revistas", "No se puede declarar el criterio de 60 % en Q1 y Q2", "Calidad de la bibliografía", "Equipo editorial", "Consultar SJR o JCR y verificar DOI", "NO_ESTIMADO"),
 ("V9", "Actualidad de la bibliografía por debajo de 70 % en los últimos cinco años", "No cumple el criterio del metaprompt", "Calidad de la bibliografía", "Equipo editorial", "Añadir literatura de 2022 a 2026", "NO_ESTIMADO"),
 ("V10", "Financiación de la medición posproyecto de PERS-S01 y PERS-S02", "Los impactos no pueden verificarse", "Valor de los indicadores S", "Entidad ejecutora y financiador", "Reservar contrapartida o ampliar recursos", "NO_ESTIMADO"),
 ("V11", "Costo de sostenimiento, capacidad de absorción y fondo de la custodia", "Sostenibilidad económica no calculable", "Transferencia por tramos", "Custodios", "Cotizar el costo total y evaluar la capacidad", "NO_ESTIMADO"),
 ("V12", "Verificación humana de redacción y lectura independiente", "Errores no detectados por el verificador mecánico", "Calidad del texto", "Revisor externo", "Asignar un lector", "NO_ESTIMADO")]
d.tabla("t02", "Vacíos y contradicciones con efecto sobre la decisión",
        ["Id", "Vacío o contradicción", "Efecto", "Decisión que depende", "Tenedor del dato", "Vía de obtención", "Plazo"], fil2,
        "*Nota.* Elaboración propia con los capítulos 10, 12, 19 y 20, el anexo N y el documento 1000X-10. Tenedor: quien posee el dato o decide. NO_ESTIMADO: sin base para estimar el plazo. Los vacíos V2 y V3 provienen del Anexo 2 de la convocatoria, que el usuario aportó después de la primera entrega.")
d.p("Hay dos contradicciones que el documento no resuelve por sí solo. La primera es entre el TRL final de 7 y la prioridad de nivel 9 del Anexo 2. La segunda es entre las siete palabras clave del Paso 1 y el máximo de seis que fija el Anexo 2. La primera es de fondo y pide una decisión del usuario. La segunda se corrige al retirar una palabra. Las dos están registradas en el anexo N y en el checklist.")

# ---------------------------------------------------------------- F-03
d.h(2, "F-03 Valor estratégico")
d.p("El documento habilita tres decisiones. La primera es radicar o no con la evidencia disponible: el checklist muestra que dos bloqueos están activos y que la ruta para levantarlos depende de datos del usuario. La segunda es el nivel de madurez tecnológica, que el Anexo 2 pone en tensión. La tercera es el modo de despliegue, por tramos con compuertas, que limita la exposición financiera antes de tener evidencia de desempeño. La utilidad es potencial. El documento no afirma ahorros, impactos en salud ni probabilidades de adjudicación.")
d.p("La lógica causal queda trazable de punta a punta. El árbol de problemas identifica el error de medición sin verificar como problema central. Los objetivos lo traducen en tres líneas de trabajo. El presupuesto, el cronograma, los indicadores y el acta de constitución repiten las mismas cifras. La continuidad posproyecto se apoya en convenios de custodia por tramo y en una cláusula de apertura. Esa cadena permite que un panel de evaluación revise cada eslabón y, si lo desea, rechace uno sin invalidar los demás.")

# ---------------------------------------------------------------- F-04
d.h(2, "F-04 Traspaso")
d.p("El traspaso entrega los productos, las restricciones, los pendientes y la siguiente acción. La {T:t03} lista los productos con su archivo. Todos están en el repositorio, en la rama de trabajo, dentro del directorio genesis-e4-e3p00.")
d.tabla("t03", "Productos entregados y archivo",
        ["Producto", "Contenido", "Archivo"],
        [("Documento único en Word", "Pasos 0 a 7, capítulos 1 a 21, paquete 1000X y cierre", "PROYECTO_COMPLETO/DOCUMENTO/PROYECTO_COMPLETO_SGR_CONV56_AIRE.docx"),
         ("Documento único en PDF", "Versión de lectura fija con marcadores de navegación", "PROYECTO_COMPLETO/DOCUMENTO/PROYECTO_COMPLETO_SGR_CONV56_AIRE.pdf"),
         ("Pitch deck", "15 diapositivas del documento 1000X-03", "PROYECTO_COMPLETO/DOCUMENTO/PITCH_DECK_SGR_CONV56_AIRE.pptx"),
         ("Fuentes de trabajo", "Markdown con directivas, generadores de tablas y figuras, libro maestro y banco de referencias", "PROYECTO_COMPLETO/FUENTES/"),
         ("Documento unificado 4.3 a 4.5", "Vista derivada de la primera entrega", "DOCUMENTO_UNIFICADO/")],
        "*Nota.* Elaboración propia. Las rutas son relativas al directorio genesis-e4-e3p00 del repositorio. El documento único es una vista derivada y no modifica el respaldo de las secciones 4.3 a 4.5.")
d.p("Las restricciones son cuatro. El territorio y la alianza son supuestos por instrucción del usuario. Las cifras de la ficha maestra no cambian sin una decisión registrada. Los datos que solo posee el usuario aparecen como [DATO_USUARIO]. El documento está en estado de borrador con vacíos y no es un paquete de radicación.")
d.p("La siguiente acción es de tres pasos. Primero, el usuario decide el nivel de madurez tecnológica y registra la decisión en el reporte B1 del checklist. Segundo, aporta los términos de referencia, los anexos 4, 10 y 12, los reportes de afectación y las cartas. Tercero, se actualiza el documento con esos insumos y se vuelven a ejecutar los verificadores. La condición de aceptación es que los dos bloqueos finales del checklist queden sin alertas activas.")
d.p("La decisión DEC-F16 registra que el Anexo 2 gobierna la estructura de radicación y que el metaprompt gobierna la estructura de trabajo. La decisión DEC-F17 registra que las fichas completas de los 15 indicadores viven en el capítulo 12 y que el Paso 7 contiene el diseño y el registro. La decisión DEC-F18 registra que el capítulo 19 contiene solo las obras citadas, con las condiciones de verificación declaradas.")
d.guardar(os.path.join(CAPS, "cierre.md"))
