#include "RootMaker/RootMaker/interface/RootMaker.h"

RootMaker::RootMaker(const edm::ParameterSet &iConfig) :
    genEventInfoToken_ (consumes<GenEventInfoProduct>(iConfig.getParameter<edm::InputTag>("genEventInfo"))),
    rhoToken_          (consumes<double>(iConfig.getParameter<edm::InputTag>("rho"))),
    PUInfoToken_       (consumes<vector<PileupSummaryInfo> >(iConfig.getParameter<edm::InputTag>("pileupSummaryInfo"))),
    l1TriggerToken_    (consumes<L1GlobalTriggerReadoutRecord>(iConfig.getParameter<edm::InputTag>("l1trigger"))),
    beamSpotToken_     (consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("beamSpot"))),

    vertexCollections(iConfig.getParameter<edm::ParameterSet>("vertexCollections")),
    objectCollections(iConfig.getParameter<edm::ParameterSet>("objectCollections")),
    isData_(iConfig.getParameter<bool>("isData"))
{
    usesResource("TFileService");

    // set up trees
    edm::Service<TFileService> FS;

    // create info tree
    infotree = FS->make<TTree> ("AC1Binfo", "AC1Binfo", 1);
    infotree->Branch("isdata",          &isdata,          "isdata/O");
    infotree->Branch("nevents",         &nevents,         "nevents/i");
    infotree->Branch("nevents_skipped", &nevents_skipped, "nevents_skipped/i");
    infotree->Branch("nevents_filled",  &nevents_filled,  "nevents_filled/i");
    infotree->Branch("sumweights",      &sumweights,      "sumweights/F");
    infotree->Branch("CMSSW_version",   &CMSSW_version);

    // create lumitree
    lumitree = FS->make<TTree> ("AC1Blumi", "AC1Blumi", 1);
    lumitree->Branch("lumi_run",      &lumi_run,      "lumi_run/i");
    lumitree->Branch("lumi_block",    &lumi_block,    "lumi_block/i");
    lumitree->Branch("lumi_value",    &lumi_value,    "lumi_value/F");
    lumitree->Branch("lumi_valueerr", &lumi_valueerr, "lumi_valueerr/F");
    lumitree->Branch("lumi_livefrac", &lumi_livefrac, "lumi_livefrac/F");
    lumitree->Branch("lumi_deadfrac", &lumi_deadfrac, "lumi_deadfrac/F");
    lumitree->Branch("lumi_quality",  &lumi_quality,  "lumi_quality/i");
    lumitree->Branch("lumi_eventsprocessed", &lumi_eventsprocessed, "lumi_eventsprocessed/i");
    lumitree->Branch("lumi_eventsfiltered",  &lumi_eventsfiltered,  "lumi_eventsfiltered/i");
    lumitree->Branch("lumi_sumweights",      &lumi_sumweights,      "lumi_sumweights/i");
    lumitree->Branch("lumi_nevents",         &lumi_nevents,         "lumi_nevents/i");

    // create event tree
    tree = FS->make<TTree>("AC1B", "AC1B");
    // once per event branches
    tree->Branch("isdata",                &isdata,                "isdata/O");
    tree->Branch("event_nr",              &event_nr,              "event_nr/l");
    tree->Branch("event_run",             &event_run,             "event_run/i");
    tree->Branch("event_timeunix",        &event_timeunix,        "event_timeunix/i");
    tree->Branch("event_timemicrosec",    &event_timemicrosec,    "event_timemicrosec/i");
    tree->Branch("event_luminosityblock", &event_luminosityblock, "event_luminosityblock/i");
    tree->Branch("event_rho",             &event_rho,             "event_rho/F");

    tree->Branch("beamspot_x",      &beamspot_x,      "beamspot_x/F");
    tree->Branch("beamspot_y",      &beamspot_y,      "beamspot_y/F");
    tree->Branch("beamspot_z",      &beamspot_z,      "beamspot_z/F");
    tree->Branch("beamspot_xwidth", &beamspot_xwidth, "beamspot_xwidth/F");
    tree->Branch("beamspot_ywidth", &beamspot_ywidth, "beamspot_ywidth/F");
    tree->Branch("beamspot_zsigma", &beamspot_zsigma, "beamspot_zsigma/F");
    tree->Branch("beamspot_cov",    &beamspot_cov,    "beamspot_cov[6]/F");

    tree->Branch("numpileupinteractionsminus", &numpileupinteractionsminus, "numpileupinteractionsminus/I");
    tree->Branch("numpileupinteractions",      &numpileupinteractions,      "numpileupinteractions/I");
    tree->Branch("numpileupinteractionsplus",  &numpileupinteractionsplus,  "numpileupinteractionsplus/I");
    tree->Branch("numtruepileupinteractions",  &numtruepileupinteractions,  "numtruepileupinteractions/F");

    // make trigger branches (these will be removed soon)
    triggerBranches = unique_ptr<TriggerBranches>(new TriggerBranches(tree, iConfig, consumesCollector()));

    // make vertex branches
    auto vertexCollectionNames = vertexCollections.getParameterNames();
    for (auto coll : vertexCollectionNames) {
        vertexCollectionBranches.emplace_back(new VertexCollectionBranches(tree, coll, vertexCollections.getParameter<edm::ParameterSet>(coll), consumesCollector()));
    }
    // make collection branches
    auto collectionNames = objectCollections.getParameterNames();
    for (auto coll : collectionNames) {
        objectCollectionBranches.emplace_back(new ObjectCollectionBranches(tree, coll, objectCollections.getParameter<edm::ParameterSet>(coll), consumesCollector()));
    }
    // make monte carlo branches, gen particles
    monteCarloBranches = unique_ptr<MonteCarloBranches>(new MonteCarloBranches(tree, iConfig, consumesCollector()));
}

