// MonteCarloInfo.cc
#include "RootMaker/RootMaker/interface/MonteCarloInfo.h"

// _________________________________________________________________________________
MonteCarloInfo::MonteCarloInfo(TTree *tree, std::string collectionName, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc):
    PUInfoToken_(cc.consumes<std::vector<PileupSummaryInfo> >(iConfig.getParameter<edm::InputTag>("pileupSummaryInfo"))),
    genEventInfoToken_(cc.consumes<GenEventInfoProduct>(iConfig.getParameter<edm::InputTag>("genEventInfo"))),
    genJetsToken_(cc.consumes<reco::GenJetCollection>(iConfig.getParameter<edm::InputTag>("genJets"))),
    lheEventProductToken_(cc.consumes<LHEEventProduct>(iConfig.getParameter<edm::InputTag>("lheEventProduct"))),
    packedGenToken_(cc.consumes<edm::View<pat::PackedGenParticle> >(iConfig.getParameter<edm::InputTag>("packedGenParticles"))),
    prunedGenToken_(cc.consumes<edm::View<reco::GenParticle> >(iConfig.getParameter<edm::InputTag>("prunedGenParticles")))
{
}

// _________________________________________________________________________________
void MonteCarloInfo::AddMonteCarloInfo(bool addGenParticles, bool addAllGenParticles, bool addGenJets)
{
}
