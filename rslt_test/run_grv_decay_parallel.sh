#!/bin/bash

run=$1
factor=$2
mail=$3
###### MODIFY HERE: running parameters #################
output=hadron_dist.dat
jobname=grv_decay
submit_mode=1      # 0:serial submittion 1:parallel submission
#job_system=kekcc  # name of computer cluster: kekcc/icrr
job_system=icrr    # name of computer cluster: kekcc/icrr
que=l

min=100
max=1000000
chi0mass=416.877 # CMSSM model
#chi0mass=188 # Natural SUSY model
#chi0mass=400 # Light gaugino model
ndiv=40
logflag=1

#imin=1
#imax=`expr $ndiv + 1`
imin=39
imax=39
mg5dir=grv_decay

# working space for jobs on a remote server
if [ $job_system == "icrr" ];then
    work_dir=/disk/th/work/takaesu/$run
    if [ -e $workdir ];then
	rm -rf $workdir
    fi
    mkdir $work_dir
elif [ $job_system == "kekcc" ];then
    work_dir=./
fi
######################################################
start=`date`
echo $start

rm -rf par_*

flag_start=0
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

    if [ $i -le 28 ];then
	nevents=`expr 8000 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 7000 \* $factor` # for AMSB
    elif [ $i -le 29 ];then
	nevents=`expr 7500 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 5600 \* $factor` # for AMSB
    elif [ $i -le 30 ];then
	nevents=`expr 7050 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 4500 \* $factor` # for AMSB
    elif [ $i -le 31 ];then
	nevents=`expr 5780 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 4100 \* $factor` # for AMSB
    elif [ $i -le 32 ];then
	nevents=`expr 4700 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 3400 \* $factor` # for AMSB
    elif [ $i -le 33 ];then
	nevents=`expr 3960 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 2700 \* $factor` # for AMSB
    elif [ $i -le 34 ];then
	nevents=`expr 3260 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 2200 \* $factor` # for AMSB
    elif [ $i -le 35 ];then
	nevents=`expr 2700 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 1800 \* $factor` # for AMSB
    elif [ $i -le 36 ];then
	nevents=`expr 2200 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 1400 \* $factor` # for AMSB
    elif [ $i -le 37 ];then
	nevents=`expr 1800 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 1200 \* $factor` # for AMSB
    elif [ $i -le 38 ];then
	nevents=`expr 1500 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 1000 \* $factor` # for AMSB
    elif [ $i -le 39 ];then
	nevents=`expr 1200 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 840 \* $factor` # for AMSB
    elif [ $i -le 40 ];then
	nevents=`expr 1000 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 680 \* $factor` # for AMSB
    elif [ $i -le 41 ];then
	nevents=`expr 900 \* $factor` # for CMSSM & Natural SUSY
#	nevents=`expr 550 \* $factor` # for AMSB
    else
	nevents=0
    fi

    if [ $flag_start -eq 0 ];then
	xx=`echo "scale=5; if( $x > $chi0mass ) 1 else 0" | bc`
	if [ $xx -eq 1 ];then
	    istart=$i
	    flag_start=1
	fi
    fi

#    echo $job_system $que $i $job "./run_grv_decay.sh run_$i $x $nevents $mg5dir $chi0mass > allprocess.log" $submit_mode $mg5dir
    ./submit_job_grv_decay.sh $job_system $que $i $job "./run_grv_decay.sh run_$i $x $nevents $mg5dir $chi0mass" $submit_mode $mg5dir $work_dir
    i=`expr $i + 1`
done
n=$i

if [ $submit_mode -eq 1 ];then
    ./monitor $work_dir
    # i=$imin
    # while [ $i -lt $n ];do
    # 	cd par_$i
    # 	if [ -e done.bjob$i ];then
    # 	    a=3
    # 	else
    # 	    ./bjob$i
    # 	fi
    # 	cd ..
    # 	i=`expr $i + 1`
    # done
fi
if [ $job_system == "icrr" ];then
    mv $work_dir/* .
    rm -rf $work_dir
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
#i=$imin
i=$istart
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
    # copy log file 
    cp -rf par_$i/allprocess.log $rsltdir/allprocess_$i.log
    i=`expr $i + 1`
done

### make plots
mkdir $rsltdir/plots
cp -rf Edist.gnu $rsltdir/.
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

echo "finished!"
echo $start
echo `date`

#rm -rf par_*

./mail_notify $mail $job_system $jobname