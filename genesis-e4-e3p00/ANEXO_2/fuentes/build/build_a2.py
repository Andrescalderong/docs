# -*- coding: utf-8 -*-
"""Construye el Anexo 2: expande macros -> ensambla -> pandoc (plantilla oficial) -> posprocesado -> índices con páginas (LibreOffice) -> PDF.
Uso: python3 build/build_a2.py SALIDA_BASE [--soporte]   (con --soporte incluye la parte inicial de soporte para la alianza)"""
import sys, os, json, subprocess, re, glob, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); A2 = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(A2, "v2"))
import ensamblar, post_a2 as post_apa, docx
import pypdf
os.environ['LC_ALL'] = 'C.UTF-8'
FLAGS = '-f markdown-smart-raw_html-tex_math_dollars-citations-superscript-subscript-implicit_header_references-yaml_metadata_block-pandoc_title_block-fancy_lists-raw_tex-inline_notes-footnotes'
TITULO = "CONVOCATORIA DE EMERGENCIA PARA LA RECUPERACIÓN Y GENERACIÓN DE CAPACIDADES TRANSFORMADORAS, EN EL MARCO DEL DECRETO 1414 DE 17 DE SEPTIEMBRE DE 2026."

def norm(s): return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s)).strip()

def paginas_titulos(pdf, heads):
    r = pypdf.PdfReader(pdf); flat = []
    def walk(o):
        for it in o:
            if isinstance(it, list): walk(it)
            else: flat.append((norm(it.title), r.get_destination_page_number(it) + 1))
    walk(r.outline)
    pages = []; i = 0
    for lvl, txt, bm in heads:
        t = norm(txt); found = None
        while i < len(flat):
            if flat[i][0] == t: found = flat[i][1]; i += 1; break
            i += 1
        pages.append(found)
    return pages

SIGLAS = [
 ("ASC", "Apropiación social del conocimiento"), ("CTeI", "Ciencia, tecnología e innovación"), ("DANE", "Departamento Administrativo Nacional de Estadística"),
 ("DNP", "Departamento Nacional de Planeación"), ("EPA", "Agencia de Protección Ambiental de Estados Unidos"), ("IES", "Institución de educación superior"),
 ("IoT", "Internet de las cosas"), ("LoRa", "Tecnología de radio de largo alcance y bajo consumo"), ("MGA", "Metodología General Ajustada"),
 ("MinCiencias", "Ministerio de Ciencia, Tecnología e Innovación"), ("NMAE", "Error absoluto medio normalizado"), ("NRMSE", "Error cuadrático medio normalizado"),
 ("OCDE", "Organización para la Cooperación y el Desarrollo Económicos"), ("OMS", "Organización Mundial de la Salud"), ("PM2,5 y PM10", "Material particulado de hasta 2,5 y 10 micrómetros"),
 ("R²", "Coeficiente de determinación"), ("SGR", "Sistema General de Regalías"), ("SIGP", "Sistema Integrado de Gestión de Proyectos"),
 ("SNCTI", "Sistema Nacional de Ciencia, Tecnología e Innovación"), ("TdR", "Términos de referencia"), ("TRL", "Nivel de madurez tecnológica"),
 ("UNGRD", "Unidad Nacional para la Gestión del Riesgo de Desastres"),
]

def front_md(path):
    L = ['::: {custom-style="FrontTitulo"}', 'Índice de tablas', ':::', '', '@@INDICE_TABLAS@@', '',
         '::: {custom-style="FrontTitulo"}', 'Índice de figuras', ':::', '', '@@INDICE_FIGURAS@@', '',
         '::: {custom-style="FrontTitulo"}', 'Lista de siglas', ':::', '']
    for s, d in SIGLAS: L.append(f'**{s}.** {d}.  ')
    L.append('')
    open(path, 'w', encoding='utf-8').write('\n'.join(L))

