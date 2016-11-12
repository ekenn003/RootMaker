#!/usr/bin/env python
import argparse
import logging
import os
import math
import sys
import glob
import subprocess
import fnmatch
import json
from socket import gethostname
try:
    from CRABClient.ClientExceptions import ClientException
    from CRABClient.ClientUtilities import initLoggers
    from httplib import HTTPException
    import CRABClient.Commands.submit as crab_client_submit
    import CRABClient.Commands.status as crab_client_status
    import CRABClient.Commands.resubmit as crab_client_resubmit
    crabloaded = True
except:
    crabloaded = False

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
log = logging.getLogger('submit_job')


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
def get_crab_workingdir(args):
    '''Get the job working area'''
    #return '{version}/{era}'.format(version=args.version,era=args.era)
    return '{era}'.format(era=args.era)

## ___________________________________________________________
def get_config(args):
    '''Get a crab config file based on the arguments of crabSubmit'''
    from CRABClient.UserUtilities import config

    config = config()

    config.General.workArea         = get_crab_workingdir(args)
    config.General.transferOutputs  = True
    config.Data.publication         = False
    config.Data.inputDBS            = 'global'
    config.JobType.pluginName       = 'Analysis'
    config.JobType.psetName         = args.cfg
    config.JobType.pyCfgParams      = args.cmsRunArgs
    if args.isReHLT: config.JobType.pyCfgParams += ['isReHLT=1']
    config.JobType.sendPythonFolder = True

    config.Data.splitting           = 'FileBased'
    config.Data.unitsPerJob         = args.filesperjob
    config.Data.outLFNDirBase       = '/store/user/ekennedy/T2_CH_CERN/smh2mu/{0}/{1}/{2}/'.format(args.version, args.era, 'mc' if args.ismc else 'data')
    if args.applylumimask:
        config.Data.lumiMask        = get_json(args.applylumimask)

    config.Site.storageSite         = 'T2_CH_CERN'

    return config



## ___________________________________________________________
def submit_das_crab(args):
    '''Submit samples using DAS'''
    tblogger, logger, memhandler = initLoggers()
    tblogger.setLevel(logging.INFO)
    logger.setLevel(logging.INFO)
    memhandler.setLevel(logging.INFO)

    # crab config
    config = get_config(args)

    # get samples
    samplelist = []
    jobnamelist = []
    #if args.samples:
    #    samplelist += args.samples
    if os.path.isfile(args.samplelist):
        with open(args.samplelist,'r') as f:
            for line in f.readlines():
                #l = line.strip()
                l = ''.join( c for c in line if c not in ' \t\r\n')
                if not l: continue
                if l.startswith('#'): continue
                jobname, samplename = l.split(':')
                jobnamelist += [jobname]
                samplelist  += [samplename]
    else:
        log.error('Sample input list {0} does not exist.'.format(args.samplelist))

    submitMap = {}
    # iterate over samples
    for i, sample in enumerate(samplelist):
        source_dataset = sample.split('/')[1]
        config.General.requestName = '{0}_{1}'.format(jobnamelist[i], args.trystring)
        config.Data.inputDataset   = sample
        config.JobType.pyCfgParams += ['sourceDS="{0}"'.format(source_dataset)]
        config.Data.outLFNDirBase += jobnamelist[i]
        

        print 'task name = {0}\nsource name = {1}\ndataset = {2}'.format(jobnamelist[i], source_dataset, sample)
        # submit the job
        submitArgs = ['--config',config]
        try:
            log.info('Submitting for input dataset {0}'.format(sample))
            print submitArgs
            submitMap[sample] = crab_client_submit.submit(logger,submitArgs)()
        except HTTPException as hte:
            log.info('Submission for input dataset {0} failed: {1}'.format(sample, hte.headers))
        except ClientException as cle:
            log.info('Submission for input dataset {0} failed: {1}'.format(sample, cle))



## ___________________________________________________________
def submit_crab(args):
    '''Create submission script for crab'''
    if not crabloaded:
        logging.error('You must source a crab environment to submit to crab.\nsource /cvmfs/cms.cern.ch/crab3/crab.sh')
        return
    if args.samplelist or args.samples:
        print 'submit_das_crab(args)'
        print args
        #submit_das_crab(args)
    else:
        log.warning('Unrecognized submit configuration: include --samples, or --samplelist.')




## ___________________________________________________________
def parse_command_line(argv):
    parser = argparse.ArgumentParser(description='Submit jobs to grid')

    # submission type
    subparsers = parser.add_subparsers(help='Submission mode')

    # crabSubmit
    parser_crabSubmit = subparsers.add_parser('crabSubmit', help='Submit jobs via crab')
    parser_crabSubmit.add_argument('--version', type=str, choices=['76X', '80X'], help='Version of CMSSW inputs were produced in')
    parser_crabSubmit.add_argument('--era', type=str, help='Era (nov16, etc)')
    parser_crabSubmit.add_argument('--trystring', type=str, help='CRAB taskname suffix')
    parser_crabSubmit.add_argument('--ismc', action='store_true', help='Is Monte Carlo')
    parser_crabSubmit.add_argument('--isReHLT', action='store_true', help='Is reHLT Monte Carlo')
    # location of RootTree.py
    parser_crabSubmit.add_argument('--cfg', type=str, help='cmsRun config file or user script')
    parser_crabSubmit.add_argument('--cmsRunArgs', nargs='*', 
        help='Arguments passed to cmsRun/script'
    )

    parser_crabSubmit_inputs = parser_crabSubmit.add_mutually_exclusive_group(required=True)
    parser_crabSubmit_inputs.add_argument('--samples', type=str, nargs='*',
        help='Space delimited list of DAS samples to submit'
    )
    parser_crabSubmit_inputs.add_argument('--samplelist', type=str,
        help='Text file list of DAS samples to submit, one per line'
    )

    parser_crabSubmit.add_argument('--applylumimask',type=str, default=None,
        choices=['Collisions15','ICHEP2016','Collisions16'],
        help='Apply the latest golden json run lumimask to data'
    )


    parser_crabSubmit.add_argument('--filesperjob', type=int, default=1,
        help='Number of files per job'
    )

    parser_crabSubmit.set_defaults(submit=submit_crab)

    return parser.parse_args(argv)



## ___________________________________________________________
def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = parse_command_line(argv)
    submit_string = args.submit(args)

if __name__ == '__main__':
    status = main()
    sys.exit(status)
