#include "RootMaker/RootMaker/interface/RootMaker.h"

RootMaker::RootMaker(const edm::ParameterSet &iConfig) :
    lheEventProductToken_(consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag>("lheEventProduct"))),
    genEventInfoToken_(consumes<GenEventInfoProduct>(iConfig.getParameter<edm::InputTag>("genEventInfo"))),
    rhoToken_(consumes<double>(iConfig.getParameter<edm::InputTag>("rho"))),
    PUInfoToken_(consumes<std::vector<PileupSummaryInfo> >(iConfig.getParameter<edm::InputTag>("pileupSummaryInfo"))),
    lumiInfoToken_(consumes<LumiSummary>(iConfig.getParameter<edm::InputTag>("lumiProducer"))),
    triggerBitsToken_(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("triggerResults"))),
    filterBitsToken_(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("filterResults"))),
    triggerObjectsToken_(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("triggerObjects"))),
    triggerPrescalesToken_(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("triggerPrescales"))),

    l1TriggerToken_(consumes<L1GlobalTriggerReadoutRecord>(iConfig.getParameter<edm::InputTag>("l1trigger"))),
    beamSpotToken_(consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("beamSpot"))),

    triggerBranches(iConfig.getParameter<edm::ParameterSet>("triggerBranches")),
    filterBranches(iConfig.getParameter<edm::ParameterSet>("filterBranches")),
    objectCollections(iConfig.getParameter<edm::ParameterSet>("objectCollections")),
    vertexCollections(iConfig.getParameter<edm::ParameterSet>("vertexCollections")),

    cHLTriggerNamesSelection(iConfig.getUntrackedParameter<vector<string> > ("HLTriggerSelection")),
    cMuHLTriggerMatching(iConfig.getUntrackedParameter<vector<string> > ("RecMuonHLTriggerMatching")),
    cElHLTriggerMatching(iConfig.getUntrackedParameter<vector<string> > ("RecElectronHLTriggerMatching")),
    cTauHLTriggerMatching(iConfig.getUntrackedParameter<vector<string> > ("RecTauHLTriggerMatching")),

    cTauDiscriminators(iConfig.getUntrackedParameter<vector<string> > ("RecTauDiscriminators")),

    cPhotonHLTriggerMatching(iConfig.getUntrackedParameter<vector<string> > ("RecPhotonHLTriggerMatching")),
    cJetHLTriggerMatching(iConfig.getUntrackedParameter<vector<string> > ("RecJetHLTriggerMatching")),


    HLTPrescaleProvider_(iConfig, consumesCollector(), *this),

    isData_(iConfig.getParameter<bool>("isData"))
{
    usesResource("TFileService");
    // get trigger parameters
    triggerBranchStrings.push_back("Pass");
    triggerBranchStrings.push_back("Prescale");
    myTriggerNames = triggerBranches.getParameterNames();
    for (auto trig : myTriggerNames) {
        edm::ParameterSet trigPSet = triggerBranches.getParameter<edm::ParameterSet>(trig);
        std::string trigString = trigPSet.getParameter<std::string>("path");
        triggerNamingMap_.insert(std::pair<std::string, std::string>(trig,trigString));
    }
    // get filter parameters
    myFilterNames = filterBranches.getParameterNames();
    for (auto trig : myFilterNames) {
        edm::ParameterSet trigPSet = filterBranches.getParameter<edm::ParameterSet>(trig);
        std::string trigString = trigPSet.getParameter<std::string>("path");
        triggerNamingMap_.insert(std::pair<std::string, std::string>(trig,trigString));
    }

    // set up trees
    edm::Service<TFileService> FS;
    //drhist = FS->make<TH1D> ("drhist", "drhist", 10000, 0., 100.);

    // create info tree
    infotree = FS->make<TTree> ("AC1Binfo", "AC1Binfo", 1);
    infotree->Branch("nevents", &nevents, "nevents/I");
    infotree->Branch("nevents_skipped", &nevents_skipped, "nevents_skipped/I");
    infotree->Branch("nevents_filled", &nevents_filled, "nevents_filled/I");
    infotree->Branch("sum_weights", &sum_weights, "sum_weights/F");

    // create run tree
    runtree = FS->make<TTree> ("AC1Brun", "AC1Brun", 1);
    runtree->Branch("run_number", &run_number, "run_number/i");
    runtree->Branch("run_hltcount", &run_hltcount, "run_hltcount/i");
    runtree->Branch("run_hltnames", run_hltnames, "run_hltnames/C");
    runtree->Branch("run_hltmunames", run_hltmunames, "run_hltmunames/C");
    runtree->Branch("run_hltelnames", run_hltelnames, "run_hltelnames/C");
    runtree->Branch("run_hlttaunames", run_hlttaunames, "run_hlttaunames/C");
    runtree->Branch("run_hltphotonnames", run_hltphotonnames, "run_hltphotonnames/C");
    runtree->Branch("run_hltjetnames", run_hltjetnames, "run_hltjetnames/C");
    runtree->Branch("run_hltprescaletablescount", &run_hltprescaletablescount, "run_hltprescaletablescount/i");
    runtree->Branch("run_hltprescaletables", run_hltprescaletables, "run_hltprescaletables[run_hltprescaletablescount]/i");
    runtree->Branch("run_hltl1prescaletables", run_hltl1prescaletables, "run_hltl1prescaletables[run_hltprescaletablescount]/i");
    runtree->Branch("run_l1algocount", &run_l1algocount, "run_l1algocount/i");
    runtree->Branch("run_l1algoprescaletablescount", &run_l1algoprescaletablescount, "run_l1algoprescaletablescount/i");
    runtree->Branch("run_l1algoprescaletables", run_l1algoprescaletables, "run_l1algoprescaletables[run_l1algoprescaletablescount]/i");
    runtree->Branch("run_l1techcount", &run_l1techcount, "run_l1techcount/i");
    runtree->Branch("run_l1techprescaletablescount", &run_l1techprescaletablescount, "run_l1techprescaletablescount/i");
    runtree->Branch("run_l1techprescaletables", run_l1techprescaletables, "run_l1techprescaletables[run_l1techprescaletablescount]/i");

    runtree->Branch("run_taudiscriminators", run_taudiscriminators, "run_taudiscriminators/C");

    // create lumitree
    lumitree = FS->make<TTree> ("AC1Blumi", "AC1Blumi", 1);
    lumitree->Branch("lumi_run", &lumi_run, "lumi_run/i");
    lumitree->Branch("lumi_block", &lumi_block, "lumi_block/i");
    lumitree->Branch("lumi_value", &lumi_value, "lumi_value/F");
    lumitree->Branch("lumi_valueerr", &lumi_valueerr, "lumi_valueerr/F");
    lumitree->Branch("lumi_livefrac", &lumi_livefrac, "lumi_livefrac/F");
    lumitree->Branch("lumi_deadfrac", &lumi_deadfrac, "lumi_deadfrac/F");
    lumitree->Branch("lumi_quality", &lumi_quality, "lumi_quality/i");
    lumitree->Branch("lumi_eventsprocessed", &lumi_eventsprocessed, "lumi_eventsprocessed/i");
    lumitree->Branch("lumi_eventsfiltered", &lumi_eventsfiltered, "lumi_eventsfiltered/i");
    lumitree->Branch("lumi_hltprescaletable", &lumi_hltprescaletable, "lumi_hltprescaletable/i");
    lumitree->Branch("lumi_l1algoprescaletable", &lumi_l1algoprescaletable, "lumi_l1algoprescaletable/i");
    lumitree->Branch("lumi_l1techprescaletable", &lumi_l1techprescaletable, "lumi_l1techprescaletable/i");

    // create event tree
    tree = FS->make<TTree>("AC1B", "AC1B");
    // once per event branches
    tree->Branch("isdata", &isdata, "isdata/O");
    tree->Branch("event_nr", &event_nr, "event_nr/D");
    tree->Branch("event_run", &event_run, "event_run/i");
    tree->Branch("event_timeunix", &event_timeunix, "event_timeunix/i");
    tree->Branch("event_timemicrosec", &event_timemicrosec, "event_timemicrosec/i");
    tree->Branch("event_luminosityblock", &event_luminosityblock, "event_luminosityblock/i");
    tree->Branch("event_rho", &event_rho, "event_rho/F");
// old
    tree->Branch("errors", &errors, "errors/i");
    tree->Branch("trigger_level1bits", &trigger_level1bits, "trigger_level1bits[8]/b");
    tree->Branch("trigger_level1", &trigger_level1, "trigger_level1[128]/b");
    tree->Branch("trigger_HLT", &trigger_HLT, "trigger_HLT[128]/b");




    tree->Branch("beamspot_x", &beamspot_x, "beamspot_x/F");
    tree->Branch("beamspot_y", &beamspot_y, "beamspot_y/F");
    tree->Branch("beamspot_z", &beamspot_z, "beamspot_z/F");
    tree->Branch("beamspot_xwidth", &beamspot_xwidth, "beamspot_xwidth/F");
    tree->Branch("beamspot_ywidth", &beamspot_ywidth, "beamspot_ywidth/F");
    tree->Branch("beamspot_zsigma", &beamspot_zsigma, "beamspot_zsigma/F");
    tree->Branch("beamspot_cov", &beamspot_cov, "beamspot_cov[6]/F");

    tree->Branch("genweight", &genweight, "genweight/F");
    tree->Branch("genid1", &genid1, "genid1/F");
    tree->Branch("genx1", &genx1, "genx1/F");
    tree->Branch("genid2", &genid2, "genid2/F");
    tree->Branch("genx2", &genx2, "genx2/F");
    tree->Branch("genScale", &genScale, "genScale/F");
    tree->Branch("numpileupinteractionsminus", &numpileupinteractionsminus, "numpileupinteractionsminus/I");
    tree->Branch("numpileupinteractions", &numpileupinteractions, "numpileupinteractions/I");
    tree->Branch("numpileupinteractionsplus", &numpileupinteractionsplus, "numpileupinteractionsplus/I");
    tree->Branch("numtruepileupinteractions", &numtruepileupinteractions, "numtruepileupinteractions/F");

/*

    tree->Branch("genparticles_count", &genparticles_count, "genparticles_count/i");
    tree->Branch("genparticles_e", genparticles_e, "genparticles_e[genparticles_count]/F");
    tree->Branch("genparticles_px", genparticles_px, "genparticles_px[genparticles_count]/F");
    tree->Branch("genparticles_py", genparticles_py, "genparticles_py[genparticles_count]/F");
    tree->Branch("genparticles_pz", genparticles_pz, "genparticles_pz[genparticles_count]/F");
    tree->Branch("genparticles_vx", genparticles_vx, "genparticles_vx[genparticles_count]/F");
    tree->Branch("genparticles_vy", genparticles_vy, "genparticles_vy[genparticles_count]/F");
    tree->Branch("genparticles_vz", genparticles_vz, "genparticles_vz[genparticles_count]/F");
    tree->Branch("genparticles_pdgid", genparticles_pdgid, "genparticles_pdgid[genparticles_count]/I");
    tree->Branch("genparticles_status", genparticles_status, "genparticles_status[genparticles_count]/I");
    tree->Branch("genparticles_indirectmother", genparticles_indirectmother, "genparticles_indirectmother[genparticles_count]/I");
    tree->Branch("genparticles_info", genparticles_info, "genparticles_info[genparticles_count]/i");

    tree->Branch("genallparticles_count", &genallparticles_count, "genallparticles_count/i");
    tree->Branch("genallparticles_e", genallparticles_e, "genallparticles_e[genallparticles_count]/F");
    tree->Branch("genallparticles_px", genallparticles_px, "genallparticles_px[genallparticles_count]/F");
    tree->Branch("genallparticles_py", genallparticles_py, "genallparticles_py[genallparticles_count]/F");
    tree->Branch("genallparticles_pz", genallparticles_pz, "genallparticles_pz[genallparticles_count]/F");
    tree->Branch("genallparticles_vx", genallparticles_vx, "genallparticles_vx[genallparticles_count]/F");
    tree->Branch("genallparticles_vy", genallparticles_vy, "genallparticles_vy[genallparticles_count]/F");
    tree->Branch("genallparticles_vz", genallparticles_vz, "genallparticles_vz[genallparticles_count]/F");
    tree->Branch("genallparticles_pdgid", genallparticles_pdgid, "genallparticles_pdgid[genallparticles_count]/I");
    tree->Branch("genallparticles_status", genallparticles_status, "genallparticles_status[genallparticles_count]/I");
    tree->Branch("genallparticles_motherbeg", genallparticles_motherbeg, "genallparticles_motherbeg[genallparticles_count]/i");
    tree->Branch("genallparticles_daughterbeg", genallparticles_daughterbeg, "genallparticles_daughterbeg[genallparticles_count]/i");

    tree->Branch("genallparticlesmother_count", &genallparticlesmother_count, "genallparticlesmother_count/i");
    tree->Branch("genallparticles_mothers", genallparticles_mothers, "genallparticles_mothers[genallparticlesmother_count]/i");

    tree->Branch("genallparticlesdaughter_count", &genallparticlesdaughter_count, "genallparticlesdaughter_count/i");
    tree->Branch("genallparticles_daughters", genallparticles_daughters, "genallparticles_daughters[genallparticlesdaughter_count]/i");

    tree->Branch("genmetcalo_ex", &genmetcalo_ex, "genmetcalo_ex/F");
    tree->Branch("genmetcalo_ey", &genmetcalo_ey, "genmetcalo_ey/F");
    tree->Branch("genmettrue_ex", &genmettrue_ex, "genmettrue_ex/F");
    tree->Branch("genmettrue_ey", &genmettrue_ey, "genmettrue_ey/F");

    tree->Branch("genak4jet_count", &genak4jet_count, "genak4jet_count/i");
    tree->Branch("genak4jet_e", genak4jet_e, "genak4jet_e[genak4jet_count]/F");
    tree->Branch("genak4jet_px", genak4jet_px, "genak4jet_px[genak4jet_count]/F");
    tree->Branch("genak4jet_py", genak4jet_py, "genak4jet_py[genak4jet_count]/F");
    tree->Branch("genak4jet_pz", genak4jet_pz, "genak4jet_pz[genak4jet_count]/F");
    tree->Branch("genak4jet_einvisible", genak4jet_einvisible, "genak4jet_einvisible[genak4jet_count]/F");
    tree->Branch("genak4jet_flavour", genak4jet_flavour, "genak4jet_flavour[genak4jet_count]/I");
    tree->Branch("genak4jet_info", genak4jet_info, "genak4jet_info[genak4jet_count]/i");
*/
    // add triggers
    for (auto trigName : myTriggerNames) {
        for (auto branch : triggerBranchStrings) {
            std::string branchName = trigName + branch;
            Int_t branchVal;
            triggerIntMap_.insert(std::pair<std::string, Int_t>(branchName,branchVal));
            std::string branchLeaf = branchName + "/I";
            tree->Branch(branchName.c_str(), &triggerIntMap_[branchName], branchLeaf.c_str());
        }
    }

    // add filters
    for (auto trigName : myFilterNames) {
        Int_t branchVal;
        triggerIntMap_.insert(std::pair<std::string, Int_t>(trigName,branchVal));
        std::string branchLeaf = trigName + "/I";
        tree->Branch(trigName.c_str(), &triggerIntMap_[trigName], branchLeaf.c_str());
    }

    // add vertices
    auto vertexCollectionNames = vertexCollections.getParameterNames();
    for (auto coll : vertexCollectionNames) {
        vertexCollectionBranches.emplace_back(new VertexCollectionBranches(tree, coll, vertexCollections.getParameter<edm::ParameterSet>(coll), consumesCollector()));
    }

    // add collections
    auto collectionNames = objectCollections.getParameterNames();
    for (auto coll : collectionNames) {
        objectCollectionBranches.emplace_back(new ObjectCollectionBranches(tree, coll, objectCollections.getParameter<edm::ParameterSet>(coll), consumesCollector()));
    }
}

