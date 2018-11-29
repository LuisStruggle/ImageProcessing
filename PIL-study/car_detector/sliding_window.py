#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/20 11:16
# @Author : ly
# @File   : sliding_window.py
"""
这也是一个生成器。给定一幅图像，返回一个从左向右滑动的窗口（滑动的步长可以指定），直到覆盖整个图像的宽度，然后回到左边界，继续下一步骤。
"""
def siliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

