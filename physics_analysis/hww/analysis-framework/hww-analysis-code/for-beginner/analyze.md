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

We define the cuts in the cut file shown below

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

