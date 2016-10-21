# RootMaker_cfi.py
# This file is imported by RootTree.py
# This is all default stuff - you shouldn't have to change anything in this file. 
import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
# set defaults:
options.register('globalTag', '', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'Global Tag')
options.register('overrideGT', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'Override the global tag with default')
options.register('skipEvents', 0, VarParsing.multiplicity.singleton, VarParsing.varType.int, 'Number of events to skip (from beginning)')
options.register('isMC', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'Is MC')
options.register('recGenParticles', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'Include GenParticles')
options.register('recAllGenParticles', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'Include AllGenParticles')
options.register('recGenJets', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'Include GenJets')
options.register('runMetFilter', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'Run the recommended MET filters')

options.register('sourceDS', 'None', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'Source dataset')

# load branches
from RootMaker.RootMaker.addTriggers     import * # triggerBranches, filterBranches
from RootMaker.RootMaker.addVertices     import * # vertexBranches
from RootMaker.RootMaker.addMuons        import * # muonBranches
from RootMaker.RootMaker.addElectrons    import * # electronBranches
from RootMaker.RootMaker.addJets         import * # jetBranches
from RootMaker.RootMaker.addMET          import * # metBranches
from RootMaker.RootMaker.addTaus         import * # tauBranches, TauDiscriminators
from RootMaker.RootMaker.addPhotons      import * # photonBranches

# set overridable defaults
makeroottree = cms.EDAnalyzer("RootMaker",
    # configuration
    isData            = cms.bool(True),
    sourceDataset     = cms.string('None'),

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
#        taus = cms.PSet(
#            collection = cms.InputTag("slimmedTaus"),
#            branches = tauBranches,
#        ),
#        photons = cms.PSet(
#            collection = cms.InputTag("slimmedPhotons"),
#            branches = photonBranches,
#        ),
        ak4pfchsjets = cms.PSet(
            collection = cms.InputTag("slimmedJets"),
            branches = jetBranches,
        ),
        pfmettype1 = cms.PSet(
            collection = cms.InputTag("slimmedMETs"),
            branches = metBranches,
        ),
    ),
)
