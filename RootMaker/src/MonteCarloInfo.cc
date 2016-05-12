// MonteCarloInfo.cc
#include "RootMaker/RootMaker/interface/MonteCarloInfo.h"

// _________________________________________________________________________________
MonteCarloInfo::MonteCarloInfo(const edm::ParameterSet &iConfig, TTree *tree, edm::ConsumesCollector cc):
    PUInfoToken_          (cc.consumes<std::vector<PileupSummaryInfo> >(iConfig.getParameter<edm::InputTag>("pileupSummaryInfo"))),
    genEventInfoToken_    (cc.consumes<GenEventInfoProduct>(iConfig.getParameter<edm::InputTag>("genEventInfo"))),
    genJetsToken_         (cc.consumes<reco::GenJetCollection>(iConfig.getParameter<edm::InputTag>("genJets"))),
    lheEventProductToken_ (cc.consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag>("lheEventProduct"))),
    packedGenToken_       (cc.consumes<edm::View<pat::PackedGenParticle> >(iConfig.getParameter<edm::InputTag>("packedGenParticles"))),
    prunedGenToken_       (cc.consumes<edm::View<reco::GenParticle> >(iConfig.getParameter<edm::InputTag>("prunedGenParticles")))
{

    testids.push_back(24);   // 0
    testids.push_back(-24);  // 1
    testids.push_back(22);   // 2
    testids.push_back(23);   // 3
    testids.push_back(25);   // 4
    testids.push_back(35);   // 5
    testids.push_back(36);   // 6
    testids.push_back(37);   // 7
    testids.push_back(-37);  // 8
    testids.push_back(6);    // 9
    testids.push_back(-6);   // 10
    testids.push_back(5);    // 11
    testids.push_back(-5);   // 12
    testids.push_back(32);   // 13
    testids.push_back(8);    // 14
    testids.push_back(-8);   // 15
    testids.push_back(15);   // 16
    testids.push_back(-15);  // 17

    tree->Branch("genweight", &genweight, "genweight/F");
    tree->Branch("genid1",    &genid1,    "genid1/F");
    tree->Branch("genx1",     &genx1,     "genx1/F");
    tree->Branch("genid2",    &genid2,    "genid2/F");
    tree->Branch("genx2",     &genx2,     "genx2/F");
    tree->Branch("genScale",  &genScale,  "genScale/F");

    tree->Branch("numpileupinteractionsminus", &numpileupinteractionsminus, "numpileupinteractionsminus/I");
    tree->Branch("numpileupinteractions",      &numpileupinteractions,      "numpileupinteractions/I");
    tree->Branch("numpileupinteractionsplus",  &numpileupinteractionsplus,  "numpileupinteractionsplus/I");
    tree->Branch("numtruepileupinteractions",  &numtruepileupinteractions,  "numtruepileupinteractions/F");

    tree->Branch("genparticles_count",  &genparticles_count,  "genparticles_count/i");
    tree->Branch("genparticles_e",      &genparticles_e,      "genparticles_e/F");
    tree->Branch("genparticles_px",     &genparticles_px,     "genparticles_px/F");
    tree->Branch("genparticles_py",     &genparticles_py,     "genparticles_py/F");
    tree->Branch("genparticles_pz",     &genparticles_pz,     "genparticles_pz/F");
    tree->Branch("genparticles_vx",     &genparticles_vx,     "genparticles_vx/F");
    tree->Branch("genparticles_vy",     &genparticles_vy,     "genparticles_vy/F");
    tree->Branch("genparticles_vz",     &genparticles_vz,     "genparticles_vz/F");
    tree->Branch("genparticles_pdgid",  &genparticles_pdgid,  "genparticles_pdgid/I");
    tree->Branch("genparticles_status", &genparticles_status, "genparticles_status/I");
    tree->Branch("genparticles_indirectmother", &genparticles_indirectmother, "genparticles_indirectmother/I");
    tree->Branch("genparticles_info",           &genparticles_info,           "genparticles_info/i");

    tree->Branch("genallparticles_count",       &genallparticles_count,       "genallparticles_count/i");
    tree->Branch("genallparticles_e",           &genallparticles_e,           "genallparticles_e/F");
    tree->Branch("genallparticles_px",          &genallparticles_px,          "genallparticles_px/F");
    tree->Branch("genallparticles_py",          &genallparticles_py,          "genallparticles_py/F");
    tree->Branch("genallparticles_pz",          &genallparticles_pz,          "genallparticles_pz/F");
    tree->Branch("genallparticles_vx",          &genallparticles_vx,          "genallparticles_vx/F");
    tree->Branch("genallparticles_vy",          &genallparticles_vy,          "genallparticles_vy/F");
    tree->Branch("genallparticles_vz",          &genallparticles_vz,          "genallparticles_vz/F");
    tree->Branch("genallparticles_pdgid",       &genallparticles_pdgid,       "genallparticles_pdgid/I");
    tree->Branch("genallparticles_status",      &genallparticles_status,      "genallparticles_status/I");
    tree->Branch("genallparticles_motherbeg",   &genallparticles_motherbeg,   "genallparticles_motherbeg/i");
    tree->Branch("genallparticles_daughterbeg", &genallparticles_daughterbeg, "genallparticles_daughterbeg/i");
    tree->Branch("genallparticlesmother_count",   &genallparticlesmother_count,   "genallparticlesmother_count/i");
    tree->Branch("genallparticles_mothers",       &genallparticles_mothers,       "genallparticles_mothers/i");
    tree->Branch("genallparticlesdaughter_count", &genallparticlesdaughter_count, "genallparticlesdaughter_count/i");
    tree->Branch("genallparticles_daughters",     &genallparticles_daughters,     "genallparticles_daughters/i");

    tree->Branch("genmetcalo_ex", &genmetcalo_ex, "genmetcalo_ex/F");
    tree->Branch("genmetcalo_ey", &genmetcalo_ey, "genmetcalo_ey/F");
    tree->Branch("genmettrue_ex", &genmettrue_ex, "genmettrue_ex/F");
    tree->Branch("genmettrue_ey", &genmettrue_ey, "genmettrue_ey/F");

    tree->Branch("genak4jet_count",      &genak4jet_count,      "genak4jet_count/i");
    tree->Branch("genak4jet_e",          &genak4jet_e,          "genak4jet_e/F");
    tree->Branch("genak4jet_px",         &genak4jet_px,         "genak4jet_px/F");
    tree->Branch("genak4jet_py",         &genak4jet_py,         "genak4jet_py/F");
    tree->Branch("genak4jet_pz",         &genak4jet_pz,         "genak4jet_pz/F");
    tree->Branch("genak4jet_einvisible", &genak4jet_einvisible, "genak4jet_einvisible/F");
    tree->Branch("genak4jet_flavour",    &genak4jet_flavour,    "genak4jet_flavour/I");
    tree->Branch("genak4jet_info",       &genak4jet_info,       "genak4jet_info/i");
}

// _________________________________________________________________________________
void MonteCarloInfo::AddMonteCarloInfo(const edm::Event &iEvent, bool addGenParticles, bool addAllGenParticles, bool addGenJets)
{
    if(addGenParticles) {
        edm::Handle<GenMETCollection> GenMetCalo;
        iEvent.getByLabel(edm::InputTag("genMetCalo"), GenMetCalo);
        edm::Handle<GenMETCollection> GenMetTrue;
        iEvent.getByLabel(edm::InputTag("genMetTrue"), GenMetTrue);

        if(GenMetCalo.isValid() && GenMetCalo->size() > 0) {
            genmetcalo_ex.push_back((*GenMetCalo)[0].px());
            genmetcalo_ey.push_back((*GenMetCalo)[0].py());
        } else {
            genmetcalo_ex.push_back(0.);
            genmetcalo_ey.push_back(0.);
        }
        if(GenMetTrue.isValid() && GenMetTrue->size() > 0) {
            genmettrue_ex.push_back((*GenMetTrue)[0].px());
            genmettrue_ey.push_back((*GenMetTrue)[0].py());
        } else {
            genmettrue_ex.push_back(0.);
            genmettrue_ey.push_back(0.);
        }
    }

}
