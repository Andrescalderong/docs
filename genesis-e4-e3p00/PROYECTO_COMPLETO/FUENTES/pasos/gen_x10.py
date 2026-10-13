# -*- coding: utf-8 -*-
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gu import *

d = Doc("X10")
cont = collections.Counter()
def sec(tid, titulo, filas, nota):
    for f in filas: cont[f[1]] += 1
    d.tabla(tid, titulo, ["Ítem", "Estado", "Evidencia o ubicación", "Brecha o acción"], filas, nota)

d.h(1, "Documento 1000X-10. Checklist de cumplimiento")
d.p("El checklist verifica los requisitos antes de la entrega. Tiene seis secciones, más una séptima que recoge los requisitos del Anexo 2 de la convocatoria. Cada ítem recibe un estado: CUMPLE, PARCIAL, NO CUMPLE, VACIO, NO_VERIFICADO o NO_EJECUTADO. VACIO indica que el dato solo lo posee el usuario. NO_EJECUTADO indica una verificación que esta corrida no realizó. El checklist termina con dos bloqueos finales del metaprompt. Si alguno está activo, el paquete no se aprueba para radicación.")
d.p("La verificación es mecánica y documental. Comprueba que el contenido exista, que sus cifras coincidan con la ficha maestra y que sus vacíos estén declarados. No comprueba la verdad de las fuentes, la validez de las probabilidades ni la admisibilidad frente a términos de referencia que no se aportaron. Un estado CUMPLE significa que el documento contiene el elemento. No significa que un evaluador lo apruebe.")

d.h(2, "X10.1 Requisitos administrativos")
d.p("Los requisitos administrativos dependen de documentos que el usuario y las entidades poseen. La {T:t01} registra siete ítems. Ninguno se cumple, porque ningún documento administrativo se aportó.")
sec("t01", "Verificación de requisitos administrativos", [
 ("Formulario diligenciado completamente", "VACIO", "Paso 1 reúne los datos de identificación; el formulario de la plataforma no se aportó", "Diligenciar el formulario con el código SIGP [DATO_USUARIO: código]"),
 ("Cartas de compromiso de todas las entidades", "VACIO", "Anexo A, tabla de cartas requeridas", "Obtener las ocho cartas del anexo A"),
 ("Avales institucionales", "VACIO", "Anexo A, fila A1", "Obtener la carta aval de la entidad ejecutora"),
 ("Certificados de grupos de investigación", "VACIO", "Anexo D", "Aportar certificados de vigencia"),
 ("Hojas de vida en el formato requerido", "VACIO", "Anexo B", "Aportar 29 hojas de vida y las de contrapartida"),
 ("RUT o NIT de las entidades", "VACIO", "Anexo J, fila J10", "Aportar los documentos tributarios"),
 ("Certificados de existencia y representación", "VACIO", "Anexo J, fila J10", "Aportar los certificados vigentes")],
 "*Nota.* Elaboración propia con la lista del metaprompt (documento 1000X-10, sección CK.1) y los anexos A, B, D y J. Todos los documentos son VACIO [DATO_USUARIO: documentos administrativos].")

d.h(2, "X10.2 Requisitos técnicos")
d.p("Los requisitos técnicos dependen del contenido que este documento sí contiene. La {T:t02} registra ocho ítems. Cinco se cumplen y tres se cumplen en parte. Las brechas provienen de la falta de cotizaciones, de líneas base por medir y de la falta de reserva de plazo.")
sec("t02", "Verificación de requisitos técnicos", [
 ("Problema claramente formulado con datos", "CUMPLE", "Capítulo 1; Pasos 4 y 5; sección 4.5", "La línea base de error se mide en el tramo 1"),
 ("Objetivos definidos con meta y plazo", "CUMPLE", "Capítulo 3; Paso 6.1", "Sin acción"),
 ("Metodología detallada", "PARCIAL", "Capítulo 6", "Añadir la actividad de administración y apoyo a la supervisión por objetivo (anexo N)"),
 ("Cronograma completo con hitos", "CUMPLE", "Capítulo 9; anexo H", "Convertir a meses en la radicación"),
 ("Presupuesto justificado por rubro", "PARCIAL", "Capítulo 8; anexos C y G", "Obtener cotizaciones; 100 % del valor solicitado carece de soporte de mercado"),
 ("Indicadores con fichas técnicas", "CUMPLE", "Capítulo 12; Paso 7", "Medir las cinco líneas base VACIO"),
 ("Marco lógico completo", "CUMPLE", "Capítulo 18", "Sin acción"),
 ("Plan de riesgos", "PARCIAL", "Capítulo 10; tabla del anexo N", "Añadir el riesgo sanitario del personal de campo")],
 "*Nota.* Elaboración propia con la lista del metaprompt (sección CK.2) y los capítulos indicados. Estados determinados por la existencia del contenido en este documento.")

