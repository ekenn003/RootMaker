import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import commonJetTauBranches

tauBranches = commonJetTauBranches.clone(
    # user data embedded from PVEmbedder
    dz  = cms.vstring('userFloat("dz")','F'),
    dzerr  = cms.vstring('dzError','F'),
    dxy = cms.vstring('userFloat("dxy")','F'),
    dxyerr = cms.vstring('dxyError','F'),
    # user data from HLTMatchEmbedder
    trigger = cms.vstring('userInt("trigger")','I'), 

    # isolation
    isolationneutralspt  = cms.vstring('tauID("neutralIsoPtSum")','F'),
    isolationneutralsnum = cms.vstring('? (isPFTau) ? isolationPFNeutrHadrCands().size() : -1','I'),
    isolationchargedpt   = cms.vstring('tauID("chargedIsoPtSum")','F'),
    isolationchargednum  = cms.vstring('? (isPFTau) ? isolationPFChargedHadrCands().size() : -1','I'),
    isolationgammapt     = cms.vstring('tauID("photonPtSumOutsideSignalCone")','F'),
    isolationgammanum    = cms.vstring('? (isPFTau) ? isolationPFGammaCands().size() : -1','I'),

    # tau ids
    againstElectronVLooseMVA5   = cms.vstring('tauID("againstElectronVLooseMVA5")','I'), 
    againstElectronLooseMVA5    = cms.vstring('tauID("againstElectronLooseMVA5")','I'),
    againstElectronMediumMVA5   = cms.vstring('tauID("againstElectronMediumMVA5")','I'),
    againstElectronTightMVA5    = cms.vstring('tauID("againstElectronTightMVA5")','I'),
    againstElectronVTightMVA5   = cms.vstring('tauID("againstElectronVTightMVA5")','I'),
    againstElectronMVA5category = cms.vstring('tauID("againstElectronMVA5category")','I'),
    againstElectronMVA5raw      = cms.vstring('tauID("againstElectronMVA5raw")','F'),
    # mva6
    againstElectronVLooseMVA6   = cms.vstring('tauID("againstElectronVLooseMVA6")','I'),
    againstElectronLooseMVA6    = cms.vstring('tauID("againstElectronLooseMVA6")','I'),
    againstElectronMediumMVA6   = cms.vstring('tauID("againstElectronMediumMVA6")','I'),
    againstElectronTightMVA6    = cms.vstring('tauID("againstElectronTightMVA6")','I'),
    againstElectronVTightMVA6   = cms.vstring('tauID("againstElectronVTightMVA6")','I'),
    againstElectronMVA6category = cms.vstring('tauID("againstElectronMVA6category")','I'),
    againstElectronMVA6raw      = cms.vstring('tauID("againstElectronMVA6raw")','F'),
    # against muon
    againstMuonLoose3 = cms.vstring('tauID("againstMuonLoose3")','I'),
    againstMuonTight3 = cms.vstring('tauID("againstMuonTight3")','I'),
    #  PileupWeighted cut-based isolation discriminators
    byLoosePileupWeightedIsolation3Hits  = cms.vstring('tauID("byLoosePileupWeightedIsolation3Hits")','I'),
    byMediumPileupWeightedIsolation3Hits = cms.vstring('tauID("byMediumPileupWeightedIsolation3Hits")','I'),
    byTightPileupWeightedIsolation3Hits  = cms.vstring('tauID("byTightPileupWeightedIsolation3Hits")','I'),
    # raw values of the isolation
    byPileupWeightedIsolationRaw3Hits = cms.vstring('tauID("byPileupWeightedIsolationRaw3Hits")','I'),
    neutralIsoPtSumWeight             = cms.vstring('tauID("neutralIsoPtSumWeight")','F'),
    footprintCorrection               = cms.vstring('tauID("footprintCorrection")','F'),
    puCorrPtSum                                     = cms.vstring('tauID("puCorrPtSum")','F'),
    # combined isolation DB corr 3 hits
    byLooseCombinedIsolationDeltaBetaCorr3Hits  = cms.vstring('tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits")','I'),
    byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.vstring('tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits")', 'I'),
    byTightCombinedIsolationDeltaBetaCorr3Hits  = cms.vstring('tauID("byTightCombinedIsolationDeltaBetaCorr3Hits")','I'),
    byCombinedIsolationDeltaBetaCorrRaw3Hits    = cms.vstring('tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits")','I'),
    # New Tau Isolation Discriminators with cone size DeltaR = 0.3 7_6_x
    byLooseCombinedIsolationDeltaBetaCorr3HitsdR03  = cms.vstring('tauID("byLooseCombinedIsolationDeltaBetaCorr3HitsdR03")','I'),
    byMediumCombinedIsolationDeltaBetaCorr3HitsdR03 = cms.vstring('tauID("byMediumCombinedIsolationDeltaBetaCorr3HitsdR03")', 'I'),
    byTightCombinedIsolationDeltaBetaCorr3HitsdR03  = cms.vstring('tauID("byTightCombinedIsolationDeltaBetaCorr3HitsdR03")','I'),
    # BDT based tau ID discriminator based on isolation Pt sums plus tau lifetime information, trained on 1-prong, "2-prong" and 3-prong tau candidates 
    byVLooseIsolationMVA3newDMwLT  = cms.vstring('tauID("byVLooseIsolationMVA3newDMwLT")','I'),
    byLooseIsolationMVA3newDMwLT   = cms.vstring('tauID("byLooseIsolationMVA3newDMwLT")','I'),
    byMediumIsolationMVA3newDMwLT  = cms.vstring('tauID("byMediumIsolationMVA3newDMwLT")', 'I'),
    byTightIsolationMVA3newDMwLT   = cms.vstring('tauID("byTightIsolationMVA3newDMwLT")','I'),
    byVTightIsolationMVA3newDMwLT  = cms.vstring('tauID("byVTightIsolationMVA3newDMwLT")', 'I'),
    byVVTightIsolationMVA3newDMwLT = cms.vstring('tauID("byVVTightIsolationMVA3newDMwLT")', 'I'),
    byIsolationMVA3newDMwLTraw     = cms.vstring('tauID("byIsolationMVA3newDMwLTraw")','F'),
    # BDT based tau ID discriminator based on isolation Pt sums plus tau lifetime information, trained on 1-prong and 3-prong tau candidates 
    byVLooseIsolationMVA3oldDMwLT  = cms.vstring('tauID("byVLooseIsolationMVA3oldDMwLT")', 'I'),
    byLooseIsolationMVA3oldDMwLT   = cms.vstring('tauID("byLooseIsolationMVA3oldDMwLT")', 'I'),
    byMediumIsolationMVA3oldDMwLT  = cms.vstring('tauID("byMediumIsolationMVA3oldDMwLT")', 'I'),
    byTightIsolationMVA3oldDMwLT   = cms.vstring('tauID("byTightIsolationMVA3oldDMwLT")', 'I'),
    byVTightIsolationMVA3oldDMwLT  = cms.vstring('tauID("byVTightIsolationMVA3oldDMwLT")', 'I'),
    byVVTightIsolationMVA3oldDMwLT = cms.vstring('tauID("byVVTightIsolationMVA3oldDMwLT")','I'),
    byIsolationMVA3oldDMwLTraw     = cms.vstring('tauID("byIsolationMVA3oldDMwLTraw")', 'F'),
    # MVA based tau isolation discriminators new 7_6_x
    # With Old Decay Mode reconstruction:
    byLooseIsolationMVArun2v1DBoldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1DBoldDMwLT")','I'),
    byMediumIsolationMVArun2v1DBoldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1DBoldDMwLT")','I'),
    byTightIsolationMVArun2v1DBoldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1DBoldDMwLT")','I'),
    byVTightIsolationMVArun2v1DBoldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1DBoldDMwLT")','I'),
    # Same but with Iso dR = 0.3
    byLooseIsolationMVArun2v1DBdR03oldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    byTightIsolationMVArun2v1DBdR03oldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    #With New Decay Mode Reconstruction:
    byLooseIsolationMVArun2v1DBnewDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1DBnewDMwLT")','I'),
    byMediumIsolationMVArun2v1DBnewDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1DBnewDMwLT")','I'),
    byTightIsolationMVArun2v1DBnewDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1DBnewDMwLT")','I'),
    byVTightIsolationMVArun2v1DBnewDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1DBnewDMwLT")','I'),
    #MVA tau ID using Pileup Weighted isolation: new 7_6_x
    #With Old Decay Mode reconstruction:
    byLooseIsolationMVArun2v1PWoldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1PWoldDMwLT")','I'),
    byMediumIsolationMVArun2v1PWoldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1PWoldDMwLT")','I'),
    byTightIsolationMVArun2v1PWoldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1PWoldDMwLT")','I'),
    byVTightIsolationMVArun2v1PWoldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1PWoldDMwLT")','I'),
    # Same but with Iso dR = 0.3
    byLooseIsolationMVArun2v1PWdR03oldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    byMediumIsolationMVArun2v1PWdR03oldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    byTightIsolationMVArun2v1PWdR03oldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    byVTightIsolationMVArun2v1PWdR03oldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    #With New Decay Mode Reconstruction:
    byLooseIsolationMVArun2v1PWnewDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1PWnewDMwLT")','I'),
    byMediumIsolationMVArun2v1PWnewDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1PWnewDMwLT")','I'),
    byTightIsolationMVArun2v1PWnewDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1PWnewDMwLT")','I'),
    byVTightIsolationMVArun2v1PWnewDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1PWnewDMwLT")','I'),
    # DecayModeFinding
    decayModeFinding       = cms.vstring('tauID("decayModeFinding")','I'),
    decayModeFindingNewDMs = cms.vstring('tauID("decayModeFindingNewDMs")','I'),

)

def addTaus(process,coll,**kwargs):
    isMC = kwargs.pop('isMC', False)
    tSrc = coll['taus']
    pvSrc = coll['vertices']
    genSrc = coll['genParticles']

    # customization path
    process.tauCustomization = cms.Path()

    ################
    ### embed pv ###
    ################
    process.tPV = cms.EDProducer(
        "TauPVEmbedder",
        src = cms.InputTag(tSrc),
        vertexSrc = cms.InputTag(pvSrc),
    )
    tSrc = 'tPV'

    process.tauCustomization *= process.tPV

    ##############################
    ### embed trigger matching ###
    ##############################
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



    ##########################
    ### embed gen tau jets ###
    ##########################
    if isMC:
        from PhysicsTools.JetMCAlgos.TauGenJets_cfi import tauGenJets
        process.tauGenJets = tauGenJets.clone(GenParticles = cms.InputTag(genSrc))
        process.tauCustomization *= process.tauGenJets

        process.tGenJetMatching = cms.EDProducer(
            "TauGenJetEmbedder",
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
