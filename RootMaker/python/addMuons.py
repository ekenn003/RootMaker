import FWCore.ParameterSet.Config as cms
from RootMaker.RootMaker.objectBase import commonObjectBranches

################################################
### muon branches ##############################
################################################
muonBranches = commonObjectBranches.clone(
    # user data from PVEmbedder
    dz     = cms.vstring('userFloat("dz")','F'),
    dzerr  = cms.vstring('dzError','F'),
    dxy    = cms.vstring('userFloat("dxy")','F'),
    dxyerr = cms.vstring('dxyError','F'),

    ## user data from MuonInfoEmbedder
    #trackermuonquality      = cms.vstring('userInt("trackermuonquality")','I'),
    #numchamberswithsegments = cms.vstring('userInt("numberOfMatches")','I'),
    #numchambers             = cms.vstring('numberOfChambers','I'),
    #nummatchedstations      = cms.vstring('numberOfMatchedStations','I'),
    #numvalidmuonhits = cms.vstring('? (globalTrack().isNonnull() ) ? globalTrack().hitPattern().numberOfValidMuonHits() : -1', 'I'),

    ecalenergy = cms.vstring('calEnergy().em','F'),
    hcalenergy = cms.vstring('calEnergy().had','F'),

    # muon ID
    is_pf_muon        = cms.vstring('isPFMuon','I'),
    is_global         = cms.vstring('isGlobalMuon','I'),
    is_tracker        = cms.vstring('isTrackerMuon','I'),
    is_standalone     = cms.vstring('isStandAloneMuon','I'),
    is_calo           = cms.vstring('isCaloMuon','I'),

    # tracks
    hasglobaltrack   = cms.vstring('globalTrack().isNonnull()','I'),
    pterror          = cms.vstring('? (globalTrack().isNonnull() ) ? globalTrack().ptError() : 0', 'F'),
    chi2             = cms.vstring('? (globalTrack().isNonnull() ) ? globalTrack().chi2() : -1', 'F'),
    ndof             = cms.vstring('? (globalTrack().isNonnull() ) ? globalTrack().ndof() : -1', 'F'),

    # isolation
    pfisolationr3_sumchargedhadronpt   = cms.vstring('pfIsolationR03().sumChargedHadronPt','F'),
    pfisolationr3_sumchargedparticlept = cms.vstring('pfIsolationR03().sumChargedParticlePt','F'),
    pfisolationr3_sumneutralhadronet   = cms.vstring('pfIsolationR03().sumNeutralHadronEt','F'),
    pfisolationr3_sumphotonet          = cms.vstring('pfIsolationR03().sumPhotonEt','F'),
    pfisolationr3_sumpupt              = cms.vstring('pfIsolationR03().sumPUPt','F'),
    pfisolationr3_sumneutralhadronethighthreshold = cms.vstring('pfIsolationR03().sumNeutralHadronEtHighThreshold','F'),
    pfisolationr3_sumphotonethighthreshold        = cms.vstring('pfIsolationR03().sumPhotonEtHighThreshold','F'),

    pfisolationr4_sumchargedhadronpt   = cms.vstring('pfIsolationR04().sumChargedHadronPt','F'),
    pfisolationr4_sumchargedparticlept = cms.vstring('pfIsolationR04().sumChargedParticlePt','F'),
    pfisolationr4_sumneutralhadronet   = cms.vstring('pfIsolationR04().sumNeutralHadronEt','F'),
    pfisolationr4_sumphotonet          = cms.vstring('pfIsolationR04().sumPhotonEt','F'),
    pfisolationr4_sumpupt              = cms.vstring('pfIsolationR04().sumPUPt','F'),
    pfisolationr4_sumneutralhadronethighthreshold = cms.vstring('pfIsolationR04().sumNeutralHadronEtHighThreshold','F'),
    pfisolationr4_sumphotonethighthreshold        = cms.vstring('pfIsolationR04().sumPhotonEtHighThreshold','F'),

    #isolationr3track    = cms.vstring('trackIso()','F'),
    #isolationr3ntrack   = cms.vstring('isolationR03().nTracks','I'),
    #isolationr3ecal     = cms.vstring('isolationR03().emEt','F'), # same as ecalIso()
    #isolationr3hcal     = cms.vstring('isolationR03().hadEt','F'), # same as hcalIso()

    # muon ID (tight ID embedded from MuonInfoEmbedder)
    is_tight_muon  = cms.vstring('userInt("isTightMuon")','I'),
    is_medium_muon = cms.vstring('isMediumMuon','I'),
    # medium2016 for moriond17
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#Short_Term_Instructions_for_Mori
    is_medium2016_muon = cms.vstring('userInt("isMedium2016Muon")','I'),
    is_loose_muon  = cms.vstring('isLooseMuon','I'),

    # user data from RochCorEmbedder
    rochesterPt     = cms.vstring('userFloat("rochesterPt")','F'),
    rochesterPx     = cms.vstring('userFloat("rochesterPx")','F'),
    rochesterPy     = cms.vstring('userFloat("rochesterPy")','F'),
    rochesterPz     = cms.vstring('userFloat("rochesterPz")','F'),
    rochesterEta    = cms.vstring('userFloat("rochesterEta")','F'),
    rochesterPhi    = cms.vstring('userFloat("rochesterPhi")','F'),
    rochesterEnergy = cms.vstring('userFloat("rochesterEnergy")','F'),
    rochesterError  = cms.vstring('userFloat("rochesterError")','F'),

    # user data from HLTMatchEmbedder
    trigger = cms.vstring('userInt("trigger")','I'),
    matches_IsoMu24                           = cms.vstring('userInt("matches_IsoMu24")','I'),
    matches_IsoTkMu24                         = cms.vstring('userInt("matches_IsoTkMu24")','I'),
    matches_IsoMu27                           = cms.vstring('userInt("matches_IsoMu27")','I'),
    matches_IsoTkMu27                         = cms.vstring('userInt("matches_IsoTkMu27")','I'),
    matches_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ   = cms.vstring('userInt("matches_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ")','I'),
    matches_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = cms.vstring('userInt("matches_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ")','I'),
)

