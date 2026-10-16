import json, sys
C = "caps/"
E = [(C+"frente_r.md","raw"),(C+"a2a_r.md","cap"),(C+"a2b_r.md","cap"),(C+"a2c_r.md","cap"),(C+"a29a_r.md","cap"),(C+"a29_refs_r.md","raw"),(C+"a29b_r.md","cap"),(C+"a2d_r.md","cap")]
NOTAS = [[None, "Los documentos técnicos de los proyectos presentados en esta convocatoria deben incluir como mínimo los elementos descritos en este Anexo, considerando las particularidades de la presente convocatoria."],
         ["00B050", "El texto entre corchetes, como [DATO_USUARIO], corresponde a información que debe diligenciar el proponente en el respectivo espacio."],
         [None, "La estructura de este documento guía atiende a la estructura de Marco Lógico implementado en la Metodología General Ajustada (MGA)."]]
opts = {"formato": "a2", "titulo": "Red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto",
        "subtitulo": "Documento técnico de la propuesta SGR_CONV56_AIRE",
        "portada": [["p","Proponente: [DATO_USUARIO: universidad con grupo de investigación reconocido por MinCiencias]",{"size":11}],
                    ["p","Estado: borrador con vacíos · Fecha de corte: 16 de octubre de 2026 · Cierre de la convocatoria: 3 de noviembre de 2026, 4:00 p. m.",{"size":11,"bold":True}]],
        "notas": NOTAS}
json.dump({"entradas": E, "opts": opts}, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(E))
