# Analyze and Submit

## Introduction

In this section, we will take the VBF analysis as an example. Therefore, we will use the VBF configuration files to introduce how we produce the results from the PxAOD samples.

### Analyze \(default\)

We run the whole VBF analysis with the following line. 

```bash
./analyze.py config/master/VBF/analyze-VBF-default.cfg
```

However, it will be take a very long time to run over the samples since the samples are huge. Therefore, we `submit` our analysis to the _batch system_ to run over the samples in parallel. 

### The workflow with submit

The workflow with `submit` instead of `analyze` is presented below. In general, the workflow is similar as before. The only difference is that the `analyze` step is replaced by the `submit` step. 

```bash
# Run in the share folder
./prepare.py config/master/VBF/prepare-VBF-default.cfg
./initialize.py config/master/VBF/initialize-VBF-default.cfg

# Use the submit step instead of analyzing
./submit.py config/master/VBF/analyze-VBF-default.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline
tqmerge -t analyze -o sampleFolders/analyzed/samples-analyzed-VBF-20190129_VBF_baseline.root batchOutput/unmerged_20190129_VBF_baseline/*.root

./visualize.py config/master/VBF/visualize-VBF-default.cfg
```

### Run with batch system

To run over the samples in parallel, we replace the `analyze` step with `submit` step. With the `submit` step, we can split our analysis to several jobs and run all the jobs parallel in the same time. After finishing all the jobs, we then merge the jobs and produce a merged analyzed file. Then, we can run the `visualize` step to produce the histograms and cutflows. There is a tutorial [slide](https://indico.cern.ch/event/771763/contributions/3246711/attachments/1768840/2874276/caf_tutorial_submission.pdf) for the batch submission. 

#### Submit step

The following command provides us an example to run with `submit` step. We have several options to control the conditions of the jobs like the size of jobs.

```text
./submit.py config/master/VBF/analyze-VBF-default.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline
```

We will discuss the options used for submit step. First, you can type the following command to show the options we could use. 

```text
./submit.py --help
```

Moreover, we can also look into submit.py to understand more detailedly. We will present the options which are commonly used in the following.

#### --jobs

This will define the processes you would like to run in parallel. 

```bash
--jobs config/jobLists/VBF/jobs-noFake.txt
```

Currently, in V18 PxAOD samples, we don't have fake samples. Therefore, here we only run without the fake samples. We split the analysis into several jobs to run over different samples like data, ggf , vbf and diboson ...etc. 

{% code title="config/jobLists/VBF/jobs-noFake.txt" %}
```text
/data/?
/sig/?/mh125/ggf/
/sig/?/mh125/vbf/
/bkg/?/diboson/NonWW/?/ZZ/
/bkg/?/diboson/NonWW/qq/WZgammaStar/
/bkg/?/diboson/WW/qq
#/bkg/?/diboson/WW/gg
/bkg/?/Zjets/?/?/ee/
/bkg/?/Zjets/?/?/mm/
/bkg/?/Zjets/?/?/tt/
/bkg/?/Vgamma/Wgamma
/bkg/?/Vgamma/Zgamma
/bkg/?/top/ttbar/
/bkg/?/top/singletop/Wt
```
{% endcode %}

#### --maxSampleSize and --maxSampleCount

After splitting to several jobs for different processes, we use these options to further split the into sub-jobs/tasks. You can set your own number for different usages.

* **--maxSampleSize** This option will limit the jobs with a maximum sample size. The unit used is MB.If you set a number for this option, then there will have a maximum size for the jobs. The smaller number is set, the analysis will be split to more jobs.
* **--maxSampleCount**  This option will limit the number of input files for each job. The smaller number for this option, the analysis will be split to more jobs.

In general, I use the following setting. It will take about 1~2 hours to run over the whole jobs. It will become longer if you run over whole Run-2 dataset.

```text
--maxSampleSize 6000 --maxSampleCount 20
```

If you are urgent to produce the results, you can also make the number smaller. For example, we can set as the following numbers

```text
--maxSampleSize 3000 --maxSampleCount 5
```

Then, you will produce many jobs to run in the same time. It will become very quick to produce the results. However, it seems there are some quota for each account. Therefore, it will be possible to run out of the quota with the batch system. It will take a few hours \(or 1-2 day\) to gain the quota back.

#### --identifier 

The identifier is an option to determine the name of the folder for all the output from different jobs. For example, if we set the identifier as following

```text
--identifier VBF_analysis
```

The output files will be generated in the following folder. All the output root files will also be produced in the following folder `batchOutput`

```text
# in the share folder
batchOutput/unmerged_VBF_analysis
```

### Monitoring

After submitting the jobs to the batch system, we should track the status of jobs. 

#### Check the status of jobs

```bash
condor_q
```

An example of the status of jobs is shown below

```text
OWNER BATCH_NAME      SUBMITTED   DONE   RUN    IDLE   HOLD  TOTAL JOB_IDS

0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended
```

* **Status of jobs**
  * completed: the jobs are finished
  * removed: the jobs are removed by users
  * running: the jobs are still running
  * idle: the jobs are pending

#### Remove jobs

The command to remove the jobs is 

```bash
condor_rm
```

We can remove the jobs with the JOB\_IDS or remove all the jobs for the user. For example, the JOB\_IDS is 14808.0. Then we can use the following the command to remove the specific job.

```bash
condor_rm 14808.0
```

We can remove all the jobs for specific user by

```bash
condor_rm youraccount
```

**Check the missing \(failed\) jobs**

Although the jobs are run, your jobs may possibly fail due to several reasons. Therefore, we should check that do we miss any sample for the `submit` step. 

After running over all the jobs, the jobs will disappear when checking the status of jobs. Then, we should add this option in the `submit` step to check the missing samples.

```text
--checkmissing
```

The command should be the identical as the command you submitted before with this additional option `--checkmissing`

```text
./submit.py config/master/VBF/analyze-VBF-default.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline --checkmissing
```

### Merging

After finishing all the jobs, we should merge all the output files to one file. 

```text
tqmerge -t analyze -o sampleFolders/analyzed/samples-analyzed-VBF-20190129_VBF_baseline.root batchOutput/unmerged_20190129_VBF_baseline/*.root
```

where ****`-o` means the name of output file. Moreover, we merge all the files which are in the folder `unmerged_20190129_VBF_baseline`**.** 

```text
batchOutput/unmerged_20190129_VBF_baseline/*.root
```

Where "\*.root" means **all** the files with the same suffix `.root`

### 注意事項！

1. 每次要submit之前，請先試跑一遍analyze，不需要跑完，而是跑到確定event已經可以在不同的cut stage算出該有的值即可，如此，你可以快速知道你的設置有沒有bugs。
2. 如果有jobs一直失敗，那記得去看你是不是有錯誤訊息，有可能跑到某些events時遇到問題，那就會失敗。
3. **記得不要在`analyze`或是`submit`的時候更改你有用到的code，不然會影響到你的結果！！**

## Troubleshooting

### Analyze with specific samples

When you found some bugs from observables, we can just analyze part of the analysis like run some specific samples. Therefore, we can use the option `--restrict`.

#### --restrict

We can limit the processes to analyze by the option `--restrict`

For example, we can run a single process. We should add the option below to the command for the `analyze` step. With this path, the analyze step will run over all the samples under this path 

```text
--restrict /sig/?/mh125/vbf/
```

The complete command to run with only VBF sample is shown below

```bash
./analyze.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --restrict /sig/?/mh125/vbf/
```

#### Run with specific multiple processes

The following example is to run only the VBF, ggF and WW processes in the same time. Please note that you **should not add an additional space between the processes paths**

```text
--restrict /sig/?/mh125/vbf/,/sig/?/mh125/ggf/,/bkg/?/diboson/WW/,/bkg/?/Zjets/?/?/tt/,/bkg/?/top/ttbar/,/bkg/?/top/singletop/Wt
```

The complete command to run with only these 6 processes is shown below

```
./analyze.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --restrict /sig/?/mh125/vbf/,/sig/?/mh125/ggf/,/bkg/?/diboson/WW/,/bkg/?/Zjets/?/?/tt/,/bkg/?/top/ttbar/,/bkg/?/top/singletop/Wt
```

