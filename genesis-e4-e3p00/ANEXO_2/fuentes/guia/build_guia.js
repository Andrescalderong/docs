// Guía para explicar el proyecto (Word). Uso: node build_guia.js SALIDA.docx RUTA_FIGURA.png
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  AlignmentType, LevelFormat, Header, Footer, PageNumber, PageBreak, VerticalAlign,
} = require("docx");

const [, , OUT, FIG] = process.argv;
const T = "2A3439", AZUL = "6699CC", MEDIO = "9EB9D4", CLARO = "B9D9EB", GRIS = "F5F5F5";
const FONT = "Arial";
const W = 10080; // ancho útil en DXA (Carta con márgenes de 0,75 in)

const run = (text, o = {}) => new TextRun({ text, font: FONT, color: T, size: o.size || 21, bold: o.bold, italics: o.italics });
const para = (children, o = {}) => new Paragraph({
  children: Array.isArray(children) ? children : [run(children, o)],
  spacing: { before: o.before ?? 0, after: o.after ?? 100, line: o.line ?? 276 },
  alignment: o.align, keepNext: o.keepNext, keepLines: o.keepLines, pageBreakBefore: o.pageBreakBefore,
});
const h1 = (t) => new Paragraph({ children: [run(t, { size: 40, bold: true })], spacing: { before: 0, after: 40 }, keepNext: true });
const sub = (t) => new Paragraph({ children: [run(t, { size: 26 })], spacing: { before: 0, after: 80 }, keepNext: true });
const h2 = (t, pb = false) => new Paragraph({
  children: [run(t, { size: 26, bold: true })], keepNext: true, pageBreakBefore: pb && t === "Preguntas frecuentes",
  spacing: { before: 200, after: 100 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: AZUL, space: 2 } },
});
const bullet = (t, o = {}) => new Paragraph({
  numbering: { reference: "viñetas", level: 0 }, spacing: { after: 70, line: 270 }, keepLines: true,
  children: Array.isArray(t) ? t : [run(t, o)],
});
const num = (ref, kids) => new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { after: 90, line: 270 }, keepLines: true, children: kids });

const thin = { style: BorderStyle.SINGLE, size: 4, color: MEDIO };
const borders = { top: thin, bottom: thin, left: thin, right: thin };
const cell = (kids, width, o = {}) => new TableCell({
  width: { size: width, type: WidthType.DXA }, borders, verticalAlign: VerticalAlign.TOP,
  shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
  margins: { top: 70, bottom: 70, left: 100, right: 100 },
  children: (Array.isArray(kids) ? kids : [kids]).map((k) => (typeof k === "string" ? para(k, { after: 40, size: o.size || 19, bold: o.bold, line: 252 }) : k)),
});
const table = (cols, head, rows, o = {}) => new Table({
  width: { size: cols.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: cols,
  rows: [
    new TableRow({ tableHeader: true, cantSplit: true, children: head.map((h, i) => cell(h, cols[i], { fill: CLARO, bold: true, size: 19 })) }),
    ...rows.map((r, k) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, cols[i], { fill: k % 2 ? GRIS : undefined, bold: i === 0 && o.boldFirst, size: 19 })) })),
  ],
});

// ---------------------------------------------------------------- contenido
const fraseCaja = new Table({
  width: { size: W, type: WidthType.DXA }, columnWidths: [W],
  rows: [new TableRow({ children: [new TableCell({
    width: { size: W, type: WidthType.DXA },
    shading: { fill: GRIS, type: ShadingType.CLEAR, color: "auto" },
    borders: { top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
      right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, left: { style: BorderStyle.SINGLE, size: 36, color: AZUL } },
    margins: { top: 120, bottom: 120, left: 200, right: 160 },
    children: [
      para([run("En una frase", { bold: true, size: 22 })], { after: 60 }),
      para("Después del terremoto del 10 de agosto se demuelen edificios y se retiran escombros en los municipios afectados. Ese trabajo levanta polvo que respiran los operarios y los vecinos, y los comités de gestión del riesgo no tienen hoy cómo medirlo con confianza ni anticiparlo. El proyecto instala sensores corregidos en esos sitios, avisa a los comités cuándo actuar y calcula, antes de cada demolición, cuánto polvo saldrá y hacia dónde irá.", { size: 22, after: 0, line: 290 }),
    ],
  })] })],
});

