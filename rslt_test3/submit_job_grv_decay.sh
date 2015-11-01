#!/bin/bash
selfdir=$(cd $(dirname $0);pwd)
if [[ "$1" == "-h" ]]; then
    echo ""
    echo "Usage: submit_job.sh [job_system] [que] [it] [jobname] [command]"
    echo ""
    exit
fi

job_system=$1
que=$2
i=$3
jobname=$4
command="$5"
submit_mode=$6 # 0:serial 1:parallel
mg5dir=$7

njob=bjob

dir=par_$i
mkdir $dir
cd $dir

echo "#!/bin/bash" > $njob$i
echo "" >> $njob$i
if [ $job_system == "icrr" ];then
    echo '#------ pjsub option --------#' >> $njob$i
    echo '#PJM -L "rscunit=common"' >> $njob$i
    echo '#PJM -L "rscgrp=A"' >> $njob$i
#    echo '#PJM -L "rscunit=group"' >> $njob$i
#    echo '#PJM -L "rscgrp=th"' >> $njob$i
    echo '#PJM -L "vnode=1"' >> $njob$i
    echo '#PJM -L "vnode-core=1"' >> $njob$i
#    echo '#PJM -L "elapse=00:30:00"' >> $njob$i # A:<3h B:<24h C:<1week th:no limit
    echo "" >> $njob$i
fi
echo '#------- Program execution -------#' >> $njob$i
echo "date >allprocess.log" >> $njob$i
echo "rm -rf $selfdir/$dir/wait.${njob}$i" >> $njob$i
echo "touch $selfdir/$dir/run.${njob}$i" >> $njob$i
echo "cp -rf ../makedir.sh ." >> $njob$i
echo "cp -rf ../$mg5dir ." >> $njob$i
echo "cp -rf ../pythia ." >> $njob$i
echo "cp -rf ../run_grv_decay.sh ." >> $njob$i
echo "./makedir.sh $selfdir/$dir/data 0" >> $njob$i
echo "$command >>allprocess.log 2>&1" >> $njob$i
echo "rm -rf $selfdir/$dir/run.${njob}$i" >> $njob$i
echo "touch $selfdir/$dir/done.${njob}$i" >> $njob$i
echo "cp -rf $mg5dir/Cards/param_card.dat ." >> $njob$i
echo "cp -rf $mg5dir/Cards/run_card.dat ." >> $njob$i
#echo "rm -rf $mg5dir" >> $njob$i
#echo "rm -rf pythia" >> $njob$i

chmod +x $njob$i
touch wait.$njob$i

if [ $submit_mode -eq 0 ];then
    echo "job$i launched"
#    ./$njob$i 1>/dev/null
    ./$njob$i
    echo "job$i finished"
    echo
else
    if [ $job_system == "kekcc" ];then
#    bsub -q $que -J $jobname ./$njob$i 1>/dev/null
	bsub -q $que -J $jobname ./$njob$i
    elif [ $job_system == "icrr" ];then
	pjsub -N $jobname -j $njob$i
    fi
    echo ""
fi

cd ..
