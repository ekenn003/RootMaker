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
//#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"


#include "TTree.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "RootMaker/RootMaker/interface/ObjectCollectionBranches.h"
#include "RootMaker/RootMaker/interface/VertexCollectionBranches.h"
#include "RootMaker/RootMaker/interface/MonteCarloBranches.h"
#include "RootMaker/RootMaker/interface/TriggerBranches.h"

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
    //void TriggerIndexSelection(vector<string> configstring, vector<pair<unsigned, int> > &triggers, string &allnames);

    // tokens
    edm::EDGetTokenT<GenEventInfoProduct> genEventInfoToken_;
    edm::EDGetTokenT<double> rhoToken_;
    edm::EDGetTokenT<vector<PileupSummaryInfo> > PUInfoToken_;
    edm::EDGetTokenT<LumiSummary> lumiInfoToken_;
    edm::EDGetTokenT<L1GlobalTriggerReadoutRecord> l1TriggerToken_;
//    edm::EDGetTokenT<reco::BeamSpot> beamSpotToken_;
    edm::EDGetTokenT<reco::VertexCollection> verticesToken_;

    // branches
    edm::ParameterSet vertexCollections;
    edm::ParameterSet objectCollections;

    // configuration
    bool isData_;
    string sourceDS_;

    // trees
    TTree *infotree;
    TTree *lumitree;
    TTree *tree;

    // data
    math::XYZPoint pv_position;
    Vertex primvertex;
    math::XYZPoint bs_position;

    // info tree branches
    Bool_t  isdata;
    UInt_t  nevents;
    UInt_t  nevents_skipped;
    UInt_t  nevents_filled;
    Float_t sumweights;
    TString CMSSW_version;
    TString source_dataset;

    // lumitree branches
    UInt_t  lumi_run;
    UInt_t  lumi_block;
    Float_t lumi_value;
    Float_t lumi_valueerr;
    Float_t lumi_livefrac;
    Float_t lumi_deadfrac;
    Float_t lumi_avgpu;
    UInt_t  lumi_quality;
    UInt_t  lumi_eventsprocessed;
    UInt_t  lumi_eventsfiltered;
    UInt_t  lumi_sumweights;
    UInt_t  lumi_nevents;

    // once per event branches
    ULong64_t event_nr;
    UInt_t   event_run;
    UInt_t   event_timeunix;
    UInt_t   event_timemicrosec;
    UInt_t   event_luminosityblock;
    Float_t  event_rho;

//    Float_t beamspot_x;
//    Float_t beamspot_y;
//    Float_t beamspot_z;
//    Float_t beamspot_xwidth;
//    Float_t beamspot_ywidth;
//    Float_t beamspot_zsigma;
//    Float_t beamspot_cov[6];
//
    Int_t   numpileupinteractionsminus;
    Int_t   numpileupinteractions;
    Int_t   numpileupinteractionsplus;
    Float_t numtruepileupinteractions;

    // collections
    vector<unique_ptr<VertexCollectionBranches> > vertexCollectionBranches;
    vector<unique_ptr<ObjectCollectionBranches> > objectCollectionBranches;
    unique_ptr<TriggerBranches>    triggerBranches;
    unique_ptr<MonteCarloBranches> monteCarloBranches;

    // Rochester corrections
    //RoccoR rc("rcdata.2016.v3");

};

void RootMaker::fillDescriptions(edm::ConfigurationDescriptions &descriptions)
{
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(RootMaker);
#endif
