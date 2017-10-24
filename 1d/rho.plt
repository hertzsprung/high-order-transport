set style data linespoints

set yrange [-0.5:1.5]

plot 'build/0.dat' using 1:2 lw 2 dt 3 lc -1 title 'Initial', \
     'build/1.dat' using 1:2 lw 3 lc -1 title 'Final'
