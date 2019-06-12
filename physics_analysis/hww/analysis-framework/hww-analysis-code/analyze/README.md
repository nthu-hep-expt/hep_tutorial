# Analyze

## Introduction

![](../../../../../.gitbook/assets/ying-mu-kuai-zhao-20190610-xia-wu-8.13.21.png)

The `analyze` step is followed by the `initialize` ****step.

The analyze config file is shown below.

```text
# define the cuts
cuts: config/cuts/ZjetsFF/ZjetsFakeFactor-cuts.def

#patches: 

# add any observables
customObservables.directories: observables/common,observables/ZjetsFF
customObservables.snippets: HWWweight, HWWLeptonIDObservable, PassWZVeto, HWWZBosonPairFakeIndex, HWWInvMass2L

# book histograms
histograms: config/histograms/ZjetsFF/ZjetsFakeFactor-histograms.txt

# include aliases
[config]
include: config/aliases/ZjetsFF/ZjetsFakeFactor-aliases.cfg
```

#### inputFile and outputFile

These are same as the [tags](../initialize/#inputfile) introduced before. 

#### channels

We have four options for the channels including same-flavor final states, `ee` and `μμ`, as well as different flavor final states, `eμ` and `μe`.

#### cuts

In this `analyze` step, we include the cut files, which are used to define cuts to select events, in the configuration file. More details are introduced in the [subsection](cuts.md). 

```text
cuts: config/cuts/common/default-couplings.def, config/cuts/VBF/VBF.def
```





### Observables

The observables are the variables to measure the kinematic distributions for events. We book observables in this analyze config file. 

{% code-tabs %}
{% code-tabs-item title="share/config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
customObservables.directories: observables/common,observables/ZjetsFF
customObservables.snippets: HWWweight, HWWLeptonIDObservable, PassWZVeto, HWWZBosonPairFakeIndex, HWWInvMass2L
```
{% endcode-tabs-item %}
{% endcode-tabs %}

We take an example observable snippet in the following. We can have an overview of how an observable snippet looks like. We will have a more complete description in the [observable](observables.md) section.

{% code-tabs %}
{% code-tabs-item title="share/observables/ZjetsFF/HWWInvMass2L.py" %}
```python
from QFramework import TQObservable,INFO,ERROR,BREAK
from HWWAnalysisCode import HWWInvMass2L

def addObservables(config):
  INFO("adding invariant mass observable")
  invmass_l0l1 = HWWInvMass2L("invMassl0l1", 0, 1)
  if not TQObservable.addObservable(invmass_l0l1):
    INFO("failed to add invariant mass Observable")
    return False
  return True

if __name__ == "__main__":
  tags = TQTaggable()
  if addObservables(tags):
    print("Successfully added invariant mass observables")
  else:
    ERROR("Failed to add invariant mass observables")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### Histograms

We book the histograms in the histogram file. Then, we include the histogram file in the config file for analyze step. Here shows how we include the histogram file in the config file.

{% code-tabs %}
{% code-tabs-item title="share/config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
histograms: config/histograms/ZjetsFF/ZjetsFakeFactor-histograms.txt
```
{% endcode-tabs-item %}
{% endcode-tabs %}

 Here, we show an example of the histogram file. We book [TH1F](https://root.cern.ch/doc/master/classTH1F.html) which is the one-dimensional histogram with a float per channel. We book the histogram at and after the CutFakeEl stages.

{% code-tabs %}
{% code-tabs-item title="share/config/histograms/ZjetsFF/ZjetsFakeFactor-histograms.txt" %}
```text
TH1F('fakeElectronEta', '', 20, -3.0, 3.0) << ([$(elFakeAny_eta)] : 'el fake \#eta');

@CutFakeEl/*: fakeElectronEta;
```
{% endcode-tabs-item %}
{% endcode-tabs %}

We will describe more detailedly in the [histogram](histograms.md) section later.

### Alias

We define the variables used in the histogram and cut files in the alias file. So, we include the alias file in the config file.

{% code-tabs %}
{% code-tabs-item title="share/config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
include: config/aliases/ZjetsFF/ZjetsFakeFactor-aliases.cfg
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Here is an example for alias file. In the alias file, we define the **elFakeAny\_eta** variable which is used in the histogram definition.

{% code-tabs %}
{% code-tabs-item title="share/config/aliases/ZjetsFF/ZjetsFakeFactor-aliases.cfg" %}
```text
[analyze]
aliases.fitsChannel: @Event$(cand).size() > 0
aliases.elFakeAny_eta: "([ZBosonPairFakeIndex]==3 ? [$(elFake0).eta()] : ( [ZBosonPairFakeIndex]==2 ? [$(lep1).eta()] : [$(lep0).eta()])) "
```
{% endcode-tabs-item %}
{% endcode-tabs %}

A more complicated description will be covered in the [alias](alias.md) section.

