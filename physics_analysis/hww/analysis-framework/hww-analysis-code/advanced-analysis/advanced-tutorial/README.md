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

#### Submit step

The following command provides us an example to run with submit step. We have several options to control the sizes of the jobs and how we define the jobs we would like to run.

```text
./submit.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline
```

We will discuss the options used for submit step. First, you can also type the following command to show the options we could use. 

```text
./submit.py --help
```

Moreover, we can also look into submit.py to understand more detailedly. 

#### --jobs

Define the jobs you want

```text
config/jobLists/VBF/jobs-noFake.txt
```

Check the status of jobs

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

