# -*- coding: utf-8 -*-
"""Importa las secciones 4.3, 4.4, 4.4-MDR y 4.5 del repositorio y las convierte al formato de directivas del ensamblador."""
import re, json, os, zipfile
R = '/home/user/docs/genesis-e4-e3p00'
def rd(p): return open(f'{R}/{p}', encoding='utf-8').read()

def strip_head(t):
    out = []; first = True
    for l in t.split('\n'):
        if first and l.startswith('# '): first = False; continue
        if l.strip().startswith('CASE_ID:'): continue
        out.append(l)
    return '\n'.join(out).strip('\n') + '\n'

def cells(line):
    s = line.strip()
    if s.startswith('|'): s = s[1:]
    if s.endswith('|') and not s.endswith('\\|'): s = s[:-1]
    out = []; cur = ''; i = 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s) and s[i + 1] == '|': cur += '\\|'; i += 2; continue
        if c == '|': out.append(cur.strip()); cur = ''
        else: cur += c
        i += 1
    out.append(cur.strip()); return out

def renum(t):
    """Prefija F en referencias internas a secciones y marca como E3 las tablas del expediente."""
    t = re.sub(r'(?<![\w.\-])4\.4-MDR', 'F4.4-MDR', t)
    t = re.sub(r'(?<![\w.\-F])(4\.[3-8](?:\.\d+)+)(?![\w\-])', r'F\1', t)       # 4.4.13 -> F4.4.13
    t = re.sub(r'((?:sección|secciones|apartado)\s)(4\.[3-8])(?![\w.\-,])', r'\1F\2', t)
    t = re.sub(r'\bTabla (\d+\.\d+[a-z]?|\d+)(?![\w.]*\})', r'Tabla E3-\1', t)
    return t

def titulo_limpio(s):
    s = re.sub(r'\*\*|\*|`', '', s).strip()
    s = re.sub(r'\s+', ' ', s)
    return s.rstrip('.:').strip()

def titulo_tabla(prev, heading, usados):
    t = prev.strip()
    m = re.match(r'^\*\*([^*]+)\*\*', t)
    cand = None
    if m:
        lab = titulo_limpio(m.group(1))
        # usa la primera oración del rótulo en negrita si es larga
        if len(lab.split()) > 14: lab = re.split(r'(?<=\))\.\s|\.\s', lab)[0]
        cand = lab
    elif t.startswith('#'):
        cand = titulo_limpio(re.sub(r'^#+\s*', '', t))
    if not cand:
        cand = titulo_limpio(re.sub(r'^#+\s*', '', heading)) if heading else 'Resultados'
    cand = re.sub(r'^F?\d+(\.\d+)*(-MDR)?(\.\d+)*\s+', '', cand)
    cand = cand[:1].upper() + cand[1:]
    n = usados.get(cand, 0); usados[cand] = n + 1
    return cand if n == 0 else f'{cand} (continuación {n})'

def convertir(texto, pref, fig_map, ctx):
    """Devuelve (lineas, tablas[(id,titulo)]). ctx: dict con contador 'n' de tablas y 'usados'."""
    L = texto.split('\n'); out = []; i = 0; fence = False; heading = ''
    L = [renum(x) if not x.startswith('```') else x for x in L]
    tablas = []
    while i < len(L):
        l = L[i]
        if l.startswith('```'):
            fence = not fence; out.append(l); i += 1; continue
        if fence: out.append(l); i += 1; continue
        mh = re.match(r'^(#{2,6})\s+(.*)$', l)
        if mh:
            nivel = len(mh.group(1)); tit = mh.group(2).strip(); heading = tit
            if nivel <= 3:
                tit = renum(tit)
                tit = re.sub(r'^(4\.[3-8][-A-Za-z0-9.]*)', r'F\1', tit) if not tit.startswith('F4') else tit
                out.append('#' * nivel + ' ' + tit); i += 1; continue
            # nivel 4+: encabezado en la misma línea del párrafo siguiente
            j = i + 1
            while j < len(L) and L[j].strip() == '': j += 1
            t = titulo_limpio(tit)
            if j < len(L) and L[j] and not re.match(r'^(\||```|!\[|#|- |\* |\d+\. |:::)', L[j]):
                out.append(f'**{t}.** {L[j]}'); i = j + 1
            else:
                out.append(f'**{t}.**'); i += 1
            continue
        # figura
        mf = re.match(r'^!\[([^\]]*)\]\(([^)]+)\.svg\)\s*$', l)
        if mf:
            alt, name = mf.group(1), mf.group(2)
            fid, titulo, nota = fig_map[name]
            k = len(out) - 1
            while k >= 0 and out[k].strip() == '': k -= 1
            mencion = False
            if k >= 0 and not out[k].startswith(('#', '|', ':::', '```')):
                nuevo, nsub = re.subn(r'\b([Ll])a (?:siguiente )?figura\b', lambda m: f'{m.group(1)}a {{F:{fid}}}', out[k], count=1)
                if nsub: out[k] = nuevo; mencion = True
            if not mencion:
                out.append(''); out.append(f'La {{F:{fid}}} presenta {titulo[:1].lower() + titulo[1:]}.'); out.append('')
            out.append(f':::FIGURA {fid} | {titulo} | {nota}'); i += 1; continue
        # tabla
        if l.startswith('|') and i + 1 < len(L) and re.match(r'^\|[\s:|-]+\|\s*$', L[i + 1]):
            j = i
            while j < len(L) and L[j].startswith('|'): j += 1
            blk = L[i:j]
            k = len(out) - 1
            while k >= 0 and out[k].strip() == '': k -= 1
            prev = out[k] if k >= 0 else ''
            ctx['n'] += 1; tid = f't{ctx["n"]:03d}'
            if prev.startswith('**Tabla RDG'):
                nodo = cells(blk[2])[1] if len(blk) > 2 else ''
                titulo = 'Registro de decisión GENESIS: ' + titulo_limpio(nodo)
                out[k] = ''          # elimina el rótulo antiguo
                prev = ''
            else:
                titulo = titulo_tabla(prev, heading, ctx['usados'])
            tablas.append((tid, titulo))
            # mención: sustituir «la tabla» del párrafo previo; si no, agregar oración
            mencion = False
            if k >= 0 and not prev.startswith(('#', '**', '|')):
                nuevo, nsub = re.subn(r'\b([Ll])a (?:siguiente )?tabla\b', lambda m: f'{m.group(1)}a {{T:{tid}}}', prev, count=1)
                if nsub: out[k] = nuevo; mencion = True
            if not mencion:
                out.append(''); out.append(f'La {{T:{tid}}} presenta {titulo[:1].lower() + titulo[1:]}.')
            out.append('')
            out.append(f':::TABLA {tid} | {titulo}')
            out.extend(blk)
            # nota: «Naturaleza…» o ninguna
            out.append(':::NOTA *Nota.* Elaboración propia con el expediente de la sección ' + ctx['sec'] + '.')
            out.append('')
            i = j; continue
        out.append(l); i += 1
    return out, tablas
