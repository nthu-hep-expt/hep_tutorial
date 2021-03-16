# Clusters and EOS

## Lxplus 

[Lxplus](https://lxplusdoc.web.cern.ch/lxplusdoc/) \(Linux Public Login User Service\) is the interactive logon service to Linux for all CERN users. 

#### **主要有幾個重要的位置，參考以下章節**

* Home directory \(10G\)
* Working directory \(100G\)：主要用來執行程式的位置
* EOS directory \(1TB\)：主要用來儲存dataset的位置

### Log in Lxplus with different systems

Log in Lxplus with CentOS CERN 7 \(CC7\) system

```bash
ssh yourAccount@lxplus.cern.ch​

# Example: metsai is my account name
ssh metsai@lxplus.cern.ch
```

{% hint style="warning" %}
注意，當他要求密碼，你打出的密碼並不會顯示在螢幕上，所以放心的輸入密碼，然後按下enter鍵。

```bash
# Then it will show up this kind of information and request the password, and enter you password and hit return.
Warning: Permanently added the ECDSA host key for IP address '2001:1458:d00:17::38c' to the list of known hosts.
Password: 
```
{% endhint %}

Log in Lxplus with Scientific Linux 6 \(SLC 6\) system

```bash
ssh yourAccount@lxplus6.cern.ch
```

#### Log in specific node of Lxplus 

For example, you can log in some specific node \(lxplus616\) by `ssh`

```
ssh yourAccount@lxplus616.cern.ch​
```

#### Login \(ssh/scp\) without password

You can follow the [instruction](https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Password-lessSsh) below.

```text
kinit <yourname>@CERN.CH
```

### Important paths in the Lxplus

#### Home directory

We have a **user** directory as your home directory in the Lxplus. For user directory, you only have 10 GB quota. The path of the **home directory** is 

```bash
/afs/cern.ch/user/<first letter of your account>/<account>
```

For example, if you account is _metsai_, the path will be  

```bash
/afs/cern.ch/user/m/metsai
```

#### Working directory

You can subscribe an additional working directory with 100 GB quota. The instruction is described [here](https://resources.web.cern.ch/resources/Help/?kbid=067040).  

```text
/afs/cern.ch/work/<first letter of your account>/<account>
```

For example, if you account is `metsai`, the path will be  

```bash
/afs/cern.ch/work/m/metsai
```

#### EOS space \(integrated with [CERNBox](https://cernbox.cern.ch/)\)

EOS space is mainly used to store the dataset and the limit of EOS space is 1 TB quota. The path to EOS space is 

```
/eos/user/<first letter of your account>/<account>
```

### Commands in the Lxplus

#### Setup for the ATLAS environment

You should initialize with the following command when you login every time

```bash
setupATLAS

# If the above is not working, please add the follows in ~/.bashrc
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
alias setupATLAS='source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh'

```

![&quot;setupATLAS&quot; initializes for the ATLAS environment](../.gitbook/assets/ying-mu-kuai-zhao-20190116-shang-wu-4.43.46.png)

#### Check the quota in user or working directory 

```bash
fs lq --human
```

## NTHU cluster

The IP of our cluster is **140.114.94.172.** To login to the cluster, you can use the following commands. For new students, please contact Jennifer. 

```bash
# login to the cluster with IP
ssh yourAccount@140.114.94.172

# Once you login to the cluster, you can access the other node #2~#4
ssh yourAccount@nthuhep02
ssh yourAccount@nthuhep03
ssh yourAccount@nthuhep04
```

## CERNBox and EOS

[CERNBox](https://cernbox.cern.ch/) corresponds to the [EOS space](lxplus.md#eos-space). You can also think the CERNBox as an online hard drive to store your files. The guideline of CERNBox is shown [here](https://cernbox.cern.ch/index.php/settings/help). 

### Sharing

It's not available to change the authorities of the files by `chmod` in the EOS space, instead, to share with others, we should **share** them with others by CERNBox. 

The followings are the instructions about sharing in the CERNBox. 

* We normally key in the full name of who you would like to share. It's because sometimes CERNBox cannot find people with only a part of the name.
* We can also share with e-groups.

![](../.gitbook/assets/ying-mu-kuai-zhao-20190611-xia-wu-4.56.59.png)

### Check quota of CERNBox/EOS space

* [Check quota with command line](https://cern.service-now.com/service-portal/article.do?n=KB0002979)
* Check quota in the CERNBox

![](../.gitbook/assets/ying-mu-kuai-zhao-20190611-xia-wu-4.54.22.png)

![](../.gitbook/assets/ying-mu-kuai-zhao-20190611-xia-wu-4.54.18.png)

### 

## Hand-on sessions

### Log in the Lxplus

We use `ssh` to log in the Lxplus. 

```
ssh yourAccount@lxplus.cern.ch​
```

Note that when you key in your password, _**your password will not be shown on your screen**_. 

![](../.gitbook/assets/ying-mu-kuai-zhao-20190608-shang-wu-3.47.48.png)

### Setup the ATLAS environment

```text
setupATLAS
```

#### Setup ROOT

In the Lxplus, we could use the ROOT in the ALTAS environment without installation which is discussed in the [ROOT section](../root/#root-installation). We can just use `lsetup` to setup ROOT

```text
lsetup root
```

However, currently we were required to use a specific version of ROOT. Therefore, here I use the recommended version of ROOT.

```bash
lsetup "root 6.14.04-x86_64-slc6-gcc62-opt" 
```

Then we can open ROOT by 

```bash
root
```

#### Displaying issue

When you open root, it will show an opening animation and this requires you to connect the server with X windows, what we've discussed in the [previous section](linux_basic.md#da-duan-terminal). If you didn't have X windows or you didn't connect the server with it, then you will get the following warning and not be able to used the windowing system.

```text
*** DISPLAY not set, setting it to 220-129-27-11.dynamic-ip.hinet.net:0.0
```

Please follow the hand-on session to [install X windows](linux_basic.md#install-x-windows). Then we should connect the Lxplus with the following command

```bash
ssh -X -Y yourAccount@lxplus.cern.ch​
```

which `-X` and `-Y` are used to enable X11 forwarding. You can look into details about these options by 

```bash
man ssh
```

If you still encounter the issue, you may use the following command

```text
export DISPLAY=:0.0
```

### 

