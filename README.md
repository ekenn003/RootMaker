# RootMaker

Recipe:

    # setup environment
    cmsrel CMSSW_8_0_25
    cd CMSSW_8_0_25/src
    cmsenv
    git cms-init
    
    git cms-merge-topic cms-met:METRecipe_8020
    
    # checkout and build
    git clone -b 80X git@github.com:ekenn003/RootMaker.git
    scramv1 b -j 20

