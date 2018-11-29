#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/16 15:26
# @Author : ly
# @File   : opencv6.py
"""
opencv的HoughCircles函数可用来检测圆，它与使用HoughLines函数类似。像用来决定删除或保留直线的两个参数minLineLength和maxLineGap一样，HoughCircles有一个
圆心间的最小距离和圆的最小及最大半径。
"""
import cv2
import numpy as np

planets = cv2.imread("resource/circle.jpg")
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
# 模糊操作
img = cv2.medianBlur(gray_img, 5)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 120, param1=100, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 2)

cv2.imshow("planets", planets)
cv2.waitKey()
cv2.destroyAllWindows()
