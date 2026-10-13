%% PREFIJO: 20

## Anexo K. Fichas bidireccionales del análisis estructural

El Anexo K reproduce las 105 fichas bidireccionales de la sección F4.4.4 en el orden del plan paritario. Cada ficha registra los dos sentidos de influencia de un par de variables, con sus mecanismos, fundamentos, valores propuestos y estados. Los valores son juicios PROPUESTOS por la instancia analítica y ninguno equivale a una adjudicación independiente.

**Ficha 001 · V04__V08 · clase INTER**

- **V04→V08** · valor **1** (admisibles: 0, 1) · signo + · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Ráfagas fuertes desalinean antenas y mástiles temporales y elevan la pérdida de paquetes y el retraso de entrega.
  - Fundamento: Premisa de la iteración previa del documento (F4.4.4). La fuente que esa iteración cita, Ali et al. (2022), es una solicitud de patente sin datos de desempeño según F-INF. La cita no respalda el mecanismo.
  - Fuentes: F-INF, §1.3 hallazgo 3 y §2.3: las patentes del corpus, incluida Ali et al. (2022), no reportan datos de desempeño (alcance: Muestra que la cita de la iteración previa no respalda el mecanismo)
  - Premisas: P-V04-V08: las cargas de viento sobre mástiles y antenas degradan el enlace (supuesto de escenario).
  - Justificación del valor: Se asigna 1: el efecto es esporádico y afecta a los enlaces con antena direccional. Se descarta 2 por falta de evidencia.
  - Ancla comparada: Igual a ANC-1. Menor que ANC-2.
  - Explicación rival: Con antenas omnidireccionales y mástiles reforzados el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Cita previa invalidada. Mecanismo plausible sin fuente.
- **V08→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El retraso de datos no modifica el viento.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso de datos no modifica el viento.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 002 · V07__V09 · clase INTRA**

- **V07→V09** · valor **1** (admisibles: 0, 1, 2) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: La calibración consume energía y puede sacar el nodo de línea durante reinicios de software.
  - Fundamento: Ledger E3-P04, fila V07->V09 (PROPUESTO, magnitud 1, signo -).
  - Fuentes: F-E3, E3-P04 §12, fila V07->V09 (alcance: Valor heredado)
  - Justificación del valor: Se asigna 1: el costo es periódico y breve. Se descarta 2 porque el modelo ligero ejecuta pocos ciclos.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Con calibración sin reinicio el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Valor heredado y consistente con el diseño de bajo consumo.
- **V09→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La disponibilidad de nodos no fija la frecuencia de calibración por nodo.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V09 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la disponibilidad de nodos no fija la frecuencia de calibración por nodo.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Menos nodos disminuyen la carga total de calibración. La frecuencia por nodo no cambia.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 003 · V06__V14 · clase INTER**

- **V06→V14** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El error afecta la protección efectiva mediante el índice (V11) y las alertas (V12). No actúa de forma directa.
  - Fundamento: Premisa P-M: la influencia de V06 sobre V14 opera solo a través de V11, V12. Se puntúa en los pares V06→V11 y V11→V14, V06→V12 y V12→V14. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el error afecta la protección efectiva mediante el índice (V11) y las alertas (V12). No actúa de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V11, V12
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V14→V06** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica el error del sensor.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V06 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica el error del sensor.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 004 · V06__V08 · clase INTRA**

- **V06→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El error de medición no cambia el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error de medición no cambia el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Los disparos espurios por error aumentan el tráfico. El efecto es de segundo orden y se refleja en V06->V09.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V08→V06** · valor **0** (admisibles: 0, 1, 2) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El retraso de transmisión no cambia el error del sensor si el nodo estampa el tiempo en origen. Solo afecta la calibración cuando la marca de tiempo se asigna a la llegada del paquete.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V06 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso de transmisión no cambia el error del sensor si el nodo estampa el tiempo en origen. Solo afecta la calibración cuando la marca de tiempo se asigna a la llegada del paquete.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La iteración previa asigna 2 apoyándose en el desfase de 35 minutos de Bang et al.. Ese desfase es temporal entre sensor y estación, no latencia de red (hallazgo H-AH de la revisión).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Depende de si el sello de tiempo se asigna en origen. Diseño no fijado en el expediente.

**Ficha 005 · V05__V10 · clase INTER**

- **V05→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros no cambia la cantidad de nodos por km² diseñada. La pérdida física se puntúa en V05->V09.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros no cambia la cantidad de nodos por km² diseñada. La pérdida física se puntúa en V05->V09.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La densidad de nodos no cambia las toneladas de escombros removidas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V05 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad de nodos no cambia las toneladas de escombros removidas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 006 · V14__V15 · clase INTRA**

- **V14→V15** · valor **2** (admisibles: 1, 2) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: La protección demostrada de personas legitima el sistema ante las autoridades y sostiene su uso y su financiamiento.
  - Fundamento: Ledger E3-P04, fila V14->V15 (INFERIDO, magnitud 2). F-INF §2.3 y §1.3 señalan como falsa causa la atribución de efectividad de SIATA. El caso asocia ausencia de víctimas con inversión (Ruiz-Carrascal et al., 2026, pp. 3 y 5).
  - Fuentes: F-E3, E3-P04 §12, fila V14->V15 (alcance: Valor heredado); F-INF, §2.3 (falsa causa en Ruiz-Carrascal et al., 2026, pp. 3 y 5) (alcance: Cita secundaria sobre atribución de efectividad)
  - Justificación del valor: Se asigna 2. La cobertura reportada sirve como argumento de legitimidad. El cálculo de beneficios es incierto y el ciclo presupuestal modera el efecto.
  - Ancla comparada: Igual a ANC-2.
  - Explicación rival: Si las instituciones solo valoran resultados de salud medidos, el valor sería 1 durante los primeros 24 meses.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo plausible. La atribución de efectividad en el caso de referencia es frágil.
