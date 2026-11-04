from base import *
# ---------- ETAPE 0 : intention
# Jeune femme samourai, mot cle CALME. 3/4 tournee vers la gauche de l'image.
# Format libre (R12) -> 128x192, personnage ~178 px, 7 tetes, semi-realiste.
# Lumiere en haut a gauche, devant. Forme dominante : triangle (hakama en A).
# Montrer l'anatomie (R13) : manches relevees par un tasuki -> avant-bras nus.
TOP, BOT = 8, 186
HH = (BOT - TOP) / 7          # 25.4 px
R = {k: round(TOP + HH * v) for k, v in dict(menton=1, epaules=1.3, seins=2, nombril=2.75,
     entrejambe=3.5, genou=5.1, cheville=6.8, pied=7).items()}
# ---------- ETAPE 2 : squelette (donnees)
J = dict(
    crane=(60, 21), menton=(55, 33), nuque=(62, 33), cou=(59, 41),
    ep_loin=(45, 44), ep_pres=(79, 47),
    coude_loin=(39, 76), poig_loin=(43, 102), main_loin=(44, 118),
    coude_pres=(91, 75), poig_pres=(78, 92), main_pres=(72, 96),
    taille=(61, 76), bassin=(61, 88),
    hanche_loin=(50, 93), hanche_pres=(73, 90),
    genou_loin=(46, 137), genou_pres=(67, 136),
    chev_loin=(43, 178), chev_pres=(62, 179),
    pied_loin=(34, 185), pied_pres=(53, 186),
)
OS = [("crane","nuque"),("nuque","cou"),("cou","ep_loin"),("cou","ep_pres"),
      ("ep_loin","coude_loin"),("coude_loin","poig_loin"),("poig_loin","main_loin"),
      ("ep_pres","coude_pres"),("coude_pres","poig_pres"),("poig_pres","main_pres"),
      ("cou","taille"),("taille","bassin"),("bassin","hanche_loin"),("bassin","hanche_pres"),
      ("hanche_loin","genou_loin"),("genou_loin","chev_loin"),("chev_loin","pied_loin"),
      ("hanche_pres","genou_pres"),("genou_pres","chev_pres"),("chev_pres","pied_pres")]
if __name__ == "__main__":
    import math
    g, d = guide()
    for i in range(8):
        y = TOP + HH * i
        d.line([P(0, y), P(W - 1, y)], fill=(60, 90, 220, 160))
        d.ellipse([P(110 - 9, y + 1), P(110 + 9, y + HH - 1)], outline=(60, 90, 220, 200))
    for k, y in R.items():
        d.line([P(2, y), P(20, y)], fill=(60, 90, 220, 255), width=2); d.text(P(2, y - 4), k, fill=(40, 60, 180, 255))
    im1 = on_bg(g); im1.save(f"{OUT}/etape_01_grille.png")
    # ligne d'action + epaules / bassin opposes + gravite
    d.line([P(60, 10), P(58, 40), P(63, 90), P(62, 180)], fill=(230, 40, 40, 255), width=3)
    d.line([P(*J["ep_loin"]), P(*J["ep_pres"])], fill=(240, 120, 0, 255), width=2)
    d.line([P(*J["hanche_loin"]), P(*J["hanche_pres"])], fill=(240, 120, 0, 255), width=2)
    d.line([P(*J["cou"]), P(J["cou"][0], 186)], fill=(0, 160, 0, 200), width=1)
    for a, b in OS:
        d.line([P(*J[a]), P(*J[b])], fill=(200, 0, 0, 255), width=3)
    for k, v in J.items():
        d.ellipse([P(v[0]-1, v[1]-1), P(v[0]+1, v[1]+1)], outline=(0, 0, 0, 255), width=2)
    d.ellipse([P(49, 8), P(71, 33)], outline=(200, 0, 0, 255), width=2)
    on_bg(g).save(f"{OUT}/etape_02_squelette.png")
    L = lambda a, b: round(math.dist(J[a], J[b]), 1)
    print(R)
    print("bras loin", L("ep_loin","coude_loin"), L("coude_loin","poig_loin"), "pres", L("ep_pres","coude_pres"), L("coude_pres","poig_pres"))
    print("cuisse", L("hanche_loin","genou_loin"), L("hanche_pres","genou_pres"), "jambe", L("genou_loin","chev_loin"), L("genou_pres","chev_pres"))
