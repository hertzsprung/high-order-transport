set style data linespoints
set logscale

set multiplot layout 1,2 title 'schaerAdvect h0=3km'

set xrange [500:1000]
set xlabel "dx"

set title 'l2'

plot 'schaerAdvect.btf.l2.dat' using 1:2 title 'cubicFit btf', \
     'schaerAdvect.btf.l2.dat' using 1:3 title 'highOrderFit btf', \
     'schaerAdvect.cutCell.l2.dat' using 1:2 title 'cubicFit cutCell', \
     'schaerAdvect.cutCell.l2.dat' using 1:3 title 'highOrderFit cutCell'

set title 'linf'

plot 'schaerAdvect.btf.linf.dat' using 1:2 title 'cubicFit btf ', \
     'schaerAdvect.btf.linf.dat' using 1:3 title 'highOrderFit btf', \
     'schaerAdvect.cutCell.linf.dat' using 1:2 title 'cubicFit cutCell ', \
     'schaerAdvect.cutCell.linf.dat' using 1:3 title 'highOrderFit cutCell'

unset multiplot
