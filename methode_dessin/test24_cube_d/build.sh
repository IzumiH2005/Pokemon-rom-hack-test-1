#!/bin/sh
# Reconstruit toutes les étapes du Dé 64×64 à partir des fichiers de commandes.
set -e
cd "$(dirname "$0")"; T=../outils; P=palette.json
python3 faces.py O O O > c01_silhouette.txt
python3 faces.py d c b > c02_trois_valeurs.txt
python3 panneaux.py c 3 8 > c04_panneaux.txt
python3 bandes.py > c05_bandes.txt
python3 $T/trace.py NEW:64x64 etape00_construction.txt c00_construction.txt
python3 $T/trace.py NEW:64x64 etape01_silhouette.txt c01_silhouette.txt
python3 $T/trace.py NEW:64x64 etape02_trois_valeurs.txt c02_trois_valeurs.txt
python3 $T/contour.py etape02_trois_valeurs.txt etape03_contour.txt
python3 $T/trace.py etape03_contour.txt etape04_panneaux.txt c04_panneaux.txt
python3 $T/trace.py etape04_panneaux.txt etape05_bandes.txt c05_bandes.txt
python3 $T/trace.py etape05_bandes.txt etape06_points.txt c06_points_aretes.txt
python3 $T/trace.py etape06_points.txt etape07_aretes.txt c07_aretes.txt
for f in etape0*.txt; do python3 $T/px.py $f 8 $P; done
# Icône 24×24, redessinée
python3 $T/trace.py NEW:23x24 etape_i01_icone.txt i01_icone.txt
python3 $T/contour.py etape_i01_icone.txt etape_i02_icone.txt
python3 $T/trace.py etape_i02_icone.txt etape_i03_icone.txt i02_details.txt
python3 $T/px.py etape_i03_icone.txt 16 $P
