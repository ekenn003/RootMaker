import FWCore.ParameterSet.Config as cms

####################################################################################
### primvertex_* branches ##########################################################
####################################################################################
vertexBranches = cms.PSet(
    x              = cms.vstring('x','F'),
    y              = cms.vstring('y','F'),
    z              = cms.vstring('z','F'),
    xError         = cms.vstring('xError','F'),
    yError         = cms.vstring('yError','F'),
    zError         = cms.vstring('zError','F'),
    chi2           = cms.vstring('chi2','F'),
    ndof           = cms.vstring('ndof','F'),
    ntracks        = cms.vstring('tracksSize','I'),
    normalizedChi2 = cms.vstring('normalizedChi2','F'),
    isvalid        = cms.vstring('isValid', 'I'),
    isfake         = cms.vstring('isFake', 'I'),
    rho            = cms.vstring('position.Rho','F'),
    cov0           = cms.vstring('covariance(0,0)','F'),
    cov1           = cms.vstring('covariance(0,1)','F'),
    cov2           = cms.vstring('covariance(0,2)','F'),
    cov3           = cms.vstring('covariance(1,1)','F'),
    cov4           = cms.vstring('covariance(1,2)','F'),
    cov5           = cms.vstring('covariance(2,2)','F'),
)
