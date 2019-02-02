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

Currently, in V18 PxAOD samples, we don't have fake samples. Therefore, here we only run without the fake samples. 

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

We use these options to further split the jobs/tasks. You can set your own number for different usages.

* **--maxSampleSize** This option will limit the jobs with a maximum sample size. The unit used is MB.If you set a number for this option, then there will have a maximum size for the jobs. The smaller number is set, the analysis will be split to more jobs.
* **--maxSampleCount**  This option will limit the number of input files for each job. The smaller number for this option, the analysis will be split to more jobs.

In general, I use the following setting. It will take about 1~2 hours to run over the whole jobs. 

```text
--maxSampleSize 6000 --maxSampleCount 20
```

If you are urgent to produce the results, you can also make the number smaller. For example, 

```text
--maxSampleSize 3000 --maxSampleCount 5
```

Then, you will produce many jobs to run in the same time. However, it seems there are some quota for each account. Therefore, it will be possible to run out of the quota with the batch system. It will take a few hours \(or 1-2 day\) to gain back the quota.

#### Monitor the jobs

After submitting the jobs to the batch system, we should track the status of jobs. 

```text
condor_q
```

Remove the jobs in the batch system

```text
condor_rm
```

You can check the missing samples with this option.

```text
--checkmissing
```

Merge the outputs

```text
tqmerge -t analyze -o sampleFolders/analyzed/samples-analyzed-VBF-20190129_VBF_baseline.root batchOutput/unmerged_20190129_VBF_baseline/*.root
```

#### 

