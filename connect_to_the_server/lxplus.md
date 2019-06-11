# Lxplus

## Introduction 

[Lxplus](https://lxplusdoc.web.cern.ch/lxplusdoc/) \(Linux Public Login User Service\) is the interactive logon service to Linux for all CERN users. We normally work with Lxplus since the environments in the Lxplus are finely set with the ATLAS experiment. It could interact to the eos system and CERNBox, which are used to stored dataset. 

### Working in the Lxplus  

Once you have CERN account, we can access the Lxplus by the following commands:

#### Log in Lxplus with different systems

Log in Lxplus with CentOS CERN 7 \(CC7\) system

```bash
ssh yourAccount@lxplus.cern.ch​
```

Log in Lxplus with Scientific Linux 6 \(SLC 6\) system

```bash
ssh yourAccount@lxplus6.cern.ch
```

#### Log in specific node of Lxplus 

For example, you can log in some specific node \(lxplus616\) by `ssh`

```
ssh yourAccount@lxplus616.cern.ch​
```

### Quota in the Lxplus

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

For example, if you account is _metsai_, the path will be  

```bash
/afs/cern.ch/work/m/metsai
```

#### EOS space

We will have an EOS space with 1 TB quota, which is mainly used as a space to store samples. The path to EOS space is 

```
/eos/user/<first letter of your account>/<account>
```

Moreover, the EOS space is integrated with [CERNBox](https://cernbox.cern.ch/). More information about CERNBox are listed [here](cernbox.md). 

### Commands in the Lxplus

#### Setup for the ATLAS environment

You should initialize with the following command when you login every time

```bash
setupATLAS
```

![&quot;setupATLAS&quot; initializes for the ATLAS environment](../.gitbook/assets/ying-mu-kuai-zhao-20190116-shang-wu-4.43.46.png)

To interact with GitHub or GitLab, we should initialize your git environment by

```bash
lsetup git
```

If you would like to use the grid system, we should setup the local panda client by

```text
localSetupPandaClient
```

#### Useful commands

* Check the quota in user or working directory 

```bash
fs lq --human
```

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

### Subscribe working directory

