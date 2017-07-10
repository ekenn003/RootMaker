// ShiftedObjEmbedder.cc
// Embed shifts

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/Candidate.h"

template<typename T>
class ShiftedObjEmbedder : public edm::stream::EDProducer<>
{
  public:
    explicit ShiftedObjEmbedder(const edm::ParameterSet&);
    ~ShiftedObjEmbedder() {}

    static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);
  
  private:
    void beginJob() {}
    virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup);
    void endJob() {}
  
    edm::EDGetTokenT<edm::View<T> > srcToken_;
    edm::EDGetTokenT<edm::View<reco::Candidate> > shiftedSrcToken_;
    std::string label_;
    std::auto_ptr<std::vector<T> > output;

};

// constructor
template<typename T>
ShiftedObjEmbedder<T>::ShiftedObjEmbedder(const edm::ParameterSet &iConfig):
    srcToken_(consumes<edm::View<T> >(iConfig.getParameter<edm::InputTag>("src"))),
    shiftedSrcToken_(consumes<edm::View<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("shiftedSrc"))),
    label_(iConfig.getParameter<std::string>("label"))
{
    produces<std::vector<T> >();
}

template<typename T>
void ShiftedObjEmbedder<T>::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    output = std::auto_ptr<std::vector<T> >(new std::vector<T>);

    edm::Handle<edm::View<T> > input;
    iEvent.getByToken(srcToken_, input);

    edm::Handle<edm::View<reco::Candidate> > shiftedSrc;
    iEvent.getByToken(shiftedSrcToken_, shiftedSrc);

    for (size_t c = 0; c < input->size(); ++c) {
        const auto obj = input->at(c);
        T newObj = obj;

        if (c < shiftedSrc->size()){
            reco::CandidatePtr shiftObj = shiftedSrc->ptrAt(c);
            newObj.addUserCand(label_, shiftObj);
        }

        output->push_back(newObj);
    }

    iEvent.put(output);
}

template<typename T>
void ShiftedObjEmbedder<T>::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"

typedef ShiftedObjEmbedder<pat::Muon> ShiftedMuonEmbedder;
typedef ShiftedObjEmbedder<pat::Jet> ShiftedJetEmbedder;
typedef ShiftedObjEmbedder<pat::MET> ShiftedMETEmbedder;

//define this as a plug-in
DEFINE_FWK_MODULE(ShiftedMuonEmbedder);
DEFINE_FWK_MODULE(ShiftedJetEmbedder);
DEFINE_FWK_MODULE(ShiftedMETEmbedder);
