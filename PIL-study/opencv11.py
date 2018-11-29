#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/19 10:32
# @Author : ly
# @File   : opencv11.py
"""
SURF特征检测算法，吸收了SIFT算法的思想，比SIFT快好几倍

SURF采用快速Hessian算法检测关键点，而SURF会提取特征。
"""
import cv2
import numpy as np

img = cv2.imread("resource/jp.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create(4000)
keypoints, descriptor = surf.detectAndCompute(gray, None)

img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(51, 163, 236))
cv2.imshow("surf_keypoints", img)

cv2.waitKey()
cv2.destroyAllWindows()

