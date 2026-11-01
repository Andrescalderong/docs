# -*- coding: utf-8 -*-
"""Soportes del TRL 4 de entrada (tabla 13.4 del Anexo 2) y ficha de identidad de Gestión y Medio Ambiente.
Uso: python3 build/soportes_trl.py carpeta_entrega"""
import os, sys, json
import docx
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = sys.argv[1]
A2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIM = json.load(open(os.path.join(A2, "data_v5", "sim_coloc.json")))
TIT = ("«Implementación de una red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por "
       "material particulado posterremoto» (SIGP 143329)")

def nuevo():
    d = docx.Document(); s = d.styles["Normal"]; s.font.name = "Arial"; s.font.size = Pt(10)
    for sec in d.sections: sec.left_margin = sec.right_margin = Cm(2.3)
    return d
def p(d, t, b=False, s=10, al=None):
    q = d.add_paragraph(); r = q.add_run(t); r.bold = b; r.font.size = Pt(s)
    if al is not None: q.alignment = al
    return q
def h(d, t): return p(d, t, b=True, s=11)
def tabla(d, enc, filas):
    t = d.add_table(rows=1, cols=len(enc)); t.style = "Table Grid"
    for i, x in enumerate(enc):
        t.rows[0].cells[i].text = x
        for r in t.rows[0].cells[i].paragraphs[0].runs: r.bold = True; r.font.size = Pt(8.5)
    for f in filas:
        c = t.add_row().cells
        for i, x in enumerate(f):
            c[i].text = x
            for r in c[i].paragraphs[0].runs: r.font.size = Pt(8.5)
    d.add_paragraph()
def pc(x): return f"{x*100:.2f} %".replace(".", ",")
def n(x, k=3): return f"{x:.{k}f}".replace(".", ",")
def guardar(d, ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True); d.save(ruta); print("ok", ruta)

