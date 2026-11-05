# Maison 3/4 vue de dessus (80×80) — journal

Toit à croupes y0-47 (60 %), façade y48-76, seuil y77-78. Porte : colonne x48-63, y48-79.

| Étape | Décision | Défaut (R5) → correction |
|---|---|---|
| 01 A/B | A : croupe simple ; B : irimoya (croupe + petits pignons) | B retenue |
| 02 | pan arrière D, faîtage C/B/A, croupe gauche D, droite B, pan avant C, mur plâtre Q / bois u | croupes arrêtées à mi-pente → remplissage par rang depuis les arêtiers ; mur même couleur que le toit → matière différente |
| 03 | ombre de l'avant-toit sur le mur, pignons éclairé/ombre, poteaux | pignons en coin → triangles droits |
| 04 | contour (contour.py), selout A/t, arêtiers | assombrissement rectangulaire = trou → retiré |
| 05 | cannelures 4 px, onigawara, tuiles rondes, koshi, shoji, noren, chōchin | paillettes D = bruit → reflet continu sous le faîtage |
| 06 | nettoyage | trous des épis → comblés D |

Portes : `portes.py maison34 maison.txt 48 48 50 58 61 75`. Variante rouge : `maison_rouge.txt` (N→R, n→r).

## v3 — refonte du toit (doc relu en entier)
Intention (B0) : toit à croupes (yosemune) en kawara, coins d'égout relevés, faîtage à onigawara ;
point d'intérêt = l'entrée (noren + mon blanc, plus fort contraste). Formes : grand = toit, moyen = façade, petit = noren/lanterne.

| Étape | Décision | Défaut (R5) → correction |
|---|---|---|
| c11 | 2 silhouettes : B carrée (`e11B_carre.txt`), A coin arrière chanfreiné + égout relevé (pas 1,1,1,2) → A retenue. Arêtier en escalier 3-2 choisi à la main. Une valeur par face : croupe gauche D, pan avant C, croupe droite B | — |
| c12 | faîtage en relief (dessus D/Q, corps B, dessous A), ombre portée plus courte que lui, arêtiers = crête D + ombre B/A, onigawara éclairés à gauche | faîtage C sur pan C illisible → corps B ; reflet Q raccourci au côté lumière |
| c13 | contour A, selout B côté lumière (haut/gauche) | — |
| c14 | tuiles rondes du faîtage à l'égout en 1 marche (B sur C), arrêtées sur les arêtiers ; lèvres claires sur 3 rangs (sous le faîtage + 2 rangs bas) ; tirets sur les croupes | v1 (`c14_v1_coulures.txt`) : ribs commencés au milieu du pan = coulures → ribs pleine longueur, relief seulement aux lèvres |
| c15 | nettoyage | trous du noren dans la silhouette → enduit ; 2 carrés blancs = « yeux » → un mon en anneau ; point Q orphelin → retiré |

Palette (A6-A) : A plus froid `#303058`, D plus chaud `#a0a8b8`.
Bilan planche — bien : silhouette claire en noir, faces séparées en gris, entrée = point d'intérêt.
À améliorer : croupes un peu vides, mur bas sombre uniforme, pas de mousse (palette pleine).
