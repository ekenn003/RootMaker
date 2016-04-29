import FWCore.ParameterSet.Config as cms

####################################################################################
### all objects have these branches ################################################
####################################################################################
commonBranches = cms.PSet(
    pt     = cms.vstring('pt()','F'),
    px     = cms.vstring('px()','F'),
    py     = cms.vstring('py()','F'),
    pz     = cms.vstring('pz()','F'),
    eta    = cms.vstring('eta()','F'),
    phi    = cms.vstring('phi()','F'),
    energy = cms.vstring('energy()','F'),
    charge = cms.vstring('charge()','F'),
    mass   = cms.vstring('mass()','F'),
    vz     = cms.vstring('vz()','F'),
    pdgid  = cms.vstring('pdgId()','I'),
)


#########################################################################
### electrons, muons, and photons additionally have these branches ######
#########################################################################
commonObjectBranches = commonBranches.clone(
    genMatch                  = cms.vstring('genParticleRef.isNonnull()','I'),
    genPdgId                  = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().pdgId() : 0', 'I'),
    genPt                     = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().pt() : 0', 'F'),
    genEta                    = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().eta() : 0', 'F'),
    genPhi                    = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().phi() : 0', 'F'),
    genMass                   = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().mass() : 0', 'F'),
    genEnergy                 = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().energy() : 0', 'F'),
    genCharge                 = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().charge() : 0', 'F'),
    genVZ                     = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().vz() : 0', 'F'),
    genStatus                 = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().status() : 0', 'I'),
    genIsPrompt               = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().isPromptFinalState() : 0', 'I'),
    genIsFromTau              = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().isDirectPromptTauDecayProductFinalState() : 0', 'I'),
    genIsPromptDecayed        = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().isPromptDecayed() : 0', 'I'),
    genIsFromHadron           = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().statusFlags().isDirectHadronDecayProduct() : 0', 'I'),
    genFromHardProcess        = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().fromHardProcessFinalState() : 0', 'I'),
    genFromHardProcessDecayed = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().fromHardProcessDecayed() : 0', 'I'),
    genFromHardProcessTau     = cms.vstring('? (genParticleRef.isNonnull() ) ? genParticleRef().isDirectHardProcessTauDecayProductFinalState() : 0', 'I'),
)


####################################################################################
### jets and taus additionally have these branches #################################
####################################################################################
commonJetTauBranches = commonBranches.clone(
    genJetMatch               = cms.vstring('userCand("genJet").isNonnull()','I'),
    genJetPdgId               = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").pdgId() : 0', 'I'),
    genJetPt                  = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").pt() : 0', 'F'),
    genJetEta                 = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").eta() : 0', 'F'),
    genJetPhi                 = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").phi() : 0', 'F'),
    genJetMass                = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").mass() : 0', 'F'),
    genJetEnergy              = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").energy() : 0', 'F'),
    genJetCharge              = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").charge() : 0', 'F'),
    genJetVZ                  = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").vz() : 0', 'F'),
    genJetStatus              = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").status() : 0', 'I'),
    genJetEMEnergy            = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").emEnergy() : 0', 'F'),
    genJetHadEnergy           = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").hadEnergy() : 0', 'F'),
    genJetInvisibleEnergy     = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").invisibleEnergy() : 0', 'F'),
    genJetNConstituents       = cms.vstring('? (userCand("genJet").isNonnull() ) ? userCand("genJet").nConstituents() : 0', 'I'),
)

