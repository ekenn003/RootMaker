// EffectiveAreaEmbedder.cc
// Embeds *_effectiveArea using a file
// RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt
// Original author: Devin Taylor, U. Wisconsin

#include <memory>
#include <vector>
#include <iostream>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/View.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"

template<typename T>
class EffectiveAreaEmbedder : public edm::stream::EDProducer<>
{
  public:
    explicit EffectiveAreaEmbedder(const edm::ParameterSet&);
    ~EffectiveAreaEmbedder() {}
    static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  private:
    // methods
    void beginJob() {}
    virtual void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);
    void endJob() {}
    float getEA(const T obj) const;

    // data
    edm::EDGetTokenT<edm::View<T> > srcToken_;
    const std::string label_;
    const std::string filename_;
    std::auto_ptr<std::vector<T> > output;
    EffectiveAreas effectiveAreas_;
};

// constructor
template<typename T>
EffectiveAreaEmbedder<T>::EffectiveAreaEmbedder(const edm::ParameterSet& iConfig):
    srcToken_(consumes<edm::View<T> >(iConfig.getParameter<edm::InputTag>("src"))),
    label_(iConfig.exists("label") ? iConfig.getParameter<std::string>("label") : std::string("EffectiveArea")),
    effectiveAreas_((iConfig.getParameter<edm::FileInPath>("configFile")).fullPath())
{
    produces<std::vector<T> >();
}

template<typename T>
void EffectiveAreaEmbedder<T>::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    output = std::auto_ptr<std::vector<T> >(new std::vector<T>);
    edm::Handle<edm::View<T> > input;
    iEvent.getByToken(srcToken_, input);

    for (size_t c = 0; c < input->size(); ++c) {
        const auto obj = input->at(c);
        T newObj = obj;
        float ea = getEA(obj);
        newObj.addUserFloat(label_, ea);
        output->push_back(newObj);
    }

    iEvent.put(output);
}

template<typename T>
float EffectiveAreaEmbedder<T>::getEA(const T obj) const
{
    float abseta = fabs(obj.eta());
    return effectiveAreas_.getEffectiveArea(abseta);
}

template<typename T>
void EffectiveAreaEmbedder<T>::fillDescriptions(edm::ConfigurationDescriptions &descriptions)
{
    //The following says we do not know what parameters are allowed so do no validation
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
typedef EffectiveAreaEmbedder<pat::Electron> ElectronEffectiveAreaEmbedder;
typedef EffectiveAreaEmbedder<pat::Photon> PhotonEffectiveAreaEmbedder;

DEFINE_FWK_MODULE(ElectronEffectiveAreaEmbedder);
DEFINE_FWK_MODULE(PhotonEffectiveAreaEmbedder);
