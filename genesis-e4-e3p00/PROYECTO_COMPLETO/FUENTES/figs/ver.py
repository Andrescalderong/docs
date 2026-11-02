import sys
from PIL import Image
def ver(png, out=None, fondo=(255,255,255), ancho=1000):
    im=Image.open(png).convert('RGBA'); bg=Image.new('RGBA',im.size,fondo+(255,)); bg.alpha_composite(im)
    bg=bg.convert('RGB'); r=ancho/bg.size[0]; bg=bg.resize((ancho,int(bg.size[1]*r)))
    out=out or png.replace('.png','_vista.jpg'); bg.save(out,quality=88); return out
if __name__=='__main__':
    for p in sys.argv[1:]: print(ver(p))
