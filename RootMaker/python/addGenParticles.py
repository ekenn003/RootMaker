import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import genParticleBranches

################################################
################################################
################################################
genParticleBranches = commonGenBranches.clone(

)

genJetBranches = commonGenBranches.clone(
    emEnergy         = cms.vstring('emEnergy()','F'),
    hadEnergy        = cms.vstring('hadEnergy()','F'),
    invisibileEnergy = cms.vstring('invisibleEnergy()','F'),
    nConstituents    = cms.vstring('nConstituents','I'),
)


## add stuff here
