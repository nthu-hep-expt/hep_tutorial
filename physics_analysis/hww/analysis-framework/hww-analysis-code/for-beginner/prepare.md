# Prepare

## Introduction

The analysis starts with **prepare** and the tags in config file will be discussed later.

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

# channels to run over
channels: ee,mm
channelPlaceholder: channel

# energy and luminosity
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

### outputfile

We could create the output file with the following config and tag. 

```text
outputFile:  sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root
```

### XsecFiles

The XsecFiles will list the informationss for the Monte-Carlo \(MC\) simulated samples including DSIDs, cross-sections \(Xsec\), k-factors and MC generators. 

```text
XsecFiles: config/samples/XSec/common/XS_13TeV.csv
```

The example of a cross-section file is shown below:

```text
SampleID , xsection , kfactor , filtereff , uncertainty , mh , generator , process , simulation

# SM ggf
341079, 0.0011020, 1.0, 4.9150E-01, --, 125,  Powheg+Pythia8+EvtGen, PowhegPythia8EvtGen_CT10_AZNLOCTEQ6L1_ggH125_WWlvlv_EF_15_5,  OFLCOND-RUN12-SDR-30
345324, 0.0011020, 1.0, 4.9318E-01, --, 125,  Powheg+Pythia8+EvtGen, PowhegPythia8EvtGen_NNLOPS_NN30_ggH125_WWlvlv_EF_15_5,  OFLCOND-RUN12-SDR-30
345339, 0.0011020, 1.0, 2.1808E-01, --, 125,  MadGraph+Pythia8+EvtGen, MadGraphPythia8EvtGen_A14NNPDF23LO_ggfhwwlnulnuNp2,  OFLCOND-RUN12-SDR-30
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

