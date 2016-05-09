// JetShapeEmbedder.cc
// embeds ak4pfchsjet_chargeda
// embeds ak4pfchsjet_chargedb
// embeds ak4pfchsjet_neutrala
// embeds ak4pfchsjet_neutralb
// embeds ak4pfchsjet_alla
// embeds ak4pfchsjet_allb
// embeds ak4pfchsjet_chargedfractionmv

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "FWCore/Framework/interface/MakerMacros.h"

using namespace std;

class JetShapeEmbedder : public edm::stream::EDProducer<>
{
  public:
    JetShapeEmbedder(const edm::ParameterSet &iConfig);
    virtual ~JetShapeEmbedder() {}
    void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);

  private:
    edm::EDGetTokenT<edm::View<pat::Jet> > jetToken_;
    edm::EDGetTokenT<pat::PackedCandidateCollection> packedPFCandsToken_;
};

JetShapeEmbedder::JetShapeEmbedder(const edm::ParameterSet &iConfig):
    jetToken_(consumes<edm::View<pat::Jet> >(iConfig.getParameter<edm::InputTag>("src"))),
    packedPFCandsToken_(consumes<pat::PackedCandidateCollection>(iConfig.getParameter<edm::InputTag>("packedSrc")))
{
    produces<pat::JetCollection>();
}

void JetShapeEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    using namespace TMath;
    auto_ptr<pat::JetCollection> output(new pat::JetCollection);
    edm::Handle<edm::View<pat::Jet> > jets;
    iEvent.getByToken(jetToken_, jets);

    edm::Handle<pat::PackedCandidateCollection> packed;
    iEvent.getByToken(packedPFCandsToken_, packed);
    output->reserve(jets->size());

    for (unsigned int i = 0; i < jets->size(); ++i) {
        pat::Jet jet = jets->at(i);
        float chargedetaeta1 = 0.;
        float chargedphiphi1 = 0.;
        float chargedetaeta2 = 0.;
        float chargedphiphi2 = 0.;
        float chargedetaphi  = 0.;
        float chargedptsum   = 0.;
        float chargedptsummv = 0.;
        float neutraletaeta1 = 0.;
        float neutralphiphi1 = 0.;
        float neutraletaeta2 = 0.;
        float neutralphiphi2 = 0.;
        float neutraletaphi  = 0.;
        float neutralptsum   = 0.;
        float alletaeta1     = 0.;
        float alletaeta2     = 0.;
        float alletaphi      = 0.;
        float allphiphi1     = 0.;
        float allphiphi2     = 0.;
        float allptsum       = 0.;

        vector<reco::CandidatePtr> daughters(jet.daughterPtrVector());
        for (unsigned int id = 0, nd = jet.numberOfDaughters(); id < nd; ++id) {
            const pat::PackedCandidate &con = dynamic_cast<const pat::PackedCandidate &>(*daughters[id]);
            float deta = jet.eta() - con.eta();
            float dphi = jet.phi() - con.phi();

            if(dphi > 4.*atan(1.)) {
                dphi = dphi-8.*atan(1.);
            }
            if(dphi < -1.*4.*atan(1.)) {
                dphi = dphi+8.*atan(1.);
            }
            if(con.charge() != 0) {
                chargedptsum += con.pt();
                chargedetaeta1 += deta*con.pt();
                chargedetaeta2 += deta*deta*con.pt();
                chargedetaphi += deta*dphi*con.pt();
                chargedphiphi1 += dphi*con.pt();
                chargedphiphi2 += dphi*dphi*con.pt();
                //int vertex = getPrimVertex(con);
                int frompv = con.fromPV();
                if (frompv > 1) {
                    chargedptsummv += con.pt();
                }
            } else {
                neutralptsum += con.pt();
                neutraletaeta1 += deta*con.pt();
                neutraletaeta2 += deta*deta*con.pt();
                neutraletaphi += deta*dphi*con.pt();
                neutralphiphi1 += dphi*con.pt();
                neutralphiphi2 += dphi*dphi*con.pt();
            }
            allptsum += con.pt();
            alletaeta1 += deta*con.pt();
            alletaeta2 += deta*deta*con.pt();
            alletaphi += deta*dphi*con.pt();
            allphiphi1 += dphi*con.pt();
            allphiphi2 += dphi*dphi*con.pt();
        }

        if(chargedptsum != 0) {
            chargedetaeta1/=chargedptsum;
            chargedetaeta2/=chargedptsum;
            chargedetaphi/=chargedptsum;
            chargedphiphi1/=chargedptsum;
            chargedphiphi2/=chargedptsum;
        } else {
            chargedetaeta1 = 0.;
            chargedetaeta2 = 0.;
            chargedetaphi = 0.;
            chargedphiphi1 = 0.;
            chargedphiphi2 = 0.;
        }

        if(neutralptsum != 0) {
            neutraletaeta1/=neutralptsum;
            neutraletaeta2/=neutralptsum;
            neutraletaphi/=neutralptsum;
            neutralphiphi1/=neutralptsum;
            neutralphiphi2/=neutralptsum;
        } else {
            neutraletaeta1 = 0.;
            neutraletaeta2 = 0.;
            neutraletaphi = 0.;
            neutralphiphi1 = 0.;
            neutralphiphi2 = 0.;
        }

        if(allptsum != 0) {
            alletaeta1/=allptsum;
            alletaeta2/=allptsum;
            alletaphi/=allptsum;
            allphiphi1/=allptsum;
            allphiphi2/=allptsum;
        } else {
            alletaeta1 = 0.;
            alletaeta2 = 0.;
            alletaphi = 0.;
            allphiphi1 = 0.;
            allphiphi2 = 0.;
        }

        float chargedetavar = chargedetaeta2-chargedetaeta1*chargedetaeta1;
        float chargedphivar = chargedphiphi2-chargedphiphi1*chargedphiphi1;
        float chargedphidetacov = chargedetaphi - chargedetaeta1*chargedphiphi1;
        float chargeddet = (chargedetavar-chargedphivar)* (chargedetavar-chargedphivar)+4*chargedphidetacov*chargedphidetacov;
        float chargedx1 = (chargedetavar+chargedphivar+sqrt(chargeddet))/2.;
        float chargedx2 = (chargedetavar+chargedphivar-sqrt(chargeddet))/2.;
        float neutraletavar = neutraletaeta2-neutraletaeta1*neutraletaeta1;
        float neutralphivar = neutralphiphi2-neutralphiphi1*neutralphiphi1;
        float neutralphidetacov = neutraletaphi - neutraletaeta1*neutralphiphi1;
        float neutraldet = (neutraletavar-neutralphivar)* (neutraletavar-neutralphivar)+4*neutralphidetacov*neutralphidetacov;
        float neutralx1 = (neutraletavar+neutralphivar+sqrt(neutraldet))/2.;
        float neutralx2 = (neutraletavar+neutralphivar-sqrt(neutraldet))/2.;
        float alletavar = alletaeta2-alletaeta1*alletaeta1;
        float allphivar = allphiphi2-allphiphi1*allphiphi1;
        float allphidetacov = alletaphi - alletaeta1*allphiphi1;
        float alldet = (alletavar-allphivar)* (alletavar-allphivar)+4*allphidetacov*allphidetacov;
        float allx1 = (alletavar+allphivar+sqrt(alldet))/2.;
        float allx2 = (alletavar+allphivar-sqrt(alldet))/2.;
        float chargedfractionmv = chargedptsummv/chargedptsum;

        jet.addUserFloat("chargeda", chargedx1);
        jet.addUserFloat("chargedb", chargedx2);
        jet.addUserFloat("neutrala", neutralx1);
        jet.addUserFloat("neutralb", neutralx2);
        jet.addUserFloat("alla", allx1);
        jet.addUserFloat("allb", allx2);
        jet.addUserFloat("chargedfractionmv", chargedfractionmv);

        output->push_back(jet);
    }
    iEvent.put(output);
}

DEFINE_FWK_MODULE(JetShapeEmbedder);
