set term postscript eps enhanced color 24
set font ",20"

set xrange [35875:38556]
set xlabel 'Timestamp'
set font ",20

f1 = "experiments/citations/Citations_Last10_Measurements.dat"
f2 = "experiments/citations/Citations_Last10_BATriRand_Measurements.dat"
f6 = "experiments/citations/Citations_Last10_BATriInv10Rand_Measurements.dat"
f3 = "experiments/citations/Citations_Last10_BA_Measurements.dat"
f4 = "experiments/citations/Citations_Last10_Rand_Measurements.dat"
f5 = "experiments/citations/Citations_Last10_Tri_Measurements.dat"

leg1 = "Real data"
leg2 = "BA, Rand, Tri"
leg3 = "BA"
leg4 = "Random"
leg5 = "Triangle Closure"
leg6 = "BA, Rand, Tri (Inv)"

set key bottom right

# Network density
set output "experiments/citations/cit_dense_last10.eps"
set yrange [0:0.2]
set title 'Density'
set ylabel 'NoLinks/NoPossibleLinks'
plot f1 using 1:5 with lines lw 5 title leg1, \
f2 using 1:5 with lines lw 5 title leg2, \
f3 using 1:5 with lines lw 3 title leg3, \
f4 using 1:5 with lines lw 3 title leg4, \
f5 using 1:5 with lines lw 3 title leg5, \
f6 using 1:5 with lines lw 5 title leg6

# Maximum degree
set output "experiments/citations/cit_maxdeg_last10.eps"
set yrange [500:700]
set title 'Maximum degree'
set ylabel 'kmax'
plot f1 using 1:6 with lines lw 5 title leg1, \
f2 using 1:6 with lines lw 5 title leg2, \
f3 using 1:6 with lines lw 3 title leg3, \
f4 using 1:6 with lines lw 3 title leg4, \
f5 using 1:6 with lines lw 3 title leg5, \
f6 using 1:6 with lines lw 3 title leg6,

# Clusterinf coeff
set output "experiments/citations/cit_cluster_last10.eps"
set yrange [0.2:0.3]
set title 'Average clustering coefficient'
set ylabel 'C'
plot f1 using 1:7 with lines lw 5 title leg1, \
f2 using 1:7 with lines lw 5 title leg2, \
f3 using 1:7 with lines lw 3 title leg3, \
f4 using 1:7 with lines lw 3 title leg4, \
f5 using 1:7 with lines lw 3 title leg5, \
f5 using 1:7 with lines lw 5 title leg6

# Mean squared degree
set output "experiments/citations/cit_meandegsq_last10.eps"
set yrange [1000:1400]
set title 'Mean squared degree'
set ylabel '<k^2>'
plot f1 using 1:8 with lines lw 5 title leg1, \
f2 using 1:8 with lines lw 5 title leg2, \
f3 using 1:8 with lines lw 3 title leg3, \
f4 using 1:8 with lines lw 3 title leg4, \
f5 using 1:8 with lines lw 3 title leg5, \
f6 using 1:8 with lines lw 5 title leg6

# Degree assortativity
set output "experiments/citations/cit_assort.eps"
set yrange [-0.05:0.05]
set title 'Degree Assortativity'
set ylabel 'r'
plot f1 using 1:9 with lines lw 5 title leg1, \
f2 using 1:9 with lines lw 5 title leg2, \
f3 using 1:9 with lines lw 3 title leg3, \
f4 using 1:9 with lines lw 3 title leg4, \
f5 using 1:9 with lines lw 3 title leg5, \
f6 using 1:9 with lines lw 5 title leg6

# Average degree
set output "experiments/citations/cit_avgdeg.eps"
set yrange [0:25]
set title 'Average Degree'
set ylabel '<k>'
plot f1 using 1:4 with lines lw 5 title leg1, \
f2 using 1:4 with lines lw 5 title leg2, \
f3 using 1:4 with lines lw 3 title leg3, \
f4 using 1:4 with lines lw 3 title leg4, \
f5 using 1:4 with lines lw 3 title leg5, \
f6 using 1:4 with lines lw 5 title leg6

# Singletons
set output "experiments/citations/cit_singles.eps"
set yrange [400:1600]
set title 'Singleton Count'
set ylabel '#Nodes of degree 1'
plot f1 using 1:11 with lines lw 3 title leg1, \
f2 using 1:11 with lines lw 3 title leg2, \
f3 using 1:11 with lines lw 3 title leg3, \
f4 using 1:11 with lines lw 3 title leg4, \
f5 using 1:11 with lines lw 3 title leg5, \
f6 using 1:11 with lines lw 3 title leg6

# Doubletons
set output "experiments/citations/cit_doubles.eps"
set yrange [1000:1400]
set title 'Doubleton Count'
set ylabel '#Nodes of degree 2'
plot f1 using 1:12 with lines lw 3 title leg1, \
f2 using 1:12 with lines lw 3 title leg2, \
f3 using 1:12 with lines lw 3 title leg3, \
f4 using 1:12 with lines lw 3 title leg4, \
f5 using 1:12 with lines lw 3 title leg5, \
f6 using 1:12 with lines lw 3 title leg6

# Triangles

set output "experiments/citations/cit_triangles.eps"
set yrange [800000:1000000]
set title 'Triangle Count'
set ylabel '#Triangles'
plot f1 using 1:13 with lines lw 3 title leg1, \
f2 using 1:13 with lines lw 3 title leg2, \
f3 using 1:13 with lines lw 3 title leg3, \
f4 using 1:13 with lines lw 3 title leg4, \
f5 using 1:13 with lines lw 3 title leg5, \
f6 using 1:13 with lines lw 3 title leg6