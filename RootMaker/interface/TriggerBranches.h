// TriggerBranches.h
#include "CondFormats/DataRecord/interface/L1GtPrescaleFactorsAlgoTrigRcd.h"
#include "CondFormats/DataRecord/interface/L1GtPrescaleFactorsTechTrigRcd.h"
#include "CondFormats/L1TObjects/interface/L1GtPrescaleFactors.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"
#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1GtUtils.h"
#include <regex>
#include "TTree.h"
#include "DataFormats/Math/interface/deltaR.h"

using namespace std;

class TriggerBranches
{
  public:
    TriggerBranches(TTree *tree, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc);
    void fill(const edm::Event &iEvent);

  private:
    int GetTriggerBit(string trigName, const edm::TriggerNames &names);

    // tokens
    edm::EDGetTokenT<edm::TriggerResults> triggerBitsToken_;
    edm::EDGetTokenT<edm::TriggerResults> filterBitsToken_;
    edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjectsToken_;
    edm::EDGetTokenT<pat::PackedTriggerPrescales> triggerPrescalesToken_;

    // handles
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<edm::TriggerResults> filterBits;
    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;

    // branch parameters
    edm::ParameterSet triggerBranches;
    edm::ParameterSet filterBranches;

    // trigger
    vector<string> myTriggerNames;
    vector<string> myFilterNames;
    vector<string> triggerBranchStrings;
    map<string, string> triggerNamingMap_;
    map<string, Int_t>  triggerIntMap_;
};
