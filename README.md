# DSAI-Electric_Bidding

## 資料
在測試的時候，訓練的資料是使用原本 Github repo 裡提供的 sample 資料。

## 過程
因為目標是要先預測當天會不會缺電或是有多出來的電，所以先用 SARIMA 分別預測產電量和用電量。

會得到如下的結果：

- 產電量
<img src="generation.png" alt="(圖)產電量" width="400">

- 用電量
<img src="consumption.png" alt="(圖)用電量" width="400">

可以發現，如果原本的線並不是太規則，後來的預測也只能有個大致的趨勢而已。

## 處理

為了減少進行兩次預測可能產生的誤差，改成用每天的產電量減去用電量後得到的值進行預測。

這麼做的結果如下：

- 用電差
<img src="diff.png" alt="(圖)用電差" width="400">

可以發現，雖然趨勢是差不多的，但是整個數值還是有可見的誤差。

我想有一個可能是測試到的這天本來的數據就比較奇怪了。不過因為實際上的資料沒辦法控制，所以只能調一個目前跑起來誤差最小的參數而已。

最後用的參數是 1、1、1、24，這個結果是參考第一次作業後修改的參數。如果換參數的話，可以發現 s 的部分影響滿大的：

- s = 2
<img src="diff2.png" alt="(圖)用電差2" width="400">

- s = 6
<img src="diff6.png" alt="(圖)用電差6" width="400">

- s = 12
<img src="diff12.png" alt="(圖)用電差12" width="400">

- s = 48
<img src="diff48.png" alt="(圖)用電差48" width="400">

以方均根差衡量的話，只要 s 不要小的太誇張，其實最後的結果都是差不多的。

## 決策

這次打算保守一點，因為最後要輸出的是投標決定，所以目標是不要多買或多賣，導致不必要的虧損就好。

買賣的邏輯是要用預測出來的電力盈餘決定要不要買。由於採用保守的態度，所以投標金額設得很小。另外因為怕預測不準導致賣太多，所以只考慮買的部分。

實際上去看結果，每天其實只會成交那麼幾筆。但是因為原本就要保守一點，所以也算是符合預期。