// destructor
RootMaker::~RootMaker() {}

// _________________________________________________________________________________
void RootMaker::beginJob()
{ 
    // reset info counters
    isdata = isData_;
    nevents = 0;
    nevents_skipped = 0;
    nevents_filled = 0;
    sumweights = 0;
}

// _________________________________________________________________________________
void RootMaker::beginRun(edm::Run const &iRun, edm::EventSetup const &iSetup) 
{
}

// _________________________________________________________________________________
void RootMaker::endRun(edm::Run const &iRun, edm::EventSetup const &iSetup)
{
}

// _________________________________________________________________________________
void RootMaker::beginLuminosityBlock(edm::LuminosityBlock const &iLumiBlock, edm::EventSetup const &iSetup)
{
    // reset values 
    lumi_eventsprocessed = 0;
    lumi_eventsfiltered  = 0;
    lumi_sumweights      = 0.;
    lumi_nevents         = 0;
    lumi_value    = -1.;
    lumi_valueerr = -1.;
    lumi_livefrac = -1.;
    lumi_deadfrac = -1.;
    lumi_quality  = 0;

    // set lumi values
    lumi_run   = iLumiBlock.run();
    lumi_block = iLumiBlock.luminosityBlock();
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
    cerr<<"nevents_skipped = "<<nevents_skipped<<endl;
    cerr<<"nevents_filled  = "<<nevents_filled<<endl;
    cerr<<"nevents total   = "<<nevents<<endl;
    cerr<<"isData = "<<isdata<<endl;
}


// _________________________________________________________________________________
void RootMaker::analyze(const edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    // get CMSSW version used to produce the first event in the job
    // (should be the same in every event, so overwrite it every time)
    if (nevents == 0) {
        CMSSW_version = (iEvent.processHistory().rbegin())->releaseVersion();
    }

    /////////////////////////////////////////
    // Proliferate event/weight counters ////
    /////////////////////////////////////////
    lumi_eventsprocessed++;
    nevents++;

    edm::Handle<GenEventInfoProduct> genEventInfo;
    iEvent.getByToken(genEventInfoToken_, genEventInfo);
    if (genEventInfo.isValid()) {
        sumweights += genEventInfo->weight();
        lumi_sumweights += genEventInfo->weight();
    } else {
        sumweights += 1.;
        lumi_sumweights += 1.;
    }
    lumi_nevents++;

    /////////////////////////////////////////
    // Event information ////////////////////
    /////////////////////////////////////////
    event_nr              = iEvent.id().event();
    event_run             = iEvent.id().run();
    event_timeunix        = iEvent.time().unixTime();
    event_timemicrosec    = iEvent.time().microsecondOffset();
    event_luminosityblock = iEvent.getLuminosityBlock().luminosityBlock();
    // rho
    edm::Handle<double> rho;
    iEvent.getByToken(rhoToken_, rho);
    event_rho = *rho;

    /////////////////////////////////////////
    // Trigger branches /////////////////////
    /////////////////////////////////////////
    triggerBranches->fill(iEvent);

    /////////////////////////////////////////
    // Beamspot /////////////////////////////
    /////////////////////////////////////////
    edm::Handle<BeamSpot> TheBeamSpot;
    iEvent.getByToken(beamSpotToken_, TheBeamSpot);

    beamspot_x = 0.;      beamspot_y = 0.;      beamspot_z = 0.;
    beamspot_xwidth = 0.; beamspot_ywidth = 0.; beamspot_zsigma = 0.;
    // reset covariance matrix
    fill_n(beamspot_cov, 6, 0);
    // fill
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
    // Pileup information ///////////////////
    /////////////////////////////////////////
    edm::Handle<vector<PileupSummaryInfo> > PUInfo;
    iEvent.getByToken(PUInfoToken_, PUInfo);
    if(PUInfo.isValid()) {
        for(vector<PileupSummaryInfo>::const_iterator PVI = PUInfo->begin(); PVI != PUInfo->end(); ++PVI) {
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
    // Fill vertices and objects branches ///
    /////////////////////////////////////////
    // add vertices
    for (auto &collBranches : vertexCollectionBranches) {
        collBranches->fill(iEvent);
    }
    // add collections
    for (auto &collBranches : objectCollectionBranches) {
        collBranches->fill(iEvent);
    }

    /////////////////////////////////////////
    // Fill genparticles, etc. //////////////
    /////////////////////////////////////////
    monteCarloBranches->fill(iEvent);

    /////////////////////////////////////////
    // Decide whether to keep event /////////
    /////////////////////////////////////////
    // decide if we store it
    // for example, require at least 1 muon

    //bool keepevent = false;
    bool keepevent = true;
    for (auto &coll : objectCollectionBranches) {
        string name = coll->getName();
        UInt_t count = coll->getCount();
        if( (name == "muons" && count > 1) ) {
            keepevent = true;
        }
    }
    if (keepevent) {
        nevents_filled++;
        tree->Fill();
    } else {
        nevents_skipped++;
    }
}

