#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 11:27
# @Author : ly
# @File   : opencv3.py
"""
Canny边缘检测算法非常复杂，但也很有趣：它有5个步骤，即使使用高斯滤波器对图像进行去噪、计算梯度、在边缘上使用非最大抑制（NMS）、在检测到的边缘上使用双（double）阀值去除假阳性（false positive），
最后还会分析所有的边缘及其之间的连接，以保留真正的边缘并消除不明显的边缘。
"""
import cv2
import numpy as np

# img = cv2.imread("resource/jp.jpg", 0)
# cv2.imwrite("resource/canny.jpg", cv2.Canny(img, 200, 300))

"""
轮廓检测：
在计算机视觉中，轮廓检测是另一个比较重要的任务，不单是用来检测图像或者视频帧中物体的轮廓，而且还有其他操作与轮廓检测有关。这些操作有：计算多边形边界、形状逼近和计算感兴趣区域。
"""
img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)  # 二值化操作

# 获取图像，图像轮廓，图像层次。参数：第一个图像，第二个图像层次类型，第三个参数轮廓逼近方法
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
# 将原图像转为BGR
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# 在原图像上画出图像的轮廓
img = cv2.drawContours(color, contours, -1, (0,255,0),2)

cv2.imshow("test", img)
cv2.waitKey()
cv2.destroyAllWindows()
