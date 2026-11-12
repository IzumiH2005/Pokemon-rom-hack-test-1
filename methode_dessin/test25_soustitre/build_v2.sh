#!/bin/sh
# Version 2 : « CONVERGENCE IDENTITAIRE » sous « VERSION ROUGE FEU ».
set -e
cd "$(dirname "$0")"; T=../outils; P=palette_v2.json
python3 $T/trace.py NEW:88x24 v2_etape01_forme.txt c11_logo.txt
python3 $T/trace.py v2_etape01_forme.txt v2_etape02_couleurs.txt c12_couleurs.txt
for f in v2_etape0*.txt; do python3 $T/px.py $f 6 $P; done
