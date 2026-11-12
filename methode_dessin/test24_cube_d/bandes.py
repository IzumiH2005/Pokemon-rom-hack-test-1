"""Rainure (1 px) puis bande sombre (2 px) le long du bord de chaque panneau : largeur
constante décidée, pas de dégradé calculé (R3). Usage : python3 bandes.py"""
for x in range(6,27):
    y0=23+(x-2)//2; y1=y0+19
    if x in (6,26): print(f'vline 1 {x} {y0} {y1}'); continue
    print(f'px 1 {x} {y0} {x} {y1}')
    if x in (7,8,24,25): print(f'vline 2 {x} {y0+1} {y1-1}')
    else: print(f'vline 2 {x} {y0+1} {y0+2}'); print(f'vline 2 {x} {y1-2} {y1-1}')
for x in range(36,57):
    y0=23+(60-x)//2; y1=y0+19
    if x in (36,56): print(f'vline 6 {x} {y0} {y1}'); continue
    print(f'px 6 {x} {y0} {x} {y1}')
    if x in (37,38,54,55): print(f'vline 7 {x} {y0+1} {y1-1}')
    else: print(f'vline 7 {x} {y0+1} {y0+2}'); print(f'vline 7 {x} {y1-2} {y1-1}')
# panneau du dessus : paroi haute à l'ombre (b), lèvre basse éclairée (e)
for y in range(8,29):
    k = y-8 if y<=18 else 28-y
    a,b = 30-2*k, 32+2*k
    col = 'b' if y<=18 else 'e'
    if y in (8,28): print(f'hline {col} {a} {b} {y}')
    else: print(f'px {col} {a} {y} {a+1} {y} {b-1} {y} {b} {y}')
