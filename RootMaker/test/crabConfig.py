from CRABClient.UserUtilities import config
config = config()

# taskname
config.General.requestName = '_try1'

config.JobType.pluginName = 'Analysis'

config.JobType.psetName = 'RootTree.py'

# input and JSON
config.Data.inputDataset = ''
config.JobType.pyCfgParams = ['sourceDS=" "']

config.Data.lumiMask = ''

# job splitting options
config.Data.inputDBS = 'global'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

# storage options
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_US_UCSD'
config.Data.outLFNDirBase = '/store/user/ekennedy/{0}/smh2mu/76X/<era>/<mc-data>/<dset>'.format(config.Site.storageSite)

config.Data.publication = False
