# RootMaker

Still missing: 
  - number of charged tracks in taus
  - puppi met / jets
  - gen met
  - unmatched gen particles

Recipe:

    # setup environment
    cmsrel CMSSW_7_6_5
    cd CMSSW_7_6_5/src
    cmsenv
    git cms-init
    
    # checkout and build
    git clone https://github.com/ekenn003/RootMaker.git
    scramv1 b -j 20
