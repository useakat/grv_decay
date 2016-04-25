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
    rm -rf grv_decay

    cp -rf grv_decay_def grv_decay
#    cp -rf grv_decay_2body_test grv_decay
#    cp -rf grv_2body+n1ff grv_decay
#    cp -rf grv_n1a_n1jj2 grv_decay
#    cp -rf grv_n1jetjet grv_decay
#    cp -rf grv_azh01_n1jetjet grv_decay

    cp ./susyhit/param_card_temp.dat.cmssm ./grv_decay/Cards/param_card_temp.dat

##### modify chi0mass in run_grv_decay_parallel.sh

    ./run_grv_decay_parallel.sh cmssm_2body_factor100 100 1
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
#fi