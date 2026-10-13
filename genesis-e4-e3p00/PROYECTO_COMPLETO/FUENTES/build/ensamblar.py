# -*- coding: utf-8 -*-
"""Ensamblador del documento único: lee archivos .md con directivas (:::TABLA, :::NOTA, :::FIGURA, {T:id}, {F:id}, %% PREFIJO)
y produce un markdown de pandoc con estilos personalizados APA. Numeración 'c.n' por prefijo, en orden de aparición."""
import re, os, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGDIR = os.path.join(ROOT, "figs", "out")

def cells(line):
    s = line.strip()
    if s.startswith("|"): s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"): s = s[:-1]
    out = []; cur = ""; i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s) and s[i + 1] == "|": cur += "\\|"; i += 2; continue
        if c == "|": out.append(cur.strip()); cur = ""
        else: cur += c
        i += 1
    out.append(cur.strip()); return out

def pesos_tabla(blk, landscape_cols=12):
    """Reescribe la fila separadora con anchos proporcionales al contenido (ver unif/build_md.py)."""
    rows = [cells(x) for x in blk]
    n = len(rows[0]); data = [r for k, r in enumerate(rows) if k != 1]
    avail = 24.9 if n >= landscape_cols else 17.0
    cc = 0.235 if n <= 6 else (0.215 if n <= 9 else (0.19 if n <= 14 else 0.16))
    need = []; des = []
    for c in range(n):
        col = [r[c] if c < len(r) else "" for r in data]
        ml = max(len(x) for x in col); mean = sum(len(x) for x in col) / len(col)
        tok = 0
        for x in col:
            for tk in re.split(r"[\s/]+", x):
                L_ = 64 if re.fullmatch(r"[0-9a-f]{64}", tk) else min(len(tk), 22)
                up = sum(ch.isupper() for ch in tk) / max(1, len(tk))
                tok = max(tok, L_ * (1 + 0.5 * up))
        need.append(tok * cc + 0.35)
        des.append(0.5 * min(ml, 60) + 0.5 * min(mean, 70) + 3)
    base = sum(need)
    if base >= avail: wcm = [x / base * avail for x in need]
    else:
        left = avail - base; sd = sum(des)
        wcm = [need[c] + left * des[c] / sd for c in range(n)]
    d = [max(3, round(x / avail * 120)) for x in wcm]
    sep = "|" + "|".join(" " + "-" * k + " " for k in d) + "|"
    return [blk[0], sep] + blk[2:]

def convertir(texto, prefijo, reg, archivo=""):
    """reg: dict global con 'tab' y 'fig' -> {(prefijo,id): numero}; contadores en reg['cnt']. Devuelve markdown pandoc."""
    L = texto.split("\n"); out = []; i = 0; fence = False
    # 1) numerar en un primer recorrido
    for l in L:
        m = re.match(r"^:::TABLA\s+(\S+)\s*\|", l)
        if m:
            reg["cnt"][("T", prefijo)] += 1; reg["tab"][(prefijo, m.group(1))] = reg["cnt"][("T", prefijo)]
        m = re.match(r"^:::FIGURA\s+(\S+)\s*\|", l)
        if m:
            reg["cnt"][("F", prefijo)] += 1; reg["fig"][(prefijo, m.group(1))] = reg["cnt"][("F", prefijo)]
    return L

def resolver_menciones(md, prefijo, reg):
    def rt(m):
        k = (prefijo, m.group(1))
        if k not in reg["tab"]: return f"**[TABLA NO RESUELTA {m.group(1)}]**"
        return f"Tabla {prefijo}.{reg['tab'][k]}"
    def rf(m):
        k = (prefijo, m.group(1))
        if k not in reg["fig"]: return f"**[FIGURA NO RESUELTA {m.group(1)}]**"
        return f"Figura {prefijo}.{reg['fig'][k]}"
    md = re.sub(r"\{T:([^}]+)\}", rt, md)
    md = re.sub(r"\{F:([^}]+)\}", rf, md)
    return md

