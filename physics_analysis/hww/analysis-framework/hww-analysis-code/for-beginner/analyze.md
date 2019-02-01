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

We define the cuts in the cut file shown below. We can only have a look into this cut file. The analysis starts with CutChannels stage after the PxAOD production. We will describe the cut files more detailedly in the [section](../advanced-analysis/vbf-analysis/analyze-for-vbf/) for VBF.

{% code-tabs %}
{% code-tabs-item title="config/cuts/ZjetsFF/ZjetsFakeFactor-cuts.def" %}
```text
# -*- mode: tqfolder -*-
# this files name is 'cuts.txt'
# to get proper syntax highlighting and indentation when using emacs,
# add the following line to your .emacs file:
#   (load-file "$TQPATH/share/tqfolder.el")

+CutChannels {
    # to use the per-event event weights poperly, use "Weight" as .weightExpression here
    <.cutExpression = "$(fitsChannel)", .weightExpression = "Weight_$(weightname):$(cand)", .title="Channel Selection">
    +CutVgammaVjet_overlap {
        <.cutExpression = "{ $(isVjets) ? $(Truth_hasFSRPhotonDR01)==0 : 1 }",  .title="Overlap: Vgamma/Vjets">
        +CutOtherLep {
            <.cutExpression = "$(lllFinalState)", .title = "lll final state">

            # find the fake index by finding the most optimal Z-boson pair
            +CutZMass {
                <.cutExpression = "[ZBosonPairFakeIndex]==3 || [ZBosonPairFakeIndex]==2 || [ZBosonPairFakeIndex]==1", .title = "Z-tagging">

                # make sure all leptons are above 15 GeV
                +CutLeptonsPt {
                    <.cutExpression = " $(lep0).pt() > 15000 && $(lep1).pt() > 15000 && $(otherPart0).pt() > 15000", .title = "lep $p_T > 15$ GeV">

                    +CutWZVeto {
                        <.cutExpression = "$(PassWZVeto)",   .title = "WZ veto">

                        +CutFakeEl {
                            <.cutExpression = "$(fakeAny_type) == $(electron)", .title = "fake type: electron">
                            +CutEtaFakeElec {
                                <.cutExpression = "(fabs($(elFakeAny_eta)) < 2.47 && (fabs($(elFakeAny_eta)) < 1.37 || fabs($(elFakeAny_eta)) > 1.52))", .title = "Fake el eta cut">

                                ##ID Selection
                                +CutFakeElecID {
                                    <.cutExpression = "$(fakeAny_id)", .title = "ID cuts", flav_ID="El_ID">

                                }
                                ##Anti-ID selection
                                +CutFakeElecAntiID {
                                    <.cutExpression = "$(fakeAny_antiid)", .title = "Anti-ID cuts", flav_ID="El_AntiID">

                                }

                            } #End: CutEtaFakeElec
                        } #End: CutFakeEl
                        +CutFakeMu {
                            <.cutExpression = "$(fakeAny_type)== $(muon)", .title = "fake type: muon">
                            +CutEtaFakeMuon {
                                <.cutExpression = "fabs($(muFakeAny_eta)) < 2.5", .title = "Fake mu |eta|<2.5 ">

                                ##ID Selection
                                +CutFakeMuonID {
                                    <.cutExpression = "$(fakeAny_id)", .title = "ID cuts", flav_ID="Mu_ID">

                                }
                                ##Anti-ID selection
                                +CutFakeMuonAntiID {
                                    <.cutExpression = "$(fakeAny_antiid)", .title = "Anti-ID cuts", flav_ID="Mu_ID">

                                }

                            } #End: CutEtaFakeMuon
                        } #End: CutFakeMu
                    } #End: CutWZVeto
                } #End: CutLeptonsPt
            } #End: CutZMass
        } #End: CutOtherLep
    } #End: CutVgammaVjet_overlap
} #End: CutChannels

```
{% endcode-tabs-item %}
{% endcode-tabs %}

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
```text
from QFramework import TQObservable,INFO,ERROR,BREAK


from HWWAnalysisCode import HWWInvMass2L

def addObservables(config):

  INFO("adding invariant mass observable")

  invmass_l0l1 = HWWInvMass2L("invMassl0l1", 0, 1)
  invmass_l0otherPart0= HWWInvMass2L("invMassl0otherPart0", 0, 2)
  invmass_l1otherPart0= HWWInvMass2L("invMassl1otherPart0", 1, 2)

  if not TQObservable.addObservable(invmass_l0l1):
    INFO("failed to add invariant mass Observable")
    return False
  if not TQObservable.addObservable(invmass_l0otherPart0):
    INFO("failed to add invariant mass Observable")
    return False
  if not TQObservable.addObservable(invmass_l1otherPart0):
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

We book the histograms with the histogram file.

{% code-tabs %}
{% code-tabs-item title="share/config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
histograms: config/histograms/ZjetsFF/ZjetsFakeFactor-histograms.txt
```
{% endcode-tabs-item %}
{% endcode-tabs %}

