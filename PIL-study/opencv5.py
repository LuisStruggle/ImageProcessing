#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 15:11
# @Author : ly
# @File   : opencv5.py
"""
通过介绍直线检测，这可以通过HoughLines和HoughLinesP函数来完成，他们仅有的差别是：
第一个函数使用标准的Hough变换，第二个函数使用概率（通过分析点的子集并估计这些点都属于一条直线的概率）Hough变换。
"""
import cv2
import numpy as np

img = cv2.imread("resource/jp.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)

minLineLength = 20
maxLineGap = 5

# 第二个和第三个参数：一般取值为1和np.pi/180。
# 第三个参数：阈值。低于该阈值的直线会被忽略。Hough变换可以理解为投票箱和投票数之间的关系，每个投票箱代表一个直线，投票数达到阈值的直线会被保留，其它的会被删除。
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength, maxLineGap)
print(lines)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()