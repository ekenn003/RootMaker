from CRABClient.UserUtilities import config
config = config()

###############################################
# configuration ###############################
###############################################

# task
taskname = '_try1'
filesperjob = 3

# input
input_dataset = ''
json          = 'Cert_271036-283685_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'

# output folder options
version = '80X'
era     = 'oct16'

# name out output directory in /store/user/ekennedy/...
output  = ''

#if it is mc or data
#real    = 'data'
real    = 'mc'


# which T2 to store it at
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_US_UCSD'





###############################################
# /end configuration ##########################
###############################################

config.General.requestName = taskname
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'RootTree.py'

config.Data.inputDataset = input_dataset
isReHLT = ('reHLT' in input_dataset)
config.JobType.pyCfgParams = ['sourceDS="{0}", isReHLT={1}'.format((config.Data.inputDataset).split('/')[1], isReHLT)]
print config.JobType.pyCfgParams

# this needs to be changed for 2015 vs 2016 collisions
if real=='data':
    config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/{0}'.format(json)

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = filesperjob

config.Data.outLFNDirBase = '/store/user/ekennedy/{0}/smh2mu/{1}/{2}/{3}/{4}'.format(config.Site.storageSite, version, era, real, output)
config.Data.publication = False

print '\nSource dataset identified as {0}'.format((config.Data.inputDataset).split('/')[1])
print 'Output will be stored in {0}\n'.format(config.Data.outLFNDirBase)

