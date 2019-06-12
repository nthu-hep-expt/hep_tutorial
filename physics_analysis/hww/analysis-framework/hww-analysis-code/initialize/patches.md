# Patches

## Introduction

A detailed introduction is provided in the [gitlab page](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/config/patches/common/README.md). 

> TQFolder Patch Files allow to place additional information on a SampleFolder structure in the form of additional tags. They also provide a way to modify the SampleFolder structure itself, e.g, by moving, copying, deleting, or creating TQ\(Sample\)Folders and TQSamples. Applying these kind of files as 'patches' or 'patch files' usually implies that they are applied to the SampleFolder structure of an analysis. The syntax, however, can be used to modify any TQFolder structure.

In the HWW analysis, we use a default patch for HWW analysis in the `initialize` step. This patch provides us to define the structure of sample folder. 

```text
preInit_patches: config/patches/common/default-patch.txt
```

Here I will discuss some syntaxes used in the [patch file](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/config/patches/common/default-patch.txt).

### Syntax 

Here, we can define the labels, as whatever you call, we can use in the analysis. For example, we define the **`channel`** to select the lepton flavors.

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

With this definition, we can use `$(channel)` as a variable to select the lepton flavors in the cut file. This is same as `label` in the patch file to select processes we want.Then we can use `$(label)` to select events.

{% code-tabs %}
{% code-tabs-item title="config/patches/common/default-patch.txt" %}
```text
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
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Here we define the labels for the same-flavor \(SF\) and different-flavor \(DF\) samples

```text
<isSF=true, isDF=false> @ ?/ee,?/mm;
<isSF=false, isDF=true> @ ?/em,?/me;
<isLeadE=true, isLeadM=false> @ ?/ee,?/em;
<isLeadE=false, isLeadM=true> @ ?/mm,?/me;
<isSubE=true, isSubM=false> @ ?/ee,?/me;
<isSubE=false, isSubM=true> @ ?/em,?/mm;
```

#### MC weight

We apply mc event weights on MC samples including both signal and background samples. It will no MC weight applied in the data!

{% code-tabs %}
{% code-tabs-item title="config/patches/common/default-patch.txt" %}
```text
<usemcweights = true> @ sig,bkg; # we want to apply mc event weights on MC samples
<usemcweights = false> @ data; # we don't want to apply any weights on data samples
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### Pool

The pool will allow us to define where to produce the plots and collect the events in the plots.

{% code-tabs %}
{% code-tabs-item title="config/patches/common/default-patch.txt" %}
```text
<.aj.pool.histograms = true> @/sig/?/?/ggf/?;
<.aj.pool.histograms = true> @/sig/?/?/vbf/?;
```
{% endcode-tabs-item %}
{% endcode-tabs %}

With the pool shown, the plots will generate at the levels of those folder instead of generating plots in a more innermost level. If we collapse the events in the outer level, then we can **save the storages and memories** used in the sample folder. 

