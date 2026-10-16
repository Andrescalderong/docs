import json, sys
C = "caps/"
E = [(C+"frente_a2.md","raw"),(C+"soporte_a.md","raw"),(C+"soporte.md","cap")]
E += [(C+n,"cap") for n in ["a2a.md","a2b.md","a2c.md","cap19a.md"]]
E += [(C+"cap19_refs.md","raw"),(C+"cap19b.md","cap"),(C+"a2d.md","cap"),(C+"parte_c.md","raw")]
E += [(C+f"paso{i}.md","cap") for i in range(8)]
E += [(C+n,"cap") for n in ["cap01.md","cap02a.md","cap02b.md","cap03.md","cap04.md","cap05.md","cap06.md","cap07.md","cap08.md","cap09.md","cap10.md","cap11.md","cap12.md","cap13.md","cap14.md","cap15.md","cap16.md","cap17.md","cap18.md","cap19_stub.md"]]
E += [(C+n,"cap") for n in ["cap20.md","anexos_km.md","anexo_n.md","cap21.md","x01.md","x02.md","x03.md","estrategia.md","x05.md","x06.md","x07.md","x08.md","x09.md","x10.md","cierre.md"]]
NOTAS = [[None, "Este archivo reúne la parte de soporte de la solicitud, el documento técnico de las 30 secciones del Anexo 2 y el expediente ampliado de formulación."],
         [None, "Cada tabla y figura lleva un rótulo con el prefijo de su parte. Los índices de contenido, de tablas y de figuras se actualizan con el comando Actualizar campos de Word."],
         ["00B050", "El texto entre corchetes, como [DATO_USUARIO], corresponde a información que solo la Universidad, el municipio, el actor reconocido o la empresa aliada pueden aportar."],
         ["FF0000", "Para radicar se usa solo la parte B (secciones 1 a 30); la convocatoria limita cada PDF a 3 MB."]]
opts = {"formato": "a2", "titulo": "Red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto",
        "subtitulo": "Proyecto completo SGR_CONV56_AIRE",
        "portada": [["p","Proponente: [DATO_USUARIO: universidad con grupo de investigación reconocido por MinCiencias]",{"size":11}],
                    ["p","Alianza: municipio de Cundinamarca, Risaralda, Caldas o Valle del Cauca; actor reconocido por MinCiencias; empresa aliada",{"size":11}],
                    ["p","Estado: borrador con vacíos · Fecha de corte: 16 de octubre de 2026 · Cierre de la convocatoria: 3 de noviembre de 2026, 4:00 p. m.",{"size":11,"bold":True}]],
        "notas": NOTAS}
json.dump({"entradas": E, "opts": opts}, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(E))
