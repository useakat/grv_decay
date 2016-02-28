#!/bin/bash

mode=1   # 0:parameter card preparation mode, 1:run mode

if [ $mode -eq 0 ];then
    cd SUSYspc
    ./make_spectrum.sh
    cd ..
    param_ext=temp
    cp -rf grv_decay_def grv_decay
    cp -rf SUSYspc/SPheno.spc grv_decay/Cards/param_card_$param_ext.dat
elif [ $mode -eq 1 ];then
    rm -rf grv_decay
#    cp -rf grv_decay_def grv_decay
    cp -rf grv_decay_2body_test grv_decay
    cp ./susyhit/param_card_temp.dat.cmssm ./grv_decay/Cards/param_card_temp.dat

# modify chi0mass in run_grv_decay_parallel.sh

#./run_grv_decay_parallel.sh HSUSY 1
# ./run_grv_decay_parallel.sh case1.120.100k_noSLHAdecay 1
# ./run_grv_decay_parallel.sh case1.120.100k 1
#    ./run_grv_decay_parallel.sh cmssm 1
#    ./run_grv_decay_parallel.sh natural 1
#    ./run_grv_decay_parallel.sh amsb 1
#    ./run_grv_decay_parallel.sh cmssm_test 1
    ./run_grv_decay_parallel.sh cmssm_2body_test 1
fi