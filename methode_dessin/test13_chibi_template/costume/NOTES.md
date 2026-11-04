# Variante costume (même template, même corps)

Demande : coupe et tenue d'après une image de référence (non versionnée). Seuls la coupe et
la tenue changent ; corps, peau, yeux et trait du template restent ceux du test 13.

- **Tenue** (`c04`, `c04b`) : veste beige à revers, chemise claire en V, cravate sombre
  (couleur du trait), poignets de chemise au-dessus des mains, pantalon du même tissu,
  chaussures sombres. Ourlet de veste en trait propre.
- **Coupe** (`c06`, `c06b`) : blonde, courte, en pointes relevées ; la masse s'évase sur les
  côtés en haut ; front dégagé avec deux mèches qui retombent.
- **Pièges vus** : pointes régulières = couronne, les rendre inégales et évasées ; la
  naissance des cheveux contre la peau faisait un bandeau sombre, éclaircie au centre ; une
  masse trop haute de 2 rangées cachait le front (compter les paires de `rows`).
- 15 couleurs.

## Retour : « une partie des cheveux est plate »
- Cause : en 24×35 il n'y avait que 2 rangées au-dessus du crâne, donc les pointes étaient écrasées en une bande plate.
- Correction : toile élargie à 32×39 (+4 px à gauche, à droite et en haut, `etape05b_toile32.txt`). Le corps et le visage ne bougent pas, ils sont seulement décalés de (+4, +4).
- Cheveux redessinés en dôme hérissé : des pointes de hauteurs inégales en haut, des dents sur les côtés, et une masse qui déborde du crâne de 2 px pour donner du volume.
- Pièges vus : six traits de mèche (`px D`/`px h`) posés sur le contour. Je les ai retirés après une vérification automatique (aucun O du contour ne doit disparaître).
- Les O du template sous les cheveux (le haut du crâne) sont recouverts exprès, comme dans la version 24×35.

## Retour : 2e référence (coupe courte en bataille)
- Ce qui a changé : la masse colle au crâne (+1 à 2 px) au lieu de former un casque. Les pointes ont chacune leur direction : vers le haut, en diagonale, à l'horizontale sur les côtés.
- Des mèches partent dès le niveau des oreilles (rangées 14 à 18) et descendent vers l'extérieur. J'ai gardé le blond, car la demande portait sur la forme.
- Asymétrie voulue : une pointe horizontale à gauche et une pointe en diagonale vers le haut à droite, pour éviter l'effet couronne.
- Piège rencontré : une pointe de 1 à 2 px d'épaisseur devient entièrement du contour. Il faut au moins 3 px sur 2 rangées pour qu'il reste de la couleur.
- J'ai aussi gardé une mèche qui tombe sur le front (x13-14) et la naissance des cheveux claire au centre.
