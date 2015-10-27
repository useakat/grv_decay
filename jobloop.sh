#!/bin/bash

i=$1
imax=$2
iiimin=$3

job_system=$4
que=$5
jobname=$6
submit_mode=$7
mg5dir=$8

logflag=$9
min=${10}
max=${11}
ndiv=${12}

ii=1
while [ $ii -eq 1 ];do
    job=${jobname}_$i
    if [ $i -lt 20 ];then
#	nevents=100000
	nevents=1000
    else
	nevents=10000
    fi

    if [ $logflag -eq 1 ];then
	x=`echo "scale=5; e( (l($min)/l(10) +(l($max)/l(10) -l($min)/l(10))/$ndiv*$i)*l(10) )" | bc -l`
    else
	x=`echo "scale=5; $min +($max -$min)/$ndiv*$i" | bc -l`
    fi
    x=`echo $x |cut -d. -f1`
    ./submit_job_grv_decay.sh $job_system $que $i $job "./run_grv_decay.sh run_$i $x $nevents $mg5dir > allprocess.log" $submit_mode $mg5dir
    ii=`echo "scale=5; if( $i < $imax -1 ) 1 else 0" | bc`
    i=`expr $i + 1`
done
n=$i
if [ $submit_mode -eq 1 ];then
    ./monitor
fi

redocount=0
iii=$iiimin
while [ $iii -lt $n ];do
    cd par_$iii
    if [ -e run.bjob$iii ];then
	redocount=`expr $redocount + 1`
    else
	a=3
    fi    
    cd ..
    iii=`expr $iii + 1`
done
iii=$iiimin
if [ $redocount -eq 0 ];then
    a=3
elif [ $redocount -le 2 ];then
    while [ $iii -lt $n ];do
	cd par_$iii
	if [ -e run.bjob$iii ];then
	    ./bjob$iii 1>/dev/null
	else
	    rm -rf *bjob$iii
	fi    
	cd ..
	iii=`expr $iii + 1`
    done
else
    while [ $iii -lt $n ];do
	cd par_$iii
	if [ -e run.bjob$iii ];then
	    if [ $submit_mode -eq 0 ];then
		./bjob$iii 1>/dev/null
	    else
		bsub -q $que -J $jobname ./bjob$iii 1>/dev/null
	    fi  
	else
	    rm -rf *bjob$iii
	fi    
	cd ..
	iii=`expr $iii + 1`
    done
    if [ $submit_mode -eq 1 ];then
	./monitor
    fi
fi

redocount=0
iii=$iiimin
while [ $iii -lt $n ];do
    cd par_$iii
    if [ -e run.bjob$iii ];then
	redocount=`expr $redocount + 1`
    else
	a=3
    fi    
    cd ..
    iii=`expr $iii + 1`
done
iii=$iiimin
if [ $redocount -eq 0 ];then
    a=3
elif [ $redocount -le 2 ];then
    while [ $iii -lt $n ];do
	cd par_$iii
	if [ -e run.bjob$iii ];then
	    ./bjob$iii 1>/dev/null
	else
	    rm -rf *bjob$iii
	fi    
	cd ..
	iii=`expr $iii + 1`
    done
else
    while [ $iii -lt $n ];do
	cd par_$iii
	if [ -e run.bjob$iii ];then
	    if [ $submit_mode -eq 0 ];then
		./bjob$iii 1>/dev/null
	    else
		bsub -q $que -J $jobname ./bjob$iii 1>/dev/null
	    fi  
	else
	    rm -rf *bjob$iii
	fi    
	cd ..
	iii=`expr $iii + 1`
    done
    if [ $submit_mode -eq 1 ];then
	./monitor
    fi
fi

redocount=0
iii=$iiimin
while [ $iii -lt $n ];do
    cd par_$iii
    if [ -e run.bjob$iii ];then
	redocount=`expr $redocount + 1`
    else
	a=3
    fi    
    cd ..
    iii=`expr $iii + 1`
done
iii=$iiimin
if [ $redocount -eq 0 ];then
    a=3
elif [ $redocount -le 2 ];then
    while [ $iii -lt $n ];do
	cd par_$iii
	if [ -e run.bjob$iii ];then
	    ./bjob$iii 1>/dev/null
	else
	    rm -rf *bjob$iii
	fi    
	cd ..
	iii=`expr $iii + 1`
    done
else
    while [ $iii -lt $n ];do
	cd par_$iii
	if [ -e run.bjob$iii ];then
	    if [ $submit_mode -eq 0 ];then
		./bjob$iii 1>/dev/null
	    else
		bsub -q $que -J $jobname ./bjob$iii 1>/dev/null
	    fi  
	else
	    rm -rf *bjob$iii
	fi    
	cd ..
	iii=`expr $iii + 1`
    done
    if [ $submit_mode -eq 1 ];then
	./monitor
    fi
fi

iii=$iiimin
while [ $iii -lt $n ];do
    cd par_$iii
    if [ -e run.bjob$iii ];then
	./bjob$iii 1>/dev/null
    else
	rm -rf *bjob$iii
    fi    
    cd ..
    iii=`expr $iii + 1`
done