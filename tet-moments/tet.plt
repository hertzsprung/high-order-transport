set terminal wxt

set xrange [0:*]
set yrange [0:*]
set zrange [0:*]

set xlabel 'x'
set ylabel 'y'
set zlabel 'z'

set xyplane 0

splot 'vertices' using 1:2:3 with linespoints
