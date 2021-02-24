# Batch

## Introduction

To run batch on the lxplus, we can use the condor system. The following provide how we can run condor. Condor is used in the HWW analysis. Here is an example of how to write a simple script to run the condor. 

The submission is done with the following command. So, we need a shell script which should initialize the environment. Then, submit the job to condor. 

```text
chmod +x batch.sh 
condor_submit job.sub
```

The job configuration is defined as following. The `batch.sh` is script you would like to run in the condor. 

```text
universe = vanilla
executable = batch.sh
output = job.out
error = job.err
log = job.log
queue
```

We need to define the environment first. 

```text
#!/bin/bash

# This is set the path where you would like to do. Should be changed by youself!
path=/atlas/data19/metsai/hbsm4top/fitter/run

# initialize the ATLAS environment
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh

# The following are the examples, you need to CHANGE FOR YOUR WORK.
cd $path/..
source setup.sh
cd $path
trex-fitter n config/SSML_BSMtttt_official_Fit_Full_syst_v1.config 'Regions=CR1b3le'
```

