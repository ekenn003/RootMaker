// JetIDEmbedder.cc
// embeds ak4pfchsjet_id*

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "RecoJets/JetProducers/plugins/PileupJetIdProducer.h"
#include "RecoJets/JetProducers/interface/MVAJetPuId.h"

using namespace std;

class JetIDEmbedder : public edm::stream::EDProducer<>
{
  public:
    JetIDEmbedder(const edm::ParameterSet &iConfig);
    virtual ~JetIDEmbedder(){}
    void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);

  private:
    edm::EDGetTokenT<edm::View<pat::Jet> > jetToken_;
};

JetIDEmbedder::JetIDEmbedder(const edm::ParameterSet  &iConfig):
    jetToken_(consumes<edm::View<pat::Jet> >(iConfig.getParameter<edm::InputTag>("src")))
{
    produces<pat::JetCollection>();
}

void JetIDEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    auto_ptr<pat::JetCollection> output(new pat::JetCollection);
    edm::Handle<edm::View<pat::Jet> > jets;
    iEvent.getByToken(jetToken_, jets);
    output->reserve(jets->size());

    for (unsigned int i = 0; i < jets->size(); ++i) {
        pat::Jet jet = jets->at(i);
        float AbsETA              = TMath::Abs(jet.eta());
        float NHF                 = jet.neutralHadronEnergyFraction();
        float NEMF                = jet.neutralEmEnergyFraction();
        float CHF                 = jet.chargedHadronEnergyFraction();
        float MUF                 = jet.muonEnergyFraction();
        float CEMF                = jet.chargedEmEnergyFraction();
        int   NumConst            = jet.chargedMultiplicity() + jet.neutralMultiplicity();
        int   NumNeutralParticles = jet.neutralMultiplicity();
        int   CHM                 = jet.chargedMultiplicity();

        bool loose        = false;
        bool tight        = false;
        bool tightLepVeto = false;

        // https://twiki.cern.ch/twiki/bin/view/CMS/JetID
        // https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2016
        if (AbsETA <= 2.7) {
            loose        = (NHF < 0.99) && (NEMF < 0.99) && (NumConst > 1);
            tight        = (NHF < 0.90) && (NEMF < 0.90) && (NumConst > 1);
            tightLepVeto = (NHF < 0.90) && (NEMF < 0.90) && (NumConst > 1) && (MUF < 0.8);
            if (AbsETA <= 2.4) {
                loose        = loose &&        (CHF > 0.) && (CHM > 0) && (CEMF < 0.99);
                tight        = tight &&        (CHF > 0.) && (CHM > 0) && (CEMF < 0.99);
                tightLepVeto = tightLepVeto && (CHF > 0.) && (CHM > 0) && (CEMF < 0.90);
            }
        } else if ((AbsETA > 2.7) && (AbsETA <= 3.)) {
            loose = (NHF < 0.98) && (NEMF > 0.01) && (NumNeutralParticles > 2);
            tight = (NHF < 0.98) && (NEMF > 0.01) && (NumNeutralParticles > 2);
        } else {
            loose = (NEMF < 0.90) && (NumNeutralParticles > 10);
            tight = (NEMF < 0.90) && (NumNeutralParticles > 10);
        }

        jet.addUserInt("idLoose", loose);
        jet.addUserInt("idTight", tight);
        jet.addUserInt("idTightLepVeto", tightLepVeto);
  
        // Pileup discriminant
        // https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetID
        float jpumva = jet.userFloat("pileupJetId:fullDiscriminant");

// debugging
        jet.addUserFloat("jpumva", jpumva);
        //*//
        jet.addUserFloat("energycorr", -1.);
        jet.addUserFloat("energycorrunc", -1.);
        jet.addUserFloat("mcflavour", -1.);
        //*//



        output->push_back(jet);
    }
    iEvent.put(output);
}

DEFINE_FWK_MODULE(JetIDEmbedder);
