# Visualize \(Basic\)

After running with analyze step, we will run the visualize step to produce the plots and cutflows.

```bash
# Run in the share folder (../HWWAnalysisCode/share)
./visualize.py config/master/ZjetsFF/visualize-ZjetsFakeFactor-Coupling-2018.cfg
```

We will briefly discuss the config file in the visualize step.

{% code title="share/config/master/ZjetsFF/visualize-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
# -*- mode: config -*-

[visualize]

# name of the input file
inputFile: sampleFolders/analyzed/samples-analyzed-ZjetsFakeFactor.root

# name of the output file
outputFile: sampleFolders/visualized/samples-visualized-ZjetsFakeFactor.root

# name of the output folder
outputDir: results/ZjetsFF

# channels to run over
channels: ee,mm, sf
channelConfig: config/channels/common/channels.txt

patches: config/visualization/style/ZjetsFF/ZjetsFakeFactor-style.txt

makePlots: *
histogramProcesses: config/visualization/processes/ZjetsFF/ZjetsFakeFactor-plot-processes.txt
plotter.style.showRatio: true
makeLogPlots: false

makeCutflows: true
cutflowFormats: txt, tex, html

cutflowProcessFiles: config/visualization/processes/ZjetsFF/ZjetsFakeFactor-cutflow-processes.txt
cutflowCutFiles: config/visualization/cuts/ZjetsFF/ZjetsFakeFactor-cutflow-cuts.txt
```
{% endcode %}

### Output directory

We can determine the path to produce the plots and cutflows.

{% code title="share/config/master/ZjetsFF/visualize-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
outputDir: results/ZjetsFF
```
{% endcode %}

### Patches

{% code title="share/config/master/ZjetsFF/visualize-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
patches: config/visualization/style/ZjetsFF/ZjetsFakeFactor-style.txt
```
{% endcode %}

In the patches, we define the definitions of different processes, like title, color, and the path to the processes.

{% code title="share/config/visualization/style/ZjetsFF/ZjetsFakeFactor-style.txt" %}
```text
# -*- mode: tqfolder -*-

<style.default.title = "Total Bkg.", style.default.histLineColor = 1, style.default.histFillColor = 15> @ /bkg/;
<style.default.title = "$Z/#gamma^{*}$", style.default.histFillColor = 210> @ /bkg/?/Zjets/;
```
{% endcode %}

### Make plots

The **makePlots** means to generate the plots we've booked. 

```text
makePlots: *
```

We can also use some tags to customize the plots we want. 

```text
histogramProcesses: config/visualization/processes/ZjetsFF/ZjetsFakeFactor-plot-processes.txt
plotter.style.showRatio: true
makeLogPlots: false
```

### Make cutflows

The **makeCutflows** is used to draw the cutflows, which will show the event yields for different processes in the different stages.

{% code title="share/config/master/ZjetsFF/visualize-ZjetsFakeFactor-Coupling-2018.cfg" %}
```text
makeCutflows: true
cutflowFormats: txt, tex, html
```
{% endcode %}

We can also use the following tags to define the processes and stages we would like to show.

```text
cutflowProcessFiles: config/visualization/processes/ZjetsFF/ZjetsFakeFactor-cutflow-processes.txt
cutflowCutFiles: config/visualization/cuts/ZjetsFF/ZjetsFakeFactor-cutflow-cuts.txt
```

