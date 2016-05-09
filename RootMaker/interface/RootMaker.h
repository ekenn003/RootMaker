#ifndef RootMaker_h
#define RootMaker_h

#include <Math/Functions.h>
#include <Math/SMatrix.h>
#include <Math/SVector.h>
#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <boost/regex.hpp>
#include <cstdlib>
#include <map>
#include <regex>
#include <string>
#include <vector>

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "CondFormats/DataRecord/interface/L1GtPrescaleFactorsAlgoTrigRcd.h"
#include "CondFormats/DataRecord/interface/L1GtPrescaleFactorsTechTrigRcd.h"
#include "CondFormats/L1TObjects/interface/L1GtPrescaleFactors.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"
#include "L1Trigger/GlobalTriggerAnalyzer/interface/L1GtUtils.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/L1GlobalTrigger/interface/L1GlobalTriggerReadoutRecord.h"
#include "FWCore/Common/interface/TriggerNames.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Luminosity/interface/LumiSummary.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"

#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "TTree.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "RootMaker/RootMaker/interface/ObjectCollectionBranches.h"
#include "RootMaker/RootMaker/interface/VertexCollectionBranches.h"

using namespace std;
using namespace reco;
using namespace pat;

class RootMaker : public edm::one::EDAnalyzer<edm::one::SharedResources,edm::one::WatchLuminosityBlocks,edm::one::WatchRuns>
{
  public:
    explicit RootMaker(const edm::ParameterSet&);
    ~RootMaker();

    static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  private:
    virtual void beginJob() override;
    virtual void beginRun(edm::Run const &iRun, edm::EventSetup const&) override;
    virtual void beginLuminosityBlock(edm::LuminosityBlock const &iLumiBlock, edm::EventSetup const&) override;
    virtual void analyze(edm::Event const &iEvent, edm::EventSetup const&) override;
    virtual void endLuminosityBlock(edm::LuminosityBlock const &iLumiBlock, edm::EventSetup const&) override;
    virtual void endRun(edm::Run const &iRun, edm::EventSetup const&) override;
    virtual void endJob() override;
    void TriggerIndexSelection(vector<string> configstring, vector<pair<unsigned, int> > &triggers, string &allnames);
    int  GetTriggerBit(string trigName, const edm::TriggerNames& names);

    // tokens
    edm::EDGetTokenT<LHEEventProduct> lheEventProductToken_;
    edm::EDGetTokenT<GenEventInfoProduct> genEventInfoToken_;
    edm::EDGetTokenT<double> rhoToken_;
    edm::EDGetTokenT<vector<PileupSummaryInfo> > PUInfoToken_;
    edm::EDGetTokenT<LumiSummary> lumiInfoToken_;
    edm::EDGetTokenT<edm::TriggerResults> triggerBitsToken_;
    edm::EDGetTokenT<edm::TriggerResults> filterBitsToken_;
    edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjectsToken_;
    edm::EDGetTokenT<pat::PackedTriggerPrescales> triggerPrescalesToken_;
    edm::EDGetTokenT<L1GlobalTriggerReadoutRecord> l1TriggerToken_;
    edm::EDGetTokenT<reco::BeamSpot> beamSpotToken_;
    edm::EDGetTokenT<reco::VertexCollection> verticesToken_;

    // handles
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<edm::TriggerResults> filterBits;
    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;

    // branch parameters
    edm::ParameterSet triggerBranches;
    edm::ParameterSet filterBranches;
    edm::ParameterSet objectCollections;
    edm::ParameterSet vertexCollections;

    // configuration
    vector<string> cHLTriggerNamesSelection;
    vector<unsigned> HLTriggerIndexSelection;


    // variables

    //*// these will be removed soon
    vector<string> cMuHLTriggerMatching;
    vector<string> cElHLTriggerMatching;
    vector<string> cTauHLTriggerMatching;

    vector<string> cTauDiscriminators;

