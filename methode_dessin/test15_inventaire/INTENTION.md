# Test 15 — UI d'inventaire (128×128), vide

**B0 Intention.** Le sac d'un voyageur-arcaniste : un écrin de bois sombre cerclé de laiton,
garni de velours bleu nuit, où chaque case est un creux moulé dans le velours. Le joyau
rubis du cimier est l'œil du sac : seul accent saturé (point d'intérêt, A6-E).

**Usage.** Écran d'inventaire d'un RPG GBA : 20 cases (5×4), 4 onglets de catégorie
(runes ○ ◆ ✚ ▲), un compteur de pièces et une jauge de poids. Rien dans les cases.

**Projection (B0b).** UI = vue de face, aucune perspective. Les volumes sont des reliefs
(moulure de bois en relief, cases en creux).

**Lumière.** Haut-gauche, partout. Relief : haut et gauche clairs, bas et droite sombres.
Creux (cases, jauge) : **ombrage inversé** — les parois haut et gauche à l'ombre, les
parois bas et droite éclairées.

**Matières (A5-8b).** Bois (5 tons, veines dans le sens des montants), laiton (5 tons,
éclat), velours (mat, 5 tons, aucun éclat blanc), rubis (4 tons + éclat), parchemin (3 tons).

**Budget (A3, 128 px).** 5 tons par matière, trait `O` partagé. 26 couleurs au total.
Pour la GBA : 2 palettes BG de 16 (bois+laiton+parchemin / velours+rubis).

**Calques (E6) — de l'arrière vers l'avant.**
| Rang | Pièce | Fichier |
|---|---|---|
| 1 | cadre de bois + panneau de velours | `pieces/cadre.txt` |
| 2 | case (une seule pièce, posée 20 fois = cel lié) | `pieces/case.txt` |
| 3 | barre du bas (pièces + jauge) | `pieces/barre.txt` |
| 4 | onglets (actif / inactif) | `pieces/onglet_*.txt` |
| 5 | bossettes de coin (une pièce, 4 fois) | `pieces/bossette.txt` |
| 6 | cimier + rubis | `pieces/cimier.txt` |
| 7 | curseur de sélection | `pieces/curseur.txt` |

Chaque pièce suit le pipeline A5 (silhouette → contour → palette → lumière → matières →
détails → nettoyage) avec ses fichiers `cXX.txt` / `etapeXX.txt`, puis l'assemblage se fait
par `stamp` (`c90_assemblage.txt`).
