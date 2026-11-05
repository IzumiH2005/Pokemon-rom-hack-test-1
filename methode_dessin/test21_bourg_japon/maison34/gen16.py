# Écrit c16a.txt : aplats du nouveau toit 3/4. Toutes les bornes sont des listes choisies à la main.
import sys
W=int(sys.argv[1])
out=['# c16a toit en vraie 3/4 (inspiré des toits du jeu : pan arrière visible, faîtage descendu)',
     'rect . 0 0 79 43']
# bord gauche de la silhouette par rangée (coin arrière chanfreiné, égout relevé)
left={0:8,1:5,2:3,3:2,4:1}
for y in range(5,40): left[y]=1
left.update({40:1,41:0,42:0,43:0})
# arêtier arrière (rangées 1-8) et avant (13-40) : x de l'arête gauche
back={1:6,2:7,3:8,4:9,5:10,6:11,7:12,8:13}
steps=[3,2,3,2,3,2,3,2,3,2,3,1]   # 28 rangées, x de 13 à 2
front={};x=13;y=13
for s in steps:
    for _ in range(s): front[y]=x; y+=1
    x-=1
for y in range(0,44):
    L=left[y]; R=W-1-L
    out.append(f'hline A {L} {R} {y}')            # contour plein
    if y in (0,) : continue
    if y<=8:   # pan arrière + croupes
        a=back[y]; out.append(f'hline D {L+1} {a} {y}'); out.append(f'hline D {a+1} {W-2-a} {y}'); out.append(f'hline B {W-1-a} {R-1} {y}')
    elif y<=12:
        out.append(f'hline D {L+1} 13 {y}'); out.append(f'hline B {W-14} {R-1} {y}')
    elif y<=40:
        a=front[y]; out.append(f'hline D {L+1} {a} {y}'); out.append(f'hline C {a+1} {W-2-a} {y}'); out.append(f'hline B {W-1-a} {R-1} {y}')
    elif y==41:
        out.append(f'hline C 1 {W-2} {y}')
open('c16a.txt','w').write('\n'.join(out)+'\n')
# ---- c16b : lumière, côtes, rangs, faîtage
o=['# c16b relief']
ribs=list(range(16,W-15,5))   # creux des côtes, pas de 5 (choisi : 10 côtes sur le pan avant)
for y in range(1,9):        # pan arrière : côtes douces (creux C), reflet Q à droite du creux
    a=back[y]
    for r in ribs:
        if a<r<W-1-a: o.append(f'px C {r} {y}')
for y in range(14,41):      # pan avant : creux B + reflet D (3 tons, comme les côtes du jeu)
    a=front[y]
    for r in ribs:
        if a+1<r<W-2-a: o.append(f'px B {r} {y}')
        if a+1<r+1<W-2-a: o.append(f'px D {r+1} {y}')
for cy in (21,28,35):       # rangs : bord de tuile ombré, bout rond clair qui déborde
    a=front[cy]
    o.append(f'hline B {a+1} {W-2-a} {cy}')
    for r in ribs:
        o.append(f'px D {r+1} {cy} {r+2} {cy}'); o.append(f'px A {r} {cy}')
# crêtes des arêtiers
for y in range(1,9):  a=back[y];  o.append(f'px Q {a} {y}'); o.append(f'px D {W-1-a} {y}')
for y in range(13,41): a=front[y]; o.append(f'px Q {a} {y}'); o.append(f'px D {W-1-a} {y}')
for y in range(15,40,4):   # croupes : rangs vus de biais
    a=front[y]; o.append(f'hline C {2} {a-2} {y}'); o.append(f'hline A {W-1-a+2} {W-3} {y}')
# faîtage
o+=[f'hline Q 14 {W-15} 9',f'hline D 14 {W-15} 10',f'hline B 14 {W-15} 11',f'hline A 14 {W-15} 12',f'hline B 16 {W-17} 13']
# égout : bouts ronds
o.append(f'hline C 1 {W-2} 41')
for r in ribs: o.append(f'px D {r+1} 41 {r+2} 41'); o.append(f'px B {r} 41')
open('c16b.txt','w').write('\n'.join(o)+'\n')
