# Xsec Whitelist

## Sample Whitelisting \(from [gitlab page](https://gitlab.cern.ch/atlas-physics/higgs/hww/HWWAnalysisCode/tree/master/share/config/samples/whitelists/common)\)

Between different \(sub\)analyses it often makes sense to share most samples and corresponding definitions such as [cross sections](../XSec/README.md) and [mappings](../maps/README.md). In order to avoid potential inconsistencies the cross-section and mapping files should in this case not be duplicated just to allow for, e.g., slightly different choices of samples \(generators, filtered samples,...\) for one / a few process\(es\). Sample whitelists provide a way to still avoid this duplication by offering an additional, separate selection layer.

### Usage

In the simplest case a whitelist lists one DSID to be whitelisted per line:

```text
361106
361107
```

It can, however, be used as a slightly more sophisticated filter:

```text
361106 $*_s*
361107 $*_s*
361108 $*_s*
```

Here, the `$` character serves as a placeholder for the DSID in the first column. When matching file names of input files \(nTuples, xAODs\) and DSIDs, in the matching pattern the DSID part, e.g., `\*361106\*` is replaced by `\*361106\*\_s\*`. In the example used here the presence of `\_s` in the file name indicates that a sample is a 'full-sim' sample \(\_s\) as opposed to an 'AFII' sample \(\_a\). Please note, however, that this naming scheme might not apply to all analyses and this example cannot be directly copied!

