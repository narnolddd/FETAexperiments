set term postscript eps enhanced color 24
set font ",20"

set xrange [0:10000]
set xlabel 'Number of Nodes'
set font ",20

f1 = "experiments/citations/Citations_Undir_Measurements.dat"
f2 = "experiments/citations/Citations_Copy_Undir_Measurements.dat"
f3 = "experiments/citations/Citations_Copy_BATri_Measurements.dat"
f4 = "experiments/citations/Citations_Copy_Undir_BA_Measurements.dat"

leg1 = "Real data"
leg2 = "0.93 BA, 0.06 Rand, 0.01 Tri"
leg3 = "0.84 BA, 0.16 Tri"
leg4 = "1.0 BA"

# Network density
set output "experiments/citations/cit_dense.eps"
set yrange [0:0.2]
set title 'Density'
set ylabel 'NoLinks/NoPossibleLinks'
plot f1 using 2:5 with lines lw 3 title leg1, \
f2 using 2:5 with lines lw 3 title leg2, \
f3 using 2:5 with lines lw 3 title leg3, \
f4 using 2:5 with lines lw 3 title leg4

# Maximum degree
set output "experiments/citations/cit_maxdeg.eps"
set yrange [0:200]
set title 'Maximum degree'
set ylabel 'kmax'
plot f1 using 2:6 with lines lw 3 title leg1, \
f2 using 2:6 with lines lw 3 title leg2, \
f3 using 2:6 with lines lw 3 title leg3, \
f4 using 2:6 with lines lw 3 title leg4

# Clusterinf coeff
set output "experiments/citations/cit_cluster.eps"
set yrange [0:0.3]
set title 'Average clustering coefficient'
set ylabel 'C'
plot f1 using 2:7 with lines lw 3 title leg1, \
f2 using 2:7 with lines lw 3 title leg2, \
f3 using 2:7 with lines lw 3 title leg3, \
f4 using 2:7 with lines lw 3 title leg4

# Mean squared degree
set output "experiments/citations/cit_meandegsq.eps"
set yrange [0:330]
set title 'Mean squared degree'
set ylabel '<k^2>'
plot f1 using 2:8 with lines lw 3 title leg1, \
f2 using 2:8 with lines lw 3 title leg2, \
f3 using 2:8 with lines lw 3 title leg3, \
f4 using 2:8 with lines lw 3 title leg4

# Degree assortativity
set output "experiments/citations/cit_assort.eps"
set yrange [-0.2:0.2]
set title 'Degree Assortativity'
set ylabel 'r'
plot f1 using 2:9 with lines lw 3 title leg1, \
f2 using 2:9 with lines lw 3 title leg2, \
f3 using 2:9 with lines lw 3 title leg3, \
f4 using 2:9 with lines lw 3 title leg4

# Average degree
set output "experiments/citations/cit_avgdeg.eps"
set yrange [0:12]
set title 'Average Degree'
set ylabel '<k>'
plot f1 using 2:4 with lines lw 3 title leg1, \
f2 using 2:4 with lines lw 3 title leg2, \
f3 using 2:4 with lines lw 3 title leg3, \
f4 using 2:4 with lines lw 3 title leg4
