#!/bin/bash

#mode=1   # 0:parameter card preparation mode, 1:run mode

# if [ $mode -eq 0 ];then
#     cd SUSYspc
#     ./make_spectrum.sh
#     cd ..
#     param_ext=temp
#     cp -rf grv_decay_def grv_decay
#     cp -rf SUSYspc/SPheno.spc grv_decay/Cards/param_card_$param_ext.dat
# elif [ $mode -eq 1 ];then
#    rm -rf grv_decay

#    cp -rf grv_decay_def grv_decay
#    cp -rf grv_decay_2body_test grv_decay
#    cp -rf grv_2body+n1ff grv_decay
#    cp -rf grv_n1a_n1jj2 grv_decay
#    cp -rf grv_n1jetjet grv_decay
#    cp -rf grv_azh01_n1jetjet grv_decay

#    cp ./susyhit/param_card_temp.dat.cmssm ./grv_decay/Cards/param_card_temp.dat

##### modify chi0mass in run_grv_decay_parallel.sh

#    ./run_grv_decay_parallel.sh cmssm_2body_factor1 1 1
#    ./run_grv_decay_parallel.sh cmssm_test_factor100 100 1
#    ./run_grv_decay_parallel.sh cmssm_2body_factor10_test 10 1
#    ./run_grv_decay_parallel.sh cmssm_2body_factor100_test 100 1
#    ./run_grv_decay_parallel.sh cmssm_2body_factor100_2 100 1
#    ./run_grv_decay_parallel.sh cmssm_factor100 100 1
#    ./run_grv_decay_parallel.sh cmssm_2body+n1ff_factor1 1 1
#    ./run_grv_decay_parallel.sh cmssm_2body+n1ff_factor10 10 1
#    ./run_grv_decay_parallel.sh cmssm_2body+n1ff_factor1_test 1 1
#    ./run_grv_decay_parallel.sh cmssm_n1jetjet_factor1_test 1 1
#    ./run_grv_decay_parallel.sh test 10 1
#    ./run_grv_decay_parallel.sh cmssm_n1qq~_factor1 1 1
#    ./run_grv_decay_parallel.sh cmssm_2body+3body_factor100_2 100 1
#    ./run_grv_decay_parallel.sh natural_2body+3body_factor100 100 1
#    ./run_grv_decay_parallel.sh amsb_2body+3body_factor100 100 1
#    ./run_grv_decay_parallel.sh amsb_2body+3body_factor1 1 1
#    ./run_grv_decay_parallel.sh amsb_2body+3body_factor10_2 10 1
    run=amsb1_factor1
    model=amsb1
    factor=1
    rm -rf par_*
    ./run_grv_decay_parallel_no-combine.sh $run $model $factor 1 41 0
#    ./run_grv_decay_parallel_no-combine.sh $run $model $factor 15 16 0
    istart=`cat istart.dat`
    rm -rf istart.dat
    ./combine_results.sh $run $istart 41 1
#fi