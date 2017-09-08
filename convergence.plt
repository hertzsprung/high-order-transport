set style data linespoints

set logscale

set yrange[*:0.5]

plot 'build/convergence.order2.stencil3.dat' using 1:2, \
     'build/convergence.order3.stencil3.dat' using 1:2, \
     'build/convergence.order2.stencil4.dat' using 1:2, \
     'build/convergence.order3.stencil4.dat' using 1:2, \
     x lc 0, \
     x**2 lc 0 dt 2
