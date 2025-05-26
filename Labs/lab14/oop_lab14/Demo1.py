import cv2
import numpy as np
from matplotlib import pyplot as plt

# 第一步：讀取圖片
img = cv2.imread("sad_man.jpg")  # 背景圖，內含哭臉 emoji
emoji = cv2.imread("smiley_emoji.png")  # 笑臉圖像

# 第二步：將圖片轉換為 HSV 色彩空間，方便抓黃色區域（哭臉）
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 第三步：設定黃色的 HSV 範圍
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([35, 255, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# 第四步：尋找黃色區域的輪廓（哭臉可能的邊界）
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 第五步：將每個找到的黃色區域替換成笑臉 emoji
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)  # 找出該區域的座標與寬高
    resized_emoji = cv2.resize(emoji, (w, h))  # 把笑臉縮放到剛好貼上
    img[y : y + h, x : x + w] = resized_emoji  # 直接蓋上去

# 第六步：顯示結果（用 matplotlib，支援 Jupyter）
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # OpenCV 是 BGR，要轉成 RGB 才正確顯示
plt.title("哭臉變笑臉結果")
plt.axis("off")
plt.show()
