YEAR_NUM="${2:-"25"}"
DAY_NUM=$1

ndir=y$YEAR_NUM/d$DAY_NUM
if [[ -d $ndir ]]; then
    echo "Day $DAY_NUM already created"
    exit
fi
mkdir $ndir

cp template/* $ndir
mv $ndir/day.py $ndir/day$DAY_NUM.py

curl https://adventofcode.com/20$YEAR_NUM/day/$DAY_NUM/input --cookie session=$AOC_SESSION -o $ndir/input.txt 