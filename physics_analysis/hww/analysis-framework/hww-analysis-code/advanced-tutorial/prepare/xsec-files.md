# Xsec Files

## Xsec file used in the HWW analysis

In the full Run-2 VBF analysis, we used the cross section files for 13 TeV. In this file, we include the informations for the Monte Carlo \(MC\) simulated samples. In this file, we have informations about both signals and background samples. 

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

### SampleID \(DSID\)

The DataSetIDentifier \(DSID\) is the ID number for the sample. This will also be used in the map and whitelist files. 

### Xsection

The cross section is the probability for the production of different process. 

### K-factor

In particle physics, the ratio of a next-to-leading-order \(NLO\) cross-section calculation to a leading-order \(LO\) equivalent is called the k- or K-factor. It is dependent on the process type, the existence or otherwise of kinematic phase-space cuts, and scale choices in both the LO and NLO calculations. \(from [wikipedia](https://en.wikipedia.org/wiki/K-factor)\)

### Filter efficiency

Filter is used to select events with specific kinematic phase space. For example, in the VBF analysis, we have a filter for $$Z\rightarrow\tau\tau$$ processes. 

The **filter efficiency** is the efficiency to select the event in the preferred kinematic phase space. 

### Generator

The MC generator is also listed in the Xsec files. We have several different MC generators. 

We have some common MC generators

* Pythia
* Powheg
* EvtGen
* MadGraph \(aMC@NLO\)
* Sherpa
* ...

### Process

The processes, which listed in the XSec file, summarize the whole information for how we produce these MC samples. 

The informations included are:

* MC generators
* Parton distribution function \(PDF\) used in the samples
* Underlying event
* Showering
* Hadronization
* Filter information
* Final states
* ...



