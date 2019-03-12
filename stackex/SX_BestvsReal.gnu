set term postscript eps enhanced color 24
set font ",20"

set xrange [1255094266:1457185813]
set xlabel 'Time (UNIX)'
set font ",20

f1 = "experiments/stackex/SX_Measurements.dat"
f2 = "experiments/stackex/SX_BATriRand_Measurements.dat"
f3 = "experiments/stackex/SX_BARand_Measurements.dat"
f4 = "experiments/stackex/SX_DegAgeRandTri_Measurements.dat"

leg1 = "Real data"
leg4 = "0.89 DegAge, 0.02 Rand, 0.09 Tri"

# Network density
set output "experiments/stackex/sx_dense.eps"
set yrange [0:0.2]
set title 'Density'
set ylabel 'NoLinks/NoPossibleLinks'
plot f1 using 1:5 with lines lw 5 title leg1, \
f4 using 1:5 with lines lw 5 dt 2 title leg4

# Maximum degree
set output "experiments/stackex/SX_maxdeg.eps"
set yrange [0:3000]
set title 'Maximum degree'
set ylabel 'kmax'
plot f1 using 1:6 with lines lw 5 title leg1, \
f4 using 1:6 with lines lw 5 dt 2 title leg4

# Clusterinf coeff
set output "experiments/stackex/SX_cluster.eps"
set yrange [0:0.3]
set title 'Average clustering coefficient'
set ylabel 'C'
plot f1 using 1:7 with lines lw 5 title leg1, \
f4 using 1:7 with lines lw 5 dt 2 title leg4

# Mean squared degree
set output "experiments/stackex/SX_meandegsq.eps"
set yrange [0:2000]
set title 'Mean squared degree'
set ylabel '<k^2>'
plot f1 using 1:8 with lines lw 5 title leg1, \
f4 using 1:8 with lines lw 5 dt 2 title leg4

# Degree assortativity
set output "experiments/stackex/SX_assort.eps"
set yrange [-0.2:0.2]
set title 'Degree Assortativity'
set ylabel 'r'
plot f1 using 1:9 with lines lw 5 title leg1, \
f4 using 1:9 with lines lw 5 dt 2 title leg4

# Average degree
set output "experiments/stackex/SX_avgdeg.eps"
set yrange [0:12]
set title 'Average Degree'
set ylabel '<k>'
plot f1 using 1:4 with lines lw 5 title leg1, \
f4 using 1:4 with lines lw 5 dt 2 title leg4