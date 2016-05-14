// MonteCarloBranches.cc
#include "RootMaker/RootMaker/interface/MonteCarloBranches.h"

// _________________________________________________________________________________
MonteCarloBranches::MonteCarloBranches(TTree *tree, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc):
    PUInfoToken_          (cc.consumes<std::vector<PileupSummaryInfo> >(iConfig.getParameter<edm::InputTag>("pileupSummaryInfo"))),
    genEventInfoToken_    (cc.consumes<GenEventInfoProduct>(iConfig.getParameter<edm::InputTag>("genEventInfo"))),
    genJetsToken_         (cc.consumes<reco::GenJetCollection>(iConfig.getParameter<edm::InputTag>("genJets"))),
    lheEventProductToken_ (cc.consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag>("lheEventProduct"))),
    packedGenToken_       (cc.consumes<edm::View<pat::PackedGenParticle> >(iConfig.getParameter<edm::InputTag>("packedGenParticles"))),
    prunedGenToken_       (cc.consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("prunedGenParticles"))),
    slimmedMETToken_      (cc.consumes<pat::METCollection>(iConfig.getParameter<edm::InputTag>("slimGenMET")))
{
    // leptons
    selfids.push_back(11); // e-
    selfids.push_back(12); // nu_e
    selfids.push_back(13); // mu-
    selfids.push_back(14); // nu_mu
    selfids.push_back(15); // tau-
    selfids.push_back(16); // nu_tau
    // quarks
    selfids.push_back(1); // d
    selfids.push_back(2); // u
    selfids.push_back(3); // s
    selfids.push_back(4); // c
    selfids.push_back(5); // b
    selfids.push_back(6); // t
    selfids.push_back(7); // b'
    selfids.push_back(8); // t'
    // gauge+higgs bosons
    selfids.push_back(23); // Z
    selfids.push_back(32); // Z'
    selfids.push_back(24); // W+
    selfids.push_back(25); // h
    selfids.push_back(35); // H
    selfids.push_back(36); // A
    selfids.push_back(37); // H+
    selfids.push_back(21);
    selfids.push_back(22);
    // mesons
    selfids.push_back(111); // neutral pion

    // motherids (formerly testids)
    motherids.push_back(5);
    motherids.push_back(6);
    motherids.push_back(8);
    motherids.push_back(15);
    motherids.push_back(22);
    motherids.push_back(23);
    motherids.push_back(24);
    motherids.push_back(25);
    motherids.push_back(32);
    motherids.push_back(35);
    motherids.push_back(36);
    motherids.push_back(37);

    // tree branches
    tree->Branch("genweight", &genweight, "genweight/F");
    tree->Branch("genid1",    &genid1,    "genid1/F");
    tree->Branch("genx1",     &genx1,     "genx1/F");
    tree->Branch("genid2",    &genid2,    "genid2/F");
    tree->Branch("genx2",     &genx2,     "genx2/F");
    tree->Branch("genScale",  &genScale,  "genScale/F");

    tree->Branch("genparticles_count", &genparticles_count, "genparticles_count/i");
    tree->Branch("genparticles_e",              &genparticles_e);
    tree->Branch("genparticles_px",             &genparticles_px);
    tree->Branch("genparticles_py",             &genparticles_py);
    tree->Branch("genparticles_pz",             &genparticles_pz);
    tree->Branch("genparticles_vx",             &genparticles_vx);
    tree->Branch("genparticles_vy",             &genparticles_vy);
    tree->Branch("genparticles_vz",             &genparticles_vz);
    tree->Branch("genparticles_pdgid",          &genparticles_pdgid);
    tree->Branch("genparticles_status",         &genparticles_status);
    tree->Branch("genparticles_indirectmother", &genparticles_indirectmother);
    tree->Branch("genparticles_info",           &genparticles_info);

    tree->Branch("genallparticles_count",         &genallparticles_count,         "genallparticles_count/i");
    tree->Branch("genallparticlesmother_count",   &genallparticlesmother_count,   "genallparticlesmother_count/i");
    tree->Branch("genallparticlesdaughter_count", &genallparticlesdaughter_count, "genallparticlesdaughter_count/i");
    tree->Branch("genallparticles_e",           &genallparticles_e);
    tree->Branch("genallparticles_px",          &genallparticles_px);
    tree->Branch("genallparticles_py",          &genallparticles_py);
    tree->Branch("genallparticles_pz",          &genallparticles_pz);
    tree->Branch("genallparticles_vx",          &genallparticles_vx);
    tree->Branch("genallparticles_vy",          &genallparticles_vy);
    tree->Branch("genallparticles_vz",          &genallparticles_vz);
    tree->Branch("genallparticles_pdgid",       &genallparticles_pdgid);
    tree->Branch("genallparticles_status",      &genallparticles_status);
    tree->Branch("genallparticles_motherbeg",   &genallparticles_motherbeg);
    tree->Branch("genallparticles_daughterbeg", &genallparticles_daughterbeg);
    tree->Branch("genallparticles_mothers",     &genallparticles_mothers);
    tree->Branch("genallparticles_daughters",   &genallparticles_daughters);

    tree->Branch("genmet_ex", &genmet_ex);
    tree->Branch("genmet_ey", &genmet_ey);

    tree->Branch("genak4jet_count", &genak4jet_count, "genak4jet_count/i");
    tree->Branch("genak4jet_e",          &genak4jet_e);
    tree->Branch("genak4jet_px",         &genak4jet_px);
    tree->Branch("genak4jet_py",         &genak4jet_py);
    tree->Branch("genak4jet_pz",         &genak4jet_pz);
    tree->Branch("genak4jet_einvisible", &genak4jet_einvisible);
    tree->Branch("genak4jet_flavour",    &genak4jet_flavour);
    tree->Branch("genak4jet_info",       &genak4jet_info);

}

