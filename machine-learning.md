# Machine Learning

## Workshops

* \*\*\*\*[**IML - HEP ML Resource list**](https://github.com/iml-wg/HEP-ML-Resources)\*\*\*\*
* [Fifth Machine Learning in High Energy Physics Summer School 2019](https://indico.cern.ch/event/768915/timetable/?view=standard)

## ML with ROOT packages

### TMVA

TMVA stands for The Toolkit for Multivariate Analysis, it lets you perform multivariate classification and multivariate regression analysis. See the [TMVA User Guide](https://root.cern.ch/download/doc/tmva/TMVAUsersGuide.pdf) or [TMVA tutorial](https://github.com/lmoneta/tmva-tutorial) for more information. 

### Example - BDT analysis on TMVA

First we instantiate a "Factory" object, and set the analysis type to "Classification". More factory configuration options can be found in the user guide.

```
TMVA::Tools::Instance();
TFile* test = TFile::Open("BDT.root", "RECREATE");
TMVA::Factory factory("TMVAClassification", test, "AnalysisType=Classification");
```

Then we declare a data loader, and add variable names and their data types into the loader.

```bash
TMVA::DataLoader * loader = new TMVA::DataLoader("dataset");
loader->AddVariable("mjj", 'F');
loader->AddVariable("dyjj", 'F');
loader->AddVariable("MvaSumOFMvaMLepxJety", 'F');
loader->AddVariable("contOLV", 'F');
loader->AddVariable("pttot", 'F');
loader->AddVariable("mt", 'F');
loader->AddVariable("mll", 'F');
loader->AddVariable("dphi", 'F');
```

Set up signals and backgrounds

```bash
TFile* vbf = TFile::Open( "vbf.root" );
TFile* WW = TFile::Open( "WW.root" );
TFile* Wt = TFile::Open( "Wt.root" );
TFile* Ztt = TFile::Open( "Ztt.root" );
TFile* ggf = TFile::Open( "ggf.root" );
TFile* ttbar = TFile::Open( "ttbar.root" );

TTree *vbfTree = (TTree*)vbf->Get("MVATree");
TTree *WWTree = (TTree*)WW->Get("MVATree");
TTree *WtTree = (TTree*)Wt->Get("MVATree");
TTree *ZttTree = (TTree*)Ztt->Get("MVATree");
TTree *ggfTree = (TTree*)ggf->Get("MVATree");
TTree *ttbarTree = (TTree*)ttbar->Get("MVATree");

loader->AddSignalTree(vbfTree);
loader->AddBackgroundTree(WWTree);
loader->AddBackgroundTree(WtTree);
loader->AddBackgroundTree(ZttTree);
loader->AddBackgroundTree(ggfTree);
loader->AddBackgroundTree(ttbarTree);
```

Set up event weights

```bash
loader->SetSignalWeightExpression("weight");
loader->SetBackgroundWeightExpression("weight");
```

And then train and evaluate the results. There are several options when booking method. 

* "NegWeightTreatment" is how you would like to deal with events with negative weight. 
* "NTrees" is the total number of trees constructed when boosting. 
* "MinNodeSize" is the minimum percentage of training events required in a leaf node. 
* "MaxDepth" is the maximum depth for each tree.
* "BoostType" is the algorithm type for boosting.
* "Shrinkage" is the learning rate for [shrinkage ](https://en.wikipedia.org/wiki/Gradient_boosting#Shrinkage)in gradiant boosting.

Other options can be found in the user guide.

```bash
loader->PrepareTrainingAndTestTree("", "");
factory.BookMethod(loader,TMVA::Types::kBDT, "BDT",
"NegWeightTreatment=Pray:NTrees=200:MinNodeSize=5%:MaxDepth=5:BoostType=Grad:Shrinkage=0.1" );

factory.TrainAllMethods();
factory.TestAllMethods();
factory.EvaluateAllMethods();
```

When you're done, you can visualize the results by using

```bash
root -l -e 'TMVA::TMVAGui("test.root")' 
```

## ML with Python packages

Here I used Mac OS to setup the environment for the machine learning \(ML\) packages with Python. 

### Install Python3

Mostly ML packages work with Python3. We have several ways to install Python3. We could use Anaconda to install, but here I will directly install the official Python3 in the website of Python. You can also follow the instruction [here](https://realpython.com/installing-python), which provide the installation of Python with command line. 

In this tutorial, I use Python 3.6.8.

### Install Tensorflow

```text
pip3 install tensorflow
```

### Install Keras

For python3

```text
pip3 install keras
```

### Pandas

```text
pip3 install pandas
```

### Theano

```text
pip3 install theano
```

### Sklearn

```text
pip3 install sklearn
```

### Xgboost

```text
pip3 install xgboost
```

If you encounter problem, you can build xgboost with the repository 

```text
brew install gcc@7
```

```text
git clone --recursive https://github.com/dmlc/xgboost
```

```text
mkdir build
cd build
CC=gcc-7 CXX=g++-7 cmake ../xgboost
make -j4
```

```text
# in xgboost folder
cd python-package; sudo python3 setup.py install
```

{% code title="~/.bashrc" %}
```bash
export PYTHONPATH=path-to-xgboost/xgboost/python-package
```
{% endcode %}

## Troubleshooting

#### 

