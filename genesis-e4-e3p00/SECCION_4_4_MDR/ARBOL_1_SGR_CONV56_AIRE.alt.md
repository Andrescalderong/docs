# A-DEC: estrategia de resolución y custodia posproyecto de la red de vigilancia de material particulado — alternativa textual

Árbol 1 · Decisión bajo incertidumbre · rol A-DEC
Pregunta: ¿Qué estrategia adopta el proyecto: no intervenir, transferir a un receptor público único o desplegar por tramos con custodia distribuida?
Naturaleza: PROPUESTO

Valor esperado en la raíz: NO_CALCULABLE 

| Nodo | Tipo | Etiqueta | Supuesto | VE o valor | Umbral |
|---|---|---|---|---|---|
| D1 | DECISION | Estrategia de resolución y custodia |  | NO_CALCULABLE | — |
| A1 | AZAR | Medición: la corrección local reduce el error frente a la lectura sin corrección dinámica | SC-1 | NO_CALCULABLE | — |
| B1 | AZAR | Medición: la corrección local reduce el error frente a la lectura sin corrección dinámica | SC-1 | NO_CALCULABLE | — |
| C0 | TERMINAL | Se mantiene la línea base: sensores aislados sin corrección dinámica ni custodia |  | NO_CALCULABLE | — |
| A2 | AZAR | Energía y enlace: nodos activos suficientes bajo maquinaria y humedad | SC-2 | NO_CALCULABLE | — |
| AT1 | TERMINAL | Expansión detenida tras el piloto; inversión limitada al primer tramo; conocimiento negativo documentado |  | NO_CALCULABLE | — |
| B2 | AZAR | Energía y enlace: nodos activos suficientes bajo maquinaria y humedad | SC-2 | NO_CALCULABLE | — |
| BT1 | TERMINAL | Inversión completa comprometida sin evidencia de reducción del error; red desplegada |  | NO_CALCULABLE | — |
| A3 | AZAR | Uso: autoridades adoptan umbrales de alerta validados en sus protocolos | SC-3 | NO_CALCULABLE | — |
| AT2 | TERMINAL | Error reducido y verificado, con cobertura insuficiente; rediseño del enlace o la energía antes del segundo tramo |  | NO_CALCULABLE | — |
| B3 | AZAR | Uso: autoridades adoptan umbrales de alerta validados en sus protocolos | SC-3 | NO_CALCULABLE | — |
| BT2 | TERMINAL | Red parcialmente inoperante con la inversión completa realizada |  | NO_CALCULABLE | — |
| A4 | AZAR | Custodia: al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo | SC-4 | NO_CALCULABLE | — |
| AT3 | TERMINAL | Mediciones verificadas sin uso institucional; tramo siguiente condicionado a la adopción de umbrales |  | NO_CALCULABLE | — |
| B4 | AZAR | Custodia: al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo | SC-4 | NO_CALCULABLE | — |
| BT3 | TERMINAL | Mediciones sin uso institucional con la inversión completa realizada |  | NO_CALCULABLE | — |
| AT5 | TERMINAL | Servicio de vigilancia sostenido con custodia distribuida; protección contribuida con otros actores |  | NO_CALCULABLE | — |
| AT4 | TERMINAL | Uso institucional sin custodio demostrado; cláusula de apertura y servicio mínimo |  | NO_CALCULABLE | — |
| BT5 | TERMINAL | Servicio continuado con receptor público único; protección contribuida con otros actores |  | NO_CALCULABLE | — |
| BT4 | TERMINAL | Orfandad después del mes 24: la red queda sin receptor que la opere |  | NO_CALCULABLE | — |

Supuestos críticos para la decisión (distancia al umbral ≤ 0,15, regla PROPUESTA): ninguno.

Errores de coherencia: ninguno detectado.
Comprobaciones del SVG: xml_bien_formado=True, viewbox=True, title=True, desc_no_vacio=True, rol_declarado=True, tipo_declarado=True, colores_fuera_de_paleta=[], sin_script_enlace_imagen=True, sin_transformaciones=True, ids_unicos=True, tamano_minimo_9_5=True