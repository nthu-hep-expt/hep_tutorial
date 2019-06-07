# ROOT

## Introduction

> ### [ROOT](https://root.cern.ch/) is ...
>
> A modular scientific software toolkit. It provides all the functionalities needed to deal with big data processing, statistical analysis, visualisation and storage. It is mainly written in C++ but integrated with other languages such as Python and R.

## ROOT Installation

We have several ways to install ROOT on your laptop \(locally\). I would recommend you to install ROOT by cloning the [repository in the GitHub](https://github.com/root-project/root) and build it with yourself. The other way is to conveniently build with the dmg file. However, it will possibly be limited by the version of Mac OS system.

### Build ROOT with [repository in the GitHub](https://github.com/root-project/root)

This can be used for both Linux and Mac OS systems. We could follow the [instruction](https://github.com/root-project/root#building) below to build ROOT. 

#### Pre-requirement 

If you don't have [cmake](https://cmake.org/download/) in the your laptop, you should install it. Then you should add the following path

```text
PATH="/<your path>/CMake.app/Contents/bin":"$PATH"
```

in your files

* For Linux:

  `~/.bashrc`

* For Mac: `~/.bash_profile`

With this, you can set up for the cmake command. 

#### Building ROOT

First open your terminal and find somewhere you would like to install. Then clone the repo

```bash
git clone https://github.com/root-project/root.gi
```

Make a directory for building

```bash
mkdir build
cd build
```

Run cmake and make

```bash
cmake ../root
make -j8
```

Setup and run ROOT

```bash
source bin/thisroot.sh
root
```

Then you have your own ROOT in your laptop!



