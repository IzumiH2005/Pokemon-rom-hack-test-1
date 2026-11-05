# Laboratoire 3/4 vue de dessus (112×80) — journal

Toit y0-47 (60 %), façade y48-76, marche y77-79. `gen.py` écrit chaque étape (`cXX.txt` = pixels posés, `eXX.txt` = état).

| Étape | Décision | Défaut (R5) → correction |
|---|---|---|
| 01 A/B | A : lanterneau sur le faîtage ; B : pignon chidori-hafu au-dessus de l'entrée | B retenue : distincte de la maison, marque l'entrée |
| 02 | croupes D/B, pan avant C, pignon D/B + face bois w, façade reprise du labo validé (4 rangs retirés) | pignon en triangle = pyramide → vu de dessus le faîtage pointe vers nous : noues en V puis rives verticales |
| 03 | bas des croupes plus sombre, face droite du pignon v, ombre portée du pignon (dessous + droite) | — |
| 04 | contour O dehors, selout A/B sur le toit, arêtiers, planches de rive t | — |
| 05 | cannelures 4 px, reflet sous le faîtage, rangs de tuiles des croupes, onigawara, bouts de tuiles rondes | cannelures du petit toit verticales → horizontales (ses pans descendent sur les côtés) |
| 06 | nettoyage rive gauche | — |

Porte : colonne x64-79, y48-79 → `portes.py labo34 labo.txt 64 48 66 57 77 74`.

## v2 — refonte à la main (plus de gen.py à formules, R3)
Même langage que la maison (rime A4b) : même escalier d'arêtier, même faîtage, mêmes onigawara, même égout relevé.
Pignon d'entrée au-dessus de la porte (x59-84) : versant gauche D / droit B, noues = creux A (pas 2,1),
rives verticales, ombre portée du pignon sur le pan avant (B, 2 px à droite), planches de rive Q/q,
face en bois v avec 3 lattes inégales, gegyo doré à l'apex (accent saturé, au-dessus de l'entrée).

| Étape | Défaut (R5) → correction |
|---|---|
| c11 | ailes fines aux coins hauts (bruit de silhouette) → chanfrein comme la maison |
| c12 | pignon « livre ouvert » sans planches de rive → planches Q/q + dessous t |
| c14 | cannelures 4 px partout (tôle) → tuiles pleine longueur 1 marche, lèvres sur 3 rangs, arrêtées sur le pignon |
