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

class RochCorEmbedder : public edm::stream::EDProducer<> {
  public:
    explicit RochCorEmbedder(const edm::ParameterSet&);
    ~RochCorEmbedder() {}
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

  private:
    // methods
    void beginJob() {}
    virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup);
    void endJob() {}

    // data
    edm::EDGetTokenT<edm::View<pat::Muon> > muonsToken_;
    bool isData_;
    std::auto_ptr<std::vector<pat::Muon> > out;
    std::auto_ptr<rochcor2015> rmcor;
};

// constructor
RochCorEmbedder::RochCorEmbedder(const edm::ParameterSet& iConfig):
    muonsToken_(consumes<edm::View<pat::Muon> >(iConfig.getParameter<edm::InputTag>("src"))),
    isData_(iConfig.getParameter<bool>("isData"))
{
    rmcor = std::auto_ptr<rochcor2015>(new rochcor2015());
    produces<std::vector<pat::Muon> >();
}

void RochCorEmbedder::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
    out = std::auto_ptr<std::vector<pat::Muon> >(new std::vector<pat::Muon>);
    edm::Handle<edm::View<pat::Muon> > muons;
    iEvent.getByToken(muonsToken_, muons);


    for (size_t c = 0; c < muons->size(); ++c) {
        const auto obj = muons->at(c);
        pat::Muon newObj = obj;
        TLorentzVector p4;

        p4.SetPtEtaPhiM(obj.pt(),obj.eta(),obj.phi(),obj.mass());
        int   charge = obj.charge();
        float qter = 1.0; 
        int   runopt = 0;
        int   ntrk = 0;

        if (isData_) {
            rmcor->momcor_data(p4, charge, runopt, qter);
        } else {
            rmcor->momcor_mc(p4, charge, ntrk, qter);
        }

        newObj.addUserFloat("rochesterPt", p4.Pt());
        newObj.addUserFloat("rochesterPx", p4.Px());
        newObj.addUserFloat("rochesterPy", p4.Py());
        newObj.addUserFloat("rochesterPz", p4.Pz());
        newObj.addUserFloat("rochesterEta", p4.Eta());
        newObj.addUserFloat("rochesterPhi", p4.Phi());
        newObj.addUserFloat("rochesterEnergy", p4.Energy());
        newObj.addUserFloat("rochesterError", qter);
        out->push_back(newObj);
    }

    iEvent.put(out);
}

void RochCorEmbedder::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(RochCorEmbedder);
