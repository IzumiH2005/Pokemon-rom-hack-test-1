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

## Compléments

`outils/completer_mont_argente.py <pokemonHnS> <jeu>` se lance après l'import :

- le poste de la Route 22 reçoit une sortie ouest qui mène à la Route 28 ;
- le Centre Pokémon du Mont Argenté (deux niveaux) et la maison de la Route 28
  sont créés sur les intérieurs existants de Rouge Feu ;
- deux panneaux, 7 objets au sol, 5 rochers brisables et Red au sommet sont placés
  aux positions de Heart & Soul ;
- les Pokémon sauvages reprennent les tables de jour de Heart & Soul ;
- la Route 28 et le Mont Argenté sont posés sur la carte de région, à l'ouest de la Route 22.

Les objets utilisent les drapeaux `FLAG_0x0B0` à `FLAG_0x0B6`.

## Vérifié en jeu

- `make firered` compile.
- Le sommet, la zone enneigée, la Route 28 et le pied du mont s'affichent correctement.
- La neige tombe au sommet et dans la zone enneigée.
- Le passage du sommet vers la grotte fonctionne, et le nom du lieu s'affiche à l'arrivée.
- Le trajet poste de la Route 22 vers Route 28 marche dans les deux sens.
- On entre et on sort du Centre Pokémon et de la maison ; l'infirmière répond.
- Le panneau de la Route 28, un objet au sol, les rochers et Red s'affichent et répondent.

## Ce qui reste

- Red n'a qu'un dialogue provisoire : le combat viendra avec le scénario.
- Les rencontres sauvages sont compilées mais n'ont pas été déclenchées en jeu.
- La carte de région affiche les deux noms, sans dessin de terrain sous le curseur.
- Le Centre Pokémon n'est pas une destination de Vol.
- Les salles du rez-de-chaussée, le deuxième étage et le flanc de montagne n'ont pas été parcourus en entier.
