// GenJetEmbedder.cc
// embeds userCand("genJet")
// Original author: Devin Taylor, U. Wisconsin
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJet.h"

#include "DataFormats/Math/interface/deltaR.h"

using namespace std;

template<typename T>
class GenJetEmbedder : public edm::stream::EDProducer<> {
  public:
    GenJetEmbedder(const edm::ParameterSet& iConfig);
    virtual ~GenJetEmbedder(){}
    void produce(edm::Event& iEvent, const edm::EventSetup& iSetup);

  private:
    edm::EDGetTokenT<edm::View<T> > srcToken_;
    edm::EDGetTokenT<edm::View<reco::GenJet> > genJetToken_;
    auto_ptr<vector<T> > out;
    double deltaR;
    bool   srcIsTaus;
};

template<typename T>
GenJetEmbedder<T>::GenJetEmbedder(const edm::ParameterSet& iConfig):
    srcToken_(consumes<edm::View<T> >(iConfig.getParameter<edm::InputTag>("src"))),
    genJetToken_(consumes<edm::View<reco::GenJet> >(iConfig.getParameter<edm::InputTag>("genJets"))),
    deltaR(iConfig.getParameter<double>("deltaR")),
    srcIsTaus(iConfig.getParameter<bool>("srcIsTaus"))
{
    produces<vector<T> >();
}

template<typename T>
void GenJetEmbedder<T>::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
    out = auto_ptr<vector<T> >(new vector<T>);
    edm::Handle<edm::View<T> > input;
    iEvent.getByToken(srcToken_, input);
    edm::Handle<edm::View<reco::GenJet> > genJets;
    iEvent.getByToken(genJetToken_, genJets);

    for (size_t i = 0; i < input->size(); ++i) {
        T obj = input->at(i);

        edm::Ptr<reco::GenJet> genJet;
        double bestDR = 9999.; // initialize to dummy value
        for (size_t j = 0; j < genJets->size(); j++) {
            // if these gen jets are for taus, only check hadronic gen jets
            // wouldn't want to accidentally match a leptonic gen jet to a tau
            // that would be embarrassing
            if(srcIsTaus) {
                bool jetIsLeptonic = false;
                for (auto jetConstituent: genJets->at(j).getGenConstituents()) {
                    if(abs(jetConstituent->pdgId()) == 11 || abs(jetConstituent->pdgId())==13 || abs(jetConstituent->pdgId())==15) jetIsLeptonic = true;
                }
                // if this is for taus and gen jet is leptonic, skip it
                if(srcIsTaus && jetIsLeptonic) continue;
            }
            double dr = reco::deltaR(obj, genJets->at(j));
            if ((dr < deltaR) && (dr < bestDR)) {
                genJet = genJets->ptrAt(j);
                bestDR = dr;
            }
        }

        obj.addUserCand("genJet", genJet);
        out->push_back(obj);
    }
    iEvent.put(out);
}

#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
typedef GenJetEmbedder<pat::Tau> TauGenJetEmbedder;
typedef GenJetEmbedder<pat::Jet> JetGenJetEmbedder;
// nothing we can do about this unfortunate naming
DEFINE_FWK_MODULE(TauGenJetEmbedder);
DEFINE_FWK_MODULE(JetGenJetEmbedder);
