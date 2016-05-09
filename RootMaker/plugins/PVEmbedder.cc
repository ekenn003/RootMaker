// PVEmbedder.cc
// embeds *_dz
// embeds *_dxy

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

using namespace std;

template<typename T>
class PVEmbedder : public edm::stream::EDProducer<>
{
  public:
    explicit PVEmbedder(const edm::ParameterSet&);
    ~PVEmbedder() {}
    static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  private:
    // methods
    void beginJob() {}
    virtual void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);
    void endJob() {}

    double dz(T obj, const reco::Vertex&) { return 0.; }
    double dxy(T obj, const reco::Vertex&) { return 0.; }

    // data
    edm::EDGetTokenT<edm::View<T> > srcToken_;
    edm::EDGetTokenT<reco::VertexCollection> vertexToken_;
    auto_ptr<vector<T> > output;
};

// constructor
template<typename T>
PVEmbedder<T>::PVEmbedder(const edm::ParameterSet& iConfig):
    srcToken_(consumes<edm::View<T> >(iConfig.getParameter<edm::InputTag>("src"))),
    vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertexSrc")))
{
    produces<vector<T> >();
}

template<typename T>
void PVEmbedder<T>::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    output = auto_ptr<vector<T> >(new vector<T>);
    edm::Handle<edm::View<T> > input;
    iEvent.getByToken(srcToken_, input);
    edm::Handle<reco::VertexCollection> vertices;
    iEvent.getByToken(vertexToken_, vertices);
    const reco::Vertex& pv = *vertices->begin();

    for (size_t c = 0; c < input->size(); ++c) {
        const auto obj = input->at(c);
        T newObj = obj;

        newObj.addUserFloat("dz", dz(obj, pv));
        newObj.addUserFloat("dxy", dxy(obj, pv));
        output->push_back(newObj);
    }

    iEvent.put(output);
}

template<> // instructions for electron dz
double PVEmbedder<pat::Electron>::dz(pat::Electron obj, const reco::Vertex &pv)
{
    return obj.gsfTrack()->dz(pv.position());
}
template<> // instructions for electron dxy
double PVEmbedder<pat::Electron>::dxy(pat::Electron obj, const reco::Vertex &pv)
{
    return obj.gsfTrack()->dxy(pv.position());
}

template<> // instructions for muon dz
double PVEmbedder<pat::Muon>::dz(pat::Muon obj, const reco::Vertex &pv)
{
    return obj.muonBestTrack()->dz(pv.position());
}
template<> // instructions for muon dxy
double PVEmbedder<pat::Muon>::dxy(pat::Muon obj, const reco::Vertex &pv)
{
    return obj.muonBestTrack()->dxy(pv.position());
}

template<> // instructions for tau dz
double PVEmbedder<pat::Tau>::dz(pat::Tau obj, const reco::Vertex &pv)
{
    pat::PackedCandidate const* packedLeadTauCand = dynamic_cast<pat::PackedCandidate const*>(obj.leadChargedHadrCand().get());
    return packedLeadTauCand->dz();
}
template<> // instructions for tau dxy
double PVEmbedder<pat::Tau>::dxy(pat::Tau obj, const reco::Vertex &pv)
{
    pat::PackedCandidate const *packedLeadTauCand = dynamic_cast<pat::PackedCandidate const*>(obj.leadChargedHadrCand().get());
    return packedLeadTauCand->dxy();
}

template<typename T>
void PVEmbedder<T>::fillDescriptions(edm::ConfigurationDescriptions &descriptions)
{
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

//define this as a plug-in
typedef PVEmbedder<pat::Electron> ElectronPVEmbedder;
typedef PVEmbedder<pat::Muon> MuonPVEmbedder;
typedef PVEmbedder<pat::Tau> TauPVEmbedder;

DEFINE_FWK_MODULE(ElectronPVEmbedder);
DEFINE_FWK_MODULE(MuonPVEmbedder);
DEFINE_FWK_MODULE(TauPVEmbedder);
