# A-TDC: teoría del cambio de la red de vigilancia con custodia distribuida — alternativa textual

Árbol 4 · Teoría del cambio · rol A-TDC
Pregunta: ¿Qué cadena causal lleva de los productos del proyecto a la protección de operarios y comunidades, y dónde termina la rendición de cuentas?
Naturaleza: PROPUESTO

| Nivel | Nodo | Texto |
|---|---|---|
| Productos | P1 | Red de nodos con corrección local desplegada y repuestos disponibles |
| Productos | P2 | Referencia gravimétrica, protocolo de calibración y sorteo semanal en operación |
| Productos | P3 | Gemelo digital y tablero con umbrales de alerta propuestos |
| Productos | P4 | Acuerdos de custodia por tramos y portafolio de financiación constituidos |
| Resultados inmediatos | R1 | Error de medición reducido y verificable frente a la referencia |
| Resultados inmediatos | R2 | Datos suficientes: nodos activos y latencia dentro de lo especificado |
| Resultados inmediatos | R3 | Fórmula local del índice y umbrales validados con la autoridad de salud |
| Resultados intermedios | I1 | Protocolos de gestión del riesgo y de salud incorporan las alertas |
| Resultados intermedios | I2 | Alertas oportunas con falsas alarmas dentro del umbral acordado |
| Resultados intermedios | I3 | Servicio operando con custodios después del mes 24 |
| Impacto | IM | Operarios y comunidades de los sitios de remoción protegidos por alertas basadas en mediciones verificadas |

Relaciones: P3 → R3 (SC-3); P1 → R2 (SC-2); P1 → R1 (SC-1); P2 → R1 (SC-1); P4 → I3 (SC-4); R3 → I1 (SC-3); R1 → I2; R2 → I2; I1 → IM (SC-3); I2 → IM; I3 → IM (SC-4); I1 → P4.

SC-1: SI los nodos con corrección local se comparan por sorteo semanal con la lectura sin corrección dinámica y con una referencia gravimétrica ENTONCES el error normalizado de los nodos corregidos resulta menor y la diferencia es detectable PORQUE la humedad y el sesgo por tamaño de partícula explican parte del error (V03→V06 = 3 en S2) y la corrección local los compensa antes de la transmisión (SUPUESTO).

SC-2: SI los nodos conservan energía y enlace intermitente bajo maquinaria, polvo y humedad ENTONCES el gemelo digital recibe datos suficientes para el mapa y el tablero PORQUE la transmisión por eventos reduce el consumo, los nodos averiados se reponen y la maquinaria destruye nodos con peso 2 (V05→V09) que el plan de repuestos absorbe (SUPUESTO).

SC-3: SI la autoridad de salud valida una fórmula local del índice y los umbrales, y los puestos de mando los incorporan en sus protocolos ENTONCES las alertas inducen acciones de protección y aumenta la población protegida PORQUE una alerta sin portador de decisión no modifica la conducta; en S2 V11→V14 y V13→V14 tienen peso 2 y son hipótesis de influencia (SUPUESTO).

SC-4: SI al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo de transferencia ENTONCES el servicio continúa después del mes 24 sin receptor público único PORQUE cada tramo exige presupuesto aprobado, personal designado y competencia jurídica documentada; sin ellos rige la cláusula de apertura (SUPUESTO).

Enfoque: TdC anidada: ejecutiva y por componente para dominio COMPLICADO en la medición y COMPLEJO en la adopción y la custodia.

Errores de coherencia: ninguno detectado.
Comprobaciones del SVG: xml_bien_formado=True, viewbox=True, title=True, desc_no_vacio=True, rol_declarado=True, tipo_declarado=True, colores_fuera_de_paleta=[], sin_script_enlace_imagen=True, sin_transformaciones=True, ids_unicos=True, tamano_minimo_9_5=True