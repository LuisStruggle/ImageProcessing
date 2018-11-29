#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 17:13
# @Author : ly
# @File   : opencv7.py
"""
使用GrabCut进行前景检测的例子
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("resource/ts.jpg")

# 创建一个与所加载图像通形状的掩膜，并用0填充。
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (100, 0, 245, 215)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

img = img * mask2[:, :, np.newaxis]

cv2.imshow("分割", img)
cv2.waitKey()
cv2.destroyAllWindows()


