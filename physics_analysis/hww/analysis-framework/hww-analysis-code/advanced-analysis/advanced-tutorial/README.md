# Advanced tutorial

## Analysis with VBF config files 

```text
./prepare.py config/master/VBF/prepare-VBF-Coupling-2018.cfg
./initialize.py config/master/VBF/initialize-VBF-Coupling-2018.cfg
./analyze.py config/master/VBF/analyze-VBF-Coupling-2018.cfg
./visualize.py config/master/VBF/visualize-VBF-Coupling-2018.cfg
```

#### Run with batch system

```text
./submit.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --jobs config/jobLists/VBF/jobs-noFake.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier 20190129_VBF_baseline
```

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

