# Test 17 — Troll moussu 128×128

## Intention (C0)
Troll original, buste de 3/4 tourné vers la gauche, voûté, grincheux et méfiant.
Marqueurs : gros nez bulbeux qui tombe, longue oreille pointue, grande défense + défense cassée,
mousse sur la bosse du dos et lichen sur le crâne. Accent saturé unique : les yeux ambre.
Lumière en haut à gauche.

## Références (recherche)
- [Polycount](https://polycount.com/discussion/comment/2758764)
- [ZBrushCentral – troll WIP](https://www.zbrushcentral.com/t/troll-wip/309413) (nez type nasique)
- [Bleeding Cool – Troll Hunter](https://www.bleedingcool.com/2011/09/01/a-guide-to-recognising-your-trolls-concept-art-from-the-troll-hunter/) (voûté comme un vieillard)
- [W3C – Kittelsen](https://www.w3.org/People/Bos/kittelsen.html) (mousse, pierre, racines)
- [pixie.haus – troll](https://pixie.haus/pixelart/12004/stout-green-troll-menacing-grin-fantasy-creature)

## Étapes (un calque par forme, vérifié à la vision après chaque passe)
construction → 2 silhouettes (A gardée, B rejetée) → A2/A3 → placement des traits → fond → plats →
nez → front/yeux → œil proche → bouche/mâchoire → défenses → joue/oreille → crâne/cou →
mousse → corps → nettoyage. Assemblage : `assembler.py`, peinture à la main : `../outils/peindre.py`.

## Corrections faites
- Bosse trop basse (troll trop droit) → remontée.
- Nez perdu dans la mâchoire, crâne en boule → silhouettes A2 puis A3.
- **Anatomie 3/4** : les deux yeux étaient du même côté du nez → racine du nez remise entre les yeux,
  œil lointain à gauche de l'arête, œil proche décalé à droite.
- Mousse en grille/écailles → touffes de 4 tailles, posées sans grille, bord haut déchiqueté,
  clair en haut-gauche, sombre en bas-droite ; manteau prolongé jusqu'en bas.
- Arcade en longue bande claire → deux arcades avec un creux à la racine du nez.
- Lèvre inférieure en bandes plates → bourrelet arrondi, reflet court à gauche.
- Corps plat → dôme d'épaule lointaine (un cran plus sombre), pli d'aisselle courbe, pectoral en arc.
- Plats non peints entre mâchoire et mousse (colonne x≈86) → cou en ombre.
- Orphelins repérés et corrigés un par un (`c19_nettoyage.txt`).

## Défauts restants
- Ligne de bouche encore très droite.
- Légère couture horizontale dans la mousse vers y≈87 et sous le menton vers y≈99.
- Test silhouette de la planche inutile ici (fond opaque).
