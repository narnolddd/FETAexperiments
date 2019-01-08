set term postscript eps enhanced color 24
unset key
set font ",20"

set xrange [0:10000]
set xlabel 'Timestamp'
set font ",20"

file = "output/BAtoRand.dat"

# Network density
set output "experiments/artificial_dense.eps"
set yrange [0:0.2]
set title 'Density'
set ylabel 'NoLinks/NoPossibleLinks'
plot file using 1:5 with lines lw 3

# Maximum degree
set output "experiments/artificial_maxdeg.eps"
set yrange [0:220]
set title 'Maximum degree'
set ylabel 'kmax'
plot file using 1:6 with lines lw 3

# Clustering coeff
set output "experiments/artificial_cluster.eps"
set yrange [0.001:0.5]
set log y
set title 'Average clustering coefficient'
set ylabel 'C'
plot file using 1:7 with lines lw 3
unset log y

# Mean squared degree
set output "experiments/artificial_meandegsq.eps"
set yrange [0:100]
set title 'Mean squared degree'
set ylabel '<k^2>'
plot file using 1:8 with lines lw 3

# Degree assortativity
set output "experiments/artificial_assort.eps"
set yrange [-0.5:0.5]
set title 'Degree Assortativity'
set ylabel 'r'
plot file using 1:9 with lines lw 3

# Average degree
set output "experiments/artificial_avgdeg.eps"
set yrange [0:8]
set title 'Average Degree'
set ylabel '<k>'
plot file using 1:4 with lines lw 3
