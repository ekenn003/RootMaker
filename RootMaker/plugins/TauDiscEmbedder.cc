// TauDiscEmbedder.cc
// embeds tau_disc
// RecTauDiscriminators is defined in addTaus.py
// run_taudiscriminators is defined in RootMaker.cc

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "FWCore/Framework/interface/MakerMacros.h"

using namespace std;

class TauDiscEmbedder : public edm::stream::EDProducer<>
{
  public:
    TauDiscEmbedder(const edm::ParameterSet &iConfig);
    virtual ~TauDiscEmbedder(){}
    void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);
  private:
    edm::EDGetTokenT<edm::View<pat::Tau> > tausToken_;
    vector<string> cTauDiscriminators;
};

TauDiscEmbedder::TauDiscEmbedder(const edm::ParameterSet &iConfig):
    tausToken_(consumes<edm::View<pat::Tau> >(iConfig.getParameter<edm::InputTag>("src"))),
    cTauDiscriminators(iConfig.getUntrackedParameter<vector<string> > ("RecTauDiscriminators"))
{
    produces<pat::TauCollection>();
}

void TauDiscEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    auto_ptr<pat::TauCollection> output(new pat::TauCollection);
    edm::Handle<edm::View<pat::Tau> > taus;
    iEvent.getByToken(tausToken_, taus);
    output->reserve(taus->size());

    for (size_t i = 0; i < taus->size(); ++i) {
        pat::Tau tau = taus->at(i);

        // determine disc
        Int_t disc = 0;
        for(size_t j = 0 ; j < cTauDiscriminators.size(); j++) {
            if( tau.tauID(cTauDiscriminators[j]) > 0.5 ) {
                disc |= 1<<j;
            }
        }

        tau.addUserInt("disc", disc);
        output->push_back(tau);
    }

    iEvent.put(output);
}

DEFINE_FWK_MODULE(TauDiscEmbedder);
