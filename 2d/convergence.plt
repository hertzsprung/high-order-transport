set style data linespoints
set logscale

set xrange [300:100]
set xlabel '# of cells in x'
set ylabel 'l2 error'
set xtics (100, 150, 200, 250)

set key inside bottom right

plot 'convergence.gaussian.dat' using 1:2 lw 1.5 title 'highOrderFit', \
     'convergence.gaussian.dat' using 1:3 lw 1.5 title 'cubicFit', \
     2e2*x**-2 lc 0 dt 3 lw 1.5 title 'x^2', \
     3e6*x**-4 lc 0 dt 4 lw 1.5 title 'x^4'
