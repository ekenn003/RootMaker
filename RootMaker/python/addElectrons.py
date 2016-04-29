import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import commonEgammaBranches

electronBranches = commonEgammaBranches.clone(
    # user data from PVEmbedder
    dz     = cms.vstring('userFloat("dz")','F'),
    dzerr  = cms.vstring('gsfTrack().dzError()','I'),
    dxy    = cms.vstring('userFloat("dxy")','F'),
    dxyerr = cms.vstring('gsfTrack().dxyError()','I'),

    correctedecalenergy              = cms.vstring('ecalEnergy','F'),

    # user data from HLTMatchEmbedder
    trigger = cms.vstring('userInt("trigger")','I'), # testing

    # electron_info:
    passconversionveto = cms.vstring('passConversionVeto','I'),
    ecaldrivenseed     = cms.vstring('ecalDrivenSeed','I'),
    trackerdrivenseed  = cms.vstring('trackerDrivenSeed','I'),

    # track information
    trackchi2   = cms.vstring('gsfTrack().chi2()','F'),
    trackndof   = cms.vstring('gsfTrack().ndof()','F'),
    nhits       = cms.vstring('gsfTrack().numberOfValidHits()','F'),
    npixelhits    = cms.vstring('gsfTrack().hitPattern().numberOfValidPixelHits()','I'),
    npixellayers  = cms.vstring('gsfTrack().hitPattern().pixelLayersWithMeasurement()','I'),
    nstriplayers  = cms.vstring('gsfTrack().hitPattern().stripLayersWithMeasurement()','I'),
    # these two things are the same in MC? 
    # user data embedded from ElectronMissingHitsEmbedder
    nmissinghits  = cms.vstring('userInt("missingHits")','I'),
    nhitsexpected = cms.vstring('gsfTrack().numberOfLostHits()','I'),

    # shower information
    r9   = cms.vstring('r9','F'),
    e1x5 = cms.vstring('e1x5','F'),
    e2x5 = cms.vstring('e2x5Max','F'),
    e5x5 = cms.vstring('e5x5','F'),

    fbrems   = cms.vstring('fbrem','F'),
    numbrems = cms.vstring('numberOfBrems','F'),

    # supercluster
    scE1x5             = cms.vstring('scE1x5','F'),
    scE2x5Max          = cms.vstring('scE2x5Max','F'),
    scE5x5             = cms.vstring('scE5x5','F'),
    esuperclusterovertrack    = cms.vstring('eSuperClusterOverP','F'),
    eseedclusterovertrack     = cms.vstring('eSeedClusterOverP','F'),
    deltaetasuperclustertrack = cms.vstring('deltaEtaSuperClusterTrackAtVtx','F'),
    deltaphisuperclustertrack = cms.vstring('deltaPhiSuperClusterTrackAtVtx','F'),

    # user data from VIDEmbedder
    cutBasedVeto         = cms.vstring('userInt("cutBasedElectronID-Spring15-25ns-V1-standalone-veto")','I'),
    cutBasedLoose        = cms.vstring('userInt("cutBasedElectronID-Spring15-25ns-V1-standalone-loose")','I'),
    cutBasedMedium       = cms.vstring('userInt("cutBasedElectronID-Spring15-25ns-V1-standalone-medium")','I'),
    cutBasedTight        = cms.vstring('userInt("cutBasedElectronID-Spring15-25ns-V1-standalone-tight")','I'),
    mvaNonTrigWP90       = cms.vstring('userInt("mvaEleID-Spring15-25ns-nonTrig-V1-wp90")','I'),
    mvaNonTrigWP80       = cms.vstring('userInt("mvaEleID-Spring15-25ns-nonTrig-V1-wp80")','I'),
    mvaTrigWP90          = cms.vstring('userInt("mvaEleID-Spring15-25ns-Trig-V1-wp90")','I'),
    mvaTrigWP80          = cms.vstring('userInt("mvaEleID-Spring15-25ns-Trig-V1-wp80")','I'),
    mvaNonTrigValues     = cms.vstring('userFloat("ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values")','F'),
    mvaTrigValues        = cms.vstring('userFloat("ElectronMVAEstimatorRun2Spring15Trig25nsV1Values")','F'),
    mvaNonTrigCategories = cms.vstring('userInt("ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories")','I'),
    mvaTrigCategories    = cms.vstring('userInt("ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories")','I'),

)


