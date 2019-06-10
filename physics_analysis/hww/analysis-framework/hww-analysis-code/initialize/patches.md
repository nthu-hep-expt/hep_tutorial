# Patches

## Introduction

A detailed introduction is provided in the [gitlab page](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/config/patches/common/README.md). 

> TQFolder Patch Files allow to place additional information on a SampleFolder structure in the form of additional tags. They also provide a way to modify the SampleFolder structure itself, e.g, by moving, copying, deleting, or creating TQ\(Sample\)Folders and TQSamples. Applying these kind of files as 'patches' or 'patch files' usually implies that they are applied to the SampleFolder structure of an analysis. The syntax, however, can be used to modify any TQFolder structure.

In the VBF analysis, we use a default patch for HWW analysis in the initialize step. This patch provides us to define the structure of sample folder. 

{% code-tabs %}
{% code-tabs-item title="share/config/master/VBF/initialize-VBF-Coupling-2018.cfg" %}
```text
preInit_patches: config/patches/common/default-patch.txt
```
{% endcode-tabs-item %}
{% endcode-tabs %}

The following is the patch file used in the HWW analysis.

{% code-tabs %}
{% code-tabs-item title="config/patches/common/default-patch.txt" %}
```text
# -*- mode: tqfolder -*-
<channel = "mm", cand = "MM", isMM=true,  isEE=false, isEM=false, isME=false> @ ?/mm; # mm channel for data,bkg,sig
<channel = "ee", cand = "EE", isMM=false, isEE=true,  isEM=false, isME=false> @ ?/ee; # ee channel for data,bkg,sig
<channel = "em", cand = "EM", isMM=false, isEE=false, isEM=true,  isME=false> @ ?/em; # em channel for data,bkg,sig
<channel = "me", cand = "ME", isMM=false, isEE=false, isEM=false, isME=true > @ ?/me; # me channel for data,bkg,sig
<matchesSTXSbin = true> @ /.;
<isSF=true, isDF=false> @ ?/ee,?/mm;
<isSF=false, isDF=true> @ ?/em,?/me;
<isLeadE=true, isLeadM=false> @ ?/ee,?/em;
<isLeadE=false, isLeadM=true> @ ?/mm,?/me;
<isSubE=true, isSubM=false> @ ?/ee,?/me;
<isSubE=false, isSubM=true> @ ?/em,?/mm;
<wildcarded = true> @ ?/?; # we usually don't care about the channel-part of the path

# we want to apply mc event weights on MC samples
# this tag is used by the sample initializer
# to determine if it should extract bookkeeping info
<usemcweights = true> @ sig,bkg; # we want to apply mc event weights on MC samples
<usemcweights = false> @ data; # we don't want to apply any weights on data samples

<isData = true, isMC = false, variation="nominal"> @ data; # for data,revert the data/MC tags
<isData = false, isMC = true, variation="nominal"> @ sig,bkg;
<isDataDriven = false> @ /.;
<isDataFakes = false> @ /.;
<isDataFakes = true> @ /bkg/?/Wjets/?/data,/bkg/?/Wjets/data;
<name = 1> @ data,/bkg/?/Wjets/data;
<isVjets = true> @ /bkg/?/Zjets,/bkg/?/Wjets/?/mc/Zjets,/bkg/?/Wjets/mc/Zjets; #make sure to always account for both, merged and split running modes!
<isVjets = false> @ /.;
<isDataDrivenWjets = false> @ sig,bkg,data;
<isDataDrivenWjets = true, p4suffix=""> @ /bkg/?/Wjets;
<name = "data_wjets"> @ bkg/?/?/?/data,bkg/?/?/data;
@ bkg/?/Wjets/*/mc {
  #$modify(tag="name", path="bkg/?/?/?/mc/*", operator="+", value="_wjets");
  $modify(tag="name", path="*", operator="+", value="_wjets");
}
<name = "data"> @ /data/?/?;

<doWjetsSplit = true> @ /.;
<isWjets = false> @ /.;
<isWjets = true> @ /bkg/?/Wjets;
<isWjetsFakeMu = false> @ /.;
<isWjetsFakeEl = false> @ /.;
<isWjetsFakeMu = true> @ /bkg/?/Wjets/FakeM/;
<isWjetsFakeEl = true> @ /bkg/?/Wjets/FakeE/;
<isDDQCD = false> @ /.;
<isDDQCD = true> @ /bkg/?/Wjets/QCD/;
<isWjetsMC = false> @ /.;
<isWjetsMC = true> @ /bkg/?/Wjets/?/mc/Wjets/,/bkg/?/Wjets/mc/Wjets/;

#new ggF signal sample, use NNPDF nominal NNLO weight
<weightIndex = 151> @ /sig/?/mh125/ggf/345324_s;
<xAODCutBookKeeperContainer="StreamDAOD_HIGG3D1", xAODCutBookKeeperName="AllExecutedEvents_NonNominalMCWeight_151", xAODCutBookKeeperKernel="HIGG3D1Kernel"> @ /sig/?/mh125/ggf/345324_s;

<label="data"> @/data/;
<label="ggF"> @/sig/?/mh125/ggf;
<label="VBF"> @/sig/?/mh125/vbf;
<label="vh"> @/sig/?/mh125/vh;
<label="htt"> @/sig/?/mh125/htt;
<label="WW"> @/bkg/?/diboson/WW;
<label="otherVV"> @/bkg/?/diboson/NonWW;
<label="Zjets"> @/bkg/?/Zjets;
<label="singletop"> @/bkg/?/top/singletop;
<label="ttbar"> @/bkg/?/top/ttbar;
<label="Vgamma"> @/bkg/?/Vgamma;
<label="Wjets"> @bkg/?/Wjets;


###---------------------------------------------------------------------###
###------                    Collapse the plots                     ----###
###---------------------------------------------------------------------###
# <.aj.pool.histograms = true> @/sig/?/?/ggf/?;
# <.aj.pool.histograms = true> @/sig/?/?/vbf/?;
# <.aj.pool.histograms = true> @/sig/?/?/vh/?;
# <.aj.pool.histograms = true> @/sig/?/?/htt/?;
# <.aj.pool.histograms = true> @/data/?;
# <.aj.pool.histograms = true> @/bkg/?/top/ttbar/?/;
# <.aj.pool.histograms = true> @/bkg/?/top/ttbar/Sherpa/?/?;
# <.aj.pool.histograms = true> @/bkg/?/top/ttbar/MGLO/?/?;
# <.aj.pool.histograms = true> @/bkg/?/top/ttbar/MGNLO/?/?;
# <.aj.pool.histograms = true> @/bkg/?/top/singletop/?;
# <.aj.pool.histograms = true> @/bkg/?/Vgamma/?/?;
# <.aj.pool.histograms = true> @/bkg/?/diboson/WW/?/?;
# <.aj.pool.histograms = true> @/bkg/?/diboson/NonWW/?;
# <.aj.pool.histograms = true> @/bkg/?/Zjets/?/DY/?/?;
# <.aj.pool.histograms = true> @/bkg/?/Zjets/?/EW/?/?;
# <.aj.pool.histograms = true> @/bkg/?/Zjets/Sherpa2p2p1/?/?;
# <.aj.pool.histograms = true> @/bkg/?/WjetsSherpa2p2p1/?;
# <.aj.pool.histograms = true> @/bkg/?/WjetsPP/?;
# <.aj.pool.histograms = true> @/bkg/?/Wjets/FakeE/mc/?;
# <.aj.pool.histograms = true> @/bkg/?/Wjets/FakeE/data;
# <.aj.pool.histograms = true> @/bkg/?/Wjets/FakeM/mc/?;
# <.aj.pool.histograms = true> @/bkg/?/Wjets/FakeM/data;
# ### and counters
# <.aj.pool.counters = true> @/sig/?/?/ggf/?;
# <.aj.pool.counters = true> @/sig/?/?/vbf/?;
# <.aj.pool.counters = true> @/sig/?/?/vh/?;
# <.aj.pool.counters = true> @/sig/?/?/htt/?;
# <.aj.pool.counters = true> @/data/?;
# <.aj.pool.counters = true> @/bkg/?/top/ttbar/?/;
# <.aj.pool.counters = true> @/bkg/?/top/ttbar/Sherpa/?/?;
# <.aj.pool.counters = true> @/bkg/?/top/ttbar/MGLO/?/?;
# <.aj.pool.counters = true> @/bkg/?/top/ttbar/MGNLO/?/?;
# <.aj.pool.counters = true> @/bkg/?/top/singletop/?;
# <.aj.pool.counters = true> @/bkg/?/Vgamma/?/?;
# <.aj.pool.counters = true> @/bkg/?/diboson/WW/?/?;
# <.aj.pool.counters = true> @/bkg/?/diboson/NonWW/?;
# <.aj.pool.counters = true> @/bkg/?/Zjets/?/DY/?/?;
# <.aj.pool.counters = true> @/bkg/?/Zjets/?/EW/?/?;
# <.aj.pool.counters = true> @/bkg/?/Zjets/Sherpa2p2p1/?/?;
# <.aj.pool.counters = true> @/bkg/?/WjetsSherpa2p2p1/?;
# <.aj.pool.counters = true> @/bkg/?/WjetsPP/?;
# <.aj.pool.counters = true> @/bkg/?/Wjets/FakeE/mc/?;
# <.aj.pool.counters = true> @/bkg/?/Wjets/FakeE/data;
# <.aj.pool.counters = true> @/bkg/?/Wjets/FakeM/mc/?;
# <.aj.pool.counters = true> @/bkg/?/Wjets/FakeM/data;
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Syntax 

Here, we can define the variables \(tags\) we can used in the analysis. For example, we define the **channel** to select the lepton flavors.

{% code-tabs %}
{% code-tabs-item title="config/patches/common/default-patch.txt" %}
```text
<channel = "mm", cand = "MM", isMM=true,  isEE=false, isEM=false, isME=false> @ ?/mm; # mm channel for data,bkg,sig
<channel = "ee", cand = "EE", isMM=false, isEE=true,  isEM=false, isME=false> @ ?/ee; # ee channel for data,bkg,sig
<channel = "em", cand = "EM", isMM=false, isEE=false, isEM=true,  isME=false> @ ?/em; # em channel for data,bkg,sig
<channel = "me", cand = "ME", isMM=false, isEE=false, isEM=false, isME=true > @ ?/me; # me channel for data,bkg,sig
```
{% endcode-tabs-item %}
{% endcode-tabs %}

With this definition, we can use $\(channel\) as a variable to select the lepton flavors. 

## Pool

The pool will allow us to define where to produce the plots. 

{% code-tabs %}
{% code-tabs-item title="config/patches/common/default-patch.txt" %}
```text
<.aj.pool.histograms = true> @/sig/?/?/ggf/?;
<.aj.pool.histograms = true> @/sig/?/?/vbf/?;
```
{% endcode-tabs-item %}
{% endcode-tabs %}

With the pool shown, the plots will generate at the levels of those folder instead of generating plots in a more innermost level. 

