import FWCore.ParameterSet.Config as cms

################################################
### gen particles branches #####################
################################################
genParticleBranches = cms.PSet(
    e      = cms.vstring('energy','F'),
    px     = cms.vstring('px','F'),
    py     = cms.vstring('py','F'),
    pz     = cms.vstring('pz','F'),
    vx     = cms.vstring('vx','F'),
    vy     = cms.vstring('vy','F'),
    vz     = cms.vstring('vz','F'),
    pdgid  = cms.vstring('pdgId','I'),
    status = cms.vstring('status','I'),

#indirectmother
#info
#motherbeg
#daughterbeg
#mother_count
#mothers
#daughter_count
#daughters

    numberOfDaughters      = cms.vstring('numberOfDaughters()','I'),
    daughter_1             = cms.vstring('? numberOfDaughters()>0 ? daughter(0).pdgId() : 0','I'),
    daughter_2             = cms.vstring('? numberOfDaughters()>1 ? daughter(1).pdgId() : 0','I'),
    numberOfMothers        = cms.vstring('numberOfMothers()','I'),
    mother_1               = cms.vstring('? numberOfMothers()>0 ? mother(0).pdgId() : 0','I'),
    mother_2               = cms.vstring('? numberOfMothers()>1 ? mother(1).pdgId() : 0','I'),
    isPrompt               = cms.vstring('isPromptFinalState()','I'),
    isFromTau              = cms.vstring('isDirectPromptTauDecayProductFinalState()','I'),
    isPromptDecayed        = cms.vstring('isPromptDecayed()','I'),
    isFromHadron           = cms.vstring('statusFlags().isDirectHadronDecayProduct()','I'),
    fromHardProcess        = cms.vstring('fromHardProcessFinalState()','I'),
    fromHardProcessDecayed = cms.vstring('fromHardProcessDecayed()','I'),
    fromHardProcessTau     = cms.vstring('isDirectHardProcessTauDecayProductFinalState()','I'),
)

################################################
### gen jets branches ##########################
################################################
genJetBranches = cms.PSet(
    e  = cms.vstring('energy','F'),
    px = cms.vstring('px','F'),
    py = cms.vstring('py','F'),
    pz = cms.vstring('pz','F'),
    einvisible    = cms.vstring('invisibleEnergy()','F'),

    emEnergy      = cms.vstring('emEnergy()','F'),
    hadEnergy     = cms.vstring('hadEnergy()','F'),
    nConstituents = cms.vstring('nConstituents','I'),
)

################################################
### gen MET branches ###########################
################################################
# gen met is embedded in the regular slimmedMETs collection
genMETBranches = cms.PSet(
    ex  = cms.vstring('genMET().px()','F'),
    ey  = cms.vstring('genMET().py()','F'),
    phi = cms.vstring('genMET().phi()','F'),
)
