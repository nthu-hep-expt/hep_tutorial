# MC production

## Introduction

### installation

Install [Madgraph\_aMC@NLO](https://launchpad.net/mg5amcnlo)

### Exercise

We can produce a process and easily get their cross sections. For example, we can produce a proton-proton collision with electron-positron final state.

```text
# generate process you want
generate p p > e- e+

# output a folder to store the information (with customed name)
output pp_ee

# launch the folder
launch pp_ee 

```



