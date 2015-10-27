if (exist("ii")==0 || ii<0) ii=1
###################### Options ###########################################
set logscale x
#set logscale y
set format x '10^{%L}'
#set format x '%L'
#set format y '10^{%L}'
#set xtics (2,3,4,5,6)
#set ytics (1,10,1E2,1E3,1E4,1E5,1E6,1E7,1E8,1E9,1E10)
#set tics scale 2
#set key at 1.0E3,1.0E7 samplen 2
#set xrange [1:7]
#set yrange [1E-5:2E8]
####################### Definitions ######################################
#file1 = 'rslt_div40/Edist_case1.dat'
#file1 = 'rslt_div40_10k/width_mass.dat'
#file1 = 'rslt_div30/width_mass.dat'
#file1 = 'rslt_Hsfermion/width_mass.dat'
#file1 = 'rslt_HSUSY/width_mass.dat'
#file1 = 'rslt_test/width_mass.dat'
#file1 = 'rslt_case1.701.10k/width_mass.dat'
file1 = 'rslt_case1.701.50k/width_mass.dat'
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

set output 'plots/Edist_'.ii.'.eps' 
start = 2 +3*ii +701*(ii-1) 
mass = int(exp((log10(100) +(log10(100000) -log10(100))/30*(ii-1))*log(10)))
end = start +700
set xrange [1E-2:100000]
#set yrange [1E-5:10]
#set yrange [0:10]
set title '{/=28 Edist}'
set label 'm3/2 = '.mass.' GeV' at graph 0.05, graph 0.92
set xlabel '{/=24 Ekin [GeV]}'
set ylabel '{/=24 Number of particles / event}' offset 0,0
#################### plot ##########################################
plot \
file1 every ::start::end u 1:2 title "pi+-" w l lt 1 lw 3 lc rgb c1, \
file1 every ::start::end u 1:3 title "neutron" w l lt 1 lw 3 lc rgb c2, \
file1 every ::start::end u 1:4 title  "proton" w l lt 1 lw 3 lc rgb c3
###########################################################################

#set nomultiplot
unset label

if (ii<31) pause 0.1; ii=ii+1; \
reread
ii=-1

reset

