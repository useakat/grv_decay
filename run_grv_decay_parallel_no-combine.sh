#!/bin/bash

run=$1
model=$2 # cmssm/natural/amsb1/amsb2
factor=$3 # factor for the generated event number
imin=$4 # 1 <= imin <= 41
imax=$5 # 1 <= imax <= 41
mail=$6
###### MODIFY HERE: running parameters #################
output=hadron_dist.dat
jobname=grv_decay
submit_mode=1      # 0:serial submittion 1:parallel submission
#job_system=kekcc  # name of computer cluster: kekcc/icrr
job_system=icrr    # name of computer cluster: kekcc/icrr
que=l

min=100
max=1000000
zmass=91

if [ $model == "cmssm" ];then # CMSSM model
    chi0mass=416.877 
elif [ $model == "natural" ];then # Natural SUSY model
    chi0mass=188 
elif [ $model == "amsb1" ];then # Light gaugino model 1 
    chi0mass=1000 
elif [ $model == "amsb2" ];then # Light gaugino model 2
    chi0mass=500 
fi

ndiv=40
logflag=1

#imin=1
#imax=`expr $ndiv + 1`

mg5dir_2body=grv_decay_def
mg5dir_3body=grv_2body+n1jetjet

# working space for jobs on a remote server
if [ $job_system == "icrr" ];then
    work_dir=/disk/th/work/takaesu/$run
    if [ -e $work_dir ];then
	echo "$work_dir exists. Delete and remake it"
	rm -rf $work_dir
    fi
    mkdir $work_dir
elif [ $job_system == "kekcc" ];then
    work_dir=./
fi

######################################################
start=`date`
echo $start

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

    if [ $model == "amsb1" -o $model == "amsb2" ];then
	if [ $i -le 28 ];then
	    nevents=`expr 7000 \* $factor` # for AMSB
	elif [ $i -le 29 ];then
	    nevents=`expr 5600 \* $factor` # for AMSB
	elif [ $i -le 30 ];then
	    nevents=`expr 4500 \* $factor` # for AMSB
	elif [ $i -le 31 ];then
	    nevents=`expr 4100 \* $factor` # for AMSB
	elif [ $i -le 32 ];then
	    nevents=`expr 3400 \* $factor` # for AMSB
	elif [ $i -le 33 ];then
	    nevents=`expr 2700 \* $factor` # for AMSB
	elif [ $i -le 34 ];then
	    nevents=`expr 2200 \* $factor` # for AMSB
	elif [ $i -le 35 ];then
	    nevents=`expr 1800 \* $factor` # for AMSB
	elif [ $i -le 36 ];then
	    nevents=`expr 1400 \* $factor` # for AMSB
	elif [ $i -le 37 ];then
	    nevents=`expr 1200 \* $factor` # for AMSB
	elif [ $i -le 38 ];then
	    nevents=`expr 1000 \* $factor` # for AMSB
	elif [ $i -le 39 ];then
	    nevents=`expr 840 \* $factor` # for AMSB
	elif [ $i -le 40 ];then
	    nevents=`expr 680 \* $factor` # for AMSB
	elif [ $i -le 41 ];then
	    nevents=`expr 550 \* $factor` # for AMSB
	else
	    nevents=0
	fi
    else
	if [ $i -le 28 ];then
	    nevents=`expr 8000 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 29 ];then
	    nevents=`expr 7500 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 30 ];then
	    nevents=`expr 7050 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 31 ];then
	    nevents=`expr 5780 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 32 ];then
	    nevents=`expr 4700 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 33 ];then
	    nevents=`expr 3960 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 34 ];then
	    nevents=`expr 3260 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 35 ];then
	    nevents=`expr 2700 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 36 ];then
	    nevents=`expr 2200 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 37 ];then
	    nevents=`expr 1800 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 38 ];then
	    nevents=`expr 1500 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 39 ];then
	    nevents=`expr 1200 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 40 ];then
	    nevents=`expr 1000 \* $factor` # for CMSSM & Natural SUSY
	elif [ $i -le 41 ];then
	    nevents=`expr 900 \* $factor` # for CMSSM & Natural SUSY
	else
	    nevents=0
	fi
    fi

    if [ $flag_start -eq 0 ];then
	xx=`echo "scale=5; if( $x > $chi0mass ) 1 else 0" | bc`
	if [ $xx -eq 1 ];then
	    istart=$i
	    flag_start=1
	fi
    fi
    
    threshold_mass=`echo "scale=5; $chi0mass +$zmass" | bc`
    zz=`echo "scale=5; if( $x < $threshold_mass ) 1 else 0" | bc`
    if [ $zz -eq 1 ];then
	mg5dir=$mg5dir_3body
    else
	mg5dir=$mg5dir_2body
    fi
    cp ./susyhit/param_card_temp.dat.$model ./$mg5dir/Cards/param_card_temp.dat

#    echo $job_system $que $i $job "./run_grv_decay.sh run_$i $x $nevents $mg5dir $chi0mass > allprocess.log" $submit_mode $mg5dir
    ./submit_job_grv_decay.sh $job_system $que $i $job "./run_grv_decay.sh run_$i $x $nevents $mg5dir $chi0mass" $submit_mode $mg5dir $work_dir
    i=`expr $i + 1`
done
n=$i

if [ ! -e istart.dat ];then
    echo $istart > istart.dat
fi

if [ $submit_mode -eq 1 ];then
    ./monitor $work_dir
fi
if [ $job_system == "icrr" ];then
    cp -rf $work_dir/* .
    rm -rf $work_dir
fi

echo "finished!"
echo $start
echo `date`

#rm -rf par_*

./mail_notify $mail $job_system $jobname