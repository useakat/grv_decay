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

dir=par_$i
mkdir $dir
cd $dir

cp -rf ../Cards .

echo "#!/bin/bash" > ajob$i
echo "date" >> ajob$i
echo "rm -rf $selfdir/$dir/wait.ajob$i" >> ajob$i
echo "touch $selfdir/$dir/run.ajob$i" >> ajob$i
echo "$command" >> ajob$i
echo "rm -rf $selfdir/$dir/run.ajob$i" >> ajob$i
echo "touch $selfdir/$dir/done.ajob$i" >> ajob$i
chmod +x ajob$i
touch wait.ajob$i

if [ $submit_mode -eq 0 ];then
    ./ajob$i 1>/dev/null
else
    bsub -q $que -J $jobname ./ajob$i 1>/dev/null
fi

cd ..
