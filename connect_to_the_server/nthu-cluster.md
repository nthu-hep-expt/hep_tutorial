# NTHU Cluster

Login with the following line

```bash
ssh yourAccount@140.114.94.172
```

Initialize the ATLAS environment for the cluster

```text
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBasesource 
${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh
alias setupATLAS='source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh'
setupATLAS
```



