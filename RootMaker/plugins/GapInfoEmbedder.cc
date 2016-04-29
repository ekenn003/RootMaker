// GapInfoEmbedder.cc
// embeds *_gapinfo

#include <memory>
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "FWCore/Framework/interface/MakerMacros.h"

template<typename T>
class GapInfoEmbedder : public edm::stream::EDProducer<>
{
  public:
    explicit GapInfoEmbedder(const edm::ParameterSet&);
    ~GapInfoEmbedder() {}
  private:
    void beginJob() {}
    virtual void produce(edm::Event& iEvent, const edm::EventSetup &iSetup);
    void endJob() {}

    edm::EDGetTokenT<edm::View<T> > srcToken_;
    std::auto_ptr<std::vector<T> > output;
};

template<typename T>
GapInfoEmbedder<T>::GapInfoEmbedder(const edm::ParameterSet& iConfig):
    srcToken_(consumes<edm::View<T> >(iConfig.getParameter<edm::InputTag>("src")))
{
    produces<std::vector<T> >();
}

template<typename T>
void GapInfoEmbedder<T>::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
     output = std::auto_ptr<std::vector<T> >(new std::vector<T>);
    edm::Handle<edm::View<T> > input;
    iEvent.getByToken(srcToken_, input);
    for (size_t c = 0; c < input->size(); ++c) {
       const auto obj = input->at(c);
       const auto ptr = input->ptrAt(c);
       T newObj = obj;

       // add gap info
       Int_t gapinfo = 0;
       gapinfo |= obj.isEB() << 0;
       gapinfo |= obj.isEE() << 1;
       gapinfo |= obj.isEBGap() << 2;
       gapinfo |= obj.isEBEtaGap() << 3;
       gapinfo |= obj.isEBPhiGap() << 4;
       gapinfo |= obj.isEEGap() << 5;
       gapinfo |= obj.isEERingGap() << 6;
       gapinfo |= obj.isEEDeeGap() << 7;
       gapinfo |= obj.isEBEEGap() << 8;
       newObj.addUserInt("gapinfo", gapinfo);

       output->push_back(newObj);
    }
    iEvent.put(output);
}

typedef GapInfoEmbedder<pat::Electron> ElectronGapInfoEmbedder;
typedef GapInfoEmbedder<pat::Photon> PhotonGapInfoEmbedder;

DEFINE_FWK_MODULE(ElectronGapInfoEmbedder);
DEFINE_FWK_MODULE(PhotonGapInfoEmbedder);
