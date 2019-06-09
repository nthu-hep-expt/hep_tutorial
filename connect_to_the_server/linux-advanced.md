# Linux \(Advanced\)

## Useful commands

### sudo & su

我們可以透過以下指令進入root身份，



### ls

#### 計算檔案數量

此指令提供我們計算這個folder裡面的所有檔案的數量

```bash
ls -1 | wc -l
```

#### 了解list出來的資訊

我們在Linux \(Basic\)的章節討論過`ls -al`這些options，而我們要怎麼去看這些顯示出來的結果呢？

```bash
[metsai@lxplus070 ~]$ ls -al
總計 1164
drw-r--r--.  3 metsai zp     2048 2018-03-18 17:59 test
drwxr-xr-x.  3 metsai zp     2048 2017-07-10 11:51 tutorial
drwxr-xr-x.  6 metsai zp     2048 2016-11-29 15:51 tutorial_hww2016
-rw-r--r--.  1 metsai zp     4257 2018-10-01 07:24 UEHEBMeetings.html
-rwxrwxrwx.  1 metsai zp     3317 2018-04-20 10:44 usercert.pem
-rwxrwxrwx.  1 metsai zp     1958 2018-04-20 10:44 userkey.pem
```

### top

top指令能查詢server的使用狀況，包含CPU、記憶體以及他人對於此server的使用情況。

進入top查詢之後可以按q退出。

![&#x6B64;&#x5716;&#x4EE5;lxplus&#x70BA;&#x4F8B;](../.gitbook/assets/top.png)

### tar （打包\)

#### 打包：

```text
tar cvf FileName.tar DirName
```

**解包：**

```text
tar xvf FileName.tar
```

### ssh

\*\*\*\*[**Secure Shell**](https://zh.wikipedia.org/wiki/Secure_Shell)（安全外殼協定，簡稱**SSH**）是一種加密的[網路傳輸協定](https://zh.wikipedia.org/wiki/%E7%BD%91%E7%BB%9C%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)，可在不安全的網路中為網路服務提供安全的傳輸環境

### scp

scp指令主要是用來上傳本地檔案到server或是下載server檔案到本地。

* **上傳檔案到server**

我們以Lxplus為例，假設我們要在本地的電腦上傳一個叫`a.txt`的檔案，這個檔案的路徑位置在`/Users/ploww/ploww`，然後你想要把檔案上傳到Lxplus裡的這個位置`/afs/cern.ch/work/m/metsai`，以下指令我要在**本地**輸入來完成以上動作

```bash
scp /Users/ploww/ploww/a.txt youraccount@lxplus.cern.ch:/afs/cern.ch/work/m/metsai
```

* **下載server上的檔案到本地**

假設我們在server有一個檔案`/afs/cern.ch/work/m/metsai/a.txt`，然後我們想要把檔案從Lxplus下載到本地的位置`/Users/ploww/ploww`，以下指令我們要在**本地**輸入來完成以上動作

```bash
scp youraccount@lxplus.cern.ch:/afs/cern.ch/work/m/metsai/a.txt /Users/ploww/ploww 
```

* **下載或上傳一整個資料夾**

如果資料夾內的檔案很多，那他會對每個檔案一個一個下載，因此需要讀取每個檔案，下載或上傳一整個資料夾會**非常耗時**！因此我們可以先把**資料夾**[**打包**](linux-advanced.md#tar-da-bao)，然後再下載**打包後的資料夾 \(.tar\)。**

假設檔案在Lxplus上，因此我們在Lxplus的檔案位置打上以下指令並將資料夾打包

```bash
tar cvf FileName.tar DirName
```

回到我們的本機（自己的電腦），然後打上這個指令來下載這個打包後的資料夾

```text
scp youraccount@lxplus.cern.ch:/afs/cern.ch/work/m/metsai/FileName.tar ~
```

### ftp service

## Hand-on sessions

### 

