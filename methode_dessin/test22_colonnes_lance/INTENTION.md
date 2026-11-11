# Test 22 : les colonnes des Colonnes Lance

Les colonnes de Platine, rendues depuis leurs modèles 3D, paraissaient floues et texturées sur la carte GBA. On les redessine à la main, dans le style des objets de Rouge Feu et d'Or HeartGold : contour sombre et chaud, aplats, 4 à 6 tons de pierre.

- Usage : objets posés sur l'esplanade de la carte `MAP_COLONNES_LANCE`, deux métatuiles de large.
- Projection : vue 3/4 de dessus, comme les bâtiments du jeu. On voit le dessus du socle et la face avant du fût.
- Lumière : en haut à gauche. Le côté gauche du fût reçoit la lumière, le côté droit tombe dans l'ombre.
- Matière : pierre taillée claire, un ton par face, cannelures verticales, joints de tambours perpendiculaires au fût.
- Rampe : O #362c28, D #5d5040, d #7e7152, m #a69a70, B #c9bd92, L #e4dab4, W #f7f0d4. Pas d'accent saturé : la scène porte ses couleurs (Dialga, Palkia).

Pièces (dossier `pieces/`) : socle octogonal 30x14, rangée de fût cannelé 20x1, sommet pointu 20x26, sommet brisé 20x26. Chaque colonne s'assemble par `stamp` de ces pièces à des positions décidées.

Tailles : pointues 104, 88 et 72 px ; brisées 100, 84 et 70 px. Le bloc effondré (modèle 514) se dessine à part.
