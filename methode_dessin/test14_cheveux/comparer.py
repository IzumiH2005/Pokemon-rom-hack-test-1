# Côte à côte : version simple (etape04) et version anime (etape05), ×1, ×4 et en situation
import subprocess
from PIL import Image
for f in ('etape04_final.txt','etape05_anime.txt'):
    subprocess.run(['python3','../outils/px.py',f,'12','palette.json'],check=True)
a=Image.open('etape04_final.png').convert('RGBA'); b=Image.open('etape05_anime.png').convert('RGBA')
def herbe(im):
    g=Image.new('RGBA',(56,56),(104,176,88,255))
    for y in range(56):
        for x in range(56):
            if (x*7+y*3)%11==0: g.putpixel((x,y),(88,156,76,255))
    g.alpha_composite(im,(12,10)); return g
W,H=32,39
out=Image.new('RGBA',(8+W*4+8+W*4+8+56*2+8+56*2+8, 8+H*4+8),(236,234,228,255))
out.alpha_composite(a.resize((W*4,H*4),Image.NEAREST),(8,8))
out.alpha_composite(b.resize((W*4,H*4),Image.NEAREST),(16+W*4,8))
x0=24+W*8
out.alpha_composite(herbe(a).resize((112,112),Image.NEAREST),(x0,8))
out.alpha_composite(herbe(b).resize((112,112),Image.NEAREST),(x0+120,8))
out.convert('RGB').save('comparaison.png')
herbe(b).save('situation_anime.png')
subprocess.run(['python3','../outils/planche.py','etape05_anime.png','planche_anime.png','situation_anime.png'],check=True)