// destructor
RootMaker::~RootMaker() { }

// _________________________________________________________________________________
void RootMaker::beginJob()
{ 
    // reset info counters
    isdata = isData_;
    nevents = 0;
    nevents_skipped = 0;
    nevents_filled = 0;
    sum_weights = 0;
}

// _________________________________________________________________________________
void RootMaker::beginRun(edm::Run const &iRun, edm::EventSetup const &iSetup) 
{
    run_number = iRun.run();
    
    /////////////////////////////////////////
    // DYNAMIC trigger decisions ////////////
    /////////////////////////////////////////
    // these are old - I haven't decided whether to keep them yet

    // L1 prescales /////////////////////////
    edm::ESHandle<L1GtPrescaleFactors> l1GtPfAlgo;
    iSetup.get<L1GtPrescaleFactorsAlgoTrigRcd>().get(l1GtPfAlgo);
    unsigned numl1algo = (l1GtPfAlgo.product()->gtPrescaleFactors())[0].size();
    unsigned numl1algotables = (l1GtPfAlgo.product()->gtPrescaleFactors()).size();
    run_l1algoprescaletablescount = numl1algo*numl1algotables;
    run_l1algocount = numl1algo;
    if(l1GtPfAlgo.isValid()) {
        for(size_t i = 0 ; i < numl1algotables ; i++) {
            for(size_t j = 0 ; j < numl1algo ; j++) {
                run_l1algoprescaletables[j+numl1algo*i] = (l1GtPfAlgo.product()->gtPrescaleFactors())[i][j];
            }
        }
    }

    edm::ESHandle<L1GtPrescaleFactors> l1GtPfTech;
    iSetup.get<L1GtPrescaleFactorsTechTrigRcd>().get(l1GtPfTech);
    unsigned numl1tech = (l1GtPfTech.product()->gtPrescaleFactors())[0].size();
    unsigned numl1techtables = (l1GtPfTech.product()->gtPrescaleFactors()).size();
    run_l1techprescaletablescount = numl1tech*numl1techtables;
    run_l1techcount = numl1tech;
    if(l1GtPfTech.isValid()) {
        for(size_t i = 0 ; i < numl1techtables ; i++) {
            for(size_t j = 0 ; j < numl1tech ; j++) {
                run_l1techprescaletables[j+numl1tech*i] = (l1GtPfTech.product()->gtPrescaleFactors())[i][j];
            }
        }
    }


    // HLT names and prescales //////////////
    bool changed = true;
    HLTConfigProvider HLTConfiguration;
    HLTConfiguration.init(iRun, iSetup, "HLT", changed);
    run_hltcount = HLTConfiguration.size();

    boost::cmatch what;
    vector<boost::regex> trigregexes;

    // these come from the option "HLTriggerSelection" in the config file. It's normally empty
    for(size_t i = 0 ; i < cHLTriggerNamesSelection.size() ; i++) {
        trigregexes.push_back(boost::regex(cHLTriggerNamesSelection[i].c_str()));
    }

    string allnames;

    for(size_t i = 0 ; i < HLTConfiguration.size() ; i++) {
        unsigned TriggerIndex = HLTConfiguration.triggerIndex(HLTConfiguration.triggerName(i));

        for(size_t j = 0 ; j < trigregexes.size() ; j++) {
            if(boost::regex_match(HLTConfiguration.triggerName(i).c_str(), what, trigregexes[j])) {
                HLTriggerIndexSelection.push_back(TriggerIndex);
            }
        }

        allnames += HLTConfiguration.triggerName(i) + string(" ");
    }

    string allmuonnames;
    string allelectronnames;
    string alltaunames;
    string allphotonnames;
    string alljetnames;
    TriggerIndexSelection(cMuHLTriggerMatching, muontriggers, allmuonnames);
    TriggerIndexSelection(cElHLTriggerMatching, electrontriggers, allelectronnames);
    TriggerIndexSelection(cTauHLTriggerMatching, tautriggers, alltaunames);
    TriggerIndexSelection(cPhotonHLTriggerMatching, photontriggers, allphotonnames);
    TriggerIndexSelection(cJetHLTriggerMatching, jettriggers, alljetnames);

    // add tau discriminators. These come from RecTauDiscriminators in addTaus.py
    string alltaudiscriminators;
    for (size_t i = 0 ; i < cTauDiscriminators.size() ; i++) {
        alltaudiscriminators += cTauDiscriminators[i] + string(" ");
    }
    strcpy(run_taudiscriminators, alltaudiscriminators.c_str());
}