def main(base, soporte):
    out_md = os.path.join(A2, 'out_md'); os.makedirs(out_md, exist_ok=True)
    subprocess.run([sys.executable, os.path.join(HERE, 'gen_s29.py')], check=True)
    secs = sorted(glob.glob(os.path.join(A2, 'sec', 's[0-9][0-9].md')))
    if not soporte: secs = [s for s in secs if not s.endswith('s00.md')]
    for s in secs: subprocess.run([sys.executable, os.path.join(A2, 'v2', 'expand.py'), s], check=True, stdout=subprocess.DEVNULL)
    fm = os.path.join(out_md, 'front.md'); front_md(fm)
    entradas = [(fm, 'raw')] + [(os.path.join(out_md, os.path.basename(s)), 'cap') for s in secs]
    md = base + '.md'; raw = base + '_raw.docx'; d0 = base + '_0.docx'; fin = base + '.docx'; pdf = base + '.pdf'
    reg = ensamblar.ensamblar(entradas, md)
    cmd = ['pandoc', md] + FLAGS.split() + ['-t', 'docx', f'--reference-doc={os.path.join(HERE, "reference_a2.docx")}', '--wrap=none', '--toc', '--toc-depth=2',
           '--no-highlight', '-M', f'title={TITULO}', '-M', 'subtitle=ANEXO 2. DOCUMENTO TÉCNICO', '-M', 'lang=es-CO', '-M', 'toc-title=CONTENIDO', '-o', raw]
    subprocess.run(cmd, check=True)
    import m2
    portada = [('p', 'Nombre del proyecto: ' + m2.IDENT['titulo'], dict(size=11, bold=False, before=4, after=10))]
    if soporte:
        portada.append(('p', 'Edición con soporte inicial para la alianza. La parte inicial se retira antes de radicar.', dict(size=10, italic=True, after=8)))
    post_apa.postprocesar(raw, d0, portada=portada)
    d = docx.Document(d0)
    n_dil = post_apa.colorear_diligenciar(d)
    pre = ['1. IDENTIFICACIÓN DEL PROYECTO'] + (['SOPORTE INICIAL'] if soporte else [])
    post_apa.salto_antes(d, pre)
    post_apa.marcar_bookmarks(d); post_apa.reorder(d.element); d.save(d0)
    d = docx.Document(d0)
    H = post_apa.titulos(d)
    ET = post_apa.entradas_indice(d, 'TablaRotulo'); EF = post_apa.entradas_indice(d, 'FiguraRotulo')
    pgs = [1] * len(H); pt = [1] * len(ET); pf = [1] * len(EF)
    for it in range(8):
        d = docx.Document(d0)
        post_apa.construir_toc(d, H, pgs)
        post_apa.construir_lista(d, '@@INDICE_TABLAS@@', ET, pt)
        post_apa.construir_lista(d, '@@INDICE_FIGURAS@@', EF, pf)
        post_apa.reorder(d.element)
        d.save(fin)
        subprocess.run([sys.executable, os.path.join(HERE, 'lo_export_a2.py'), fin, pdf, base + '_pag.json'], check=True)
        pj = json.load(open(base + '_pag.json'))
        npg = paginas_titulos(pdf, H)
        if None in npg: print('aviso: títulos sin página:', [H[i][1][:40] for i, x in enumerate(npg) if x is None][:5]); npg = [x or 1 for x in npg]
        npt = [pj.get(b, 0) for _, _, b in ET]; npf = [pj.get(b, 0) for _, _, b in EF]
        cambios = sum(a != b for a, b in zip(pgs, npg)) + sum(a != b for a, b in zip(pt, npt)) + sum(a != b for a, b in zip(pf, npf))
        print('iteración', it, 'cambios', cambios, flush=True)
        if cambios == 0: break
        pgs, pt, pf = npg, npt, npf
    print('marcadores verdes:', n_dil, 'tablas:', len(ET), 'figuras:', len(EF), 'títulos en el contenido:', len(H))
    return fin, pdf

if __name__ == '__main__':
    base = sys.argv[1]; sop = '--soporte' in sys.argv
    print(main(base, sop))