d.h(2, "X10.3 Requisitos de formato")
d.p("Los requisitos de formato se verifican sobre el archivo entregado. La {T:t03} registra siete ítems. El límite de extensión no se verificó, porque los términos de referencia no lo informan. La paginación, la tabla de contenido y las listas de tablas y figuras son automáticas.")
sec("t03", "Verificación de requisitos de formato", [
 ("Extensión dentro del límite de páginas o palabras", "NO_VERIFICADO", "Los términos de referencia no se aportaron", "Confirmar el límite; el PDF entregado informa el número de páginas"),
 ("Formato de archivo correcto", "PARCIAL", "Se entregan DOCX y PDF; el formato de la plataforma no se aportó", "Confirmar el formato exigido"),
 ("Numeración de páginas", "CUMPLE", "Encabezado con número de página", "Sin acción"),
 ("Tabla de contenido", "CUMPLE", "Índice automático con enlaces", "Actualizar campos en Word"),
 ("Lista de tablas y figuras", "CUMPLE", "Índices de tablas y de figuras", "Actualizar campos en Word"),
 ("Referencias en formato APA 7", "PARCIAL", "Capítulo 19: solo obras citadas, con sangría francesa", "72 referencias NO_VERIFICADO; verificar DOI y páginas"),
 ("Anexos etiquetados correctamente", "CUMPLE", "Anexos A a N en el capítulo 20", "Sin acción")],
 "*Nota.* Elaboración propia con la lista del metaprompt (sección CK.3) y el archivo ensamblado. El recuento de páginas es el del PDF entregado.")

d.h(2, "X10.4 Coherencia del proyecto")
d.p("La coherencia comprueba que las partes del documento se sostengan entre sí. La {T:t04} registra seis ítems. Uno se cumple, cuatro se cumplen en parte y uno depende de datos del usuario. El hallazgo más importante es que el nivel de madurez tecnológica, 7, no coincide con la prioridad del Anexo 2.")
sec("t04", "Verificación de coherencia del proyecto", [
 ("Alineación entre problema, objetivos e indicadores", "CUMPLE", "Capítulos 1, 3, 12 y 18; trazabilidad de indicadores", "Sin acción"),
 ("El presupuesto corresponde con las actividades", "PARCIAL", "Capítulo 8 y anexo G: cada línea pertenece a un paquete de trabajo", "Separar la administración por objetivo"),
 ("El cronograma es realista", "PARCIAL", "Capítulo 9: ruta crítica de 104 semanas sin reserva de plazo", "Añadir una reserva de plazo o aceptar el riesgo"),
 ("El equipo tiene las capacidades requeridas", "VACIO", "Capítulo 17 y anexo B: perfiles PROPUESTO", "Aportar hojas de vida"),
 ("El TRL es coherente con la tipología", "PARCIAL", "Capítulo 6: TRL 4 a 7", "El Anexo 2 prioriza TRL 9; decidir (hallazgo G1)"),
 ("Los resultados son medibles y alcanzables", "PARCIAL", "Capítulo 12: 10 de 15 indicadores con línea base calculada", "Medir líneas base de cinco indicadores")],
 "*Nota.* Elaboración propia con la lista del metaprompt (sección CK.4). Los hallazgos G1 a G8 están en el anexo N.")

