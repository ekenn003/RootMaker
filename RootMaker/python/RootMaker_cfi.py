# RootMaker_cfi.py
# This file is imported by RootTree.py
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

# define input tags given for objectCollections
objectCollections = {
    'prunedgen'    : 'prunedGenParticles',
    'packedgen'    : 'packedGenParticles',
    'genjets'      : 'slimmedGenJets',
    'genmet'       : 'slimmedMETs', # genMET is embedded in slimmedMETs
    'electrons'    : 'slimmedElectrons',
    'muons'        : 'slimmedMuons',
    'taus'         : 'slimmedTaus',
    'photons'      : 'slimmedPhotons',
    'ak4pfchsjets' : 'slimmedJets',
    'pfmettype1'   : 'slimmedMETs',
    'rho'          : 'fixedGridRhoFastjetAll',
    'vertices'     : 'offlineSlimmedPrimaryVertices',
    'packed'       : 'packedPFCandidates',
}

makeroottree = cms.EDAnalyzer("RootMaker",
    # configuration
    isData            = cms.bool(True),

    addGenParticles    = cms.bool(False),
    addAllGenParticles = cms.bool(False),
    addGenJets         = cms.bool(False),

    # generator info
    genEventInfo       = cms.InputTag("generator"),
    lheEventProduct    = cms.InputTag("externalLHEProducer"),
    prunedGenParticles = cms.InputTag(objectCollections['prunedgen']),
    packedGenParticles = cms.InputTag(objectCollections['packedgen']),
    genJets            = cms.InputTag(objectCollections['genjets']),
    slimGenMET         = cms.InputTag(objectCollections['genmet']),

    # event info
    pileupSummaryInfo = cms.InputTag("slimmedAddPileupInfo"),
    rho               = cms.InputTag(objectCollections['rho']),
    vertices          = cms.InputTag(objectCollections['vertices']),
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

    # object collections
    vertexCollections = cms.PSet(
        vertices = cms.PSet(
            collection = cms.InputTag(objectCollections['vertices']),
            branches = vertexBranches,
        ),
    ),
    objectCollections = cms.PSet(
        electrons = cms.PSet(
            collection = cms.InputTag(objectCollections['electrons']),
            branches = electronBranches,
        ),
        muons = cms.PSet(
            collection = cms.InputTag(objectCollections['muons']),
            branches = muonBranches,
        ),
        taus = cms.PSet(
            collection = cms.InputTag(objectCollections['taus']),
            branches = tauBranches,
        ),
        photons = cms.PSet(
            collection = cms.InputTag(objectCollections['photons']),
            branches = photonBranches,
        ),
        ak4pfchsjets = cms.PSet(
            collection = cms.InputTag(objectCollections['ak4pfchsjets']),
            branches = jetBranches,
        ),
        pfmettype1 = cms.PSet(
            collection = cms.InputTag(objectCollections['pfmettype1']),
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
