// ElectronMissingHitsEmbedder.cc
// embeds electron_nmissinghits

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

class ElectronMissingHitsEmbedder : public edm::stream::EDProducer<>
{
  public:
    ElectronMissingHitsEmbedder(const edm::ParameterSet &iConfig);
    virtual ~ElectronMissingHitsEmbedder(){}
    void produce(edm::Event& iEvent, const edm::EventSetup &iSetup);
  private:
    edm::EDGetTokenT<edm::View<pat::Electron> > srcToken_;
};

ElectronMissingHitsEmbedder::ElectronMissingHitsEmbedder(const edm::ParameterSet &iConfig):
    srcToken_(consumes<edm::View<pat::Electron> >(iConfig.getParameter<edm::InputTag>("src")))
{
    produces<pat::ElectronCollection>();
}

void ElectronMissingHitsEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    std::auto_ptr<pat::ElectronCollection> output(new pat::ElectronCollection);
    edm::Handle<edm::View<pat::Electron> > electrons;
    iEvent.getByToken(srcToken_, electrons);
    output->reserve(electrons->size());
    for (size_t i = 0; i < electrons->size(); ++i) {
        pat::Electron electron = electrons->at(i);

        // add missing hits
        int missingHits = electron.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS);
        electron.addUserInt("missingHits", missingHits);

        // add gap info
        Int_t gapinfo = 0;
        gapinfo |= electron.isEB() << 0;
        gapinfo |= electron.isEE() << 1;
        gapinfo |= electron.isEBGap() << 2;
        gapinfo |= electron.isEBEtaGap() << 3;
        gapinfo |= electron.isEBPhiGap() << 4;
        gapinfo |= electron.isEEGap() << 5;
        gapinfo |= electron.isEERingGap() << 6;
        gapinfo |= electron.isEEDeeGap() << 7;
        gapinfo |= electron.isEBEEGap() << 8;
        electron.addUserInt("gapinfo", gapinfo);

        output->push_back(electron);
    }

    iEvent.put(output);
}

DEFINE_FWK_MODULE(ElectronMissingHitsEmbedder);
