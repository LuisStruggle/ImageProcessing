#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/19 13:17
# @Author : ly
# @File   : opencv13.py
"""
FLANN（近似最近邻的快速库，Fast Library for Approximate Nearest Neighbors），像ORB一样，
FLANN比SIFT或SURF更宽松的许可协议，可以在项目中自由使用。FLANN具有一种内部机制，该机制可以根据
数据本身选择最合适的算法来处理数据集。经验证，FLANN比其他的最近邻搜索软件快10倍。
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

queryImage = cv2.imread("resource/bathory_album.jpg", 0)
trainingImage = cv2.imread("resource/vinyls.jpg", 0)

# 创建SIFT特征提取器
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(queryImage, None)
kp2, des2 = sift.detectAndCompute(trainingImage, None)

# 设置FLANN匹配参数
FLANN_INDEX_KDTREE = 0
# 可选LinearIndex、KTreeIndex、KMeansIndex、CompositeIndex和AutotuneIndex，另一个参数是待处理核密度的数量，最理想的数量在1-16之间。
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
# searchParams字典只包含一个字段（名为checks），用来指定索引数要被遍历的次数，该值越高，计算匹配花费的时间越长，但也会更准确。
searchParams = dict(checks=50)

flann = cv2.FlannBasedMatcher(indexParams, searchParams)

matches = flann.knnMatch(des1, des2, k=2)

# 为了画好匹配，定一个空的mask
matchesMask = [[0, 0] for i in range(len(matches))]

# 丢弃任何距离大于0.7的值，可以避免几乎90%的错误匹配。
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        matchesMask[i] = [1, 0]

drawParams = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), matchesMask=matchesMask, flags=0)

resultImage = cv2.drawMatchesKnn(queryImage, kp1, trainingImage, kp2, matches, None, **drawParams)

plt.imshow(resultImage)
plt.show()

"""
单应性是一个条件，该条件表明当两幅图像中的一副出现投影畸变时，他们还能彼此匹配。
"""


