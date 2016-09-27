from CRABClient.UserUtilities import config
config = config()

# taskname
config.General.requestName = '_try1'

config.JobType.pluginName = 'Analysis'

config.JobType.psetName = 'RootTree.py'

# input and JSON
config.Data.inputDataset = ''
config.Data.lumiMask = ''

# job splitting options
config.Data.inputDBS = 'global'

# for data:
#config.Data.splitting = 'LumiBased'
#config.Data.unitsPerJob = 3

# for MC:
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

# storage options
config.Data.outLFNDirBase = '/store/user/ekennedy/smh2mu/76X/<era>/<dset>'
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_US_UCSD'

config.Data.publication = False
