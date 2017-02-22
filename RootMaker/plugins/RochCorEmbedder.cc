// RochCorEmbedder.cc
// embeds muon_rochester*
// https://twiki.cern.ch/twiki/bin/viewauth/CMS/RochcorMuon

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "TLorentzVector.h"

#include "RootMaker/RootMaker/plugins/RoccoR.h"

using namespace std;

class RochCorEmbedder : public edm::stream::EDProducer<> {
  public:
    explicit RochCorEmbedder(const edm::ParameterSet&);
    ~RochCorEmbedder() {}
    static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  private:
    // methods
    void beginJob() {}
    virtual void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);
    void endJob() {}

    // data
    edm::EDGetTokenT<edm::View<pat::Muon> > muonToken_;
    bool isData_;
    auto_ptr<vector<pat::Muon> > output;
    RoccoR* rc;
};

// constructor
RochCorEmbedder::RochCorEmbedder(const edm::ParameterSet& iConfig):
    muonToken_(consumes<edm::View<pat::Muon> >(iConfig.getParameter<edm::InputTag>("src"))),
    isData_(iConfig.getParameter<bool>("isData"))
{
    produces<vector<pat::Muon> >();
    rc = new RoccoR("rcdata.2016.v3");
}

void RochCorEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    output = auto_ptr<vector<pat::Muon> >(new vector<pat::Muon>);
    edm::Handle<edm::View<pat::Muon> > muons;
    iEvent.getByToken(muonToken_, muons);

    for (size_t c = 0; c < muons->size(); ++c) {
        const auto obj = muons->at(c);
        pat::Muon newObj = obj;
        //TLorentzVector p4;

        //p4.SetPtEtaPhiM(obj.pt(),obj.eta(),obj.phi(),obj.mass());
        //int   charge = obj.charge();
        //float qter = 1.0; 
        //int   runopt = 0;
        int   ntrk = obj.innerTrack()->hitPattern().trackerLayersWithMeasurement();
        float q_term = 1.;

        srand( time(NULL) );
        int iRand_1 = rand();
        int iRand_2 = (iRand_1 % 1000)*(iRand_1 % 1000);
        float fRand_1 = (iRand_1 % 1000) * 0.001;
        float fRand_2 = (iRand_2 % 1000) * 0.001;

        if(isData_) q_term = rc->kScaleDT(obj.charge(), obj.pt(), obj.eta(), obj.phi(), 0, 0 );
        else q_term = rc->kScaleAndSmearMC(obj.charge(), obj.pt(), obj.eta(), obj.phi(), ntrk, fRand_1, fRand_2, 0, 0);

        newObj.addUserFloat("rochesterPt", q_term*obj.pt());
        //newObj.addUserFloat("rochesterPt_up", q_term*obj.Pt());
        //newObj.addUserFloat("rochesterPt_down", p4.Pt());
        output->push_back(newObj);
    }

    iEvent.put(output);
}

void RochCorEmbedder::fillDescriptions(edm::ConfigurationDescriptions &descriptions)
{
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(RochCorEmbedder);
