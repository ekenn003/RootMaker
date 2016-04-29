// PhotonShowerShapeEmbedder.cc
// embeds photon_nmissinghits

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

class PhotonShowerShapeEmbedder : public edm::stream::EDProducer<>
{
  public:
    PhotonShowerShapeEmbedder(const edm::ParameterSet &iConfig);
    virtual ~PhotonShowerShapeEmbedder() {}
    void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);

  private:
    edm::EDGetTokenT<edm::View<pat::Photon> > photonToken_;
    edm::EDGetTokenT<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit>>> ebRecHitsToken_;
    edm::EDGetTokenT<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit>>> eeRecHitsToken_;
};

PhotonShowerShapeEmbedder::PhotonShowerShapeEmbedder(const edm::ParameterSet &iConfig):
    photonToken_(consumes<edm::View<pat::Photon> >(iConfig.getParameter<edm::InputTag>("src"))),
    ebRecHitsToken_(consumes<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > >(iConfig.getParameter<edm::InputTag>("barrelHits"))),
    eeRecHitsToken_(consumes<edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> > >(iConfig.getParameter<edm::InputTag>("endcapHits")))
{
    produces<pat::PhotonCollection>();
}

void PhotonShowerShapeEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    std::auto_ptr<pat::PhotonCollection> output(new pat::PhotonCollection);
    edm::Handle<edm::View<pat::Photon> > photons;
    edm::Handle<EcalRecHitCollection> barrelHits;
    edm::Handle<EcalRecHitCollection> endcapHits;
    iEvent.getByToken(ebRecHitsToken_, barrelHits);
    iEvent.getByToken(eeRecHitsToken_, endcapHits);
    iEvent.getByToken(photonToken_, photons);
    output->reserve(photons->size());

    for (size_t i = 0; i < photons->size(); ++i) {
        pat::Photon photon = photons->at(i);

        EcalClusterLazyTools lazyTools(iEvent, iSetup, ebRecHitsToken_, eeRecHitsToken_);
        std::vector<float> localcovariances = lazyTools.localCovariances(* (photon.superCluster()->seed()));

        Float_t sigmaiphiiphi = TMath::Sqrt(localcovariances[2]);
        Float_t sigmaietaiphi = TMath::Sqrt(localcovariances[1]);

        photon.addUserFloat("sigmaiphiiphi", sigmaiphiiphi);
        photon.addUserFloat("sigmaietaiphi", sigmaietaiphi);

        output->push_back(photon);
    }

    iEvent.put(output);
}

DEFINE_FWK_MODULE(PhotonShowerShapeEmbedder);
