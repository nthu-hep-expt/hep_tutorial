# Data and MC Paths

## How to include data and MC paths

We have several samples including data and MC samples. For the fake estimation,  we also have both data and MC samples for W+jets.

### Include data and MC samples with paths

#### Data and MC samples

{% code-tabs %}
{% code-tabs-item title="share/config/master/VBF/initialize-VBF-Coupling-2018.cfg" %}
```text
dataPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18/2LDF/data/:CollectionTree
mcPaths: /eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18/2LDF/mc/:CollectionTree
```
{% endcode-tabs-item %}
{% endcode-tabs %}

#### Setup for fake data and MC samples

We can also add the fake samples by the paths. 

{% code-tabs %}
{% code-tabs-item title="share/config/master/VBF/initialize-VBF-Coupling-2018.cfg" %}
```text
ddFakes.dataPaths: /eos/user/m/metsai/PAOD_2LDF/v17b/fake_data/:CollectionTree
ddFakes.mcPaths: /eos/user/m/metsai/PAOD_2LDF/v17b/fake_mc/:CollectionTree
ddFakes.baseFolderName: Wjets
ddFakes.subFolderNames: FakeE,FakeM, QCDCorr
ddFakes.mcFoldersToVeto: Wjets
```
{% endcode-tabs-item %}
{% endcode-tabs %}

Please note that we should add `:CollectionTree` followed by the paths!

### Include data and MC samples with file lists

We would 

```text
dataFileList: share/config/samples/inputFileLists/ggF/ggF-dataFileList-Rel21Val.txt
dataFileListTreeName: CollectionTree
mcFileList: share/config/samples/inputFileLists/ggF/ggF-mcFileList-Rel21Val.txt
mcFileListTreeName: CollectionTree
```

```text
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18.1/2LDF/group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_2L.V18.1_PAOD_2LDF/group.phys-higgs.361598.e4875_e6174_s3126_s3136_r9364_r9315_p3639.15672696.PAOD_2LDF._000054.pool.root
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18.1/2LDF/group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_2L.V18.1_PAOD_2LDF/group.phys-higgs.361598.e4875_e6174_s3126_s3136_r9364_r9315_p3639.15672696.PAOD_2LDF._000063.pool.root
/eos/atlas/atlascerngroupdisk/phys-higgs/HSG3/R21/PAOD_V18.1/2LDF/group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_2L.V18.1_PAOD_2LDF/group.phys-higgs.361602.e4054_s3126_r9364_r9315_p3639.15672696.PAOD_2LDF._000005.pool.root
```

