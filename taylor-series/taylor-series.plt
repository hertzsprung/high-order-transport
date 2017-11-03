set key outside top center

set xlabel 'x'
set ylabel 'coefficient
set xrange [-2.5:2.5]
set yrange [-1.6:1.6]
set xzeroaxis

plot 'gradient-zeroed.dat' pt 1 ps 2 lw 1.5 title 'Taylor series 5-point cell centre gradient', \
     'lr-flux-sum.dat' pt 2 ps 2 lw 1.5 title '4-point cubicFit face flux', \
     'lr-highOrder-flux-sum.dat' pt 4 ps 2 lw 1.5 title '4-point highOrderFit face flux'
