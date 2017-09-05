set style data linespoints

set yrange [-0.5:1.5]

plot 'build/0.dat' using 1:2 dt 3 lw 2 lc -1, \
     'build/1.dt.dat' using 1:2, \
     'build/2.dt.dat' using 1:2, \
     'build/3.dt.dat' using 1:2, \
     'build/1.dat' using 1:2 lw 3 lc -1
