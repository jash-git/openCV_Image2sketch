import cv2

img_path = "/小/姐/姐/美/图.jpg"
img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inv = 255 - gray

#ksize和sigma兩個參數可根據實際情況調節，我這裡調參的覺得ksize=15, sigma=50效果還可以。你也可以調節下這兩個參數，看看不同參數對最終素描化效果的影響。
blur = cv2.GaussianBlur(inv, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)

res = cv2.divide(gray, 255 - blur, scale=255)