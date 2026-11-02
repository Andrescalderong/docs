import re,collections
CATS = [
 ("Términos de referencia y requisitos de la convocatoria", r"términos de referencia|\btdr\b|convocatoria|rubros admisibles|requisitos? de|porcentaje exigido|nivel mínimo|extensión y formato|clasificación de revistas|periodicidad|calendario y número|tasa social|enfoque diferencial|código de radicación|código de tipología|reasignación|elegibilidad|reglas de titularidad|código id"),
 ("Articulación con planes y políticas (PDD, PIIOM, ODS, PND, MGA)", r"\bpdd\b|piiom|\bods\b|plan nacional|planes (?:de desarrollo|vigentes)|demanda|\bmga\b|sigp|misión|vocación|transformación|objetivo y|línea de acción|\beje\b|artículos? (?:aplicables|y códigos|o eje)|indicadores? (?:y meta|del plan|, línea base)|indicador y meta|foco y recomendación|líneas de política|acciones del documento|tipología mmg|^código$|^indicador"),
 ("Documentos y compromisos jurídicos", r"carta|\bacta\b|acto o|acuerdo|convenio|reglamento|comité de ética|\baval\b|certificad|tratamiento de datos|gestor autorizado|ordenanza|instrumento"),
 ("Datos económicos y de financiación", r"cotizacion|costos? de|monto|financiación|plazo de adquisición|^proporción$|porcentaje máximo"),
 ("Datos técnicos, bibliométricos y de medición", r"gateway|distancia máxima|monitor|aqhi|viento|validación de laboratorio|inventario de equipos|evidencia|pilotos|resultados por base|scopus|cuartiles?|especificación|capacidad de procesamiento|calendario de informes"),
 ("Territorio, población y sitios de remoción", r"municipio|polígono|operarios|habitantes|población|organizaciones comunitarias|caracterización|\bsitios?\b|toneladas|rango|censo|dane|volumen removido|asistentes|horas por comité|comités (?:del tramo|para la prueba)|fecha del evento|número en"),
 ("Nombres de entidades, aliados y razón social", r"razón social|\bnit\b|nombre de la (?:ies|empresa|entidad)|nombres? de (?:los )?aliados|nombres de las (?:entidades|alcaldías)|nombres de los (?:comités|interesados)|entidades|proveedores|laboratorios|evaluador|nombre y organización|nombre de la persona o|logotipo|titular de la marca|dependencia y contacto|nombre del equipo formulador|custodio|nombres y roles de la entidad|panel|número y organizaciones|nombre del comité"),
 ("Personas, perfiles y grupos de investigación", r"hojas? de vida|\bnombres?\b|nombres? del|nombres por rol|nombre del investigador|nombre de la persona|nombre y cargo|nombre y hoja|grupo|grupl|categoría|líneas de investigación|programas? de|modalidad de joven|jornada laboral|credenciales|proyecto similar|proyectos propios|certificaciones de proyectos|personas designadas|composición del comité"),
 ("Fechas, firmas, contacto y presentación", r"fecha|firma|autorización|contacto|\bqr\b|fotograf|colores|responsable|decisión|reglas"),
]
def categorizar(desc):
    out=collections.defaultdict(list)
    for d in desc:
        for n,p in CATS:
            if re.search(p,d): out[n].append(d); break
        else: out["Otros"].append(d)
    return out
if __name__=='__main__':
    import json
    D=json.load(open('datos.json',encoding='utf-8'))
    c=categorizar(D['marcadores']['desc'].keys())
    for k,v in c.items():
        print('###',len(v),k)
        for x in sorted(v): print('   ',x[:90])
