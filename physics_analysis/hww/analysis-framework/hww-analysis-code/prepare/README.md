# Prepare \(Basic\)

## Introduction

### Tags

#### outputfile

Designate your path and name of output folder.

```text
outputFile:  sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root
```

#### XsecFiles

The `XsecFiles` list the informations of Monte-Carlo \(MC\) simulated samples including DSIDs, cross-sections \(Xsec\), k-factors and MC generators. More details are shown in the [subsection](xsec-files.md). 

```text
XsecFiles: config/samples/XSec/common/XS_13TeV.csv
```

### XsecWhitelist

The XsecWhitelist will determine the samples you would like to run. 

```text
XsecWhitelist: config/samples/whitelists/ZjetsFF/ZjetsFakeFactor-whitelist.txt
```

The example of whitelist provides the DSID which you would like to run. Therefore, if you add the only the following DSID, you can only use the following samples in the further steps. 

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

### XsecMap

The XsecMap will define the structure in the SampleFolder. 

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