# ------------------------------------------------------------------ informe 4
def informe4():
    d = nuevo(); E = SIM["escenarios"]; D = SIM["diseno"]
    p(d, "[Diligenciar: membrete de la Universidad Santo Tomás]", al=WD_ALIGN_PARAGRAPH.CENTER, s=9)
    p(d, "INFORME TÉCNICO 4. PROTOTIPO DEL MODELO DE CORRECCIÓN POR HUMEDAD", b=True, s=12, al=WD_ALIGN_PARAGRAPH.CENTER)
    p(d, f"Soporte del TRL 4 de entrada, tabla 13.4 del Anexo 2. Proyecto {TIT}.", s=9, al=WD_ALIGN_PARAGRAPH.CENTER)
    h(d, "1. Objeto")
    p(d, "Documentar el algoritmo de corrección que se ejecutará en los gateways y verificar, mediante simulación, que el diseño de colocalización del tramo 1 permite estimarlo y evaluarlo con los criterios de aceptación de la compuerta C1. Este informe valida el diseño del análisis; no mide el desempeño físico de ningún sensor.")
    h(d, "2. Algoritmo implementado")
    p(d, "Regresión lineal común a los nodos de un municipio: Ĉ = b0 + b1·S + b2·HR + b3·S·HR, donde S es la lectura cruda del nodo (µg/m³), HR la humedad relativa (%) y Ĉ la concentración corregida. Los coeficientes se estiman por mínimos cuadrados con las semanas 1 a 11 y se evalúan con las semanas 12 a 16 (partición temporal). La transferencia espacial se evalúa entrenando con un municipio y probando en el otro, en los dos sentidos. El código se encuentra en fuentes/v2/sim_coloc.py del repositorio del proyecto, con semilla fija 20261029.")
    h(d, "3. Diseño simulado")
    tabla(d, ["Parámetro", "Valor"], [
        ("Municipios y nodos", f"{D['municipios']} municipios, {D['nodos_por_municipio']} nodos por municipio"),
        ("Duración", f"16 semanas, {D['horas_por_nodo']:,} horas por nodo".replace(",", ".")),
        ("Referencia", "Conjunto rotativo: monitor beta y monitor óptico intercambiados entre municipios en la semana 8; sesgo de instrumento de +3 % y −3 %"),
        ("Respuesta del sensor", "Factor de crecimiento higroscópico 1 + 0,10·(HR/100)²/(1 − HR/100); ganancia por nodo N(1; 0,10); desplazamiento N(0; 2) µg/m³"),
        ("Concentración", "Serie horaria autocorrelacionada con ciclo diario y episodios de remoción (3 a 8 veces el nivel de fondo); medias supuestas de 22 y 18 µg/m³"),
        ("Humedad", "Medias supuestas de 80 % y 74 %, con ciclo diario"),
        ("Escenarios de ruido", "Bajo (15 % multiplicativo y 1 µg/m³ aditivo), medio (30 % y 2 µg/m³) y alto (50 % y 4 µg/m³)"),
        ("Campañas", f"{D['campanas_por_escenario']:,} por escenario".replace(",", "."))])
    h(d, "4. Criterio de aceptación (fijado antes de simular)")
    p(d, "Cumplimiento simultáneo a 24 horas de R² ≥ 0,70, NRMSE ≤ 30 %, pendiente entre 0,65 y 1,35 y sesgo entre −5 y 5 µg/m³, en al menos 80 % de las campañas del escenario medio.")
    h(d, "5. Resultados")
    tabla(d, ["Indicador", "Bajo", "Medio", "Alto"], [
        ("R² a 1 hora (mediana)", n(E["bajo"]["R2_1h_mediana"]), n(E["medio"]["R2_1h_mediana"]), n(E["alto"]["R2_1h_mediana"])),
        ("NRMSE a 1 hora (mediana)", pc(E["bajo"]["NRMSE_1h_mediana"]), pc(E["medio"]["NRMSE_1h_mediana"]), pc(E["alto"]["NRMSE_1h_mediana"])),
        ("R² a 24 horas (mediana)", n(E["bajo"]["R2_24h_mediana"]), n(E["medio"]["R2_24h_mediana"]), n(E["alto"]["R2_24h_mediana"])),
        ("NRMSE a 24 horas (mediana)", pc(E["bajo"]["NRMSE_24h_mediana"]), pc(E["medio"]["NRMSE_24h_mediana"]), pc(E["alto"]["NRMSE_24h_mediana"])),
        ("Pendiente a 24 horas (mediana)", n(E["bajo"]["pend_24h_mediana"]), n(E["medio"]["pend_24h_mediana"]), n(E["alto"]["pend_24h_mediana"])),
        ("Campañas que cumplen a 24 horas", pc(E["bajo"]["cumple_24h"]), pc(E["medio"]["cumple_24h"]), pc(E["alto"]["cumple_24h"])),
        ("Campañas que cumplen a 1 hora", pc(E["bajo"]["cumple_1h"]), pc(E["medio"]["cumple_1h"]), pc(E["alto"]["cumple_1h"])),
        ("Transferencia entre municipios, cumplimiento a 24 horas (2.000 pruebas: 1.000 campañas en dos sentidos)", f"{pc(E['bajo']['transfer_cumple_24h'])} ({round(E['bajo']['transfer_cumple_24h']*2000):,} de 2.000)".replace(",", "."), f"{pc(E['medio']['transfer_cumple_24h'])} ({round(E['medio']['transfer_cumple_24h']*2000):,} de 2.000)".replace(",", "."), f"{pc(E['alto']['transfer_cumple_24h'])} ({round(E['alto']['transfer_cumple_24h']*2000):,} de 2.000)".replace(",", "."))])
    h(d, "5a. Reproducibilidad")
    p(d, "El código (sim_coloc.py), la salida completa (sim_coloc.json), la salida de consola y las huellas SHA-256 se entregan en la carpeta Anexo_informe4_codigo_y_salidas junto a este informe. Se reproduce con Python 3 y NumPy: python3 sim_coloc.py sim_coloc.json. La semilla fija (20261029) produce exactamente las cifras de este informe.")
    h(d, "6. Conclusión")
    p(d, f"El algoritmo está implementado y, en el escenario medio, cumple el criterio a 24 horas en {pc(E['medio']['cumple_24h'])} de las campañas, por encima del 80 % fijado; en el escenario alto, en {pc(E['alto']['cumple_24h'])}. A 1 hora no cumple en los escenarios medio y alto, razón por la cual el proyecto usa el promedio de 24 horas como criterio principal de las compuertas y el horario como secundario.")
    h(d, "7. Limitaciones")
    p(d, "Los parámetros de la respuesta del sensor, de la humedad y de la concentración son supuestos de formulación, no mediciones del territorio. La simulación no incluye la fracción gruesa del polvo de escombros ni la deriva del cabezal. La validación física del modelo ocurre en la actividad 1.2 (cámara climática y banco de aerosol) y en la colocalización del tramo 1 (actividad 1.3), cuyos resultados decide la compuerta C1 en el mes 12.")
    p(d, "\nElaboró: [Diligenciar: nombre, cargo y firma del responsable técnico de la universidad]    Fecha: [Diligenciar]")
    guardar(d, os.path.join(OUT, "02_FIRMAR", "A_Universidad_Santo_Tomas", "Informe_TRL4_04_modelo_de_correccion.docx"))

