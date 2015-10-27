#!/bin/bash

run=$1
mail=$2

###### MODIFY HERE: running parameters #################
output=width_mass.dat
jobname=grv_decay
submit_mode=0 # 0:serial submittion 1:parallel submission
job_system=bsub
que=s

# gravitino mass
min=100
max=10000
ndiv=30
logflag=1

mg5dir=grv_decay
######################################################
start=`date`
echo $start

i=0
iiimin=0
imax=`expr $ndiv + 1`
./jobloop.sh $i $imax $iiimin $job_system $que $jobname $submit_mode $mg5dir $logflag $min $max $ndiv

#iiimin=`$imax + 1`
#imax=`expr $ndiv + 1`
#./jobloop.sh $i $imax $iiimin $job_system $que $jobname $submit_mode $mg5dir $logflag $min $max $ndiv

n=$imax

rsltdir=rslt_$run
if [ -e $rsltdir ];then
    a=3
else
    mkdir $rsltdir
fi
rm -rf $rsltdir/$output
touch $rsltdir/$output

echo "1, 141, 300, 0, 30, 1" >> $rsltdir/$output
echo "%%%%%" >> $rsltdir/$output
x=$min
i=0
while [ $i -lt $n ];do
### MODIFY HERE for preparing result files ###############
    grvinfo=`cat par_$i/grvinfo.dat`
    Evis_tot=`cat par_$i/data/run_$i/Evis_tot.dat`
#    cat par_$i/grvinfo.dat >> $rsltdir/$output
    echo $grvinfo $Evis_tot >> $rsltdir/$output
    cat par_$i/data/run_$i/Edist.dat >> $rsltdir/$output
    echo "%%%%%" >> $rsltdir/$output
###################################################
    i=`expr $i + 1`
done

### MODIFY HERE for saving files relatee to this run
cp -rf par_1/param_card.dat $rsltdir/.
cp -rf par_1/run_card.dat $rsltdir/.
cp -rf par_1/run_grv_decay.sh $rsltdir/.
cp -rf submit_job_grv_decay.sh $rsltdir/.
cp -rf run_grv_decay_parallel.sh $rsltdir/.
###################################################

echo "finished!"
echo $start
echo `date`

rm -rf par_*

if [ $mail -eq 1 ];then
    bsub -q e -J cbscan -u takaesu@post.kek.jp nulljob.sh >/dev/null 2>&1
fi