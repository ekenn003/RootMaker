import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import commonJetTauBranches

################################################
################################################
################################################
jetBranches = commonJetTauBranches.clone(
    area = cms.vstring('jetArea','F'),

    # user data embedded with ??? these are all like -1 right now
    #energycorr      = cms.vstring('userFloat("energycorr")','F'),
    #energycorrl7uds = cms.vstring('userFloat("energycorrl7uds")','F'),
    #energycorrl7bottom = cms.vstring('userFloat("energycorrl7bottom")','F'),
    #energycorrunc   = cms.vstring('userFloat("energycorrunc")','F'),
    #mcflavour       = cms.vstring('userFloat("mcflavour")','F'),

    # user data embedded with BtagEmbedder


    # btagging
    btag_pfJetProbabilityBJetTags                     = cms.vstring('bDiscriminator("pfJetProbabilityBJetTags")','F'),
    btag_pfCombinedInclusiveSecondaryVertexV2BJetTags = cms.vstring('bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")','F'),
    btag_pfCombinedMVAV2BJetTags                      = cms.vstring('bDiscriminator("pfCombinedMVAV2BJetTags")','F'),

    btag_passJPL     = cms.vstring('? bDiscriminator("pfJetProbabilityBJetTags") > 0.245 ? 1 : 0','I'),
    btag_passJPM     = cms.vstring('? bDiscriminator("pfJetProbabilityBJetTags") > 0.515 ? 1 : 0','I'),
    btag_passJPT     = cms.vstring('? bDiscriminator("pfJetProbabilityBJetTags") > 0.760 ? 1 : 0','I'),
    # pfCombinedInclusiveSecondaryVertexV2BJetTags
    btag_passCSVv2L  = cms.vstring('? bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.5426 ? 1 : 0','I'),
    btag_passCSVv2M  = cms.vstring('? bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.8484 ? 1 : 0','I'),
    btag_passCSVv2T  = cms.vstring('? bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.9535 ? 1 : 0','I'),
    # pfCombinedMVAV2BJetTags
    btag_passCMVAv2L = cms.vstring('? bDiscriminator("pfCombinedMVAV2BJetTags") > -0.5884 ? 1 : 0','I'),
    btag_passCMVAv2M = cms.vstring('? bDiscriminator("pfCombinedMVAV2BJetTags") > 0.4432 ? 1 : 0','I'),
    btag_passCMVAv2T = cms.vstring('? bDiscriminator("pfCombinedMVAV2BJetTags") > 0.9432 ? 1 : 0','I'),

#    # energies
#    hadronicenergy        = cms.vstring('chargedHadronEnergy + neutralHadronEnergy','F'),
#    chargedhadronicenergy = cms.vstring('chargedHadronEnergy','F'),
#    emenergy              = cms.vstring('chargedEmEnergy + neutralEmEnergy','F'),
#    chargedemenergy       = cms.vstring('chargedEmEnergy','F'),
#    hfhadronicenergy      = cms.vstring('HFHadronEnergy','F'),
#    hfemenergy            = cms.vstring('HFEMEnergy','F'),
#    electronenergy        = cms.vstring('electronEnergy','F'),
#    muonenergy            = cms.vstring('muonEnergy','F'),
#    # multiplicities
#    chargedmulti    = cms.vstring('chargedMultiplicity','I'),
#    neutralmulti    = cms.vstring('neutralMultiplicity','I'),
#    hfhadronicmulti = cms.vstring('HFHadronMultiplicity','I'),
#    hfemmulti       = cms.vstring('HFEMMultiplicity','I'),
#    electronmulti   = cms.vstring('electronMultiplicity','I'),
#    muonmulti       = cms.vstring('muonMultiplicity','I'),
#    # energy fractions
#    neutralhadronenergyfraction = cms.vstring('neutralHadronEnergyFraction','F'),
#    neutralemenergyfraction     = cms.vstring('neutralEmEnergyFraction','F'),
#    chargedhadronenergyfraction = cms.vstring('chargedHadronEnergyFraction','F'),
#    muonenergyfraction          = cms.vstring('muonEnergyFraction','F'),
#    chargedemenergyfraction     = cms.vstring('chargedEmEnergyFraction','F'),

    # user data embedded from JetIDEmbedder
    is_loose        = cms.vstring('userInt("idLoose")','I'),
    is_tight        = cms.vstring('userInt("idTight")','I'),
    is_tightLepVeto = cms.vstring('userInt("idTightLepVeto")','I'),
    #jpumva          = cms.vstring('userFloat("jpumva")','F'),
    #mva             = cms.vstring('userFloat("mva")','F'),
    #puid_loose      = cms.vstring('userInt("puid_loose")','I'),
    #puid_medium     = cms.vstring('userInt("puid_medium")','I'),
    #puid_tight      = cms.vstring('userInt("puid_tight")','I'),

#    # user data embedded from JetShapeEmbedder
#    chargeda          = cms.vstring('userFloat("chargeda")','F'),
#    chargedb          = cms.vstring('userFloat("chargedb")','F'),
#    neutrala          = cms.vstring('userFloat("neutrala")','F'),
#    neutralb          = cms.vstring('userFloat("neutralb")','F'),
#    alla              = cms.vstring('userFloat("alla")','F'),
#    allb              = cms.vstring('userFloat("allb")', 'F'),
#    chargedfractionmv = cms.vstring('userFloat("chargedfractionmv")','F'),
)


################################################
### produce jet collection #####################
################################################
def addJets(process, coll, **kwargs):
# note: jet cleaning is defined in RootTree.py
    isMC = kwargs.pop('isMC', False)
    jSrc = coll['ak4pfchsjets']
    pvSrc = coll['vertices']
    genSrc = coll['prunedgen']
    packedSrc = coll['packed']
    # customization path
    process.jetCustomization = cms.Path()

    # recorrect jets
    ######################
    #####from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

    #####jetCorr = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')
    #####if isMC:
    #####    jetCorr = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None')
    #####updateJetCollection(
    #####    process,
    #####    jetSource = cms.InputTag(jSrc),
    #####    jetCorrections = jetCorr,
    #####)
    #####process.updatedPatJets.userData.userFloats.src += ['pileupJetIdUpdated:fullDiscriminant']
    #####jSrc = 'updatedPatJets'

    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJetCorrFactors
    process.patJetCorrFactorsReapplyJEC = updatedPatJetCorrFactors.clone(
        src = cms.InputTag(jSrc),
        levels = ['L1FastJet', 
                  'L2Relative', 
                  'L3Absolute'],
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

    #process.load('RecoJets.JetProducers.PileupJetID_cfi')
    #process.jpuID = process.pileupJetId.clone(
    #    jets=cms.InputTag(jSrc),
    #    inputIsCorrected=True,
    #    applyJec=True,
    #    vertexes=cms.InputTag(pvSrc)
    #)

    #process.jetCustomization *= process.jpuID
    #jSrc = 'jpuID'

    # embed shapes
    process.jShape = cms.EDProducer(
        'JetShapeEmbedder',
        src = cms.InputTag(jSrc),
        packedSrc = cms.InputTag(packedSrc),
    )
    process.jetCustomization *= process.jShape
    jSrc = 'jShape'

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
