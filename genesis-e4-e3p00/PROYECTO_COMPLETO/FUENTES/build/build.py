# -*- coding: utf-8 -*-
"""Construye el documento único: ensamblado de capítulos -> pandoc -> post_apa -> índices con páginas -> PDF.
Uso: python3 build.py LISTA.json SALIDA_BASE   (LISTA.json: [[ruta, 'cap'|'raw'], ...] ; opciones en 'opts')"""
import sys, os, json, subprocess, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ensamblar, post_apa, docx
import pypdf, unicodedata
os.environ['LC_ALL'] = 'C.UTF-8'
FLAGS = '-f markdown-smart-raw_html-tex_math_dollars-citations-superscript-subscript-implicit_header_references-yaml_metadata_block-pandoc_title_block-fancy_lists-raw_tex-inline_notes-footnotes'

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

def main(lista, base):
    cfg = json.load(open(lista, encoding='utf-8'))
    entradas = [tuple(x) for x in cfg['entradas']]
    opts = cfg.get('opts', {})
    md = base + '.md'; raw = base + '_raw.docx'; d0 = base + '_0.docx'; fin = base + '.docx'; pdf = base + '.pdf'
    reg = ensamblar.ensamblar(entradas, md)
    json.dump({'tab': {f'{k[0]}|{k[1]}': v for k, v in reg['tab'].items()}, 'fig': {f'{k[0]}|{k[1]}': v for k, v in reg['fig'].items()}},
              open(base + '_registro.json', 'w'), ensure_ascii=False)
    cmd = ['pandoc', md] + FLAGS.split() + ['-t', 'docx', f'--reference-doc={os.path.join(HERE, "reference_apa.docx")}', '--wrap=none', '--toc', '--toc-depth=3',
           '--no-highlight', '-M', f'title={opts.get("title", "Proyecto")}', '-M', f'subtitle={opts.get("subtitle", "")}', '-M', 'lang=es-CO',
           '-M', 'toc-title=Contenido', '-o', raw]
    subprocess.run(cmd, check=True)
    post_apa.postprocesar(raw, d0, portada=opts.get('portada'))
    d = docx.Document(d0); post_apa.marcar_bookmarks(d); d.save(d0)
    d = docx.Document(d0)
    H = post_apa.titulos(d)
    ET = post_apa.entradas_indice(d, 'TablaRotulo'); EF = post_apa.entradas_indice(d, 'FiguraRotulo')
    pgs = [1] * len(H); pt = [1] * len(ET); pf = [1] * len(EF)
    for it in range(6):
        d = docx.Document(d0)
        post_apa.construir_toc(d, H, pgs)
        post_apa.construir_lista(d, '@@INDICE_TABLAS@@', ET, pt)
        post_apa.construir_lista(d, '@@INDICE_FIGURAS@@', EF, pf)
        post_apa.reorder(d.element)
        d.save(fin)
        subprocess.run(['python3', os.path.join(HERE, 'lo_export2.py'), fin, pdf, base + '_pag.json'], check=True)
        pj = json.load(open(base + '_pag.json'))
        npg = paginas_titulos(pdf, H)
        assert None not in npg, [H[i] for i, x in enumerate(npg) if x is None][:3]
        npt = [pj.get(b, 0) for _, _, b in ET]; npf = [pj.get(b, 0) for _, _, b in EF]
        cambios = sum(a != b for a, b in zip(pgs, npg)) + sum(a != b for a, b in zip(pt, npt)) + sum(a != b for a, b in zip(pf, npf))
        print('iteración', it, 'cambios', cambios)
        if cambios == 0: break
        pgs, pt, pf = npg, npt, npf
    else:
        raise SystemExit('índices no convergen')
    import fix_word; tmp = fin + '.tmp'; fix_word.fix(fin, tmp); os.replace(tmp, fin)
    return fin, pdf

if __name__ == '__main__':
    print(main(sys.argv[1], sys.argv[2]))
