###################### Options ###########################################
set logscale x
set logscale y
set format x '%L'
set format y '10^{%L}'
#set xtics (2,3,4,5,6)
#set ytics (1,10,1E2,1E3,1E4,1E5,1E6,1E7,1E8,1E9,1E10)
#set tics scale 2
#set key at 1.0E3,1.0E7 samplen 2
#set xrange [1:7]
#set yrange [1E-5:2E8]
####################### Definitions ######################################
file1 = 'dist.dat'
c1 = 'red'
c2 = 'blue'
c3 = '#006400' # dark green
c4 = 'purple'
c5 = '#ff33ff'
c6 = '#cc6600' # dark orange
##########################################################################
set terminal postscript eps enhanced 'Times-Roman' color 20
set grid
set key spacing 1.5 samplen 2
#set multiplot
 
set output 'z_decay_Ele_log.eps'
#file2 = 'test2/GamE.dat'
file2 = 'dist_takaesu.dat'
#file3 = 'GamE_pythia.dat'
set title '{/=28 e^+ + e^- distribution}'
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Electrons/Z-decay}' offset 1.5,0
#################### plot ##########################################
plot \
file1 u 1:2 title 'Moroi' lc rgb c1, \
file2 u 1:2 title 'Takesu' lc rgb c2
###########################################################################

set output 'z_decay_Gam_log.eps'
set title '{/=28 Photon distribution}'
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Photons/Z-decay}' offset 1.5,0
#################### plot ##########################################
plot \
file1 u 1:3 title 'Moroi' lc rgb c1, \
file2 u 1:3 title 'Takesu' lc rgb c2
###########################################################################

set output 'z_decay_P_log.eps'
set title '{/=28 p^+ + p^- distribution}'
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Protons/Z-decay}' offset 1.5,0
#################### plot ##########################################
plot \
file1 u 1:4 title 'Moroi' lc rgb c1, \
file2 u 1:4 title 'Takesu' lc rgb c2
###########################################################################

set output 'z_decay_N_log.eps'
set title '{/=28 n^+ + n^- distribution}'
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Neutrons/Z-decay}' offset 1.5,0
#################### plot ##########################################
plot \
file1 u 1:5 title 'Moroi' lc rgb c1, \
file2 u 1:5 title 'Takesu' lc rgb c2
###########################################################################

set output 'z_decay_Neue_log.eps'
set title '{/=28 neu_e + neu_e-bar distribution}'
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Neu_e/Z-decay}' offset 1.5,0
#################### plot ##########################################
plot \
file1 u 1:6 title 'Moroi' lc rgb c1, \
file2 u 1:6 title 'Takesu' lc rgb c2
###########################################################################

set output 'z_decay_Neumu_log.eps'
set title '{/=28 neu_mu + neu_mu-bar distribution}'
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Neu_mu/Z-decay}' offset 1.5,0
#################### plot ##########################################
plot \
file1 u 1:7 title 'Moroi' lc rgb c1, \
file2 u 1:7 title 'Takesu' lc rgb c2
###########################################################################

set output 'z_decay_Neutau_log.eps'
set title '{/=28 neu_tau + neu_tau-bar distribution}'
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Neu_tau/Z-decay}' offset 1.5,0
#################### plot ##########################################
plot \
file1 u 1:8 title 'Moroi' lc rgb c1, \
file2 u 1:8 title 'Takesu' lc rgb c2
###########################################################################

#set nomultiplot
reset
