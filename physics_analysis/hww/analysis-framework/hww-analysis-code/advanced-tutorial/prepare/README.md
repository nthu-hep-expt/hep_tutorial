# Prepare

## Introduction

We use the config file for VBF HWW coupling analysis for discussion.  

```bash
# Run in the share folder
./prepare.py config/master/VBF/prepare-VBF-Coupling-2018.cfg
```

In general, the setup is similar as the [example](../../prepare/).

{% code-tabs %}
{% code-tabs-item title="share/config/master/VBF/prepare-VBF-Coupling-2018.cfg" %}
```text
# -*- mode: config -*-

[prepare]

# name of the output file
outputFile:  sampleFolders/prepared/samples-prepared-VBF-Coupling-2018.root

# input DSIDs (whitelisted and and mapped)
XsecFiles: config/samples/XSec/common/XS_13TeV.csv
### At the moment we use the same for ggF and VBF
XsecWhitelist: config/samples/whitelists/ggF/ggF-whitelist-v17b.txt
XsecMap: config/samples/maps/common/run2-mc15.map
XsecUnit: nb

# channels to run over
channels: em,me
channelPlaceholder: channel

# energy and luminosity
luminosity: 36074.56
#after badBatman flag:
#luminosity: 35551.7
luminosityUnit: pb
energy: 13
#energyUnit: TeV

# patch files to apply
#patches: 

```
{% endcode-tabs-item %}
{% endcode-tabs %}

For the XsecWhitelist, we use the `config/samples/whitelists/ggF/ggF-whitelist-v17b.txt`because we will use the same samples for both ggF and VBF in the full Run-2 analysis. The `v17b` is the version which we used to produce the first Run-2 HWW publication. This whitelist may change a bit when the analysis progress. But, at this moment, we could use this to produce the results to validate the analysis between Release 20.7 and Release 21 samples



