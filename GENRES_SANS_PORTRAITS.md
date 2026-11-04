# Genres de jeux : lesquels on peut faire sans portraits ni gros sprites

Ce document liste les grands genres de jeux vidéo et leurs sous-genres. Pour chacun, il dit si on peut le faire **sans illustrations de personnages** : ni portraits détaillés, ni grands sprites dessinés.

## Ce qu'on sait déjà produire

D'après les tests du dossier `methode_dessin/` et le reste du dépôt :
- tuiles et décors ;
- cartes ;
- intérieurs ;
- objets et icônes ;
- cadres de dialogue et interface ;
- effets visuels ;
- petits personnages de 16 à 32 px (chibi, monstres simples) ;
- textes, systèmes et règles.

Ce qui ne marche pas : les portraits détaillés de 64 à 256 px (tests 16, 19 et 20).

## Légende

- ✅ **Idéal** : l'art des personnages n'est pas nécessaire, ou de simples formes suffisent.
- 🟡 **Faisable avec astuces** : petits sprites, silhouettes, texte à la place des visages.
- ❌ **À éviter** : le genre repose sur des personnages dessinés en grand.

---

## 1. Puzzle / réflexion

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Blocs qui tombent | ✅ | Tetris, Puyo Puyo |
| Pousser des caisses (Sokoban) | ✅ | Sokoban, Baba Is You |
| Logique sur grille | ✅ | Picross, Démineur, sudoku |
| Assembler des éléments identiques (match-3) | ✅ | Bejeweled, Candy Crush |
| Physique | ✅ | World of Goo, Angry Birds |
| Puzzle spatial ou de perspective | 🟡 | Monument Valley, Fez |

