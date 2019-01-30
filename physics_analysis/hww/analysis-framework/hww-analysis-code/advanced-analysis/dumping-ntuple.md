# Dumping Ntuple and Eventlists

## Introduction

We have an introduction [**slide**](https://indico.cern.ch/event/771763/contributions/3207862/attachments/1767975/2871431/sauerburger2018-12-10_dump.pdf) for nTuple dumping. Dumping nTuple is to covert our sample format to a more accessible data format, a flat nTuple!

![Description from Frank Sauerburger&apos;s slide ](../../../../../.gitbook/assets/ying-mu-kuai-zhao-20190130-xia-wu-4.20.15.png)

### Booking nTuple

We book the nTuple definition in the analyze config file.

```text
ntuples: config/nTuples/VBF/mva_ntuple.txt
```

```text
# Define branches (make sure that this is a single line)
skim: int evt_num << EventInfo.eventNumber(), int isEM << [ "$(channel)"=="em" ] , int isME << [ "$(channel)"=="me" ], float lep0_pt << $(lep0).pt(), float lep0_phi << $(lep0).phi(), float lep0_eta << $(lep0).eta();

# Book at cuts
@CutVBFZttVeto_2jet_MVA: skim >> dump/mva_ntuple.root:HWW_$(channel)
```

### Define the labels for your nTuple

We can create a file to include the labels which will allow us to define the variables to distinguish processes.

```text
config/patches/VBF/patch-VBF-MVA.txt
```

{% code-tabs %}
{% code-tabs-item title="config/patches/VBF/patch-VBF-MVA.txt" %}
```text
<ntupName = "ggf"> @/sig/?/mh125/ggf;
<ntupName = "vbf"> @/sig/?/mh125/vbf;
<ntupName = "WW"> @/bkg/?/diboson/WW;
<ntupName = "Ztt"> @/bkg/?/Zjets/?/?/tt/;
<ntupName = "ttbar"> @/bkg/?/top/ttbar;
<ntupName = "Wt"> @/bkg/?/top/singletop/Wt;
```
{% endcode-tabs-item %}
{% endcode-tabs %}

### Define the jobs to run parallel

```text
config/jobLists/VBF/jobs-MVA.txt
```

{% code-tabs %}
{% code-tabs-item title="config/jobLists/VBF/jobs-MVA.txt" %}
```text
/sig/?/mh125/ggf/
/sig/?/mh125/vbf/
/bkg/?/diboson/WW/
/bkg/?/Zjets/?/?/tt/
/bkg/?/top/ttbar/
/bkg/?/top/singletop/Wt
```
{% endcode-tabs-item %}
{% endcode-tabs %}

```text

```

### Submit to dump nTuple

```bash
./submit.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --jobs config/jobLists/VBF/jobs-MVA.txt --maxSampleSize 6000 --maxSampleCount 20 --identifier VBF_nTuple_dumping
```