def a_pandoc(L, prefijo, reg, ancho_fig_cm=15.5):
    out = []; i = 0
    while i < len(L):
        l = L[i]
        if l.startswith("%% PREFIJO"): i += 1; continue
        if l.startswith("%% INSUFICIENCIA"):
            out.append("*" + l[3:].strip() + "*"); i += 1; continue
        m = re.match(r"^:::TABLA\s+(\S+)\s*\|\s*(.+)$", l)
        if m:
            n = reg["tab"][(prefijo, m.group(1))]
            titulo = m.group(2).strip()
            out += ["", '::: {custom-style="TablaRotulo"}', f"**Tabla {prefijo}.{n}**", ":::", "",
                    '::: {custom-style="TablaTitulo"}', f"*{titulo}*", ":::", ""]
            i += 1
            blk = []
            while i < len(L) and L[i].startswith("|"): blk.append(L[i]); i += 1
            if blk and re.match(r"^\|[\s:|-]+\|\s*$", blk[1] if len(blk) > 1 else ""):
                blk = pesos_tabla(blk)
            out += blk
            # nota (siguiente línea :::NOTA)
            j = i
            while j < len(L) and L[j].strip() == "": j += 1
            if j < len(L) and L[j].startswith(":::NOTA"):
                nota = L[j][len(":::NOTA"):].strip()
                out += ["", '::: {custom-style="TablaNota"}', nota, ":::", ""]
                i = j + 1
            else:
                out += [""]
            continue
        m = re.match(r"^:::FIGURA\s+(\S+)\s*\|\s*([^|]+)\|?(.*)$", l)
        if m:
            n = reg["fig"][(prefijo, m.group(1))]
            titulo = m.group(2).strip(); nota = m.group(3).strip()
            png = os.path.join(FIGDIR, f"c{prefijo}_{m.group(1)}.png")
            if not nota.startswith("*Nota") and not nota.startswith("Nota"): nota = "Nota. " + nota if nota else "Nota."
            nota = re.sub(r"^Nota\.", "*Nota.*", nota)
            out += ["", '::: {custom-style="FiguraRotulo"}', f"**Figura {prefijo}.{n}**", ":::", "",
                    '::: {custom-style="FiguraTitulo"}', f"*{titulo}*", ":::", "",
                    f"![]({png}){{width={ancho_fig_cm}cm}}", "",
                    '::: {custom-style="FiguraNota"}', nota, ":::", ""]
            i += 1; continue
        if l.startswith(":::NOTA"):
            out += ["", '::: {custom-style="TablaNota"}', l[len(":::NOTA"):].strip(), ":::", ""]; i += 1; continue
        out.append(l); i += 1
    return out

def procesar_archivo(path, reg, prefijo_forzado=None):
    t = open(path, encoding="utf-8").read()
    m = re.search(r"^%% PREFIJO:\s*(\S+)", t, re.M)
    pref = prefijo_forzado or (m.group(1) if m else "X")
    L = convertir(t, pref, reg, os.path.basename(path))
    return pref, L

def ensamblar(entradas, salida_md):
    """entradas: lista de (ruta, tipo) con tipo 'cap' (directivas) o 'raw' (markdown tal cual). Retorna estado del registro."""
    reg = {"tab": {}, "fig": {}, "cnt": collections.Counter()}
    leidos = []
    for ruta, tipo in entradas:
        if tipo == "raw":
            leidos.append((ruta, tipo, None, open(ruta, encoding="utf-8").read())); continue
        pref, L = procesar_archivo(ruta, reg)
        leidos.append((ruta, tipo, pref, L))
    partes = []
    for ruta, tipo, pref, cont in leidos:
        if tipo == "raw": partes.append(cont); continue
        pandoc_lines = a_pandoc(cont, pref, reg)
        partes.append(resolver_menciones("\n".join(pandoc_lines), pref, reg))
    open(salida_md, "w", encoding="utf-8").write("\n\n".join(partes))
    return reg