**Pourquoi ça marche :** le joueur regarde les règles, pas les personnages. Tetris n'a aucun personnage.
- Baba Is You est entièrement fait de petites icônes et de mots, et a pourtant gagné des prix majeurs ([Wikipédia](https://fr.wikipedia.org/wiki/Baba_Is_You)).
- Le genre : [Jeu de puzzle — Wikipédia](https://fr.wikipedia.org/wiki/Jeu_de_puzzle).

## 2. Roguelike / roguelite

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Roguelike classique au tour par tour, sur grille | ✅ | Rogue, NetHack, Brogue |
| Roguelike minimal sur une petite grille | ✅ | Hoplite, Desktop Dungeons |
| Bullet-heaven (survivre à des vagues) | ✅ | Vampire Survivors, Brotato |
| Roguelite d'action | 🟡 | Enter the Gungeon, Downwell |
| Roguelite narratif | ❌ | Hades |

**Pourquoi ça marche :**
- Le genre est né avec des lettres ASCII : `@` pour le héros, `D` pour un dragon ([Rogue — Wikipédia](https://fr.wikipedia.org/wiki/Rogue_(jeu_vid%C3%A9o))). Dwarf Fortress et Brogue ont gardé ce style des décennies.
- La rejouabilité vient de la génération procédurale et des combinaisons d'objets, pas de l'art.
- Vampire Survivors a été fait par une seule personne, avec des sprites de 16 à 32 px. C'est exactement la taille qu'on maîtrise.
- Sur le genre : [Roguelike — Wikipédia](https://fr.wikipedia.org/wiki/Roguelike) et la définition de Berlin ([RogueBasin](https://www.roguebasin.com/index.php/Berlin_Interpretation)).

## 3. Cartes et deckbuilding

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Solitaires, jeux de cartes classiques | ✅ | Solitaire, poker |
| Deckbuilder roguelite | 🟡 | Slay the Spire, Balatro |
| Jeu de cartes à collectionner | 🟡 | Hearthstone, cartes Pokémon |
| Jeu de cartes et d'aventure | 🟡 | Inscryption, Cultist Simulator |

**Pourquoi ça marche :**
- Une carte, c'est un cadre, une icône et un texte. Les icônes d'objets, on sait les faire (tests 3, 4 et 15).
- Balatro n'utilise que des cartes à jouer classiques, retravaillées, et a été un des grands succès de 2024 ([Wikipédia](https://en.wikipedia.org/wiki/Balatro)).
- Cultist Simulator tient presque entièrement sur du texte et des icônes.
- Sur le genre : [Deck-building game — Wikipédia](https://en.wikipedia.org/wiki/Deck-building_game).

## 4. Stratégie

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Tower defense | ✅ | Bloons, Kingdom Rush, Plants vs. Zombies |
| Tactique au tour par tour sur grille | 🟡 | Into the Breach, Fire Emblem, Advance Wars |
| 4X (explorer, s'étendre, exploiter, exterminer) | ✅ | Civilization, Polytopia |
| Grande stratégie | ✅ | Europa Universalis |
| Temps réel (RTS) | 🟡 | StarCraft, Northgard |
| Jeux abstraits (échecs, go) | ✅ | Échecs, Go |

**Pourquoi ça marche :**
- Les unités sont vues de loin et en petit. Advance Wars et Fire Emblem sur GBA utilisent des unités de 16×16 sur la carte.
- Into the Breach fait tout tenir sur une grille de 8×8 avec de petits sprites. Ses créateurs expliquent que la lisibilité passait avant tout ([conférence GDC sur YouTube](https://www.youtube.com/watch?v=SWg3CYDPhaw)).
- Pour la grande stratégie et le 4X, la carte et les chiffres sont le jeu.
- Attention : Fire Emblem et Advance Wars ont des portraits dans les dialogues. On peut les remplacer par un nom et une couleur.
- Sur le genre : [Jeu de stratégie — Wikipédia](https://fr.wikipedia.org/wiki/Jeu_vid%C3%A9o_de_strat%C3%A9gie).

## 5. Gestion et simulation

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Tycoon (gestion d'entreprise) | ✅ | RollerCoaster Tycoon, Game Dev Tycoon |
| Construction de ville | ✅ | SimCity, Mini Metro |
| Colonie | ✅ | Dwarf Fortress, RimWorld |
| Ferme et vie quotidienne | 🟡 | Stardew Valley, Harvest Moon |
| Jeu incrémental ou idle | ✅ | Cookie Clicker, A Dark Room |
| Simulation de métier | ✅ | Papers, Please |

**Pourquoi ça marche :**
- Le joueur regarde des systèmes : flux, ressources, chiffres.
- Mini Metro n'est fait que de lignes et de ronds ([Wikipédia](https://en.wikipedia.org/wiki/Mini_Metro)).
- A Dark Room commence en texte seul, sur une page blanche ([Wikipédia](https://en.wikipedia.org/wiki/A_Dark_Room)).
- RimWorld a des colons sans bras ni jambes, et c'est assumé.
- Papers, Please montre de petits visages pixelisés, volontairement grossiers.
- Sur le genre : [Jeu de gestion — Wikipédia](https://fr.wikipedia.org/wiki/Jeu_de_gestion).

## 6. Narratif

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Fiction interactive (texte) | ✅ | Zork, 80 Days, Choice of Games |
| « Livre dont vous êtes le héros » | ✅ | Sorcery!, Lifeline |
| Jeu d'enquête sur documents ou interface | ✅ | Her Story, Return of the Obra Dinn |
| Walking simulator | 🟡 | Gone Home, Firewatch |
| Visual novel | ❌ | Doki Doki, Phoenix Wright |

**Pourquoi ça marche :**
- Dans le texte, c'est le lecteur qui imagine les visages, ce qui marche souvent mieux qu'un portrait moyen.
- Scott McCloud explique (*L'Art invisible*) qu'un visage simple ou absent permet au joueur de s'identifier plus facilement ([Understanding Comics — Wikipédia](https://en.wikipedia.org/wiki/Understanding_Comics)).
- Return of the Obra Dinn est en 1-bit (noir et blanc) : les visages sont presque des esquisses.
- Le visual novel repose entièrement sur les portraits : c'est ce qu'il faut éviter pour nous.
- Sur le genre : [Fiction interactive — Wikipédia](https://fr.wikipedia.org/wiki/Fiction_interactive).

## 7. Action et arcade

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Shoot'em up (vaisseaux) | ✅ | Space Invaders, Ikaruga |
| Shooter vu de dessus (twin-stick) | ✅ | Geometry Wars, Nuclear Throne |
| Arcade avec des formes | ✅ | Asteroids, Pac-Man, Snake |
| Rythme | ✅ | Rhythm Heaven, A Dance of Fire and Ice |
| Beat'em up | ❌ | Streets of Rage |
| Combat en un contre un | ❌ | Street Fighter |

**Pourquoi ça marche :**
- Un vaisseau, une balle ou un rond se lisent instantanément.
- Geometry Wars n'est fait que de formes au néon ([Wikipédia](https://en.wikipedia.org/wiki/Geometry_Wars)).
- A Dance of Fire and Ice, c'est deux planètes sur un chemin.
- Le combat demande des personnages grands et très animés : trop coûteux.
- Sur le genre : [Shoot 'em up — Wikipédia](https://fr.wikipedia.org/wiki/Shoot_%27em_up).

## 8. Plateforme

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Plateforme de précision | ✅ | Super Meat Boy, Celeste, N++ |
| Plateforme minimaliste (formes simples) | ✅ | Thomas Was Alone |
| Plateforme et puzzle | ✅ | Braid, Limbo (silhouettes) |
| Metroidvania | 🟡 | Hollow Knight, Axiom Verge |
| Plateforme classique avec mascotte | 🟡 | Mario, Shovel Knight |

**Pourquoi ça marche :**
- Le héros d'un jeu de plateforme est petit : 16 à 32 px suffisent. Celeste utilise un héros de 8×8 environ dans les niveaux.
- Thomas Was Alone a pour personnages des rectangles de couleur, et la narration en voix off leur donne une personnalité ([Wikipédia](https://en.wikipedia.org/wiki/Thomas_Was_Alone)).
- Limbo n'a que des silhouettes noires ([Wikipédia](https://fr.wikipedia.org/wiki/Limbo_(jeu_vid%C3%A9o))).
- Sur le genre : [Jeu de plates-formes — Wikipédia](https://fr.wikipedia.org/wiki/Jeu_de_plates-formes).

## 9. RPG

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Dungeon crawler à la première personne | ✅ | Wizardry, Legend of Grimrock |
| RPG en texte ou en ASCII | ✅ | Kingdom of Loathing, Caves of Qud |
| RPG minimal sans portraits | 🟡 | Undertale, Minit, Earthbound |
| RPG de collection de monstres | 🟡 | Pokémon, Cassette Beasts |
| JRPG classique | 🟡 | Dragon Quest, Final Fantasy VI |
| RPG d'action | 🟡 | Zelda vu de dessus |
| CRPG ou RPG narratif lourd | ❌ | Baldur's Gate, Disco Elysium |

**Pourquoi ça marche :**
- Dans un dungeon crawler, on voit des murs, pas le héros. On dessine des monstres de face, une fois chacun.
- Dragon Quest 1 à 3 et Final Fantasy 1 n'avaient aucun portrait : seulement des sprites de 16×16 sur la carte.
- Undertale n'a presque pas de portraits : le style volontairement simple est devenu sa marque ([Wikipédia](https://fr.wikipedia.org/wiki/Undertale)).
- Minit est en noir et blanc avec des sprites minuscules ([Wikipédia](https://en.wikipedia.org/wiki/Minit_(video_game))).
- **Pour notre hack Pokémon :** les Pokémon, les dresseurs de combat et les personnages de carte existent déjà dans le moteur. Voir `CAPACITES_DU_MOTEUR.md`. Les jeux Pokémon de la GBA n'ont pas de portraits dans les dialogues : il ne manque donc rien.
- Sur le genre : [Jeu vidéo de rôle — Wikipédia](https://fr.wikipedia.org/wiki/Jeu_vid%C3%A9o_de_r%C3%B4le).

## 10. Horreur

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Horreur d'ambiance en 2D | ✅ | Lone Survivor, Fran Bow (en partie) |
| Horreur RPG Maker | 🟡 | Ib, Yume Nikki, The Witch's House |
| Horreur en texte ou en interface | ✅ | Sara Is Missing, Simulacra |
| Survival horror | 🟡 | Resident Evil vu de dessus |

**Pourquoi ça marche :**
- En horreur, ce qu'on ne voit pas fait plus peur que ce qu'on voit. L'obscurité, le son et le cadrage cachent les limites de l'art.
- Yume Nikki et Ib sont faits sous RPG Maker, avec des sprites minuscules. Ce sont des classiques du genre ([Yume Nikki — Wikipédia](https://fr.wikipedia.org/wiki/Yume_Nikki)).
- Ça colle avec le style sombre et sanglant de ton personnage de test, sans avoir à le dessiner en grand.

## 11. Course, sport, party

| Sous-genre | Faisable | Exemples |
|---|---|---|
| Course vue de dessus | ✅ | Micro Machines, Super Sprint |
| Sport arcade | 🟡 | Sensible Soccer, Windjammers |
| Golf ou billard | ✅ | Desert Golfing, Golf Story (en partie) |
| Mini-jeux (party) | 🟡 | WarioWare |

**Pourquoi ça marche :** une voiture vue d'en haut, une balle ou un club se dessinent en quelques pixels. Desert Golfing, c'est une balle, du sable et rien d'autre ([Wikipédia](https://en.wikipedia.org/wiki/Desert_Golfing)).

---

## Le pourquoi, en résumé

1. **Les mécaniques portent le jeu.** Dans les genres ✅, le joueur passe son temps à lire des règles, une grille, des chiffres ou des formes. Les personnages en grand n'y servent pas.
2. **L'abstraction aide l'identification.** Plus un personnage est simple, plus le joueur se projette dedans (McCloud). Le texte laisse l'imagination faire les visages.
3. **La petite taille cache les faiblesses.** À 16 ou 32 px, on dessine l'idée d'un personnage, pas ses traits. C'est la taille où nos tests réussissent.
4. **Beaucoup de grands jeux sont minimalistes par choix :** Tetris, Mini Metro, Thomas Was Alone, Baba Is You, Vampire Survivors, Return of the Obra Dinn, Undertale.
5. **Les contraintes forcent le style.** Un style très limité (1-bit, silhouettes, ASCII, formes géométriques) devient une identité visuelle s'il est assumé partout ([Minimalisme dans le jeu vidéo, GDC Vault](https://www.gdcvault.com/)).

## Ce que je recommande pour toi

| Projet | Pourquoi |
|---|---|
| **Continuer le hack Pokémon sans portraits** | C'est déjà le standard GBA. Pokémon, dresseurs et personnages de carte sont fournis, et nos décors, objets et effets s'y ajoutent. |
| **Roguelike ou tactique sur grille** | Il ne faut que des petits sprites, que je sais faire. La profondeur vient des systèmes. |
| **Deckbuilder** | Il ne faut que des icônes, des cadres et du texte. Tout ça est déjà testé. |
| **Horreur d'ambiance à la Yume Nikki** | Petits sprites et obscurité. Ça rejoint le ton sombre de ton personnage. |

Si un jour tu veux des portraits, tu peux les faire faire à part (outil d'IA spécialisé ou artiste), puis je les adapte et les intègre. Aucun de ces genres n'en a besoin pour exister.
