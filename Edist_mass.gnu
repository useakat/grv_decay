if (exist("ii")==0 || ii<0) ii=1
###################### Options ###########################################
set logscale x
set logscale y
set format x '10^{%L}'
#set format x '%L'
set format y '10^{%L}'
#set xtics (2,3,4,5,6)
#set ytics (1,10,1E2,1E3,1E4,1E5,1E6,1E7,1E8,1E9,1E10)
#set tics scale 2
#set key at 1.0E3,1.0E7 samplen 2
#set xrange [1:7]
#set yrange [1E-7:2E8]
####################### Definitions ######################################
mode = 'tautau'
mass = 1000000 # DM mass in GeV
#file1 = 'results/rslt_bbbar_check_1k/np_sptrm_bbbar_'.mass.'.dat'
#file1 = 'results/rslt_'.mode.'_10k/np_sptrm_'.mode.'_'.mass.'.dat'
#file1 = 'results/rslt_'.mode.'_100k/np_sptrm_'.mode.'_'.mass.'.dat'
file1 = 'results/rslt_'.mode.'_10m/np_sptrm_'.mode.'_'.mass.'.dat'
#file1 = 'results/rslt_'.mode.'_100m/np_sptrm_'.mode.'_'.mass.'.dat'
#file1 = 'results/rslt_'.mode.'_800m/np_sptrm_'.mode.'_'.mass.'.dat'
#file1 = 'results/rslt_'.mode.'_1g/np_sptrm_'.mode.'_'.mass.'.dat'
#file1 = 'results/rslt_'.mode.'_test/np_sptrm_'.mode.'_'.mass.'.dat'
c1 = 'red'
c2 = 'blue'
c3 = '#006400' # dark green
c4 = 'purple'
c5 = '#ff33ff'
c6 = '#cc6600' # dark orange
####################### Parameters #######################################
ndiv = 1
Mmin = 1  # for qq~ modes
#Mmin = 1  # for qq~ modes
Mmax = 1000000
##########################################################################
set terminal postscript eps enhanced 'Times-Roman' color 20
set grid
set key spacing 1.5 samplen 2
#set multiplot

set output 'plots/Edist_'.mass.'.eps' 
start = 1 +802*(ii-1) 
end = start +800
set xrange [1E-2:1000000]
set yrange [1E-8:1]
#set yrange [0:10]
#set title '{/=28 Edist}'
set label 'mDM = '.mass.' GeV' at graph 0.05, graph 0.92
set xlabel '{/=24 kinetic energy [GeV]}'
set ylabel '{/=24 Particles / DM decay}' offset 0,0
#################### plot ##########################################
plot \
file1 every ::start::end u 2:3 title "neutron" w l lt 1 lw 3 lc rgb c1, \
file1 every ::start::end u 2:4 title "proton" w l lt 1 lw 3 lc rgb c2, \
file1 every ::start::end u 2:5 title "pi+" w l lt 1 lw 3 lc rgb c3, \
file1 every ::start::end u 2:6 title "pi-" w l lt 1 lw 3 lc rgb c4, \
file1 every ::start::end u 2:7 title "K+" w l lt 1 lw 3 lc rgb c5, \
file1 every ::start::end u 2:8 title "K-" w l lt 1 lw 3 lc rgb c6, \
file1 every ::start::end u 2:9 title "KLong" w l lt 2 lw 3 lc rgb c1, \
file1 every ::start::end u 2:10 title "anti-neutron" w l lt 2 lw 3 lc rgb c2, \
file1 every ::start::end u 2:11 title "anti-proton" w l lt 2 lw 3 lc rgb c3
###########################################################################

#set nomultiplot
unset label

if (ii<ndiv) pause 0.1; ii=ii+1; \
reread
ii=-1

reset

