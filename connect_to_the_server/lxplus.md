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

#### Login \(ssh/scp\) without password

You can follow the [instruction](https://twiki.atlas-canada.ca/bin/view/AtlasCanada/Password-lessSsh) below.

```text
kinit <yourname>@CERN.CH
```

Then do the following steps.

* Create a key and enter a password \(It is dangerous to not use a passphrase for shell accounts. Your only protection is your passphrase. This is particularly important for laptops.\).  


  ```text
      ssh-keygen -t rsa 
  ```

  Note that the default key file will be id\_rsa and id\_rsa.pub but you can create it with a different name \(in case you need different keys for different remote hosts but try not to do that unless you have good reason !\) by adding the option `-f ~/.ssh/<filename>`.

* Copy the public key to your remote machine; replace &lt;username&gt; and &lt;remote machine name&gt; below.

```text
    ssh-copy-id <username>@<remote machine name>
```

* After copying the above public key to lxplus, login to lxplus and type `/afs/cern.ch/project/svn/dist/bin/set_ssh`. This will fix the acl permissions of the file on lxplus.
* Create a file ~/.ssh/config with the following information \(there is a template you can copy from `$ATLAS_LOCAL_ROOT_BASE/user/sshConfig`\).
  * If your lxplus username is different from your local account, add a "User &lt;your lxplus username&gt;" to the lxplus, git and svn sections.

```text
Host svn.cern.ch svn 
GSSAPIAuthentication yes 
GSSAPIDelegateCredentials yes 
Protocol 2 
ForwardX11 no

Host gitlab.cern.ch
GSSAPIAuthentication yes 
GSSAPIDelegateCredentials yes 
Protocol 2 
ForwardX11 no

Host lxplus*.cern.ch lxplus lxplus*
Protocol 2 
GSSAPIAuthentication yes 
GSSAPIDelegateCredentials yes 
PubkeyAuthentication no 
ForwardX11 yes

Host *
  Protocol 2
  AddKeysToAgent yes   
  IdentityFile ~/.ssh/id_rsa
  ServerAliveInterval 120
```

Make sure the permissions of the ~/.ssh directory and its contents have permissions set correctly; an example is

```text
  chmod 700 ~/.ssh
  chmod 600 ~/.ssh/id_rsa
  chmod 644 ~/.ssh/config ~/.ssh/id_rsa.pub
```

Finally, when you open a new terminal, you probably need to kinit again. 

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

Moreover, the EOS space is integrated with [CERNBox](https://cernbox.cern.ch/). More information about CERNBox are listed [here](). 

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

### Subscribe working directory

Please follow the [instruction](https://resources.web.cern.ch/resources/Help/?kbid=067040) to subscribe working directory since normally the accumulated output root and histogram files will be large.

