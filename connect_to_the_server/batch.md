# Batch system

## Introduction

我們一般會在Lxplus上面的**`condor`**來完成平行化的執行程式來增加效率！

可以參考的文件：[https://batchdocs.web.cern.ch/local/submit.html](https://batchdocs.web.cern.ch/local/submit.html)

## Examples

### Job submission

首先，你需要將你想要執行的指令都整理在一個shell script上面，在這裡我們稱為`batch.sh`。在這裡我們，就只做`echo`現在的路徑，你可以取代成自己的指令們。

{% code title="batch.sh" %}
```bash
#!/bin/bash

env=$PWD
echo "Current location is "$env
```
{% endcode %}

接下來，你需要定義這個job submission的設定檔，我們在這稱為job.sub。你可以自訂輸出`output`, `error`, `log`這些的路徑或是名字。

{% code title="job.sub" %}
```text
universe = vanilla
executable = batch.sh
output = job.out
error = job.err
log = job.log
queue
```
{% endcode %}

接下來只需要做完以下兩個指令就可以完成job submission這件事了！

第一個指令是更改batch.sh的權限讓他是可以執行的檔案，第二個`condor_submit`就是把job丟進condor pool裡面去run job。

```bash
chmod +x batch.sh 
condor_submit job.sub
```

好的！所以你完成了首次的condor job submission！

### Job status / removal

#### Check job status

接下來就是要檢查自己的condor job的狀態，檢查condor狀態透過`condor_q`來查詢，在後面加上你的username會檢查你個人的condor jobs。

```bash
condor_q username

# expected print out 
-- Schedd: umt3int02.aglt2.org : <10.10.1.51:9618?... @ 02/24/21 08:23:18
 ID       OWNER            SUBMITTED     RUN_TIME ST PRI SIZE CMD
90703.0   metsai          2/24 08:18   0+00:03:13 R  10  97.7 4T_validation_BDT_NTree1000_nominal_212120_v15_nj_sumbj6_deco_all_event.sh
90704.0   metsai          2/24 08:18   0+00:02:49 R  10  97.7 4T_validation_BDT_NTree1000_nominal_212120_v15_nj_sumbj4_deco_ttW78j_ratio04_a
90705.0   metsai          2/24 08:18   0+00:00:56 R  10  97.7 4T_validation_BDT_NTree1000_nominal_212120_v15_j6_nTrk1000_deco_all_event.sh
...

```

#### Remove jobs

移除jobs可以透過`condor_rm`來完成，可以移除所有你的jobs或是特定的job。

```bash
# remove all jobs in your username
condor_rm username

# remove specific job (use example ID from previous code block)
condor_rm 90703
```

