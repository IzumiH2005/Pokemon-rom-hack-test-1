#!/bin/sh
# Reconstruit le sous-titre « I.C / CONVERGENCE IDENTITAIRE » étape par étape.
set -e
cd "$(dirname "$0")"; T=../outils; P=palette.json
python3 $T/trace.py NEW:128x24 etape01_relief.txt c01_relief.txt
# Trait : seules les faces de l'emblème (X), contre le vide et contre le relief r.
python3 $T/contour.py etape01_relief.txt etape02_contour.txt X r
python3 $T/trace.py etape02_contour.txt etape03_couleurs.txt c03_couleurs.txt
for f in etape0*.txt; do python3 $T/px.py $f 6 $P; done
