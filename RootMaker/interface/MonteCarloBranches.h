#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETFwd.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METFwd.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETFwd.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "SimDataFormats/JetMatching/interface/JetFlavourMatching.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "TTree.h"

using namespace std;
using namespace reco;

class MonteCarloBranches
{
  public:
    MonteCarloBranches(TTree *tree, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc);
    ~MonteCarloBranches();
    //void fill(const edm::Event &iEvent, bool addGenParticles, bool addAllGenParticles, bool addGenJets);
    void fill(const edm::Event &iEvent);

  private:
    // data
    edm::EDGetTokenT<std::vector<PileupSummaryInfo>> PUInfoToken_;
    edm::EDGetTokenT<GenEventInfoProduct> genEventInfoToken_;
    edm::EDGetTokenT<reco::GenJetCollection> genJetsToken_;
    edm::EDGetTokenT<LHEEventProduct> lheEventProductToken_;
    edm::EDGetTokenT<edm::View<pat::PackedGenParticle> > packedGenToken_;
    edm::EDGetTokenT<reco::GenParticleCollection> prunedGenToken_;
    edm::EDGetTokenT<pat::METCollection> slimmedMETToken_;

    bool addGenParticles;
    bool addAllGenParticles;
    bool addGenJets;

    vector<int> motherids;
    vector<int> selfids;
    vector<GenParticle> GenPartons;

    Float_t genweight;
    Float_t genid1;
    Float_t genx1;
    Float_t genid2;
    Float_t genx2;
    Float_t genScale;

    // these are vectors of size one in order to be 
    // consistent with the reconstructed MET
    vector<Float_t> genmet_ex;
    vector<Float_t> genmet_ey;

    UInt_t genak4jet_count;
    vector<Float_t> genak4jet_e;
    vector<Float_t> genak4jet_px;
    vector<Float_t> genak4jet_py;
    vector<Float_t> genak4jet_pz;
    vector<Float_t> genak4jet_einvisible;
    vector<Int_t>   genak4jet_flavour;
    vector<UInt_t>  genak4jet_info;

    UInt_t genparticles_count;
    vector<Float_t> genparticles_e;
    vector<Float_t> genparticles_px;
    vector<Float_t> genparticles_py;
    vector<Float_t> genparticles_pz;
    vector<Float_t> genparticles_vx;
    vector<Float_t> genparticles_vy;
    vector<Float_t> genparticles_vz;
    vector<Int_t>   genparticles_pdgid;
    vector<Int_t>   genparticles_status;
    vector<Int_t>   genparticles_indirectmother;
    vector<UInt_t>  genparticles_info;

    UInt_t genallparticles_count;
    UInt_t genallparticlesmother_count;
    UInt_t genallparticlesdaughter_count;
    vector<Float_t> genallparticles_e;
    vector<Float_t> genallparticles_px;
    vector<Float_t> genallparticles_py;
    vector<Float_t> genallparticles_pz;
    vector<Float_t> genallparticles_vx;
    vector<Float_t> genallparticles_vy;
    vector<Float_t> genallparticles_vz;
    vector<Int_t>   genallparticles_pdgid;
    vector<Int_t>   genallparticles_status;
    vector<UInt_t>  genallparticles_motherbeg;
    vector<UInt_t>  genallparticles_daughterbeg;
    vector<UInt_t>  genallparticles_mothers;
    vector<UInt_t>  genallparticles_daughters;

    // methods
    UInt_t FindGenParticle(const Candidate *particle);
    pair<Int_t, Int_t> HasAnyMother(const GenParticle *particle, vector<int> ids);
    Int_t HasAnyMother(const GenParticle *particle, int id);

};