################################################
### produce muon collection ####################
################################################
def addMuons(process, coll, **kwargs):
    isMC = kwargs.pop('isMC', False)
    mSrc = coll['muons']
    pvSrc = coll['vertices']
    # customization path
    process.muonCustomization = cms.Path()

    ###################################
    ### embed rochester corrections ###
    ###################################
    process.mRoch = cms.EDProducer(
        'RochCorEmbedder',
        src = cms.InputTag(mSrc),
        isData = cms.bool(not isMC),
    )
    mSrc = 'mRoch'
    process.muonCustomization *= process.mRoch


    ################
    ### embed pv ###
    ################
    process.mPV = cms.EDProducer(
        'MuonPVEmbedder',
        src = cms.InputTag(mSrc),
        vertexSrc = cms.InputTag(pvSrc),
    )
    mSrc = 'mPV'
    process.muonCustomization *= process.mPV

    #####################
    ### embed muon id ###
    #####################
    process.mID = cms.EDProducer(
        'MuonInfoEmbedder',
        src = cms.InputTag(mSrc),
        vertexSrc = cms.InputTag(pvSrc),
    )
    mSrc = 'mID'
    process.muonCustomization *= process.mID

    ##############################
    ### embed trigger matching ###
    ##############################
    process.mTrig = cms.EDProducer(
        'MuonHLTMatchEmbedder',
        src = cms.InputTag(mSrc),
        triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
        triggerObjects = cms.InputTag('selectedPatTrigger'),
        deltaR = cms.double(0.5),
        labels = cms.vstring( # needs to match paths
            # single muon
            'matches_IsoMu24',
            'matches_IsoTkMu24',
            'matches_IsoMu27',
            'matches_IsoTkMu27',
            # double muon
            'matches_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ',
            'matches_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ',
        ),
        paths = cms.vstring( # needs to match labels
            # single muon
            'HLT_IsoMu24_v\\[0-9]+',
            'HLT_IsoTkMu24_v\\[0-9]+',
            'HLT_IsoMu27_v\\[0-9]+',
            'HLT_IsoTkMu27_v\\[0-9]+',
            # double muon
            'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v\\[0-9]+',
            'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v\\[0-9]+',
        ),
    )
    mSrc = 'mTrig'
    process.muonCustomization *= process.mTrig

    # add to schedule
    process.schedule.append(process.muonCustomization)
    coll['muons'] = mSrc
    return coll
