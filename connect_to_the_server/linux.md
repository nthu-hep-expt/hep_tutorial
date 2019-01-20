# Basic Linux

## 打開終端機（terminal）

### Mac

用spotlight搜尋"terminal"就能找到終端機的app，直接點擊開即可

如果希望顯示遠端的影像，則須額外安裝X window，而Mac常用的X window是：

* [XQuartz](https://www.xquartz.org/)

### Windows

使用Windows系統則需另外安裝以下SSH client端，此程式主要是利用SSH來連結server，當中有兩個較好用的軟體：

* [MobaXterm](https://mobaxterm.mobatek.net/)
* [PuTTY](https://www.putty.org/)

MobaXterm的好處是內建FTP上傳下載的功能，因此並不需額外使用FTP的程式，也不需要自己用scp指令來下載檔案，並且MobaXterm的功能十分健全跟強大！

另外，Windows系統中常用的X window軟體則為：

* [Xming](http://www.straightrunning.com/XmingNotes/)

## pwd - 查看當前路徑

pwd = Print Working Directory

```bash
pwd
```

## ls - 列出檔案資訊

ls = list

```bash
ls
```

加上 option -a = list all 會列出 **每個檔案/資料夾**

```bash
ls -a
```

加上 option -l 會列出 **詳細資訊**

```bash
ls -l
```

可以合起來用，例如：  
同時加上 option -a 和 -l 會列出 **每個檔案/資料夾** 的 **詳細資訊**

```bash
ls -al
```

## cd - 切換資料夾/前往路徑

cd = Change Directory

cd 後面可以加 絕對路徑 也可以加 相對路徑

```bash
cd <欲前往的路徑>
```

#### 絕對路徑

就是你 pwd 完看到的那種，標示從根目錄至該處的路徑

#### 相對路徑

* 使用者的家目錄：~（蟲蟲）
* 表示當前路徑：. （一個點）
* 表示當前路徑的上一層路徑：.. （兩個點）

### Example

![](../.gitbook/assets/screen-shot-20190116-xia-wu-4.46.00.png)

## vim 或 emacs - 編輯器

這世界上的編輯器流派只有三個，一派是Emacs，一派是Vim，剩下的都是其他

Vim：編輯器之神  
Emacs：神之編輯器

雖然Jennifer都用emacs，但是因為我用vim所以我要來介紹vim，耶

簡單來說只要知道以下指令就可以使用了：

* vim &lt;fileName&gt; 可以進入vim編輯器修改檔案
* 按 i 可以進入編輯模式
* 按 esc 可以離開編輯模式
* 按 :w 可以儲存
* 按 :q 可以離開vim編輯器



欲知更多可以看下面這張圖（希望大家不要看了圖之後就拒絕使用vim）

![&#x4F86;&#x6E90;&#xFF1A;http://blog.faq-book.com/?p=3029](../.gitbook/assets/vim.jpg)

或是看點動畫檔可能會更好懂

{% embed url="https://vimgifs.com/" %}

最後分享一個很棒的 vim 教學結束這回合！（Better, Stronger, Faster！）

{% embed url="https://coolshell.cn/articles/5426.html" %}