# ------------------------------------------------------------------ protocolo informes 1 a 3
def protocolo():
    d = nuevo()
    p(d, "PROTOCOLO DE LAS PRUEBAS DE ACEPTACIÓN DE LOS LOTES DE NODOS Y GATEWAYS (MESES 4 A 6, ACTIVIDAD 1.2)", b=True, s=12, al=WD_ALIGN_PARAGRAPH.CENTER)
    p(d, f"Proyecto {TIT}. Se ejecuta en el banco de calibración y la cámara de humedad del proyecto (Anexo 3, EQ-07 y EQ-23) sobre cada lote recibido. Verifica lo que el fabricante declara en su documentación técnica, su informe de prueba de fábrica y su declaración de conformidad (tabla 13.4 del Anexo 2). Cada informe lo firma el especialista en metrología y calibración de la universidad y se archiva como evidencia del TRL 5.", s=9)
    comun = ("Contenido mínimo de cada informe: (a) identificación de la unidad ensayada (fabricante, modelo, número de serie, versión de firmware); "
             "(b) laboratorio, fecha, responsable y condiciones ambientales; (c) instrumentos de referencia con su certificado de calibración vigente; "
             "(d) montaje y procedimiento; (e) datos crudos en anexo digital; (f) métricas calculadas; (g) comparación con el criterio de aceptación; "
             "(h) firma del responsable técnico.")
    p(d, comun)
    for tit, obj, proc, met, crit in [
        ("Prueba 1. Caracterización del sensor óptico de partículas",
         "Demostrar que el cabezal integrado en el nodo responde a PM2,5 y PM10 y cuantificar el efecto de la humedad.",
         "Exponer el nodo y un instrumento de referencia en cámara cerrada a un aerosol de prueba (polvo de ensayo normalizado) en al menos cuatro niveles de concentración, a humedad relativa de 40 %, 60 %, 80 % y 90 %, con 30 minutos de estabilización por nivel.",
         "Pendiente, intercepto, R² y sesgo por nivel de humedad; curva de crecimiento con la humedad.",
         "R² ≥ 0,90 a humedad ≤ 60 %. El sesgo por humedad se reporta sin umbral, porque es el dato que el modelo de corrección corrige."),
        ("Prueba 2. Enlace nodo-gateway",
         "Demostrar que el nodo y el gateway intercambian datos en la banda de uso libre de 915 a 928 MHz.",
         "Configurar el nodo para transmitir cada minuto y registrar al menos 1.000 paquetes por punto en campo abierto y entre edificios, a distancias crecientes hasta la distancia de diseño entre nodo y gateway.",
         "Tasa de entrega de paquetes, RSSI y SNR por distancia; factor de dispersión usado.",
         "Entrega ≥ 90 % de los paquetes a la distancia de diseño."),
        ("Prueba 3. Consumo y autonomía del nodo",
         "Demostrar que el presupuesto de energía del nodo, con el panel y la batería ofertados, es compatible con 14 días sin sol.",
         "Medir con fuente y medidor de corriente el consumo en reposo, en medición y en transmisión durante al menos 24 horas de operación normal; medir la capacidad útil de la batería en un ciclo de descarga a temperatura ambiente.",
         "Consumo diario (Wh/día), capacidad útil (Wh) y autonomía calculada con radiación nula.",
         "Autonomía calculada ≥ 14 días.")]:
        p(d, tit, b=True, s=11)
        tabla(d, ["Campo", "Contenido"], [("Objeto", obj), ("Procedimiento", proc), ("Métricas", met), ("Criterio de aceptación", crit), ("Resultado", "[Diligenciar al ejecutar la prueba]"), ("Firma del responsable técnico", "[Diligenciar]")])
    p(d, "Un lote que no cumple un criterio de aceptación se devuelve al proveedor, según la condición incluida en el documento de compra. Los resultados alimentan la verificación del TRL 5 en el mes 10.", s=9)
    guardar(d, os.path.join(OUT, "04_OBTENER_DE_TERCEROS", "Protocolo_pruebas_aceptacion_lotes_meses_4_a_6.docx"))


