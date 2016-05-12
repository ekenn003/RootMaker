// MonteCarloInfo.cc
#include "RootMaker/RootMaker/interface/MonteCarloInfo.h"

// _________________________________________________________________________________
MonteCarloInfo::MonteCarloInfo(const edm::ParameterSet &iConfig, TTree *tree, edm::ConsumesCollector cc):
    PUInfoToken_          (cc.consumes<std::vector<PileupSummaryInfo> >(iConfig.getParameter<edm::InputTag>("pileupSummaryInfo"))),
    genEventInfoToken_    (cc.consumes<GenEventInfoProduct>(iConfig.getParameter<edm::InputTag>("genEventInfo"))),
    genJetsToken_         (cc.consumes<reco::GenJetCollection>(iConfig.getParameter<edm::InputTag>("genJets"))),
    lheEventProductToken_ (cc.consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag>("lheEventProduct"))),
    packedGenToken_       (cc.consumes<edm::View<pat::PackedGenParticle> >(iConfig.getParameter<edm::InputTag>("packedGenParticles"))),
    prunedGenToken_       (cc.consumes<edm::View<reco::GenParticle> >(iConfig.getParameter<edm::InputTag>("prunedGenParticles"))),
    slimmedMETToken_      (cc.consumes<pat::METCollection>(iConfig.getParameter<edm::InputTag>("slimGenMET")))
{
    // leptons
    selfids.push_back(11); // e-
    //selfids.push_back(-11);
    selfids.push_back(12); // nu_e
    //selfids.push_back(-12);
    selfids.push_back(13); // mu-
    //selfids.push_back(-13);
    selfids.push_back(14); // nu_mu
    //selfids.push_back(-14);
    selfids.push_back(15); // tau-
    //selfids.push_back(-15);
    selfids.push_back(16); // nu_tau
    //selfids.push_back(-16);
    // quarks
    selfids.push_back(1); // d
    //selfids.push_back(-1);
    selfids.push_back(2); // u
    //selfids.push_back(-2);
    selfids.push_back(3); // s
    //selfids.push_back(-3);
    selfids.push_back(4); // c
    //selfids.push_back(-4);
    selfids.push_back(5); // b
    //selfids.push_back(-5);
    selfids.push_back(6); // t
    //selfids.push_back(-6);
    selfids.push_back(7); // b'
    //selfids.push_back(-7);
    selfids.push_back(8); // t'
    //selfids.push_back(-8);
    // gauge+higgs bosons
    selfids.push_back(23); // Z
    selfids.push_back(32); // Z'
    selfids.push_back(24); // W+
    //selfids.push_back(-24);
    selfids.push_back(25); // h
    selfids.push_back(35); // H
    selfids.push_back(36); // A
    selfids.push_back(37); // H+
    //selfids.push_back(-37);
    selfids.push_back(21);
    selfids.push_back(22);
    // pion
    selfids.push_back(111);

    // motherids (formerly testids)
    motherids.push_back(24);  // 0
    motherids.push_back(-24); // 1
    motherids.push_back(22);  // 2
    motherids.push_back(23);  // 3
    motherids.push_back(25);  // 4
    motherids.push_back(35);  // 5
    motherids.push_back(36);  // 6
    motherids.push_back(37);  // 7
    motherids.push_back(-37); // 8
    motherids.push_back(6);   // 9
    motherids.push_back(-6);  // 10
    motherids.push_back(5);   // 11
    motherids.push_back(-5);  // 12
    motherids.push_back(32);  // 13
    motherids.push_back(8);   // 14
    motherids.push_back(-8);  // 15
    motherids.push_back(15);  // 16
    motherids.push_back(-15); // 17

    // tree branches
    tree->Branch("genweight", &genweight, "genweight/F");
    tree->Branch("genid1",    &genid1,    "genid1/F");
    tree->Branch("genx1",     &genx1,     "genx1/F");
    tree->Branch("genid2",    &genid2,    "genid2/F");
    tree->Branch("genx2",     &genx2,     "genx2/F");
    tree->Branch("genScale",  &genScale,  "genScale/F");

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

    tree->Branch("genmet_ex",     &genmet_ex,     "genmet_ex/F");
    tree->Branch("genmet_ey",     &genmet_ey,     "genmet_ey/F");

    tree->Branch("genak4jet_count",      &genak4jet_count,      "genak4jet_count/i");
    tree->Branch("genak4jet_e",          &genak4jet_e,          "genak4jet_e/F");
    tree->Branch("genak4jet_px",         &genak4jet_px,         "genak4jet_px/F");
    tree->Branch("genak4jet_py",         &genak4jet_py,         "genak4jet_py/F");
    tree->Branch("genak4jet_pz",         &genak4jet_pz,         "genak4jet_pz/F");
    tree->Branch("genak4jet_einvisible", &genak4jet_einvisible, "genak4jet_einvisible/F");
    tree->Branch("genak4jet_flavour",    &genak4jet_flavour,    "genak4jet_flavour/I");
    tree->Branch("genak4jet_info",       &genak4jet_info,       "genak4jet_info/i");
}

