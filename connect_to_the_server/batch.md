# Batch system

## Introduction

我們一般會在Lxplus上面的**`condor`**來完成平行化的執行程式來增加效率！

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

接下來就可以做job submission這件事了！

第一個指令是更改batch.sh的權限讓他是可以執行的檔案，第二個`condor_submit`就是把job丟進condor pool裡面去run job。

```bash
chmod +x batch.sh 
condor_submit job.sub
```

好的！所以你完成了首次的condor job submission！

### Job status

接下來就是要檢查自己的condor job的狀態



