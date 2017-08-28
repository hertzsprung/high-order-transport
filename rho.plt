set style data lines

plot 'build/0.dat' using 1:2, \
     'build/0.125.dat' using 1:2, \
     'build/1.0.dat' using 1:2, \
     'build/1.0.diff.dat' using 1:2
