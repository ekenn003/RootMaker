#!/usr/bin/env python
import argparse
import os
import sys


# This is because when you make an assignment to a variable in a scope,
# that variable becomes local to that scope and shadows any
# similarly named variable in the outer scope.
# I.e. 'global ..' is only needed in functions which modify.
samplelist = []
sourceDSlist = []
jobnamelist = []

pyname = 'crabconfig.py'


## ___________________________________________________________
def get_json(runperiod):
    json15dir = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/'
    json16dir = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/'

    jsons = {
        'Collisions15': json15dir + 'Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt',

        'ReReco16':     json16dir + 'ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt',

        'PromptReco16': json16dir + 'Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt',
    }
    if runperiod in jsons: return jsons[runperiod]


## ___________________________________________________________
def submit_jobs(args):
    # go to working area
    os.chdir('{0}/src/RootMaker/RootMaker/test/{1}'.format(os.environ['CMSSW_BASE'], args.era))
    for i, sample in enumerate(samplelist):
        os.chdir(jobnamelist[i])
        os.system('crab submit -c {0}'.format(pyname))
        print 'crab submit -c {1}/{0}'.format(pyname, os.getcwd())
        os.chdir('../')
        print
    os.chdir('../')

## ___________________________________________________________
def write_crab_configs(args):
    # go to working area
    os.chdir('{0}/src/RootMaker/RootMaker/test/{1}'.format(os.environ['CMSSW_BASE'], args.era))
    for i, sample in enumerate(samplelist):
        # check if there exists a directory for this job yet
        try:
            os.chdir(jobnamelist[i])
        except OSError:
            os.mkdir(jobnamelist[i])
            os.chdir(jobnamelist[i])

        write_crab_config(args, i)
        os.chdir('../')

    os.chdir('../')

    print 'Created the following files:'
    for i, sample in enumerate(samplelist):
        print '    {0}/src/RootMaker/RootMaker/test/{1}/{2}/{3}'.format(os.environ['CMSSW_BASE'], args.era, jobnamelist[i], pyname)


## ___________________________________________________________
def get_sample_lists(args):
    global samplelist
    global sourceDSlist
    global jobnamelist
    # get samples from samplelist
    if os.path.isfile(args.samplelist):
        with open(args.samplelist, 'r') as fin:
            for line in fin.readlines():
                l = ''.join( c for c in line if c not in ' \t\r\n')
                if not l: continue
                if l.startswith('#'): continue
                jobname, samplename = l.split(':')
                samplelist   += [samplename]
                sourceDSlist += [samplename.split('/')[1]]
                jobnamelist  += [jobname]
    else:
        log.error('Sample input list {0} does not exist.'.format(args.samplelist))



## ___________________________________________________________
def write_crab_config(args, n):
    with open(pyname, 'w') as fout:
        fout.write('from CRABClient.UserUtilities import config')
        fout.write('\nconfig = config()')
        fout.write('\nconfig.Site.storageSite = \'T2_CH_CERN\'')
        fout.write('\nconfig.General.requestName = \'{0}_{1}\''.format(jobnamelist[n], args.trystring))
        fout.write('\nconfig.JobType.pluginName = \'Analysis\'')
        fout.write('\nconfig.JobType.psetName = \'{0}/src/RootMaker/RootMaker/test/RootTree.py\''.format(os.environ['CMSSW_BASE']))
        fout.write('\nconfig.Data.inputDBS = \'global\'')
        fout.write('\nconfig.Data.splitting = \'FileBased\'')
        fout.write('\nconfig.Data.unitsPerJob = {0}'.format(args.filesperjob))
        fout.write('\nconfig.Data.inputDataset = \'{0}\''.format(samplelist[n]))
        fout.write('\nconfig.JobType.pyCfgParams = [\'sqlhead="src/RootMaker/RootMaker/"\']')
        fout.write('\nconfig.JobType.pyCfgParams += [\'sourceDS="{0}"\']'.format(sourceDSlist[n]))
        # add rehlt option
        if args.isReHLT:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isReHLT=1\']')
        else:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isReHLT=0\']')
        # add mc option
        if args.isMC:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isMC=1\']')
        else:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isMC=0\']')
        # add rereco option
        if args.isReReco:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isReReco=1\']')
        else:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isReReco=0\']')
        if args.applylumimask is not None:
            fout.write('\nconfig.Data.lumiMask = \'{0}\''.format(get_json(args.applylumimask)))
        fout.write('\nconfig.Data.outLFNDirBase = \'/store/user/ekennedy/T2_CH_CERN/smh2mu/80X/{0}/{1}/{2}\''.format(args.era, 'mc' if args.isMC else 'data', jobnamelist[n]))
        fout.write('\nconfig.Data.publication = False')



## ___________________________________________________________
def parse_command_line(argv):
    parser = argparse.ArgumentParser(description='Submit jobs to grid')

    parser.add_argument('--era',       type=str, help='Era (nov16, etc)')
    parser.add_argument('--trystring', type=str, help='CRAB taskname suffix')
    parser.add_argument('--isMC',     action='store_true', help='Is Monte Carlo')
    parser.add_argument('--isReHLT',  action='store_true', help='Is reHLT Monte Carlo')
    parser.add_argument('--isReReco', action='store_true', help='Is reReco data')
    # input list files
    parser.add_argument('--samplelist', type=str, help='Text file list of DAS samples to submit, one per line')
    # more optional args
    parser.add_argument('--applylumimask', type=str, default=None, choices=['Collisions15','ReReco16','PromptReco16'])
    parser.add_argument('--filesperjob',   type=int, default=1)

    return parser.parse_args(argv)



## ___________________________________________________________
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parse_command_line(argv)



    get_sample_lists(args)
    write_crab_configs(args)
    submit_jobs(args)





## ___________________________________________________________
if __name__ == '__main__':
    main()
