#!/bin/bash
# chmod me and run me with ./submit_many_jobs.sh
n=$(date +%m%d%H%M)
submit_sig=false
submit_bkg=false
submit_data_rereco=false
submit_data_prompt=false


era="feb17"
try="try1_$n"


submit_sig=true
submit_bkg=true
#submit_data_rereco=true
#submit_data_prompt=true

sig_list="inputlist_feb17_sig.txt"
bkg_list="inputlist_feb17_bkg.txt"
data_list_rereco="inputlist_feb17_data_rereco.txt"
data_list_prompt="inputlist_feb17_data_prompt.txt"


if [ "$submit_sig" = "true" ]; then
    ./submit_many_crab_jobs.py --samplelist $sig_list --era $era --trystring $try --filesperjob=5 --isMC
fi 

if [ "$submit_bkg" = "true" ]; then
    ./submit_many_crab_jobs.py --samplelist $bkg_list --era $era --trystring $try --filesperjob=5 --isMC
fi 

if [ "$submit_data_rereco" = "true" ]; then
    ./submit_many_crab_jobs.py --samplelist $data_list_rereco --era $era --trystring $try --filesperjob=6 --applylumimask="ReReco16" --isReReco
fi

if [ "$submit_data_prompt" = "true" ]; then
    ./submit_many_crab_jobs.py --samplelist $data_list_prompt --era $era --trystring $try --filesperjob=6 --applylumimask="PromptReco16"
fi

