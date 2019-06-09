# Setups and Examples

The [HWW Analysis Code](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode) provides an example analysis on xAOD inputs. In the following sections, we will give detailed explanations for the steps to run the analysis.

## Cloning the analysis framework

Since PxAOD samples are normally stored in the EOS space, we should use the Lxplus to analyze samples. After log in the Lxplus, we could follow the steps in the [README.md](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/README.md) to setup the analysis framework.

```bash
setupATLAS

# setup the git 
lsetup git

# make a new directory for your analysis code and move into the directory
mkdir HWWAnalysis
cd HWWAnalysis

# Then clone (download) the repository 
# --recursive is an option to clone all the things in the directory
git clone --recursive https://:@gitlab.cern.ch:8443/atlas-physics/higgs/hww/HWWAnalysisCode.git
```

Once we have the analysis framework, we should build \(compile\) the analysis framework. The introduction of command **'make'** can be found [here](https://www.tutorialspoint.com/unix_commands/make.htm). 

```bash
# 'build' is the directory where you store your compiled codes
# 'run' is the place where you should run in 
mkdir build run

# move to 'build' and build your analysis framework
cd build
asetup AnalysisBase,21.2.49
cmake ../HWWAnalysisCode

# setup the environment for the analysis framework
source ../HWWAnalysisCode/setup/setupAnalysis.sh

# compile 
# -j specifies the number of jobs (commands) to run simultaneously
# -j4 means to use 4 jobs to run simultaneously
make -j4

```

## Running the example analysis

After building your framework, we could first run the example analysis with the following steps. You can run in the **'share'** directory. 

```bash
cd ../HWWAnalysisCode/share
./prepare.py config/master/ZjetsFF/prepare-ZjetsFakeFactor-Coupling-2018.cfg
./initialize.py config/master/ZjetsFF/initialize-ZjetsFakeFactor-Coupling-2018.cfg
./analyze.py config/master/ZjetsFF/analyze-ZjetsFakeFactor-Coupling-2018.cfg
./visualize.py config/master/ZjetsFF/visualize-ZjetsFakeFactor-Coupling-2018.cfg
```

We have four steps shown below. Normally, we don't need to modify these four python files. Instead, we should change the **config files** to change the setups we would like to run. 

* [prepare.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/prepare.py):  setup basic **SampleFolder** \(SF\) structure.
* [initialize.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/initialize.py): discover samples and read Meta-Info \(sumOfWeights\).
* [analyze.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/analyze.py): analyze individual events as well as book histograms  yields.
* [visualize.py](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/share/visualize.py): Draw the histograms and cutflow tables.

The following table summarizes the usage of these four steps. This table is from [Ralf's slides](https://indico.cern.ch/event/771763/contributions/3207844/attachments/1767899/2871281/caf_tutorial_concepts.pdf) in the CAF tutorial.

![](../../../../../.gitbook/assets/ying-mu-kuai-zhao-20190119-xia-wu-8.46.07.png)

