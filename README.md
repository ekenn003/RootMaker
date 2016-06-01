# RootMaker

Still missing: 
  - number of charged tracks in taus
  - puppi met / jets
  - unmatched gen particles

Recipe:

    # setup environment
    cmsrel CMSSW_8_0_9
    cd CMSSW_8_0_9/src
    cmsenv
    git cms-init
    
    # checkout and build
    git clone -b 80X https://github.com/ekenn003/RootMaker.git
    scramv1 b -j 20
