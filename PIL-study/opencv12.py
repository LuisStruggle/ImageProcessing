#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/19 11:03
# @Author : ly
# @File   : opencv12.py
"""
FAST（Features from Accelerated Segment Test）算法会在像素周围绘制一个圆，该圆包括16个像素，这是一种不错的方法。
然后，FAST会将每个像素与加上一个阈值的圆心像素值进行比较，若有连续、比加上一个阈值的圆心的像素值还亮或暗的像素，则可认为圆心是角点。
"""

"""
BRIEF（Binary Robust Independent Elementary Features）并不是特征检测算法，他只是一个描述符。关键点描述符是图像的一种表示，因为可以比较两个图像的关键点描述符，
并找到它们的共同之处，所以描述符可以作为特征匹配的一种方法（gateway）。
"""

"""
暴力匹配（Brute-Force）匹配方法是一种描述符匹配方法，该方法比较两个描述符，并产生匹配结果的列表。称为暴力匹配的原因是该算法基本上不涉及优化，第一个描述符的所有特征都用来和第二个描述符的特征进行比较。每次比较都会给出一个距离值，而最好的比较结果会被认为是一个匹配。
"""

"""
ORB旨在优化和加快操作速度，包括非常重要的一步：以旋转感知（rotation-aware）的方式使用BRIEF，这样即使在训练图像与查询图像之间旋转差别很大的情况下也能够提高匹配效果。
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("resource/manowar_logo.jpg", 0)
img2 = cv2.imread("resource/manowar_single.jpg", 0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)  # 遍历描述符，确定描述符是否已经匹配，然后计算匹配质量（距离）
matches = sorted(matches, key=lambda x: x.distance)  # 排序，这样就可以在一定置信度下显示前n个匹配，以此得到那两幅图像是匹配的。

# 可视化匹配结果
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:40], img2, flags=2)
plt.imshow(img3)
plt.show()





