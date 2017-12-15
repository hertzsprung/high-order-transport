set style data linespoints
set logscale

plot 'convergence.gaussian.dat' using 1:2 title 'highorderFit', \
     'convergence.gaussian.dat' using 1:3 title 'cubicFit', \
     2e2*x**-2 lc 0 dt 3
