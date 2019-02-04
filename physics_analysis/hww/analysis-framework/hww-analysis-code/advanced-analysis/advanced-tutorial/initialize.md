# Initialize

## Introduction

The [config file](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/config/master/VBF/initialize-VBF-Coupling-2018.cfg) for the initialize step is shown below. 

{% hint style="warning" %}
### Warning!

In the following file, I modified the paths for samples to run with V18 PAOD samples. 
{% endhint %}



{% code-tabs %}
{% code-tabs-item title="share/config/master/VBF/initialize-VBF-Coupling-2018.cfg" %}
```text
# -*- mode: config -*-

[initialize]

# name of the input file
inputFile: sampleFolders/prepared/samples-prepared-VBF-Coupling-2018.root

# name of the output file
outputFile: sampleFolders/initialized/samples-initialized-VBF-Coupling-2018.root

# paths and names of the input data files
dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18/2LDF/data/:CollectionTree
mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18/2LDF/mc/:CollectionTree

doDDfakes: False

purgeSamples: true

printSamplesFailed: true
verbose: true

# channels to run over
channels: em,me
channelPlaceholder: channel

# preInit patch files to apply
preInit_patches: config/patches/common/default-patch.txt
```
{% endcode-tabs-item %}
{% endcode-tabs %}

