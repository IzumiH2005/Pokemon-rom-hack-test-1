# Ce qu'on peut faire (et ne pas faire) dans le hack

Base : pokeemerald-expansion. Ce document sert à trier les idées de l'histoire :
ce qui est faisable, ce qui demande du travail, ce qu'il faut écarter.

## 1. Cartes et contenu : Émeraude + Rouge Feu en même temps

- Toutes les cartes d'Émeraude (Hoenn, Zone de Combat…).
- 419 cartes Rouge Feu / Vert Feuille : tout Kanto + les îles Sevii.
- Les décors (tilesets) des deux jeux : 64 tilesets Rouge Feu en plus de ceux d'Émeraude.
- Les personnages de carte des deux jeux, écrans titre, intros, carte dresseur, aperçus de lieux.
- Le moteur peut même compiler une version « base Rouge Feu » (`make firered`, pas encore testé).

## 2. Dresseurs : on peut les faire passer d'un jeu à l'autre

- 181 sprites de combat déjà dans le moteur (Émeraude + 86 Rouge Feu), avec leurs palettes.
- Or/Argent GBC : les 66 dresseurs convertis automatiquement, testés en combat (OK, plus plats : 4 couleurs).
- HeartGold/SoulSilver : récupérables via Pokémon Showdown, réduits de 80x80 à 64x64,
  testés en combat (bon rendu, perso 20 % plus petits, petits détails parfois à retoucher).
- Pas dans la décompilation HGSS de GitHub : les images y sont extraites de la ROM au moment de la compilation.

## 3. Pokémon, objets, capacités : tout est déjà là

- Les 1025 Pokémon de la 1G à la 9G (~1670 avec les formes : Méga, Alola, Galar, Hisui, Paldea, Gigamax).
- Toutes les capacités jusqu'à la 9G (~900) + capacités Z et Dynamax.
- Tous les talents (~300) et plus de 1000 objets.
- Méga-Évolution, capacités Z, Dynamax, Téracristal disponibles.
- Règles de combat réglables génération par génération (`include/config/battle.h`).

## 4. Création : nouveaux objets et nouvelles cartes (dans la limite du possible)

- Nouvelles cartes et nouveaux décors : faisable (tests 1, 2 et 4 : carte japonaise, intérieurs, cadre de dialogue).
- Nouveaux objets : faisable (données + icône 24x24, petite taille donc dessinable).
- Dialogues, scripts, événements : faisable (test 3).
- Animations de capacités et effets sur la carte (météo, particules) : faisable (test 11, pétales de sakura).

## 5. Apparence des dresseurs : modifier oui, créer non

- Personnages de carte (overworld) : on peut en faire de nouveaux (test 6) et changer les tenues (test 5).
- Sprites de combat : on peut retoucher tenues, couleurs, petits détails d'un sprite existant.
- Créer un sprite de combat entièrement nouveau : écarté (tests 7, 9, 10, N, Porypal : résultat pas au niveau).
- Contournement : réutiliser un sprite existant d'un autre jeu (point 2).

## Comment s'en servir pour l'histoire

- Un personnage important doit avoir un sprite de combat existant quelque part (Émeraude, Rouge Feu, Or/Argent, HGSS)
  ou pouvoir être une variante retouchée d'un sprite existant.
- Lieux, Pokémon, objets, mécaniques : presque aucune limite.
