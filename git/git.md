# Git Intro

## **請先跟我一起想像：**

你的 git 資料夾是一個房子，裡面有很多家具。  
你手上有一台神奇的數位相機，正在對著這個房子的內部拍照。

在數位相機的預覽畫面中，你可以選擇要不要把這個東西拍進去。  
「我要拍這張桌子，但是先不要拍這張椅子」像是這樣。  
選好要拍什麼東西之後，按下快門，就會拍下照片放入相簿。

## **對應到git指令/術語：**

* 家具 = 資料夾內的檔案/資料夾
* 觀看相機預覽 = git status
* 選擇要不要把東西拍進去 = git add / git rm
* 按下快門 = git commit
* 一張照片 = 一個 commit
* 從修改到記錄的三個階段
  * 房子 = Working Space
  * 相機預覽 = Staging Area
  * 相簿 = Repository

## **因此，上面的描述換成git的操作會變成：**

你的 git 資料夾是一個 Working Space（房子），  
裡面有很多 files/directories（家具）。  
你使用 git（手上有一台神奇的數位相機），  
對這個資料夾做版本控制（對著這個房子的內部拍照）。

在 Staging Area（數位相機的預覽畫面）中，  
你可以 git add / git rm（選擇要不要把這個東西拍進去）。  
git add thisFile（「我要拍這張桌子，）  
git rm thatFile（但是先不要拍這張椅子」）像是這樣。  
選好要在commit裡加入什麼東西（拍什麼東西）之後，  
git commit（按下快門），  
就會馬上產生一個commit（拍下照片）記錄進repository（放入相簿）。

