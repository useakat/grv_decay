#!/bin/bash

run=$1
mail=$2

###### MODIFY HERE: running parameters #################
output=hadron_dist.dat
jobname=grv_decay
submit_mode=0 # 0:serial submittion 1:parallel submission
job_system=bsub
que=l

min=100
#max=1000000
max=1000
#chi0mass=227
chi0mass=120 # model case1 
ndiv=1
#ndiv=3
logflag=1

imin=2
#imax=31
imax=`expr $ndiv + 1`
#imin=2
#imax=3
mg5dir=grv_decay
######################################################
start=`date`
echo $start

i=$imin
while [ $i -le $imax ];do
    job=${jobname}_$i
    if [ $i -eq 1 ];then
	x=$min
    elif [ $i -le $ndiv ];then
	if [ $logflag -eq 1 ];then
	    x=`echo "scale=5; e( (l($min)/l(10) +(l($max)/l(10) -l($min)/l(10))/$ndiv*($i-1))*l(10) )" | bc -l`
	else
	    x=`echo "scale=5; $min +($max -$min)/$ndiv*($i-1)" | bc -l`
	fi
    else
	x=$max
    fi
    if [ $i -le 15 ];then
#	nevents=250000
	nevents=1000
    else
#	nevents=50000
	nevents=1000
    fi
#    ./submit_job_grv_decay.sh $job_system $que $i $job "./run_grv_decay.sh run_$i $x $nevents $mg5dir $chi0mass > allprocess.log" $submit_mode $mg5dir
    ./submit_job_grv_decay_icrr.sh $job_system $que $i $job "./run_grv_decay.sh run_$i $x $nevents $mg5dir $chi0mass > allprocess.log" $submit_mode $mg5dir
    i=`expr $i + 1`
done
n=$i

if [ $submit_mode -eq 1 ];then
    ./monitor
    i=$imin
    while [ $i -lt $n ];do
    	cd par_$i
    	if [ -e done.bjob$i ];then
    	    a=3
    	else
    	    ./bjob$i
    	fi
    	cd ..
    	i=`expr $i + 1`
    done
fi

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
x=$min
i=$imin
while [ $i -lt $n ];do
### MODIFY HERE for preparing result files ###############
    grvinfo=`cat par_$i/grvinfo.dat`
    Evis_tot=`cat par_$i/data/run_$i/Evis_tot.dat`
    echo $grvinfo $Evis_tot >> $rsltdir/$output
    cat par_$i/data/run_$i/Edist.dat >> $rsltdir/$output
    echo "%%%%%" >> $rsltdir/$output
    if [ $i -eq $imin ];then
	cat par_$i/data/run_$i/np_sptrm.dat > $rsltdir/np_sptrm_$ext.dat
	cat par_$i/data/run_$i/nini.dat > $rsltdir/nini_$ext.dat
	cat par_$i/data/run_$i/Evis.dat > $rsltdir/Evis_$ext.dat
    else
	cat par_$i/data/run_$i/np_sptrm.dat >> $rsltdir/np_sptrm_$ext.dat
	cat par_$i/data/run_$i/nini.dat >> $rsltdir/nini_$ext.dat
	cat par_$i/data/run_$i/Evis.dat >> $rsltdir/Evis_$ext.dat
    fi
###################################################
    i=`expr $i + 1`
done

### MODIFY HERE for saving files relatee to this run
cp -rf par_$imin/param_card.dat $rsltdir/.
cp -rf par_$imin/run_card.dat $rsltdir/.
cp -rf par_$imin/run_grv_decay.sh $rsltdir/.
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