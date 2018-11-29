#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 13:32
# @Author : ly
# @File   : opencv4.py
"""
边界框、最小矩形区域和最小闭圆的轮廓
"""
import cv2
import numpy as np

img = cv2.imread("resource/lk.jpg", cv2.IMREAD_UNCHANGED)

# 将图像的长宽减为原始图像一半的大小
# img = cv2.pyrDown(img)

# 二值化图像
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

# 画出轮廓
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    # 将轮廓信息转换成（x，y）坐标，并加上矩形的高度和宽度。
    # 边界框
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # 最小矩形区域
    rect = cv2.minAreaRect(c)
    box =  cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

    #最小闭圆的轮廓
    (x, y), radius = cv2.minEnclosingCircle(c)
    center = (int(x), int(y))
    radius = int(radius)
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", img)
cv2.waitKey()
cv2.destroyAllWindows()
