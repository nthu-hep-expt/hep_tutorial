# Initialize

## Introduction

![](../../../../../.gitbook/assets/ying-mu-kuai-zhao-20190610-xia-wu-8.13.10.png)

After `prepare`, the analysis continues with `initialize`**.**

### Tages

#### inputFile

We use the output file from `prepare` as the input file in the `initialize` step. Hence, we pass the input file by the tag `inputFile`.

```text
inputFile: sampleFolders/prepared/samples-prepared-VBF-default.root
```

#### outputFile

Same as prepare step, we will output a root file from `initialize` step, which will be used in the next step `analyze`.

```text
outputFile: sampleFolders/initialized/samples-initialized-VBF-default.root
```

```text

# paths and names of the input data files
dataFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-dataFileList.txt
dataFileListTreeName: CollectionTree
#dataPaths: /eos/user/d/dshope/forCAFExample/xAOD_Example/data/:CollectionTree
# additional input file configurations - these are already the defaults
#dataFilePattern: *.root*
#dataFolderPattern: data/$(channel)/all

# paths and names of the input mc files to initialize
mcFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-mcFileList.txt
mcFileListTreeName: CollectionTree
#mcPaths: /eos/user/d/dshope/forCAFExample/xAOD_Example/mc/:CollectionTree
# additional input file configurations - these are already the defaults
#mcFilenameSuffix: *.root*
#mcFilenamePrefix: *

# some debugging options for the sample initializer
# initialize: false
printSamplesFailed: true
verbose: true

# channels to run over
channels: ee,mm
channelPlaceholder: channel

# preInit patch files to apply
preInit_patches: config/patches/ZjetsFF/ZjetsFakeFactor-default-patch.txt

# postInit patch files to apply
#postInit_patches: 

```

### Run with samples

We have several ways to run with our samples. We could run with the given lists or run with the samples inside some certain folders. Here we show two ways:

#### File list

We use the file list to pass the samples we would like to run.

```
dataFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-dataFileList.txt
dataFileListTreeName: CollectionTree
mcFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-mcFileList.txt
mcFileListTreeName: CollectionTree
```

#### **Data path**

We use the data path to run all the samples inside the folder. The following show an example path.

```text
dataPaths: /eos/user/d/dshope/forCAFExample/xAOD_Example/data/:CollectionTree
```

### 

### Include the patch \(style\) for the  TQSampleFolder

```text
preInit_patches: config/patches/ZjetsFF/ZjetsFakeFactor-default-patch.txt
```

In the patch file, we define the labels and tags for the TQSampleFolder

{% code-tabs %}
{% code-tabs-item title="config/patches/ZjetsFF/ZjetsFakeFactor-default-patch.txt" %}
```text
# -*- mode: tqfolder -*-

<channel = "mm", cand = "MM", isMM=true,  isEE=false, isEM=false, isME=false> @ ?/mm; # mm channel for data,bkg,sig
<channel = "ee", cand = "EE", isMM=false, isEE=true,  isEM=false, isME=false> @ ?/ee; # ee channel for data,bkg,sig
<channel = "em", cand = "EM", isMM=false, isEE=false, isEM=true,  isME=false> @ ?/em; # em channel for data,bkg,sig
<channel = "me", cand = "ME", isMM=false, isEE=false, isEM=false, isME=true > @ ?/me; # me channel for data,bkg,sig
<isSF=true, isDF=false> @ ?/ee,?/mm;
<isSF=false, isDF=true> @ ?/em,?/me;
<isLeadE=true, isLeadM=false> @ ?/ee,?/em;
<isLeadE=false, isLeadM=true> @ ?/mm,?/me;
<isSubE=true, isSubM=false> @ ?/ee,?/me;
<isSubE=false, isSubM=true> @ ?/em,?/mm;
<wildcarded = true> @ ?/?; # we usually don't care about the channel-part of the path
<isData = true, isMC = false, variation="nominal"> @ data; # for data,revert the data/MC tags
<isData = false, isMC = true, variation="nominal"> @ sig,bkg;
<isVjets = false> @ sig,bkg,data;
<isVjets = true> @ /bkg/?/Zjets;

# we want to apply mc event weights on MC samples
# this tag is used by the sample initializer
# to determine if it should extract bookkeeping info
<usemcweights = true> @ sig,bkg; # we want to apply mc event weights on MC samples
<usemcweights = false> @ data; # we don't want to apply any weights on data samples

# Sherpa WZ normalisation = 1.15
$modify(tag='.xsp.xSecScale',operator='=',value=1.15,path='bkg/?/diboson/NonWW/qq/WZgammaStar/*',filter='s',create=true);
```
{% endcode-tabs-item %}
{% endcode-tabs %}