# ------------------------------------------------------------------ carta al proveedor
def carta_siot():
    d = nuevo()
    p(d, "[Diligenciar: ciudad], 1 de noviembre de 2026")
    p(d, "Señores\nSIOT\n[Diligenciar: nombre y cargo del contacto comercial]\n[Diligenciar: correo]")
    p(d, "Asunto: solicitud de documentación técnica del nodo X950LS TRACK+ y del gateway SG50 solar para el proyecto SIGP 143329", b=True)
    p(d, f"Respetados señores: la Universidad Santo Tomás, entidad proponente del proyecto {TIT}, agradece su comunicación comercial del 26 de octubre de 2026. "
         "El documento técnico del proyecto sustenta el nivel de madurez de entrada con equipos comerciales ya probados. Por eso solicitamos los siguientes documentos sobre los equipos ofertados:")
    tabla(d, ["N.º", "Documento", "Contenido mínimo"], [
        ("1", "Documentación técnica del nodo X950LS TRACK+ y del gateway SG50 solar", "Fichas técnicas; fabricante y modelo del sensor óptico de partículas; rango y resolución de PM2,5 y PM10; consumo en reposo, medición y transmisión; capacidad de la batería y potencia del panel; versión de firmware"),
        ("2", "Informe de prueba de fábrica o de laboratorio del nodo enlazado con el gateway", "Unidades identificadas por modelo y número de serie; paquetes enviados y recibidos; lecturas de PM2,5 y PM10 visibles en la plataforma; fecha, lugar y firma del responsable técnico"),
        ("3", "Declaración de conformidad con la banda de uso libre", "Operación en 915 a 928 MHz, sin uso del segmento 902 a 915 MHz; plan de canales; potencia máxima radiada (PIRE) y ganancia de la antena; conformidad con el Anexo 1 de la Resolución ANE 105 de 2020 en su compilación vigente; homologación o registro ante la CRC, si aplica"),
        ("4", "Referencias de instalación", "Instalaciones en operación del mismo modelo: cliente, ciudad, año, número de nodos y contacto que confirme la referencia"),
        ("5", "Aceptación de las pruebas de aceptación por lote", "Confirmación de que aceptan las pruebas de sensor, enlace y autonomía de los meses 4 a 6 y la devolución del lote que no cumpla los criterios adjuntos"),
    ])
    p(d, "Criterios de aceptación por lote: R² ≥ 0,90 del sensor frente a la referencia con humedad de hasta 60 %, con el sesgo por humedad reportado; entrega de al menos 90 % de los paquetes a la distancia de diseño entre nodo y gateway; y autonomía calculada de al menos 14 días sin sol con la batería ofertada.")
    p(d, "Agradecemos enviar los documentos firmados por su representante o responsable técnico a más tardar el lunes 2 de noviembre de 2026 a las 12:00 m., porque la convocatoria cierra el martes 3 de noviembre a las 4:00 p. m. Si algún documento no está disponible en ese plazo, les pedimos indicarlo por escrito con la fecha en que podrán entregarlo.")
    p(d, "Esta solicitud no constituye orden de compra ni compromiso contractual.", s=9)
    p(d, "Cordialmente,")
    p(d, "\n\n[Diligenciar: nombre]\n[Diligenciar: cargo]\nUniversidad Santo Tomás\n[Diligenciar: correo y teléfono]")
    guardar(d, os.path.join(OUT, "04_OBTENER_DE_TERCEROS", "Carta_solicitud_SIOT_documentacion_tecnica.docx"))

