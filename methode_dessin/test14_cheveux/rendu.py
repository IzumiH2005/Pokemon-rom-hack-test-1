# Rendu : planche de contrôle + mise en situation sur herbe (56x56, sprite en 12,10)
import sys, subprocess
from PIL import Image
src=sys.argv[1]; b=src.rsplit('.',1)[0]
subprocess.run(['python3','../outils/px.py',src,'12','palette.json'],check=True)
im=Image.open(b+'.png').convert('RGBA')
g=Image.new('RGBA',(56,56),(104,176,88,255))
for y in range(56):
    for x in range(56):
        if (x*7+y*3)%11==0: g.putpixel((x,y),(88,156,76,255))
g.alpha_composite(im,(12,10)); g.save('situation.png')
subprocess.run(['python3','../outils/planche.py',b+'.png','planche.png','situation.png'],check=True)
