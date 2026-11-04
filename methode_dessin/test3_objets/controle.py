from PIL import Image, ImageDraw, ImageOps
from commun import rendre
import potion, coffre
P=potion.P; C=[''.join(r) for r in coffre.G]
def remap(g,m): return [''.join(m.get(c,c) for c in r) for r in g]
def etapes(g,pal,contour,aplat,nom,k):
    sil=remap(g,{c:'O' for c in pal if c!='S'})
    con=[''.join(c if c in contour else ('.' if c in '.S' else '.') for c in r) for r in g]
    apl=remap(g,aplat)
    ims=[rendre(x,pal,k=k,fond=(236,232,220,255)) for x in (sil,con,apl,g)]
    w,h=ims[0].size; out=Image.new('RGB',(4*w+30,h+24),(255,255,255)); d=ImageDraw.Draw(out)
    for i,(im,t) in enumerate(zip(ims,['5 silhouette','6 contour','7 aplats','8-10 final'])):
        out.paste(im,(i*(w+10),24)); d.text((i*(w+10)+4,6),t,fill=(0,0,0))
    out.save(nom)
etapes(P,potion.PAL,'OR',{**{c:'3' for c in '1245'},'W':'g','a':'g','r':'g','k':'c','C':'c'},'etapes_potion.png',12)
etapes(C,coffre.PAL,'Oa',{**{c:'c' for c in 'bde'},**{c:'3' for c in '1245'},**{c:'r' for c in 'pqsW'}},'etapes_coffre.png',8)
# contrôle final : taille réelle, x2, x4, gris, miroir, inventaire
def gris(im): return ImageOps.grayscale(im.convert('RGB')).convert('RGB')
out=Image.new('RGB',(700,300),(255,255,255)); d=ImageDraw.Draw(out)
y=10
for g,pal,n in ((P,potion.PAL,16),(C,coffre.PAL,32)):
    x=10
    for k,fond in ((1,(236,232,220,255)),(2,(236,232,220,255)),(4,(236,232,220,255)),(4,(40,44,52,255))):
        im=rendre(g,pal,k=k,fond=fond); out.paste(im,(x,y)); x+=im.size[0]+12
    im=rendre(g,pal,k=4,fond=(236,232,220,255))
    out.paste(gris(im),(x,y)); x+=im.size[0]+12
    out.paste(ImageOps.mirror(im),(x,y))
    y+=n*4+14
# inventaire de jeu (taille réelle x2, cases 36 px)
inv=Image.new('RGB',(36*6+14,50),(52,40,70)); di=ImageDraw.Draw(inv)
for i in range(6):
    di.rectangle([6+i*36,6,6+i*36+33,6+37],fill=(86,70,110),outline=(180,160,210))
p2=rendre(P,potion.PAL,k=2); c1=rendre(C,coffre.PAL,k=1)
inv.paste(p2,(6+1,8),p2); inv.paste(c1,(6+36+1,9),c1); inv.paste(p2,(6+72+1,8),p2)
out.paste(inv,(10,y+4)); d.text((240,y+20),"inventaire (x2 potion, x1 coffre)",fill=(0,0,0))
out.save('etape_11_controle.png')
rendre(P,potion.PAL,'potion_16.png'); rendre(C,coffre.PAL,'coffre_32.png')
rendre(P,potion.PAL,'potion_16_x8.png',k=8); rendre(C,coffre.PAL,'coffre_32_x8.png',k=8)
