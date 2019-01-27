# Basic Git Command

## git status：查看目前的檔案狀態 <a id="git-status"></a>

```bash
git status
```

* **Untracked files**：新增於 working space，未被追蹤
* **Changes not staged for commit**：有追蹤，未加入 staging area
* **Changes to be committed**：已加入 staging area，未 commit

**可用參數**

加上 -s 參數，僅顯示已修改的檔案名稱

```bash
git status -s
```

在 -s 後面再加上 -b 參數（-s -b 或 -sb），顯示分支的名稱

```bash
git status -sb
```

## git log <a id="git-log"></a>

## git branch <a id="git-branch"></a>

## git add <a id="git-add"></a>

## git commit <a id="git-commit"></a>

