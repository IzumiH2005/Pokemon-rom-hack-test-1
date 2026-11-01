# Test 6 : création d'un nouveau personnage (Aventurine)

Sprite overworld 16x32 complet (9 frames : face, dos, profil, 2 pas de marche par direction). Il reprend la structure du sprite de Brendan : gabarit de tête, placement du visage et des yeux, bras écartés, jambes et décalage de marche.

## Ce qui a été repris des références
- Cheveux blond cendré, mèche balayée sur le front, mèches sur la nuque.
- Yeux violets.
- Col en fourrure blanche.
- Chemise turquoise avec as de pique doré.
- Gilet noir à liseré doré.
- Manches noires avec revers turquoise et gants noirs.
- Pans dorés sur les côtés.
- Basques turquoise et bleues avec pompons (visibles de dos et de profil).
- Pantalon blanc et chaussures noires et turquoise.

## Ajout dans le moteur (pokeemerald-expansion)
- `OBJ_EVENT_GFX_AVENTURINE` et une palette dédiée `OBJ_EVENT_PAL_TAG_AVENTURINE` (0x1170).
- Pic, palette, table d'images, GraphicsInfo, pointeur, entrée dans `sObjectEventSpritePalettes`.
- PNJ placé à Bourg-en-Vol (8,10). Il se promène et a son propre dialogue.

## Fichiers
- `aventurine.png` et `aventurine.pal` : la planche finale et sa palette.
- `avk.py`, `av4.py` (poses fixes), `av5.py` (marche) : le dessin pixel par pixel.
- `install_av.py` : installe la planche et enregistre le PNJ dans le moteur.
