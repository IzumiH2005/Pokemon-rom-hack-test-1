# Test 14 : cheveux en appliquant C6b

Personnage original sur le même corps que le test 13 (toile 32×39, `etape01_base.txt` =
corps et visage du costume sans cheveux). Tenue recolorée en vert sauge par la palette.
Coupe : carré auburn mi-long, frange balayée vers la droite, mèches avant en pointe,
cheveux de dos plus sombres, une mèche rebelle sur le dessus. Lumière en haut à gauche.

Fichiers : `cheveux.py` (calque posé à la main, coordonnées commentées), `rendu.py`
(rendu, situation sur herbe, planche), `etape02_masse` → `etape03_ombre` → `etape04_final`.

## Ce qui vient de C6b
- Rampe 3 valeurs + reflet, avec glissement de teinte : orange (h) → rouge auburn (H) →
  bordeaux froid (D) → prune (X) ; reflet pêche pâle (L).
- Frange en 3 touffes de 2 px qui s'affinent à 1 px, pointes au-dessus des yeux.
- Ombre portée de la frange : seulement en haut des trous et sous chaque pointe.
- Reflet en arc cassé en tirets en haut à gauche ; un tiret clair par touffe de frange.
- Ombre du côté droit de largeur variable (pas de bande régulière).
- Selout : trait du haut à gauche en prune (X), trait du bas et de droite en O.
- Pas de trait noir entre cheveux et peau : le contraste de couleur suffit.
- Mèches avant claires qui finissent en pointe devant des cheveux de dos sombres
  (profondeur sans contour).
- Mèche rebelle posée en dernier comme accent.

## Pièges vus pendant le test
- 1er jet : carré en seau (côtés droits sur 14 rangées, bas plat) et traits de mèche en
  pointillés qui faisaient du bruit. Corrigé : côtés rentrés en haut et en bas, moins de
  lignes de mèche.
- Une ombre portée sur tout le bord en biseau de la frange faisait des rayures sur le
  front : réduite au haut des trous.
- Repeindre le visage sous la frange avait effacé le trait de la mâchoire et les cheveux
  de dos : on ne restaure que les pixels non vides de la base.
- Deux trous dans le trait (rangées 10 à 12) causés par l'ombrage posé sur le contour :
  l'ombre ne doit jamais remplacer un O.
