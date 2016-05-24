import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import commonJetTauBranches

################################################
### tau branches ###############################
################################################
tauBranches = commonJetTauBranches.clone(
    # user data embedded from PVEmbedder
    dz     = cms.vstring('userFloat("dz")','F'),
    dzerr  = cms.vstring('dzError','F'),
    dxy    = cms.vstring('userFloat("dxy")','F'),
    dxyerr = cms.vstring('dxyError','F'),
    # user data from HLTMatchEmbedder
    trigger = cms.vstring('userInt("trigger")','I'), 


    #jet_refisnonnull = cms.vstring('jetRef().isNonnull','I'),
    #jet_pfrefisnonnull = cms.vstring('pfJetRef().isNonnull','I'),
    #jet_e = cms.vstring('? (jetRef().isNonnull) ?  : -1','F'),
    #jet_px
    #jet_py
    #jet_pz
    #jet_hadronicenergy
    #jet_chargedhadronicenergy
    #jet_emenergy
    #jet_chargedemenergy
    #jet_chargedmulti
    #jet_neutralmulti

    # isolation
    isolationneutralspt  = cms.vstring('tauID("neutralIsoPtSum")','F'),
    isolationneutralsnum = cms.vstring('? (isPFTau) ? isolationPFNeutrHadrCands().size() : -1','I'),
    isolationchargedpt   = cms.vstring('tauID("chargedIsoPtSum")','F'),
    isolationchargednum  = cms.vstring('? (isPFTau) ? isolationPFChargedHadrCands().size() : -1','I'),
    isolationgammapt     = cms.vstring('tauID("photonPtSumOutsideSignalCone")','F'),
    isolationgammanum    = cms.vstring('? (isPFTau) ? isolationPFGammaCands().size() : -1','I'),

    # tau ids
    # user data from TauDiscEmbedder
    disc = cms.vstring('userInt("disc")','I'), 
    # raw values of the isolation
    neutralIsoPtSumWeight = cms.vstring('tauID("neutralIsoPtSumWeight")','F'),
    footprintCorrection   = cms.vstring('tauID("footprintCorrection")','F'),
    puCorrPtSum           = cms.vstring('tauID("puCorrPtSum")','F'),
)

