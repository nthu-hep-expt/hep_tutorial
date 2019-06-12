# Initialize

## Introduction

![](../../../../../.gitbook/assets/ying-mu-kuai-zhao-20190610-xia-wu-8.13.10.png)

After `prepare`, the analysis continues with `initialize`**.** 

### Tags

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

#### Campaigns

This is same as we introduced in the [prepare](../prepare/#campaigns) step.

#### Fake estimation

If you're not working on the fake estimation, you normally don't need to care about this. 

```text
#--------------------------------------------------------------
# Fake configuration
doDDfakes: true
ddFakes.baseFolderName: ddFakes
# subfolders living inside above folder, each one will carry around its own full copy of data and mc.
# intended to enable split up, e.g. in e-fakes and mu-fakes. You can also comment this line out completely,
# which means no subfolders are created (you get only the base folder)
ddFakes.subFolderNames: eFakes,mFakes,doubleFakes
# mc processes to be ignored in the EW subtraction (i.e. folders with these names will not be copied)
ddFakes.mcFoldersToVeto: Wjets
# if there's already a mc sample in the bkg folder with the same name as base bkg folder given above,
# it will be removed unless you flag true here (then, it will be saved under bkg/?/<process>MC/)
#makeSampleFile.ddFakes.keepMCBkg: false
```

The only think you should notice here is that you can close the fake estimation by 

```text
doDDfakes: false
```

#### Debug setting

```text
printSamplesFailed: true
verbose: true
```

#### Patches

Patches provide the style for the TQSampleFolder as described [here](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/tree/master/share/config/patches/common#tqfolder-patches). 

> TQFolder Patch Files allow to place additional information on a SampleFolder structure in the form of additional tags. They also provide a way to modify the SampleFolder structure itself, e.g, by moving, copying, deleting, or creating TQ\(Sample\)Folders and TQSamples.

```text
preInit_patches: config/patches/common/default-patch.txt
```

