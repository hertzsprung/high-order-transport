set style data linespoints

set logscale

set format x "10^{%L}"
set format y "10^{%L}"

set xrange[0.001:0.1]
set yrange[*:0.5]

set key outside top center

plot 'build/convergence.order2.stencil3.dat' using 1:2 lw 2 title '3-point stencil, linear', \
     'build/convergence.order3.stencil3.dat' using 1:2 lw 2 title '3-point stencil, quadratic', \
     'build/convergence.order2.stencil4.dat' using 1:2 lw 2 title '4-point stencil, linear', \
     'build/convergence.order3.stencil4.dat' using 1:2 lw 2 title '4-point stencil, quadratic', \
     'build/convergence.order4.stencil4.dat' using 1:2 lw 2 title '4-point stencil, cubic', \
     5*x lc 0 dt 1 lw 2 title 'x', \
     1e2*x**2 lc 0 dt 2 lw 2 title 'x^2', \
     1e4*x**3 lc 0 dt 3 lw 2 title 'x^3', \
     1e5*x**4 lc 0 dt 4 lw 2 title 'x^4'

     # for uniform meshes
     #1e1*x lc 0 dt 1 lw 2 title 'x', \
     #1e2*x**2 lc 0 dt 2 lw 2 title 'x^2', \
     #1e3*x**3 lc 0 dt 3 lw 2 title 'x^3', \
     #1e4*x**4 lc 0 dt 4 lw 2 title 'x^4'
