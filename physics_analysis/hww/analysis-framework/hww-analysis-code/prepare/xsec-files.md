# XsecFiles

## Introduction 

In the full Run-2 VBF analysis, we used data collided at 13 TeV. Therefore, we include the Xsec files with 13 TeV. 

In the `XS_13TeV.csv` files, it includes the informations of the MC simulated samples including both signals and background samples. The following is part of the `XS_13TeV.csv` file.

{% code-tabs %}
{% code-tabs-item title="share/config/samples/XSec/common/XS\_13TeV.csv" %}
```text
SampleID , xsection , kfactor , filtereff , uncertainty , mh , generator , process , simulation

# SM ggf
341079, 0.0011020, 1.0, 4.9150E-01, --, 125,  Powheg+Pythia8+EvtGen, PowhegPythia8EvtGen_CT10_AZNLOCTEQ6L1_ggH125_WWlvlv_EF_15_5,  OFLCOND-RUN12-SDR-30
## Not Added to the whitelist yet - issue with weights
345324, 0.0011020, 1.0, 4.9318E-01, --, 125,  Powheg+Pythia8+EvtGen, PowhegPythia8EvtGen_NNLOPS_NN30_ggH125_WWlvlv_EF_15_5,  OFLCOND-RUN12-SDR-30
345339, 0.0011020, 1.0, 2.1808E-01, --, 125,  MadGraph+Pythia8+EvtGen, MadGraphPythia8EvtGen_A14NNPDF23LO_ggfhwwlnulnuNp2,  OFLCOND-RUN12-SDR-30

## ggf + 2 jets CP SM even, CP mixed, CP odd
343475, 0.000318, 1.0, 0.7, --, 125,  MGaMcAtNlo+Pythia8+EvtGen, MGaMcAtNloPy8EG_A14_NNPDF23_ggFhwwlvlv_CP_EVEN_emu,  OFLCOND-RUN12-SDR-30
343987, 0.000318, 1.0, 0.7, --, 125,  MGaMcAtNlo+Pythia8+EvtGen, MGaMcAtNloPy8EG_A14_NNPDF23_ggFhwwlvlv_CP_EVEN_mue,  OFLCOND-RUN12-SDR-30
343476, 0.000318, 1.0, 0.7, --, 125,  MGaMcAtNlo+Pythia8+EvtGen, MGaMcAtNloPy8EG_A14_NNPDF23_ggFhwwlvlv_CP_MIX_emu,  OFLCOND-RUN12-SDR-30
343988, 0.000318, 1.0, 0.7, --, 125,  MGaMcAtNlo+Pythia8+EvtGen, MGaMcAtNloPy8EG_A14_NNPDF23_ggFhwwlvlv_CP_MIX_mue,  OFLCOND-RUN12-SDR-30
343477, 0.000318, 1.0, 0.7, --, 125,  MGaMcAtNlo+Pythia8+EvtGen, MGaMcAtNloPy8EG_A14_NNPDF23_ggFhwwlvlv_CP_ODD_emu,  OFLCOND-RUN12-SDR-30
343989, 0.000318, 1.0, 0.7, --, 125,  MGaMcAtNlo+Pythia8+EvtGen, MGaMcAtNloPy8EG_A14_NNPDF23_ggFhwwlvlv_CP_ODD_mue,  OFLCOND-RUN12-SDR-30
```
{% endcode-tabs-item %}
{% endcode-tabs %}

## Informations

### SampleID \(DSID\)

The DataSetIDentifier \(DSID\) is the ID number for the sample. This will also be used in the `map` and `whitelist` files. 

### Xsection

The cross sections, which represent the probabilities of the productions of different process, are calculated by their related theories. We include the numbers as inputs which will be normalized in the analysis.

### K-factor

In particle physics, the ratio of a next-to-leading-order \(NLO\) cross-section calculation to a leading-order \(LO\) equivalent is called the k- or K-factor. It is dependent on the process type, the existence or otherwise of kinematic phase-space cuts, and scale choices in both the LO and NLO calculations. \(from [wikipedia](https://en.wikipedia.org/wiki/K-factor)\)

### Filter and its efficiency

* **Filter** is used to select events with specific kinematic phase space. For example, in the VBF analysis, we have filters for $$\text{Z}\rightarrow\tau\tau$$ processes since we don't have enough MC statistics for such DY background in the high mjj region.
* **Filter efficiency** is the efficiency to select the event in the preferred kinematic phase space. 

### MC generators

**MC generators** are also listed in the Xsec files. We have several different MC generators. We list some common MC generators below

* Pythia
* Powheg
* EvtGen
* MadGraph \(aMC@NLO\)
* Sherpa
* ...

### Process

The **process** summarizes the whole information about how we produced these MC samples including

* MC generators
* Parton distribution function \(PDF\) used in the samples
* Underlying event
* Showering
* Hadronization
* Filter information
* Final states
* ...



