# Frameworks

## Introduction 

As mentioned previously, we have two framework frequently used in the HWW group. 

* [HWWAnalysisCode](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode) is the **analysis code** for the HWW subgroup based on the Common Analysis Framework \(CAF\).
* [HWWPhysicsxAODMaker](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWPhysicsxAODMaker) is the **production code** for the HWW subgroup based on the ASG AthAnalysis release.

With _HWWPhysicsxAODMaker_, we can derivate the DxAOD samples to PxAOD, which we use in the _HWWAnalysisCode_. Then we could produce the results presented by histograms and cutflows. 

* \*\*\*\*[**HSG3AnalysisCode**](https://svnweb.cern.ch/trac/atlasoff/browser/PhysicsAnalysis/HiggsPhys/HSG3/HSG3AnalysisCode?order=name) is the old version of the analysis code.

### Group Disks

ATLAS HWW group has a group disk for the PxAOD samples. The samples are stored in the following link.

```text
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/
```

#### Release 21 \(R21\) samples 

R21 samples are updated with new technical recommendations and will contain the events with full Run-2 dataset about 140 fb^-1 \(from 2015 to 2018 data\). 

```text
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21
```

#### EMTopo and PFlow

We use EMTopo method to define our jets in the ATLAS experiment before, now we would like to migrate from EMTopo to Particle Flow \(PFlow\) algorithm, which was also used in the CMS experiment, in the HWW analysis. Therefore, we've two kind of R21 samples with different methods currently.

