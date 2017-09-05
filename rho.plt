set style data linespoints

plot 'build/0.dat' using 1:2, \
     'build/1.dt.dat' using 1:2, \
     'build/2.dt.dat' using 1:2, \
     'build/3.dt.dat' using 1:2, \
     'build/1.dat' using 1:2 lw 3 lc -1
