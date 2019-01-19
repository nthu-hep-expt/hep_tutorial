# For Beginner

The [HWW Analysis Code](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode) provides an example analysis on xAOD inputs. In the following sections, we will give detailed explanations for the steps to run the analysis.

## Cloning the analysis framework

Since PxAOD samples are normally stored in the EOS space, we should use the lxplus to analyze samples. After login the lxplus, we could follow the steps below to run with the example analysis.

{% hint style="warning" %}
The following steps may be out of date. So, please also check the steps shown in this [README.md](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/README.md) for the correct setups.
{% endhint %}

The first step to run with the analysis is to setup the ATLAS environment and make a new directory for your analysis codes. Then clone \(download!\) the repository with **git clone.** 

```bash
# setup the ATLAS environment
setupATLAS

# setup the git 
lsetup git

# make a new directory for your analysis code and move into the directory
mkdir HWWAnalysis
cd HWWAnalysis

# Then clone (download) the repository 
# --recursive is an option to clone all the things in the directory
git clone --recursive https://:@gitlab.cern.ch:8443/atlas-physics/higgs/hww/HWWAnalysisCode.git
```

Once we have the analysis framework, we should build \(compile\) the analysis framework. The introduction of command **'make'** can be found [here](https://www.tutorialspoint.com/unix_commands/make.htm). 

```bash
# 'build' is the directory where you store your compiled codes
# 'run' is the place where you should run in 
mkdir build run

# move to 'build' and build your analysis framework
cd build
asetup AnalysisBase,21.2.49
cmake ../HWWAnalysisCode

# setup the environment for the analysis framework
source ../HWWAnalysisCode/setup/setupAnalysis.sh

# compile 
# -j specifies the number of jobs (commands) to run simultaneously
# -j4 means to use 4 jobs to run simultaneously
make -j4

```

## Running the example analysis

After building your framework, we could first run the example analysis with the following steps. You can run in the **'share'** directory. 

```bash
cd ../HWWAnalysisCode/share
./prepare.py config/master/ZjetsFF/prepare-ZjetsFakeFactor-Coupling-2018.cfg
./initialize.py config/master/ZjetsFF/initialize-ZjetsFakeFactor-Coupling-2018.cfg
./analyze.py config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg
./visualize.py config/master/ZjetsFF/visualize-ZjetsFakeFactor-Coupling-2018.cfg
```

We have four steps shown below. Normally, we don't need to modify these four python files. Instead, we should change the **config files** to change the setups we would like to run. 

* [prepare.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/prepare.py):  setup basic **SampleFolder** \(SF\) structure.
* [initialize.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/initialize.py): discover samples and read Meta-Info \(sumOfWeights\).
* [analyze.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/analyze.py): analyze individual events as well as book histograms  yields.
* [visualize.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/visualize.py): Draw the histograms and cutflow tables.

The following table summarizes the usage of these four steps. This table is from [Ralf's slides](https://indico.cern.ch/event/771763/contributions/3207844/attachments/1767899/2871281/caf_tutorial_concepts.pdf) in the CAF tutorial.

![](../../../../.gitbook/assets/ying-mu-kuai-zhao-20190119-xia-wu-8.46.07.png)

## Physics with config files

In this section, we will explain the setups in the config files in different steps. We used [configparser](https://docs.python.org/3/library/configparser.html) in the config file to interact with python files. 

### Prepare

The analysis starts with "**prepare**". We will explain the "**tag**" used in the config files. 

{% code-tabs %}
{% code-tabs-item title="config/master/ZjetsFF/prepare-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
# -*- mode: config -*-

[prepare]

# name of the output file
outputFile:  sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root

# input DSIDs (whitelisted and and mapped)
XsecFiles: config/samples/XSec/common/XS_13TeV.csv
XsecWhitelist: config/samples/whitelists/ZjetsFF/ZjetsFakeFactor-whitelist.txt
XsecMap: config/samples/maps/ZjetsFF/ZjetsFakeFactor.map
XsecUnit: nb



# Book the map which will define your structure in the SampleFolder
XsecMap: config/samples/maps/ZjetsFF/ZjetsFakeFactor.map
XsecUnit: nb

# channels to run over
# Since we have same flavor (ee, mm) and different flavor (em, me)
# df means the em+me channels
# channels: ee,mm,em,me,df

channels: ee,mm
channelPlaceholder: channel

# energy and luminosity
# For the Run-2 HWW analysis, we use 36.1 fb-1 data
# Therefore, the luminosity here is 36074.56
# For the full Run-2 analysis, we will have about 150 fb-1

luminosity: 36074.56
luminosityUnit: pb
energy: 13
#energyUnit: TeV

# patch files to apply
#patches: 

```
{% endcode-tabs-item %}

{% code-tabs-item title=undefined %}
```

```
{% endcode-tabs-item %}
{% endcode-tabs %}

First, the **outputfile** is a tag for the config file. we could book what output file we would like to create. The name and the path we would like to create.

{% code-tabs %}
{% code-tabs-item title="config/master/ZjetsFF/prepare-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
outputFile:  sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root
```
{% endcode-tabs-item %}
{% endcode-tabs %}

The **XsecFiles** \(XS\_13TeV.csv\) lists all the informations for the samples including the DSID, cross-sections, k-factors and MC generators.

{% code-tabs %}
{% code-tabs-item title="config/master/ZjetsFF/prepare-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
XsecFiles: config/samples/XSec/common/XS_13TeV.csv
```
{% endcode-tabs-item %}
{% endcode-tabs %}

The **XsecWhitelist** \(ZjetsFakeFactor-whitelist.txt\) is to determine which samples you would like to run. 

```text
XsecWhitelist: config/samples/whitelists/ZjetsFF/ZjetsFakeFactor-whitelist.txt
```

