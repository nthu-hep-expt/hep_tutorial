# Prepare \(Basic\)

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
XsecWhitelist: config/samples/whitelists/ZjetsFF/ZjetsFakeFactor-whitelist.txt
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

The `XsecMap` will define the structure in the `SampleFolder`. 

```text
XsecMap: config/samples/maps/ZjetsFF/ZjetsFakeFactor.map
```

The example of map file:

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

### Channel

Since we have same flavors \($$ee$$ , $$\mu\mu$$\) and different flavors \($$e\mu$$ , $$\mu e$$\) final states in the $$H\rightarrow WW^*\rightarrow\ell\nu\ell\nu$$ analysis, we separate our structure of SampleFolder to run over different channels. We can select the channels with the following config:

* For same flavor final states

```text
channels: ee, mm
```

* For different final states

```text
channels: em, me
```

### Energy and luminosity

For our first Run-2 HWW analysis, we use about $$\textrm{36 }fb^{-1}$$ data samples. The luminosity here is $$\textrm{36074.56 } nb^{-1}$$. For our full Run-2 analysis, we will have about $$\textrm{150 }fb^{-1}$$data samples.

```text
luminosity: 36074.56
luminosityUnit: pb
energy: 13
```

### VeryLoose

## Hand-on sessions

#### Run with only VBF sample

If you only want to run the VBF sample with DSID `345948`, then what we could do is to use a `whitelist` file with only this DSID.

So, we could create a new `whitelist` file called, whatever you like, 

```text
config/samples/whitelists/VBF/VBF-only-whitelist.txt
```

Then in this `VBF-only-whitelist.txt`, we should include only VBF DSID as the following

```text
## SM VBF HWW
345948 $*_s*
```

Now, the whole analysis will run over only the sample with DSID 345948.



