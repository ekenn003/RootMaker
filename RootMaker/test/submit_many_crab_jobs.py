#!/usr/bin/env python
import argparse
#import logging
import os
#import math
import sys
#import glob
#import subprocess
#import fnmatch
#import json


# This is because when you make an assignment to a variable in a scope,
# that variable becomes local to that scope and shadows any
# similarly named variable in the outer scope.
# I.e. 'global ..' is only needed in functions which modify.
samplelist = []
sourceDSlist = []
jobnamelist = []



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
        print '    {0}/src/RootMaker/RootMaker/test/{1}/{2}/crabconfig.py'.format(os.environ['CMSSW_BASE'], args.era, jobnamelist[i])


## ___________________________________________________________
def get_sample_lists(args):
    global samplelist
    global sourceDSlist
    global jobnamelist
    # get samples from samplelist
    if os.path.isfile(args.samplelist):
        with open(args.samplelist,'r') as f:
            for line in f.readlines():
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
def get_json(runperiod):
    jsons = {
        'Collisions15': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/'\
                        'Collisions15/13TeV/'\
                        'Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt',
        'ICHEP2016':    '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/'\
                        'Collisions16/13TeV/'\
                        'Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt',
        'Collisions16': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/'\
                        'Collisions16/13TeV/'\
                        'Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt',
    }
    if runperiod in jsons: return jsons[runperiod]



## ___________________________________________________________
def write_crab_config(args, n):
    with open('crabconfig.py', 'w') as fout:
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
        fout.write('\nconfig.JobType.pyCfgParams = [\'sourceDS="{0}"\']'.format(sourceDSlist[n]))
        if args.isReHLT:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isReHLT=1\']')
        if args.isMC:
            fout.write('\nconfig.JobType.pyCfgParams += [\'isMC=1\']')
        if args.applylumimask is not None:
            fout.write('\nconfig.Data.lumiMask = \'{0}\''.format(get_json(args.applylumimask)))
        fout.write('\nconfig.Data.outLFNDirBase = \'/store/user/ekennedy/T2_CH_CERN/smh2mu/80X/{0}/{1}/{2}\''.format(args.era, 'mc' if args.isMC else 'data', jobnamelist[n]))
        fout.write('\nconfig.Data.publication = False')



## ___________________________________________________________
def parse_command_line(argv):
    parser = argparse.ArgumentParser(description='Submit jobs to grid')

    parser.add_argument('--era',       type=str, help='Era (nov16, etc)')
    parser.add_argument('--trystring', type=str, help='CRAB taskname suffix')
    parser.add_argument('--isMC',    action='store_true', help='Is Monte Carlo')
    parser.add_argument('--isReHLT', action='store_true', help='Is reHLT Monte Carlo')
    # input list files
    parser.add_argument('--samplelist', type=str, help='Text file list of DAS samples to submit, one per line')
    # more optional args
    parser.add_argument('--applylumimask', type=str, default=None, choices=['Collisions15','ICHEP2016','Collisions16'])
    parser.add_argument('--filesperjob',   type=int, default=1)

    return parser.parse_args(argv)



## ___________________________________________________________
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parse_command_line(argv)



    get_sample_lists(args)
    write_crab_configs(args)





## ___________________________________________________________
if __name__ == '__main__':
    main()
