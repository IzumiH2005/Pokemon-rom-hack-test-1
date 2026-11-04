# Test 18 — Chevalier squelette venu de l'au-delà, 128×128, en pied

## Intention (C0)
Squelette original en armure de chevalier spectral, debout, lumière en haut à gauche, fond transparent.
Épée longue tenue basse à gauche, flamme spectrale dans la paume levée à droite.
Accent saturé unique : cyan-vert spectral (orbites, flamme, runes de la lame, panache, sigil du tabard).
Armure **asymétrique en diagonale** : grande épaulière + gantelet en haut à gauche,
genouillère + jambière + soleret en bas à droite. Os laissés nus : main de la flamme, pied gauche,
coude d'épée, côtes visibles par la cassure du plastron.

## Références (recherche)
- [pixie.haus – undead knight](https://pixie.haus/pixelart/544608/undead-knight-sword-shield-pose)
- [pixie.haus – skeletal warrior 128×128](https://pixie.haus/pixelart/559350/skeletal-warrior-ready-stance-128x128)
- [pixie.haus – undead warrior dark armor](https://pixie.haus/pixelart/597721/undead-warrior-dark-armor-ominous-stance)
- [Proko – cage thoracique](https://www.proko.com/how-to-draw-the-rib-cage-step-by-step)
- [Art in Context – squelette](https://artincontext.org/how-to-draw-a-skeleton)

## Étapes (une forme par calque, vérifiée à la vision après chaque passe)
construction (7 têtes) → 2 silhouettes (A gardée, B rejetée : épée mal placée) → A2 (cape étroite) →
**squelette seul** : crâne → cou + clavicules → cage (cavité d'abord, côtes ensuite) → lombaires + bassin →
bras (radius/cubitus séparés) + mains → jambes (tibia/péroné) + pieds → planche du squelette →
**armure pièce par pièce** : heaume → panache émissif → gorgerin → plastron brisé → épaulière →
canon + gantelet → ceinture/boucle/tassette/tabard → genouillère/jambière/soleret → cape → épée
(lame, garde, poignée, pommeau) → effets (flamme, reflets sur les doigts, étincelles, volutes) →
assemblage (`assembler.py`) → contour sélectif (`selout.py`) → planche.
Voir `etapes_chevalier.png`.

## Corrections faites
- Silhouettes A/B : cape en bloc qui mangeait le squelette et le vide sous le bras levé → cape étroite, bord droit presque vertical, 3 lambeaux.
- Mâchoire trop large et carrée → resserrée, dents du haut et du bas séparées.
- Cage hachée → repeinte rangée par rangée : côtes de 2 px, cavité de 1 px, sternum, arche costale ouverte ;
  côtes « radiateur » → bouts courbés vers le bas ; côté droit trop sombre → éclairci d'un cran.
- Bas du bassin confus → deux anneaux obturateurs nets.
- Épaulière en barres empilées → lames qui descendent et s'inclinent en suivant le bras.
- Boucle de ceinture confondue avec le cuir → cuir foncé + reflet sur la boucle.
- Garde d'épée en fil de 1 px → garde de 4 px centrée sur le haut de la lame, quillons.
- Trou de 3 rangées dans la cape (y77-79) → comblé.
- Volute isolée qui flottait trop loin sous la cape → retirée.
- **Retour : cape et panache trop rigides** (diagonales droites, bandes parallèles, bord presque rectiligne).
  - Panache refait (`c21_panache.py`) : 3 rubans en S posés point par point, épaisseur qui s'affine
    jusqu'à une pointe recourbée, cœur lumineux le long de chaque ruban, étincelles près des pointes.
    Il occupe maintenant tout l'espace libre à gauche du heaume.
  - Cape refaite (`c28_cape.py`) : bord droit qui gonfle puis s'évase jusqu'à x120, 4 grands plis en S
    qui se resserrent vers l'épaule, flanc éclairé large à gauche de chaque crête et flanc d'ombre court
    à droite, 5 lambeaux de longueurs différentes qui se courbent vers la droite en descendant.
  - Nouvel outil `../outils/tube.py` : peint un ruban émissif autour d'une ligne médiane posée à la main.

## Défauts restants
- Le soleret reste un peu « en escalier » ; la pointe pourrait être arrondie.
- Le canon d'avant-bras avance par marches (tube penché sur peu de pixels).
- La main levée est un peu raide (doigts parallèles).

## Outil
`trace.py` a gagné l'op `line C x1 y1 x2 y2` (segment entre deux points décidés).
