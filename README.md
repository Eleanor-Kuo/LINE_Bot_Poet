# LINE Bot
這個專案為以動物圖片作詩的 LINE Bot。藉由辨識(Xception)使用者輸入的動物圖片，以該動物名稱為首自動產生詩句(GPT2)，讓現代人也能體驗古人詠物作詩的風雅。

### 主要撰寫的檔案
- `\generator\picture_recognize.py`：載入自己預先訓練好的 Xception 圖片辨識模型，辨識動物種類並回傳動物名稱。
- `\generator\poem.py`：載入開放社群上預先訓練好的 GPT2 古詩生成模型，以動物名稱作為開頭生成固定長度的古詩。
- `\generator\views.py`：建立 LINE Bot 互動，並呼叫 `\generator\picture_recognize.py` 和 `\generator\poem.py` 的 function，辨識使用者上傳的動物圖片並生成古詩詞後回傳到 LINE Bot 介面。
