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