# ------------------------------------------------------------------ ficha GMA
def ficha_gma():
    d = nuevo()
    p(d, "FICHA DE IDENTIDAD Y CAPACIDADES DE GESTIÓN Y MEDIO AMBIENTE", b=True, s=12, al=WD_ALIGN_PARAGRAPH.CENTER)
    p(d, f"Entidad aliada No. 4 del proyecto {TIT}. Datos que alimentan las secciones 1 y 26 del Anexo 2, el Anexo 1 y el numeral 10.12 de los términos de referencia.", s=9)
    tabla(d, ["Campo", "Dato", "Soporte"], [
        ("Razón social", "[Diligenciar]", "Certificado de existencia y representación legal (menos de 90 días)"),
        ("NIT", "[Diligenciar]", "RUT"),
        ("Fecha de constitución (al menos un año antes del 8 de octubre de 2026)", "[Diligenciar]", "Certificado de existencia; verificación en el RUES"),
        ("Domicilio principal", "Manizales (Caldas) [Diligenciar: dirección]", "Certificado de existencia"),
        ("Representante legal y cédula", "[Diligenciar]", "Certificado de existencia"),
        ("Objeto social relacionado con calidad del aire", "[Diligenciar]", "Certificado de existencia"),
        ("Tamaño de empresa y sector (CIIU)", "[Diligenciar]", "RUT"),
        ("Equipos de monitoreo que aporta (EQ-13)", "[Diligenciar: marca, modelo, serie, variable medida y fecha del último certificado de calibración de cada equipo]", "Inventario firmado y certificados de calibración"),
        ("Personal técnico que aporta", "[Diligenciar: nombre, formación y años de experiencia en monitoreo]", "Hojas de vida"),
        ("Experiencia en monitoreo de calidad del aire (últimos cinco años)", "[Diligenciar: cliente, objeto, lugar, año y valor de cada servicio]", "Certificaciones de clientes o contratos"),
        ("Acreditación o autorizaciones (si las tiene)", "[Diligenciar: acreditación ante el IDEAM u ONAC, si aplica]", "Resolución o certificado"),
        ("Aporte en efectivo (VI-05)", "150.000.000 COP", "Certificación de contrapartida firmada y soporte de disponibilidad"),
        ("Responsable institucional ante el proyecto", "[Diligenciar: nombre, cargo, correo y teléfono]", "Certificado de participación 10.18"),
        ("Inhabilidades, liquidación o reestructuración", "Declara no estar incursa [Diligenciar: confirmación]", "Declaración del representante legal")])
    guardar(d, os.path.join(OUT, "02_FIRMAR", "E_Gestion_y_Medio_Ambiente", "Ficha_identidad_y_capacidades_GMA.docx"))

if __name__ == "__main__":
    informe4(); protocolo(); carta_siot(); ficha_gma()
