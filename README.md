<h1>Coin Detection</h1>

<h2>偵測 1000, 500, 100, 50, 1 的硬幣及紙鈔</h2>

<p style="font-size:18px;">以下是 YOLO 模型的指令，用於偵測紙鈔以及硬幣：</p>

```bash
yolo detect predict model="xx.pt" source=0 show=True  # 用鏡頭去偵測紙鈔以及硬幣
