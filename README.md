# DSAI-Electric_Bidding

## 處理 & 過程
因為目標是要先預測當天會不會缺電或是有多出來的電，所以先用 SARIMA 分別預測產電量和用電量。

會得到如下的效果：

產電量
<img src="generation.png" alt="(圖)產電量" width="400">

用電量
<img src="consumption.png" alt="(圖)用電量" width="400">

將每天的產電量減去用電量，得到