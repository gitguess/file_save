# -*- coding: UTF-8 -*-
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np


img = cv2.imdecode(np.fromfile('2.jpg', dtype=np.uint8), 1)
img_ori = img.copy()

#图片先转成灰度的
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#转换二值图
ret,binary=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
#反色
binary=cv2.bitwise_not(binary)
#轮廓识别
contours, hierarchy=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

contours_seed = []
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    print(area)
    #设定阈值
    if area < 25 or area > 70:
        cv2.drawContours(binary,[contours[i]],0,0,-1)
        continue
    contours_seed.append(contours[i])
cv2.drawContours(img_ori, contours_seed, -1, (0, 0, 255), 1)

cv2.imshow("binary",binary)

print(len(contours_seed))
cv2.imshow("img_ori",img_ori)
cv2.waitKey(0)