// destructor
MonteCarloBranches::~MonteCarloBranches()
{
    selfids.erase(selfids.begin());
    motherids.erase(motherids.begin());
}

// _________________________________________________________________________________
void MonteCarloBranches::fill(const edm::Event &iEvent, bool addGenParticles, bool addAllGenParticles, bool addGenJets)
{
    // reset everything from the last event
    genweight = 1.;
    genid1    = 0.;
    genx1     = 0.;
    genid2    = 0.;
    genx2     = 0.;
    genScale  = 0.;

    genmet_ex.clear();
    genmet_ey.clear();

    genak4jet_count = 0;
    genak4jet_e.clear();
    genak4jet_px.clear();
    genak4jet_py.clear();
    genak4jet_pz.clear();
    genak4jet_einvisible.clear();
    genak4jet_flavour.clear();
    genak4jet_info.clear();

    genparticles_count = 0;
    genparticles_e.clear();
    genparticles_px.clear();
    genparticles_py.clear();
    genparticles_pz.clear();
    genparticles_vx.clear();
    genparticles_vy.clear();
    genparticles_vz.clear();
    genparticles_pdgid.clear();
    genparticles_status.clear();
    genparticles_indirectmother.clear();
    genparticles_info.clear();

    genallparticles_count = 0;
    genallparticlesmother_count = 0;
    genallparticlesdaughter_count = 0;
    genallparticles_e.clear();
    genallparticles_px.clear();
    genallparticles_py.clear();
    genallparticles_pz.clear();
    genallparticles_vx.clear();
    genallparticles_vy.clear();
    genallparticles_vz.clear();
    genallparticles_pdgid.clear();
    genallparticles_status.clear();
    genallparticles_motherbeg.clear();
    genallparticles_daughterbeg.clear();
    genallparticles_mothers.clear();
    genallparticles_daughters.clear();


    /////////////////////////////////////////
    // Add generator information ////////////
    /////////////////////////////////////////
    edm::Handle<GenEventInfoProduct> HEPMC;
    iEvent.getByToken(genEventInfoToken_, HEPMC);
    if(HEPMC.isValid()) {
        genweight = HEPMC->weight();
        genid1    = HEPMC->pdf()->id.first;
        genx1     = HEPMC->pdf()->x.first;
        genid2    = HEPMC->pdf()->id.second;
        genx2     = HEPMC->pdf()->x.second;
        genScale  = HEPMC->qScale();
    }

    /////////////////////////////////////////
    // Add GenMET ///////////////////////////
    /////////////////////////////////////////
    if(addGenParticles || addAllGenParticles) {
        edm::Handle<pat::METCollection> met;
        iEvent.getByToken(slimmedMETToken_, met);
        if(met.isValid() && met->size() > 0) {
            genmet_ex.push_back(met->at(0).genMET()->px());
            genmet_ey.push_back(met->at(0).genMET()->py());
        } else {
            genmet_ex.push_back(0.);
            genmet_ey.push_back(0.);
        }
    }


    /////////////////////////////////////////
    // Add GenJets //////////////////////////
    /////////////////////////////////////////
    if(addGenJets) {
        edm::Handle<reco::GenJetCollection> GenAK4Jets;
        iEvent.getByToken(genJetsToken_, GenAK4Jets);
        if(GenAK4Jets.isValid()) {
            for(GenJetCollection::const_iterator genjet = GenAK4Jets->begin(); genjet != GenAK4Jets->end() ; ++genjet) {
                if( not(genjet->pt() > 15.) ) continue;

                genak4jet_e.push_back(genjet->energy());
                genak4jet_px.push_back(genjet->px());
                genak4jet_py.push_back(genjet->py());
                genak4jet_pz.push_back(genjet->pz());
                genak4jet_einvisible.push_back(genjet->invisibleEnergy());

                // loop over the partons to see which flavour the jet is
                Int_t  flavour = 0;
                UInt_t info = 0;
                double ptmax = 0;
                for(size_t j = 0 ; j < GenPartons.size() ; ++j) {
                    if(deltaR(GenPartons[j], *genjet) < 0.5) {
                        if(GenPartons[j].pdgId() == 5)           info |= 1<<0;
                        else if(GenPartons[j].pdgId() == -5)     info |= 1<<1;
                        else if(GenPartons[j].pdgId() == 4)      info |= 1<<2;
                        else if(GenPartons[j].pdgId() == -4)     info |= 1<<3;
                        else if(abs(GenPartons[j].pdgId()) <= 3) info |= 1<<4;
                        else if(GenPartons[j].pdgId() == 21)     info |= 1<<5;

                        if(GenPartons[j].pt() > ptmax) {
                            ptmax = GenPartons[j].pt();
                            flavour = GenPartons[j].pdgId();
                        }

                    }
                }
                genak4jet_flavour.push_back(flavour);
                genak4jet_info.push_back(info);

                genak4jet_count++;

            }
        }
    }

    edm::Handle<GenParticleCollection> GenParticles;
    iEvent.getByToken(prunedGenToken_, GenParticles);
    if( not(GenParticles.isValid()) ) return;

    /////////////////////////////////////////
    // Add GenParticles /////////////////////
    /////////////////////////////////////////
    if(addGenParticles) {
        // loop over GenParticles and (1) save the partons and/or (2) fill the tree if they qualify
        GenPartons.clear();
        for(size_t i = 0 ; i < GenParticles->size() ; i++) {
            int   id     = (*GenParticles)[i].pdgId();
            int   status = (*GenParticles)[i].status();
            float pt     = (*GenParticles)[i].pt();

            // if the gen particle is a quark or gluon, store it in GenPartons
            if( (abs(id) <= 5 || id  == 21) && (*GenParticles)[i].pt() > 10.) GenPartons.push_back( (*GenParticles)[i] );

            // decide whether to keep this GenParticle:
            bool keep = false;
            // keep if it's on the selfids list
            for(int n : selfids) {
                if(id == n) keep = true;
            }
            // keep if it's a photon WITHOUT a neutral pion as an ancestor
            if(id == 22 && status == 1 && pt > 10. && HasAnyMother(& (*GenParticles)[i], 111) == 0) keep = true;
            // keep if it's a neutral pion WITHOUT a neutral pion as an ancestor
            else if(id == 111 && pt > 10. && HasAnyMother(& (*GenParticles)[i], 111) == 0) keep = true;

            if(keep) {
                genparticles_e.push_back((*GenParticles)[i].energy());
                genparticles_px.push_back((*GenParticles)[i].px());
                genparticles_py.push_back((*GenParticles)[i].py());
                genparticles_pz.push_back((*GenParticles)[i].pz());
                genparticles_vx.push_back((*GenParticles)[i].vx());
                genparticles_vy.push_back((*GenParticles)[i].vy());
                genparticles_vz.push_back((*GenParticles)[i].vz());
                genparticles_pdgid.push_back(id);
                genparticles_status.push_back(status);

                pair<Int_t, Int_t> motherinfo = HasAnyMother(& (*GenParticles)[i], motherids);
                genparticles_info.push_back(motherinfo.first);
                genparticles_indirectmother.push_back(motherinfo.second);

                genparticles_count++;
            }
        } // end loop over gen particles

    }

    /////////////////////////////////////////
    // Add AllGenParticles //////////////////
    /////////////////////////////////////////
    if(addAllGenParticles) {
        // loop over GenParticles and (1) save the partons and/or (2) fill the tree
        GenPartons.clear();
        for(size_t i = 0 ; i < GenParticles->size() ; i++) {
            // save the partons
            if((abs((*GenParticles)[i].pdgId()) <= 5 || (*GenParticles)[i].pdgId() == 21) && (*GenParticles)[i].pt() > 10.) {
                GenPartons.push_back((*GenParticles)[i]);
            }
            genallparticles_e.push_back((*GenParticles)[i].energy());
            genallparticles_px.push_back((*GenParticles)[i].px());
            genallparticles_py.push_back((*GenParticles)[i].py());
            genallparticles_pz.push_back((*GenParticles)[i].pz());
            genallparticles_vx.push_back((*GenParticles)[i].vx());
            genallparticles_vy.push_back((*GenParticles)[i].vy());
            genallparticles_vz.push_back((*GenParticles)[i].vz());
            genallparticles_pdgid.push_back((*GenParticles)[i].pdgId());
            genallparticles_status.push_back((*GenParticles)[i].status());
            genallparticles_count++;
        }

        for(size_t i = 0 ; i < GenParticles->size() ; i++) {
            genallparticles_motherbeg.push_back(genallparticlesmother_count);
            genallparticles_daughterbeg.push_back(genallparticlesdaughter_count);

            for(size_t j = 0 ; j < (*GenParticles)[i].numberOfMothers() ; j++) {
                genallparticles_mothers.push_back(FindGenParticle((*GenParticles)[i].mother(j)));
                genallparticlesmother_count++;
            }
            for(size_t j = 0 ; j < (*GenParticles)[i].numberOfDaughters() ; j++) {
                genallparticles_daughters.push_back(FindGenParticle((*GenParticles)[i].daughter(j)));
                genallparticlesdaughter_count++;
            }
        }
    }






}

