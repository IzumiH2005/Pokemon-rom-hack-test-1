from commun import *
PAL={'O':(36,20,30),
 'a':(74,34,38),'b':(108,52,42),'c':(148,82,50),'d':(204,144,80),'e':(232,186,112),
 '1':(38,42,64),'2':(70,80,106),'3':(132,146,164),'4':(184,198,206),'5':(226,232,222),
 'p':(116,58,30),'q':(186,110,32),'r':(234,174,50),'s':(252,226,118),'W':(255,250,228),
 'S':(20,16,30,96)}
W,H=32,32
G=[['.']*W for _ in range(H)]
def seg(y,x0,x1,c):
    for x in range(x0,x1+1): G[y][x]=c
def px(x,y,c): G[y][x]=c
# --- silhouette + contour (étapes 5-6) ---
seg(3,3,28,'O'); px(2,4,'O'); px(29,4,'O')
for y in range(5,28): px(1,y,'O'); px(30,y,'O')
seg(27,1,30,'O')
# --- dessus du couvercle (vu d'en haut, éclairé) y4-6 ---
seg(4,3,28,'d'); seg(5,2,29,'d'); seg(6,2,29,'d')
# --- arête avant du couvercle (lumière) y7 ---
seg(7,2,29,'e')
# --- face avant du couvercle y8-10, bord de fer y11-12 ---
for y in (8,9,10): seg(y,2,29,'c')
seg(11,2,29,'3'); seg(12,2,29,'2')
# --- joint couvercle / corps ---
seg(13,2,29,'O')
# --- corps y14-26 ---
seg(14,2,29,'a'); seg(15,2,29,'b')        # ombre portée du couvercle
for y in range(16,25): seg(y,2,29,'c')
seg(25,2,29,'3'); seg(26,2,29,'2')        # bande basse en fer

# --- étapes 8-9 : bandes de fer (cylindre aplati : bord gauche clair, droit sombre) ---
for xb in (6,23):
    for y in (4,):  seg(y,xb+1,xb+3,'4'); px(xb+1,y,'5')
    for y in (5,6): px(xb,y,'5'); px(xb+1,y,'4'); px(xb+2,y,'3')
    px(xb,7,'5'); px(xb+1,7,'5'); px(xb+2,7,'4')
    for y in (8,9,10)+tuple(range(16,25)): px(xb,y,'4'); px(xb+1,y,'3'); px(xb+2,y,'2')
    px(xb,14,'2'); px(xb+1,14,'1'); px(xb+2,14,'1')
    px(xb,15,'3'); px(xb+1,15,'2'); px(xb+2,15,'1')
    px(xb+1,11,'4'); px(xb+1,25,'4')                    # croisement des bandes
    for y in (9,17,22): px(xb+1,y,'5')                  # rivets
    px(xb+3,10,'b'); px(xb+3,18,'b'); px(xb+3,23,'b')   # petite ombre portée des rivets
# --- planches du corps : joints sombres, chanfrein clair dessous, cassés ---
for y,xs in ((19,[(3,5),(10,12),(20,22),(27,29)]),(22,[(2,5),(10,12),(20,22),(26,29)])):
    for a,b in xs: seg(y,a,b,'b')
for x,y in ((3,20),(4,20),(11,20),(27,20),(28,20),(10,23),(21,23),(26,23)): px(x,y,'d')
# fibres du bois, par 2 ou 3, dans les tons moyens (I7)
for x0,x1,y in ((3,4,17),(11,12,16),(20,21,24),(26,28,17),(3,5,24),(27,28,9),(10,11,8),(3,4,10)): seg(y,x0,x1,'b')
# joints du dessus, peu (zone éclairée)
seg(5,11,13,'c'); seg(6,18,20,'c'); seg(5,26,27,'c'); seg(6,3,4,'c')
# --- serrure (accent saturé), largeur impaire centrée sur x16 ---
for y in range(8,13):
    px(14,y,'p'); px(15,y,'s' if y<10 else 'r'); px(16,y,'r'); px(17,y,'r' if y<11 else 'q'); px(18,y,'p')
px(15,8,'W'); px(19,9,'b'); px(19,10,'b')
for y in range(14,21):
    px(13,y,'p'); px(19,y,'p')
    for x in range(14,19): px(x,y,'r' if y<17 else 'q')
seg(14,13,19,'p'); seg(20,14,18,'p')
px(14,15,'W'); px(15,15,'s'); px(14,16,'s'); px(18,19,'p')
px(16,16,'p'); px(16,17,'O'); px(16,18,'O'); px(16,19,'p')   # trou de serrure
for y in range(15,22): px(20,y,'b')                    # ombre portée de la plaque
seg(21,14,20,'b')
# contour plus clair côté lumière (selout)
seg(3,3,28,'a'); px(2,4,'a')
# --- ombre au sol ---
seg(28,4,27,'S'); seg(29,7,24,'S')
if __name__=='__main__': vue([''.join(r) for r in G],PAL,'coffre_travail.png',k=14)
