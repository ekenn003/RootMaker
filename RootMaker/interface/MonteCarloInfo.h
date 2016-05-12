// MonteCarloInfo.h
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"


#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETFwd.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/JetMatching/interface/JetFlavourMatching.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "TTree.h"

using namespace std;
using namespace reco;

class MonteCarloInfo
{
  public:
    MonteCarloInfo(TTree *tree, std::string collectionName, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc);
    void AddMonteCarloInfo(bool addGenParticles, bool addAllGenParticles, bool addGenJets);

  private:
    edm::EDGetTokenT<std::vector<PileupSummaryInfo>> PUInfoToken_;
    edm::EDGetTokenT<GenEventInfoProduct> genEventInfoToken_;
    edm::EDGetTokenT<reco::GenJetCollection> genJetsToken_;
    edm::EDGetTokenT<LHEEventProduct> lheEventProductToken_;
    edm::EDGetTokenT<edm::View<pat::PackedGenParticle> > packedGenToken_;
    edm::EDGetTokenT<edm::View<reco::GenParticle> > prunedGenToken_;
};