// _________________________________________________________________________________
void RootMaker::TriggerIndexSelection(vector<string> configstring, vector<pair<unsigned, int> > &triggers, string &allnames)
{
    triggers.clear();
    allnames.clear();
    boost::cmatch what;
    vector<pair<boost::regex, bool> > regexes;

    for(size_t i = 0 ; i < configstring.size() ; i++) {
        vector<string> strs;
        boost::split(strs, configstring[i], boost::is_any_of(":"));
        bool dofilter = false;
        if(strs.size() == 2 && strs[1] == "FilterTrue") {
            dofilter = true;
        }
        regexes.push_back(pair<boost::regex, bool> (boost::regex(strs[0].c_str()), dofilter));
    }

    for(size_t i = 0 ; i < HLTConfiguration.size() ; i++) {
        unsigned TriggerIndex = HLTConfiguration.triggerIndex(HLTConfiguration.triggerName(i));
        const vector<string> &ModuleLabels(HLTConfiguration.moduleLabels(TriggerIndex));
        for(size_t j = 0 ; j < regexes.size() ; j++) {
            if(boost::regex_match(HLTConfiguration.triggerName(i).c_str(), what, regexes[j].first) && triggers.size() < 32) {
                for(int u = ModuleLabels.size()-1 ; u >= 0 ; u--) {
                    if(HLTConfiguration.saveTags(ModuleLabels[u])) {
                        allnames += HLTConfiguration.triggerName(i) + string(":") + ModuleLabels[u] + string(" ");
                        triggers.push_back(pair<unsigned, int> (TriggerIndex, u));

                        //if (cdebug) {
                        //    cout<<"triggers.size() = "<<triggers.size()<< ": "<<endl;
                        //    cout<<"HLTConfiguration.triggerName("<<i<<") = "<<HLTConfiguration.triggerName(i)<<endl;
                        //    cout<<"TriggerIndex = "<<TriggerIndex<<endl;
                        //    cout<<"ModuleLabels["<<u<<"] = "<<ModuleLabels[u]<<"\n"<<endl;
                        //}
                        if("hltL1sL1DoubleMu10MuOpen" == ModuleLabels[u]) {
                            allnames += HLTConfiguration.triggerName(i) + string(":") + ModuleLabels[u] + string("gt10 ");
                            triggers.push_back(pair<unsigned, int> (TriggerIndex, -1*u));
                        }

                        if(regexes[j].second == false) {
                            break;
                        }
                    }
                }
            }
        }
    }

    if(triggers.size() == 32) {
        cout << "ERROR: more than 32 triggers to match" << endl;
    }
}



