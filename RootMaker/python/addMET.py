import FWCore.ParameterSet.Config as cms

################################################
### missing ET branches ########################
################################################
metBranches = cms.PSet(
    ex     = cms.vstring('px()','F'),
    ey     = cms.vstring('py()','F'),
    et     = cms.vstring('pt()','F'),
    phi    = cms.vstring('phi()','F'),

    ## shifts
#    et_jetResUp           = cms.vstring('userCand("JetResUp").pt()','F'),
#    et_jetResDown         = cms.vstring('userCand("JetResDown").pt()','F'),
#    et_jetEnUp            = cms.vstring('userCand("JetEnUp").pt()','F'),
#    et_jetEnDown          = cms.vstring('userCand("JetEnDown").pt()','F'),
#    et_muonEnUp           = cms.vstring('userCand("MuonEnUp").pt()','F'),
#    et_muonEnDown         = cms.vstring('userCand("MuonEnDown").pt()','F'),
)

################################################
### produce MET object #########################
################################################
def addMET(process, coll, **kwargs):
    isMC = kwargs.pop('isMC', False)
    metSrc = coll['pfmettype1']
    jSrc   = coll['ak4pfchsjets']
    pSrc   = coll['photons']
    eSrc   = coll['electrons']
    mSrc   = coll['muons']
    tSrc   = coll['taus']
    pfSrc  = coll['packed']
    # customization path
    process.metCustomization = cms.Path()

    #################################
    ### recompute met uncertainty ###
    #################################
    postfix = 'New'
    from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
    runMetCorAndUncFromMiniAOD(process,
        jetCollUnskimmed='slimmedJets',
        photonColl=pSrc,
        electronColl=eSrc,
        muonColl=mSrc,
        tauColl=tSrc,
        pfCandColl=pfSrc,
        isData=not isMC,
        postfix=postfix)

    # correct things to make it work
    getattr(process,'patPFMetTxyCorr{0}'.format(postfix)).vertexCollection = cms.InputTag('offlineSlimmedPrimaryVertices')
    del getattr(process,'slimmedMETs{0}'.format(postfix)).caloMET

    metSrc = 'slimmedMETs{0}'.format(postfix)


    ####################
    ### embed shifts ###
    ####################
    print '... Embedding shifts'
    for shift in ['JetRes','JetEn','MuonEn']:
        for sign in ['Up','Down']:
            mod = cms.EDProducer(
                'ShiftedMETEmbedder',
                src = cms.InputTag(metSrc),
                label = cms.string('{0}{1}'.format(shift,sign)),
                shiftedSrc = cms.InputTag('patPFMetT1{0}{1}{2}'.format(shift,sign,postfix)),
            )
            modName = 'embed{0}{1}'.format(shift,sign)
            setattr(process,modName,mod)
            metSrc = modName
            process.metCustomization += getattr(process,modName)



    for sign in ['Up','Down']:
        # muons
        shift = 'MuonEn'
        mod = cms.EDProducer(
            'ShiftedMuonEmbedder',
            src = cms.InputTag(mSrc),
            label = cms.string('{0}{1}'.format(shift,sign)),
            shiftedSrc = cms.InputTag('shiftedPat{0}{1}{2}'.format(shift,sign,postfix)),
        )
        modName = 'muonEmbed{0}{1}'.format(shift,sign)
        setattr(process,modName,mod)
        mSrc = modName
        process.metCustomization += getattr(process,modName)

        # jets
        shift = 'JetEn'
        mod = cms.EDProducer(
            'ShiftedJetEmbedder',
            src = cms.InputTag(jSrc),
            label = cms.string('{0}{1}'.format(shift,sign)),
            shiftedSrc = cms.InputTag('shiftedPat{0}{1}{2}'.format(shift,sign,postfix)),
        )
        modName = 'jetEmbed{0}{1}'.format(shift,sign)
        setattr(process,modName,mod)
        jSrc = modName
        process.metCustomization += getattr(process,modName)

    process.schedule.append(process.metCustomization)



    return coll
