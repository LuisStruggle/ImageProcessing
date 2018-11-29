#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/20 10:24
# @Author : ly
# @File   : pyramid.py
"""
图像金字塔
"""
import cv2

def resize(img, scaleFactor):
    return cv2.resize(img, (int(img.shape[1] * (1 / scaleFactor)), int(img.shape[0] * (1 / scaleFactor))), interpolation=cv2.INTER_AREA)

def pyramid(image, scale=1.5, minSize=(200, 80)):
    yield image

    while True:
        image = resize(image, scale)
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        yield image

"""
通过指定的因子来调整图像的大小

建立图像金字塔。返回被调整过大小的图像直到宽度和高度都达到所规定的最小约束。
"""
