import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.RootMaker_cfi import *
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

##############################
### MC / data ################
##############################
#options.isMC = False # data
options.isMC = True # MC

##############################
### Global tag ###############
##############################
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
#options.globalTag = '80X_dataRun2_Prompt_ICHEP16JEC_v0'
options.globalTag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'

# uncomment this line to override the given global tag with the latest one (not recommended)
options.overrideGT = False # (default is false)

##############################
### Input files ##############
##############################

#options.inputFiles = 'file:/afs/cern.ch/work/e/ekennedy/work/tuplizer/tup80/CMSSW_8_0_12/src/RootMaker/RootMaker/da_SMu16B_80x.root'
options.inputFiles = 'file:/afs/cern.ch/work/e/ekennedy/work/tuplizer/tup80/CMSSW_8_0_12/src/RootMaker/RootMaker/mc_DYJets_80x.root'

#############################
## Running options ##########
#############################

options.maxEvents = 1000

#options.skipEvents = 20

options.runMetFilter = False

# include gen particles? (if !isMC they will be False anyway)
if options.isMC:
    options.recGenParticles = True # (default is False)
    options.recAllGenParticles = True # (default is False)
    options.recGenJets = True # (default is False)



#############################################################
### you probably don't have to change anything below here ###
#############################################################

#############################
### Object sources ##########
#############################
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

#############################
### PROCESS #################
#############################
process = cms.Process("ROOTMAKER")

process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.Services_cff')

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
)

#############################
### Output file #############
#############################
if options.isMC:
    options.outputFile = 'AC1B_80mc.root'
else:
    options.outputFile = 'AC1B_80data.root'


################################
### Override global tag ########
################################
process.GlobalTag.globaltag = options.globalTag
if options.overrideGT:
    envvar = 'mcgt' if options.isMC else 'datagt'
    from Configuration.AlCa.GlobalTag import GlobalTag
    #GT = {'mcgt': 'auto:run2_mc', 'datagt': 'auto:run2_data'}
    # ichep GT (includes JECs)
    # https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC
    GT = {'mcgt': '80X_mcRun2_asymptotic_2016_miniAODv2_v1', 'datagt': '80X_dataRun2_Prompt_ICHEP16JEC_v0'}
    process.GlobalTag = GlobalTag(process.GlobalTag, GT[envvar], '')



################################
### Run options ################
################################
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

###########################
### Profiling utilities ###
###########################
#process.ProfilerService = cms.Service (
#      "ProfilerService",
#       firstEvent = cms.untracked.int32(2),
#       lastEvent = cms.untracked.int32(500),
#       paths = cms.untracked.vstring('schedule') 
#)
#



#process.SimpleMemoryCheck = cms.Service(
#    "SimpleMemoryCheck",
#    ignoreTotal = cms.untracked.int32(1)
#)



# To use IgProf's neat memory profiling tools, uncomment the following 
# lines then run this cfg with igprof like so:
#      $ igprof -d -mp -z -o igprof.mp.gz cmsRun ... 
# this will create a memory profile every 250 events so you can track use
# Turn the profile into text with
#      $ igprof-analyse -d -v -g -r MEM_LIVE igprof.yourOutputFile.gz > igreport_live.res
# To do a performance profile instead of a memory profile, change -mp to -pp
# in the first command and remove  -r MEM_LIVE from the second
# For interpretation of the output, see http://igprof.org/text-output-format.html

#from IgTools.IgProf.IgProfTrigger import igprof
#process.load("IgTools.IgProf.IgProfTrigger")
#process.igprofPath = cms.Path(process.igprof)
#process.igprof.reportEventInterval     = cms.untracked.int32(250)
#process.igprof.reportToFileAtBeginJob  = cms.untracked.string("|gzip -c>igprof.begin-job.gz")
#process.igprof.reportToFileAtEvent = cms.untracked.string("|gzip -c>igprof.%I.%E.%L.%R.event.gz")
#process.schedule.append(process.igprofPath)


