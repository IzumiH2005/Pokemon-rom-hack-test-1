#!/bin/sh
# Version 3 : « CONVERGENCE » seul sous « VERSION ROUGE FEU ».
set -e
cd "$(dirname "$0")"; T=../outils; P=palette_v2.json
python3 $T/trace.py NEW:88x16 v3_etape01_forme.txt c21_logo.txt
python3 $T/trace.py v3_etape01_forme.txt v3_etape02_couleurs.txt c22_couleurs.txt
for f in v3_etape0*.txt; do python3 $T/px.py $f 6 $P; done
