# Prepare

## Introduction

`Prepare` is the first step to run the analysis. We take the PxAOD samples as inputs, and then `prepare` them to become samples stored in the `SampleFolder`.

In the following, I will briefly introduce the tags we frequently used in the `prepare` configuration file. 

### Tags

#### outputfile

Designate your path and name of output sample folder.

```text
outputFile:  sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root
```

#### XsecFiles

The `XsecFiles` list the informations of Monte-Carlo \(MC\) simulated samples including DSIDs, cross-sections \(Xsec\), k-factors and MC generators. More details are shown in the [subsection](xsec-files.md). 

```text
XsecFiles: config/samples/XSec/common/XS_13TeV.csv
```

#### XsecWhitelist

The `XsecWhitelist` will determine what samples you would like to analyze in the analysis. 

```text
XsecWhitelist: config/samples/whitelists/ggF/ggF-whitelist-v19.txt
```

In the `whitelist` file, it mainly contains the DSIDs of samples. The format of `whitelist` file are introduced in the [official repository](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/config/samples/whitelists/common/README.md). 

```text
# Powheg Z
361106 $*_s*
361107 $*_s*
361108 $*_s*

#Alpgen Z
361700 $*_s*
361701 $*_s*
361702 $*_s*
361703 $*_s*
```

#### XsecMap

The `XsecMap` will define the structure in the `SampleFolder`. The description and introduction for the usage is shown in the [gitlab](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/tree/master/share/config/samples/maps/common). 

```text
XsecMap: config/samples/maps/common/run2-mc16.map
```

The example of map file is shown below. The numbers shown here are the DSIDs. Moreover, the following paths define the structure of sample folders.

```text
##Powheg Z+jets
361106 /bkg/$(channel)/Zjets_Powheg/ee/
361107 /bkg/$(channel)/Zjets_Powheg/mm/
361108 /bkg/$(channel)/Zjets_Powheg/tt/

##Alpgen Z+jets
361700 /bkg/$(channel)/Zjets_Alpgen/ee/
361701 /bkg/$(channel)/Zjets_Alpgen/ee/
361702 /bkg/$(channel)/Zjets_Alpgen/ee/
```

#### Channel

In the HWW analysis wit leptonic decays, we have same flavors \(ee, μμ\) and different flavors \(eμ, μe\) final states. We can select the channels with the following configuration

Setup this before using `channel` 

```text
channelPlaceholder: channel
```

* For same flavor final states

```text
channels: ee, mm
```

* For different final states

```text
channels: em, me
```

#### Energy and luminosity

In our first Run-2 HWW publication, we use 36 fb^-1 data samples. In the legacy paper, we will have about 150 fb^-1data samples.

```text
luminosity: 36074.56
luminosityUnit: pb
energy: 13
```

#### Campaigns

With the full Run-2 dataset collected from 2015 to 2018, we have several campaigns for the MC simulated samples corresponding to the year of data. 

| data | MC samples |
| :--- | :--- |
| data15+data16  | mc16a |
| data17 | mc16d |
| data18 | mc16e |

```text
#import options specific to different campaigns and announce the ones that should be processed
campaignsConfig: config/master/common/campaigns.cfg
campaigns: c16a,c16d,c16e
```

The campaigns are stored and organized in our group disk.

{% code-tabs %}
{% code-tabs-item title="config/master/common/campaigns.cfg" %}
```text
[c16a]
luminosity: 36207.66
dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data1516/:CollectionTree
mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16a/:CollectionTree
# Note, in v19 the 'standard' and fake inputs are the same
ddFakes.dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data1516/:CollectionTree
ddFakes.mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16a/:CollectionTree

[c16d]
luminosity: 44307.40
dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data17/:CollectionTree
mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16d/:CollectionTree
ddFakes.dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data17/:CollectionTree
ddFakes.mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16d/:CollectionTree

[c16e]
luminosity: 58450.10 
dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data18/:CollectionTree
mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16e/:CollectionTree
ddFakes.dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data18/:CollectionTree
ddFakes.mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16e/:CollectionTree
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Hand-on sessions

#### Run with only one sample

If you only want to run only some specific sample, said the VBF sample with DSID `345948`, then what we could do is to input a `whitelist` file containing only this DSID. So, we could create a new `whitelist` file called, whatever you like, 

```text
config/samples/whitelists/VBF/VBF-only-whitelist.txt
```

Then in this `VBF-only-whitelist.txt`, we should include only VBF DSID as the following

{% code-tabs %}
{% code-tabs-item title="config/samples/whitelists/VBF/VBF-only-whitelist.txt" %}
```text
## SM VBF HWW
345948 $*_s*
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Then we should modify the `whitelist` file in the `prepare` configuration file with the following tag.

```text
XsecWhitelist: config/samples/whitelists/VBF/VBF-only-whitelist.txt
```

Now, the whole analysis will run over only the sample with DSID 345948.



