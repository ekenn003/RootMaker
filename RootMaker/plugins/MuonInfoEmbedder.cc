// MuonInfoEmbedder.cc
// Embeds muon_trackermuonquality
// Embeds muon_innertrack_dz
// Embeds muon_innertrack_dxy
// Embeds muon_isTightMuon
// Embeds muon_isMedium2016Muon
// Embeds muon_numberOfMatches

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

using namespace std;

class MuonInfoEmbedder : public edm::stream::EDProducer<>
{
  public:
    explicit MuonInfoEmbedder(const edm::ParameterSet&);
    ~MuonInfoEmbedder() {}
    bool isMedium2016Muon(const reco::Muon &recoMu);
    static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  private:
    void beginJob() {}
    virtual void produce(edm::Event& iEvent, const edm::EventSetup &iSetup);
    void endJob() {}

    edm::EDGetTokenT<edm::View<pat::Muon> > muonToken_;
    edm::EDGetTokenT<reco::VertexCollection> vertexToken_;
    auto_ptr<vector<pat::Muon> > output;
};

MuonInfoEmbedder::MuonInfoEmbedder(const edm::ParameterSet& iConfig):
    muonToken_(consumes<edm::View<pat::Muon> >(iConfig.getParameter<edm::InputTag>("src"))),
    vertexToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertexSrc")))
{
    produces<vector<pat::Muon> >();
}

void MuonInfoEmbedder::produce(edm::Event& iEvent, const edm::EventSetup &iSetup)
{
    output = auto_ptr<vector<pat::Muon> >(new vector<pat::Muon>);
    edm::Handle<edm::View<pat::Muon> > muons;
    iEvent.getByToken(muonToken_, muons);
    edm::Handle<reco::VertexCollection> vertices;
    iEvent.getByToken(vertexToken_, vertices);

    const reco::Vertex &pv = *vertices->begin();
    for (size_t c = 0; c < muons->size(); ++c) {
        const auto muon = muons->at(c);
        pat::Muon newMuon = muon;

        // add tight muon id
        newMuon.addUserInt("isTightMuon", muon.isTightMuon(pv));
        newMuon.addUserInt("isMedium2016Muon", isMedium2016Muon(muon));

        // add numberOfMatches
        Int_t nmatches = muon.numberOfMatches(reco::Muon::SegmentAndTrackArbitration);
        newMuon.addUserInt("numberOfMatches", nmatches);

        // add muon_trackermuonquality
        Int_t quality = 0;
        {
            using namespace muon;
            if(isGoodMuon(muon, All))                                    { quality |= 1 << 0; }
            if(isGoodMuon(muon, AllGlobalMuons))                         { quality |= 1 << 1; }
            if(isGoodMuon(muon, AllStandAloneMuons))                     { quality |= 1 << 2; }
            if(isGoodMuon(muon, AllTrackerMuons))                        { quality |= 1 << 3; }
            if(isGoodMuon(muon, TrackerMuonArbitrated))                  { quality |= 1 << 4; }
            if(isGoodMuon(muon, AllArbitrated))                          { quality |= 1 << 5; }
            if(isGoodMuon(muon, GlobalMuonPromptTight))                  { quality |= 1 << 6; }
            if(isGoodMuon(muon, TMLastStationLoose))                     { quality |= 1 << 7; }
            if(isGoodMuon(muon, TMLastStationTight))                     { quality |= 1 << 8; }
            if(isGoodMuon(muon, TM2DCompatibilityLoose))                 { quality |= 1 << 9; }
            if(isGoodMuon(muon, TM2DCompatibilityTight))                 { quality |= 1 << 10; }
            if(isGoodMuon(muon, TMOneStationLoose))                      { quality |= 1 << 11; }
            if(isGoodMuon(muon, TMOneStationTight))                      { quality |= 1 << 12; }
            if(isGoodMuon(muon, TMLastStationOptimizedLowPtLoose))       { quality |= 1 << 13; }
            if(isGoodMuon(muon, TMLastStationOptimizedLowPtTight))       { quality |= 1 << 14; }
            if(isGoodMuon(muon, GMTkChiCompatibility))                   { quality |= 1 << 15; }
            if(isGoodMuon(muon, GMStaChiCompatibility))                  { quality |= 1 << 16; }
            if(isGoodMuon(muon, GMTkKinkTight))                          { quality |= 1 << 17; }
            if(isGoodMuon(muon, TMLastStationAngLoose))                  { quality |= 1 << 18; }
            if(isGoodMuon(muon, TMLastStationAngTight))                  { quality |= 1 << 19; }
            if(isGoodMuon(muon, TMOneStationAngLoose))                   { quality |= 1 << 20; }
            if(isGoodMuon(muon, TMOneStationAngTight))                   { quality |= 1 << 21; }
            if(isGoodMuon(muon, TMLastStationOptimizedBarrelLowPtLoose)) { quality |= 1 << 22; }
            if(isGoodMuon(muon, TMLastStationOptimizedBarrelLowPtTight)) { quality |= 1 << 23; }
        }
        if(muon.time().direction() == 1) { quality |= 1<<30; } 
        else if(muon.time().direction() == -1) { quality |= 1<<31; }
        newMuon.addUserInt("trackermuonquality", quality);

        // add innertrack_d*
        Float_t innertrack_dz  = 0.;
        Float_t innertrack_dxy = 0.;
        if(muon.innerTrack().isNonnull()) {
            innertrack_dz  = muon.innerTrack()->dz(pv.position());
            innertrack_dxy = muon.innerTrack()->dxy(pv.position());
        }
        newMuon.addUserFloat("innertrack_dz", innertrack_dz);
        newMuon.addUserFloat("innertrack_dxy", innertrack_dxy);

        // save it
        output->push_back(newMuon);
    }
    // put it in our new muons
    iEvent.put(output);
}

// https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#Short_Term_Instructions_for_Mori
bool MuonInfoEmbedder::isMedium2016Muon(const reco::Muon &recoMu)
{
    bool goodGlob = recoMu.isGlobalMuon() &&
                    recoMu.globalTrack()->normalizedChi2() < 3 &&
                    recoMu.combinedQuality().chi2LocalPosition < 12 &&
                    recoMu.combinedQuality().trkKink < 20;
    bool isMedium = muon::isLooseMuon(recoMu) &&
                    recoMu.innerTrack()->validFraction() > 0.49 &&
                    muon::segmentCompatibility(recoMu) > (goodGlob ? 0.303 : 0.451);
    return isMedium;
}

void MuonInfoEmbedder::fillDescriptions(edm::ConfigurationDescriptions &descriptions)
{
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(MuonInfoEmbedder);
