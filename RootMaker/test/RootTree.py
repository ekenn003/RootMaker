import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.RootMaker_cfi import *

options.inputFiles = 'file:/afs/cern.ch/work/e/ekennedy/work/tuplizer/tup76/SingleRunD_16dec_76.root'
#options.inputFiles = 'file:/afs/cern.ch/work/e/ekennedy/work/tuplizer/tup76/ZZT4L_powheg_76.root'

# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
#process.GlobalTag.globaltag = cms.string('76X_dataRun2_v15')
#process.GlobalTag.globaltag = cms.string('76X_mcRun2_asymptotic_v12')

options.isMC = 0
#options.isMC = 1

options.maxEvents = 1000
#options.maxEvents = -1

#options.skipEvents = 20

options.runMetFilter = 0

#####################
### setup process ###
#####################

if options.isMC:
    options.outputFile = 'AC1B_76mc.root'
else:
    options.outputFile = 'AC1B_76data.root'



#################
### GlobalTag ###
#################
# uncomment this section to override the given global tag with the latest one (not recommended)
envvar = 'mcgt' if options.isMC else 'datagt'
from Configuration.AlCa.GlobalTag import GlobalTag
GT = {'mcgt': 'auto:run2_mc', 'datagt': 'auto:run2_data'}
process.GlobalTag = GlobalTag(process.GlobalTag, GT[envvar], '')



#############################
### Setup rest of running ###
#############################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    skipEvents = cms.untracked.uint32(options.skipEvents)
)
process.TFileService = cms.Service("TFileService", 
    fileName = cms.string(options.outputFile),
)
process.schedule = cms.Schedule()

# first create objectCollections to analyze
objectCollections = {
    'genParticles' : 'prunedGenParticles',
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

# the selections for each object (to be included in ntuple)
# will always be the last thing done to the collection, so can use embedded things from previous steps
selections = {
    'electrons'    : 'pt>4 && abs(eta)<5.',
    'muons'        : 'pt>4 && abs(eta)<5.',
    'taus'         : 'pt>4 && abs(eta)<5.',
    'photons'      : 'pt>4 && abs(eta)<5.',
    'ak4pfchsjets' : 'pt>4 && abs(eta)<5.',
}

# selection for cleaning (objects should match final selection)
cleaning = {
    # clean jets agains electrons, muons, and taus with dR of 0.3
    'ak4pfchsjets' : {
        'electrons' : {
            'cut' : 'pt > 10 && abs(eta) < 2.5',
            'dr'  : 0.3,
        },
        'muons' : {
            'cut' : 'pt > 10 && abs(eta) < 2.4 && isMediumMuon && trackIso/pt < 0.3 && userFloat("dxy") < 0.02 && userFloat("dz") < 0.14 && (pfIsolationR04().sumChargedHadronPt+max(0.,pfIsolationR04().sumNeutralHadronEt+pfIsolationR04().sumPhotonEt-0.5*pfIsolationR04().sumPUPt))/pt < 0.15',
            'dr'  : 0.3,
        },
        'taus' : {
            'cut' : 'pt > 20 && abs(eta) < 2.3 && tauID("decayModeFinding")',
            'dr'  : 0.3,
        },
    },
}

# filters
filters = []

# met filters
if options.runMetFilter:
    from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
    hltFilter = hltHighLevel.clone()
    # PAT for MC and RECO for data
    hltFilter.TriggerResultsTag = cms.InputTag('TriggerResults', '', 'PAT') if options.isMC else cms.InputTag('TriggerResults', '', 'RECO')
    hltFilter.throw = cms.bool(True)
    for flag in ["HBHENoiseFilter", "HBHENoiseIsoFilter", "CSCTightHalo2015Filter", "EcalDeadCellTriggerPrimitiveFilter", "goodVertices", "eeBadScFilter"]:
        mod = hltFilter.clone(HLTPaths=cms.vstring('Flag_{0}'.format(flag)))
        modName = 'filter{0}'.format(flag)
        setattr(process,modName,mod)
        filters += [getattr(process,modName)]

# now do any customization/cleaning
#from RootMaker.RootMaker.addElectrons import addElectrons
objectCollections = addElectrons(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)

#from RootMaker.RootMaker.addMuons import addMuons
objectCollections = addMuons(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)

#from RootMaker.RootMaker.addTaus import addTaus
objectCollections = addTaus(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)

#from RootMaker.RootMaker.addPhotons import addPhotons
objectCollections = addPhotons(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)

#from RootMaker.RootMaker.addJets import addJets
objectCollections = addJets(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)

#from RootMaker.RootMaker.addMET import addMET
objectCollections = addMET(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)

# select desired objects
from RootMaker.RootMaker.objectTools import collectionFilter, objectCleaner
for coll in selections:
    objectCollections[coll] = collectionFilter(process,coll,objectCollections[coll],selections[coll])
for coll in cleaning:
    objectCollections[coll] = objectCleaner(process,coll,objectCollections[coll],objectCollections,cleaning[coll])

# add the analyzer
process.load("RootMaker.RootMaker.RootMaker_cfi")

process.makeroottree.isData = not options.isMC
process.makeroottree.filterResults = cms.InputTag('TriggerResults', '', 'PAT') if options.isMC else cms.InputTag('TriggerResults', '', 'RECO')
process.makeroottree.vertexCollections.vertices.collection = objectCollections['vertices']
#if options.isMC:
#    from RootMaker.RootMaker.branchTemplates import genParticleBranches 
#    process.makeroottree.objectCollections.genParticles = cms.PSet(
#        collection = cms.InputTag(objectCollections['genParticles']),
#        branches = genParticleBranches,
#    )
process.makeroottree.objectCollections.electrons.collection    = objectCollections['electrons']
process.makeroottree.objectCollections.muons.collection        = objectCollections['muons']
process.makeroottree.objectCollections.taus.collection         = objectCollections['taus']
process.makeroottree.objectCollections.photons.collection      = objectCollections['photons']
process.makeroottree.objectCollections.ak4pfchsjets.collection = objectCollections['ak4pfchsjets']
process.makeroottree.objectCollections.pfmettype1.collection   = objectCollections['pfmettype1']
process.makeroottree.rho = objectCollections['rho']

process.makeroottreePath = cms.Path()
for f in filters:
    process.makeroottreePath += f
process.makeroottreePath += process.makeroottree
process.schedule.append(process.makeroottreePath)
process.schedule.append(process.makeroottreePath)

print process.GlobalTag.globaltag
