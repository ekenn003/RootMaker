// TriggerBranches.cc
#include "RootMaker/RootMaker/interface/TriggerBranches.h"

TriggerBranches::TriggerBranches(TTree *tree, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc):
    triggerBitsToken_      (cc.consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("triggerResults"))),
    filterBitsToken_       (cc.consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("filterResults"))),
    triggerObjectsToken_   (cc.consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("triggerObjects"))),
    triggerPrescalesToken_ (cc.consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("triggerPrescales"))),
    triggerBranches (iConfig.getParameter<edm::ParameterSet>("triggerBranches")),
    filterBranches  (iConfig.getParameter<edm::ParameterSet>("filterBranches"))
{
    // get trigger parameters
    triggerBranchStrings.push_back("Pass");
    triggerBranchStrings.push_back("Prescale");
    myTriggerNames = triggerBranches.getParameterNames();
    for (auto trig : myTriggerNames) {
        edm::ParameterSet trigPSet = triggerBranches.getParameter<edm::ParameterSet>(trig);
        std::string trigString = trigPSet.getParameter<std::string>("path");
        triggerNamingMap_.insert(std::pair<std::string, std::string>(trig,trigString));
    }
    // get filter parameters
    myFilterNames = filterBranches.getParameterNames();
    for (auto trig : myFilterNames) {
        edm::ParameterSet trigPSet = filterBranches.getParameter<edm::ParameterSet>(trig);
        std::string trigString = trigPSet.getParameter<std::string>("path");
        triggerNamingMap_.insert(std::pair<std::string, std::string>(trig,trigString));
    }

    // add triggers
    for (auto trigName : myTriggerNames) {
        for (auto branch : triggerBranchStrings) {
            std::string branchName = trigName + branch;
            Int_t branchVal;
            triggerIntMap_.insert(std::pair<std::string, Int_t>(branchName,branchVal));
            std::string branchLeaf = branchName + "/I";
            tree->Branch(branchName.c_str(), &triggerIntMap_[branchName], branchLeaf.c_str());
        }
    }
    // add filters
    for (auto trigName : myFilterNames) {
        Int_t branchVal;
        triggerIntMap_.insert(std::pair<std::string, Int_t>(trigName,branchVal));
        std::string branchLeaf = trigName + "/I";
        tree->Branch(trigName.c_str(), &triggerIntMap_[trigName], branchLeaf.c_str());
    }

}

// GetTriggerBit returns the trigger bit corresponding to the HLT name passed to it.
// It returns -1 if there is no match and throws an exception if there is more than one match.
// _________________________________________________________________________________
int TriggerBranches::GetTriggerBit(std::string trigName, const edm::TriggerNames &names)
{
    std::string trigPathString = triggerNamingMap_[trigName];
    std::regex regexp(trigPathString);
    int trigBit = -1;
    for (size_t i = 0; i < names.size(); i++) {
        if (std::regex_match(names.triggerName(i), regexp)) {
            if (trigBit != -1) { // if this isn't the first match
                throw cms::Exception("DuplicateTrigger");
            }
            trigBit = i;
        }
    }
    return trigBit;
}
