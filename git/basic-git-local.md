# Git Command \(Local\)

## git init：初始化 git repository <a id="git-status"></a>

```bash
git init
```

在你想要當作 git 資料夾的位置執行這個指令，系統便會自動幫你創建一個 `.git` 資料夾，裡面將會記錄之後你在這個資料夾內的檔案變更

## git status：查看目前的檔案狀態 <a id="git-status"></a>

```bash
git status
```

* **Untracked files**：新增於 working space，未被追蹤
* **Changes not staged for commit**：有追蹤，未加入 staging area
* **Changes to be committed**：已加入 staging area，未 commit

#### **其他可用參數**

加上 -s 參數，僅顯示已修改的檔案名稱

```bash
git status -s
```

在 -s 後面再加上 -b 參數（-s -b 或 -sb），顯示分支的名稱

```bash
git status -sb
```

## git add：新增檔案於 Staging Area <a id="git-add"></a>

## git commit：提交紀錄 <a id="git-commit"></a>

## git log：查看過往的 Commit <a id="git-log"></a>

## git branch：分支 <a id="git-branch"></a>

## git checkout

