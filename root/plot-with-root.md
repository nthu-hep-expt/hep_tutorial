# Plotting with ROOT

## Introduction

The following sample is used to test the plotting. 

```text
/eos/user/m/metsai/public/NTHUTutorial/nTuples/BSM4tops.root
```

* [TCanvas class reference](https://root.cern.ch/doc/master/classTCanvas.html)
* 
## TH1

## TH2

To draw a two-dimensional plot, we can write C++/python macro to draw the plot. The following provide an introduction about the 2D plot. 

First we should create a macro \(C++ version\) called `draw2dopt.cxx` . We can run this file by the following command

```text
# remember to initialize the environment like the following 
setupATLAS
lsetup root

# if environment is setup, then run this to plot!
root -l draw2dopt.cxx
```

The plotting code is like the following `draw2dopt.cxx`

```text
void draw2dopt(){
  
  gStyle->SetOptStat(0);
  gROOT->SetBatch(kTRUE);

  // First, include you root file with TFile
  TFile *f = new TFile("samples/official_v3_newBDT/4tops.root");
  
  // Show the tree in your file and can see the tree name
  // Can be commented out anyway.
  f->ls();

  // Get the tree from the file 
  // tree name is nominal_Loose
  auto tree = f->Get<TTree>("nominal_Loose");
  
  // Now this is for the plotting 
  // Create an canvas first. 
  // The class is TCanvas (const char *name, const char *title, Int_t ww, Int_t wh)
  // First two arguments are the name and title
  // 3rd and 4th arguments are horizontal and vertical width

  auto Canvas_BDT_LO_HT = new TCanvas("Canvas_BDT_LO_HT","Canvas_BDT_LO_HT",1550, 1200);
  
  // move to the canvas 
  Canvas_BDT_LO_HT->cd();
  
  // draw the tree
  // first argument: var1:var2 is the variable1 for x-axis and variable1 for y-axis
  // The following two are optional 
  // ">>TH2" is make the plot go into an TH2 object
  // "(12,-1,1,12,-1,1)" is the binning for this plot
  // The second argument is the weight and cuts you would like to apply
  // The last arugment is the plot options you would like to have
  
  tree->Draw("BDT_LO_new:BDT_LO>>TH2_BDT_L0_old_new(12,-1,1,12,-1,1)","138965.16*(36207.7*(runNumber==284500)+44307.4*(runNumber==300000)+(runNumber==310000)*58450.1)*(1/138965.16)*weight_normalise*weight_pileup*weight_jvt*weight_mc*weight_leptonSF*weight_bTagSF_MV2c10_Continuous_CDI20190730*(weight_indiv_SF_EL_ChargeID*(SSee_passECIDS||SSem_passECIDS)+1*(!(SSee_passECIDS||SSem_passECIDS)))*((SSee_passECIDS||SSem_passECIDS||SSmm||eee_Zveto||eem_Zveto||emm_Zveto||mmm_Zveto) && HT_all>500000. && nBTags_MV2c10_77>=2 && nJets>=6 && mcChannelNumber==412043)","scat=5"); //#CONT, COLZ
  
  // Here is to get the TH2 object which we can use to set the options for the TH2 plot
  TH2F * hist1 = (TH2F*)gDirectory->Get("TH2_BDT_L0_old_new");
  
  // Set the title on the x-axis
  hist1->GetXaxis()->SetTitle("BDT");
  
  // Set the title on the y-axis
  hist1->GetYaxis()->SetTitle("BDT_new");
  
  // Set the title for the TH2 plot
  hist1->SetTitle("SM 4tops");
  
  // Set the offset for the title on the x-axis
  hist1->GetYaxis()->SetTitleOffset(1.35);
  
  // Update the canvas
  Canvas_BDT_LO_HT->Update();
  
  // Save this plot as a pdf
  Canvas_BDT_LO_HT->SaveAs("results/BDT_LO_old_new/SMtttt_BDT_LO_old_new.pdf");

}
```

