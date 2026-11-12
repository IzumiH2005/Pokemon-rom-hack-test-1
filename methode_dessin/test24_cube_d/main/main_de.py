# Mini-Dé tenu en main, dessiné dans la palette de Red (indices 0-f).
# '.' = garder le pixel d'origine. Chaque ligne = une rangée.
# Couleurs du Dé : a/9 dessus gris, d jaune et e ocre (face Pikachu),
# 5 orange (face Dracaufeu). La pose n'utilise 5, d et e nulle part ailleurs :
# le jeu les garde en couleur quand Red est gris.
import sys
from PIL import Image
DE_TERNE = [".ffff.",
            "faaaaf",
            "feaa5f",
            "fee55f",
            ".ee55f",
            ".fe5f.",
            "..ff.."]
DE_ALLUME = [".ffff.",
             "fa99af",
             "fdaa5f",
             "fdd55f",
             ".dd55f",
             ".fd5f.",
             "..ff.."]
DE_BAS = [".fff.",   # tenu bas, de côté (frame 5)
          "faaaf",
          "fea5f",
          "fee5f",
          ".fff."]
# frame, x, y, dessin
POSES = [(5,3,21,DE_BAS),(6,9,20,DE_TERNE),(7,10,16,DE_TERNE),(8,10,15,DE_ALLUME)]
src,dst=sys.argv[1],sys.argv[2]
im=Image.open(src)
for f,x0,y0,g in POSES:
    for dy,row in enumerate(g):
        for dx,c in enumerate(row):
            if c!='.': im.putpixel((f*16+x0+dx,y0+dy),int(c,16))
im.save(dst)
