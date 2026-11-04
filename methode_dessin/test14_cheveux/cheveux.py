# Test 14 : calque cheveux posé à la main sur le corps du test 13 (toile 32x39).
# Coupe : carré auburn mi-long, frange balayée vers la droite en 3 touffes, deux mèches
# avant qui finissent en pointe devant des cheveux de dos plus sombres, une mèche rebelle.
base=[list(l.rstrip('\n')) for l in open('etape01_base.txt') if l.strip()]
G=[r[:] for r in base]
def put(c,*xy):
    for x,y in zip(xy[::2],xy[1::2]): G[y][x]=c
def span(c,y,a,b):
    for x in range(a,b+1): G[y][x]=c
def save(n): open(n,'w').write('\n'.join(''.join(r) for r in G)+'\n')

# 1. cheveux de dos (derrière la nuque), sombres
for y in range(18,24):
    for x in list(range(5,11))+list(range(21,27)):
        if base[y][x]=='.': G[y][x]='D'
for y in (22,23): put('O',5,y,26,y)
for y in (18,19,20,21): put('O',4,y,27,y)
span('O',24,6,10); span('O',24,21,25)
for y in (20,21): put('X',5,y,26,y)
for y in (22,23): put('X',6,y,25,y)
# 2. dôme et mèches avant : bord gauche / droit du trait par rangée
bord={4:(11,20),5:(9,22),6:(7,24),7:(6,25),8:(5,26),9:(5,26),10:(5,26),11:(5,26),12:(5,26)}
for y in range(13,18): bord[y]=(4,27)
for y,(a,b) in bord.items():
    span('H',y,a,b)
    d=1 if y in (5,6) else 0
    span('O',y,a,a+d); span('O',y,b-d,b)
span('O',4,11,20)
# mèche avant gauche x5..8, pointe en (6,22) ; droite x23..26, pointe en (25,22)
for x,fin in {5:21,6:22,7:21,8:20}.items():
    for y in range(18,fin+1): G[y][x]='H'
for x,fin in {23:20,24:21,25:22,26:21}.items():
    for y in range(18,fin+1): G[y][x]='H'
# 3. fenêtre du visage sous la frange : 3 touffes en biseau, pointes au-dessus des yeux
prof={9:12,10:13,11:14,12:15,13:16, 14:12,15:13,16:14,17:15,18:16, 19:12,20:13,21:14,22:15}
for x,b in prof.items():
    for y in range(b+1,24):
        if base[y][x]!='.': G[y][x]=base[y][x]
save('etape02_masse.txt')

# ===== 4. ombrage (lumière en haut à gauche) =====
# zone claire du dôme en haut à gauche, reflet L en arc cassé en tirets
span('h',5,11,15); span('h',6,9,13); span('h',7,7,11); span('h',8,6,9); span('h',9,6,7); span('h',10,6,7)
put('L',13,5,14,5, 10,6,11,6, 8,7, 7,8,6,9)
# reflets des touffes de frange (un tiret par touffe éclairée)
put('h',10,10,11,10, 15,9,16,9,16,8, 20,9,21,9)
# côté droit à l'ombre, largeur variable (pas de bande régulière)
put('D',21,5,22,6, 23,7,24,7, 24,8,25,8, 24,9,25,9, 23,10,24,10,25,10, 24,11,25,11)
for y in range(12,18): put('D',25,y)
for y in range(13,18): put('D',26,y)
put('X',26,14,26,15,26,16,26,17)
# lignes de touffes : de la raie vers les encoches de la frange
put('D',13,9,13,10,14,11, 17,8,18,9,18,10,19,11)
# dessous de chaque touffe : la pointe et le pixel au-dessus en D

# mèches avant : gauche éclairée (tiret h cassé), droite à l'ombre
for y in range(11,16): put('h',6,y)
put('h',6,18,6,19)
put('D',8,19,8,20,7,20,7,21, 23,19,23,20,24,20,24,21, 26,18,26,19,26,20,26,21)
put('X',25,21)
put('H',6,21,6,22,25,21,25,22); put('h',6,20); put('H',5,20,5,21); put('D',26,20,26,21); put('O',11,23,20,23)
put('D',8,11,8,12)          # séparation mèche gauche / touffe A
# ombre portée de la frange sur le front : haut des trous et sous les pointes
put('S',14,13,14,14,15,14, 19,13,19,14,20,14, 9,13,9,14,10,14, 13,17,18,17,22,16)
# 5. mèche rebelle sur le dessus, courbée vers la droite (accent posé en dernier)
put('O',16,2,17,2,15,3,18,3,18,4); put('h',16,3); put('H',17,3,16,4,17,4)
# selout : trait du haut côté lumière en couleur sombre des cheveux, bas et droite en O
for y in range(2,15):
    for x in range(0,17):
        if G[y][x]=='O': G[y][x]='X'
save('etape03_ombre.txt')