// _________________________________________________________________________________
UInt_t MonteCarloBranches::FindGenParticle(const Candidate *particle) {
    for(size_t i = 0 ; i < genallparticles_count ; i++) {
        if(particle->pdgId() == genallparticles_pdgid[i] &&
                particle->status() == genallparticles_status[i] &&
                float(particle->energy()) == genallparticles_e[i] &&
                float(particle->px()) == genallparticles_px[i] &&
                float(particle->py()) == genallparticles_py[i] &&
                float(particle->pz()) == genallparticles_pz[i]) {
            return (i);
        }
    }
    return (genallparticles_count);
}

// _________________________________________________________________________________
Int_t MonteCarloBranches::HasAnyMother(const GenParticle *particle, int id)
{
    vector<unsigned> bknummother;
    vector<const GenParticle *> bkparticle;
    bknummother.reserve(10);
    bkparticle.reserve(10);
    int level = 0;
    bkparticle.push_back(particle);
    bknummother.push_back(0);

    unsigned j = 0;

    while(true) {
        if(j == bkparticle[level]->numberOfMothers()) {
            level--;

            if(level == -1) { return (0); }

            j = bknummother[level];
            bkparticle.resize(level+1);
            bknummother.resize(level+1);
            continue;
        }

        if(bkparticle[level]->mother(j)->pdgId() == id) { return (2); }

        if(abs(bkparticle[level]->mother(j)->pdgId()) == abs(id)) { return (1); }

        if(bkparticle[level]->mother(j)->numberOfMothers() > 0) {
            bknummother[level] = j+1;
            bkparticle.push_back(dynamic_cast<const GenParticle *>(bkparticle[level]->mother(j)));
            bknummother.push_back(0);
            j = 0;
            level++;
            continue;
        }

        j++;
    }

    return (0);
}

