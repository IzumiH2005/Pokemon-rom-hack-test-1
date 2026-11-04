# Test 12 — L'herboristerie à la tour : journal des étapes

Chaque étape = `cXX.txt` (commandes) → `etapeXX.txt` / `.png` / `_vue.png`.
Outils : `../outils/` (trace.py, contour.py, px.py, planche.py).

## 64×64 (`b64/`)
| Étape | Contenu | Défaut relevé → correction |
|---|---|---|
| c01 | repères (sol, égout, faîtage, sablière, axes) + volumes | — |
| c02 | aplats par matière | pignon de lucarne d'1 rang trop court → corrigé dans c02 |
| c03 | lumière par face, ombres de surplomb, creux de porte, cylindre de tour, coins du cône | le faîtage passait sur le corps de la cheminée → corrigé en c04 |
| c04 | contour.py puis selout à la main (trait = ton sombre du matériau en haut/gauche), arêtes intérieures cône/toit, tour/maison, lucarne | — |
| c05 | porte à claveaux, enseigne feuille, fenêtres, colombages, tuiles, pierres, mousse, herbe, fumée | 42 pixels orphelins listés |
| c06 | nettoyage : q isolés sous les appuis, éclats de pierre (bruit), arêtes de pierre à 2 px, touffes regroupées | — |

21 couleurs (≤ 24). Final : `b64/batiment64.png`, planche : `b64/planche64.png`.

## 128×128 (`b128/`) — redessiné, pas agrandi
Même silhouette et mêmes repères d'identité (tour à cône, cheminée qui fume, enseigne à la feuille),
avec ce que le 64 ne pouvait pas porter : tuiles une par une, tuiles en arc sur le cône, épi,
pierres de cheminée, claveaux en rayons + clé de voûte, planches et pentures de porte,
rideaux, lanterne allumée, tonneau, lierre sur la tour, meurtrière.

| Étape | Défaut relevé → correction |
|---|---|
| c03 | les 3 rangs bas du toit passaient devant la tour → corrigé en c06 |
| c04 | pied de tour en escalier irrégulier → redessiné en arc (1-2-3 puis plat) |
| c05 | 69 orphelins listés ; gardés : reflets de feuilles, rivets, ombre des fleurs ; retirés : lèvres de tuiles coupées, arêtes cachées |

22 couleurs (palette 64 + `y` lumière de lanterne). Final : `b128/batiment128.png`, planche : `b128/planche128.png`.

Contrôle gris : toit, plâtre et pierre se séparent ; le toit et la tour sont proches en valeur mais
se distinguent par la texture et le trait.