We shows an example for the histogram file. We will describe more detailedly in the [histogram](../advanced-analysis/vbf-analysis/analyze-for-vbf/histograms.md) section.

{% code-tabs %}
{% code-tabs-item title="share/config/histograms/ZjetsFF/ZjetsFakeFactor-histograms.txt" %}
```text
#####################
# Define histograms #

TH1F('fakeElectronPt', '', 27, 15., 150.) << ( [$(elFakeAny_pt)]*0.001 : 'el fake p_{T} [GeV]');
TH1F('fakeElectronEta', '', 20, -3.0, 3.0) << ([$(elFakeAny_eta)] : 'el fake \#eta');
TH2F('FakeElecEtaVsPt', '', {15., 20., 25., 35., 1000.},            {0., 1.5, 2.5}) << ( [$(elFakeAny_pt)]/1000 : 'Fake candidate p_{T} [GeV]', abs([$(elFakeAny_eta)])  : 'Fake candidate |\#eta|' );

TH1F('fakeMuonPt', '', 27, 15., 150.) << ( [$(elFakeAny_pt)]*0.001 : 'mu fake p_{T} [GeV]');
TH1F('fakeMuonEta', '', 20, -3.0, 3.0) << ([$(elFakeAny_eta)] : 'mu fake \#eta');
TH2F('FakeMuonEtaVsPt', '', {15., 20., 25., 1000.}, {0., 1.05, 2.5}) << ( [$(elFakeAny_pt)]/1000 : 'Fake candidate p_{T} [GeV]', abs([$(elFakeAny_eta)])  : 'Fake candidate |\#eta|' );

TH1F('invMass', '', 40, 70., 110.) << ( $(invMassOptZTag)*0.001: 'm_{l,l}^{Z} [GeV]' );

#################################################
# and specify for which cut levels to fill them #


### fake eta and pt

# electron:
@CutFakeEl/*: fakeElectronPt, fakeElectronEta;
@CutFakeElecID: FakeElecEtaVsPt;
@CutFakeElecAntiID: FakeElecEtaVsPt;
# muon:
@CutFakeMu/*: fakeMuonPt, fakeMuonEta;
@CutFakeMuonID: FakeMuonEtaVsPt;
@CutFakeMuonAntiID: FakeMuonEtaVsPt;

### Invariant mass of Zcand pair

@CutLeptonsPt: invMass;

```
{% endcode-tabs-item %}
{% endcode-tabs %}

### Alias

We also need the alias file to define the variable to use in the histogram and cut files. 

