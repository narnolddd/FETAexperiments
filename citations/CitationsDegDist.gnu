fileReal = "experiments/citations/Citations_Undir_MeasurementsDeg.dat"
fileCopy = "experiments/citations/Citations_Copy_Undir_MeasurementsDeg.dat"

set term postscript eps enhanced color 24
set font ",20"

set output "experiments/citations/CitationsTSDeg.eps"
set log xy
set title "Degree Distribution of Citation Network and Best Fitting Model"
set xlabel "Degree"
set ylabel "Frequency"
plot fileReal matrix every :::1290::1290 pt 7 title 'Real', fileCopy matrix every :::1290::1290 pt 7 title '0.93 BA, 0.06 Rand, 0.01 Tri'