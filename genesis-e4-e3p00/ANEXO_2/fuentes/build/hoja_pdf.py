# -*- coding: utf-8 -*-
"""Hoja de contacto de páginas de un PDF. Uso: python3 build/hoja_pdf.py PDF SALIDA.jpg DPI pag1,pag2,... [columnas]"""
import sys, subprocess, os, tempfile
from PIL import Image
pdf, out, dpi, pags = sys.argv[1], sys.argv[2], int(sys.argv[3]), [int(x) for x in sys.argv[4].split(",")]
cols = int(sys.argv[5]) if len(sys.argv) > 5 else 3
tmp = tempfile.mkdtemp(prefix="hoja_")
ims = []
for p in pags:
    base = os.path.join(tmp, f"p{p}")
    subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", str(dpi), "-png", pdf, base], check=True)
    f = [x for x in os.listdir(tmp) if x.startswith(f"p{p}-")][0]
    ims.append(Image.open(os.path.join(tmp, f)).convert("RGB"))
w = max(i.size[0] for i in ims); h = max(i.size[1] for i in ims)
filas = (len(ims) + cols - 1) // cols
H = Image.new("RGB", (cols * w + (cols + 1) * 6, filas * h + (filas + 1) * 6), (120, 120, 120))
for k, im in enumerate(ims):
    r, c = divmod(k, cols)
    H.paste(im, (6 + c * (w + 6), 6 + r * (h + 6)))
H.save(out, quality=82)
print(out, H.size)
