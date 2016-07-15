// TriggerBranches.cc
#include "RootMaker/RootMaker/interface/TriggerBranches.h"

// _________________________________________________________________________________
TriggerBranches::TriggerBranches(TTree *tree, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc):
    triggerBitsToken_      (cc.consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("triggerResults"))),
    filterBitsToken_       (cc.consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("filterResults"))),
    triggerObjectsToken_   (cc.consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("triggerObjects"))),
    triggerPrescalesToken_ (cc.consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("triggerPrescales"))),
    triggerBranches (iConfig.getParameter<edm::ParameterSet>("triggerBranches")),
    filterBranches  (iConfig.getParameter<edm::ParameterSet>("filterBranches"))
{
    // get trigger parameters
    triggerBranchStrings.push_back("passes_");
    triggerBranchStrings.push_back("prescale_");
    myTriggerNames = triggerBranches.getParameterNames();
    for (auto trig : myTriggerNames) {
        edm::ParameterSet trigPSet = triggerBranches.getParameter<edm::ParameterSet>(trig);
        string trigString = trigPSet.getParameter<string>("path");
        triggerNamingMap_.insert(pair<string, string>(trig,trigString));
    }
    // get filter parameters
    myFilterNames = filterBranches.getParameterNames();
    for (auto trig : myFilterNames) {
        edm::ParameterSet trigPSet = filterBranches.getParameter<edm::ParameterSet>(trig);
        string trigString = trigPSet.getParameter<string>("path");
        triggerNamingMap_.insert(pair<string, string>(trig,trigString));
    }

    /////////////////////////////////////////
    // EXPLICIT trigger decisions ///////////
    /////////////////////////////////////////
    // add triggers
    for (auto trigName : myTriggerNames) {
        for (auto branch : triggerBranchStrings) {
            string branchName = branch + trigName;
            Int_t branchVal;
            triggerIntMap_.insert(pair<string, Int_t>(branchName, branchVal));
            string branchLeaf = branchName + "/I";
            tree->Branch(branchName.c_str(), &triggerIntMap_[branchName], branchLeaf.c_str());
        }
    }
    // add filters
    for (auto trigName : myFilterNames) {
        Int_t branchVal;
        triggerIntMap_.insert(pair<string, Int_t>(trigName, branchVal));
        string branchLeaf = trigName + "/I";
        tree->Branch(trigName.c_str(), &triggerIntMap_[trigName], branchLeaf.c_str());
    }

}

// _________________________________________________________________________________
void TriggerBranches::fill(const edm::Event &iEvent)
{
    iEvent.getByToken(triggerBitsToken_, triggerBits);
    iEvent.getByToken(filterBitsToken_, filterBits);
    iEvent.getByToken(triggerObjectsToken_, triggerObjects);
    iEvent.getByToken(triggerPrescalesToken_, triggerPrescales);
    const edm::TriggerNames& names = iEvent.triggerNames(*triggerBits);

    // triggers
    for (auto trigName : myTriggerNames) {
        int trigBit = GetTriggerBit(trigName, names);
        string passString = "passes_" + trigName;
        string prescaleString = "prescale_" + trigName;
        if (trigBit == -1) {
            triggerIntMap_[passString] = -1;
            triggerIntMap_[prescaleString] = -1;
        }
        else {
            triggerIntMap_[passString] = triggerBits->accept(trigBit);
            triggerIntMap_[prescaleString] = triggerPrescales->getPrescaleForIndex(trigBit);
        }
    }
    // filters
    const edm::TriggerNames& filters = iEvent.triggerNames(*filterBits);
    for (auto trigName : myFilterNames) {
        int trigBit = GetTriggerBit(trigName, filters);
        if (trigBit == -1) {
            triggerIntMap_[trigName] = -1;
        }
        else {
            triggerIntMap_[trigName] = filterBits->accept(trigBit);
        }
    }

}

// GetTriggerBit returns the trigger bit corresponding to the HLT name passed to it.
// It returns -1 if there is no match and throws an exception if there is more than one match.
// _________________________________________________________________________________
int TriggerBranches::GetTriggerBit(string trigName, const edm::TriggerNames &names)
{
    string trigPathString = triggerNamingMap_[trigName];
    regex regexp(trigPathString);
    int trigBit = -1;
    for (size_t i = 0; i < names.size(); i++) {
        if (regex_match(names.triggerName(i), regexp)) {
            if (trigBit != -1) { // if this isn't the first match
                throw cms::Exception("DuplicateTrigger");
            }
            trigBit = i;
        }
    }
    return trigBit;
}
