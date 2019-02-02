# Analyze

After the **initialize** step, We will now run the **analyze** step with the initialized samples.

{% code-tabs %}
{% code-tabs-item title="share/config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
# -*- mode: config -*-

[analyze]

# name of the input file
inputFile: sampleFolders/initialized/samples-initialized-ZjetsFakeFactor.root

# name of the output file
outputFile: sampleFolders/analyzed/samples-analyzed-ZjetsFakeFactor.root

# channels to run over
channels: ee,mm

useMultiChannelVisitor: true

purgeRemainder: true

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
{% endcode-tabs-item %}
{% endcode-tabs %}

### Cuts

In this analyze step, we should define our cuts to select events. 

{% code-tabs %}
{% code-tabs-item title="share/config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
cuts: config/cuts/ZjetsFF/ZjetsFakeFactor-cuts.def
```
{% endcode-tabs-item %}
{% endcode-tabs %}

We define the cuts like the cut file shown below. The following lines show an example of the cut file. You can only have a quick look at it. We will describe the cut files more detailedly in the [section](../advanced-analysis/vbf-analysis/analyze-for-vbf/) for VBF.

Here, the analysis starts with **CutChannels** stage after the PxAOD production. Then, a **CutVgammaVjet\_overlap** selection is applied after CutChannels stage.

```
+CutChannels {
# to use the per-event event weights poperly, use "Weight" as .weightExpression here
    <.cutExpression = "$(fitsChannel)", .weightExpression = "Weight_$(weightname):$(cand)", .title="Channel Selection">
    +CutVgammaVjet_overlap {
        <.cutExpression = "{ $(isVjets) ? $(Truth_hasFSRPhotonDR01)==0 : 1 }",  .title="Overlap: Vgamma/Vjets">
         } #End: CutVgammaVjet_overlap
} #End: CutChannels
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

We take an example observable snippet in the following. We can have an overview of how an observable snippet looks like. We will have a more complete description in the [observable](../advanced-analysis/vbf-analysis/analyze-for-vbf/observables.md) section.

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

We will describe more detailedly in the [histogram](../advanced-analysis/vbf-analysis/analyze-for-vbf/histograms.md) section later.

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

A more complicated description will be covered in the [alias](../advanced-analysis/vbf-analysis/analyze-for-vbf/alias.md) section.

