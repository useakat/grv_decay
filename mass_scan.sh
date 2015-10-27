#!/bin/bash

run=$1
mail=$2

###### MODIFY HERE: running parameters #################
output=width_mass.dat
jobname=grv_width
submit_mode=0 # 0:serial submittion 1:parallel submission
job_system=bsub
que=s
cmnd="../bin/generate_events test -f > $output"

# model case1 - case4 are those defined in PRD78.065011 (2008)
#min=130 #case1
#min=260 #case2
#min=130 #case3
min=530 #case4
#min=10000
max=1000000
ndiv=30
logflag=1
######################################################
start=`date`
echo $start

x=$min
xx=1
i=1
while [ $xx -eq 1 ];do
    job=${jobname}_$i
#    sed -e "s/MMGRV/$x/" Cards/param_card_case1.dat > Cards/param_card.dat
#    sed -e "s/MMGRV/$x/" Cards/param_card_case2.dat > Cards/param_card.dat
#    sed -e "s/MMGRV/$x/" Cards/param_card_case3.dat > Cards/param_card.dat
    sed -e "s/MMGRV/$x/" Cards/param_card_case4.dat > Cards/param_card.dat
    ./submit_job_mass_scan.sh $job_system $que $i $job "$cmnd" $submit_mode
    if [ $logflag -eq 1 ];then
	x=`echo "scale=5; e( (l($min)/l(10) +(l($max)/l(10) -l($min)/l(10))/$ndiv*$i)*l(10) )" | bc -l`
    else
	x=`echo "scale=5; $min +($max -$min)/$ndiv*$i" | bc -l`
    fi
    xx=`echo "scale=5; if( $x < $max ) 1 else 0" | bc`
    i=`expr $i + 1`
done
n=$i

if [ $submit_mode -eq 1 ];then
    ./monitor
fi

rsltdir=rslt_$run
if [ -e $rsltdir ];then
    a=3
else
    mkdir $rsltdir
fi
rm -rf $rsltdir/$output
touch $rsltdir/$output

x=$min
i=1
while [ $i -lt $n ];do
### MODIFY HERE for preparing result files ###############
    line=`grep "Width :" par_${i}/$output `
    width=${line#*:}
    width=${width%+-*}
    echo $x $width >> $rsltdir/$output
    if [ $logflag -eq 1 ];then
	x=`echo "scale=5; e( (l($min)/l(10) +(l($max)/l(10) -l($min)/l(10))/$ndiv*$i)*l(10) )" | bc -l`
    else
	x=`echo "scale=5; $min +($max -$min)/$ndiv*$i" | bc -l`
    fi
###################################################
    i=`expr $i + 1`
done

### MODIFY HERE for saving files relatee to this run
cp -rf par_1/Cards/param_card.dat $rsltdir/.
cp -rf mass_scan.sh $rsltdir/.
###################################################

echo "finished!"
echo $start
echo `date`

rm -rf par_*

if [ $mail -eq 1 ];then
    bsub -q e -J cbscan -u takaesu@post.kek.jp nulljob.sh >/dev/null 2>&1
fi