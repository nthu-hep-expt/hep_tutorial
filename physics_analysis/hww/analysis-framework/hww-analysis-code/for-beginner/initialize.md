# Initialize

```text
# -*- mode: config -*-

[initialize]

# name of the input file
inputFile: sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root

# name of the output file
outputFile: sampleFolders/initialized/samples-initialized-ZjetsFakeFactor.root

# paths and names of the input data files
dataFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-dataFileList.txt
dataFileListTreeName: CollectionTree
#dataPaths: /eos/user/d/dshope/forCAFExample/xAOD_Example/data/:CollectionTree
# additional input file configurations - these are already the defaults
#dataFilePattern: *.root*
#dataFolderPattern: data/$(channel)/all

# paths and names of the input mc files to initialize
mcFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-mcFileList.txt
mcFileListTreeName: CollectionTree
#mcPaths: /eos/user/d/dshope/forCAFExample/xAOD_Example/mc/:CollectionTree
# additional input file configurations - these are already the defaults
#mcFilenameSuffix: *.root*
#mcFilenamePrefix: *

# some debugging options for the sample initializer
# initialize: false
printSamplesFailed: true
verbose: true

# channels to run over
channels: ee,mm
channelPlaceholder: channel

# preInit patch files to apply
preInit_patches: config/patches/ZjetsFF/ZjetsFakeFactor-default-patch.txt

# postInit patch files to apply
#postInit_patches: 

```

### inputFile

We use the output root file from prepare step as our input sample.

```text
inputFile: sampleFolders/prepared/samples-prepared-ZjetsFakeFactor.root
```

### outputFile

An output file will be created after the initialize step. 

```text
outputFile: sampleFolders/initialized/samples-initialized-ZjetsFakeFactor.root
```

### Run with samples

We have several ways to run with our samples. We could run with the given lists or run with the samples inside some certain folders. Here we show two ways:

* File list 

We use the file list to pass the samples we would like to run.

```
dataFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-dataFileList.txt
dataFileListTreeName: CollectionTree
mcFileList: config/samples/inputFileLists/ZjetsFF/ZjetsFakeFactor-mcFileList.txt
mcFileListTreeName: CollectionTree
```

*   ```text
  dataPaths
  ```

```text
dataPaths: /eos/user/d/dshope/forCAFExample/xAOD_Example/data/:CollectionTree
```

