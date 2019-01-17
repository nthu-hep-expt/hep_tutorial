# MakeClass

## Make a Class Yourself

```bash
$ root myRootFile.root

root [1] TTree *t = (TTree*) _file0->Get("treeName")
root [2] t->MakeClass("myWonderfulClass")
```

It will create two new files: \(of course you can change the class name\)

* myWonderfulClass.h
* myWonderfulClass.C

Now you can edit those files and try to run them!

```text
$ root
root [0] .L myWonderfulClass.C
root [1]  myWonderfulClass t;
root [2]  t.Loop();
```

