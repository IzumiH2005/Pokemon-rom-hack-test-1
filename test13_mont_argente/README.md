# Test 13 : Route 28 et Mont Argenté

Ce test importe la Route 28 et le Mont Argenté du projet Pokémon Heart & Soul
dans le build Rouge Feu du jeu. Le prologue de l'histoire se passe au sommet.

## Ce que fait le script

`outils/importer_hns.py <pokemonHnS> <jeu>` copie depuis un clone de Heart & Soul :

- 7 tilesets, renommés avec le préfixe `Hns_` et convertis au format Rouge Feu
  (attributs de métatuiles passés de 16 à 32 bits) ;
- les animations d'eau, de fleurs et de cascade du tileset principal ;
- 11 cartes : Route 28, pied du mont, trois salles du rez-de-chaussée,
  deux étages de grotte, flanc de montagne, zone enneigée, sommet de jour et de nuit.

Le script peut être relancé sans risque : il détecte ce qui est déjà en place.

Les tilesets et les cartes ne sont pas stockés dans ce dépôt. Ils viennent de
Heart & Soul et le script les récupère à la demande.

## Vérifié en jeu

- `make firered` compile.
- Le sommet, la zone enneigée, la Route 28 et le pied du mont s'affichent correctement.
- La neige tombe au sommet et dans la zone enneigée.
- Le passage du sommet vers la grotte fonctionne, et le nom du lieu s'affiche à l'arrivée.

## Ce qui manque

- Les intérieurs (Centre Pokémon, maison de la Route 28) : leurs portes ramènent sur place.
- Les PNJ, les objets, les panneaux et les Pokémon sauvages.
- Le raccord de la Route 28 au reste de Kanto.
- La position des deux lieux sur la carte de la région.
