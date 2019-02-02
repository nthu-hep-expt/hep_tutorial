# Analyze \(advanced\)

## Analyze with particular options

### --restrict

We can limit the processes to analyze by the option **--restrict.** 

#### Run with a specific process

We can run a single process. We should add the option below to the command for the analyze step. With this path, the analyze step will run over all the samples under this path 

```text
--restrict /sig/?/mh125/vbf/
```

The complete command to run with only VBF sample is shown below

```bash
./analyze.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --restrict /sig/?/mh125/vbf/
```

#### Run with specific multiple processes

The following example is to run only the VBF, ggF and WW processes in the same time. Please note that you should not add an additional space between the processes paths. 

```text
--restrict /sig/?/mh125/vbf/,/sig/?/mh125/ggf/,/bkg/?/diboson/WW/,/bkg/?/Zjets/?/?/tt/,/bkg/?/top/ttbar/,/bkg/?/top/singletop/Wt
```

The complete command to run with only these 6 processes is shown below

```
./analyze.py config/master/VBF/analyze-VBF-Coupling-2018.cfg --restrict /sig/?/mh125/vbf/,/sig/?/mh125/ggf/,/bkg/?/diboson/WW/,/bkg/?/Zjets/?/?/tt/,/bkg/?/top/ttbar/,/bkg/?/top/singletop/Wt
```

