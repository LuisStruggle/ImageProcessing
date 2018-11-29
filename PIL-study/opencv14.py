#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/19 14:23
# @Author : ly
# @File   : opencv14.py
"""
在计算机视觉中很多目标检测核识别技术都会用到：梯度直方图（Histogram of Oriented Gradient）、图像金字塔（image pyramid）、滑动窗口（sliding window）

HOG是一个特征描述符，因此HOG与SIFT、SURF和ORB属于同一类型的描述符。在图像和视频处理中常常会进行目标检测。其内部机制都差不多：将图像划分成多个部分，并计算各个部分的梯度。前面曾介绍过类似的方法，比如，用于人脸识别的LBPH描述符。

HOG不是基于颜色值而是基于梯度来计算直方图的。HOG所得到的特征描述符能够为特征匹配和目标检测（或目标识别）提供非常重要的信息。

图像金字塔：为了解决在定位识别过程中，图像尺寸不同的问题。图像的多尺度表示（或图像金字塔）有助于解决不同尺度下的目标检测问题。

滑动窗口：为了解决在定位识别过程中，图像位置不同的问题。滑动窗口是用于计算机视觉的一种技术，它包括图像中要移动部分（滑动窗口）的检查以及使用图像金字塔对各部分进行检测。这是为了在多尺度下检测对象。

解决滑块区域重叠的问题：非最大抑制。它是指给定一组重叠区域，可以用最大评分来抑制所有未分类区域。
非最大（或非极大）抑制是一种与图像同一区域相关的所有结果进行抑制的技术，这些区域没有最大评分。这是因为同样排放（colocate）的窗口往往具有更高的评分，并且重叠区域会变得明显，但是这里只关心结果最好的窗口，并丢弃评分较低的重叠窗口。
"""
# 检测人
import cv2
import numpy as np

# 检测是否有矩形框包含在另一个矩形中
def is_inside(o, i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox +ow < ix + iw and oy + oh < iy + ih

def draw_person(image, person):
    x, y, w, h = person
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

img = cv2.imread("resource/person.jpg")
hog = cv2.HOGDescriptor()
# 如何确定窗口的评分呢？需要一个分类系统来确定某一特征是否存在，并且对这种分类会有一个置信度评分，这里采用支持向量机（SVM）来分类。
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

found, w = hog.detectMultiScale(img)

found_filtered = []
for ri, r in enumerate(found):
    for qi, q in enumerate(found):
        if ri != qi and is_inside(r, q):
            break
        else:
            found_filtered.append(r)

for person in found_filtered:
    draw_person(img, person)

cv2.imshow("people detection", img)
cv2.waitKey()
cv2.destroyAllWindows()