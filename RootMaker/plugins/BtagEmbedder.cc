// BtagEmbedder.cc
// embeds ak4pfchsjet_btag

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "FWCore/Framework/interface/MakerMacros.h"

class BtagEmbedder : public edm::stream::EDProducer<>
{
  public:
    BtagEmbedder(const edm::ParameterSet &iConfig);
    virtual ~BtagEmbedder(){}
    void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);
  private:
    edm::EDGetTokenT<edm::View<pat::Jet> > srcToken_;
};

BtagEmbedder::BtagEmbedder(const edm::ParameterSet &iConfig):
    srcToken_(consumes<edm::View<pat::Jet> >(iConfig.getParameter<edm::InputTag>("src")))
{
  produces<pat::JetCollection>();
}

void BtagEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    using namespace TMath;
    std::auto_ptr<pat::JetCollection> output(new pat::JetCollection);
    edm::Handle<edm::View<pat::Jet> > jets;
    iEvent.getByToken(srcToken_, jets);
    output->reserve(jets->size());

    for (unsigned int i = 0; i < jets->size(); ++i) {
        pat::Jet jet = jets->at(i);
        Int_t btag = 0;

        // https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation#Recommendation_for_13_TeV_Data
        bool passJPL     = (jet.bDiscriminator("pfJetProbabilityBJetTags") > 0.245);
        bool passJPM     = (jet.bDiscriminator("pfJetProbabilityBJetTags") > 0.515);
        bool passJPT     = (jet.bDiscriminator("pfJetProbabilityBJetTags") > 0.760);
        bool passCSVv2L  = (jet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.460);
        bool passCSVv2M  = (jet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.800);
        bool passCSVv2T  = (jet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.935);
        bool passCMVAv2L = (jet.bDiscriminator("pfCombinedMVAV2BJetTags") > -0.715);
        bool passCMVAv2M = (jet.bDiscriminator("pfCombinedMVAV2BJetTags") > 0.185);
        bool passCMVAv2T = (jet.bDiscriminator("pfCombinedMVAV2BJetTags") > 0.875);

        // turn on a different bit in btag for each discriminator.
        // you can then check whether a certain bit has been turned 
        // on by checking "btag & bit"
        // e.g. if passJPT is true, (btag & 3) will return true
        if (passJPL) btag |= 1;
        if (passJPM) btag |= 2; 
        if (passJPT) btag |= 3; 
        if (passCSVv2L) btag |= 4; 
        if (passCSVv2M) btag |= 5; 
        if (passCSVv2T) btag |= 6; 
        if (passCMVAv2L) btag |= 7; 
        if (passCMVAv2M) btag |= 8; 
        if (passCMVAv2T) btag |= 9; 

        jet.addUserInt("btag", btag);

        output->push_back(jet);
    }
    iEvent.put(output);
}

DEFINE_FWK_MODULE(BtagEmbedder);
