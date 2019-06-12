# Grid

## Introduction

We always work with the grid services to run the samples on the grid. The tutorial for grid system is shown [here](https://indico.cern.ch/event/757797/timetable/?view=standard#b-309103-the-grid-and-getting).

## Grid certificate

The instruction to apply for Grid certificate and ATLAS VO is described [here](https://twiki.cern.ch/twiki/bin/viewauth/AtlasComputing/SoftwareTutorialSoftwareBasics#Grid_Certificates). After you follow the instruction to install the certificate to Lxplus, you can start to use `rucio` to download the files to your CERNBox directory. Moreover, we should include the certificate in your browser to visit some websites like [ATLAS BigPanda](https://bigpanda.cern.ch/) and [AMI](https://ami.in2p3.fr/).

### Hands-on

* Log in to [https://ca.cern.ch/ca/](https://ca.cern.ch/ca/) and follow the instruction to generate the `.p12` certificate file.

![](../.gitbook/assets/ying-mu-kuai-zhao-20190612-xia-wu-2.17.36.png)

* When you generate and download the certificate file in your local laptop. Then, you need to send them to the Lxplus.

```bash
scp myCertificate.p12 youraccount@lxplus.cern.ch:.
```

* You need to convert your certificate into the correct form using

```bash
openssl pkcs12 -in mycert.pfx -clcerts -nokeys -out usercert.pem
openssl pkcs12 -in mycert.pfx -nocerts -out userkey.pem
chmod 400 userkey.pem
chmod 444 usercert.pem
```

* Move the `userkey.pem` and `usercert.pem` to the `~/.globus`.

```text
mv userkey.pem ~/.globus
mv usercert.pem ~/.globus
```

You can check that everything is working by doing

```
setupATLAS
diagnostics
gridCert
```

If you get the following in the end of the results, then you are totally fine with the grid system. You can then enjoy working with them!

```bash
  Step Test Description                                   Result
     1 Permissions certificate/key                         OK
     2 Setting up grid software                            OK
     3 Certificate validity                                OK
     4 Key / Certificate match                             OK
     5 Check grid proxy                                    OK
     6 Authenticate voms server                            OK
     7 Role check                                          OK
     8 Nickname check                                      OK
     9 Pandaserver connect check                           OK
    10 AMI access check                                    OK
    11 Rucio Information                                   OK
```

## Grid submission

#### [ATLAS BigPanda](https://bigpanda.cern.ch/)

## Rucio

Here are some tutorials and twikis about `rucio`. Please find the instructions below.

* [twiki for rucio](https://twiki.cern.ch/twiki/bin/view/AtlasComputing/SoftwareTutorialGettingDatasets)
* [slides for rucio](https://indico.cern.ch/event/757797/contributions/3141910/attachments/1735918/2807718/Overview_of_Rucio_-_ATLAS_Software_Tutorial_10_2018.pdf)

#### Initialization 

```bash
setupATLAS
lsetu rucio
voms-proxy-init -voms atlas
```

#### Useful Commands

