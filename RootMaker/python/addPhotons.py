import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import commonEgammaBranches

photonBranches = commonEgammaBranches.clone(
    # photon_info:
    hasconversiontracks = cms.vstring('hasConversionTracks','I'),
    haspixelseed        = cms.vstring('hasPixelSeed','I'),
    passelectronveto    = cms.vstring('passElectronVeto','I'),
    ispfphoton          = cms.vstring('isPFlowPhoton','I'),

    maxenergyxtal = cms.vstring('maxEnergyXtal','F'), 
    # shower information
    e1x5 = cms.vstring('e1x5','F'), 
    e2x5 = cms.vstring('e2x5','F'), 
    e3x3 = cms.vstring('e3x3','F'), 
    e5x5 = cms.vstring('e5x5','F'), 

    # more isolation
    isolationr3trackhollow  = cms.vstring('trkSumPtHollowConeDR03','F'),
    isolationr3ntrack       = cms.vstring('nTrkSolidConeDR03','I'),
    isolationr3ntrackhollow = cms.vstring('nTrkHollowConeDR03','I'),
    isolationr4trackhollow  = cms.vstring('trkSumPtHollowConeDR04','F'),
    isolationr4ntrack       = cms.vstring('nTrkSolidConeDR04','I'),
    isolationr4ntrackhollow = cms.vstring('nTrkHollowConeDR04','I'),
)

def addPhotons(process, coll, **kwargs):
    isMC = kwargs.pop('isMC', False)
    pSrc = coll['photons']
    # customization path
    process.photonCustomization = cms.Path()

    ######################
    ### embed gap info ###
    ######################
    process.pGI = cms.EDProducer(
        "PhotonGapInfoEmbedder",
        src = cms.InputTag(pSrc),
    )
    pSrc = 'pGI'
    process.photonCustomization *= process.pGI

    ####################################
    ### embed shower shape variables ###
    ####################################
    if isMC:
        process.pSS = cms.EDProducer(
            "PhotonShowerShapeEmbedder",
            src = cms.InputTag(pSrc),
            barrelHits = cms.InputTag("reducedEgamma", "reducedEBRecHits", "PAT"),
            endcapHits = cms.InputTag("reducedEgamma", "reducedEERecHits", "PAT"),
        )
    else:
        process.pSS = cms.EDProducer(
            "PhotonShowerShapeEmbedder",
            src = cms.InputTag(pSrc),
            barrelHits = cms.InputTag("reducedEgamma", "reducedEBRecHits", "RECO"),
            endcapHits = cms.InputTag("reducedEgamma", "reducedEERecHits", "RECO"),
        )
    pSrc = 'pSS'
    process.photonCustomization *= process.pSS

    #############################
    ### embed effective areas ###
    #############################
    eaFile = 'RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'
    process.pEffArea = cms.EDProducer(
        "PhotonEffectiveAreaEmbedder",
        src = cms.InputTag(pSrc),
        label = cms.string("EffectiveArea"), # embeds a user float with this name
        configFile = cms.FileInPath(eaFile), # the effective areas file
    )
    pSrc = 'pEffArea'
    process.photonCustomization *= process.pEffArea

    ###################################
    ### scale and smear corrections ###
    ###################################
    #process.load('EgammaAnalysis.ElectronTools.calibratedPhotonsRun2_cfi')
    #process.calibratedPatPhotons.photons = pSrc
    #process.calibratedPatPhotons.isMC = isMC
    #process.photonCustomization *= process.calibratedPatPhotons
    #pSrc = 'calibratedPatPhotons'

    # add to schedule
    process.schedule.append(process.photonCustomization)
    coll['photons'] = pSrc
    return coll
