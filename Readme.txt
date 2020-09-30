任意圖像轉素描：Python+OPENCV 實現[openCV_Image2sketch]

資料來源: https://mp.weixin.qq.com/s?__biz=MzU0NjgzMDIxMQ==&mid=2247491518&idx=1&sn=1a8ec3a066b5b03d65a6a7a25c6f26a7&chksm=fb56fd52cc217444250f046ced89760026f265d4433beaac0e13b39093af21571bc72f84190c&scene=126&sessionid=1601432874&key=391633c74d74d5c55ba8b08bb9e9d76ba4fbf53cdeb3fa09c1c699df50d0785159e98cd688fb10484ee0090ba3885c1b75464a9e7090c08f7302a82a4a46902a0c933773b3bdfb1572ebdd1c62d0cab7802d6c17683d8ee92f0ae7f3c63095d529d74843ffdd55cd547942c20188aeeced14176fc4d22d0cc7614de28fe949c5&ascene=1&uin=MjIwODk2NDgxNw%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_TW&exportkey=Aj42O6c7BYE6scI28gmQ2fA%3D&pass_ticket=ZXd0TLshznF2GmwT4Jgu6LKIpdRAWXmNdMiS14%2BNhFmo1glaxJXdkqvVhtu%2Bdp59&wx_header=0


程式流程:

	灰度图->取反->高斯滤波->再取反(除法里面)->除法运算(divide)

程式碼:

import cv2

img_path = "/小/姐/姐/美/图.jpg"
img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inv = 255 - gray

#ksize和sigma兩個參數可根據實際情況調節，我這裡調參的覺得ksize=15, sigma=50效果還可以。你也可以調節下這兩個參數，看看不同參數對最終素描化效果的影響。
blur = cv2.GaussianBlur(inv, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)

res = cv2.divide(gray, 255 - blur, scale=255)
