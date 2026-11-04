# Test 13 : notes d'étapes

| Étape | Fichier commandes | Résultat |
|---|---|---|
| 01 reproduction du template | (grille recopiée) | `etape01_template.txt` : 0 pixel d'écart avec l'image fournie |
| 02 aplat de peau, yeux recolorés | `c02.txt` | `etape02_peau` |
| 03 ombres du corps | `c03.txt` | `etape03_ombres` (corps validé) |
| 04 calque vêtements | `c04.txt`, contour, `c04b.txt` | `etape04_vetements` |
| 05 visage | `c05.txt` | `etape05_visage` |
| 06 calque cheveux + barrette | `c06.txt`, contour ×2, `c06b.txt` | `etape06_cheveux` |
| 07 nettoyage | `c07.txt` | `etape07_final` |
| 08 budget couleurs (19 → 14) | `c08.txt` | `etape08_final`, `planche_finale.png` |

## Erreurs et corrections (règle 4)
- **c03** : deux `vline` d'ombre trop longues ont écrasé 3 pixels du trait du template
  (x15 r22, x19 r6-7). Le contour du calque vêtements s'est alors propagé de travers.
  Corrigé dans `c03.txt`, puis tout relancé. Ajout de `verif_trait.py`, qui vérifie après
  chaque étape qu'aucune peau n'a remplacé le trait du template.
- **c06** : le contour contre la peau en brun foncé faisait une bande sombre sous toute la
  frange (lecture « sourcils froncés »). Frange remise en ton de base au centre, sombre
  seulement sur les côtés, ombre portée d'1 rangée sur le front.
- **c06b** : une ombre de mèche posée sur le trait du crâne (x20 r7) : raccourcie.
- **Manches** : le contour contre la main transformait la manche entière en trait ; un
  revers de 1 px remplace le trait (clair à gauche, sombre à droite).

## Ce que le template impose
- Corps très fin (torse de 8 px) : le tissu reste dans le trait du template sur le torse
  au lieu de déborder d'1 px ; seuls l'ourlet et les cheveux passent par-dessus le trait.
- Mains de 2 px de large : les manches longues ne laissent qu'une rangée de main.
- Jambes de 2 px : une rangée de peau, puis revers et botte.

## Retouche après retour (v2)
- **Bouche retirée** (`c05`) : le pixel brun sous les yeux se lisait comme un nez.
- **Coupe anime** (`c06`, `c06b`) : trois pointes sur le dessus, toutes penchées vers la
  droite (mèches balayées) ; frange en trois mèches avec une longue pointe centrale qui
  descend entre les yeux ; mèches de côté évasées vers l'extérieur.
- **Piège vu** : des pointes symétriques aux deux coins du crâne se lisent comme des
  oreilles de chat. Les pencher dans le même sens.
- **Piège vu** : une pointe d'1 px de large devient tout trait au contour ; il faut une base
  de 3 px sur 3 rangées pour garder 1 px de couleur dedans.
