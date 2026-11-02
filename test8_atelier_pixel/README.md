# Test 8 — Atelier pixel (sprite de combat d'Aventurine, version 2)

Un petit outil (`studio/studio.py`) pour dessiner pixel par pixel avec un retour visuel immédiat. Après chaque modification, il génère `view.png` avec :
- la référence (zone recadrée : tête, buste, jambes…) ;
- la zone de travail zoomée, avec une grille et les pixels modifiés entourés en magenta ;
- la base d'origine (Pierre Rochard) ;
- le sprite entier en x3 et en x1 ;
- un aperçu sur fond de combat ;
- la palette.

## Commandes
```
python3 studio.py ed "<cmds>" [x0,y0,x1,y1] [tete|buste|jambes|mains|tout]
python3 studio.py view [zone] [ref]
python3 studio.py undo
```
Les commandes sont séparées par `;` :
- `p x y c` : un pixel ;
- `r y x0 chaine` : une ligne de pixels (`_` = ne pas toucher) ;
- `f x0 y0 x1 y1 c` : un rectangle ;
- `map x0 y0 x1 y1 ab:cd` : remplace a par b et c par d dans la zone.

Chaque étape est enregistrée dans `studio/hist/`.

L'image de référence (`ref_a.png`) n'est pas incluse : mets la tienne à côté de `studio.py`.

## Images
- `1_comparaison.png` : référence / base / test 7 / test 8
- `2_etapes.png` : progression étape par étape
- `3_outil_vue.png` : ce que je vois pendant le dessin
- `4_en_combat.png` : capture dans le jeu

## Installation
Copier `aventurine_combat.png` vers `graphics/trainers/front_pics/aventurine.png` et `aventurine_combat.pal` vers `graphics/trainers/palettes/aventurine.pal`. Le dresseur doit déjà être déclaré : voir `test7_sprite_combat/install_combat.py`.
