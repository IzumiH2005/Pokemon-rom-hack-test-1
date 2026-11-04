from PIL import Image
def rendre(grille, pal, nom=None, k=1, fond=None):
    h=len(grille); w=len(grille[0])
    assert all(len(r)==w for r in grille), [ (i,len(r)) for i,r in enumerate(grille) if len(r)!=w]
    im=Image.new('RGBA',(w,h),(0,0,0,0) if fond is None else fond)
    for y,r in enumerate(grille):
        for x,c in enumerate(r):
            if c!='.': 
                col=pal[c]; 
                if len(col)==4:
                    base=im.getpixel((x,y)); a=col[3]/255
                    col=tuple(int(base[i]*(1-a)+col[i]*a) for i in range(3))+(255 if fond else col[3],)
                im.putpixel((x,y),col)
    im=im.resize((w*k,h*k),Image.NEAREST)
    if nom: im.save(nom)
    return im
def vue(grille,pal,nom,k=20):
    # x1, puis agrandi avec grille, sur fond clair et fond sombre
    from PIL import ImageDraw
    h=len(grille); w=len(grille[0])
    a=rendre(grille,pal,k=k,fond=(236,232,220,255)); b=rendre(grille,pal,k=k,fond=(40,44,52,255))
    for im in (a,b):
        d=ImageDraw.Draw(im)
        for i in range(w+1): d.line([(i*k,0),(i*k,h*k)],fill=(128,128,128))
        for i in range(h+1): d.line([(0,i*k),(w*k,i*k)],fill=(128,128,128))
    out=Image.new('RGB',(w*k*2+20+w*3+20, h*k),(255,255,255))
    out.paste(a,(0,0)); out.paste(b,(w*k+20,0))
    out.paste(rendre(grille,pal,k=1,fond=(236,232,220,255)),(w*k*2+30,0))
    out.paste(rendre(grille,pal,k=2,fond=(40,44,52,255)),(w*k*2+30,h+10))
    out.save(nom)
