# DSAI-Electric_Bidding

## 資料
在測試的時候，訓練的資料是使用原本 Github repo 裡提供的 sample 資料。

## 處理 & 過程
因為目標是要先預測當天會不會缺電或是有多出來的電，所以先用 SARIMA 分別預測產電量和用電量。

會得到如下的結果：

- 產電量
<img src="generation.png" alt="(圖)產電量" width="400">

- 用電量
<img src="consumption.png" alt="(圖)用電量" width="400">

可以發現，如果原本的線並不是太規則，後來的預測也只能有個大致的趨勢而已。

為了減少進行兩次預測可能產生的誤差，改成用每天的產電量減去用電量後得到的值進行預測。

這麼做的結果如下：

- 用電差
<img src="diff.png" alt="(圖)用電差" width="400">