################################
### Selections definitions #####
################################
# the selections for each object (to be included in ntuple)
# will always be the last thing done to the collection, so can use embedded things from previous steps
selections = {
    'electrons'    : 'pt>4 && abs(eta)<5.',
    'muons'        : 'pt>4 && abs(eta)<5.',
    'taus'         : 'pt>4 && abs(eta)<5.',
    'photons'      : 'pt>4 && abs(eta)<5.',
    'ak4pfchsjets' : 'pt>4 && abs(eta)<5.',
}

################################
### Cleaning definitions #######
################################
# selection for cleaning (objects should match final selection)
cleaning = {
#    # clean jets agains electrons, muons, and taus with dR of 0.3
#    'ak4pfchsjets' : {
#        'electrons' : {
#            'cut' : 'pt > 10 && abs(eta) < 2.5',
#            'dr'  : 0.3,
#        },
#        'muons' : {
#            'cut' : 'pt > 10 && abs(eta) < 2.4 && isMediumMuon && trackIso/pt < 0.3 && userFloat("dxy") < 0.02 && userFloat("dz") < 0.14 && (pfIsolationR04().sumChargedHadronPt+max(0.,pfIsolationR04().sumNeutralHadronEt+pfIsolationR04().sumPhotonEt-0.5*pfIsolationR04().sumPUPt))/pt < 0.15',
#            'dr'  : 0.3,
#        },
#        'taus' : {
#            'cut' : 'pt > 20 && abs(eta) < 2.3 && tauID("decayModeFinding")',
#            'dr'  : 0.3,
#        },
#    },
}

################################
### Filters ####################
################################
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

################################
### Add object collections #####
################################
objectCollections = addElectrons(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)
objectCollections = addMuons(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)
objectCollections = addTaus(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)
objectCollections = addPhotons(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)
objectCollections = addJets(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)
objectCollections = addMET(
    process,
    objectCollections,
    isMC=bool(options.isMC),
)

################################
### Select/clean objects #######
################################
from RootMaker.RootMaker.objectTools import collectionFilter, objectCleaner
for coll in selections:
    objectCollections[coll] = collectionFilter(process, coll, objectCollections[coll], selections[coll])
for coll in cleaning:
    objectCollections[coll] = objectCleaner(process, coll, objectCollections[coll], objectCollections, cleaning[coll])

################################
### Load the analyzer ##########
################################
process.load("RootMaker.RootMaker.RootMaker_cfi")

process.makeroottree.isData = not options.isMC
process.makeroottree.addGenParticles    = bool(options.recGenParticles)
process.makeroottree.addAllGenParticles = bool(options.recAllGenParticles)
process.makeroottree.addGenJets         = bool(options.recGenJets)

process.makeroottree.filterResults = cms.InputTag('TriggerResults', '', 'PAT') if options.isMC else cms.InputTag('TriggerResults', '', 'RECO')
# send collections again in case they've been modified:
process.makeroottree.vertexCollections.vertices.collection     = objectCollections['vertices']
process.makeroottree.objectCollections.electrons.collection    = objectCollections['electrons']
process.makeroottree.objectCollections.muons.collection        = objectCollections['muons']
process.makeroottree.objectCollections.taus.collection         = objectCollections['taus']
process.makeroottree.objectCollections.photons.collection      = objectCollections['photons']
process.makeroottree.objectCollections.ak4pfchsjets.collection = objectCollections['ak4pfchsjets']
process.makeroottree.objectCollections.pfmettype1.collection   = objectCollections['pfmettype1']

################################
### Path #######################
################################
process.makeroottreePath = cms.Path()
for f in filters:
    process.makeroottreePath += f
process.makeroottreePath += process.makeroottree
process.schedule.append(process.makeroottreePath)


################################
### debugging ##################
################################
print process.GlobalTag.globaltag