const FIG_W = 536, FIG_H = Math.round(536 * 1943 / 2200);
const figura = new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 120, after: 40 }, keepNext: true,
  children: [new ImageRun({ type: "png", data: fs.readFileSync(FIG), transformation: { width: FIG_W, height: FIG_H },
    altText: { title: "Recorrido del terremoto a la decisión", description: "Cadena de cuatro eslabones, lo que falta, tres acciones del proyecto y el resultado al mes 24", name: "figura_recorrido" } })],
});

const etapas = table([1500, 4800, 3780], ["Etapa", "Qué ocurre", "Qué ve el comité"], [
  ["Meses 1 a 12", "Se eligen los sitios, se instalan los primeros 30 sensores y 3 antenas receptoras, y se comparan con el equipo de referencia para corregirlos. Se diseña el laboratorio y se compra su equipo.",
   "Primeros datos corregidos y primeras pruebas del tablero. Al mes 12 hay una revisión: si los datos son confiables y el comité usa el tablero, se compra el siguiente lote."],
  ["Meses 13 a 17", "Se instalan 40 sensores más y 4 antenas. Se miden las primeras demoliciones reales y se calibra el modelo del laboratorio.",
   "Alertas con el protocolo acordado. Al mes 17 hay una segunda revisión."],
  ["Meses 18 a 24", "Se instalan los últimos 30 sensores y 3 antenas, se hace un ensayo independiente y el laboratorio entrega evaluaciones previas de demolición.",
   "Decisiones documentadas con el tablero y evaluaciones previas antes de demoler. Al mes 24 se cierra y los equipos pasan a custodia."],
], { boldFirst: true });

const integrantes = table([1700, 2900, 2700, 2780], ["Integrante", "Qué hace", "Qué recibe", "Qué se le pide ahora"], [
  ["Universidad (entidad proponente)", "Lidera la ciencia y la administración, aloja y valida el laboratorio y forma a 9 personas.",
   "Documentos de investigación, datos propios, y un laboratorio y un modelo propios.", "Carta de aval, certificado de existencia y representación legal, y contrapartida en especie ($ 1.244 millones)."],
  ["Municipio aliado", "Facilita el acceso a los sitios y a las demoliciones, su comité usa el tablero y decide, y custodia la red en su territorio.",
   "Tablero y protocolo de alerta, personas formadas, evaluación previa de demoliciones y los equipos en custodia.",
   "Los tres soportes de la emergencia (acto de calamidad, reporte de afectación y cronograma de demoliciones), aval, partida para operar la red y contrapartida en especie ($ 120 millones)."],
  ["Actor del SNCTI", "Valida el método comparando los monitores, forma custodios y custodia los datos con criterio científico.",
   "Coautoría de documentos, capacidad en medición de partículas y acceso a las series de datos.", "Resolución de reconocimiento vigente, aval y valor certificado de su aporte."],
  ["Empresa tecnológica", "Instala y mantiene los sensores, la plataforma y la nube, e integra el modelo del laboratorio.",
   "Validación independiente de su tecnología, datos de campo y derechos según el acuerdo de propiedad intelectual.", "Certificado de existencia, aval, cotizaciones y contrapartida ($ 210 millones en efectivo y $ 800 millones en especie)."],
  ["Comités de gestión del riesgo (usuarios)", "Co-diseñan el protocolo, usan el tablero y deciden.",
   "Alertas con datos de error conocido y una estimación previa del polvo de cada demolición.", "Asistir a los talleres y firmar las actas de uso."],
], { boldFirst: true });