####################################################################################
### electrons and photons additionally have these branches #########################
####################################################################################
commonEgammaBranches = commonObjectBranches.clone(
    isphoton   = cms.vstring('isPhoton', 'I'),
    iselectron = cms.vstring('isElectron','I'),

    supercluster_e             = cms.vstring('superCluster().energy','F'),
    supercluster_x             = cms.vstring('superCluster().x','F'),
    supercluster_y             = cms.vstring('superCluster().y','F'),
    supercluster_z             = cms.vstring('superCluster().z','F'),
    supercluster_eta           = cms.vstring('superCluster().eta','F'),
    supercluster_phi           = cms.vstring('superCluster().phi','F'),
    supercluster_rawe          = cms.vstring('superCluster().rawEnergy','F'),
    supercluster_preshowere    = cms.vstring('superCluster().preshowerEnergy','F'),
    supercluster_phiwidth      = cms.vstring('superCluster().phiWidth','F'),
    supercluster_etawidth      = cms.vstring('superCluster().etaWidth','F'),
    supercluster_nbasiccluster = cms.vstring('superCluster().clustersSize()','I'),

    # user data embedded from GapInfoEmbedder
    gapinfo = cms.vstring('userInt("gapinfo")','I'),

    # user data from EffectiveAreaEmbedder
    effectiveArea = cms.vstring('userFloat("EffectiveArea")','F'),

    # isolation
    isolationpfr3charged   = cms.vstring('chargedHadronIso', 'F'),
    isolationpfr3chargedpu = cms.vstring('puChargedHadronIso','F'),
    isolationpfr3photon    = cms.vstring('photonIso', 'F'),
    isolationpfr3neutral   = cms.vstring('neutralHadronIso', 'F'),

    isolationr3track = cms.vstring('? (isElectron) ? dr03TkSumPt : trkSumPtSolidConeDR03','F'),
    isolationr3ecal  = cms.vstring('? (isElectron) ? dr03EcalRecHitSumEt : ecalRecHitSumEtConeDR03','F'),
    isolationr3hcal  = cms.vstring('? (isElectron) ? dr03HcalTowerSumEt : hcalTowerSumEtConeDR03','F'),
    isolationr4track = cms.vstring('? (isElectron) ? dr04TkSumPt : trkSumPtSolidConeDR04','F'),
    isolationr4ecal  = cms.vstring('? (isElectron) ? dr04EcalRecHitSumEt : ecalRecHitSumEtConeDR04','F'),
    isolationr4hcal  = cms.vstring('? (isElectron) ? dr04HcalTowerSumEt : hcalTowerSumEtConeDR04','F'),

    # shower shapes
    sigmaetaeta   = cms.vstring('sigmaEtaEta','F'),
    sigmaietaieta = cms.vstring('sigmaIetaIeta','F'),
    # user data embedded from PhotonShowerShapeEmbedder
    sigmaiphiiphi = cms.vstring('? (isElectron) ? sigmaIphiIphi : userFloat("sigmaiphiiphi")','F'),
    sigmaietaiphi = cms.vstring('? (isElectron) ? sigmaIetaIphi : userFloat("sigmaietaiphi")','F'),

    hcalOverEcal             = cms.vstring('? (isElectron) ? hcalOverEcal : hadronicOverEm','F'),
    ehcaloverecaldepth1      = cms.vstring('? (isElectron) ? hcalDepth1OverEcal : hadronicDepth1OverEm','F'),
    ehcaloverecaldepth2      = cms.vstring('? (isElectron) ? hcalDepth2OverEcal : hadronicDepth2OverEm','F'),
    ehcaltoweroverecaldepth1 = cms.vstring('? (isElectron) ? hcalDepth1OverEcalBc : hadTowDepth1OverEm','F'),
    ehcaltoweroverecaldepth2 = cms.vstring('? (isElectron) ? hcalDepth2OverEcalBc : hadTowDepth2OverEm','F'),


)

####################################################################################
### gen particles have these branches in addition to commonBranches ################
####################################################################################
genParticleBranches = commonBranches.clone(
    status                 = cms.vstring('status()','I'),
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

####################################################################################
### gen jets have these branches in addition to commonBranches #####################
####################################################################################
genJetBranches = commonBranches.clone(
    emEnergy         = cms.vstring('emEnergy()','F'),
    hadEnergy        = cms.vstring('hadEnergy()','F'),
    invisibileEnergy = cms.vstring('invisibleEnergy()','F'),
    nConstituents    = cms.vstring('nConstituents','I'),
)