def addElectrons(process, coll, **kwargs):
    isMC = kwargs.pop('isMC', False)
    eSrc = coll['electrons']
    pvSrc = coll['vertices']
    # customization path
    process.electronCustomization = cms.Path()

    ###################################
    ### scale and smear corrections ###
    ###################################
    #process.load('EgammaAnalysis.ElectronTools.calibratedElectronsRun2_cfi')
    #process.calibratedPatElectrons.electrons = eSrc
    #process.calibratedPatElectrons.isMC = isMC
    #process.electronCustomization *= process.calibratedPatElectrons
    #eSrc = 'calibratedPatElectrons'

    ######################
    ### embed gap info ###
    ######################
    process.eGI = cms.EDProducer(
        "ElectronGapInfoEmbedder",
        src = cms.InputTag(eSrc),
    )
    eSrc = 'eGI'
    process.electronCustomization *= process.eGI

    #################
    ### embed VID ###
    #################
    from PhysicsTools.SelectorUtils.tools.vid_id_tools import switchOnVIDElectronIdProducer, setupAllVIDIdsInModule, DataFormat, setupVIDElectronSelection
    switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
    
    # define which IDs we want to produce
    my_id_modules = [
        'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff',
        'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff',
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring15_25ns_nonTrig_V1_cff',
        'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring15_25ns_Trig_V1_cff',
    ]
    
    # add them to the VID producer
    for idmod in my_id_modules:
        setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

    # update the collection
    process.egmGsfElectronIDs.physicsObjectSrc = cms.InputTag(eSrc)
    process.electronMVAValueMapProducer.srcMiniAOD = cms.InputTag(eSrc)
    process.electronRegressionValueMapProducer.srcMiniAOD = cms.InputTag(eSrc)

    idDecisionLabels = [
        'cutBasedElectronID-Spring15-25ns-V1-standalone-veto',
        'cutBasedElectronID-Spring15-25ns-V1-standalone-loose',
        'cutBasedElectronID-Spring15-25ns-V1-standalone-medium',
        'cutBasedElectronID-Spring15-25ns-V1-standalone-tight',
        'heepElectronID-HEEPV60',
        'mvaEleID-Spring15-25ns-nonTrig-V1-wp80',
        'mvaEleID-Spring15-25ns-nonTrig-V1-wp90',
        'mvaEleID-Spring15-25ns-Trig-V1-wp90',
        'mvaEleID-Spring15-25ns-Trig-V1-wp80',
    ]
    idDecisionTags = [
        cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-veto'),
        cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-loose'),
        cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-medium'),
        cms.InputTag('egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-V1-standalone-tight'),
        cms.InputTag('egmGsfElectronIDs:heepElectronID-HEEPV60'),
        cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp80'),
        cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring15-25ns-nonTrig-V1-wp90'),
        cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring15-25ns-Trig-V1-wp90'),
        cms.InputTag('egmGsfElectronIDs:mvaEleID-Spring15-25ns-Trig-V1-wp80'),
    ]
    mvaValueLabels = [
        #"ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values",
        #"ElectronMVAEstimatorRun2Spring15Trig25nsV1Values",
    ]
    mvaValueTags = [
        #cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        #cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
    ]
    mvaCategoryLabels = [
        #"ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories",
        #"ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories",
    ]
    mvaCategoryTags = [
        #cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        #cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
    ]

    process.eidEmbedder = cms.EDProducer(
        "ElectronVIDEmbedder",
        src=cms.InputTag(eSrc),
        idLabels = cms.vstring(*idDecisionLabels),        # labels for bool maps
        ids = cms.VInputTag(*idDecisionTags),             # bool maps
        valueLabels = cms.vstring(*mvaValueLabels),       # labels for float maps
        values = cms.VInputTag(*mvaValueTags),            # float maps
        categoryLabels = cms.vstring(*mvaCategoryLabels), # labels for int maps
        categories = cms.VInputTag(*mvaCategoryTags),     # int maps
    )
    eSrc = 'eidEmbedder'
    process.electronCustomization *= process.egmGsfElectronIDSequence
    process.electronCustomization *= process.eidEmbedder

    ##########################
    ### embed missing hits ###
    ##########################
    process.eMH = cms.EDProducer(
        "ElectronMissingHitsEmbedder",
        src = cms.InputTag(eSrc),
    )
    eSrc = 'eMH'
    process.electronCustomization *= process.eMH

    #############################
    ### embed effective areas ###
    #############################
    eaFile = 'RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'
    process.eEffArea = cms.EDProducer(
        "ElectronEffectiveAreaEmbedder",
        src = cms.InputTag(eSrc),
        label = cms.string("EffectiveArea"), # embeds a user float with this name
        configFile = cms.FileInPath(eaFile), # the effective areas file
    )
    eSrc = 'eEffArea'
    process.electronCustomization *= process.eEffArea

    ################
    ### embed pv ###
    ################
    process.ePV = cms.EDProducer(
        "ElectronPVEmbedder",
        src = cms.InputTag(eSrc),
        vertexSrc = cms.InputTag(pvSrc),
    )
    eSrc = 'ePV'
    process.electronCustomization *= process.ePV

    ##############################
    ### embed trigger matching ###
    ##############################
    process.eTrig = cms.EDProducer(
        "ElectronHLTMatchEmbedder",
        src = cms.InputTag(eSrc),
        triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
        triggerObjects = cms.InputTag("selectedPatTrigger"),
        deltaR = cms.double(0.5),
        labels = cms.vstring(
        ),
        paths = cms.vstring(
        ),
    )
    eSrc = 'eTrig'
    process.electronCustomization *= process.eTrig

    # add to schedule
    process.schedule.append(process.electronCustomization)
    coll['electrons'] = eSrc
    return coll