const glosario = table([3000, 7080], ["Evite", "Diga en su lugar"], [
  ["Nodos y gateways", "Sensores y antenas receptoras."],
  ["PM2,5 y PM10", "Polvo fino y polvo grueso, el que entra a los pulmones."],
  ["Calibración y corrección", "Ajustar los sensores con un equipo de referencia para que no se desvíen."],
  ["Gemelo digital", "Un modelo en computador que calcula el polvo esperado."],
  ["Compuerta", "Revisión de resultados antes de comprar el siguiente lote."],
  ["TRL", "Nivel de madurez de la tecnología, de prototipo a sistema probado."],
  ["Custodia", "Entrega formal de los equipos a quien los opera después del proyecto."],
]);

const preguntas = table([3300, 6780], ["Pregunta", "Respuesta corta"], [
  ["¿Es un proyecto de salud?", "No. No mide enfermedades ni promete efectos en la salud. Mide polvo y mejora decisiones: parar, humedecer, desviar o avisar."],
  ["¿Qué tiene que ver con el terremoto?", "El polvo que se mide es el de las demoliciones y de la remoción de escombros que dejó el terremoto, en los sitios de trabajo. Sin terremoto no habría esa actividad masiva."],
  ["¿Y si la remoción termina antes de que el proyecto avance?", "La reconstrucción también demuele y levanta polvo. El laboratorio y el protocolo sirven para demoliciones futuras y la red queda en custodia. Por eso se pide a cada municipio su cronograma de demoliciones y remoción."],
  ["¿Y si el modelo del laboratorio falla?", "Se informa el desempeño real y se limita su uso. El resultado apoya la decisión del comité y nunca autoriza ni prohíbe una demolición."],
  ["¿Quién se queda con los equipos?", "Al mes 24 pasan a custodios designados por convenio. La titularidad se define en el convenio."],
  ["¿Por qué sensores y no estaciones oficiales?", "Una estación fija cuesta más de siete veces por punto de medición y no se puede mover. Los sensores cubren más sitios si se corrigen con los equipos de referencia."],
]);

const semana = table([2300, 5600, 2180], ["Fecha", "Qué se necesita", "Quién"], [
  ["Sábado 24 y domingo 25", "Reunión corta con cada integrante, con el guion de esta guía. Pedir los soportes y las cotizaciones.", "Universidad"],
  ["Lunes 26", "Los tres soportes de la emergencia, los datos pendientes del documento, las cotizaciones y el valor certificado del aporte del actor del SNCTI.", "Municipio aliado y demás integrantes"],
  ["Martes 27", "Firma de la carta de aval (Anexo 1) y de los certificados de los numerales 10.18 y 10.19. Versión 2 del Anexo 2 con los datos reales.", "Los cuatro representantes legales; universidad"],
  ["Miércoles 28 y jueves 29", "Congelación del Anexo 2 y del Anexo A, revisión cruzada, PDF de menos de 3 MB y prueba de carga.", "Universidad"],
  ["Viernes 30", "Radicación anticipada en el SIGP. El cierre oficial es el martes 3 de noviembre a las 4:00 p. m.", "Universidad"],
], { boldFirst: true });