d.h(2, "X10.5 Criterios de evaluación")
d.p("Los criterios de evaluación son los cinco que el metaprompt asigna a una convocatoria del SGR, con los pesos que él declara. Los pesos son un supuesto, porque los términos de referencia no se aportaron. La {T:t05} registra la evidencia incluida para cada criterio y el estado.")
sec("t05", "Verificación de criterios de evaluación", [
 ("Criterio 1, pertinencia y articulación territorial (20 a 25 %): evidencia incluida", "PARCIAL", "Paso 5.0 y capítulo 5; PDD y Anexo 4 sin aportar", "Aportar el PDD, el Anexo 4 y los reportes de afectación"),
 ("Criterio 2, fortalecimiento regional de CTeI (25 a 27 %): evidencia incluida", "PARCIAL", "Capítulos 11, 12 y 16: productos tipificados MMG 2021", "Verificar la tipología con el catálogo MGA (anexo N)"),
 ("Criterio 3, calidad técnica (20 a 25 %): evidencia incluida", "CUMPLE", "Capítulos 6, 7 y 12; Pasos 4 a 7", "Ratificar las 105 fichas del análisis estructural"),
 ("Criterio 4, impacto esperado (15 a 20 %): evidencia incluida", "PARCIAL", "Capítulo 13: impactos institucionales sin efectos en salud", "Medir líneas base de E01, E02, S01 y S02"),
 ("Criterio 5, viabilidad presupuestal (10 a 15 %): evidencia incluida", "PARCIAL", "Capítulo 8: validación meta-recurso-cronograma sin alertas", "Cotizaciones y certificación de contrapartida")],
 "*Nota.* Elaboración propia con los criterios y los pesos del metaprompt, que son SUPUESTO y NO_VERIFICADO. CTeI: ciencia, tecnología e innovación. Los estados reflejan la evidencia presente en este documento.")

d.h(2, "X10.6 Revisión final")
d.p("La revisión final combina controles mecánicos y controles humanos. Esta corrida ejecutó los mecánicos y dejó pendientes los humanos. La {T:t06} registra seis ítems. El control de redacción verificó oraciones de 25 palabras o menos, palabras enfáticas, marcadores de omisión y citas frente al banco de referencias. No sustituye la lectura de una persona.")
sec("t06", "Verificación de la revisión final", [
 ("Revisión ortográfica y gramatical", "PARCIAL", "Verificador mecánico de redacción por capítulo; sin revisión humana", "Lectura de corrección de estilo"),
 ("Verificación de datos y cifras", "CUMPLE", "Cifras tomadas de la ficha maestra y de maestro.py; aserciones de coherencia en el código", "Repetir tras cualquier cambio de cifras"),
 ("Consistencia de terminología", "PARCIAL", "Glosario implícito en la ficha maestra", "Revisión humana de términos y siglas"),
 ("Lectura por tercero independiente", "NO_EJECUTADO", "No se realizó", "Asignar un lector externo"),
 ("Copia de respaldo de los archivos", "CUMPLE", "Repositorio con control de versiones y respaldo ZIP de las secciones 4.3 a 4.5", "Actualizar el respaldo con este documento"),
 ("Prueba de carga en plataforma", "NO_EJECUTADO", "La plataforma no es accesible desde esta corrida", "Probar la carga en el SIGP")],
 "*Nota.* Elaboración propia con la lista del metaprompt (sección CK.6). Las verificaciones NO_EJECUTADO requieren a una persona o a un sistema externo.")

d.h(2, "X10.7 Requisitos del Anexo 2 de la convocatoria")
d.p("El Anexo 2 añade requisitos que el metaprompt no contempla. El anexo N los cruza sección por sección. La {T:t07} resume los ocho hallazgos y su estado. Dos son de fondo: la madurez tecnológica de nivel 9 y el mínimo de 1 % de recursos para transferencia.")
sec("t07", "Verificación de los hallazgos derivados del Anexo 2", [
 ("G1: madurez tecnológica prioritaria de nivel 9", "NO CUMPLE", "Capítulo 6: TRL 4 a 7; anexo N", "Decidir TRL objetivo y reunir evidencias del TRL de entrada"),
 ("G2: 1 % de recursos para transferencia, adopción y valoración", "PARCIAL", "Capítulo 15; líneas S02, O03 y S09; anexo N", "Redactar el plan en el formato del Anexo 2 y confirmar la base de cálculo"),
 ("G3: actividad de administración y apoyo a la supervisión por objetivo", "NO CUMPLE", "Capítulo 9; anexo N, cadena de valor", "Separar WP0 en tres actividades"),
 ("G4: afectación por la emergencia con soporte oficial", "VACIO", "Paso 5.0; anexo J, fila J6", "Aportar reportes y municipios afectados"),
 ("G5: productos del catálogo MGA, programa 3906", "PARCIAL", "Capítulo 11; anexo N", "Verificar el catálogo y adoptar la asignación"),
 ("G6: máximo seis palabras clave", "NO CUMPLE", "Paso 1 lista siete", "Retirar una palabra"),
 ("G7: una entidad no es cooperante y beneficiaria a la vez", "NO_VERIFICADO", "Documento 1000X-08", "Reclasificar a los participantes"),
 ("G8: riesgos sanitarios en el registro", "NO CUMPLE", "Capítulo 10", "Añadir el riesgo de exposición del personal de campo")],
 "*Nota.* Elaboración propia con el Anexo 2 de la convocatoria y el anexo N. Estados: NO CUMPLE indica un requisito explícito del Anexo 2 que el documento no satisface hoy.")

