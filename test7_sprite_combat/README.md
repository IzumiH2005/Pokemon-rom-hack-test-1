# Test 7 : sprite de combat d'Aventurine

But : créer le sprite de **combat** (image de face, 64×64) d'Aventurine en partant de celui de **Brendan**, modifié **pas à pas** (la tête de Brendan est gardée et retouchée, pas redessinée).

## Images
- `1_reference_base_resultat.png` : référence, Brendan d'origine, résultat.
- `2_etapes.png` : les 11 étapes, de Brendan à Aventurine.
- `3_tete_pas_a_pas.png` : zoom sur la tête (casquette → cheveux, contour, frange, mèches).
- `4_en_combat.png` : capture dans l'émulateur, « Un combat est lancé par GENTLEMAN AVENTURINE ! ».

## Les étapes
1. Recoloration auto du corps + casquette et bandeau transformés en cheveux blonds (yeux bleus).
2. Contour des cheveux en brun (au lieu du noir/bleu de la casquette).
3. Frange en pointes sur le front.
4. Mèches sur les côtés du visage.
5. Veste noire, chemise turquoise, sacoche → éléments dorés.
6. Manches longues noires, gants noirs, jeton doré dans la main (à la place de la Poké Ball).
7. Pantalon blanc.
8. Col en fourrure blanche.
9. Pans de cape dorés avec le bas turquoise.
10. Finitions du gant.
11. Pli du pantalon adouci (il dessinait un « R » façon Team Rocket).

## Dans le jeu
- Nouveau dresseur `TRAINER_AVENTURINE` (classe Gentleman), équipe : Ténéfix N.6, Gromago N.7.
- Le PNJ de Bourg-en-Vol : si l'équipe est vide, il donne un Poussifeu N.10, puis lance le combat.

## Fichiers
- `aventurine_combat.png` / `.pal` : sprite final (16 couleurs indexées) + palette.
- `steps.py` (+ `btk.py`, `g0.txt`) : toutes les étapes, pixel par pixel.
- `install_combat.py` : installe le sprite, le dresseur et le script dans pokeemerald-expansion.
