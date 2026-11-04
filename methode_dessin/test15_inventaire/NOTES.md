# Test 15 — Inventaire RPG 128×128 (UI vide), dessiné en calques

Résultat : `inventaire.png` (×1), `inventaire_x4.png`, `planche.png` (contrôle A5-11),
`situation.png` (écran GBA 240×160 en pause), `calques.png` (chaque pièce seule).
Intention, palette et ordre des calques : `INTENTION.md`.

## Méthode suivie
1. **Construction** (`c00`, R/B/V) : axe, masse de l'écrin, repères de la grille 5×4, de la
   barre, des onglets ; volumes du cimier et des bossettes.
2. **Chaque pièce passe seule dans le pipeline A5**, avec ses fichiers :
   - cadre : `c01` silhouette → contour (`contour.py`) → `c03` lumière (moulure, coupe
     d'onglet, feuillure, ombre portée sur le velours) → `c04` matières (veines par groupes,
     couture en tirets 2/2) ;
   - case : silhouette dessinée à la main → `c06` creux à ombrage inversé + rune vide ;
     essai de grille `c07` ;
   - barre : `c08` (logement de pièce dessiné à la main, plaque, jauge en creux) ;
   - onglets : gabarit et runes dessinés à la main, posés par `onglets.py` (l'inactif est
     le même dessin un ton plus bas) ;
   - bossette, rubis, curseur : grilles écrites à la main ;
   - cimier : `c09` silhouette → contour → `c11` lumière de l'or, rubis serti, nettoyage.
3. **Assemblage** `c90` par `stamp`, de l'arrière vers l'avant (E6-B) : onglets inactifs
   → cadre → 20 cases → barre → onglet actif → bossettes → cimier → curseur.
4. **Planche**, défauts notés et corrigés, nouvelle planche.

`trace.py` a gagné la commande `stamp piece.txt x y` (prévue par E6-E) : elle pose une
pièce telle quelle, les `.` restent transparents.

## Défauts trouvés à la planche et corrigés
- Runes des onglets inactifs invisibles (même ton que le fond) → rune `n` sur fond `l`.
- Plaque du compteur en parchemin trop claire : elle volait le contraste du rubis (point
  d'intérêt, A6-E) → fond `p`, chanfrein `P`, ombre `c` ; une couleur de moins (`Q`).
- Bouts de la bride du cimier carrés et raides → coins arrondis.
- Éclat posé sur l'or clair du bout de bride : perdu (leçon T15) → retiré ; l'éclat reste
  en haut de la monture, contre le trait.
- Rivets de la bride sombres en haut et clairs en bas : lus comme des trous → inversés.

## Leçons
- **Creux d'UI = ombrage inversé** : parois haut/gauche à l'ombre, parois bas/droite
  claires, plus une lèvre claire d'1 px sur le velours en bas et à droite. Sans la lèvre,
  la case se lit comme un carré sombre posé dessus, pas comme un trou.
- **Cel lié** : la case est dessinée une fois et posée 20 fois ; une retouche la corrige
  partout. Une pièce **symétrique** (bossette ronde) se réutilise aux 4 coins sans casser la
  lumière ; une pièce **asymétrique** (coins du curseur) se dessine coin par coin, jamais en
  miroir, sinon la lumière passe à droite.
- **L'ordre des calques donne la profondeur** : les onglets inactifs, posés avant le cadre,
  passent dessous et paraissent derrière ; l'actif, posé après, est devant et plus haut.
- **Un seul accent saturé** (rubis) ; l'or ne sert qu'aux pièces qu'on touche (curseur,
  cadre de jauge, logement) ; le velours reste mat et calme, sans éclat.
- **Couleurs** : 23 au total ; elles tiennent dans 2 palettes BG GBA de 16 :
  chaud `O a b c d e h i j y z p P` (13) et froid `O k l m n q r s t u w` (11).

## v2 — rebords dorés retravaillés (demande utilisateur)
- **Jauge** : le cadre d'or plat d'1 px devient une moulure à deux tons (bourrelet clair +
  filet moyen en haut et à gauche, filet et bourrelet sombres en bas et à droite), coins
  chanfreinés, éclat de 3 px au coin haut-gauche. Plaque et jauge passent à 10 px de haut,
  alignées sur le logement de pièce.
- **Plaque** : les deux clous sont remplacés par quatre **coins de laiton** de registre
  (triangle clair en haut-gauche, sombre en bas-droite, arête en `h`).
- **Cimier** (`c12_cimier_volutes.txt`) : les bouts carrés de la bride deviennent des
  **volutes**, un anneau d'or autour d'un œil `O`. Les anciens rivets disparaissent.
- **Curseur** : chaque équerre a un bout **taillé en biais** (le filet intérieur dépasse
  d'1 px), et l'ombre tourne avec le coin (clair en haut-gauche, sombre en bas-droite).
- Leçon : un filet d'or d'1 px se lit comme un trait de couleur ; à partir de 2 tons
  (clair + sombre) il se lit comme du métal en relief.

## v3 — coins de coffre (remplacent les bossettes)
- Les 4 bossettes rondes sont remplacées par des **équerres de laiton** de 16×16
  (`coins.py` → `pieces/coin_{hg,hd,bg,bd}.txt`) : une plaque en L qui enveloppe l'angle,
  deux bras courts finis en lobe arrondi avec une rainure, et un **dôme de rivet** dans l'angle.
- Le coin haut-gauche est dessiné à la main en étiquettes de biseau (haut, gauche, plat,
  droite, bas). Les trois autres en sont des miroirs, avec échange des biseaux pour que la
  lumière reste en haut à gauche partout.
- Leçons :
  - le dôme collé au bord de la plaque crée un double trait : le décaler d'1 px ;
  - un dôme du même ton que la plaque disparaît : corps en clair (y) et reflet z de 3 px ;
  - les bras du haut sont limités par l'onglet actif (x18).