################################################
### tau discriminators #########################
################################################
TauDiscriminators = cms.untracked.vstring(
    # mva5
    'againstElectronVLooseMVA5',
    'againstElectronLooseMVA5',
    'againstElectronMediumMVA5',
    'againstElectronTightMVA5',
    'againstElectronVTightMVA5',
    'againstElectronMVA5category',
    'againstElectronMVA5raw',
    # mva6
    'againstElectronVLooseMVA6',
    'againstElectronLooseMVA6',
    'againstElectronMediumMVA6',
    'againstElectronTightMVA6',
    'againstElectronVTightMVA6',
    'againstElectronMVA6category',
    'againstElectronMVA6raw',
    # against muon
    'againstMuonLoose3',
    'againstMuonTight3',
    # pileup-weighted cut-based isolation discriminators
    'byLoosePileupWeightedIsolation3Hits',
    'byMediumPileupWeightedIsolation3Hits',
    'byTightPileupWeightedIsolation3Hits',
    'byPileupWeightedIsolationRaw3Hits',
    # combined isolation DB corr 3 hits
    'byLooseCombinedIsolationDeltaBetaCorr3Hits',
    'byMediumCombinedIsolationDeltaBetaCorr3Hits',
    'byTightCombinedIsolationDeltaBetaCorr3Hits',
    'byCombinedIsolationDeltaBetaCorrRaw3Hits',
    # New Tau Isolation Discriminators with cone size DeltaR = 0.3 7_6_x
    'byLooseCombinedIsolationDeltaBetaCorr3HitsdR03',
    'byMediumCombinedIsolationDeltaBetaCorr3HitsdR03',
    'byTightCombinedIsolationDeltaBetaCorr3HitsdR03',
    # BDT based tau ID discriminator based on isolation Pt sums plus tau lifetime information, trained on 1-prong, "2-prong" and 3-prong tau candidates
    'byVLooseIsolationMVA3newDMwLT',
    'byLooseIsolationMVA3newDMwLT',
    'byMediumIsolationMVA3newDMwLT',
    'byTightIsolationMVA3newDMwLT',
    'byVTightIsolationMVA3newDMwLT',
    'byVVTightIsolationMVA3newDMwLT',
    'byIsolationMVA3newDMwLTraw',
    # BDT based tau ID discriminator based on isolation Pt sums plus tau lifetime information, trained on 1-prong and 3-prong tau candidates
    'byVLooseIsolationMVA3oldDMwLT',
    'byLooseIsolationMVA3oldDMwLT',
    'byMediumIsolationMVA3oldDMwLT',
    'byTightIsolationMVA3oldDMwLT',
    'byVTightIsolationMVA3oldDMwLT',
    'byVVTightIsolationMVA3oldDMwLT',
    'byIsolationMVA3oldDMwLTraw',
    # MVA based tau isolation discriminators new 7_6_x
    # With Old Decay Mode reconstruction:
    'byLooseIsolationMVArun2v1DBoldDMwLT',
    'byMediumIsolationMVArun2v1DBoldDMwLT',
    'byTightIsolationMVArun2v1DBoldDMwLT',
    'byVTightIsolationMVArun2v1DBoldDMwLT',
    # Same but with Iso dR = 0.3
    'byLooseIsolationMVArun2v1DBdR03oldDMwLT',
    'byMediumIsolationMVArun2v1DBdR03oldDMwLT',
    'byTightIsolationMVArun2v1DBdR03oldDMwLT',
    'byVTightIsolationMVArun2v1DBdR03oldDMwLT',
    #With New Decay Mode Reconstruction:
    'byLooseIsolationMVArun2v1DBnewDMwLT',
    'byMediumIsolationMVArun2v1DBnewDMwLT',
    'byTightIsolationMVArun2v1DBnewDMwLT',
    'byVTightIsolationMVArun2v1DBnewDMwLT',
    #MVA tau ID using Pileup Weighted isolation: new 7_6_x
    #With Old Decay Mode reconstruction:
    'byLooseIsolationMVArun2v1PWoldDMwLT',
    'byMediumIsolationMVArun2v1PWoldDMwLT',
    'byTightIsolationMVArun2v1PWoldDMwLT',
    'byVTightIsolationMVArun2v1PWoldDMwLT',
    # Same but with Iso dR = 0.3
    'byLooseIsolationMVArun2v1PWdR03oldDMwLT',
    'byMediumIsolationMVArun2v1PWdR03oldDMwLT',
    'byTightIsolationMVArun2v1PWdR03oldDMwLT',
    'byVTightIsolationMVArun2v1PWdR03oldDMwLT',
    #With New Decay Mode Reconstruction:
    'byLooseIsolationMVArun2v1PWnewDMwLT',
    'byMediumIsolationMVArun2v1PWnewDMwLT',
    'byTightIsolationMVArun2v1PWnewDMwLT',
    'byVTightIsolationMVArun2v1PWnewDMwLT',
    # DecayModeFinding
    'decayModeFinding',
    'decayModeFindingNewDMs',
)

################################################
### produce tau collection #####################
################################################
def addTaus(process,coll,**kwargs):
    isMC = kwargs.pop('isMC', False)
    tSrc = coll['taus']
    pvSrc = coll['vertices']
    genSrc = coll['prunedgen']
    # customization path
    process.tauCustomization = cms.Path()

    # embed pv
    process.tPV = cms.EDProducer(
        "TauPVEmbedder",
        src = cms.InputTag(tSrc),
        vertexSrc = cms.InputTag(pvSrc),
    )
    tSrc = 'tPV'
    process.tauCustomization *= process.tPV

    # embed tau discriminators
    process.tDisc = cms.EDProducer(
        "TauDiscEmbedder",
        src = cms.InputTag(tSrc),
        RecTauDiscriminators = cms.untracked.vstring(TauDiscriminators),
    )
    tSrc = 'tDisc'
    process.tauCustomization *= process.tDisc

    # embed trigger matching
    process.tTrig = cms.EDProducer(
        "TauHLTMatchEmbedder",
        src = cms.InputTag(tSrc),
        triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
        triggerObjects = cms.InputTag("selectedPatTrigger"),
        deltaR = cms.double(0.5),
        labels = cms.vstring(
        ),
        paths = cms.vstring(
        ),
    )
    tSrc = 'tTrig'
    process.tauCustomization *= process.tTrig

    # embed gen tau jets
    if isMC:
        from PhysicsTools.JetMCAlgos.TauGenJets_cfi import tauGenJets
        process.tauGenJets = tauGenJets.clone(GenParticles = cms.InputTag(genSrc))
        process.tauCustomization *= process.tauGenJets
        process.tGenJetMatching = cms.EDProducer(
            "TauMatchedGenJetEmbedder",
            src = cms.InputTag(tSrc),
            genJets = cms.InputTag("tauGenJets"),
            srcIsTaus = cms.bool(True),
            deltaR = cms.double(0.5),
        )
        tSrc = "tGenJetMatching"
        process.tauCustomization *= process.tGenJetMatching



    # add to schedule
    process.schedule.append(process.tauCustomization)
    coll['taus'] = tSrc
    return coll