    vector<string> cPhotonHLTriggerMatching;
    vector<string> cJetHLTriggerMatching;
    vector<pair<unsigned, int> > muontriggers;
    vector<pair<unsigned, int> > electrontriggers;
    vector<pair<unsigned, int> > tautriggers;
    vector<pair<unsigned, int> > photontriggers;
    vector<pair<unsigned, int> > jettriggers;
    HLTPrescaleProvider HLTPrescaleProvider_;
    HLTConfigProvider HLTConfiguration;
    //*//


    bool isData_;

    // trees
    TTree *infotree;
    TTree *tree;
    TTree *runtree;
    TTree *lumitree;
    TH1D  *drhist;

    // info tree branches
    Bool_t  isdata;
    Int_t   nevents;
    Int_t   nevents_skipped;
    Int_t   nevents_filled;
    Float_t sum_weights;

    // data
    math::XYZPoint pv_position;
    Vertex primvertex;
    math::XYZPoint bs_position;

    //*// these will be removed or fixed soon
    // right now they are here to please the merger.cc
    // but soon AnalysisTool won't require LUMI_INFO.root
    // runtree branches
    UInt_t run_number;
    UInt_t run_hltcount;
    Char_t run_hltnames[20000];
    Char_t run_hltmunames[10000];
    Char_t run_hltelnames[10000];
    Char_t run_hlttaunames[10000];
    Char_t run_hltphotonnames[10000];
    Char_t run_hltjetnames[10000];
    UInt_t run_hltprescaletablescount;
    UInt_t run_hltprescaletables[10000];
    UInt_t run_hltl1prescaletables[10000];
    UInt_t run_l1algocount;
    UInt_t run_l1algoprescaletablescount;
    UInt_t run_l1algoprescaletables[10000];
    UInt_t run_l1techcount;
    UInt_t run_l1techprescaletablescount;
    UInt_t run_l1techprescaletables[10000];

    Char_t run_taudiscriminators[10000];


    // lumitree branches
    Int_t   lumi_run;
    Int_t   lumi_block;
    Float_t lumi_value;
    Float_t lumi_valueerr;
    Float_t lumi_livefrac;
    Float_t lumi_deadfrac;
    UInt_t  lumi_quality;
    UInt_t  lumi_eventsprocessed;
    UInt_t  lumi_eventsfiltered;
    UInt_t  lumi_hltprescaletable;
    UInt_t  lumi_l1algoprescaletable;
    UInt_t  lumi_l1techprescaletable;
    UInt_t  errors;

    UChar_t trigger_level1bits[8];
    UChar_t trigger_level1[128];
    UChar_t trigger_HLT[128];
    //*//

    // once per event branches
    Double_t event_nr;
    UInt_t   event_run;
    UInt_t   event_timeunix;
    UInt_t   event_timemicrosec;
    UInt_t   event_luminosityblock;
    Float_t  event_rho;

    Float_t beamspot_x;
    Float_t beamspot_y;
    Float_t beamspot_z;
    Float_t beamspot_xwidth;
    Float_t beamspot_ywidth;
    Float_t beamspot_zsigma;
    Float_t beamspot_cov[6];

    Float_t genweight;
    Float_t genid1;
    Float_t genx1;
    Float_t genid2;
    Float_t genx2;
    Float_t genScale;

    UInt_t  numpileupinteractionsminus;
    UInt_t  numpileupinteractions;
    UInt_t  numpileupinteractionsplus;
    Float_t numtruepileupinteractions;

    // trigger
    vector<string> myTriggerNames;
    vector<string> myFilterNames;
    vector<string> triggerBranchStrings;
    map<string, string> triggerNamingMap_;
    map<string, Int_t>  triggerIntMap_;

    // collections
    vector<unique_ptr<ObjectCollectionBranches> > objectCollectionBranches;
    vector<unique_ptr<VertexCollectionBranches> > vertexCollectionBranches;
};

void RootMaker::fillDescriptions(edm::ConfigurationDescriptions &descriptions)
{
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(RootMaker);
#endif
