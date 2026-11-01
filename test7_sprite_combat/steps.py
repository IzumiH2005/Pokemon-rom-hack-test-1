# Tete de combat d'Aventurine : modifications pas a pas de la tete de Brendan
import sys; sys.path.insert(0,'.')
from btk import *
from PIL import Image
H='0123456789abcdef'
br=Image.open('/home/user/pokeemeraude-expansion/graphics/trainers/front_pics/brendan.png').load()
B=[[H[br[x,y]] for x in range(64)] for y in range(64)]
body=[[H[v] for v in r] for r in load_txt('g0.txt')]   # corps deja recolore (provisoire)
def head_box(g): return [r[16:42] for r in g[6:27]]
steps=[]
# Etape 0 : tete de Brendan d'origine (palette d'Aventurine appliquee plus bas uniquement pour la peau)
g=[r[:] for r in body]
for y in range(6,24):
    for x in range(16,42): g[y][x]=B[y][x] if B[y][x]!='0' else '.'
# Etape 1 : bonnet blanc et bandeau vert -> cheveux blonds (meme forme)
M={'e':'5','9':'5','5':'6','6':'4','7':'7','8':'7','a':'5','b':'6'}
for y in range(6,18):
    for x in range(16,42):
        v=B[y][x]
        if v in M and not (y>=16 and 22<=x<=35 and v in '1234'): g[y][x]=M[v]
for y in range(18,24):
    for x in range(16,42):
        v=B[y][x]
        if v=='5': g[y][x]='b'      # iris
        elif v=='8': g[y][x]='4'
steps.append([r[:] for r in g])
# Etape 2 : contour des cheveux unifie (brun fonce au lieu du noir/bleu)
for y in range(6,18):
    for x in range(16,42):
        v=g[y][x]
        if v=='f': g[y][x]='4'
        elif v in '567' and any(g[y+dy][x+dx] in '.0' for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))): g[y][x]='4'
steps.append([r[:] for r in g])
def show(g,fn):
    im=prev([[0 if c in '.' else H.index(c) for c in r] for r in g],1)
    im.crop((14,4,44,30)).resize((30*16,26*16),Image.NEAREST).save(fn)
def dump(g):
    print('   '+''.join(str(x%10) for x in range(16,42)))
    for y in range(6,25): print('%2d '%y+''.join(g[y][16:42]))
# Etape 3 : meches de frange en pointe sur le front
def put(y,x0,s):
    for i,c in enumerate(s):
        if c!=' ': g[y][x0+i]=c
put(14,24,'55556555655')
put(15,24,'555565556566')
put(16,24,'55662566256')
put(17,24,'67723713326')
steps.append([r[:] for r in g])
# Etape 4 : meches laterales le long du visage
put(17,21,'456')
put(18,21,'465')
put(19,21,'46')
put(20,21,'4')
put(17,35,'674')
put(18,35,'664')
put(19,35,'64')
put(20,36,'4')
steps.append([r[:] for r in g])
def show2(g,fn,box=(10,20,54,64)):
    im=prev([[0 if c in '.' else H.index(c) for c in r] for r in g],1)
    w,h=box[2]-box[0],box[3]-box[1]
    im.crop(box).resize((w*12,h*12),Image.NEAREST).save(fn)
def dump2(g,y0=24,y1=64,x0=12,x1=52):
    print('   '+''.join(str(x%10) for x in range(x0,x1)))
    for y in range(y0,y1): print('%2d '%y+''.join(g[y][x0:x1]))
def nb(y,x): return [g[y+dy][x+dx] for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))]
# Etape 5 : veste noire, chemise turquoise, sacoche -> pans dores
src=[r[:] for r in g]
for y in range(24,38):
    for x in range(20,38):
        v=src[y][x]
        if v=='d': g[y][x]='c'
        elif v=='8': g[y][x]='a' if 27<=x<=31 else 'c'
        elif v=='b': g[y][x]='b' if any(n in 'fc' for n in [src[y+dy][x+dx] for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))]) else 'a'
put(33,29,'8 8 8')
put(34,30,'8')
steps.append([r[:] for r in g])
# Etape 6 : manches longues noires + gants noirs, jeton dore en main
for y in range(29,45):
    for x in range(13,49):
        if 21<=x<=37 and y<38: continue
        v=g[y][x]
        if v in '123': g[y][x]='c'
        elif v=='4': g[y][x]='f'
        elif x>=40 and v=='e': g[y][x]='8'
        elif x>=40 and v=='d': g[y][x]='9'
put(37,16,'aa')
put(36,17,'a')
put(33,40,'a')
put(34,40,'aa')
steps.append([r[:] for r in g])
# Etape 7 : pantalon blanc
src=[r[:] for r in g]
for y in range(38,51):
    for x in range(21,38):
        if src[y][x]=='d':
            g[y][x]='d' if any(n in 'f0' for n in [src[y][x+1],src[y][x-1]]) else 'e'
steps.append([r[:] for r in g])
# Etape 8 : epaules sans peau + col en fourrure blanche
for y in range(29,38):
    for x in list(range(19,24))+list(range(34,40)):
        if g[y][x] in '123': g[y][x]='c'
put(25,23,' ed')
put(26,22,'eedde')
put(27,22,'fdeed')
put(28,22,'fded')
put(25,32,'de')
put(26,32,'edee')
put(27,33,'deef')
put(28,34,'edf')
steps.append([r[:] for r in g])
# Etape 9 : pans de cape dores (bas turquoise) derriere les jambes
for y in range(37,51):
    row=g[y]
    xs=[x for x in range(18,40) if row[x] not in '0.']
    xs=[x for x in xs if x>=21]
    if not xs: continue
    l,r=min(xs),max(xs)
    lo='ba' if y>=46 else '98'
    for i,c in enumerate(('f',lo[0],lo[1])):
        x=l-3+i
        if row[x]=='0': row[x]=c
    for i,c in enumerate((lo[1],lo[0],'f')):
        x=r+1+i
        if row[x]=='0': row[x]=c
put(51,19,'fff')
put(51,37,'fff')
steps.append([r[:] for r in g])
# Etape 10 : finitions du gant (doigts sans peau)
for y in range(26,36):
    for x in range(42,50):
        if g[y][x]=='4': g[y][x]='f'
        elif g[y][x] in '123': g[y][x]='c'
steps.append([r[:] for r in g])
# Etape 11 : pli du pantalon adouci (il dessinait un R)
for y in range(42,47):
    g[y][29]="e"; g[y][30]="e"; g[y][32]="e"; g[y][31]="d" if y>=45 else "e"
steps.append([r[:] for r in g])
final=[[0 if c in '.' else H.index(c) for c in r] for r in g]
