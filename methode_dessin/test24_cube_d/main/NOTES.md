# Le Dé dans la main de Red

Le script `main_de.py` peint le mini-Dé sur les frames 5 à 8 du sprite « objet » de Red.
Il prend le sprite source en argument : le dépôt ne contient aucun pixel de Red.

Trois poses existent. DE_BAS montre le Dé tenu bas, DE_TERNE le montre levé et éteint, DE_ALLUME le montre levé et brillant.

Le Dé utilise les indices 5, 13 et 14, que la pose de Red n'emploie pas.
Le jeu sauve ces trois couleurs, les remplace par l'orange, le jaune et l'ocre du Dé, puis les rend quand Red range l'objet.
Le Dé garde ainsi ses couleurs quand Red devient gris.

En jeu, le special `Prologue_RedDe` pilote l'animation avec VAR_0x8004 : 0 lève le Dé, 1 le fait briller, 2 le range.