# ------------------------------------------------------------------ bloqueos finales
d.h(2, "X10.8 Bloqueos finales del paquete")
d.p("El metaprompt fija dos bloqueos finales. El primero es toda alerta de compromiso débil emitida por el control jurídico de las cartas que permanezca sin subsanar. El segundo es todo reporte de brecha no resuelta que no exhiba una decisión humana registrada. La {T:t08} muestra el resultado. Ambos bloqueos están activos.")
sec("t08", "Verificación de los bloqueos finales", [
 ("Alertas de compromiso débil sin subsanar (aserción AS-18)", "NO CUMPLE", "Anexo A: ocho documentos VACIO; las cartas de las alcaldías sin partida son las más débiles", "Subsanar las alertas con cartas completas"),
 ("Reportes de brecha no resuelta con decisión humana (aserción AS-07)", "NO CUMPLE", "Tabla de reportes de brecha de este documento: seis reportes sin decisión", "Registrar la decisión (a), (b) o (c) en cada reporte")],
 "*Nota.* Elaboración propia con las reglas del metaprompt (documento 1000X-10). NO CUMPLE indica bloqueo activo: el paquete no se aprueba para radicación.")
d.p("Los reportes de brecha no resuelta siguen la plantilla del metaprompt. Cada reporte nombra el criterio incumplido, resume los intentos correctivos y pide una decisión del formulador. En esta corrida ningún intento correctivo fue posible, porque el dato faltante lo posee el usuario. La {T:t09} presenta los seis reportes.")
sec("t09", "Reportes de brecha no resuelta y decisión humana requerida", [
 ("B1: nivel de madurez tecnológica (TRL 7 frente a la prioridad de TRL 9)", "VACIO", "Intentos: ninguno posible; la decisión modifica el cronograma y el presupuesto. Decisión requerida: (a) aceptar TRL 7 con reserva; (b) aportar información y rediseñar; (c) eliminar el componente", "[DATO_USUARIO: decisión (a), (b) o (c), fecha y justificación]"),
 ("B2: cartas de compromiso con partida de las alcaldías", "VACIO", "Intentos: ninguno posible; las cartas las emiten las entidades. Decisión requerida: (a), (b) o (c)", "[DATO_USUARIO: decisión, fecha y justificación]"),
 ("B3: cotizaciones de mercado de equipos y servicios", "VACIO", "Intentos: ninguno posible; los proveedores deben cotizar. Decisión requerida: (a), (b) o (c)", "[DATO_USUARIO: decisión, fecha y justificación]"),
 ("B4: línea base de error de los nodos", "VACIO", "Intentos: ninguno posible antes del tramo 1. Decisión requerida: (a) aceptar con reserva; (b), (c)", "[DATO_USUARIO: decisión, fecha y justificación]"),
 ("B5: afectación por la emergencia y municipios afectados", "VACIO", "Intentos: ninguno posible; exige reportes oficiales. Decisión requerida: (a), (b) o (c)", "[DATO_USUARIO: decisión, fecha y justificación]"),
 ("B6: certificación de la contrapartida", "VACIO", "Intentos: ninguno posible; exige certificados contables. Decisión requerida: (a), (b) o (c)", "[DATO_USUARIO: decisión, fecha y justificación]")],
 "*Nota.* Elaboración propia con la plantilla Reporte de Brecha No Resuelta del metaprompt. El campo Brecha o acción contiene la decisión humana pendiente. Las opciones son: (a) aceptar el componente con reserva declarada; (b) aportar información adicional y relanzar el ciclo correctivo; (c) eliminar el componente.")

total = sum(cont.values())
d.p(f"El conteo de las secciones X10.1 a X10.8 da {total} ítems. De ellos, {cont['CUMPLE']} cumplen y {cont['PARCIAL']} cumplen en parte. Otros {cont['NO CUMPLE']} no cumplen y {cont['VACIO']} dependen de datos del usuario. Quedan {cont['NO_VERIFICADO']} sin verificar y {cont['NO_EJECUTADO']} sin ejecutar. El paquete no está listo para radicación. La ruta más corta para desbloquearlo consiste en tres acciones del usuario. Debe aportar los documentos de la convocatoria, decidir el nivel de madurez tecnológica y obtener las cartas con partida.")
d.guardar(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "caps", "x10.md"))
print("ok", dict(cont), total)
