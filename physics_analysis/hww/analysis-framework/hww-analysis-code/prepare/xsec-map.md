# Xsec Map

## Introduction

The `map` file is used to define our `TQSampleFolder` of output files. The description and introduction for the usage is shown in the [gitlab](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/tree/master/share/config/samples/maps/common). 

Here we used `run2-mc15.map`. However, I believe that we will use the `run2-mc16.map` instead in the future. Moreover, it seems there is no difference between these two maps. 

The following file shows the map file which we used in the VBF analysis.

{% code-tabs %}
{% code-tabs-item title="share/config/samples/maps/common/run2-mc15.map" %}
```text
341079 /sig/$(channel)/mh125/ggf/
341080 /sig/$(channel)/mh125/vbf/
345323 /sig/$(channel)/mh125/vbf/
343393 /sig/$(channel)/mh125/ggf/
345324 /sig/$(channel)/mh125/ggf/
341122 /sig/$(channel)/mh125/htt/ggf/
341155 /sig/$(channel)/mh125/htt/vbf/
```
{% endcode-tabs-item %}
{% endcode-tabs %}

The numbers shown here are the DSIDs. The following paths are the paths to define the structure of sample folders.

