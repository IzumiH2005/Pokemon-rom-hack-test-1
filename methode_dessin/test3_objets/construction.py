# Étapes 0-3 : intention, grille, volumes (couleurs de construction R7)
from PIL import Image, ImageDraw
def planche(n, nom, dessine):
    S=20; im=Image.new('RGB',(n*S,n*S),(245,245,240)); d=ImageDraw.Draw(im)
    for i in range(n+1):
        c=(200,200,200) if i%4 else (150,150,150)
        d.line([(i*S,0),(i*S,n*S)],fill=c); d.line([(0,i*S),(n*S,i*S)],fill=c)
    dessine(d,S); im.save(nom)
# Potion 16x16 : sphère (ventre) + cylindre (col) + bouchon. Lumière haut-gauche.
def potion(d,S):
    B=(40,90,230); V=(30,160,60); R=(220,40,40)
    d.rectangle([2*S,5*S,14*S,16*S],outline=B,width=2)          # boîte englobante sphère
    d.ellipse([1*S,5*S,15*S,16*S],outline=V,width=3)            # sphère 14x11
    d.rectangle([5*S,3*S,11*S,5*S],outline=V,width=3)           # col (lèvre y3)
    d.rectangle([5*S,0,11*S,3*S],outline=V,width=3)             # bouchon
    d.line([(1*S,7.5*S),(15*S,7.5*S)],fill=R,width=2)           # niveau du liquide
    d.arc([1*S,6*S,15*S,9*S],0,180,fill=V,width=2)              # ellipse de surface (maillage)
    d.line([(8*S,0),(8*S,16*S)],fill=R,width=1)                 # axe de symétrie
    d.line([(14*S,6*S),(3*S,15*S)],fill=(200,120,0),width=2)    # terminateur (lumière haut-gauche)
    d.polygon([(0,0),(2*S,0),(0,2*S)],fill=(255,200,0))         # source de lumière
# Coffre 32x32 : boîte vue de face, un peu d'en haut (dessus visible).
def coffre(d,S):
    B=(40,90,230); V=(30,160,60); R=(220,40,40)
    d.polygon([(3*S,3*S),(29*S,3*S),(31*S,7*S),(1*S,7*S)],outline=V,width=3)   # dessus (perspective)
    d.rectangle([1*S,7*S,31*S,13*S],outline=V,width=3)                          # face avant couvercle
    d.rectangle([1*S,13*S,31*S,28*S],outline=V,width=3)                         # corps
    for x0 in (6,23): d.rectangle([x0*S,4*S,(x0+3)*S,27*S],outline=B,width=2)  # bandes de fer
    d.rectangle([13*S,9*S,19*S,19*S],outline=R,width=3)                         # serrure (accent)
    d.ellipse([2*S,28*S,30*S,31*S],outline=(120,120,120),width=2)              # ombre portée
    d.polygon([(0,0),(3*S,0),(0,3*S)],fill=(255,200,0))
planche(16,'etape_03_potion_volumes.png',potion)
planche(32,'etape_03_coffre_volumes.png',coffre)