{% code-tabs %}
{% code-tabs-item title="share/config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
include: config/aliases/ZjetsFF/ZjetsFakeFactor-aliases.cfg
```
{% endcode-tabs-item %}
{% endcode-tabs %}

We will have an example for alias file. A more complicated description will be covered in the [alias](../advanced-analysis/vbf-analysis/analyze-for-vbf/alias.md) section. 

{% code-tabs %}
{% code-tabs-item title="share/config/aliases/ZjetsFF/ZjetsFakeFactor-aliases.cfg" %}
```text
[analyze]

# CutChannels
aliases.fitsChannel: @Event$(cand).size() > 0

# CutVgammaVjet_overlap
aliases.Truth_hasFSRPhotonDR01: [SGAuxCDec:EventInfo:truth_hasFSRPhotonDR01]

# CutOtherLep
aliases.nOtherElec: Event$(cand)[0].nOtherElectrons()
aliases.nOtherMuon: Event$(cand)[0].nOtherMuons()
aliases.lllFinalState: ($(nOtherElec) == 1 && $(nOtherMuon) == 0) || ($(nOtherElec) == 0 && $(nOtherMuon) == 1)

# CutZMass

# CutLeptonsPt
aliases.lep0: 		Event$(cand)[0].part(0)
aliases.lep1: 		Event$(cand)[0].part(1)
aliases.otherPart0: Event$(cand)[0].otherPart(0)

# CutWZVeto
aliases.PassWZVeto: "([ZBosonPairFakeIndex]==3 ? [PassWZVetoThirdLep]: ( [ZBosonPairFakeIndex]==2 ? [PassWZVetoSubleadLep]: [PassWZVetoLeadLep] ) )"

# CutFakeEl
# CutFakeMu
aliases.electron: 6
aliases.muon: 8
aliases.fakeAny_type: "([ZBosonPairFakeIndex]==3 ? [$(otherPart0).type()] : ( [ZBosonPairFakeIndex]==2 ? [$(lep1).type()]: [$(lep0).type()] ) )"

# CutEtaFakeElec
# CutEtaFakeMuon
aliases.elFake0: Event$(cand)[0].otherElectron(0)
aliases.muFake0: Event$(cand)[0].otherMuon(0)
aliases.elFakeAny_eta: "([ZBosonPairFakeIndex]==3 ? [$(elFake0).eta()] : ( [ZBosonPairFakeIndex]==2 ? [$(lep1).eta()] : [$(lep0).eta()])) "
aliases.muFakeAny_eta: "([ZBosonPairFakeIndex]==3 ? [$(muFake0).eta()] : ( [ZBosonPairFakeIndex]==2 ? [$(lep1).eta()] : [$(lep0).eta()])) "

# CutFakeElecID
# CutFakeMuonID
aliases.fakeAny_id: "([ZBosonPairFakeIndex]==3 ? [otherLep0ID]: ( [ZBosonPairFakeIndex]==2 ? [subleadLepID]: [leadLepID] ) )"

# CutFakeElecAntiID
# CutFakeMuonAntiID
aliases.fakeAny_antiid: "([ZBosonPairFakeIndex]==3 ? [otherLep0AntiID]: ( [ZBosonPairFakeIndex]==2 ? [subleadLepAntiID]: [leadLepAntiID] ) )"


###
### just For histograms
###
aliases.elFakeAny_pt: "([ZBosonPairFakeIndex]==3 ? [$(elFake0).pt()] : ( [ZBosonPairFakeIndex]==2 ? [$(lep1).pt()] : [$(lep0).pt()])) "
aliases.muFakeAny_pt: "([ZBosonPairFakeIndex]==3 ? [$(muFake0).pt()] : ( [ZBosonPairFakeIndex]==2 ? [$(lep1).pt()] : [$(lep0).pt()])) "
aliases.invMassOptZTag: "([ZBosonPairFakeIndex]==3 ? [invMassl0l1]: ( [ZBosonPairFakeIndex]==2 ? [invMassl0otherPart0]: [invMassl1otherPart0] ) )"

```
{% endcode-tabs-item %}
{% endcode-tabs %}



