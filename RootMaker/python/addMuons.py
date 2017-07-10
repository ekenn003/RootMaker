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

    # energy
    ecalenergy = cms.vstring('calEnergy().em','F'),
    hcalenergy = cms.vstring('calEnergy().had','F'),

    # muon ID
    is_pf_muon        = cms.vstring('isPFMuon','I'),
    is_global         = cms.vstring('isGlobalMuon','I'),
    is_tracker        = cms.vstring('isTrackerMuon','I'),
    is_standalone     = cms.vstring('isStandAloneMuon','I'),

    # tracks
    #hasglobaltrack   = cms.vstring('globalTrack().isNonnull()','I'),
    #pterror          = cms.vstring('? (globalTrack().isNonnull() ) ? globalTrack().ptError() : 0', 'F'),
    chi2             = cms.vstring('? (globalTrack().isNonnull() ) ? globalTrack().chi2() : -1', 'F'),
    ndof             = cms.vstring('? (globalTrack().isNonnull() ) ? globalTrack().ndof() : -1', 'F'),

    # isolation
    pfisolationr4_sumchargedhadronpt   = cms.vstring('pfIsolationR04().sumChargedHadronPt','F'),
    pfisolationr4_sumchargedparticlept = cms.vstring('pfIsolationR04().sumChargedParticlePt','F'),
    pfisolationr4_sumneutralhadronet   = cms.vstring('pfIsolationR04().sumNeutralHadronEt','F'),
    pfisolationr4_sumphotonet          = cms.vstring('pfIsolationR04().sumPhotonEt','F'),
    pfisolationr4_sumpupt              = cms.vstring('pfIsolationR04().sumPUPt','F'),
    pfisolationr4_sumneutralhadronethighthreshold = cms.vstring('pfIsolationR04().sumNeutralHadronEtHighThreshold','F'),
    pfisolationr4_sumphotonethighthreshold        = cms.vstring('pfIsolationR04().sumPhotonEtHighThreshold','F'),

    # muon ID (tight ID embedded from MuonInfoEmbedder)
    is_tight_muon  = cms.vstring('userInt("isTightMuon")','I'),
    is_medium_muon = cms.vstring('isMediumMuon','I'),
    # medium2016 for moriond17
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#Short_Term_Instructions_for_Mori
    is_medium2016_muon = cms.vstring('userInt("isMedium2016Muon")','I'),
    is_loose_muon  = cms.vstring('isLooseMuon','I'),

    # user data from RochCorEmbedder
    rochesterPt     = cms.vstring('userFloat("rochesterPt")','F'),

    # user data from HLTMatchEmbedder
    matches_IsoMu24                           = cms.vstring('userInt("matches_IsoMu24")','I'),
    matches_IsoTkMu24                         = cms.vstring('userInt("matches_IsoTkMu24")','I'),

    # energy shifts
    pt_muonEnUp                 = cms.vstring('? hasUserCand("MuonEnUp") ? userCand("MuonEnUp").pt() : 0','F'),
    energy_muonEnUp             = cms.vstring('? hasUserCand("MuonEnUp") ? userCand("MuonEnUp").energy() : 0','F'),
    pt_muonEnDown               = cms.vstring('? hasUserCand("MuonEnDown") ? userCand("MuonEnDown").pt() : 0','F'),
    energy_muonEnDown           = cms.vstring('? hasUserCand("MuonEnDown") ? userCand("MuonEnDown").energy() : 0','F'),
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
        rochCorrDataDir = cms.FileInPath('RootMaker/RootMaker/data/rcdata.2016.v3/config.txt'),
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
