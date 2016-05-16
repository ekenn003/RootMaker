# RootMaker_cfi.py
# This file is imported by RootTree.py
# This is all default stuff - you shouldn't have to change anything in this file. 
import FWCore.ParameterSet.Config as cms

# load branches
from RootMaker.RootMaker.addTriggers     import * # triggerBranches, filterBranches
from RootMaker.RootMaker.addVertices     import * # vertexBranches
from RootMaker.RootMaker.addMuons        import * # muonBranches
from RootMaker.RootMaker.addElectrons    import * # electronBranches
from RootMaker.RootMaker.addJets         import * # jetBranches
from RootMaker.RootMaker.addMET          import * # metBranches
from RootMaker.RootMaker.addTaus         import * # tauBranches, TauDiscriminators
from RootMaker.RootMaker.addPhotons      import * # photonBranches

makeroottree = cms.EDAnalyzer("RootMaker",
    # configuration
    isData            = cms.bool(True),

    addGenParticles    = cms.bool(False),
    addAllGenParticles = cms.bool(False),
    addGenJets         = cms.bool(False),

    # generator info
    genEventInfo       = cms.InputTag("generator"),
    lheEventProduct    = cms.InputTag("externalLHEProducer"),
    prunedGenParticles = cms.InputTag("prunedGenParticles"),
    packedGenParticles = cms.InputTag("packedGenParticles"),
    genJets            = cms.InputTag("slimmedGenJets"),
    slimGenMET         = cms.InputTag("slimmedMETs"),

    # event info
    pileupSummaryInfo = cms.InputTag("slimmedAddPileupInfo"),
    rho               = cms.InputTag("fixedGridRhoFastjetAll"),
    vertices          = cms.InputTag("offlineSlimmedPrimaryVertices"),
    lumiProducer      = cms.InputTag("lumiProducer"),
    beamSpot          = cms.InputTag("offlineBeamSpot", "", "RECO"),

    # trigger
    triggerResults    = cms.InputTag("TriggerResults",  "", "HLT"),
    filterResults     = cms.InputTag("TriggerResults",  "", "PAT"),
    triggerObjects    = cms.InputTag("selectedPatTrigger"),
    triggerPrescales  = cms.InputTag("patTrigger"),
    l1trigger         = cms.InputTag("gtDigis"),
    # trigger branches
    triggerBranches   = triggerBranches,
    filterBranches    = filterBranches,

    # tau discriminators defined in python/addTaus.py
    RecTauDiscriminators = cms.untracked.vstring(TauDiscriminators),

    # set default object collections (overridden by "objectCollections" in RootTree.py)
    vertexCollections = cms.PSet(
        vertices = cms.PSet(
            collection = cms.InputTag("offlineSlimmedPrimaryVertices"),
            branches = vertexBranches,
        ),
    ),
    objectCollections = cms.PSet(
        electrons = cms.PSet(
            collection = cms.InputTag("slimmedElectrons"),
            branches = electronBranches,
        ),
        muons = cms.PSet(
            collection = cms.InputTag("slimmedMuons"),
            branches = muonBranches,
        ),
        taus = cms.PSet(
            collection = cms.InputTag("slimmedTaus"),
            branches = tauBranches,
        ),
        photons = cms.PSet(
            collection = cms.InputTag("slimmedPhotons"),
            branches = photonBranches,
        ),
        ak4pfchsjets = cms.PSet(
            collection = cms.InputTag("slimmedJets"),
            branches = jetBranches,
        ),
        pfmettype1 = cms.PSet(
            collection = cms.InputTag("slimmedMETs"),
            branches = metBranches,
        ),
    ),

    HLTriggerSelection = cms.untracked.vstring(),

    # Which triggers will be available for matching (going to move this to addMuons, etc.):
    RecMuonHLTriggerMatching = cms.untracked.vstring(
        'HLT_IsoMu20_v.*:FilterTrue', 
        'HLT_IsoTkMu20_v.*:FilterTrue'
    ),
    RecElectronHLTriggerMatching = cms.untracked.vstring(
    ),
    RecPhotonHLTriggerMatching = cms.untracked.vstring(
    ),
    RecTauHLTriggerMatching = cms.untracked.vstring(
    ),
    RecJetHLTriggerMatching = cms.untracked.vstring(
    ),

)
