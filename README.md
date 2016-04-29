# RootMaker

Still missing: 
  - number of charged tracks in taus
  - puppi met / jets
  - gen met
  - unmatched gen particles

Recipe:

    # setup environment
    cmsrel CMSSW_7_6_4
    cd CMSSW_7_6_4/src
    cmsenv
    git cms-init
    
    # add fix for met corr
    echo /CommonTools/PileupAlgos/ > .git/info/sparse-checkout
    echo /CommonTools/Utils/ >> .git/info/sparse-checkout
    echo /JetMETCorrections/Configuration/ >> .git/info/sparse-checkout
    echo /JetMETCorrections/Modules/ >> .git/info/sparse-checkout
    echo /JetMETCorrections/Type1MET/ >> .git/info/sparse-checkout
    echo /PhysicsTools/PatAlgos/ >> .git/info/sparse-checkout
    echo /PhysicsTools/PatUtils/ >> .git/info/sparse-checkout
    echo /RecoMET/METAlgorithms/ >> .git/info/sparse-checkout
    echo /RecoMET/METProducers/ >> .git/info/sparse-checkout
    git cms-merge-topic cms-met:metTool76X
    
    # compile this first bc its kind of a mess. 
    # this step might have to be repeated if there are compilation errors, just do it twice
    scramv1 b -j 20 
    
    ## add stuff for jet pileup id (fix pending)
    #cd $CMSSW_BASE/src
    #git cms-addpkg RecoJets/JetProducers
    #git remote add -f PUJetId https://github.com/jbrands/cmssw.git
    #git checkout PUJetId/pileupJetId76X -b pileupJetId76X
    #cd RecoJets/JetProducers/data/
    #wget https://github.com/jbrands/RecoJets-JetProducers/raw/3dad903ed25d025f68be94d6f781ca957d6f86ac/pileupJetId_76x_Eta0to2p5_BDT.weights.xml.gz
    #wget https://github.com/jbrands/RecoJets-JetProducers/raw/3dad903ed25d025f68be94d6f781ca957d6f86ac/pileupJetId_76x_Eta2p5to2p75_BDT.weights.xml.gz
    #wget https://github.com/jbrands/RecoJets-JetProducers/raw/3dad903ed25d025f68be94d6f781ca957d6f86ac/pileupJetId_76x_Eta2p75to3_BDT.weights.xml.gz
    #wget https://github.com/jbrands/RecoJets-JetProducers/raw/3dad903ed25d025f68be94d6f781ca957d6f86ac/pileupJetId_76x_Eta3to5_BDT.weights.xml.gz
    #cd ../../..
    ## build
    #scramv1 b -j 20 
    
    # checkout actual ntuplizer
    git clone https://github.com/ekenn003/RootMaker.git
    # build
    scramv1 b -j 20
