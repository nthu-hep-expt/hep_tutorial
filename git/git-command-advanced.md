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

