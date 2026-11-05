# Pieces dessinees a la main (R3). Lumiere haut-gauche : p clair, q pierre, r ombre, s joint/contour.
HST = ["rppppqqs",   # pierre de bord haut/bas, 8x5 (periode 8 = raccord des quarts)
       "pqqqqqrs",
       "pqqqqrrs",
       "qqqqrrrs",
       "srrrrsss"]
VST = ["rppqs",      # pierre de bord gauche/droit, 5x8
       "ppqqs",
       "pqqrs",
       "qqqrs",
       "qqqrs",
       "qqrrs",
       "qrrrs",
       "sssss"]
COIN = ["rpppppqs",  # gros galet de coin 8x8
        "ppqqqqqs",
        "pqqqqqrs",
        "pqqqqqrs",
        "qqqqqrrs",
        "qqqqrrrs",
        "sqrrrrss",
        ".sssss.."]
PETIT = ["rpqs",     # petit galet de coin interieur 4x4
         "pqrs",
         "qrrs",
         "ssss"]
# R5 : pierres identiques = mur de briques -> 2e pierre plus ronde, alternee (periode 16)
HST2 = ["ssrppqss",
        "rppqqqrs",
        "pqqqqrrs",
        "qqqrrrrs",
        "ssrrrssx"]
VST2 = ["srpps",
        "rppqs",
        "pqqqs",
        "pqqrs",
        "qqrrs",
        "qrrrx",
        "srrsx",
        "sssxx"]
KOI = ["K..KW..",    # koi nageant vers la droite : queue fourchue a gauche, taches blanches, ombre y
       ".KKWKKK",
       "K..KK..",
       "..yyy.."]
KOI_G = [r[::-1] for r in KOI]
LYS = [".LLxL.",     # nenuphar : encoche x, fleur W, ombre y
       "LLWLLL",
       "LLLLLL",
       ".LLLy.",
       "..yy.."]
