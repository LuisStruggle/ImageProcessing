#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/19 10:04
# @Author : ly
# @File   : opencv10.py
"""
前面用的cornerHarris是与尺度有关的角点检测，SIFI（尺度不变特征变换，Scale-Invariant Feature Transform）。

SIFT本身并不检测关键点，关键点由DoG（Difference of Gaussians）检测，但SIFT会通过一个特征向量来描述关键点周围的情况。
DoG是对同一图像使用不同高斯滤波器所得到的结果。
"""
import cv2
import numpy as np

img = cv2.imread("resource/jp.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(gray, None)

img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(51, 163, 236))
cv2.imshow("sift_keypoints", img)

cv2.waitKey()
cv2.destroyAllWindows()
