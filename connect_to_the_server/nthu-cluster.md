# NTHU Cluster

## Introduction

The IP of our cluster is **140.114.94.172.** To login to the cluster, you can use the following commands. For new students, please contact Jennifer. 

```bash
# login to the cluster with IP
ssh yourAccount@140.114.94.172

# Once you login to the cluster, you can access the other node #2~#4
ssh yourAccount@nthuhep02
ssh yourAccount@nthuhep03
ssh yourAccount@nthuhep04
```

## Hand-on sessions

### Setup ATLAS environment 

You can setup the ATLAS environment automatically or manually, depending on whatever you like. 

To automatically setup the ATLAS environment, you can add the following lines in the `~/.bashrc`.

{% code title="~/.bashrc" %}
```bash
# add these lines in the ~/.bashrc
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
alias setupATLAS='source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh'

# Run the command with the following
setupATLAS
```
{% endcode %}