// _________________________________________________________________________________
pair<Int_t, Int_t> MonteCarloBranches::HasAnyMother(const GenParticle *particle, vector<int> ids)
{
    Int_t motherid = 0;
    vector<unsigned> bknummother;
    vector<const GenParticle *> bkparticle;
    bknummother.reserve(10);
    bkparticle.reserve(10);
    int level = 0;
    bkparticle.push_back(particle);
    bknummother.push_back(0);

    //vector<int>::const_iterator it;
    vector<int>::const_iterator it;
    UInt_t result = 0;
    unsigned j = 0;

    while(true) {
        if(j == bkparticle[level]->numberOfMothers()) {
            level--;

            if(level == -1) { break; }

            j = bknummother[level];
            bkparticle.resize(level+1);
            bknummother.resize(level+1);
            continue;
        }

        if(motherid == 0 && bkparticle[level]->mother(j)->pdgId() != particle->pdgId()) {
            motherid = bkparticle[level]->mother(j)->pdgId();
        }

        it = find(ids.begin(), ids.end(), bkparticle[level]->mother(j)->pdgId());

        if(it != ids.end()) { result |= 1<< (it-ids.begin()); }

        if(bkparticle[level]->mother(j)->numberOfMothers() > 0) {
            bknummother[level] = j+1;
            bkparticle.push_back(dynamic_cast<const GenParticle *>(bkparticle[level]->mother(j)));
            bknummother.push_back(0);
            j = 0;
            level++;
            continue;
        }

        j++;
    }

    return (pair<Int_t, Int_t> (result, motherid));
}
