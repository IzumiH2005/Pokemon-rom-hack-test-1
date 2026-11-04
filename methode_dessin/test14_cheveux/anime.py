# Test 14 bis : même personnage, coupe beaucoup plus stylisée « anime ».
# Masque des cheveux défini à la main, trait posé automatiquement là où les cheveux touchent
# le vide ou les vêtements (jamais la peau), puis couleurs en aplats nets (cel-shading).
base=[list(l.rstrip('\n')) for l in open('etape01_base.txt') if l.strip()]
H_,W_=len(base),len(base[0])
M=set()
def span(y,a,b):
    for x in range(a,b+1): M.add((x,y))
# 1. masque : ahoge, dôme, masse de dos avec une pointe épaisse vers l'extérieur de chaque côté
for y,(a,b) in {0:(19,21),1:(18,21),2:(17,20),3:(12,19),4:(9,22),5:(7,24),6:(6,25),7:(5,26)}.items(): span(y,a,b)
gauche={8:4,9:4,10:3,11:3,12:3,13:2,14:1,15:0,16:1,17:2,18:3,19:3,20:4,21:4,22:5,23:5}
droite={8:27,9:27,10:28,11:28,12:28,13:28,14:28,15:29,16:30,17:31,18:30,19:29,20:27,21:27,22:26,23:26}
for y in range(8,24): span(y,gauche[y],droite[y])
# 2. mèches avant longues et effilées, devant les épaules (4 px qui s'affinent à 1 px)
for y,(a,b) in {24:(5,9),25:(5,8),26:(6,7)}.items(): span(y,a,b)
for y,(a,b) in {24:(22,26),25:(23,26),26:(24,25)}.items(): span(y,a,b)
# 3. fenêtre du visage : 3 pointes de frange + longue mèche centrale entre les yeux
prof={10:15,11:16,12:14,13:12,14:14,15:16,16:18,17:15,18:12,19:14,20:16,21:15}
for x,b in prof.items():
    for y in range(b+1,24):
        if base[y][x]!='.': M.discard((x,y))
for y in range(21,24):
    for x in range(10,22): M.discard((x,y))
G=[r[:] for r in base]
for (x,y) in M: G[y][x]='H'
for (x,y) in list(M):
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx,ny=x+dx,y+dy
        dehors=not(0<=nx<W_ and 0<=ny<H_)
        if dehors or ((nx,ny) not in M and base[ny][nx] not in 'sSlEir'):
            G[y][x]='O'; break
def put(c,*xy):
    for x,y in zip(xy[::2],xy[1::2]): G[y][x]=c
def hs(c,y,a,b):
    for x in range(a,b+1):
        if G[y][x] not in 'O.': G[y][x]=c
open('etape05_anime_masse.txt','w').write('\n'.join(''.join(r) for r in G)+'\n')

# ===== couleurs en aplats nets (lumière en haut à gauche) =====
# masse de dos : sombre, mais la pointe gauche (côté lumière) garde un aplat moyen
for y in range(8,24):
    for x in range(32):
        if G[y][x]=='H' and (x<=4 or x>=27 or (y>=20 and x in (5,26))): G[y][x]='D'
hs('H',14,2,4); hs('H',15,1,4); hs('H',16,2,4); put('h',2,15,3,14)
hs('X',17,28,30); hs('X',16,28,29); hs('X',18,28,29)
# anneau de reflet (« angel ring ») en dents de scie
hs('L',5,10,13); hs('h',5,14,16)
hs('L',6,8,11); hs('h',6,12,19)
put('L',7,7); hs('h',7,8,9); hs('h',7,13,14); hs('h',7,18,19)
put('h',8,8,8,9,14,8,19,8)
# ombre nette à droite
hs('D',5,22,23); hs('D',6,22,24); hs('D',7,23,25); hs('D',8,23,26); hs('D',9,23,26)
hs('D',10,22,27); hs('D',11,22,27); hs('D',12,23,27); hs('D',13,23,27)
# une seule coupure nette par grosse mèche, vers la raie
put('D',13,9,13,10,13,11, 18,9,18,10,18,11)
# frange : côté droit de chaque pointe en aplat sombre, côté gauche éclairé
put('D',12,12,12,13,12,14, 17,12,17,13,17,14,17,15, 21,13,21,14,21,15)
put('h',10,12,10,13,10,14,14,12,15,13,15,14,19,12,19,13)
put('H',11,15,11,16,16,16,16,17,16,18,20,15,20,16)
# mèches avant : gauche éclairée (reflet cassé), droite à l'ombre ; bas des mèches sombre
for y in range(12,27): put('h',6,y) if G[y][6]=='H' else None
put('H',6,18,6,19)
for y in range(22,29):
    for x in range(5,10):
        if G[y][x]=='H' and x>=8: G[y][x]='D'
for y in range(12,29):
    for x in range(22,28):
        if G[y][x]=='H' and x>=24: G[y][x]='D'
for y in range(20,29):
    for x in range(22,28):
        if G[y][x]=='D' and x>=25: G[y][x]='X'
# ombre portée de la frange sur le front
for x,b in prof.items():
    if G[b+1][x] in 'sl': G[b+1][x]='S'
# selout : trait du haut à gauche en prune
for y in range(0,16):
    for x in range(0,19):
        if G[y][x]=='O': G[y][x]='X'
open('etape05_anime.txt','w').write('\n'.join(''.join(r) for r in G)+'\n')
