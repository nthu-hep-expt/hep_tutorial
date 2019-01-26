# NTHU Cluster

The IP of our cluster is **140.114.94.172.** We have 4 computers which located in 綜二.

Once you have account in our cluster, you can access it by the following commands:  
\(If you don't have an account, please check the next section "New User".\)

* Login to the cluster \#1

```bash
ssh yourAccount@140.114.94.172
```

* After login to the cluster \#1, you can then login to cluster \#2~\#4

```bash
ssh yourAccount@nthuhep02
ssh yourAccount@nthuhep03
ssh yourAccount@nthuhep04
```

## New User

If you are a new student in our group and you want to have an account, please follow the steps below to get access to our cluster.

**Step 1.** Contact our postdoc Yun-Ju \(Yun-Ju.Lu@cern.ch\)

* Tell him the account name you want \(space is not allowed\)

**Step 2.** Check if the new account works

* After receive your new ID \(i.e. you account name\) and PW \(password\), try to login

```bash
ssh yourAccount@140.114.94.172
```

* If any problems occur, contact Yun-Ju again

**Step 3.** Change your password

Change your password with command "passwd"

```bash
passwd
```





