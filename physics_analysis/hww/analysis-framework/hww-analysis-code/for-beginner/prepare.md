# Prepare

The analysis starts with **prepare** and the tags will be discussed later.

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

#### outputfile

First, the outputfile is a tag for the config file. we could book what output file we would like to create. 

```text
outputFile:  sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root
```

#### XsecFiles

The XsecFiles list all the informations for the samples including the DSID, cross-sections, k-factors and MC generators. 

```text
XsecFiles: config/samples/XSec/common/XS_13TeV.csv
```

The example of XsecFiles:

```text
SampleID , xsection , kfactor , filtereff , uncertainty , mh , generator , process , simulation

# SM ggf
341079, 0.0011020, 1.0, 4.9150E-01, --, 125,  Powheg+Pythia8+EvtGen, PowhegPythia8EvtGen_CT10_AZNLOCTEQ6L1_ggH125_WWlvlv_EF_15_5,  OFLCOND-RUN12-SDR-30
## Not Added to the whitelist yet - issue with weights
345324, 0.0011020, 1.0, 4.9318E-01, --, 125,  Powheg+Pythia8+EvtGen, PowhegPythia8EvtGen_NNLOPS_NN30_ggH125_WWlvlv_EF_15_5,  OFLCOND-RUN12-SDR-30
345339, 0.0011020, 1.0, 2.1808E-01, --, 125,  MadGraph+Pythia8+EvtGen, MadGraphPythia8EvtGen_A14NNPDF23LO_ggfhwwlnulnuNp2,  OFLCOND-RUN12-SDR-30

```

#### XsecWhitelist

The XsecWhitelist is to determine which samples you would like to run. 

```text
XsecWhitelist: config/samples/whitelists/ZjetsFF/ZjetsFakeFactor-whitelist.txt
```

The example of whitelist provide the DSID which you would like to run.

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

The XsecMap will define the structure in the SampleFolder

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

