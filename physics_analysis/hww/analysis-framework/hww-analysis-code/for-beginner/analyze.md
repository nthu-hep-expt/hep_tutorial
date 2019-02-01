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

