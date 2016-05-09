// RochCorEmbedder.cc
// embeds muon_rochester*
// https://twiki.cern.ch/twiki/bin/viewauth/CMS/RochcorMuon

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

#include "RootMaker/RootMaker/plugins/rochcor2015.h"

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
    auto_ptr<rochcor2015> rmcor;
};

// constructor
RochCorEmbedder::RochCorEmbedder(const edm::ParameterSet& iConfig):
    muonToken_(consumes<edm::View<pat::Muon> >(iConfig.getParameter<edm::InputTag>("src"))),
    isData_(iConfig.getParameter<bool>("isData"))
{
    rmcor = auto_ptr<rochcor2015>(new rochcor2015());
    produces<vector<pat::Muon> >();
}

void RochCorEmbedder::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    output = auto_ptr<vector<pat::Muon> >(new vector<pat::Muon>);
    edm::Handle<edm::View<pat::Muon> > muons;
    iEvent.getByToken(muonToken_, muons);

    for (size_t c = 0; c < muons->size(); ++c) {
        const auto obj = muons->at(c);
        pat::Muon newObj = obj;
        TLorentzVector p4;

        p4.SetPtEtaPhiM(obj.pt(),obj.eta(),obj.phi(),obj.mass());
        int   charge = obj.charge();
        float qter = 1.0; 
        int   runopt = 0;
        int   ntrk = 0;

        if(isData_) rmcor->momcor_data(p4, charge, runopt, qter);
        else rmcor->momcor_mc(p4, charge, ntrk, qter);

        newObj.addUserFloat("rochesterPt", p4.Pt());
        newObj.addUserFloat("rochesterPx", p4.Px());
        newObj.addUserFloat("rochesterPy", p4.Py());
        newObj.addUserFloat("rochesterPz", p4.Pz());
        newObj.addUserFloat("rochesterEta", p4.Eta());
        newObj.addUserFloat("rochesterPhi", p4.Phi());
        newObj.addUserFloat("rochesterEnergy", p4.Energy());
        newObj.addUserFloat("rochesterError", qter);
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
