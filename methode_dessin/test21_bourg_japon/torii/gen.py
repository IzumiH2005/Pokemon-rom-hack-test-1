"""Commandes du torii pour une largeur W (48/64/96). Les nombres sont mes decisions ; ce script ne fait que les ecrire."""
import sys
W=int(sys.argv[1]); step=sys.argv[2]; var=sys.argv[3] if len(sys.argv)>3 else 'A'
pl=(5,10); pr=(W-11,W-6)          # poteaux centres dans la 1re et la derniere case
mid=W//2
L=[]
def P(*a): L.append(" ".join(map(str,a)))
if step=='c01':
    if var=='A':   # myojin : kasagi courbe, bouts releves
        P('rect 3 0 1',W-1,3); P('px 3 0 0 1 0',W-1,0,W-2,0)
    else:          # shinmei : barre droite
        P('rect 3 2 1',W-3,3)
    P('rect 3 1 4',W-2,6); P('rect 3 2 10',W-3,12); P('rect 3',mid-2,7,mid+1,9)
    for a,b in (pl,pr): P('rect 3',a,7,b,31); P('rect 3',a-1,28,b+1,31)
if step=='c02':
    P('rect A 0 1',W-1,3); P('px A 0 0 1 0 2 0',W-1,0,W-2,0,W-3,0)      # shimaki noir, bouts releves sur 3 px
    P('rect l 1 4',W-2,6)                                      # kasagi vermillon
    P('rect l 2 10',W-3,12)                                    # nuki
    P('rect l',mid-2,7,mid+1,9)                                # gakuzuka
    for a,b in (pl,pr): P('rect l',a,7,b,27); P('rect A',a-1,28,b+1,31)   # poteaux + kamebara noir
    if W>=96: P('rect A',mid-6,6,mid+5,12); P('rect z',mid-5,7,mid+4,11); P('rect A',mid-4,8,mid+3,10)  # plaque gaku noire, cadre dore
if step=='c03':
    P('hline O 0',W-1,0) if False else None
    P('hline B 1',W-2,1) if False else None
    P('hline s 3',W//4,1)       # reflet court de la laque, cote lumiere
    P('hline m 1',W-2,4); P('hline k 1',W-2,6)
    P('hline m 2',W-3,10); P('hline k 2',W-3,12)
    P('vline m',mid-2,7,9)
    for a,b in (pl,pr):
        P('vline m',a,7,27); P('vline k',b,7,27); P('vline k',b-1,7,27)
        P('hline k',a,b,13)        # ombre du nuki sur le poteau
        P('hline q',a-1,b+1,28)
    if W>=96: P('hline w',mid-5,mid+4,11); P('vline w',mid+4,7,11)
if step=='c04':
    P('rep O A 0 0',W-1,3); P('rep O k 0 4',W-1,27); P('rep O A 0 28',W-1,31)
if step=='c05':
    for a,b in (pl,pr): P('rect A',a,11,b,11)                 # kusabi (cales) sombres
    if W>=96: P('vline z',mid-2,8,10); P('px z',mid-1,9); P('vline z',mid+1,8,10)  # glyphe de la plaque
    P('px m 3 5 4 5',W-5,5,W-4,5) if False else None
print("\n".join(l for l in L if l and l!='None'))
