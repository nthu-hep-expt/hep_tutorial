# Machine Learning

## Introduction

Machine learning is a hot topic now. In HEP, we always use TMVA to run the MVA with root nTuple. However, there are more novel ways to do the MVA training with Python packages like XGBoost, Keras and  Tensorflow with Pandas dataframe. 

In the following, we will provide some hands-on example with TMVA and python packages.

## Lesson 1 - TMVA

TMVA stands for The Toolkit for Multivariate Analysis, it lets you perform multivariate classification and multivariate regression analysis. See the [TMVA User Guide](https://root.cern.ch/download/doc/tmva/TMVAUsersGuide.pdf) or [TMVA tutorial](https://github.com/lmoneta/tmva-tutorial) for more information. 



When you're done, you can visualize the results by using

```bash
root -l -e 'TMVA::TMVAGui("test.root")' 
```

## Workshops

* \*\*\*\*[**IML - HEP ML Resource list**](https://github.com/iml-wg/HEP-ML-Resources)\*\*\*\*
* [Fifth Machine Learning in High Energy Physics Summer School 2019](https://indico.cern.ch/event/768915/timetable/?view=standard)