- **V15→V14** · valor **2** (admisibles: 1, 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: Las instituciones que usan el tablero ejecutan protocolos en el Puesto de Mando Unificado y difunden alertas a cuadrillas y comunidades. Sin ese uso el índice no llega a las personas.
  - Fundamento: E3-P17: las alcaldías son responsables de la emisión de alertas (matriz RACI); E3-P18, artefactos P17 y P22.
  - Fuentes: F-E3, E3-P17 §12 (fila Emisión de alertas M4: Alcaldías A); E3-P18, P17 y P22 (alcance: Responsabilidad propuesta, no firmada)
  - Justificación del valor: Se asigna 2: el uso institucional es condición para que la información llegue a las personas. El canal puede suplirse parcialmente con comunicación directa a las cuadrillas.
  - Ancla comparada: Igual a ANC-2.
  - Explicación rival: Si la protección depende solo de la comunicación directa a las cuadrillas, el valor sería 1.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Condición institucional descrita en el diseño. Sin protocolo vigente.

**Ficha 007 · V03__V11 · clase INTER**

- **V03→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La humedad no entra al cálculo del índice de peligro de PM. Su efecto aparece por el sesgo de medición (V06) o la concentración (V01, V02).
  - Fundamento: Premisa P-M: la influencia de V03 sobre V11 opera solo a través de V06, V01, V02. Se puntúa en los pares V03→V06 y V06→V11, V03→V01 y V01→V11, V03→V02 y V02→V11. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la humedad no entra al cálculo del índice de peligro de PM. Su efecto aparece por el sesgo de medición (V06) o la concentración (V01, V02).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un índice que corrigiera por humedad la incorporaría. El expediente no lo describe así.
  - Mediadores del modelo: V06, V01, V02
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V11→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El índice emitido en pantalla no modifica la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el índice emitido en pantalla no modifica la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 008 · V06__V07 · clase INTRA**

- **V06→V07** · valor **1** (admisibles: 0, 1, 2) · signo + · naturaleza PROPUESTO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: Un error por encima del umbral dispara el reentrenamiento o la recalibración del modelo de corrección.
  - Fundamento: Regla de disparo del Capítulo 10 (Tabla E3-10.4, R-TEC-01: NMAE mayor que 15 % durante 48 horas reentrena los pesos) y Hito 2 del Capítulo 9. La regla es una propuesta no ejecutada.
  - Fuentes: F-E3, Capítulo 10, Tabla E3-10.4, fila R-TEC-01; Capítulo 9, Tabla E3-9.1, Hito 2 (alcance: Regla de disparo propuesta); F-E3, Capítulo 8, Tabla E3-8.3, fila Monitores gravimétricos patrón (3 unidades) (alcance: Cantidad de referencias presupuestadas)
  - Justificación del valor: Se asigna 1: el disparo exige una referencia para medir el error, y el diseño dispone de solo 3 monitores gravimétricos (Tabla E3-8.3). La retroalimentación cubre pocos nodos.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Si la calibración se ejecuta por calendario fijo, el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Regla documentada como propuesta en el expediente. Cobertura de referencias limitada.
- **V07→V06** · valor **3** (admisibles: 2, 3) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: La calibración dinámica con referencia estima el sesgo higroscópico y la deriva, y los resta de la lectura. Reduce el error del sensor.
  - Fundamento: F-INF §3.1 documenta en una red urbana de Seúl una mejora de R2 de menos de 0,2 a 0,81 (Bang et al., 2026, pp. 6-8). La corrección usó una estación cercana y 35 minutos de desfase. F-INF §11.6 plantea la hipótesis H1 (más sofisticación, menos error) como hipótesis no probada.
  - Fuentes: F-INF, §3.1 y §1.3 hallazgo 3 (Bang et al., 2026, pp. 6-8): R2 de menos de 0,2 a 0,81 (alcance: Cita secundaria; método de corrección, no frecuencia); F-INF, §11.6, hipótesis H1 y H2 (alcance: Hipótesis del informe, sin resultado); F-E3, E3-P04 §12, fila V07->V06 (PROPUESTO, magnitud 3) (alcance: Valor heredado)
  - Justificación del valor: Se asigna 3 porque la corrección actúa directamente sobre el sesgo sin intermediario, con efecto grande en el caso documentado. El valor supone que existen referencias disponibles.
  - Ancla comparada: Igual a ANC-3 en nivel.
  - Explicación rival: La variable explicativa del informe es el método de corrección y la distancia a la referencia. La frecuencia puede tener rendimientos decrecientes y un efecto menor.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Efecto documentado en otra red con otro método. La frecuencia de ajuste no fue la variable estudiada.

**Ficha 009 · V04__V14 · clase INTER**

- **V04→V14** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El viento no cambia directamente el número de personas protegidas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V04 con V14 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el viento no cambia directamente el número de personas protegidas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V14→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica el viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica el viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 010 · V03__V05 · clase INTRA**

- **V03→V05** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Razón del cero: La humedad relativa no cambia el volumen de escombros removidos. La lluvia, que sí detiene obras, no figura como variable del modelo.
  - Fundamento: Premisa P-E: V05 es exógena al sistema de monitoreo dentro de H. Responde a procesos fuera de V01-V15.
  - Justificación del valor: Se asigna 0 porque la humedad relativa no cambia el volumen de escombros removidos. La lluvia, que sí detiene obras, no figura como variable del modelo.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La lluvia asociada a alta humedad detiene la remoción. Sin variable de precipitación, esa ruta queda fuera de la frontera (VACIO V-LLUVIA-01).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Exogeneidad por razonamiento. Sin fuente específica.
- **V05→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros removidos no modifica la humedad relativa del aire a escala de sitio.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros removidos no modifica la humedad relativa del aire a escala de sitio.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: El rociado de agua aumenta la humedad local de forma marginal. No se considera en H.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 011 · V03__V14 · clase INTER**

- **V03→V14** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La humedad no cambia el número de personas protegidas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V03 con V14 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la humedad no cambia el número de personas protegidas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V14→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 012 · V01__V03 · clase INTRA**

- **V01→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La masa de PM2,5 no modifica la humedad relativa del aire a escala de sitio dentro de H.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V01 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la masa de PM2,5 no modifica la humedad relativa del aire a escala de sitio dentro de H.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Los aerosoles higroscópicos actúan como núcleos de condensación, pero el efecto sobre la humedad ambiental de un sitio abierto es despreciable.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V03→V01** · valor **1** (admisibles: 0, 1) · signo MIXTO · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: La humedad modifica el tamaño de las partículas por crecimiento higroscópico y favorece la deposición húmeda. El efecto sobre la masa de PM2,5 tiene signo variable.
  - Fundamento: Procesos físicos generales de aerosoles. E3-P04 lo rotula DOCUMENTADO con signo (+) sin localizador. La revisión no encontró la fuente en F-INF.
  - Fuentes: F-E3, E3-P04 §12, fila V03->V01 (rotulada DOCUMENTADO sin localizador) (alcance: Valor heredado; el rótulo DOCUMENTADO no se acepta sin localizador)
  - Premisas: P-V03-V01: la humedad altera el reparto de masa entre tamaños y la deposición húmeda remueve partículas (conocimiento general de aerosoles).
  - Justificación del valor: Se asigna 1: la masa seca no cambia con la humedad, pero sí la distribución por tamaño y la remoción. Efecto débil y de signo mixto.
  - Ancla comparada: Igual a ANC-1 en nivel.
  - Explicación rival: Para sensores ópticos el efecto aparente sobre la lectura es mayor. Ese efecto se puntúa en V03->V06, no aquí.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo general. Sin fuente localizada. Signo mixto.

**Ficha 013 · V05__V11 · clase INTER**

- **V05→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros afecta el índice por la concentración que genera (V01, V02), no de forma directa.
  - Fundamento: Premisa P-M: la influencia de V05 sobre V11 opera solo a través de V01, V02. Se puntúa en los pares V05→V01 y V01→V11, V05→V02 y V02→V11. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros afecta el índice por la concentración que genera (V01, V02), no de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V01, V02
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V11→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El índice no cambia por sí solo las toneladas removidas. Una orden de pausa o rociado requiere decisión institucional.
  - Fundamento: Premisa P-M: la influencia de V11 sobre V05 opera solo a través de V15. Se puntúa en los pares V11→V15 y V15→V05. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el índice no cambia por sí solo las toneladas removidas. Una orden de pausa o rociado requiere decisión institucional.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La orden de cese basada en el índice se puntúa en V15->V05.
  - Mediadores del modelo: V15
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.

**Ficha 014 · V12__V13 · clase INTRA**

- **V12→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no cambian el tiempo de aviso.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no cambian el tiempo de aviso.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica la tasa de falsas alarmas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V12 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica la tasa de falsas alarmas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 015 · V09__V11 · clase INTER**

- **V09→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La pérdida de nodos afecta el índice mediante la densidad y la representatividad (V10).
  - Fundamento: Premisa P-M: la influencia de V09 sobre V11 opera solo a través de V10. Se puntúa en los pares V09→V10 y V10→V11. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la pérdida de nodos afecta el índice mediante la densidad y la representatividad (V10).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V10
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V11→V09** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El nivel del índice no cambia la disponibilidad de los nodos.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V09 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el nivel del índice no cambia la disponibilidad de los nodos.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 016 · V13__V15 · clase INTRA**

- **V13→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El tiempo de aviso afecta el uso institucional mediante la protección lograda (V14), no de forma directa.
  - Fundamento: Premisa P-M: la influencia de V13 sobre V15 opera solo a través de V14. Se puntúa en los pares V13→V14 y V14→V15. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso afecta el uso institucional mediante la protección lograda (V14), no de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V14
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V15→V13** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La adopción institucional no cambia el tiempo físico de aviso. Podría reducir el tiempo de decisión, efecto que no está modelado.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la adopción institucional no cambia el tiempo físico de aviso. Podría reducir el tiempo de decisión, efecto que no está modelado.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un protocolo en el Puesto de Mando Unificado acorta la decisión. El diseño lo trata como parte de V14.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 017 · V02__V09 · clase INTER**

- **V02→V09** · valor **1** (admisibles: 0, 1) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: El polvo grueso se deposita sobre paneles solares y entradas de aire, reduce la carga disponible y obliga a limpiezas que sacan nodos de servicio.
  - Fundamento: Premisa general de ensuciamiento fotovoltaico. Sin fuente en el expediente. F-INF no reporta datos de energía de nodos.
  - Fuentes: F-E3, Capítulo 10, Tabla E3-10.5, fila Mes 6: pivote por baterías o módulos fotovoltaicos (alcance: Indica que el diseño contempla energía solar; no cuantifica el efecto del polvo)
  - Premisas: P-V02-V09: el depósito de polvo reduce la generación fotovoltaica y bloquea ventilación (conocimiento técnico general).
  - Justificación del valor: Se asigna 1: el efecto es gradual y mitigable con limpieza, comparable con ANC-1 (V03->V09). Se descarta 2 porque no destruye el nodo.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Si los nodos usan solo batería primaria sin panel, el efecto es 0. El expediente cita módulos fotovoltaicos en el plan de pivote (Tabla E3-10.5).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa general. Tecnología de alimentación no definida.
- **V09→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La disponibilidad de nodos no modifica la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V09 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la disponibilidad de nodos no modifica la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 018 · V13__V14 · clase INTRA**

- **V13→V14** · valor **2** (admisibles: 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: Más tiempo de aviso permite que más operarios y residentes adopten medidas de protección antes del impacto.
  - Fundamento: Ledger E3-P04, fila V13->V14 (INFERIDO, magnitud 3). F-INF §1.3 hallazgo 2: ningún documento de alertas reporta anticipación, por lo que no hay curva empírica aviso-protección.
  - Fuentes: F-E3, E3-P04 §12, fila V13->V14 (alcance: Valor heredado; la revisión lo modifica); F-INF, §1.3 hallazgo 2 (alcance: Ausencia de evidencia sobre anticipación)
  - Justificación del valor: Se asigna 2 y no 3: el efecto crece hasta superar el tiempo de respuesta (colocar mascarilla, evacuar) y luego satura. Para operarios con mascarilla disponible el rendimiento marginal es bajo.
  - Ancla comparada: Igual a ANC-2.
  - Explicación rival: Para evacuación de comunidades el aviso es crítico y el valor sería 3.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo lógico con saturación. Sin curva empírica.
- **V14→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica el tiempo de aviso.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica el tiempo de aviso.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 019 · V03__V06 · clase INTER**

- **V03→V06** · valor **3** (admisibles: 2, 3) · signo + · naturaleza DOCUMENTADO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: El crecimiento higroscópico infla el tamaño aparente de las partículas y las gotas dispersan la luz del contador láser. El resultado es un sesgo positivo en la lectura óptica.
  - Fundamento: F-INF §1.3 hallazgo 3 y §3.1 registran una correlación de 0,73 entre partículas y humedad en una mina a cielo abierto (Suresh et al., 2025, p. 30). El valor documentado es una correlación, no el NMAE.
  - Fuentes: F-INF, §1.3 hallazgo 3 y §3.1 (Suresh et al., 2025, p. 30): correlación PM-humedad = 0,73 (alcance: Cita secundaria; alcance: sesgo por humedad en mina a cielo abierto); F-INF, §3.1 (Bang et al., 2026, pp. 6-8): R2 de <0,2 a 0,81 con corrección por estación cercana (alcance: Respalda que el sesgo corregible existe en una red urbana)
  - Premisas: P-V03-V06: la dispersión de luz por gotas y partículas hidratadas aumenta la señal óptica a igual masa seca (principio físico de los contadores ópticos).
  - Justificación del valor: Se asigna 3 porque la humedad determina de forma crítica el sesgo del sensor óptico en las condiciones de interés, sin intermediario. Es el vínculo mejor respaldado del modelo.
  - Ancla comparada: Igual a ANC-3 en nivel. Mayor que ANC-1 porque el efecto es medido y no solo gradual.
  - Explicación rival: La corrección con referencia cercana puede neutralizar el sesgo. Eso se puntúa en V07->V06. La correlación 0,73 podría reflejar covariación estacional de PM y humedad.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Fuente secundaria localizada. Correlación en mina, no NMAE en escombreras. El artículo original no fue leído.
- **V06→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El error del sensor óptico no modifica la humedad relativa del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error del sensor óptico no modifica la humedad relativa del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 020 · V11__V15 · clase INTRA**

- **V11→V15** · valor **1** (admisibles: 0, 1, 2) · signo + · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Un índice comprensible y útil incentiva el uso del tablero por parte de las alcaldías y la UNGRD.
  - Fundamento: Premisa de utilidad percibida; F-INF §8.4 D-05 recomienda validar un índice local con desenlaces, lo que indica que la utilidad aún no está demostrada.
  - Fuentes: F-INF, §8.4 D-05 (alcance: Recomienda validar el índice local)
  - Premisas: P-V11-V15: la utilidad percibida del indicador principal sostiene el uso institucional (supuesto de escenario).
  - Justificación del valor: Se asigna 1: el uso depende más del mandato formal y de la confiabilidad que del nivel del índice.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Si el índice se considera la razón principal del tablero, el valor sería 2.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa sin medición.
- **V15→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La adopción institucional no cambia el valor del índice emitido.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V11 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la adopción institucional no cambia el valor del índice emitido.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Las instituciones podrían modificar la fórmula. Sería una decisión explícita fuera de esta relación.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 021 · V07__V13 · clase INTER**

- **V07→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración no cambia el tiempo de aviso.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V07 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la calibración no cambia el tiempo de aviso.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica la frecuencia de calibración.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica la frecuencia de calibración.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 022 · V01__V02 · clase INTRA**

- **V01→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: PM2,5 está contenida en PM10 por definición de tamaño (partículas <2,5 µm dentro de las <10 µm). La inclusión no es influencia causal.
  - Fundamento: Premisa P-D: la relación entre V01 y V02 es definicional (inclusión matemática). Una inclusión no justifica una flecha causal.
  - Justificación del valor: Se asigna 0 porque pM2,5 está contenida en PM10 por definición de tamaño (partículas <2,5 µm dentro de las <10 µm). La inclusión no es influencia causal.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una lectura causal supondría que más PM2,5 genera PM10. La masa fina ya está sumada en PM10 y no crea masa gruesa.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Relación definicional verificable en el diccionario.
- **V02→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: PM10 incluye la masa de PM2,5 por definición de tamaño; PM10 no genera PM2,5 y la inclusión no es una flecha causal.
  - Fundamento: Premisa P-D: la relación entre V02 y V01 es definicional (inclusión matemática). Una inclusión no justifica una flecha causal.
  - Justificación del valor: Se asigna 0 porque pM10 incluye la masa de PM2,5 por definición de tamaño; PM10 no genera PM2,5 y la inclusión no es una flecha causal.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La fragmentación de partículas gruesas produce algo de masa fina. Su magnitud es despreciable dentro de H y se contabiliza en V05->V01.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Relación definicional verificable en el diccionario.

**Ficha 023 · V01__V14 · clase INTER**

- **V01→V14** · valor **1** (admisibles: 0, 1) · signo + · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: La bruma visible por PM2,5 alerta a operarios y vecinos sin intervención del sistema y los lleva a protegerse.
  - Fundamento: Premisa visual de la iteración previa del documento (Paso 4, F4.4.4), de naturaleza INFERIDA. Sin fuente en el corpus. Aquí se rotula SUPUESTO.
  - Premisas: P-V01-V14: la reducción de visibilidad por partículas finas induce conductas de protección sin mediación del sistema de alerta (supuesto de escenario).
  - Justificación del valor: Se asigna 1 y no 0 porque la señal sensorial puede inducir protección autónoma. Se descarta 2 porque la bruma fina es menos perceptible que la nube de polvo grueso y no activa un protocolo.
  - Ancla comparada: Igual en nivel a ANC-1. Menor que ANC-2 por ausencia de mecanismo institucional.
  - Explicación rival: V14 cuenta personas protegidas por alerta. La protección autónoma podría quedar fuera de su definición, y entonces el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa visual sin fuente. Ambigüedad en la definición de V14.
- **V14→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 024 · V11__V14 · clase INTRA**

- **V11→V14** · valor **2** (admisibles: 1, 2, 3) · signo + · naturaleza PROPUESTO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: Un nivel alto activa el protocolo de alerta. La protección efectiva exige que el protocolo exista y se ejecute.
  - Fundamento: Ledger E3-P04 asigna 3 (PROPUESTO). F-INF §1.3 hallazgo 9 cita a Rendón-Marín et al. (2024, p. 8). En estudiantes de Medellín, el conocimiento no se asocia de forma directa con la práctica.
  - Fuentes: F-E3, E3-P04 §12, fila V11->V14; E3-P18 tabla de artefactos, P17 Protocolo de Alertas (alcance: Valor heredado y protocolo propuesto); F-INF, §1.3 hallazgo 9 (Rendón-Marín et al., 2024, p. 8) (alcance: Cita secundaria; población de estudiantes de medicina)
  - Justificación del valor: Se asigna 2 y no 3: la información es necesaria pero no suficiente para producir conducta protectora. El efecto depende además del protocolo y del mensaje.
  - Ancla comparada: Mayor que ANC-1. Igual a ANC-2.
  - Explicación rival: Si el protocolo obligatorio (E3-P18, artefacto P17) activa medidas automáticas, el valor sería 3.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo plausible. Evidencia indirecta de brecha conocimiento-conducta.
- **V14→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica el valor del índice.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V11 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica el valor del índice.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 025 · V07__V11 · clase INTER**

- **V07→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración afecta el índice mediante el error (V06), no de forma directa.
  - Fundamento: Premisa P-M: la influencia de V07 sobre V11 opera solo a través de V06. Se puntúa en los pares V07→V06 y V06→V11. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la calibración afecta el índice mediante el error (V06), no de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V06
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V11→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El nivel del índice no fija la frecuencia de calibración.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el nivel del índice no fija la frecuencia de calibración.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un índice alto sostenido podría motivar auditoría de sensores. Esa ruta pasa por V12 y V06.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 026 · V02__V05 · clase INTRA**

- **V02→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La concentración de PM10 no cambia por sí sola las toneladas removidas. La suspensión de obras exige una decisión institucional.
  - Fundamento: Premisa P-M: la influencia de V02 sobre V05 opera solo a través de V11, V15. Se puntúa en los pares V02→V11 y V11→V05, V02→V15 y V15→V05. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la concentración de PM10 no cambia por sí sola las toneladas removidas. La suspensión de obras exige una decisión institucional.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una nube densa puede detener la maquinaria por seguridad visual. Esa decisión se puntúa en V15->V05.
  - Mediadores del modelo: V11, V15
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V05→V02** · valor **3** (admisibles: 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Mecanismo: La demolición, carga y transporte de escombros resuspenden y generan polvo grueso en proporción directa al volumen movido.
  - Fundamento: E3-P04 asigna 3 (INFERIDO). El cociente PM2,5/PM10 de 0,88 de la mina (F-INF) indica un régimen distinto. Para escombros se espera fracción gruesa mayoritaria.
  - Fuentes: F-E3, E3-P04 §12, fila V05->V02 (INFERIDO, magnitud 3); Paso 4, F4.4.2, ancla del valor 3 (alcance: Define el ancla)
  - Premisas: P-V05-V02: la emisión de polvo por manejo de material granular crece con la masa movida (inventarios de emisión, conocimiento general).
  - Justificación del valor: Se asigna 3 porque el movimiento de material produce polvo grueso de forma casi mecánica, sin intermediario: es el ancla ANC-3.
  - Ancla comparada: Es ANC-3.
  - Explicación rival: El rociado de agua y los cerramientos pueden reducir la emisión. Eso sería una intervención sobre V05, no un cambio de esta relación.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo físico directo. Magnitud exacta dependiente de la tarea.

**Ficha 027 · V04__V06 · clase INTER**

- **V04→V06** · valor **1** (admisibles: 0, 1) · signo MIXTO · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: El viento modifica el flujo de aire en la entrada del sensor. Cambia la eficiencia de captura de partículas y sesga la lectura.
  - Fundamento: Efecto conocido de la meteorología sobre sensores de bajo costo. El expediente lo incluye como control (F-INF §11.4 lista el viento como control del error).
  - Fuentes: F-INF, §11.4 Modelo conceptual causal: el viento figura entre los controles del NMAE (alcance: Respalda la inclusión como control; no cuantifica el efecto)
  - Premisas: P-V04-V06: la velocidad del aire en la entrada del sensor altera la eficiencia de muestreo (conocimiento técnico general).
  - Justificación del valor: Se asigna 1: el efecto es secundario frente a la humedad y su sentido depende del diseño del inlet.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Con inlet protegido el valor tiende a 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Control declarado en el diseño del informe. Magnitud desconocida.
- **V06→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El error del sensor no modifica el viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error del sensor no modifica el viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 028 · V07__V10 · clase INTRA**

- **V07→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración no cambia la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V07 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la calibración no cambia la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La densidad de nodos no fija la frecuencia de calibración por nodo.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad de nodos no fija la frecuencia de calibración por nodo.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Más nodos aumentan la carga de calibración. La frecuencia por nodo no cambia.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 029 · V03__V07 · clase INTER**

- **V03→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La humedad relativa no fija la frecuencia de calibración. La calibración depende de la regla operativa y de la deriva detectada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V03 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la humedad relativa no fija la frecuencia de calibración. La calibración depende de la regla operativa y de la deriva detectada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una regla de recalibración por umbral de humedad la haría depender de V03. El diseño del expediente no la establece.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V07→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración no modifica la humedad relativa del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V07 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la calibración no modifica la humedad relativa del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 030 · V02__V03 · clase INTRA**

- **V02→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La masa de PM10 no modifica la humedad relativa del aire a escala de sitio.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V02 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la masa de PM10 no modifica la humedad relativa del aire a escala de sitio.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V03→V02** · valor **1** (admisibles: 0, 1) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: La humedad del aire y del material reduce la resuspensión de polvo y favorece su sedimentación.
  - Fundamento: Principio de supresión de polvo por humedad del material (práctica de rociado en obras). E3-P04 asigna signo (+) por condensación. La revisión invierte el signo.
  - Premisas: P-V03-V02: la humedad superficial del material y del aire reduce la emisión por resuspensión (práctica de control de polvo).
  - Justificación del valor: Se asigna 1: la humedad ambiental se asocia a humedad superficial solo de forma parcial. Efecto débil.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: El rociado de agua sobre escombros es una intervención (V05 modificado), no la humedad relativa del aire.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo conocido en práctica de obra. Correlato entre humedad del aire y del material es parcial.

**Ficha 031 · V08__V11 · clase INTER**

- **V08→V11** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La latencia retrasa la actualización del índice pero no cambia su valor para un instante dado. La oportunidad se mide en V13.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V11 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la latencia retrasa la actualización del índice pero no cambia su valor para un instante dado. La oportunidad se mide en V13.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un índice basado en datos rezagados describe un instante anterior. Esa pérdida de vigencia se capta en V13.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V11→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El nivel del índice no cambia el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el nivel del índice no cambia el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 032 · V03__V04 · clase INTRA**

- **V03→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La humedad relativa no altera la velocidad del viento superficial a escala de sitio.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V03 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la humedad relativa no altera la velocidad del viento superficial a escala de sitio.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La convección húmeda modifica el viento regional. No es relevante dentro de H a escala de sitio.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V04→V03** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La velocidad del viento no modifica la humedad relativa a escala de sitio en H. La dirección del viento sí la modifica por advección de masas de aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V04 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la velocidad del viento no modifica la humedad relativa a escala de sitio en H. La dirección del viento sí la modifica por advección de masas de aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La advección de aire húmedo cambia la humedad. Depende de la dirección y de las masas de aire, no de la velocidad.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 033 · V03__V09 · clase INTER**

- **V03→V09** · valor **1** (admisibles: 0, 1, 2) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: La humedad sostenida condensa y corroe carcasas y conectores, y reduce la vida útil de la electrónica de bajo costo.
  - Fundamento: Mismo vínculo que el ancla ANC-1 definida en el Paso 4 del documento (F4.4.2). F-INF cita 96 de 570 estaciones inactivas en Brasil (Tavella et al., 2026, p. 6) sin atribuir causa.
  - Fuentes: F-E3, Paso 4, F4.4.2, ancla del valor 1; Capítulo 8, Tabla E3-8.4 (kits NEMA 4X) (alcance: Define el ancla y la mitigación presupuestada); F-INF, §3.1 (Tavella et al., 2026, p. 6): 96 de 570 estaciones inactivas o sin estado (16,8 %) (alcance: No atribuye la inactividad a la humedad)
  - Justificación del valor: Se asigna 1: el efecto es gradual y las carcasas NEMA 4X (Tabla E3-8.4) lo mitigan. Es el ancla del valor 1.
  - Ancla comparada: Es ANC-1.
  - Explicación rival: Con carcasas bien selladas el valor tiende a 0. Con sellos defectuosos puede subir a 2.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo conocido. Mitigación presupuestada. Sin dato de falla por humedad.
- **V09→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La disponibilidad de nodos no modifica la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V09 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la disponibilidad de nodos no modifica la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 034 · V09__V10 · clase INTRA**

- **V09→V10** · valor **3** (admisibles: 0, 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: Si V10 mide la resolución efectiva del mapa, la cantidad de nodos activos determina aritméticamente los nodos por km² con datos.
  - Fundamento: Ledger E3-P04, fila V09->V10 (PROPUESTO, magnitud 3). El diccionario define V10 como resolución del mapa predictivo (nodos/km²) sin precisar si es nominal o efectiva (VACIO V-DIC-02).
  - Fuentes: F-E3, E3-P04 §12, fila V09->V10; Paso 4, F4.4.2, ancla del valor 2 (alcance: Muestra la incoherencia del documento previo)
  - Justificación del valor: Se asigna 3 bajo la lectura efectiva: la relación es definicional y sin intermediario (ancla ANC-3). El documento previo usa el mismo vínculo como ancla del valor 2, lo que es incoherente con su propio ledger.
  - Ancla comparada: Es ANC-3 bajo la lectura efectiva.
  - Explicación rival: Si V10 es la densidad nominal de diseño, el valor es 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Depende de una ambigüedad del diccionario (V-DIC-02).
- **V10→V09** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La densidad de diseño no cambia el porcentaje de nodos activos.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V09 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad de diseño no cambia el porcentaje de nodos activos.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 035 · V02__V14 · clase INTER**

- **V02→V14** · valor **1** (admisibles: 0, 1) · signo + · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: La nube de polvo grueso visible alerta a las cuadrillas, que se resguardan o usan mascarilla sin esperar el sistema.
  - Fundamento: Premisa visual de la iteración previa del documento (Paso 4, F4.4.4), INFERIDA. Sin fuente en el corpus. Aquí se rotula SUPUESTO.
  - Premisas: P-V02-V14: la nube de polvo visible induce conductas de protección sin mediación del sistema de alerta (supuesto de escenario).
  - Justificación del valor: Se asigna 1: la nube visible es más perceptible que la bruma fina, pero no equivale a una alerta protocolizada. Se descarta 2 por esa razón.
  - Ancla comparada: Igual en nivel a ANC-1. Menor que ANC-2.
  - Explicación rival: Si V14 solo cuenta personas protegidas por alerta del sistema, el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa visual sin fuente. Definición de V14 ambigua.
- **V14→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 036 · V06__V10 · clase INTRA**

- **V06→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El error de medición no cambia la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error de medición no cambia la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V06** · valor **1** (admisibles: 0, 1, 2) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Una red densa permite validación cruzada entre vecinos y corrección de valores atípicos. Reduce el error del producto de red más que el del sensor individual.
  - Fundamento: Ledger E3-P04, fila V10->V06 (PROPUESTO, magnitud 2, signo -). El diccionario define V06 como desfase metrológico del sensor láser, es decir, del sensor individual.
  - Fuentes: F-E3, E3-P04 §12, fila V10->V06; Paso 4, F4.4.2, definición de V06 (alcance: Valor heredado y definición)
  - Justificación del valor: Se asigna 1. Bajo la definición de V06 como error de cada sensor, la densidad no lo cambia. Actúa solo mediante correcciones de red. Se baja el valor heredado de 2.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Si V06 se redefine como error del producto de red, el valor sería 2.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Depende de la definición de V06 (VACIO V-DIC-03).

**Ficha 037 · V09__V13 · clase INTER**

- **V09→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La pérdida de nodos afecta el aviso mediante la capacidad de detección temprana (V10).
  - Fundamento: Premisa P-M: la influencia de V09 sobre V13 opera solo a través de V10. Se puntúa en los pares V09→V10 y V10→V13. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la pérdida de nodos afecta el aviso mediante la capacidad de detección temprana (V10).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V10
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V13→V09** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica la disponibilidad de nodos.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V09 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica la disponibilidad de nodos.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 038 · V01__V05 · clase INTRA**

- **V01→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La concentración de PM2,5 no cambia por sí sola las toneladas removidas por día. Una suspensión de obras depende de una decisión institucional.
  - Fundamento: Premisa P-M: la influencia de V01 sobre V05 opera solo a través de V11, V15. Se puntúa en los pares V01→V11 y V11→V05, V01→V15 y V15→V05. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la concentración de PM2,5 no cambia por sí sola las toneladas removidas por día. Una suspensión de obras depende de una decisión institucional.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una orden de cese basada en el índice reduciría V05. Esa ruta se puntúa en V15->V05.
  - Mediadores del modelo: V11, V15
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V05→V01** · valor **2** (admisibles: 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: La demolición, trituración y carga de escombros emiten partículas finas, y la maquinaria diésel suma PM2,5 de combustión.
  - Fundamento: E3-P04 asigna 3 (INFERIDO). La revisión baja a 2: la masa de la emisión por demolición es principalmente gruesa y la fracción fina es menor; F-INF cita decisión sobre flota diésel (D-08 del informe) sin cuantificar.
  - Fuentes: F-E3, E3-P04 §12, fila V05->V01 (INFERIDO, magnitud 3) (alcance: Valor heredado; la revisión lo modifica); F-INF, §1.4 y §8.4 (flota diésel con emisiones como decisión del informe) (alcance: Respalda la relevancia de las emisiones de la maquinaria; no cuantifica)
  - Premisas: P-V05-V01: la demolición y la combustión diésel generan PM2,5 en proporción al trabajo mecánico (inventarios de emisión, conocimiento general).
  - Justificación del valor: Se asigna 2 y no 3: la emisión es directa, pero la fracción fina es menor que la gruesa (V05->V02).
  - Ancla comparada: Menor que ANC-3 (V05->V02). Mayor que ANC-1.
  - Explicación rival: Con maquinaria eléctrica o con rociado de agua el valor sería menor. Con trituración de concreto sin control podría ser 3.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo físico sólido. Cociente fino/grueso del escombro local desconocido (VACIO).

**Ficha 039 · V03__V15 · clase INTER**

- **V03→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La humedad no determina el uso institucional del tablero.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V03 con V15 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la humedad no determina el uso institucional del tablero.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V15→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El uso institucional del tablero no modifica la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el uso institucional del tablero no modifica la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Las órdenes de rociado afectan las emisiones por V05, no la humedad ambiental.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 040 · V08__V10 · clase INTRA**

- **V08→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El retraso no cambia la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso no cambia la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V08** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: Con 100 nodos, la densidad no satura los enlaces ni cambia el retraso de forma apreciable.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque con 100 nodos, la densidad no satura los enlaces ni cambia el retraso de forma apreciable.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Redes de más de mil nodos (S-Dot de Seúl, 1.138 sitios) podrían congestionar enlaces. No es el caso de 100 nodos.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 041 · V02__V10 · clase INTER**

- **V02→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración no cambia la cantidad de nodos por km² del gemelo.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V02 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración no cambia la cantidad de nodos por km² del gemelo.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La densidad de nodos no modifica la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad de nodos no modifica la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 042 · V01__V04 · clase INTRA**

- **V01→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración de partículas no altera la velocidad del viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V01 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración de partículas no altera la velocidad del viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: El forzamiento radiativo de los aerosoles modifica la circulación solo a escalas regionales y a plazos mayores que H.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V04→V01** · valor **2** (admisibles: 1, 2, 3) · signo - · naturaleza DOCUMENTADO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: El viento advecta y dispersa las partículas. Reduce la concentración local de PM2,5 y modula los episodios regionales.
  - Fundamento: F-INF §1.3 hallazgo 9: el episodio de 2022 del Valle de Aburrá se explicó por advección (Ayala-Parra et al., 2026, pp. 7-10). El hallazgo documenta transporte regional, no dispersión local de plumas de escombros.
  - Fuentes: F-INF, §1.3 hallazgo 9 (Ayala-Parra et al., 2026, pp. 7-10): advección explica el episodio de 2022 (alcance: Cita secundaria; transporte regional)
  - Premisas: P-V04-V01: la dilución por mezcla y arrastre reduce la concentración a sotavento (principio de dispersión atmosférica).
  - Justificación del valor: Se asigna 2 y no 3: la dispersión depende de la estabilidad atmosférica y de la distancia a la fuente, que el modelo no incluye. El efecto es moderado y variable.
  - Ancla comparada: Mayor que ANC-1. Menor que ANC-3 porque la relación no es mecánica.
  - Explicación rival: A baja velocidad el viento no dispersa y acumula. El signo depende del régimen.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Fuente secundaria sobre transporte. Falta evidencia local de dispersión de plumas de obra.

**Ficha 043 · V06__V12 · clase INTER**

- **V06→V12** · valor **2** (admisibles: 1, 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: En el protocolo por eventos, los picos falsos por sesgo o ruido disparan la alerta local antes de agregar el índice.
  - Fundamento: Ledger E3-P04 asigna 3 (INFERIDO). La revisión baja a 2 para no duplicar la ruta por V11. La alerta parte del índice (V11->V12) y, en el nodo, del umbral estadístico (ruta directa).
  - Fuentes: F-E3, E3-P04 §12, fila V06->V12 (INFERIDO, magnitud 3) (alcance: Valor heredado; la revisión lo modifica); F-INF, §1.3 hallazgo 2: ninguno de los cinco documentos de alertas reporta falsas alarmas (alcance: Muestra ausencia de evidencia empírica sobre falsas alarmas en el corpus)
  - Justificación del valor: Se asigna 2: solo la porción directa, el disparo por umbral en el nodo, se atribuye a V06->V12. La porción mediada por el índice se cuenta en V06->V11 y V11->V12.
  - Ancla comparada: Igual a ANC-2.
  - Explicación rival: Si todas las alertas parten del índice agregado, el valor directo sería 0 o 1.
  - Mediadores del modelo: V11
  - Motivo de la confianza: Depende de dónde se evalúa el umbral. Arquitectura de alertas no fijada.
- **V12→V06** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no modifican el error del sensor.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V06 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no modifican el error del sensor.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 044 · V12__V15 · clase INTRA**

- **V12→V15** · valor **2** (admisibles: 1, 2, 3) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: Las alertas inútiles generan fatiga de alarma y los municipios reducen o suspenden el uso del tablero.
  - Fundamento: Ledger E3-P04, fila V12->V15 (INFERIDO, magnitud 3, signo -). La revisión baja a 2 porque el uso institucional también depende de un mandato formal (E3-P18, artefacto P22) que amortigua el abandono.
  - Fuentes: F-E3, E3-P04 §12, fila V12->V15; E3-P18, artefacto P22 (resolución de adopción) (alcance: Valor heredado y mandato propuesto)
  - Justificación del valor: Se asigna 2 y no 3: el efecto es fuerte pero el mandato administrativo y la contrapartida contractual retienen el uso. No se declara el máximo sin haberlo examinado.
  - Ancla comparada: Igual a ANC-2. Menor que ANC-3.
  - Explicación rival: Si un municipio suspende el uso tras dos episodios, el valor sería 3.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo conocido en alertas. Sin evidencia local. Amortiguación por mandato supuesta.
- **V15→V12** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La adopción institucional no cambia por sí sola la tasa de falsas alarmas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V12 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la adopción institucional no cambia por sí sola la tasa de falsas alarmas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: El uso sostenido genera retroalimentación para ajustar umbrales. El diseño no lo establece.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 045 · V05__V12 · clase INTER**

- **V05→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros no determina las falsas alarmas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V12 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros no determina las falsas alarmas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V12→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: Las falsas alarmas no cambian por sí solas las toneladas removidas. Podrían inducir pausas innecesarias por decisión institucional (V15).
  - Fundamento: Premisa P-M: la influencia de V12 sobre V05 opera solo a través de V15. Se puntúa en los pares V12→V15 y V15→V05. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no cambian por sí solas las toneladas removidas. Podrían inducir pausas innecesarias por decisión institucional (V15).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La pausa innecesaria se puntúa en V15->V05.
  - Mediadores del modelo: V15
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.

**Ficha 046 · V02__V04 · clase INTRA**

- **V02→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración de polvo no altera la velocidad del viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V02 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración de polvo no altera la velocidad del viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible a escala de sitio.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V04→V02** · valor **2** (admisibles: 1, 2, 3) · signo MIXTO · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: El viento dispersa el polvo, pero también lo resuspende desde superficies expuestas y suma emisión. El signo neto depende de la velocidad.
  - Fundamento: E3-P04 asigna signo (-) por dispersión. La revisión añade la resuspensión eólica de polvo grueso.
  - Fuentes: F-E3, E3-P04 §12, fila V04->V02 (INFERIDO, magnitud 2, signo -) (alcance: Valor heredado)
  - Premisas: P-V04-V02: la velocidad del viento supera el umbral de arrastre del polvo seco y lo resuspende. A la vez lo diluye (aerodinámica de partículas).
  - Justificación del valor: Se asigna 2: el viento actúa directamente sobre la emisión y la dilución del polvo grueso. No se asigna 3 por el signo variable.
  - Ancla comparada: Mayor que ANC-1. Menor que ANC-3.
  - Explicación rival: Con superficies húmedas o cubiertas la resuspensión es nula y el signo es (-).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Dos mecanismos opuestos. Sin datos de campo.

**Ficha 047 · V06__V15 · clase INTER**

- **V06→V15** · valor **1** (admisibles: 0, 1) · signo - · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Técnicos y usuarios detectan discrepancias con instrumentos de referencia y restan credibilidad a los datos aunque no haya falsas alarmas.
  - Fundamento: Supuesto de escenario. La Tabla E3-5.3 del Paso 5 lista la confianza de la UNGRD en el AQHI como riesgo si persiste el sesgo.
  - Fuentes: F-E3, Paso 5, Tabla E3-5.3, fila Tasa de adopción institucional (V15) (alcance: Plantea el riesgo; no mide el efecto)
  - Premisas: P-V06-V15: la divergencia observable entre el sensor y la referencia reduce la confianza institucional en el dato (supuesto de escenario).
  - Justificación del valor: Se asigna 1: el efecto de credibilidad se expresa sobre todo por las falsas alarmas (V12->V15), que se puntúan aparte.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Si los usuarios solo observan alertas y no cotejan datos, el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Supuesto sin fuente. Comportamiento de usuarios no observado.
- **V15→V06** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La adopción institucional no cambia el error del sensor individual. Actúa mediante el financiamiento de calibración y mantenimiento (V07, V09).
  - Fundamento: Premisa P-M: la influencia de V15 sobre V06 opera solo a través de V07, V09. Se puntúa en los pares V15→V07 y V07→V06, V15→V09 y V09→V06. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la adopción institucional no cambia el error del sensor individual. Actúa mediante el financiamiento de calibración y mantenimiento (V07, V09).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V07, V09
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.

**Ficha 048 · V08__V09 · clase INTRA**

- **V08→V09** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El retraso no descarga la batería. La retransmisión por enlace pobre sí, pero es un efecto de segundo orden.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V09 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso no descarga la batería. La retransmisión por enlace pobre sí, pero es un efecto de segundo orden.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Enlaces con retransmisiones frecuentes consumirían más energía. No hay dato del enlace.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V09→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La caída de nodos no cambia el retraso de los nodos activos de forma directa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V09 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la caída de nodos no cambia el retraso de los nodos activos de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La congestión baja con menos nodos. El efecto es despreciable con 100 nodos.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 049 · V01__V09 · clase INTER**

- **V01→V09** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La masa de PM2,5 no daña ni descarga los nodos. El depósito relevante para la energía y los lentes corresponde a la fracción gruesa (V02->V09).
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V01 con V09 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la masa de PM2,5 no daña ni descarga los nodos. El depósito relevante para la energía y los lentes corresponde a la fracción gruesa (V02->V09).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: El depósito fino en lentes y ventiladores podría acortar la vida útil. Se considera cubierto por V02->V09.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V09→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La disponibilidad de nodos no modifica la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V09 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la disponibilidad de nodos no modifica la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 050 · V07__V08 · clase INTRA**

- **V07→V08** · valor **1** (admisibles: 0, 1) · signo + · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: El cómputo de calibración y la descarga de pesos usan CPU y ancho de banda y retrasan la emisión de otros paquetes.
  - Fundamento: Premisa de la iteración previa del documento (F4.4.4, V07->V08 = 1, mecanismo de software). Sin medición en el expediente.
  - Premisas: P-V07-V08: la actualización de pesos compite por CPU y canal con la telemetría (supuesto de diseño).
  - Justificación del valor: Se asigna 1: la carga adicional es pequeña para 100 nodos y para actualizaciones espaciadas.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Con actualizaciones fuera de ventanas de transmisión el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa de software sin medición.
- **V08→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El retraso de datos no fija la frecuencia de calibración.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso de datos no fija la frecuencia de calibración.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La descarga tardía de pesos puede retrasar un ajuste. El efecto es de segundo orden.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 051 · V01__V13 · clase INTER**

- **V01→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración no cambia el tiempo de aviso, que depende de la detección temprana, el enlace y el pronóstico.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V01 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración no cambia el tiempo de aviso, que depende de la detección temprana, el enlace y el pronóstico.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Concentraciones altas podrían acelerar la detección. La detección depende de la densidad (V10) y de la latencia (V08).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 052 · V12__V14 · clase INTRA**

- **V12→V14** · valor **1** (admisibles: 0, 1, 2) · signo - · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Tras falsas alarmas repetidas, cuadrillas y población atienden menos las alertas siguientes y la protección efectiva baja.
  - Fundamento: Efecto de alarma falsa repetida descrito en la literatura general de alertas; F-INF no lo documenta y reporta ausencia de datos de falsas alarmas en el corpus.
  - Fuentes: F-INF, §1.3 hallazgo 2 (alcance: Ausencia de datos de falsas alarmas en el corpus)
  - Premisas: P-V12-V14: la repetición de alertas falsas reduce el cumplimiento de alertas posteriores (efecto de alarma falsa repetida).
  - Justificación del valor: Se asigna 1: el efecto aparece tras varios episodios, no en los primeros meses, y se amortigua con protocolos obligatorios.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: En un entorno de mando estricto, con uso obligatorio de protección, el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo general sin evidencia local.
- **V14→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica la tasa de falsas alarmas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V12 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica la tasa de falsas alarmas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 053 · V04__V10 · clase INTER**

- **V04→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La velocidad del viento no cambia la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V04 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la velocidad del viento no cambia la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La densidad de nodos no modifica el viento.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad de nodos no modifica el viento.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 054 · V04__V05 · clase INTRA**

- **V04→V05** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Razón del cero: La velocidad del viento no cambia las toneladas de escombros removidas, salvo condiciones extremas sin umbral documentado.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V04 con V05 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la velocidad del viento no cambia las toneladas de escombros removidas, salvo condiciones extremas sin umbral documentado.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Vientos fuertes detienen grúas y demolición. El umbral operativo no figura en el expediente (VACIO V-VIENTO-01).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V05→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros removidos no altera la velocidad del viento a escala de sitio.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros removidos no altera la velocidad del viento a escala de sitio.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Las pilas de escombros cambian la rugosidad local. El efecto es despreciable para el modelo.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 055 · V10__V14 · clase INTER**

- **V10→V14** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La densidad afecta la protección efectiva mediante el índice (V11) y el aviso (V13).
  - Fundamento: Premisa P-M: la influencia de V10 sobre V14 opera solo a través de V11, V13. Se puntúa en los pares V10→V11 y V11→V14, V10→V13 y V13→V14. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la densidad afecta la protección efectiva mediante el índice (V11) y el aviso (V13).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V11, V13
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V14→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 056 · V06__V09 · clase INTRA**

- **V06→V09** · valor **1** (admisibles: 0, 1) · signo - · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: En el protocolo por eventos, el ruido y el sesgo generan disparos espurios de transmisión que consumen batería.
  - Fundamento: Premisa de arquitectura de ALT-03: el nodo transmite al superar umbrales estadísticos (Paso 1, sección C del documento). No hay medición de consumo en el expediente.
  - Fuentes: F-E3, Paso 1, sección C (solución propuesta): transmisión por umbrales estadísticos (alcance: Describe el protocolo; no mide consumo)
  - Premisas: P-V06-V09: cada transmisión adicional consume energía del nodo en proporción a la cantidad de eventos espurios (modelo energético general).
  - Justificación del valor: Se asigna 1: el costo energético depende del umbral y del filtrado local. No se asigna 2 porque un nodo con consenso previo no transmite por ruido.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Con consenso multinodo previo a la transmisión el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa de diseño sin medición.
- **V09→V06** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La pérdida de nodos no cambia el error del sensor individual. Reduce la corrección entre vecinos, efecto que pasa por la densidad (V10).
  - Fundamento: Premisa P-M: la influencia de V09 sobre V06 opera solo a través de V10. Se puntúa en los pares V09→V10 y V10→V06. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la pérdida de nodos no cambia el error del sensor individual. Reduce la corrección entre vecinos, efecto que pasa por la densidad (V10).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V10
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.

**Ficha 057 · V01__V07 · clase INTER**

- **V01→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La concentración de PM2,5 no fija la frecuencia de calibración, que es una decisión operativa y de diseño.
  - Fundamento: Premisa P-M: la influencia de V01 sobre V07 opera solo a través de V06. Se puntúa en los pares V01→V06 y V06→V07. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la concentración de PM2,5 no fija la frecuencia de calibración, que es una decisión operativa y de diseño.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un episodio extremo podría motivar calibraciones adicionales. Esa respuesta pasa por el error observado (V06) y por la decisión institucional.
  - Mediadores del modelo: V06
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V07→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración algorítmica corrige la lectura, no la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V07 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la calibración algorítmica corrige la lectura, no la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 058 · V11__V13 · clase INTRA**

- **V11→V13** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El nivel del índice no cambia el tiempo de aviso. Un índice con pronóstico sí lo haría, pero el diseño no lo incluye.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el nivel del índice no cambia el tiempo de aviso. Un índice con pronóstico sí lo haría, pero el diseño no lo incluye.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un índice predictivo cambiaría el aviso. Se evalúa como alternativa en F4.4-MDR.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica el valor del índice.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V11 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica el valor del índice.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 059 · V04__V15 · clase INTER**

- **V04→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El viento no determina el uso institucional del tablero.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V04 con V15 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el viento no determina el uso institucional del tablero.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V15→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El uso institucional del tablero no modifica el viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el uso institucional del tablero no modifica el viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Las órdenes de rociado afectan las emisiones por V05, no la humedad ambiental.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 060 · V11__V12 · clase INTRA**

- **V11→V12** · valor **2** (admisibles: 1, 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: El umbral del índice define qué se considera alerta. Umbrales bajos o índices hipersensibles aumentan la proporción de alertas sin superación de umbral real.
  - Fundamento: Ledger E3-P04, fila V11->V12 (INFERIDO, magnitud 2, signo +). F-INF §1.3 hallazgo 2: ningún documento de alertas reporta falsas alarmas, por lo que no existe línea base empírica.
  - Fuentes: F-E3, E3-P04 §12, fila V11->V12 (alcance: Valor heredado); F-INF, §1.3 hallazgo 2; §8.4 D-05 (validar un índice local AQHI) (alcance: Respalda la ausencia de validación y la recomendación de validar)
  - Justificación del valor: Se asigna 2. El umbral es un parámetro de diseño que modifica la tasa sin agente intermedio. Una validación adecuada acota su efecto.
  - Ancla comparada: Igual a ANC-2.
  - Explicación rival: Si el umbral se calibra con curva ROC y verdad de referencia, el índice no aumenta por sí mismo las falsas alarmas. El valor sería 0 o 1.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo de diseño. Sin línea base empírica en el corpus.
- **V12→V11** · valor **1** (admisibles: 0, 1, 2) · signo - · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Ante falsas alarmas repetidas, los responsables ajustan a la baja la sensibilidad del índice para evitar pánico y desgaste.
  - Fundamento: Premisa de la iteración previa del documento (F4.4.4, V12->V11 = 1, mecanismo algorítmico). Sin fuente en el corpus.
  - Premisas: P-V12-V11: los operadores del índice reajustan umbrales en respuesta a la tasa de falsas alarmas observada (práctica de gestión).
  - Justificación del valor: Se asigna 1: el ajuste es una respuesta de gestión posible pero no automática ni inmediata.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Si los umbrales están fijados por norma, el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa de gestión sin evidencia.

**Ficha 061 · V10__V15 · clase INTER**

- **V10→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La densidad no determina el uso institucional del tablero de forma directa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V15 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad no determina el uso institucional del tablero de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una mayor resolución puede aumentar la utilidad percibida. Ese efecto pasa por V11.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V15→V10** · valor **1** (admisibles: 0, 1) · signo + · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Las entidades que adoptan el sistema pueden financiar nodos adicionales y ampliar la resolución del gemelo.
  - Fundamento: Paso 5, Tabla E3-5.0: indicador del PDD de Caldas con línea base 12 y meta 40 estaciones. El documento lo rotula Verificado sin aportar fuente.
  - Fuentes: F-E3, Paso 5, Tabla E3-5.0, fila Indicador del PDD asociado (alcance: Indicador citado sin fuente en el expediente)
  - Justificación del valor: Se asigna 1: la ampliación es una opción posterior a la adopción y depende de ciclos presupuestales de dos años.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Sin recursos de expansión el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Meta territorial sin verificación. El territorio es un SUPUESTO.

**Ficha 062 · V02__V11 · clase INTER**

- **V02→V11** · valor **2** (admisibles: 0, 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Las formulaciones de AQHI con PM10 incorporan el polvo grueso al nivel de peligro. En actividades de demolición el PM10 predomina en la exposición ocupacional.
  - Fundamento: Mismas bases que V01->V11. La participación del PM10 en la fórmula local es VACIO V-AQHI-01.
  - Fuentes: F-INF, §1.3 hallazgo 5 (Liao et al., 2026, pp. 6 y 8) (alcance: Respalda la existencia de la familia de índices; no la composición local)
  - Premisas: P-AQHI: el índice del proyecto usa PM2,5 y PM10 como insumos (descripción del tablero en E3-P09 y E3-P11).
  - Justificación del valor: Se asigna 2 y no 3. El PM10 entra al índice con menor peso de mortalidad que el PM2,5 en las formulaciones conocidas. Su participación local es incierta.
  - Ancla comparada: Menor que ANC-3. Mayor que ANC-2 porque el efecto es directo, no una resta parcial.
  - Explicación rival: Si el índice usa solo PM2,5, el valor sería 0. Si el tablero reporta PM10 como índice separado, el valor sería 3.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Fórmula local no disponible.
- **V11→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El índice emitido en pantalla no modifica la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el índice emitido en pantalla no modifica la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 063 · V10__V12 · clase INTER**

- **V10→V12** · valor **1** (admisibles: 0, 1, 2) · signo - · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: El consenso entre nodos vecinos filtra picos espurios antes de emitir una alerta.
  - Fundamento: Paso 4, Tabla E3-4.2, fila C11 (V12): alternativa imaginable de suprimir alertas espurias con lógica de consenso multinodo (decisión Cuestionar).
  - Fuentes: F-E3, Paso 4, Tabla E3-4.2, fila C11 (V12) (alcance: Propuesta de diseño)
  - Justificación del valor: Se asigna 1: el consenso requiere vecinos cercanos y sensores independientes, condición que 100 nodos en tres departamentos cumplen solo en parte.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Con nodos dispersos sin vecinos, el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Alternativa de diseño sin evidencia empírica.
- **V12→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no cambian la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no cambian la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 064 · V02__V07 · clase INTER**

- **V02→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La concentración de PM10 no fija la frecuencia de calibración. Esta es una decisión operativa.
  - Fundamento: Premisa P-M: la influencia de V02 sobre V07 opera solo a través de V06. Se puntúa en los pares V02→V06 y V06→V07. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la concentración de PM10 no fija la frecuencia de calibración. Esta es una decisión operativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un episodio extremo podría motivar calibraciones adicionales mediante el error observado (V06).
  - Mediadores del modelo: V06
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V07→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración algorítmica corrige la lectura, no la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V07 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la calibración algorítmica corrige la lectura, no la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 065 · V03__V08 · clase INTER**

- **V03→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La humedad relativa no altera el retraso de transmisión en los enlaces sub-GHz y celulares considerados.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V03 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la humedad relativa no altera el retraso de transmisión en los enlaces sub-GHz y celulares considerados.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La lluvia degrada enlaces de microondas. No aplica a los enlaces del diseño y la lluvia no está en el modelo.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V08→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El retraso de datos no modifica la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso de datos no modifica la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 066 · V02__V15 · clase INTER**

- **V02→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La concentración de polvo no determina el uso institucional del tablero.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V02 con V15 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración de polvo no determina el uso institucional del tablero.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una exposición visible podría aumentar la demanda de información. Esa demanda se expresa por V11.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V15→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El uso institucional del tablero no modifica la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el uso institucional del tablero no modifica la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Las órdenes de rociado afectan las emisiones por V05, no la humedad ambiental.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 067 · V08__V15 · clase INTER**

- **V08→V15** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Razón del cero: El retraso no determina el uso institucional del tablero de forma directa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V15 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso no determina el uso institucional del tablero de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Latencias perceptibles pueden desmotivar el uso. No hay evidencia en el expediente.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V15→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La adopción institucional no cambia el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la adopción institucional no cambia el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 068 · V02__V12 · clase INTER**

- **V02→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: Una concentración real alta genera alertas verdaderas. La falsa alarma proviene del error de medición o del umbral.
  - Fundamento: Premisa P-M: la influencia de V02 sobre V12 opera solo a través de V06, V11. Se puntúa en los pares V02→V06 y V06→V12, V02→V11 y V11→V12. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque una concentración real alta genera alertas verdaderas. La falsa alarma proviene del error de medición o del umbral.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Cerca del umbral, una concentración alta aumenta la probabilidad de clasificar mal. Ese efecto opera por V06 y V11.
  - Mediadores del modelo: V06, V11
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V12→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no modifican la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no modifican la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 069 · V04__V11 · clase INTER**

- **V04→V11** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El viento afecta el índice a través de la concentración (V01, V02), no directamente.
  - Fundamento: Premisa P-M: la influencia de V04 sobre V11 opera solo a través de V01, V02. Se puntúa en los pares V04→V01 y V01→V11, V04→V02 y V02→V11. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el viento afecta el índice a través de la concentración (V01, V02), no directamente.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un pronóstico de viento integrado al índice cambiaría la relación. El expediente no lo describe.
  - Mediadores del modelo: V01, V02
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V11→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El índice emitido en pantalla no modifica el viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el índice emitido en pantalla no modifica el viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 070 · V07__V12 · clase INTER**

- **V07→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La calibración reduce las falsas alarmas mediante el error (V06) y el índice (V11).
  - Fundamento: Premisa P-M: la influencia de V07 sobre V12 opera solo a través de V06, V11. Se puntúa en los pares V07→V06 y V06→V12, V07→V11 y V11→V12. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la calibración reduce las falsas alarmas mediante el error (V06) y el índice (V11).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V06, V11
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V12→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: Las falsas alarmas no fijan la frecuencia de calibración. La revisión técnica de alertas espurias se realiza mediante el error detectado (V06).
  - Fundamento: Premisa P-M: la influencia de V12 sobre V07 opera solo a través de V06. Se puntúa en los pares V12→V06 y V06→V07. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no fijan la frecuencia de calibración. La revisión técnica de alertas espurias se realiza mediante el error detectado (V06).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una política de auditoría tras cada falsa alarma elevaría la frecuencia. No está definida.
  - Mediadores del modelo: V06
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.

**Ficha 071 · V09__V12 · clase INTER**

- **V09→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La pérdida de nodos afecta las falsas alarmas mediante la capacidad de consenso (V10).
  - Fundamento: Premisa P-M: la influencia de V09 sobre V12 opera solo a través de V10. Se puntúa en los pares V09→V10 y V10→V12. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la pérdida de nodos afecta las falsas alarmas mediante la capacidad de consenso (V10).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V10
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V12→V09** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: Las falsas alarmas no cambian la disponibilidad de nodos.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V09 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no cambian la disponibilidad de nodos.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Las transmisiones por alerta consumen batería. El efecto es el de V06->V09.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 072 · V05__V08 · clase INTER**

- **V05→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros no cambia el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros no cambia el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V08→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El retraso de datos no cambia las toneladas de escombros removidas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V05 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso de datos no cambia las toneladas de escombros removidas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 073 · V07__V14 · clase INTER**

- **V07→V14** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La calibración afecta la protección efectiva mediante V06, V11 y V12.
  - Fundamento: Premisa P-M: la influencia de V07 sobre V14 opera solo a través de V06, V11. Se puntúa en los pares V07→V06 y V06→V14, V07→V11 y V11→V14. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la calibración afecta la protección efectiva mediante V06, V11 y V12.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V06, V11
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V14→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica la frecuencia de calibración.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica la frecuencia de calibración.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 074 · V03__V12 · clase INTER**

- **V03→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La humedad produce falsas alarmas al sesgar la lectura óptica. La ruta pasa por V06.
  - Fundamento: Premisa P-M: la influencia de V03 sobre V12 opera solo a través de V06. Se puntúa en los pares V03→V06 y V06→V12. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la humedad produce falsas alarmas al sesgar la lectura óptica. La ruta pasa por V06.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un umbral dependiente de la humedad cambiaría la relación. No existe en el expediente.
  - Mediadores del modelo: V06
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V12→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no modifican la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no modifican la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 075 · V10__V11 · clase INTER**

- **V10→V11** · valor **2** (admisibles: 1, 2, 3) · signo NO_IDENTIFICADO · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Mayor resolución espacial representa mejor la exposición local y cambia el valor del índice asignado a cada sitio.
  - Fundamento: Ledger E3-P04, fila V10->V11 (PROPUESTO, magnitud 3, signo +). El sentido de la influencia no es un aumento del nivel del índice sino un cambio de su fidelidad.
  - Fuentes: F-E3, E3-P04 §12, fila V10->V11 (alcance: Valor heredado; la revisión lo modifica)
  - Justificación del valor: Se asigna 2 y no 3: la resolución mejora la representatividad pero no altera la fórmula. El efecto es moderado y su signo no es identificable.
  - Ancla comparada: Igual a ANC-2.
  - Explicación rival: Con interpolación pobre entre nodos, la densidad no mejoraría la fidelidad y el valor sería 1.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Relación de fidelidad, no de magnitud. Sin dato de representatividad.
- **V11→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El nivel del índice no cambia la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el nivel del índice no cambia la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un índice crítico podría justificar más nodos. Esa decisión pasa por V15->V10.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 076 · V10__V13 · clase INTER**

- **V10→V13** · valor **1** (admisibles: 0, 1, 2) · signo + · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Una red más densa detecta la pluma aguas arriba y alarga el aviso a los receptores.
  - Fundamento: Relación geométrica entre la distancia de detección y los receptores (P-V04-V13).
  - Premisas: P-V10-V13: más puntos de detección reducen la distancia media entre la pluma y el sensor más cercano (relación geométrica).
  - Justificación del valor: Se asigna 1: el beneficio depende de la geometría fuente-receptor, no definida.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Para exposición dentro del sitio el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Relación geométrica sin diseño de ubicación.
- **V13→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica la cantidad de nodos por km² diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica la cantidad de nodos por km² diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 077 · V09__V15 · clase INTER**

- **V09→V15** · valor **1** (admisibles: 0, 1, 2) · signo + · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Un tablero con huecos por nodos inactivos pierde utilidad percibida. La confiabilidad del servicio sostiene el uso institucional.
  - Fundamento: Supuesto de escenario. F-INF §3.1 documenta 96 de 570 estaciones inactivas o sin estado en Brasil (Tavella et al., 2026, p. 6). No mide su efecto sobre el uso.
  - Fuentes: F-INF, §3.1 (Tavella et al., 2026, p. 6): 96 de 570 estaciones inactivas o sin estado (alcance: Cita secundaria; no mide efecto sobre uso)
  - Premisas: P-V09-V15: la percepción de falla del servicio reduce el uso del tablero (supuesto de escenario).
  - Justificación del valor: Se asigna 1: la relación es plausible y directa, pero el uso depende más del mandato formal y de la utilidad del índice.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Con cobertura redundante la caída de nodos no sería visible para el usuario y el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Supuesto sin medición. El efecto sobre el uso no se estudia en el corpus.
- **V15→V09** · valor **2** (admisibles: 1, 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: La adopción institucional legitima el gasto en cuadrillas de mantenimiento que reponen baterías y nodos, y sostiene la disponibilidad.
  - Fundamento: Iteración previa del documento (F4.4.4, V15->V09 = 2). La Tabla E3-14.2 presupuesta mantenimiento FRU de 25 a 45 M por año con convenios con ARL y corporación. F-INF cita 96 de 570 estaciones inactivas en Brasil (Tavella et al., 2026, p. 6).
  - Fuentes: F-E3, Capítulo 14, Tabla E3-14.2, fila Mantenimiento FRU (alcance: Propuesta de financiamiento); F-INF, §3.1 y §10.2 (Tavella et al., 2026, p. 6): pérdida de datos por falta de mantenimiento (alcance: Cita secundaria)
  - Justificación del valor: Se asigna 2: el mantenimiento depende de presupuesto recurrente de quien adopta. Es una condición clara pero no mecánica de la disponibilidad.
  - Ancla comparada: Igual a ANC-2.
  - Explicación rival: Si el mantenimiento lo cubre la empresa por contrato, el valor sería 1.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo coherente con la evidencia de inactividad por falta de mantenimiento. Sin compromiso firmado.

**Ficha 078 · V08__V14 · clase INTER**

- **V08→V14** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El retraso afecta la protección efectiva mediante el tiempo de aviso (V13).
  - Fundamento: Premisa P-M: la influencia de V08 sobre V14 opera solo a través de V13. Se puntúa en los pares V08→V13 y V13→V14. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el retraso afecta la protección efectiva mediante el tiempo de aviso (V13).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V13
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V14→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 079 · V06__V11 · clase INTER**

- **V06→V11** · valor **3** (admisibles: 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: El error del hardware entra al cálculo del índice sin intermediario humano y desplaza su nivel de peligro.
  - Fundamento: Ledger E3-P04, fila V06->V11 (INFERIDO, magnitud 3). F-INF documenta que los índices carecen de validación (9,4 % con partición de datos). Las patentes de calificación cambian de valor con reglas de datos faltantes.
  - Fuentes: F-E3, E3-P04 §12, fila V06->V11; Paso 4, F4.4.2, ancla del valor 3 (alcance: Define el ancla); F-INF, §1.3 hallazgo 5 (Liao et al., 2026, pp. 6 y 8; Wilson et al., 2024, p. 108) (alcance: Respalda la sensibilidad de los índices a las reglas de datos; no cuantifica la propagación del error)
  - Justificación del valor: Se asigna 3 porque la propagación es aritmética y no tiene paso humano intermedio: es el ancla ANC-3.
  - Ancla comparada: Es ANC-3.
  - Explicación rival: Un índice con filtros de calidad de dato que descarte lecturas dudosas amortiguaría la propagación. El expediente no los describe.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo aritmético. Filtros de calidad no descritos.
- **V11→V06** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El nivel del índice no cambia el error del sensor.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V06 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el nivel del índice no cambia el error del sensor.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 080 · V01__V08 · clase INTER**

- **V01→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración no cambia el retraso de transmisión de los paquetes. El contenido del dato no altera el enlace.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V01 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración no cambia el retraso de transmisión de los paquetes. El contenido del dato no altera el enlace.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V08→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El retraso de datos no modifica la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso de datos no modifica la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 081 · V09__V14 · clase INTER**

- **V09→V14** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La pérdida de nodos afecta la protección efectiva mediante el índice (V11) y el aviso (V13).
  - Fundamento: Premisa P-M: la influencia de V09 sobre V14 opera solo a través de V11, V13. Se puntúa en los pares V09→V11 y V11→V14, V09→V13 y V13→V14. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque la pérdida de nodos afecta la protección efectiva mediante el índice (V11) y el aviso (V13).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V11, V13
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V14→V09** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El número de personas protegidas no modifica la disponibilidad de nodos.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V14 con V09 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no modifica la disponibilidad de nodos.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 082 · V05__V07 · clase INTER**

- **V05→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros no fija la frecuencia de calibración.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros no fija la frecuencia de calibración.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V07→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración no cambia las toneladas de escombros removidas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V07 con V05 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la calibración no cambia las toneladas de escombros removidas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 083 · V05__V09 · clase INTER**

- **V05→V09** · valor **2** (admisibles: 1, 2, 3) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: La maquinaria pesada golpea, entierra o desplaza nodos instalados cerca del frente de obra, y el vandalismo aumenta con la actividad.
  - Fundamento: Premisa de la iteración previa (F4.4.4, V05->V09 = 2) citada a Ruiz-Carrascal et al. (2026, p. 14), cuya página no figura en F-INF (F-INF cita pp. 3, 5, 6 y 8). El mecanismo es plausible y coherente con los riesgos de vandalismo y antivandálicos del expediente.
  - Fuentes: F-E3, Paso 4, F4.4.4, fila V05->V09; Capítulo 10 R-TEC; Capítulo 8 Tabla E3-8.4 (antivandálico) (alcance: El expediente anticipa vandalismo y daño físico); F-INF, §1.3 hallazgo 4 y §3.1: SIATA opera 535 equipos (Ruiz-Carrascal et al., 2026, p. 8) (alcance: No reporta pérdidas por maquinaria)
  - Premisas: P-V05-V09: los nodos en el frente de obra enfrentan tránsito de maquinaria pesada y movimiento de material (condición del sitio).
  - Justificación del valor: Se asigna 2. La pérdida física de nodos es una falla propia del sitio. Es mayor que la corrosión gradual (ANC-1) y menor que una destrucción total de la red.
  - Ancla comparada: Mayor que ANC-1. Igual a ANC-2 en nivel.
  - Explicación rival: Con ubicación acordada fuera del frente de obra (P03) el valor sería 1.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo plausible. Cita previa no verificable en F-INF. Sin tasa de pérdida.
- **V09→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La disponibilidad de nodos no cambia las toneladas de escombros removidas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V09 con V05 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la disponibilidad de nodos no cambia las toneladas de escombros removidas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 084 · V04__V09 · clase INTER**

- **V04→V09** · valor **1** (admisibles: 0, 1) · signo - · naturaleza SUPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: El viento fuerte derriba o daña mástiles y carcasas montadas sobre escombros inestables.
  - Fundamento: Premisa de ingeniería. El expediente presupuesta mástiles NEMA 4X antivandálicos (Tabla E3-8.4) sin carga de viento declarada.
  - Fuentes: F-E3, Capítulo 8, Tabla E3-8.4 (kits de cerramiento NEMA 4X y mástiles) (alcance: Muestra la existencia de mástiles; no declara cargas de viento)
  - Premisas: P-V04-V09: las ráfagas generan cargas sobre estructuras ligeras en terreno inestable (conocimiento de ingeniería general).
  - Justificación del valor: Se asigna 1: la falla por viento es esporádica. La causa principal de pérdida física es la maquinaria (V05->V09).
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Con cimentación adecuada el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Sin dato de diseño estructural.
- **V09→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La disponibilidad de nodos no modifica el viento.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V09 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la disponibilidad de nodos no modifica el viento.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 085 · V01__V12 · clase INTER**

- **V01→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: Una concentración real alta genera alertas verdaderas. La falsa alarma proviene del error de medición o del umbral, no de la concentración.
  - Fundamento: Premisa P-M: la influencia de V01 sobre V12 opera solo a través de V06, V11. Se puntúa en los pares V01→V06 y V06→V12, V01→V11 y V11→V12. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque una concentración real alta genera alertas verdaderas. La falsa alarma proviene del error de medición o del umbral, no de la concentración.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Cerca del umbral, una concentración alta aumenta la probabilidad de clasificar mal. Ese efecto opera por V06 y V11.
  - Mediadores del modelo: V06, V11
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V12→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no modifican la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no modifican la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 086 · V03__V10 · clase INTER**

- **V03→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La humedad no cambia la cantidad de nodos por km² del gemelo diseñada.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V03 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la humedad no cambia la cantidad de nodos por km² del gemelo diseñada.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Si V10 midiera densidad efectiva, la humedad actuaría por V09. Ese vínculo se puntúa allí.
  - Mediadores del modelo: V09
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La densidad de nodos no modifica la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad de nodos no modifica la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 087 · V02__V06 · clase INTER**

- **V02→V06** · valor **3** (admisibles: 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: El polvo grueso ensucia lentes y entradas de aire del sensor. El canal de PM10 de los sensores de bajo costo tiene eficiencia de captura limitada. Ambos efectos elevan el error sistemático.
  - Fundamento: Mecanismo de ensuciamiento de lente del ledger E3-P04 (INFERIDO, magnitud 3). F-INF registra en una mina a cielo abierto un PM2,5 medio de 159,11 µg/m3 y un cociente PM2,5/PM10 de 0,88. Eso muestra carga de polvo alta en sitios de operación.
  - Fuentes: F-INF, §3.1 Tabla maestra de KPI (Suresh et al., 2025, pp. 10, 22 y 30): PM2,5 medio 159,11 µg/m3; PM2,5/PM10 = 0,88 (alcance: Respalda la carga de polvo en sitio de mina; no mide ensuciamiento de lente); F-E3, E3-P04 §12, fila V02->V06 (INFERIDO, magnitud 3) (alcance: Valor heredado)
  - Premisas: P-V02-V06: el depósito de partículas sobre la óptica del sensor aumenta con la exposición acumulada y degrada la lectura (conocimiento técnico general).
  - Justificación del valor: Se asigna 3. El depósito de polvo grueso degrada la medición de forma persistente y obliga a limpiar o sustituir. Difiere del efecto gradual de ANC-1.
  - Ancla comparada: Menor o igual que ANC-3: el ensuciamiento actúa con el tiempo de exposición, no de forma instantánea.
  - Explicación rival: Los sensores con inlet protegido y limpieza programada reducen el efecto. El valor sería 2 si el mantenimiento preventivo (P05) se cumple.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo físico plausible. Evidencia indirecta de carga de polvo. Efecto del mantenimiento desconocido.
- **V06→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El error del sensor altera la medición de PM10. No altera la masa de partículas que el diccionario define como V02.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error del sensor altera la medición de PM10. No altera la masa de partículas que el diccionario define como V02.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Si V02 se leyera como concentración medida por la red, el error la modificaría (VACIO V-DIC-01).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 088 · V04__V13 · clase INTER**

- **V04→V13** · valor **1** (admisibles: 0, 1, 2) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: La velocidad del viento determina el tiempo de transporte de una pluma entre la detección aguas arriba y la llegada a receptores. Mayor velocidad reduce el aviso útil.
  - Fundamento: Relación geométrica distancia/velocidad. Aplica a receptores a sotavento, no a operarios dentro de la propia nube.
  - Premisas: P-V04-V13: tiempo de aviso aguas abajo = distancia entre detección y receptor dividida por velocidad de advección (relación cinemática).
  - Justificación del valor: Se asigna 1. El efecto es real para comunidades vecinas, no para el personal en el sitio. Depende de la geometría de la red.
  - Ancla comparada: Menor que ANC-2 (V08->V13). Igual a ANC-1 en nivel.
  - Explicación rival: Para exposición in situ el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Relación geométrica. Depende de la ubicación de nodos y receptores, no definida.
- **V13→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica el viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica el viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 089 · V02__V13 · clase INTER**

- **V02→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración de polvo no cambia el tiempo de aviso.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V02 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración de polvo no cambia el tiempo de aviso.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 090 · V03__V13 · clase INTER**

- **V03→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La humedad no cambia el tiempo de aviso.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V03 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la humedad no cambia el tiempo de aviso.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V03** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica la humedad relativa.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V03 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica la humedad relativa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 091 · V08__V13 · clase INTER**

- **V08→V13** · valor **2** (admisibles: 1, 2, 3) · signo - · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: El retraso de datos resta minutos al tiempo útil de aviso desde la detección hasta el impacto.
  - Fundamento: Ledger E3-P04, fila V08->V13 (PROPUESTO, magnitud 2, signo -). F-INF §1.3 hallazgo 2 informa que ningún documento de alertas reporta anticipación, por lo que no hay línea base empírica.
  - Fuentes: F-E3, E3-P04 §12, fila V08->V13; Paso 4, F4.4.2, ancla del valor 2 (alcance: Define el ancla); F-INF, §1.3 hallazgo 2 (alcance: Ausencia de línea base de anticipación)
  - Justificación del valor: Se asigna 2. La relación es aritmética: tiempo de aviso igual a tiempo de impacto menos tiempo de detección menos latencia. Es parcial cuando el aviso se mide en horas.
  - Ancla comparada: Es ANC-2.
  - Explicación rival: Con aviso medido en horas y latencia de minutos la porción relativa es pequeña y el valor sería 1.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Relación aritmética. Magnitudes de aviso y latencia sin medición.
- **V13→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 092 · V07__V15 · clase INTER**

- **V07→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El uso institucional depende de la calidad percibida del dato, que la calibración mejora por V06 y V12.
  - Fundamento: Premisa P-M: la influencia de V07 sobre V15 opera solo a través de V06, V12. Se puntúa en los pares V07→V06 y V06→V15, V07→V12 y V12→V15. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el uso institucional depende de la calidad percibida del dato, que la calibración mejora por V06 y V12.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: V06, V12
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V15→V07** · valor **1** (admisibles: 0, 1, 2) · signo + · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Con presupuesto operativo de las alcaldías se sostienen científicos de datos y ciclos de actualización de la calibración.
  - Fundamento: Iteración previa del documento (F4.4.4, V15->V07 = 2). La Tabla E3-14.2 asigna 120 M anuales de soporte de algoritmos a la IES y la UNGRD en especie.
  - Fuentes: F-E3, Capítulo 14, Tabla E3-14.2, fila Personal técnico y soporte de algoritmos; Paso 4, F4.4.4 (alcance: Propuesta de financiamiento; no hay compromiso)
  - Justificación del valor: Se asigna 1 y no 2: la calibración puede contratarse con la IES o la empresa independientemente del uso institucional durante H. El vínculo cobra fuerza en la fase posproyecto.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Bajo la premisa PD-0 (continuidad sin receptor público único), el financiamiento posproyecto de calibración depende de la adopción y el valor sería 2.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Depende del diseño de sostenibilidad aún no ratificado.

**Ficha 093 · V01__V15 · clase INTER**

- **V01→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: La concentración no determina el uso institucional del tablero. El uso depende de la utilidad percibida y del mandato (V11, V12, V14).
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V01 con V15 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración no determina el uso institucional del tablero. El uso depende de la utilidad percibida y del mandato (V11, V12, V14).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una exposición visible podría aumentar la demanda de información. Esa demanda se expresa mediante la utilidad del índice (V11).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V15→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El uso institucional del tablero no modifica la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V15 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el uso institucional del tablero no modifica la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Las órdenes de rociado afectan las emisiones por V05, no la humedad ambiental.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 094 · V05__V15 · clase INTER**

- **V05→V15** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros no determina el uso institucional del tablero.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V15 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros no determina el uso institucional del tablero.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V15→V05** · valor **1** (admisibles: 0, 1) · signo - · naturaleza PROPUESTO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Las autoridades que usan el tablero pueden ordenar rociado, reprogramación o pausas de obra que reducen el volumen removido.
  - Fundamento: Registro RDG ND-16 del Capítulo 12 del documento: orden de cese de actividades basada en el dato como condición de eficacia. No hay norma de umbrales de PM para pausar obras en el expediente.
  - Fuentes: F-E3, Capítulo 12, registro RDG ND-16, campo NODOS_GRISES (alcance: Plantea la orden de cese como condición de eficacia)
  - Justificación del valor: Se asigna 1: la remoción es una prioridad de reconstrucción y las pausas serían excepcionales y localizadas.
  - Ancla comparada: Igual a ANC-1.
  - Explicación rival: Si las órdenes se limitan a la evacuación de personas sin pausar la remoción, el valor sería 0.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Premisa de gestión. Sin umbral normativo.

**Ficha 095 · V06__V13 · clase INTER**

- **V06→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El error de medición no cambia el tiempo de aviso.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error de medición no cambia el tiempo de aviso.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Un error grande puede retrasar la confirmación de una alerta. El efecto es de segundo orden.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V06** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El tiempo de aviso no modifica el error del sensor.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V13 con V06 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no modifica el error del sensor.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 096 · V02__V08 · clase INTER**

- **V02→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración de polvo no cambia el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V02 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración de polvo no cambia el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V08→V02** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El retraso de datos no modifica la masa de PM10 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V02 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso de datos no modifica la masa de PM10 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 097 · V04__V12 · clase INTER**

- **V04→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El viento no determina las falsas alarmas, que dependen del error y del umbral.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V04 con V12 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el viento no determina las falsas alarmas, que dependen del error y del umbral.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V12→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no modifican el viento superficial.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no modifican el viento superficial.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 098 · V01__V11 · clase INTER**

- **V01→V11** · valor **3** (admisibles: 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Mecanismo: El AQHI se calcula a partir de concentraciones ponderadas por riesgo. El PM2,5 entra directamente a la fórmula del índice sin acción humana intermedia.
  - Fundamento: Definición de los índices de calidad del aire y salud (conocimiento técnico general). La fórmula local de V11 no figura en el expediente: VACIO V-AQHI-01. F-INF documenta la familia de índices AQHI y su baja validación.
  - Fuentes: F-INF, §1.3 hallazgo 5 (Liao et al., 2026, pp. 6 y 8): 53 estudios de índices; 9,4 % con partición de datos (alcance: Respalda la existencia y baja validación de la familia de índices; no la fórmula local)
  - Premisas: P-AQHI: el índice del proyecto usa PM2,5 y PM10 como insumos. E3-P09 y E3-P11 describen un tablero AQHI alimentado por los nodos de material particulado.
  - Justificación del valor: Se asigna 3 porque un cambio en PM2,5 modifica el valor del índice de forma casi mecánica, igual que el ancla ANC-3. E3-P04 omitió este vínculo (hallazgo H-E de la revisión).
  - Ancla comparada: Igual a ANC-3 (V06->V11).
  - Explicación rival: Si el índice local se basara solo en NO2 y O3, la influencia sería 0. El expediente describe un tablero alimentado por nodos de material particulado.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Mecanismo definicional. Fórmula local no disponible. Los demás contaminantes no están en el modelo.
- **V11→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El índice emitido en pantalla no modifica la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V11 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el índice emitido en pantalla no modifica la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 099 · V01__V10 · clase INTER**

- **V01→V10** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La concentración no cambia la cantidad de nodos por km² del gemelo.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V01 con V10 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la concentración no cambia la cantidad de nodos por km² del gemelo.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V10→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La densidad de nodos no modifica la masa de PM2,5 del aire.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V10 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la densidad de nodos no modifica la masa de PM2,5 del aire.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 100 · V08__V12 · clase INTER**

- **V08→V12** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El retraso no determina la tasa de alertas sin superación de umbral real.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V08 con V12 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el retraso no determina la tasa de alertas sin superación de umbral real.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Datos rezagados podrían disparar alertas sobre condiciones ya superadas. El efecto es de segundo orden.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V12→V08** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: Las falsas alarmas no cambian el retraso de transmisión.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V12 con V08 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque las falsas alarmas no cambian el retraso de transmisión.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 101 · V05__V06 · clase INTER**

- **V05→V06** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El volumen de escombros afecta el error de medición por la carga de partículas (V01, V02), no de forma directa.
  - Fundamento: Premisa P-M: la influencia de V05 sobre V06 opera solo a través de V01, V02. Se puntúa en los pares V05→V01 y V01→V06, V05→V02 y V02→V06. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros afecta el error de medición por la carga de partículas (V01, V02), no de forma directa.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La vibración de la maquinaria puede afectar el sensor. El efecto es despreciable frente al polvo.
  - Mediadores del modelo: V01, V02
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.
- **V06→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El error del sensor no cambia las toneladas de escombros removidas.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V05 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error del sensor no cambia las toneladas de escombros removidas.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Una decisión de obra basada en datos erróneos modificaría V05 por la vía institucional. Se puntúa en V15->V05.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 102 · V01__V06 · clase INTER**

- **V01→V06** · valor **2** (admisibles: 1, 2, 3) · signo + · naturaleza INFERIDO · estado PROPUESTO · confianza BAJA
  - Mecanismo: Concentraciones muy altas saturan el contador óptico y elevan el error de coincidencia frente a la referencia gravimétrica.
  - Fundamento: Mecanismo de saturación del contador láser del ledger E3-P04 (INFERIDO, magnitud 2). El umbral de saturación del sensor no figura en el expediente: VACIO.
  - Fuentes: F-E3, E3-P04 §12, fila V01->V06 (INFERIDO, magnitud 2) (alcance: Documenta el valor heredado, no su veracidad)
  - Premisas: P-V01-V06: el contador láser tiene un límite superior de detección. Sobre él la lectura se satura o se subestima (conocimiento técnico general, no fuente del expediente).
  - Justificación del valor: Se asigna 2 y no 3: el error crece con la concentración solo sobre un umbral de saturación del sensor que se desconoce. Sobre él la influencia sería mayor.
  - Ancla comparada: Mayor que ANC-1 (V03->V09, efecto gradual) y menor que ANC-3 (V06->V11, determinación sin intermediario).
  - Explicación rival: El error normalizado puede disminuir con la concentración, porque el cociente se divide por un denominador mayor. El signo podría ser MIXTO.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Sin ficha técnica del sensor. Mecanismo plausible. Dominio admisible amplio.
- **V06→V01** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El error del sensor altera la medición de PM2,5. No altera la masa de partículas que el diccionario define como V01.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V06 con V01 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el error del sensor altera la medición de PM2,5. No altera la masa de partículas que el diccionario define como V01.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Si V01 se leyera como concentración medida por la red, el error la modificaría. El diccionario E3-P01 la define como masa física (VACIO V-DIC-01).
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.

**Ficha 103 · V05__V13 · clase INTER**

- **V05→V13** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: El volumen de escombros no cambia el tiempo de aviso.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V13 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros no cambia el tiempo de aviso.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V13→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El tiempo de aviso no cambia por sí solo las toneladas removidas. Una pausa programada exige decisión institucional (V15).
  - Fundamento: Premisa P-M: la influencia de V13 sobre V05 opera solo a través de V15. Se puntúa en los pares V13→V15 y V15→V05. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el tiempo de aviso no cambia por sí solo las toneladas removidas. Una pausa programada exige decisión institucional (V15).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La pausa programada se puntúa en V15->V05.
  - Mediadores del modelo: V15
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.

**Ficha 104 · V05__V14 · clase INTER**

- **V05→V14** · valor **0** (admisibles: 0, 1) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El volumen de escombros no cambia directamente el número de personas protegidas. La población expuesta es un dato de contexto fuera del modelo.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V05 con V14 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque el volumen de escombros no cambia directamente el número de personas protegidas. La población expuesta es un dato de contexto fuera del modelo.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Más trabajo implica más operarios expuestos. La variable V14 mide protección efectiva, no exposición.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V14→V05** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza MEDIA
  - Razón del cero: El número de personas protegidas no cambia por sí solo las toneladas removidas. La protección podría imponer pausas por decisión institucional (V15).
  - Fundamento: Premisa P-M: la influencia de V14 sobre V05 opera solo a través de V15. Se puntúa en los pares V14→V15 y V15→V05. No se duplica aquí.
  - Justificación del valor: Se asigna 0 porque el número de personas protegidas no cambia por sí solo las toneladas removidas. La protección podría imponer pausas por decisión institucional (V15).
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: La pausa se puntúa en V15->V05.
  - Mediadores del modelo: V15
  - Motivo de la confianza: Ruta indirecta explícita en el modelo.

**Ficha 105 · V04__V07 · clase INTER**

- **V04→V07** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La velocidad del viento no fija la frecuencia de calibración.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V04 con V07 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la velocidad del viento no fija la frecuencia de calibración.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.
- **V07→V04** · valor **0** (admisibles: 0) · signo NO_APLICA · naturaleza INFERIDO · estado PROPUESTO · confianza ALTA
  - Razón del cero: La calibración no modifica el viento.
  - Fundamento: Premisa P-0: no existe mecanismo físico, informático ni institucional que conecte V07 con V04 dentro de la frontera y el horizonte declarados.
  - Justificación del valor: Se asigna 0 porque la calibración no modifica el viento.
  - Ancla comparada: ANC-0 (ver F4.4.2).
  - Explicación rival: Ninguna alternativa plausible dentro de la frontera.
  - Mediadores del modelo: ninguno
  - Motivo de la confianza: Ausencia de mecanismo por razonamiento físico. Sin medición ni fuente específica.



## Anexo L. JSON canónico de los árboles A-DEC, A-TDC y A-PROB

Los tres árboles se regeneran con la herramienta de referencia a partir de su JSON canónico. El texto de cada bloque coincide con el del archivo correspondiente del repositorio.

### L.1 JSON canónico del árbol A-DEC (ARBOL_1_SGR_CONV56_AIRE.json)

```
{
 "tipo": "DECISION",
 "rol": "A-DEC",
 "titulo": "A-DEC: estrategia de resolución y custodia posproyecto de la red de vigilancia de material particulado",
 "naturaleza": "PROPUESTO",
 "fuente": "Sección 4.4 (escenario S2), E3-P00 a E3-P21 y MDR v3.0; probabilidades y utilidades no declaradas",
 "pregunta": "¿Qué estrategia adopta el proyecto: no intervenir, transferir a un receptor público único o desplegar por tramos con custodia distribuida?",
 "descripcion": "Árbol de decisión cualitativo con tres alternativas: R0 sin intervención, R3 transferencia al receptor público único y R4 despliegue por tramos bajo la premisa de diseño sin receptor público único. Cuatro supuestos críticos en cadena: SC-1 medición, SC-2 energía y enlace, SC-3 uso institucional y SC-4 custodia. Los resultados indican el nivel de la cadena alcanzado. Sin probabilidades ni utilidades declaradas, el valor esperado es NO_CALCULABLE y no se marca ninguna rama elegida.",
 "raiz": {
  "id": "D1",
  "tipo": "DECISION",
  "etiqueta": "Estrategia de resolución y custodia",
  "hijos": [
   {
    "rama": "R4 Despliegue por tramos con piloto de contraste y custodia distribuida",
    "nodo": {
     "id": "A1",
     "tipo": "AZAR",
     "supuesto": "SC-1",
     "etiqueta": "Medición: la corrección local reduce el error frente a la lectura sin corrección dinámica",
     "hijos": [
      {
       "rama": "SC-1 se cumple",
       "nodo": {
        "id": "A2",
        "tipo": "AZAR",
        "supuesto": "SC-2",
        "etiqueta": "Energía y enlace: nodos activos suficientes bajo maquinaria y humedad",
        "hijos": [
         {
          "rama": "SC-2 se cumple",
          "nodo": {
           "id": "A3",
           "tipo": "AZAR",
           "supuesto": "SC-3",
           "etiqueta": "Uso: autoridades adoptan umbrales de alerta validados en sus protocolos",
           "hijos": [
            {
             "rama": "SC-3 se cumple",
             "nodo": {
              "id": "A4",
              "tipo": "AZAR",
              "supuesto": "SC-4",
              "etiqueta": "Custodia: al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo",
              "hijos": [
               {
                "rama": "SC-4 se cumple",
                "nodo": {
                 "id": "AT5",
                 "tipo": "TERMINAL",
                 "etiqueta": "Servicio de vigilancia sostenido con custodia distribuida; protección contribuida con otros actores",
                 "nivel_tdc": "IMPACTO",
                 "resultado": "Valor no declarado (NO_CALCULABLE)"
                }
               },
               {
                "rama": "SC-4 falla",
                "nodo": {
                 "id": "AT4",
                 "tipo": "TERMINAL",
                 "etiqueta": "Uso institucional sin custodio demostrado; cláusula de apertura y servicio mínimo",
                 "nivel_tdc": "RESULTADO_INTERMEDIO",
                 "resultado": "Valor no declarado (NO_CALCULABLE)"
                }
               }
              ]
             }
            },
            {
             "rama": "SC-3 falla",
             "nodo": {
              "id": "AT3",
              "tipo": "TERMINAL",
              "etiqueta": "Mediciones verificadas sin uso institucional; tramo siguiente condicionado a la adopción de umbrales",
              "nivel_tdc": "RESULTADO_INMEDIATO",
              "resultado": "Valor no declarado (NO_CALCULABLE)"
             }
            }
           ]
          }
         },
         {
          "rama": "SC-2 falla",
          "nodo": {
           "id": "AT2",
           "tipo": "TERMINAL",
           "etiqueta": "Error reducido y verificado, con cobertura insuficiente; rediseño del enlace o la energía antes del segundo tramo",
           "nivel_tdc": "RESULTADO_INMEDIATO",
           "resultado": "Valor no declarado (NO_CALCULABLE)"
          }
         }
        ]
       }
      },
      {
       "rama": "SC-1 falla",
       "nodo": {
        "id": "AT1",
        "tipo": "TERMINAL",
        "etiqueta": "Expansión detenida tras el piloto; inversión limitada al primer tramo; conocimiento negativo documentado",
        "nivel_tdc": "PRODUCTO",
        "resultado": "Valor no declarado (NO_CALCULABLE)"
       }
      }
     ]
    }
   },
   {
    "rama": "R3 Red del E3 con transferencia a las alcaldías al mes 25 (receptor único)",
    "nodo": {
     "id": "B1",
     "tipo": "AZAR",
     "supuesto": "SC-1",
     "etiqueta": "Medición: la corrección local reduce el error frente a la lectura sin corrección dinámica",
     "hijos": [
      {
       "rama": "SC-1 se cumple",
       "nodo": {
        "id": "B2",
        "tipo": "AZAR",
        "supuesto": "SC-2",
        "etiqueta": "Energía y enlace: nodos activos suficientes bajo maquinaria y humedad",
        "hijos": [
         {
          "rama": "SC-2 se cumple",
          "nodo": {
           "id": "B3",
           "tipo": "AZAR",
           "supuesto": "SC-3",
           "etiqueta": "Uso: autoridades adoptan umbrales de alerta validados en sus protocolos",
           "hijos": [
            {
             "rama": "SC-3 se cumple",
             "nodo": {
              "id": "B4",
              "tipo": "AZAR",
              "supuesto": "SC-4",
              "etiqueta": "Custodia: al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo",
              "hijos": [
               {
                "rama": "SC-4 se cumple",
                "nodo": {
                 "id": "BT5",
                 "tipo": "TERMINAL",
                 "etiqueta": "Servicio continuado con receptor público único; protección contribuida con otros actores",
                 "nivel_tdc": "IMPACTO",
                 "resultado": "Valor no declarado (NO_CALCULABLE)"
                }
               },
               {
                "rama": "SC-4 falla",
                "nodo": {
                 "id": "BT4",
                 "tipo": "TERMINAL",
                 "etiqueta": "Orfandad después del mes 24: la red queda sin receptor que la opere",
                 "nivel_tdc": "RESULTADO_INTERMEDIO",
                 "resultado": "Valor no declarado (NO_CALCULABLE)"
                }
               }
              ]
             }
            },
            {
             "rama": "SC-3 falla",
             "nodo": {
              "id": "BT3",
              "tipo": "TERMINAL",
              "etiqueta": "Mediciones sin uso institucional con la inversión completa realizada",
              "nivel_tdc": "RESULTADO_INMEDIATO",
              "resultado": "Valor no declarado (NO_CALCULABLE)"
             }
            }
           ]
          }
         },
         {
          "rama": "SC-2 falla",
          "nodo": {
           "id": "BT2",
           "tipo": "TERMINAL",
           "etiqueta": "Red parcialmente inoperante con la inversión completa realizada",
           "nivel_tdc": "RESULTADO_INMEDIATO",
           "resultado": "Valor no declarado (NO_CALCULABLE)"
          }
         }
        ]
       }
      },
      {
       "rama": "SC-1 falla",
       "nodo": {
        "id": "BT1",
        "tipo": "TERMINAL",
        "etiqueta": "Inversión completa comprometida sin evidencia de reducción del error; red desplegada",
        "nivel_tdc": "PRODUCTO",
        "resultado": "Valor no declarado (NO_CALCULABLE)"
       }
      }
     ]
    }
   },
   {
    "rama": "R0 Sin intervención del proyecto",
    "nodo": {
     "id": "C0",
     "tipo": "TERMINAL",
     "etiqueta": "Se mantiene la línea base: sensores aislados sin corrección dinámica ni custodia",
     "nivel_tdc": "PRODUCTO",
     "resultado": "Valor no declarado (NO_CALCULABLE)"
    }
   }
  ]
 }
}
```

### L.2 JSON canónico del árbol A-TDC (ARBOL_4_SGR_CONV56_AIRE.json)

```
{
 "tipo": "TDC",
 "rol": "A-TDC",
 "nivel_detalle": "EJECUTIVA",
 "titulo": "A-TDC: teoría del cambio de la red de vigilancia con custodia distribuida",
 "naturaleza": "PROPUESTO",
 "fuente": "Sección 4.4 (S2), E3-P00 a E3-P21 y MDR v3.0",
 "pregunta": "¿Qué cadena causal lleva de los productos del proyecto a la protección de operarios y comunidades, y dónde termina la rendición de cuentas?",
 "descripcion": "Teoría del cambio de cuatro niveles y once resultados. Los productos y resultados inmediatos quedan bajo control del proyecto; los resultados intermedios y el impacto dependen de otros actores. Cuatro supuestos SC-1 a SC-4 rotulan las flechas críticas. La retroalimentación del uso institucional hacia los acuerdos de custodia representa el bucle de demanda. El panel declara dominio, arquitectura, efectos y riesgo de desajuste.",
 "niveles": [
  "Productos",
  "Resultados inmediatos",
  "Resultados intermedios",
  "Impacto"
 ],
 "techo_despues_de": 1,
 "nodos": [
  {
   "id": "P1",
   "nivel": 0,
   "texto": "Red de nodos con corrección local desplegada y repuestos disponibles"
  },
  {
   "id": "P2",
   "nivel": 0,
   "texto": "Referencia gravimétrica, protocolo de calibración y sorteo semanal en operación"
  },
  {
   "id": "P3",
   "nivel": 0,
   "texto": "Gemelo digital y tablero con umbrales de alerta propuestos"
  },
  {
   "id": "P4",
   "nivel": 0,
   "texto": "Acuerdos de custodia por tramos y portafolio de financiación constituidos"
  },
  {
   "id": "R1",
   "nivel": 1,
   "texto": "Error de medición reducido y verificable frente a la referencia"
  },
  {
   "id": "R2",
   "nivel": 1,
   "texto": "Datos suficientes: nodos activos y latencia dentro de lo especificado"
  },
  {
   "id": "R3",
   "nivel": 1,
   "texto": "Fórmula local del índice y umbrales validados con la autoridad de salud"
  },
  {
   "id": "I1",
   "nivel": 2,
   "texto": "Protocolos de gestión del riesgo y de salud incorporan las alertas"
  },
  {
   "id": "I2",
   "nivel": 2,
   "texto": "Alertas oportunas con falsas alarmas dentro del umbral acordado"
  },
  {
   "id": "I3",
   "nivel": 2,
   "texto": "Servicio operando con custodios después del mes 24"
  },
  {
   "id": "IM",
   "nivel": 3,
   "texto": "Operarios y comunidades de los sitios de remoción protegidos por alertas basadas en mediciones verificadas",
   "destacado": true
  }
 ],
 "enlaces": [
  {
   "de": "P3",
   "a": "R3",
   "supuesto": "SC-3"
  },
  {
   "de": "P1",
   "a": "R2",
   "supuesto": "SC-2"
  },
  {
   "de": "P1",
   "a": "R1",
   "supuesto": "SC-1"
  },
  {
   "de": "P2",
   "a": "R1",
   "supuesto": "SC-1"
  },
  {
   "de": "P4",
   "a": "I3",
   "supuesto": "SC-4"
  },
  {
   "de": "R3",
   "a": "I1",
   "supuesto": "SC-3"
  },
  {
   "de": "R1",
   "a": "I2"
  },
  {
   "de": "R2",
   "a": "I2"
  },
  {
   "de": "I1",
   "a": "IM",
   "supuesto": "SC-3"
  },
  {
   "de": "I2",
   "a": "IM"
  },
  {
   "de": "I3",
   "a": "IM",
   "supuesto": "SC-4"
  },
  {
   "de": "I1",
   "a": "P4"
  }
 ],
 "supuestos": [
  {
   "id": "SC-1",
   "si": "los nodos con corrección local se comparan por sorteo semanal con la lectura sin corrección dinámica y con una referencia gravimétrica",
   "entonces": "el error normalizado de los nodos corregidos resulta menor y la diferencia es detectable",
   "porque": "la humedad y el sesgo por tamaño de partícula explican parte del error (V03→V06 = 3 en S2) y la corrección local los compensa antes de la transmisión",
   "naturaleza": "SUPUESTO",
   "nodo_arbol": "A1 y B1"
  },
  {
   "id": "SC-2",
   "si": "los nodos conservan energía y enlace intermitente bajo maquinaria, polvo y humedad",
   "entonces": "el gemelo digital recibe datos suficientes para el mapa y el tablero",
   "porque": "la transmisión por eventos reduce el consumo, los nodos averiados se reponen y la maquinaria destruye nodos con peso 2 (V05→V09) que el plan de repuestos absorbe",
   "naturaleza": "SUPUESTO",
   "nodo_arbol": "A2 y B2"
  },
  {
   "id": "SC-3",
   "si": "la autoridad de salud valida una fórmula local del índice y los umbrales, y los puestos de mando los incorporan en sus protocolos",
   "entonces": "las alertas inducen acciones de protección y aumenta la población protegida",
   "porque": "una alerta sin portador de decisión no modifica la conducta; en S2 V11→V14 y V13→V14 tienen peso 2 y son hipótesis de influencia",
   "naturaleza": "SUPUESTO",
   "nodo_arbol": "A3 y B3"
  },
  {
   "id": "SC-4",
   "si": "al menos un custodio por componente demuestra capacidad de absorción antes de cada tramo de transferencia",
   "entonces": "el servicio continúa después del mes 24 sin receptor público único",
   "porque": "cada tramo exige presupuesto aprobado, personal designado y competencia jurídica documentada; sin ellos rige la cláusula de apertura",
   "naturaleza": "SUPUESTO",
   "nodo_arbol": "A4 y B4"
  }
 ],
 "enfoque": {
  "dominio": "COMPLICADO en la medición y COMPLEJO en la adopción y la custodia",
  "naturaleza_dominio": "INFERIDO",
  "arquitectura": "TdC anidada: ejecutiva y por componente",
  "efectos": [
   {
    "dimension": "Formulación",
    "efecto": "TdC ejecutiva de once nodos y cadena propia para medición, alertas y custodia"
   },
   {
    "dimension": "Presupuesto",
    "efecto": "Por componente con reasignación interna regulada y tramos condicionados"
   },
   {
    "dimension": "Indicadores",
    "efecto": "Por componente y agregados; metas comprometidas solo bajo el techo"
   },
   {
    "dimension": "Evaluación",
    "efecto": "Contraste con sorteo en la medición; contribución en adopción y custodia"
   },
   {
    "dimension": "Gobernanza",
    "efecto": "Comités por componente y comité integrador con revisión trimestral de supuestos"
   },
   {
    "dimension": "Sostenibilidad",
    "efecto": "Custodia distribuida por componente con cláusula de apertura"
   }
  ],
  "riesgo_desajuste": "Si la adopción es CLARA y no COMPLEJA, la revisión trimestral genera sobrecosto; si es CAOTICA, la coordinación por componente es lenta"
 }
}
```

### L.3 JSON canónico del árbol A-PROB (ARBOL_5_SGR_CONV56_AIRE.json)

```
{
 "tipo": "PROBLEMAS",
 "rol": "A-PROB",
 "titulo": "A-PROB: árbol de problemas de la vigilancia de material particulado en sitios de remoción de escombros",
 "naturaleza": "PROPUESTO",
 "fuente": "Sección 4.4 (S2), 4.4-MDR y E3-P00 a E3-P21; relaciones con estatuto HIE",
 "pregunta": "¿Qué estados problemáticos, causas y efectos sustentan el error de medición sin verificar como problema central?",
 "descripcion": "Árbol de problemas con diez nodos y diez relaciones en cinco niveles. El problema central es el error de medición sin verificar frente a una referencia (V06). Las causas directas son humedad, PM10, PM2,5 y frecuencia de calibración. La causa indirecta es la remoción de escombros. Los efectos son un índice sin fórmula local, falsas alarmas sin medir, baja adopción institucional y personas sin protección efectiva. Todas las relaciones son hipótesis de influencia estructural sin efecto estimado.",
 "niveles": [
  "Efectos indirectos",
  "Efectos directos",
  "Problema central",
  "Causas directas",
  "Causas indirectas"
 ],
 "nodos": [
  {
   "id": "V14",
   "nivel": 0,
   "texto": "Personas sin protección efectiva por alertas confiables (V14)"
  },
  {
   "id": "V15",
   "nivel": 0,
   "texto": "Baja adopción institucional del tablero y de las alertas (V15)"
  },
  {
   "id": "V11",
   "nivel": 1,
   "texto": "Índice AQHI sin fórmula local validada y con error de entrada (V11)"
  },
  {
   "id": "V12",
   "nivel": 1,
   "texto": "Tasa de falsas alarmas sin medir (V12)"
  },
  {
   "id": "V06",
   "nivel": 2,
   "texto": "Error de medición de PM2,5 y PM10 sin verificar frente a una referencia (V06)",
   "destacado": true
  },
  {
   "id": "V03",
   "nivel": 3,
   "texto": "Humedad relativa alta en los sitios de remoción (V03)"
  },
  {
   "id": "V02",
   "nivel": 3,
   "texto": "Concentración de PM10 con fracción gruesa (V02)"
  },
  {
   "id": "V01",
   "nivel": 3,
   "texto": "Concentración de PM2,5 (V01)"
  },
  {
   "id": "V07",
   "nivel": 3,
   "texto": "Frecuencia de calibración de los nodos baja o nula (V07)"
  },
  {
   "id": "V05",
   "nivel": 4,
   "texto": "Remoción de escombros en curso (V05)"
  }
 ],
 "enlaces": [
  {
   "de": "V05",
   "a": "V02"
  },
  {
   "de": "V05",
   "a": "V01"
  },
  {
   "de": "V03",
   "a": "V06"
  },
  {
   "de": "V02",
   "a": "V06"
  },
  {
   "de": "V01",
   "a": "V06"
  },
  {
   "de": "V07",
   "a": "V06"
  },
  {
   "de": "V06",
   "a": "V11"
  },
  {
   "de": "V06",
   "a": "V12"
  },
  {
   "de": "V11",
   "a": "V14"
  },
  {
   "de": "V12",
   "a": "V15"
  }
 ]
}
```

## Anexo M. Inventario de archivos de la sección 4

El manifiesto del respaldo CP_20261013_E4_4_5_01 registra 107 archivos con su huella SHA-256 calculada sobre los bytes. El manifiesto no incluye su propio hash. El método declarado es SHA256_EJECUTADO_SOBRE_BYTES. La {T:k01} permite verificar que los archivos fuente del repositorio coinciden con los que originan las secciones F4.3 a F4.5.

:::TABLA k01 | Inventario de archivos del respaldo con huella SHA-256
| Archivo | Clase | Bytes | SHA-256 |
| --- | --- | --- | --- |
| INFORMES/00_INFORME_DE_REVISION_E3-P00.md | ENTREGADO | 37998 | 464e140dcff3bacb9943636646445b43e9ec838f203449ab003ef267fddd4ee2 |
| INFORMES/01_ADMISION_TV1_GATE0_Y_ALCANCE.md | ENTREGADO | 12098 | 3ed7940d51c80a6bc857ec5e517675c50c3a499cf0aaac1e7f07e2ed02113ad4 |
| INFORMES/REGISTRO_ENTREGAS.json | RESULTADO | 9679 | 89bc1974874324a010003029c4f30b13a15b7e460b691c6c9de50e085a062992 |
| INFORMES/REGISTRO_ENTREGAS.md | ENTREGADO | 4368 | 52efc45cfb4534a5058e25c1a201ed7337caedae84eb1926f7a71530d34d56e5 |
| README.md | ENTREGADO | 4273 | 7103b1a7e3345fb8d78a4a6c9e5e76ca80e3d145a438b6a9a6ec7467105f4ebd |
| SECCION_4_3/DAG_E1.alt.md | GRAFICO | 471 | 19ca54cb6e264dfa7da132c4c516707406b7a9fd00d32cad6f924a0d16fa75c0 |
| SECCION_4_3/DAG_E1.svg | GRAFICO | 9014 | dc705481b850e7e60ca11afcb4349115c056be25c3648c0201a2f51221b8938c |
| SECCION_4_3/SECCION_4_3_SGR_CONV56_AIRE.md | ENTREGADO | 18116 | 819ac18380f5957060adabdc7b04ffbcc44b835f1d6d00114035792307417ab4 |
| SECCION_4_4/ANALISIS_COMPLEMENTARIO.json | RESULTADO | 32414 | ca89bb46a81c953a99bd2f2dec6d6ca75a0b25664c8f08e2bbb6ca77bc908076 |
| SECCION_4_4/CHECKPOINT_MOTOR.json | RESULTADO | 900 | f4e2e51022d3f9618f7aa6ceb3d3eb39528863f7343edc7d9d4fd2e61f089458 |
| SECCION_4_4/ENTRADA_MOTOR.json | RESULTADO | 428502 | 959c1fa7af9abbde9cd84624ce92e2d48aa628b813595043f8aa669f0a5d29c1 |
| SECCION_4_4/FICHAS_PARITARIAS.csv | FICHA | 151537 | aff75d88fd8f0a94a4e1c8c5cebbb5eee917571e61100e68711dfd255d909c76 |
| SECCION_4_4/FICHAS_PARITARIAS.json | FICHA | 410996 | 68aff6b7443a52caf0847ac1fe45df66d0c30e5e5ef65e01c22b11d41d9fcd83 |
| SECCION_4_4/MICMAC_S0_HISTORICO_CONDICIONADO.svg | GRAFICO | 2268 | 48d61aef71e348e4f1b1ce92b05e891b54325c278d3a7ac83ef1fcb51770c201 |
| SECCION_4_4/MICMAC_S1_PREVIO_DOC.svg | GRAFICO | 3761 | e5d581d8a4e42171280fa57edd7e784bdf128cbc7e1a545861c19345ca21d1c2 |
| SECCION_4_4/MICMAC_S3_ENVOLVENTE_ADMISIBLE_BAJA.svg | GRAFICO | 3159 | 0ec7de5bde98992b7a44590edba7941a8e633f50b0c912c40b7673784f7064de |
| SECCION_4_4/MICMAC_S4_ENVOLVENTE_ADMISIBLE_ALTA.svg | GRAFICO | 3793 | 10c13e62e9fffebde79e07c9b25a5cf154551a7d98693a9925c90817582f6d4c |
| SECCION_4_4/MICMAC_S_TRABAJO_PROPUESTO.svg | GRAFICO | 3774 | 17b2ab7eb18f664ec27eaa7cb03421c54349273d03cd3206fc364ae1237af2b3 |
| SECCION_4_4/MID_FORMAL.csv | MATRIZ | 923 | 76995024e4e89975d4df2b378c0b683e6090ad6b81e0e43468a79948c66b8232 |
| SECCION_4_4/MID_S0_HISTORICO_CONDICIONADO.csv | MATRIZ | 677 | 6d5645b4c7b744890c9a114128547cad0c8614f650319570ad9d48c32ca4c3ae |
| SECCION_4_4/MID_S1_PREVIO_DOC.csv | MATRIZ | 677 | 19c90418a21154004a6053db3b90a87ae7f4ee60e7748b64fbc6f57a0d3ce3b8 |
| SECCION_4_4/MID_S3_ENVOLVENTE_ADMISIBLE_BAJA.csv | MATRIZ | 676 | 7282cd08a256021d99e07ea81c1c613b73a9543eb8788a522a9c21d66569e6dd |
| SECCION_4_4/MID_S4_ENVOLVENTE_ADMISIBLE_ALTA.csv | MATRIZ | 687 | 593158f040bf81361bf3adab964370207ce593820866c0b9f7a4a64ef487385a |
| SECCION_4_4/MID_S_TRABAJO_PROPUESTO.csv | MATRIZ | 678 | 4527524414ed9404c4e36f3e357568ab13bdb74cb5b8dddc5479b31d13df2a89 |
| SECCION_4_4/PLAN_PARITARIO.csv | MATRIZ | 2873 | 882db0ada826d41f73d2826294929f99d4a859c0672311a6e8787a565f41d11d |
| SECCION_4_4/REGISTRO_DIRECCIONES.csv | MATRIZ | 9406 | 068fc3b505c27ca078bb4892ae99f03dcc86763e126b18ff711e9ba5fbe963ef |
| SECCION_4_4/RESULTADOS.json | RESULTADO | 884791 | 452990c1f3ef37bec031172afb9a88bc991e21ef15f23b39734e0d1caad9ec19 |
| SECCION_4_4/REVISION_SOLAPAMIENTO.csv | MATRIZ | 13678 | d0e7b9ac6ab3eed38b4aaf7338373111bcf5c33507c3452f61e845e60460ed59 |
| SECCION_4_4/RUTAS_Y_CICLOS.json | RESULTADO | 24835 | 5f20fd459ab12a19947aadb8f126c5d8253561c1ed5cc431897f88e0a0350d91 |
| SECCION_4_4/SECCION_4_4_SALIDA_CRUDA_DEL_MOTOR.md | ENTREGADO | 25224 | 96b93455593c0e1b0bf8e2e4e4465eaf0b347fc72720a943a78bfd8b5aa38ffb |
| SECCION_4_4/SECCION_4_4_SGR_CONV56_AIRE.md | ENTREGADO | 262374 | 623ae50cf0472b7bf6b4a38283ad733713d1b85dd0acbad39fd477e6eac516ea |
| SECCION_4_4/SECCION_4_4_orquestador.json | RESULTADO | 527 | 6161364f6fb4a81537b46b49e3b0a653f3b6611b2ce7c11ccc0179e3cf2d2785 |
| SECCION_4_4/SECCION_4_4_scope_guard.json | RESULTADO | 527 | 6161364f6fb4a81537b46b49e3b0a653f3b6611b2ce7c11ccc0179e3cf2d2785 |
| SECCION_4_4/SENSIBILIDAD_ORDINAL.json | RESULTADO | 209573 | 7040991d2a3db239623e1f2bb8e3021e6bd9cf4da0f9d7fe814fac296bc39409 |
| SECCION_4_4/VESTER_S0_HISTORICO_CONDICIONADO.svg | GRAFICO | 3500 | 6f9498af263cc33e40afb62e3201f6645693a9ac7ce5b13798abfc4ec3b108ad |
| SECCION_4_4/VESTER_S1_PREVIO_DOC.svg | GRAFICO | 3489 | c090fd603f800cb0f6a2bb6bb5ddbd73e780976147b99d6d4283b48f6ac3e80e |
| SECCION_4_4/VESTER_S3_ENVOLVENTE_ADMISIBLE_BAJA.svg | GRAFICO | 3394 | 033a24d182b53a9a392250bec425f01e636867ffebe2979198b3dc0adbb961b3 |
| SECCION_4_4/VESTER_S4_ENVOLVENTE_ADMISIBLE_ALTA.svg | GRAFICO | 3779 | 9444a9ab6dcc78bf75fedea600d2a58978dcfb644b0d0962f2ceae8f2c85bf14 |
| SECCION_4_4/VESTER_S_TRABAJO_PROPUESTO.svg | GRAFICO | 3738 | c67821e03cda9f5b63036e07b2072d66c633c6c1cee07d76eca8993f2b5119d4 |
| SECCION_4_4/potencias/S0_HISTORICO_CONDICIONADO_A01.csv | RESULTADO | 677 | 6d5645b4c7b744890c9a114128547cad0c8614f650319570ad9d48c32ca4c3ae |
| SECCION_4_4/potencias/S0_HISTORICO_CONDICIONADO_A02.csv | RESULTADO | 696 | 4e77ae546a20f68a68f1013c7c6e3e20a7d83281bcb25ce0516670dfcd009328 |
| SECCION_4_4/potencias/S0_HISTORICO_CONDICIONADO_A03.csv | RESULTADO | 721 | 02388ad8ef4ff7d21ea6274f37b7bc94dc1c1e1fc1fc9c8f24fdca11ade9698d |
| SECCION_4_4/potencias/S0_HISTORICO_CONDICIONADO_A04.csv | RESULTADO | 724 | ce3f3bca8de259d6e3243ddc53a6058246d30d07df33d2bbe9820605232aaf48 |
| SECCION_4_4/potencias/S0_HISTORICO_CONDICIONADO_A05.csv | RESULTADO | 705 | c2ab163f1c94a11b974f4a6623aaca7a7c7ea478670f1dd8a399c11990c5dcf6 |
| SECCION_4_4/potencias/S0_HISTORICO_CONDICIONADO_A06.csv | RESULTADO | 683 | 5144e36bf9761694a3b2ad600e42b796006b9f3f307d35cbcd069f1ea69da1fa |
| SECCION_4_4/potencias/S0_HISTORICO_CONDICIONADO_A07.csv | RESULTADO | 675 | c0519fa1a1acc69b28eae2b03f796f5495681167a345319c2940f777c90202f5 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A01.csv | RESULTADO | 677 | 19c90418a21154004a6053db3b90a87ae7f4ee60e7748b64fbc6f57a0d3ce3b8 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A02.csv | RESULTADO | 702 | b2762c4a8e0f9a25afff5de9c88307d9792c91f3000bfb19dfe99c6b743f4cc0 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A03.csv | RESULTADO | 754 | bc7de9aaa81b4b42790eced547689723c7cf843a7d371e395b76f53865a584b2 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A04.csv | RESULTADO | 829 | 73c7f275a22394ea735ad0dfb8c3e0687172395ec0ee033af9a911a99114bd4d |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A05.csv | RESULTADO | 939 | 63844b154e48ed58b1ad97f47bba6912eb2c435c8873a2f5e233b0c776518f30 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A06.csv | RESULTADO | 1043 | db0b67cbf3f7e3b17db230d22a6263aeb44da2264671b3ff655c3a20b06de5a7 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A07.csv | RESULTADO | 1156 | a9a4d4b2d6fda87249a6280b2e73cfcf28ea1783d9728bba0a913fc3d1f290a4 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A08.csv | RESULTADO | 1279 | a1e9dd055d541be08fc16f486946efbfa27f6973cd10797b2d747ff8bbf54303 |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A09.csv | RESULTADO | 1383 | fd7c6cd9daf930ed138bf0c9f17bd1952c21ecb46d56148add7238e9d3f681bd |
| SECCION_4_4/potencias/S1_PREVIO_DOC_A10.csv | RESULTADO | 1518 | aa83c20856a8b10abeb5331982ea4d7618854ccbe380b75827e52e2d027c7f21 |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A01.csv | RESULTADO | 676 | 7282cd08a256021d99e07ea81c1c613b73a9543eb8788a522a9c21d66569e6dd |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A02.csv | RESULTADO | 679 | ba33656876892a3c8af7adc3620d3e46441536a6073535b80a96e6edca33d8bf |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A03.csv | RESULTADO | 688 | 0cde5796daef9ae3a6167b74a9434695062abe33d79272d671398858b4a0cfbc |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A04.csv | RESULTADO | 690 | 9fb7e35efd11ec8c150d9625253c9e1b77596cbb9d65d8ed9976c006d79bd4ed |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A05.csv | RESULTADO | 690 | b9acf9bffae1fa0cdd154df21b4bd4ac31dc9fcce179e2e7651408b7d818e0e8 |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A06.csv | RESULTADO | 691 | 9eeecd8f62190a191f20189bccfe003b3c3a90b55fbce67110b169bdc4db9989 |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A07.csv | RESULTADO | 690 | b9acf9bffae1fa0cdd154df21b4bd4ac31dc9fcce179e2e7651408b7d818e0e8 |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A08.csv | RESULTADO | 691 | 9eeecd8f62190a191f20189bccfe003b3c3a90b55fbce67110b169bdc4db9989 |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A09.csv | RESULTADO | 690 | b9acf9bffae1fa0cdd154df21b4bd4ac31dc9fcce179e2e7651408b7d818e0e8 |
| SECCION_4_4/potencias/S3_ENVOLVENTE_ADMISIBLE_BAJA_A10.csv | RESULTADO | 691 | 9eeecd8f62190a191f20189bccfe003b3c3a90b55fbce67110b169bdc4db9989 |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A01.csv | RESULTADO | 687 | 593158f040bf81361bf3adab964370207ce593820866c0b9f7a4a64ef487385a |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A02.csv | RESULTADO | 732 | ecd4e48835279e0c12e4ecc3c5a6c64df58120b479aa01eb7aa8834aac946890 |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A03.csv | RESULTADO | 879 | feb37c669e4df60a66f778c6122cf41887d0d2ee5d6a63c906355142e3747142 |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A04.csv | RESULTADO | 1074 | fb86bb833a1149086b85dac049ca93de36e8092dced8bb40c879e0c4c8bb43e1 |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A05.csv | RESULTADO | 1286 | cad1f114f1d9ae3459ce0c9dfbd0a9fc5b6d810927f3ef5e8ddbfd2c8cc5c272 |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A06.csv | RESULTADO | 1489 | a33352dc5a7f0dada3664c87a1436b91cfff4c0e8baf8a335d2ab0a1808d5d1d |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A07.csv | RESULTADO | 1657 | ae80549323f340524a7cebfd6c5ececc52c34783b061bee9d2ada18b35cccba4 |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A08.csv | RESULTADO | 1833 | 2c5eb3e2671e0d7289482fea7f512f293a25ee6e7d0a87b8ae117e81eab0ade3 |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A09.csv | RESULTADO | 2014 | aa8332c28b3847ec539ad6b7f67ae42f7984c1b04f61eff243decc1ed814a10e |
| SECCION_4_4/potencias/S4_ENVOLVENTE_ADMISIBLE_ALTA_A10.csv | RESULTADO | 2205 | c4f8be6c32088634054286079d896787b0520362b03ff0b18d4fefb75206824b |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A01.csv | RESULTADO | 678 | 4527524414ed9404c4e36f3e357568ab13bdb74cb5b8dddc5479b31d13df2a89 |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A02.csv | RESULTADO | 706 | bb99bf8d0b3b77d550c7d78bddd8b75362a814a1c13d84e452458ee08c685a14 |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A03.csv | RESULTADO | 794 | f2f0161cd375030e95d3ad6a9a45f78ba15d53935bb2155be8bff31b88e3eb26 |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A04.csv | RESULTADO | 918 | 29cd4e14dc26bb1fde8c68beb3127218ea89280359454896ceb263a0776d2f1b |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A05.csv | RESULTADO | 1068 | ab60c9efd45ab2d8357f30dc87d94ea9394335827c1e42ac557f87d05379c06d |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A06.csv | RESULTADO | 1241 | 6e7d8416374a27ca3ea670dd188a676379453358817b656d48ddd48d528569a5 |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A07.csv | RESULTADO | 1395 | 31de5205d6de0e3eec9c283fa794fee3033dd28163cecd504c4828e55bd77442 |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A08.csv | RESULTADO | 1524 | ce66001f639fdfe829852b517356de76680d9bb315932e9312885576ca445ca5 |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A09.csv | RESULTADO | 1701 | a8adabfc46de968d61ff67cd42cc0161342dfe341703bca0f677fe60345355fa |
| SECCION_4_4/potencias/S_TRABAJO_PROPUESTO_A10.csv | RESULTADO | 1861 | 6ff11654fae4fc88dd3b51ebaa96f1815ecb230a489be7b8c9f256d6c82b4dc5 |
| SECCION_4_4/xlsx/Vester_MICMAC_S0_historico.xlsx | MATRIZ | 327092 | f0649acf1e2c557117207aefb3435aad49ca9a8da050ea3f4af67af0865f9123 |
| SECCION_4_4/xlsx/Vester_MICMAC_S1_previo_doc.xlsx | MATRIZ | 327106 | adb24f0dd6551abd8cff2684aa252f5919ebe8f997b2221feb84589c73bf88ad |
| SECCION_4_4/xlsx/Vester_MICMAC_S2_trabajo_propuesto.xlsx | MATRIZ | 327130 | 568b961d032caf6d62c4969db89eca0bc3da1eb2489cee6de4140bbd2608e663 |
| SECCION_4_4_MDR/ARBOL_1_SGR_CONV56_AIRE.alt.md | GRAFICO | 3488 | fe72e08b63a603461224d9b172079cb6ac44a50817aad714f3a9ee44a2d6ec84 |
| SECCION_4_4_MDR/ARBOL_1_SGR_CONV56_AIRE.json | RESULTADO | 7779 | 56bbfcf900417513e0affb3f63beb78501c032da4b77cabbcac2fa615360aa5c |
| SECCION_4_4_MDR/ARBOL_1_SGR_CONV56_AIRE.svg | GRAFICO | 26353 | 9bf2357debcd55c9fefb3ff8730cebe43c14fd61e318de94236e36054fe0df9f |
| SECCION_4_4_MDR/ARBOL_4_SGR_CONV56_AIRE.alt.md | GRAFICO | 3602 | b56f43df8133e428c4e7e67bbd9462ad9fee6545e9425163843e49bf2af707e0 |
| SECCION_4_4_MDR/ARBOL_4_SGR_CONV56_AIRE.json | RESULTADO | 6102 | 35781fb46115dcf27addcb35cc47da4cfa5e9f6e748c275d3ebccc9eff045211 |
| SECCION_4_4_MDR/ARBOL_4_SGR_CONV56_AIRE.svg | GRAFICO | 20727 | 0de6c7603bbbad0f11fa28d4866bea99b399a78c18ef02b8adcb942b31691636 |
| SECCION_4_4_MDR/CONTROL_MDR_SGR_CONV56_AIRE.json | RESULTADO | 13294 | ce3ba55f023d670d838a9c890b8059ef4266229aeffa889784d1f8e473586352 |
| SECCION_4_4_MDR/EXPEDIENTE_MDR_SGR_CONV56_AIRE.json | RESULTADO | 65840 | e4424b08473d69186aaea9f6d1de88e0b0b254acbd5f4b182641fff83f011808 |
| SECCION_4_4_MDR/EXPEDIENTE_MDR_SGR_CONV56_AIRE.md | ENTREGADO | 34379 | ab1fb035d5862c602c7944d88872c5b8547fdbca57df829a014bb67ad00a0fe2 |
| SECCION_4_4_MDR/REGISTRO_CONTRASTE_ARBOL_SGR_CONV56_AIRE.csv | MATRIZ | 17171 | 8789733645dbaeb5462b053a197497372efa9d5c08969e056986ea5575f895c4 |
| SECCION_4_4_MDR/SECCION_4_4_MDR_SGR_CONV56_AIRE.md | ENTREGADO | 116668 | 534e3535d16e81318c0918ad547dbb8a35ccb9e7d6d5a3052e570cf502bdf5ad |
| SECCION_4_5/ARBOL_5_SGR_CONV56_AIRE.alt.md | GRAFICO | 1666 | 024a4dd59dbe0c867226b15f9b03bd2e089cee8c9ed8a05277b31ffab4060ef0 |
| SECCION_4_5/ARBOL_5_SGR_CONV56_AIRE.json | RESULTADO | 2595 | b2d8a131eb0591fae251894d1101594f757ba302409c3bb331757e4137c6641b |
| SECCION_4_5/ARBOL_5_SGR_CONV56_AIRE.svg | GRAFICO | 10403 | eb4db09aaf836283cde81ebeef9f6d7e3887e5a90a618e380192e23a46e847e1 |
| SECCION_4_5/SECCION_4_5_SGR_CONV56_AIRE.md | ENTREGADO | 14620 | a34185340e5924e71e812fe96eb9ba0ac86b5ec5ce10fbdc9922a23a84e580b3 |
| ESTADO.json | ESTADO | 55993 | 051e300781ebd41b24a11fd4fce3327319eaf26c7770cb1b1b98b4a6e5368525 |
| CAPSULA.json | INDICE_DE_REANUDACION | 13418 | 7a61d3af1cb4b795e479df33f4fe07c5a1d8e0934075d05062fa17885e92e98e |
| LEEME_REANUDAR.txt | INSTRUCCION | 458 | 6d831509cb6f8bfe93dbfd2770d7e9e2135518ef8955588436639034946635d5 |
:::NOTA *Nota.* Elaboración propia con MANIFIESTO.json del respaldo RESPALDO_SGR_CONV56_AIRE_CP_20261013_E4_4_5_01.zip.