// destructor
MonteCarloInfo::~MonteCarloInfo()
{
    selfids.erase(selfids.begin());
    motherids.erase(motherids.begin());
}

// _________________________________________________________________________________
void MonteCarloInfo::AddMonteCarloInfo(const edm::Event &iEvent, bool addGenParticles, bool addAllGenParticles, bool addGenJets)
{
    genweight = 1.;
    genid1    = 0.;
    genx1     = 0.;
    genid2    = 0.;
    genx2     = 0.;
    genScale  = 0.;
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


        edm::Handle<GenParticleCollection> GenParticles;
        iEvent.getByToken(prunedGenToken_, GenParticles);
        if(GenParticles.isValid()) {
            GenPartons.clear();
            // loop over GenParticles and (1) save the partons and/or (2) fill the tree if they qualify
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

    }


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
                genak4jet_flavour.push_back(0);
                genak4jet_info.push_back(0);
                double ptmax = 0;

                for(size_t j = 0 ; j < GenPartons.size() ; ++j) {
                    if(deltaR(GenPartons[j], *genjet) < 0.5) {
                        if(GenPartons[j].pdgId() == 5)           genak4jet_info[genak4jet_count] |= 1<<0;
                        else if(GenPartons[j].pdgId() == -5)     genak4jet_info[genak4jet_count] |= 1<<1;
                        else if(GenPartons[j].pdgId() == 4)      genak4jet_info[genak4jet_count] |= 1<<2;
                        else if(GenPartons[j].pdgId() == -4)     genak4jet_info[genak4jet_count] |= 1<<3;
                        else if(abs(GenPartons[j].pdgId()) <= 3) genak4jet_info[genak4jet_count] |= 1<<4;
                        else if(GenPartons[j].pdgId() == 21)     genak4jet_info[genak4jet_count] |= 1<<5;

                        if(GenPartons[j].pt() > ptmax) {
                            ptmax = GenPartons[j].pt();
                            genak4jet_flavour.push_back(GenPartons[j].pdgId());
                        }

                    }
                }

                genak4jet_count++;

            }
        }
    }





/*
    if(addAllGenParticles) {
        edm::Handle<GenParticleCollection> GenParticles;
        iEvent.getByToken(genSimParticlesToken_, GenParticles);

        if(GenParticles.isValid()) {
            GenPartons.clear();

            for(unsigned i = 0 ; i < GenParticles->size() ; i++) {
                if((abs((*GenParticles)[i].pdgId()) <= 5 || (*GenParticles)[i].pdgId() == 21) && (*GenParticles)[i].pt() > 10.) {
                    GenPartons.push_back((*GenParticles)[i]);
                }

                genallparticles_e[genallparticles_count] = (*GenParticles)[i].energy();
                genallparticles_px[genallparticles_count] = (*GenParticles)[i].px();
                genallparticles_py[genallparticles_count] = (*GenParticles)[i].py();
                genallparticles_pz[genallparticles_count] = (*GenParticles)[i].pz();
                genallparticles_vx[genallparticles_count] = (*GenParticles)[i].vx();
                genallparticles_vy[genallparticles_count] = (*GenParticles)[i].vy();
                genallparticles_vz[genallparticles_count] = (*GenParticles)[i].vz();
                genallparticles_pdgid[genallparticles_count] = (*GenParticles)[i].pdgId();
                genallparticles_status[genallparticles_count] = (*GenParticles)[i].status();

                genallparticles_count++;

                if(genallparticles_count == M_genallparticlesmaxcount) {
                    cerr << "Number of genallparticles > M_genallparticlesmaxcount. They are missing." << endl;
                    errors |= 1<<15;
                    break;
                }

            }

            for(unsigned i = 0 ; i < GenParticles->size() ; i++) {
                genallparticles_motherbeg[i] = genallparticlesmother_count;
                genallparticles_daughterbeg[i] = genallparticlesdaughter_count;

                for(unsigned j = 0 ; j < (*GenParticles)[i].numberOfMothers() ; j++) {
                    genallparticles_mothers[genallparticlesmother_count] = FindGenParticle((*GenParticles)[i].mother(j));
                    genallparticlesmother_count++;

                    if(genallparticlesmother_count == M_genmotherdaughtermaxcount) {
                        break;
                    }
                }

                for(unsigned j = 0 ; j < (*GenParticles)[i].numberOfDaughters() ; j++) {
                    genallparticles_daughters[genallparticlesdaughter_count] = FindGenParticle((*GenParticles)[i].daughter(j));
                    genallparticlesdaughter_count++;

                    if(genallparticlesdaughter_count == M_genmotherdaughtermaxcount) {
                        break;
                    }
                }

            }
        }
    }

*/
}

// _________________________________________________________________________________
pair<Int_t, Int_t> MonteCarloInfo::HasAnyMother(const GenParticle *particle, vector<int> ids)
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

// _________________________________________________________________________________
Int_t MonteCarloInfo::HasAnyMother(const GenParticle *particle, int id)
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
