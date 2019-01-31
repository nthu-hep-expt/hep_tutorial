# Git Command \(Advanced\)

## git stash

當你還不想將變更做 commit，但又需要執行諸如切換 branch 這種，需要 working space 淨空的指令時，可以利用 stash 進行暫存。

* 對當前狀態執行暫存

```bash
git stash
```

* 查看暫存

```bash
git stash list
```

* 恢復暫存（大括號內的數字是暫存的編號，從零開始）

```bash
git stash apply stash@{0}
```

## git reset

{% hint style="danger" %}
此區請千萬！務必！小心慎用，以防悲劇發生OAQ
{% endhint %}

* 放棄 add，但保留修改 （即：對 staging area 裡的所有 file 做 `git reset HEAD file`）

```bash
git reset
```

* 放棄所有修改，回到上個 commit 完成後的狀態

```bash
git reset --hard
```

* 回到最新一個 commit 版本

```bash
git reset --hard HEAD
```

* 回到前一個 commit 版本（一個 ^ 表示往前一次，以此類推）

```bash
git reset --hard HEAD^
```

* 回復到 commit 提交前的狀態

```bash
git reset --soft HEAD^
```



