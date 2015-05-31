set terminal postscript landscape monochrome font "times,18" solid size 9,5.6
set output 'be_distribution.eps'
set boxwidth 0.2 absolute
set title "Distribution of binding energies\nalong binding pathway" 
set xrange [ 0.00000 : 8.0000 ] noreverse nowriteback
set yrange [ -7.5 : -4.0 ] noreverse nowriteback
set xtics ("C3" 1, "C2" 2, "C1" 3, "A" 4, "T1" 5, "T2" 6, "T3" 7)
set xlabel ("Points on binding pathway")
set ylabel ("Binding energy (kcal/mol)")
plot 'be_distribution.dat' using 1:3:2:6:5 with candlesticks lt 3 lw 1.2 notitle whiskerbars,'' using 1:4:4:4:4 with candlesticks lt -1 lw 1.2 notitle
