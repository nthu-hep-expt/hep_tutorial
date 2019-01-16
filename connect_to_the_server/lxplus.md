# lxplus

## Working in the lxplus  <a id="working-in-the-lxplus"></a>

Once you have CERN account, we can access the lxplus by the following commands:

* Login a random computer in the cluster

```bash
ssh yourAccount@lxplus.cern.ch​
```

* Login the specific computer in the cluster \(001-138\)

```bash
ssh yourAccount@lxplus001.cern.ch
```

## Commands in the lxplus

### Set up for the ATLAS environment

You should initialize with the following command when you login every time

```bash
setupATLAS
```

![&quot;setupATLAS&quot; initializes for the ATLAS environment](../.gitbook/assets/ying-mu-kuai-zhao-20190116-shang-wu-4.43.46.png)

### Tips and useful commands in the lxplus

* Check the quota in user or working directory 

```bash
fs lq --human
```

