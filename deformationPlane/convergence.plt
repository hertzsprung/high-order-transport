set style data linespoints
set logscale

set xrange [500:100]
set yrange [1e-2:1]
set xlabel '# of cells in x'
set ylabel 'l2 error'
set xtics (120, 180, 240, 480)

set key inside bottom right

plot 'convergence.dat' using 1:2 lw 1.5 title 'highOrderFit uniform', \
     'convergence.dat' using 1:3 lw 1.5 title 'cubicFit uniform', \
     'convergence.dat' using 1:4 lw 1.5 lc 1 dt 2 title 'highOrderFit severely distorted', \
     'convergence.dat' using 1:5 lw 1.5 lc 2 dt 2 title 'cubicFit severely distorted', \
     'convergence.dat' using 1:6 lw 1.5 lc 1 dt 3 title 'highOrderFit mildly distorted', \
     'convergence.dat' using 1:7 lw 1.5 lc 2 dt 3 title 'cubicFit mildly distorted', \
     5e1*x**-1 lc 0 dt 2 lw 1.5 title 'x', \
     5e3*x**-2 lc 0 dt 3 lw 1.5 title 'x^2', \
     5e8*x**-4 lc 0 dt 4 lw 1.5 title 'x^4'
