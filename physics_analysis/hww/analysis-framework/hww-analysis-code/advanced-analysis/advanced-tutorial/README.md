# Advanced tutorial

## Introduction

In the advanced tutorial, we will take the VBF analysis as an example. Therefore, we will use the VBF config files to introduce how to produce the results from the PxAOD samples.

### Analysis with VBF config files 

To produce the results for VBF analysis, we should run these four steps including **prepare**, **initialize**, **analyze** and **visualize**. Now, the VBF config files are still under construction. We need to modify several lines to accomplish what we would like to do! Please see the following sections to have a complete picture. 

The four steps to produce the VBF results:

```bash
# Run in the share folder
./prepare.py config/master/VBF/prepare-VBF-Coupling-2018.cfg
./initialize.py config/master/VBF/initialize-VBF-Coupling-2018.cfg
./analyze.py config/master/VBF/analyze-VBF-Coupling-2018.cfg
./visualize.py config/master/VBF/visualize-VBF-Coupling-2018.cfg
```

{% hint style="warning" %}
### Warning!

It will take very long time to run over all the samples in the analyze steps! Therefore, we should use the **batch system** **to run over the samples in parallel**.
{% endhint %}

## The workflow with submit

The workflow with submit step is presented below. In general, the workflow is same as before. The only difference is that the analyze step is replaced by the submit step. 

```text
# Run in the share folder
./prepare.py config/master/VBF/prepare-VBF-Coupling-2018.cfg
./initialize.py config/master/VBF/initialize-VBF-Coupling-2018.cfg

# Use the submit step instead of analyzing
./submit.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline
tqmerge -t analyze -o sampleFolders/analyzed/samples-analyzed-VBF-20190129_VBF_baseline.root batchOutput/unmerged_20190129_VBF_baseline/*.root

./visualize.py config/master/VBF/visualize-VBF-Coupling-2018.cfg
```

### Run with batch system

To run over the samples in parallel, we replace the analyze step with **submit** step. With the submit step, we can split our analysis to several jobs and run all the jobs parallel in the same time. After finishing all the jobs, we then merge the jobs and produce a merged analyzed file. Then, we can run the visualize step to produce the plots and cutflows. 

We also have a tutorial [slide](https://indico.cern.ch/event/771763/contributions/3246711/attachments/1768840/2874276/caf_tutorial_submission.pdf) for the batch submission. 

#### Submit step

The following command provides us an example to run with submit step. We have several options to control the sizes of the jobs and how we define the jobs we would like to run.

```text
./submit.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline
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

Currently, in V18 PxAOD samples, we don't have fake samples. Therefore, here we only run without the fake samples. We first split the analysis by different processes. Therefore, we will split the analysis to jobs for **data**, **ggf** , **vbf**, **diboson**, ... etc. 

{% code-tabs %}
{% code-tabs-item title="config/jobLists/VBF/jobs-noFake.txt" %}
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
{% endcode-tabs-item %}
{% endcode-tabs %}

#### --maxSampleSize and --maxSampleCount

After splitting to several jobs for different processes, we use these options to further split the jobs/tasks. You can set your own number for different usages.

* **--maxSampleSize** This option will limit the jobs with a maximum sample size. The unit used is MB.If you set a number for this option, then there will have a maximum size for the jobs. The smaller number is set, the analysis will be split to more jobs.
* **--maxSampleCount**  This option will limit the number of input files for each job. The smaller number for this option, the analysis will be split to more jobs.

In general, I use the following setting. It will take about 1~2 hours to run over the whole jobs. 

```text
--maxSampleSize 6000 --maxSampleCount 20
```

If you are urgent to produce the results, you can also make the number smaller. For example, we can set as the following numbers

```text
--maxSampleSize 3000 --maxSampleCount 5
```

Then, you will produce many jobs to run in the same time. It will become very quick to produce the results. However, it seems there are some quota for each account. Therefore, it will be possible to run out of the quota with the batch system. It will take a few hours \(or 1-2 day\) to gain back the quota.

#### --identifier 

The identifier is an option to determine the name of the folder for all the output from different jobs. 

For example, if we set the identifier as following

```text
--identifier VBF_analysis
```

The output files will be generated in the following folder. All the output root files will also be produced in the following folder. 

```text
# in the share folder
batchOutput/unmerged_VBF_analysis
```

### Monitor the jobs

After submitting the jobs to the batch system, we should track the status of jobs. 

* **Check the status of jobs**
  * completed: the jobs are finished
  * removed: the jobs are finished
  * running: the jobs are still running
  * idle: the jobs are pending

```text
condor_q
```

The status of jobs will be shown as below:

```text
OWNER BATCH_NAME      SUBMITTED   DONE   RUN    IDLE   HOLD  TOTAL JOB_IDS

0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended
```

* **Remove the jobs in the batch system** We can remove the jobs with the JOB\_IDS. Besides, we can also remove all the jobs for the user.  

The command used to remove the jobs is 

```bash
condor_rm
```

For example, the JOB\_IDS is 14808.0. Then we can use the following the command to remove the specific job.

```bash
condor_rm 14808.0
```

We can also remove all the jobs for specific user by the following command.

```bash
condor_rm youraccount
```

* **Check the missing \(failed\) jobs** Although the jobs are run, your jobs may possibly fail due to several reasons. Therefore, we should check that do we miss any sample for the submit step. 

After running over all the jobs, the jobs will disappear when checking the status of jobs. 

```text
OWNER BATCH_NAME      SUBMITTED   DONE   RUN    IDLE   HOLD  TOTAL JOB_IDS

0 jobs; 0 completed, 0 removed, 0 idle, 0 running, 0 held, 0 suspended
```

We should add this option in the submit step to check the missing samples.

```text
--checkmissing
```

The command **should be the same** **as the command you submitted before** with this additional option. 

```text
./submit.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline --checkmissing
```

### Merge the outputs

After finishing all the jobs, we should merge all the output files to one file. 

```text
tqmerge -t analyze -o sampleFolders/analyzed/samples-analyzed-VBF-20190129_VBF_baseline.root batchOutput/unmerged_20190129_VBF_baseline/*.root
```

where **-o** means the name of output file. Moreover, we merge all the files in the folder **unmerged\_20190129\_VBF\_baseline.** 

```text
batchOutput/unmerged_20190129_VBF_baseline/*.root
```

Where the **\*** means **all** the files with the same suffix \(.root\).

## FAQ

If you find all the jobs are always failed. -&gt; check the code first