const children = [
  h1("Cómo explicar el proyecto"),
  sub("Del terremoto del 10 de agosto a la decisión del comité de gestión del riesgo"),
  para([run("Guía de trabajo para la reunión con los integrantes de la alianza. No sustituye al Anexo 2: lo vuelve comprensible.", { italics: true, size: 19 })], { after: 140 }),
  fraseCaja,
  figura,
  para([run("Figura 1. ", { bold: true, size: 18 }), run("Del terremoto del 10 de agosto a la decisión del comité. Elaboración propia con la formulación del proyecto.", { size: 18, italics: true })], { align: AlignmentType.CENTER, after: 100 }),
  h2("Por qué esto responde a la emergencia"),
  bullet("Sin el terremoto no habría esta demolición ni esta remoción masiva de escombros en los centros urbanos."),
  bullet("Sin ellas no habría este polvo en sitios donde los comités no tienen cómo medirlo."),
  bullet("El proyecto no repara edificios. Atiende el riesgo nuevo que dejó el terremoto en la reconstrucción."),
  para("La convocatoria exige una relación directa y específica con la emergencia, y estar en un departamento afectado no basta. Por eso el municipio aliado debe aportar tres soportes: el acto de calamidad pública, el reporte de afectación de las edificaciones y el cronograma de demoliciones y remoción.", { before: 60 }),

  h2("Qué se hace durante los 24 meses", true),
  etapas,
  h2("Qué hace y qué recibe cada integrante"),
  integrantes,

  h2("Cómo explicarlo en cinco minutos", true),
  num("pasos", [run("Pregunte primero (30 segundos). ", { bold: true }), run("¿Qué decide hoy su comité cuando una demolición levanta polvo, y con qué dato? Escuche la respuesta: ahí aparece la brecha.")]),
  num("pasos", [run("Cuente el recorrido (1 minuto). ", { bold: true }), run("El 10 de agosto hubo un terremoto. Se demuelen edificios y se retiran escombros. Eso levanta polvo que respiran trabajadores y vecinos. Señale los pasos 1 a 3 de la figura.")]),
  num("pasos", [run("Diga qué falta (1 minuto). ", { bold: true }), run("El comité debe decidir, pero no sabe con confianza cuánto polvo hay ni cuánto habrá.")]),
  num("pasos", [run("Diga qué hace el proyecto, en tres palabras (1 minuto). ", { bold: true }), run("Medir bien, avisar a tiempo, anticipar.")]),
  num("pasos", [run("Diga qué cambia para esa persona (1 minuto). ", { bold: true }), run("Use la fila de su entidad en la tabla de integrantes.")]),
  num("pasos", [run("Cierre con lo que se pide (30 segundos). ", { bold: true }), run("Los soportes, los datos y la firma, con fecha.")]),
  para([run("Prueba de comprensión. ", { bold: true }), run("Pida que lo cuente de vuelta en 30 segundos, como se lo contaría a su alcalde o a su gerente. Si no menciona el polvo de la demolición y la decisión del comité, repita los pasos 2 y 3. Si menciona los sensores pero no la decisión, falta el paso 5.")], { before: 60 }),
  para([run("Ejemplo ilustrativo, no es un dato medido. ", { bold: true }), run("Un sensor sin corregir puede marcar mucho más polvo que el equipo de referencia cuando el aire está húmedo. Con ese dato, un comité podría parar una obra sin necesidad. Con el sensor corregido, el comité sabe cuánto confiar en cada lectura.")]),

  h2("Qué evitar y qué decir en su lugar"),
  glosario,

  h2("Preguntas frecuentes", true),
  preguntas,

  h2("Lo que se necesita esta semana"),
  semana,
  para([run("Las fechas son una propuesta que la alianza ajusta. El detalle está en la tabla S.7 del soporte inicial del documento de trabajo.", { italics: true, size: 18 })], { before: 80 }),
];

const doc = new Document({
  creator: "Equipo formulador", title: "Cómo explicar el proyecto", description: "Guía para explicar el proyecto a los integrantes de la alianza",
  styles: { default: { document: { run: { font: FONT, size: 21, color: T } } } },
  numbering: { config: [
    { reference: "viñetas", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] },
    { reference: "pasos", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } } } }] },
  ] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, right: 1080, bottom: 1000, left: 1080, header: 500, footer: 500 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 0 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: MEDIO, space: 2 } },
      children: [run("Proyecto SGR_CONV56_AIRE · Guía para explicar el proyecto · 24 de octubre de 2026", { size: 16 })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text: "Página ", font: FONT, size: 16, color: T }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: T }),
      new TextRun({ text: " de ", font: FONT, size: 16, color: T }), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 16, color: T })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(OUT, b); console.log("ok", OUT, b.length); });
