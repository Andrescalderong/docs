import json, sys, os
C = "caps/"
E = [(C+"frente.md","raw")]
E += [(C+"soporte_a.md","raw"),(C+"soporte.md","cap")]
E += [(C+n,"cap") for n in ["a2a.md","a2b.md","a2c.md"]]
E += [(C+"cap19a.md","cap"),(C+"cap19_refs.md","raw"),(C+"cap19b.md","cap"),(C+"a2d.md","cap")]
E += [(C+f"paso{i}.md","cap") for i in range(8)]
E += [(C+n,"cap") for n in ["cap01.md","cap02a.md","cap02b.md","cap03.md","cap04.md","cap05.md","cap06.md","cap07.md","cap08.md","cap09.md","cap10.md","cap11.md","cap12.md","cap13.md","cap14.md","cap15.md","cap16.md","cap17.md","cap18.md","cap19_stub.md"]]
E += [(C+n,"cap") for n in ["cap20.md","anexos_km.md","anexo_n.md","cap21.md","x01.md","x02.md","x03.md","estrategia.md","x05.md","x06.md","x07.md","x08.md","x09.md","x10.md","cierre.md"]]
opts = {"title": "Proyecto completo SGR_CONV56_AIRE",
        "subtitle": "Red IoT híbrida Edge-Cloud y gemelo digital para la gestión anticipada del riesgo por material particulado posterremoto",
        "portada": [["p","Convocatoria de Emergencia, Decreto 1414 de 2026 (SGR_CONV56)",{"size":13,"before":36,"after":6}],
                    ["p","Sistema General de Regalías · Ministerio de Ciencia, Tecnología e Innovación",{"size":12,"after":6}],
                    ["p","Caso SGR_CONV56_AIRE · Formulado con GENESIS-CTeI 36.10 RC2",{"size":12,"after":24}],
                    ["p","Proponente: [DATO_USUARIO: universidad con grupo de investigación reconocido por MinCiencias]",{"size":12,"after":6}],
                    ["p","Alianza: municipio de Cundinamarca, Risaralda, Caldas o Valle del Cauca; actor reconocido por MinCiencias; empresa aliada",{"size":12,"after":6}],
                    ["p","Estado: borrador con vacíos · Fecha de corte: 13 de octubre de 2026",{"size":12,"bold":True,"after":6}],
                    ["break","",{}]]}
json.dump({"entradas": E, "opts": opts}, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(E))
