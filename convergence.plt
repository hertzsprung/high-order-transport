set style data linespoints

set logscale

set yrange[*:0.5]

set key outside top center

plot 'build/convergence.order2.stencil3.dat' using 1:2, \
     'build/convergence.order3.stencil3.dat' using 1:2, \
     'build/convergence.order2.stencil4.dat' using 1:2, \
     'build/convergence.order3.stencil4.dat' using 1:2, \
     'build/convergence.order4.stencil4.dat' using 1:2, \
     1e1*x**2 lc 0 dt 2, \
     1e2*x**3 lc 0 dt 3, \
     5e2*x**4 lc 0 dt 4
