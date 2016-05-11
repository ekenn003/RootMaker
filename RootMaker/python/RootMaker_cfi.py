# RootMaker_cfi.py
# 
# This file is imported by RootTree.py
# 
# options are registered (initialised) in this file, but
# this file does not know what they are set to in RootTree.py.
# Therefore any actions which depend on the values of options
# (eg isMC) must go in RootTree.py and not this file.

import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.register('skipEvents', 0)
options.register('isMC', False)
options.register('runMetFilter', 0, VarParsing.multiplicity.singleton, VarParsing.varType.int, "Run the recommended MET filters")

process = cms.Process("ROOTMAKER")

process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.Services_cff')

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
)

# load branches
from RootMaker.RootMaker.addTriggers     import * # triggerBranches, filterBranches
from RootMaker.RootMaker.addVertices     import * # vertexBranches
from RootMaker.RootMaker.addMuons        import * # muonBranches
from RootMaker.RootMaker.addElectrons    import * # electronBranches
from RootMaker.RootMaker.addJets         import * # jetBranches
from RootMaker.RootMaker.addMET          import * # metBranches
from RootMaker.RootMaker.addTaus         import * # tauBranches, TauDiscriminators
from RootMaker.RootMaker.addPhotons      import * # photonBranches
from RootMaker.RootMaker.addGenParticles import * # genParticleBranches, genJetBranches, getMETBranches

# default selections (overridden in RootTree.py)
selections = {
    'electrons'    : 'pt>4 && abs(eta)<5.',
    'muons'        : 'pt>4 && abs(eta)<5.',
    'taus'         : 'pt>4 && abs(eta)<5.',
    'photons'      : 'pt>4 && abs(eta)<5.',
    'ak4pfchsjets' : 'pt>4 && abs(eta)<5.',
}

makeroottree = cms.EDAnalyzer("RootMaker",
    isData            = cms.bool(True),
    # input tags
    genEventInfo      = cms.InputTag("generator"),
    lheEventProduct   = cms.InputTag("externalLHEProducer"),
    rho               = cms.InputTag("fixedGridRhoFastjetAll"),
    pileupSummaryInfo = cms.InputTag("slimmedAddPileupInfo"),
    lumiProducer      = cms.InputTag("lumiProducer"),
    beamSpot          = cms.InputTag("offlineBeamSpot", "", "RECO"),
    triggerResults    = cms.InputTag("TriggerResults","","HLT"),
    filterResults     = cms.InputTag("TriggerResults","","PAT"),
    triggerObjects    = cms.InputTag("selectedPatTrigger"),
    triggerPrescales  = cms.InputTag("patTrigger"),

    l1trigger = cms.InputTag("gtDigis"),
    RecTauDiscriminators = cms.untracked.vstring(TauDiscriminators),

    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),


    triggerBranches   = triggerBranches,
    filterBranches    = filterBranches,


    vertexCollections = cms.PSet(
        vertices = cms.PSet(
            collection = cms.InputTag("slimmedOfflinePrimaryVertices"),
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

