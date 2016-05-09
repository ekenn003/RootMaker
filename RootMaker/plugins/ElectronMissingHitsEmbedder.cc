// ElectronMissingHitsEmbedder.cc
// embeds electron_nmissinghits

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

using namespace std;

class ElectronMissingHitsEmbedder : public edm::stream::EDProducer<>
{
  public:
    ElectronMissingHitsEmbedder(const edm::ParameterSet &iConfig);
    virtual ~ElectronMissingHitsEmbedder() {}
    void produce(edm::Event& iEvent, const edm::EventSetup &iSetup);
  private:
    edm::EDGetTokenT<edm::View<pat::Electron> > electronToken_;
};

ElectronMissingHitsEmbedder::ElectronMissingHitsEmbedder(const edm::ParameterSet &iConfig):
    electronToken_(consumes<edm::View<pat::Electron> >(iConfig.getParameter<edm::InputTag>("src")))
{
    produces<pat::ElectronCollection>();
}

void ElectronMissingHitsEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    auto_ptr<pat::ElectronCollection> output(new pat::ElectronCollection);
    edm::Handle<edm::View<pat::Electron> > electrons;
    iEvent.getByToken(electronToken_, electrons);
    output->reserve(electrons->size());

    for (size_t i = 0; i < electrons->size(); ++i) {
        pat::Electron electron = electrons->at(i);

        // add missing hits
        int missingHits = electron.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS);
        electron.addUserInt("missingHits", missingHits);

        output->push_back(electron);
    }

    iEvent.put(output);
}

DEFINE_FWK_MODULE(ElectronMissingHitsEmbedder);
