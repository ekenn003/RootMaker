import FWCore.ParameterSet.Config as cms

####################################################################################
### event HLT and filter matching ##################################################
### only for event matching! not individual objects. ###############################
####################################################################################
# trigger
triggerBranches = cms.PSet(
    # single muon
    #IsoMu20 = cms.PSet(
    #    path = cms.string('HLT_IsoMu20_v\\[0-9]+'),
    #),
    #IsoTkMu20 = cms.PSet(
    #    path = cms.string('HLT_IsoTkMu20_v\\[0-9]+'),
    #),
    #IsoMu22 = cms.PSet(
    #    path = cms.string('HLT_IsoMu22_v\\[0-9]+'),
    #),
    #IsoTkMu22 = cms.PSet(
    #    path = cms.string('HLT_IsoTkMu22_v\\[0-9]+'),
    #),
    IsoMu24 = cms.PSet(
        path = cms.string('HLT_IsoMu24_v\\[0-9]+'),
    ),
    IsoTkMu24 = cms.PSet(
        path = cms.string('HLT_IsoTkMu24_v\\[0-9]+'),
    ),
    IsoMu27 = cms.PSet(
        path = cms.string('HLT_IsoMu27_v\\[0-9]+'),
    ),
    IsoTkMu27 = cms.PSet(
        path = cms.string('HLT_IsoTkMu27_v\\[0-9]+'),
    ),
    # double muon
    Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ = cms.PSet(
        path = cms.string('HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v\\[0-9]+'),
    ),
    Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = cms.PSet(
        path = cms.string('HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v\\[0-9]+'),
    ),
)

# filters
filterBranches = cms.PSet(
    HBHENoiseFilter = cms.PSet(
        path = cms.string('Flag_HBHENoiseFilter'),
    ),
    HBHENoiseIsoFilter = cms.PSet(
        path = cms.string('Flag_HBHENoiseIsoFilter'),
    ),
    CSCTightHalo2015Filter = cms.PSet(
        path = cms.string('Flag_CSCTightHalo2015Filter'),
    ),
    EcalDeadCellTriggerPrimitiveFilter = cms.PSet(
        path = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    ),
    goodVertices = cms.PSet(
        path = cms.string('Flag_goodVertices'),
    ),
    eeBadScFilter = cms.PSet(
        path = cms.string('Flag_eeBadScFilter'),
    ),
)
