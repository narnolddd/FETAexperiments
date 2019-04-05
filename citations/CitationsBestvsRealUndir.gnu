set term postscript eps enhanced color 24
set font ",20"

set xrange [35875:38556]
set xlabel 'Timestamp'
set font ",20

f1 = "experiments/citations/Citations_Last10_Measurements.dat"
f2 = "experiments/citations/Citations_Last10_BATriInv10Rand_Measurements.dat"
f3 = "experiments/citations/Citations_Copy_BATri_Measurements.dat"
f4 = "experiments/citations/Citations_Copy_Undir_BA_Measurements.dat"

leg1 = "Real data"
leg2 = "0.47 BA, 0.03 Rand, 0.5 Tri 10 Inv Deg"
leg3 = "0.84 BA, 0.16 Tri"
leg4 = "1.0 BA"

# Network density
set output "experiments/citations/cit_dense_last10.eps"
set yrange [0:0.2]
set title 'Density'
set ylabel 'NoLinks/NoPossibleLinks'
plot f1 using 1:5 with lines lw 3 title leg1, \
f2 using 1:5 with lines lw 3 title leg2

# Maximum degree
set output "experiments/citations/cit_maxdeg_last10.eps"
set yrange [0:700]
set title 'Maximum degree'
set ylabel 'kmax'
plot f1 using 1:6 with lines lw 3 title leg1, \
f2 using 1:6 with lines lw 3 title leg2

# Clusterinf coeff
set output "experiments/citations/cit_cluster_last10.eps"
set yrange [0:0.3]
set title 'Average clustering coefficient'
set ylabel 'C'
plot f1 using 1:7 with lines lw 3 title leg1, \
f2 using 1:7 with lines lw 3 title leg2

# Mean squared degree
set output "experiments/citations/cit_meandegsq_last10.eps"
set yrange [0:1500]
set title 'Mean squared degree'
set ylabel '<k^2>'
plot f1 using 1:8 with lines lw 3 title leg1, \
f2 using 1:8 with lines lw 3 title leg2

# Degree assortativity
set output "experiments/citations/cit_assort.eps"
set yrange [-0.2:0.2]
set title 'Degree Assortativity'
set ylabel 'r'
plot f1 using 1:9 with lines lw 3 title leg1, \
f2 using 1:9 with lines lw 3 title leg2

# Average degree
set output "experiments/citations/cit_avgdeg.eps"
set yrange [0:25]
set title 'Average Degree'
set ylabel '<k>'
plot f1 using 1:4 with lines lw 3 title leg1, \
f2 using 1:4 with lines lw 3 title leg2
