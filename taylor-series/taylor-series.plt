set key inside bottom right

set xrange [-3:3]
set yrange [-1.5:1.5]

plot 'gradient.dat', 'lr-flux-sum.dat', 'lr-highOrder-flux-sum.dat'
