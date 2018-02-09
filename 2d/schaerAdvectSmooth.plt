set style data linespoints
set logscale
set format x "$10^{%L}$"
set format y "$10^{%L}$"

set xrange [10000:100]
set yrange [1e-4:1]

set xlabel "$\\Delta x$ (\\si{\\meter})" offset 0,0.5
set ylabel "$\\ell_2 error" offset 1.5

plot 'schaerAdvectCos4.dat' using 1:2 lw 2 title 'highOrderFit BTF h0=3km cos^4', \
     'schaerAdvectCos4.dat' using 1:3 lw 2 title 'cubicFit BTF h0=3km cos^4', \
     'schaerAdvectCos4.dat' using 1:4 lc 1 lw 2 dt 2 title 'highOrderFit uniform cos^4', \
     'schaerAdvectCos4.dat' using 1:5 lc 2 lw 2 dt 2 title 'cubicFit uniform cos^4', \
     'schaerAdvectCos2.dat' using 1:2 lc 1 title 'highOrderFit BTF h0=3km cos^2', \
     'schaerAdvectCos2.dat' using 1:3 lc 2 title 'cubicFit BTF h0=3km cos^2', \
     'schaerAdvectCos2.dat' using 1:4 lc 1 dt 2 title 'highOrderFit uniform cos^2', \
     'schaerAdvectCos2.dat' using 1:5 lc 2 dt 2 title 'cubicFit uniform cos^2', \
     x**2 * 8e-8 lc rgbcolor 'black' title "x^2", \
     x**2 * 9e-9 lc rgbcolor 'black' notitle, \
     x**3 * 3e-10 lc rgbcolor 'black' dt 3 lw 1.3 title "x^3", \
     x**4 * 1e-14 lc rgbcolor 'black' dt 4 lw 1.3 title "x^4"
