"""Pose les runes (dessinées à la main ci-dessous) dans le gabarit d'onglet dessiné à la main.
Inactif = un ton plus sombre (il est derrière le cadre), rune éteinte en n sur fond l."""
actif = """..OOOOOOOOOOO..
.OeeeeeeeeeedO.
OedOOOOOOOOOcbO
OedOkkkkkkkOcbO
OedOkRRRRRnOcbO
OedOkRRRRRnOcbO
OdcOkRRRRRnOcbO
OdcOkRRRRRnOcbO
OdcOkRRRRRnOcbO
OdcOknnnnnnOcbO
OdcOOOOOOOOOcbO
OdcccccccccccbO""".split('\n')
runes = {
 'rond':    [".XXX.","X...X","X...X","X...X",".XXX."],
 'losange': ["..X..",".X.X.","X...X",".X.X.","..X.."],
 'croix':   ["..X..","..X..","XXXXX","..X..","..X.."],
 'pic':     ["..X..","..X..",".X.X.",".X.X.","XXXXX"],
}
def faire(rune):
    g=[list(r) for r in actif]; k=0
    for y,r in enumerate(g):
        s=''.join(r)
        if 'R' in s:
            x0=s.index('R')
            for i in range(5): g[y][x0+i] = 'X' if runes[rune][k][i]=='X' else 'F'
            k+=1
    return [''.join(r) for r in g]
on  = str.maketrans({'X':'y','F':'m'})
off = str.maketrans({'e':'d','d':'c','c':'b','b':'a','n':'m','X':'n','F':'l'})
for nom in runes:
    g=faire(nom)
    open(f'pieces/onglet_{nom}_actif.txt','w').write('\n'.join(r.translate(on) for r in g)+'\n')
    open(f'pieces/onglet_{nom}_inactif.txt','w').write('\n'.join(r.translate(off) for r in g[:11])+'\n')
