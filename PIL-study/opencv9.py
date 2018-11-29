#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 21:41
# @Author : ly
# @File   : opencv9.py
"""
使用opencv来检测图像特征，并利用这些特征进行图像匹配和搜索。
有许多特征检测核提取算法：
Harris：该算法用于检测角点
SIFT：该算法用于检测斑点（blob）
SURF：该算法用于检测斑点
FAST：该算法用于检测角点
BRIEF：该算法用于检测斑点
ORB：该算法代表带方向的FAST算法与具有旋转不变性的BRIEF算法

通过以下方式进行特征匹配：
暴力（Brute-Force）匹配法
基于FLANN的匹配法

通过单应性（homography）来检测这些图像是否存在于另一个图像中
"""

"""
什么是特征：粗略地讲，特征就是有意义的图像区域，该区域具有独特性或易于识别性。
因此，角点及高密度区域是很好的特征，而大量重复的模式或低密度区域（例如图像中的蓝色天空）则不是好的特征。
边缘可以将图像分为两个区域，因此也可以看作好的特征。斑点（与周围有很大差别的图像区域）也是有意义的特征。

大多数特征检测算法都会涉及图像的角点、边和斑点的识别，也有一些涉及脊向（ridge）的概念，可以认为脊向是细长物体的对称轴（例如：识别图像中的一条路）
"""

"""
使用cornerHarris识别角点
"""
import cv2
import numpy as np

img = cv2.imread("resource/qp.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# cornerHarris函数会使用Sobel算子，并且第三个参数定义了Sobel算子的中孔。简单地说，该参数定义了角点检测的敏感度，其取值必须是介于3和31之间的奇数。
# 第二个参数标记角点的大小
dst = cv2.cornerHarris(gray, 2, 23, 0.04)

# 筛选大于0.01*dst.max()的角点
img[dst>0.01 * dst.max()] = [0, 0, 255]

cv2.imshow("corners", img)
cv2.waitKey()
cv2.destroyAllWindows()

