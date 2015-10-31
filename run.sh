#!/bin/bash

cd SUSYspc
./make_spectrum.sh
cd ..

param_ext=temp
cp -rf grv_decay_def grv_decay
cp -rf SUSYspc/SPheno.spc grv_decay/Cards/param_card_$param_ext.dat

#./run_grv_decay_parallel.sh HSUSY 1
# ./run_grv_decay_parallel.sh case1.120.100k_noSLHAdecay 1
# ./run_grv_decay_parallel.sh case1.120.100k 1
#./run_grv_decay_parallel.sh test3 0