set term postscript eps enhanced color 24
set font ",20"

file = "experiments/citations/triangle_analysis.txt"

set output "experiments/citations/triangle_analysis_real.eps"

set title "End-degrees of triangle-closing edges"
set xlabel "Degree of sourcenode"
set ylabel "Degree of destnode"
plot file using 1:2 pt 7 ps 0.5