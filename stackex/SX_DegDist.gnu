fileReal = "experiments/stackex/SX_degdist_fixed_2.dat"
fileCopy = "experiments/stackex/SX_best_degdist_fixed_2.dat"

set term postscript eps enhanced color 24
set font ",20"

set output "experiments/stackex/SX_degdist.eps"
set log xy
set title "Degree Distribution of SX Network and Best Fitting Model"
set xlabel "Degree"
set ylabel "Frequency"
plot fileReal matrix every :::49::49 pt 7 title 'Real', fileCopy matrix every :::49::49 pt 7 title '0.89 DegAge, 0.02 Rand, 0.09 Tri'