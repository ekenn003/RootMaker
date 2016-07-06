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

    # raw values of isolation
    neutralIsoPtSumWeight = cms.vstring('tauID("neutralIsoPtSumWeight")','F'),
    footprintCorrection   = cms.vstring('tauID("footprintCorrection")','F'),
    puCorrPtSum           = cms.vstring('tauID("puCorrPtSum")','F'),
    photonPtSumOutsideSignalCone = cms.vstring('tauID("photonPtSumOutsideSignalCone")','F'),
    neutralIsoPtSum              = cms.vstring('tauID("neutralIsoPtSum")','F'),
    chargedIsoPtSum              = cms.vstring('tauID("chargedIsoPtSum")','F'),

    # tau discriminators
    # against electron mva6
    tdisc_againstElectronVLooseMVA6   = cms.vstring('tauID("againstElectronVLooseMVA6")','I'),
    tdisc_againstElectronLooseMVA6    = cms.vstring('tauID("againstElectronLooseMVA6")','I'),
    tdisc_againstElectronMediumMVA6   = cms.vstring('tauID("againstElectronMediumMVA6")','I'),
    tdisc_againstElectronTightMVA6    = cms.vstring('tauID("againstElectronTightMVA6")','I'),
    tdisc_againstElectronVTightMVA6   = cms.vstring('tauID("againstElectronVTightMVA6")','I'),
    tdisc_againstElectronMVA6category = cms.vstring('tauID("againstElectronMVA6category")','I'),
    tdisc_againstElectronMVA6raw      = cms.vstring('tauID("againstElectronMVA6Raw")','F'),
    # against muon
    tdisc_againstMuonLoose3 = cms.vstring('tauID("againstMuonLoose3")','I'),
    tdisc_againstMuonTight3 = cms.vstring('tauID("againstMuonTight3")','I'),
    ## pileup weighted cut-based isolation discriminators
    #tdisc_byLoosePileupWeightedIsolation3Hits  = cms.vstring('tauID("byLoosePileupWeightedIsolation3Hits")','I'),
    #tdisc_byMediumPileupWeightedIsolation3Hits = cms.vstring('tauID("byMediumPileupWeightedIsolation3Hits")','I'),
    #tdisc_byTightPileupWeightedIsolation3Hits  = cms.vstring('tauID("byTightPileupWeightedIsolation3Hits")','I'),
    # combined isolation dB corr 3 hits
    tdisc_byLooseCombinedIsolationDeltaBetaCorr3Hits  = cms.vstring('tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits")','I'),
    tdisc_byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.vstring('tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits")', 'I'),
    tdisc_byTightCombinedIsolationDeltaBetaCorr3Hits  = cms.vstring('tauID("byTightCombinedIsolationDeltaBetaCorr3Hits")','I'),
    tdisc_byCombinedIsolationDeltaBetaCorrRaw3Hits    = cms.vstring('tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits")','I'),
    ## New Tau Isolation Discriminators with cone size DeltaR = 0.3 7_6_x
    #tdisc_byLooseCombinedIsolationDeltaBetaCorr3HitsdR03  = cms.vstring('tauID("byLooseCombinedIsolationDeltaBetaCorr3HitsdR03")','I'),
    #tdisc_byMediumCombinedIsolationDeltaBetaCorr3HitsdR03 = cms.vstring('tauID("byMediumCombinedIsolationDeltaBetaCorr3HitsdR03")', 'I'),
    #tdisc_byTightCombinedIsolationDeltaBetaCorr3HitsdR03  = cms.vstring('tauID("byTightCombinedIsolationDeltaBetaCorr3HitsdR03")','I'),
    ## BDT based tau ID discriminator based on isolation Pt sums plus tau lifetime information, trained on 1-prong, "2-prong" and 3-prong tau candidates 
    #tdisc_byVLooseIsolationMVA3newDMwLT  = cms.vstring('tauID("byVLooseIsolationMVA3newDMwLT")','I'),
    #tdisc_byLooseIsolationMVA3newDMwLT   = cms.vstring('tauID("byLooseIsolationMVA3newDMwLT")','I'),
    #tdisc_byMediumIsolationMVA3newDMwLT  = cms.vstring('tauID("byMediumIsolationMVA3newDMwLT")', 'I'),
    #tdisc_byTightIsolationMVA3newDMwLT   = cms.vstring('tauID("byTightIsolationMVA3newDMwLT")','I'),
    #tdisc_byVTightIsolationMVA3newDMwLT  = cms.vstring('tauID("byVTightIsolationMVA3newDMwLT")', 'I'),
    #tdisc_byVVTightIsolationMVA3newDMwLT = cms.vstring('tauID("byVVTightIsolationMVA3newDMwLT")', 'I'),
    #tdisc_byIsolationMVA3newDMwLTraw     = cms.vstring('tauID("byIsolationMVA3newDMwLTRaw")','F'),
    ## BDT based tau ID discriminator based on isolation Pt sums plus tau lifetime information, trained on 1-prong and 3-prong tau candidates 
    #tdisc_byVLooseIsolationMVA3oldDMwLT  = cms.vstring('tauID("byVLooseIsolationMVA3oldDMwLT")', 'I'),
    #tdisc_byLooseIsolationMVA3oldDMwLT   = cms.vstring('tauID("byLooseIsolationMVA3oldDMwLT")', 'I'),
    #tdisc_byMediumIsolationMVA3oldDMwLT  = cms.vstring('tauID("byMediumIsolationMVA3oldDMwLT")', 'I'),
    #tdisc_byTightIsolationMVA3oldDMwLT   = cms.vstring('tauID("byTightIsolationMVA3oldDMwLT")', 'I'),
    #tdisc_byVTightIsolationMVA3oldDMwLT  = cms.vstring('tauID("byVTightIsolationMVA3oldDMwLT")', 'I'),
    #tdisc_byVVTightIsolationMVA3oldDMwLT = cms.vstring('tauID("byVVTightIsolationMVA3oldDMwLT")','I'),
    #tdisc_byIsolationMVA3oldDMwLTraw     = cms.vstring('tauID("byIsolationMVA3oldDMwLTRaw")', 'F'),
    # With Old Decay Mode reconstruction:
    tdisc_byLooseIsolationMVArun2v1DBoldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1DBoldDMwLT")','I'),
    tdisc_byMediumIsolationMVArun2v1DBoldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1DBoldDMwLT")','I'),
    tdisc_byTightIsolationMVArun2v1DBoldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1DBoldDMwLT")','I'),
    tdisc_byVTightIsolationMVArun2v1DBoldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1DBoldDMwLT")','I'),
    # Same but with Iso dR = 0.3
    tdisc_byLooseIsolationMVArun2v1DBdR03oldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    tdisc_byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    tdisc_byTightIsolationMVArun2v1DBdR03oldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    tdisc_byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1DBdR03oldDMwLT")','I'),
    # With New Decay Mode Reconstruction:
    tdisc_byLooseIsolationMVArun2v1DBnewDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1DBnewDMwLT")','I'),
    tdisc_byMediumIsolationMVArun2v1DBnewDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1DBnewDMwLT")','I'),
    tdisc_byTightIsolationMVArun2v1DBnewDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1DBnewDMwLT")','I'),
    tdisc_byVTightIsolationMVArun2v1DBnewDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1DBnewDMwLT")','I'),
    # With Old Decay Mode reconstruction:
    tdisc_byLooseIsolationMVArun2v1PWoldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1PWoldDMwLT")','I'),
    tdisc_byMediumIsolationMVArun2v1PWoldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1PWoldDMwLT")','I'),
    tdisc_byTightIsolationMVArun2v1PWoldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1PWoldDMwLT")','I'),
    tdisc_byVTightIsolationMVArun2v1PWoldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1PWoldDMwLT")','I'),
    # Same but with Iso dR = 0.3
    tdisc_byLooseIsolationMVArun2v1PWdR03oldDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    tdisc_byMediumIsolationMVArun2v1PWdR03oldDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    tdisc_byTightIsolationMVArun2v1PWdR03oldDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    tdisc_byVTightIsolationMVArun2v1PWdR03oldDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1PWdR03oldDMwLT")','I'),
    # With New Decay Mode Reconstruction:
    tdisc_byLooseIsolationMVArun2v1PWnewDMwLT  = cms.vstring('tauID("byLooseIsolationMVArun2v1PWnewDMwLT")','I'),
    tdisc_byMediumIsolationMVArun2v1PWnewDMwLT = cms.vstring('tauID("byMediumIsolationMVArun2v1PWnewDMwLT")','I'),
    tdisc_byTightIsolationMVArun2v1PWnewDMwLT  = cms.vstring('tauID("byTightIsolationMVArun2v1PWnewDMwLT")','I'),
    tdisc_byVTightIsolationMVArun2v1PWnewDMwLT = cms.vstring('tauID("byVTightIsolationMVArun2v1PWnewDMwLT")','I'),
    # DecayModeFinding
    tdisc_decayModeFinding       = cms.vstring('tauID("decayModeFinding")','I'),
    tdisc_decayModeFindingNewDMs = cms.vstring('tauID("decayModeFindingNewDMs")','I'),
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
