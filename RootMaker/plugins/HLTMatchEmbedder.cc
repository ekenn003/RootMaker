// HLTMatchEmbedder.cc
// embeds *_matches<HLT>
// embeds *_trigger

#include <regex>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/Math/interface/deltaR.h"

using namespace std;

template<typename T>
class HLTMatchEmbedder : public edm::stream::EDProducer<>
{
  public:
    explicit HLTMatchEmbedder(const edm::ParameterSet&);
    ~HLTMatchEmbedder() {}
    //static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  private:
    // methods
    //void beginJob() {}
    virtual void produce(edm::Event &iEvent, const edm::EventSetup &iSetup);
    //void endJob() {}

    size_t GetTriggerBit(string trigPathString, const edm::TriggerNames &names);
    int MatchToTriggerObject(T obj, string trigPathString, const edm::TriggerNames &names);

    // data
    edm::EDGetTokenT<edm::View<T> > srcToken_;
    edm::EDGetTokenT<edm::TriggerResults> triggerBitsToken_;
    edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjectsToken_;
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    double deltaR;
    vector<string> labels_;
    vector<string> paths_;
    auto_ptr<vector<T> > output;
};

// constructor
template<typename T>
HLTMatchEmbedder<T>::HLTMatchEmbedder(const edm::ParameterSet& iConfig):
    srcToken_(consumes<edm::View<T> >(iConfig.getParameter<edm::InputTag>("src"))),
    triggerBitsToken_(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("triggerResults"))),
    triggerObjectsToken_(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("triggerObjects"))),
    deltaR(iConfig.getParameter<double>("deltaR")),
    labels_(iConfig.getParameter<vector<string> >("labels")),
    paths_(iConfig.getParameter<vector<string> >("paths"))
{
    if (labels_.size() != paths_.size()) {
        throw cms::Exception("SizeMismatch")<<"Mismatch in number of labels ("<<labels_.size()<<") and number of paths ("<<paths_.size()<<")."<<endl;
    }
    produces<vector<T> >();
}

template<typename T>
void HLTMatchEmbedder<T>::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    output = auto_ptr<vector<T> >(new vector<T>);
    edm::Handle<edm::View<T> > input;
    iEvent.getByToken(srcToken_, input);
    iEvent.getByToken(triggerBitsToken_, triggerBits);
    iEvent.getByToken(triggerObjectsToken_, triggerObjects);
    const edm::TriggerNames& names = iEvent.triggerNames(*triggerBits);

    for (size_t c = 0; c < input->size(); ++c) {
        const auto obj = input->at(c);
        T newObj = obj;

        int hasMatch = 0;
        for (size_t i = 0; i < labels_.size(); i++) {
            string label = labels_.at(i);
            string trigPathString = paths_.at(i);
            int match = MatchToTriggerObject(obj, trigPathString, names);
            // add matched
            newObj.addUserInt(label, match);
            // if we haven't found a match before but we just did, turn on hasMatch
            if (hasMatch == 0 && match != 0) hasMatch = 1;
        }

        // add *_trigger
        newObj.addUserInt("trigger", hasMatch);

        output->push_back(newObj);
    }
  iEvent.put(output);
}

// GetTriggerBit returns the trigger bit corresponding to the HLT name passed to it.
// It returns -1 if there is no match and throws an exception if there is more than one match.
template<typename T>
size_t HLTMatchEmbedder<T>::GetTriggerBit(string trigPathString, const edm::TriggerNames &names)
{
    regex regexp(trigPathString);
    int trigBit = -1;
    for (unsigned int i = 0; i < names.size(); i++) {
        if (regex_match(names.triggerName(i), regexp)) {
            if (trigBit != -1) { // if this isn't the first match
                throw cms::Exception("DuplicateTrigger");
            }
            trigBit = i;
        }
    }
    return trigBit;
}

template<typename T>
int HLTMatchEmbedder<T>::MatchToTriggerObject(T obj, string trigPathString, const edm::TriggerNames &names)
{
    int matched = 0;
    int trigBit = GetTriggerBit(trigPathString, names);
    if(trigBit == -1) return (-1);
    string pathToMatch = names.triggerName(trigBit);
    for (auto trigObj : *triggerObjects) {
       if(abs(trigObj.pdgId()) != abs(obj.pdgId())) continue;
       if(reco::deltaR(trigObj, obj) > deltaR) continue;
       trigObj.unpackPathNames(names);
       vector<string> allPathNames = trigObj.pathNames(false);
       for (auto pathName : allPathNames) {
           if(pathName.compare(pathToMatch) == 0) {
               matched = 1;
               return matched;
           }
       }
    }
    return matched;
}

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
typedef HLTMatchEmbedder<pat::Electron> ElectronHLTMatchEmbedder;
typedef HLTMatchEmbedder<pat::Muon> MuonHLTMatchEmbedder;

DEFINE_FWK_MODULE(ElectronHLTMatchEmbedder);
DEFINE_FWK_MODULE(MuonHLTMatchEmbedder);
