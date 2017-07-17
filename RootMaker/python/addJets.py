import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import commonJetTauBranches

################################################
################################################
################################################
jetBranches = commonJetTauBranches.clone(
    area = cms.vstring('jetArea','F'),

    # user data embedded with BtagEmbedder
    # pfCombinedInclusiveSecondaryVertexV2BJetTags
    btag_passCSVv2L  = cms.vstring('? bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.5426 ? 1 : 0','I'),
    btag_passCSVv2M  = cms.vstring('? bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.8484 ? 1 : 0','I'),
    btag_passCSVv2T  = cms.vstring('? bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.9535 ? 1 : 0','I'),
    # pfCombinedMVAV2BJetTags
    btag_passCMVAv2L = cms.vstring('? bDiscriminator("pfCombinedMVAV2BJetTags") > -0.5884 ? 1 : 0','I'),
    btag_passCMVAv2M = cms.vstring('? bDiscriminator("pfCombinedMVAV2BJetTags") > 0.4432 ? 1 : 0','I'),
    btag_passCMVAv2T = cms.vstring('? bDiscriminator("pfCombinedMVAV2BJetTags") > 0.9432 ? 1 : 0','I'),

    # user data embedded from JetShiftEmbedder
    #pt_Down = cms.vstring('userFloat("pt_Down")','F'),
    #pt_Up   = cms.vstring('userFloat("pt_Up")','F'),

    # user data embedded from JetIDEmbedder
    is_loose        = cms.vstring('userInt("idLoose")','I'),
    is_tight        = cms.vstring('userInt("idTight")','I'),
    is_tightLepVeto = cms.vstring('userInt("idTightLepVeto")','I'),
    #jpumva          = cms.vstring('userFloat("jpumva")','F'),
    #mva             = cms.vstring('userFloat("mva")','F'),
    #puid_loose      = cms.vstring('userInt("puid_loose")','I'),
    #puid_medium     = cms.vstring('userInt("puid_medium")','I'),
    #puid_tight      = cms.vstring('userInt("puid_tight")','I'),

    ## energy shifts
    #pt_jetEnUp       = cms.vstring('? hasUserCand("JetEnUp") ? userCand("JetEnUp").pt() : 0','F'),
    #energy_jetEnUp   = cms.vstring('? hasUserCand("JetEnUp") ? userCand("JetEnUp").energy() : 0','F'),
    #pt_jetEnDown     = cms.vstring('? hasUserCand("JetEnDown") ? userCand("JetEnDown").pt() : 0','F'),
    #energy_jetEnDown = cms.vstring('? hasUserCand("JetEnDown") ? userCand("JetEnDown").energy() : 0 ','F'),

)


################################################
### produce jet collection #####################
################################################
def addJets(process, coll, **kwargs):
# note: jet cleaning is defined in RootTree.py
    runP = kwargs.pop('runP', 'NA')
    isMC = kwargs.pop('isMC', False)
    jSrc = coll['ak4pfchsjets']
    pvSrc = coll['vertices']
    genSrc = coll['prunedgen']
    packedSrc = coll['packed']
    # customization path
    process.jetCustomization = cms.Path()


    ####################
    #### recorrect jets
    ####################
    levels = ['L1FastJet',
              'L2Relative',
              'L3Absolute']
    if not isMC: levels.append('L2L3Residual')


    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJetCorrFactors
    process.patJetCorrFactorsReapplyJEC = updatedPatJetCorrFactors.clone(
        src = cms.InputTag(jSrc),
        levels = levels,
        payload = 'AK4PFchs' 
    )
    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJets
    process.patJetsReapplyJEC = updatedPatJets.clone(
        jetSource = cms.InputTag(jSrc),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag('patJetCorrFactorsReapplyJEC'))
    )
    process.jetCustomization *= process.patJetCorrFactorsReapplyJEC
    process.jetCustomization *= process.patJetsReapplyJEC
    jSrc = 'patJetsReapplyJEC'

    # embed ids
    process.jID = cms.EDProducer(
        'JetIDEmbedder',
        src = cms.InputTag(jSrc),
    )
    process.jetCustomization *= process.jID
    jSrc = 'jID'

    ## embed pt shifts
    #jecUncDataFile_ = 'RootMaker/RootMaker/data/'
    #if isMC:
    #    jecUncDataFile_ += 'Summer16_23Sep2016V4_MC_Uncertainty_AK4PFchs.txt'
    #elif runP in ['B','C','D']:
    #    jecUncDataFile_ += 'Summer16_23Sep2016BCDV4_DATA_Uncertainty_AK4PFchs.txt'
    #elif runP in ['E','F']:
    #    jecUncDataFile_ += 'Summer16_23Sep2016EFV4_DATA_Uncertainty_AK4PFchs.txt'
    #elif runP in ['G']:
    #    jecUncDataFile_ += 'Summer16_23Sep2016GV4_DATA_Uncertainty_AK4PFchs.txt'
    #else:
    #    jecUncDataFile_ += 'Summer16_23Sep2016HV4_DATA_Uncertainty_AK4PFchs.txt'

    #process.jShift = cms.EDProducer(
    #    'JetShiftEmbedder',
    #    src = cms.InputTag(jSrc),
    #    jecUncDataFile = cms.FileInPath(jecUncDataFile_),
    #)
    #jSrc = 'jShift'
    #process.jetCustomization *= process.jShift

    #process.load('RecoJets.JetProducers.PileupJetID_cfi')
    #process.jpuID = process.pileupJetId.clone(
    #    jets=cms.InputTag(jSrc),
    #    inputIsCorrected=True,
    #    applyJec=True,
    #    vertexes=cms.InputTag(pvSrc)
    #)

    #process.jetCustomization *= process.jpuID
    #jSrc = 'jpuID'

    ## embed gen jets
    #if isMC:
    #    process.jGenJet = cms.EDProducer(
    #        'JetMatchedGenJetEmbedder',
    #        src = cms.InputTag(jSrc),
    #        genJets = cms.InputTag('slimmedGenJets'),
    #        srcIsTaus = cms.bool(False),
    #        deltaR = cms.double(0.5),
    #    )
    #    jSrc = 'jGenJet'
    #    process.jetCustomization *= process.jGenJet


    # add to schedule
    process.schedule.append(process.jetCustomization)
    coll['ak4pfchsjets'] = jSrc
    return coll
