# Test 14 : cheveux en appliquant C6 (ex-C6b)

Personnage original sur le même corps que le test 13 (toile 32×39, `etape01_base.txt` =
corps et visage du costume sans cheveux). Tenue recolorée en vert sauge par la palette.
Coupe : carré auburn mi-long, frange balayée vers la droite, mèches avant en pointe,
cheveux de dos plus sombres, une mèche rebelle sur le dessus. Lumière en haut à gauche.

Fichiers : `cheveux.py` (calque posé à la main, coordonnées commentées), `rendu.py`
(rendu, situation sur herbe, planche), `etape02_masse` → `etape03_ombre` → `etape04_final`.

## Ce qui vient de C6 (ex-C6b)
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

## Variante « anime » (`anime.py` → `etape05_anime`, `comparaison.png`)
Même corps, même palette ; la coupe est poussée vers le style anime :
- **Silhouette plus grosse** (le dôme monte jusqu'à la rangée 3) avec une **pointe épaisse
  vers l'extérieur** de chaque côté, à hauteur des joues (gauche plus haute que droite).
- **Ahoge** : une grande mèche courbée qui sort du haut du crâne (3 px de large).
- **Frange** en 3 pointes inégales + une **longue mèche centrale** qui descend entre les yeux.
- **Mèches avant longues** jusqu'aux épaules, 4 px qui s'affinent.
- **Cel-shading** : aplats nets, pas de dégradé. Chaque pointe de frange a son côté droit
  sombre et son côté gauche éclairé.
- **Anneau de reflet** (angel ring) en dents de scie qui suit le crâne.
- Masque des cheveux défini à la main, trait posé automatiquement là où les cheveux
  touchent le vide ou les vêtements, jamais la peau.

Pièges vus :
- 1er jet : pointes extérieures et longues mèches trop fines, entièrement en trait (règle
  des 3 px sur 2 rangées). Épaissies.
- Colorer en D toute la colonne d'une pointe de frange en fait une rayure sombre sur le
  visage : la pointe reste claire, seule la colonne voisine passe en D.
- Des mèches qui descendent devant les mains se mêlent au trait des bras : arrêtées à la
  rangée 26.
