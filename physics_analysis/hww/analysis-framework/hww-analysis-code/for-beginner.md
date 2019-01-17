# For Beginner

The [HWW Analysis Code](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode) provides an example analysis on xAOD inputs. In the following sections, we will give detailed explanations for the steps to run the analysis.

## Cloning the analysis framework

Since PxAOD samples are normally stored in the EOS space, we should use the lxplus to analyze samples. After login the lxplus, we could follow the steps below to run with the example analysis.

{% hint style="warning" %}
The following steps may be out of date. So, please also check the steps shown in this [README.md](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/blob/master/README.md) for the correct setups.
{% endhint %}

The first step to run with the analysis is to setup the ATLAS environment and make a new directory for your analysis codes. Then clone \(download!\) the repository with **git clone.** 

```bash
# setup the ATLAS environment
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

