#!/bin/bash

run=$1
istart=$2
iend=$3
mail=$4
###### MODIFY HERE: running parameters #################
#job_system=kekcc  # name of computer cluster: kekcc/icrr
job_system=icrr    # name of computer cluster: kekcc/icrr
job_name=combine_results
output=hadron_dist.dat
imin=1
######################################################
start=`date`
echo $start

rsltdir=rslt_$run
if [ -e $rsltdir ];then
    a=3
else
    mkdir $rsltdir
fi
rm -rf $rsltdir/$output
touch $rsltdir/$output

ext=gravitino
echo "1, 141, 300, 0, 30, 1" >> $rsltdir/$output
echo "%%%%%" >> $rsltdir/$output

i=$istart
n=`expr $iend`
while [ $i -le $n ];do
### MODIFY HERE for preparing result files ###############
    grvinfo=`cat par_$i/grvinfo.dat`
    Evis_tot=`cat par_$i/data/run_$i/Evis_tot.dat`
    echo $grvinfo $Evis_tot >> $rsltdir/$output
    cat par_$i/data/run_$i/Edist.dat >> $rsltdir/$output
    echo "%%%%%" >> $rsltdir/$output
    if [ $i -eq $istart ];then
	cat par_$i/data/run_$i/np_sptrm.dat > $rsltdir/np_sptrm_$ext.dat
	cat par_$i/data/run_$i/nini.dat > $rsltdir/nini_$ext.dat
	cat par_$i/data/run_$i/Evis.dat > $rsltdir/Evis_$ext.dat
    else
	cat par_$i/data/run_$i/np_sptrm.dat >> $rsltdir/np_sptrm_$ext.dat
	cat par_$i/data/run_$i/nini.dat >> $rsltdir/nini_$ext.dat
	cat par_$i/data/run_$i/Evis.dat >> $rsltdir/Evis_$ext.dat
    fi
    # copy log file 
    cp -rf par_$i/allprocess.log $rsltdir/allprocess_$i.log
    i=`expr $i + 1`
done

### make plots
./makedir.sh $rsltdir/plots 1
ioffset=`expr $istart - 1`
sed -e "s/OFFSET/$ioffset/" Edist.gnu > Edist.tmp
mv Edist.tmp $rsltdir/Edist.gnu
##########################################################################

### MODIFY HERE for saving files relatee to this run
cp -rf par_$imin/param_card.dat $rsltdir/.
cp -rf par_$imin/run_card.dat $rsltdir/.
cp -rf run.sh $rsltdir/.
cp -rf run_grv_decay_parallel.sh $rsltdir/.
cp -rf submit_job_grv_decay.sh $rsltdir/.
cp -rf par_$imin/run_grv_decay.sh $rsltdir/.
git log --oneline | head -1 | tail -1 > $rsltdir/program.version
###################################################

cd $rsltdir
gnuplot Edist.gnu
cd ..

echo "finished combine!"
echo $start
echo `date`

./mail_notify $mail $job_system $job_name