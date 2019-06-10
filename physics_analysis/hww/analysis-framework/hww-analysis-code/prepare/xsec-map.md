# Xsec Map

## Sample Mapping \(from [gitlab](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/tree/master/share/config/samples/maps/common)\)

These files define the mapping of a DataSetIDentifier \(DSID\) to a \(usually more intuitive\) path in a SampleFolder.

###  Usage

Mapping files are simple tab/whitespace separated columns of DSIDs and corresponding SampleFolder paths, e.g.:

```text
361106 /bkg/$(channel)/Zjets_Powheg/ee/
```

The first column lists the DSID, the second the desired location in the SampleFolder structure under which a handle \(one or more instances of TQSample\) for samples \(input files=nTuples or xAODs\) belonging to this DSID will be stored. The `$(channel)` part is a placeholder which will be replaced with the name of the respective channel. If, or example, an analysis defines two channels 'em' and 'me', one would end up with two TQSamples for each input file belonging to the DSID in question located under

```text
/bkg/em/Zjets_Powheg/ee/
/bkg/me/Zjets_Powheg/ee/
```

Each pair of DSID and path is to be listed in one line \(empty lines and commentary lines can be used as well\).

###  Advanced

The DSID is not strictly required to be numerical but is technically used to select input files \(nTuples or xAODs\) from a \(large\) set of input files where the DSID needs to be contained in the file path/name of the files to be matched.

