# Écrit et trace une colonne : assembler.sh nom type hauteur "joints"
# type : brise (cassure.txt), brise2 (cassure2.txt) ou pointe (pointe.txt : lame et collier)
# La base (dalle, tore, ombre) occupe les 28 dernières rangées ; dy décale tout ce qui est bas.
nom=$1; type=$2; H=$3; joints=$4
f=colonnes/c_$nom.txt; dy=$((H-80))
case $type in pointe) d=38;; *) d=20;; esac
{
echo "# colonne $nom : $type, hauteur $H, joints à $joints"
echo "stamp pieces/base.txt 0 $((52+dy))"
for y in $(seq $d $((58+dy))); do echo "stamp pieces/fut.txt 6 $y"; done
echo "stamp pieces/pied.txt 6 $((59+dy))"
case $type in
  brise)  echo "stamp pieces/cassure.txt 6 4";;
  brise2) echo "stamp pieces/cassure2.txt 6 5";;
  pointe) echo "stamp pieces/pointe.txt 5 0";;
esac
for j in $joints; do echo "stamp pieces/joint.txt 6 $j"; done
[ -f colonnes/d_$nom.txt ] && cat colonnes/d_$nom.txt
} > $f
python3 ../outils/trace.py NEW:34x$H colonnes/$nom.txt $f
python3 ../outils/px.py colonnes/$nom.txt 4 palette.json