// _________________________________________________________________________________
void RootMaker::endRun(edm::Run const &iRun, edm::EventSetup const &iSetup)
{
    runtree->Fill();
}

// _________________________________________________________________________________
void RootMaker::beginLuminosityBlock(edm::LuminosityBlock const &iLumiBlock, edm::EventSetup const &iSetup)
{
    lumi_run      = iLumiBlock.run();
    lumi_block    = iLumiBlock.luminosityBlock();
    lumi_value    = -1.;
    lumi_valueerr = -1.;
    lumi_livefrac = -1.;
    lumi_deadfrac = -1.;
    lumi_quality  = 0;

    edm::Handle<LumiSummary> lumiSummary;
    iLumiBlock.getByLabel(edm::InputTag("lumiProducer"), lumiSummary);

    if(lumiSummary.isValid()) {
        lumi_value    = lumiSummary->avgInsDelLumi();
        lumi_valueerr = lumiSummary->avgInsDelLumiErr();
        lumi_livefrac = lumiSummary->liveFrac();
        lumi_deadfrac = lumiSummary->deadFrac();
        lumi_quality  = lumiSummary->lumiSecQual();
    }
}

// _________________________________________________________________________________
void RootMaker::endLuminosityBlock(edm::LuminosityBlock const &iLumiBlock, edm::EventSetup const &iSetup)
{
    lumitree->Fill();
}

