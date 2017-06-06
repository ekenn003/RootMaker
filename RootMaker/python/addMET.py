import FWCore.ParameterSet.Config as cms

################################################
### missing ET branches ########################
################################################
metBranches = cms.PSet(
    ex     = cms.vstring('px()','F'),
    ey     = cms.vstring('py()','F'),
    et     = cms.vstring('pt()','F'),
    phi    = cms.vstring('phi()','F'),
#    rawet  = cms.vstring('uncorPt','F'),
#    rawphi = cms.vstring('uncorPhi','F'),
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
    postfix = "New"
    from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
    runMetCorAndUncFromMiniAOD(process,
        jetCollUnskimmed="slimmedJets",
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

    metSrc = "slimmedMETs{0}".format(postfix)
    return coll
