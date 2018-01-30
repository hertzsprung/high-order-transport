#!/bin/bash
sumFields -scale0 1 -scale1 -1 5 T_diff 0 T 5 T
globalSum -time 5 T_diff
mv globalSumT_diff.dat 5
tail -n1 5/globalSumT_diff.dat | cut -d' ' -f3 > 5/l2errorT_diff.txt

cp 0/T 5/T_analytic
globalSum -time 5 T_analytic
mv globalSumT_analytic.dat 5
tail -n1 5/globalSumT_analytic.dat | cut -d' ' -f3 > 5/l2errorT_analytic.txt

python3 -c "print(`paste -d'/' 5/l2errorT_diff.txt 5/l2errorT_analytic.txt`)" > 5/l2errorT.txt