// _________________________________________________________________________________
void RootMaker::endJob()
{
    infotree->Fill();
    std::cerr<<"nevents_skipped = "<<nevents_skipped<<std::endl;
    std::cerr<<"nevents_filled  = "<<nevents_filled<<std::endl;
    std::cerr<<"nevents total   = "<<nevents<<std::endl;
    std::cerr<<"isData = "<<isdata<<std::endl;
}

// GetTriggerBit returns the trigger bit corresponding to the HLT name passed to it.
// It returns -1 if there is no match and throws an exception if there is more than one match.
// _________________________________________________________________________________
int RootMaker::GetTriggerBit(std::string trigName, const edm::TriggerNames &names)
{
    std::string trigPathString = triggerNamingMap_[trigName];
    std::regex regexp(trigPathString);
    int trigBit = -1;
    for (size_t i = 0; i < names.size(); i++) {
        if (std::regex_match(names.triggerName(i), regexp)) {
            if (trigBit != -1) { // if this isn't the first match
                throw cms::Exception("DuplicateTrigger");
            }
            trigBit = i;
        }
    }
    return trigBit;
}

// _________________________________________________________________________________
void RootMaker::analyze(const edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    /////////////////////////////////////////
    // Once-per-event stuff /////////////////
    /////////////////////////////////////////
    edm::Handle<double> rho;
    iEvent.getByToken(rhoToken_, rho);
    event_rho = *rho;
    lumi_eventsprocessed++;
    nevents++;
    sum_weights += genweight;

    // event information
    event_nr              = iEvent.id().event();
    event_run             = iEvent.id().run();
    event_timeunix        = iEvent.time().unixTime();
    event_timemicrosec    = iEvent.time().microsecondOffset();
    event_luminosityblock = iEvent.getLuminosityBlock().luminosityBlock();

    // old: will be removed soon
    edm::Handle<L1GlobalTriggerReadoutRecord> L1trigger;
    iEvent.getByToken(l1TriggerToken_, L1trigger);
    const TechnicalTriggerWord &L1triggerbits = L1trigger->technicalTriggerWord();
    for(int i  = 0  ; i < 8 ; i++) {
        trigger_level1bits[i] = 0;
    }
    for(size_t i = 0 ; i < min(unsigned(L1triggerbits.size()), unsigned(64)) ; i++) {
        trigger_level1bits[i/8] |= (Byte_t)L1triggerbits[i] << (i%8);
    }
    //L1TriggerAlgos
    const DecisionWord &L1triggeralgos = L1trigger->decisionWord();
    for(int i = 0  ; i < 128 ; i++) {
        trigger_level1[i] = 0;
    }
    for(size_t i = 0 ; i < min(unsigned(L1triggeralgos.size()), unsigned(1024)) ; i++) {
        trigger_level1[i/8] |= (Byte_t)L1triggeralgos[i] << (i%8);
    }
    lumi_l1techprescaletable = (L1trigger->gtFdlWord()).gtPrescaleFactorIndexTech();
    lumi_l1algoprescaletable = (L1trigger->gtFdlWord()).gtPrescaleFactorIndexAlgo();
    //lumi_hltprescaletable = HLTConfiguration.prescaleSet(iEvent, iSetup);
    lumi_hltprescaletable = HLTPrescaleProvider_.prescaleSet(iEvent, iSetup);

    // beamspot
    edm::Handle<BeamSpot> TheBeamSpot;
    iEvent.getByToken(beamSpotToken_, TheBeamSpot);

    beamspot_x = 0.;
    beamspot_y = 0.;
    beamspot_z = 0.;
    beamspot_xwidth = 0.;
    beamspot_ywidth = 0.;
    beamspot_zsigma = 0.;
    beamspot_cov[0] = 0.;
    beamspot_cov[1] = 0.;
    beamspot_cov[2] = 0.;
    beamspot_cov[3] = 0.;
    beamspot_cov[4] = 0.;
    beamspot_cov[5] = 0.;
    if(TheBeamSpot.isValid()) {
        beamspot_x = TheBeamSpot->x0();
        beamspot_y = TheBeamSpot->y0();
        beamspot_z = TheBeamSpot->z0();
        beamspot_xwidth = TheBeamSpot->BeamWidthX();
        beamspot_ywidth = TheBeamSpot->BeamWidthY();
        beamspot_zsigma = TheBeamSpot->sigmaZ();
        beamspot_cov[0] = TheBeamSpot->covariance(0,0);
        beamspot_cov[1] = TheBeamSpot->covariance(0,1);
        beamspot_cov[2] = TheBeamSpot->covariance(0,2);
        beamspot_cov[3] = TheBeamSpot->covariance(1,1);
        beamspot_cov[4] = TheBeamSpot->covariance(1,2);
        beamspot_cov[5] = TheBeamSpot->covariance(2,2);
        bs_position = TheBeamSpot->position();
    }

    /////////////////////////////////////////
    // Generator information ////////////////
    /////////////////////////////////////////
    edm::Handle<GenEventInfoProduct> HEPMC;
    iEvent.getByToken(genEventInfoToken_, HEPMC);
    genweight = 0.; if (isdata) genweight = 1.;
    genid1    = 0.;
    genx1     = 0.;
    genid2    = 0.;
    genx2     = 0.;
    genScale  = 0.;
    if (HEPMC.isValid()) {
        genweight = HEPMC->weight();
        genid1 = HEPMC->pdf()->id.first;
        genx1 = HEPMC->pdf()->x.first;
        genid2 = HEPMC->pdf()->id.second;
        genx2 = HEPMC->pdf()->x.second;
        genScale = HEPMC->qScale();
    }

    /////////////////////////////////////////
    // Pileup information ///////////////////
    /////////////////////////////////////////
    edm::Handle<std::vector<PileupSummaryInfo> > PUInfo;
    iEvent.getByToken(PUInfoToken_, PUInfo);
    if(PUInfo.isValid()) {
        for(std::vector<PileupSummaryInfo>::const_iterator PVI = PUInfo->begin(); PVI != PUInfo->end(); ++PVI) {
            int BX = PVI->getBunchCrossing();
            if (BX == -1) {
                numpileupinteractionsminus = PVI->getPU_NumInteractions();
            } else if (BX == 0) {
                numpileupinteractions = PVI->getPU_NumInteractions();
                numtruepileupinteractions = PVI->getTrueNumInteractions();
            } else if (BX == 1) {
                numpileupinteractionsplus = PVI->getPU_NumInteractions();
            }
        }
    }

    /////////////////////////////////////////
    // EXPLICIT trigger decisions ///////////
    /////////////////////////////////////////
    iEvent.getByToken(triggerBitsToken_, triggerBits);
    iEvent.getByToken(filterBitsToken_, filterBits);
    iEvent.getByToken(triggerObjectsToken_, triggerObjects);
    iEvent.getByToken(triggerPrescalesToken_, triggerPrescales);
    const edm::TriggerNames& names = iEvent.triggerNames(*triggerBits);
    // triggers
    for (auto trigName : myTriggerNames) {
        size_t trigBit = RootMaker::GetTriggerBit(trigName,names);
        std::string passString = trigName + "Pass";
        std::string prescaleString = trigName + "Prescale";
        if (trigBit==9999) {
            triggerIntMap_[passString] = -1;
            triggerIntMap_[prescaleString] = -1;
        }
        else {
            triggerIntMap_[passString] = triggerBits->accept(trigBit);
            triggerIntMap_[prescaleString] = triggerPrescales->getPrescaleForIndex(trigBit);
        }
    }
    // filters
    const edm::TriggerNames& filters = iEvent.triggerNames(*filterBits);
    for (auto trigName : myFilterNames) {
        size_t trigBit = RootMaker::GetTriggerBit(trigName,filters);
        if (trigBit==9999) {
            triggerIntMap_[trigName] = -1;
        }
        else {
            triggerIntMap_[trigName] = filterBits->accept(trigBit);
        }
    }

    /////////////////////////////////////////
    // Fill vertices and objects branches ///
    /////////////////////////////////////////
    // add vertices
    for ( auto &coll : vertexCollectionBranches ) {
        coll->fill(iEvent);
    }
    // add collections
    for ( auto &coll : objectCollectionBranches ) {
        coll->fill(iEvent);
    }


    /////////////////////////////////////////
    // Decide whether to keep event /////////
    /////////////////////////////////////////
    // decide if we store it
    // for example, require at least 1 muon
    bool keepevent = true;
    for ( auto &coll : objectCollectionBranches ) {
        std::string name = coll->getName();
        UInt_t count = coll->getCount();
        if(not (name == "muons" && count > 0) ) {
            // uncomment the lines below to only keep events with at least 1 muon
            //keepevent = false;
        }
    }
    if (keepevent) {
        nevents_filled++;
        tree->Fill();
    } else {
        nevents_skipped++;
    }
}

