import json, sys
C = "caps/"
E = [(C+"frente_r.md","raw"),(C+"a2a_r.md","cap"),(C+"a2b_r.md","cap"),(C+"a2c_r.md","cap"),(C+"a29a_r.md","cap"),(C+"a29_refs_r.md","raw"),(C+"a29b_r.md","cap"),(C+"a2d_r.md","cap")]
opts = {"title": "Documento técnico de la propuesta (Anexo 2)",
        "subtitle": "Red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto",
        "portada": [["p","Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)",{"size":13,"before":36,"after":6}],
                    ["p","Anexo 2. Documento técnico de la propuesta · Sistema General de Regalías",{"size":12,"after":6}],
                    ["p","Proponente: [DATO_USUARIO: universidad con grupo de investigación reconocido por MinCiencias]",{"size":12,"after":6}],
                    ["p","Estado: borrador con vacíos · Fecha de corte: 16 de octubre de 2026",{"size":12,"bold":True,"after":6}],
                    ["break","",{}]]}
json.dump({"entradas": E, "opts": opts}, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(E))
