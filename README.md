# communication-simulation
<img src="http://www.cuelogic.com/blog/wp-content/uploads/2015/10/Python-35.jpg" width="100px" height="100px" />

這是將我目前在LAB所學到的知識，進行模擬的結果  
目前主要專攻於**ofdm**，~~mimo的模擬先暫時告一段落XDD~~

## 使用前說明

該repository的所有模擬在python3.5.2(64bits)環境下可順利執行  
請先至[官網](https://www.python.org/downloads/windows/)下載python3.0以上的版本，建議用3.5.2  
安裝時請記得勾選Add Python 3.5 to PATH，之後才能直接在命令提示字元中執行python  
若沒有勾選的話，需要在安裝完後將python直譯器執行檔路徑加入環境變數PATH中，才能在命令提示字元中執行python

<img src="https://raw.githubusercontent.com/XassassinXsaberX/test/master/img/python%E6%95%99%E5%AD%B8001.png" />

預設python3.5安裝路徑為C:\Users\user\AppData\Local\Programs\Python  
使用者變數可設為
```
C:\Users\user\AppData\Local\Programs\Python\Python35\Scripts\;C:\Users\user\AppData\Local\Programs\Python\Python35
```
如此一來除了可以在命令提示字元中執行python直譯器，亦可執行Scripts資料夾中的pip、easy_install等腳本檔
</br>
</br>

接下來可以執行[get-pip.py](https://raw.githubusercontent.com/XassassinXsaberX/test/master/get-pip.py)來下載並安裝pip腳本檔  
再來可以用pip來安裝該模擬所需的套件  
可在命令提示字元中輸入來下載並安裝繪圖套件matplotlib
```
pip install matplotlib
```
而科學計算套件scipy的安裝會比較麻煩  
請先到[此網站](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)下載numpy套件  
到[這裡](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy)下載scipy套件  
假設numpy的.whl檔下載至C:\Users\user\Downloads中  
請執行命令提示字元，並進行如下步驟
```
先用cd指令切換目錄
cd \d C:\Users\user\Downloads

再用pip來安裝.whl檔
pip install 你下載的numpy.whl檔

安裝完numpy套件後才能scipy套件，注意順序不可顛倒
pip install 你下載的scipy.whl檔
```
最後我非常推薦使用[PyCharm](https://www.jetbrains.com/pycharm/)這套python IDE來編寫python程式
</br>
</br>
</br>
</br>

## MIMO
主要分為`capacity`模擬、space-time block code(`STBC`)模擬、`detection`模擬  
using channel state information(`CSI`)模擬、`MU-MIMO`模擬
</br>

## OFDM 
基本架構中，我花了些時間去模擬對ofdm symbol取樣的結果是否真的有IFFT關係
還有模擬ofdm的power spectrum density，及載波間的正交性關係，最後也做了是否考慮rayleigh fading的BER模擬
目前以完成探討symbol timing offset對星座的的影響問題




```
該模擬大量參考該書
```
[![mimo-ofdm](http://t2.gstatic.com/images?q=tbn:ANd9GcRn4Q5yArUd2YeJdfQBdnV0RBHN-D0B2wzTWPD0PeJ_s0Yk3NEN "book")](https://www.google.com.tw/search?q=mimo-ofdm+wireless+communications+with+matlab&oq=mimo+ofdm&aqs=chrome.4.69i57j69i60l2j69i61j35i39l2.5235j0j7&sourceid=chrome&ie=UTF-8)

亦可參考以下書籍  `fundamental of wireless communication`  
[![wireless]](https://www.google.com.tw/search?q=fundamental+of+wireless+communication&source=lnms&sa=X&ved=0ahUKEwjqvK3H5_PTAhVJGJQKHZvkAy8Q_AUICSgA&biw=1920&bih=901&dpr=1)

[請按我](https://www.google.com.tw/search?q=fundamental+of+wireless+communication&source=lnms&sa=X&ved=0ahUKEwjqvK3H5_PTAhVJGJQKHZvkAy8Q_AUICSgA&biw=1920&bih=901&dpr=1)


![baidu-w150](http://www.baidu.com/img/bdlogo.gif "百度logo")
<img src="https://avatars2.githubusercontent.com/u/3265208?v=3&s=100" />
<img src="https://avatars2.githubusercontent.com/u/3265208?v=3&s=100" width="100px" height="200px" />

---------------------------------------
### 測試一下
```
我現在
要打字喔
```
--------------------------------

[wireless]:http://i100.photobucket.com/albums/m32/ganelon9/5356224f.jpg 
