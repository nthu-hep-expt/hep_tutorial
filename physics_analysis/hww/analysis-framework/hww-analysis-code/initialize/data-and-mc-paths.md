# Data and MC Paths

## How to include data and MC paths

### Include samples by `dataPaths` and `mcPaths`

#### For non-fake samples

{% code title="" %}
```text
dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data1516/:CollectionTree
mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16a/:CollectionTree
```
{% endcode %}

#### For fake data and MC samples

{% code title="" %}
```text
ddFakes.dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/data/data1516/:CollectionTree
ddFakes.mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V19/EMTopoJets/2LDF/MC_Nominal/mc16a/:CollectionTree
```
{% endcode %}

Please note that we should add `:CollectionTree` followed by the paths since the informations of events are stored in the **CollectionTree** in the input PxAOD samples. 

### Include samples by `dataFileList` and `mcFileList`

We could use tag to use the file lists which contain the lists of samples we would like to run.  We take the ggF file list for Release 21 validation as an example. 

{% code title="share/config/master/VBF/initialize-VBF-Coupling-2018.cfg" %}
```text
dataFileList: share/config/samples/inputFileLists/ggF/ggF-dataFileList-Rel21Val.txt
dataFileListTreeName: CollectionTree
mcFileList: share/config/samples/inputFileLists/ggF/ggF-mcFileList-Rel21Val.txt
mcFileListTreeName: CollectionTree
```
{% endcode %}

In this file list, we could easily add the paths for different root files.

{% code title="share/config/samples/inputFileLists/ggF/ggF-mcFileList-Rel21Val.txt" %}
```text
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18.1/2LDF/group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_2L.V18.1_PAOD_2LDF/group.phys-higgs.361598.e4875_e6174_s3126_s3136_r9364_r9315_p3639.15672696.PAOD_2LDF._000054.pool.root
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18.1/2LDF/group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_2L.V18.1_PAOD_2LDF/group.phys-higgs.361598.e4875_e6174_s3126_s3136_r9364_r9315_p3639.15672696.PAOD_2LDF._000063.pool.root
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18.1/2LDF/group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_2L.V18.1_PAOD_2LDF/group.phys-higgs.361602.e4054_s3126_r9364_r9315_p3639.15672696.PAOD_2LDF._000005.pool.root
```
{% endcode %}

### Include samples by `Campaigns`

We currently use the `Campaigns` to include the samples. 

```text
campaignsConfig: config/master/common/campaigns.cfg
campaigns: c16a,c16d,c16e
```

Then in the `config/master/common/campaigns.cfg`, we use the [previous methods](data-and-mc-paths.md#include-samples-by-datapaths-and-mcpaths) to include samples.

